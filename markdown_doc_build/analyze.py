import os, collections, hashlib

exts = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')
files = []
for dp, dirs, fs in os.walk('.'):
    norm = dp.replace('\\', '/')
    if norm.startswith('./markdown_docs') or '/.git' in norm or norm.startswith('./.git'):
        continue
    for fn in fs:
        if fn.lower().endswith(exts):
            p = os.path.join(dp, fn).replace('\\', '/')
            if p.startswith('./'):
                p = p[2:]
            files.append(p)

print("source images total:", len(files))
bn = collections.defaultdict(list)
for f in files:
    bn[os.path.basename(f)].append(f)
cols = {k: v for k, v in bn.items() if len(v) > 1}
print("basename collisions among source:", len(cols))


def h(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


bad = 0
for k, v in cols.items():
    hs = {h(p) for p in v}
    status = 'SAME' if len(hs) == 1 else '*** DIFFERENT ***'
    if len(hs) != 1:
        bad += 1
    print(f"{k}: {status}")
    for p in v:
        print("    ", p)
print("collisions with DIFFERENT content:", bad)
