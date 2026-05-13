# Checkpoints — Research Notes

**Last updated:** 2026-05-12
**Status:** 35 checkpoints committed (30 success-direction + 5 failure-criteria). Ready for article integration.

---

## The prediction architecture

Every checkpoint is derived from data already in the article (Legs 1-4 + cohort map). The article's analytical chain is:

```
Raw data (Legs 1-4)
   ↓
Constraint-clipped projections (methodology §3)
   ↓
Cohort map (when does each labor group cross)
   ↓
Falsifiable checkpoints (specific dates × metrics × thresholds)
   ↓
Retrospective scoring (12 months post-publication, then annually)
```

No checkpoint is asserted without a data source already pulled into the article. The CSV's `verification_source` column maps each prediction to its check.

---

## Confidence tier breakdown

**8 of 32 success-direction predictions are `confidence: high`.** These are the article's load-bearing bets:

| ID | Prediction | Why high confidence |
|---|---|---|
| CP_2026_01 | METR p50 > 24 hr by end-2026 | Already at 17.4 hr Feb 2026; 4.2-month doubling makes this trivial |
| CP_2026_05 | Grid wait > 4.5 yr by end-2026 | Queue depth growing; LBNL data already shows 4+ yr |
| CP_2028_05 | Grid queue > 1,800 GW by 2028 | Net additions ~100-150 GW/yr; current 1,400 GW |
| CP_2028_07 | China >80% humanoid manufacturing share through 2028 | Currently ~90%; gradual decline plausible but stays well above 80% |
| CP_2030_06 | US debt-to-GDP > 110% by 2030 | CBO baseline projection |
| CP_2030_08 | China working-age < 970M by 2030 | UN WPP medium-scenario projection |
| CP_2032_03 | South Korea working-age < 32M by 2032 | UN WPP medium-scenario projection |
| CP_2035_02 | US debt-to-GDP > 118% by 2035 | CBO baseline projection |

If any of these miss, something material has changed in the underlying data — which means the methodology was wrong, not just the prediction.

**11 of 32 success-direction predictions are `confidence: medium`.** These bet directionally with conservative thresholds. Reasonably defensible.

**13 of 32 are `confidence: low`.** These are exploratory commitments. Worth making for accountability but readers should weight them less.

---

## The failure-criteria design

Five FAIL_NN rows define what would prove the thesis materially wrong. Each picks a specific failure mode:

| Failure | Tests this claim |
|---|---|
| FAIL_01 | AI capability acceleration continues (Leg 1 doubling) |
| FAIL_02 | Manufacturing ramp arrives on the forecast path (Leg 2 BofA path) |
| FAIL_03 | Cohorts actually start displacing (Leg 3 reliability threshold + cohort map) |
| FAIL_04 | Capital is willing to keep funding the buildout (Leg 4 Mag7 capex) |
| FAIL_05 | Grid constraint doesn't get magically solved (Leg 3 C1) |

**The article should commit in print: if any FAIL_NN triggers, I will publish a retraction post within 60 days.** This is intellectual-honesty discipline that 99% of pundit forecasts skip.

The FAIL_05 row is interesting because it's a "change criterion" not a "thesis wrong" criterion. If a major grid-easing breakthrough hits scale, the timeline doesn't disprove the thesis — it shortens it. That's a useful asymmetry.

---

## Mapping checkpoints to article sections

| Section | Relevant checkpoints |
|---|---|
| Part 1.5 (the 2028-2035 window with checkpoints) | All 35 checkpoints — condensed to 8-12 in body, full table in appendix |
| Part 2.1-2.2 (capital allocation + financing) | CP_2026_02, CP_2028_04, CP_2030_06, CP_2032_04, CP_2035_02 |
| Part 2.3 (K-shape) | CP_2030_05, CP_2030_07, CP_2032_02, CP_2035_01, CP_2035_04 |
| Part 3 (positioning) | The COHORT-LEVEL failure criteria (CP_FAIL_03) — useful for "where you sit on the cohort map matters" |

---

## What this section actually looks like in the article

The article body (Part 1.5) carries the predictions in narrative + a single condensed table. Roughly:

> **What I expect to see by the time I revisit this article. If I'm wrong, I'll say so.**
>
> *By end of 2026:* The frontier AI model exceeds 24 hours of human-equivalent task autonomy [METR]. Mag7 aggregate capex exceeds $600B [10-K filings]. US grid wait times push past 4.5 years [LBNL]. China industrial robot installs exceed 320K [IFR]. At least one humanoid manufacturer ships 25K+ units [IFR + company disclosures].
>
> *By end of 2028:* METR autonomy crosses 1 week per task. Mag7 cumulative AI capex 2023-2028 exceeds $2.5 trillion. US grid queue exceeds 1,800 GW. **First YoY decline in Cohort 1 US employment (warehouse + stockers + truckers).**
>
> *By end of 2030:* Global data center electricity > 900 TWh. Humanoid annual shipments > 1M units. Cohort 1 US employment down 5%+ from 2024. US debt-to-GDP > 110%. Labor share of GDP down >1.5 percentage points from 2024.
>
> *By end of 2032:* Cohort 1 down 12%+. First skilled-trades commercial humanoid deployment >5K units. South Korea working-age below 32M. AI capex on Goldman path > $1.3T.
>
> *By end of 2035:* Cohort 1+2 combined employment down 15-25%. US debt-to-GDP exceeds 1946 WWII record (118%). Global data center electricity 1,200 TWh. Labor share down ≥3pp.
>
> **What would prove me wrong:**
> - METR task-horizon shows 12+ consecutive months of no SOTA improvement before 2032
> - 2030 humanoid shipments come in below 500K (half the BofA forecast)
> - Cohort 1 US employment is HIGHER in 2032 than 2024
> - Mag7 capex declines >10% YoY in any year
> - A grid-easing breakthrough (modular reactor, superconducting transmission at scale) hits commercial scale before 2030
>
> *I will revisit this list in May 2027 and score myself. If any failure criterion triggers, I will publish a retraction within 60 days of the data becoming public.*

---

## What we now have at end-of-research

| Component | Status | Volume |
|---|---|---|
| Thesis | Locked | 1 paragraph + outline |
| Methodology | Locked | 11 sections incl. operational decisions |
| Sources tracker | 30+ sources, mix pulled/proposed | Master discipline doc |
| Leg 1 (AI capability/cost) | Tier 1 done | 4 files, 2 PDFs |
| Leg 2 (robotics deployment/cost) | Tier 1 done | 5 files, 1 PDF |
| Leg 3 (execution layer) | Tier 1 done | 7 files, 3 PDFs |
| Leg 4 (macro forces) | Tier 1 done | 5 files |
| Cohort map | Done | 3 files (16 occupations + cost tiers + analysis) |
| Falsifiable checkpoints | Done | 3 files (35 predictions across 5 horizons + 5 failure criteria) |

**The data scaffolding is complete enough to draft Part 1.** Tier 2 verification items become pre-publish refinement.
