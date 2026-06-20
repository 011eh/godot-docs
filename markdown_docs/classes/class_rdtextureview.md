# RDTextureView

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture view (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)         | format_override   | `232`   |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------|---------|
| [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) | swizzle_a               | `6`     |
| [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) | swizzle_b               | `5`     |
| [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) | swizzle_g               | `4`     |
| [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) | swizzle_r               | `3`     |

---

## Property Descriptions

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **format_override** = `232`

-  **set_format_override**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_format_override**()

Optional override for the data format to return sampled values in. The corresponding [RDTextureFormat](class_rdtextureformat.md#class-rdtextureformat) must have had this added as a shareable format. The default value of [RenderingDevice.DATA_FORMAT_MAX](class_renderingdevice.md#class-renderingdevice-constant-data-format-max) does not override the format.

---

[TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **swizzle_a** = `6`

-  **set_swizzle_a**(value: [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle))
- [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **get_swizzle_a**()

The channel to sample when sampling the alpha channel.

---

[TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **swizzle_b** = `5`

-  **set_swizzle_b**(value: [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle))
- [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **get_swizzle_b**()

The channel to sample when sampling the blue color channel.

---

[TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **swizzle_g** = `4`

-  **set_swizzle_g**(value: [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle))
- [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **get_swizzle_g**()

The channel to sample when sampling the green color channel.

---

[TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **swizzle_r** = `3`

-  **set_swizzle_r**(value: [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle))
- [TextureSwizzle](class_renderingdevice.md#enum-renderingdevice-textureswizzle) **get_swizzle_r**()

The channel to sample when sampling the red color channel.
