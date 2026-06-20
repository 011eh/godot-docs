# CurveXYZTexture

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 1D texture where the red, green, and blue color channels correspond to points on 3 curves.

## Description

A 1D texture where the red, green, and blue color channels correspond to points on 3 unit [Curve](class_curve.md#class-curve) resources. Compared to using separate [CurveTexture](class_curvetexture.md#class-curvetexture)s, this further simplifies the task of saving curves as image files.

If you only need to store one curve within a single texture, use [CurveTexture](class_curvetexture.md#class-curvetexture) instead. See also [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d) and [GradientTexture2D](class_gradienttexture2d.md#class-gradienttexture2d).

## Properties

| [Curve](class_curve.md#class-curve)   | curve_x   |                                                                                                   |
|---------------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [Curve](class_curve.md#class-curve)   | curve_y   |                                                                                                   |
| [Curve](class_curve.md#class-curve)   | curve_z   |                                                                                                   |
| [bool](class_bool.md#class-bool)      | resource_local_to_scene                              | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [int](class_int.md#class-int)         | width       | `256`                                                                                             |

---

## Property Descriptions

[Curve](class_curve.md#class-curve) **curve_x**

-  **set_curve_x**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_curve_x**()

The [Curve](class_curve.md#class-curve) that is rendered onto the texture's red channel. Should be a unit [Curve](class_curve.md#class-curve).

---

[Curve](class_curve.md#class-curve) **curve_y**

-  **set_curve_y**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_curve_y**()

The [Curve](class_curve.md#class-curve) that is rendered onto the texture's green channel. Should be a unit [Curve](class_curve.md#class-curve).

---

[Curve](class_curve.md#class-curve) **curve_z**

-  **set_curve_z**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_curve_z**()

The [Curve](class_curve.md#class-curve) that is rendered onto the texture's blue channel. Should be a unit [Curve](class_curve.md#class-curve).

---

[int](class_int.md#class-int) **width** = `256`

-  **set_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_width**()

The width of the texture (in pixels). Higher values make it possible to represent high-frequency data better (such as sudden direction changes), at the cost of increased generation time and memory usage.
