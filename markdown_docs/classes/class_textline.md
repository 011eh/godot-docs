# TextLine

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds a line of text.

## Description

Abstraction over [TextServer](class_textserver.md#class-textserver) for handling a single line of text.

## Properties

| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)   | alignment                         | `0`     |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------|---------|
| [Direction](class_textserver.md#enum-textserver-direction)                          | direction                         | `0`     |
| [String](class_string.md#class-string)                                              | ellipsis_char                 | `"…"`   |
| [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)]        | flags                                 | `3`     |
| [Orientation](class_textserver.md#enum-textserver-orientation)                      | orientation                     | `0`     |
| [bool](class_bool.md#class-bool)                                                    | preserve_control           | `false` |
| [bool](class_bool.md#class-bool)                                                    | preserve_invalid           | `true`  |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior)              | text_overrun_behavior | `3`     |
| [float](class_float.md#class-float)                                                 | width                                 | `-1.0`  |

## Methods

| [bool](class_bool.md#class-bool)                           | add_object(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0)   |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                           | add_string(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null)                                                  |
|                                                            | clear()                                                                                                                                                                                                                                                                                                         |
|                                                            | draw(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                                                             |
|                                                            | draw_outline(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                            |
| TextLine                                | duplicate()                                                                                                                                                                                                                                                                                                 |
| [Direction](class_textserver.md#enum-textserver-direction) | get_inferred_direction()                                                                                                                                                                                                                                                                       |
| [float](class_float.md#class-float)                        | get_line_ascent()                                                                                                                                                                                                                                                                                     |
| [float](class_float.md#class-float)                        | get_line_descent()                                                                                                                                                                                                                                                                                   |
| [float](class_float.md#class-float)                        | get_line_underline_position()                                                                                                                                                                                                                                                             |
| [float](class_float.md#class-float)                        | get_line_underline_thickness()                                                                                                                                                                                                                                                           |
| [float](class_float.md#class-float)                        | get_line_width()                                                                                                                                                                                                                                                                                       |
| [Rect2](class_rect2.md#class-rect2)                        | get_object_rect(key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                       |
| [Array](class_array.md#class-array)                        | get_objects()                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                              | get_rid()                                                                                                                                                                                                                                                                                                     |
| [Vector2](class_vector2.md#class-vector2)                  | get_size()                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                           | has_object(key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                              | hit_test(coords: [float](class_float.md#class-float))                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                           | resize_object(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0)                                        |
|                                                            | set_bidi_override(override: [Array](class_array.md#class-array))                                                                                                                                                                                                                                    |
|                                                            | tab_align(tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))                                                                                                                                                                                                            |

---

## Property Descriptions

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **alignment** = `0`

-  **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

Sets text alignment within the line as if the line was horizontal.

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

[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **flags** = `3`

-  **set_flags**(value: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_flags**()

Line alignment rules. For more info see [TextServer](class_textserver.md#class-textserver).

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

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **text_overrun_behavior** = `3`

-  **set_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the text line's set width.

---

[float](class_float.md#class-float) **width** = `-1.0`

-  **set_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_width**()

Text line width.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **add_object**(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---

[bool](class_bool.md#class-bool) **add_string**(text: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int), language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null)

Adds text span and font to draw it.

---

 **clear**()

Clears text line (removes text and inline objects).

---

 **draw**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

 **draw_outline**(canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

TextLine **duplicate**()

Duplicates this **TextLine**.

---

[Direction](class_textserver.md#enum-textserver-direction) **get_inferred_direction**()

Returns the text writing direction inferred by the BiDi algorithm.

---

[float](class_float.md#class-float) **get_line_ascent**()

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---

[float](class_float.md#class-float) **get_line_descent**()

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---

[float](class_float.md#class-float) **get_line_underline_position**()

Returns pixel offset of the underline below the baseline.

---

[float](class_float.md#class-float) **get_line_underline_thickness**()

Returns thickness of the underline.

---

[float](class_float.md#class-float) **get_line_width**()

Returns width (for horizontal layout) or height (for vertical) of the text.

---

[Rect2](class_rect2.md#class-rect2) **get_object_rect**(key: [Variant](class_variant.md#class-variant))

Returns bounding rectangle of the inline object.

---

[Array](class_array.md#class-array) **get_objects**()

Returns array of inline objects.

---

[RID](class_rid.md#class-rid) **get_rid**()

Returns TextServer buffer RID.

---

[Vector2](class_vector2.md#class-vector2) **get_size**()

Returns size of the bounding box of the text.

---

[bool](class_bool.md#class-bool) **has_object**(key: [Variant](class_variant.md#class-variant))

Returns `true` if an object with `key` is embedded in this line.

---

[int](class_int.md#class-int) **hit_test**(coords: [float](class_float.md#class-float))

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

---

[bool](class_bool.md#class-bool) **resize_object**(key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0)

Sets new size and alignment of embedded object.

---

 **set_bidi_override**(override: [Array](class_array.md#class-array))

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

---

 **tab_align**(tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Aligns text to the given tab-stops.
