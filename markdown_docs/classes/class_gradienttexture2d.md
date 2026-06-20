# GradientTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D texture that creates a pattern with colors obtained from a [Gradient](class_gradient.md#class-gradient).

## Description

A 2D texture that obtains colors from a [Gradient](class_gradient.md#class-gradient) to fill the texture data. This texture is able to transform a color transition into different patterns such as a linear or a radial gradient. The texture is filled by interpolating colors starting from fill_from to fill_to offsets by default, but the gradient fill can be repeated to cover the entire texture.

The gradient is sampled individually for each pixel so it does not necessarily represent an exact copy of the gradient (see width and height). See also [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d), [CurveTexture](class_curvetexture.md#class-curvetexture) and [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture).

## Properties

| Fill         | fill           | `0`                                                                                               |
|----------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [Vector2](class_vector2.md#class-vector2)    | fill_from | `Vector2(0, 0)`                                                                                   |
| [Vector2](class_vector2.md#class-vector2)    | fill_to     | `Vector2(1, 0)`                                                                                   |
| [Gradient](class_gradient.md#class-gradient) | gradient   |                                                                                                   |
| [int](class_int.md#class-int)                | height       | `64`                                                                                              |
| Repeat     | repeat       | `0`                                                                                               |
| [bool](class_bool.md#class-bool)             | resource_local_to_scene                                  | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [bool](class_bool.md#class-bool)             | use_hdr     | `false`                                                                                           |
| [int](class_int.md#class-int)                | width         | `64`                                                                                              |

---

## Enumerations

enum **Fill**:

Fill **FILL_LINEAR** = `0`

The colors are linearly interpolated in a straight line.

Fill **FILL_RADIAL** = `1`

The colors are linearly interpolated in a circular pattern.

Fill **FILL_SQUARE** = `2`

The colors are linearly interpolated in a square pattern.

Fill **FILL_CONIC** = `3`

The colors are linearly interpolated in a cone pattern.

---

enum **Repeat**:

Repeat **REPEAT_NONE** = `0`

The gradient fill is restricted to the range defined by fill_from to fill_to offsets.

Repeat **REPEAT** = `1`

The texture is filled starting from fill_from to fill_to offsets, repeating the same pattern in both directions.

Repeat **REPEAT_MIRROR** = `2`

The texture is filled starting from fill_from to fill_to offsets, mirroring the pattern in both directions.

---

## Property Descriptions

Fill **fill** = `0`

-  **set_fill**(value: Fill)
- Fill **get_fill**()

The gradient's fill type.

---

[Vector2](class_vector2.md#class-vector2) **fill_from** = `Vector2(0, 0)`

-  **set_fill_from**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_fill_from**()

The initial offset used to fill the texture specified in UV coordinates.

---

[Vector2](class_vector2.md#class-vector2) **fill_to** = `Vector2(1, 0)`

-  **set_fill_to**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_fill_to**()

The final offset used to fill the texture specified in UV coordinates.

---

[Gradient](class_gradient.md#class-gradient) **gradient**

-  **set_gradient**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_gradient**()

The [Gradient](class_gradient.md#class-gradient) used to fill the texture.

---

[int](class_int.md#class-int) **height** = `64`

-  **set_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_height**()

The number of vertical color samples that will be obtained from the [Gradient](class_gradient.md#class-gradient), which also represents the texture's height.

---

Repeat **repeat** = `0`

-  **set_repeat**(value: Repeat)
- Repeat **get_repeat**()

The gradient's repeat type.

---

[bool](class_bool.md#class-bool) **use_hdr** = `false`

-  **set_use_hdr**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_hdr**()

If `true`, the generated texture will support high dynamic range ([Image.FORMAT_RGBAF](class_image.md#class-image-constant-format-rgbaf) format). This allows for glow effects to work if [Environment.glow_enabled](class_environment.md#class-environment-property-glow-enabled) is `true`. If `false`, the generated texture will use low dynamic range; overbright colors will be clamped ([Image.FORMAT_RGBA8](class_image.md#class-image-constant-format-rgba8) format).

---

[int](class_int.md#class-int) **width** = `64`

-  **set_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_width**()

The number of horizontal color samples that will be obtained from the [Gradient](class_gradient.md#class-gradient), which also represents the texture's width.
