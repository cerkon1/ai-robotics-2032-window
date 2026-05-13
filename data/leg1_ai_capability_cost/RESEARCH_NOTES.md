# Leg 1 — Research Notes

**Last updated:** 2026-05-12
**Status:** Tier 1 pulled (Epoch + METR + Stanford AI Index PDF); Tier 2 (inference cost, benchmark saturation) outstanding.

---

## What's been pulled

### 1. Epoch AI Notable AI Models database

- **Raw:** `epoch_notable_ai_models_raw.csv` (2.17 MB, 1,016 model rows, 47 columns, latest entry 2026-04-24)
- **Cleaned:** `epoch_frontier_post2017.csv` (28.8 KB, 165 rows post-2017 with frontier flag OR ≥1e23 FLOP training compute)
- **Source URL:** https://epoch.ai/data/notable_ai_models.csv
- **Updated by Epoch:** 2026-05-07 (yesterday relative to retrieval)
- **License:** CC BY 4.0 — free use with attribution
- **Citation format:** "Epoch AI, 'Data on AI Models'. Published online at epoch.ai"
- **Methodology docs:** https://epoch.ai/data/ai-models-documentation

**Inclusion criteria** (any one of):
- Highly cited (>5,000 citations), OR
- High training cost (>$1M in 2023 USD, or ≥1% of most expensive model to date), OR
- Significant use (>1M MAU), OR
- State-of-the-art on recognized benchmarks at release, OR
- Historical significance, OR
- Discretionary inclusion (cost-efficiency leaders etc.)

**Confidence tier distribution** (full dataset):
- Confident: 457
- Likely: 211
- Unknown: 182
- Speculative: 91
- Blank: 75

**Year distribution** (full dataset): 1950 → 2026, sparse before 2006, takeoff 2017+.

**Post-2017 frontier subset (165 rows) year distribution:**
- 2017: 3 · 2018: 1 · 2019: 10 · 2020: 4 · 2021: 9 · 2022: 21 · 2023: 28 · 2024: 48 · 2025: 37 · 2026: 4

### 2. METR autonomy horizon benchmark (METR-Horizon-v1.1)

- **Raw:** `metr_benchmark_results_raw.yaml` (16 KB, 541 lines)
- **Cleaned:** `metr_autonomy_horizons.csv` (4 KB, 26 model rows from gpt2 [2019-02-14] to claude_mythos_preview_early [latest])
- **Source URL:** https://metr.org/assets/benchmark_results_1_1.yaml
- **Reference paper:** https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
- **Repo:** https://github.com/METR/eval-analysis-public

