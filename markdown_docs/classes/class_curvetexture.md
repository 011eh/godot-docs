# CurveTexture

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 1D texture where pixel brightness corresponds to points on a curve.

## Description

A 1D texture where pixel brightness corresponds to points on a unit [Curve](class_curve.md#class-curve) resource, either in grayscale or in red. This visual representation simplifies the task of saving curves as image files.

If you need to store up to 3 curves within a single texture, use [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture) instead. See also [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d) and [GradientTexture2D](class_gradienttexture2d.md#class-gradienttexture2d).

## Properties

| [Curve](class_curve.md#class-curve)           | curve               |                                                                                                   |
|-----------------------------------------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)              | resource_local_to_scene                                   | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| TextureMode | texture_mode | `0`                                                                                               |
| [int](class_int.md#class-int)                 | width               | `256`                                                                                             |

---

## Enumerations

enum **TextureMode**:

TextureMode **TEXTURE_MODE_RGB** = `0`

Store the curve equally across the red, green and blue channels. This uses more video memory, but is more compatible with shaders that only read the green and blue values.

TextureMode **TEXTURE_MODE_RED** = `1`

Store the curve only in the red channel. This saves video memory, but some custom shaders may not be able to work with this.

---

## Property Descriptions

[Curve](class_curve.md#class-curve) **curve**

-  **set_curve**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_curve**()

The [Curve](class_curve.md#class-curve) that is rendered onto the texture. Should be a unit [Curve](class_curve.md#class-curve).

---

TextureMode **texture_mode** = `0`

-  **set_texture_mode**(value: TextureMode)
- TextureMode **get_texture_mode**()

The format the texture should be generated with. When passing a CurveTexture as an input to a [Shader](class_shader.md#class-shader), this may need to be adjusted.

---

[int](class_int.md#class-int) **width** = `256`

-  **set_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_width**()

The width of the texture (in pixels). Higher values make it possible to represent high-frequency data better (such as sudden direction changes), at the cost of increased generation time and memory usage.
