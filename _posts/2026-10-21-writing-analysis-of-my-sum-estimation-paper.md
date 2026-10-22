[*Sum Estimation via Vector Similarity Search*  
arXiv:2601.11765v1 (Jan 2026)](https://arxiv.org/abs/2601.11765v1)

**Code:** the notebook, helper library and data are in [my Github repo](https://github.com/mehulsr/mehulsr.github.io/tree/master/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper).

This notebook measures the paper's prose and answers four questions, each with charts:

1. **Word choice, sentence structure and sentence length**
2. **Clarity and the logical flow of the argument**
3. **Tone and pacing**
4. **Audience density.** Which parts are dense for a lay reader and which for an AI expert, and what order each should read the paper in.

It then covers some extra checks: terminology consistency, whether the abstract's claims are backed up, how the figures and cross-references work, and a list of copy-edits. It ends with conclusions and recommendations.

**Method in brief.** PDF text extraction breaks up the mathematics. So the prose was transcribed into `paper_clean.txt` using the authors' exact wording, typos included. Inline maths is replaced by the token `⟨m⟩` and each display equation by an `[EQ]` line. As a cross-check, the maths density is also measured directly on the raw PDF text. All metrics are standard stylometric measures or transparent heuristics, defined where they're used. The audience scores are a model, not ground truth: they show *relative* density between sections.

## 0. The paper at a glance

|  | Whole paper |
|---|---|
| Prose words | 3680 |
| Sentences | 229 |
| Display equations | 79 |
| Inline maths expressions | 284 |
| Mean sentence length (words) | 16.1 |
| Median sentence length (words) | 14 |
| Flesch–Kincaid grade (whole paper) | 11.5 |

### Where the words go: a map of the paper
The left panel shows the prose word count per section. The right panel shows how much maths each section carries: display equations, plus maths symbols counted straight from the PDF as an independent check.

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_5_0.png)

|  | % of prose words | % of display equations |
|---|---|---|
| Appendix | 12.5 | 84.8 |
| Related work & discussion | 11.3 | 0 |
| Experiments | 34.5 | 5.1 |
| Front matter | 19.8 | 0 |
| Method | 10.4 | 2.5 |
| Theory / proofs | 11.5 | 7.6 |

**Reading the map.** The paper has about 3,700 words of prose, 79 display equations and about 280 inline maths expressions. Most of the prose is in the experiments sections (35%) and the front matter (20%). 85% of the display equations sit in Appendices A–B; Section 3.3 holds most of the rest. The main text is shaped like an *hourglass*: wordy, readable framing at both ends and a thin middle (Sections 2–3.2) that carries the actual algorithm in about 380 words. That middle is the paper's core idea, so its brevity is a strength for experts and a cliff for everyone else (see Q4).

---
# Q1. Word choice, sentence structure and sentence length

### 1a. Sentence length
Reference points: the US *Plain Language* guidelines aim for an average of 15–20 words. Academic science writing typically averages 22–26 words. Sentences over 35 words are where readers start to lose the thread.

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_8_0.png)
    

> Main text: mean 17.5, median 16, 4% of sentences over 35 words; coefficient of variation 0.55

*Sentences of 35+ words (candidates for splitting)*

| Section | Words | Clauses | Citations | Sentence |
|---|---|---|---|---|
| 6 | 58 | 3 | 0 | Because HNSW methods make use of randomly assigned levels with exponentially decaying probabilities, and for each query execution iteratively find a (approximate) most similar vector within each level, it is likely that a slightly modified HNSW algorithm could return the similar vectors at every level for a single query, significantly cutting the total computation time of our method. |
| 1 | 55 | 2 | 0 | In this work, we assume access to a maximization oracle: given a non-negative function ⟨m⟩ (eg, the exponentiation of the negative squared Euclidean distance for KDE with Gaussian kernel) and a set of ⟨m⟩ objects ⟨m⟩, the oracle builds a data-structure that allows it to quickly compute ⟨m⟩ based on a query ⟨m⟩, and more generally, retrieve the top-k objects. |
| 4.6 | 46 | 4 | 0 | Note that the runtime for our method does not scale linearly with ⟨m⟩; in Section 6 we discuss a relatively straightforward opportunity to integrate HNSW methods and our proposed method to improve the runtime, taking advantage of the fact that HNSW also uses random levels with exponentially-decaying probabilities. |
| 5 | 42 | 3 | 1 | Locality sensitive hashing (LSH) (Indyk and Motwani, 1998; Charikar, 2002; Lv et al, 2007; Andoni and Indyk, 2008; Andoni et al, 2015) is a set of vector similarity search techniques that are perhaps the only class of methods which have theoretical guarantees (and avoid an exponential dependence on the dimension), though clustering-based methods and proximity-graph-based methods empirically perform much better. |
| 2 | 39 | 3 | 0 | While we can exactly compute the sum via a linear scan, here, we leverage a black-box maximization oracle, for example a vector similarity search technique, which, given a pre-computed data-structure, can empirically be much faster than a linear scan. |
| 3.4 | 38 | 2 | 0 | In Appendix B, we motivate selecting ⟨m⟩ as the average value of the lower half of the ⟨m⟩ values: ⟨m⟩, which can be estimated from a uniform random sample (the union of elements on unfilled levels is a uniform random sample). |
| 4.6 | 36 | 1 | 0 | To illustrate the performance of methods with respect to the flatness/peakiness, we present the median relative error as a function of the bandwidth for KDE on Open Images for the four methods in Figure 2(a). |
| 6 | 35 | 2 | 0 | One limitation of our use of a black-box maximization oracle in the design of the algorithm is that our performance guarantee is in terms of the number of retrieved similar vectors, rather than total runtime. |

