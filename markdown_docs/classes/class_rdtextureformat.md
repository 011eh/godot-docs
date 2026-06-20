# RDTextureFormat

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture format (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [int](class_int.md#class-int)                                                        | array_layers           | `1`     |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|---------|
| [int](class_int.md#class-int)                                                        | depth                         | `1`     |
| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)               | format                       | `8`     |
| [int](class_int.md#class-int)                                                        | height                       | `1`     |
| [bool](class_bool.md#class-bool)                                                     | is_discardable       | `false` |
| [bool](class_bool.md#class-bool)                                                     | is_resolve_buffer | `false` |
| [int](class_int.md#class-int)                                                        | mipmaps                     | `1`     |
| [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples)       | samples                     | `0`     |
| [TextureType](class_renderingdevice.md#enum-renderingdevice-texturetype)             | texture_type           | `1`     |
| [[TextureUsageBits](class_renderingdevice.md#enum-renderingdevice-textureusagebits)] | usage_bits               | `0`     |
| [int](class_int.md#class-int)                                                        | width                         | `1`     |

## Methods

|    | add_shareable_format(format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))       |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | remove_shareable_format(format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)) |

---

## Property Descriptions

[int](class_int.md#class-int) **array_layers** = `1`

-  **set_array_layers**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_array_layers**()

The number of layers in the texture. Only relevant for 2D texture arrays.

---

[int](class_int.md#class-int) **depth** = `1`

-  **set_depth**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_depth**()

The texture's depth (in pixels). This is always `1` for 2D textures.

---

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **format** = `8`

-  **set_format**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_format**()

The texture's pixel data format.

---

[int](class_int.md#class-int) **height** = `1`

-  **set_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_height**()

The texture's height (in pixels).

---

[bool](class_bool.md#class-bool) **is_discardable** = `false`

-  **set_is_discardable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_is_discardable**()

If a texture is discardable, its contents do not need to be preserved between frames. This flag is only relevant when the texture is used as target in a draw list.

This information is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice) to figure out if a texture's contents can be discarded, eliminating unnecessary writes to memory and boosting performance.

---

[bool](class_bool.md#class-bool) **is_resolve_buffer** = `false`

-  **set_is_resolve_buffer**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_is_resolve_buffer**()

The texture will be used as the destination of a resolve operation.

---

[int](class_int.md#class-int) **mipmaps** = `1`

-  **set_mipmaps**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mipmaps**()

The number of mipmaps available in the texture.

---

[TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **samples** = `0`

-  **set_samples**(value: [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples))
- [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **get_samples**()

The number of samples used when sampling the texture.

---

[TextureType](class_renderingdevice.md#enum-renderingdevice-texturetype) **texture_type** = `1`

-  **set_texture_type**(value: [TextureType](class_renderingdevice.md#enum-renderingdevice-texturetype))
- [TextureType](class_renderingdevice.md#enum-renderingdevice-texturetype) **get_texture_type**()

The texture type.

---

[[TextureUsageBits](class_renderingdevice.md#enum-renderingdevice-textureusagebits)] **usage_bits** = `0`

-  **set_usage_bits**(value: [[TextureUsageBits](class_renderingdevice.md#enum-renderingdevice-textureusagebits)])
- [[TextureUsageBits](class_renderingdevice.md#enum-renderingdevice-textureusagebits)] **get_usage_bits**()

The texture's usage bits, which determine what can be done using the texture.

---

[int](class_int.md#class-int) **width** = `1`

-  **set_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_width**()

The texture's width (in pixels).

---

## Method Descriptions

 **add_shareable_format**(format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))

Adds `format` as a valid format for the corresponding [RDTextureView](class_rdtextureview.md#class-rdtextureview)'s [RDTextureView.format_override](class_rdtextureview.md#class-rdtextureview-property-format-override) property. If any format is added as shareable, then the main format must also be added.

---

 **remove_shareable_format**(format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))

Removes `format` from the list of valid formats that the corresponding [RDTextureView](class_rdtextureview.md#class-rdtextureview)'s [RDTextureView.format_override](class_rdtextureview.md#class-rdtextureview-property-format-override) property can be set to.
