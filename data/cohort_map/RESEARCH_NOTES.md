# Cohort Map — Research Notes

**Last updated:** 2026-05-12
**Status:** Tier 1 cohort map complete. 16 occupations across 5 cohorts. Cost-vs-reliability crossover analysis baked in.

---

## The framework

The cohort map combines four inputs from prior legs:

1. **Cohort wage** (from BLS OES May 2024) — what the substitution threshold is
2. **Robot fully-loaded $/hr** (derived from Leg 2 pricing data) — what the cost curve is at each tier
3. **Reliability threshold per task class** (from Leg 1 capability data + Leg 3 AV analog) — when the robot can actually do the job
4. **Cohort year crossover** = MAX(cost_crossover_year, reliability_threshold_year)

For nearly every cohort in the substitution path, **the cost already crossed**. Reliability is the gate.

---

## The load-bearing insight

**For every cohort with a wage > $14/hr, the commodity humanoid ($13.5K Unitree G1, $2.65/hr fully-loaded) has ALREADY crossed the cost threshold.**

- Fast food worker: $16.23/hr — commodity humanoid is 6× cheaper
- Janitor: $17.27/hr — 6.5× cheaper
- Hand laborer: $18.10/hr — 6.8× cheaper
- Stocker: $15.85/hr — 6× cheaper
- Truck driver: $27.60/hr — 10× cheaper
- Electrician: $29.97/hr — 11× cheaper
- Home aide: $16.80/hr — 6.3× cheaper

This is not a forecast. It is the situation today. The robot hardware is cheap enough. **The reason 20 million American workers in these roles still have jobs is that current humanoids cannot do the work reliably at human-equivalent quality.**

The popular AI-displacement narrative says "robots will get cheap enough to replace workers." The honest narrative says: "Robots are already cheap enough. The question is can they do the job."

This is the load-bearing insight for Part 1.5 and Part 2.4 of the article.

---

## Cost-curve breakdown (`cost_per_hour_robot_tiers.csv`)

| Robot tier | Reference | $/hr fully-loaded | "Annual salary" equivalent |
|---|---|---|---|
| Commodity (today) | Unitree G1 $13.5K | **$2.65/hr** | $5,300/yr equivalent |
| Target (per company guidance) | Tesla Optimus <$30K | **$6.00/hr** | $12,000/yr |
| Initial commercial | Tesla / Figure / Apptronik $100K | **$15.00/hr** | $30,000/yr |
| Frontier (current build) | Mid-range $75K | **$26.67/hr** | $53,000/yr |
| Projected 2030 | $15K + 10hr/day + 7yr depreciation | **$2.06/hr** | $4,100/yr |

Methodology: capex / (depreciation_years × annual_hours) + ~30% maintenance + ~50% overhead.

The cost curve crashes through the wage floor in 2026-2028 for commodity humanoids — but commodity humanoids can only do commodity tasks. The frontier humanoids (which can do MORE) are at $15-27/hr today.

The cost-curve crosses skilled-trades wage levels (~$30/hr) only at the frontier tier today, but by 2030 the same capability at the commodity tier becomes cost-feasible. **Cost ceases to be the binding constraint for ALL cohorts somewhere between 2028 and 2032.**

---

## Cohort-by-cohort analysis

### Cohort 1 — Earliest (2026-2029): ~8.2M US jobs

Warehouse / stockers / hand laborers / logisticians / truckers.

- Wages cluster $15-28/hr
- Tasks: structured, repetitive, low-dexterity, predictable environment
- Cost: crossed at all robot tiers
- Reliability: Amazon / Walmart Symbotic / Digit already deployed (testing → commercial transitions in progress)
- Trucking is special: AV trucking has its own long testing tail; commercial deployment in ~12 states 2025-2028 expected
- **Crossover window: 2026-2029 for in-warehouse; 2028-2032 for long-haul trucking**

### Cohort 2 — Mid (2029-2032): ~6.4M US jobs

Fast food / janitors / cooks / food prep.

- Wages cluster $15-17/hr — cost crossed
- Tasks: semi-structured, medium-dexterity, variable environments
- Reliability gate is real (sanitation, food safety, customer interaction)
- BMW Spartanburg (Figure) + Mercedes (Apptronik) pilots demonstrate the path
- **Crossover window: 2029-2032 for high-routine; 2030-2033 for full-menu kitchens**

### Cohort 3 — Late (2032-2037): ~2.1M US jobs

Skilled trades — electricians / plumbers / mechanics.

