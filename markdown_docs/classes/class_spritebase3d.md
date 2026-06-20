# SpriteBase3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [AnimatedSprite3D](class_animatedsprite3d.md#class-animatedsprite3d), [Sprite3D](class_sprite3d.md#class-sprite3d)

2D sprite node in 3D environment.

## Description

A node that displays 2D texture information in a 3D environment. See also [Sprite3D](class_sprite3d.md#class-sprite3d) where many other properties are defined.

## Properties

| [float](class_float.md#class-float)                                                | alpha_antialiasing_edge   | `0.0`               |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------|
| [AlphaAntiAliasing](class_basematerial3d.md#enum-basematerial3d-alphaantialiasing) | alpha_antialiasing_mode   | `0`                 |
| AlphaCutMode                                    | alpha_cut                               | `0`                 |
| [float](class_float.md#class-float)                                                | alpha_hash_scale                 | `1.0`               |
| [float](class_float.md#class-float)                                                | alpha_scissor_threshold   | `0.5`               |
| [Axis](class_vector3.md#enum-vector3-axis)                                         | axis                                         | `2`                 |
| [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode)         | billboard                               | `0`                 |
| [bool](class_bool.md#class-bool)                                                   | centered                                 | `true`              |
| [bool](class_bool.md#class-bool)                                                   | double_sided                         | `true`              |
| [bool](class_bool.md#class-bool)                                                   | fixed_size                             | `false`             |
| [bool](class_bool.md#class-bool)                                                   | flip_h                                     | `false`             |
| [bool](class_bool.md#class-bool)                                                   | flip_v                                     | `false`             |
| [Color](class_color.md#class-color)                                                | modulate                                 | `Color(1, 1, 1, 1)` |
| [bool](class_bool.md#class-bool)                                                   | no_depth_test                       | `false`             |
| [Vector2](class_vector2.md#class-vector2)                                          | offset                                     | `Vector2(0, 0)`     |
| [float](class_float.md#class-float)                                                | pixel_size                             | `0.01`              |
| [int](class_int.md#class-int)                                                      | render_priority                   | `0`                 |
| [bool](class_bool.md#class-bool)                                                   | shaded                                     | `false`             |
| [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter)         | texture_filter                     | `3`                 |
| [bool](class_bool.md#class-bool)                                                   | transparent                           | `true`              |

## Methods

| [TriangleMesh](class_trianglemesh.md#class-trianglemesh)   | generate_triangle_mesh()                                                                         |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                           | get_draw_flag(flag: DrawFlags)                                            |
| [Rect2](class_rect2.md#class-rect2)                        | get_item_rect()                                                                                           |
|                                                            | set_draw_flag(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool)) |

---

## Enumerations

enum **DrawFlags**:

DrawFlags **FLAG_TRANSPARENT** = `0`

If set, the texture's transparency and the opacity are used to make those parts of the sprite invisible.

DrawFlags **FLAG_SHADED** = `1`

If set, lights in the environment affect the sprite.

DrawFlags **FLAG_DOUBLE_SIDED** = `2`

If set, texture can be seen from the back as well. If not, the texture is invisible when looking at it from behind.

DrawFlags **FLAG_DISABLE_DEPTH_TEST** = `3`

Disables the depth test, so this object is drawn on top of all others. However, objects drawn after it in the draw order may cover it.

DrawFlags **FLAG_FIXED_SIZE** = `4`

Label is scaled by depth so that it always appears the same size on screen.

DrawFlags **FLAG_MAX** = `5`

Represents the size of the DrawFlags enum.

---

enum **AlphaCutMode**:

AlphaCutMode **ALPHA_CUT_DISABLED** = `0`

This mode performs standard alpha blending. It can display translucent areas, but transparency sorting issues may be visible when multiple transparent materials are overlapping.

AlphaCutMode **ALPHA_CUT_DISCARD** = `1`

This mode only allows fully transparent or fully opaque pixels. Harsh edges will be visible unless some form of screen-space antialiasing is enabled (see [ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-screen-space-aa)). On the bright side, this mode doesn't suffer from transparency sorting issues when multiple transparent materials are overlapping. This mode is also known as *alpha testing* or *1-bit transparency*.

AlphaCutMode **ALPHA_CUT_OPAQUE_PREPASS** = `2`

This mode draws fully opaque pixels in the depth prepass. This is slower than ALPHA_CUT_DISABLED or ALPHA_CUT_DISCARD, but it allows displaying translucent areas and smooth edges while using proper sorting.

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

[Axis](class_vector3.md#enum-vector3-axis) **axis** = `2`

-  **set_axis**(value: [Axis](class_vector3.md#enum-vector3-axis))
- [Axis](class_vector3.md#enum-vector3-axis) **get_axis**()

The direction in which the front of the texture faces.

---

[BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode) **billboard** = `0`

-  **set_billboard_mode**(value: [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode))
- [BillboardMode](class_basematerial3d.md#enum-basematerial3d-billboardmode) **get_billboard_mode**()

The billboard mode to use for the sprite.

**Note:** When billboarding is enabled and the material also casts shadows, billboards will face **the** camera in the scene when rendering shadows. In scenes with multiple cameras, the intended shadow cannot be determined and this will result in undefined behavior. See [GitHub Pull Request #72638](https://github.com/godotengine/godot/pull/72638) for details.

---

[bool](class_bool.md#class-bool) **centered** = `true`

-  **set_centered**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_centered**()

If `true`, texture will be centered.

---

[bool](class_bool.md#class-bool) **double_sided** = `true`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, texture can be seen from the back as well, if `false`, it is invisible when looking at it from behind.

---

[bool](class_bool.md#class-bool) **fixed_size** = `false`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, the texture is rendered at the same size regardless of distance. The texture's size on screen is the same as if the camera was `1.0` units away from the texture's origin, regardless of the actual distance from the camera. The [Camera3D](class_camera3d.md#class-camera3d)'s field of view (or [Camera3D.size](class_camera3d.md#class-camera3d-property-size) when in orthogonal/frustum mode) still affects the size the sprite is drawn at.

---

[bool](class_bool.md#class-bool) **flip_h** = `false`

-  **set_flip_h**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_h**()

If `true`, texture is flipped horizontally.

---

[bool](class_bool.md#class-bool) **flip_v** = `false`

-  **set_flip_v**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_v**()

If `true`, texture is flipped vertically.

---

[Color](class_color.md#class-color) **modulate** = `Color(1, 1, 1, 1)`

-  **set_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_modulate**()

A color value used to *multiply* the texture's colors. Can be used for mood-coloring or to simulate the color of ambient light.

**Note:** Unlike [CanvasItem.modulate](class_canvasitem.md#class-canvasitem-property-modulate) for 2D, colors with values above `1.0` (overbright) are not supported.

**Note:** If a [GeometryInstance3D.material_override](class_geometryinstance3d.md#class-geometryinstance3d-property-material-override) is defined on the **SpriteBase3D**, the material override must be configured to take vertex colors into account for albedo. Otherwise, the color defined in modulate will be ignored. For a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) must be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function.

---

[bool](class_bool.md#class-bool) **no_depth_test** = `false`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, depth testing is disabled and the object will be drawn in render order.

---

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)`

-  **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The texture's drawing offset.

**Note:** When you increase offset.y in Sprite3D, the sprite moves upward in world space (i.e., +Y is up).

---

[float](class_float.md#class-float) **pixel_size** = `0.01`

-  **set_pixel_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pixel_size**()

The size of one pixel's width on the sprite to scale it in 3D.

---

[int](class_int.md#class-int) **render_priority** = `0`

-  **set_render_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_render_priority**()

Sets the render priority for the sprite. Higher priority objects will be sorted in front of lower priority objects.

**Note:** This only applies if alpha_cut is set to ALPHA_CUT_DISABLED (default value).

**Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).

---

[bool](class_bool.md#class-bool) **shaded** = `false`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, the [Light3D](class_light3d.md#class-light3d) in the [Environment](class_environment.md#class-environment) has effects on the sprite.

---

[TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter) **texture_filter** = `3`

-  **set_texture_filter**(value: [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter))
- [TextureFilter](class_basematerial3d.md#enum-basematerial3d-texturefilter) **get_texture_filter**()

Filter flags for the texture.

**Note:** Linear filtering may cause artifacts around the edges, which are especially noticeable on opaque textures. To prevent this, use textures with transparent or identical colors around the edges.

---

[bool](class_bool.md#class-bool) **transparent** = `true`

-  **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags) 

If `true`, the texture's transparency and the opacity are used to make those parts of the sprite invisible.

---

## Method Descriptions

[TriangleMesh](class_trianglemesh.md#class-trianglemesh) **generate_triangle_mesh**()

Returns a [TriangleMesh](class_trianglemesh.md#class-trianglemesh) with the sprite's vertices following its current configuration (such as its axis and pixel_size).

---

[bool](class_bool.md#class-bool) **get_draw_flag**(flag: DrawFlags)

Returns the value of the specified flag.

---

[Rect2](class_rect2.md#class-rect2) **get_item_rect**()

Returns the rectangle representing this sprite.

---

 **set_draw_flag**(flag: DrawFlags, enabled: [bool](class_bool.md#class-bool))

If `true`, the specified flag will be enabled.
