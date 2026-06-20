# SystemFont

**Inherits:** [Font](class_font.md#class-font) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A font loaded from a system font. Falls back to a default theme font if not implemented on the host OS.

## Description

**SystemFont** loads a font from a system font with the first matching name from font_names.

It will attempt to match font style, but it's not guaranteed.

The returned font might be part of a font collection or be a variable font with OpenType "weight", "width" and/or "italic" features set.

You can create [FontVariation](class_fontvariation.md#class-fontvariation) of the system font for precise control over its features.

**Note:** This class is implemented on iOS, Linux, macOS and Windows, on other platforms it will fallback to default theme font.

## Properties

| [bool](class_bool.md#class-bool)                                               | allow_system_fallback                           | `true`                |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------|
| [FontAntialiasing](class_textserver.md#enum-textserver-fontantialiasing)       | antialiasing                                             | `1`                   |
| [bool](class_bool.md#class-bool)                                               | disable_embedded_bitmaps                     | `true`                |
| [bool](class_bool.md#class-bool)                                               | font_italic                                               | `false`               |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)        | font_names                                                 | `PackedStringArray()` |
| [int](class_int.md#class-int)                                                  | font_stretch                                             | `100`                 |
| [int](class_int.md#class-int)                                                  | font_weight                                               | `400`                 |
| [bool](class_bool.md#class-bool)                                               | force_autohinter                                     | `false`               |
| [bool](class_bool.md#class-bool)                                               | generate_mipmaps                                     | `false`               |
| [Hinting](class_textserver.md#enum-textserver-hinting)                         | hinting                                                       | `1`                   |
| [bool](class_bool.md#class-bool)                                               | keep_rounding_remainders                     | `true`                |
| [bool](class_bool.md#class-bool)                                               | modulate_color_glyphs                           | `false`               |
| [int](class_int.md#class-int)                                                  | msdf_pixel_range                                     | `16`                  |
| [int](class_int.md#class-int)                                                  | msdf_size                                                   | `48`                  |
| [bool](class_bool.md#class-bool)                                               | multichannel_signed_distance_field | `false`               |
| [float](class_float.md#class-float)                                            | oversampling                                             | `0.0`                 |
| [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) | subpixel_positioning                             | `1`                   |

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

[bool](class_bool.md#class-bool) **disable_embedded_bitmaps** = `true`

-  **set_disable_embedded_bitmaps**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_disable_embedded_bitmaps**()

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

---

[bool](class_bool.md#class-bool) **font_italic** = `false`

-  **set_font_italic**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_font_italic**()

If set to `true`, italic or oblique font is preferred.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **font_names** = `PackedStringArray()`

-  **set_font_names**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_names**()

Array of font family names to search, first matching font found is used.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

[int](class_int.md#class-int) **font_stretch** = `100`

-  **set_font_stretch**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_stretch**()

Preferred font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

---

[int](class_int.md#class-int) **font_weight** = `400`

-  **set_font_weight**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_weight**()

Preferred weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

---

[bool](class_bool.md#class-bool) **force_autohinter** = `false`

-  **set_force_autohinter**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_force_autohinter**()

If set to `true`, auto-hinting is supported and preferred over font built-in hinting.

---

[bool](class_bool.md#class-bool) **generate_mipmaps** = `false`

-  **set_generate_mipmaps**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_generate_mipmaps**()

If set to `true`, generate mipmaps for the font textures.

---

[Hinting](class_textserver.md#enum-textserver-hinting) **hinting** = `1`

-  **set_hinting**(value: [Hinting](class_textserver.md#enum-textserver-hinting))
- [Hinting](class_textserver.md#enum-textserver-hinting) **get_hinting**()

Font hinting mode.

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

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

---

[float](class_float.md#class-float) **oversampling** = `0.0`

-  **set_oversampling**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_oversampling**()

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See [Viewport.oversampling](class_viewport.md#class-viewport-property-oversampling). This value doesn't override the `oversampling` parameter of `draw_*` methods.

---

[SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **subpixel_positioning** = `1`

-  **set_subpixel_positioning**(value: [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning))
- [SubpixelPositioning](class_textserver.md#enum-textserver-subpixelpositioning) **get_subpixel_positioning**()

Font glyph subpixel positioning mode. Subpixel positioning provides shaper text and better kerning for smaller font sizes, at the cost of memory usage and font rasterization speed. Use [TextServer.SUBPIXEL_POSITIONING_AUTO](class_textserver.md#class-textserver-constant-subpixel-positioning-auto) to automatically enable it based on the font size.
