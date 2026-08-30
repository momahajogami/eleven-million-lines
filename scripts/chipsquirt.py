#!/usr/bin/env python3
"""
Chipsquirt — letter-level color tinting for HTML headers.
Named in honor of Chip Kidd, who understood that design is not decoration.

Each letter in a header gets its own color — all within the same dark hue zone,
oscillating rhythmically or wandering randomly. The result is barely perceptible
at a glance and quietly alive on inspection.

Usage:
    from chipsquirt import teal, magenta, apply_to_headers, apply_cycle

    html = apply_to_headers(html, teal, levels=['h1', 'h2'])
    html = apply_cycle(html, levels=['h2'], mode='walk')

Run directly for a demo:
    python3 scripts/chipsquirt.py > /tmp/demo.html && open /tmp/demo.html
"""

import colorsys
import math
import random
import re


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _hsl_to_rgb01(h_deg, s_pct, l_pct):
    """HSL (degrees, percent, percent) → RGB as floats in [0,1].
    Note: colorsys.hls_to_rgb takes (h, l, s) — not (h, s, l)."""
    r, g, b = colorsys.hls_to_rgb(h_deg / 360.0, l_pct / 100.0, s_pct / 100.0)
    return r, g, b


# ---------------------------------------------------------------------------
# Core colorizer
# ---------------------------------------------------------------------------

