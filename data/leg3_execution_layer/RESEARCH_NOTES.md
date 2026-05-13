# Leg 3 — Research Notes

**Last updated:** 2026-05-12
**Status:** Tier 1 pulled for C1 (grid), C2 (manufacturing), C3 (reliability), C5 (regulation). C4 (demographics) topline only — country-level working-age data from UN WPP 2024 PDF pending deep-read.

---

## What's been pulled

### C1 — Grid / Energy

- **IEA Energy and AI report** (`iea_energy_and_ai_2025.pdf`, 8.2 MB) — preserved
- **LBNL "Queued Up" 2024 Edition** (`lbnl_queued_up_2024.pdf`, 9.1 MB) — preserved
- Clean CSVs: `c1_grid_data_center_demand.csv` + `c1_grid_interconnection_queue.csv`

**Headline numbers:**
- AI/data center electricity 2025-2035: **485 TWh → 945 TWh (2030) → 1,200 TWh (2035)**
- ~3% of global electricity by 2030
- US + China = 80% of growth
- AI-optimized data center demand more than quadruples by 2030
- **US grid queue (end-2024): 10,300 projects, 1,400 GW generation + 890 GW storage**
- **Median wait time: <2 yrs (2000-2007) → >4 yrs (2018-2024)** — doubled
- 77% of capacity submitted 2000-2019 was *withdrawn* before reaching commercial operation

### C2 — Manufacturing capacity

- Clean CSV: `c2_humanoid_manufacturing_capacity.csv`

**Stated 2026 targets sum:**
- Tesla 100K + BYD 20K + Unitree 15K + Figure 12K + Xiaomi ~30K = **~177K units IF ALL targets hit**
- BofA analyst forecast: 90K for 2026 — **analysts are at 50% of stated targets**
- **Critical contradiction: Musk DECLINED to confirm Tesla 2026 target in Q1 2026 earnings call.** Stated "100K" target is industry hearsay, not company guidance.
- ~90% of humanoid robots sold in 2025 were Chinese-manufactured
- BofA long-term forecast: 1.2M (2030) → 3B (2060 stock); treat as forecast not data

### C3 — Reliability (AV analog)

- Clean CSV: `c3_av_reliability_progression.csv`

**Headline pattern:**
- Waymo testing miles: 3.67M (2023) → 2.39M (2024), -35%
- Industry total: 4.5M (2024), -50%
- BUT — Waymo CA driverless permits: 380 → 1,080 (+184%)
- Active fleet: 1,035 vehicles (+136%)
- **Interpretation: NOT a reliability regression — a testing-to-commercial pivot.** The single most useful analog for what humanoid maturation will look like: long testing tail, then sharp transition to commercial deployment.

### C4 — Demographics

- `un_wpp_2024_summary.pdf` (18.5 MB) preserved
- Topline only in clean CSV; country-level pending
- Global pop peaks 2084 at ~10.3B (down from 2086 / 10.4B in WPP 2022)
- Global fertility 5+ (1960s) → 2.3 (2024)

**Country-level working-age data PENDING.** This is the biggest single gap in Leg 3. The article needs working-age-population (15-64) projections by year for: China, Japan, S. Korea, Germany, Italy, US (at minimum). UN WPP PDF has these in tables — needs targeted PDF page-reads.

### C5 — Regulation

- Clean CSV: `c5_regulatory_milestones.csv`

**Key dates:**
- EU AI Act in force: 1 Aug 2024
- High-risk Annex III obligations: **2 Aug 2026 (now)**
- Article 6(1) Annex I: 2 Aug 2027
- Possible Digital Omnibus delay to 2 Dec 2027 (trilogue)
- US state-level + OSHA: pending Tier 2

---

## Initial analytical observations

These observations are for the thesis pass, NOT verbatim citations.

### 1. The grid is the single hardest physical constraint

Not capability. Not cost. Not labor. **The grid.** AI-optimized data center electricity demand quadruples by 2030. The US queue has 1,400 GW of generation waiting an average of 4+ years to interconnect. 77% of past-decade queue applicants withdrew. China + US together absorb 80% of global data center growth.

This is the load-bearing claim of the article's *unconstrained-vs-constrained* visual. Naive AI capability extrapolation says "doubling continues." Grid says "you can't power what you can't connect." The convergence date moves significantly under different grid-buildout scenarios.

### 2. The "manufacturing capacity gap" is real and measurable

Sum of stated 2026 humanoid production targets = ~177K. Bank of America analyst forecast = 90K. **The gap (50%) IS the execution-layer wedge.** Companies announce, factories underdeliver, analysts apply a haircut. Tesla literally declined to confirm its widely-cited 100K figure in Q1 2026 — implying the company itself doesn't believe the number.

This is the manufacturing-capacity S-curve clipper. For the article: chart "stated targets" vs "analyst forecasts" vs "actual shipments" — the gap closes only as factory ramp-up cycles complete (~2-3 years per gigafactory).

### 3. The AV analog tells a specific story about timing

