"""Text extraction and stylometric metrics for the writing-style notebook.

The PDF is converted with `pdftotext` (poppler). Equations and figure axes come
out as fragments, so each line is classified as prose or non-prose; prose lines
feed the language metrics and non-prose lines feed the math/figure density.
"""
import re
import subprocess
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import textstat

# Section headers in document order: (id, short label, regex locating the header
# in the pdftotext output, role in the paper).
SECTIONS = [
    ("Abs", "Abstract", r"\nAbstract\n", "front"),
    ("1", "1 Introduction", r"\n1\n\nIntroduction\n", "front"),
    ("2", "2 Setting", r"\n2\n\nSetting\n", "method"),
    ("3", "3 Method & Analysis (intro)", r"\n3\n\nMethod & Analysis\n", "method"),
    ("3.1", "3.1 Union of top-k", r"\n3\.1\n\nUnion of top-k\n", "method"),
    ("3.2", "3.2 Unbiased estimate", r"\n3\.2\n\nConstructing an unbiased estimate\n", "method"),
    ("3.3", "3.3 High-probability bound", r"\n3\.3\n\nHigh probability bound\n", "theory"),
    ("3.4", "3.4 Control variates", r"\n3\.4\n\nControl variates term\n", "theory"),
    ("4", "4 Experiments (intro)", r"\n4\n\nExperiments\n", "experiments"),
    ("4.1", "4.1 Tasks", r"\n4\.1\n\nTasks\n", "experiments"),
    ("4.2", "4.2 Models", r"\n4\.2\n\nModels\n", "experiments"),
    ("4.3", "4.3 Datasets", r"\n4\.3\n\nDatasets\n", "experiments"),
    ("4.4", "4.4 Baselines", r"\n4\.4\n\nBaselines\n", "experiments"),
    ("4.5", "4.5 Experimental setup", r"\n4\.5\n\n.*?\n\nExperimental setup\n", "experiments"),
    ("4.6", "4.6 Results", r"\n4\.6\n\nExperimental results\n", "experiments"),
    ("5", "5 Related Work", r"\n5\n\nRelated Work\n", "context"),
    ("6", "6 Discussion", r"\n6\n\nDiscussion\n", "context"),
    ("Ref", "References", r"\nReferences\n", "skip"),
    ("A", "A Proofs (A.1)", r"\nA\n\nProofs of a select number of lemmas\n", "appendix"),
    ("A.2", "A.2 Tighter variance bound", r"\nA\.2\n\nA tighter bound", "appendix"),
    ("A.3", "A.3 Bernstein restatement", r"\nA\.3\n", "appendix"),
    ("B", "B Correction-term choice", r"\nB\n\n(?:p\n\n)?.*?Choice of hyperparameter", "appendix"),
    ("C", "C Full results", r"\nC\n\nFull Experimental Results\n", "appendix"),
]

# Page furniture and footnotes that are not part of the running text.
NOISE_LINES = {"Equal contribution", "Preprint.", "Work done while at Coactive AI"}
NOISE_PREFIXES = ("Corresponding author", "arXiv:")

MATH_CHARS = set("∈∉⊂⊆∪∩∀∃≤≥≠≈∝∼∑∏√∞∥⌈⌉⌊⌋←→⇒·×±−αβγδϵεθλμσπτωΣΔℓ∗′")

ABBREVIATIONS = {
    "et al.": "et al", "e.g.": "eg", "i.e.": "ie", "Fig.": "Fig", "vs.": "vs",
    "approx.": "approx", "Eq.": "Eq",
}

CITATION_RE = re.compile(
    r"\((?:[A-Z][A-Za-zÀ-ÿ\-]+(?: and [A-Z][A-Za-zÀ-ÿ\-]+| et al\.?)?,? \d{4}[a-z]?;?\s*)+\)"
    r"|[A-Z][A-Za-zÀ-ÿ\-]+(?: et al\.?| and [A-Z][A-Za-zÀ-ÿ\-]+)? \(\d{4}[a-z]?\)"
)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z\-']*[A-Za-z]|[A-Za-z]")


def extract_text(pdf_path):
    return subprocess.run(["pdftotext", str(pdf_path), "-"], capture_output=True,
                          text=True, check=True).stdout.replace("\x0c", "\n")


