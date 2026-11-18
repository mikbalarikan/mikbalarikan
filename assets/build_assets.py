"""Generates the SVG assets of the GitHub profile README.

Run:  python assets/build_assets.py
Palette = Türkişi Engineering "Lacivert Çelik" tokens; mascot = KUMPAS.
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).parent

# ---- palette -------------------------------------------------------------
GECE, DERIN, ZEMIN, PANEL = "#070C11", "#0D161F", "#141F2B", "#202E3C"
GUNMETAL, TITAN, GUMUS, KROM = "#394A5A", "#808E9B", "#B7C3CD", "#ECF1F5"
KIRMIZI, KOYU_KIRMIZI, SARI = "#FF3347", "#AF1537", "#E6FF1F"
MAVI, YESIL, CAMGOBEGI = "#64BFFF", "#46D193", "#22D3EE"

SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'Cascadia Code', Consolas, 'Liberation Mono', monospace"


def kumpas(x, y, s, anim=True, uid="k"):
    """KUMPAS caliper-bot mascot, drawn in a 512 box, placed at (x, y), scale s."""
    blink = f"""<animateTransform attributeName="transform" type="scale" values="1 1;1 1;1 .08;1 1;1 1"
        keyTimes="0;.9;.94;.98;1" dur="4.5s" repeatCount="indefinite"/>""" if anim else ""
    jaw = f"""<animateTransform attributeName="transform" type="translate" values="0 0;-26 0;-26 0;0 0;0 0"
        keyTimes="0;.3;.55;.85;1" dur="6s" repeatCount="indefinite"/>""" if anim else ""
    bob = f"""<animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0"
        dur="3s" repeatCount="indefinite"/>""" if anim else ""
    lamp = f"""<animate attributeName="fill" values="{KIRMIZI};#ff8a96;{KIRMIZI}" dur="1.6s" repeatCount="indefinite"/>""" if anim else ""
    ticks_big = "".join(f"M{40 + 40 * i},232V254" for i in range(11))
    ticks_small = "".join(f"M{60 + 40 * i},232V244" for i in range(11))
    return f"""
<g transform="translate({x} {y}) scale({s})">
  <rect x="20" y="222" width="472" height="58" rx="10" fill="{GUMUS}" stroke="{GECE}" stroke-width="14"/>
  <g stroke="{GECE}" stroke-width="5"><path d="{ticks_big}"/><path d="{ticks_small}"/></g>
  <path d="M60,270 L130,270 L130,470 L98,500 L60,500 Z" fill="{GUMUS}" stroke="{GECE}" stroke-width="14" stroke-linejoin="round"/>
  <g>{jaw}
    <path d="M382,270 L452,270 L452,500 L414,500 L382,470 Z" fill="{GUMUS}" stroke="{GECE}" stroke-width="14" stroke-linejoin="round"/>
  </g>
  <g>{bob}
    <rect x="96" y="96" width="320" height="300" rx="56" fill="{KIRMIZI}" stroke="{GECE}" stroke-width="14"/>
    <path d="M96,300 L416,300 L416,340 Q416,396 360,396 L152,396 Q96,396 96,340 Z" fill="{KOYU_KIRMIZI}" opacity=".6"/>
    <rect x="96" y="96" width="320" height="300" rx="56" fill="none" stroke="{GECE}" stroke-width="14"/>
    <rect x="136" y="140" width="240" height="150" rx="22" fill="{GECE}"/>
    <g transform="translate(256 205)"><g>{blink}<g transform="translate(-256 -205)">
      <path d="M182.4,212.9 Q205.4,183 228.4,212.9" fill="none" stroke="{SARI}" stroke-width="12.6" stroke-linecap="round"/>
      <path d="M283.6,212.9 Q306.6,183 329.6,212.9" fill="none" stroke="{SARI}" stroke-width="12.6" stroke-linecap="round"/>
    </g></g></g>
    <path d="M230.7,256.6 Q256,275 281.3,256.6" fill="none" stroke="{SARI}" stroke-width="9.2" stroke-linecap="round"/>
    <circle cx="196" cy="340" r="15" fill="{KROM}" stroke="{GECE}" stroke-width="7"/>
    <circle cx="256" cy="340" r="15" fill="{KROM}" stroke="{GECE}" stroke-width="7"/>
    <circle cx="316" cy="340" r="15" fill="{KROM}" stroke="{GECE}" stroke-width="7"/>
    <circle cx="256" cy="52" r="34" fill="{KIRMIZI}" stroke="{GECE}" stroke-width="14">{lamp}</circle>
    <path d="M236,52 L276,52 M256,32 L256,72" stroke="{GECE}" stroke-width="9" stroke-linecap="round"/>
    <rect x="244" y="80" width="24" height="22" fill="{TITAN}" stroke="{GECE}" stroke-width="8"/>
  </g>