def colorize_letters(text, hue_center=170, hue_drift=10, sat=58,
                      light_center=8, light_range=3,
                      mode='sine', freq=0.45, seed=None):
    """
    Return HTML where each non-whitespace character is wrapped in a
    <span style="color: hsl(...)"> with a slightly varying shade.

    Parameters
    ----------
    hue_center  : center of the hue zone (0–360)
    hue_drift   : maximum hue deviation from center
    sat         : saturation % — keep moderate so dark colors read as hued, not grey
    light_center: center lightness % — keep low (6–12) for near-black effect
    light_range : how much lightness oscillates around center
    mode        : 'sine'                  — smooth wave, meditative and rhythmic
                  'random'               — independent per-letter noise, speckled
                  'walk'                 — random walk, wanders and drifts
                  'unit-squared'         — parabolic: most letters near-black, rare bright flashes
                  'fourth-power-interval'— like unit-squared but t⁴; flashes even rarer
                  'orbit'                — 3D Lissajous path through HSV space
    freq        : oscillation frequency for sine mode
    seed        : fix the random seed for reproducible output
    """
    if seed is not None:
        random.seed(seed)

    phase = random.uniform(0, math.tau)
    walk_h = float(hue_center)
    walk_l = float(light_center)

    result = []
    i = 0  # letter index (whitespace doesn't count)

    for ch in text:
        if ch in ' \t\n\r':
            result.append(ch)
            continue

        if mode == 'sine':
            h = hue_center + hue_drift * math.sin(i * freq * 0.71 + phase)
            l = light_center + light_range * math.sin(i * freq + phase + 1.0)
            l = max(10.0, min(45.0, l))
            color = f"hsl({h:.1f},{sat}%,{l:.1f}%)"

        elif mode == 'random':
            h = hue_center + random.uniform(-hue_drift, hue_drift)
            l = light_center + random.uniform(-light_range, light_range)
            l = max(10.0, min(45.0, l))
            color = f"hsl({h:.1f},{sat}%,{l:.1f}%)"

        elif mode == 'walk':
            step_h = random.uniform(-hue_drift * 0.25, hue_drift * 0.25)
            step_l = random.uniform(-light_range * 0.25, light_range * 0.25)
            walk_h = max(hue_center - hue_drift, min(hue_center + hue_drift, walk_h + step_h))
            walk_l = max(light_center - light_range, min(light_center + light_range, walk_l + step_l))
            h, l = walk_h, walk_l
            l = max(10.0, min(45.0, l))
            color = f"hsl({h:.1f},{sat}%,{l:.1f}%)"

        elif mode == 'unit-squared':
            # 1. Dark anchor: the family's base hue at low lightness.
            anchor_r, anchor_g, anchor_b = _hsl_to_rgb01(
                hue_center, sat, max(light_center - light_range, 6.0)
            )
            # 2. Random bright endpoint: nearby hue, modestly higher lightness.
            bright_h = hue_center + random.uniform(-hue_drift, hue_drift)
            bright_s = min(sat + random.uniform(0, 15), 100.0)
            bright_l = min(light_center + random.uniform(8, light_range * 3 + 8), 60.0)
            bright_r, bright_g, bright_b = _hsl_to_rgb01(bright_h, bright_s, bright_l)
            # 3. Draw the line segment in RGB. Pick t uniformly, then squeeze
            #    toward anchor with t² — most letters land near the dark end.
            t     = random.random()
            t_sq  = t * t
            r = anchor_r + t_sq * (bright_r - anchor_r)
            g = anchor_g + t_sq * (bright_g - anchor_g)
            b = anchor_b + t_sq * (bright_b - anchor_b)
            color = f"rgb({int(r*255)},{int(g*255)},{int(b*255)})"

        elif mode == 'fourth-power-interval':
            # Like unit-squared but t⁴ instead of t² — probability density is even
            # more sharply concentrated near the dark anchor. Chromatic flashes are
            # rarer and more startling: perhaps one letter in twenty escapes the dark.
            anchor_r, anchor_g, anchor_b = _hsl_to_rgb01(
                hue_center, sat, max(light_center - light_range, 6.0)
            )
            bright_h = hue_center + random.uniform(-hue_drift, hue_drift)
            bright_s = min(sat + random.uniform(0, 15), 100.0)
            bright_l = min(light_center + random.uniform(8, light_range * 3 + 8), 60.0)
            bright_r, bright_g, bright_b = _hsl_to_rgb01(bright_h, bright_s, bright_l)
            t      = random.random()
            t_4    = t * t * t * t
            r = anchor_r + t_4 * (bright_r - anchor_r)
            g = anchor_g + t_4 * (bright_g - anchor_g)
            b = anchor_b + t_4 * (bright_b - anchor_b)
            color = f"rgb({int(r*255)},{int(g*255)},{int(b*255)})"

        elif mode == 'orbit':
            # A 3D Lissajous path through HSV space.
            # Three incommensurate frequencies (1, φ, φ²) produce a quasi-periodic
            # orbit that never exactly repeats — each letter sits at a unique point
            # on the torus. Converted from HSV to RGB for full gamut control.
            PHI  = 1.6180339887   # golden ratio
            PHI2 = 2.6180339887   # φ² = φ+1

            h_hsv = (hue_center + hue_drift * math.sin(i * freq         + phase))          % 360
            s_hsv =  (sat / 100) + 0.18  * math.sin(i * freq * PHI      + phase + 1.1)
            v_hsv =  0.30        + 0.18  * math.sin(i * freq * PHI2     + phase + 2.3)

            s_hsv = max(0.0, min(1.0, s_hsv))
            v_hsv = max(0.08, min(0.60, v_hsv))

            r, g, b = colorsys.hsv_to_rgb(h_hsv / 360.0, s_hsv, v_hsv)
            color = f"rgb({int(r*255)},{int(g*255)},{int(b*255)})"

        else:
            color = f"hsl({hue_center},{sat}%,{light_center}%)"

        escaped = ch.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        result.append(f'<span style="color:{color}">{escaped}</span>')
        i += 1

    return ''.join(result)


# ---------------------------------------------------------------------------
# Color families
# All dark — the hue is felt more than seen
# ---------------------------------------------------------------------------

def teal(text, mode='sine', **kw):
    """Rich green-blue, dark. Cool, oceanic."""
    return colorize_letters(text, hue_center=172, hue_drift=12, sat=70,
                             light_center=28, light_range=8, mode=mode, **kw)


def magenta(text, mode='sine', **kw):
    """Deep magenta, dark. Warm, pressured."""
    return colorize_letters(text, hue_center=312, hue_drift=10, sat=65,
                             light_center=26, light_range=8, mode=mode, **kw)


def amber(text, mode='sine', **kw):
    """Dark amber. Ancient, candlelit."""
    return colorize_letters(text, hue_center=36, hue_drift=8, sat=75,
                             light_center=28, light_range=8, mode=mode, **kw)


def violet(text, mode='sine', **kw):
    """Deep violet, dark. Nocturnal, mathematical."""
    return colorize_letters(text, hue_center=268, hue_drift=14, sat=60,
                             light_center=26, light_range=8, mode=mode, **kw)


