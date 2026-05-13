# Methodology

Rules for how data is collected, normalized, projected, and presented. Written before any data is pulled so the discipline is fixed in advance.

**Principle:** A reader should be able to disagree with the article from the same starting point. That requires showing the data, the transformations, and the projections — all reproducible.

---

## 1. Data collection

1. **Primary source preferred.** Always pull from the original publisher (Epoch AI's CSV, BLS OES, SEC EDGAR 10-K) when available. Secondary citations only when the primary is paywalled or unavailable.
2. **Retrieval date logged.** Every series in `sources.md` has its retrieval date. Re-pull older than 6 months requires a re-verification pass.
3. **Raw data preserved.** Original CSV/PDF/JSON saved into the leg's folder. Any cleanup happens in a separate `*_clean.csv` with a `*_README.md` documenting the transformation.
4. **No silent imputation.** Missing values stay missing (or are explicitly imputed with documented method). Never fill a gap silently.

---

## 2. Normalization

Across legs, data lives in different units and time bases. Normalization rules:

1. **Common date axis: annual** (calendar year) unless quarterly data is essential. Monthly compressed to annual via end-of-period or average — documented per series.
2. **Currency: nominal USD 2025** (i.e., headline numbers, not real). Real-USD comparisons computed separately when needed (CPI deflator from FRED).
3. **Units: as published.** Don't unit-convert silently. If a paper reports FLOPs and another reports MMLU score, those don't get normalized — they live in their own series.
4. **Indexed series** (e.g., capability index, cost index) are only constructed when triangulating downstream metrics. The index construction is documented in a per-series README.

---

## 3. Projection rules

The thesis is forward-looking. Projection methodology must be defensible against the "naive exponential extrapolation" critique.

### 3.1 Default: constraint-clipped S-curve

Each forward series is projected as a logistic / S-curve, NOT a naive exponential, unless the constraints have been explicitly enumerated and shown to be non-binding in the projection window.

S-curve parameters:
- **Lower asymptote:** current measured level
- **Upper asymptote:** the binding constraint (manufacturing capacity, grid capacity, market saturation, etc.)
- **Inflection:** estimated from input-curve doubling time + constraint lead time

### 3.2 Show both: unconstrained and constrained

For every forward chart, plot the naive exponential extrapolation as a dashed line and the constraint-clipped projection as a solid line. The gap between them is the article's central visual argument.

### 3.3 Time horizon

Projections cap at 2035 unless explicitly extended. Beyond 2035 the article is no longer making claims.

### 3.4 No point estimates without ranges

"Crossover in 2032" is not allowed without a range like "crossover in 2030-2034 under moderate assumptions; 2028-2031 under aggressive assumptions; 2033-2036 under constrained assumptions." Show the sensitivity.

---

## 4. The Leg 3 "derived not measured" disclosure

Leg 3 in the original thesis (the marriage of AI and robotics at scale) has no clean measured series. The article handles this honestly:

- Leg 3 was renamed and refocused as the **execution layer** — observable constraints (grid, manufacturing, reliability, demographics, regulation), not deployment data.
- The intersection of Legs 1 and 2 is derived from input curves, not directly observed.
- The article states this explicitly in §1.2, in a sentence the reader will see, not buried in an appendix.

---

## 5. Cohort sizing

Labor cohort sizing (§1.4 cohort map) uses BLS OES for US, NBS for China.

- Cohort buckets are defined by SOC (Standard Occupational Classification) codes or equivalent
- Each cohort's headcount, median wage, and automation-exposure score are listed
- "First to be affected" claims are pegged to specific SOC codes, not vague labels

---

## 6. Falsifiable checkpoints

§1.5 commits to specific predictions. Each checkpoint must be:

1. **Specific** — a threshold value, not "significant progress"
2. **Trackable** — tied to a publicly published metric
3. **Dated** — by month/year, not "by the late 2020s"
4. **Pre-registered** — in the article itself, not in a later post

The article ends with a revisit date (proposed: 12 months post-publication). A follow-up post scores the predictions.

---

## 7. Visual standards

- Every chart cites its source in the caption ("Data: Epoch AI Notable Models DB, retrieved 2026-MM-DD")
- Every chart has a link to the raw CSV in the article's data appendix
- Color use is consistent across the series (Leg 1 = blue family, Leg 2 = green family, Leg 3 = amber/red constraint family, Macro = neutral grey)
- Projections vs measured data are visually distinct (solid line = measured; dashed = projection)

---

## 8. Counterargument handling

For every load-bearing claim, the strongest counterargument is acknowledged in the article body — not relegated to a footnote.

Examples:
- AI capability extrapolation: "Critics including Subbarao Kambhampati and Yann LeCun argue current scaling laws plateau before AGI..."
- Robot cost trajectory: "Boston Consulting / others argue total cost of ownership remains 3-5× hardware cost..."
- BTC as scarce asset: "BTC's monetary properties are still being tested; volatility, regulatory risk, and custody risk are real..."

This is not balance for balance's sake. It is acknowledging that the thesis could be wrong, and naming where.

---

## 9. What disqualifies a source

- Vendor-published forecasts treated as data (bank TAM reports, consulting white papers)
- Anonymous or unattributed estimates
- Numbers that can't be traced to a primary publication
- Data behind a paywall we don't have access to (unless a public summary is sufficient)

These can appear in the article as commentary ("Goldman forecasts $X TAM") but never as data points in a chart.

---

## 10. Pruning rule

If, after data collection, a leg or sub-axis can't be defended at the standard set above, it gets pruned from the article. A 2-leg article with a strong execution-layer chapter is better than a 3-leg article with a weak third leg.

---

## 11. Operational decisions (locked-in)

These data-handling decisions are fixed and apply to all charts in the article. Locked in to avoid drift across sessions.

### 11.1 Closed-model compute handling
Models with no publisher-disclosed training compute (GPT-4 / GPT-4o / Claude 3 Opus / Claude 3.5+ / Gemini etc.) are included in charts using Epoch AI's `Speculative` or `Likely` estimates. Required treatment:
- **Visual confidence tier marker** on every closed-model data point (e.g., open circle for Speculative, half-filled for Likely, filled for Confident).
- **Explicit error bars** for any Speculative/Likely value where Epoch provides a range; otherwise a visual "uncertainty halo" matching the tier.
- Legend explains the tier-to-marker mapping.
- Locked 2026-05-12.

### 11.2 METR autonomy chart — p50 lead, p80 overlay
The Section 1 autonomy chart uses METR's p50 horizon (50% success threshold) as the primary series — this matches METR's published headline doubling-time figure. p80 (80% threshold) is overlaid as a fainter secondary series. The 2023-onward acceleration (128.7-day doubling vs 187.8-day all-time) is the lead finding, not the all-time figure.
- Locked 2026-05-12.

### 11.3 Data-freeze cutoff
**Cutoff date: 2026-04-30.** Models, releases, and reports published after this date are NOT included in the article's charts and analysis. Any post-cutoff developments are noted in a final "post-freeze update" footnote but do not change the projections.
- Why a freeze: prevents the article's analysis from drifting as drafts iterate.
- Re-freeze rule: if a draft cycle extends past 2026-08-31, the freeze date moves forward to 2026-07-31 (always one full month back from current).
- Locked 2026-05-12.

---

**Last updated:** 2026-05-12 (added §11 operational decisions)
