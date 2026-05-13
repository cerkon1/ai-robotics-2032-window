# Leg 2 — Robotics deployment/cost

Industrial + humanoid robotics data feeding Section 1's "Robot deployment/cost" curve.

## Planned series

| File | Topic | Source(s) | Status |
|---|---|---|---|
| `ifr_industrial_robots_topline.csv` | Annual installations + stock + density by country | LEG2_IFR_WORLD_ROBOTICS | Pulled (Tier 1, headline figures from press releases) |
| `humanoid_funding_rounds.csv` | Capex flowing to humanoid robotics startups 2024-2026 | LEG2_HUMANOID_FUNDING | Pulled (Tier 1) |
| `humanoid_pricing_snapshot.csv` | Retail / disclosed / estimated unit prices by company | LEG2_UNITREE_PRICING + Tesla disclosures + others | Pulled (Tier 1) |
| `humanoid_policy_milestones.csv` | China MIIT roadmap + Tesla guidance + Apptronik / Figure commercial milestones | LEG2_CHINA_MIIT_HUMANOID + earnings call data | Pulled (Tier 1) |
| `vla_benchmarks.csv` | RT-2, RT-X, OpenVLA, π0 capability progression | LEG2_VLA_BENCHMARKS | Not yet pulled |
| `ifr_full_dataset.csv` | Full historical installations + stock + density (paid-report data) | LEG2_IFR_WORLD_ROBOTICS | Partial — exec summary PDF available, full DB paywalled |

## Schema commitments

Same rules as Leg 1: every CSV has `source_id`, `confidence`, `verified`, `notes`.

For humanoid funding rounds in particular, `verified` flips `true` only when the figure is from a primary source (company announcement, SEC filing) or a credible third-party (Crunchbase, SEC, Reuters). Aggregate sums quoted second-hand without primary attribution stay `verified: false`.

## Data anchors (key figures captured)

**Industrial robotics (IFR World Robotics 2025 report, covering 2024 data):**
- Global operational stock: ~4.3M+ (2023 figure 4,281,585; 2024 expected to push ~4.7M)
- 2023 annual installations: 541,302 units
- 2024 annual installations: 54% in China alone — ~295,000 China + ~252,000 RoW ≈ 547,000 total estimated
- Top 5 countries by 2023 installs: China (281K), Japan (46K), US, Korea, Germany (28K)
- Robot density 2024: Korea 1,220 / Singapore 818 / Germany 449 / Japan 446 / US 307 / China 166
- Western Europe 267 (+3% YoY) / North America 204 (+4% YoY) / Asia 131 (+11% YoY)

**Humanoid funding 2024-2026:**
- 2024 aggregate robotics funding: $8.2B
- 2025 aggregate robotics funding: ~$14B (+70%)
- 2025 exceeded 2021 peak of $13.1B
- Headline 2025 rounds: Figure AI $1B+ Series C at $39B post-money, Skild AI $1.4B (announced Jan 2026), Physical Intelligence $600M Series B, Apptronik $935M total ($415M Series A + $520M extension Feb 2026)
- 1X Technologies reportedly pursuing up to $1B

**Unit cost reference points (2026):**
- Unitree G1 (commodity humanoid): $13.5K USD retail
- Tesla Optimus current cost: $50K-$100K per unit; initial commercial pricing $100K-$150K; target <$30K
- Apptronik Apollo: no public pricing disclosed
- Figure 02: no public pricing disclosed

**Policy / production targets:**
- China MIIT (2023 roadmap): mass production by 2025; world leadership + integrated economy by 2027
- China MIIT (Feb 2026): first national standard system for humanoid robots and embodied intelligence published
- Tesla Q1 2026: Optimus production begins Fremont late July/August 2026; second factory Giga Texas summer 2027; Musk declined to provide 2026 production target
- Tesla capex >$25B for 2026 (3x 2025)