- Wages $24-30/hr — initial-commercial tier crosses cost; commodity comfortably so
- Tasks: unstructured, high-dexterity, novel environments (legacy buildings, varied tools)
- Safety-critical → regulation-bottlenecked
- New-construction can automate earlier (~2030); legacy work much later
- **Crossover window: 2033-2037 with regulatory uncertainty extending the tail**

### Cohort 4 — Demand-buffered (2034-2040+): ~5.7M US jobs

Personal care / nursing assistants.

- Wages $17-20/hr — cost crossed
- Tasks: interpersonal-dominant, dignity-sensitive
- **Demographic counter-pressure dominates here.** US population aged 65+ projected to grow from ~58M (2024) to ~82M (2050). This cohort's labor demand grows ~17%/decade per BLS. Robots SUPPLEMENT rather than replace.
- This is the cleanest example of the article's "robots fill jobs we can't staff" framing.
- **No clean crossover year. Instead: gradual augmentation through 2035+.**

### Cohort 5 — Augmented not replaced

Knowledge workers — managers, developers, professionals.

- AI is productivity multiplier, not headcount substitute (at first)
- METR autonomy data points to direct partial-displacement risk for routine knowledge work by 2028-2030 (12 hours of expert-equivalent task work TODAY)
- But: managers, designers, judgment-heavy roles persist as augmentation beneficiaries
- This is where the K-shape's UP arm lives — workers who effectively use AI tools become hyper-productive; those who don't see wage stagnation

---

## The total exposure picture

| Cohort | US headcount | Wage exposure (rough est.) | Crossover window |
|---|---|---|---|
| 1 — Earliest | 8.2M | ~$330B/yr | 2026-2029 |
| 2 — Mid | 6.4M | ~$220B/yr | 2029-2032 |
| 3 — Late trades | 2.1M | ~$140B/yr | 2033-2037 |
| 4 — Demand-buffered | 5.7M | ~$200B/yr | 2034-2040+ but demand growth offsets |
| **Total in substitution path (1-3)** | **16.7M** | **~$690B/yr** | **by 2035** |
| Total in broader exposure (1-4) | 22.4M | ~$890B/yr | by 2040 |

**$690B/yr in wages is the rough magnitude of labor income at stake in cohorts 1-3 by 2035.** That number is in the same order of magnitude as the Mag7 2026 AI capex ($650B). The financing and the displacement are matched scales — capital is going IN at roughly the rate that labor income is at risk going OUT.

This is the K-shape made concrete: dollars flowing from wage-earners to capital-owners on the order of hundreds of billions per year by mid-2030s.

---

## How the cohort map informs falsifiable checkpoints (next task)

For each cohort, the article can commit to specific predictions:

- **2026 checkpoints (testing for Cohort 1):**
  - At least one US warehouse operator deploys >5,000 humanoids in routine ops
  - Truck drivers SOC employment plateau or decline (currently +4% projected — if this turns)

- **2028 checkpoints (commercial for Cohort 1):**
  - First cost-per-task crossover documented at the full-loaded level in a published case study
  - Total US warehouse/stocker employment shows YoY decline for first time

- **2030 checkpoints (testing for Cohort 2):**
  - First commercial humanoid deployment in fast-food chain or commercial cleaning >10K units
  - China robot density crosses 250/10K manufacturing employees

- **2032 checkpoints (commercial for Cohort 2 / testing for Cohort 3):**
  - Cohort 1-2 combined employment down 5% from 2024 baseline
  - First skilled-trades humanoid pilot announcements

- **2035 checkpoints (full convergence):**
  - All four metrics (cost-per-task / robot density / labor share / capex) confirm or refute crossover
  - Cohort 1-2 combined employment down 15-25% from 2024 baseline

---

## What's NOT yet in the cohort map (Tier 2)

- China occupational mirror — what do NBS labor data say about Chinese workforce composition? Important for the China-deployment-leads-the-world thread.
- EU occupational mirror — Eurostat data on labor cohorts in Germany/France/Italy for the EU-regulation slow-deployment scenario.
- Wage data for plumbers, food prep workers, packers — current rows have BLS-inferred estimates rather than verified counts. Tier 2 should pull these specifically.
- Geographic concentration within US — which states / metros have the highest Cohort 1-2 exposure? Useful for the K-shape geographic flavor.

These are not blocking on the draft. They are refinement work.

---

## Source-tracker update

In `sources.md`, add LEG3_BLS_OES as a new source row covering BLS May 2024 OES data accessed via search aggregation (BLS HTML pages blocked from this environment).