</g>"""


def grid_bg(w, h, uid, step=24):
    return f"""
<defs>
  <pattern id="g{uid}" width="{step}" height="{step}" patternUnits="userSpaceOnUse">
    <path d="M{step} 0H0V{step}" fill="none" stroke="{ZEMIN}" stroke-width="1"/>
  </pattern>
  <pattern id="G{uid}" width="{step*5}" height="{step*5}" patternUnits="userSpaceOnUse">
    <path d="M{step*5} 0H0V{step*5}" fill="none" stroke="{PANEL}" stroke-width="1.2"/>
  </pattern>
</defs>
<rect width="{w}" height="{h}" rx="18" fill="{DERIN}"/>
<rect width="{w}" height="{h}" rx="18" fill="url(#g{uid})"/>
<rect width="{w}" height="{h}" rx="18" fill="url(#G{uid})"/>"""


def gear(cx, cy, r, teeth, color, dur, op=.18, rev=False):
    import math
    pts = []
    for i in range(teeth * 4):
        a = 2 * math.pi * i / (teeth * 4)
        rr = r if (i % 4) in (0, 1) else r * .84
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    frm, to = (360, 0) if rev else (0, 360)
    return f"""<g opacity="{op}"><polygon points="{' '.join(pts)}" fill="none" stroke="{color}" stroke-width="2"/>
  <circle cx="{cx}" cy="{cy}" r="{r*.32:.1f}" fill="none" stroke="{color}" stroke-width="2"/>
  <animateTransform attributeName="transform" type="rotate" from="{frm} {cx} {cy}" to="{to} {cx} {cy}" dur="{dur}s" repeatCount="indefinite"/></g>"""


# ---- 1. banner -----------------------------------------------------------
def banner():
    W, H = 1200, 380
    lines = [
        ("spec.md", "agent", "STEP", "measured ✓"),
        ("scan.stl", "design intent", "parametric CAD", "verified ✓"),
        ("prompt", "MCP", "Siemens NX", "built ✓"),
    ]
    n = len(lines)
    rot = []
    for i, parts in enumerate(lines):
        txt = f'<tspan fill="{SARI}">$</tspan> ' + f' <tspan fill="{TITAN}">→</tspan> '.join(
            f'<tspan fill="{KROM if j < 3 else YESIL}">{escape(p)}</tspan>' for j, p in enumerate(parts))
        kt = ";".join(f"{v:.3f}" for v in [0, i / n, i / n + .02, (i + 1) / n - .02, (i + 1) / n, 1])
        vals = "0;0;1;1;0;0" if i else "1;1;1;1;0;0"
        if i == 0:
            kt, vals = f"0;{1/n - .02:.3f};{1/n:.3f};{1 - .02:.3f};1", "1;1;0;0;1"
        rot.append(f'<text x="64" y="300" font-family="{MONO}" font-size="18" opacity="0">{txt}'
                   f'<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="9s" repeatCount="indefinite"/></text>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img"
  aria-label="Muhammed İkbal Arıkan — agentic CAD researcher, with KUMPAS the caliper-bot">
<title>Muhammed İkbal Arıkan · Agentic CAD</title>
{grid_bg(W, H, 'b')}
{gear(1040, 70, 70, 14, CAMGOBEGI, 30)}
{gear(1138, 168, 42, 9, SARI, 18, rev=True)}
{gear(760, 350, 56, 12, KIRMIZI, 26, op=.14)}
<!-- chips -->
<g font-family="{SANS}" font-size="14" font-weight="700" letter-spacing="1">
  <rect x="64" y="52" width="196" height="32" rx="7" fill="{KOYU_KIRMIZI}"/>
  <circle cx="84" cy="68" r="5" fill="{KROM}"><animate attributeName="opacity" values="1;.2;1" dur="1.4s" repeatCount="indefinite"/></circle>
  <text x="98" y="73" fill="{KROM}">PhD RESEARCHER</text>
  <rect x="270" y="52" width="104" height="32" rx="7" fill="#3461a0"/>
  <text x="289" y="73" fill="{KROM}">@ KAUST</text>
</g>
<text x="62" y="150" font-family="{SANS}" font-size="58" font-weight="800" fill="{KROM}">Muhammed İkbal Arıkan</text>
<text x="64" y="200" font-family="{SANS}" font-size="27" font-weight="600" fill="{GUMUS}">I teach <tspan fill="{SARI}">AI agents</tspan> to draw <tspan fill="{SARI}">real</tspan> parts</text>
<text x="64" y="236" font-family="{SANS}" font-size="27" font-weight="600" fill="{GUMUS}">and <tspan fill="{CAMGOBEGI}">measure</tspan> every millimetre.</text>
<rect x="56" y="270" width="630" height="44" rx="9" fill="{GECE}" stroke="{GUNMETAL}" stroke-width="1.5"/>
{''.join(rot)}
<text x="64" y="350" font-family="{SANS}" font-size="15" font-weight="800" letter-spacing="2" fill="{CAMGOBEGI}">AGENTIC CAD · REVERSE ENGINEERING · MCP TOOLING</text>
<!-- dimension line above the mascot -->
<g stroke="{SARI}" stroke-width="2" fill="{SARI}">
  <path d="M852 92V112M1104 92V112" />
  <path d="M858 102H1098"/>
  <path d="M858 102l10-5v10zM1098 102l-10-5v10z" stroke="none"/>
</g>
<rect x="934" y="88" width="88" height="26" rx="5" fill="{DERIN}"/>
<text x="978" y="107" text-anchor="middle" font-family="{MONO}" font-size="16" font-weight="700" fill="{SARI}">Ø 42.00</text>
{kumpas(846, 118, .5, uid='banner')}
</svg>"""
    (OUT / "banner.svg").write_text(svg, encoding="utf-8")