**Findings on sentence length**
- The paper's average sentence (16 words overall, 17.5 in the main text) is **shorter than typical academic prose** and inside the plain-English band. Only 4% of main-text sentences exceed 35 words. The authors are economical writers.
- Sentence length varies a lot (coefficient of variation 0.55), which keeps the rhythm from going monotonous. But the variation is **split by section** rather than mixed within paragraphs. The framing sections (Abstract, Introduction, 4.6 Results, 6 Discussion) run at 22–26 words a sentence. The method and proof sections run at 10–12, because maths carries the content and the prose turns into short connective statements ("Define …", "Then, …").
- The long tail is just 8 sentences, listed above, and they come in three types. All are easy to split.
  - *Clause chains* (the HNSW-integration sentence in Section 6, at 58 words; the runtime and bandwidth sentences in 4.6; the limitation sentence in Section 6) stack 2–4 clauses before the main point lands.
  - *Definitions packed with examples* (the maximization-oracle sentence in the Introduction, at 55 words; the linear-scan sentence in Section 2; the correction-term sentence in 3.4) carry a definition, an example and a consequence all in one sentence.
  - *Citation trains.* The table counts words with citations removed. With them, the Introduction's opening sentence runs to 66 words across 11 references, and the LSH sentence in Related Work carries 5 references in one parenthesis. Readers experience the raw length.

### 1b. Word choice: vocabulary, word length and lexical variety

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_12_0.png)
    

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_13_0.png)
    

> Whole-paper MTLD (lexical diversity): 65  (roughly 70-90 is common for scientific prose; higher = more varied vocabulary)

*Acronyms: first use and expansion*

| Acronym | Uses | First used in | Spelled out in |
|---|---|---|---|
| KDE | 10 | Abs | Abs |
| LSH | 6 | 1 | 1 |
| HNSW | 8 | 1 | 1 |
| CLIP | 5 | 4.2 | never |
| ViT | 2 | 4.2 | 4.2 |
| BERT | 4 | 4.2 | never |
| DistilBERT | 3 | 4.2 | never |
| AWS | 2 | 4 | never |
| RAM | 2 | 4 | never |
| GB | 2 | 4 | never |
| pdf | 2 | 4.1 | 4.1 |
| KL | 1 | A | never |

**Findings on word choice**
- **The vocabulary is precise and repetitive by design.** *Vector similarity search* (17 times, the most frequent phrase), *relative error*, *maximization oracle* and *top-k* recur as fixed technical labels, and the authors avoid "elegant variation" (swapping in synonyms for the same thing). That consistency is good for clarity, and it explains why lexical diversity (MTLD about 65) sits slightly *below* the usual range for scientific prose. The cost is heaviness: a 3-word noun phrase repeated 17 times. Coining a short form once ("VSS") would lighten the Introduction, Section 5 and Section 6.
- **Plain verbs, little puffery.** The verbs that do the work are *define, compute, estimate, retrieve, show, prove*. Nominalisations (nouns built from verbs, such as *estimation*, *exponentiation*, *instantiation*) peak in 4.1 Tasks, 3.3, the Abstract and the Introduction. In the front matter, that noun-heavy style is what makes sentences long (see 1c).
- **Two vocabularies, cleanly separated.** AI/ML vocabulary (*embedding, softmax, HNSW, CLIP*) dominates the Introduction and Section 4. Probability vocabulary (*martingale, filtration, Bernstein, union bound*) is fenced into 3.3 and the appendix. A reader can therefore pick a lane.
- **Acronym hygiene is mostly good.** KDE, LSH, HNSW and ViT are expanded on first use. **CLIP and BERT are never expanded**, which is standard for ML readers but opaque to anyone else. *AWS/RAM/GB* are fine.

### 1c. Sentence structure

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_17_0.png)
    

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_18_0.png)
    

