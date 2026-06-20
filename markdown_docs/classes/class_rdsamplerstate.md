# RDSamplerState

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Sampler state (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [float](class_float.md#class-float)                                                    | anisotropy_max     | `1.0`   |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------|---------|
| [SamplerBorderColor](class_renderingdevice.md#enum-renderingdevice-samplerbordercolor) | border_color         | `2`     |
| [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator)       | compare_op             | `7`     |
| [bool](class_bool.md#class-bool)                                                       | enable_compare     | `false` |
| [float](class_float.md#class-float)                                                    | lod_bias                 | `0.0`   |
| [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter)           | mag_filter             | `0`     |
| [float](class_float.md#class-float)                                                    | max_lod                   | `1e+20` |
| [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter)           | min_filter             | `0`     |
| [float](class_float.md#class-float)                                                    | min_lod                   | `0.0`   |
| [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter)           | mip_filter             | `0`     |
| [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode)   | repeat_u                 | `2`     |
| [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode)   | repeat_v                 | `2`     |
| [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode)   | repeat_w                 | `2`     |
| [bool](class_bool.md#class-bool)                                                       | unnormalized_uvw | `false` |
| [bool](class_bool.md#class-bool)                                                       | use_anisotropy     | `false` |

---

## Property Descriptions

[float](class_float.md#class-float) **anisotropy_max** = `1.0`

-  **set_anisotropy_max**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_anisotropy_max**()

Maximum anisotropy that can be used when sampling. Only effective if use_anisotropy is `true`. Higher values result in a sharper sampler at oblique angles, at the cost of performance (due to memory bandwidth). This value may be limited by the graphics hardware in use. Most graphics hardware only supports values up to `16.0`.

If anisotropy_max is `1.0`, forcibly disables anisotropy even if use_anisotropy is `true`.

---

[SamplerBorderColor](class_renderingdevice.md#enum-renderingdevice-samplerbordercolor) **border_color** = `2`

-  **set_border_color**(value: [SamplerBorderColor](class_renderingdevice.md#enum-renderingdevice-samplerbordercolor))
- [SamplerBorderColor](class_renderingdevice.md#enum-renderingdevice-samplerbordercolor) **get_border_color**()

The border color that will be returned when sampling outside the sampler's bounds and the repeat_u, repeat_v or repeat_w modes have repeating disabled.

---

[CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator) **compare_op** = `7`

-  **set_compare_op**(value: [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator))
- [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator) **get_compare_op**()

The compare operation to use. Only effective if enable_compare is `true`.

---

[bool](class_bool.md#class-bool) **enable_compare** = `false`

-  **set_enable_compare**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_compare**()

If `true`, returned values will be based on the comparison operation defined in compare_op. This is a hardware-based approach and is therefore faster than performing this manually in a shader. For example, compare operations are used for shadow map rendering by comparing depth values from a shadow sampler.

---

[float](class_float.md#class-float) **lod_bias** = `0.0`

-  **set_lod_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lod_bias**()

The mipmap LOD bias to use. Positive values will make the sampler blurrier at a given distance, while negative values will make the sampler sharper at a given distance (at the risk of looking grainy). Recommended values are between `-0.5` and `0.0`. Only effective if the sampler has mipmaps available.

---

[SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter) **mag_filter** = `0`

-  **set_mag_filter**(value: [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter))
- [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter) **get_mag_filter**()

The sampler's magnification filter. It is the filtering method used when sampling texels that appear bigger than on-screen pixels.

---

[float](class_float.md#class-float) **max_lod** = `1e+20`

-  **set_max_lod**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_lod**()

The maximum mipmap LOD bias to display (lowest resolution). Only effective if the sampler has mipmaps available.

---

[SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter) **min_filter** = `0`

-  **set_min_filter**(value: [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter))
- [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter) **get_min_filter**()

The sampler's minification filter. It is the filtering method used when sampling texels that appear smaller than on-screen pixels.

---

[float](class_float.md#class-float) **min_lod** = `0.0`

-  **set_min_lod**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_lod**()

The minimum mipmap LOD bias to display (highest resolution). Only effective if the sampler has mipmaps available.

---

[SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter) **mip_filter** = `0`

-  **set_mip_filter**(value: [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter))
- [SamplerFilter](class_renderingdevice.md#enum-renderingdevice-samplerfilter) **get_mip_filter**()

The filtering method to use for mipmaps.

---

[SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode) **repeat_u** = `2`

-  **set_repeat_u**(value: [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode))
- [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode) **get_repeat_u**()

The repeat mode to use along the U axis of UV coordinates. This affects the returned values if sampling outside the UV bounds.

---

[SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode) **repeat_v** = `2`

-  **set_repeat_v**(value: [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode))
- [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode) **get_repeat_v**()

The repeat mode to use along the V axis of UV coordinates. This affects the returned values if sampling outside the UV bounds.

---

[SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode) **repeat_w** = `2`

-  **set_repeat_w**(value: [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode))
- [SamplerRepeatMode](class_renderingdevice.md#enum-renderingdevice-samplerrepeatmode) **get_repeat_w**()

The repeat mode to use along the W axis of UV coordinates. This affects the returned values if sampling outside the UV bounds. Only effective for 3D samplers.

---

[bool](class_bool.md#class-bool) **unnormalized_uvw** = `false`

-  **set_unnormalized_uvw**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_unnormalized_uvw**()

If `true`, the texture will be sampled with coordinates ranging from 0 to the texture's resolution. Otherwise, the coordinates will be normalized and range from 0 to 1.

---

[bool](class_bool.md#class-bool) **use_anisotropy** = `false`

-  **set_use_anisotropy**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_anisotropy**()

If `true`, perform anisotropic sampling. See anisotropy_max.
