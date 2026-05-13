# Data — AI × Robotics Article

Raw data series feeding the article's charts and projections.

**Layout:** one folder per leg. Each folder has its own README documenting what series live there, their schema, and their `source_id` in `../sources.md`.

```
data/
├── README.md                              (this file)
├── leg1_ai_capability_cost/               AI capability + cost trends
│   ├── README.md
│   └── notable_models_training_compute.csv   (example series — schema demo)
├── leg2_robotics_deployment_cost/         Industrial + humanoid robotics
│   └── (to be populated)
├── leg3_execution_layer/                  Grid, manufacturing, reliability, demographics, regulation
│   └── (to be populated)
├── leg4_macro_forces/                     Capex, sovereign funds, fiscal, monetary
│   └── (to be populated)
└── cohort_map/                            Labor segment sizing + timeline
    └── (to be populated)
```

---

## Naming conventions

- File names: `{series_slug}.csv` — lowercase, underscores, no spaces.
- Cleaned variants: `{series_slug}_clean.csv` with a `{series_slug}_README.md` documenting the cleanup.
- Schema documented in each leg's README, not inferred from column headers.

## Schema commitments

Every data CSV in this tree has these mandatory columns:

| Column | Meaning |
|---|---|
| `source_id` | Links to a row in `../sources.md`. Required on every row. |
| `confidence` | `high` / `medium` / `low` per the source. |
| `verified` | `true` once the value has been cross-checked against the canonical source. Starts `false`. |
| `notes` | Caveats, methodology comments, "PENDING X" markers. |

Plus series-specific columns documented in each leg's README.

## What goes in `data/` vs what doesn't

**Belongs here:**
- Raw CSV/TSV downloads from primary sources
- Cleaned/normalized derivatives (paired with a README)
- Per-claim spreadsheets we build by hand (e.g., humanoid funding rounds aggregated)

**Does NOT belong here:**
- Working notes (those go in the article folder root)
- Charts (rendered separately for the article)
- PDFs (those go in `../sources_archive/` if we need to preserve a PDF)