# ---- 2. project cards ----------------------------------------------------
CARDS = [
    ("ReCADBench", "benchmark", CAMGOBEGI,
     ["Scan → parametric CAD reverse-engineering", "benchmark for AI agents. 10 tasks, scored."],
     ["benchmark", "reverse-eng", "STEP"]),
    ("turkisi-cad", "live league", KIRMIZI,
     ["Agentic CAD League: same model, 4 CAD tools,", "5 harnesses, 45 parts — drawn blind from a spec."],
     ["NX", "SolidWorks", "build123d"]),
    ("agentic_STL-to-CAD", "skills", SARI,
     ["SKILL.md pipeline: intake → measure →", "rebuild → independent verify → deliver."],
     ["Claude skills", "trimesh", "build123d"]),
    ("NX MCP", "mcp server", MAVI,
     ["MCP servers that let AI agents drive", "Siemens NX through NXOpen (47–130+ tools)."],
     ["MCP", "Siemens NX", "NXOpen"]),
    ("PoCAD", "phone cad", YESIL,
     ["Turns an old Android phone into a CAD station:", "live 3D viewer + Claude Code chat, side by side."],
     ["Termux", "build123d", "agentcad"]),
    ("open-dedica", "open hardware", "#F59E0B",
     ["Open-source DIY espresso machine: real Dedica", "internals in a fully open 3D-printed chassis."],
     ["3D scan", "STEP", "community"]),
]