**Findings on sentence structure**
- **Active, first-person voice dominates.** 47% of sentences use *we/our/us* (100% in the Discussion, about 85% in the Abstract, 4.5 and 4.6). Passive voice appears in only about 10%, low for a theory-plus-experiments paper. The prose reads as authors walking you through their work, which aids clarity. The passive clusters in 4.2 Models (38%: "is trained on", "obtained through"), where it is appropriate.
- **Openers are formulaic but functional.** *For*, *We*, *The*, *In*, *If* and *This* open most sentences. In the method and proof sections the rhythm ("Define … If … Then … Thus …") mirrors mathematical style and suits it. In the Abstract, 6 of 8 sentences open with *We/Our/With* or *In this work, we*, a slightly monotone cadence.
- **Parentheticals are a habit.** The paper leans on brackets for definitions, licences, examples and asides. Section 4.2 averages about one per sentence (licences, model sizes), and 4.6 and the Section 4 intro about 0.7. They are fine for experts, but they interrupt the sentence for lay readers. Licence details (*Apache 2.0 license*, *CC BY 4.0*) could go into a single footnote or appendix table.
- **Long ≠ complex.** The front matter has the *longest* sentences, yet about 70% of them are single-clause. Their length comes from stacked noun phrases and lists ("words and tokens (…), sentences and documents (…), images (…), audio clips (…), videos (…)") rather than nested reasoning. The method and theory sections are the opposite: short sentences, but more than half carry a subordinate clause (*if, where, since, which*), because definitions and conditions are packed in. So lay readers face long-but-flat sentences up front, and short-but-dense ones in the middle.

---
# Q2. Clarity and logical flow

### 2a. Readability by section
The Flesch–Kincaid grade estimates the US school grade needed to follow the prose, computed with maths tokens removed. Here it is paired with how much maths the section carries, because maths is an extra cost that a prose readability formula can't see.

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_21_0.png)
    

The two panels mirror each other. **The sections that read hardest as prose (Abstract, Introduction, Related Work, Discussion: grade 16–20) contain almost no maths. The sections with the easiest prose (3.x and the appendix: grade 4–11) carry 10–26 inline maths expressions per 100 words.** The overall grade is 11.5, but that average hides the trade-off. The only sections easy on *both* counts are 4.2–4.3 and 4.6, the descriptive parts of the experiments. Everywhere else the reader pays either in sentence complexity or in notation. The low grades in Section 3 flatter it, because "Then, ⟨m⟩." scores as easy text.

### 2b. Logical connectives: how explicitly is the reasoning signposted?

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_23_0.png)
    

**Findings.** The reasoning is **explicit where the maths is and implicit where the prose is**. The theory sections and appendix run at 8–10 connectives per 100 words: causal (*since, thus, so*), sequencing (*first, then, finally*) and signposts to lemmas and equations. That is a well-walked proof. The front matter, experiments and related work run at only about 2–3 per 100 words. Those parts read as a sequence of statements, and the reader must infer *why* one sentence follows another. **Contrast markers are among the scarcest types**, even though the paper's main claim is comparative (O(log n) against O(√n), lower error than the combined baseline). Section 4.6 has the most contrast markers (*while, except, unlike*), which is right. But the Introduction states the gap with a single "Unfortunately", and Related Work positions the paper mostly by listing ("In comparison…", "differs"). A sharper "prior methods do X; we do Y, which buys Z" line would make the contribution land faster.

### 2c. Sentence-to-sentence cohesion
The overlap between each sentence's content words (TF-IDF) and those of the sentence before it. High values mean each sentence picks up where the last left off. Dips mark topic jumps.

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_25_0.png)
    

*Sentences with ~zero overlap with the preceding sentence (main text)*

| Section | Sentence |
|---|---|
| Abs | We show results on applications in estimating densities, computing softmax denominators, and counting the number of vectors within a ball. |
| Abs | Our partially redacted code can be found at URL. |
| 1 | In this work, we study a related set of problems that involve computing or estimating a sum over all elements in a dataset. |
| 1 | For a query ⟨m⟩, we retrieve the top-k objects from each level, and compute an unbiased estimate using a simple algorithm (see details in Section 3.2). |
| 1 | We present experimental results showing the effectiveness of our method for sum estimation tasks on Open Images and Amazon Reviews. |
| 1 | Our contributions are several: |
| 1 | Show an estimator of the sum given the top-k elements from each exponentially-sampled level. |
| 1 | Introduce an additional sum estimation application: counting the number of elements within a ball. |
| 1 | Present experimental results that demonstrate the effectiveness of our method. |
| 1 | Finally, we conclude by covering related work and a opportunities and limitations in Sections 5 and 6. |

