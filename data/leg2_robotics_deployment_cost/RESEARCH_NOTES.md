# Leg 2 — Research Notes

**Last updated:** 2026-05-12
**Status:** Tier 1 pulled (IFR topline + humanoid funding + humanoid pricing + policy milestones). Tier 2 outstanding (IFR exec summary PDF deep-read; per-round primary-source verification; VLA capability benchmarks).

---

## What's been pulled

### 1. IFR World Robotics — topline figures

- **Source preserved:** `ifr_executive_summary_2024.pdf` (565 KB) — IFR's free Executive Summary of the paid World Robotics 2024 report (which covers 2023 data).
- **Clean data:** `ifr_industrial_robots_topline.csv` — 32 rows combining 2023 installations + 2024 density figures.
- **IFR press releases used as primary sources:**
  - https://ifr.org/ifr-press-releases/news/record-of-4-million-robots-working-in-factories-worldwide (Sep 2024, 2023 data)
  - https://ifr.org/ifr-press-releases/news/robot-density-surges-in-europe-asia-and-americas (April 8, 2026, 2024 density data from World Robotics 2025 report)
  - https://ifr.org/ifr-press-releases/news/china-makes-ai-powered-robots-core-of-national-strategy (May 5, 2026, 2024 installations from World Robotics 2025)
  - https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years (World Robotics 2025)
- **License:** Press releases are publicly cite-able. Full World Robotics report is paywalled (~€800).

### 2. Humanoid funding rounds 2024-2026

- **Clean data:** `humanoid_funding_rounds.csv` — 12 entries
- **Key sources used:**
  - https://news.crunchbase.com/venture/ai-humanoid-robot-funding-apptronik/ (Feb 11, 2026 — Apptronik $520M + aggregate sector stats)
  - https://news.crunchbase.com/robotics/apptronik-startup-funding-humanoid-robots-goog/ (earlier Apptronik round)
  - Multiple secondary sources for Figure AI Series C, Skild AI, Physical Intelligence, 1X
- **Status:** All rows currently `verified: false`. Many depend on third-party aggregators (Lukas Ziegler tracking on X; Crunchbase News). For draft-ready citation, each company round should be cross-checked against the company's own press release or SEC filing. Tier 2 verification work.

### 3. Humanoid pricing snapshot

- **Clean data:** `humanoid_pricing_snapshot.csv`
- **Tier 1 confidence:**
  - **Unitree G1 $13,500** — directly verified from unitree.com/g1 product page (`verified: true`)
  - **Tesla Optimus current $50-100K / target <$30K** — from Q1 2026 earnings call coverage. Need a direct Tesla source (10-Q, earnings call transcript) to flip to `verified: true`.
  - Apptronik Apollo / Figure 02 / 1X NEO — no public pricing
- **Cost-curve implication:** the commodity floor is already at $13.5K (Unitree G1, shipping). The frontier per-unit-cost is at the Tesla / Figure / Apptronik tier ($50-150K range). The 5-10× spread is the article's "robot-cost decline" wedge.

### 4. Policy + production milestones

- **Clean data:** `humanoid_policy_milestones.csv` — 9 events covering China MIIT (Nov 2023 roadmap + Feb 2026 standards) and Tesla guidance (Q1 2026 earnings).
- **Key sources used:**
  - https://www.scmp.com/news/china/politics/article/3240259/china-says-humanoid-robots-are-new-engine-growth-pushes-mass-production-2025-and-world-leadership (SCMP coverage of MIIT)
  - https://www.therobotreport.com/china-plans-to-mass-produce-humanoids-by-2025/
  - https://www.uscc.gov/sites/default/files/2024-10/Humanoid_Robots.pdf (US-China Economic and Security Review Commission report)
  - https://seekingalpha.com/news/4578385-tesla-signals-over-25b-2025minus-2026-capex-as-it-targets-optimus-production-by-late-july (Tesla Q1 2026)

---

## Initial analytical observations

These observations are for the thesis pass, NOT verbatim citations.

1. **The "China leads in volume; Korea leads in density" split is critical for the macro section.** 54% of all 2024 industrial-robot installations went to China (~295K of ~547K global), but China's per-10K-employee density is only 166 — rank 22 globally. Korea (1,220), Singapore (818), Germany (449), Japan (446) lead density. Interpretation: China is undergoing the deployment phase RIGHT NOW; mature economies have already reshaped their factories. For the article, this means China's installation ramp continues for years, while Western/Korean/Japanese density rises modestly.

