# RDPipelineRasterizationState

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline rasterization state (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [PolygonCullMode](class_renderingdevice.md#enum-renderingdevice-polygoncullmode)   | cull_mode                                   | `0`     |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------|
| [float](class_float.md#class-float)                                                | depth_bias_clamp                     | `0.0`   |
| [float](class_float.md#class-float)                                                | depth_bias_constant_factor | `0.0`   |
| [bool](class_bool.md#class-bool)                                                   | depth_bias_enabled                 | `false` |
| [float](class_float.md#class-float)                                                | depth_bias_slope_factor       | `0.0`   |
| [bool](class_bool.md#class-bool)                                                   | discard_primitives                 | `false` |
| [bool](class_bool.md#class-bool)                                                   | enable_depth_clamp                 | `false` |
| [PolygonFrontFace](class_renderingdevice.md#enum-renderingdevice-polygonfrontface) | front_face                                 | `0`     |
| [float](class_float.md#class-float)                                                | line_width                                 | `1.0`   |
| [int](class_int.md#class-int)                                                      | patch_control_points             | `1`     |
| [bool](class_bool.md#class-bool)                                                   | wireframe                                   | `false` |

---

## Property Descriptions

[PolygonCullMode](class_renderingdevice.md#enum-renderingdevice-polygoncullmode) **cull_mode** = `0`

-  **set_cull_mode**(value: [PolygonCullMode](class_renderingdevice.md#enum-renderingdevice-polygoncullmode))
- [PolygonCullMode](class_renderingdevice.md#enum-renderingdevice-polygoncullmode) **get_cull_mode**()

The cull mode to use when drawing polygons, which determines whether front faces or backfaces are hidden.

---

[float](class_float.md#class-float) **depth_bias_clamp** = `0.0`

-  **set_depth_bias_clamp**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_bias_clamp**()

A limit for how much each depth value can be offset. If negative, it serves as a minimum value, but if positive, it serves as a maximum value.

---

[float](class_float.md#class-float) **depth_bias_constant_factor** = `0.0`

-  **set_depth_bias_constant_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_bias_constant_factor**()

A constant offset added to each depth value. Applied after depth_bias_slope_factor.

---

[bool](class_bool.md#class-bool) **depth_bias_enabled** = `false`

-  **set_depth_bias_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_depth_bias_enabled**()

If `true`, each generated depth value will by offset by some amount. The specific amount is generated per polygon based on the values of depth_bias_slope_factor and depth_bias_constant_factor.

---

[float](class_float.md#class-float) **depth_bias_slope_factor** = `0.0`

-  **set_depth_bias_slope_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_bias_slope_factor**()

A constant scale applied to the slope of each polygons' depth. Applied before depth_bias_constant_factor.

---

[bool](class_bool.md#class-bool) **discard_primitives** = `false`

-  **set_discard_primitives**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_discard_primitives**()

If `true`, primitives are discarded immediately before the rasterization stage.

---

[bool](class_bool.md#class-bool) **enable_depth_clamp** = `false`

-  **set_enable_depth_clamp**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_depth_clamp**()

If `true`, clamps depth values according to the minimum and maximum depth of the associated viewport.

---

[PolygonFrontFace](class_renderingdevice.md#enum-renderingdevice-polygonfrontface) **front_face** = `0`

-  **set_front_face**(value: [PolygonFrontFace](class_renderingdevice.md#enum-renderingdevice-polygonfrontface))
- [PolygonFrontFace](class_renderingdevice.md#enum-renderingdevice-polygonfrontface) **get_front_face**()

The winding order to use to determine which face of a triangle is considered its front face.

---

[float](class_float.md#class-float) **line_width** = `1.0`

-  **set_line_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_width**()

The line width to use when drawing lines (in pixels). Thick lines may not be supported on all hardware.

---

[int](class_int.md#class-int) **patch_control_points** = `1`

-  **set_patch_control_points**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_patch_control_points**()

The number of control points to use when drawing a patch with tessellation enabled. Higher values result in higher quality at the cost of performance.

---

[bool](class_bool.md#class-bool) **wireframe** = `false`

-  **set_wireframe**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_wireframe**()

If `true`, performs wireframe rendering for triangles instead of flat or textured rendering.