**Findings.** *(Caveat: the measure only sees words, so in maths-heavy sections the link carried by symbols is invisible and scores read low.)*
- **Best-knit prose: the Introduction, 4.3 Datasets, 4.5 Setup and 6 Discussion.** Each paragraph develops one object and repeats its key nouns, so a reader is never lost about the topic.
- **Weakest: 4.1 Tasks, 3.1 and 4.2 Models.** 4.1 jumps between three tasks (KDE → softmax → counting), and inside each it alternates a prose sentence with a formula sentence ("Here, ⟨m⟩ is 'peaky' for small ⟨m⟩"). The three paragraphs share a template but never say so. One framing sentence ("Each task is a sum of a monotone function of distance or similarity, so a vector search can find its largest terms") would tie them together and tell the reader *why these three*.
- **Topic jumps sit at paragraph starts, as they should.** The near-zero dips in the trace are mostly the first sentence of a new run-in paragraph (Models, Datasets, Baselines), which is acceptable in reference-style sections. The one costly jump is in the Introduction: paragraph 1 surveys embeddings → search algorithms → commercial systems, and the *sum* problem arrives only in paragraph 2. A bridging sentence ("Many downstream tasks need not just the nearest items but an aggregate over *all* items …") would join them.

### 2d. Cross-reference flow: does the paper point forwards or backwards?
Each arc is an explicit reference (Section/Appendix/Figure/Algorithm/Lemma/Theorem/Equation) from where it is written to where its target lives. **Forward** references (above the axis) ask the reader to trust something not yet shown. **Backward** references (below) consolidate.

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_27_0.png)

| Section | 1 | 3.1 | 3.3 | 3.4 | 4.4 | 4.6 | 6 | A.2 | B | C |
|---|---|---|---|---|---|---|---|---|---|---|
| Backward | 0 | 1 | 0 | 0 | 1 | 3 | 0 | 1 | 2 | 2 |
| Forward | 6 | 0 | 4 | 1 | 0 | 2 | 1 | 0 | 0 | 0 |

**Findings.** The paper has **more forward references than backward ones**. Most come from three sources:
1. The Introduction's roadmap, which is expected.
2. Section 3.3 deferring proofs to Appendices A.1–A.3, which is standard.
3. Results sending readers to Appendix C.

The arc from 6 → C (recall values) is the right way to back a limitation with evidence. **One problem**: Figure 1 lives in Section 2 but illustrates the proof of Proposition 3.1 in Section 3.1. A reader meets it before they can understand it. Likewise, Figure 3 is typeset inside Related Work although it belongs to 4.6. Moving each figure next to its first reference would remove two "where is this?" detours.

### 2e. Concept introduction map: are ideas set up before they are used?

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_29_0.png)
    

**Findings on flow**
- **The skeleton is classic and sound**: problem → prior work's gap (O(√n)) → key idea (levels) → estimator → guarantee → experiments → limitations. Every contribution bullet has a matching section.
- **"Unbiased" and "high-probability bound" are promised in the Abstract and Introduction long before they are defined** (3.2, 3.3). That is normal, but a one-sentence intuition early ("each sampled value is up-weighted by the inverse of its chance of being seen") would let lay readers follow the promise.
- **Some definitions live only in notation.** *Top-k* is defined in Section 2 purely as ⟨m⟩ (the empty black square in the chart), and the first plain-words explanation comes in 4.4 Baselines. *Maximization oracle* is defined in prose in the Introduction, which is good, but it is a theory-of-computing term many ML readers will pause on.
- **"Peaky vs flat" is the paper's best intuition device, but it first appears in Section 4.** It explains *why* top-k fails in one regime and random sampling in the other, and why the new method is needed. Introduced in the Introduction, it would motivate the whole design, not just the experiments.
- **Runtime is claimed in the Abstract ("less computational time") but the theory says nothing about runtime** (Section 6 says so explicitly). The claim is supported only by Figure 3, and one panel shows a tie. The argument flows, but the Abstract slightly over-reaches relative to the evidence (see 5b).
- **There is no Conclusion section.** The paper ends on a forward-looking HNSW paragraph, so the reader never gets a closing restatement of what was shown.

---
# Q3. Tone and pacing

### 3a. Tone: hedging versus confident language
Hedges soften a claim (*perhaps, likely, approximately, typically, may*). Boosters strengthen it (*prove, provably, novel, significantly, always, simple, key*). Both are counted per 100 words.

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_32_0.png)
    

> Whole paper: 0.68 hedges and 1.82 boosters per 100 words

