import os, re, collections

root = 'markdown_docs'
# any markdown link/image target
link_re = re.compile(r'!?\[[^\]]*\]\(([^)\s]+)\)')
exts = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')

forms = collections.Counter()
unresolved = collections.Counter()
samples = collections.defaultdict(list)

for dp, _, fs in os.walk(root):
    for fn in fs:
        if not fn.endswith('.md'):
            continue
        fp = os.path.join(dp, fn)
        t = open(fp, encoding='utf-8').read()
        for m in link_re.finditer(t):
            tgt = m.group(1)
            low = tgt.split('#')[0].lower()
            if not low.endswith(exts):
                continue
            if tgt.startswith(('http://', 'https://', 'mailto:', 'data:')):
                forms['http'] += 1
                continue
            # classify
            if tgt.startswith('../'):
                key = 'dotdot'
            elif tgt.startswith('/'):
                key = 'abs'
            else:
                key = 'rel'
            forms[key] += 1
            # try resolve relative to md file dir and relative to root
            cand1 = os.path.normpath(os.path.join(dp, tgt))
            cand2 = os.path.normpath(os.path.join(root, tgt))
            # source candidate (strip markdown_docs prefix -> project source)
            src = os.path.normpath(os.path.join('.', tgt))
            if not (os.path.exists(cand1) or os.path.exists(cand2) or os.path.exists(src)):
                unresolved[key] += 1
                if len(samples[key]) < 8:
                    samples[key].append((fp.replace('\\', '/'), tgt))

print("forms:", dict(forms))
print("unresolved:", dict(unresolved))
for k, v in samples.items():
    print("---", k)
    for fp, tgt in v:
        print("   ", fp, "->", tgt)
