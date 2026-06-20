# TextServer

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [TextServerExtension](class_textserverextension.md#class-textserverextension)

A server interface for font management and text rendering.

## Description

**TextServer** is the API backend for managing fonts and rendering text.

**Note:** This is a low-level API, consider using [TextLine](class_textline.md#class-textline), [TextParagraph](class_textparagraph.md#class-textparagraph), and [Font](class_font.md#class-font) classes instead.

This is an abstract class, so to get the currently active **TextServer** instance, use the following code:

GDScript

```gdscript
var ts = TextServerManager.get_primary_interface()
```

C#

```csharp
var ts = TextServerManager.GetPrimaryInterface();
```

## Methods

| [RID](class_rid.md#class-rid)                                                           | create_font()                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)                                                           | create_font_linked_variation(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                            |
| [RID](class_rid.md#class-rid)                                                           | create_shaped_text(direction: Direction = 0, orientation: Orientation = 0)                                                                                                                                                                                                                                                                                                   |
|                                                                                         | draw_hex_code_box(canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                                                                             |
|                                                                                         | font_clear_glyphs(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | font_clear_kerning_map(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | font_clear_size_cache(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | font_clear_system_fallback_cache()                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | font_clear_textures(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | font_draw_glyph(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                                                           |
|                                                                                         | font_draw_glyph_outline(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                              |
| FontAntialiasing                                   | font_get_antialiasing(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                          |
| [float](class_float.md#class-float)                                                     | font_get_ascent(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                     | font_get_baseline_offset(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                                           | font_get_char_from_glyph_index(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                       |
| [float](class_float.md#class-float)                                                     | font_get_descent(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | font_get_disable_embedded_bitmaps(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                  |
| [float](class_float.md#class-float)                                                     | font_get_embolden(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | font_get_face_count(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | font_get_face_index(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | font_get_fixed_size(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| FixedSizeScaleMode                               | font_get_fixed_size_scale_mode(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | font_get_generate_mipmaps(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                  |
| [float](class_float.md#class-float)                                                     | font_get_global_oversampling()                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Vector2](class_vector2.md#class-vector2)                                               | font_get_glyph_advance(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                             |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | font_get_glyph_contours(font: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                           | font_get_glyph_index(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int))                                                                                                                                                                                                                                               |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | font_get_glyph_list(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                          |
| [Vector2](class_vector2.md#class-vector2)                                               | font_get_glyph_offset(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                                               | font_get_glyph_size(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                                           | font_get_glyph_texture_idx(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                           | font_get_glyph_texture_rid(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                      |
| [Vector2](class_vector2.md#class-vector2)                                               | font_get_glyph_texture_size(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                    |
| [Rect2](class_rect2.md#class-rect2)                                                     | font_get_glyph_uv_rect(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                              |
| Hinting                                                     | font_get_hinting(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | font_get_keep_rounding_remainders(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                  |
| [Vector2](class_vector2.md#class-vector2)                                               | font_get_kerning(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                     |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)]       | font_get_kerning_list(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | font_get_language_support_override(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                              |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | font_get_language_support_overrides(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | font_get_msdf_pixel_range(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | font_get_msdf_size(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                |
| [String](class_string.md#class-string)                                                  | font_get_name(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                          |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | font_get_opentype_feature_overrides(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                              |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | font_get_ot_name_strings(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                    |
| [float](class_float.md#class-float)                                                     | font_get_oversampling(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                          |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)                    | font_get_palette_colors(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                           | font_get_palette_count(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                        |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)                    | font_get_palette_custom_colors(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | font_get_palette_name(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                    |
| [float](class_float.md#class-float)                                                     | font_get_scale(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | font_get_script_support_override(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                    |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | font_get_script_support_overrides(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                  |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | font_get_size_cache_info(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                    |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)]       | font_get_size_cache_list(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                                           | font_get_spacing(font_rid: [RID](class_rid.md#class-rid), spacing: SpacingType)                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | font_get_stretch(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                    |
| [FontStyle]                                               | font_get_style(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | font_get_style_name(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| SubpixelPositioning                             | font_get_subpixel_positioning(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                          |
| [String](class_string.md#class-string)                                                  | font_get_supported_chars(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                    |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | font_get_supported_glyphs(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | font_get_texture_count(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                    |
| [Image](class_image.md#class-image)                                                     | font_get_texture_image(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                      |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | font_get_texture_offsets(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                  |
| [Transform2D](class_transform2d.md#class-transform2d)                                   | font_get_transform(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                |
| [float](class_float.md#class-float)                                                     | font_get_underline_position(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                         |
| [float](class_float.md#class-float)                                                     | font_get_underline_thickness(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                           | font_get_used_palette(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                          |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | font_get_variation_coordinates(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | font_get_weight(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | font_has_char(font_rid: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | font_is_allow_system_fallback(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | font_is_force_autohinter(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | font_is_language_supported(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | font_is_modulate_color_glyphs(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | font_is_multichannel_signed_distance_field(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                        | font_is_script_supported(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | font_remove_glyph(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                        |
|                                                                                         | font_remove_kerning(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                               |
|                                                                                         | font_remove_language_support_override(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                        |
|                                                                                         | font_remove_script_support_override(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                              |
|                                                                                         | font_remove_size_cache(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | font_remove_texture(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                            |
|                                                                                         | font_render_glyph(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                        |
|                                                                                         | font_render_range(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))                                                                                                                                                                                                                                                    |
|                                                                                         | font_set_allow_system_fallback(font_rid: [RID](class_rid.md#class-rid), allow_system_fallback: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                               |
|                                                                                         | font_set_antialiasing(font_rid: [RID](class_rid.md#class-rid), antialiasing: FontAntialiasing)                                                                                                                                                                                                                                                                                                     |
|                                                                                         | font_set_ascent(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                    |
|                                                                                         | font_set_baseline_offset(font_rid: [RID](class_rid.md#class-rid), baseline_offset: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                              |
|                                                                                         | font_set_data(font_rid: [RID](class_rid.md#class-rid), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | font_set_descent(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                 |
|                                                                                         | font_set_disable_embedded_bitmaps(font_rid: [RID](class_rid.md#class-rid), disable_embedded_bitmaps: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                      |
|                                                                                         | font_set_embolden(font_rid: [RID](class_rid.md#class-rid), strength: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | font_set_face_index(font_rid: [RID](class_rid.md#class-rid), face_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | font_set_fixed_size(font_rid: [RID](class_rid.md#class-rid), fixed_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | font_set_fixed_size_scale_mode(font_rid: [RID](class_rid.md#class-rid), fixed_size_scale_mode: FixedSizeScaleMode)                                                                                                                                                                                                                                                                      |
|                                                                                         | font_set_force_autohinter(font_rid: [RID](class_rid.md#class-rid), force_autohinter: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                              |
|                                                                                         | font_set_generate_mipmaps(font_rid: [RID](class_rid.md#class-rid), generate_mipmaps: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                              |
|                                                                                         | font_set_global_oversampling(oversampling: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | font_set_glyph_advance(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                         |
|                                                                                         | font_set_glyph_offset(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                             |
|                                                                                         | font_set_glyph_size(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                |
|                                                                                         | font_set_glyph_texture_idx(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                          |
|                                                                                         | font_set_glyph_uv_rect(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                                |
|                                                                                         | font_set_hinting(font_rid: [RID](class_rid.md#class-rid), hinting: Hinting)                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | font_set_keep_rounding_remainders(font_rid: [RID](class_rid.md#class-rid), keep_rounding_remainders: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                      |
|                                                                                         | font_set_kerning(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                 |
|                                                                                         | font_set_language_support_override(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                 |
|                                                                                         | font_set_modulate_color_glyphs(font_rid: [RID](class_rid.md#class-rid), modulate: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                            |
|                                                                                         | font_set_msdf_pixel_range(font_rid: [RID](class_rid.md#class-rid), msdf_pixel_range: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | font_set_msdf_size(font_rid: [RID](class_rid.md#class-rid), msdf_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | font_set_multichannel_signed_distance_field(font_rid: [RID](class_rid.md#class-rid), msdf: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                      |
|                                                                                         | font_set_name(font_rid: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | font_set_opentype_feature_overrides(font_rid: [RID](class_rid.md#class-rid), overrides: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                                                                                                                                                                               |
|                                                                                         | font_set_oversampling(font_rid: [RID](class_rid.md#class-rid), oversampling: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | font_set_palette_custom_colors(font_rid: [RID](class_rid.md#class-rid), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))                                                                                                                                                                                                                                                                          |
|                                                                                         | font_set_scale(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                       |
|                                                                                         | font_set_script_support_override(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                       |
|                                                                                         | font_set_spacing(font_rid: [RID](class_rid.md#class-rid), spacing: SpacingType, value: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                        |
|                                                                                         | font_set_stretch(font_rid: [RID](class_rid.md#class-rid), weight: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | font_set_style(font_rid: [RID](class_rid.md#class-rid), style: [FontStyle])                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | font_set_style_name(font_rid: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | font_set_subpixel_positioning(font_rid: [RID](class_rid.md#class-rid), subpixel_positioning: SubpixelPositioning)                                                                                                                                                                                                                                                                       |
|                                                                                         | font_set_texture_image(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image))                                                                                                                                                                                                                          |
|                                                                                         | font_set_texture_offsets(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array))                                                                                                                                                                                    |
|                                                                                         | font_set_transform(font_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                              |
|                                                                                         | font_set_underline_position(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                |
|                                                                                         | font_set_underline_thickness(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float))                                                                                                                                                                                                                                                             |
|                                                                                         | font_set_used_palette(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | font_set_variation_coordinates(font_rid: [RID](class_rid.md#class-rid), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                                                                                                                                                                             |
|                                                                                         | font_set_weight(font_rid: [RID](class_rid.md#class-rid), weight: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                               |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | font_supported_feature_list(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                              |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | font_supported_variation_list(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                          |
| [String](class_string.md#class-string)                                                  | format_number(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | free_rid(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                           | get_features()                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Vector2](class_vector2.md#class-vector2)                                               | get_hex_code_box_size(size: [int](class_int.md#class-int), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | get_name()                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)                       | get_support_data()                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [String](class_string.md#class-string)                                                  | get_support_data_filename()                                                                                                                                                                                                                                                                                                                                                                                                         |
| [String](class_string.md#class-string)                                                  | get_support_data_info()                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | has(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | has_feature(feature: Feature)                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                           | is_confusable(string: [String](class_string.md#class-string), dict: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | is_locale_right_to_left(locale: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | is_locale_using_support_data(locale: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | is_valid_identifier(string: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | is_valid_letter(unicode: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | load_support_data(filename: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                           | name_to_tag(name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                         |
| [String](class_string.md#class-string)                                                  | parse_number(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                                              |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)]       | parse_structured_text(parser_type: StructuredTextParser, args: [Array](class_array.md#class-array), text: [String](class_string.md#class-string))                                                                                                                                                                                                                                              |
| [String](class_string.md#class-string)                                                  | percent_sign(language: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | save_support_data(filename: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                           | shaped_get_run_count(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| Direction                                                 | shaped_get_run_direction(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)                                                           | shaped_get_run_font_rid(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | shaped_get_run_font_size(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | shaped_get_run_glyph_range(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)                                                  | shaped_get_run_language(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                  |
| [Variant](class_variant.md#class-variant)                                               | shaped_get_run_object(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                      |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | shaped_get_run_range(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | shaped_get_run_text(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                                           | shaped_get_span_count(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                            |
| [Variant](class_variant.md#class-variant)                                               | shaped_get_span_embedded_object(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                  |
| [Variant](class_variant.md#class-variant)                                               | shaped_get_span_meta(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                        |
| [Variant](class_variant.md#class-variant)                                               | shaped_get_span_object(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                    |
| [String](class_string.md#class-string)                                                  | shaped_get_span_text(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | shaped_get_text(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | shaped_set_span_update_font(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary) = {})                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_add_object(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0)                                                                            |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_add_string(shaped: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary) = {}, language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null)                 |
|                                                                                         | shaped_text_clear(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                           | shaped_text_closest_character_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                |
|                                                                                         | shaped_text_draw(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float) = -1, clip_r: [float](class_float.md#class-float) = -1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)                                                                  |
|                                                                                         | shaped_text_draw_outline(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float) = -1, clip_r: [float](class_float.md#class-float) = -1, outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0) |
| [RID](class_rid.md#class-rid)                                                           | shaped_text_duplicate(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                     | shaped_text_fit_to_width(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), justification_flags: [JustificationFlag] = 3)                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)                                                     | shaped_text_get_ascent(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                          |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | shaped_text_get_carets(shaped: [RID](class_rid.md#class-rid), position: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                 |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | shaped_text_get_character_breaks(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                           | shaped_text_get_custom_ellipsis(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | shaped_text_get_custom_punctuation(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                  |
| [float](class_float.md#class-float)                                                     | shaped_text_get_descent(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                        |
| Direction                                                 | shaped_text_get_direction(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                    |
| Direction                                                 | shaped_text_get_dominant_direction_in_range(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                           | shaped_text_get_ellipsis_glyph_count(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                              |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | shaped_text_get_ellipsis_glyphs(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | shaped_text_get_ellipsis_pos(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | shaped_text_get_glyph_count(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | shaped_text_get_glyphs(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                          |
| [Vector2](class_vector2.md#class-vector2)                                               | shaped_text_get_grapheme_bounds(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                    |
| Direction                                                 | shaped_text_get_inferred_direction(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                  |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | shaped_text_get_line_breaks(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), start: [int](class_int.md#class-int) = 0, break_flags: [LineBreakFlag] = 3)                                                                                                                                                                                                      |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | shaped_text_get_line_breaks_adv(shaped: [RID](class_rid.md#class-rid), width: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), start: [int](class_int.md#class-int) = 0, once: [bool](class_bool.md#class-bool) = true, break_flags: [LineBreakFlag] = 3)                                                                                                        |
| [int](class_int.md#class-int)                                                           | shaped_text_get_object_glyph(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                              |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | shaped_text_get_object_range(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                              |
| [Rect2](class_rect2.md#class-rect2)                                                     | shaped_text_get_object_rect(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                |
| [Array](class_array.md#class-array)                                                     | shaped_text_get_objects(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                        |
| Orientation                                             | shaped_text_get_orientation(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)                                                           | shaped_text_get_parent(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_get_preserve_control(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_get_preserve_invalid(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                      |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | shaped_text_get_range(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                            |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)              | shaped_text_get_selection(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                          |
| [Vector2](class_vector2.md#class-vector2)                                               | shaped_text_get_size(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | shaped_text_get_spacing(shaped: [RID](class_rid.md#class-rid), spacing: SpacingType)                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | shaped_text_get_trim_pos(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)                                                     | shaped_text_get_underline_position(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                  |
| [float](class_float.md#class-float)                                                     | shaped_text_get_underline_thickness(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                |
| [float](class_float.md#class-float)                                                     | shaped_text_get_width(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                            |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | shaped_text_get_word_breaks(shaped: [RID](class_rid.md#class-rid), grapheme_flags: [GraphemeFlag] = 264, skip_grapheme_flags: [GraphemeFlag] = 4)                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_has_object(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_has_visible_chars(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                                           | shaped_text_hit_test_grapheme(shaped: [RID](class_rid.md#class-rid), coords: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                           | shaped_text_hit_test_position(shaped: [RID](class_rid.md#class-rid), coords: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_is_ready(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | shaped_text_next_character_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                           | shaped_text_next_grapheme_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | shaped_text_overrun_trim_to_width(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float) = 0, overrun_trim_flags: [TextOverrunFlag] = 0)                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | shaped_text_prev_character_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                           | shaped_text_prev_grapheme_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_resize_object(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0)                                                                                                                 |
|                                                                                         | shaped_text_set_bidi_override(shaped: [RID](class_rid.md#class-rid), override: [Array](class_array.md#class-array))                                                                                                                                                                                                                                                                                                             |
|                                                                                         | shaped_text_set_custom_ellipsis(shaped: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | shaped_text_set_custom_punctuation(shaped: [RID](class_rid.md#class-rid), punct: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                   |
|                                                                                         | shaped_text_set_direction(shaped: [RID](class_rid.md#class-rid), direction: Direction = 0)                                                                                                                                                                                                                                                                                                            |
|                                                                                         | shaped_text_set_orientation(shaped: [RID](class_rid.md#class-rid), orientation: Orientation = 0)                                                                                                                                                                                                                                                                                                  |
|                                                                                         | shaped_text_set_preserve_control(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                           |
|                                                                                         | shaped_text_set_preserve_invalid(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                           |
|                                                                                         | shaped_text_set_spacing(shaped: [RID](class_rid.md#class-rid), spacing: SpacingType, value: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                        | shaped_text_shape(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                    |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | shaped_text_sort_logical(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                           | shaped_text_substr(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), length: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                     |
| [float](class_float.md#class-float)                                                     | shaped_text_tab_align(shaped: [RID](class_rid.md#class-rid), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | spoof_check(string: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                       |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | string_get_character_breaks(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | string_get_word_breaks(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "", chars_per_line: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | string_to_lower(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | string_to_title(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | string_to_upper(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | strip_diacritics(string: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                                                  | tag_to_name(tag: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                   |

---

## Enumerations

enum **FontAntialiasing**:

FontAntialiasing **FONT_ANTIALIASING_NONE** = `0`

Font glyphs are rasterized as 1-bit bitmaps.

FontAntialiasing **FONT_ANTIALIASING_GRAY** = `1`

Font glyphs are rasterized as 8-bit grayscale anti-aliased bitmaps.

FontAntialiasing **FONT_ANTIALIASING_LCD** = `2`

Font glyphs are rasterized for LCD screens.

LCD subpixel layout is determined by the value of the [ProjectSettings.gui/theme/lcd_subpixel_layout](class_projectsettings.md#class-projectsettings-property-gui-theme-lcd-subpixel-layout) setting.

LCD subpixel anti-aliasing mode is suitable only for rendering horizontal, unscaled text in 2D.

---

enum **FontLCDSubpixelLayout**:

FontLCDSubpixelLayout **FONT_LCD_SUBPIXEL_LAYOUT_NONE** = `0`

Unknown or unsupported subpixel layout, LCD subpixel antialiasing is disabled.

FontLCDSubpixelLayout **FONT_LCD_SUBPIXEL_LAYOUT_HRGB** = `1`

Horizontal RGB subpixel layout.

FontLCDSubpixelLayout **FONT_LCD_SUBPIXEL_LAYOUT_HBGR** = `2`

Horizontal BGR subpixel layout.

FontLCDSubpixelLayout **FONT_LCD_SUBPIXEL_LAYOUT_VRGB** = `3`

Vertical RGB subpixel layout.

FontLCDSubpixelLayout **FONT_LCD_SUBPIXEL_LAYOUT_VBGR** = `4`

Vertical BGR subpixel layout.

FontLCDSubpixelLayout **FONT_LCD_SUBPIXEL_LAYOUT_MAX** = `5`

Represents the size of the FontLCDSubpixelLayout enum.

---

enum **Direction**:

Direction **DIRECTION_AUTO** = `0`

Text direction is determined based on contents and current locale.

Direction **DIRECTION_LTR** = `1`

Text is written from left to right.

Direction **DIRECTION_RTL** = `2`

Text is written from right to left.

Direction **DIRECTION_INHERITED** = `3`

Text writing direction is the same as base string writing direction. Used for BiDi override only.

---

enum **Orientation**:

Orientation **ORIENTATION_HORIZONTAL** = `0`

Text is written horizontally.

Orientation **ORIENTATION_VERTICAL** = `1`

Left to right text is written vertically from top to bottom.

Right to left text is written vertically from bottom to top.

---

flags **JustificationFlag**:

JustificationFlag **JUSTIFICATION_NONE** = `0`

Do not justify text.

JustificationFlag **JUSTIFICATION_KASHIDA** = `1`

Justify text by adding and removing kashidas.

JustificationFlag **JUSTIFICATION_WORD_BOUND** = `2`

Justify text by changing width of the spaces between the words.

JustificationFlag **JUSTIFICATION_TRIM_EDGE_SPACES** = `4`

Remove trailing and leading spaces from the justified text.

JustificationFlag **JUSTIFICATION_AFTER_LAST_TAB** = `8`

Only apply justification to the part of the text after the last tab.

JustificationFlag **JUSTIFICATION_CONSTRAIN_ELLIPSIS** = `16`

Apply justification to the trimmed line with ellipsis.

JustificationFlag **JUSTIFICATION_SKIP_LAST_LINE** = `32`

Do not apply justification to the last line of the paragraph.

JustificationFlag **JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS** = `64`

Do not apply justification to the last line of the paragraph with visible characters (takes precedence over JUSTIFICATION_SKIP_LAST_LINE).

JustificationFlag **JUSTIFICATION_DO_NOT_SKIP_SINGLE_LINE** = `128`

Always apply justification to the paragraphs with a single line (JUSTIFICATION_SKIP_LAST_LINE and JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS are ignored).

---

enum **AutowrapMode**:

AutowrapMode **AUTOWRAP_OFF** = `0`

Autowrap is disabled.

AutowrapMode **AUTOWRAP_ARBITRARY** = `1`

Wraps the text inside the node's bounding rectangle by allowing to break lines at arbitrary positions, which is useful when very limited space is available.

AutowrapMode **AUTOWRAP_WORD** = `2`

Wraps the text inside the node's bounding rectangle by soft-breaking between words.

AutowrapMode **AUTOWRAP_WORD_SMART** = `3`

Behaves similarly to AUTOWRAP_WORD, but force-breaks a word if that single word does not fit in one line.

---

flags **LineBreakFlag**:

LineBreakFlag **BREAK_NONE** = `0`

Do not break the line.

LineBreakFlag **BREAK_MANDATORY** = `1`

Break the line at the line mandatory break characters (e.g. `"\n"`).

LineBreakFlag **BREAK_WORD_BOUND** = `2`

Break the line between the words.

LineBreakFlag **BREAK_GRAPHEME_BOUND** = `4`

Break the line between any unconnected graphemes.

LineBreakFlag **BREAK_ADAPTIVE** = `8`

Should be used only in conjunction with BREAK_WORD_BOUND, break the line between any unconnected graphemes, if it's impossible to break it between the words.

LineBreakFlag **BREAK_TRIM_EDGE_SPACES** = `16`

**Deprecated:** Use `BREAK_TRIM_START_EDGE_SPACES | BREAK_TRIM_END_EDGE_SPACES` instead.

Remove edge spaces from the broken line segments.

LineBreakFlag **BREAK_TRIM_INDENT** = `32`

Subtract first line indentation width from all lines after the first one.

LineBreakFlag **BREAK_TRIM_START_EDGE_SPACES** = `64`

Remove spaces and line break characters from the start of broken line segments.

E.g, after line breaking, the second segment of the following text `test  \n  next`, is `next` if the flag is set, and \`\`  next\`\` if it is not.

LineBreakFlag **BREAK_TRIM_END_EDGE_SPACES** = `128`

Remove spaces and line break characters from the end of broken line segments.

E.g, after line breaking, the first segment of the following text `test  \n  next`, is `test` if the flag is set, and `test  \n` if it is not.

---

enum **VisibleCharactersBehavior**:

VisibleCharactersBehavior **VC_CHARS_BEFORE_SHAPING** = `0`

Trims text before the shaping. e.g, increasing [Label.visible_characters](class_label.md#class-label-property-visible-characters) or [RichTextLabel.visible_characters](class_richtextlabel.md#class-richtextlabel-property-visible-characters) value is visually identical to typing the text.

**Note:** In this mode, trimmed text is not processed at all. It is not accounted for in line breaking and size calculations.

VisibleCharactersBehavior **VC_CHARS_AFTER_SHAPING** = `1`

Displays glyphs that are mapped to the first [Label.visible_characters](class_label.md#class-label-property-visible-characters) or [RichTextLabel.visible_characters](class_richtextlabel.md#class-richtextlabel-property-visible-characters) characters from the beginning of the text.

VisibleCharactersBehavior **VC_GLYPHS_AUTO** = `2`

Displays [Label.visible_ratio](class_label.md#class-label-property-visible-ratio) or [RichTextLabel.visible_ratio](class_richtextlabel.md#class-richtextlabel-property-visible-ratio) glyphs, starting from the left or from the right, depending on [Control.layout_direction](class_control.md#class-control-property-layout-direction) value.

VisibleCharactersBehavior **VC_GLYPHS_LTR** = `3`

Displays [Label.visible_ratio](class_label.md#class-label-property-visible-ratio) or [RichTextLabel.visible_ratio](class_richtextlabel.md#class-richtextlabel-property-visible-ratio) glyphs, starting from the left.

VisibleCharactersBehavior **VC_GLYPHS_RTL** = `4`

Displays [Label.visible_ratio](class_label.md#class-label-property-visible-ratio) or [RichTextLabel.visible_ratio](class_richtextlabel.md#class-richtextlabel-property-visible-ratio) glyphs, starting from the right.

---

enum **OverrunBehavior**:

OverrunBehavior **OVERRUN_NO_TRIMMING** = `0`

No text trimming is performed.

OverrunBehavior **OVERRUN_TRIM_CHAR** = `1`

Trims the text per character.

OverrunBehavior **OVERRUN_TRIM_WORD** = `2`

Trims the text per word.

OverrunBehavior **OVERRUN_TRIM_ELLIPSIS** = `3`

Trims the text per character and adds an ellipsis to indicate that parts are hidden if trimmed text is 6 characters or longer.

OverrunBehavior **OVERRUN_TRIM_WORD_ELLIPSIS** = `4`

Trims the text per word and adds an ellipsis to indicate that parts are hidden if trimmed text is 6 characters or longer.

OverrunBehavior **OVERRUN_TRIM_ELLIPSIS_FORCE** = `5`

Trims the text per character and adds an ellipsis to indicate that parts are hidden regardless of trimmed text length.

OverrunBehavior **OVERRUN_TRIM_WORD_ELLIPSIS_FORCE** = `6`

Trims the text per word and adds an ellipsis to indicate that parts are hidden regardless of trimmed text length.

---

flags **TextOverrunFlag**:

TextOverrunFlag **OVERRUN_NO_TRIM** = `0`

No trimming is performed.

TextOverrunFlag **OVERRUN_TRIM** = `1`

Trims the text when it exceeds the given width.

TextOverrunFlag **OVERRUN_TRIM_WORD_ONLY** = `2`

Trims the text per word instead of per grapheme.

TextOverrunFlag **OVERRUN_ADD_ELLIPSIS** = `4`

Determines whether an ellipsis should be added at the end of the text.

TextOverrunFlag **OVERRUN_ENFORCE_ELLIPSIS** = `8`

Determines whether the ellipsis at the end of the text is enforced and may not be hidden.

TextOverrunFlag **OVERRUN_JUSTIFICATION_AWARE** = `16`

Accounts for the text being justified before attempting to trim it (see JustificationFlag).

TextOverrunFlag **OVERRUN_SHORT_STRING_ELLIPSIS** = `32`

Determines whether the ellipsis should be added regardless of the string length, otherwise it is added only if the string is 6 characters or longer.

---

flags **GraphemeFlag**:

GraphemeFlag **GRAPHEME_IS_VALID** = `1`

Grapheme is supported by the font, and can be drawn.

GraphemeFlag **GRAPHEME_IS_RTL** = `2`

Grapheme is part of right-to-left or bottom-to-top run.

GraphemeFlag **GRAPHEME_IS_VIRTUAL** = `4`

Grapheme is not part of source text, it was added by justification process.

GraphemeFlag **GRAPHEME_IS_SPACE** = `8`

Grapheme is whitespace.

GraphemeFlag **GRAPHEME_IS_BREAK_HARD** = `16`

Grapheme is mandatory break point (e.g. `"\n"`).

GraphemeFlag **GRAPHEME_IS_BREAK_SOFT** = `32`

Grapheme is optional break point (e.g. space).

GraphemeFlag **GRAPHEME_IS_TAB** = `64`

Grapheme is the tabulation character.

GraphemeFlag **GRAPHEME_IS_ELONGATION** = `128`

Grapheme is kashida.

GraphemeFlag **GRAPHEME_IS_PUNCTUATION** = `256`

Grapheme is punctuation character.

GraphemeFlag **GRAPHEME_IS_UNDERSCORE** = `512`

Grapheme is underscore character.

GraphemeFlag **GRAPHEME_IS_CONNECTED** = `1024`

Grapheme is connected to the previous grapheme. Breaking line before this grapheme is not safe.

GraphemeFlag **GRAPHEME_IS_SAFE_TO_INSERT_TATWEEL** = `2048`

It is safe to insert a U+0640 before this grapheme for elongation.

GraphemeFlag **GRAPHEME_IS_EMBEDDED_OBJECT** = `4096`

Grapheme is an object replacement character for the embedded object.

GraphemeFlag **GRAPHEME_IS_SOFT_HYPHEN** = `8192`

Grapheme is a soft hyphen.

---

enum **Hinting**:

Hinting **HINTING_NONE** = `0`

Disables font hinting (smoother but less crisp).

Hinting **HINTING_LIGHT** = `1`

Use the light font hinting mode.

Hinting **HINTING_NORMAL** = `2`

Use the default font hinting mode (crisper but less smooth).

**Note:** This hinting mode changes both horizontal and vertical glyph metrics. If applied to monospace font, some glyphs might have different width.

---

enum **SubpixelPositioning**:

SubpixelPositioning **SUBPIXEL_POSITIONING_DISABLED** = `0`

Glyph horizontal position is rounded to the whole pixel size, each glyph is rasterized once.

SubpixelPositioning **SUBPIXEL_POSITIONING_AUTO** = `1`

Glyph horizontal position is rounded based on font size.

- To one quarter of the pixel size if font size is smaller or equal to SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE.
- To one half of the pixel size if font size is smaller or equal to SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE.
- To the whole pixel size for larger fonts.

SubpixelPositioning **SUBPIXEL_POSITIONING_ONE_HALF** = `2`

Glyph horizontal position is rounded to one half of the pixel size, each glyph is rasterized up to two times.

SubpixelPositioning **SUBPIXEL_POSITIONING_ONE_QUARTER** = `3`

Glyph horizontal position is rounded to one quarter of the pixel size, each glyph is rasterized up to four times.

SubpixelPositioning **SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE** = `20`

Maximum font size which will use "one half of the pixel" subpixel positioning in SUBPIXEL_POSITIONING_AUTO mode.

SubpixelPositioning **SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE** = `16`

Maximum font size which will use "one quarter of the pixel" subpixel positioning in SUBPIXEL_POSITIONING_AUTO mode.

---

enum **Feature**:

Feature **FEATURE_SIMPLE_LAYOUT** = `1`

TextServer supports simple text layouts.

Feature **FEATURE_BIDI_LAYOUT** = `2`

TextServer supports bidirectional text layouts.

Feature **FEATURE_VERTICAL_LAYOUT** = `4`

TextServer supports vertical layouts.

Feature **FEATURE_SHAPING** = `8`

TextServer supports complex text shaping.

Feature **FEATURE_KASHIDA_JUSTIFICATION** = `16`

TextServer supports justification using kashidas.

Feature **FEATURE_BREAK_ITERATORS** = `32`

TextServer supports complex line/word breaking rules (e.g. dictionary based).

Feature **FEATURE_FONT_BITMAP** = `64`

TextServer supports loading bitmap fonts.

Feature **FEATURE_FONT_DYNAMIC** = `128`

TextServer supports loading dynamic (TrueType, OpeType, etc.) fonts.

Feature **FEATURE_FONT_MSDF** = `256`

TextServer supports multichannel signed distance field dynamic font rendering.

Feature **FEATURE_FONT_SYSTEM** = `512`

TextServer supports loading system fonts.

Feature **FEATURE_FONT_VARIABLE** = `1024`

TextServer supports variable fonts.

Feature **FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION** = `2048`

TextServer supports locale dependent and context sensitive case conversion.

Feature **FEATURE_USE_SUPPORT_DATA** = `4096`

TextServer require external data file for some features, see load_support_data().

Feature **FEATURE_UNICODE_IDENTIFIERS** = `8192`

TextServer supports UAX #31 identifier validation, see is_valid_identifier().

Feature **FEATURE_UNICODE_SECURITY** = `16384`

TextServer supports [Unicode Technical Report #36](https://unicode.org/reports/tr36/) and [Unicode Technical Standard #39](https://unicode.org/reports/tr39/) based spoof detection features.

---

enum **ContourPointTag**:

ContourPointTag **CONTOUR_CURVE_TAG_ON** = `1`

Contour point is on the curve.

ContourPointTag **CONTOUR_CURVE_TAG_OFF_CONIC** = `0`

Contour point isn't on the curve, but serves as a control point for a conic (quadratic) Bézier arc.

ContourPointTag **CONTOUR_CURVE_TAG_OFF_CUBIC** = `2`

Contour point isn't on the curve, but serves as a control point for a cubic Bézier arc.

---

enum **SpacingType**:

SpacingType **SPACING_GLYPH** = `0`

Spacing for each glyph.

SpacingType **SPACING_SPACE** = `1`

Spacing for the space character.

SpacingType **SPACING_TOP** = `2`

Spacing at the top of the line.

SpacingType **SPACING_BOTTOM** = `3`

Spacing at the bottom of the line.

SpacingType **SPACING_MAX** = `4`

Represents the size of the SpacingType enum.

---

flags **FontStyle**:

FontStyle **FONT_BOLD** = `1`

Font is bold.

FontStyle **FONT_ITALIC** = `2`

Font is italic or oblique.

FontStyle **FONT_FIXED_WIDTH** = `4`

Font has fixed-width characters (also known as monospace).

---

enum **StructuredTextParser**:

StructuredTextParser **STRUCTURED_TEXT_DEFAULT** = `0`

Use default Unicode BiDi algorithm.

StructuredTextParser **STRUCTURED_TEXT_URI** = `1`

BiDi override for URI.

StructuredTextParser **STRUCTURED_TEXT_FILE** = `2`

BiDi override for file path.

StructuredTextParser **STRUCTURED_TEXT_EMAIL** = `3`

BiDi override for email.

StructuredTextParser **STRUCTURED_TEXT_LIST** = `4`

BiDi override for lists. Structured text options: list separator [String](class_string.md#class-string).

StructuredTextParser **STRUCTURED_TEXT_GDSCRIPT** = `5`

BiDi override for GDScript.

StructuredTextParser **STRUCTURED_TEXT_CUSTOM** = `6`

User defined structured text BiDi override function.

---

enum **FixedSizeScaleMode**:

FixedSizeScaleMode **FIXED_SIZE_SCALE_DISABLE** = `0`

Bitmap font is not scaled.

FixedSizeScaleMode **FIXED_SIZE_SCALE_INTEGER_ONLY** = `1`

Bitmap font is scaled to the closest integer multiple of the font's fixed size. This is the recommended option for pixel art fonts.

FixedSizeScaleMode **FIXED_SIZE_SCALE_ENABLED** = `2`

Bitmap font is scaled to an arbitrary (fractional) size. This is the recommended option for non-pixel art fonts.

---

## Method Descriptions

[RID](class_rid.md#class-rid) **create_font**()

Creates a new, empty font cache entry resource. To free the resulting resource, use the free_rid() method.

---

[RID](class_rid.md#class-rid) **create_font_linked_variation**(font_rid: [RID](class_rid.md#class-rid))

Creates a new variation existing font which is reusing the same glyph cache and font data. To free the resulting resource, use the free_rid() method.

---

[RID](class_rid.md#class-rid) **create_shaped_text**(direction: Direction = 0, orientation: Orientation = 0)

Creates a new buffer for complex text layout, with the given `direction` and `orientation`. To free the resulting buffer, use free_rid() method.

**Note:** Direction is ignored if server does not support FEATURE_BIDI_LAYOUT feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced)).

**Note:** Orientation is ignored if server does not support FEATURE_VERTICAL_LAYOUT feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced)).

---

 **draw_hex_code_box**(canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Draws box displaying character hexadecimal code. Used for replacing missing characters.

---

 **font_clear_glyphs**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes all rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use font_remove_texture() to remove them manually.

---

 **font_clear_kerning_map**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Removes all kerning overrides.

---

 **font_clear_size_cache**(font_rid: [RID](class_rid.md#class-rid))

Removes all font sizes from the cache entry.

---

 **font_clear_system_fallback_cache**()

Frees all automatically loaded system fonts.

---

 **font_clear_textures**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes all textures from font cache entry.

**Note:** This function will not remove glyphs associated with the texture, use font_remove_glyph() to remove them manually.

---

 **font_draw_glyph**(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draws single glyph into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Note:** Glyph index is specific to the font, use glyphs indices returned by shaped_text_get_glyphs() or font_get_glyph_index().

**Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

---

 **font_draw_glyph_outline**(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draws single glyph outline of size `outline_size` into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Note:** Glyph index is specific to the font, use glyphs indices returned by shaped_text_get_glyphs() or font_get_glyph_index().

**Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

---

FontAntialiasing **font_get_antialiasing**(font_rid: [RID](class_rid.md#class-rid))

Returns font anti-aliasing mode.

---

[float](class_float.md#class-float) **font_get_ascent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns the font ascent (number of pixels above the baseline).

---

[float](class_float.md#class-float) **font_get_baseline_offset**(font_rid: [RID](class_rid.md#class-rid))

Returns extra baseline offset (as a fraction of font height).

---

[int](class_int.md#class-int) **font_get_char_from_glyph_index**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int))

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid. See font_get_glyph_index().

---

[float](class_float.md#class-float) **font_get_descent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns the font descent (number of pixels below the baseline).

---

[bool](class_bool.md#class-bool) **font_get_disable_embedded_bitmaps**(font_rid: [RID](class_rid.md#class-rid))

Returns whether the font's embedded bitmap loading is disabled.

---

[float](class_float.md#class-float) **font_get_embolden**(font_rid: [RID](class_rid.md#class-rid))

Returns font embolden strength.

---

[int](class_int.md#class-int) **font_get_face_count**(font_rid: [RID](class_rid.md#class-rid))

Returns number of faces in the TrueType / OpenType collection.

---

[int](class_int.md#class-int) **font_get_face_index**(font_rid: [RID](class_rid.md#class-rid))

Returns an active face index in the TrueType / OpenType collection.

---

[int](class_int.md#class-int) **font_get_fixed_size**(font_rid: [RID](class_rid.md#class-rid))

Returns bitmap font fixed size.

---

FixedSizeScaleMode **font_get_fixed_size_scale_mode**(font_rid: [RID](class_rid.md#class-rid))

Returns bitmap font scaling mode.

---

[bool](class_bool.md#class-bool) **font_get_generate_mipmaps**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if font texture mipmap generation is enabled.

---

[float](class_float.md#class-float) **font_get_global_oversampling**()

**Deprecated:** Use [Viewport](class_viewport.md#class-viewport) oversampling, or the `oversampling` argument of the `draw_*` methods instead.

This method does nothing and always returns `1.0`.

---

[Vector2](class_vector2.md#class-vector2) **font_get_glyph_advance**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int))

Returns glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

---

[Dictionary](class_dictionary.md#class-dictionary) **font_get_glyph_contours**(font: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), index: [int](class_int.md#class-int))

Returns outline contours of the glyph as a [Dictionary](class_dictionary.md#class-dictionary) with the following contents:

`points`         - [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), containing outline points. `x` and `y` are point coordinates. `z` is the type of the point, using the ContourPointTag values.

`contours`       - [PackedInt32Array](class_packedint32array.md#class-packedint32array), containing indices the end points of each contour.

`orientation`    - [bool](class_bool.md#class-bool), contour orientation. If `true`, clockwise contours must be filled.

- Two successive CONTOUR_CURVE_TAG_ON points indicate a line segment.
- One CONTOUR_CURVE_TAG_OFF_CONIC point between two CONTOUR_CURVE_TAG_ON points indicates a single conic (quadratic) Bézier arc.
- Two CONTOUR_CURVE_TAG_OFF_CUBIC points between two CONTOUR_CURVE_TAG_ON points indicate a single cubic Bézier arc.
- Two successive CONTOUR_CURVE_TAG_OFF_CONIC points indicate two successive conic (quadratic) Bézier arcs with a virtual CONTOUR_CURVE_TAG_ON point at their middle.
- Each contour is closed. The last point of a contour uses the first point of a contour as its next point, and vice versa. The first point can be CONTOUR_CURVE_TAG_OFF_CONIC point.

---

[int](class_int.md#class-int) **font_get_glyph_index**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int))

Returns the glyph index of a `char`, optionally modified by the `variation_selector`. See font_get_char_from_glyph_index().

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **font_get_glyph_list**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Returns list of rendered glyphs in the cache entry.

---

[Vector2](class_vector2.md#class-vector2) **font_get_glyph_offset**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns glyph offset from the baseline.

---

[Vector2](class_vector2.md#class-vector2) **font_get_glyph_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns size of the glyph.

---

[int](class_int.md#class-int) **font_get_glyph_texture_idx**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns index of the cache texture containing the glyph.

---

[RID](class_rid.md#class-rid) **font_get_glyph_texture_rid**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns resource ID of the cache texture containing the glyph.

**Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

---

[Vector2](class_vector2.md#class-vector2) **font_get_glyph_texture_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns size of the cache texture containing the glyph.

**Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

---

[Rect2](class_rect2.md#class-rect2) **font_get_glyph_uv_rect**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns rectangle in the cache texture containing the glyph.

---

Hinting **font_get_hinting**(font_rid: [RID](class_rid.md#class-rid))

Returns the font hinting mode. Used by dynamic fonts only.

---

[bool](class_bool.md#class-bool) **font_get_keep_rounding_remainders**(font_rid: [RID](class_rid.md#class-rid))

Returns glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

[Vector2](class_vector2.md#class-vector2) **font_get_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))

Returns kerning for the pair of glyphs.

---

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **font_get_kerning_list**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns list of the kerning overrides.

---

[bool](class_bool.md#class-bool) **font_get_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))

Returns `true` if support override is enabled for the `language`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **font_get_language_support_overrides**(font_rid: [RID](class_rid.md#class-rid))

Returns list of language support overrides.

---

[int](class_int.md#class-int) **font_get_msdf_pixel_range**(font_rid: [RID](class_rid.md#class-rid))

Returns the width of the range around the shape between the minimum and maximum representable signed distance.

---

[int](class_int.md#class-int) **font_get_msdf_size**(font_rid: [RID](class_rid.md#class-rid))

Returns source font size used to generate MSDF textures.

---

[String](class_string.md#class-string) **font_get_name**(font_rid: [RID](class_rid.md#class-rid))

Returns font family name.

---

[Dictionary](class_dictionary.md#class-dictionary) **font_get_opentype_feature_overrides**(font_rid: [RID](class_rid.md#class-rid))

Returns font OpenType feature set override.

---

[Dictionary](class_dictionary.md#class-dictionary) **font_get_ot_name_strings**(font_rid: [RID](class_rid.md#class-rid))

Returns [Dictionary](class_dictionary.md#class-dictionary) with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

---

[float](class_float.md#class-float) **font_get_oversampling**(font_rid: [RID](class_rid.md#class-rid))

Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **font_get_palette_colors**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the array in the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors. Colors can be overridden using font_set_palette_custom_colors().

---

[int](class_int.md#class-int) **font_get_palette_count**(font_rid: [RID](class_rid.md#class-rid))

Returns the number of predefined color palettes. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **font_get_palette_custom_colors**(font_rid: [RID](class_rid.md#class-rid))

Returns array of custom colors to override predefined palette.

---

[String](class_string.md#class-string) **font_get_palette_name**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the name of the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---

[float](class_float.md#class-float) **font_get_scale**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns scaling factor of the color bitmap font.

---

[bool](class_bool.md#class-bool) **font_get_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))

Returns `true` if support override is enabled for the `script`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **font_get_script_support_overrides**(font_rid: [RID](class_rid.md#class-rid))

Returns list of script support overrides.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **font_get_size_cache_info**(font_rid: [RID](class_rid.md#class-rid))

Returns font cache information, each entry contains the following fields: `Vector2i size_px` - font size in pixels, `float viewport_oversampling` - viewport oversampling factor, `int glyphs` - number of rendered glyphs, `int textures` - number of used textures, `int textures_size` - size of texture data in bytes.

---

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **font_get_size_cache_list**(font_rid: [RID](class_rid.md#class-rid))

Returns list of the font sizes in the cache. Each size is [Vector2i](class_vector2i.md#class-vector2i) with font size and outline size.

---

[int](class_int.md#class-int) **font_get_spacing**(font_rid: [RID](class_rid.md#class-rid), spacing: SpacingType)

Returns the spacing for `spacing` in pixels (not relative to the font size).

---

[int](class_int.md#class-int) **font_get_stretch**(font_rid: [RID](class_rid.md#class-rid))

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

[FontStyle] **font_get_style**(font_rid: [RID](class_rid.md#class-rid))

Returns font style flags.

---

[String](class_string.md#class-string) **font_get_style_name**(font_rid: [RID](class_rid.md#class-rid))

Returns font style name.

---

SubpixelPositioning **font_get_subpixel_positioning**(font_rid: [RID](class_rid.md#class-rid))

Returns font subpixel glyph positioning mode.

---

[String](class_string.md#class-string) **font_get_supported_chars**(font_rid: [RID](class_rid.md#class-rid))

Returns a string containing all the characters available in the font.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **font_get_supported_glyphs**(font_rid: [RID](class_rid.md#class-rid))

Returns an array containing all glyph indices in the font.

---

[int](class_int.md#class-int) **font_get_texture_count**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Returns number of textures used by font cache entry.

---

[Image](class_image.md#class-image) **font_get_texture_image**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Returns font cache texture image data.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **font_get_texture_offsets**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Returns array containing glyph packing data.

---

[Transform2D](class_transform2d.md#class-transform2d) **font_get_transform**(font_rid: [RID](class_rid.md#class-rid))

Returns 2D transform applied to the font outlines.

---

[float](class_float.md#class-float) **font_get_underline_position**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns pixel offset of the underline below the baseline.

---

[float](class_float.md#class-float) **font_get_underline_thickness**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns thickness of the underline in pixels.

---

[int](class_int.md#class-int) **font_get_used_palette**(font_rid: [RID](class_rid.md#class-rid))

Returns used palette index.

---

[Dictionary](class_dictionary.md#class-dictionary) **font_get_variation_coordinates**(font_rid: [RID](class_rid.md#class-rid))

Returns variation coordinates for the specified font cache entry. See font_supported_variation_list() for more info.

---

[int](class_int.md#class-int) **font_get_weight**(font_rid: [RID](class_rid.md#class-rid))

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

[bool](class_bool.md#class-bool) **font_has_char**(font_rid: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int))

Returns `true` if a Unicode `char` is available in the font.

---

[bool](class_bool.md#class-bool) **font_is_allow_system_fallback**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if system fonts can be automatically used as fallbacks.

---

[bool](class_bool.md#class-bool) **font_is_force_autohinter**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if auto-hinting is supported and preferred over font built-in hinting. Used by dynamic fonts only.

---

[bool](class_bool.md#class-bool) **font_is_language_supported**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))

Returns `true` if the font supports the given language (as a [ISO 639](https://en.wikipedia.org/wiki/ISO_639-1) code).

---

[bool](class_bool.md#class-bool) **font_is_modulate_color_glyphs**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if color modulation is applied when drawing the font's colored glyphs.

---

[bool](class_bool.md#class-bool) **font_is_multichannel_signed_distance_field**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

---

[bool](class_bool.md#class-bool) **font_is_script_supported**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))

Returns `true` if the font supports the given script (as a [ISO 15924](https://en.wikipedia.org/wiki/ISO_15924) code).

---

 **font_remove_glyph**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Removes specified rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use font_remove_texture() to remove them manually.

---

 **font_remove_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))

Removes kerning override for the pair of glyphs.

---

 **font_remove_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))

Remove language support override.

---

 **font_remove_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))

Removes script support override.

---

 **font_remove_size_cache**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes specified font size from the cache entry.

---

 **font_remove_texture**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Removes specified texture from the cache entry.

**Note:** This function will not remove glyphs associated with the texture, remove them manually, using font_remove_glyph().

---

 **font_render_glyph**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int))

Renders specified glyph to the font cache texture.

---

 **font_render_range**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))

Renders the range of characters to the font cache texture.

---

 **font_set_allow_system_fallback**(font_rid: [RID](class_rid.md#class-rid), allow_system_fallback: [bool](class_bool.md#class-bool))

If set to `true`, system fonts can be automatically used as fallbacks.

---

 **font_set_antialiasing**(font_rid: [RID](class_rid.md#class-rid), antialiasing: FontAntialiasing)

Sets font anti-aliasing mode.

---

 **font_set_ascent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float))

Sets the font ascent (number of pixels above the baseline).

---

 **font_set_baseline_offset**(font_rid: [RID](class_rid.md#class-rid), baseline_offset: [float](class_float.md#class-float))

Sets extra baseline offset (as a fraction of font height).

---

 **font_set_data**(font_rid: [RID](class_rid.md#class-rid), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Sets font source data, e.g contents of the dynamic font source file.

---

 **font_set_descent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float))

Sets the font descent (number of pixels below the baseline).

---

 **font_set_disable_embedded_bitmaps**(font_rid: [RID](class_rid.md#class-rid), disable_embedded_bitmaps: [bool](class_bool.md#class-bool))

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

---

 **font_set_embolden**(font_rid: [RID](class_rid.md#class-rid), strength: [float](class_float.md#class-float))

Sets font embolden strength. If `strength` is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---

 **font_set_face_index**(font_rid: [RID](class_rid.md#class-rid), face_index: [int](class_int.md#class-int))

Sets an active face index in the TrueType / OpenType collection.

---

 **font_set_fixed_size**(font_rid: [RID](class_rid.md#class-rid), fixed_size: [int](class_int.md#class-int))

Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.

---

 **font_set_fixed_size_scale_mode**(font_rid: [RID](class_rid.md#class-rid), fixed_size_scale_mode: FixedSizeScaleMode)

Sets bitmap font scaling mode. This property is used only if `fixed_size` is greater than zero.

---

 **font_set_force_autohinter**(font_rid: [RID](class_rid.md#class-rid), force_autohinter: [bool](class_bool.md#class-bool))

If set to `true` auto-hinting is preferred over font built-in hinting.

---

 **font_set_generate_mipmaps**(font_rid: [RID](class_rid.md#class-rid), generate_mipmaps: [bool](class_bool.md#class-bool))

If set to `true` font texture mipmap generation is enabled.

---

 **font_set_global_oversampling**(oversampling: [float](class_float.md#class-float))

**Deprecated:** Use [Viewport](class_viewport.md#class-viewport) oversampling, or the `oversampling` argument of the `draw_*` methods instead.

This method does nothing.

---

 **font_set_glyph_advance**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2))

Sets glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

---

 **font_set_glyph_offset**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2))

Sets glyph offset from the baseline.

---

 **font_set_glyph_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2))

Sets size of the glyph.

---

 **font_set_glyph_texture_idx**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int))

Sets index of the cache texture containing the glyph.

---

 **font_set_glyph_uv_rect**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2))

Sets rectangle in the cache texture containing the glyph.

---

 **font_set_hinting**(font_rid: [RID](class_rid.md#class-rid), hinting: Hinting)

Sets font hinting mode. Used by dynamic fonts only.

---

 **font_set_keep_rounding_remainders**(font_rid: [RID](class_rid.md#class-rid), keep_rounding_remainders: [bool](class_bool.md#class-bool))

Sets glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

 **font_set_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2))

Sets kerning for the pair of glyphs.

---

 **font_set_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))

Adds override for font_is_language_supported().

---

 **font_set_modulate_color_glyphs**(font_rid: [RID](class_rid.md#class-rid), modulate: [bool](class_bool.md#class-bool))

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---

 **font_set_msdf_pixel_range**(font_rid: [RID](class_rid.md#class-rid), msdf_pixel_range: [int](class_int.md#class-int))

Sets the width of the range around the shape between the minimum and maximum representable signed distance.

---

 **font_set_msdf_size**(font_rid: [RID](class_rid.md#class-rid), msdf_size: [int](class_int.md#class-int))

Sets source font size used to generate MSDF textures.

---

 **font_set_multichannel_signed_distance_field**(font_rid: [RID](class_rid.md#class-rid), msdf: [bool](class_bool.md#class-bool))

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

**Note:** MSDF font rendering does not render glyphs with overlapping shapes correctly. Overlapping shapes are not valid per the OpenType standard, but are still commonly found in many font files, especially those converted by Google Fonts. To avoid issues with overlapping glyphs, consider downloading the font file directly from the type foundry instead of relying on Google Fonts.

---

 **font_set_name**(font_rid: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))

Sets the font family name.

---

 **font_set_opentype_feature_overrides**(font_rid: [RID](class_rid.md#class-rid), overrides: [Dictionary](class_dictionary.md#class-dictionary))

Sets font OpenType feature set override.

---

 **font_set_oversampling**(font_rid: [RID](class_rid.md#class-rid), oversampling: [float](class_float.md#class-float))

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---

 **font_set_palette_custom_colors**(font_rid: [RID](class_rid.md#class-rid), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))

Sets array of custom colors to override predefined palette. Set to empty array to reset overrides. Use `Color(0, 0, 0, 0)`, to keep predefined palette color at specific position.

---

 **font_set_scale**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float))

Sets scaling factor of the color bitmap font.

---

 **font_set_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))

Adds override for font_is_script_supported().

---

 **font_set_spacing**(font_rid: [RID](class_rid.md#class-rid), spacing: SpacingType, value: [int](class_int.md#class-int))

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

---

 **font_set_stretch**(font_rid: [RID](class_rid.md#class-rid), weight: [int](class_int.md#class-int))

Sets font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

**Note:** This value is used for font matching only and will not affect font rendering. Use font_set_face_index(), font_set_variation_coordinates(), or font_set_transform() instead.

---

 **font_set_style**(font_rid: [RID](class_rid.md#class-rid), style: [FontStyle])

Sets the font style flags.

**Note:** This value is used for font matching only and will not affect font rendering. Use font_set_face_index(), font_set_variation_coordinates(), font_set_embolden(), or font_set_transform() instead.

---

 **font_set_style_name**(font_rid: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))

Sets the font style name.

---

 **font_set_subpixel_positioning**(font_rid: [RID](class_rid.md#class-rid), subpixel_positioning: SubpixelPositioning)

Sets font subpixel glyph positioning mode.

---

 **font_set_texture_image**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image))

Sets font cache texture image data.

---

 **font_set_texture_offsets**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Sets array containing glyph packing data.

---

 **font_set_transform**(font_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

For example, to simulate italic typeface by slanting, apply the following transform `Transform2D(1.0, slant, 0.0, 1.0, 0.0, 0.0)`.

---

 **font_set_underline_position**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float))

Sets pixel offset of the underline below the baseline.

---

 **font_set_underline_thickness**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float))

Sets thickness of the underline in pixels.

---

 **font_set_used_palette**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Sets used palette index.

---

 **font_set_variation_coordinates**(font_rid: [RID](class_rid.md#class-rid), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary))

Sets variation coordinates for the specified font cache entry. See font_supported_variation_list() for more info.

---

 **font_set_weight**(font_rid: [RID](class_rid.md#class-rid), weight: [int](class_int.md#class-int))

Sets weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

**Note:** This value is used for font matching only and will not affect font rendering. Use font_set_face_index(), font_set_variation_coordinates(), or font_set_embolden() instead.

---

[Dictionary](class_dictionary.md#class-dictionary) **font_supported_feature_list**(font_rid: [RID](class_rid.md#class-rid))

Returns the dictionary of the supported OpenType features.

---

[Dictionary](class_dictionary.md#class-dictionary) **font_supported_variation_list**(font_rid: [RID](class_rid.md#class-rid))

Returns the dictionary of the supported OpenType variation coordinates.

---

[String](class_string.md#class-string) **format_number**(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")

**Deprecated:** Use [TranslationServer.format_number()](class_translationserver.md#class-translationserver-method-format-number) instead.

Converts a number from Western Arabic (0..9) to the numeral system used in the given `language`.

If `language` is an empty string, the active locale will be used.

---

 **free_rid**(rid: [RID](class_rid.md#class-rid))

Frees an object created by this **TextServer**.

---

[int](class_int.md#class-int) **get_features**()

Returns text server features, see Feature.

---

[Vector2](class_vector2.md#class-vector2) **get_hex_code_box_size**(size: [int](class_int.md#class-int), index: [int](class_int.md#class-int))

Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).

---

[String](class_string.md#class-string) **get_name**()

Returns the name of the server interface.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_support_data**()

Returns default TextServer database (e.g. ICU break iterators and dictionaries).

---

[String](class_string.md#class-string) **get_support_data_filename**()

Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.

---

[String](class_string.md#class-string) **get_support_data_info**()

Returns TextServer database (e.g. ICU break iterators and dictionaries) description.

---

[bool](class_bool.md#class-bool) **has**(rid: [RID](class_rid.md#class-rid))

Returns `true` if `rid` is valid resource owned by this text server.

---

[bool](class_bool.md#class-bool) **has_feature**(feature: Feature)

Returns `true` if the server supports a feature.

---

[int](class_int.md#class-int) **is_confusable**(string: [String](class_string.md#class-string), dict: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Returns index of the first string in `dict` which is visually confusable with the `string`, or `-1` if none is found.

**Note:** This method doesn't detect invisible characters, for spoof detection use it in combination with spoof_check().

**Note:** Always returns `-1` if the server does not support the FEATURE_UNICODE_SECURITY feature.

---

[bool](class_bool.md#class-bool) **is_locale_right_to_left**(locale: [String](class_string.md#class-string))

Returns `true` if locale is right-to-left.

---

[bool](class_bool.md#class-bool) **is_locale_using_support_data**(locale: [String](class_string.md#class-string))

Returns `true` if the locale requires text server support data for line/word breaking.

---

[bool](class_bool.md#class-bool) **is_valid_identifier**(string: [String](class_string.md#class-string))

Returns `true` if `string` is a valid identifier.

If the text server supports the FEATURE_UNICODE_IDENTIFIERS feature, a valid identifier must:

- Conform to normalization form C.
- Begin with a Unicode character of class XID_Start or `"_"`.
- May contain Unicode characters of class XID_Continue in the other positions.
- Use UAX #31 recommended scripts only (mixed scripts are allowed).

If the FEATURE_UNICODE_IDENTIFIERS feature is not supported, a valid identifier must:

- Begin with a Unicode character of class XID_Start or `"_"`.
- May contain Unicode characters of class XID_Continue in the other positions.

---

[bool](class_bool.md#class-bool) **is_valid_letter**(unicode: [int](class_int.md#class-int))

Returns `true` if the given code point is a valid letter, i.e. it belongs to the Unicode category "L".

---

[bool](class_bool.md#class-bool) **load_support_data**(filename: [String](class_string.md#class-string))

Loads optional TextServer database (e.g. ICU break iterators and dictionaries).

**Note:** This function should be called before any other TextServer functions used, otherwise it won't have any effect.

---

[int](class_int.md#class-int) **name_to_tag**(name: [String](class_string.md#class-string))

Converts the given readable name of a feature, variation, script, or language to an OpenType tag.

---

[String](class_string.md#class-string) **parse_number**(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")

**Deprecated:** Use [TranslationServer.parse_number()](class_translationserver.md#class-translationserver-method-parse-number) instead.

Converts `number` from the numeral system used in the given `language` to Western Arabic (0..9).

If `language` is an empty string, the active locale will be used.

---

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **parse_structured_text**(parser_type: StructuredTextParser, args: [Array](class_array.md#class-array), text: [String](class_string.md#class-string))

Default implementation of the BiDi algorithm override function.

---

[String](class_string.md#class-string) **percent_sign**(language: [String](class_string.md#class-string) = "")

**Deprecated:** Use [TranslationServer.get_percent_sign()](class_translationserver.md#class-translationserver-method-get-percent-sign) instead.

Returns the percent sign used in the given `language`.

If `language` is an empty string, the active locale will be used.

---

[bool](class_bool.md#class-bool) **save_support_data**(filename: [String](class_string.md#class-string))

Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.

**Note:** This function is used by during project export, to include TextServer database.

---

[int](class_int.md#class-int) **shaped_get_run_count**(shaped: [RID](class_rid.md#class-rid))

Returns the number of uniform text runs in the buffer.

---

Direction **shaped_get_run_direction**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the direction of the `index` text run (in visual order).

---

[RID](class_rid.md#class-rid) **shaped_get_run_font_rid**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the font RID of the `index` text run (in visual order).

---

[int](class_int.md#class-int) **shaped_get_run_font_size**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the font size of the `index` text run (in visual order).

---

[Vector2i](class_vector2i.md#class-vector2i) **shaped_get_run_glyph_range**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the glyph range of the `index` text run (in visual order).

---

[String](class_string.md#class-string) **shaped_get_run_language**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the language of the `index` text run (in visual order).

---

[Variant](class_variant.md#class-variant) **shaped_get_run_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the embedded object of the `index` text run (in visual order).

---

[Vector2i](class_vector2i.md#class-vector2i) **shaped_get_run_range**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the source text range of the `index` text run (in visual order).

---

[String](class_string.md#class-string) **shaped_get_run_text**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the source text of the `index` text run (in visual order).

---

[int](class_int.md#class-int) **shaped_get_span_count**(shaped: [RID](class_rid.md#class-rid))

Returns number of text spans added using shaped_text_add_string() or shaped_text_add_object().

---

[Variant](class_variant.md#class-variant) **shaped_get_span_embedded_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns text embedded object key.

---

[Variant](class_variant.md#class-variant) **shaped_get_span_meta**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns text span metadata.

---

[Variant](class_variant.md#class-variant) **shaped_get_span_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the text span embedded object key.

---

[String](class_string.md#class-string) **shaped_get_span_text**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the text span source text.

---

[String](class_string.md#class-string) **shaped_get_text**(shaped: [RID](class_rid.md#class-rid))

Returns the text buffer source text, including object replacement characters.

---

 **shaped_set_span_update_font**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary) = {})

Changes text span font, font size, and OpenType features, without changing the text.

---

[bool](class_bool.md#class-bool) **shaped_text_add_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, length: [int](class_int.md#class-int) = 1, baseline: [float](class_float.md#class-float) = 0.0)

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---

[bool](class_bool.md#class-bool) **shaped_text_add_string**(shaped: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary) = {}, language: [String](class_string.md#class-string) = "", meta: [Variant](class_variant.md#class-variant) = null)

Adds text span and font to draw it to the text buffer.

---

 **shaped_text_clear**(rid: [RID](class_rid.md#class-rid))

Clears text buffer (removes text and inline objects).

---

[int](class_int.md#class-int) **shaped_text_closest_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns composite character position closest to the `pos`.

---

 **shaped_text_draw**(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float) = -1, clip_r: [float](class_float.md#class-float) = -1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

`clip_l` and `clip_r` are offsets relative to `pos`, going to the right in horizontal layout and downward in vertical layout. If `clip_l` is not negative, glyphs starting before the offset are clipped. If `clip_r` is not negative, glyphs ending after the offset are clipped.

---

 **shaped_text_draw_outline**(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float) = -1, clip_r: [float](class_float.md#class-float) = -1, outline_size: [int](class_int.md#class-int) = 1, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), oversampling: [float](class_float.md#class-float) = 0.0)

Draw the outline of the shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

`clip_l` and `clip_r` are offsets relative to `pos`, going to the right in horizontal layout and downward in vertical layout. If `clip_l` is not negative, glyphs starting before the offset are clipped. If `clip_r` is not negative, glyphs ending after the offset are clipped.

---

[RID](class_rid.md#class-rid) **shaped_text_duplicate**(rid: [RID](class_rid.md#class-rid))

Duplicates shaped text buffer.

---

[float](class_float.md#class-float) **shaped_text_fit_to_width**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), justification_flags: [JustificationFlag] = 3)

Adjusts text width to fit to specified width, returns new text width.

---

[float](class_float.md#class-float) **shaped_text_get_ascent**(shaped: [RID](class_rid.md#class-rid))

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

**Note:** Overall ascent can be higher than font ascent, if some glyphs are displaced from the baseline.

---

[Dictionary](class_dictionary.md#class-dictionary) **shaped_text_get_carets**(shaped: [RID](class_rid.md#class-rid), position: [int](class_int.md#class-int))

Returns shapes of the carets corresponding to the character offset `position` in the text. Returned caret shape is 1 pixel wide rectangle.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **shaped_text_get_character_breaks**(shaped: [RID](class_rid.md#class-rid))

Returns array of the composite character boundaries.

---

[int](class_int.md#class-int) **shaped_text_get_custom_ellipsis**(shaped: [RID](class_rid.md#class-rid))

Returns ellipsis character used for text clipping.

---

[String](class_string.md#class-string) **shaped_text_get_custom_punctuation**(shaped: [RID](class_rid.md#class-rid))

Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

[float](class_float.md#class-float) **shaped_text_get_descent**(shaped: [RID](class_rid.md#class-rid))

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

**Note:** Overall descent can be higher than font descent, if some glyphs are displaced from the baseline.

---

Direction **shaped_text_get_direction**(shaped: [RID](class_rid.md#class-rid))

Returns direction of the text.

---

Direction **shaped_text_get_dominant_direction_in_range**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))

Returns dominant direction of in the range of text.

---

[int](class_int.md#class-int) **shaped_text_get_ellipsis_glyph_count**(shaped: [RID](class_rid.md#class-rid))

Returns number of glyphs in the ellipsis.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **shaped_text_get_ellipsis_glyphs**(shaped: [RID](class_rid.md#class-rid))

Returns array of the glyphs in the ellipsis.

---

[int](class_int.md#class-int) **shaped_text_get_ellipsis_pos**(shaped: [RID](class_rid.md#class-rid))

Returns position of the ellipsis.

---

[int](class_int.md#class-int) **shaped_text_get_glyph_count**(shaped: [RID](class_rid.md#class-rid))

Returns number of glyphs in the buffer.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **shaped_text_get_glyphs**(shaped: [RID](class_rid.md#class-rid))

Returns an array of glyphs in the visual order.

---

[Vector2](class_vector2.md#class-vector2) **shaped_text_get_grapheme_bounds**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns composite character's bounds as offsets from the start of the line.

---

Direction **shaped_text_get_inferred_direction**(shaped: [RID](class_rid.md#class-rid))

Returns direction of the text, inferred by the BiDi algorithm.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **shaped_text_get_line_breaks**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), start: [int](class_int.md#class-int) = 0, break_flags: [LineBreakFlag] = 3)

Breaks text to the lines and returns character ranges for each line.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **shaped_text_get_line_breaks_adv**(shaped: [RID](class_rid.md#class-rid), width: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), start: [int](class_int.md#class-int) = 0, once: [bool](class_bool.md#class-bool) = true, break_flags: [LineBreakFlag] = 3)

Breaks text to the lines and columns. Returns character ranges for each segment.

---

[int](class_int.md#class-int) **shaped_text_get_object_glyph**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))

Returns the glyph index of the inline object.

---

[Vector2i](class_vector2i.md#class-vector2i) **shaped_text_get_object_range**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))

Returns the character range of the inline object.

---

[Rect2](class_rect2.md#class-rect2) **shaped_text_get_object_rect**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))

Returns bounding rectangle of the inline object.

---

[Array](class_array.md#class-array) **shaped_text_get_objects**(shaped: [RID](class_rid.md#class-rid))

Returns array of inline objects.

---

Orientation **shaped_text_get_orientation**(shaped: [RID](class_rid.md#class-rid))

Returns text orientation.

---

[RID](class_rid.md#class-rid) **shaped_text_get_parent**(shaped: [RID](class_rid.md#class-rid))

Returns the parent buffer from which the substring originates.

---

[bool](class_bool.md#class-bool) **shaped_text_get_preserve_control**(shaped: [RID](class_rid.md#class-rid))

Returns `true` if text buffer is configured to display control characters.

---

[bool](class_bool.md#class-bool) **shaped_text_get_preserve_invalid**(shaped: [RID](class_rid.md#class-rid))

Returns `true` if text buffer is configured to display hexadecimal codes in place of invalid characters.

**Note:** If set to `false`, nothing is displayed in place of invalid characters.

---

[Vector2i](class_vector2i.md#class-vector2i) **shaped_text_get_range**(shaped: [RID](class_rid.md#class-rid))

Returns substring buffer character range in the parent buffer.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **shaped_text_get_selection**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))

Returns selection rectangles for the specified character range.

---

[Vector2](class_vector2.md#class-vector2) **shaped_text_get_size**(shaped: [RID](class_rid.md#class-rid))

Returns size of the text.

---

[int](class_int.md#class-int) **shaped_text_get_spacing**(shaped: [RID](class_rid.md#class-rid), spacing: SpacingType)

Returns extra spacing added between glyphs or lines in pixels.

---

[int](class_int.md#class-int) **shaped_text_get_trim_pos**(shaped: [RID](class_rid.md#class-rid))

Returns the position of the overrun trim.

---

[float](class_float.md#class-float) **shaped_text_get_underline_position**(shaped: [RID](class_rid.md#class-rid))

Returns pixel offset of the underline below the baseline.

---

[float](class_float.md#class-float) **shaped_text_get_underline_thickness**(shaped: [RID](class_rid.md#class-rid))

Returns thickness of the underline.

---

[float](class_float.md#class-float) **shaped_text_get_width**(shaped: [RID](class_rid.md#class-rid))

Returns width (for horizontal layout) or height (for vertical) of the text.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **shaped_text_get_word_breaks**(shaped: [RID](class_rid.md#class-rid), grapheme_flags: [GraphemeFlag] = 264, skip_grapheme_flags: [GraphemeFlag] = 4)

Breaks text into words and returns array of character ranges. Use `grapheme_flags` to set what characters are used for breaking.

---

[bool](class_bool.md#class-bool) **shaped_text_has_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))

Returns `true` if an object with `key` is embedded in this shaped text buffer.

---

[bool](class_bool.md#class-bool) **shaped_text_has_visible_chars**(shaped: [RID](class_rid.md#class-rid))

Returns `true` if text buffer contains any visible characters.

---

[int](class_int.md#class-int) **shaped_text_hit_test_grapheme**(shaped: [RID](class_rid.md#class-rid), coords: [float](class_float.md#class-float))

Returns grapheme index at the specified pixel offset at the baseline, or `-1` if none is found.

---

[int](class_int.md#class-int) **shaped_text_hit_test_position**(shaped: [RID](class_rid.md#class-rid), coords: [float](class_float.md#class-float))

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

---

[bool](class_bool.md#class-bool) **shaped_text_is_ready**(shaped: [RID](class_rid.md#class-rid))

Returns `true` if buffer is successfully shaped.

---

[int](class_int.md#class-int) **shaped_text_next_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns composite character end position closest to the `pos`.

---

[int](class_int.md#class-int) **shaped_text_next_grapheme_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns grapheme end position closest to the `pos`.

---

 **shaped_text_overrun_trim_to_width**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float) = 0, overrun_trim_flags: [TextOverrunFlag] = 0)

Trims text if it exceeds the given width.

---

[int](class_int.md#class-int) **shaped_text_prev_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns composite character start position closest to the `pos`.

---

[int](class_int.md#class-int) **shaped_text_prev_grapheme_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns grapheme start position closest to the `pos`.

---

[bool](class_bool.md#class-bool) **shaped_text_resize_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, baseline: [float](class_float.md#class-float) = 0.0)

Sets new size and alignment of embedded object.

---

 **shaped_text_set_bidi_override**(shaped: [RID](class_rid.md#class-rid), override: [Array](class_array.md#class-array))

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

---

 **shaped_text_set_custom_ellipsis**(shaped: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int))

Sets ellipsis character used for text clipping.

---

 **shaped_text_set_custom_punctuation**(shaped: [RID](class_rid.md#class-rid), punct: [String](class_string.md#class-string))

Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

 **shaped_text_set_direction**(shaped: [RID](class_rid.md#class-rid), direction: Direction = 0)

Sets desired text direction. If set to DIRECTION_AUTO, direction will be detected based on the buffer contents and current locale.

**Note:** Direction is ignored if server does not support FEATURE_BIDI_LAYOUT feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced)).

---

 **shaped_text_set_orientation**(shaped: [RID](class_rid.md#class-rid), orientation: Orientation = 0)

Sets desired text orientation.

**Note:** Orientation is ignored if server does not support FEATURE_VERTICAL_LAYOUT feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced)).

---

 **shaped_text_set_preserve_control**(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If set to `true` text buffer will display control characters.

---

 **shaped_text_set_preserve_invalid**(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If set to `true` text buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.

---

 **shaped_text_set_spacing**(shaped: [RID](class_rid.md#class-rid), spacing: SpacingType, value: [int](class_int.md#class-int))

Sets extra spacing added between glyphs or lines in pixels.

---

[bool](class_bool.md#class-bool) **shaped_text_shape**(shaped: [RID](class_rid.md#class-rid))

Shapes buffer if it's not shaped. Returns `true` if the string is shaped successfully.

**Note:** It is not necessary to call this function manually, buffer will be shaped automatically as soon as any of its output data is requested.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **shaped_text_sort_logical**(shaped: [RID](class_rid.md#class-rid))

Returns text glyphs in the logical order.

---

[RID](class_rid.md#class-rid) **shaped_text_substr**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), length: [int](class_int.md#class-int))

Returns text buffer for the substring of the text in the `shaped` text buffer (including inline objects).

---

[float](class_float.md#class-float) **shaped_text_tab_align**(shaped: [RID](class_rid.md#class-rid), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Aligns shaped text to the given tab-stops.

---

[bool](class_bool.md#class-bool) **spoof_check**(string: [String](class_string.md#class-string))

Returns `true` if `string` is likely to be an attempt at confusing the reader.

**Note:** Always returns `false` if the server does not support the FEATURE_UNICODE_SECURITY feature.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **string_get_character_breaks**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")

Returns array of the composite character boundaries.

```gdscript
var ts = TextServerManager.get_primary_interface()
print(ts.string_get_character_breaks("Test ❤️‍🔥 Test")) # Prints [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14]
```

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **string_get_word_breaks**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "", chars_per_line: [int](class_int.md#class-int) = 0)

Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.

When `chars_per_line` is greater than zero, line break boundaries are returned instead.

```gdscript
var ts = TextServerManager.get_primary_interface()
# Corresponds to the substrings "The", "Godot", "Engine", and "4".
print(ts.string_get_word_breaks("The Godot Engine, 4")) # Prints [0, 3, 4, 9, 10, 16, 18, 19]
# Corresponds to the substrings "The", "Godot", "Engin", and "e, 4".
print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 5)) # Prints [0, 3, 4, 9, 10, 15, 15, 19]
# Corresponds to the substrings "The Godot" and "Engine, 4".
print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 10)) # Prints [0, 9, 10, 19]
```

---

[String](class_string.md#class-string) **string_to_lower**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")

Returns the string converted to `lowercase`.

**Note:** Casing is locale dependent and context sensitive if server support FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced)).

**Note:** The result may be longer or shorter than the original.

---

[String](class_string.md#class-string) **string_to_title**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")

Returns the string converted to `Title Case`.

**Note:** Casing is locale dependent and context sensitive if server support FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced)).

**Note:** The result may be longer or shorter than the original.

---

[String](class_string.md#class-string) **string_to_upper**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string) = "")

Returns the string converted to `UPPERCASE`.

**Note:** Casing is locale dependent and context sensitive if server support FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION feature (supported by [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced)).

**Note:** The result may be longer or shorter than the original.

---

[String](class_string.md#class-string) **strip_diacritics**(string: [String](class_string.md#class-string))

Strips diacritics from the string.

**Note:** The result may be longer or shorter than the original.

---

[String](class_string.md#class-string) **tag_to_name**(tag: [int](class_int.md#class-int))

Converts the given OpenType tag to the readable name of a feature, variation, script, or language.