**Findings on tone**
- **The tone is confident, measured and understated.** Boosters outnumber hedges about 2.7 to 1 (1.8 against 0.7 per 100 words). But the top boosters are *technical*, not promotional. *Show* (9), *unbiased* (6), *prove* (6) and *high probability* (5) are claims of the method's actual properties, not adjectives. The two promotional words, *novel* (Abstract) and *significantly* (Section 6), appear once each.
- **The Abstract and Introduction are the most assertive parts** (about 3.5 boosters per 100 words). That fits their job, but it puts the strongest language exactly where the evidence hasn't been shown yet (see 5b).
- ***Simple* is the paper's favourite self-description** (5 uses: "a simple algorithm", "simple estimate", "the simple algorithm", "simple way", "simple form"). It sets a friendly, unpretentious tone. But it is also a mild booster that can backfire when the very next paragraph is a martingale argument. Keep it for Algorithm 1, where it is earned.
- **Hedging is concentrated where it should be**: the Discussion (the most hedged section: "typically approximate", "it is likely that a slightly modified HNSW…", "assumes perfect recall"), 3.4 Control variates ("imperfect", "typically") and Related Work ("perhaps the only class"). The authors are candid about the oracle assumption and the missing runtime guarantee. That honesty builds credibility.
- The **voice is collegial "we"**, with occasional conversational touches ("perhaps surprisingly", "too quickly", "we're done", "best of both worlds", "don't"). They make the proofs feel walked-through rather than recited, though the contractions are slightly informal for a venue paper.

### 3b. Pacing: how fast does the paper move?

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_34_0.png)
    

*Reading-time model:* a lay reader reads at 200 wpm, spends about 1 min per display equation and about 6 s per inline expression. An expert reads at 250 wpm, spends about 20 s per equation and about 2 s per inline expression. These are rough, but the ratios between sections are what matter.

**Findings on pacing**
- **The pacing is front-loaded with concepts.** The Abstract introduces about 12 new technical terms per 100 words, roughly 3× the Introduction and higher than anywhere else. Embeddings, vector similarity search, KDE, softmax, top-k, levels, unbiasedness and relative-error bounds all arrive in 197 words. That is a steep on-ramp for a non-specialist. 4.2 Models is the second spike (CLIP, ViT, DistilBERT, BERT, knowledge distillation), but those terms are incidental to the argument.
- **The method itself (Sections 2–3.2) is very fast.** The core algorithm takes about 380 words, plus Algorithm 1. For experts this is admirable concision. For everyone else it is the moment the paper speeds up without warning: the orange maths line in the rhythm chart jumps the moment Section 2 begins.
- **Section 3.3 is the slow, heavy stretch.** It takes over a quarter of a lay reader's main-text time for a result the Abstract summarises in one clause. Experts move through it in about 5 minutes, because the proof pattern (Chernoff → union bound → Bernstein) is familiar.
- **The experiments decelerate nicely.** Sections 4.1–4.5 use short sentences with one idea per paragraph. Section 4.6 picks the pace back up with long comparative sentences, the right move for a results section.
- **The ending is abrupt.** Section 6 has the paper's longest average sentence (26 words) and stops without a summary. The reader exits mid-thought (see the recommendation to add a Conclusion).
- **Overall cost:** about 50 minutes for a lay reader to get through the main text closely (about 125 minutes including the appendix), against about 23 minutes (about 50 with the appendix) for an expert.

---
# Q4. Audience density: lay readers versus AI experts

### 4a. Two density indices
Each section is scored on eight components. Each component is min–max normalised across sections, and the weighted sum is rescaled so that, for each audience, the lightest section scores 0 and the densest scores 100. The weights differ by audience:

| Component | Lay-reader weight | AI-expert weight | Why |
|---|---|---|---|
| Inline maths per 100 words | 0.25 | 0.25 | Notation is the biggest single barrier for a lay reader, and still costly for experts |
| Display equations per 100 words (log) | 0.20 | 0.25 | |
| Probability/theory vocabulary | 0.15 | 0.25 | Many ML practitioners don't use martingales daily |
| Flesch–Kincaid grade | 0.10 | 0.05 | Long sentences slow everyone, but experts less so |
| Dale–Chall "difficult" words % | 0.10 | 0.00 | Experts know academic vocabulary |
| AI/ML vocabulary | 0.10 | 0.00 | *Embedding, softmax, HNSW* are everyday words for experts |
| Acronyms per 100 words | 0.05 | 0.00 | |
| New-concept rate | 0.05 | 0.20 | Experts are slowed by *new ideas*, not by vocabulary |

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_37_0.png)
    

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_38_0.png)