Waymo testing miles DROPPED 35% in 2024 — but this is GOOD news for the curve. It means commercial deployment crossed the testing threshold. The pattern was: 2010-2020 long testing tail, 2020-2024 commercialization inflection.

Humanoid robotics is currently in the *testing tail* phase. BMW Spartanburg (Figure 02), Mercedes Sindelfingen (Apptronik), Amazon Digit — these are *pilots*, not commercial deployment. By the AV analog, the testing-to-commercial transition for humanoids should hit somewhere in **2027-2030**. This anchors the 2028-2035 thesis window from a reliability angle.

### 4. Demographic counter-pressure is the most under-discussed point

Most "AI takes jobs" discourse assumes labor supply is constant. **It is not, in advanced economies.** Japan, Korea, Italy, Germany are already past peak working-age population. China hit peak ~2015. The US is plateauing. In the same 2028-2035 window the article discusses AI×robotics ramp, the labor force in advanced economies CONTRACTS.

The doom framing ("robots will replace workers") is the popular story. The more defensible thesis is: **"robots fill the labor gap demographics already opened."** This is the strongest counterargument to the K-shape doom reading — and worth weaving into Section 2 as a tone-modulator. The K-shape still happens (capital captures gains), but the cause is incentive-structural, not malicious.

### 5. EU regulation is a real but bounded clip

EU AI Act high-risk obligations apply 2 Aug 2026 — TODAY in calendar terms. Possible delay to Dec 2027. Either way, the EU becomes a slower-deployment jurisdiction than US/China for a 1-3 year window. Important for the cohort map: deployment will be markedly uneven across geographies, not just sectors.

### 6. China is doing the OPPOSITE of EU on regulation

China MIIT published its first national standard system for humanoid robots in Feb 2026 — but the framing is *enabling* (standardize so industry can scale), not *restricting* (classify and gate high-risk uses). This is policy-side reinforcement of China's deployment lead (54% of 2024 industrial robot installations, ~90% of humanoid manufacturing).

### 7. The "all bottlenecks compound" point

Each constraint independently clips the curve. **Compounded, they bend the trajectory significantly.** If the article shows:
- Naive exponential: convergence ~2030
- Grid-clipped: 2032
- Manufacturing-clipped: 2032-2034
- Reliability-clipped: 2030 (per AV analog)
- Demographic counter-pressure: makes deployment more politically tolerable, doesn't clip
- Regulation-clipped: 2031-2033 in EU; 2029-2031 in US; 2027-2030 in China

...the multi-constraint S-curve lands the *median crossover* in **2031-2033, with a long tail to 2035**. That's the article's 2028-2035 window, derived from constraint compounding rather than asserted.

---

## What's NOT yet pulled (Tier 2)

| Source | What it covers | Effort |
|---|---|---|
| UN WPP 2024 PDF deep-read | Country-level working-age 15-64 projections 2024/2030/2050 for CN/JP/KR/DE/IT/US | 30-60 min (targeted PDF page reads) |
| IEA Energy and AI PDF deep-read | Hyperscaler PPA velocity, transmission-line lead times, regional bottleneck specifics | 30-60 min |
| LBNL Queued Up 2025 Edition | More recent data through end-2024 (currently using 2024 ed. with 2023 data) | 30 min — PDF available at emp.lbl.gov/queues |
| OSHA human-robot collaboration | Current US workplace safety guidance for humanoid deployment | 30-45 min |
| US state AI regulations | CA SB-1047 status, CO AI Act, NYC bias audit, TX TRAIGA | 60-90 min |
| BLS OES occupational data | Cohort-sizing for §1.4 cohort map (warehouse / cleaning / trades by SOC code) | 60 min |
| AV reliability — Waymo/Cruise commercial deployment city list + ride volumes | Tightens the AV analog | 30 min |

**Recommendation:** UN WPP deep-read is the highest-value Tier 2 item — the working-age demographics chart is one of the article's load-bearing visuals. The rest can wait for Leg 4 / cohort-map / pre-draft.

---

## Source-tracker updates

In `sources.md`:
- `LEG3_EIA_GRID` → upgrade to `LEG3_IEA_ELECTRICITY` (using IEA not EIA — different agency, better dataset for AI focus). Mark `pulled`.
- `LEG3_FERC_QUEUE` → `pulled` (LBNL 2024 ed. PDF + topline figures)
- `LEG3_IEA_ELECTRICITY` → `pulled`
- `LEG3_UN_WPP_DEMOGRAPHICS` → `pulled` (PDF preserved; topline figures only; country-level deep-read pending)
- `LEG3_AV_HISTORICAL` → `pulled` (CA DMV 2024 figures; deeper time series pending)
- `LEG3_EU_AI_ACT` → `pulled`
- New rows needed: BoA humanoid forecast source, individual humanoid maker production targets (Tesla / BYD / Unitree / Figure / Xiaomi / XPeng — sources differ; treat each as separate row), CA DMV 2024 disengagement report source.