def slate(text, mode='sine', **kw):
    """Cold blue-grey, dark. Formal, lapidary."""
    return colorize_letters(text, hue_center=215, hue_drift=8, sat=40,
                             light_center=28, light_range=8, mode=mode, **kw)


def forest(text, mode='sine', **kw):
    """Dark green. Earthy, patient."""
    return colorize_letters(text, hue_center=140, hue_drift=10, sat=60,
                             light_center=25, light_range=8, mode=mode, **kw)


FAMILIES = {
    'teal':    teal,
    'magenta': magenta,
    'amber':   amber,
    'violet':  violet,
    'slate':   slate,
    'forest':  forest,
}


# ---------------------------------------------------------------------------
# HTML application
# ---------------------------------------------------------------------------

def apply_to_headers(html, colorizer, levels=None, mode='sine'):
    """
    Apply one colorizer to every instance of the specified header tags.

    Parameters
    ----------
    html       : HTML string to transform
    colorizer  : one of the family functions (teal, magenta, etc.)
    levels     : list of tag names, default ['h2']
    mode       : oscillation mode passed to colorizer
    """
    if levels is None:
        levels = ['h2']

    for tag in levels:
        def replace(m, tag=tag):
            attrs = m.group(1)
            inner = m.group(2)
            if '<' in inner:   # skip headers that already contain HTML
                return m.group(0)
            return f'<{tag}{attrs}>{colorizer(inner, mode=mode)}</{tag}>'

        html = re.sub(
            rf'<{tag}([^>]*)>(.*?)</{tag}>',
            replace,
            html,
            flags=re.DOTALL,
        )

    return html


def apply_cycle(html, levels=None, mode='sine'):
    """
    Apply a different color family to each header in sequence, cycling.
    Good for pages with multiple h2s that should each feel distinct.
    """
    if levels is None:
        levels = ['h2']

    family_list = list(FAMILIES.values())
    counter = [0]
    tags_pat = '|'.join(re.escape(t) for t in levels)

    def replace(m):
        tag   = m.group(1)
        attrs = m.group(2)
        inner = m.group(3)
        if '<' in inner:
            return m.group(0)
        colorizer = family_list[counter[0] % len(family_list)]
        counter[0] += 1
        return f'<{tag}{attrs}>{colorizer(inner, mode=mode)}</{tag}>'

    return re.sub(
        rf'<({tags_pat})([^>]*)>(.*?)</\1>',
        replace,
        html,
        flags=re.DOTALL,
    )


# ---------------------------------------------------------------------------
# Demo — run directly to see all families and modes
# ---------------------------------------------------------------------------

DEMO_SENTENCES = [
    "The browser as operating system.",
    "Eleven million lines you should know.",
    "Coding is writing, electrified.",
    "The file. The process. The pipe.",
    "Grothendieck rewrote algebraic geometry from scratch.",
]

if __name__ == '__main__':
    print("""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>Chipsquirt Demo</title>
<style>
  body { background: #fdfaf5; font-family: Georgia, serif; padding: 3rem 4rem; max-width: 800px; }
  h1 { font-size: 1.1rem; font-weight: normal; color: #aaa; margin-bottom: 3rem; letter-spacing: .05em; }
  .family { margin-bottom: 3rem; }
  .label { font-size: 0.75rem; color: #ccc; font-family: monospace; margin-bottom: 0.25rem; }
  h2 { font-size: 1.5rem; font-weight: normal; margin: 0 0 0.1rem; }
  hr { border: none; border-top: 1px solid #e8e0d4; margin: 2rem 0; }
</style></head><body>
<h1>Chipsquirt — color family demo</h1>
""")

    sentences = DEMO_SENTENCES.copy()
    for name, fn in FAMILIES.items():
        print(f'<div class="family">')
        for mode in ('sine', 'walk', 'random', 'unit-squared', 'fourth-power-interval', 'orbit'):
            text = sentences[0]
            sentences = sentences[1:] + [sentences[0]]
            colored = fn(text, mode=mode)
            print(f'<p class="label">{name} / {mode}</p>')
            print(f'<h2>{colored}</h2>')
        print('</div><hr>')

    print('</body></html>')