2. **The "China builds, China deploys, China supplies" trifecta is reaching critical mass.** Domestic Chinese supplier share went 30% → 57% (industrial) / 59% (electronics) / 85% (metal+machinery) over 2020-2024. China is no longer an import-dependent robotics market. This is the policy-incentive-success story to cite in Section 2.

3. **Robotics funding 2024→2025 nearly doubled ($8.2B → $14B).** This is the cleanest single capex datapoint for the macro section. It exceeded the 2021 peak ($13.1B) — meaning 2025 is the new high for robotics capital allocation.

4. **The Tesla guidance reduction is a signal worth recording.** Musk DECLINED to provide a 2026 Optimus production target in the Q1 2026 earnings call. Earlier (2024-2025) guidance had been "thousands by year end." Combined with current unit cost of $50-100K and target of <$30K, this suggests the cost curve is steeper than the company can ramp through quickly. This is the "execution layer clip" in real-time.

5. **Skild AI's $14B valuation matters for VLA story.** Skild's pitch is "cross-embodiment AI brain" — a software-only play that can be deployed across multiple humanoid hardware platforms. $1.4B at $14B is the market saying: the AI brain is worth more than the hardware. This is foreshadowing of the AI/robotics marriage point.

6. **The Unitree G1 retail at $13.5K is the cost-floor anchor.** Commodity humanoid hardware is already cheaper than the average US car. The reason production isn't 10M units/year already: the *software* (autonomy, dexterity, reliability) isn't there yet. This is a major insight for Leg 3 (execution layer): reliability/VLA is the binding constraint, not hardware cost.

7. **Western Europe robot density at 267 (+3%) suggests density saturation is well underway in advanced economies.** With Korea at 1,220 and Singapore at 818, the absolute ceiling on industrial-robot density isn't far above current US/EU levels. Volume growth for traditional industrial robots will increasingly come from middle-income economies (China, India, Mexico, Vietnam).

---

## What's NOT yet pulled (Tier 2)

| Source | What it covers | Effort |
|---|---|---|
| LEG2_IFR_EXEC_SUMMARY_2024 (deep-read) | Granular country-by-country installations 2018-2023 + sector breakdown | 30-60 min (need pdftotext / PDF parsing) |
| Figure AI Series C primary source | Verify $1B / $39B figures from company announcement | 15 min |
| Physical Intelligence Series B primary source | Verify $600M figure + announce date | 15 min |
| 1X Technologies funding update | Latest closed (not "pursuing") | 15 min |
| Tesla Q1 2026 earnings call transcript / 10-Q | Verify Optimus cost figures, capex allocation | 30 min |
| China MIIT 2023 roadmap official text (in English) | Direct quote, not via SCMP | 30 min |
| LEG2_VLA_BENCHMARKS | RT-2, RT-X, OpenVLA, π0 capability progression | 60-90 min — most fragmented data |
| LEG2_GOLDMAN_HUMANOID_TAM | Goldman humanoid TAM forecast (as contrasting "industry forecast") | 15 min if accessible |
| Boston Dynamics / Atlas commercial deployment | Hyundai parent context | 30 min |

**Recommendation:** Tier 2 verification is "must-do before drafting" but not "blocking on Leg 3." Tier 1 is already enough to argue the Leg 2 thesis qualitatively.

---

## Source-tracker updates

In `sources.md`:
- `LEG2_IFR_WORLD_ROBOTICS` → `pulled` (headline figures from press releases; exec summary PDF downloaded; full report still paywalled)
- `LEG2_HUMANOID_FUNDING` → `pulled` (Tier 1 aggregate; per-round primary verification pending)
- `LEG2_UNITREE_PRICING` → `pulled` + `verified` (direct from product page)
- `LEG2_CHINA_MIIT_HUMANOID` → `pulled` (via SCMP/Robot Report secondary sources; primary MIIT doc text pending)
- New source rows to add: TSLA_2026_Q1_EARNINGS, IFR specific press releases (with dates), Crunchbase News articles, USCC Humanoid Robots report.
