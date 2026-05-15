# The 2032 Window — Data Appendix

**Article series:** *The 2032 Window: When AI and Robotics Cross the Cost-of-Labor Line*
**Author:** Cerkon (Substack: [cerkon.substack.com](https://cerkon.substack.com))
**Status:** v1.1 — Part 1 published 2026-05-15; debt-trajectory chart + macro-flows chart + supporting CSV added in this revision (see [`CHANGELOG.md`](CHANGELOG.md))

This repository is the data appendix for a three-part Substack series. Every numeric claim in the articles maps to a CSV row here. Every chart is reproducible from the included Python pipeline.

The premise: if you disagree with the analysis, you can disagree from the same starting point.

---

## The articles

| Part | Title | Substack link |
|------|-------|---------------|
| 1 | The Trajectory | [cerkon.substack.com/p/the-2032-window](https://cerkon.substack.com/p/the-2032-window) |
| 2 | The Macro Forces — Who's Paying, and Why | <TK> |
| 3 | K-Shape and Positioning — Where You'll Be Standing | <TK> |

The series argues that AI capability + robotics cost + execution-layer constraints + macroeconomic forces converge on a 2028-2035 window for at-scale substitution of specific US labor cohorts. The full thesis is in [`THESIS.md`](THESIS.md). The methodology — projection rules, confidence tiers, data-freeze cutoff, retraction policy — is in [`methodology.md`](methodology.md).

---

## What's in this repository

```
.
├── THESIS.md                # Canonical 1-paragraph thesis + 4-section outline
├── methodology.md           # 11 sections: projection rules, confidence tiers, retraction policy
├── sources.md               # 30+ source rows, status-tracked (proposed / pulled / verified / cited)
├── data/
│   ├── README.md            # Data folder index
│   ├── charts/              # 13 production charts + Python build pipeline
│   │   ├── build_charts.py
│   │   ├── article_style.py
│   │   └── chart_NN_*.png   # Rendered charts (200 DPI)
│   ├── checkpoints/         # 35 falsifiable predictions across 2026-2035 horizons
│   ├── cohort_map/          # US labor cohort taxonomy + occupational wages + CPI components
│   ├── leg1_ai_capability_cost/        # METR autonomy benchmark + Epoch AI compute data
│   ├── leg2_robotics_deployment_cost/  # IFR industrial robotics + humanoid funding/pricing/policy
│   ├── leg3_execution_layer/           # Grid / manufacturing / AV reliability / demographics / regulation
│   └── leg4_macro_forces/              # Mag7 capex / K-shape labor share / scarce-asset performance
```

Each `leg*/` folder contains a `README.md` describing the data sources for that leg and a `RESEARCH_NOTES.md` documenting analytical observations.

---

## How to verify a claim

1. Find the chart or numeric claim in the article.
2. The chart caption names the data file (e.g., "Source: Epoch AI Notable AI Models database — 147-model regression").
3. Locate the corresponding CSV in this repo ([`sources.md`](sources.md) maps source name → file path).
4. Inspect the row. Every CSV has a `verified` column flagging whether the value has been confirmed against primary source (`true`) or carries derivation uncertainty (`false`).

If you find a discrepancy, please [open an issue](../../issues/new). Documented errata appear in `CHANGELOG.md` (post-publish).

---

## How to reproduce the charts

```bash
git clone https://github.com/cerkon1/ai-robotics-2032-window.git
cd ai-robotics-2032-window/data/charts
pip install pandas matplotlib
python build_charts.py
```

This regenerates all 13 PNGs into `data/charts/`. The pipeline is idempotent — outputs are byte-comparable across runs on the same input data.

Current settings produce: Mag7 capex hockey-stick ending at $738B for 2026, AI compute scaling at 2.2×/yr (broad frontier) / 3.1×/yr (top-10%), working-age population projections indexed to 2024 for 7 countries, scarce-asset performance 2015-2024 with Bitcoin at 258× on a log Y-axis, the K-shape since 2000 (labor share −4.5pp / S&P 500 TR ~8.3×), the four 2026 macro flows on one axis (Mag7 capex $738B / Cohort 1-3 wages $690B / federal deficit $1.9T / M2 trailing-12 $1.6T), and US federal debt 1946-2036 with the 1946 peacetime peak (106.1%) breached on the CBO Feb 2026 baseline at FY2030 (107.7%). If you re-run with updated source data (e.g., 2027 10-Ks), update the corresponding CSVs and re-run; the chart code does not need to change.

---

## Falsifiable predictions

[`data/checkpoints/falsifiable_checkpoints.csv`](data/checkpoints/falsifiable_checkpoints.csv) contains 35 specific predictions across 2026 / 2028 / 2030 / 2032 / 2035 horizons, plus 5 explicit failure criteria that would invalidate the thesis.

The author has committed to a public scoring in May 2027 (against the 2026 checkpoints) and a 60-day retraction if any failure criterion fires.

---

## Licensing

**This repository's derivative work** (CSV cleaning, chart code, methodology, analytical notes) is dedicated to the public domain under [Creative Commons Zero (CC0 1.0)](LICENSE). No attribution required for the derivative; reuse freely.

**Upstream data sources retain their original licenses.** When citing data that originates from a third party, please credit the original source per their license:

| Source | License | Required attribution |
|--------|---------|----------------------|
| Epoch AI (Notable AI Models database) | CC BY 4.0 | "Epoch AI, *Data on Notable AI Models*, https://epoch.ai/data/notable-ai-models" |
| UN World Population Prospects 2024 | CC BY 3.0 IGO | "UN DESA Population Division, *World Population Prospects 2024*" |
| IFR World Robotics | Press-release fair use | "International Federation of Robotics, World Robotics 2024 / 2025 press releases" |
| IEA Energy and AI Special Report | © OECD/IEA | Cite as analysis source; reproduction of full report restricted |
| LBNL Queued Up 2025 Edition | US-government work | "Lawrence Berkeley National Laboratory, *Queued Up: 2025 Edition*" |
| Stanford AI Index 2025 | CC BY-ND 4.0 | "Stanford HAI, *AI Index Report 2025*" |
| US BLS data | Public domain | "US Bureau of Labor Statistics, OEWS May 2024 / CPI components" |
| FRED time series | Free public domain | "Federal Reserve Bank of St. Louis, FRED [series ID]" |
| Visual Capitalist / CNBC / Wolf Street aggregations | Fair-use citation | Original publisher credited in CSV `notes` column |

Full attribution chain per data file is in the `notes` column of each CSV and the corresponding `leg*/README.md`.

**Why CC0 for the derivative work:** the analytical value is in the synthesis and reproducibility — not in restricting reuse. A reader who finds this useful should be free to remix it without legal friction. The upstream attribution chain matters; my derivative does not.

---

## Citation

If you reference this appendix, the suggested format is:

> Cerkon. *The 2032 Window: When AI and Robotics Cross the Cost-of-Labor Line — Data Appendix.* GitHub: cerkon1/ai-robotics-2032-window. Published 2026-MM-DD.

---

## Contact

- **Substack:** [cerkon.substack.com](https://cerkon.substack.com)
- **Corrections / errata:** [open a GitHub issue](../../issues/new)
- **Other:** see Substack contact

---

## Versioning

This repo follows a frozen-at-publish + tagged-errata model:

- `v1.0` — original publication state
- Tags will be cut for material corrections (e.g., `v1.1-errata-chart8`) with a CHANGELOG entry
- The 60-day retraction commitment from `methodology.md` §11 applies to material thesis-invalidating findings

The data freeze date is documented in `methodology.md`. Updates made after the freeze date will be flagged in the CHANGELOG.
