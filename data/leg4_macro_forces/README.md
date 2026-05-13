# Leg 4 — Macro forces

Capital allocation + financing data feeding Section 2 of the article.

## Planned series

| File | Topic | Source(s) | Status |
|---|---|---|---|
| `mag7_capex_2022_2026.csv` | Mag7 + hyperscaler capex 2022-2026 | LEG4_MAG7_CAPEX + analyst aggregations | Pulled (Tier 1) |
| `stargate_commitments.csv` | Stargate Project + related sovereign-fund commitments | LEG4_STARGATE + primary announcements | Pulled (Tier 1) |
| `us_fiscal_trajectory.csv` | US deficit / debt projections | LEG4_CBO_DEFICIT | Pulled (Tier 1) |
| `us_monetary_aggregates.csv` | Fed balance sheet (WALCL) + M2 (M2SL) | LEG4_FRED_FED_BALANCE + LEG4_FRED_M2 | Pulled via search (direct FRED CSV blocked from this env — see methodology note) |
| `named_capital_voices.csv` | Public statements from named capital allocators | Andreessen / Karp / Schmidt + sovereign fund chiefs | Pending (Tier 2) |
| `sovereign_fund_ai_allocations.csv` | PIF + G42 + Mubadala + Temasek AI commitments | LEG4_PIF_AUM + announcements | Pending (Tier 2) |

## Anchor findings (key quants captured)

**Mag7 / hyperscaler capex acceleration:**
- 2024: $224B aggregate
- 2025: $413B aggregate (**+84% YoY**)
- 2026: $600-700B aggregate (estimated)
- Five-company subset (MS, GOOGL, AMZN, META, ORCL): $660-690B committed for 2026
- Per-company 2026 plans: Amazon $200B, Alphabet $175-185B (revised up 3× from initial $71-73B), Meta $125B, Microsoft $120B+, Tesla ~$20B (doubled YoY for Optimus + Robotaxi), Apple $13B (lagging)
- Goldman Sachs: $765B annual AI capex in 2026 → $1.6T by 2031

**Stargate Project:**
- Announced January 21, 2025
- **$500B over 4 years**, $100B deployed immediately
- Partners: OpenAI + SoftBank (40% ownership each), Oracle + MGX (7% each)
- Initial capital: SoftBank $19B + OpenAI $19B + Oracle $7B + MGX $7B = $52B
- Q1 2026 update: nearly 7 GW capacity announced, over $400B planned in 3 years
- 5 new US data center sites announced
- International expansion: UAE (2026), UK / Norway / Argentina / South Korea (in development)

**US fiscal trajectory (CBO Budget and Economic Outlook):**
- FY2025 deficit: $1.9 trillion (6.2% of GDP)
- FY2026 deficit: $1.9 trillion (CBO Feb 2026 baseline)
- FY2027 deficit: 5.2% of GDP as TCJA effects + revenue growth narrow
- By 2035: $2.7T deficit; federal debt held by public at **118% of GDP** (surpasses 1946 peak of 106%)
- By 2036: $3.1T deficit, 120% debt-to-GDP, 6.7% of GDP

**US monetary aggregates:**
- M2: $22.5T (Jan 2026), up from $20.4T (mid-2025) — **+$1.6T over ~12 months**
- M2 currently ~$0.5T below COVID-era peak
- FRED WALCL (Fed balance sheet): direct values pending — direct CSV blocked from this environment, alternate route needed (Tier 2)
- Mises Institute (Feb 2026): described money-supply growth as "multi-year high as the Fed pumps new QE"

## Schema commitments

Same `source_id`, `verified`, `notes` columns. Confidence on capex figures: `medium` until cross-checked against company 10-K filings (Tier 2).

## Data access constraint to record

Direct FRED CSV downloads (https://fred.stlouisfed.org/graph/fredgraph.csv?id=*) hit "Connection was reset" or 403 from this environment. Pulled values via WebSearch summaries from FRED + Federal Reserve H.6 release. Tier 2 follow-up: try FRED direct CSV from a different network, or fetch H.6 PDFs from federalreserve.gov.
