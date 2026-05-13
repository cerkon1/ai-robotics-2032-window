"""
Shared visual style for all article charts.
Used by build_charts.py.

Palette inspired by editorial financial publications (Financial Times / Bloomberg style).
Conservative, professional, suitable for Substack publication.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

# Color palette
PALETTE = {
    'primary': '#1c2e4a',        # Dark navy — main lines, primary series
    'accent': '#d97706',         # Burnt orange — highlights, callouts
    'secondary': '#6b7280',      # Medium gray — secondary lines
    'tertiary': '#2d5016',       # Dark green — third series
    'quaternary': '#8b1e3f',     # Dark crimson — fourth series
    'success': '#15803d',        # Forest green — positive changes
    'danger': '#b91c1c',         # Dark red — negative changes / warnings
    'grid': '#e5e7eb',           # Very light gray — gridlines
    'axis': '#9ca3af',           # Light gray — axis lines
    'text': '#1f2937',           # Dark gray — body text
    'source': '#6b7280',         # Medium gray — source attribution
    'bg': '#ffffff',             # White background
}

# Categorical palette for multi-line charts
CATEGORICAL = [
    '#1c2e4a',  # navy
    '#d97706',  # burnt orange
    '#15803d',  # forest green
    '#8b1e3f',  # dark crimson
    '#7c3aed',  # purple
    '#0891b2',  # cyan-blue
    '#a16207',  # dark yellow-gold
    '#6b7280',  # gray
    '#be185d',  # pink
    '#1e40af',  # bright navy
]


def apply_style():
    """Apply the unified article style to matplotlib."""
    mpl.rcParams.update({
        'figure.figsize': (10, 6),
        'figure.facecolor': PALETTE['bg'],
        'figure.dpi': 100,
        'figure.subplot.top': 0.86,
        'figure.subplot.bottom': 0.15,
        'savefig.dpi': 200,
        'savefig.facecolor': PALETTE['bg'],
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.4,

        'font.family': 'sans-serif',
        'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
        'font.size': 11,
        'font.weight': 'normal',

        'axes.facecolor': PALETTE['bg'],
        'axes.edgecolor': PALETTE['axis'],
        'axes.linewidth': 0.8,
        'axes.titlesize': 14,
        'axes.titleweight': 'bold',
        'axes.titlepad': 30,
        'axes.titlelocation': 'left',
        'axes.labelsize': 11,
        'axes.labelweight': 'normal',
        'axes.labelcolor': PALETTE['text'],
        'axes.labelpad': 8,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True,
        'axes.grid': True,
        'axes.grid.axis': 'both',
        'axes.axisbelow': True,
        'axes.prop_cycle': mpl.cycler(color=CATEGORICAL),

        'xtick.color': PALETTE['text'],
        'xtick.labelsize': 10,
        'xtick.direction': 'out',
        'xtick.major.size': 4,
        'xtick.major.width': 0.6,

        'ytick.color': PALETTE['text'],
        'ytick.labelsize': 10,
        'ytick.direction': 'out',
        'ytick.major.size': 4,
        'ytick.major.width': 0.6,

        'grid.color': PALETTE['grid'],
        'grid.linestyle': '-',
        'grid.linewidth': 0.6,
        'grid.alpha': 1.0,

        'legend.frameon': False,
        'legend.fontsize': 10,
        'legend.title_fontsize': 10,
        'legend.loc': 'best',

        'lines.linewidth': 2.2,
        'lines.markersize': 6,

        'patch.linewidth': 0.6,
        'patch.edgecolor': PALETTE['bg'],
    })


def add_source(fig, source_text, retrieval_date='2026-05-12'):
    """Add a source attribution line at the bottom of the figure.

    Anchored to the bottom-most plot area's left spine (not the figure's left edge)
    so the source line sits under the chart proper, leaving the figure's left margin
    free for the y-axis label only. Wraps to the plot-area width.

    The effect: x:y plot ratio is preserved at full plot width; the source line
    visually associates with the data it describes; consistent across all charts.
    """
    import textwrap
    full_source = f'Source: {source_text} | Retrieved {retrieval_date}'
    axes = list(fig.axes)
    if axes:
        bottom_ax = min(axes, key=lambda a: a.get_position().y0)
        bbox = bottom_ax.get_position()
        x_anchor = bbox.x0
        plot_width_inches = fig.get_figwidth() * (bbox.x1 - bbox.x0)
        # ~13 chars/inch for italic 9-pt sans-serif — conservative
        wrap_width = max(40, int(plot_width_inches * 13))
    else:
        x_anchor = 0.01
        wrap_width = 140
    full_source = textwrap.fill(full_source, width=wrap_width)
    fig.text(
        x_anchor, 0.005,
        full_source,
        fontsize=9,
        color=PALETTE['source'],
        style='italic',
        ha='left',
        va='bottom',
    )


def set_titles(ax, title, subtitle=None):
    """Set a bold left-aligned title and an optional subtitle below it.
    Replaces ax.set_title + add_subtitle to prevent overlap.

    Title is drawn above the axes at y=1.16 (transAxes).
    Subtitle is drawn at y=1.05.
    """
    ax.text(
        0, 1.16,
        title,
        fontsize=14,
        fontweight='bold',
        color=PALETTE['text'],
        ha='left',
        va='bottom',
        transform=ax.transAxes,
    )
    if subtitle:
        ax.text(
            0, 1.04,
            subtitle,
            fontsize=10.5,
            color=PALETTE['secondary'],
            ha='left',
            va='bottom',
            transform=ax.transAxes,
        )


def add_subtitle(ax, subtitle):
    """Backwards-compat: still used by older chart code paths."""
    ax.text(
        0, 1.04,
        subtitle,
        fontsize=10.5,
        color=PALETTE['secondary'],
        ha='left',
        va='bottom',
        transform=ax.transAxes,
    )


def add_annotation_box(ax, text, xy_relative=(0.02, 0.92), color=None):
    """Add a callout text box with a light background."""
    if color is None:
        color = PALETTE['text']
    ax.text(
        xy_relative[0], xy_relative[1],
        text,
        transform=ax.transAxes,
        fontsize=9,
        color=color,
        verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f9fafb', edgecolor=PALETTE['grid'], linewidth=0.8),
    )
