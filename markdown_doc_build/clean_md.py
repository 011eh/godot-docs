import os, re

root = 'markdown_docs'
comment_re = re.compile(r'<!--[\s\S]*?-->[\r\n]*')
anchor_re = re.compile(r'<a id="[^"]*"></a>\n+')
# 🔗 "section permalink" icon at end of a line (eat leading/trailing blanks).
# \U0001F517 == 🔗 ; used as escape to stay source-encoding agnostic.
link_icon_re = re.compile(r'[ \t]*\[\U0001F517\]\([^)]*\)[ \t]*$', re.MULTILINE)
# In-page reference links [text](#anchor): the <a id> targets above are gone,
# so these are dead links -> unwrap to plain text. The text may itself contain
# one nested [...] pair (e.g. "operator []", "Handling [url] tag clicks").
# Cross-file links [text](file.md#anchor) end with ](file... not ](# -> untouched.
inpage_link_re = re.compile(r'\[((?:[^\[\]]|\[[^\]]*\])*)\]\(#[^)]*\)')

changed = 0
for dp, _, fs in os.walk(root):
    for fn in fs:
        if not fn.endswith('.md'):
            continue
        fp = os.path.join(dp, fn)
        with open(fp, encoding='utf-8') as f:
            t = f.read()
        nt = comment_re.sub('', t)
        nt = anchor_re.sub('', nt)
        nt = link_icon_re.sub('', nt)        # 1) drop 🔗 icons (end of line)
        nt = inpage_link_re.sub(r'\1', nt)   # 2) unwrap dead in-page links
        if nt != t:
            with open(fp, 'w', encoding='utf-8', newline='') as f:
                f.write(nt)
            changed += 1

print("cleaned files:", changed)
