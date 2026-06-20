# TextParagraph

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds a paragraph of text.

## Description

Abstraction over [TextServer](class_textserver.md#class-textserver) for handling a single paragraph of text.

## Properties

| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)   | alignment                         | `0`     |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------|---------|
| [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]                | break_flags                     | `3`     |
| [String](class_string.md#class-string)                                              | custom_punctuation       | `""`    |
| [Direction](class_textserver.md#enum-textserver-direction)                          | direction                         | `0`     |
| [String](class_string.md#class-string)                                              | ellipsis_char                 | `"…"`   |
| [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)]        | justification_flags     | `163`   |
| [float](class_float.md#class-float)                                                 | line_spacing                   | `0.0`   |
| [int](class_int.md#class-int)                                                       | max_lines_visible         | `-1`    |
| [Orientation](class_textserver.md#enum-textserver-orientation)                      | orientation                     | `0`     |
| [bool](class_bool.md#class-bool)                                                    | preserve_control           | `false` |
| [bool](class_bool.md#class-bool)                                                    | preserve_invalid           | `true`  |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior)              | text_overrun_behavior | `0`     |
| [float](class_float.md#class-float)                                                 | width                                 | `-1.0`  |

## Methods

| [bool](class_bool.md#class-bool)                           | add_object(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0)                                           |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                           | add_string(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null)                                                                                          |
|                                                            | clear()                                                                                                                                                                                                                                                                                                                                                 |
|                                                            | clear_dropcap()                                                                                                                                                                                                                                                                                                                                 |
|                                                            | draw(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                                  |
|                                                            | draw_dropcap(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                                                                                     |
|                                                            | draw_dropcap_outline(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                    |
|                                                            | draw_line(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), line: [int](class_int.md#class-int), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                                                      |
|                                                            | draw_line_outline(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), line: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                     |
|                                                            | draw_outline(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) |
| TextParagraph                      | duplicate()                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                              | get_dropcap_lines()                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                              | get_dropcap_rid()                                                                                                                                                                                                                                                                                                                             |
| [Vector2](class_vector2.md#class-vector2)                  | get_dropcap_size()                                                                                                                                                                                                                                                                                                                           |
| [Direction](class_textserver.md#enum-textserver-direction) | get_inferred_direction()                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                        | get_line_ascent(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                              | get_line_count()                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                        | get_line_descent(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                        |
| [Rect2](class_rect2.md#class-rect2)                        | get_line_object_rect(line: [int](class_int.md#class-int), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                |
| [Array](class_array.md#class-array)                        | get_line_objects(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                        |
| [Vector2i](class_vector2i.md#class-vector2i)               | get_line_range(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                            |
| [RID](class_rid.md#class-rid)                              | get_line_rid(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                  | get_line_size(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                              |
| [float](class_float.md#class-float)                        | get_line_underline_position(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                  |
| [float](class_float.md#class-float)                        | get_line_underline_thickness(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                |
| [float](class_float.md#class-float)                        | get_line_width(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                            |
| [Vector2](class_vector2.md#class-vector2)                  | get_non_wrapped_size()                                                                                                                                                                                                                                                                                                                   |
| [Vector2i](class_vector2i.md#class-vector2i)               | get_range()                                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                              | get_rid()                                                                                                                                                                                                                                                                                                                                             |
| [Vector2](class_vector2.md#class-vector2)                  | get_size()                                                                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                           | has_object(key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                              | hit_test(coords: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                           | resize_object(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0)                                                                                |
|                                                            | set_bidi_override(override: [Array](class_array.md#class-array))                                                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                           | set_dropcap(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), dropcap_margins: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), language: [String](class_string.md#class-string) = "")                                                                      |
|                                                            | tab_align(tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))                                                                                                                                                                                                                                                    |

---

## Property Descriptions

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **alignment** = `0`

-  **set_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_alignment**()

Paragraph horizontal alignment.

---

[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **break_flags** = `3`

-  **set_break_flags**(value: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])
- [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **get_break_flags**()

Line breaking rules. For more info see [TextServer](class_textserver.md#class-textserver).

---

[String](class_string.md#class-string) **custom_punctuation** = `""`

-  **set_custom_punctuation**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_custom_punctuation**()

Custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

[Direction](class_textserver.md#enum-textserver-direction) **direction** = `0`

-  **set_direction**(value: [Direction](class_textserver.md#enum-textserver-direction))
- [Direction](class_textserver.md#enum-textserver-direction) **get_direction**()

Text writing direction.

---

[String](class_string.md#class-string) **ellipsis_char** = `"…"`

-  **set_ellipsis_char**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_ellipsis_char**()

Ellipsis character used for text clipping.

---

[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **justification_flags** = `163`

-  **set_justification_flags**(value: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_justification_flags**()

Line fill alignment rules.

---

[float](class_float.md#class-float) **line_spacing** = `0.0`

-  **set_line_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

[int](class_int.md#class-int) **max_lines_visible** = `-1`

-  **set_max_lines_visible**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_lines_visible**()

Limits the lines of text shown.

---

[Orientation](class_textserver.md#enum-textserver-orientation) **orientation** = `0`

-  **set_orientation**(value: [Orientation](class_textserver.md#enum-textserver-orientation))
- [Orientation](class_textserver.md#enum-textserver-orientation) **get_orientation**()

Text orientation.

---

[bool](class_bool.md#class-bool) **preserve_control** = `false`

-  **set_preserve_control**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_preserve_control**()

If set to `true` text will display control characters.

---

[bool](class_bool.md#class-bool) **preserve_invalid** = `true`

-  **set_preserve_invalid**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_preserve_invalid**()

If set to `true` text will display invalid characters.

---

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **text_overrun_behavior** = `0`

-  **set_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the paragraph's set width.

---

[float](class_float.md#class-float) **width** = `-1.0`

-  **set_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_width**()

Paragraph width.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **add_object**(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---

[bool](class_bool.md#class-bool) **add_string**(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null)

Adds text span and font to draw it.

---

 **clear**()

Clears text paragraph (removes text and inline objects).

---

 **clear_dropcap**()

Removes dropcap.

---

 **draw**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

 **draw_dropcap**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

 **draw_dropcap_outline**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw drop cap outline into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

 **draw_line**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), line: [int](class_int.md#class-int), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

 **draw_line_outline**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), line: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw outline of the single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

 **draw_outline**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), dc_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw outlines of all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

TextParagraph **duplicate**()

Duplicates this **TextParagraph**.

---

[int](class_int.md#class-int) **get_dropcap_lines**()

Returns number of lines used by dropcap.

---

[RID](class_rid.md#class-rid) **get_dropcap_rid**()

Returns drop cap text buffer RID.

---

[Vector2](class_vector2.md#class-vector2) **get_dropcap_size**()

Returns drop cap bounding box size.

---

[Direction](class_textserver.md#enum-textserver-direction) **get_inferred_direction**()

Returns the text writing direction inferred by the BiDi algorithm.

---

[float](class_float.md#class-float) **get_line_ascent**(line: [int](class_int.md#class-int))

Returns the text line ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---

[int](class_int.md#class-int) **get_line_count**()

Returns number of lines in the paragraph.

---

[float](class_float.md#class-float) **get_line_descent**(line: [int](class_int.md#class-int))

Returns the text line descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---

[Rect2](class_rect2.md#class-rect2) **get_line_object_rect**(line: [int](class_int.md#class-int), key: [Variant](class_variant.md#class-variant))

Returns bounding rectangle of the inline object.

---

[Array](class_array.md#class-array) **get_line_objects**(line: [int](class_int.md#class-int))

Returns array of inline objects in the line.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_line_range**(line: [int](class_int.md#class-int))

Returns character range of the line.

---

[RID](class_rid.md#class-rid) **get_line_rid**(line: [int](class_int.md#class-int))

Returns TextServer line buffer RID.

---

[Vector2](class_vector2.md#class-vector2) **get_line_size**(line: [int](class_int.md#class-int))

Returns size of the bounding box of the line of text. Returned size is rounded up.

---

[float](class_float.md#class-float) **get_line_underline_position**(line: [int](class_int.md#class-int))

Returns pixel offset of the underline below the baseline.

---

[float](class_float.md#class-float) **get_line_underline_thickness**(line: [int](class_int.md#class-int))

Returns thickness of the underline.

---

[float](class_float.md#class-float) **get_line_width**(line: [int](class_int.md#class-int))

Returns width (for horizontal layout) or height (for vertical) of the line of text.

---

[Vector2](class_vector2.md#class-vector2) **get_non_wrapped_size**()

Returns the size of the bounding box of the paragraph, without line breaks.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_range**()

Returns the character range of the paragraph.

---

[RID](class_rid.md#class-rid) **get_rid**()

Returns TextServer full string buffer RID.

---

[Vector2](class_vector2.md#class-vector2) **get_size**()

Returns the size of the bounding box of the paragraph.

---

[bool](class_bool.md#class-bool) **has_object**(key: [Variant](class_variant.md#class-variant))

Returns `true` if an object with `key` is embedded in this shaped text buffer.

---

[int](class_int.md#class-int) **hit_test**(coords: [Vector2](class_vector2.md#class-vector2))

Returns caret character offset at the specified coordinates. This function always returns a valid position.

---

[bool](class_bool.md#class-bool) **resize_object**(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0)

Sets new size and alignment of embedded object.

---

 **set_bidi_override**(override: [Array](class_array.md#class-array))

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

---

[bool](class_bool.md#class-bool) **set_dropcap**(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), dropcap_margins: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), language: [String](class_string.md#class-string) = "")

Sets drop cap, overrides previously set drop cap. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.

---

 **tab_align**(tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Aligns paragraph to the given tab-stops.
