# RenderSceneBuffersConfiguration

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration object used to setup a [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) object.

## Description

This configuration object is created and populated by the render engine on a viewport change and used to (re)configure a [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) object.

## Properties

| [ViewportAnisotropicFiltering](class_renderingserver.md#enum-renderingserver-viewportanisotropicfiltering)   | anisotropic_filtering_level   | `2`              |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| [float](class_float.md#class-float)                                                                          | fsr_sharpness                               | `0.0`            |
| [Vector2i](class_vector2i.md#class-vector2i)                                                                 | internal_size                               | `Vector2i(0, 0)` |
| [ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa)                                   | msaa_3d                                           | `0`              |
| [RID](class_rid.md#class-rid)                                                                                | render_target                               | `RID()`          |
| [ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode)                 | scaling_3d_mode                           | `255`            |
| [ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa)                 | screen_space_aa                           | `0`              |
| [Vector2i](class_vector2i.md#class-vector2i)                                                                 | target_size                                   | `Vector2i(0, 0)` |
| [float](class_float.md#class-float)                                                                          | texture_mipmap_bias                   | `0.0`            |
| [int](class_int.md#class-int)                                                                                | view_count                                     | `1`              |

---

## Property Descriptions

[ViewportAnisotropicFiltering](class_renderingserver.md#enum-renderingserver-viewportanisotropicfiltering) **anisotropic_filtering_level** = `2`

-  **set_anisotropic_filtering_level**(value: [ViewportAnisotropicFiltering](class_renderingserver.md#enum-renderingserver-viewportanisotropicfiltering))
- [ViewportAnisotropicFiltering](class_renderingserver.md#enum-renderingserver-viewportanisotropicfiltering) **get_anisotropic_filtering_level**()

Level of the anisotropic filter.

---

[float](class_float.md#class-float) **fsr_sharpness** = `0.0`

-  **set_fsr_sharpness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fsr_sharpness**()

FSR Sharpness applicable if FSR upscaling is used.

---

[Vector2i](class_vector2i.md#class-vector2i) **internal_size** = `Vector2i(0, 0)`

-  **set_internal_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_internal_size**()

The size of the 3D render buffer used for rendering.

---

[ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa) **msaa_3d** = `0`

-  **set_msaa_3d**(value: [ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa))
- [ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa) **get_msaa_3d**()

The MSAA mode we're using for 3D rendering.

---

[RID](class_rid.md#class-rid) **render_target** = `RID()`

-  **set_render_target**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_render_target**()

The render target associated with these buffer.

---

[ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode) **scaling_3d_mode** = `255`

-  **set_scaling_3d_mode**(value: [ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode))
- [ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode) **get_scaling_3d_mode**()

The requested scaling mode with which we upscale/downscale if internal_size and target_size are not equal.

---

[ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa) **screen_space_aa** = `0`

-  **set_screen_space_aa**(value: [ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa))
- [ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa) **get_screen_space_aa**()

The requested screen space AA applied in post processing.

---

[Vector2i](class_vector2i.md#class-vector2i) **target_size** = `Vector2i(0, 0)`

-  **set_target_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_target_size**()

The target (upscale) size if scaling is used.

---

[float](class_float.md#class-float) **texture_mipmap_bias** = `0.0`

-  **set_texture_mipmap_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_mipmap_bias**()

Bias applied to mipmaps.

**Note:** This property is only supported in the Forward+ and Mobile renderers, not Compatibility. In Compatibility, this property is always treated as if it was set to `0.0`.

---

[int](class_int.md#class-int) **view_count** = `1`

-  **set_view_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_view_count**()

The number of views we're rendering.