|  | Section | Lay density (0-100) | Expert density (0-100) | Lay reading minutes | Expert reading minutes |
|---|---|---|---|---|---|
| A.3 | A.3 Bernstein restatement | 100 | 91.8 | 9.6 | 3.3 |
| A | A.1 Chernoff-style lemma | 88 | 100 | 21.6 | 7.3 |
| A.2 | A.2 Tighter variance bound | 84.2 | 83.2 | 29.3 | 9.7 |
| 3.3 | 3.3 High-probability bound | 70.6 | 78.4 | 13.6 | 5.1 |
| B | B Correction-term choice | 67 | 67.5 | 14.6 | 5.1 |
| 3 | 3 Method & Analysis | 57.3 | 40.6 | 1.1 | 0.4 |
| 3.2 | 3.2 Unbiased estimate | 53.7 | 52 | 4.6 | 1.7 |
| 2 | 2 Setting | 52.7 | 34.8 | 2.8 | 1.2 |
| 4.4 | 4.4 Baselines | 52 | 38.5 | 5.4 | 2 |
| 4.1 | 4.1 Tasks | 51.4 | 28.5 | 4.7 | 2.1 |
| Abs | Abstract | 46.2 | 43.2 | 1.3 | 0.9 |
| 4.2 | 4.2 Models | 45.1 | 17.8 | 0.8 | 0.6 |
| 1 | 1 Introduction | 38.9 | 21.4 | 4 | 2.5 |
| 3.1 | 3.1 Union of top-k | 38.9 | 40.7 | 2.1 | 0.8 |
| 4.5 | 4.5 Experimental setup | 36.9 | 13.8 | 1.5 | 0.9 |
| 5 | 5 Related Work | 35.4 | 10.2 | 1.5 | 0.9 |
| 6 | 6 Discussion | 32.5 | 6.4 | 1.1 | 0.9 |
| 4 | 4 Experiments | 26 | 19.7 | 1.4 | 0.7 |
| 3.4 | 3.4 Control variates | 24.5 | 26.4 | 1.5 | 0.7 |
| 4.6 | 4.6 Results | 18.4 | 13.6 | 2.2 | 1.4 |
| 4.3 | 4.3 Datasets | 10.5 | 0 | 0.7 | 0.5 |
| C | C Full results | 0 | 4.6 | 0.7 | 0.5 |

**Findings on density**

*For a lay reader*
- **Densest:** the appendix (A.3, A.1, A.2, B), then **3.3 High-probability bound**, then the method block (**3, 3.2, 2**). Notation and theory vocabulary pile up there. **Section 2 is the real cliff.** It is the *first* place maths takes over (from 2.5 to 12.6 inline expressions per 100 words) and it comes straight after a readable Introduction.
- **Dense without maths:** **4.4 Baselines, 4.1 Tasks, the Abstract and 4.2 Models** sit in the middle of the lay scale for different reasons. 4.1 and 4.4 embed formulas; the Abstract has the highest new-concept rate; 4.2 is wall-to-wall model names. The Abstract's maths symbols (O(√n), O(log n)) are few, but they are the punchline, and a lay reader can't decode them.
- **Most accessible:** **Appendix C, 4.3 Datasets, 4.6 Results, 3.4 (short), Section 4's intro and 6 Discussion.** Concrete nouns (Amazon reviews, images, AWS machines) and plain claims ("our method achieves lower error for the same runtime").

*For an AI expert*
- **Densest:** the appendix proofs (A.1, A.3, A.2) and **3.3**, then **B** and **3.2**. The difficulty is conceptual (martingale concentration, inverse-probability weighting), not linguistic. **3.2 Unbiased estimate** is dense *per word*: the whole estimator is packed into about 130 words.
- **Light:** 4.3, Appendix C, the Discussion, Related Work, 4.5 and 4.6. These are familiar territory for an ML researcher, who can move quickly.
- **Biggest audience gap** (lay ≫ expert): **4.2 Models, 6 Discussion, 5 Related Work, 4.5 Setup and 4.1 Tasks.** Vocabulary that is jargon to one reader (CLIP, softmax, HNSW, LSH) is everyday language to the other, and long sentences cost a lay reader more.
- **No section is "dense for experts but easy for lay readers"** (the empty top-left quadrant). Everything hard for an expert is harder still for a lay reader, as you'd expect from a paper whose difficulty is mathematical.

### 4b. Recommended reading order for each audience
The paper is cut into 15 reading units; the Introduction is split into its motivation half and its idea/contributions half. Each unit gets a **value** for each audience:
- a lay reader wants what problem this solves, whether it works, and what its limits are;
- an expert wants what is new, how it works, why it is correct, and how it compares.

The **depth** (read closely / skim / optional) is computed from value and density: units with value ≥ 0.7 are read closely, and units with value ≥ 0.4, or with low density for that audience, are skimmed. The **order** is editorial. It follows each audience's natural sequence of questions and respects prerequisites (for example, Results come after Tasks and Baselines). Bar length is the time cost at that depth, and the label is the unit's density index for that audience.

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_40_0.png)
    

**Recommended reading orders**

**Lay reader (curious non-specialist, about 20 min)**
1. **Abstract.** Read for the problem only: "estimate a sum over everything using a search engine for similar items".
2. **Introduction ¶1–2.** Why embeddings and similarity search are everywhere, and why existing tricks need √n lookups.
3. **4.1 Tasks.** The three concrete uses (density, softmax, counting). This is where the problem becomes tangible. Skip past the formulas; the words around them carry the meaning.
4. **4.4 Baselines.** "Only the top items" versus "a random sample", plus the *peaky/flat* intuition. **This is the best plain-language explanation of the problem in the paper; read it before the method.**
5. **4.6 Results + Figures 2–3.** Does it work? Yes, mostly, at lower error for equal runtime.
6. **6 Discussion.** Honest limitations and the HNSW opportunity.
7. *Skim* Introduction ¶3–5 (the key idea of "levels") and 4.2/4.3/4.5 (what data and models were used).
8. *Optional:* Sections 2–3.2 for the flavour of the algorithm, and Appendix C. *Skip* 3.3, 3.4, Related Work and the proofs.

