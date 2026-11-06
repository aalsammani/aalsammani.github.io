# -*- coding: utf-8 -*-
"""Regenerate preview/*.preview.html: self-contained copies of the seven generated pages
(stylesheet, scripts, portrait, and favicon inlined) that render correctly when opened as a
single file. Run after build.py:   python3 _build/make_previews.py
These files are for previewing only; the site itself is the root folder."""
import os, re, base64
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
PAGES = ['index', 'research', 'publications', 'group', 'teaching', 'cv', 'contact']

def read(rel, mode='r'):
    with open(os.path.join(ROOT, rel), mode, **({} if 'b' in mode else {'encoding': 'utf-8'})) as f:
        return f.read()

def data_uri(rel, mime):
    return f'data:{mime};base64,' + base64.b64encode(read(rel, 'rb')).decode('ascii')

CSS = read('assets/css/style.css')
JS = {p: read(p) for p in ('assets/js/main.js', 'assets/js/explorers.js')}
IMG = data_uri('assets/img/profile.jpg', 'image/jpeg')
ICO = data_uri('assets/img/favicon.svg', 'image/svg+xml')

os.makedirs(os.path.join(ROOT, 'preview'), exist_ok=True)
for name in PAGES:
    html = read(f'{name}.html')
    html = html.replace('<link rel="stylesheet" href="assets/css/style.css">', '<style>\n' + CSS + '\n</style>')
    for path, src in JS.items():
        html = html.replace(f'<script src="{path}" defer></script>', '<script>\ndocument.addEventListener("DOMContentLoaded",function(){\n' + src + '\n});\n</script>')
    html = html.replace('href="assets/img/favicon.svg"', f'href="{ICO}"')
    html = html.replace('src="assets/img/profile.jpg"', f'src="{IMG}"')
    # internal page links -> sibling previews; root files -> parent folder
    html = re.sub(r'href="(index|research|publications|group|teaching|cv|contact)\.html(#[^"]*)?"', lambda m: f'href="{m.group(1)}.preview.html{m.group(2) or ""}"', html)
    html = re.sub(r'href="((?:CV|AI-Guide-4-students)\.pdf)"', r'href="../\1"', html)
    with open(os.path.join(ROOT, 'preview', f'{name}.preview.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote preview/' + name + '.preview.html')