def card(name, kind, accent, desc, tags, fname):
    W, H = 400, 168
    tag_svg, tx = [], 24
    for t in tags:
        w = 14 + 7.6 * len(t)
        tag_svg.append(f'<rect x="{tx}" y="126" width="{w:.0f}" height="24" rx="6" fill="{PANEL}" stroke="{GUNMETAL}"/>'
                       f'<text x="{tx + w/2:.0f}" y="142.5" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{GUMUS}">{escape(t)}</text>')
        tx += w + 8
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(name)}">
<title>{escape(name)}</title>
{grid_bg(W, H, fname, 20)}
<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="17" fill="none" stroke="{GUNMETAL}" stroke-width="1.5"/>
<rect x="0" y="22" width="5" height="40" rx="2" fill="{accent}"/>
<text x="24" y="50" font-family="{SANS}" font-size="23" font-weight="800" fill="{KROM}">{escape(name)}</text>
<text x="{W-22}" y="48" text-anchor="end" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="1" fill="{accent}">{escape(kind.upper())}</text>
<text font-family="{SANS}" font-size="15" fill="{GUMUS}"><tspan x="24" y="84">{escape(desc[0])}</tspan><tspan x="24" y="105">{escape(desc[1])}</tspan></text>
{''.join(tag_svg)}
</svg>"""
    (OUT / "cards" / f"{fname}.svg").write_text(svg, encoding="utf-8")


# ---- 3. agent pipeline ---------------------------------------------------
def pipeline():
    W, H = 1200, 215
    steps = [("spec.md / scan.stl", "input", TITAN), ("Planner", "intake + plan", MAVI),
             ("Drafter", "build123d · NX", SARI), ("QA gate", "re-measure", KIRMIZI),
             ("STEP + report", "delivered", YESIL)]
    bw, gap, y = 196, 50, 70
    x0 = (W - (5 * bw + 4 * gap)) / 2
    body = []
    for i, (t, sub, c) in enumerate(steps):
        x = x0 + i * (bw + gap)
        body.append(f'<rect x="{x:.0f}" y="{y}" width="{bw}" height="84" rx="12" fill="{GECE}" stroke="{c}" stroke-width="2"/>'
                    f'<text x="{x + bw/2:.0f}" y="{y+38}" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="800" fill="{KROM}">{escape(t)}</text>'
                    f'<text x="{x + bw/2:.0f}" y="{y+62}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c}">{escape(sub)}</text>')
        if i < 4:
            ax = x + bw + 6
            body.append(f'<path d="M{ax:.0f} {y+42}H{ax+gap-14:.0f}" stroke="{GUNMETAL}" stroke-width="3" stroke-dasharray="6 6">'
                        f'<animate attributeName="stroke-dashoffset" from="24" to="0" dur=".8s" repeatCount="indefinite"/></path>'
                        f'<path d="M{ax+gap-14:.0f} {y+35}l9 7-9 7z" fill="{GUMUS}"/>')
    # revise loop: QA gate -> Drafter
    xq = x0 + 3 * (bw + gap) + bw / 2
    xd = x0 + 2 * (bw + gap) + bw / 2
    loop = (f'<path d="M{xq:.0f} {y+84}V{y+128}H{xd:.0f}V{y+92}" fill="none" stroke="{KIRMIZI}" stroke-width="2.5" stroke-dasharray="7 6">'
            f'<animate attributeName="stroke-dashoffset" from="0" to="26" dur="1s" repeatCount="indefinite"/></path>'
            f'<path d="M{xd-7:.0f} {y+98}l7-9 7 9z" fill="{KIRMIZI}"/>'
            f'<rect x="{(xq+xd)/2-92:.0f}" y="{y+116}" width="184" height="24" rx="6" fill="{DERIN}"/>'
            f'<text x="{(xq+xd)/2:.0f}" y="{y+133}" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="700" fill="{KIRMIZI}">REVISE · max 3 loops</text>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Agent pipeline: input, planner, drafter, QA gate with revise loop, delivered STEP">
<title>How my CAD agents work</title>
{grid_bg(W, H, 'p')}
<text x="40" y="42" font-family="{MONO}" font-size="14" font-weight="700" letter-spacing="2" fill="{CAMGOBEGI}">// HOW MY CAD AGENTS WORK — NOTHING IS APPROVED UNTIL IT IS MEASURED</text>
{''.join(body)}
{loop}
</svg>"""
    (OUT / "pipeline.svg").write_text(svg, encoding="utf-8")


