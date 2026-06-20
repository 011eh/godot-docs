# GradientTexture1D

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 1D texture that uses colors obtained from a [Gradient](class_gradient.md#class-gradient).

## Description

A 1D texture that obtains colors from a [Gradient](class_gradient.md#class-gradient) to fill the texture data. The texture is filled by sampling the gradient for each pixel. Therefore, the texture does not necessarily represent an exact copy of the gradient, as it may miss some colors if there are not enough pixels. See also [GradientTexture2D](class_gradienttexture2d.md#class-gradienttexture2d), [CurveTexture](class_curvetexture.md#class-curvetexture) and [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture).

## Properties

| [Gradient](class_gradient.md#class-gradient)   | gradient   |                                                                                                   |
|------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)               | resource_local_to_scene                                  | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [bool](class_bool.md#class-bool)               | use_hdr     | `false`                                                                                           |
| [int](class_int.md#class-int)                  | width         | `256`                                                                                             |

---

## Property Descriptions

[Gradient](class_gradient.md#class-gradient) **gradient**

-  **set_gradient**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_gradient**()

The [Gradient](class_gradient.md#class-gradient) used to fill the texture.

---

[bool](class_bool.md#class-bool) **use_hdr** = `false`

-  **set_use_hdr**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_hdr**()

If `true`, the generated texture will support high dynamic range ([Image.FORMAT_RGBAF](class_image.md#class-image-constant-format-rgbaf) format). This allows for glow effects to work if [Environment.glow_enabled](class_environment.md#class-environment-property-glow-enabled) is `true`. If `false`, the generated texture will use low dynamic range; overbright colors will be clamped ([Image.FORMAT_RGBA8](class_image.md#class-image-constant-format-rgba8) format).

---

[int](class_int.md#class-int) **width** = `256`

-  **set_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_width**()

The number of color samples that will be obtained from the [Gradient](class_gradient.md#class-gradient).
