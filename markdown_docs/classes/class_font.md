# Font

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [FontFile](class_fontfile.md#class-fontfile), [FontVariation](class_fontvariation.md#class-fontvariation), [SystemFont](class_systemfont.md#class-systemfont)

Abstract base class for fonts and font variations.

## Description

Abstract base class for different font types. It has methods for drawing text and font character introspection.

## Properties

| [Array](class_array.md#class-array)[Font]   | fallbacks   | `[]`   |
|------------------------------------------------------------|-----------------------------------------------|--------|

## Methods

| [float](class_float.md#class-float)                                  | draw_char(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float)                                  | draw_char_outline(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int), size: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                      | draw_multiline_string(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0)                                                          |
|                                                                      | draw_multiline_string_outline(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0) |
|                                                                      | draw_string(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0)                                                                                                                                                                                                                  |
|                                                                      | draw_string_outline(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0)                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                        | find_variation(variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary), face_index: [int](class_int.md#class-int) = 0, strength: [float](class_float.md#class-float) = 0.0, transform: [Transform2D](class_transform2d.md#class-transform2d) = Transform2D(1, 0, 0, 1, 0, 0), spacing_top: [int](class_int.md#class-int) = 0, spacing_bottom: [int](class_int.md#class-int) = 0, spacing_space: [int](class_int.md#class-int) = 0, spacing_glyph: [int](class_int.md#class-int) = 0, baseline_offset: [float](class_float.md#class-float) = 0.0, palette_index: [int](class_int.md#class-int) = 0, custom_colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) = PackedColorArray())                                                                                                                                                                                                                                       |
| [float](class_float.md#class-float)                                  | get_ascent(font_size: [int](class_int.md#class-int) = 16)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                            | get_char_size(char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [float](class_float.md#class-float)                                  | get_descent(font_size: [int](class_int.md#class-int) = 16)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                        | get_face_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)                               | get_font_name()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                        | get_font_stretch()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [[FontStyle](class_textserver.md#enum-textserver-fontstyle)]         | get_font_style()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)                               | get_font_style_name()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                        | get_font_weight()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [float](class_float.md#class-float)                                  | get_height(font_size: [int](class_int.md#class-int) = 16)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                            | get_multiline_string_size(text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, brk_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0)                                                                                                                                                                                                                                                                          |
| [Dictionary](class_dictionary.md#class-dictionary)                   | get_opentype_features()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Dictionary](class_dictionary.md#class-dictionary)                   | get_ot_name_strings()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) | get_palette_colors(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                        | get_palette_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [String](class_string.md#class-string)                               | get_palette_name(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]   | get_rids()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                        | get_spacing(spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Vector2](class_vector2.md#class-vector2)                            | get_string_size(text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [String](class_string.md#class-string)                               | get_supported_chars()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Dictionary](class_dictionary.md#class-dictionary)                   | get_supported_feature_list()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dictionary](class_dictionary.md#class-dictionary)                   | get_supported_variation_list()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [float](class_float.md#class-float)                                  | get_underline_position(font_size: [int](class_int.md#class-int) = 16)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                  | get_underline_thickness(font_size: [int](class_int.md#class-int) = 16)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                     | has_char(char: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                     | is_language_supported(language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                     | is_script_supported(script: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                      | set_cache_capacity(single_line: [int](class_int.md#class-int), multi_line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

---

## Property Descriptions

[Array](class_array.md#class-array)[Font] **fallbacks** = `[]`

-  **set_fallbacks**(value: [Array](class_array.md#class-array)[Font])
- [Array](class_array.md#class-array)[Font] **get_fallbacks**()

Array of fallback **Font**s to use as a substitute if a glyph is not found in this current **Font**.

If this array is empty in a [FontVariation](class_fontvariation.md#class-fontvariation), the [FontVariation.base_font](class_fontvariation.md#class-fontvariation-property-base-font)'s fallbacks are used instead.

---

## Method Descriptions

[float](class_float.md#class-float) **draw_char**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw a single Unicode character `char` into a canvas item using the font, at a given position, with `modulate` color. `pos` specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Note:** Do not use this function to draw strings character by character, use draw_string() or [TextLine](class_textline.md#class-textline) instead.

---

[float](class_float.md#class-float) **draw_char_outline**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int), size: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw a single Unicode character `char` outline into a canvas item using the font, at a given position, with `modulate` color and `size` outline size. `pos` specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Note:** Do not use this function to draw strings character by character, use draw_string() or [TextLine](class_textline.md#class-textline) instead.

---

 **draw_multiline_string**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0)

Breaks `text` into lines using rules specified by `brk_flags` and draws it into a canvas item using the font, at a given position, with `modulate` color, optionally clipping the width and aligning horizontally. `pos` specifies the baseline of the first line, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

See also [CanvasItem.draw_multiline_string()](class_canvasitem.md#class-canvasitem-method-draw-multiline-string).

---

 **draw_multiline_string_outline**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), brk_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0)

Breaks `text` to the lines using rules specified by `brk_flags` and draws text outline into a canvas item using the font, at a given position, with `modulate` color and `size` outline size, optionally clipping the width and aligning horizontally. `pos` specifies the baseline of the first line, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

See also [CanvasItem.draw_multiline_string_outline()](class_canvasitem.md#class-canvasitem-method-draw-multiline-string-outline).

---

 **draw_string**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0)

Draw `text` into a canvas item using the font, at a given position, with `modulate` color, optionally clipping the width and aligning horizontally. `pos` specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

See also [CanvasItem.draw_string()](class_canvasitem.md#class-canvasitem-method-draw-string).

---

 **draw_string_outline**(canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, size: [int](class_int.md#class-int) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0, oversampling: [float](class_float.md#class-float) = 0.0)

Draw `text` outline into a canvas item using the font, at a given position, with `modulate` color and `size` outline size, optionally clipping the width and aligning horizontally. `pos` specifies the baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

See also [CanvasItem.draw_string_outline()](class_canvasitem.md#class-canvasitem-method-draw-string-outline).

---

[RID](class_rid.md#class-rid) **find_variation**(variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary), face_index: [int](class_int.md#class-int) = 0, strength: [float](class_float.md#class-float) = 0.0, transform: [Transform2D](class_transform2d.md#class-transform2d) = Transform2D(1, 0, 0, 1, 0, 0), spacing_top: [int](class_int.md#class-int) = 0, spacing_bottom: [int](class_int.md#class-int) = 0, spacing_space: [int](class_int.md#class-int) = 0, spacing_glyph: [int](class_int.md#class-int) = 0, baseline_offset: [float](class_float.md#class-float) = 0.0, palette_index: [int](class_int.md#class-int) = 0, custom_colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) = PackedColorArray())

Returns [TextServer](class_textserver.md#class-textserver) RID of the font cache for specific variation.

---

[float](class_float.md#class-float) **get_ascent**(font_size: [int](class_int.md#class-int) = 16)

Returns the maximum font ascent (number of pixels above the baseline) of this font and all fallback fonts.

**Note:** Real ascent of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate (e.g. as the ascent of empty line).

---

[Vector2](class_vector2.md#class-vector2) **get_char_size**(char: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int))

Returns the size of a character. Does not take kerning into account.

**Note:** Do not use this function to calculate width of the string character by character, use get_string_size() or [TextLine](class_textline.md#class-textline) instead. The height returned is the font height (see also get_height()) and has no relation to the glyph height.

---

[float](class_float.md#class-float) **get_descent**(font_size: [int](class_int.md#class-int) = 16)

Returns the maximum font descent (number of pixels below the baseline) of this font and all fallback fonts.

**Note:** Real descent of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate (e.g. as the descent of empty line).

---

[int](class_int.md#class-int) **get_face_count**()

Returns number of faces in the TrueType / OpenType collection.

---

[String](class_string.md#class-string) **get_font_name**()

Returns font family name.

---

[int](class_int.md#class-int) **get_font_stretch**()

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] **get_font_style**()

Returns font style flags.

---

[String](class_string.md#class-string) **get_font_style_name**()

Returns font style name.

---

[int](class_int.md#class-int) **get_font_weight**()

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

[float](class_float.md#class-float) **get_height**(font_size: [int](class_int.md#class-int) = 16)

Returns the total average font height (ascent plus descent) in pixels.

**Note:** Real height of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate (e.g. as the height of empty line).

---

[Vector2](class_vector2.md#class-vector2) **get_multiline_string_size**(text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, max_lines: [int](class_int.md#class-int) = -1, brk_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] = 3, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0)

Returns the size of a bounding box of a string broken into the lines, taking kerning and advance into account.

See also draw_multiline_string().

---

[Dictionary](class_dictionary.md#class-dictionary) **get_opentype_features**()

Returns a set of OpenType feature tags. More info: [OpenType feature tags](https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags).

---

[Dictionary](class_dictionary.md#class-dictionary) **get_ot_name_strings**()

Returns [Dictionary](class_dictionary.md#class-dictionary) with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_palette_colors**(index: [int](class_int.md#class-int))

Returns the array in the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors. Colors can be overridden using [FontVariation](class_fontvariation.md#class-fontvariation).

---

[int](class_int.md#class-int) **get_palette_count**()

Returns the number of predefined color palettes. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---

[String](class_string.md#class-string) **get_palette_name**(index: [int](class_int.md#class-int))

Returns the name of the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_rids**()

Returns [Array](class_array.md#class-array) of valid **Font** [RID](class_rid.md#class-rid)s, which can be passed to the [TextServer](class_textserver.md#class-textserver) methods.

---

[int](class_int.md#class-int) **get_spacing**(spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype))

Returns the amount of spacing for the given `spacing` type.

---

[Vector2](class_vector2.md#class-vector2) **get_string_size**(text: [String](class_string.md#class-string), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 0, width: [float](class_float.md#class-float) = -1, font_size: [int](class_int.md#class-int) = 16, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 3, direction: [Direction](class_textserver.md#enum-textserver-direction) = 0, orientation: [Orientation](class_textserver.md#enum-textserver-orientation) = 0)

Returns the size of a bounding box of a single-line string, taking kerning, advance and subpixel positioning into account. See also get_multiline_string_size() and draw_string().

For example, to get the string size as displayed by a single-line Label, use:

GDScript

```gdscript
var string_size = $Label.get_theme_font("font").get_string_size($Label.text, HORIZONTAL_ALIGNMENT_LEFT, -1, $Label.get_theme_font_size("font_size"))
```

C#

```csharp
Label label = GetNode<Label>("Label");
Vector2 stringSize = label.GetThemeFont("font").GetStringSize(label.Text, HorizontalAlignment.Left, -1, label.GetThemeFontSize("font_size"));
```

**Note:** Since kerning, advance and subpixel positioning are taken into account by get_string_size(), using separate get_string_size() calls on substrings of a string then adding the results together will return a different result compared to using a single get_string_size() call on the full string.

**Note:** Real height of the string is context-dependent and can be significantly different from the value returned by get_height().

---

[String](class_string.md#class-string) **get_supported_chars**()

Returns a string containing all the characters available in the font.

If a given character is included in more than one font data source, it appears only once in the returned string.

---

[Dictionary](class_dictionary.md#class-dictionary) **get_supported_feature_list**()

Returns list of OpenType features supported by font.

---

[Dictionary](class_dictionary.md#class-dictionary) **get_supported_variation_list**()

Returns list of supported [variation coordinates](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg), each coordinate is returned as `tag: Vector3i(min_value,max_value,default_value)`.

Font variations allow for continuous change of glyph characteristics along some given design axis, such as weight, width or slant.

To print available variation axes of a variable font:

```gdscript
var fv = FontVariation.new()
fv.base_font = load("res://RobotoFlex.ttf")
var variation_list = fv.get_supported_variation_list()
for tag in variation_list:
    var name = TextServerManager.get_primary_interface().tag_to_name(tag)
    var values = variation_list[tag]
    print("variation axis: %s (%d)\n\tmin, max, default: %s" % [name, tag, values])
```

**Note:** To set and get variation coordinates of a [FontVariation](class_fontvariation.md#class-fontvariation), use [FontVariation.variation_opentype](class_fontvariation.md#class-fontvariation-property-variation-opentype).

---

[float](class_float.md#class-float) **get_underline_position**(font_size: [int](class_int.md#class-int) = 16)

Returns average pixel offset of the underline below the baseline.

**Note:** Real underline position of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate.

---

[float](class_float.md#class-float) **get_underline_thickness**(font_size: [int](class_int.md#class-int) = 16)

Returns average thickness of the underline.

**Note:** Real underline thickness of the string is context-dependent and can be significantly different from the value returned by this function. Use it only as rough estimate.

---

[bool](class_bool.md#class-bool) **has_char**(char: [int](class_int.md#class-int))

Returns `true` if a Unicode `char` is available in the font.

---

[bool](class_bool.md#class-bool) **is_language_supported**(language: [String](class_string.md#class-string))

Returns `true` if the font supports the given language (as a [ISO 639](https://en.wikipedia.org/wiki/ISO_639-1) code).

---

[bool](class_bool.md#class-bool) **is_script_supported**(script: [String](class_string.md#class-string))

Returns `true` if the font supports the given script (as a [ISO 15924](https://en.wikipedia.org/wiki/ISO_15924) code).

---

 **set_cache_capacity**(single_line: [int](class_int.md#class-int), multi_line: [int](class_int.md#class-int))

Sets LRU cache capacity for `draw_*` methods.
