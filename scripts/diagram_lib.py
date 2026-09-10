"""Tiny SVG diagram toolkit used to generate the framework images in
marketing-program/images/. No dependencies beyond the standard library.

Run scripts/make_diagrams.py to regenerate every image.
"""
from __future__ import annotations

import html
import math
from dataclasses import dataclass, field

FONT = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"
INK = "#1f2937"
MUTED = "#6b7280"
LINE = "#9ca3af"
ACCENT = "#2563eb"
ACCENT_SOFT = "#dbeafe"
WARM = "#d97706"
WARM_SOFT = "#fef3c7"
GREEN = "#059669"
GREEN_SOFT = "#d1fae5"
ROSE = "#dc2626"
ROSE_SOFT = "#fee2e2"
PAPER = "#ffffff"
PANEL = "#f3f4f6"

PALETTE = [
    (ACCENT, ACCENT_SOFT),
    (GREEN, GREEN_SOFT),
    (WARM, WARM_SOFT),
    (ROSE, ROSE_SOFT),
    ("#7c3aed", "#ede9fe"),
    ("#0891b2", "#cffafe"),
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def wrap(text: str, max_chars: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        cand = (cur + " " + w).strip()
        if len(cand) > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return lines or [""]


@dataclass
class Canvas:
    width: int
    height: int
    title: str = ""
    parts: list[str] = field(default_factory=list)

    def add(self, s: str) -> None:
        self.parts.append(s)

    def text(self, x, y, s, size=14, color=INK, weight="normal", anchor="middle", max_chars=None, lh=1.3, italic=False):
        lines = wrap(s, max_chars) if max_chars else [s]
        total = (len(lines) - 1) * size * lh
        y0 = y - total / 2
        style = f"font-family:{FONT};font-size:{size}px;fill:{color};font-weight:{weight};" + ("font-style:italic;" if italic else "")
        out = []
        for i, ln in enumerate(lines):
            out.append(
                f'<text x="{x}" y="{y0 + i * size * lh:.1f}" text-anchor="{anchor}" dominant-baseline="middle" style="{style}">{esc(ln)}</text>'
            )
        self.add("".join(out))

    def box(self, x, y, w, h, label="", sub="", fill=PANEL, stroke=LINE, size=14, radius=10, color=INK, weight="600", max_chars=None, sw=1.5):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
        mc = max_chars or max(8, int(w / (size * 0.58)))
        if label and sub:
            self.text(x + w / 2, y + h / 2 - size * 0.7, label, size=size, weight=weight, color=color, max_chars=mc)
            self.text(x + w / 2, y + h / 2 + size * 0.9, sub, size=size - 3, color=MUTED, max_chars=int(mc * 1.25))
        elif label:
            self.text(x + w / 2, y + h / 2, label, size=size, weight=weight, color=color, max_chars=mc)

    def arrow(self, x1, y1, x2, y2, color=LINE, width=2, dashed=False, label="", curve=0.0):
        dash = ' stroke-dasharray="6 5"' if dashed else ""
        if curve:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            dx, dy = x2 - x1, y2 - y1
            L = math.hypot(dx, dy) or 1
            nx, ny = -dy / L, dx / L
            cx, cy = mx + nx * curve, my + ny * curve
            d = f"M{x1},{y1} Q{cx},{cy} {x2},{y2}"
            lx, ly = (x1 + 2 * cx + x2) / 4, (y1 + 2 * cy + y2) / 4
        else:
            d = f"M{x1},{y1} L{x2},{y2}"
            lx, ly = (x1 + x2) / 2, (y1 + y2) / 2
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{dash} marker-end="url(#arrow)"/>')
        if label:
            tw = len(label) * 7 + 12
            self.add(f'<rect x="{lx - tw / 2}" y="{ly - 10}" width="{tw}" height="20" rx="6" fill="{PAPER}"/>')
            self.text(lx, ly, label, size=12, color=MUTED)

    def line(self, x1, y1, x2, y2, color=LINE, width=1.5, dashed=False):
        dash = ' stroke-dasharray="6 5"' if dashed else ""
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{dash}/>')

    def circle(self, cx, cy, r, fill=PANEL, stroke=LINE, sw=1.5):
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def polygon(self, pts, fill=PANEL, stroke=LINE, sw=1.5):
        p = " ".join(f"{x},{y}" for x, y in pts)
        self.add(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def caption(self, s: str):
        self.text(self.width / 2, self.height - 18, s, size=12, color=MUTED, italic=True, max_chars=int(self.width / 7))

    def render(self) -> str:
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
            f'viewBox="0 0 {self.width} {self.height}" font-family="{FONT}">'
            f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/></marker></defs>'
            f'<rect width="100%" height="100%" fill="{PAPER}"/>'
        )
        title = ""
        if self.title:
            title = (
                f'<text x="{self.width / 2}" y="30" text-anchor="middle" dominant-baseline="middle" '
                f'style="font-family:{FONT};font-size:20px;font-weight:700;fill:{INK}">{esc(self.title)}</text>'
            )
        return head + title + "".join(self.parts) + "</svg>"


def edge_arrow(c: Canvas, x1, y1, w1, h1, x2, y2, w2, h2, pad=6, **kw):
    """Arrow from the boundary of box 1 (centered at x1,y1) to the boundary of box 2."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L

    def t_for(w, h):
        tx = (w / 2) / abs(ux) if ux else float("inf")
        ty = (h / 2) / abs(uy) if uy else float("inf")
        return min(tx, ty)

    t1 = t_for(w1, h1) + pad
    t2 = t_for(w2, h2) + pad
    c.arrow(x1 + ux * t1, y1 + uy * t1, x2 - ux * t2, y2 - uy * t2, **kw)


# ---------- Higher level layouts ----------

def flow(title, steps, width=1000, caption="", subs=None, colors=None, height=220):
    """Left-to-right chain of boxes joined by arrows."""
    c = Canvas(width, height, title)
    n = len(steps)
    gap = 28
    margin = 30
    bw = (width - 2 * margin - gap * (n - 1)) / n
    bh = 84
    y = (height - bh) / 2 + 10
    for i, s in enumerate(steps):
        x = margin + i * (bw + gap)
        stroke, fill = (colors[i] if colors else PALETTE[i % len(PALETTE)])
        c.box(x, y, bw, bh, s, subs[i] if subs else "", fill=fill, stroke=stroke, size=14)
        if i < n - 1:
            c.arrow(x + bw + 2, y + bh / 2, x + bw + gap - 4, y + bh / 2)
    if caption:
        c.caption(caption)
    return c.render()


def cycle(title, steps, width=760, height=560, caption="", center="", r=190):
    """Nodes arranged on a circle with arrows around the loop."""
    c = Canvas(width, height, title)
    cx, cy = width / 2, height / 2 + 10
    n = len(steps)
    pts = []
    for i in range(n):
        a = -math.pi / 2 + i * 2 * math.pi / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    bw, bh = 170, 66
    for i, (x, y) in enumerate(pts):
        stroke, fill = PALETTE[i % len(PALETTE)]
        c.box(x - bw / 2, y - bh / 2, bw, bh, steps[i], fill=fill, stroke=stroke, size=14)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        edge_arrow(c, x1, y1, bw, bh, x2, y2, bw, bh, curve=-22, width=2.5, color=ACCENT)
    if center:
        c.text(cx, cy, center, size=15, weight="700", color=INK, max_chars=18)
    if caption:
        c.caption(caption)
    return c.render()


def funnel(title, stages, width=760, height=540, caption="", right_notes=None):
    """Classic narrowing funnel; each stage is a trapezoid with a label."""
    c = Canvas(width, height, title)
    n = len(stages)
    top_w, bot_w = 520, 180
    x0 = 60
    y = 60
    h = (height - 120) / n
    for i, s in enumerate(stages):
        w1 = top_w - (top_w - bot_w) * i / n
        w2 = top_w - (top_w - bot_w) * (i + 1) / n
        cx = x0 + top_w / 2
        pts = [(cx - w1 / 2, y), (cx + w1 / 2, y), (cx + w2 / 2, y + h - 6), (cx - w2 / 2, y + h - 6)]
        stroke, fill = PALETTE[i % len(PALETTE)]
        c.polygon(pts, fill=fill, stroke=stroke)
        c.text(cx, y + (h - 6) / 2, s, size=15, weight="600")
        if right_notes:
            c.text(x0 + top_w + 20, y + (h - 6) / 2, right_notes[i], size=12, color=MUTED, anchor="start", max_chars=22)
        y += h
    if caption:
        c.caption(caption)
    return c.render()


def matrix(title, x_axis, y_axis, quadrants, width=760, height=600, caption=""):
    """2x2 matrix. quadrants = [top-left, top-right, bottom-left, bottom-right] labels."""
    c = Canvas(width, height, title)
    left, top = 110, 70
    gw, gh = width - left - 40, height - top - 90
    cw, ch = gw / 2, gh / 2
    for i, q in enumerate(quadrants):
        col, row = i % 2, i // 2
        stroke, fill = PALETTE[i % len(PALETTE)]
        c.box(left + col * cw + 4, top + row * ch + 4, cw - 8, ch - 8, q[0], q[1] if len(q) > 1 else "", fill=fill, stroke=stroke, size=15)
    # axes
    c.arrow(left, top + gh + 8, left + gw, top + gh + 8, color=INK)
    c.arrow(left - 8, top + gh, left - 8, top, color=INK)
    c.text(left + gw / 2, top + gh + 30, x_axis, size=13, color=MUTED, weight="600")
    c.add(f'<g transform="translate({left - 30},{top + gh / 2}) rotate(-90)">')
    c.text(0, 0, y_axis, size=13, color=MUTED, weight="600")
    c.add("</g>")
    if caption:
        c.caption(caption)
    return c.render()


def stack(title, layers, width=760, height=None, caption="", subs=None, bottom_up=True):
    """Vertical stack of horizontal bands, widest at bottom (a pyramid-ish stack)."""
    n = len(layers)
    height = height or 90 + n * 78
    c = Canvas(width, height, title)
    y = 60
    for i, s in enumerate(layers):
        idx = i
        shrink = (n - 1 - i) * 40 if bottom_up else i * 40
        w = width - 100 - shrink
        x = (width - w) / 2
        stroke, fill = PALETTE[idx % len(PALETTE)]
        c.box(x, y, w, 64, s, subs[i] if subs else "", fill=fill, stroke=stroke, size=15)
        y += 74
    if caption:
        c.caption(caption)
    return c.render()


def tree(title, root, children, width=1000, height=460, caption="", grandchildren=None):
    """One root, a row of children, and optional grandchildren lists per child."""
    c = Canvas(width, height, title)
    rw, rh = 260, 66
    rx, ry = width / 2 - rw / 2, 60
    c.box(rx, ry, rw, rh, root, fill=ACCENT_SOFT, stroke=ACCENT, size=16)
    n = len(children)
    margin = 30
    gap = 20
    bw = (width - 2 * margin - gap * (n - 1)) / n
    by = 190
    for i, ch in enumerate(children):
        x = margin + i * (bw + gap)
        stroke, fill = PALETTE[(i + 1) % len(PALETTE)]
        c.box(x, by, bw, 60, ch, fill=fill, stroke=stroke, size=14)
        c.arrow(width / 2, ry + rh, x + bw / 2, by - 2)
        if grandchildren and i < len(grandchildren):
            gy = by + 80
            for g in grandchildren[i]:
                c.box(x + 6, gy, bw - 12, 40, g, fill=PAPER, stroke=LINE, size=12, weight="normal", radius=6)
                gy += 48
    if caption:
        c.caption(caption)
    return c.render()


def rings(title, labels, width=720, height=640, caption=""):
    """Concentric circles, innermost label first."""
    c = Canvas(width, height, title)
    cx, cy = width / 2, height / 2 + 10
    n = len(labels)
    rmax = min(width, height) / 2 - 70
    for i in range(n - 1, -1, -1):
        r = rmax * (i + 1) / n
        stroke, fill = PALETTE[i % len(PALETTE)]
        c.circle(cx, cy, r, fill=fill, stroke=stroke)
    for i, lab in enumerate(labels):
        r_in = rmax * i / n
        r_out = rmax * (i + 1) / n
        yy = cy - (r_in + r_out) / 2 if i else cy
        c.text(cx, yy, lab, size=14, weight="600", max_chars=22)
    if caption:
        c.caption(caption)
    return c.render()


def table(title, headers, rows, width=1000, caption="", col_widths=None):
    """Simple grid table with header row."""
    n = len(headers)
    rh = 58
    height = 90 + rh * (len(rows) + 1) + 30
    c = Canvas(width, height, title)
    margin = 30
    if col_widths is None:
        col_widths = [(width - 2 * margin) / n] * n
    x = margin
    y = 60
    for i, h in enumerate(headers):
        c.box(x, y, col_widths[i], rh - 4, h, fill=ACCENT_SOFT, stroke=ACCENT, size=14, radius=6)
        x += col_widths[i]
    y += rh
    for r in rows:
        x = margin
        for i, cell in enumerate(r):
            c.box(x, y, col_widths[i], rh - 4, cell, fill=PAPER if i else PANEL, stroke=LINE, size=12, weight="600" if i == 0 else "normal", radius=6)
            x += col_widths[i]
        y += rh
    if caption:
        c.caption(caption)
    return c.render()


def timeline(title, phases, width=1000, height=300, caption="", subs=None):
    """Horizontal timeline with numbered phases."""
    c = Canvas(width, height, title)
    n = len(phases)
    margin = 120
    y = 160
    c.line(margin, y, width - margin, y, color=LINE, width=3)
    step = (width - 2 * margin) / (n - 1) if n > 1 else 0
    for i, p in enumerate(phases):
        x = margin + i * step
        stroke, fill = PALETTE[i % len(PALETTE)]
        c.circle(x, y, 18, fill=fill, stroke=stroke, sw=2.5)
        c.text(x, y, str(i + 1), size=14, weight="700")
        c.text(x, y - 65, p, size=14, weight="600", max_chars=20)
        if subs:
            c.text(x, y + 60, subs[i], size=12, color=MUTED, max_chars=24)
    if caption:
        c.caption(caption)
    return c.render()
