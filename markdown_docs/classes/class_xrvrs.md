# XRVRS

**Inherits:** [Object](class_object.md#class-object)

Helper class for XR interfaces that generates VRS images.

## Description

This class is used by various XR interfaces to generate VRS textures that can be used to speed up rendering.

## Properties

| [float](class_float.md#class-float)    | vrs_min_radius       | `20.0`               |
|----------------------------------------|--------------------------------------------------------------|----------------------|
| [Rect2i](class_rect2i.md#class-rect2i) | vrs_render_region | `Rect2i(0, 0, 0, 0)` |
| [float](class_float.md#class-float)    | vrs_strength           | `1.0`                |

## Methods

| [RID](class_rid.md#class-rid)   | make_vrs_texture(target_size: [Vector2](class_vector2.md#class-vector2), eye_foci: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))   |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

## Property Descriptions

[float](class_float.md#class-float) **vrs_min_radius** = `20.0`

-  **set_vrs_min_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_vrs_min_radius**()

The minimum radius around the focal point where full quality is guaranteed if VRS is used as a percentage of screen size.

---

[Rect2i](class_rect2i.md#class-rect2i) **vrs_render_region** = `Rect2i(0, 0, 0, 0)`

-  **set_vrs_render_region**(value: [Rect2i](class_rect2i.md#class-rect2i))
- [Rect2i](class_rect2i.md#class-rect2i) **get_vrs_render_region**()

The render region that the VRS texture will be scaled to when generated.

---

[float](class_float.md#class-float) **vrs_strength** = `1.0`

-  **set_vrs_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_vrs_strength**()

The strength used to calculate the VRS density map. The greater this value, the more noticeable VRS is.

---

## Method Descriptions

[RID](class_rid.md#class-rid) **make_vrs_texture**(target_size: [Vector2](class_vector2.md#class-vector2), eye_foci: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))

Generates the VRS texture based on a render `target_size` adjusted by our VRS tile size. For each eyes focal point passed in `eye_foci` a layer is created. Focal point should be in NDC.

The result will be cached, requesting a VRS texture with unchanged parameters and settings will return the cached RID.
