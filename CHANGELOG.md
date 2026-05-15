# Changelog

All notable changes to this data appendix.

This file follows the spirit of [Keep a Changelog](https://keepachangelog.com/) — material additions, corrections, and revisions are tagged. Per the methodology commitment, any thesis-invalidating finding triggers a 60-day retraction window; smaller corrections are tagged as `vX.Y-errata-<topic>`.

The data freeze date for the original publication is documented in [`methodology.md`](methodology.md). Updates after the freeze date are flagged below.

---

## [v1.1] — 2026-05-15 — Debt-trajectory chart + Part 2 supporting data

### Added
- **Chart 12** — *Four 2026 US macro flows, on one axis* (`data/charts/chart_12_macro_flows.png`). Horizontal bar chart comparing Mag7 capex 2026 ($738B), Cohort 1-3 aggregate wages 2024 ($690B), US federal deficit FY26 ($1.9T), and M2 trailing-12-month expansion ($1.6T). The matched-magnitude pair (capex ≈ wages) is highlighted with a bracket annotation. Used in Part 2 §2.2 as the article's structural-spine claim.
- **Chart 13** — *US federal debt vs the 1946 peacetime peak* (`data/charts/chart_13_debt_trajectory.png`). Time-series 1946-2036, solid navy historical line + dashed orange CBO projection + red dotted reference line at the 1946 peak (106.1%). Annotations: 1946 peak / 1974 trough / FY2030 breach (107.7%) / FY2036 endpoint (120%). Used in Part 2 §2.2.
- **CSV** — `data/leg4_macro_forces/us_debt_to_gdp_1946_2036.csv` (92 rows). Annual historical 1946-2024 from FRED FYPUGDA188S (via Multpl mirror — direct FRED CSV download blocked from the build environment per methodology note); CBO Feb 2026 baseline 2025-2036 with 4 published anchor years (FY25/26/30/36) plus linear-interpolated intermediate years flagged `verified: false` in the CSV.
- **Sources** — two new rows in `sources.md` Leg 4 section:
  - `LEG4_DEBT_HISTORICAL` — FRED FYPUGDA188S historical series (cited).
  - `LEG4_CBO_BASELINE` — CBO Feb 2026 anchor years cross-referenced via American Action Forum + CRFB summaries (cited).
- **Build pipeline** — `data/charts/build_charts.py` extended with `chart_12_macro_flows()` and `chart_13_debt_trajectory()` functions; `__main__` runner now produces 13 charts (was 11). Pipeline remains idempotent.
- **CHANGELOG.md** — this file. README's commitment to maintain post-publish errata documentation is now actually being maintained.

### Changed
- **`README.md`** — chart-count references updated from 11 to 13 (file-tree comment + reproduce-charts paragraph). Status line bumped from `v1.0` to `v1.1`. Part 1 link in the articles table replaced placeholder with the published Substack URL ([cerkon.substack.com/p/the-2032-window](https://cerkon.substack.com/p/the-2032-window)).
- **`sources.md`** — `LEG4_CBO_DEFICIT` row corrected: prior text described "100%→118%(2035)→120%(2036), passes 1946 WWII peak" — now corrected to "99% (FY25) → 108% (FY30, breaches 1946 peacetime peak of 106.1%) → 120% (FY36)" matching CBO Feb 2026's own framing of FY2030 as "a new record." Status changed from `pulled` to `cited`.
- **`data/leg4_macro_forces/README.md`** — added new debt-trajectory CSV row to the planned-series table; corrected the CBO anchor findings section to lead with the FY2030 breach year (was FY2035 in v1.0); added a debt-to-GDP anchor-findings block listing 1946/1974/2008/2020/2024 historical values plus the CBO baseline path.

### Why the breach-year correction
The v1.0 publication used "118% by 2035" as the headline framing, derived from an earlier-CBO-baseline-aligned sketch. CBO's actual February 2026 publication — pulled and verified during Chart 13 production — projects the literal first-crossing of the 1946 peacetime peak (106.1%) at fiscal year 2030 with debt-to-GDP at 107.7%, and CBO's own publication describes FY2030 as "a new record." Both framings are technically defensible (the 2035 version emphasizes how *much* above the record we will be; the 2030 version emphasizes *when* the line first crosses). The corrected framing aligns the data appendix with CBO's own publication and with the Part 2 article prose.

This is a methodological correction, not a thesis revision — the underlying argument (peacetime debt record breach within the analyst horizon, financed at a level that aligns with the K-shape framing) is unchanged and arguably strengthened by the earlier breach year.

### Not changed (intentional)
- All v1.0 data files unchanged (Mag7 capex, Stargate, M2, K-shape, demographics, METR, Epoch, IFR, etc.). Chart 12's wage-side input is the existing `data/cohort_map/cohort_map_us_occupations.csv` row data — no modification, just a new derived aggregate documented in the chart caption.
- `methodology.md` and the public `THESIS.md` unchanged. The methodology framework was correct; only one downstream data point needed a corrected anchor.

---

## [v1.0] — 2026-05-13 — Original publication state

### Initial release
- 11 production charts (`chart_01` through `chart_11`) covering all four legs of the thesis: AI capability/cost (Charts 1, 2), robotics deployment (Chart 3), execution-layer constraints (Charts 4-7), and macro forces (Chart 8) plus K-shape outcomes (Charts 9-11).
- 25 source CSVs across the five `data/leg*/` and `data/cohort_map/` and `data/checkpoints/` directories.
- Python build pipeline (`data/charts/build_charts.py` + `data/charts/article_style.py`) producing all 11 PNGs at 200 DPI from the underlying CSVs. Pipeline is idempotent and self-contained against the included CSVs.
- 35 falsifiable predictions in `data/checkpoints/falsifiable_checkpoints.csv` across 2026/2028/2030/2032/2035 horizons + 5 explicit failure criteria.
- Full thesis (`THESIS.md`), methodology (`methodology.md`, 11 sections), and source tracker (`sources.md`, 30+ source rows).
- CC0-licensed derivative work (CSV cleaning, chart code, methodology, analytical notes); upstream sources retain their original licenses.

### Repo metadata
- 57 files / ~6.5 MB at initial publication
- Three initial commits: `1bf6b2e` (initial), `2e9d4b3` (initial publication state — data appendix v1.0), `091816b` (cleaned `THESIS.md` for public repo from 168-line working version to 45-line reader-facing version).

---

## Versioning policy

Per the README's versioning section:

- **Major.minor** — `vX.Y` for additive content (new charts / new CSVs / new sources); the chart pipeline must remain idempotent and existing data unchanged unless a correction is documented above.
- **Errata tags** — `vX.Y-errata-<topic>` for material corrections to existing data. Documented above with explicit `### Why` rationale.
- **Retraction trigger** — if any of the 5 failure criteria in `data/checkpoints/falsifiable_checkpoints.csv` fires before its stated horizon, the methodology commits to a published retraction within 60 days. That would be tagged `vX.Y-retraction-<topic>` with a top-level `### Retraction notice` entry above.

The data freeze date in `methodology.md` §11.3 (2026-04-30) applies to the v1.0 release. Any post-freeze additions in v1.1+ are noted in the entry above.
