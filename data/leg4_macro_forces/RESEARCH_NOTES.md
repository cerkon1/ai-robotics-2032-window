# Leg 4 — Research Notes

**Last updated:** 2026-05-12
**Status:** Tier 1 pulled. Tier 2 outstanding for: FRED direct CSVs (blocked), 10-K capex cross-verification, named-capital-voices, sovereign-fund AI allocations.

---

## What's been pulled

### Mag7 / hyperscaler capex acceleration

- `mag7_capex_2022_2026.csv` — 12 rows
- **The most arresting datapoint of the entire macro section:** $224B (2024) → $413B (2025, +84%) → $600-700B (2026 estimate, ~3x 2024). Goldman Sachs estimates $765B 2026 AI capex broadly, projecting $1.6T by 2031.
- Per-company 2026: Amazon $200B, Alphabet $175-185B, Meta $125B, MS $120B+, Tesla $20B, Apple $13B.

### Stargate Project

- `stargate_commitments.csv` — 10 rows
- **$500B over 4 years** — announced Jan 21 2025. $100B deployed immediately.
- Partners: OpenAI + SoftBank (40% each), Oracle + MGX (7% each)
- Q1 2026 update: nearly 7 GW capacity, $400B over 3 years, 5 new US sites, UAE 2026, UK/Norway/Argentina/South Korea in development.

### US fiscal trajectory

- `us_fiscal_trajectory.csv` — 13 rows
- FY25 + FY26 deficits: $1.9T each (6.2% / 5.5% of GDP)
- FY36 deficit: $3.1T (6.7% of GDP)
- Federal debt held by public: 100% (2025) → 118% (2035) → 120% (2036) — **passes 1946 WWII peak**

### US monetary aggregates

- `us_monetary_aggregates.csv` — 8 rows
- M2: $22.4T (Jan 2026), +$1.6T in trailing 12 months, ~$0.5T below COVID peak
- WALCL (Fed balance sheet): **PENDING — direct FRED CSV blocked from this environment**

---

## Initial analytical observations

These observations are for the thesis pass, NOT verbatim citations.

### 1. The Mag7 capex curve is the single most arresting data point for Section 2

$224B → $413B → $650B over 3 years. **A 3× expansion in 2 years.** Seven companies are deploying ~$650B annually toward AI infrastructure that, mechanistically, will displace labor. This is the financing-data smoking gun for the article's "capital allocation toward labor automation is incentive-driven, not conspiratorial" thesis. No abstract argument needed — the numbers do the work.

For comparison: $650B annual capex from 7 companies > GDP of Sweden, Belgium, Switzerland, or Israel. For Mag7 alone, this is roughly 4× their combined 2014 capex.

### 2. The "Alphabet 3× upward revision" pattern is itself the story

Alphabet's initial 2025 capex guidance: **$71-73B**. Current 2026 guidance: **$175-185B**. The 2026 number is **3× the original 2025 guidance, after 3 successive upward revisions**. Companies are discovering the demand curve as they ramp; analysts are perpetually catching up. **Stated capex numbers in 2025-2026 are floors, not ceilings.** The article should foreground this revision-up pattern as evidence that the AI/robotics capital deployment isn't slowing — it's accelerating faster than projections can keep up.

### 3. The K-shape financing chain is now explicit

- Mag7 + sovereign funds (MGX, PIF, SoftBank-as-proxy) commit hundreds of billions annually
- US fiscal deficit persists at ~6% of GDP, financed via Treasury issuance
- Fed balance sheet + M2 expansion provide the absorbing liquidity (M2 +$1.6T in 12 months as of Jan 2026)
- Federal debt-to-GDP heading from 100% (2025) → 120% (2036) — **breaking the 1946 WWII record**
- Workers receive wages denominated in this expanding money supply
- AI/robotics owners receive equity in productive assets that capture surplus

The article's "abundant money + cheap goods + scarce assets" K-shape is no longer abstract — every link in the chain has its own data row.

### 4. Stargate's structure is the macro story in miniature

$500B AI buildout, with sovereign-fund capital (MGX from UAE, SoftBank as Japan-proxy) interlocking with US tech giants and government coordination (announced from White House, Trump on stage). The capital is **transnational, government-aligned, and AI-targeted.** This is the canonical example to cite when explaining "the actors are public, not shadowy" — Stargate's existence is the answer to "who is paying for this?"

### 5. The fiscal trajectory matters for the BTC positioning argument

CBO projects federal debt held by the public to exceed the 1946 WWII high (106%) and reach 118-120% by mid-2030s. Either fiscal consolidation happens (politically hard, especially with AI-displaced workers needing transfers), OR inflation/financial repression handles the debt burden. Both paths feed the "scarce assets win" thesis. The article should note this is the macro logic *behind* BTC's position in a diversified scarce-asset portfolio, not advocacy.

### 6. Tesla's $20B 2026 capex (vs $8-9B in 2025) is the connecting tissue

Tesla DOUBLED capex specifically for robotaxi + Optimus production. This is the rare datapoint that directly bridges Section 2 (capital allocation) and Section 1 (humanoid + AV deployment). $20B sounds small next to Amazon's $200B — but every dollar of Tesla's is going to robotics/AV specifically, not general data centers.

---

## What's NOT yet pulled (Tier 2)

| Source | Why it matters | Effort |
|---|---|---|
| FRED WALCL CSV direct | Fed balance sheet trajectory for the K-shape monetary chart | 30 min (need alternate network or H.6 PDFs) |
| FRED PRS85006173 (labor share) | Direct historical labor-share-of-GDP series for the "wages losing pricing power" chart | 30 min |
| Mag7 10-K capex line items | Cross-verify the $224B / $413B / $650B aggregates from primary filings | 90-120 min (SEC EDGAR per company) |
| Stargate site-by-site detail | Granular MW/GW per location, expected online dates | 30-45 min |
| Andreessen Techno-Optimist Manifesto | Primary source for "named capital voices" | 15 min |
| Karp Foundry / Palantir CEO essays | Primary source for "Western capital allocators talking openly about AI/labor displacement" | 30 min |
| Schmidt SCSP report | Primary source for US national-strategy framing | 30 min |
| MIIT humanoid roadmap (English) | Primary source for China policy framing | 30 min |
| Sovereign fund AI commitments (PIF, G42, GIC, Temasek) | Quantify the non-US capital deploying into AI | 60-90 min |

---

## Source-tracker updates

In `sources.md`:
- `LEG4_MAG7_CAPEX` → `pulled` (per analyst aggregations; 10-K verification Tier 2)
- `LEG4_STARGATE` → `pulled`
- `LEG4_CBO_DEFICIT` → `pulled`
- `LEG4_FRED_M2` → `pulled` (via search aggregation; direct CSV pending)
- `LEG4_FRED_FED_BALANCE` → `pending` (direct CSV blocked, alternate route needed)
- `LEG4_NAMED_CAPITAL_VOICES` → `pending`

---

## What we now have, end-to-end (all 4 legs)

| Leg | Status | Confidence on Tier 1 |
|---|---|---|
| Leg 1 — AI capability/cost | Tier 1 done | High |
| Leg 2 — Robotics deployment/cost | Tier 1 done | Medium-high |
| Leg 3 — Execution layer (5 axes) | Tier 1 done incl. C4 country-level | High (except C2 mfg cap and BofA forecast) |
| Leg 4 — Macro forces | Tier 1 done | Medium (need 10-K verification) |

**We can now begin drafting Part 1** with the data we have. Tier 2 items become refinement work pre-publish rather than block-the-draft work.
