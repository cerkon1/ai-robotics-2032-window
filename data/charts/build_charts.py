"""
Build all 11 article charts as PNG files for The 2032 Window article.

Run from anywhere:
  python build_charts.py

Outputs to data/charts/chart_NN_<name>.png
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Make article_style importable
sys.path.insert(0, str(Path(__file__).parent))
from article_style import apply_style, add_source, add_subtitle, add_annotation_box, set_titles, PALETTE, CATEGORICAL

apply_style()

# Base paths
ROOT = Path(__file__).parent.parent  # data/
CHARTS = Path(__file__).parent  # data/charts/

# ----------------------------------------------------------------------
# Chart 1 — METR autonomy doubling
# ----------------------------------------------------------------------
def chart_1_metr():
    df = pd.read_csv(ROOT / 'leg1_ai_capability_cost' / 'metr_autonomy_horizons.csv')
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df = df.dropna(subset=['release_date', 'p50_horizon_minutes']).copy()
    df['p50'] = pd.to_numeric(df['p50_horizon_minutes'], errors='coerce')
    df = df.dropna(subset=['p50'])

    fig, ax = plt.subplots()
    sota = df[df['is_sota'] == True]
    nonsota = df[df['is_sota'] != True]
    ax.scatter(nonsota['release_date'], nonsota['p50'], s=50, c=PALETTE['secondary'], alpha=0.5, edgecolor='white', linewidth=0.5, label='Non-SOTA')
    ax.scatter(sota['release_date'], sota['p50'], s=90, c=PALETTE['primary'], edgecolor='white', linewidth=0.8, label='State-of-the-art at release')

    # Doubling trend lines
    # 6.2-mo (187.8d) anchored at GPT-2 (2019-02-14), spans whole period
    anchor_alltime = pd.Timestamp('2019-02-14')
    anchor_alltime_val = 0.054
    df_sorted = df.sort_values('release_date')
    days_alltime = (df_sorted['release_date'] - anchor_alltime).dt.days
    ax.plot(df_sorted['release_date'], anchor_alltime_val * np.power(2.0, days_alltime / 187.8),
            '--', color=PALETTE['accent'], alpha=0.6, linewidth=1.5, label='6.2-month doubling (2019-2026 fit)')

    # 4.2-mo (128.7d) anchored at GPT-4 (Mar 2023), spans 2023 onward only
    anchor_2023 = pd.Timestamp('2023-03-14')
    anchor_2023_val = 4.0
    from_2023_df = df_sorted[df_sorted['release_date'] >= anchor_2023].copy()
    days_from_2023 = (from_2023_df['release_date'] - anchor_2023).dt.days
    ax.plot(from_2023_df['release_date'], anchor_2023_val * np.power(2.0, days_from_2023 / 128.7),
            '--', color=PALETTE['danger'], alpha=0.7, linewidth=1.5, label='4.2-month doubling (2023 onward fit)')

    # Annotate key SOTA models. Note: most post-2023 frontier model IDs in the CSV
    # carry an `_inspect` suffix — keys here must match exactly or the lookup
    # silently no-ops.
    key_models = {
        'gpt2':                                ('GPT-2',           (-50,   6)),
        'davinci_002':                         ('GPT-3',           (-40, -16)),
        'gpt_4':                               ('GPT-4',           (  8,   8)),
        'gpt_4o_inspect':                      ('GPT-4o',          (-25, -22)),
        'claude_3_5_sonnet_20240620_inspect':  ('Claude 3.5',      ( 10, -16)),
        'o1_inspect':                          ('o1',              ( 10,   8)),
        'claude_3_7_sonnet_inspect':           ('Claude 3.7',      (-75,   8)),
        'o3_inspect':                          ('o3',              ( 10,  -6)),
        'gpt_5_2025_08_07_inspect':            ('GPT-5',           ( 10,   8)),
        'claude_opus_4_6_inspect':             ('Opus 4.6',        (-65,   8)),
        'claude_mythos_preview_early_inspect': ('Mythos',          (-55,  10)),
    }
    for model_key, (label, offset) in key_models.items():
        row = df[df['model_id'] == model_key]
        if not row.empty:
            r = row.iloc[0]
            ax.annotate(label, (r['release_date'], r['p50']),
                        xytext=offset, textcoords='offset points',
                        fontsize=8.5, color=PALETTE['text'], weight='bold',
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.85))

    ax.set_yscale('log')
    ax.set_ylim(0.01, 5000)
    ax.set_xlabel('Model release date')
    ax.set_ylabel('p50 task horizon (minutes, log scale)')

    # Reference horizontal lines for human-readable thresholds.
    # All labels anchored on the LEFT in a vertical stack — the dense 2025-2026
    # SOTA cluster sits on the right and would collide with right-anchored
    # reference text. The 17-hr line carries the headline emphasis (dashed
    # accent color, bold), the rest are subdued (solid axis-gray, normal).
    for y_val, label_text in [(1, '1 min'), (60, '1 hr'), (480, '1 work-day (8 hr)'), (1020, '17 hr task horizon')]:
        is_headline = (y_val == 1020)
        ax.axhline(
            y=y_val,
            color=PALETTE['accent'] if is_headline else PALETTE['axis'],
            linewidth=1.1 if is_headline else 0.5,
            alpha=0.7 if is_headline else 0.5,
            linestyle='--' if is_headline else '-',
        )
        ax.text(
            pd.Timestamp('2019-03-01'), y_val * 1.15, label_text,
            fontsize=9 if is_headline else 8,
            color=PALETTE['accent'] if is_headline else PALETTE['secondary'],
            style='italic',
            weight='bold' if is_headline else 'normal',
            ha='left',
        )

    set_titles(ax,
               'AI task autonomy: 3 seconds to 17 hours in 7 years',
               'p50 task horizon at 50% success — METR-Horizon-v1.1 benchmark')
    ax.legend(loc='lower right', fontsize=9, framealpha=0.95, facecolor='white', edgecolor=PALETTE['grid'], frameon=True)

    add_source(fig, 'METR (Model Evaluation and Threat Research) — METR-Horizon-v1.1 benchmark, 26 frontier models')
    plt.savefig(CHARTS / 'chart_01_metr_autonomy.png')
    plt.close()
    print('Chart 1 saved.')


# ----------------------------------------------------------------------
# Chart 2 — Frontier training compute scaling
# ----------------------------------------------------------------------
def chart_2_compute():
    df = pd.read_csv(ROOT / 'leg1_ai_capability_cost' / 'epoch_frontier_post2017.csv')
    df['Publication date'] = pd.to_datetime(df['Publication date'], errors='coerce')
    df = df.dropna(subset=['Publication date'])
    df['compute'] = pd.to_numeric(df['Training compute (FLOP)'], errors='coerce')
    df = df.dropna(subset=['compute'])
    df = df[df['compute'] > 1e22]

    # Regression on log10(compute) vs year (decimal)
    df['year_numeric'] = df['Publication date'].dt.year + (df['Publication date'].dt.dayofyear - 1) / 365.25
    df['log10_compute'] = np.log10(df['compute'])
    slope, intercept = np.polyfit(df['year_numeric'], df['log10_compute'], 1)
    y_pred = slope * df['year_numeric'] + intercept
    ss_res = ((df['log10_compute'] - y_pred) ** 2).sum()
    ss_tot = ((df['log10_compute'] - df['log10_compute'].mean()) ** 2).sum()
    r_squared = 1 - ss_res / ss_tot
    mult_per_year = 10 ** slope
    doubling_months = (np.log10(2) / slope) * 12

    # Top-10% per year regression (true frontier-of-frontier)
    df['year_int'] = df['Publication date'].dt.year
    top = df.groupby('year_int').apply(lambda x: x.nlargest(max(1, int(len(x) * 0.10)), 'compute'), include_groups=False).reset_index(drop=True)
    slope_top, intercept_top = np.polyfit(top['year_numeric'], top['log10_compute'], 1)
    mult_top = 10 ** slope_top

    fig, ax = plt.subplots()
    df['country_group'] = df['Country (of organization)'].apply(
        lambda c: c if c in ['United States of America', 'China'] else (
            'European Union' if isinstance(c, str) and any(eu in c for eu in ['Germany', 'France', 'UK', 'United Kingdom', 'Netherlands', 'Israel']) else 'Other'
        )
    )
    colors = {'United States of America': PALETTE['primary'], 'China': PALETTE['danger'], 'European Union': PALETTE['accent'], 'Other': PALETTE['secondary']}
    labels = {'United States of America': 'United States', 'China': 'China', 'European Union': 'EU / UK / Israel', 'Other': 'Other'}

    for grp, sub in df.groupby('country_group'):
        ax.scatter(sub['Publication date'], sub['compute'], s=38, c=colors.get(grp, PALETTE['secondary']),
                   alpha=0.55, edgecolor='white', linewidth=0.4, label=labels.get(grp, grp))

    # Regression trend line — full frontier subset
    year_min = df['year_numeric'].min()
    year_max = df['year_numeric'].max()
    year_pts = np.linspace(year_min - 0.1, year_max + 0.3, 50)
    log_pts = slope * year_pts + intercept
    date_pts = [pd.Timestamp(f'{int(y)}-01-01') + pd.Timedelta(days=(y - int(y)) * 365.25) for y in year_pts]
    ax.plot(date_pts, 10 ** log_pts, '-', color=PALETTE['text'], linewidth=2.0, alpha=0.85,
            label=f'All-frontier fit: {mult_per_year:.1f}x/yr  (R²={r_squared:.2f})')

    # Top-10% per year trend line
    log_pts_top = slope_top * year_pts + intercept_top
    ax.plot(date_pts, 10 ** log_pts_top, '--', color=PALETTE['danger'], linewidth=2.0, alpha=0.85,
            label=f'Top-10% per year fit: {mult_top:.1f}x/yr')

    # Annotate frontier models — exact match on Model column so labels point to
    # the historical model the text references, not a later family member with
    # higher compute. (Previously str.contains('GPT-3') matched GPT-3.5 too,
    # which has higher compute, so "GPT-3" label landed on the 2022 davinci-002
    # dot instead of the 2020 GPT-3 dot. Same class of bug for GPT-4 / PaLM.)
    key = {
        'GPT-3 175B (davinci)': 'GPT-3',
        'PaLM (540B)':          'PaLM',
        'GPT-4 (Mar 2023)':     'GPT-4',
        'GPT-4.5':              'GPT-4.5',
        'Grok 4':               'Grok 4',
    }
    for model_exact, label in key.items():
        row = df[df['Model'] == model_exact].head(1)
        if not row.empty:
            r = row.iloc[0]
            ax.annotate(label, (r['Publication date'], r['compute']),
                        xytext=(7, 8), textcoords='offset points', fontsize=9, color=PALETTE['text'], weight='bold')

    ax.set_yscale('log')
    ax.set_xlabel('Publication date')
    ax.set_ylabel('Training compute (FLOPs, log scale)')
    set_titles(ax,
               'Frontier model training compute, 2017-2026',
               f'{len(df)} models in the post-2017 frontier subset — measured trend, not assumed')
    ax.legend(loc='upper left', fontsize=8.5, title='Origin / fit', title_fontsize=9, ncol=1)

    # Lift the bottom margin so "Publication date" sits clear of the source line.
    # (Source line is shorter now too — slope / R² duplicates the legend.)
    fig.subplots_adjust(bottom=0.16)
    add_source(fig, 'Epoch AI Notable AI Models database — 147-model regression')
    plt.savefig(CHARTS / 'chart_02_compute_scaling.png')
    plt.close()
    print(f'Chart 2 saved. (Trend: {mult_per_year:.2f}x/yr all frontier; {mult_top:.2f}x/yr top-10%; doubling ~{doubling_months:.1f} months)')


# ----------------------------------------------------------------------
# Chart 3 — Robot cost-tier vs cohort wages
# ----------------------------------------------------------------------
def chart_3_cost_vs_wages():
    df = pd.read_csv(ROOT / 'cohort_map' / 'cohort_map_us_occupations.csv')
    df = df[df['cohort'].isin([1, 2, 3, 4])].copy()
    df['hourly_wage_equiv'] = pd.to_numeric(df['hourly_wage_equiv'], errors='coerce')
    df = df.dropna(subset=['hourly_wage_equiv'])
    df = df.sort_values('hourly_wage_equiv', ascending=True)

    # Explicit short labels — no truncation
    label_map = {
        'Logisticians': 'Logisticians',
        'Electricians': 'Electricians',
        'Plumbers Pipefitters Steamfitters': 'Plumbers / Pipefitters',
        'Heavy and Tractor-Trailer Truck Drivers': 'Heavy truck drivers',
        'Auto Service Technicians and Mechanics': 'Auto mechanics',
        'Nursing Assistants': 'Nursing assistants',
        'Laborers and Freight/Stock/Material Movers Hand': 'Hand laborers / movers',
        'Janitors and Cleaners (except maids)': 'Janitors / cleaners',
        'Home Health Aides + Personal Care Aides': 'Home + personal care aides',
        'Fast Food and Counter Workers': 'Fast food / counter',
        'Stockers and Order Fillers': 'Stockers / order fillers',
        'Cooks Restaurant': 'Restaurant cooks',
        'Food Preparation Workers': 'Food prep workers',
        'Packers and Packagers Hand': 'Hand packers',
    }
    df['label'] = df['occupation_title'].map(lambda s: label_map.get(s, s[:28]))

    # Color by cohort
    cohort_colors = {1: PALETTE['danger'], 2: PALETTE['accent'], 3: PALETTE['tertiary'], 4: PALETTE['quaternary']}
    bar_colors = [cohort_colors[c] for c in df['cohort']]

    fig, ax = plt.subplots(figsize=(12, 7.5))
    bars = ax.barh(df['label'], df['hourly_wage_equiv'], color=bar_colors, alpha=0.85, edgecolor='white', linewidth=0.4)

    # Reference lines for robot tiers (staggered y-offset to avoid label collisions)
    tiers = [
        (2.65, 'Commodity\n$2.65/hr', PALETTE['success'], 2.0),
        (6.00, 'Target tier\n$6/hr', PALETTE['accent'], 1.0),
        (15.00, 'Initial commercial\n$15/hr', PALETTE['danger'], 2.0),
        (26.67, 'Frontier today\n$27/hr', '#4b5563', 1.0),
    ]
    for x, label, color, y_offset in tiers:
        ax.axvline(x=x, color=color, linestyle='--', linewidth=1.3, alpha=0.75)
        ax.text(x, len(df) - 0.5 + y_offset, label, ha='center', va='bottom', fontsize=8.5, color=color, weight='bold',
                bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor=color, linewidth=0.6, alpha=0.92))

    ax.set_xlim(0, 75)
    ax.set_ylim(-0.5, len(df) + 3.5)
    ax.set_xlabel('Hourly wage (USD)')
    ax.set_ylabel('')

    # Explainer arrow / annotation about what the vertical lines mean
    ax.annotate('Robot operating\ncost tiers (per hour)',
                xy=(15, len(df) + 1.8), xytext=(50, len(df) + 2.8),
                fontsize=9.5, color=PALETTE['text'], weight='bold', ha='center',
                arrowprops=dict(arrowstyle='->', color=PALETTE['text'], lw=1.2,
                                connectionstyle='arc3,rad=0.2'))

    set_titles(ax,
               'Cost is not the bottleneck. Reliability is.',
               'US occupational median wages vs fully-loaded robot operating cost per hour')

    # Manual cohort legend
    cohort_labels = {1: 'Cohort 1 (warehouse / logistics)', 2: 'Cohort 2 (cleaning / food)', 3: 'Cohort 3 (skilled trades)', 4: 'Cohort 4 (care / nursing)'}
    handles = [plt.Rectangle((0, 0), 1, 1, color=cohort_colors[k], alpha=0.85) for k in [1, 2, 3, 4]]
    ax.legend(handles, [cohort_labels[k] for k in [1, 2, 3, 4]], loc='lower right', fontsize=9, title='Labor cohort', title_fontsize=9)

    add_source(fig, 'BLS Occupational Employment and Wage Statistics May 2024; robot cost tiers from Unitree retail + Tesla Q1 2026 disclosed ranges')
    plt.savefig(CHARTS / 'chart_03_robot_vs_wages.png')
    plt.close()
    print('Chart 3 saved.')


# ----------------------------------------------------------------------
# Chart 4 — Grid constraint (two-panel)
# ----------------------------------------------------------------------
def chart_4_grid():
    # Panel A: wait-time evolution (top)
    # Panel B: data center electricity scenarios (bottom)
    fig, (axA, axB) = plt.subplots(2, 1, figsize=(10, 11), gridspec_kw={'height_ratios': [1, 1.3], 'hspace': 0.5})

    # Panel A: wait time bars + queue capacity context.
    # Bar labels match the underlying LBNL data: <2 years for 2000-2007 (the
    # earlier value is bounded ABOVE by 2 years, not below); >4 years for 2018-2024.
    wait_periods = ['2000-2007', '2018-2024']
    wait_vals = [2, 4]
    wait_labels = ['<2 years', '>4 years']
    bar_colors_A = [PALETTE['success'], PALETTE['danger']]
    bars = axA.bar(wait_periods, wait_vals, color=bar_colors_A, alpha=0.85, edgecolor='white', linewidth=0.6, width=0.55)
    axA.set_ylabel('Median wait time (years)')
    axA.set_xlabel('Project completion period')
    axA.set_title('Panel A — US grid interconnection wait times have doubled', fontsize=12, loc='left', pad=14)
    axA.set_ylim(0, 5.5)
    for i, (v, lbl) in enumerate(zip(wait_vals, wait_labels)):
        axA.text(i, v + 0.15, lbl, ha='center', va='bottom', fontsize=10.5, fontweight='bold', color=bar_colors_A[i])

    # Annotation arrow showing the 2x doubling (conservative — true ratio >2x).
    axA.annotate('', xy=(1, 4), xytext=(0, 2),
                 arrowprops=dict(arrowstyle='->', color=PALETTE['text'], lw=1.2, alpha=0.6,
                                 connectionstyle='arc3,rad=-0.25'))
    axA.text(0.5, 3.4, '2x\nslower', ha='center', va='center', fontsize=10, color=PALETTE['text'], weight='bold')

    # Caption uses explicit "earlier window" phrasing so the 2000-2019 withdrawal
    # window doesn't read as inconsistent with the 2018-2024 bar window.
    axA.text(0.5, -0.32,
             'End of 2024: 10,300 projects in queue · 1,400 GW generation + 890 GW storage waiting\n'
             'Over the longer 2000-2019 lookback: 77% of submitted capacity was withdrawn before reaching commercial operations',
             transform=axA.transAxes, ha='center', va='top', fontsize=9.5, color=PALETTE['text'],
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#f9fafb', edgecolor=PALETTE['grid'], linewidth=0.8))

    # Panel B: data center electricity scenarios
    dc = pd.read_csv(ROOT / 'leg3_execution_layer' / 'c1_grid_data_center_demand.csv')
    dc_global = dc[(dc['scope'] == 'Global') & (dc['metric'] == 'data_center_electricity_consumption')].copy()
    dc_global['value'] = pd.to_numeric(dc_global['value'], errors='coerce')
    dc_global['year'] = pd.to_numeric(dc_global['year'], errors='coerce')

    # Historical (actual): 2023, 2024, 2025
    historical = dc_global[dc_global['scenario'] == 'actual'].sort_values('year')
    axB.plot(historical['year'], historical['value'], 'o-', color=PALETTE['primary'], linewidth=2.5, markersize=8, label='Actual')

    # Four scenarios for 2030, 2035
    scenario_colors = {'headwinds_case': PALETTE['success'], 'high_efficiency_case': PALETTE['accent'], 'base_case': PALETTE['primary'], 'lift_off_case': PALETTE['danger']}
    scenario_labels = {'headwinds_case': 'Headwinds', 'high_efficiency_case': 'High Efficiency', 'base_case': 'Base Case', 'lift_off_case': 'Lift-Off'}
    for sc, color in scenario_colors.items():
        sc_data = dc_global[dc_global['scenario'] == sc].sort_values('year')
        if len(sc_data) > 0:
            # Connect 2025 to scenario
            x_data = [2025] + sc_data['year'].tolist()
            y_data = [historical[historical['year'] == 2025]['value'].iloc[0]] + sc_data['value'].tolist()
            axB.plot(x_data, y_data, '--', color=color, alpha=0.7, linewidth=1.5, marker='o', markersize=6, label=scenario_labels[sc])

    axB.set_xlabel('Year')
    axB.set_ylabel('Global data center electricity (TWh)')
    axB.set_title('Panel B — Data center electricity demand, four scenarios to 2035', fontsize=12, loc='left', pad=14)
    axB.set_ylim(0, 1900)
    axB.legend(loc='upper left', fontsize=9, title='Scenario', title_fontsize=9)

    fig.suptitle('The bottleneck is electrons, not algorithms', fontsize=15, fontweight='bold', y=0.97, x=0.06, ha='left')

    # Chart 4 is 11" tall (vs 6" default) so the global figure.subplot.bottom=0.15
    # translates to ~1.6" of empty space below the bottom axis. Override tighter
    # and shorten source to a single line so the bottom band stays compact.
    fig.subplots_adjust(bottom=0.08)
    add_source(fig, 'Panel A: LBNL Queued Up 2025 | Panel B: IEA Energy and AI 2025')
    plt.savefig(CHARTS / 'chart_04_grid_constraint.png')
    plt.close()
    print('Chart 4 saved.')


# ----------------------------------------------------------------------
# Chart 5 — K-shape
# ----------------------------------------------------------------------
def chart_5_kshape():
    df = pd.read_csv(ROOT / 'leg4_macro_forces' / 'kshape_chart_data.csv')

    labor = df[df['metric'] == 'labor_share_nonfarm_business'].copy()
    labor['year'] = pd.to_numeric(labor['year'], errors='coerce')
    labor['value'] = pd.to_numeric(labor['value'], errors='coerce')
    labor = labor.dropna().sort_values('year')

    spx = df[df['metric'] == 'sp500_total_return_indexed_to_2000_=_100'].copy()
    spx['year'] = pd.to_numeric(spx['year'], errors='coerce')
    spx['value'] = pd.to_numeric(spx['value'], errors='coerce')
    spx = spx.dropna().sort_values('year')

    fig, ax1 = plt.subplots()
    color_labor = PALETTE['danger']
    color_capital = PALETTE['primary']

    ax1.plot(labor['year'], labor['value'], 'o-', color=color_labor, linewidth=2.5, markersize=7, label='Labor share (left axis)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('US labor share of nonfarm business output (%)', color=color_labor)
    ax1.tick_params(axis='y', labelcolor=color_labor)
    ax1.set_ylim(54, 65)

    ax2 = ax1.twinx()
    ax2.plot(spx['year'], spx['value'], 's-', color=color_capital, linewidth=2.5, markersize=7, label='S&P 500 total return (right axis)')
    ax2.set_ylabel('S&P 500 total return index (2000 = 100)', color=color_capital)
    ax2.tick_params(axis='y', labelcolor=color_capital)
    ax2.spines['top'].set_visible(False)
    ax2.set_ylim(0, 1000)

    # Endpoint annotations — show headline numbers
    labor_first = labor.iloc[0]
    labor_last = labor.iloc[-1]
    spx_first = spx.iloc[0]
    spx_last = spx.iloc[-1]
    ax1.annotate(f"{labor_first['value']:.1f}%", xy=(labor_first['year'], labor_first['value']),
                 xytext=(-32, 6), textcoords='offset points', fontsize=10, color=color_labor, weight='bold')
    ax1.annotate(f"{labor_last['value']:.1f}%", xy=(labor_last['year'], labor_last['value']),
                 xytext=(6, 8), textcoords='offset points', fontsize=10, color=color_labor, weight='bold')
    # SPX start point label dropped — right-axis title already says "2000 = 100".
    # Keeping it overlapped with the K-shape delta callout in the lower-left.
    ax2.annotate(f"{int(spx_last['value'])}", xy=(spx_last['year'], spx_last['value']),
                 xytext=(8, -4), textcoords='offset points', fontsize=10, color=color_capital, weight='bold')

    # Headline-number callout box
    ax1.text(0.02, 0.04,
             'Labor share: -4.5 pp\nS&P 500 TR: ~8.3x',
             transform=ax1.transAxes, fontsize=9.5, color=PALETTE['text'], weight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#f9fafb', edgecolor=PALETTE['grid'], linewidth=0.8))

    set_titles(ax1,
               'Capital up, labor share down: the K-shape since 2000',
               'US labor share of GDP vs S&P 500 total return — two trajectories from a common start')

    # Combined legend — lower-right (away from data crossover)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower right', fontsize=10,
               framealpha=0.95, frameon=True, facecolor='white', edgecolor=PALETTE['grid'])

    add_source(fig, 'US BLS labor share (FRED PRS85006173) + S&P Dow Jones ^SP500TR')
    plt.savefig(CHARTS / 'chart_05_kshape.png')
    plt.close()
    print('Chart 5 saved.')


# ----------------------------------------------------------------------
# Chart 6 — Working-age population decline
# ----------------------------------------------------------------------
def chart_6_demographics():
    df = pd.read_csv(ROOT / 'leg3_execution_layer' / 'c4_working_age_population_by_country.csv')
    df['pop_age_15_64'] = pd.to_numeric(df['pop_age_15_64'], errors='coerce')
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df = df.dropna(subset=['pop_age_15_64', 'year'])

    countries = ['South Korea', 'Italy', 'Japan', 'China', 'Germany', 'United States', 'India']
    color_map = {
        'South Korea': '#b91c1c',     # darker red
        'Italy': '#dc2626',
        'Japan': '#e3650b',           # orange-red
        'China': '#d97706',           # burnt orange
        'Germany': '#a16207',         # dark gold
        'United States': '#1c2e4a',   # navy
        'India': '#2d5016',           # dark green
    }

    fig, ax = plt.subplots(figsize=(11, 6.5))

    # Indexed to 2024 = 100
    for country in countries:
        sub = df[df['country_name'] == country].sort_values('year').copy()
        if sub.empty:
            continue
        ref_2024 = sub[sub['year'] == 2024]['pop_age_15_64'].iloc[0] if 2024 in sub['year'].values else sub.iloc[(sub['year'] - 2024).abs().argsort()[:1]]['pop_age_15_64'].iloc[0]
        sub['indexed'] = sub['pop_age_15_64'] / ref_2024 * 100
        ax.plot(sub['year'], sub['indexed'], '-', color=color_map[country], linewidth=2.2, label=country, alpha=0.92)

    # Thesis window shaded band
    ax.axvspan(2028, 2035, alpha=0.13, color=PALETTE['accent'], label='_nolegend_')
    ax.text(2031.5, 130, 'Thesis window\n2028-2035', ha='center', va='top', fontsize=9, color=PALETTE['accent'], weight='bold')

    # Horizontal 100 reference line + anchor marker at 2024.
    # The crossing point is mathematical, not coincidental: every country is
    # indexed to its OWN 2024 value, so all lines = 100 in 2024 by construction.
    # Mark the anchor explicitly so the reader understands the visual.
    ax.axhline(y=100, color=PALETTE['axis'], linestyle='--', linewidth=0.6, alpha=0.7)
    ax.axvline(x=2024, color=PALETTE['text'], linestyle=':', linewidth=0.9, alpha=0.5)
    # Anchor annotation in the upper-left empty zone (above all lines, below
    # the thesis-window text). Leader points down-right to (2024, 100).
    ax.annotate('Anchor: 2024 = 100\n(all lines indexed here)',
                xy=(2024, 100), xytext=(1996, 128),
                fontsize=8.5, color=PALETTE['text'], style='italic', ha='left',
                arrowprops=dict(arrowstyle='->', color=PALETTE['text'], lw=0.7, alpha=0.5,
                                connectionstyle='arc3,rad=-0.2'))

    # All 7 country labels in a single right-side column at x=2081, each at the
    # line's interpolated 2080 y-value. Space (no em-dash) between country name
    # and the % delta — em-dash was reading as a confusing punctuation break
    # between the two pieces of information.
    countries_labeled = ['United States', 'India', 'China', 'Germany', 'Italy', 'Japan', 'South Korea']
    for country in countries_labeled:
        sub = df[df['country_name'] == country].sort_values('year').copy()
        if sub.empty:
            continue
        ref_2024 = sub[sub['year'] == 2024]['pop_age_15_64'].iloc[0]
        sub['indexed'] = sub['pop_age_15_64'] / ref_2024 * 100
        # Interpolate at x=2080 (1/3 of the way between 2070 and 2100 data points).
        v_2070 = sub[sub['year'] == 2070]['indexed'].iloc[0]
        v_2100 = sub[sub['year'] == 2100]['indexed'].iloc[0]
        y_2080 = v_2070 + (v_2100 - v_2070) * (10.0 / 30.0)
        delta_2050 = sub[sub['year'] == 2050]['indexed'].iloc[0] - 100
        label = f'{country} {int(round(delta_2050)):+d}% by 2050'
        ax.text(2081, y_2080, label,
                va='center', ha='left', fontsize=8.5, color=color_map[country], weight='bold')

    # Right side widened to fit the 7-country label column at x=2081.
    ax.set_xlim(1990, 2102)
    ax.set_ylim(45, 135)
    ax.set_xlabel('Year')
    ax.set_ylabel('Working-age population (15-64), indexed to 2024 = 100')
    set_titles(ax,
               'Aging economies fund their own labor replacement',
               'Working-age population (15-64) indexed to 2024 — UN WPP 2024 medium scenario')

    add_source(fig, 'UN World Population Prospects 2024 (medium scenario) — via Our World in Data mirror')
    plt.savefig(CHARTS / 'chart_06_working_age.png')
    plt.close()
    print('Chart 6 saved.')


# ----------------------------------------------------------------------
# Chart 7 — Cohort timeline (Gantt-style)
# ----------------------------------------------------------------------
def chart_7_cohort_timeline():
    cohorts = [
        # name, employment_m, wage_b, start, end, color
        ('Cohort 1\nWarehouse / Logistics / Trucking', 8.2, 330, 2026, 2029, PALETTE['danger']),
        ('Cohort 2\nCleaning / Food prep / Counter', 6.4, 220, 2029, 2032, PALETTE['accent']),
        ('Cohort 3\nSkilled trades (Electrical / Plumbing)', 2.1, 140, 2033, 2037, PALETTE['tertiary']),
        ('Cohort 4\nPersonal care / Nursing', 5.7, 200, 2034, 2040, PALETTE['quaternary']),
        ('Cohort 5\nKnowledge work (augmentation)', 30.0, None, 2024, 2040, PALETTE['secondary']),
    ]

    fig, ax = plt.subplots(figsize=(11.5, 6))
    y_positions = list(range(len(cohorts), 0, -1))

    for (name, emp, wage, start, end, color), y in zip(cohorts, y_positions):
        is_cohort5 = wage is None
        alpha = 0.85 if not is_cohort5 else 0.55
        hatch = '' if not is_cohort5 else '////'
        bar_width = end - start
        ax.barh(y, bar_width, left=start, height=0.55, color=color, alpha=alpha, edgecolor='white', linewidth=0.6, hatch=hatch)

        # Label content
        wage_str = f'${wage}B/yr wage exposure' if not is_cohort5 else 'Augmentation, not displacement'
        full_label = f'{emp:.1f}M jobs  ·  {wage_str}'

        # Cohort 5 (hatched) — always dark text on light background, placed to right
        if is_cohort5:
            ax.text(end + 0.3, y, full_label, va='center', fontsize=9, color=PALETTE['text'], weight='bold')
        # Wide enough for inside-bar white text — only the widest bars
        elif bar_width >= 8:
            ax.text(start + 0.3, y, full_label, va='center', fontsize=9, color='white', weight='bold')
        # Narrow bar — place to the right of bar in cohort color
        else:
            ax.text(end + 0.3, y, full_label, va='center', fontsize=9, color=color, weight='bold')

    ax.set_yticks(y_positions)
    ax.set_yticklabels([c[0] for c in cohorts], fontsize=9.5)
    ax.set_xlim(2024, 2053)
    ax.set_xlabel('Crossover window — when reliability threshold is plausibly met')

    # Thesis window
    ax.axvspan(2028, 2035, alpha=0.12, color=PALETTE['accent'])
    ax.text(2031.5, len(cohorts) + 0.7, 'Thesis window 2028-2035', ha='center', fontsize=9.5, color=PALETTE['accent'], weight='bold')

    ax.set_ylim(0.3, len(cohorts) + 1.2)
    set_titles(ax,
               'When each US labor cohort hits the AI-robotics crossover',
               '~22 million US jobs across cohorts 1-4; cohort 5 augmented, not displaced')

    add_source(fig, 'BLS Occupational Employment and Wage Statistics May 2024; cohort framework synthesized from Legs 1-3 analysis')
    plt.savefig(CHARTS / 'chart_07_cohort_timeline.png')
    plt.close()
    print('Chart 7 saved.')


# ----------------------------------------------------------------------
# Chart 8 — Mag7 / Hyperscaler capex hockey-stick
# ----------------------------------------------------------------------
def chart_8_capex():
    df = pd.read_csv(ROOT / 'leg4_macro_forces' / 'mag7_capex_2022_2026.csv')
    # Use the Mag7 aggregate series (re-derived 2026-05-13 from per-company verified
    # components — see CSV notes). The earlier hyperscaler series was a workaround
    # for missing Mag7 pre-2024 baseline; now resolved.
    mag7 = df[(df['source_id'] == 'LEG4_MAG7_CAPEX') & (df['company'] == 'All_Mag7_aggregate')].copy()
    mag7['capex_usd'] = pd.to_numeric(mag7['capex_usd'], errors='coerce')
    mag7['year'] = pd.to_numeric(mag7['year'], errors='coerce')
    mag7 = mag7.dropna(subset=['capex_usd', 'year']).sort_values('year')
    mag7['capex_bn'] = mag7['capex_usd'] / 1e9

    fig, ax = plt.subplots()
    years = mag7['year'].astype(int).tolist()
    values = mag7['capex_bn'].tolist()
    colors = [PALETTE['secondary']] * (len(years) - 1) + [PALETTE['accent']]
    bars = ax.bar(years, values, color=colors, alpha=0.85, edgecolor='white', linewidth=0.6)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 18, f'${int(round(val))}B', ha='center', va='bottom', fontsize=10, fontweight='bold', color=PALETTE['text'])

    # Annotations for key inflections — YoY ratios re-derived from new series:
    # 2022→2023: -1% (flat — Amazon/Meta capex pause)
    # 2023→2024: +60%
    # 2024→2025: +61%
    # 2025→2026: +63%
    ax.annotate('+61% YoY\n2024 → 2025', xy=(2025, 454), xytext=(2023.2, 580),
                fontsize=9, color=PALETTE['danger'], weight='bold',
                arrowprops=dict(arrowstyle='->', color=PALETTE['danger'], lw=1.2))
    ax.annotate('+63% planned\n2025 → 2026', xy=(2026, 738), xytext=(2024.4, 820),
                fontsize=9, color=PALETTE['danger'], weight='bold',
                arrowprops=dict(arrowstyle='->', color=PALETTE['danger'], lw=1.2))

    # 5-year cumulative annotation
    cumulative = sum(values)
    ax.text(0.97, 0.04, f'5-year cumulative:\n${int(round(cumulative)):,}B', transform=ax.transAxes,
            fontsize=10, color=PALETTE['text'], weight='bold', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f9fafb', edgecolor=PALETTE['grid'], linewidth=0.8))

    ax.set_xticks(years)
    ax.set_xlabel('Year')
    ax.set_ylabel('Aggregate capital expenditure (USD billions)')
    set_titles(ax,
               r'Mag7 capex: \$177B in 2022 to \$738B planned in 2026',
               'Amazon, Alphabet, Meta, Microsoft, Tesla, Apple, Nvidia — aggregate annual capital expenditure')
    ax.set_ylim(0, 900)

    add_source(fig, 'Per-company 10-K and earnings guidance aggregated; calendar-year alignment (Oracle/Nvidia/Apple fiscal-year proxies). Methodology in CSV notes.')
    plt.savefig(CHARTS / 'chart_08_capex.png')
    plt.close()
    print('Chart 8 saved.')


# ----------------------------------------------------------------------
# Chart 9 — CPI components diverging
# ----------------------------------------------------------------------
def chart_9_cpi_components():
    df = pd.read_csv(ROOT / 'cohort_map' / 'cpi_components_2000_2024.csv')
    df['price_change_pct_2000_2024'] = pd.to_numeric(df['price_change_pct_2000_2024'], errors='coerce')
    df = df.dropna(subset=['price_change_pct_2000_2024'])

    # Exclude aggregate categories
    components = df[~df['category'].isin(['Aggregate', 'Wages'])].copy().sort_values('price_change_pct_2000_2024')
    components['color'] = components['price_change_pct_2000_2024'].apply(lambda x: PALETTE['danger'] if x > 0 else PALETTE['success'])

    fig, ax = plt.subplots(figsize=(11, 7))
    bars = ax.barh(components['subcategory'].str.replace('_', ' '), components['price_change_pct_2000_2024'],
                    color=components['color'], alpha=0.85, edgecolor='white', linewidth=0.5)

    # Reference lines: overall CPI (+87.3%) and wages (+123.3%)
    # Place labels INSIDE plot area at the bottom to avoid collision with subtitle
    ax.axvline(x=87.3, color=PALETTE['text'], linestyle='--', linewidth=1.2, alpha=0.7)
    ax.text(87.3, -1.3, 'Overall CPI:\n+87%', ha='center', va='top', fontsize=9, color=PALETTE['text'], weight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=PALETTE['text'], linewidth=0.6, alpha=0.95))
    ax.axvline(x=123.3, color=PALETTE['accent'], linestyle='--', linewidth=1.2, alpha=0.7)
    ax.text(123.3, -1.3, 'Wages:\n+123%', ha='center', va='top', fontsize=9, color=PALETTE['accent'], weight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=PALETTE['accent'], linewidth=0.6, alpha=0.95))
    ax.axvline(x=0, color=PALETTE['axis'], linestyle='-', linewidth=0.6)

    # Annotation: wages outran CPI on average — placed in upper-LEFT empty area
    # (negative-change bars all extend leftward from zero; the upper-left zone above them is empty)
    ax.text(0.03, 0.97, 'Wages outran CPI on average (+36pp gap)\n— but housing, healthcare, education\nran much faster',
            transform=ax.transAxes, fontsize=9, color=PALETTE['text'], ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f9fafb', edgecolor=PALETTE['grid'], linewidth=0.6))

    for bar, val in zip(bars, components['price_change_pct_2000_2024']):
        sign = '+' if val > 0 else ''
        offset = 3 if val > 0 else -3
        ha = 'left' if val > 0 else 'right'
        ax.text(val + offset, bar.get_y() + bar.get_height()/2, f'{sign}{int(val)}%', va='center', ha=ha, fontsize=8.5, color=PALETTE['text'])

    ax.set_xlim(-110, 290)
    ax.set_ylim(-3, len(components) + 0.5)
    ax.set_xlabel('Price change, 2000 to 2024 (%)')
    ax.set_ylabel('')
    set_titles(ax,
               'What got expensive, what got cheap — US CPI 2000-2024',
               'The cheaper-goods categories are mostly things you already get from your phone')

    add_source(fig, 'Mark J. Perry, "Chart of the Century" via AEI Carpe Diem; underlying data US BLS Consumer Price Index')
    plt.savefig(CHARTS / 'chart_09_cpi_components.png')
    plt.close()
    print('Chart 9 saved.')


# ----------------------------------------------------------------------
# Chart 10 — Skill durability quadrant
# ----------------------------------------------------------------------
def chart_10_skill_quadrant():
    df = pd.read_csv(ROOT / 'cohort_map' / 'cohort_map_us_occupations.csv')
    df['hourly_wage_equiv'] = pd.to_numeric(df['hourly_wage_equiv'], errors='coerce')
    df['us_employment_2024'] = pd.to_numeric(df['us_employment_2024'], errors='coerce')
    df['cohort'] = pd.to_numeric(df['cohort'], errors='coerce')
    df = df.dropna(subset=['hourly_wage_equiv', 'us_employment_2024', 'cohort'])

    # Automatable score: cohort 1 = high (4), cohort 2 = med-high (3), cohort 3 = med (2), cohort 4 = low-med (1), cohort 5 = low (0)
    cohort_to_score = {1: 4.0, 2: 3.0, 3: 2.0, 4: 1.5, 5: 0.5}
    df['automatable'] = df['cohort'].map(cohort_to_score)
    # Add some jitter for visual clarity
    np.random.seed(42)
    df['automatable_j'] = df['automatable'] + np.random.uniform(-0.25, 0.25, len(df))

    cohort_colors = {1: PALETTE['danger'], 2: PALETTE['accent'], 3: PALETTE['tertiary'], 4: PALETTE['quaternary'], 5: PALETTE['secondary']}
    cohort_labels_full = {1: 'Cohort 1: warehouse / logistics', 2: 'Cohort 2: cleaning / food', 3: 'Cohort 3: skilled trades', 4: 'Cohort 4: care / nursing', 5: 'Cohort 5: knowledge work'}

    fig, ax = plt.subplots(figsize=(11, 7))

    # Bigger jitter for less overlap
    np.random.seed(42)
    df['automatable_j'] = df['automatable'] + np.random.uniform(-0.42, 0.42, len(df))
    df['wage_jit'] = df['hourly_wage_equiv'] + np.random.uniform(-0.6, 0.6, len(df))

    for cohort, sub in df.groupby('cohort'):
        ax.scatter(sub['automatable_j'], sub['wage_jit'],
                   s=(sub['us_employment_2024'] / 1e6) * 60 + 40,
                   c=cohort_colors[int(cohort)], alpha=0.65, edgecolor='white', linewidth=0.8,
                   label=cohort_labels_full[int(cohort)])

    # Annotate key occupations with leader arrows pointing to exact bubble positions
    annot_list = [
        ('Stockers and Order Fillers', 'Stockers', (15, -18)),
        ('Fast Food and Counter Workers', 'Fast food', (-65, 12)),
        ('Heavy and Tractor-Trailer Truck Drivers', 'Truck drivers', (-75, 0)),
        ('Electricians', 'Electricians', (12, 6)),
        ('Home Health Aides + Personal Care Aides', 'Home aides', (12, -6)),
        ('Software Developers', 'Software devs', (-80, 6)),
        ('Nursing Assistants', 'Nursing assts', (-75, 6)),
    ]
    for full_name, short_label, offset in annot_list:
        row = df[df['occupation_title'].str.contains(full_name.split(' ')[0], regex=False, na=False)].head(1)
        if not row.empty:
            r = row.iloc[0]
            ax.annotate(short_label,
                        xy=(r['automatable_j'], r['wage_jit']),
                        xytext=offset, textcoords='offset points',
                        fontsize=8.5, color=PALETTE['text'], weight='bold', alpha=0.95,
                        arrowprops=dict(arrowstyle='-', color=PALETTE['secondary'], lw=0.6, alpha=0.6,
                                        shrinkA=2, shrinkB=4))

    ax.set_xlim(-0.5, 5)
    ax.set_ylim(0, 75)
    ax.set_xlabel('Automatable today  →  Less automatable')
    ax.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5])
    ax.set_xticklabels(['Knowledge\nwork', 'Care /\nnursing', 'Skilled\ntrades', 'Routine\ncommercial', 'Warehouse /\nlogistics'])
    ax.invert_xaxis()
    ax.set_ylabel('Median hourly wage (USD, May 2024)')
    set_titles(ax,
               'Where US labor cohorts sit on the AI-robotics map',
               'Bubble size = US employment count; color = labor cohort')
    ax.legend(loc='upper left', fontsize=9, title='Cohort', title_fontsize=9)

    add_source(fig, 'BLS Occupational Employment and Wage Statistics May 2024; cohort framework synthesized from article analysis')
    plt.savefig(CHARTS / 'chart_10_skill_quadrant.png')
    plt.close()
    print('Chart 10 saved.')


# ----------------------------------------------------------------------
# Chart 11 — Scarce-asset performance 2015-2024 (log scale)
# ----------------------------------------------------------------------
def chart_11_scarce_assets():
    df = pd.read_csv(ROOT / 'leg4_macro_forces' / 'scarce_asset_performance_2015_2025.csv')
    df['index_2015_=_100'] = pd.to_numeric(df['index_2015_=_100'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['index_2015_=_100', 'date'])

    asset_labels = {
        'Bitcoin': 'Bitcoin',
        'Gold': 'Gold',
        'US_median_home': 'US median home',
        'SP500_total_return': 'S&P 500 total return',
        'MSCI_World_total_return': 'MSCI World total return',
    }
    asset_colors = {
        'Bitcoin': PALETTE['accent'],
        'Gold': '#a16207',
        'US_median_home': PALETTE['tertiary'],
        'SP500_total_return': PALETTE['primary'],
        'MSCI_World_total_return': PALETTE['secondary'],
    }

    fig, ax = plt.subplots(figsize=(11, 6.5))

    # Vertical y-offsets per asset to prevent endpoint-label collisions
    label_offsets = {'Bitcoin': 1.0, 'SP500_total_return': 1.18, 'MSCI_World_total_return': 0.78, 'Gold': 1.04, 'US_median_home': 0.85}
    return_multiples = {'Bitcoin': '258x', 'SP500_total_return': '3.8x', 'MSCI_World_total_return': '2.7x', 'Gold': '2.4x', 'US_median_home': '1.4x'}
    for asset, label in asset_labels.items():
        sub = df[df['asset'] == asset].sort_values('date')
        if len(sub) >= 2:
            ax.plot(sub['date'], sub['index_2015_=_100'], 'o-', color=asset_colors[asset], linewidth=2.2, markersize=7, label=label)
            # Annotate endpoint with vertical offset + show return multiple
            last = sub.iloc[-1]
            offset_y = last['index_2015_=_100'] * label_offsets.get(asset, 1.0)
            mult = return_multiples.get(asset, '')
            ax.text(last['date'] + pd.Timedelta(days=90), offset_y, f'  {mult}', va='center', fontsize=10, color=asset_colors[asset], weight='bold')

    # Magnitude annotation — BTC vs others
    ax.annotate('Bitcoin dwarfs all\nother scarce assets\nby ~100x',
                xy=(pd.Timestamp('2024-06-01'), 25758), xytext=(pd.Timestamp('2018-06-01'), 8000),
                fontsize=10, color=PALETTE['accent'], weight='bold', ha='center',
                arrowprops=dict(arrowstyle='->', color=PALETTE['accent'], lw=1.5, alpha=0.7,
                                connectionstyle='arc3,rad=-0.2'))

    ax.set_yscale('log')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total return, indexed to 2015 = 100 (log scale)')
    set_titles(ax,
               'Scarce-asset performance, 2015 to 2024',
               'Total return indexed to 2015 — Bitcoin dwarfs traditional scarce assets (log Y-axis)')
    # Legend placed in the empty log-Y band between the bottom cluster
    # (Gold / homes / S&P / MSCI top out near indexed 380) and the Bitcoin
    # curve at its right-edge endpoint (~25,000). Anchored upper-right at
    # axes y ≈ 0.60 to give the cluster below more breathing room while
    # staying clear of Bitcoin's right-side endpoint. Frameless.
    ax.legend(
        loc='center right',
        bbox_to_anchor=(0.98, 0.60),
        bbox_transform=ax.transAxes,
        fontsize=9, title='Asset', title_fontsize=9,
        frameon=False,
    )
    ax.set_ylim(80, 80000)
    ax.set_xlim(pd.Timestamp('2014-09-01'), pd.Timestamp('2026-06-01'))

    add_source(fig, 'Bitcoin: CoinMarketCap | Gold: LBMA | US median home: FRED MSPUS | S&P 500 TR: Yahoo Finance ^SP500TR | MSCI World: MSCI Index')
    plt.savefig(CHARTS / 'chart_11_scarce_assets.png')
    plt.close()
    print('Chart 11 saved.')


# ----------------------------------------------------------------------
# Chart 12 — Four 2026 US macro flows, on one axis (Part 2 §2.2)
# ----------------------------------------------------------------------
def chart_12_macro_flows():
    """2026 macro-flows comparison.
    Replaces the §2.2 bullet list in Part 2 with a single visual.

    Sources:
      - Mag7 capex 2026: $738B per leg4_macro_forces/mag7_capex_2022_2026.csv
      - Cohort 1-3 (minus Logisticians) aggregate wages: $690B per
        cohort_map/cohort_map_us_occupations.csv (sum of us_employment_2024 *
        median_annual_wage_usd_2024 across cohorts 1-3, excluding the
        Logisticians row whose CSV bottleneck flag is augmentation_not_replacement)
      - US federal deficit FY26: $1.9T per leg4_macro_forces/us_fiscal_trajectory.csv
      - M2 trailing-12 expansion: $1.6T per leg4_macro_forces/us_monetary_aggregates.csv
    """
    # Top to bottom by magnitude — backdrop pair on top, matched pair on bottom.
    # Color: capital side navy, labor side red, backdrop gray. Mirrors chart 5.
    flows = [
        ('US federal deficit (FY26)',           1900, PALETTE['secondary']),
        ('M2 expansion (trailing 12 months)',   1600, PALETTE['secondary']),
        ('Mag7 capex (2026 planned)',            738, PALETTE['primary']),
        ('Cohort 1-3 aggregate wages (2024)',    690, PALETTE['danger']),
    ]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    labels = [f[0] for f in flows]
    values = [f[1] for f in flows]
    colors = [f[2] for f in flows]
    y_positions = list(range(len(flows)))

    bars = ax.barh(y_positions, values, color=colors, alpha=0.88,
                   edgecolor='white', linewidth=0.6, height=0.62)

    for bar, val in zip(bars, values):
        if val >= 1000:
            label = f'${val/1000:.1f}T'
        else:
            label = f'${val}B'
        ax.text(bar.get_width() + 35, bar.get_y() + bar.get_height()/2, label,
                va='center', ha='left', fontsize=11.5, fontweight='bold',
                color=PALETTE['text'])

    # Vertical bracket linking the matched pair (rows 2 and 3) at the right of
    # their bar tips, with a 'matched magnitudes' annotation.
    bracket_x = max(738, 690) + 220
    ax.plot([bracket_x, bracket_x], [2, 3], color=PALETTE['text'], lw=1.2,
            solid_capstyle='butt')
    # Small caps at top/bottom of the bracket
    ax.plot([bracket_x - 14, bracket_x], [2, 2], color=PALETTE['text'], lw=1.2)
    ax.plot([bracket_x - 14, bracket_x], [3, 3], color=PALETTE['text'], lw=1.2)
    ax.text(bracket_x + 30, 2.5, 'matched\nmagnitudes',
            va='center', ha='left', fontsize=10, fontweight='bold',
            color=PALETTE['text'], style='italic')

    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels, fontsize=10.5)
    ax.set_xlim(0, 2350)
    ax.invert_yaxis()  # row 0 sits on top
    ax.grid(axis='y', visible=False)
    # x-axis tick labels in $B; no axis label needed (bar values are labeled directly,
    # title makes scale obvious). Avoids label/source-line collision.
    ax.set_xticks([0, 500, 1000, 1500, 2000])
    ax.set_xticklabels(['$0', '$500B', '$1.0T', '$1.5T', '$2.0T'])

    set_titles(ax,
               'Four 2026 US macro flows, on one axis',
               'Mag7 capital expenditure and Cohort 1-3 aggregate wages are matched in magnitude')

    add_source(fig,
               'Mag7 capex: 10-K + 2026 earnings guidance | Cohort wages: BLS OES May 2024 (cohorts 1-3 less Logisticians) | '
               'Deficit: CBO Feb 2026 baseline | M2: FRED M2SL trailing 12 months')
    plt.savefig(CHARTS / 'chart_12_macro_flows.png')
    plt.close()
    print('Chart 12 saved.')


# ----------------------------------------------------------------------
# Chart 13 — US federal debt vs the 1946 peacetime peak (Part 2 §2.2)
# ----------------------------------------------------------------------
def chart_13_debt_trajectory():
    """US federal debt held by the public, % of GDP, 1946-2036.
    Historical 1946-2024 from FRED FYPUGDA188S (via Multpl mirror — annual);
    CBO Feb 2026 baseline 2025-2036 (4 anchor years 2025/2026/2030/2036
    with linear interpolation through intermediate years).

    Visualizes the article's claim: the country has been below the 1946 WWII
    peacetime peak (106.1%) for 80 years and is on a CBO trajectory to breach
    it around 2030 (CBO's own description: "new record" by FY2030).
    """
    df = pd.read_csv(ROOT / 'leg4_macro_forces' / 'us_debt_to_gdp_1946_2036.csv')
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    historical = df[df['source_id'] == 'LEG4_DEBT_HISTORICAL'].sort_values('year')
    baseline = df[df['source_id'] == 'LEG4_CBO_BASELINE'].sort_values('year')

    fig, ax = plt.subplots(figsize=(11, 6))

    # Historical: solid navy
    ax.plot(historical['year'], historical['value'], '-',
            color=PALETTE['primary'], lw=2.4, label='Historical (FRED)')

    # Visual bridge from 2024 historical to 2025 baseline (so the line is continuous)
    bridge = pd.concat([historical.tail(1), baseline.head(1)])
    ax.plot(bridge['year'], bridge['value'], '--',
            color=PALETTE['accent'], lw=1.6, alpha=0.5)

    # Projection: dashed orange (signals projected vs historical)
    ax.plot(baseline['year'], baseline['value'], '--',
            color=PALETTE['accent'], lw=2.4, label='CBO Feb 2026 baseline')

    # Horizontal reference line at 106.1% (1946 peacetime peak)
    ax.axhline(y=106.1, color=PALETTE['danger'], linestyle=':',
               linewidth=1.6, alpha=0.85)
    ax.text(1990, 109, '1946 peacetime peak: 106.1%',
            fontsize=10, color=PALETTE['danger'], fontweight='bold', ha='center')

    # Mark the breach point at FY2030
    ax.scatter([2030], [107.7], color=PALETTE['accent'], s=110,
               zorder=5, edgecolor='white', lw=1.5)

    # Annotations
    # 1946 peak
    ax.annotate('1946 peak\n106.1%',
                xy=(1946, 106.1), xytext=(1958, 92),
                fontsize=10, fontweight='bold', color=PALETTE['text'],
                arrowprops=dict(arrowstyle='->', color=PALETTE['text'], lw=1.0))
    # 1974 trough
    ax.annotate('1974 trough\n23.2%',
                xy=(1974, 23.2), xytext=(1980, 6),
                fontsize=10, fontweight='bold', color=PALETTE['text'],
                arrowprops=dict(arrowstyle='->', color=PALETTE['text'], lw=1.0))
    # 2030 breach
    ax.annotate('FY2030: peacetime\nrecord breached\n(107.7%)',
                xy=(2030, 107.7), xytext=(2008, 60),
                fontsize=10, fontweight='bold', color=PALETTE['danger'],
                arrowprops=dict(arrowstyle='->', color=PALETTE['danger'], lw=1.2))
    # 2036 endpoint label
    ax.text(2036.6, 120, '120%',
            fontsize=10.5, fontweight='bold',
            color=PALETTE['accent'], va='center', ha='left')

    ax.set_xlim(1944, 2042)
    ax.set_ylim(0, 132)
    ax.set_ylabel('Federal debt held by public (% of GDP)')
    ax.set_xlabel('Fiscal year')
    ax.legend(loc='upper left', frameon=True, framealpha=0.95,
              facecolor='white', edgecolor=PALETTE['grid'])

    set_titles(ax,
               'US federal debt vs the 1946 peacetime peak',
               'Historical descent + projected breach in FY2030 — 80 years of restraint, ending')

    add_source(fig,
               'Historical 1946-2024: FRED FYPUGDA188S via Multpl mirror | '
               'Projected 2025-2036: CBO Feb 2026 Budget and Economic Outlook '
               '(4 anchor years 2025/2026/2030/2036, intermediate years linear-interpolated)')
    plt.savefig(CHARTS / 'chart_13_debt_trajectory.png')
    plt.close()
    print('Chart 13 saved.')


# ----------------------------------------------------------------------
# Build all
# ----------------------------------------------------------------------
if __name__ == '__main__':
    print('Building 13 article charts...')
    print()

    chart_1_metr()
    chart_2_compute()
    chart_3_cost_vs_wages()
    chart_4_grid()
    chart_5_kshape()
    chart_6_demographics()
    chart_7_cohort_timeline()
    chart_8_capex()
    chart_9_cpi_components()
    chart_10_skill_quadrant()
    chart_11_scarce_assets()
    chart_12_macro_flows()
    chart_13_debt_trajectory()

    print()
    print('All charts built. Output at data/charts/')
