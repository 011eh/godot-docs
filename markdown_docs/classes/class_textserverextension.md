# TextServerExtension

**Inherits:** [TextServer](class_textserver.md#class-textserver) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [TextServerAdvanced](class_textserveradvanced.md#class-textserveradvanced), [TextServerDummy](class_textserverdummy.md#class-textserverdummy), [TextServerFallback](class_textserverfallback.md#class-textserverfallback)

Base class for custom [TextServer](class_textserver.md#class-textserver) implementations (plugins).

## Description

External [TextServer](class_textserver.md#class-textserver) implementations should inherit from this class.

## Methods

|                                                                                         | \_cleanup()                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)                                                           | \_create_font()                                                                                                                                                                                                                                                                                                                                                                                                    |
| [RID](class_rid.md#class-rid)                                                           | \_create_font_linked_variation(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                           |
| [RID](class_rid.md#class-rid)                                                           | \_create_shaped_text(direction: [Direction](class_textserver.md#enum-textserver-direction), orientation: [Orientation](class_textserver.md#enum-textserver-orientation))                                                                                                                                                                                                                                    |
|                                                                                         | \_draw_hex_code_box(canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                                            |
|                                                                                         | \_font_clear_glyphs(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                             |
|                                                                                         | \_font_clear_kerning_map(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_font_clear_size_cache(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | \_font_clear_system_fallback_cache()                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | \_font_clear_textures(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                         |
|                                                                                         | \_font_draw_glyph(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float))                                                                                    |
|                                                                                         | \_font_draw_glyph_outline(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float))                       |
| [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing)                | \_font_get_antialiasing(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
| [float](class_float.md#class-float)                                                     | \_font_get_ascent(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                |
| [float](class_float.md#class-float)                                                     | \_font_get_baseline_offset(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | \_font_get_char_from_glyph_index(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)                                                     | \_font_get_descent(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | \_font_get_disable_embedded_bitmaps(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                     | \_font_get_embolden(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | \_font_get_face_count(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | \_font_get_face_index(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | \_font_get_fixed_size(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode)            | \_font_get_fixed_size_scale_mode(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | \_font_get_generate_mipmaps(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                     | \_font_get_global_oversampling()                                                                                                                                                                                                                                                                                                                                                                  |
| [Vector2](class_vector2.md#class-vector2)                                               | \_font_get_glyph_advance(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                            |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_font_get_glyph_contours(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                                           | \_font_get_glyph_index(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int))                                                                                                                                                                                                              |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_font_get_glyph_list(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                         |
| [Vector2](class_vector2.md#class-vector2)                                               | \_font_get_glyph_offset(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                               |
| [Vector2](class_vector2.md#class-vector2)                                               | \_font_get_glyph_size(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | \_font_get_glyph_texture_idx(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [RID](class_rid.md#class-rid)                                                           | \_font_get_glyph_texture_rid(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [Vector2](class_vector2.md#class-vector2)                                               | \_font_get_glyph_texture_size(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                   |
| [Rect2](class_rect2.md#class-rect2)                                                     | \_font_get_glyph_uv_rect(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                             |
| [Hinting](class_textserver.md#enum-textserver-hinting)                                  | \_font_get_hinting(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | \_font_get_keep_rounding_remainders(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [Vector2](class_vector2.md#class-vector2)                                               | \_font_get_kerning(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                    |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)]       | \_font_get_kerning_list(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | \_font_get_language_support_override(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                             |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_font_get_language_support_overrides(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | \_font_get_msdf_pixel_range(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | \_font_get_msdf_size(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
| [String](class_string.md#class-string)                                                  | \_font_get_name(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                         |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_font_get_opentype_feature_overrides(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                             |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_font_get_ot_name_strings(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [float](class_float.md#class-float)                                                     | \_font_get_oversampling(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)                    | \_font_get_palette_colors(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                           | \_font_get_palette_count(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)                    | \_font_get_palette_custom_colors(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | \_font_get_palette_name(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                   |
| [float](class_float.md#class-float)                                                     | \_font_get_scale(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | \_font_get_script_support_override(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_font_get_script_support_overrides(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_font_get_size_cache_info(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)]       | \_font_get_size_cache_list(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | \_font_get_spacing(font_rid: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype))                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                                           | \_font_get_stretch(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                   |
| [[FontStyle](class_textserver.md#enum-textserver-fontstyle)]                            | \_font_get_style(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | \_font_get_style_name(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning)          | \_font_get_subpixel_positioning(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                         |
| [String](class_string.md#class-string)                                                  | \_font_get_supported_chars(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_font_get_supported_glyphs(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | \_font_get_texture_count(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                   |
| [Image](class_image.md#class-image)                                                     | \_font_get_texture_image(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_font_get_texture_offsets(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                 |
| [Transform2D](class_transform2d.md#class-transform2d)                                   | \_font_get_transform(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                     | \_font_get_underline_position(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                                     | \_font_get_underline_thickness(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                           | \_font_get_used_palette(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_font_get_variation_coordinates(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                           | \_font_get_weight(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | \_font_has_char(font_rid: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | \_font_is_allow_system_fallback(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | \_font_is_force_autohinter(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | \_font_is_language_supported(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                        | \_font_is_modulate_color_glyphs(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | \_font_is_multichannel_signed_distance_field(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | \_font_is_script_supported(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                   |
|                                                                                         | \_font_remove_glyph(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                       |
|                                                                                         | \_font_remove_kerning(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                              |
|                                                                                         | \_font_remove_language_support_override(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                       |
|                                                                                         | \_font_remove_script_support_override(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))                                                                                                                                                                                                                                                             |
|                                                                                         | \_font_remove_size_cache(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                   |
|                                                                                         | \_font_remove_texture(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                           |
|                                                                                         | \_font_render_glyph(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                       |
|                                                                                         | \_font_render_range(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))                                                                                                                                                                                                                   |
|                                                                                         | \_font_set_allow_system_fallback(font_rid: [RID](class_rid.md#class-rid), allow_system_fallback: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                              |
|                                                                                         | \_font_set_antialiasing(font_rid: [RID](class_rid.md#class-rid), antialiasing: [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing))                                                                                                                                                                                                                                                 |
|                                                                                         | \_font_set_ascent(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                   |
|                                                                                         | \_font_set_baseline_offset(font_rid: [RID](class_rid.md#class-rid), baseline_offset: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                             |
|                                                                                         | \_font_set_data(font_rid: [RID](class_rid.md#class-rid), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                                                                                                                                |
|                                                                                         | \_font_set_data_ptr(font_rid: [RID](class_rid.md#class-rid), data_ptr: `const uint8_t*`, data_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                           |
|                                                                                         | \_font_set_descent(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                |
|                                                                                         | \_font_set_disable_embedded_bitmaps(font_rid: [RID](class_rid.md#class-rid), disable_embedded_bitmaps: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                     |
|                                                                                         | \_font_set_embolden(font_rid: [RID](class_rid.md#class-rid), strength: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_font_set_face_index(font_rid: [RID](class_rid.md#class-rid), face_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_font_set_fixed_size(font_rid: [RID](class_rid.md#class-rid), fixed_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_font_set_fixed_size_scale_mode(font_rid: [RID](class_rid.md#class-rid), fixed_size_scale_mode: [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode))                                                                                                                                                                                                                  |
|                                                                                         | \_font_set_force_autohinter(font_rid: [RID](class_rid.md#class-rid), force_autohinter: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                             |
|                                                                                         | \_font_set_generate_mipmaps(font_rid: [RID](class_rid.md#class-rid), generate_mipmaps: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                             |
|                                                                                         | \_font_set_global_oversampling(oversampling: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | \_font_set_glyph_advance(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                        |
|                                                                                         | \_font_set_glyph_offset(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                            |
|                                                                                         | \_font_set_glyph_size(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                               |
|                                                                                         | \_font_set_glyph_texture_idx(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int))                                                                                                                                                                                         |
|                                                                                         | \_font_set_glyph_uv_rect(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                               |
|                                                                                         | \_font_set_hinting(font_rid: [RID](class_rid.md#class-rid), hinting: [Hinting](class_textserver.md#enum-textserver-hinting))                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_font_set_keep_rounding_remainders(font_rid: [RID](class_rid.md#class-rid), keep_rounding_remainders: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                     |
|                                                                                         | \_font_set_kerning(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                |
|                                                                                         | \_font_set_language_support_override(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                |
|                                                                                         | \_font_set_modulate_color_glyphs(font_rid: [RID](class_rid.md#class-rid), modulate: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                           |
|                                                                                         | \_font_set_msdf_pixel_range(font_rid: [RID](class_rid.md#class-rid), msdf_pixel_range: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                |
|                                                                                         | \_font_set_msdf_size(font_rid: [RID](class_rid.md#class-rid), msdf_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                     |
|                                                                                         | \_font_set_multichannel_signed_distance_field(font_rid: [RID](class_rid.md#class-rid), msdf: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                     |
|                                                                                         | \_font_set_name(font_rid: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                           |
|                                                                                         | \_font_set_opentype_feature_overrides(font_rid: [RID](class_rid.md#class-rid), overrides: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                                                                                                                                              |
|                                                                                         | \_font_set_oversampling(font_rid: [RID](class_rid.md#class-rid), oversampling: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                      |
|                                                                                         | \_font_set_palette_custom_colors(font_rid: [RID](class_rid.md#class-rid), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))                                                                                                                                                                                                                                         |
|                                                                                         | \_font_set_scale(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                      |
|                                                                                         | \_font_set_script_support_override(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                      |
|                                                                                         | \_font_set_spacing(font_rid: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int))                                                                                                                                                                                                                                    |
|                                                                                         | \_font_set_stretch(font_rid: [RID](class_rid.md#class-rid), stretch: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                           |
|                                                                                         | \_font_set_style(font_rid: [RID](class_rid.md#class-rid), style: [[FontStyle](class_textserver.md#enum-textserver-fontstyle)])                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_font_set_style_name(font_rid: [RID](class_rid.md#class-rid), name_style: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                         |
|                                                                                         | \_font_set_subpixel_positioning(font_rid: [RID](class_rid.md#class-rid), subpixel_positioning: [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning))                                                                                                                                                                                                                   |
|                                                                                         | \_font_set_texture_image(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image))                                                                                                                                                                                         |
|                                                                                         | \_font_set_texture_offsets(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array))                                                                                                                                                   |
|                                                                                         | \_font_set_transform(font_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                             |
|                                                                                         | \_font_set_underline_position(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float))                                                                                                                                                                                                                               |
|                                                                                         | \_font_set_underline_thickness(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float))                                                                                                                                                                                                                            |
|                                                                                         | \_font_set_used_palette(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                   |
|                                                                                         | \_font_set_variation_coordinates(font_rid: [RID](class_rid.md#class-rid), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                                                                                                                                            |
|                                                                                         | \_font_set_weight(font_rid: [RID](class_rid.md#class-rid), weight: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                              |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_font_supported_feature_list(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                             |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_font_supported_variation_list(font_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                         |
| [String](class_string.md#class-string)                                                  | \_format_number(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                |
|                                                                                         | \_free_rid(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | \_get_features()                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Vector2](class_vector2.md#class-vector2)                                               | \_get_hex_code_box_size(size: [int](class_int.md#class-int), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | \_get_name()                                                                                                                                                                                                                                                                                                                                                                                                          |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)                       | \_get_support_data()                                                                                                                                                                                                                                                                                                                                                                                          |
| [String](class_string.md#class-string)                                                  | \_get_support_data_filename()                                                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | \_get_support_data_info()                                                                                                                                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                        | \_has(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | \_has_feature(feature: [Feature](class_textserver.md#enum-textserver-feature))                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | \_is_confusable(string: [String](class_string.md#class-string), dict: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | \_is_locale_right_to_left(locale: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | \_is_locale_using_support_data(locale: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | \_is_valid_identifier(string: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | \_is_valid_letter(unicode: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | \_load_support_data(filename: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | \_name_to_tag(name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | \_parse_number(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                  |
| [Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)]       | \_parse_structured_text(parser_type: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser), args: [Array](class_array.md#class-array), text: [String](class_string.md#class-string))                                                                                                                                                                                          |
| [String](class_string.md#class-string)                                                  | \_percent_sign(language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_reference_oversampling_level(oversampling: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | \_save_support_data(filename: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | \_shaped_get_run_count(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [Direction](class_textserver.md#enum-textserver-direction)                              | \_shaped_get_run_direction(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                           | \_shaped_get_run_font_rid(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | \_shaped_get_run_font_size(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                               |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | \_shaped_get_run_glyph_range(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                           |
| [String](class_string.md#class-string)                                                  | \_shaped_get_run_language(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                 |
| [Variant](class_variant.md#class-variant)                                               | \_shaped_get_run_object(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                     |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | \_shaped_get_run_range(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | \_shaped_get_run_text(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                           | \_shaped_get_span_count(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                           |
| [Variant](class_variant.md#class-variant)                                               | \_shaped_get_span_embedded_object(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                 |
| [Variant](class_variant.md#class-variant)                                               | \_shaped_get_span_meta(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                       |
| [Variant](class_variant.md#class-variant)                                               | \_shaped_get_span_object(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                   |
| [String](class_string.md#class-string)                                                  | \_shaped_get_span_text(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | \_shaped_get_text(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | \_shaped_set_span_update_font(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_add_object(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment), length: [int](class_int.md#class-int), baseline: [float](class_float.md#class-float))                                                         |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_add_string(shaped: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary), language: [String](class_string.md#class-string), meta: [Variant](class_variant.md#class-variant)) |
|                                                                                         | \_shaped_text_clear(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | \_shaped_text_closest_character_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                               |
|                                                                                         | \_shaped_text_draw(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float), clip_r: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float))                                                                     |
|                                                                                         | \_shaped_text_draw_outline(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float), clip_r: [float](class_float.md#class-float), outline_size: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float))        |
| [RID](class_rid.md#class-rid)                                                           | \_shaped_text_duplicate(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                           |
| [float](class_float.md#class-float)                                                     | \_shaped_text_fit_to_width(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])                                                                                                                                                                                      |
| [float](class_float.md#class-float)                                                     | \_shaped_text_get_ascent(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | \_shaped_text_get_carets(shaped: [RID](class_rid.md#class-rid), position: [int](class_int.md#class-int), r_caret: `CaretInfo*`)                                                                                                                                                                                                                                                                         |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_shaped_text_get_character_breaks(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | \_shaped_text_get_custom_ellipsis(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | \_shaped_text_get_custom_punctuation(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                     | \_shaped_text_get_descent(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
| [Direction](class_textserver.md#enum-textserver-direction)                              | \_shaped_text_get_direction(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | \_shaped_text_get_dominant_direction_in_range(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | \_shaped_text_get_ellipsis_glyph_count(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                             |
| `const Glyph*`                                                                          | \_shaped_text_get_ellipsis_glyphs(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                           | \_shaped_text_get_ellipsis_pos(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | \_shaped_text_get_glyph_count(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                               |
| `const Glyph*`                                                                          | \_shaped_text_get_glyphs(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
| [Vector2](class_vector2.md#class-vector2)                                               | \_shaped_text_get_grapheme_bounds(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                   |
| [Direction](class_textserver.md#enum-textserver-direction)                              | \_shaped_text_get_inferred_direction(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_shaped_text_get_line_breaks(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), start: [int](class_int.md#class-int), break_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])                                                                                                                                                          |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_shaped_text_get_line_breaks_adv(shaped: [RID](class_rid.md#class-rid), width: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), start: [int](class_int.md#class-int), once: [bool](class_bool.md#class-bool), break_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])                                                                   |
| [int](class_int.md#class-int)                                                           | \_shaped_text_get_object_glyph(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                             |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | \_shaped_text_get_object_range(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                             |
| [Rect2](class_rect2.md#class-rect2)                                                     | \_shaped_text_get_object_rect(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                               |
| [Array](class_array.md#class-array)                                                     | \_shaped_text_get_objects(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
| [Orientation](class_textserver.md#enum-textserver-orientation)                          | \_shaped_text_get_orientation(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                           | \_shaped_text_get_parent(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_get_preserve_control(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_get_preserve_invalid(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                     |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | \_shaped_text_get_range(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                           |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)              | \_shaped_text_get_selection(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))                                                                                                                                                                                                                                                         |
| [Vector2](class_vector2.md#class-vector2)                                               | \_shaped_text_get_size(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | \_shaped_text_get_spacing(shaped: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype))                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | \_shaped_text_get_trim_pos(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                     |
| [float](class_float.md#class-float)                                                     | \_shaped_text_get_underline_position(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                     | \_shaped_text_get_underline_thickness(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                     | \_shaped_text_get_width(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                           |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_shaped_text_get_word_breaks(shaped: [RID](class_rid.md#class-rid), grapheme_flags: [[GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag)], skip_grapheme_flags: [[GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag)])                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_has_object(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                           | \_shaped_text_hit_test_grapheme(shaped: [RID](class_rid.md#class-rid), coord: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                           | \_shaped_text_hit_test_position(shaped: [RID](class_rid.md#class-rid), coord: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_is_ready(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | \_shaped_text_next_character_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | \_shaped_text_next_grapheme_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                       |
|                                                                                         | \_shaped_text_overrun_trim_to_width(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), trim_flags: [[TextOverrunFlag](class_textserver.md#enum-textserver-textoverrunflag)])                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | \_shaped_text_prev_character_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | \_shaped_text_prev_grapheme_pos(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_resize_object(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment), baseline: [float](class_float.md#class-float))                                                                                          |
|                                                                                         | \_shaped_text_set_bidi_override(shaped: [RID](class_rid.md#class-rid), override: [Array](class_array.md#class-array))                                                                                                                                                                                                                                                                            |
|                                                                                         | \_shaped_text_set_custom_ellipsis(shaped: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_shaped_text_set_custom_punctuation(shaped: [RID](class_rid.md#class-rid), punct: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                  |
|                                                                                         | \_shaped_text_set_direction(shaped: [RID](class_rid.md#class-rid), direction: [Direction](class_textserver.md#enum-textserver-direction))                                                                                                                                                                                                                                                            |
|                                                                                         | \_shaped_text_set_orientation(shaped: [RID](class_rid.md#class-rid), orientation: [Orientation](class_textserver.md#enum-textserver-orientation))                                                                                                                                                                                                                                                  |
|                                                                                         | \_shaped_text_set_preserve_control(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                          |
|                                                                                         | \_shaped_text_set_preserve_invalid(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                          |
|                                                                                         | \_shaped_text_set_spacing(shaped: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int))                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_shape(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                   |
| `const Glyph*`                                                                          | \_shaped_text_sort_logical(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                     |
| [RID](class_rid.md#class-rid)                                                           | \_shaped_text_substr(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), length: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                    |
| [float](class_float.md#class-float)                                                     | \_shaped_text_tab_align(shaped: [RID](class_rid.md#class-rid), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_update_breaks(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | \_shaped_text_update_justification_ops(shaped: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                        | \_spoof_check(string: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                      |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_string_get_character_breaks(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                    |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | \_string_get_word_breaks(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string), chars_per_line: [int](class_int.md#class-int))                                                                                                                                                                                                                               |
| [String](class_string.md#class-string)                                                  | \_string_to_lower(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)                                                  | \_string_to_title(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)                                                  | \_string_to_upper(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)                                                  | \_strip_diacritics(string: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)                                                  | \_tag_to_name(tag: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_unreference_oversampling_level(oversampling: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                             |

---

## Method Descriptions

 **\_cleanup**()

This method is called before text server is unregistered.

---

[RID](class_rid.md#class-rid) **\_create_font**()

Creates a new, empty font cache entry resource.

---

[RID](class_rid.md#class-rid) **\_create_font_linked_variation**(font_rid: [RID](class_rid.md#class-rid))

Optional, implement if font supports extra spacing or baseline offset.

Creates a new variation existing font which is reusing the same glyph cache and font data.

---

[RID](class_rid.md#class-rid) **\_create_shaped_text**(direction: [Direction](class_textserver.md#enum-textserver-direction), orientation: [Orientation](class_textserver.md#enum-textserver-orientation))

Creates a new buffer for complex text layout, with the given `direction` and `orientation`.

---

 **\_draw_hex_code_box**(canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Draws box displaying character hexadecimal code.

---

 **\_font_clear_glyphs**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes all rendered glyph information from the cache entry.

---

 **\_font_clear_kerning_map**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Removes all kerning overrides.

---

 **\_font_clear_size_cache**(font_rid: [RID](class_rid.md#class-rid))

Removes all font sizes from the cache entry.

---

 **\_font_clear_system_fallback_cache**()

Frees all automatically loaded system fonts.

---

 **\_font_clear_textures**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes all textures from font cache entry.

---

 **\_font_draw_glyph**(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float))

Draws single glyph into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

 **\_font_draw_glyph_outline**(font_rid: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), outline_size: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float))

Draws single glyph outline of size `outline_size` into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

[FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) **\_font_get_antialiasing**(font_rid: [RID](class_rid.md#class-rid))

Returns font anti-aliasing mode.

---

[float](class_float.md#class-float) **\_font_get_ascent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns the font ascent (number of pixels above the baseline).

---

[float](class_float.md#class-float) **\_font_get_baseline_offset**(font_rid: [RID](class_rid.md#class-rid))

Returns extra baseline offset (as a fraction of font height).

---

[int](class_int.md#class-int) **\_font_get_char_from_glyph_index**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int))

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid.

---

[float](class_float.md#class-float) **\_font_get_descent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns the font descent (number of pixels below the baseline).

---

[bool](class_bool.md#class-bool) **\_font_get_disable_embedded_bitmaps**(font_rid: [RID](class_rid.md#class-rid))

Returns whether the font's embedded bitmap loading is disabled.

---

[float](class_float.md#class-float) **\_font_get_embolden**(font_rid: [RID](class_rid.md#class-rid))

Returns font embolden strength.

---

[int](class_int.md#class-int) **\_font_get_face_count**(font_rid: [RID](class_rid.md#class-rid))

Returns number of faces in the TrueType / OpenType collection.

---

[int](class_int.md#class-int) **\_font_get_face_index**(font_rid: [RID](class_rid.md#class-rid))

Returns an active face index in the TrueType / OpenType collection.

---

[int](class_int.md#class-int) **\_font_get_fixed_size**(font_rid: [RID](class_rid.md#class-rid))

Returns bitmap font fixed size.

---

[FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode) **\_font_get_fixed_size_scale_mode**(font_rid: [RID](class_rid.md#class-rid))

Returns bitmap font scaling mode.

---

[bool](class_bool.md#class-bool) **\_font_get_generate_mipmaps**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if font texture mipmap generation is enabled.

---

[float](class_float.md#class-float) **\_font_get_global_oversampling**()

Returns the font oversampling factor, shared by all fonts in the TextServer.

---

[Vector2](class_vector2.md#class-vector2) **\_font_get_glyph_advance**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int))

Returns glyph advance (offset of the next glyph).

---

[Dictionary](class_dictionary.md#class-dictionary) **\_font_get_glyph_contours**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), index: [int](class_int.md#class-int))

Returns outline contours of the glyph.

---

[int](class_int.md#class-int) **\_font_get_glyph_index**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int))

Returns the glyph index of a `char`, optionally modified by the `variation_selector`.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_font_get_glyph_list**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Returns list of rendered glyphs in the cache entry.

---

[Vector2](class_vector2.md#class-vector2) **\_font_get_glyph_offset**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns glyph offset from the baseline.

---

[Vector2](class_vector2.md#class-vector2) **\_font_get_glyph_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns size of the glyph.

---

[int](class_int.md#class-int) **\_font_get_glyph_texture_idx**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns index of the cache texture containing the glyph.

---

[RID](class_rid.md#class-rid) **\_font_get_glyph_texture_rid**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns resource ID of the cache texture containing the glyph.

---

[Vector2](class_vector2.md#class-vector2) **\_font_get_glyph_texture_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns size of the cache texture containing the glyph.

---

[Rect2](class_rect2.md#class-rect2) **\_font_get_glyph_uv_rect**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns rectangle in the cache texture containing the glyph.

---

[Hinting](class_textserver.md#enum-textserver-hinting) **\_font_get_hinting**(font_rid: [RID](class_rid.md#class-rid))

Returns the font hinting mode. Used by dynamic fonts only.

---

[bool](class_bool.md#class-bool) **\_font_get_keep_rounding_remainders**(font_rid: [RID](class_rid.md#class-rid))

Returns glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

[Vector2](class_vector2.md#class-vector2) **\_font_get_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))

Returns kerning for the pair of glyphs.

---

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **\_font_get_kerning_list**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns list of the kerning overrides.

---

[bool](class_bool.md#class-bool) **\_font_get_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))

Returns `true` if support override is enabled for the `language`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_font_get_language_support_overrides**(font_rid: [RID](class_rid.md#class-rid))

Returns list of language support overrides.

---

[int](class_int.md#class-int) **\_font_get_msdf_pixel_range**(font_rid: [RID](class_rid.md#class-rid))

Returns the width of the range around the shape between the minimum and maximum representable signed distance.

---

[int](class_int.md#class-int) **\_font_get_msdf_size**(font_rid: [RID](class_rid.md#class-rid))

Returns source font size used to generate MSDF textures.

---

[String](class_string.md#class-string) **\_font_get_name**(font_rid: [RID](class_rid.md#class-rid))

Returns font family name.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_font_get_opentype_feature_overrides**(font_rid: [RID](class_rid.md#class-rid))

Returns font OpenType feature set override.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_font_get_ot_name_strings**(font_rid: [RID](class_rid.md#class-rid))

Returns [Dictionary](class_dictionary.md#class-dictionary) with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

---

[float](class_float.md#class-float) **\_font_get_oversampling**(font_rid: [RID](class_rid.md#class-rid))

Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **\_font_get_palette_colors**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the array in the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors. Colors can be overridden using \_font_set_palette_custom_colors().

---

[int](class_int.md#class-int) **\_font_get_palette_count**(font_rid: [RID](class_rid.md#class-rid))

Returns the number of predefined color palettes. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **\_font_get_palette_custom_colors**(font_rid: [RID](class_rid.md#class-rid))

Returns array of custom colors to override predefined palette.

---

[String](class_string.md#class-string) **\_font_get_palette_name**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the name of the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

---

[float](class_float.md#class-float) **\_font_get_scale**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns scaling factor of the color bitmap font.

---

[bool](class_bool.md#class-bool) **\_font_get_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))

Returns `true` if support override is enabled for the `script`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_font_get_script_support_overrides**(font_rid: [RID](class_rid.md#class-rid))

Returns list of script support overrides.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_font_get_size_cache_info**(font_rid: [RID](class_rid.md#class-rid))

Returns font cache information, each entry contains the following fields: `Vector2i size_px` - font size in pixels, `float viewport_oversampling` - viewport oversampling factor, `int glyphs` - number of rendered glyphs, `int textures` - number of used textures, `int textures_size` - size of texture data in bytes.

---

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **\_font_get_size_cache_list**(font_rid: [RID](class_rid.md#class-rid))

Returns list of the font sizes in the cache. Each size is [Vector2i](class_vector2i.md#class-vector2i) with font size and outline size.

---

[int](class_int.md#class-int) **\_font_get_spacing**(font_rid: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype))

Returns the spacing for `spacing` in pixels (not relative to the font size).

---

[int](class_int.md#class-int) **\_font_get_stretch**(font_rid: [RID](class_rid.md#class-rid))

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] **\_font_get_style**(font_rid: [RID](class_rid.md#class-rid))

Returns font style flags.

---

[String](class_string.md#class-string) **\_font_get_style_name**(font_rid: [RID](class_rid.md#class-rid))

Returns font style name.

---

[SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **\_font_get_subpixel_positioning**(font_rid: [RID](class_rid.md#class-rid))

Returns font subpixel glyph positioning mode.

---

[String](class_string.md#class-string) **\_font_get_supported_chars**(font_rid: [RID](class_rid.md#class-rid))

Returns a string containing all the characters available in the font.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_font_get_supported_glyphs**(font_rid: [RID](class_rid.md#class-rid))

Returns an array containing all glyph indices in the font.

---

[int](class_int.md#class-int) **\_font_get_texture_count**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Returns number of textures used by font cache entry.

---

[Image](class_image.md#class-image) **\_font_get_texture_image**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Returns font cache texture image data.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_font_get_texture_offsets**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Returns array containing glyph packing data.

---

[Transform2D](class_transform2d.md#class-transform2d) **\_font_get_transform**(font_rid: [RID](class_rid.md#class-rid))

Returns 2D transform applied to the font outlines.

---

[float](class_float.md#class-float) **\_font_get_underline_position**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns pixel offset of the underline below the baseline.

---

[float](class_float.md#class-float) **\_font_get_underline_thickness**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Returns thickness of the underline in pixels.

---

[int](class_int.md#class-int) **\_font_get_used_palette**(font_rid: [RID](class_rid.md#class-rid))

Returns used palette index.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_font_get_variation_coordinates**(font_rid: [RID](class_rid.md#class-rid))

Returns variation coordinates for the specified font cache entry.

---

[int](class_int.md#class-int) **\_font_get_weight**(font_rid: [RID](class_rid.md#class-rid))

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

[bool](class_bool.md#class-bool) **\_font_has_char**(font_rid: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int))

Returns `true` if a Unicode `char` is available in the font.

---

[bool](class_bool.md#class-bool) **\_font_is_allow_system_fallback**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if system fonts can be automatically used as fallbacks.

---

[bool](class_bool.md#class-bool) **\_font_is_force_autohinter**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if auto-hinting is supported and preferred over font built-in hinting.

---

[bool](class_bool.md#class-bool) **\_font_is_language_supported**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))

Returns `true` if the font supports the given language (as a [ISO 639](https://en.wikipedia.org/wiki/ISO_639-1) code).

---

[bool](class_bool.md#class-bool) **\_font_is_modulate_color_glyphs**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if color modulation is applied when drawing the font's colored glyphs.

---

[bool](class_bool.md#class-bool) **\_font_is_multichannel_signed_distance_field**(font_rid: [RID](class_rid.md#class-rid))

Returns `true` if glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

---

[bool](class_bool.md#class-bool) **\_font_is_script_supported**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))

Returns `true` if the font supports the given script (as a [ISO 15924](https://en.wikipedia.org/wiki/ISO_15924) code).

---

 **\_font_remove_glyph**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Removes specified rendered glyph information from the cache entry.

---

 **\_font_remove_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))

Removes kerning override for the pair of glyphs.

---

 **\_font_remove_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))

Remove language support override.

---

 **\_font_remove_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string))

Removes script support override.

---

 **\_font_remove_size_cache**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes specified font size from the cache entry.

---

 **\_font_remove_texture**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Removes specified texture from the cache entry.

---

 **\_font_render_glyph**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int))

Renders specified glyph to the font cache texture.

---

 **\_font_render_range**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))

Renders the range of characters to the font cache texture.

---

 **\_font_set_allow_system_fallback**(font_rid: [RID](class_rid.md#class-rid), allow_system_fallback: [bool](class_bool.md#class-bool))

If set to `true`, system fonts can be automatically used as fallbacks.

---

 **\_font_set_antialiasing**(font_rid: [RID](class_rid.md#class-rid), antialiasing: [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing))

Sets font anti-aliasing mode.

---

 **\_font_set_ascent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float))

Sets the font ascent (number of pixels above the baseline).

---

 **\_font_set_baseline_offset**(font_rid: [RID](class_rid.md#class-rid), baseline_offset: [float](class_float.md#class-float))

Sets extra baseline offset (as a fraction of font height).

---

 **\_font_set_data**(font_rid: [RID](class_rid.md#class-rid), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Sets font source data, e.g contents of the dynamic font source file.

---

 **\_font_set_data_ptr**(font_rid: [RID](class_rid.md#class-rid), data_ptr: `const uint8_t*`, data_size: [int](class_int.md#class-int))

Sets pointer to the font source data, e.g contents of the dynamic font source file.

---

 **\_font_set_descent**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float))

Sets the font descent (number of pixels below the baseline).

---

 **\_font_set_disable_embedded_bitmaps**(font_rid: [RID](class_rid.md#class-rid), disable_embedded_bitmaps: [bool](class_bool.md#class-bool))

If set to `true`, embedded font bitmap loading is disabled.

---

 **\_font_set_embolden**(font_rid: [RID](class_rid.md#class-rid), strength: [float](class_float.md#class-float))

Sets font embolden strength. If `strength` is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---

 **\_font_set_face_index**(font_rid: [RID](class_rid.md#class-rid), face_index: [int](class_int.md#class-int))

Sets an active face index in the TrueType / OpenType collection.

---

 **\_font_set_fixed_size**(font_rid: [RID](class_rid.md#class-rid), fixed_size: [int](class_int.md#class-int))

Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.

---

 **\_font_set_fixed_size_scale_mode**(font_rid: [RID](class_rid.md#class-rid), fixed_size_scale_mode: [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode))

Sets bitmap font scaling mode. This property is used only if `fixed_size` is greater than zero.

---

 **\_font_set_force_autohinter**(font_rid: [RID](class_rid.md#class-rid), force_autohinter: [bool](class_bool.md#class-bool))

If set to `true` auto-hinting is preferred over font built-in hinting.

---

 **\_font_set_generate_mipmaps**(font_rid: [RID](class_rid.md#class-rid), generate_mipmaps: [bool](class_bool.md#class-bool))

If set to `true` font texture mipmap generation is enabled.

---

 **\_font_set_global_oversampling**(oversampling: [float](class_float.md#class-float))

Sets oversampling factor, shared by all font in the TextServer.

---

 **\_font_set_glyph_advance**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2))

Sets glyph advance (offset of the next glyph).

---

 **\_font_set_glyph_offset**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2))

Sets glyph offset from the baseline.

---

 **\_font_set_glyph_size**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2))

Sets size of the glyph.

---

 **\_font_set_glyph_texture_idx**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int))

Sets index of the cache texture containing the glyph.

---

 **\_font_set_glyph_uv_rect**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2))

Sets rectangle in the cache texture containing the glyph.

---

 **\_font_set_hinting**(font_rid: [RID](class_rid.md#class-rid), hinting: [Hinting](class_textserver.md#enum-textserver-hinting))

Sets font hinting mode. Used by dynamic fonts only.

---

 **\_font_set_keep_rounding_remainders**(font_rid: [RID](class_rid.md#class-rid), keep_rounding_remainders: [bool](class_bool.md#class-bool))

Sets glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

 **\_font_set_kerning**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2))

Sets kerning for the pair of glyphs.

---

 **\_font_set_language_support_override**(font_rid: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))

Adds override for \_font_is_language_supported().

---

 **\_font_set_modulate_color_glyphs**(font_rid: [RID](class_rid.md#class-rid), modulate: [bool](class_bool.md#class-bool))

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---

 **\_font_set_msdf_pixel_range**(font_rid: [RID](class_rid.md#class-rid), msdf_pixel_range: [int](class_int.md#class-int))

Sets the width of the range around the shape between the minimum and maximum representable signed distance.

---

 **\_font_set_msdf_size**(font_rid: [RID](class_rid.md#class-rid), msdf_size: [int](class_int.md#class-int))

Sets source font size used to generate MSDF textures.

---

 **\_font_set_multichannel_signed_distance_field**(font_rid: [RID](class_rid.md#class-rid), msdf: [bool](class_bool.md#class-bool))

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

---

 **\_font_set_name**(font_rid: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))

Sets the font family name.

---

 **\_font_set_opentype_feature_overrides**(font_rid: [RID](class_rid.md#class-rid), overrides: [Dictionary](class_dictionary.md#class-dictionary))

Sets font OpenType feature set override.

---

 **\_font_set_oversampling**(font_rid: [RID](class_rid.md#class-rid), oversampling: [float](class_float.md#class-float))

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

---

 **\_font_set_palette_custom_colors**(font_rid: [RID](class_rid.md#class-rid), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))

Sets array of custom colors to override predefined palette. Set to empty array to reset overrides. Use `Color(0, 0, 0, 0)`, to keep predefined palette color at specific position.

---

 **\_font_set_scale**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float))

Sets scaling factor of the color bitmap font.

---

 **\_font_set_script_support_override**(font_rid: [RID](class_rid.md#class-rid), script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))

Adds override for \_font_is_script_supported().

---

 **\_font_set_spacing**(font_rid: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int))

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

---

 **\_font_set_stretch**(font_rid: [RID](class_rid.md#class-rid), stretch: [int](class_int.md#class-int))

Sets font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

 **\_font_set_style**(font_rid: [RID](class_rid.md#class-rid), style: [[FontStyle](class_textserver.md#enum-textserver-fontstyle)])

Sets the font style flags.

---

 **\_font_set_style_name**(font_rid: [RID](class_rid.md#class-rid), name_style: [String](class_string.md#class-string))

Sets the font style name.

---

 **\_font_set_subpixel_positioning**(font_rid: [RID](class_rid.md#class-rid), subpixel_positioning: [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning))

Sets font subpixel glyph positioning mode.

---

 **\_font_set_texture_image**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image))

Sets font cache texture image data.

---

 **\_font_set_texture_offsets**(font_rid: [RID](class_rid.md#class-rid), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Sets array containing glyph packing data.

---

 **\_font_set_transform**(font_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

---

 **\_font_set_underline_position**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float))

Sets pixel offset of the underline below the baseline.

---

 **\_font_set_underline_thickness**(font_rid: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float))

Sets thickness of the underline in pixels.

---

 **\_font_set_used_palette**(font_rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Sets used palette index.

---

 **\_font_set_variation_coordinates**(font_rid: [RID](class_rid.md#class-rid), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary))

Sets variation coordinates for the specified font cache entry.

---

 **\_font_set_weight**(font_rid: [RID](class_rid.md#class-rid), weight: [int](class_int.md#class-int))

Sets weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_font_supported_feature_list**(font_rid: [RID](class_rid.md#class-rid))

Returns the dictionary of the supported OpenType features.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_font_supported_variation_list**(font_rid: [RID](class_rid.md#class-rid))

Returns the dictionary of the supported OpenType variation coordinates.

---

[String](class_string.md#class-string) **\_format_number**(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string))

**Deprecated:** Use [TranslationServer.format_number()](class_translationserver.md#class-translationserver-method-format-number) instead.

Converts a number from Western Arabic (0..9) to the numeral system used in the given `language`.

If `language` is an empty string, the active locale will be used.

---

 **\_free_rid**(rid: [RID](class_rid.md#class-rid))

Frees an object created by this [TextServer](class_textserver.md#class-textserver).

---

[int](class_int.md#class-int) **\_get_features**()

Returns text server features, see [Feature](class_textserver.md#enum-textserver-feature).

---

[Vector2](class_vector2.md#class-vector2) **\_get_hex_code_box_size**(size: [int](class_int.md#class-int), index: [int](class_int.md#class-int))

Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).

---

[String](class_string.md#class-string) **\_get_name**()

Returns the name of the server interface.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **\_get_support_data**()

Returns default TextServer database (e.g. ICU break iterators and dictionaries).

---

[String](class_string.md#class-string) **\_get_support_data_filename**()

Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.

---

[String](class_string.md#class-string) **\_get_support_data_info**()

Returns TextServer database (e.g. ICU break iterators and dictionaries) description.

---

[bool](class_bool.md#class-bool) **\_has**(rid: [RID](class_rid.md#class-rid))

Returns `true` if `rid` is valid resource owned by this text server.

---

[bool](class_bool.md#class-bool) **\_has_feature**(feature: [Feature](class_textserver.md#enum-textserver-feature))

Returns `true` if the server supports a feature.

---

[int](class_int.md#class-int) **\_is_confusable**(string: [String](class_string.md#class-string), dict: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Returns index of the first string in `dict` which is visually confusable with the `string`, or `-1` if none is found.

---

[bool](class_bool.md#class-bool) **\_is_locale_right_to_left**(locale: [String](class_string.md#class-string))

Returns `true` if locale is right-to-left.

---

[bool](class_bool.md#class-bool) **\_is_locale_using_support_data**(locale: [String](class_string.md#class-string))

Returns `true` if the locale requires text server support data for line/word breaking.

---

[bool](class_bool.md#class-bool) **\_is_valid_identifier**(string: [String](class_string.md#class-string))

Returns `true` if `string` is a valid identifier.

---

[bool](class_bool.md#class-bool) **\_is_valid_letter**(unicode: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_load_support_data**(filename: [String](class_string.md#class-string))

Loads optional TextServer database (e.g. ICU break iterators and dictionaries).

---

[int](class_int.md#class-int) **\_name_to_tag**(name: [String](class_string.md#class-string))

Converts the given readable name of a feature, variation, script, or language to an OpenType tag.

---

[String](class_string.md#class-string) **\_parse_number**(number: [String](class_string.md#class-string), language: [String](class_string.md#class-string))

**Deprecated:** Use [TranslationServer.parse_number()](class_translationserver.md#class-translationserver-method-parse-number) instead.

Converts `number` from the numeral system used in the given `language` to Western Arabic (0..9).

If `language` is an empty string, the active locale will be used.

---

[Array](class_array.md#class-array)[[Vector3i](class_vector3i.md#class-vector3i)] **\_parse_structured_text**(parser_type: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser), args: [Array](class_array.md#class-array), text: [String](class_string.md#class-string))

Default implementation of the BiDi algorithm override function.

---

[String](class_string.md#class-string) **\_percent_sign**(language: [String](class_string.md#class-string))

**Deprecated:** Use [TranslationServer.get_percent_sign()](class_translationserver.md#class-translationserver-method-get-percent-sign) instead.

Returns percent sign used in the given `language`.

---

 **\_reference_oversampling_level**(oversampling: [float](class_float.md#class-float))

Increases the reference count of the specified oversampling level. This method is called by [Viewport](class_viewport.md#class-viewport), and should not be used directly.

---

[bool](class_bool.md#class-bool) **\_save_support_data**(filename: [String](class_string.md#class-string))

Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.

---

[int](class_int.md#class-int) **\_shaped_get_run_count**(shaped: [RID](class_rid.md#class-rid))

Returns the number of uniform text runs in the buffer.

---

[Direction](class_textserver.md#enum-textserver-direction) **\_shaped_get_run_direction**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the direction of the `index` text run (in visual order).

---

[RID](class_rid.md#class-rid) **\_shaped_get_run_font_rid**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the font RID of the `index` text run (in visual order).

---

[int](class_int.md#class-int) **\_shaped_get_run_font_size**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the font size of the `index` text run (in visual order).

---

[Vector2i](class_vector2i.md#class-vector2i) **\_shaped_get_run_glyph_range**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the glyph range of the `index` text run (in visual order).

---

[String](class_string.md#class-string) **\_shaped_get_run_language**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the language of the `index` text run (in visual order).

---

[Variant](class_variant.md#class-variant) **\_shaped_get_run_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the embedded object of the `index` text run (in visual order).

---

[Vector2i](class_vector2i.md#class-vector2i) **\_shaped_get_run_range**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the source text range of the `index` text run (in visual order).

---

[String](class_string.md#class-string) **\_shaped_get_run_text**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the source text of the `index` text run (in visual order).

---

[int](class_int.md#class-int) **\_shaped_get_span_count**(shaped: [RID](class_rid.md#class-rid))

Returns number of text spans added using \_shaped_text_add_string() or \_shaped_text_add_object().

---

[Variant](class_variant.md#class-variant) **\_shaped_get_span_embedded_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns text embedded object key.

---

[Variant](class_variant.md#class-variant) **\_shaped_get_span_meta**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns text span metadata.

---

[Variant](class_variant.md#class-variant) **\_shaped_get_span_object**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the text span embedded object key.

---

[String](class_string.md#class-string) **\_shaped_get_span_text**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the text span source text.

---

[String](class_string.md#class-string) **\_shaped_get_text**(shaped: [RID](class_rid.md#class-rid))

Returns the text buffer source text, including object replacement characters.

---

 **\_shaped_set_span_update_font**(shaped: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary))

Changes text span font, font size, and OpenType features, without changing the text.

---

[bool](class_bool.md#class-bool) **\_shaped_text_add_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment), length: [int](class_int.md#class-int), baseline: [float](class_float.md#class-float))

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

---

[bool](class_bool.md#class-bool) **\_shaped_text_add_string**(shaped: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string), fonts: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], size: [int](class_int.md#class-int), opentype_features: [Dictionary](class_dictionary.md#class-dictionary), language: [String](class_string.md#class-string), meta: [Variant](class_variant.md#class-variant))

Adds text span and font to draw it to the text buffer.

---

 **\_shaped_text_clear**(shaped: [RID](class_rid.md#class-rid))

Clears text buffer (removes text and inline objects).

---

[int](class_int.md#class-int) **\_shaped_text_closest_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns composite character position closest to the `pos`.

---

 **\_shaped_text_draw**(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float), clip_r: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float))

Draw shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

 **\_shaped_text_draw_outline**(shaped: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), clip_l: [float](class_float.md#class-float), clip_r: [float](class_float.md#class-float), outline_size: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), oversampling: [float](class_float.md#class-float))

Draw the outline of the shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

---

[RID](class_rid.md#class-rid) **\_shaped_text_duplicate**(shaped: [RID](class_rid.md#class-rid))

Duplicates shaped text buffer.

---

[float](class_float.md#class-float) **\_shaped_text_fit_to_width**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])

Adjusts text width to fit to specified width, returns new text width.

---

[float](class_float.md#class-float) **\_shaped_text_get_ascent**(shaped: [RID](class_rid.md#class-rid))

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

---

 **\_shaped_text_get_carets**(shaped: [RID](class_rid.md#class-rid), position: [int](class_int.md#class-int), r_caret: `CaretInfo*`)

Returns shapes of the carets corresponding to the character offset `position` in the text. Returned caret shape is 1 pixel wide rectangle.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_shaped_text_get_character_breaks**(shaped: [RID](class_rid.md#class-rid))

Returns array of the composite character boundaries.

---

[int](class_int.md#class-int) **\_shaped_text_get_custom_ellipsis**(shaped: [RID](class_rid.md#class-rid))

Returns ellipsis character used for text clipping.

---

[String](class_string.md#class-string) **\_shaped_text_get_custom_punctuation**(shaped: [RID](class_rid.md#class-rid))

Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

[float](class_float.md#class-float) **\_shaped_text_get_descent**(shaped: [RID](class_rid.md#class-rid))

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

---

[Direction](class_textserver.md#enum-textserver-direction) **\_shaped_text_get_direction**(shaped: [RID](class_rid.md#class-rid))

Returns direction of the text.

---

[int](class_int.md#class-int) **\_shaped_text_get_dominant_direction_in_range**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))

Returns dominant direction of in the range of text.

---

[int](class_int.md#class-int) **\_shaped_text_get_ellipsis_glyph_count**(shaped: [RID](class_rid.md#class-rid))

Returns number of glyphs in the ellipsis.

---

`const Glyph*` **\_shaped_text_get_ellipsis_glyphs**(shaped: [RID](class_rid.md#class-rid))

Returns array of the glyphs in the ellipsis.

---

[int](class_int.md#class-int) **\_shaped_text_get_ellipsis_pos**(shaped: [RID](class_rid.md#class-rid))

Returns position of the ellipsis.

---

[int](class_int.md#class-int) **\_shaped_text_get_glyph_count**(shaped: [RID](class_rid.md#class-rid))

Returns number of glyphs in the buffer.

---

`const Glyph*` **\_shaped_text_get_glyphs**(shaped: [RID](class_rid.md#class-rid))

Returns an array of glyphs in the visual order.

---

[Vector2](class_vector2.md#class-vector2) **\_shaped_text_get_grapheme_bounds**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns composite character's bounds as offsets from the start of the line.

---

[Direction](class_textserver.md#enum-textserver-direction) **\_shaped_text_get_inferred_direction**(shaped: [RID](class_rid.md#class-rid))

Returns direction of the text, inferred by the BiDi algorithm.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_shaped_text_get_line_breaks**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), start: [int](class_int.md#class-int), break_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])

Breaks text to the lines and returns character ranges for each line.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_shaped_text_get_line_breaks_adv**(shaped: [RID](class_rid.md#class-rid), width: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), start: [int](class_int.md#class-int), once: [bool](class_bool.md#class-bool), break_flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])

Breaks text to the lines and columns. Returns character ranges for each segment.

---

[int](class_int.md#class-int) **\_shaped_text_get_object_glyph**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))

Returns the glyph index of the inline object.

---

[Vector2i](class_vector2i.md#class-vector2i) **\_shaped_text_get_object_range**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))

Returns the character range of the inline object.

---

[Rect2](class_rect2.md#class-rect2) **\_shaped_text_get_object_rect**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))

Returns bounding rectangle of the inline object.

---

[Array](class_array.md#class-array) **\_shaped_text_get_objects**(shaped: [RID](class_rid.md#class-rid))

Returns array of inline objects.

---

[Orientation](class_textserver.md#enum-textserver-orientation) **\_shaped_text_get_orientation**(shaped: [RID](class_rid.md#class-rid))

Returns text orientation.

---

[RID](class_rid.md#class-rid) **\_shaped_text_get_parent**(shaped: [RID](class_rid.md#class-rid))

Returns the parent buffer from which the substring originates.

---

[bool](class_bool.md#class-bool) **\_shaped_text_get_preserve_control**(shaped: [RID](class_rid.md#class-rid))

Returns `true` if text buffer is configured to display control characters.

---

[bool](class_bool.md#class-bool) **\_shaped_text_get_preserve_invalid**(shaped: [RID](class_rid.md#class-rid))

Returns `true` if text buffer is configured to display hexadecimal codes in place of invalid characters.

---

[Vector2i](class_vector2i.md#class-vector2i) **\_shaped_text_get_range**(shaped: [RID](class_rid.md#class-rid))

Returns substring buffer character range in the parent buffer.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **\_shaped_text_get_selection**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))

Returns selection rectangles for the specified character range.

---

[Vector2](class_vector2.md#class-vector2) **\_shaped_text_get_size**(shaped: [RID](class_rid.md#class-rid))

Returns size of the text.

---

[int](class_int.md#class-int) **\_shaped_text_get_spacing**(shaped: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype))

Returns extra spacing added between glyphs or lines in pixels.

---

[int](class_int.md#class-int) **\_shaped_text_get_trim_pos**(shaped: [RID](class_rid.md#class-rid))

Returns the position of the overrun trim.

---

[float](class_float.md#class-float) **\_shaped_text_get_underline_position**(shaped: [RID](class_rid.md#class-rid))

Returns pixel offset of the underline below the baseline.

---

[float](class_float.md#class-float) **\_shaped_text_get_underline_thickness**(shaped: [RID](class_rid.md#class-rid))

Returns thickness of the underline.

---

[float](class_float.md#class-float) **\_shaped_text_get_width**(shaped: [RID](class_rid.md#class-rid))

Returns width (for horizontal layout) or height (for vertical) of the text.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_shaped_text_get_word_breaks**(shaped: [RID](class_rid.md#class-rid), grapheme_flags: [[GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag)], skip_grapheme_flags: [[GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag)])

Breaks text into words and returns array of character ranges. Use `grapheme_flags` to set what characters are used for breaking.

---

[bool](class_bool.md#class-bool) **\_shaped_text_has_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant))

Returns `true` if an object with `key` is embedded in this shaped text buffer.

---

[int](class_int.md#class-int) **\_shaped_text_hit_test_grapheme**(shaped: [RID](class_rid.md#class-rid), coord: [float](class_float.md#class-float))

Returns grapheme index at the specified pixel offset at the baseline, or `-1` if none is found.

---

[int](class_int.md#class-int) **\_shaped_text_hit_test_position**(shaped: [RID](class_rid.md#class-rid), coord: [float](class_float.md#class-float))

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

---

[bool](class_bool.md#class-bool) **\_shaped_text_is_ready**(shaped: [RID](class_rid.md#class-rid))

Returns `true` if buffer is successfully shaped.

---

[int](class_int.md#class-int) **\_shaped_text_next_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns composite character end position closest to the `pos`.

---

[int](class_int.md#class-int) **\_shaped_text_next_grapheme_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns grapheme end position closest to the `pos`.

---

 **\_shaped_text_overrun_trim_to_width**(shaped: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float), trim_flags: [[TextOverrunFlag](class_textserver.md#enum-textserver-textoverrunflag)])

Trims text if it exceeds the given width.

---

[int](class_int.md#class-int) **\_shaped_text_prev_character_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns composite character start position closest to the `pos`.

---

[int](class_int.md#class-int) **\_shaped_text_prev_grapheme_pos**(shaped: [RID](class_rid.md#class-rid), pos: [int](class_int.md#class-int))

Returns grapheme start position closest to the `pos`.

---

[bool](class_bool.md#class-bool) **\_shaped_text_resize_object**(shaped: [RID](class_rid.md#class-rid), key: [Variant](class_variant.md#class-variant), size: [Vector2](class_vector2.md#class-vector2), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment), baseline: [float](class_float.md#class-float))

Sets new size and alignment of embedded object.

---

 **\_shaped_text_set_bidi_override**(shaped: [RID](class_rid.md#class-rid), override: [Array](class_array.md#class-array))

Overrides BiDi for the structured text.

---

 **\_shaped_text_set_custom_ellipsis**(shaped: [RID](class_rid.md#class-rid), char: [int](class_int.md#class-int))

Sets ellipsis character used for text clipping.

---

 **\_shaped_text_set_custom_punctuation**(shaped: [RID](class_rid.md#class-rid), punct: [String](class_string.md#class-string))

Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

---

 **\_shaped_text_set_direction**(shaped: [RID](class_rid.md#class-rid), direction: [Direction](class_textserver.md#enum-textserver-direction))

Sets desired text direction. If set to [TextServer.DIRECTION_AUTO](class_textserver.md#class-textserver-constant-direction-auto), direction will be detected based on the buffer contents and current locale.

---

 **\_shaped_text_set_orientation**(shaped: [RID](class_rid.md#class-rid), orientation: [Orientation](class_textserver.md#enum-textserver-orientation))

Sets desired text orientation.

---

 **\_shaped_text_set_preserve_control**(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If set to `true` text buffer will display control characters.

---

 **\_shaped_text_set_preserve_invalid**(shaped: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If set to `true` text buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.

---

 **\_shaped_text_set_spacing**(shaped: [RID](class_rid.md#class-rid), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int))

Sets extra spacing added between glyphs or lines in pixels.

---

[bool](class_bool.md#class-bool) **\_shaped_text_shape**(shaped: [RID](class_rid.md#class-rid))

Shapes buffer if it's not shaped. Returns `true` if the string is shaped successfully.

---

`const Glyph*` **\_shaped_text_sort_logical**(shaped: [RID](class_rid.md#class-rid))

Returns text glyphs in the logical order.

---

[RID](class_rid.md#class-rid) **\_shaped_text_substr**(shaped: [RID](class_rid.md#class-rid), start: [int](class_int.md#class-int), length: [int](class_int.md#class-int))

Returns text buffer for the substring of the text in the `shaped` text buffer (including inline objects).

---

[float](class_float.md#class-float) **\_shaped_text_tab_align**(shaped: [RID](class_rid.md#class-rid), tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Aligns shaped text to the given tab-stops.

---

[bool](class_bool.md#class-bool) **\_shaped_text_update_breaks**(shaped: [RID](class_rid.md#class-rid))

Updates break points in the shaped text. This method is called by default implementation of text breaking functions.

---

[bool](class_bool.md#class-bool) **\_shaped_text_update_justification_ops**(shaped: [RID](class_rid.md#class-rid))

Updates justification points in the shaped text. This method is called by default implementation of text justification functions.

---

[bool](class_bool.md#class-bool) **\_spoof_check**(string: [String](class_string.md#class-string))

Returns `true` if `string` is likely to be an attempt at confusing the reader.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_string_get_character_breaks**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string))

Returns array of the composite character boundaries.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_string_get_word_breaks**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string), chars_per_line: [int](class_int.md#class-int))

Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.

---

[String](class_string.md#class-string) **\_string_to_lower**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string))

Returns the string converted to `lowercase`.

---

[String](class_string.md#class-string) **\_string_to_title**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string))

Returns the string converted to `Title Case`.

---

[String](class_string.md#class-string) **\_string_to_upper**(string: [String](class_string.md#class-string), language: [String](class_string.md#class-string))

Returns the string converted to `UPPERCASE`.

---

[String](class_string.md#class-string) **\_strip_diacritics**(string: [String](class_string.md#class-string))

Strips diacritics from the string.

---

[String](class_string.md#class-string) **\_tag_to_name**(tag: [int](class_int.md#class-int))

Converts the given OpenType tag to the readable name of a feature, variation, script, or language.

---

 **\_unreference_oversampling_level**(oversampling: [float](class_float.md#class-float))

Decreases the reference count of the specified oversampling level, and frees the font cache for oversampling level when the reference count reaches zero. This method is called by [Viewport](class_viewport.md#class-viewport), and should not be used directly.
