# RDAccelerationStructureGeometry

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Acceleration structure geometry (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

**RDAccelerationStructureGeometry** describes a set of triangles used as raytracing geometry in the [RenderingDevice.blas_create()](class_renderingdevice.md#class-renderingdevice-method-blas-create) method.

The geometry is always in triangle list form, either indexed or non-indexed. Triangle strips are not supported.

## Properties

| [[AccelerationStructureGeometryFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructuregeometryflagbits)]   | flags                 | `0`     |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|---------|
| [RID](class_rid.md#class-rid)                                                                                                    | index_buffer   | `RID()` |
| [int](class_int.md#class-int)                                                                                                    | index_count     | `0`     |
| [int](class_int.md#class-int)                                                                                                    | index_offset   | `0`     |
| [RID](class_rid.md#class-rid)                                                                                                    | vertex_buffer | `RID()` |
| [int](class_int.md#class-int)                                                                                                    | vertex_count   | `0`     |
| [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat)                                                           | vertex_format | `232`   |
| [int](class_int.md#class-int)                                                                                                    | vertex_offset | `0`     |
| [int](class_int.md#class-int)                                                                                                    | vertex_stride | `0`     |

---

## Property Descriptions

[[AccelerationStructureGeometryFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructuregeometryflagbits)] **flags** = `0`

-  **set_flags**(value: [[AccelerationStructureGeometryFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructuregeometryflagbits)])
- [[AccelerationStructureGeometryFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructuregeometryflagbits)] **get_flags**()

Flags for the geometry.

---

[RID](class_rid.md#class-rid) **index_buffer** = `RID()`

-  **set_index_buffer**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_index_buffer**()

Buffer containing vertex indices. If `null`, triangles are non-indexed.

---

[int](class_int.md#class-int) **index_count** = `0`

-  **set_index_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_index_count**()

Number of indices used by this geometry in index_buffer.

---

[int](class_int.md#class-int) **index_offset** = `0`

-  **set_index_offset**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_index_offset**()

Byte offset of the first index in index_buffer.

---

[RID](class_rid.md#class-rid) **vertex_buffer** = `RID()`

-  **set_vertex_buffer**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_vertex_buffer**()

Buffer containing vertices.

---

[int](class_int.md#class-int) **vertex_count** = `0`

-  **set_vertex_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vertex_count**()

Number of vertices used by this geometry in vertex_buffer.

---

[DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **vertex_format** = `232`

-  **set_vertex_format**(value: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat))
- [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat) **get_vertex_format**()

Format of the vertices in vertex_buffer.

---

[int](class_int.md#class-int) **vertex_offset** = `0`

-  **set_vertex_offset**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vertex_offset**()

Byte offset of the first vertex in vertex_buffer.

---

[int](class_int.md#class-int) **vertex_stride** = `0`

-  **set_vertex_stride**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vertex_stride**()

Number of bytes between each vertex in vertex_buffer.
