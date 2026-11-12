"""Build a self-contained slide deck: inline images and number the slides.

Usage: python tools/build.py w9
Reads <week>/src/deck.html and <week>/src/img/*, writes <week>/index.html.
"""
import base64, pathlib, re, sys

week = pathlib.Path(__file__).resolve().parent.parent / sys.argv[1]
html = (week / 'src' / 'deck.html').read_text(encoding='utf-8')

def inline(m):
    p = next((week / 'src' / 'img').glob(m.group(1) + '.*'))
    mime = 'image/png' if p.suffix == '.png' else 'image/jpeg'
    return f'data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}'

html = re.sub(r'\{\{IMG:(\w+)\}\}', inline, html)
n = iter(range(1, 1000))
html = re.sub(r'<div data-n class="slide', lambda m: f'<div data-n="{next(n)}" class="slide', html)
out = week / 'index.html'
out.write_text(html, encoding='utf-8')
print(out, f'{out.stat().st_size/1e6:.2f} MB', html.count('class="frame"'), 'slides')
