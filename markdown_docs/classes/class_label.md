# Label

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control for displaying plain text.

## Description

A control for displaying plain text. It gives you control over the horizontal and vertical alignment and can wrap the text inside the node's bounding rectangle. It doesn't support bold, italics, or other rich text formatting. For that, use [RichTextLabel](class_richtextlabel.md#class-richtextlabel) instead.

**Note:** A single Label node is not designed to display huge amounts of text. To display large amounts of text in a single node, consider using [RichTextLabel](class_richtextlabel.md#class-richtextlabel) instead as it supports features like an integrated scroll bar and threading. [RichTextLabel](class_richtextlabel.md#class-richtextlabel) generally performs better when displaying large amounts of text (several pages or more).

## Tutorials

- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)

## Properties

| [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode)                           | autowrap_mode                                                 | `0`                                                                                    |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]                       | autowrap_trim_flags                                     | `192`                                                                                  |
| [bool](class_bool.md#class-bool)                                                           | clip_text                                                         | `false`                                                                                |
| [String](class_string.md#class-string)                                                     | ellipsis_char                                                 | `"…"`                                                                                  |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)          | horizontal_alignment                                   | `0`                                                                                    |
| [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)]               | justification_flags                                     | `163`                                                                                  |
| [LabelSettings](class_labelsettings.md#class-labelsettings)                                | label_settings                                               |                                                                                        |
| [String](class_string.md#class-string)                                                     | language                                                           | `""`                                                                                   |
| [int](class_int.md#class-int)                                                              | lines_skipped                                                 | `0`                                                                                    |
| [int](class_int.md#class-int)                                                              | max_lines_visible                                         | `-1`                                                                                   |
| [MouseFilter](class_control.md#enum-control-mousefilter)                                   | mouse_filter                                                                                         | `2` (overrides [Control](class_control.md#class-control-property-mouse-filter))        |
| [String](class_string.md#class-string)                                                     | paragraph_separator                                     | `"\\n"`                                                                                |
| [[SizeFlags](class_control.md#enum-control-sizeflags)]                                     | size_flags_vertical                                                                                  | `4` (overrides [Control](class_control.md#class-control-property-size-flags-vertical)) |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser)           | structured_text_bidi_override                 | `0`                                                                                    |
| [Array](class_array.md#class-array)                                                        | structured_text_bidi_override_options | `[]`                                                                                   |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)                 | tab_stops                                                         | `PackedFloat32Array()`                                                                 |
| [String](class_string.md#class-string)                                                     | text                                                                   | `""`                                                                                   |
| [TextDirection](class_control.md#enum-control-textdirection)                               | text_direction                                               | `0`                                                                                    |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior)                     | text_overrun_behavior                                 | `0`                                                                                    |
| [bool](class_bool.md#class-bool)                                                           | uppercase                                                         | `false`                                                                                |
| [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment)              | vertical_alignment                                       | `0`                                                                                    |
| [int](class_int.md#class-int)                                                              | visible_characters                                       | `-1`                                                                                   |
| [VisibleCharactersBehavior](class_textserver.md#enum-textserver-visiblecharactersbehavior) | visible_characters_behavior                     | `0`                                                                                    |
| [float](class_float.md#class-float)                                                        | visible_ratio                                                 | `1.0`                                                                                  |

## Methods

| [Rect2](class_rect2.md#class-rect2)   | get_character_bounds(pos: [int](class_int.md#class-int))    |
|---------------------------------------|---------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)         | get_line_count()                                                  |
| [int](class_int.md#class-int)         | get_line_height(line: [int](class_int.md#class-int) = -1)        |
| [int](class_int.md#class-int)         | get_total_character_count()                            |
| [int](class_int.md#class-int)         | get_visible_line_count()                                  |

## Theme Properties

| [Color](class_color.md#class-color)          | font_color                      | `Color(1, 1, 1, 1)`   |
|----------------------------------------------|------------------------------------------------------------------------|-----------------------|
| [Color](class_color.md#class-color)          | font_outline_color      | `Color(0, 0, 0, 1)`   |
| [Color](class_color.md#class-color)          | font_shadow_color        | `Color(0, 0, 0, 0)`   |
| [int](class_int.md#class-int)                | line_spacing               | `3`                   |
| [int](class_int.md#class-int)                | outline_size               | `0`                   |
| [int](class_int.md#class-int)                | paragraph_spacing     | `0`                   |
| [int](class_int.md#class-int)                | shadow_offset_x         | `1`                   |
| [int](class_int.md#class-int)                | shadow_offset_y         | `1`                   |
| [int](class_int.md#class-int)                | shadow_outline_size | `1`                   |
| [Font](class_font.md#class-font)             | font                                   |                       |
| [int](class_int.md#class-int)                | font_size                    |                       |
| [StyleBox](class_stylebox.md#class-stylebox) | focus                                |                       |
| [StyleBox](class_stylebox.md#class-stylebox) | normal                              |                       |

---

## Property Descriptions

[AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **autowrap_mode** = `0`

-  **set_autowrap_mode**(value: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode))
- [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **get_autowrap_mode**()

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off), the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

**Note:** Labels with autowrapping enabled must have a custom maximum width configured to work correctly, either through the Label's own [Control.custom_maximum_size](class_control.md#class-control-property-custom-maximum-size) or as a result of a propagated maximum size from a parent Control with [Control.propagate_maximum_size](class_control.md#class-control-property-propagate-maximum-size) enabled.

---

[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **autowrap_trim_flags** = `192`

-  **set_autowrap_trim_flags**(value: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])
- [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **get_autowrap_trim_flags**()

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-start-edge-spaces) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-end-edge-spaces) for more info.

---

[bool](class_bool.md#class-bool) **clip_text** = `false`

-  **set_clip_text**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_clipping_text**()

If `true`, the Label only shows the text that fits inside its bounding rectangle and will clip text horizontally.

---

[String](class_string.md#class-string) **ellipsis_char** = `"…"`

-  **set_ellipsis_char**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_ellipsis_char**()

Ellipsis character used for text clipping.

---

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **horizontal_alignment** = `0`

-  **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---

[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **justification_flags** = `163`

-  **set_justification_flags**(value: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_justification_flags**()

Line fill alignment rules.

---

[LabelSettings](class_labelsettings.md#class-labelsettings) **label_settings**

-  **set_label_settings**(value: [LabelSettings](class_labelsettings.md#class-labelsettings))
- [LabelSettings](class_labelsettings.md#class-labelsettings) **get_label_settings**()

A [LabelSettings](class_labelsettings.md#class-labelsettings) resource that can be shared between multiple **Label** nodes. Takes priority over theme properties.

---

[String](class_string.md#class-string) **language** = `""`

-  **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

[int](class_int.md#class-int) **lines_skipped** = `0`

-  **set_lines_skipped**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_lines_skipped**()

The number of the lines ignored and not displayed from the start of the text value.

---

[int](class_int.md#class-int) **max_lines_visible** = `-1`

-  **set_max_lines_visible**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_lines_visible**()

Limits the lines of text the node shows on screen.

---

[String](class_string.md#class-string) **paragraph_separator** = `"\\n"`

-  **set_paragraph_separator**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_paragraph_separator**()

String used as a paragraph separator. Each paragraph is processed independently, in its own BiDi context.

---

[StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **structured_text_bidi_override** = `0`

-  **set_structured_text_bidi_override**(value: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser))
- [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

---

[Array](class_array.md#class-array) **structured_text_bidi_override_options** = `[]`

-  **set_structured_text_bidi_override_options**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

---

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **tab_stops** = `PackedFloat32Array()`

-  **set_tab_stops**(value: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))
- [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_tab_stops**()

Aligns text to the given tab-stops.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) for more details.

---

[String](class_string.md#class-string) **text** = `""`

-  **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

The text to display on screen.

---

[TextDirection](class_control.md#enum-control-textdirection) **text_direction** = `0`

-  **set_text_direction**(value: [TextDirection](class_control.md#enum-control-textdirection))
- [TextDirection](class_control.md#enum-control-textdirection) **get_text_direction**()

Base text writing direction.

---

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **text_overrun_behavior** = `0`

-  **set_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the node's bounding rectangle.

---

[bool](class_bool.md#class-bool) **uppercase** = `false`

-  **set_uppercase**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_uppercase**()

If `true`, all the text displays as UPPERCASE.

---

[VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **vertical_alignment** = `0`

-  **set_vertical_alignment**(value: [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment))
- [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **get_vertical_alignment**()

Controls the text's vertical alignment. Supports top, center, bottom, and fill.

---

[int](class_int.md#class-int) **visible_characters** = `-1`

-  **set_visible_characters**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_visible_characters**()

The number of characters to display. If set to `-1`, all characters are displayed. This can be useful when animating the text appearing in a dialog box.

**Note:** Setting this property updates visible_ratio accordingly.

**Note:** Characters are counted as Unicode codepoints. A single visible grapheme may contain multiple codepoints (e.g. certain emoji use three codepoints). A single codepoint may contain two UTF-16 characters, which are used in C# strings.

---

[VisibleCharactersBehavior](class_textserver.md#enum-textserver-visiblecharactersbehavior) **visible_characters_behavior** = `0`

-  **set_visible_characters_behavior**(value: [VisibleCharactersBehavior](class_textserver.md#enum-textserver-visiblecharactersbehavior))
- [VisibleCharactersBehavior](class_textserver.md#enum-textserver-visiblecharactersbehavior) **get_visible_characters_behavior**()

The clipping behavior when visible_characters or visible_ratio is set.

---

[float](class_float.md#class-float) **visible_ratio** = `1.0`

-  **set_visible_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_visible_ratio**()

The fraction of characters to display, relative to the total number of characters (see get_total_character_count()). If set to `1.0`, all characters are displayed. If set to `0.5`, only half of the characters will be displayed. This can be useful when animating the text appearing in a dialog box.

**Note:** Setting this property updates visible_characters accordingly.

---

## Method Descriptions

[Rect2](class_rect2.md#class-rect2) **get_character_bounds**(pos: [int](class_int.md#class-int))

Returns the bounding rectangle of the character at position `pos` in the label's local coordinate system. If the character is a non-visual character or `pos` is outside the valid range, an empty [Rect2](class_rect2.md#class-rect2) is returned. If the character is a part of a composite grapheme, the bounding rectangle of the whole grapheme is returned.

---

[int](class_int.md#class-int) **get_line_count**()

Returns the number of lines of text the Label has.

---

[int](class_int.md#class-int) **get_line_height**(line: [int](class_int.md#class-int) = -1)

Returns the height of the line `line`.

If `line` is set to `-1`, returns the biggest line height.

If there are no lines, returns font size in pixels.

---

[int](class_int.md#class-int) **get_total_character_count**()

Returns the total number of printable characters in the text (excluding spaces and newlines).

---

[int](class_int.md#class-int) **get_visible_line_count**()

Returns the number of lines shown. Useful if the **Label**'s height cannot currently display all lines.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **font_color** = `Color(1, 1, 1, 1)`

Default text [Color](class_color.md#class-color) of the **Label**.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The color of text outline.

---

[Color](class_color.md#class-color) **font_shadow_color** = `Color(0, 0, 0, 0)`

[Color](class_color.md#class-color) of the text's shadow effect.

---

[int](class_int.md#class-int) **line_spacing** = `3`

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

[int](class_int.md#class-int) **outline_size** = `0`

Text outline size.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

**Note:** Using a value that is larger than half the font size is not recommended, as the font outline may fail to be fully closed in this case.

---

[int](class_int.md#class-int) **paragraph_spacing** = `0`

Vertical space between paragraphs. Added on top of line_spacing.

---

[int](class_int.md#class-int) **shadow_offset_x** = `1`

The horizontal offset of the text's shadow.

---

[int](class_int.md#class-int) **shadow_offset_y** = `1`

The vertical offset of the text's shadow.

---

[int](class_int.md#class-int) **shadow_outline_size** = `1`

The size of the shadow outline.

---

[Font](class_font.md#class-font) **font**

[Font](class_font.md#class-font) used for the **Label**'s text.

---

[int](class_int.md#class-int) **font_size**

Font size of the **Label**'s text.

---

[StyleBox](class_stylebox.md#class-stylebox) **focus**

[StyleBox](class_stylebox.md#class-stylebox) used when the **Label** is focused (when used with assistive apps).

---

[StyleBox](class_stylebox.md#class-stylebox) **normal**

Background [StyleBox](class_stylebox.md#class-stylebox) for the **Label**.
