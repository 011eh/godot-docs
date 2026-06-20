# CapsuleMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a capsule-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Description

Class representing a capsule-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Properties

| [float](class_float.md#class-float)   | height                   | `2.0`   |
|---------------------------------------|----------------------------------------------------------------|---------|
| [int](class_int.md#class-int)         | radial_segments | `64`    |
| [float](class_float.md#class-float)   | radius                   | `0.5`   |
| [int](class_int.md#class-int)         | rings                     | `8`     |

---

## Property Descriptions

[float](class_float.md#class-float) **height** = `2.0`

-  **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

Total height of the capsule mesh (including the hemispherical ends).

**Note:** The height of a capsule must be at least twice its radius. Otherwise, the capsule becomes a circle. If the height is less than twice the radius, the properties adjust to a valid value.

---

[int](class_int.md#class-int) **radial_segments** = `64`

-  **set_radial_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_radial_segments**()

Number of radial segments on the capsule mesh.

---

[float](class_float.md#class-float) **radius** = `0.5`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

Radius of the capsule mesh.

**Note:** The radius of a capsule cannot be greater than half of its height. Otherwise, the capsule becomes a circle. If the radius is greater than half of the height, the properties adjust to a valid value.

---

[int](class_int.md#class-int) **rings** = `8`

-  **set_rings**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_rings**()

Number of rings along the height of the capsule.
