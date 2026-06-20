# SphereMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a spherical [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Description

Class representing a spherical [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Properties

| [float](class_float.md#class-float)   | height                   | `1.0`   |
|---------------------------------------|---------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)      | is_hemisphere     | `false` |
| [int](class_int.md#class-int)         | radial_segments | `64`    |
| [float](class_float.md#class-float)   | radius                   | `0.5`   |
| [int](class_int.md#class-int)         | rings                     | `32`    |

---

## Property Descriptions

[float](class_float.md#class-float) **height** = `1.0`

-  **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

Full height of the sphere.

---

[bool](class_bool.md#class-bool) **is_hemisphere** = `false`

-  **set_is_hemisphere**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_is_hemisphere**()

If `true`, a hemisphere is created rather than a full sphere.

**Note:** To get a regular hemisphere, the height and radius of the sphere must be equal.

---

[int](class_int.md#class-int) **radial_segments** = `64`

-  **set_radial_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_radial_segments**()

Number of radial segments on the sphere.

---

[float](class_float.md#class-float) **radius** = `0.5`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

Radius of sphere.

---

[int](class_int.md#class-int) **rings** = `32`

-  **set_rings**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_rings**()

Number of segments along the height of the sphere.
