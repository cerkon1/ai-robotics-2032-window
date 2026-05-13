# Cohort Map

Maps US labor cohorts to AI×robotics crossover years, with cost-vs-reliability bottleneck identification.

## Files

| File | Purpose |
|---|---|
| `cohort_map_us_occupations.csv` | 16 occupations across 5 cohorts. SOC code, headcount, wage, crossover analysis. |
| `cost_per_hour_robot_tiers.csv` | Fully-loaded robot $/hr by tier (commodity / target / initial / frontier / projected-2030). |
| `RESEARCH_NOTES.md` | Cohort-level analytical observations + the load-bearing insight. |

## Cohort definitions

| Cohort | Timing | Task profile | Bottleneck |
|---|---|---|---|
| **1 — Earliest (2026-2029)** | Warehouse / logistics / structured manufacturing / trucking | Structured, low-dexterity, predictable environment | Reliability (cost already crossed) |
| **2 — Mid (2029-2032)** | Cleaning / food prep / fast food / counter | Semi-structured, medium-dexterity | Reliability (cost at-parity) |
| **3 — Late (2032-2037)** | Skilled trades — electricians / plumbers / mechanics | Unstructured, high-dexterity, novel environments | Reliability + regulation |
| **4 — Demand-buffered (2034-2040+)** | Personal care / nursing assistants | Interpersonal-dominant, dignity-sensitive | Reliability + DEMAND GROWTH offsetting substitution |
| **5 — Augmented not replaced** | Knowledge work — managers / developers / professionals | Knowledge work | Productivity multiplier, not substitution |

## Schema

`cohort_map_us_occupations.csv` columns:

| Column | Meaning |
|---|---|
| cohort | 1-5 per definitions above |
| soc_code | BLS Standard Occupational Classification |
| us_employment_2024 | BLS OES May 2024 headcount (or estimate if not pulled) |
| median_annual_wage_usd_2024 | BLS OES May 2024 median |
| hourly_wage_equiv | Median annual / 2080 hours |
| task_structure / dexterity_required / environment_variability | Qualitative task profile inputs |
| cost_crossed_{commodity,target,initial} | true / false / at-parity — did the robot cost-tier cross this cohort's wage? |
| reliability_threshold_estimate | Year range when reliability is plausible for this occupation |
| crossover_year_estimate | Synthesized year — max(cost, reliability) since both must be met |
| bottleneck | cost / reliability / both / demand_growth_offsets / augmentation |

## The single most important finding

**For every cohort with a wage > $14/hr, the commodity humanoid cost ($2.65/hr fully-loaded) has ALREADY crossed the cost threshold.** The wage gate fell years ago. The binding constraint is reliability/dexterity at the task level — exactly the autonomous-vehicle "long testing tail" pattern from Leg 3.

This reframes the popular narrative:
- Popular: "Robots will get cheap enough to replace workers"
- Honest: "Robots are already cheap enough on paper. The question is whether they can do the job."

## Total US employment in displacement-path cohorts (1-4)

| Cohort | Estimated US headcount 2024 | Crossover window |
|---|---|---|
| 1 — Earliest | ~8.2M (warehouse + stockers + truckers + logisticians) | 2026-2029 |
| 2 — Mid | ~6.4M (fast food + janitors + cooks + food prep) | 2029-2032 |
| 3 — Late | ~2.1M (electricians + plumbers + mechanics) | 2032-2037 |
| 4 — Demand-buffered | ~5.7M (home aides + nursing assistants) | 2034-2040+ but demand growth dominates |
| **Total (1-3)** | **~16.7M jobs in the active substitution path** | by ~2035 |
| **Total (1-4)** | **~22.4M jobs in the broader exposure pool** | by ~2040 |

For comparison: US working-age population is 224M (2024) → 232M (2050) per UN WPP. Cohorts 1-3 = ~7% of working-age. Demographics ADD ~8M working-age over the same window — almost exactly offsetting cohort 1-3 displacement, IF the substitution proceeds on the bottom end of the timeline.

## The K-shape outcome — quantified

If cohort 1-3 ($16.7M jobs) earn aggregate wages of ~$700-800B/yr (rough estimate using cohort-weighted medians), and that wage flow is rerouted to capital owners via productivity gains from $650B/yr Mag7 capex deployment, **the wage-to-capital transfer is on the order of $700B+/yr by mid-2030s**. This is the K-shape made concrete. Section 2 should anchor this number.
