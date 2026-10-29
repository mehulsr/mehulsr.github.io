# What it costs to hire a person in Silicon Valley

*San Francisco Bay Area · 2026 tax year · all figures USD*

**Code:** the notebook, the sourced inputs and the figures are in [my Github repo](https://github.com/mehulsr/mehulsr.github.io/tree/master/code/2026-10-28-cost-of-a-person).

A base salary is one line on an invoice. The cost of employing someone is larger, and it has four
other parts. Payroll taxes stop scaling partway up the salary range. The benefits bill is nearly
flat in dollars. Overhead never appears in an offer letter. And equity costs the company a different
amount from what it is worth to the employee.

I built that number from the bottom up. The inputs are SEC filings, BLS releases, IRS and California
EDD rate tables, KFF's premium survey, Carta's tenure data and levels.fyi. Every assumption is a
parameter rather than part of a fixed multiple.

For one senior engineer on a $241,000 base:

| | |
|---|---|
| Cash cost (salary, bonus, tax, benefits, overhead) | **$375,037 — 1.56× base** |
| Including the GAAP equity expense | **$551,037 — 2.29× base** |
| Cash above base salary, not in the offer letter | **$134,037** |
| Margin of error once the offer is known | **±3.5% at 80% confidence** |
| Margin of error when the level is not yet fixed | **±22%** |

The rest of this post breaks that down. Several results contradict the usual rules of thumb.

---

## How the model is built

Most "true cost of an employee" calculators mix incremental cash costs with accounting allocations.
Those answer different questions. This model keeps six tiers separate, so you can choose which ones
to add:

| Tier | What it is | Cash? | Incremental to one more hire? |
|---|---|---|---|
| 1 · Direct cash comp | base + cash bonus | yes | yes |
| 2 · Statutory | employer payroll taxes, workers' comp | yes | yes |
| 3 · Benefits | health, retirement, leave, perks | yes | mostly |
| 4 · Operating overhead | recruiting, space, tools, devices, cloud | yes | partly — space is lumpy |
| 5 · Equity | GAAP stock-based compensation expense | **no** | yes |
| 6 · Allocated org overhead | share of management, HR, finance, legal | yes | **no** — an allocation |

It also excludes three items that inflate many published figures:

1. **Paid leave.** BLS counts paid time off as a benefit worth about 9% of total compensation. For a
   salaried engineer that time is already inside the salary. You pay the same $241k whether they
   take 10 days or 25. Counting it again double-counts it.
2. **Supplemental pay.** BLS's "supplemental pay" category is bonuses. Those are already in Tier 1.
3. **California SDI.** State Disability Insurance is paid by the employee in California. It appears
   as an employer cost in a number of published calculators. It costs the employer nothing.

The result is calibrated against the BLS Employer Costs for Employee Compensation release. That is
the only nationally representative measurement of this quantity. The check is in section 5.

---

## 1 · What the market pays

Two views of the same market, answering different questions.

![Pay composition by level, and the spread across the Bay Area market](/code/2026-10-28-cost-of-a-person/images/01-market-pay-by-level.png)

**Across the market**, levels.fyi reports a median of **$280,000** total comp for Bay Area software
engineers (n = 12,061). The quartiles are $206k and $384k, and the 90th percentile is $512k. The
90th percentile is **2.5×** the 25th for the same job title. Most of that width comes from level
rather than from company.

**By level**, the split between cash and stock matters more for cost. Cash falls from **81% of total
comp at L3 to 51% at L6**. The higher the level, the less of the package is subject to payroll tax
and the 401(k) match, and the more of it is a non-cash accounting expense.

> **One caveat applies throughout.** levels.fyi is self-reported. It skews toward large public
> employers and toward people who are satisfied enough with an offer to post it. These medians are
> closer to the upper half of the market than to its middle.

---

## 2 · Employer payroll taxes

A common estimate is that payroll tax runs about 7.65%, so a $241k engineer costs roughly $18k in
tax. That estimate is wrong in two directions, and the errors do not cancel.

![Employer payroll tax flattens at the cap, so it is regressive](/code/2026-10-28-cost-of-a-person/images/02-employer-payroll-taxes.png)

**Three of the five employer taxes are capped.** Two of them are capped very low.

- Social Security stops at **$184,500** of wages in 2026. Above that the 6.2% ends.
- California SUI and ETT apply only to the first **$7,000** of wages per employee per year. At the
  3.4% new-employer rate that is **$245 in total**. The figure is the same for a new grad and a
  Distinguished Engineer.
- FUTA also applies only to the first $7,000.

| Employer statutory cost | $100k cash | $241k cash | $500k cash |
|---|---|---|---|
| Social Security (6.2%, capped) | $10k | $11k | $11k |
| Medicare (1.45%, uncapped) | $2k | $6k | $12k |
| FUTA (CA credit reduction) | $126 | $126 | $126 |
| CA SUI | $238 | $238 | $238 |
| CA ETT | $7 | $7 | $7 |
| Workers' compensation | $400 | $964 | $2k |
| **Total** | **$13k** | **$18k** | **$25k** |

*(Assumes RSUs worth 60% of cash comp vest each year.)*

Employer payroll tax is about **7.4% of a $100k salary and under 5% of a $400k one**. It is
regressive.

**RSUs also carry a cash tax.** RSUs are W-2 wages when they vest, and the employer owes FICA on
them. Base salary has usually passed the Social Security cap by then, so the marginal rate is
Medicare's 1.45%. On a $176k annual grant that is **$2,552 a year**. It is a cash cost attached to a
non-cash benefit, and most models omit it. Medicare is the only uncapped employer tax.

---

## 3 · Benefits

Benefits fall into two groups. Treating them as one group is the second most common modelling error,
after the payroll-tax one.

![Annual employer cost of each benefit, and how the identical package is regressive](/code/2026-10-28-cost-of-a-person/images/03-benefits-menu.png)

**Flat-dollar benefits** cost about the same at every level: health, dental, vision, life,
disability, perks. A $16k medical bill is 11% of a $150k salary and 5.5% of a $290k one.

**Salary-linked benefits** scale, but not without limit. The 401(k) match is computed on
compensation capped at **$360,000** under IRC §401(a)(17).

The default package costs **$38,572 for an L5, or 16.0% of base**. Medical ($16,286) and the 401(k)
match ($10,421) are **69% of that**. Every other benefit combined costs less than medical alone. So
the benefits that read as generous are the cheap ones, and most of the money goes to two lines that
are not usually thought of as perks.

Two modelling choices worth stating:

- **The 401(k) match is set at about 80% of the promised rate.** Vanguard reports a mean promised
  match of 4.7% of pay. The employer pays it only when the employee defers enough to capture it.
- **Parental leave is amortised across the workforce** rather than charged in full to each hire. The
  calculation is 12 weeks × weekly salary × the roughly 8% of staff who take it in a given year.
  Charging every employee a full 12 weeks overstates the cost by more than 10×.

One California rule is often missed. Accrued, unused vacation must be paid out at termination here.
An accruing PTO balance is a growing balance-sheet liability, worth roughly 0.6% of salary a year.
Unlimited PTO removes the accrual. That is a real reason employers prefer it, and it is rarely
stated.

---

## 4 · Overhead

The largest item in this tier does not come up in compensation discussions at all.

![Recruiting is the biggest overhead line; remote removes about $12k a year](/code/2026-10-28-cost-of-a-person/images/04-overhead-stack.png)

**Recruiting.** A contingency agency fee for a Bay Area senior engineer is 18–30% of first-year base.
On a $241k salary that is about **$53,000**. Spread over the 3.5-year expected tenure it is
**$15,000 a year**, which is more than the medical bill. SHRM's mean cost-per-hire of $5,475 is the
internal-sourcing figure. It applies if you have a sourcing team and not otherwise.

**Office space.** SF asking rents were $70–73/sqft gross in Q3 2026. Vacancy was **29.3%**, so
effective rents after concessions are well below asking. At 175 sqft per person and a 0.8
desk-sharing ratio, space costs about $10k a year. Fully remote it is zero. That is the clearest
financial argument for remote work, and it weakens as the office market tightens.

**Tools and compute.** This line is easy to undercount: IDE, GitHub and Copilot, cloud dev
environments, observability, Slack, Atlassian, design seats, and a share of dev and staging
infrastructure. $11k combined is conservative for a current engineering org. Where engineers run
large training or inference jobs it can exceed the salary.

Totals come to **$39,825 a year** for a hybrid, agency-sourced L5. Internal sourcing brings that to
**$26,241**. Allocated management (Tier 6) would add $74,286 at a span of seven. It is shown
separately and left off by default: adding a 9th engineer to an 8-person team does not buy 1/7th of
a manager. Adding the 50th eventually does.

---

## 5 · Total cost

![Cost waterfall for one senior engineer for one year](/code/2026-10-28-cost-of-a-person/images/05-cost-waterfall.png)

```
Cash cost (tiers 1–4):          $375,036   =  1.56× base salary
Plus equity (GAAP, non-cash):   $551,036   =  2.29× base salary
Cash above base salary:         $134,036   not shown in the offer letter
```

The multiple is not fixed.

![The fully-loaded multiple falls as salary rises](/code/2026-10-28-cost-of-a-person/images/06-multiple-vs-salary.png)

It **falls as salary rises: 1.70× at $150k, 1.56× at $241k, 1.45× at $400k**. The reason is that the
two largest non-salary tiers, statutory tax and flat-dollar benefits, are both capped. A flat 1.4×
rule overstates the cost of junior hires and understates the cost of senior ones.

### Checking the model against BLS

```
BLS, professional occupations — insurance + retirement + legally required,
as a load on wages:                       25.6%   (national, all private industry)
This model, same three categories:        20.9%   (Bay Area, senior engineer)
```

The model sits **4.6 points below** the national benchmark. That is the expected direction and size.
The Social Security cap bites well below a senior engineer's salary, which pushes the model down.
Bay Area health plans and a 4.7% match push it up. A gap of 15 points or more would indicate a bug.

### How much benefit choices move the total

![The same engineer under four benefit packages](/code/2026-10-28-cost-of-a-person/images/07-package-comparison.png)

| Package | Cash cost | Equity (non-cash) | Allocated mgmt | Total | × base |
|---|---|---|---|---|---|
| Lean (statutory only) | $320k | $176k | $0 | $496k | 2.06× |
| Market (default) | $375k | $176k | $0 | $551k | 2.29× |
| Generous (big-tech) | $396k | $176k | $0 | $572k | 2.37× |
| Generous + allocated mgmt | $396k | $176k | $74k | $646k | 2.68× |

For the same person at the same salary, benefits and overhead choices move total cost by **1.30×**.
The gap between the lean and market packages alone is **$55,378 a year**.

---

## 6 · What equity costs the company

For equity, the employer's cost and the employee's benefit are different quantities in different
units.

- **The employer's cost** is GAAP stock-based compensation. It is grant-date fair value recognised
  over the vesting period. It is recorded whether or not the share price moves, and whether or not
  the employee stays past the cliff. It is non-cash for the company and dilutive for shareholders.
- **The employee's benefit** is a random variable. For public RSUs the distribution is narrow. For
  private options it is wide. The employee has to survive to the cliff, keep vesting, see the company
  reach liquidity, clear the strike price, and fund the exercise inside a 90-day window.

The filings give the employer's side precisely.

![Stock comp expense per employee, and as a share of revenue](/code/2026-10-28-cost-of-a-person/images/08-sbc-per-employee.png)

| Company | FY | SBC | Revenue | Employees | SBC/employee | Revenue/employee | SBC % of revenue |
|---|---|---|---|---|---|---|---|
| Meta | FY2025 | $20,430M | $200,970M | 78,865 | **$259k** | $2.55M | 10.2% |
| NVIDIA | FY2026 | $6,386M | $215,938M | 42,000 | $152k | $5.14M | 3.0% |
| Alphabet | FY2025 | $24,953M | $402,836M | 190,820 | $131k | $2.11M | 6.2% |
| Microsoft | FY2026 | $12,400M | $331,840M | 228,000 | $54k | $1.46M | 3.7% |
| Salesforce | FY2026 | $3,510M | $41,520M | 83,334 | **$42k** | $498k | 8.5% |

Stock comp per employee ranges from $42k to $259k across these filers. A round $100k is not a
reliable assumption in either direction.

---

## 7 · How much equity actually vests

An offer letter might say "$600,000 of equity over four years." Three conditions stand between that
sentence and money in a bank account. Only the first is under the employee's control.

1. **Do they stay?** Carta's data on 185,000+ startup employees puts median tenure at **2.0 years**.
   Cumulative departures reach 50% at **month 37**, inside a four-year vest. The one-year cliff is a
   step function. Leaving at month 11 yields nothing.
2. **Does the equity become worth anything?** For public RSUs, almost always. For private options the
   company has to reach liquidity. Carta's 2022 seed cohort reached Series A at **17%** within two
   years, down from 27.5% for the 2018 cohort. Shutdowns on Carta rose 25.6% between 2023 and 2024.
3. **Do they exercise?** The standard post-termination window is **90 days**. Secondary data puts the
   share who exercise within it at about **38%**. People leave, decline to pay the strike price and
   the resulting AMT bill, and the options lapse.

I simulated all three conditions across **200,000 employees per scenario**. Tenure is drawn from a
Weibull survival curve calibrated to each scenario's median. The vest fraction applies the cliff and
the quarterly schedule. The payoff uses a lognormal distribution around grant value for public RSUs
and a heavy-tailed, mostly-zero distribution for private options.

![Vesting simulation: the vest is a staircase, attrition is a slide](/code/2026-10-28-cost-of-a-person/images/09-vesting-simulation.png)

| Scenario | Reaches cliff | Fully vests | Mean fraction vested | **P(realise nothing)** | Median per $1 | Mean per $1 | P90 per $1 |
|---|---|---|---|---|---|---|---|
| Public megacap RSUs | 87.9% | 43.5% | 69.2% | 12.1% | **$0.74** | $0.92 | $1.90 |
| Late-stage private RSUs | 82.1% | 35.1% | 61.3% | **55.0%** | **$0.00** | $0.40 | $1.08 |
| Early-stage startup options | 74.4% | 25.7% | 51.9% | **95.2%** | **$0.00** | $0.04 | $0.00 |

The early-stage row is the one to read closely. The **mean** realised value is positive because of a
long right tail. The **median is zero**. Both facts are true at once. Quoting a candidate the face
value of a grant, or even its expected value, without the median and the probability of zero leaves
out the more likely outcome.

The schedule and the attrition curve also work against each other by design. Half of startup
employees have left by month 37, three months short of full vesting.

![A $704,000 equity grant is not a $704,000 benefit](/code/2026-10-28-cost-of-a-person/images/10-equity-cost-vs-value.png)

```
Public megacap RSUs      92% of accounting cost reaches the employee on average,  74% at the median
Late-stage private RSUs  40% of accounting cost reaches the employee on average,   0% at the median
Early-stage options       4% of accounting cost reaches the employee on average,   0% at the median
```

The gap is not waste. It is risk transfer. The employer converts a certain accounting cost into an
uncertain employee benefit and retains the forfeitures. Whether that trade favours the employee
depends on which row they are in.

---

## 8 · Margin of error

A figure like "$375,000" implies more precision than the model has. About a third of the inputs are
practitioner benchmarks with no published error bars.

So every uncertain input gets a distribution instead of a point estimate. Triangular distributions
are used where only a plausible low, likely and high can be stated. Normal distributions are used
where a survey publishes a mean over a large sample. Bernoulli distributions are used where the
input is a policy choice. The model then runs 40,000 draws.

![Two different questions, two very different error bars, plus a tornado chart](/code/2026-10-28-cost-of-a-person/images/11-uncertainty-bands.png)

The width of the answer depends on which question is being asked.

| Percentile | Band A — offer known | × base | Band B — budgeting a hire |
|---|---|---|---|
| P5 | $356,032 | 1.48× | $259,380 |
| P10 | $359,229 | 1.49× | $272,311 |
| P25 | $364,787 | 1.51× | $301,451 |
| **Median** | **$372,140** | **1.54×** | **$340,687** |
| P75 | $379,574 | 1.57× | $383,734 |
| P90 | $385,628 | 1.60× | $423,652 |
| P95 | $388,934 | 1.61× | $447,643 |

- **Band A: the offer is known.** The salary is settled and only the loading is uncertain. The 80%
  interval is $359,229–$385,628, or **±3.5%**. This is the question a finance partner asks when
  approving a req.
- **Band B: budgeting for a hire.** The level and negotiated salary are also unknown, drawn from a
  plausible Bay Area hiring mix. The 80% interval is $272,311–$423,652, or **±22.2%**. This is the
  question a founder asks when planning headcount.

Band B is six times wider than Band A. Once the salary is settled the loading is predictable to about
±4%. The largest source of uncertainty in what a hire will cost is the salary itself, not the
benefits model.

Ranking the individual inputs:

```
Biggest single input:   Agency vs internal sourcing   (swing $13,309)
Second:                 Cloud + dev infra             (swing $12,811)
Third:                  Work mode (office or not)     (swing $12,051)
Smallest:               FUTA rate (CA)                (swing $101) — not worth measuring
```

All three of the top inputs are policy choices rather than estimates. A sensitivity analysis over
continuous inputs alone would have missed them. Workers' comp, FUTA and the desk-sharing ratio are
noise at this scale.

---

## 9 · Revenue needed to break even

Cost is half the question. The filings give a benchmark for the other half.

![Revenue per employee from the filings, and breakeven by gross margin](/code/2026-10-28-cost-of-a-person/images/12-revenue-breakeven.png)

| Gross margin | Revenue needed (cash cost) | Revenue needed (incl. equity) |
|---|---|---|
| 35% | $1,071,533 | $1,574,390 |
| 50% | $750,073 | $1,102,073 |
| 65% | $576,979 | $847,748 |
| 80% | $468,795 | $688,795 |
| 90% | $416,707 | $612,263 |

At a 78% SaaS gross margin, one senior engineer has to be associated with **$706,457 of revenue** to
break even fully loaded. For comparison, Alphabet runs at $2.11M of revenue per employee, NVIDIA at
$5.14M and Salesforce at $498k.

That is a **10.3× spread** in revenue per head. Fully-loaded cost per head varies by well under 2×.
That asymmetry explains why the most productive companies can pay above market and still hold
margin. It also explains why a company at Salesforce's revenue per head cannot match Google's offer.

---

## 10 · Ramp and turnover

Two costs that rarely appear in a compensation budget.

![A new hire is under water for most of year one; annualised waste by departure point](/code/2026-10-28-cost-of-a-person/images/13-ramp-and-turnover.png)

**Ramp.** A mid-to-senior engineer takes roughly six months to reach full productivity in a real
codebase. That is six months of fully-loaded cost against partial output, plus the onboarding time
of the engineers around them.

**Replacement.** Practitioner benchmarks put the cost of replacing a technical employee at 0.5× to
2.0× salary. That covers recruiting again, the vacancy, the new person's ramp and the drag on the
team.

```
Year-one deficit on a single senior hire:   $94,540 before they have paid back their ramp
A hire who leaves at 18 months:             $244,529 per year of tenure
A hire who stays 4 years:                   $91,698 per year of tenure — 2.7× cheaper
```

The default benefits package costs $38,572 a year. An 18-month departure costs 5.9 years' worth of
it. Retention and benefits spending point in the same direction here, which is unusual in this
analysis.

---

## Findings

**1 · The multiple is about 1.56× in cash and 2.29× including equity, and it is not constant.** On a
$241k base that is $375k of cash cost and $551k all-in, including $134k of cash that is not in the
offer letter. The multiple falls from 1.70× at $150k to 1.45× at $400k.

**2 · Employer payroll tax is regressive and nearly flat above $185k.** California SUI and ETT stop
at $7,000 of wages, or $245 in total, regardless of level. Medicare is the only uncapped employer
tax, which is also why RSUs carry a cash cost.

**3 · Recruiting is the largest overhead line, ahead of health insurance.** About $15k a year
amortised, against roughly $16k for medical. The sourcing channel is also the largest single swing in
the sensitivity analysis. Measuring your own cost per hire matters more than refining anything else
in this model.

**4 · Benefits are flat in dollars, so they are regressive too.** About $38.6k at every level: 16% of
a new grad's base and 13% of a senior's. Medical and the 401(k) match are 69% of the total.

**5 · A $704,000 grant is not a $704,000 benefit.** For early-stage options the median outcome is
zero while the mean is positive. The expected value sits in a thin right tail. The gap between the
company's cost and the employee's benefit is risk transfer, and the employee holds the risk.

**6 · The attrition curve and a four-year vest are close to adversarial.** Half of startup employees
are gone by month 37. About 26% of early-stage employees reach the end of the schedule.

**7 · The margin of error depends on the question.** ±4% once the salary is settled, six times wider
before it is. The salary dominates, then the recruiting channel.

**8 · The first year is the expensive one.** A new senior hire is roughly $95k under water through
month 12. A departure at 18 months costs about $245k per year of tenure, against $92k for someone who
stays four years.

**9 · Cost per head varies much less than output per head.** Roughly 10× spread in revenue per
employee, under 2× in cost.

---

## What this model is not

- **Not a tax or legal opinion.** The 2026 California FUTA credit reduction is unsettled until the
  IRS notice lands in November 2026. Your actual SUI rate is experience-rated and will not be the
  3.4% new-employer rate. Confirm both with EDD and your payroll provider.
- **Not a market survey.** levels.fyi is self-reported and skews toward large public employers and
  toward people satisfied enough with an offer to post it.
- **Not a prediction about any individual.** The vesting simulation is a population model. It says
  nothing about a specific grant. The early-stage volatility parameter is a modelling choice, not a
  measurement.
- **Not auditable as GAAP.** Tier 5 approximates steady-state stock comp using the annualised grant
  value. Real expense recognition involves graded vesting, forfeiture estimates and mark-to-market on
  liability-classified awards.

---

## Sources

Every input is declared once, with a URL, an as-of date and a confidence tier. **A** is a primary
filing or government release. **B** is a large private dataset published by its owner. **C** is
secondary reporting or a practitioner benchmark. The tally is 6 Tier A, 14 Tier B and 2 Tier C. The
Tier C rows are the ones that drive the error bars in section 8.

**Tier A — primary filings and government releases**

- [BLS, Employer Costs for Employee Compensation, June 2026](https://www.bls.gov/news.release/pdf/ecec.pdf) (USDL-26-1494) — the calibration benchmark
- [SEC EDGAR XBRL company facts](https://www.sec.gov/edgar/searchedgar/companysearch) — stock-based compensation and revenue for Alphabet, Meta, NVIDIA, Microsoft, Salesforce
- [Meta FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm) — headcount
- IRS / SSA 2026 cost-of-living adjustments — wage bases and contribution limits

**Tier B — large datasets published by their owners**

- [levels.fyi — SF Bay Area software engineer salaries](https://www.levels.fyi/t/software-engineer/locations/san-francisco-bay-area) (n = 12,061) and the [Google by-level page](https://www.levels.fyi/companies/google/salaries/software-engineer/locations/san-francisco-bay-area)
- [KFF 2025 Employer Health Benefits Survey](https://www.kff.org/health-costs/2025-employer-health-benefits-survey/) — premiums and employer share
- [Carta — startup employment tenure](https://carta.com/data/employment-tenure-startups/) and [startup shutdowns](https://carta.com/data/startup-shutdowns-q1-2024/)
- Vanguard, *How America Saves 2025* — 401(k) match rates
- [Cushman & Wakefield SF Office MarketBeat Q3 2026](https://www.cushmanwakefield.com/en/united-states/insights/us-marketbeats/san-francisco-marketbeats/office) and Savills *Market in Minutes* Q3 2026 — office rents and vacancy
- [California EDD](https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/) — SUI, ETT, SDI
- SHRM 2025 Talent Acquisition Benchmarking (n = 2,371) — cost per hire

**Tier C — practitioner benchmarks, wide error bars.** Agency fee percentages, sqft per employee,
per-seat software and cloud spend, ancillary benefit costs, ramp time, replacement cost, and the 38%
option-exercise rate. These are the inputs the uncertainty analysis varies, and the tornado chart
shows which of them matter.
