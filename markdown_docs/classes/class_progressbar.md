# ProgressBar

**Inherits:** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control used for visual representation of a percentage.

## Description

A control used for visual representation of a percentage. Shows the fill percentage in the center. Can also be used to show indeterminate progress. For more fill modes, use [TextureProgressBar](class_textureprogressbar.md#class-textureprogressbar) instead.

## Properties

| [bool](class_bool.md#class-bool)   | editor_preview_indeterminate   |         |
|------------------------------------|--------------------------------------------------------------------------------------------|---------|
| [int](class_int.md#class-int)      | fill_mode                                         | `0`     |
| [bool](class_bool.md#class-bool)   | indeterminate                                 | `false` |
| [bool](class_bool.md#class-bool)   | show_percentage                             | `true`  |

## Theme Properties

| [Color](class_color.md#class-color)          | font_color                 | `Color(0.95, 0.95, 0.95, 1)`   |
|----------------------------------------------|-------------------------------------------------------------------------|--------------------------------|
| [Color](class_color.md#class-color)          | font_outline_color | `Color(0, 0, 0, 1)`            |
| [int](class_int.md#class-int)                | outline_size          | `0`                            |
| [Font](class_font.md#class-font)             | font                              |                                |
| [int](class_int.md#class-int)                | font_size               |                                |
| [StyleBox](class_stylebox.md#class-stylebox) | background                 |                                |
| [StyleBox](class_stylebox.md#class-stylebox) | fill                             |                                |

---

## Enumerations

enum **FillMode**:

FillMode **FILL_BEGIN_TO_END** = `0`

The progress bar fills from begin to end horizontally, according to the language direction. If [Control.is_layout_rtl()](class_control.md#class-control-method-is-layout-rtl) returns `false`, it fills from left to right, and if it returns `true`, it fills from right to left.

FillMode **FILL_END_TO_BEGIN** = `1`

The progress bar fills from end to begin horizontally, according to the language direction. If [Control.is_layout_rtl()](class_control.md#class-control-method-is-layout-rtl) returns `false`, it fills from right to left, and if it returns `true`, it fills from left to right.

FillMode **FILL_TOP_TO_BOTTOM** = `2`

The progress fills from top to bottom.

FillMode **FILL_BOTTOM_TO_TOP** = `3`

The progress fills from bottom to top.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **editor_preview_indeterminate**

-  **set_editor_preview_indeterminate**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editor_preview_indeterminate_enabled**()

If `false`, the indeterminate animation will be paused in the editor.

---

[int](class_int.md#class-int) **fill_mode** = `0`

-  **set_fill_mode**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fill_mode**()

The fill direction. See FillMode for possible values.

---

[bool](class_bool.md#class-bool) **indeterminate** = `false`

-  **set_indeterminate**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_indeterminate**()

When set to `true`, the progress bar indicates that something is happening with an animation, but does not show the fill percentage or value.

---

[bool](class_bool.md#class-bool) **show_percentage** = `true`

-  **set_show_percentage**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_percentage_shown**()

If `true`, the fill percentage is displayed on the bar.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **font_color** = `Color(0.95, 0.95, 0.95, 1)`

The color of the text.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The tint of text outline of the **ProgressBar**.

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[Font](class_font.md#class-font) **font**

Font used to draw the fill percentage if show_percentage is `true`.

---

[int](class_int.md#class-int) **font_size**

Font size used to draw the fill percentage if show_percentage is `true`.

---

[StyleBox](class_stylebox.md#class-stylebox) **background**

The style of the background.

---

[StyleBox](class_stylebox.md#class-stylebox) **fill**

The style of the progress (i.e. the part that fills the bar).
