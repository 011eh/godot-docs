# PrismMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a prism-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Description

Class representing a prism-shaped [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Properties

| [float](class_float.md#class-float)       | left_to_right       | `0.5`              |
|-------------------------------------------|----------------------------------------------------------------|--------------------|
| [Vector3](class_vector3.md#class-vector3) | size                         | `Vector3(1, 1, 1)` |
| [int](class_int.md#class-int)             | subdivide_depth   | `0`                |
| [int](class_int.md#class-int)             | subdivide_height | `0`                |
| [int](class_int.md#class-int)             | subdivide_width   | `0`                |

---

## Property Descriptions

[float](class_float.md#class-float) **left_to_right** = `0.5`

-  **set_left_to_right**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_left_to_right**()

Displacement of the upper edge along the X axis. 0.0 positions edge straight above the bottom-left edge.

---

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(1, 1, 1)`

-  **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

Size of the prism.

---

[int](class_int.md#class-int) **subdivide_depth** = `0`

-  **set_subdivide_depth**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_subdivide_depth**()

Number of added edge loops along the Z axis.

---

[int](class_int.md#class-int) **subdivide_height** = `0`

-  **set_subdivide_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_subdivide_height**()

Number of added edge loops along the Y axis.

---

[int](class_int.md#class-int) **subdivide_width** = `0`

-  **set_subdivide_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_subdivide_width**()

Number of added edge loops along the X axis.
