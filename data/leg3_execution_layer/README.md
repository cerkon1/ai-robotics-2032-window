# Leg 3 — Execution layer constraints

Five sub-axes of physical/regulatory/demographic constraints that bend the AI×robotics deployment curve from exponential into S-shape.

## Five constraint axes

| Axis | What | Files | Status |
|---|---|---|---|
| C1 — Grid / energy | Electricity demand from AI + interconnection bottlenecks | `c1_grid_data_center_demand.csv`, `c1_grid_interconnection_queue.csv`, IEA + LBNL PDFs | Pulled (Tier 1) |
| C2 — Manufacturing capacity | Humanoid factory production targets, lead times | `c2_humanoid_manufacturing_capacity.csv` | Pulled (Tier 1) |
| C3 — Reliability threshold | Autonomous vehicle analog — disengagement, commercial deployment | `c3_av_reliability_progression.csv` | Pulled (Tier 1) |
| C4 — Demographics | Working-age population projections | `c4_demographics_peak_milestones.csv` (placeholder) + UN WPP PDF | Topline only — country-level pending PDF deep-read |
| C5 — Regulation | EU AI Act, OSHA, US state-level | `c5_regulatory_milestones.csv` | Pulled (Tier 1) |

## Schema commitments

Same `source_id`, `verified`, `notes` columns as Legs 1+2.

## Anchor findings (key quants captured)

**C1 — Grid:**
- Global data center electricity: 485 TWh (2025) → 945-950 TWh (2030 base case) → ~1,200 TWh (2035)
- ~3% of global electricity by 2030
- US growth: +240 TWh (+130% vs 2024)
- China growth: +175 TWh (+170% vs 2024)
- Europe growth: +45 TWh (+70% vs 2024)
- AI-optimized data centers more than quadruple by 2030
- **US grid queue: 10,300 projects, 1,400 GW generation + 890 GW storage waiting end-2024**
- Median wait time interconnection request → commercial operation: <2 years (2000-2007) → **>4 years (2018-2024)**
- 77% of capacity submitted 2000-2019 withdrew before reaching operations

**C2 — Manufacturing:**
- Tesla: 5K (2025) → 100K (2026 plan) → 1M/yr long-term target; first factory Fremont late Jul/Aug 2026; second Giga Texas summer 2027. **Note contradiction: Musk DECLINED to confirm 2026 target in Q1 2026 call**
- BYD: 1.5K (2025) → 20K (2026)
- Unitree: 5.5K+ (2025) → 10-20K (2026)
- Figure AI: BotQ factory targets 12K/yr; deployed at BMW X3 production line (30K BMW X3 vehicles in 10 months)
- Xiaomi: hundreds → tens of thousands 2025-2027
- XPeng: mass production end 2026 (IRON humanoid)
- **~90% of humanoid robots sold in 2025 were Chinese**
- BofA forecast: ~90K shipments (2026) → 1.2M (2030) global

**C3 — Reliability (autonomous-vehicle analog):**
- Waymo 2024: 2,389,565 testing miles (-35% YoY) — pivoting to commercial ops
- Waymo CA fleet: 1,035 vehicles (+136% YoY)
- Waymo driverless permits: 380 (2023) → 1,080 (2024)
- Industry: 4.5M total CA AV test miles 2024 (-50% YoY); driverless miles 3.26M → 552K (-83%)
- **Interpretation:** the testing-miles decline is NOT a reliability regression — it's the testing-to-commercial transition. Useful analog for what humanoid maturation looks like.
- Waymo commercial: live in SF, LA, Phoenix; expanding

**C4 — Demographics:**
- Global population peaks 2084 at ~10.3B (UN WPP 2024)
- 2024 revision downgraded Asia/Africa/LatAm projections; upgraded Europe/NA
- Global fertility: 5+ (1960s) → 2.3 (2024)
- **Country-level working-age projections (15-64 by year) for China/Japan/Korea/Germany/Italy — PENDING UN WPP PDF deep-read**

**C5 — Regulation:**
- EU AI Act high-risk (Annex III) obligations apply 2 Aug 2026
- EU AI Act Article 6(1) high-risk (Annex I — products in harmonised legislation) apply 2 Aug 2027
- Possible Digital Omnibus delay to 2 Dec 2027 (currently in trilogue)
- Article 6 implementation guidelines deadline: 2 Feb 2026
- OSHA, US state-level: gathering needed for Tier 2