def split_sections(raw):
    """Return {section_id: raw text} using the header regexes in SECTIONS."""
    starts, pos = [], 0
    for sid, _, pattern, _ in SECTIONS:
        m = re.compile(pattern, re.S).search(raw, pos)
        if m is None:
            raise ValueError(f"header for section {sid} not found")
        starts.append((sid, m.start(), m.end()))
        pos = m.end()
    out = {}
    for i, (sid, _, body_start) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else len(raw)
        out[sid] = raw[body_start:end]
    return out


def is_prose_line(line):
    s = line.strip()
    if not s or s in NOISE_LINES or s.startswith(NOISE_PREFIXES):
        return False
    tokens = s.split()
    if len(tokens) < 4:
        return False
    wordlike = sum(bool(re.fullmatch(r"[\"“(]?[A-Za-z][A-Za-z\-']+[.,;:)”\"]?", t)) for t in tokens)
    return wordlike / len(tokens) >= 0.55


def raw_math_density(pdf_path):
    """Math symbols and non-prose lines per section, straight from the PDF text.

    Used as an independent cross-check of the hand-marked math in the clean text.
    """
    secs = split_sections(extract_text(pdf_path))
    rows = []
    for sid, text in secs.items():
        rows.append(dict(sid=sid,
                         raw_math_symbols=sum(ch in MATH_CHARS for ch in text),
                         raw_nonprose_lines=sum(1 for l in text.split("\n")
                                                if l.strip() and not is_prose_line(l))))
    return pd.DataFrame(rows)


def split_sentences(paragraph):
    t = paragraph
    for k, v in ABBREVIATIONS.items():
        t = t.replace(k, v)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z“\"(⟨])", t)
    return [p.strip() for p in parts if len(WORD_RE.findall(p.replace("⟨m⟩", ""))) >= 3]


def strip_citations(s):
    return re.sub(r"\s+", " ", CITATION_RE.sub("", s)).strip()


def words(s):
    return WORD_RE.findall(s.replace("⟨m⟩", " "))


def load_clean(path):
    """Parse paper_clean.txt into section and sentence tables."""
    sections, sentences, captions = [], [], []
    cur = None
    para_idx = 0
    for line in Path(path).read_text().split("\n"):
        if line.startswith("# ") or not line.strip():
            continue
        if line.startswith("## "):
            sid, label, role = [x.strip() for x in line[3:].split("|")]
            cur = dict(sid=sid, label=label, role=role, order=len(sections),
                       equations=0, paragraphs=0, bullets=0, text="")
            sections.append(cur)
            continue
        if line.strip() == "[EQ]":
            cur["equations"] += 1
            continue
        if line.startswith("CAPTION:"):
            captions.append(dict(sid=cur["sid"], text=line[len("CAPTION:"):].strip()))
            continue
        kind = "bullet" if line.startswith("- ") else "body"
        body = line[2:] if kind == "bullet" else line
        # Run-in paragraph headings are marked "§Heading.§" in the clean text.
        m = re.match(r"§(.+?)§ ", body)
        if m:
            cur.setdefault("runin", []).append(m.group(1).rstrip("."))
            body = body[m.end():]
        cur["paragraphs"] += 1
        cur["bullets"] += kind == "bullet"
        cur["text"] += body + "\n"
        para_idx += 1
        for s in split_sentences(body):
            sentences.append(dict(sid=cur["sid"], label=cur["label"], role=cur["role"],
                                  order=cur["order"], para=para_idx, kind=kind, text=s,
                                  text_nocite=strip_citations(s)))
    sec = pd.DataFrame(sections)
    sen = pd.DataFrame(sentences)
    sen["pos"] = np.arange(len(sen))
    sen["idx"] = sen.groupby("sid").cumcount()
    return sec, sen, pd.DataFrame(captions)


# ---------------------------------------------------------------- word lists --

HEDGES = ["perhaps", "likely", "approximately", "roughly", "typically", "may",
          "might", "could", "slightly", "somewhat", "relatively", "intuitively",
          "around", "suggest", "appears", "generally", "to a lesser extent",
          "we do not get", "imperfect", "assume", "assumes"]
BOOSTERS = ["prove", "proves", "provably", "provably-accurate", "novel", "significant",
            "significantly", "always", "perfect", "exactly", "key", "guarantee",
            "guarantees", "unbiased", "effectiveness", "demonstrate", "show",
            "clearly", "only requires", "much", "best", "high probability",
            "surprisingly", "easy", "simple", "simply", "straightforward"]
