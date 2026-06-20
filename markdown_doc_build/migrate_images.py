import os, re, shutil, hashlib, collections

root = 'markdown_docs'
imgroot = os.path.join(root, 'img')
exts = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')
link_re = re.compile(r'(!?\[[^\]]*\]\()([^)\s]+?)(\s+"[^"]*")?(\))')


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


# 1. Resolve every image reference in every md file to an existing SOURCE file.
#    Build the set of source files that are actually referenced + their resolution.
md_files = []
for dp, _, fs in os.walk(root):
    for fn in fs:
        if fn.endswith('.md'):
            md_files.append(os.path.join(dp, fn))


def resolve(md_path, tgt):
    """Return existing source path (project tree, outside markdown_docs) for a ref, or None."""
    path = tgt.split('#')[0]
    md_dir = os.path.dirname(md_path)
    # markdown_docs mirrors project layout; project source dir for this md file:
    src_dir = os.path.relpath(md_dir, root)  # e.g. tutorials/2d
    candidates = []
    # root-relative (most common): tgt is relative to markdown_docs root == project root
    candidates.append(os.path.normpath(path))
    # file-relative: relative to the md file's source dir
    candidates.append(os.path.normpath(os.path.join(src_dir, path)))
    for c in candidates:
        if os.path.isfile(c) and c.lower().endswith(exts):
            return c.replace('\\', '/')
    return None


# 2. Collect all referenced source files, assign flattened target names (handle collisions).
referenced = {}  # src_path -> None (placeholder)
for md in md_files:
    t = open(md, encoding='utf-8').read()
    for m in link_re.finditer(t):
        tgt = m.group(2)
        low = tgt.split('#')[0].lower()
        if not low.endswith(exts):
            continue
        if tgt.startswith(('http://', 'https://', 'mailto:', 'data:')):
            continue
        src = resolve(md, tgt)
        if src:
            referenced[src] = None

# assign names: basename, disambiguate collisions by content
by_base = collections.defaultdict(list)
for src in referenced:
    by_base[os.path.basename(src)].append(src)

assigned = {}  # src_path -> flat filename
used = set()
for base, srcs in by_base.items():
    if len(srcs) == 1:
        assigned[srcs[0]] = base
        used.add(base)
    else:
        # group by content hash
        h2srcs = collections.defaultdict(list)
        for s in srcs:
            h2srcs[md5(s)].append(s)
        stem, ext = os.path.splitext(base)
        first = True
        for i, (h, group) in enumerate(sorted(h2srcs.items())):
            if first:
                name = base
                first = False
            else:
                # disambiguate
                k = 1
                name = f"{stem}_{k}{ext}"
                while name in used:
                    k += 1
                    name = f"{stem}_{k}{ext}"
            used.add(name)
            for s in group:
                assigned[s] = name

print("referenced source images:", len(referenced))
print("flattened target names:", len(set(assigned.values())))

# Unambiguous basename -> flat name lookup (fallback for refs that don't resolve
# to a source file directly, e.g. Sphinx "../../_images/foo.webp" full-size links).
base_lookup = collections.defaultdict(set)
for src, name in assigned.items():
    base_lookup[os.path.basename(src)].add(name)

# 3. Copy source images into markdown_docs/img
os.makedirs(imgroot, exist_ok=True)
for src, name in assigned.items():
    shutil.copy2(src, os.path.join(imgroot, name))
print("copied to", imgroot)

# 4. Rewrite references in md files.
unresolved = []
rewritten = 0


def make_repl(md):
    def repl(m):
        global rewritten
        pre, tgt, title, close = m.group(1), m.group(2), m.group(3) or '', m.group(4)
        low = tgt.split('#')[0].lower()
        if not low.endswith(exts) or tgt.startswith(('http://', 'https://', 'mailto:', 'data:')):
            return m.group(0)
        # keep any anchor fragment (rare for images)
        frag = ''
        path = tgt
        if '#' in tgt:
            path, frag = tgt.split('#', 1)
            frag = '#' + frag
        src = resolve(md, tgt)
        if src and src in assigned:
            name = assigned[src]
        else:
            # Fallback: match by basename (handles Sphinx "_images/" full-size
            # links and other forms that don't resolve to a source path).
            cands = base_lookup.get(os.path.basename(path), set())
            if len(cands) == 1:
                name = next(iter(cands))
            else:
                unresolved.append((md.replace('\\', '/'), tgt))
                return m.group(0)
        newtgt = 'img/' + name + frag
        rewritten += 1
        return f"{pre}{newtgt}{title}{close}"
    return repl


for md in md_files:
    t = open(md, encoding='utf-8').read()
    nt = link_re.sub(make_repl(md), t)
    if nt != t:
        with open(md, 'w', encoding='utf-8', newline='') as f:
            f.write(nt)

print("rewritten references:", rewritten)
print("unresolved references:", len(unresolved))
for md, tgt in unresolved[:20]:
    print("   ", md, "->", tgt)

# 5. Cleanup: remove the scattered per-directory img/ folders that Sphinx
#    recreated (their files are now consolidated in markdown_docs/img/), then
#    drop any 0-byte placeholder images left in markdown_docs/img/.
removed_dirs = 0
keep = os.path.normpath(imgroot)
for dp, dirs, _ in os.walk(root):
    for d in list(dirs):
        full = os.path.join(dp, d)
        if d == 'img' and os.path.normpath(full) != keep:
            shutil.rmtree(full)
            dirs.remove(d)  # don't let os.walk descend into the deleted dir
            removed_dirs += 1
print("removed scattered img/ dirs:", removed_dirs)

removed_empty = 0
for fn in os.listdir(imgroot):
    fp = os.path.join(imgroot, fn)
    if os.path.isfile(fp) and os.path.getsize(fp) == 0:
        os.remove(fp)
        removed_empty += 1
print("removed 0-byte images:", removed_empty)
