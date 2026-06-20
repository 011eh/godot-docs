# CylinderMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class representing a cylindrical [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

## Description

Class representing a cylindrical [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh). This class can be used to create cones by setting either the top_radius or bottom_radius properties to `0.0`.

## Properties

| [float](class_float.md#class-float)   | bottom_radius     | `0.5`   |
|---------------------------------------|-----------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)      | cap_bottom           | `true`  |
| [bool](class_bool.md#class-bool)      | cap_top                 | `true`  |
| [float](class_float.md#class-float)   | height                   | `2.0`   |
| [int](class_int.md#class-int)         | radial_segments | `64`    |
| [int](class_int.md#class-int)         | rings                     | `4`     |
| [float](class_float.md#class-float)   | top_radius           | `0.5`   |

---

## Property Descriptions

[float](class_float.md#class-float) **bottom_radius** = `0.5`

-  **set_bottom_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bottom_radius**()

Bottom radius of the cylinder. If set to `0.0`, the bottom faces will not be generated, resulting in a conic shape. See also cap_bottom.

---

[bool](class_bool.md#class-bool) **cap_bottom** = `true`

-  **set_cap_bottom**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_cap_bottom**()

If `true`, generates a cap at the bottom of the cylinder. This can be set to `false` to speed up generation and rendering when the cap is never seen by the camera. See also bottom_radius.

**Note:** If bottom_radius is `0.0`, cap generation is always skipped even if cap_bottom is `true`.

---

[bool](class_bool.md#class-bool) **cap_top** = `true`

-  **set_cap_top**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_cap_top**()

If `true`, generates a cap at the top of the cylinder. This can be set to `false` to speed up generation and rendering when the cap is never seen by the camera. See also top_radius.

**Note:** If top_radius is `0.0`, cap generation is always skipped even if cap_top is `true`.

---

[float](class_float.md#class-float) **height** = `2.0`

-  **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

Full height of the cylinder.

---

[int](class_int.md#class-int) **radial_segments** = `64`

-  **set_radial_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_radial_segments**()

Number of radial segments on the cylinder. Higher values result in a more detailed cylinder/cone at the cost of performance.

---

[int](class_int.md#class-int) **rings** = `4`

-  **set_rings**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_rings**()

Number of edge rings along the height of the cylinder. Changing rings does not have any visual impact unless a shader or procedural mesh tool is used to alter the vertex data. Higher values result in more subdivisions, which can be used to create smoother-looking effects with shaders or procedural mesh tools (at the cost of performance). When not altering the vertex data using a shader or procedural mesh tool, rings should be kept to its default value.

---

[float](class_float.md#class-float) **top_radius** = `0.5`

-  **set_top_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_top_radius**()

Top radius of the cylinder. If set to `0.0`, the top faces will not be generated, resulting in a conic shape. See also cap_top.
