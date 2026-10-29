# The cost of a person in Silicon Valley

A bottom-up, fully-sourced model of what it actually costs to employ one software engineer in the
San Francisco Bay Area in 2026 — and what the equity in their offer is really worth.

- **[`cost_of_a_person.ipynb`](cost_of_a_person.ipynb)** — the analysis. 32 cells, 13 figures,
  executed end to end with outputs saved, so it reads as a document without running anything.
- **[`data/sources.json`](data/sources.json)** — every input, with a URL, an as-of date and a
  confidence tier. Nothing in the notebook is a number invented in a cell.

## Headline findings

| | |
|---|---|
| Cash cost of a $241k L5 senior engineer | **$375,000/yr — 1.56× base** |
| Including the GAAP equity expense | **$551,000/yr — 2.29× base** |
| Cash above base salary that isn't in the offer letter | **$134,000** |
| Biggest overhead line | **Recruiting** (~$15k/yr amortised), bigger than health insurance |
| Error bar, offer already known | **±4% at 80% confidence** |
| Error bar, budgeting a hire whose level isn't fixed | **±22% — six times wider** |
| Early-stage startup options: median realised value | **$0.00 per $1 granted** (mean $0.04) |

The multiple is **not a constant**: 1.70× at $150k base, 1.56× at $241k, 1.45× at $400k. Employer
payroll tax and flat-dollar benefits are both capped, so the load is regressive.

## What it answers

1. What the Bay Area market actually pays, by level (levels.fyi)
2. Why employer payroll tax doesn't scale — and why RSUs cost real cash
3. What each benefit costs, with a **selectable menu** of 18 of them
4. The overhead stack nobody budgets for
5. The fully-loaded multiple, calibrated against the BLS ECEC release
6. **Interactive:** base-salary slider + benefit checkboxes + work mode + recruiting channel
7. Equity: GAAP cost vs. employee value, from SEC 10-K filings
8. **Monte Carlo:** how often options actually vest (200k simulated employees × 3 scenarios)
9. **Range of accuracy:** 40k-draw uncertainty propagation + a tornado chart
10. How much revenue the hire has to generate
11. What ramp and turnover cost

## Running it

```bash
python3 -m venv .venv && ./.venv/bin/pip install numpy pandas matplotlib scipy ipywidgets jupyterlab
./.venv/bin/jupyter lab cost_of_a_person.ipynb
```

A `.venv` is already set up in this directory. The interactive controls in §7 need a live kernel;
every section also renders a static default, so the saved notebook reads correctly as-is. The
random seed is fixed — every figure reproduces exactly.

## Sources

Confidence tiers are marked on every input in `data/sources.json`.

**Tier A — primary filings and government releases**
- [BLS, Employer Costs for Employee Compensation, June 2026](https://www.bls.gov/news.release/pdf/ecec.pdf) (USDL-26-1494) — the calibration benchmark
- [SEC EDGAR XBRL company facts](https://www.sec.gov/edgar/searchedgar/companysearch) — stock-based compensation and revenue for Alphabet, Meta, NVIDIA, Microsoft, Netflix, Salesforce
- [Meta FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) — headcount, quoted verbatim
- IRS / SSA 2026 cost-of-living adjustments — wage bases and contribution limits

**Tier B — large datasets published by their owners**
- [levels.fyi — SF Bay Area software engineer salaries](https://www.levels.fyi/t/software-engineer/locations/san-francisco-bay-area) (n = 12,061) and the [Google by-level page](https://www.levels.fyi/companies/google/salaries/software-engineer/locations/san-francisco-bay-area)
- [KFF 2025 Employer Health Benefits Survey](https://www.kff.org/health-costs/2025-employer-health-benefits-survey/) — premiums and employer share
- [Carta — startup employment tenure](https://carta.com/data/employment-tenure-startups/) and [startup shutdown data](https://carta.com/data/startup-shutdowns-q1-2024/)
- Vanguard, *How America Saves 2025* — 401(k) match rates
- [Cushman & Wakefield SF Office MarketBeat Q3 2026](https://www.cushmanwakefield.com/en/united-states/insights/us-marketbeats/san-francisco-marketbeats/office) and Savills *Market in Minutes* Q3 2026 — office rents
- [California EDD](https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/) — SUI, ETT, SDI
- SHRM 2025 Talent Acquisition Benchmarking (n = 2,371) — cost per hire

**Tier C — practitioner benchmarks, wide error bars.** Agency fee percentages, sqft per employee,
per-seat software and cloud spend, ancillary benefit costs, ramp time, replacement cost, and the
~38% option-exercise rate attributed to Pave. These are the inputs the uncertainty analysis in §10
varies, and the tornado chart shows which ones actually matter.

## Caveats

- **Not a tax opinion.** The 2026 California FUTA credit reduction is unsettled until the IRS
  notice lands in November 2026, and your SUI rate is experience-rated, not the 3.4% new-employer
  rate. Confirm with EDD and your payroll provider.
- **levels.fyi is self-reported** and skews toward large public employers and toward people pleased
  with their offer. Treat the medians as the upper half of the real market.
- **The vesting simulation is a population model**, not a prediction about any individual grant.
  The early-stage volatility parameter is a modelling choice, not a measurement.
- **Tier 5 is not auditable GAAP.** It approximates steady-state SBC with the annualised grant
  value; real recognition involves graded vesting, forfeiture estimates and mark-to-market on
  liability-classified awards.