**AI expert (ML researcher or engineer, about 30 min)**
1. **Abstract → Introduction ¶3–5 (key idea + contributions).** The O(log n) against O(√n) claim and the skip-list/HNSW-style levels.
2. **Section 2 → 3–3.2 + Algorithm 1.** The whole method. Read slowly; it is short but dense.
3. **4.4 Baselines → 4.6 Results (Figures 2–3).** Check the error/runtime trade-off and the one tie (3b).
4. **3.3 Theorem 3.2 statement and the worked example** (n = 10⁷, k = 200 → error < 0.16). Theorists continue into the proof and Appendices A–B. Practitioners can stop at the statement.
5. **5 Related Work → 6 Discussion.** Position against Mussmann et al. 2017, Karppa et al. 2022 and the LSH-based estimators, plus the limits of the oracle assumption.
6. *Skim* Introduction ¶1–2, 4.1, 4.2/4.3/4.5 and 3.4. *Optional:* Appendix C (recall by level supports the perfect-recall assumption).

The key difference: **lay readers should reach the *results* and the *peaky/flat intuition* before the method; experts should reach the *method* before the results.** The paper's own order (Intro → Setting → Method → Theory → Experiments) is built for the expert path. That is right for a cs.DS preprint, but it means a lay reader has to jump to Section 4 to find their footing.

---
# 5. Other questions worth answering
### 5a. Terminology consistency

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_42_0.png)
    

Inconsistent spellings are small, but they add up. **Open Images / OpenImages**, **top-k / Top-k / TopK**, **data structure / data-structure** and the hyphenation of *exponentially(-)decaying* and *high(-)probability* all vary. Pick one form each, using hyphens only when the compound is used as a modifier ("a high-probability bound", "holds with high probability").

### 5b. Do the Abstract's claims match the evidence?

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_44_0.png)
    

| Claim (Abstract / Intro) | Where the paper backs it | Verdict |
|---|---|---|
| Reduces requirement from O(√n) to O(log n) similar vectors | §3.1 Prop 3.1, §3.2, Thm 3.2 | Supported |
| Unbiased estimate of the sum | §3.2 (one-line argument) | Supported |
| High-probability relative-error bound | §3.3, App A | Supported |
| Bound is tight in practice ('at most loose by a factor of 2') | §4.6, Fig 2b (synthetic only) | Partly supported |
| Lower error than existing reductions | §4.6, Fig 3 (4 of 5 panels) | Mostly supported |
| …using less computational time | Fig 3 only; no runtime theory (§6); 3b is a tie | Partly supported |
| Applications: densities, softmax, counting | §4.1, Figs 3-4 | Supported |

### 5c. Figures and captions

| Figure | placed in | first referenced in | Words | self-contained? |
|---|---|---|---|---|
| Figure 1 | 2 | 3.1 | 52 | no – references proof terms (U, ℓ*) |
| Figure 2 | 4.5 | 4.6 | 36 | yes |
| Figure 3 | 5 | 4.6 | 66 | yes |
| Table 1 | B | never | 6 | no – title only, no takeaway |
| Figure 4 | C | C | 59 | yes |
| Figure 5 | C | C | 38 | yes |

- **Table 1 is never referenced by name.** Appendix C says "See *Figure 1* for the recall values for TopK without levels", which should be **Table 1**.
- Figure 1 sits in Section 2 but explains the proof in 3.1. Figure 3, the paper's key result figure, floats into Related Work.
- Captions are generally informative. They state what is plotted *and* how the confidence intervals were computed, which experts appreciate. They rarely state the **takeaway** ("Our method is the only one with low error across the whole flat-to-peaky range"). A one-sentence conclusion in each caption would help skimmers, who often read only the figures.

### 5d. Copy-edit list (found by a full read, plus an automatic duplicate-word check)

> Automatic duplicate-word check found: "when when" in Section 4.6

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_48_1.png)
    

