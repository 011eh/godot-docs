# RDPipelineMultisampleState

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline multisample state (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

**RDPipelineMultisampleState** is used to control how multisample or supersample antialiasing is being performed when rendering using [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [bool](class_bool.md#class-bool)                                               | enable_alpha_to_coverage   | `false`   |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------|
| [bool](class_bool.md#class-bool)                                               | enable_alpha_to_one             | `false`   |
| [bool](class_bool.md#class-bool)                                               | enable_sample_shading         | `false`   |
| [float](class_float.md#class-float)                                            | min_sample_shading               | `0.0`     |
| [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) | sample_count                           | `0`       |
| [Array](class_array.md#class-array)[[int](class_int.md#class-int)]             | sample_masks                           | `[]`      |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **enable_alpha_to_coverage** = `false`

-  **set_enable_alpha_to_coverage**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_alpha_to_coverage**()

If `true`, alpha to coverage is enabled. This generates a temporary coverage value based on the alpha component of the fragment's first color output. This allows alpha transparency to make use of multisample antialiasing.

---

[bool](class_bool.md#class-bool) **enable_alpha_to_one** = `false`

-  **set_enable_alpha_to_one**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_alpha_to_one**()

If `true`, alpha is forced to either `0.0` or `1.0`. This allows hardening the edges of antialiased alpha transparencies. Only relevant if enable_alpha_to_coverage is `true`.

---

[bool](class_bool.md#class-bool) **enable_sample_shading** = `false`

-  **set_enable_sample_shading**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_sample_shading**()

If `true`, enables per-sample shading which replaces MSAA by SSAA. This provides higher quality antialiasing that works with transparent (alpha scissor) edges. This has a very high performance cost. See also min_sample_shading. See the [per-sample shading Vulkan documentation](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#primsrast-sampleshading) for more details.

---

[float](class_float.md#class-float) **min_sample_shading** = `0.0`

-  **set_min_sample_shading**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_sample_shading**()

The multiplier of sample_count that determines how many samples are performed for each fragment. Must be between `0.0` and `1.0` (inclusive). Only effective if enable_sample_shading is `true`. If min_sample_shading is `1.0`, fragment invocation must only read from the coverage index sample. Tile image access must not be used if enable_sample_shading is *not* `1.0`.

---

[TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **sample_count** = `0`

-  **set_sample_count**(value: [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples))
- [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **get_sample_count**()

The number of MSAA samples (or SSAA samples if enable_sample_shading is `true`) to perform. Higher values result in better antialiasing, at the cost of performance.

---

[Array](class_array.md#class-array)[[int](class_int.md#class-int)] **sample_masks** = `[]`

-  **set_sample_masks**(value: [Array](class_array.md#class-array)[[int](class_int.md#class-int)])
- [Array](class_array.md#class-array)[[int](class_int.md#class-int)] **get_sample_masks**()

The sample mask array. See the [sample mask Vulkan documentation](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#fragops-samplemask) for more details.
