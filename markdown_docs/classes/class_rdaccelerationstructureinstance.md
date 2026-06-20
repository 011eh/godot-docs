# RDAccelerationStructureInstance

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Acceleration structure instance (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

**RDAccelerationStructureInstance** describes an instance of a Bottom-Level Acceleration Structure (BLAS) used in the [RenderingDevice.tlas_build()](class_renderingdevice.md#class-renderingdevice-method-tlas-build) method.

## Properties

| [RID](class_rid.md#class-rid)                                                                                                  | blas                   | `RID()`                                           |
|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------|
| [[AccelerationStructureInstanceFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructureinstanceflagbits)] | flags                 | `0`                                               |
| [int](class_int.md#class-int)                                                                                                  | hit_sbt_range | `0`                                               |
| [int](class_int.md#class-int)                                                                                                  | id                       | `0`                                               |
| [int](class_int.md#class-int)                                                                                                  | mask                   | `255`                                             |
| [Transform3D](class_transform3d.md#class-transform3d)                                                                          | transform         | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |

---

## Property Descriptions

[RID](class_rid.md#class-rid) **blas** = `RID()`

-  **set_blas**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_blas**()

The BLAS referenced by this instance. If `null`, the instance is treated as a placeholder but still contributes to `gl_InstanceIndex` in GLSL.

---

[[AccelerationStructureInstanceFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructureinstanceflagbits)] **flags** = `0`

-  **set_flags**(value: [[AccelerationStructureInstanceFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructureinstanceflagbits)])
- [[AccelerationStructureInstanceFlagBits](class_renderingdevice.md#enum-renderingdevice-accelerationstructureinstanceflagbits)] **get_flags**()

Flags for the instance.

---

[int](class_int.md#class-int) **hit_sbt_range** = `0`

-  **set_hit_sbt_range**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_hit_sbt_range**()

Hit shader binding table range used for this instance, allocated using the [RenderingDevice.hit_sbt_range_alloc()](class_renderingdevice.md#class-renderingdevice-method-hit-sbt-range-alloc) method.

---

[int](class_int.md#class-int) **id** = `0`

-  **set_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_id**()

Custom instance ID that can be accessed in GLSL using `gl_InstanceCustomIndexEXT`.

---

[int](class_int.md#class-int) **mask** = `255`

-  **set_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mask**()

Visibility mask used to control which rays can intersect this instance.

---

[Transform3D](class_transform3d.md#class-transform3d) **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

-  **set_transform**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_transform**()

Transform applied to the referenced BLAS for this instance.
