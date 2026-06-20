# Markdown 文档构建流程

Conda env: `godot-docs`

## 一键执行（推荐）

在 `godot-docs` 环境下，于项目根目录运行：

```
python markdown_doc_build/build_all.py
```

可选参数：

- `--skip-build`：跳过 Sphinx 构建，复用现有 `markdown_docs/` 输出，仅跑后处理（步骤 2-4）。

## 流程说明（build_all.py 依次执行 4 步）

### 1. Sphinx 构建
```
python -m sphinx -T -j auto -b markdown -d _build/doctrees -D language=en . markdown_docs
```
生成 `markdown_docs/` 下全部 `.md`。完整日志写入 `markdown_doc_build/build.log`。

### 2. 清理 Markdown（clean_md.py）
按顺序处理（先删 🔗 再剥锚点链接，避免裸 🔗 残留）：
- HTML 注释：`<!--[\s\S]*?-->[\r\n]*`
- 独立锚点行：`<a id="[^"]*"></a>\n+`
- 行末 🔗 永久链接图标：`[ \t]*\[🔗\]\([^)]*\)[ \t]*$`（MULTILINE）。纯 UI 噪声，全删。
- 页内参照死链：`[text](#anchor)` → 剥壳留 `text`。因上一步已删 `<a id>` 着地点，
  这些指向 `#...` 的链接已失效；跨文件链接 `[text](file.md#anchor)`（不以 `#` 开头）保留不动。

（注：表格单元格内、无换行结尾的内联 `<a id>` 不匹配该正则，会被保留。）

### 3. 图片归集 + 引用重写（migrate_images.py）
- 把所有被引用的图片汇总到 `markdown_docs/img/`。
- 重写 md 中的全部图片引用，如 `about/img/unstable.png` → `img/unstable.png`。
- 同名不同内容的图片冲突，用 `_N` 后缀消歧（避免互相覆盖）。
- 清理 Sphinx 重新生成的各子目录 `img/`，以及 `img/` 下的 0 字节占位图。

### 4. 校验（verify.py）
检查每个 `img/...` 引用都有对应文件；存在断链或越界引用时以非 0 退出码失败。
（未被本地引用的"孤儿图"仅告警，不算失败。）

## 辅助脚本（非主流程，分析用）
- `analyze.py`：统计源图片的同名冲突情况。
- `survey_refs.py`：统计 md 中图片引用的各种形态。
