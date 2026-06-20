import os, re, sys

root = 'markdown_docs'
imgroot = os.path.join(root, 'img')
exts = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')
link_re = re.compile(r'!?\[[^\]]*\]\(([^)\s]+?)(?:\s+"[^"]*")?\)')

on_disk = set(os.listdir(imgroot))
referenced = set()
broken = []
non_img = []

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
                continue
            path = tgt.split('#')[0]
            if not path.startswith('img/'):
                non_img.append((fp.replace('\\', '/'), tgt))
                continue
            name = path[len('img/'):]
            referenced.add(name)
            if name not in on_disk:
                broken.append((fp.replace('\\', '/'), tgt))

print("images on disk:", len(on_disk))
print("distinct images referenced:", len(referenced))
print("broken references:", len(broken))
for x in broken[:20]:
    print("  BROKEN", x)
print("references not under img/:", len(non_img))
for x in non_img[:20]:
    print("  NONIMG", x)
orphans = on_disk - referenced
print("orphan images on disk (unreferenced):", len(orphans))

# Broken or stray references are failures; orphans are only a warning.
if broken or non_img:
    sys.exit(f"VERIFY FAILED: {len(broken)} broken, {len(non_img)} not under img/")
print("VERIFY OK")