| Where | As written | Suggested |
|---|---|---|
| Abstract | vector similar search implementation | vector similarity search implementation |
| Abstract | OpenImages | Open Images (match body text) |
| §1 ¶1 | there has been significant advances | there have been significant advances |
| §1 roadmap | analyze our algorithm in Section 3 We then | …in Section 3. We then |
| §1 roadmap | a opportunities and limitations | opportunities and limitations |
| §3.3 | This will later allow us to lower bound pᵢ , Our main step | …lower bound pᵢ. Our main step |
| §3.3 Lemma 3.6 | positive and monotonically nondecreasing | non-increasing (fᵢ are sorted in decreasing order) |
| §4.1 | the bandwidth parameters that controls | the bandwidth parameter that controls |
| §4.2 | which is Vision Transformer (ViT) | which is a Vision Transformer (ViT) |
| §4.3 | The Flick30k dataset | The Flickr30k dataset |
| §4.3 | with train dataset having about 20,000 classes | with the train set having about 20,000 classes |
| §4.4 | and the use the unbiased estimate | and then use the unbiased estimate |
| §4.5 | randomly sample human-provided captions | randomly sampled human-provided captions |
| §4.6 | low error when when f is | low error when f is |
| Fig 3 caption | so it is cutoff in the plot | so they are cut off in the plot |
| §5 | hashing-based estimators Charikar and Siminelakis (2017) | hashing-based estimators (Charikar and Siminelakis, 2017) |
| §6 | find a (approximate) most similar vector | find an (approximate) most similar vector |
| App A title | Proofs of a select number of lemmas | Proofs of selected lemmas |
| App A.3 title | Restatement Bernstein's inequality | Restatement of Bernstein's inequality |
| App A.3 | Dzhaparidze and Van Zanten (2001) cites | …cite |
| App C | See Figure 1 for the recall values for TopK | See Table 1 … |
| References | Open Images dataset v4 (title) vs v7 (text) | Check which version was used |

---
# 6. Conclusions

### The style in one paragraph
The paper is written in a **lean, confident, engineer-mathematician style**. Sentences are short by academic standards (main-text mean 17.5 words). The voice is active and first-person ("we"), the vocabulary is precise and consistently reused, and the claims are measured: boosters are technical, not promotional, and the limitations are stated candidly. Its weaknesses come from **economy rather than excess**. The core method is compressed into about 380 words, the best intuition ("peaky vs flat") is held back until Section 4, the paper ends without a conclusion, and about 20 copy-level slips suggest a final proofreading pass was skipped.

### Scorecard

    
![png](/code/2026-10-21-writing-analysis-of-my-sum-estimation-paper/writing_style_analysis_files/writing_style_analysis_50_0.png)
    

| Dimension | Score (1-5) | Why |
|---|---|---|
| Word choice | 4 | Precise, consistent terms; minimal puffery. Heavy repetition of 'vector similarity search'; CLIP/BERT unexpanded. |
| Sentence structure | 4 | Short, active, first-person. A handful of 35-50-word citation trains and clause chains. |
| Sentence length | 4 | Mean 16 (all) / 17.5 (main text); good variety. Abstract/Discussion run long. |
| Clarity | 3 | Precise for experts; abrupt jump into notation in §2; key intuition arrives late. |
| Logical flow | 4 | Clean problem→idea→proof→experiments arc; every contribution backed; figures misplaced; no conclusion. |
| Tone | 4 | Confident, honest, collegial. 'Simple' over-used; a few contractions. |
| Pacing | 3 | Concept-dense opening, very fast method, slow proof, abrupt ending. |
| Lay accessibility | 2 | Readable only in §4 and §6; abstract/intro assume ML literacy. |
| Expert accessibility | 4 | Efficient: an expert gets the whole idea in ~2 pages. |
| Polish / correctness of prose | 2 | ~20 typos/grammar slips, one wrong cross-reference, inconsistent spellings. |

### Top recommendations, in priority order
1. **Fix the copy-edits in 5d** (about 30 minutes of work, the largest gain in perceived quality). Above all, fix *Figure 1 → Table 1* in Appendix C and *nondecreasing → non-increasing* in Lemma 3.6, which is a mathematical, not cosmetic, slip.
2. **Move the "peaky vs flat" intuition into the Introduction.** Two sentences would do: "Top-k works when a few items dominate the sum; random sampling works when contributions are even; our levels interpolate automatically." This is the single biggest clarity win for every audience.
3. **Add a plain-language bridge before Section 2**, such as: "Think of each level as a progressively thinner random subsample: level 1 holds half the data, level 2 a quarter … The top results from each level tell us about both the heavy hitters and the long tail." This softens the notation cliff.
4. **Add a short Conclusion** restating the result (O(log n) vs O(√n), unbiased, bound within 2× of empirical) and the main limitation.
5. **Temper "less computational time" in the Abstract** to match the evidence, for example "lower error at equal or lower computational time in four of five settings".
6. **Split the 35+-word sentences** listed in 1a, especially the maximization-oracle definition in the Introduction and the HNSW sentence in Section 6, and break up the opening sentence's 11-reference citation train.
7. **Relocate Figures 1 and 3** next to their first references, and add a one-line takeaway to each caption.
8. **Standardise terminology** (5a), expand CLIP and BERT once, and move licence details out of the running text.
