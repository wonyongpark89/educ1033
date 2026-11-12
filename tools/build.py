"""Build a self-contained slide deck: inline images and number the slides.

Usage: python tools/build.py w9
Reads <week>/src/deck.html, <week>/src/img/* and <week>/src/icons/*.svg
(Lucide icons, ISC licence), writes <week>/index.html.
"""
import base64, pathlib, re, sys

week = pathlib.Path(__file__).resolve().parent.parent / sys.argv[1]
html = (week / 'src' / 'deck.html').read_text(encoding='utf-8')

def inline(m):
    p = next((week / 'src' / 'img').glob(m.group(1) + '.*'))
    mime = 'image/png' if p.suffix == '.png' else 'image/jpeg'
    return f'data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}'

html = re.sub(r'\{\{IMG:(\w+)\}\}', inline, html)

def icon(m):
    svg = (week / 'src' / 'icons' / (m.group(1) + '.svg')).read_text(encoding='utf-8')
    svg = re.sub(r'<!--.*?-->', '', svg, flags=re.S)
    svg = re.sub(r'\s*(class|width|height)="[^"]*"', '', svg)
    svg = re.sub(r'\s+', ' ', svg).strip().replace('<svg ', '<svg aria-hidden="true" ', 1)
    return svg.replace(' />', '/>').replace('> <', '><')

html = re.sub(r'\{\{ICON:([\w-]+)\}\}', icon, html)
n = iter(range(1, 1000))
html = re.sub(r'<div data-n class="slide', lambda m: f'<div data-n="{next(n)}" class="slide', html)
out = week / 'index.html'
out.write_text(html, encoding='utf-8')
print(out, f'{out.stat().st_size/1e6:.2f} MB', html.count('class="frame"'), 'slides')