CONNECTIVES = {
    "causal": ["because", "since", "thus", "therefore", "so", "hence", "due to",
               "as a result", "this motivates", "this will later allow", "implies"],
    "contrast": ["however", "while", "unfortunately", "although", "but", "unlike",
                 "in comparison", "rather than", "except", "despite", "differs"],
    "additive": ["furthermore", "additionally", "moreover", "also", "as well",
                 "in addition", "correspondingly"],
    "sequence": ["first", "then", "next", "finally", "for the remainder",
                 "we begin", "we next", "later"],
    "example": ["for example", "eg", "such as", "as an example", "for instance",
                "a concrete example", "ie"],
    "signpost": ["see ", "section ", "appendix", "figure ", "algorithm ", "equation ",
                 "lemma ", "theorem "],
}

# Vocabulary an AI/ML practitioner meets daily. Costly for lay readers only.
ML_JARGON = ["embedding", "embeddings", "semantic", "vector", "vectors", "softmax",
             "kde", "kernel", "hnsw", "lsh", "top-k", "query", "queries", "dataset",
             "baseline", "baselines", "clip", "resnet-", "distilbert", "bert", "vit",
             "encoder", "pre-trained", "token", "tokens", "temperature", "bandwidth",
             "recall", "hyperparameters", "hyperparameter", "inference", "runtime",
             "log-linear", "contrastive", "partition", "logits", "knowledge distillation",
             "classification", "retrieval", "index", "indexed", "indexing", "oracle",
             "data-structure", "nearest", "neighbor", "hashing", "hash", "hashes",
             "transformer", "multimodal", "skip-lists", "density", "normalizing",
             "qdrant", "aws", "gaussian", "euclidean", "dot product", "argmax"]
# Probability/theory vocabulary. Costly for lay readers AND for many ML
# practitioners who are not theorists (weighted lower for experts).
THEORY_JARGON = ["martingale", "filtration", "bernstein", "chernoff", "binomial",
                 "unbiased", "variance", "conditional", "lemma", "theorem", "proposition",
                 "proof", "bound", "bounds", "union bound", "indicator", "geometric",
                 "random variable", "expectation", "probability", "control variates",
                 "kl-divergence", "tail", "monotonically", "non-parametric",
                 "relative error", "high probability", "corollary", "inequality",
                 "o(log", "asymptotic", "iid", "independently"]


def count_terms(text, terms):
    t = " " + text.lower() + " "
    return sum(len(re.findall(r"(?<![a-z])" + re.escape(term) + r"(?![a-z])", t)) for term in terms)


def term_hits(text, terms):
    t = " " + text.lower() + " "
    return Counter({term: len(re.findall(r"(?<![a-z])" + re.escape(term) + r"(?![a-z])", t))
                    for term in terms if re.search(r"(?<![a-z])" + re.escape(term) + r"(?![a-z])", t)})


PASSIVE_RE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?"
    r"(?:\w+ed|built|done|found|given|known|shown|taken|run|made|seen|written|drawn|chosen|proven)\b",
    re.I)
NOMINAL_RE = re.compile(r"\b\w{4,}(?:tion|tions|ment|ments|ness|ity|ities|ance|ence|ances|ences)\b", re.I)
SUBORD_RE = re.compile(r"\b(?:which|that|where|when|while|because|since|if|although|whereas|unless)\b", re.I)


def sentence_features(df):
    out = df.copy()
    out["words"] = out.text_nocite.map(lambda s: len(words(s)))
    out["words_raw"] = out.text.map(lambda s: len(words(s)))
    out["citations"] = out.text.map(lambda s: len(CITATION_RE.findall(s)))
    out["passive"] = out.text_nocite.map(lambda s: len(PASSIVE_RE.findall(s)) > 0)
    out["nominalizations"] = out.text_nocite.map(lambda s: len(NOMINAL_RE.findall(s)))
    out["clauses"] = out.text_nocite.map(lambda s: 1 + len(SUBORD_RE.findall(s)) + s.count(";"))
    out["commas"] = out.text_nocite.str.count(",")
    out["parens"] = out.text_nocite.str.count(r"\(")
    out["we"] = out.text_nocite.str.contains(r"\b(?:we|our|us)\b", case=False)
    out["syllables"] = out.text_nocite.map(textstat.syllable_count)
    out["fk_grade"] = out.text_nocite.map(textstat.flesch_kincaid_grade)
    out["opener"] = out.text_nocite.map(lambda s: (words(s) or [""])[0])
    return out
