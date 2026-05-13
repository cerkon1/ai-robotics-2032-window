# Falsifiable Checkpoints

The article commits to specific predictions readers can verify on a published timeline. This folder is the canonical commitment list.

## Files

| File | Purpose |
|---|---|
| `falsifiable_checkpoints.csv` | 35 specific predictions with thresholds, dates, sources, and direction. |
| `RESEARCH_NOTES.md` | Prediction methodology + how to interpret success/failure. |

## Why falsifiability matters

Most "AI is coming" Substack pundits make vague claims that age into either "obvious in hindsight" or "wrong but unmemorable" without specific accountability. This article takes the opposite stance: **make specific predictions that a reader in 2028 / 2030 / 2032 can check**, then publish the scoring follow-up.

The article ends with the revisit date. A follow-up post ~12 months later scores the predictions.

## Structure

5 horizons, each with their own verification window:

| Horizon | Verify by | Number of checkpoints | Purpose |
|---|---|---|---|
| 2026 | Dec 31 2026 | 8 | Short-term acceleration signals (12-month follow-up window) |
| 2028 | Dec 31 2028 | 7 | First-inflection signals (Cohort 1 displacement begins) |
| 2030 | Dec 31 2030 | 9 | Mid-thesis signals (deployment scale + visible labor effects) |
| 2032 | Dec 31 2032 | 4 | Lower-bound thesis confirmation |
| 2035 | Dec 31 2035 | 4 | Upper-bound thesis confirmation |
| Failure | various | 5 | Explicit FAILURE criteria — what would prove the thesis wrong |

## Schema

| Column | Meaning |
|---|---|
| `checkpoint_id` | Stable identifier (CP_YYYY_NN). |
| `verify_by_date` | Date by which the metric should reach threshold. |
| `domain` | ai_capability / capex / manufacturing / robotics / grid / money / reliability / cohort / fiscal / labor_share / demographics |
| `metric` | The specific measure |
| `threshold_value` | Numeric trigger |
| `unit` | Unit of the value |
| `verification_source` | Where to check |
| `thesis_supports` | Which thesis claim this prediction backstops |
| `direction` | exceeds / below / equals — which direction confirms |
| `confidence_today` | high / medium / low — our confidence the prediction will land |
| `notes` | Methodology + rationale |

## Methodology rules

1. **Each prediction has a specific numeric threshold.** "Significant growth" is not allowed. "Exceeds 24 hours" is.
2. **Each prediction has a single canonical source for verification.** No reader-decides-which-source ambiguity.
3. **Each prediction has a specific date.** December 31 of the year, unless otherwise noted.
4. **Conservative thresholds.** Predictions are set at the LOWER bound of what our data implies. If the cohort/Goldman/IEA forecasts predict $1.6T AI capex by 2031, the article should predict $1.3T by 2032 — beat the conservative bar.
5. **Failure criteria are explicit.** Five CP_2035_FAIL_NN rows define what would invalidate the thesis. If any FAIL criterion triggers before its date, the article was wrong about a load-bearing claim and the author commits to publishing the retraction.
6. **High/medium/low confidence flagged.** Where data is strong (METR doubling, Mag7 capex), confidence is high. Where data is weak (precise Cohort 1 displacement timing), confidence is low — and the prediction should be more conservative.

## Reading the success predictions

8 of 32 success-direction predictions are flagged `confidence: high`. These are the load-bearing claims:
- METR p50 horizon exceeds 24 hr by end-2026 (already on trajectory)
- US debt-to-GDP exceeds 110% by 2030 (CBO baseline)
- US debt-to-GDP exceeds 118% by 2035 (CBO baseline)
- China working-age population below 970M by 2030 (UN WPP)
- South Korea working-age below 32M by 2032 (UN WPP)
- China share of humanoid manufacturing >80% by 2028
- US grid queue capacity >1,800 GW by 2028
- Mag7 aggregate capex >$600B by 2026 (already analyst-aggregated)

These are the bets the article can stand on. Lower-confidence predictions hedge directionally without staking the thesis.

## Reading the failure predictions

The 5 failure rows are the article's intellectual-honesty commitment. If any fire:

| Failure | What it would prove |
|---|---|
| FAIL_01: METR no improvement 12 mo | AI capability acceleration thesis is wrong |
| FAIL_02: Humanoid <500K by 2030 | Manufacturing ramp is materially behind |
| FAIL_03: Cohort 1 employment GROWING by 2032 | Substitution thesis is wrong |
| FAIL_04: Mag7 capex declines >10% YoY | Financing wall hit |
| FAIL_05: Grid constraint breakthrough | Bottleneck shifts substantially earlier |

The article should commit, in print, to publishing a retraction if any of these trigger.

## How this section appears in the article

Part 1.5 of the article carries a condensed version: roughly 8-12 checkpoints across 2026 / 2028 / 2030 / 2032 / 2035, in a single table. The full 35-row CSV is the data appendix.
