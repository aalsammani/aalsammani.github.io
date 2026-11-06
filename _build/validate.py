# -*- coding: utf-8 -*-
"""Offline checks for the generated site. Run from the site root after build.py:
    python3 _build/validate.py            # structure, internal links, data consistency
    python3 _build/validate.py --external # also resolve every DOI and external link (network)
Exit status is non-zero if any check fails."""
import os, re, sys, json, html.parser, urllib.request, urllib.parse, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..'))
PAGES = ['index', 'research', 'publications', 'group', 'teaching', 'cv', 'contact']
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr',
        'path', 'circle', 'rect', 'line', 'use', 'stop', 'ellipse', 'polyline', 'polygon'}
errors, warnings = [], []
def err(m): errors.append(m)
def warn(m): warnings.append(m)

class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.links, self.imgs, self.heads, self.text = [], [], [], [], [], []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a' and 'href' in a: self.links.append(a['href'])
        if tag in ('link', 'script', 'img') and (a.get('href') or a.get('src')):
            self.links.append(a.get('href') or a.get('src'))
        if tag == 'img': self.imgs.append(a)
        if re.fullmatch(r'h[1-6]', tag): self.heads.append(int(tag[1]))
        if tag not in VOID: self.stack.append((tag, self.getpos()[0]))
    def handle_startendtag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
    def handle_endtag(self, tag):
        if tag in VOID: return
        if not self.stack: err(f'{self.name}: stray </{tag}> line {self.getpos()[0]}'); return
        if self.stack[-1][0] == tag: self.stack.pop(); return
        if any(t == tag for t, _ in self.stack):
            while self.stack and self.stack[-1][0] != tag:
                t, ln = self.stack.pop()
                if t not in ('p', 'li', 'td', 'th', 'tr', 'option'):
                    err(f'{self.name}: <{t}> opened line {ln} not closed before </{tag}>')
            self.stack.pop()
        else:
            err(f'{self.name}: unexpected </{tag}> line {self.getpos()[0]}')
    def handle_data(self, d): self.text.append(d)

parsed = {}
for name in PAGES:
    src = open(os.path.join(ROOT, name + '.html'), encoding='utf-8').read()
    p = Page(); p.name = name + '.html'; p.feed(src); p.close(); parsed[name] = p
    if re.search(r'<\s+[a-zA-Z]', src): err(f'{p.name}: malformed tag ("< tag")')
    left = [t for t, _ in p.stack if t not in ('p', 'li')]
    if left: err(f'{p.name}: unclosed elements {left}')
    dup = {i for i in p.ids if p.ids.count(i) > 1}
    if dup: err(f'{p.name}: duplicate ids {sorted(dup)}')
    if p.heads.count(1) != 1: err(f'{p.name}: expected exactly one <h1>, found {p.heads.count(1)}')
    for a, b in zip(p.heads, p.heads[1:]):
        if b > a + 1: warn(f'{p.name}: heading level jumps h{a} -> h{b}')
    for im in p.imgs:
        if not im.get('alt'): err(f'{p.name}: <img> without alt ({im.get("src", "")[:40]})')
    for m in ('<title>', 'name="description"', 'rel="canonical"', 'name="viewport"'):
        if m not in src: err(f'{p.name}: missing {m}')

# internal links and anchors
for name, p in parsed.items():
    for href in p.links:
        if href.startswith(('http://', 'https://', 'mailto:', 'data:', '//')): continue
        path, _, frag = href.partition('#')
        target = path or name + '.html'
        if not os.path.exists(os.path.join(ROOT, target)): err(f'{name}.html: broken link {href}'); continue
        if frag and target.endswith('.html'):
            tp = parsed.get(target[:-5])
            if tp and frag not in tp.ids: err(f'{name}.html: missing anchor {href}')

# data <-> HTML consistency
pubs = json.load(open(os.path.join(ROOT, '_data', 'publications.json'), encoding='utf-8'))
ids = [x['id'] for x in pubs]
if len(ids) != len(set(ids)): err('publications.json: duplicate ids')
pubhtml = open(os.path.join(ROOT, 'publications.html'), encoding='utf-8').read()
for x in pubs:
    if x['type'] not in ('journal', 'conference', 'preprint', 'abstract', 'other'): err(f'{x["id"]}: bad type')
    if x.get('status') not in (None, 'accepted'): err(f'{x["id"]}: bad status')
    if x.get('status') == 'accepted' and any('doi.org/10.' in u and 'zenodo' not in u for u in x['links'].values()):
        warn(f'{x["id"]}: accepted record carries a journal DOI; if published, remove "status"')
    if x['title'] not in pubhtml: err(f'{x["id"]}: title not rendered in publications.html')
n_accepted = sum(1 for x in pubs if x.get('status') == 'accepted')
if pubhtml.count('Accepted (in press)') != n_accepted + sum(1 for x in pubs if x.get('status') == 'accepted' and x.get('selected')):
    err('publications.html: accepted label count does not match data')
for n in ('news', 'featured', 'resources', 'people'):
    json.load(open(os.path.join(ROOT, '_data', n + '.json'), encoding='utf-8'))
if sum(1 for x in json.load(open(os.path.join(ROOT, '_data', 'news.json'), encoding='utf-8')) if x.get('home')) != 3:
    warn('news.json: expected exactly three "home": true items')

# optional: external links and DOIs
if '--external' in sys.argv:
    urls = sorted({u for p in parsed.values() for u in p.links if u.startswith('http')})
    UA = {'User-Agent': 'Mozilla/5.0 (site link check)'}
    for u in urls:
        if 'fonts.g' in u: continue
        m = re.match(r'https://doi\.org/(10\..+)$', u)
        try:
            if m:  # ask the DOI registry directly (publisher sites often block scripts)
                api = 'https://doi.org/api/handles/' + urllib.parse.quote(urllib.parse.unquote(m.group(1)), safe='/')
                code = json.load(urllib.request.urlopen(urllib.request.Request(api, headers=UA), timeout=30)).get('responseCode')
                (print if code == 1 else err)(f'DOI {"ok" if code == 1 else "NOT REGISTERED"}: {u}')
            else:
                r = urllib.request.urlopen(urllib.request.Request(u.replace('&amp;', '&'), headers=UA), timeout=30)
                print(f'{r.status}: {u}')
        except urllib.error.HTTPError as e:
            (warn if e.code in (401, 403, 429, 999) else err)(f'HTTP {e.code}: {u}')
        except Exception as e:
            warn(f'unreachable ({type(e).__name__}): {u}')

for w in warnings: print('WARN ', w)
for e in errors: print('ERROR', e)
print(f'{len(errors)} error(s), {len(warnings)} warning(s)')
sys.exit(1 if errors else 0)
