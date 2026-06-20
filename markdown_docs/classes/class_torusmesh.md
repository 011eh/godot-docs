# TorusMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a torus [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Description

Class representing a torus [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Properties

| [float](class_float.md#class-float)   | inner_radius   | `0.5`   |
|---------------------------------------|----------------------------------------------------------|---------|
| [float](class_float.md#class-float)   | outer_radius   | `1.0`   |
| [int](class_int.md#class-int)         | ring_segments | `32`    |
| [int](class_int.md#class-int)         | rings                 | `64`    |

---

## Property Descriptions

[float](class_float.md#class-float) **inner_radius** = `0.5`

-  **set_inner_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_inner_radius**()

The inner radius of the torus.

---

[float](class_float.md#class-float) **outer_radius** = `1.0`

-  **set_outer_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_outer_radius**()

The outer radius of the torus.

---

[int](class_int.md#class-int) **ring_segments** = `32`

-  **set_ring_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_ring_segments**()

The number of edges each ring of the torus is constructed of.

---

[int](class_int.md#class-int) **rings** = `64`

-  **set_rings**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_rings**()

The number of slices the torus is constructed of.