# ---- 4. Türkişi Engineering panel ---------------------------------------
def turkisi():
    W, H = 1200, 300
    stats = [("4", "CAD tools"), ("5", "harnesses"), ("45", "parts"), ("1", "model")]
    st = []
    for i, (n, l) in enumerate(stats):
        x = 450 + i * 150
        st.append(f'<rect x="{x}" y="196" width="136" height="70" rx="10" fill="{GECE}" stroke="{GUNMETAL}" stroke-width="1.5"/>'
                  f'<text x="{x+68}" y="234" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="800" fill="{SARI}">{n}</text>'
                  f'<text x="{x+68}" y="256" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{GUMUS}">{l}</text>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Türkişi Engineering YouTube channel and its mascot KUMPAS">
<title>Türkişi Engineering</title>
{grid_bg(W, H, 't')}
{gear(1110, 240, 80, 16, KIRMIZI, 34, op=.15)}
{kumpas(36, 40, .48, uid='te')}
<!-- speech bubble -->
<path d="M262 22h132a12 12 0 0 1 12 12v46a12 12 0 0 1-12 12H292l-26 18 6-18h-10a12 12 0 0 1-12-12V34a12 12 0 0 1 12-12z" fill="{KROM}"/>
<text x="328" y="51" text-anchor="middle" font-family="{SANS}" font-size="15" font-weight="800" fill="{GECE}">Ölçmeden</text>
<text x="328" y="73" text-anchor="middle" font-family="{SANS}" font-size="15" font-weight="800" fill="{GECE}">onay yok! 📏</text>
<g font-family="{SANS}">
  <rect x="450" y="40" width="176" height="30" rx="7" fill="{KOYU_KIRMIZI}"/>
  <text x="538" y="61" text-anchor="middle" font-size="13" font-weight="800" letter-spacing="1.5" fill="{KROM}">▶ YOUTUBE CHANNEL</text>
  <text x="448" y="116" font-size="44" font-weight="800" fill="{KROM}">Türkişi Engineering</text>
  <text x="450" y="152" font-size="19" fill="{GUMUS}">Agentic CAD and engineering, built live and in Turkish.</text>
  <text x="450" y="178" font-size="19" fill="{GUMUS}">Mascot: <tspan fill="{KIRMIZI}" font-weight="800">KUMPAS</tspan>, the caliper-bot that measures everything.</text>
</g>
{''.join(st)}
</svg>"""
    (OUT / "turkisi.svg").write_text(svg, encoding="utf-8")


# ---- 5. mascot alone (for small use) ------------------------------------
def mascot():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="160" height="160" viewBox="0 0 512 512" role="img" aria-label="KUMPAS">
<title>KUMPAS</title>{kumpas(0, 0, 1)}</svg>"""
    (OUT / "kumpas.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    (OUT / "cards").mkdir(exist_ok=True)
    banner()
    for c in CARDS:
        card(*c, fname=c[0].split(" ")[0].lower().replace("_", "-"))
    pipeline()
    turkisi()
    mascot()
    print("ok:", sorted(p.name for p in OUT.rglob("*.svg")))
