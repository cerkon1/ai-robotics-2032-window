# Leg 1 — AI capability/cost

Data series for the AI side of the convergence argument.

## Planned series

| File | Topic | Source(s) | Status |
|---|---|---|---|
| `notable_models_training_compute.csv` | Frontier model training compute scaling | LEG1_EPOCH_NOTABLE_2024 | Schema-demo populated (5 rows, unverified) |
| `metr_autonomy_doubling.csv` | Task-length doubling time (autonomy proxy) | LEG1_METR_AUTONOMY_2024 | Not yet pulled |
| `inference_cost_per_mtok.csv` | Inference $/Mtok by model + release date | LEG1_API_PRICING_HISTORY + LEG1_ARTIFICIAL_ANALYSIS | Not yet pulled |
| `benchmark_saturation.csv` | Multi-benchmark score by model + date (MMLU, GPQA, ARC-AGI, SWE-Bench) | LEG1_ARC_AGI + LEG1_GPQA + LEG1_SWEBENCH + AI Index | Not yet pulled |
| `ai_index_aggregate.csv` | Stanford AI Index headline metrics over time | LEG1_STANFORD_HAI_AIINDEX | Not yet pulled |

## Schema details

### `notable_models_training_compute.csv`

| Column | Type | Meaning |
|---|---|---|
| `source_id` | string | Row in `../../sources.md`. |
| `confidence` | enum | `high`/`medium`/`low`. |
| `verified` | bool | `true` once cross-checked against canonical source. |
| `model_id` | string | Slug, stable across releases (e.g., `gpt-4`, `claude-3-opus`). |
| `model_name` | string | Display name. |
| `release_date` | YYYY-MM-DD | First public availability. |
| `training_compute_flops` | scientific | Total training compute, in FLOPs. |
| `parameters` | scientific | Model parameter count (may be unknown/None for closed models). |
| `publisher` | string | Releasing organization. |
| `notes` | string | PENDING markers, estimate ranges, methodology notes. |

### `metr_autonomy_doubling.csv` (to come)

Anticipated schema: `date`, `task_horizon_minutes_50pct`, `task_horizon_minutes_80pct`, `model_id`, `source_id`, `confidence`, `verified`, `notes`.

### `inference_cost_per_mtok.csv` (to come)

Anticipated schema: `model_id`, `provider`, `price_date`, `input_per_mtok_usd`, `output_per_mtok_usd`, `source_id`, `confidence`, `verified`, `notes`.

---

## Verification protocol

For each row added:

1. Pull from primary source (Epoch AI CSV download, METR blog post HTML, provider pricing page).
2. Record `source_id`, `confidence`, set `verified: false`.
3. Cross-check value against a second source where possible (Stanford AI Index, paper citation, Wayback Machine snapshot).
4. Flip `verified: true` only when cross-check passes.
5. Add to `../../sources.md` with status `verified` and retrieval date.

Rows with `verified: false` cannot be used in a published draft.
