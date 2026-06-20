# RDVertexAttribute

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Vertex attribute (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [int](class_int.md#class-int)                                                    | binding     | `4294967295`   |
|----------------------------------------------------------------------------------|----------------------------------------------------------|----------------|
| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)           | format       | `232`          |
| [VertexFrequency](class_renderingdevice.md#enum-renderingdevice-vertexfrequency) | frequency | `0`            |
| [int](class_int.md#class-int)                                                    | location   | `0`            |
| [int](class_int.md#class-int)                                                    | offset       | `0`            |
| [int](class_int.md#class-int)                                                    | stride       | `0`            |

---

## Property Descriptions

[int](class_int.md#class-int) **binding** = `4294967295`

-  **set_binding**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_binding**()

The index of the buffer in the vertex buffer array to bind this vertex attribute. When set to `-1`, it defaults to the index of the attribute.

**Note:** You cannot mix binding explicitly assigned attributes with implicitly assigned ones (i.e. `-1`). Either all attributes must have their binding set to `-1`, or all must have explicit bindings.

---

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **format** = `232`

-  **set_format**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_format**()

The way that this attribute's data is interpreted when sent to a shader.

---

[VertexFrequency](class_renderingdevice.md#enum-renderingdevice-vertexfrequency) **frequency** = `0`

-  **set_frequency**(value: [VertexFrequency](class_renderingdevice.md#enum-renderingdevice-vertexfrequency))
- [VertexFrequency](class_renderingdevice.md#enum-renderingdevice-vertexfrequency) **get_frequency**()

The rate at which this attribute is pulled from its vertex buffer.

---

[int](class_int.md#class-int) **location** = `0`

-  **set_location**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_location**()

The location in the shader that this attribute is bound to.

---

[int](class_int.md#class-int) **offset** = `0`

-  **set_offset**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_offset**()

The number of bytes between the start of the vertex buffer and the first instance of this attribute.

---

[int](class_int.md#class-int) **stride** = `0`

-  **set_stride**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stride**()

The number of bytes between the starts of consecutive instances of this attribute.
