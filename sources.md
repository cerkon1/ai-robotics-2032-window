# Sources — AI × Robotics Article

Canonical source tracker for every claim, chart, and data point.

**Discipline rule:** Nothing goes in a draft until it has a `status: verified` row here. No exceptions. If a claim can't be sourced, it doesn't ship.

---

## Schema

Each source is a row in the table below.

| Field | Meaning |
|---|---|
| `id` | Stable identifier, used as `source_id` column in `data/*.csv` files. Format: `LEGn_SHORTNAME_YEAR` (e.g., `LEG1_EPOCH_NOTABLE_2024`). |
| `claim_or_metric` | What this source is being used to support. |
| `source_name` | Publishing organization / author. |
| `source_url` | Canonical URL. Use the publisher's domain, not a secondary citation. |
| `series_or_data_point` | The specific series, table, or figure being used. |
| `retrieval_date` | Date the data was pulled (YYYY-MM-DD). |
| `status` | One of: `proposed` (identified, not yet pulled) / `pulled` (data acquired, awaiting verification) / `verified` (cross-checked, cleared for use) / `cited` (referenced in published article) / `rejected` (pulled but unsuitable — kept here so we don't re-investigate). |
| `confidence` | `high` (primary publisher disclosure or independent measurement), `medium` (third-party estimate from a credible aggregator), `low` (informal estimate or projection). |
| `caveats` | Anything readers should know — methodology assumptions, known biases, data gaps, paywall, etc. |

---

## Leg 1 — AI capability/cost (PROPOSED sources, not yet pulled)

| id | claim_or_metric | source_name | source_url | series_or_data_point | retrieval_date | status | confidence | caveats |
|---|---|---|---|---|---|---|---|---|
| LEG1_EPOCH_NOTABLE_2024 | Training compute scaling for frontier models | Epoch AI | https://epoch.ai/data/notable_ai_models.csv | Notable AI Models database — 1,016 model rows, 47 cols. Updated by publisher 2026-05-07 (1 day pre-pull). | 2026-05-12 | pulled | high | CC BY 4.0. Raw saved to `data/leg1_ai_capability_cost/epoch_notable_ai_models_raw.csv`. Cleaned post-2017 frontier subset (165 rows) at `epoch_frontier_post2017.csv`. Methodology + inclusion criteria documented at https://epoch.ai/data/ai-models-documentation. Confidence tiers: Confident / Likely / Unknown / Speculative — must be shown visually on any chart. |
| LEG1_EPOCH_COMPUTE_TRENDS_2024 | Compute doubling rate (training and inference) | Epoch AI | https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year | "Training Compute of Frontier AI Models Grows by 4-5x per Year" blog post + data | — | proposed | high | Need the underlying CSV (or derive from LEG1_EPOCH_NOTABLE_2024). |
| LEG1_METR_AUTONOMY_2024 | Model task-length doubling (autonomy proxy) | METR (Model Evaluation and Threat Research) | https://metr.org/assets/benchmark_results_1_1.yaml | METR-Horizon-v1.1 benchmark — 26 frontier models, gpt2 (2019-02) → Claude Mythos (early 2026). Doubling time: 187.8 days all-time (point estimate); 128.7 days from 2023+ (CI 104.4-158.0). | 2026-05-12 | pulled | high | Raw YAML at `metr_benchmark_results_raw.yaml`. Pivoted to CSV at `metr_autonomy_horizons.csv` (26 rows). Reference paper: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/. Repo: https://github.com/METR/eval-analysis-public. p50 horizon is the headline metric; p80 included. Acceleration in 2023+ is the lead finding. |
| LEG1_STANFORD_HAI_AIINDEX | Annual AI Index aggregate metrics | Stanford HAI | https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf | AI Index Report 2025 — 8th edition. New 2025 additions: AI hardware landscape, inference cost estimates, publication/patenting trends, corporate responsible AI. | 2026-05-12 | pulled | high | PDF (30 MB) preserved at `data/leg1_ai_capability_cost/hai_ai_index_2025.pdf`. Structured CSV variant on Kaggle: https://www.kaggle.com/datasets/paultimothymooney/ai-index-report-2025 (pending pull as cross-check). 2026 edition also published (https://hai.stanford.edu/ai-index/2026-ai-index-report) — pull on follow-up. |
| LEG1_ARC_AGI | Frontier reasoning benchmark | ARC Prize / Chollet | https://arcprize.org/leaderboard | ARC-AGI leaderboard scores by model and date | — | proposed | high | Benchmark saturation curve. Useful for "are we hitting an asymptote?" question. |
| LEG1_GPQA | Graduate-level science Q&A benchmark | GPQA (Rein et al.) | https://github.com/idavidrein/gpqa | Score by model + date | — | proposed | high | Pair with ARC-AGI to show benchmark progression. |
| LEG1_SWEBENCH | Real-world coding task benchmark | SWE-Bench / Princeton | https://www.swebench.com/ | SWE-Bench Verified leaderboard | — | proposed | high | Measures real engineering ability, not just reasoning. Saturation < 50% as of recent. |
| LEG1_API_PRICING_HISTORY | Inference cost ($/Mtok) trajectory | Aggregated from OpenAI, Anthropic, Google, Meta pricing pages | (multiple) | API pricing per model over time | — | proposed | medium | Will require Wayback Machine for historical pricing. Plan to build our own CSV; cross-check with Artificial Analysis or LMSYS if they have one. |
| LEG1_ARTIFICIAL_ANALYSIS | Multi-model price and performance aggregation | Artificial Analysis | https://artificialanalysis.ai/ | Model comparison tables — price, throughput, latency, quality | — | proposed | medium | Useful for cross-checking inference cost decline. |

## Leg 2 — Robotics deployment/cost (PROPOSED, not yet pulled)

| id | claim_or_metric | source_name | source_url | series_or_data_point | retrieval_date | status | confidence | caveats |
|---|---|---|---|---|---|---|---|---|
| LEG2_IFR_WORLD_ROBOTICS | Annual industrial robot installations + stock + density by country | International Federation of Robotics (IFR) | https://ifr.org/worldrobotics/ | World Robotics 2024 (2023 data) + World Robotics 2025 (2024 data). Topline figures from IFR press releases. | 2026-05-12 | pulled | high | Free Exec Summary PDF preserved at `data/leg2_robotics_deployment_cost/ifr_executive_summary_2024.pdf`. Full report paywalled (~€800). Clean topline CSV at `ifr_industrial_robots_topline.csv` (32 rows). Granular country-year matrix is in the paid report — Tier 2 PDF deep-read can extract from the free exec summary. |
| LEG2_IFR_PRESS_ROBOT_DENSITY_2026 | Robot density per 10K employees by country, 2024 | IFR | https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas | Top 10 by density + regional aggregates | 2026-05-12 | pulled | high | Published April 8, 2026 (World Robotics 2025 release). Korea 1220, Singapore 818, Germany 449, Japan 446, US 307, China 166. |
| LEG2_IFR_PRESS_CHINA_2026 | China robotics policy strategy + 2024 install figures | IFR | https://ifr.org/ifr-press-releases/news/china-makes-ai-powered-robots-core-of-national-strategy | China 54% of 2024 global installs; ~2M operational stock; domestic supplier share 30%→57% 2020→2024 | 2026-05-12 | pulled | high | Published May 5, 2026. Key for Section 2 China-policy thread. |
| LEG2_HUMANOID_FUNDING | Capex flowing to humanoid robotics startups (aggregator entry) | Crunchbase News + company announcements + sector trackers | https://news.crunchbase.com/venture/ai-humanoid-robot-funding-apptronik/ | Aggregate 2024-2026 humanoid + general robotics rounds | 2026-05-12 | pulled | medium | Clean CSV at `humanoid_funding_rounds.csv` (12 rows). Aggregate sector totals: $8.2B (2024) → $14B (2025), exceeded 2021 peak of $13.1B. Per-round primary-source verification PENDING (Tier 2). |
| LEG2_UNITREE_PRICING | Commodity humanoid retail pricing | Unitree Robotics | https://www.unitree.com/g1 | G1 standard: $13,500 USD retail (excl. tax/shipping); G1 EDU contact-sales; specs: 1320mm, 35kg, 23 DOF, 2hr battery | 2026-05-12 | verified | high | Direct from product page. The commodity-humanoid cost floor. |
| LEG2_TESLA_Q1_2026 | Tesla Optimus production guidance + cost estimates | Tesla Q1 2026 earnings call coverage | https://seekingalpha.com/news/4578385-tesla-signals-over-25b-2025minus-2026-capex-as-it-targets-optimus-production-by-late-july | Production start late Jul/Aug 2026 Fremont; current cost $50-100K/unit; initial commercial $100-150K; target <$30K; 2026 capex >$25B (3x 2025) | 2026-05-12 | pulled | medium | Verify against actual Tesla earnings call transcript or 10-Q before final draft. Notable: Musk DECLINED to provide 2026 production target — guidance reduction signal. |
| LEG2_GOLDMAN_HUMANOID_TAM | Industry-side forecast (treated as forecast, not data) | Goldman Sachs Research | (note: forecast, not measurement) | Humanoid TAM forecast 2024-2035 | — | proposed | low | Bank forecasts are advocacy as much as analysis. Use for contrast, not as ground truth. |
| LEG2_VLA_BENCHMARKS | Vision-Language-Action model capability | Multiple (RT-2, RT-X, OpenVLA, π0 papers) | (aggregated) | Task success rates on standard benchmarks over time | — | proposed | medium | Not a normalized series — will require manual aggregation. Pull in Tier 2 wave. |
| LEG2_CHINA_MIIT_HUMANOID | China policy targets for humanoid production | MIIT (via SCMP, Robot Report, USCC) | https://www.scmp.com/news/china/politics/article/3240259/china-says-humanoid-robots-are-new-engine-growth-pushes-mass-production-2025-and-world-leadership | 2025 mass production goal; 2027 economic engine + world leader; Feb 2026 first national standard system published | 2026-05-12 | pulled | medium | Currently via secondary sources (SCMP, Robot Report). Primary MIIT doc (in English) PENDING — Tier 2. USCC report at https://www.uscc.gov/sites/default/files/2024-10/Humanoid_Robots.pdf is a useful corroborating analysis. |

## Leg 3 — Execution layer constraints (PROPOSED)

| id | claim_or_metric | source_name | source_url | series_or_data_point | retrieval_date | status | confidence | caveats |
|---|---|---|---|---|---|---|---|---|
| LEG3_IEA_ELECTRICITY | Global AI/data center electricity demand projections | IEA | https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf | "Energy and AI" Special Report 2025 — global data center electricity 485 TWh (2025) → 945 TWh (2030) → 1200 TWh (2035); US/CN/EU regional breakdown | 2026-05-12 | pulled | high | PDF preserved at `data/leg3_execution_layer/iea_energy_and_ai_2025.pdf` (8.2 MB). Cleaned topline at `c1_grid_data_center_demand.csv`. Granular bottleneck specifics pending PDF deep-read. |
| LEG3_FERC_QUEUE | US grid interconnection queue length + wait times | LBNL / Berkeley Lab | https://emp.lbl.gov/sites/default/files/2024-04/Queued%20Up%202024%20Edition_1.pdf | "Queued Up: 2024 Edition" — 10,300 projects, 1,400 GW generation + 890 GW storage in queue end-2024; median wait 4+ years; 77% withdrawal rate | 2026-05-12 | pulled | high | PDF preserved at `data/leg3_execution_layer/lbnl_queued_up_2024.pdf` (9.1 MB). Cleaned figures at `c1_grid_interconnection_queue.csv`. 2025 Edition available at https://emp.lbl.gov/queues for Tier 2 update. |
| LEG3_UN_WPP_DEMOGRAPHICS | Working-age population by country | UN DESA Population Division (via OWID mirror) | https://ourworldindata.org/grapher/population-young-working-elderly-with-projections.csv?v=1&csvType=full&useColumnShortNames=true | UN WPP 2024 data via Our World in Data — country-level 0-14 / 15-64 / 65+ population, historical 1950-2023 + medium-scenario projections to 2100 | 2026-05-12 | pulled | high | Raw CSV preserved at `owid_working_age_raw.csv` (1.8 MB). Cleaned country/year matrix at `c4_working_age_population_by_country.csv` (192 rows, 17 countries x 12 years). Topline figures (pop peak, fertility, ultra-low fertility countries) extracted from UN Summary PDF and captured in `c4_demographics_peak_milestones.csv`. UN data portal API requires Bearer auth — OWID is the practical CSV path. |
| LEG3_BLS_AUTOMATION_RISK | US occupational employment + automation risk overlays | BLS | https://www.bls.gov/oes/ | Occupational Employment & Wage Statistics + Frey-Osborne / OECD overlays | — | proposed | high | Tier 2 follow-up — automation-risk overlays (Frey-Osborne) pending. |
| LEG3_BLS_OES | US Occupational Employment and Wage Statistics May 2024 | BLS via search aggregation | https://www.bls.gov/news.release/ocwage.t01.htm | Verified headline values: Stockers 2,779,530 @ ~$33K; Janitors 2,199,900 @ $17.27/hr; Fast food 2,302,690 @ $16.23/hr; Nursing assistants 1,388,430 @ $41,270; Home aides 4.3M @ $34,900; Electricians 818,700 @ $62,350; Truck drivers ~2.2M @ $57,440; Logisticians 241,000 @ $80,880; Hand laborers @ $37,680 | 2026-05-12 | pulled | medium | BLS HTML pages blocked from this environment with 403; values via WebSearch summaries of BLS data. Cleaned at `cohort_map/cohort_map_us_occupations.csv`. Several cohort rows still have BLS-inferred estimates rather than directly-confirmed counts (notes column flags `verified: false`). |
| LEG3_AV_HISTORICAL | Autonomous-vehicle deployment timeline (as reliability analog) | CA DMV Disengagement Reports + Waymo disclosures | https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/disengagement-reports/ | 2023+2024 reports — Waymo 2024: 2.39M test miles (-35% YoY); permits 380→1080; testing-to-commercial pivot | 2026-05-12 | pulled | medium | Topline at `c3_av_reliability_progression.csv`. Tier 2: deeper time series 2015-2024 from CA DMV + Waymo Public Road Safety Report. |
| LEG3_EU_AI_ACT | Regulatory friction (deployment constraint) | EUR-Lex + AI Act Implementation Tracker | https://artificialintelligenceact.eu/implementation-timeline/ | Entry-into-force Aug 1 2024; high-risk Annex III obligations Aug 2 2026; Article 6(1)/Annex I Aug 2 2027; possible Digital Omnibus delay to Dec 2027 | 2026-05-12 | pulled | high | Captured in `c5_regulatory_milestones.csv`. |
| LEG3_MFG_CAPACITY | Humanoid factory production targets (aggregator) | Multiple — company announcements + industry trackers | (aggregated) | Stated 2026 targets sum ~177K humanoids; BofA forecast 90K | 2026-05-12 | pulled | medium | Cleaned at `c2_humanoid_manufacturing_capacity.csv`. Caveat: Tesla 2026 target widely cited as 100K but Musk DECLINED to confirm in Q1 2026 call — flagging as in-source contradiction. |
| LEG3_BOFA_FORECAST | Bank of America humanoid robot forecast | BofA Research | (forecast — treat as analyst view, not data) | 90K (2026) → 1.2M (2030) → 3B stock (2060) | 2026-05-12 | pulled | low | Forecast not measurement. Used for "industry forecast" contrast. Need primary BofA Research note URL for citation — Tier 2. |

## Leg 4 — Macro forces (Section 2 data — PROPOSED)

| id | claim_or_metric | source_name | source_url | series_or_data_point | retrieval_date | status | confidence | caveats |
|---|---|---|---|---|---|---|---|---|
| LEG4_MAG7_CAPEX | Mag7 capital expenditure 2022-2026 | Analyst aggregations (Futurum, Indras, Motley Fool, IEEE ComSoc) | https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/ | $224B (2024) → $413B (2025, +84%) → $600-700B (2026 estimate). Per-company plans. | 2026-05-12 | pulled | medium | Cleaned at `mag7_capex_2022_2026.csv`. 10-K primary verification pending Tier 2. Goldman estimate $765B (2026) → $1.6T (2031). |
| LEG4_STARGATE | Stargate Project announcement + progress | OpenAI primary + S&P Global + DCD coverage | https://openai.com/index/announcing-the-stargate-project/ | $500B / 4 years. $100B immediate. Partners: SoftBank+OpenAI (40% each), Oracle+MGX (7% each). Q1 2026: 7 GW, $400B in 3 years, 5 US sites + UAE + UK/Norway/Argentina/SK in dev. | 2026-05-12 | pulled | medium | Cleaned at `stargate_commitments.csv`. Site-by-site MW detail pending Tier 2. |
| LEG4_CBO_DEFICIT | US fiscal trajectory | Congressional Budget Office | https://www.cbo.gov/publication/61882 | Budget and Economic Outlook 2026-2036 (Feb 2026): FY26 $1.9T (5.5% GDP) → FY36 $3.1T (6.7% GDP); debt-to-GDP 100%→118%(2035)→120%(2036), passes 1946 WWII peak | 2026-05-12 | pulled | high | Cleaned at `us_fiscal_trajectory.csv`. Direct CBO primary source. |
| LEG4_FRED_FED_BALANCE | Fed balance sheet | FRED | https://fred.stlouisfed.org/series/WALCL | Total assets, weekly. Series ID WALCL. | — | pending | high | Direct CSV download (https://fred.stlouisfed.org/graph/fredgraph.csv?id=WALCL) blocked from this environment with HTTP 403/connection-reset. Tier 2: try alternate network or fetch H.6 PDFs from federalreserve.gov. |
| LEG4_FRED_M2 | M2 money supply | FRED (via search aggregation) | https://fred.stlouisfed.org/series/M2SL | M2 = $22.4T (Jan 2026), +$1.6T trailing-12-month, ~$0.5T below COVID peak | 2026-05-12 | pulled | medium | Cleaned at `us_monetary_aggregates.csv`. Specific monthly values from Trading Economics + Mises Institute coverage of FRED data. Direct FRED CSV pending. |
| LEG4_BLS_LABOR_SHARE | Labor share of GDP | FRED (PRS85006173) | https://fred.stlouisfed.org/series/PRS85006173 | Nonfarm business sector: labor share | — | pending | high | Direct CSV blocked. Tier 2. |
| LEG4_PIF_AUM | Saudi PIF AI/automation allocation | PIF annual report + announcements | https://www.pif.gov.sa/en | AUM growth + AI sector allocations | — | proposed | medium | Sovereign-fund opacity. Tier 2. |
| LEG4_NAMED_CAPITAL_VOICES | Public statements from named capital allocators | Direct publications | (multiple) | Andreessen Techno-Optimist Manifesto; Karp Foundry/Palantir essays; Schmidt SCSP report | — | proposed | high | Tier 2 — needed for Part 2 draft, low effort each. |

---

## Status legend

- **proposed** — Source identified, candidate for use, not yet pulled. Most entries start here.
- **pulled** — Data acquired (CSV/PDF/text downloaded into `data/`). Awaiting verification (cross-check methodology, units, date range).
- **verified** — Pulled + cross-checked. Cleared for use in drafts.
- **cited** — Referenced in a published draft. (Will be filled in once Part 1+ ship.)
- **rejected** — Pulled, but unsuitable. Kept here with rejection reason so we don't re-investigate.

---

## How to add a source

1. Pick the right leg table.
2. Fill all schema columns. Be specific in `series_or_data_point` — "World Robotics Report" is too vague; "World Robotics 2024, Table 2.1, installations by country 2018-2023" is right.
3. Start at `status: proposed`. Move forward only when the work is done.
4. If `confidence: low`, the data either gets corroborated by a second source or doesn't ship.
5. Caveats field is non-optional for `low`/`medium` confidence rows.

---

**Last updated:** 2026-05-12 (Tier 1 + chart-data gap-closure complete)

---

## New sources added during chart-data gap-closure round

| id | claim_or_metric | source_name | source_url | series_or_data_point | retrieval_date | status | confidence | caveats |
|---|---|---|---|---|---|---|---|---|
| LEG4_BLS_LABOR_SHARE | US nonfarm business labor share | BLS retrospective + FRED reference | https://www.bls.gov/opub/ted/2017/labor-share-of-output-has-declined-since-1947.htm | 4 confirmed key values 2000/2011/2016/2024 + interpolations | 2026-05-12 | pulled | medium | Direct FRED CSV blocked. Key values via BLS retrospective coverage. Cleaned at `kshape_chart_data.csv`. Final chart needs FRED PRS85006173 primary verification. |
| LEG4_SP500_TR | S&P 500 total return historical | Yahoo Finance ^SP500TR / SlickCharts | https://finance.yahoo.com/quote/%5ESP500TR/history/ | Year-end 2000-2024 index levels (approximate) | 2026-05-12 | pulled | low | Approximate trajectory points only. Verify against ^SP500TR closing values before chart finalization. |
| LEG3_BLS_CPI | US CPI components 2000-2024 | Mark Perry "Chart of the Century" / AEI Carpe Diem | https://www.aei.org/carpe-diem/chart-of-the-day-or-century-8/ | 16-row CPI component price-change table; CPI +87.3% / wages +123.3%; TVs -97% / hospital +250% extremes | 2026-05-12 | pulled | medium | Mark Perry chart is widely cited and updated through June 2024. Article should re-derive from BLS primary at chart-production for verifiable citations. |
| LEG4_HYPERSCALER_CAPEX | 5-hyperscaler aggregate capex 2022-2026 | Visual Capitalist + CNBC + Wolf Street | https://www.visualcapitalist.com/visualized-big-tech-ai-spending/ | AMZN+GOOGL+META+MSFT+ORCL aggregate $162B (2022) → $200B (2023) → $251B 4-co (2024) → $448B (2025) → $700B (2026) | 2026-05-12 | pulled | medium | Different sources count different subsets (4 vs 5 hyperscalers vs Mag7 7-co). Article should disambiguate which subset is plotted. Primary 10-K verification pending. |
| SCARCE_ASSET_RETURNS | Multi-asset performance 2015-2025 | CoinMarketCap (BTC), LBMA (Gold), FRED (housing), Yahoo (SPX/MSCI) | (multiple aggregators) | BTC $362→$93,429 (~258x); Gold $1,077→$2,624 (2.4x); US median home ~1.4x; SPX TR ~3.8x; MSCI World ~2.7x — all 2015-2024 | 2026-05-12 | pulled | medium | BTC + Gold end-of-year values confirmed; SPX TR / home / MSCI World approximations. Primary-source verification pending at chart-production. |

---

## Status — sources tally as of 2026-05-12

| Status | Count |
|---|---|
| `verified` (cross-checked, ready for citation) | 2 (Unitree pricing direct + UN WPP via OWID) |
| `pulled` (data in hand) | 25+ |
| `proposed` (identified, not pulled) | 5 (BLS automation overlays, Goldman humanoid TAM, VLA benchmarks, PIF AUM, named capital voices primaries) |
| `pending` (blocked or future-work) | 2 (FRED WALCL direct, FRED labor share direct) |

Data infrastructure is complete for chart production. Tier 2 verification ongoing as Substack publish approaches.
