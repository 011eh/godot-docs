# RDAttachmentFormat

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Attachment format (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)         | format           | `36`   |
|--------------------------------------------------------------------------------|---------------------------------------------------------------|--------|
| [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) | samples         | `0`    |
| [int](class_int.md#class-int)                                                  | usage_flags | `0`    |

---

## Property Descriptions

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **format** = `36`

-  **set_format**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_format**()

The attachment's data format.

---

[TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **samples** = `0`

-  **set_samples**(value: [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples))
- [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **get_samples**()

The number of samples used when sampling the attachment.

---

[int](class_int.md#class-int) **usage_flags** = `0`

-  **set_usage_flags**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_usage_flags**()

The attachment's usage flags, which determine what can be done with it.
