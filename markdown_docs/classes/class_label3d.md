# Label3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node for displaying plain text in 3D space.

## Description

A node for displaying plain text in 3D space. By adjusting various properties of this node, you can configure things such as the text's appearance and whether it always faces the camera.

## Tutorials

- [3D text](../tutorials/3d/3d_text.md)

## Properties

| [float](class_float.md#class-float)                                                              | alpha_antialiasing_edge                             | `0.0`                                                                                                           |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing)               | alpha_antialiasing_mode                             | `0`                                                                                                             |
| AlphaCutMode                                                       | alpha_cut                                                         | `0`                                                                                                             |
| [float](class_float.md#class-float)                                                              | alpha_hash_scale                                           | `1.0`                                                                                                           |
| [float](class_float.md#class-float)                                                              | alpha_scissor_threshold                             | `0.5`                                                                                                           |
| [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode)                                 | autowrap_mode                                                 | `0`                                                                                                             |
| [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]                             | autowrap_trim_flags                                     | `192`                                                                                                           |
| [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode)                       | billboard                                                         | `0`                                                                                                             |
| [ShadowCastingSetting](class_geometryinstance3d.md#enum-geometryinstance3d-shadowcastingsetting) | cast_shadow                                                                                            | `0` (overrides [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d-property-cast-shadow)) |
| [bool](class_bool.md#class-bool)                                                                 | double_sided                                                   | `true`                                                                                                          |
| [bool](class_bool.md#class-bool)                                                                 | fixed_size                                                       | `false`                                                                                                         |
| [Font](class_font.md#class-font)                                                                 | font                                                                   |                                                                                                                 |
| [int](class_int.md#class-int)                                                                    | font_size                                                         | `32`                                                                                                            |
| [GIMode](class_geometryinstance3d.md#enum-geometryinstance3d-gimode)                             | gi_mode                                                                                                | `0` (overrides [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d-property-gi-mode))     |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)                | horizontal_alignment                                   | `1`                                                                                                             |
| [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)]                     | justification_flags                                     | `163`                                                                                                           |
| [String](class_string.md#class-string)                                                           | language                                                           | `""`                                                                                                            |
| [float](class_float.md#class-float)                                                              | line_spacing                                                   | `0.0`                                                                                                           |
| [Color](class_color.md#class-color)                                                              | modulate                                                           | `Color(1, 1, 1, 1)`                                                                                             |
| [bool](class_bool.md#class-bool)                                                                 | no_depth_test                                                 | `false`                                                                                                         |
| [Vector2](class_vector2.md#class-vector2)                                                        | offset                                                               | `Vector2(0, 0)`                                                                                                 |
| [Color](class_color.md#class-color)                                                              | outline_modulate                                           | `Color(0, 0, 0, 1)`                                                                                             |
| [int](class_int.md#class-int)                                                                    | outline_render_priority                             | `-1`                                                                                                            |
| [int](class_int.md#class-int)                                                                    | outline_size                                                   | `12`                                                                                                            |
| [float](class_float.md#class-float)                                                              | pixel_size                                                       | `0.005`                                                                                                         |
| [int](class_int.md#class-int)                                                                    | render_priority                                             | `0`                                                                                                             |
| [bool](class_bool.md#class-bool)                                                                 | shaded                                                               | `false`                                                                                                         |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser)                 | structured_text_bidi_override                 | `0`                                                                                                             |
| [Array](class_array.md#class-array)                                                              | structured_text_bidi_override_options | `[]`                                                                                                            |
| [String](class_string.md#class-string)                                                           | text                                                                   | `""`                                                                                                            |
| [Direction](class_textserver.md#enum-textserver-direction)                                       | text_direction                                               | `0`                                                                                                             |
| [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter)                       | texture_filter                                               | `3`                                                                                                             |
| [bool](class_bool.md#class-bool)                                                                 | uppercase                                                         | `false`                                                                                                         |
| [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment)                    | vertical_alignment                                       | `1`                                                                                                             |
| [float](class_float.md#class-float)                                                              | width                                                                 | `500.0`                                                                                                         |

## Methods

| [TriangleMesh](class_trianglemesh.md#class-trianglemesh)   | generate_triangle_mesh()                                                                    |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                           | get_draw_flag(flag: DrawFlags)                                            |
|                                                            | set_draw_flag(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool)) |

---

## Enumerations

enum **DrawFlags**:

DrawFlags **FLAG_SHADED** = `0`

If set, lights in the environment affect the label.

DrawFlags **FLAG_DOUBLE_SIDED** = `1`

If set, text can be seen from the back as well. If not, the text is invisible when looking at it from behind.

DrawFlags **FLAG_DISABLE_DEPTH_TEST** = `2`

Disables the depth test, so this object is drawn on top of all others. However, objects drawn after it in the draw order may cover it.

DrawFlags **FLAG_FIXED_SIZE** = `3`

Label is scaled by depth so that it always appears the same size on screen.

DrawFlags **FLAG_MAX** = `4`

Represents the size of the DrawFlags enum.

---

enum **AlphaCutMode**:

AlphaCutMode **ALPHA_CUT_DISABLED** = `0`

This mode performs standard alpha blending. It can display translucent areas, but transparency sorting issues may be visible when multiple transparent materials are overlapping. [GeometryInstance3D.cast_shadow](class_geometryinstance3d.md#class-geometryinstance3d-property-cast-shadow) has no effect when this transparency mode is used; the **Label3D** will never cast shadows.

AlphaCutMode **ALPHA_CUT_DISCARD** = `1`

This mode only allows fully transparent or fully opaque pixels. Harsh edges will be visible unless some form of screen-space antialiasing is enabled (see [ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-screen-space-aa)). This mode is also known as *alpha testing* or *1-bit transparency*.

**Note:** This mode might have issues with anti-aliased fonts and outlines, try adjusting alpha_scissor_threshold or using MSDF font.

**Note:** When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.

AlphaCutMode **ALPHA_CUT_OPAQUE_PREPASS** = `2`

This mode draws fully opaque pixels in the depth prepass. This is slower than ALPHA_CUT_DISABLED or ALPHA_CUT_DISCARD, but it allows displaying translucent areas and smooth edges while using proper sorting.

**Note:** When using text with overlapping glyphs (e.g., cursive scripts), this mode might have transparency sorting issues between the main text and the outline.

AlphaCutMode **ALPHA_CUT_HASH** = `3`

This mode draws cuts off all values below a spatially-deterministic threshold, the rest will remain opaque.

---

## Property Descriptions

[float](class_float.md#class-float) **alpha_antialiasing_edge** = `0.0`

-  **set_alpha_antialiasing_edge**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_alpha_antialiasing_edge**()

Threshold at which antialiasing will be applied on the alpha channel.

---

[AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing) **alpha_antialiasing_mode** = `0`

-  **set_alpha_antialiasing**(value: [AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing))
- [AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing) **get_alpha_antialiasing**()

The type of alpha antialiasing to apply.

---

AlphaCutMode **alpha_cut** = `0`

-  **set_alpha_cut_mode**(value: AlphaCutMode)
- AlphaCutMode **get_alpha_cut_mode**()

The alpha cutting mode to use for the sprite.

---

[float](class_float.md#class-float) **alpha_hash_scale** = `1.0`

-  **set_alpha_hash_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_alpha_hash_scale**()

The hashing scale for Alpha Hash. Recommended values between `0` and `2`.

---

[float](class_float.md#class-float) **alpha_scissor_threshold** = `0.5`

-  **set_alpha_scissor_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_alpha_scissor_threshold**()

Threshold at which the alpha scissor will discard values.

---

[AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **autowrap_mode** = `0`

-  **set_autowrap_mode**(value: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode))
- [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **get_autowrap_mode**()

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off), the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

---

[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **autowrap_trim_flags** = `192`

-  **set_autowrap_trim_flags**(value: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])
- [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **get_autowrap_trim_flags**()

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-start-edge-spaces) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-end-edge-spaces) for more info.

---

[BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode) **billboard** = `0`

-  **set_billboard_mode**(value: [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode))
- [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode) **get_billboard_mode**()

The billboard mode to use for the label.

---

[bool](class_bool.md#class-bool) **double_sided** = `true`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, text can be seen from the back as well, if `false`, it is invisible when looking at it from behind.

---

[bool](class_bool.md#class-bool) **fixed_size** = `false`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, the label is rendered at the same size regardless of distance. The label's size on screen is the same as if the camera was `1.0` units away from the label's origin, regardless of the actual distance from the camera. The [Camera3D](class_camera3d.md#class-camera3d)'s field of view (or [Camera3D.size](class_camera3d.md#class-camera3d-property-size) when in orthogonal/frustum mode) still affects the size the label is drawn at.

---

[Font](class_font.md#class-font) **font**

-  **set_font**(value: [Font](class_font.md#class-font))
- [Font](class_font.md#class-font) **get_font**()

Font configuration used to display text.

---

[int](class_int.md#class-int) **font_size** = `32`

-  **set_font_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_size**()

Font size of the **Label3D**'s text. To make the font look more detailed when up close, increase font_size while decreasing pixel_size at the same time.

Higher font sizes require more time to render new characters, which can cause stuttering during gameplay.

---

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **horizontal_alignment** = `1`

-  **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---

[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **justification_flags** = `163`

-  **set_justification_flags**(value: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_justification_flags**()

Line fill alignment rules.

---

[String](class_string.md#class-string) **language** = `""`

-  **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

[float](class_float.md#class-float) **line_spacing** = `0.0`

-  **set_line_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

[Color](class_color.md#class-color) **modulate** = `Color(1, 1, 1, 1)`

-  **set_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_modulate**()

Text [Color](class_color.md#class-color) of the **Label3D**.

---

[bool](class_bool.md#class-bool) **no_depth_test** = `false`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, depth testing is disabled and the object will be drawn in render order.

---

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)`

-  **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The text drawing offset (in pixels).

---

[Color](class_color.md#class-color) **outline_modulate** = `Color(0, 0, 0, 1)`

-  **set_outline_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_outline_modulate**()

The tint of text outline.

---

[int](class_int.md#class-int) **outline_render_priority** = `-1`

-  **set_outline_render_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_outline_render_priority**()

Sets the render priority for the text outline. Higher priority objects will be sorted in front of lower priority objects.

**Note:** This only applies if alpha_cut is set to ALPHA_CUT_DISABLED (default value).

**Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).

---

[int](class_int.md#class-int) **outline_size** = `12`

-  **set_outline_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_outline_size**()

Text outline size.

---

[float](class_float.md#class-float) **pixel_size** = `0.005`

-  **set_pixel_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pixel_size**()

The size of one pixel's width on the label to scale it in 3D. To make the font look more detailed when up close, increase font_size while decreasing pixel_size at the same time.

---

[int](class_int.md#class-int) **render_priority** = `0`

-  **set_render_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_render_priority**()

Sets the render priority for the text. Higher priority objects will be sorted in front of lower priority objects.

**Note:** This only applies if alpha_cut is set to ALPHA_CUT_DISABLED (default value).

**Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).

---

[bool](class_bool.md#class-bool) **shaded** = `false`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, the [Light3D](class_light3d.md#class-light3d) in the [Environment](class_environment.md#class-environment) has effects on the label.

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

[String](class_string.md#class-string) **text** = `""`

-  **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

The text to display on screen.

---

[Direction](class_textserver.md#enum-textserver-direction) **text_direction** = `0`

-  **set_text_direction**(value: [Direction](class_textserver.md#enum-textserver-direction))
- [Direction](class_textserver.md#enum-textserver-direction) **get_text_direction**()

Base text writing direction.

---

[TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter) **texture_filter** = `3`

-  **set_texture_filter**(value: [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter))
- [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter) **get_texture_filter**()

Filter flags for the texture.

---

[bool](class_bool.md#class-bool) **uppercase** = `false`

-  **set_uppercase**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_uppercase**()

If `true`, all the text displays as UPPERCASE.

---

[VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **vertical_alignment** = `1`

-  **set_vertical_alignment**(value: [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment))
- [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **get_vertical_alignment**()

Controls the text's vertical alignment. Supports top, center, and bottom.

---

[float](class_float.md#class-float) **width** = `500.0`

-  **set_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_width**()

Text width (in pixels), used for autowrap and fill alignment.

---

## Method Descriptions

[TriangleMesh](class_trianglemesh.md#class-trianglemesh) **generate_triangle_mesh**()

Returns a [TriangleMesh](class_trianglemesh.md#class-trianglemesh) with the label's vertices following its current configuration (such as its pixel_size).

---

[bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags)

Returns the value of the specified flag.

---

 **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))

If `true`, the specified `flag` will be enabled.
