# FontFile

**Inherits:** [Font](class_font.md#class-font) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds font source data and prerendered glyph cache, imported from a dynamic or a bitmap font.

## Description

**FontFile** contains a set of glyphs to represent Unicode characters imported from a font file, as well as a cache of rasterized glyphs, and a set of fallback [Font](class_font.md#class-font)s to use.

Use [FontVariation](class_fontvariation.md#class-fontvariation) to access specific OpenType variation of the font, create simulated bold / slanted version, and draw lines of text.

For more complex text processing, use [FontVariation](class_fontvariation.md#class-fontvariation) in conjunction with [TextLine](class_textline.md#class-textline) or [TextParagraph](class_textparagraph.md#class-textparagraph).

Supported font formats:

- Dynamic font importer: TrueType (.ttf), TrueType collection (.ttc), OpenType (.otf), OpenType collection (.otc), WOFF (.woff), WOFF2 (.woff2), Type 1 (.pfb, .pfm).
- Bitmap font importer: AngelCode BMFont (.fnt, .font), text and binary (version 3) format variants.
- Monospace image font importer: All supported image formats.

**Note:** A character is a symbol that represents an item (letter, digit etc.) in an abstract way.

**Note:** A glyph is a bitmap or a shape used to draw one or more characters in a context-dependent manner. Glyph indices are bound to the specific font data source.

**Note:** If none of the font data sources contain glyphs for a character used in a string, the character in question will be replaced with a box displaying its hexadecimal code.

GDScript

```gdscript
var f = load("res://BarlowCondensed-Bold.ttf")
$Label.add_theme_font_override("font", f)
$Label.add_theme_font_size_override("font_size", 64)
```

C#

```csharp
var f = ResourceLoader.Load<FontFile>("res://BarlowCondensed-Bold.ttf");
GetNode("Label").AddThemeFontOverride("font", f);
GetNode("Label").AddThemeFontSizeOverride("font_size", 64);
```

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

## Properties

| [bool](class_bool.md#class-bool)                                               | allow_system_fallback                           | `true`              |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------|
| [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing)       | antialiasing                                             | `1`                 |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)              | data                                                             | `PackedByteArray()` |
| [bool](class_bool.md#class-bool)                                               | disable_embedded_bitmaps                     | `true`              |
| [int](class_int.md#class-int)                                                  | fixed_size                                                 | `0`                 |
| [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode)   | fixed_size_scale_mode                           | `0`                 |
| [String](class_string.md#class-string)                                         | font_name                                                   | `""`                |
| [int](class_int.md#class-int)                                                  | font_stretch                                             | `100`               |
| [[FontStyle](class_textserver.md#enum-textserver-fontstyle)]                   | font_style                                                 | `0`                 |
| [int](class_int.md#class-int)                                                  | font_weight                                               | `400`               |
| [bool](class_bool.md#class-bool)                                               | force_autohinter                                     | `false`             |
| [bool](class_bool.md#class-bool)                                               | generate_mipmaps                                     | `false`             |
| [Hinting](class_textserver.md#enum-textserver-hinting)                         | hinting                                                       | `1`                 |
| [bool](class_bool.md#class-bool)                                               | keep_rounding_remainders                     | `true`              |
| [bool](class_bool.md#class-bool)                                               | modulate_color_glyphs                           | `false`             |
| [int](class_int.md#class-int)                                                  | msdf_pixel_range                                     | `16`                |
| [int](class_int.md#class-int)                                                  | msdf_size                                                   | `48`                |
| [bool](class_bool.md#class-bool)                                               | multichannel_signed_distance_field | `false`             |
| [Dictionary](class_dictionary.md#class-dictionary)                             | opentype_feature_overrides                 | `{}`                |
| [float](class_float.md#class-float)                                            | oversampling                                             | `0.0`               |
| [String](class_string.md#class-string)                                         | style_name                                                 | `""`                |
| [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) | subpixel_positioning                             | `1`                 |

## Methods

|                                                                                   | clear_cache()                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                   | clear_glyphs(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                           |
|                                                                                   | clear_kerning_map(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))                                                                                                                                                |
|                                                                                   | clear_size_cache(cache_index: [int](class_int.md#class-int))                                                                                                                                                                                       |
|                                                                                   | clear_textures(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                       |
| [float](class_float.md#class-float)                                               | get_cache_ascent(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))                                                                                                                                                  |
| [int](class_int.md#class-int)                                                     | get_cache_count()                                                                                                                                                                                                                                   |
| [float](class_float.md#class-float)                                               | get_cache_descent(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))                                                                                                                                                |
| [float](class_float.md#class-float)                                               | get_cache_scale(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))                                                                                                                                                    |
| [float](class_float.md#class-float)                                               | get_cache_underline_position(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))                                                                                                                          |
| [float](class_float.md#class-float)                                               | get_cache_underline_thickness(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))                                                                                                                        |
| [int](class_int.md#class-int)                                                     | get_char_from_glyph_index(size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int))                                                                                                                                |
| [float](class_float.md#class-float)                                               | get_embolden(cache_index: [int](class_int.md#class-int))                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                               | get_extra_baseline_offset(cache_index: [int](class_int.md#class-int))                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                     | get_extra_spacing(cache_index: [int](class_int.md#class-int), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype))                                                                                                            |
| [int](class_int.md#class-int)                                                     | get_face_index(cache_index: [int](class_int.md#class-int))                                                                                                                                                                                           |
| [Vector2](class_vector2.md#class-vector2)                                         | get_glyph_advance(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int))                                                                                                          |
| [int](class_int.md#class-int)                                                     | get_glyph_index(size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int))                                                                                                        |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)              | get_glyph_list(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                       |
| [Vector2](class_vector2.md#class-vector2)                                         | get_glyph_offset(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                             |
| [Vector2](class_vector2.md#class-vector2)                                         | get_glyph_size(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_glyph_texture_idx(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                   |
| [Rect2](class_rect2.md#class-rect2)                                               | get_glyph_uv_rect(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                           |
| [Vector2](class_vector2.md#class-vector2)                                         | get_kerning(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                  |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | get_kerning_list(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                  | get_language_support_override(language: [String](class_string.md#class-string))                                                                                                                                                       |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)           | get_language_support_overrides()                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                  | get_script_support_override(script: [String](class_string.md#class-string))                                                                                                                                                             |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)           | get_script_support_overrides()                                                                                                                                                                                                         |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | get_size_cache_list(cache_index: [int](class_int.md#class-int))                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_texture_count(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                 |
| [Image](class_image.md#class-image)                                               | get_texture_image(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                                   |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)              | get_texture_offsets(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                               |
| [Transform2D](class_transform2d.md#class-transform2d)                             | get_transform(cache_index: [int](class_int.md#class-int))                                                                                                                                                                                             |
| [Dictionary](class_dictionary.md#class-dictionary)                                | get_variation_coordinates(cache_index: [int](class_int.md#class-int))                                                                                                                                                                     |
| [Error](class_@globalscope.md#enum-globalscope-error)                             | load_bitmap_font(path: [String](class_string.md#class-string))                                                                                                                                                                                     |
| [Error](class_@globalscope.md#enum-globalscope-error)                             | load_dynamic_font(path: [String](class_string.md#class-string))                                                                                                                                                                                   |
|                                                                                   | remove_cache(cache_index: [int](class_int.md#class-int))                                                                                                                                                                                               |
|                                                                                   | remove_glyph(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))                                                                                                     |
|                                                                                   | remove_kerning(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))                                                                                            |
|                                                                                   | remove_language_support_override(language: [String](class_string.md#class-string))                                                                                                                                                 |
|                                                                                   | remove_script_support_override(script: [String](class_string.md#class-string))                                                                                                                                                       |
|                                                                                   | remove_size_cache(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                 |
|                                                                                   | remove_texture(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))                                                                                         |
|                                                                                   | render_glyph(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int))                                                                                                     |
|                                                                                   | render_range(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))                                                                 |
|                                                                                   | set_cache_ascent(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float))                                                                                                     |
|                                                                                   | set_cache_descent(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float))                                                                                                  |
|                                                                                   | set_cache_scale(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float))                                                                                                        |
|                                                                                   | set_cache_underline_position(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float))                                                                 |
|                                                                                   | set_cache_underline_thickness(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float))                                                              |
|                                                                                   | set_embolden(cache_index: [int](class_int.md#class-int), strength: [float](class_float.md#class-float))                                                                                                                                                |
|                                                                                   | set_extra_baseline_offset(cache_index: [int](class_int.md#class-int), baseline_offset: [float](class_float.md#class-float))                                                                                                               |
|                                                                                   | set_extra_spacing(cache_index: [int](class_int.md#class-int), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int))                                                                      |
|                                                                                   | set_face_index(cache_index: [int](class_int.md#class-int), face_index: [int](class_int.md#class-int))                                                                                                                                                |
|                                                                                   | set_glyph_advance(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2))                                                      |
|                                                                                   | set_glyph_offset(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2))                                          |
|                                                                                   | set_glyph_size(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2))                                             |
|                                                                                   | set_glyph_texture_idx(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int))                                       |
|                                                                                   | set_glyph_uv_rect(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2))                                             |
|                                                                                   | set_kerning(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2))                                              |
|                                                                                   | set_language_support_override(language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))                                                                                                          |
|                                                                                   | set_script_support_override(script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))                                                                                                                |
|                                                                                   | set_texture_image(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image))                                       |
|                                                                                   | set_texture_offsets(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) |
|                                                                                   | set_transform(cache_index: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                           |
|                                                                                   | set_variation_coordinates(cache_index: [int](class_int.md#class-int), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary))                                                                                          |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_system_fallback** = `true`

-  **set_allow_system_fallback**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_system_fallback**()

If set to `true`, system fonts can be automatically used as fallbacks.

---

[FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) **antialiasing** = `1`

-  **set_antialiasing**(value: [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing))
- [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing) **get_antialiasing**()

Font anti-aliasing mode.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **data** = `PackedByteArray()`

-  **set_data**(value: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_data**()

Contents of the dynamic font source file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[bool](class_bool.md#class-bool) **disable_embedded_bitmaps** = `true`

-  **set_disable_embedded_bitmaps**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_disable_embedded_bitmaps**()

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

---

[int](class_int.md#class-int) **fixed_size** = `0`

-  **set_fixed_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fixed_size**()

Font size, used only for the bitmap fonts.

---

[FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode) **fixed_size_scale_mode** = `0`

-  **set_fixed_size_scale_mode**(value: [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode))
- [FixedSizeScaleMode](class_textserver.md#enum-textserver-fixedsizescalemode) **get_fixed_size_scale_mode**()

Scaling mode, used only for the bitmap fonts with fixed_size greater than zero.

---

[String](class_string.md#class-string) **font_name** = `""`

-  **set_font_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_font_name**()

Font family name.

---

[int](class_int.md#class-int) **font_stretch** = `100`

-  **set_font_stretch**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_stretch**()

Font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

[[FontStyle](class_textserver.md#enum-textserver-fontstyle)] **font_style** = `0`

-  **set_font_style**(value: [[FontStyle](class_textserver.md#enum-textserver-fontstyle)])
- [[FontStyle](class_textserver.md#enum-textserver-fontstyle)] **get_font_style**()

Font style flags.

---

[int](class_int.md#class-int) **font_weight** = `400`

-  **set_font_weight**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_weight**()

Weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

[bool](class_bool.md#class-bool) **force_autohinter** = `false`

-  **set_force_autohinter**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_force_autohinter**()

If set to `true`, auto-hinting is supported and preferred over font built-in hinting. Used by dynamic fonts only (MSDF fonts don't support hinting).

---

[bool](class_bool.md#class-bool) **generate_mipmaps** = `false`

-  **set_generate_mipmaps**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_generate_mipmaps**()

If set to `true`, generate mipmaps for the font textures.

---

[Hinting](class_textserver.md#enum-textserver-hinting) **hinting** = `1`

-  **set_hinting**(value: [Hinting](class_textserver.md#enum-textserver-hinting))
- [Hinting](class_textserver.md#enum-textserver-hinting) **get_hinting**()

Font hinting mode. Used by dynamic fonts only.

---

[bool](class_bool.md#class-bool) **keep_rounding_remainders** = `true`

-  **set_keep_rounding_remainders**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_keep_rounding_remainders**()

If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

---

[bool](class_bool.md#class-bool) **modulate_color_glyphs** = `false`

-  **set_modulate_color_glyphs**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_modulate_color_glyphs**()

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

---

[int](class_int.md#class-int) **msdf_pixel_range** = `16`

-  **set_msdf_pixel_range**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_msdf_pixel_range**()

The width of the range around the shape between the minimum and maximum representable signed distance. If using font outlines, msdf_pixel_range must be set to at least *twice* the size of the largest font outline. The default msdf_pixel_range value of `16` allows outline sizes up to `8` to look correct.

---

[int](class_int.md#class-int) **msdf_size** = `48`

-  **set_msdf_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_msdf_size**()

Source font size used to generate MSDF textures. Higher values allow for more precision, but are slower to render and require more memory. Only increase this value if you notice a visible lack of precision in glyph rendering.

---

[bool](class_bool.md#class-bool) **multichannel_signed_distance_field** = `false`

-  **set_multichannel_signed_distance_field**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_multichannel_signed_distance_field**()

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field (MSDF) generated from the dynamic font vector data. Since this approach does not rely on rasterizing the font every time its size changes, this allows for resizing the font in real-time without any performance penalty. Text will also not look grainy for [Control](class_control.md#class-control)s that are scaled down (or for [Label3D](class_label3d.md#class-label3d)s viewed from a long distance). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

**Note:** If using font outlines, msdf_pixel_range must be set to at least *twice* the size of the largest font outline.

**Note:** MSDF font rendering does not render glyphs with overlapping shapes correctly. Overlapping shapes are not valid per the OpenType standard, but are still commonly found in many font files, especially those converted by Google Fonts. To avoid issues with overlapping glyphs, consider downloading the font file directly from the type foundry instead of relying on Google Fonts.

---

[Dictionary](class_dictionary.md#class-dictionary) **opentype_feature_overrides** = `{}`

-  **set_opentype_feature_overrides**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_opentype_feature_overrides**()

Font OpenType feature set override.

---

[float](class_float.md#class-float) **oversampling** = `0.0`

-  **set_oversampling**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_oversampling**()

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods.

---

[String](class_string.md#class-string) **style_name** = `""`

-  **set_font_style_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_font_style_name**()

Font style name.

---

[SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **subpixel_positioning** = `1`

-  **set_subpixel_positioning**(value: [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning))
- [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **get_subpixel_positioning**()

Font glyph subpixel positioning mode. Subpixel positioning provides shaper text and better kerning for smaller font sizes, at the cost of higher memory usage and lower font rasterization speed. Use [TextServer.SUBPIXEL_POSITIONING_AUTO](class_textserver.md#class-textserver-constant-subpixel-positioning-auto) to automatically enable it based on the font size.

---

## Method Descriptions

 **clear_cache**()

Removes all font cache entries.

---

 **clear_glyphs**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes all rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use remove_texture() to remove them manually.

---

 **clear_kerning_map**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Removes all kerning overrides.

---

 **clear_size_cache**(cache_index: [int](class_int.md#class-int))

Removes all font sizes from the cache entry.

---

 **clear_textures**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes all textures from font cache entry.

**Note:** This function will not remove glyphs associated with the texture, use remove_glyph() to remove them manually.

---

[float](class_float.md#class-float) **get_cache_ascent**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Returns the font ascent (number of pixels above the baseline).

---

[int](class_int.md#class-int) **get_cache_count**()

Returns number of the font cache entries.

---

[float](class_float.md#class-float) **get_cache_descent**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Returns the font descent (number of pixels below the baseline).

---

[float](class_float.md#class-float) **get_cache_scale**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Returns scaling factor of the color bitmap font.

---

[float](class_float.md#class-float) **get_cache_underline_position**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Returns pixel offset of the underline below the baseline.

---

[float](class_float.md#class-float) **get_cache_underline_thickness**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Returns thickness of the underline in pixels.

---

[int](class_int.md#class-int) **get_char_from_glyph_index**(size: [int](class_int.md#class-int), glyph_index: [int](class_int.md#class-int))

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid. See get_glyph_index().

---

[float](class_float.md#class-float) **get_embolden**(cache_index: [int](class_int.md#class-int))

Returns embolden strength, if is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---

[float](class_float.md#class-float) **get_extra_baseline_offset**(cache_index: [int](class_int.md#class-int))

Returns extra baseline offset (as a fraction of font height).

---

[int](class_int.md#class-int) **get_extra_spacing**(cache_index: [int](class_int.md#class-int), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype))

Returns spacing for `spacing` in pixels (not relative to the font size).

---

[int](class_int.md#class-int) **get_face_index**(cache_index: [int](class_int.md#class-int))

Returns an active face index in the TrueType / OpenType collection.

---

[Vector2](class_vector2.md#class-vector2) **get_glyph_advance**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int))

Returns glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

---

[int](class_int.md#class-int) **get_glyph_index**(size: [int](class_int.md#class-int), char: [int](class_int.md#class-int), variation_selector: [int](class_int.md#class-int))

Returns the glyph index of a `char`, optionally modified by the `variation_selector`.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_glyph_list**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))

Returns list of rendered glyphs in the cache entry.

---

[Vector2](class_vector2.md#class-vector2) **get_glyph_offset**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns glyph offset from the baseline.

---

[Vector2](class_vector2.md#class-vector2) **get_glyph_size**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns glyph size.

---

[int](class_int.md#class-int) **get_glyph_texture_idx**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns index of the cache texture containing the glyph.

---

[Rect2](class_rect2.md#class-rect2) **get_glyph_uv_rect**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Returns rectangle in the cache texture containing the glyph.

---

[Vector2](class_vector2.md#class-vector2) **get_kerning**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))

Returns kerning for the pair of glyphs.

---

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **get_kerning_list**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Returns list of the kerning overrides.

---

[bool](class_bool.md#class-bool) **get_language_support_override**(language: [String](class_string.md#class-string))

Returns `true` if support override is enabled for the `language`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_language_support_overrides**()

Returns list of language support overrides.

---

[bool](class_bool.md#class-bool) **get_script_support_override**(script: [String](class_string.md#class-string))

Returns `true` if support override is enabled for the `script`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_script_support_overrides**()

Returns list of script support overrides.

---

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **get_size_cache_list**(cache_index: [int](class_int.md#class-int))

Returns list of the font sizes in the cache. Each size is [Vector2i](class_vector2i.md#class-vector2i) with font size and outline size.

---

[int](class_int.md#class-int) **get_texture_count**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))

Returns number of textures used by font cache entry.

---

[Image](class_image.md#class-image) **get_texture_image**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Returns a copy of the font cache texture image.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_texture_offsets**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Returns a copy of the array containing glyph packing data.

---

[Transform2D](class_transform2d.md#class-transform2d) **get_transform**(cache_index: [int](class_int.md#class-int))

Returns 2D transform, applied to the font outlines, can be used for slanting, flipping and rotating glyphs.

---

[Dictionary](class_dictionary.md#class-dictionary) **get_variation_coordinates**(cache_index: [int](class_int.md#class-int))

Returns variation coordinates for the specified font cache entry. See [Font.get_supported_variation_list()](class_font.md#class-font-method-get-supported-variation-list) for more info.

---

[Error](class_@globalscope.md#enum-globalscope-error) **load_bitmap_font**(path: [String](class_string.md#class-string))

Loads an AngelCode BMFont (.fnt, .font) bitmap font from file `path`.

**Warning:** This method should only be used in the editor or in cases when you need to load external fonts at run-time, such as fonts located at the `user://` directory.

---

[Error](class_@globalscope.md#enum-globalscope-error) **load_dynamic_font**(path: [String](class_string.md#class-string))

Loads a TrueType (.ttf), OpenType (.otf), WOFF (.woff), WOFF2 (.woff2) or Type 1 (.pfb, .pfm) dynamic font from file `path`.

**Warning:** This method should only be used in the editor or in cases when you need to load external fonts at run-time, such as fonts located at the `user://` directory.

---

 **remove_cache**(cache_index: [int](class_int.md#class-int))

Removes specified font cache entry.

---

 **remove_glyph**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int))

Removes specified rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use remove_texture() to remove them manually.

---

 **remove_kerning**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i))

Removes kerning override for the pair of glyphs.

---

 **remove_language_support_override**(language: [String](class_string.md#class-string))

Remove language support override.

---

 **remove_script_support_override**(script: [String](class_string.md#class-string))

Removes script support override.

---

 **remove_size_cache**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i))

Removes specified font size from the cache entry.

---

 **remove_texture**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int))

Removes specified texture from the cache entry.

**Note:** This function will not remove glyphs associated with the texture. Remove them manually using remove_glyph().

---

 **render_glyph**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int))

Renders specified glyph to the font cache texture.

---

 **render_range**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), start: [int](class_int.md#class-int), end: [int](class_int.md#class-int))

Renders the range of characters to the font cache texture.

---

 **set_cache_ascent**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), ascent: [float](class_float.md#class-float))

Sets the font ascent (number of pixels above the baseline).

---

 **set_cache_descent**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), descent: [float](class_float.md#class-float))

Sets the font descent (number of pixels below the baseline).

---

 **set_cache_scale**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), scale: [float](class_float.md#class-float))

Sets scaling factor of the color bitmap font.

---

 **set_cache_underline_position**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), underline_position: [float](class_float.md#class-float))

Sets pixel offset of the underline below the baseline.

---

 **set_cache_underline_thickness**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), underline_thickness: [float](class_float.md#class-float))

Sets thickness of the underline in pixels.

---

 **set_embolden**(cache_index: [int](class_int.md#class-int), strength: [float](class_float.md#class-float))

Sets embolden strength, if is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

---

 **set_extra_baseline_offset**(cache_index: [int](class_int.md#class-int), baseline_offset: [float](class_float.md#class-float))

Sets extra baseline offset (as a fraction of font height).

---

 **set_extra_spacing**(cache_index: [int](class_int.md#class-int), spacing: [SpacingType](class_textserver.md#enum-textserver-spacingtype), value: [int](class_int.md#class-int))

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

---

 **set_face_index**(cache_index: [int](class_int.md#class-int), face_index: [int](class_int.md#class-int))

Sets an active face index in the TrueType / OpenType collection.

---

 **set_glyph_advance**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph: [int](class_int.md#class-int), advance: [Vector2](class_vector2.md#class-vector2))

Sets glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

---

 **set_glyph_offset**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2))

Sets glyph offset from the baseline.

---

 **set_glyph_size**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), gl_size: [Vector2](class_vector2.md#class-vector2))

Sets glyph size.

---

 **set_glyph_texture_idx**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), texture_idx: [int](class_int.md#class-int))

Sets index of the cache texture containing the glyph.

---

 **set_glyph_uv_rect**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), glyph: [int](class_int.md#class-int), uv_rect: [Rect2](class_rect2.md#class-rect2))

Sets rectangle in the cache texture containing the glyph.

---

 **set_kerning**(cache_index: [int](class_int.md#class-int), size: [int](class_int.md#class-int), glyph_pair: [Vector2i](class_vector2i.md#class-vector2i), kerning: [Vector2](class_vector2.md#class-vector2))

Sets kerning for the pair of glyphs.

---

 **set_language_support_override**(language: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))

Adds override for [Font.is_language_supported()](class_font.md#class-font-method-is-language-supported).

---

 **set_script_support_override**(script: [String](class_string.md#class-string), supported: [bool](class_bool.md#class-bool))

Adds override for [Font.is_script_supported()](class_font.md#class-font-method-is-script-supported).

---

 **set_texture_image**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), image: [Image](class_image.md#class-image))

Sets font cache texture image.

---

 **set_texture_offsets**(cache_index: [int](class_int.md#class-int), size: [Vector2i](class_vector2i.md#class-vector2i), texture_index: [int](class_int.md#class-int), offset: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Sets array containing glyph packing data.

---

 **set_transform**(cache_index: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

---

 **set_variation_coordinates**(cache_index: [int](class_int.md#class-int), variation_coordinates: [Dictionary](class_dictionary.md#class-dictionary))

Sets variation coordinates for the specified font cache entry. See [Font.get_supported_variation_list()](class_font.md#class-font-method-get-supported-variation-list) for more info.