**Headline doubling times (from the YAML's own top-level fields):**
- All-time stitched (2019-2026): **187.8 days** point estimate (~6.2 months)
- From 2023 onward: **128.7 days** point estimate, CI [104.4, 158.0] (~4.2 months, CI 3.4-5.2 months)

**This is the most arresting data point for Section 1.** The doubling is *accelerating*, not constant. The earlier "7-month doubling" headline from METR's 2025 paper is the all-time figure; the 2023-onward figure is meaningfully faster.

**Methodology:** Task horizon at success threshold X is the time a human expert would need for tasks the model completes with success probability X. p50 = 50% success threshold; p80 = 80% threshold (the harder bar).

**Capability progression (full series, p50 horizon in minutes):**

| Date | Model | p50 (min) |
|---|---|---|
| 2019-02-14 | GPT-2 | 0.05 |
| 2020-05-28 | davinci-002 (GPT-3 family) | 0.14 |
| (later GPT-3.5) | gpt-3.5-turbo-instruct | 0.60 |
| 2023-03 | GPT-4 | 3.99 |
| 2024-04 | GPT-4 Turbo | 3.73 |
| 2024-03-04 | Claude 3 Opus | 3.95 |
| 2024-05 | GPT-4o | 6.99 |
| 2024-06-20 | Claude 3.5 Sonnet | 11.40 |
| 2024-09 | o1-preview | 20.33 |
| 2024-10-22 | Claude 3.5 Sonnet (Oct) | 20.52 |
| 2024-12 | o1 | 38.83 |
| 2025-02-24 | Claude 3.7 Sonnet | 60.39 |
| 2025-04 | o3 | 119.73 |
| 2025-05-22 | Claude 4 Opus | 100.37 |
| 2025-08-05 | Claude 4.1 Opus | 100.47 |
| 2025-08-07 | GPT-5 | 203.01 |
| 2025-11-18 | Gemini 3 Pro | 224.33 |
| 2025-11-? | GPT-5.1 Codex Max | 223.71 |
| 2025-11-24 | Claude Opus 4.5 | 292.99 |
| (late 2025) | GPT-5.2 | 352.25 |
| 2026-02-05 | Claude Opus 4.6 | 718.81 (~12 hr) |
| 2026-02-05 | GPT-5.3 Codex | 349.53 |
| 2026-02-19 | Gemini 3.1 Pro | 384.15 |
| (latest) | GPT-5.4 | 341.74 |
| (latest) | Claude Mythos preview | 1044.78 (~17.4 hr) |

**Span:** 0.05 min (2019) → 1044 min (2026) = ~21,000× over 7 years.

### 3. Stanford HAI AI Index Report 2025

- **PDF:** `hai_ai_index_2025.pdf` (30.3 MB) — 8th annual edition
- **Source URL:** https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf
- **Page:** https://hai.stanford.edu/ai-index/2025-ai-index-report
- **Structured data (Kaggle):** https://www.kaggle.com/datasets/paultimothymooney/ai-index-report-2025

Topics covered (per the publisher's overview):
- AI hardware landscape and trends
- Inference cost estimates (new in 2025 edition)
- Publication and patenting trends
- Corporate responsible-AI practices
- AI in science and medicine
- Training cost trends for frontier models
- Investment / capex

**Status:** PDF preserved. Specific quantitative claims pending extraction (will use targeted page reads for the figures we cite). Kaggle CSV variant pending pull as a cross-check.

Note: a 2026 edition is also published (https://hai.stanford.edu/ai-index/2026-ai-index-report). To be pulled in a follow-up if cited.

---

## What's NOT yet pulled (Tier 2)

| Source | What it covers | Effort estimate |
|---|---|---|
| LEG1_API_PRICING_HISTORY | Inference cost ($/Mtok) trajectory 2020-2026 across OpenAI/Anthropic/Google models | 1-2 hr (Wayback Machine snapshots + manual aggregation) |
| LEG1_ARTIFICIAL_ANALYSIS | Multi-model price/performance current snapshot | 30 min |
| LEG1_ARC_AGI | ARC-AGI saturation leaderboard | 30 min |
| LEG1_GPQA | GPQA scores by model + date | 30 min |
| LEG1_SWEBENCH | SWE-Bench Verified leaderboard | 30 min |

**Recommendation:** pull these in a focused Tier 2 wave so Section 1's "benchmark saturation" sub-claim has matching data, but they're not blockers for starting on Leg 2 (robotics).

---

## Initial analytical observations (pre-chart, pre-draft)

These are observations for the thesis pass, NOT claims to be cited verbatim in the article without further verification.

1. **The doubling-time acceleration is the load-bearing capability claim.** 187 days (all-time) vs 128 days (2023+) is the difference between a 2032 crossover and a 2030 crossover under naive extrapolation. The article should foreground this acceleration, not the all-time average.

2. **The capability frontier in early 2026 sits at ~12-17 hours of human-equivalent task work.** Claude Opus 4.6 (Feb 2026, 12 hr) and the "Mythos preview" (17 hr) bracket the current frontier. This is no longer "AI can answer questions" — it's "AI can do most of a working day's expert task."

3. **Naive extrapolation from current frontier:** if doubling continues at 128 days from 12 hours (Feb 2026), then by 2030 the model frontier would be at 12 × 2^11.4 ≈ 32,400 hours ≈ 3.7 years of equivalent human task work. This is the *unconstrained* exponential extrapolation. The constrained S-curve (per methodology §3) will be the article's actual projection — but the unconstrained number is useful as the "upper bound under continuing trends" anchor.

4. **Compute scaling continues — Epoch shows GPT-4.5 at 3.8e26 FLOPs, Grok 4 at 5e26.** Training compute up roughly 10× per year for frontier models since 2017. Public attention recently focused on inference (RL/reasoning), but pre-training compute is still climbing.

5. **China is on the frontier list now.** Epoch's recent frontier entries include DeepSeek-V4 (April 2026, 9.7e24 FLOPs active), GLM-4-Plus, and others. The geography of frontier development is broadening, which matters for the macro section's "China State Council" thread.

6. **Confidence tiers must be displayed.** For closed-model entries (GPT-4o, Claude 3 Opus, etc.), Epoch marks training-compute as "Speculative" or "Likely." Any chart that includes these MUST visually distinguish them from "Confident" entries — methodology §1.4 ("no silent imputation") + §7 (visual standards).

7. **The Frontier-model flag is a useful filter but not the only one.** Only 57 of 723 post-2017 rows are marked frontier=True. Many notable models (Llama 3, Mixtral, Qwen, Yi etc.) are not flagged frontier but are central to the open-weights story. Article will likely show two series: frontier-only (capability ceiling) and notable-broad (the diffusion).

---

## Open methodology questions

These need decisions before charting:

1. **For closed models with no disclosed compute, do we use Epoch's "Speculative" or "Likely" estimates, or exclude them?** Per §3.4 (no point estimates without ranges), the right move is to plot them with explicit error bars. Need a methodology note on the chart.

2. **For the doubling-time chart, do we use p50 or p80 horizon?** p50 is the headline METR uses; p80 is the more demanding benchmark. The 2023-only doubling time figure is for p50. Recommend p50 with a note that p80 is harder.

3. **Cutoff date for inclusion in this article's data freeze:** suggested cutoff = 2026-04-30 (latest full month). Models released after the cutoff get a "post-freeze, not included" note.

---

## Source-tracker status to flip

After this pull, update `sources.md`:

- `LEG1_EPOCH_NOTABLE_2024` → `pulled` (was `proposed`)
- `LEG1_METR_AUTONOMY_2024` → `pulled`
- `LEG1_STANFORD_HAI_AIINDEX` → `pulled` (PDF preserved; specific figures pending in-article verification)

`verified` flip happens once specific data points are cross-referenced at chart-construction time.
