# MeshConvexDecompositionSettings

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Parameters to be used with a [Mesh](class_mesh.md#class-mesh) convex decomposition operation.

## Description

Parameters to be used with a [Mesh](class_mesh.md#class-mesh) convex decomposition operation.

## Properties

| [bool](class_bool.md#class-bool)                   | convex_hull_approximation               | `true`   |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------|
| [int](class_int.md#class-int)                      | convex_hull_downsampling                 | `4`      |
| [float](class_float.md#class-float)                | max_concavity                                       | `1.0`    |
| [int](class_int.md#class-int)                      | max_convex_hulls                                 | `1`      |
| [int](class_int.md#class-int)                      | max_num_vertices_per_convex_hull | `32`     |
| [float](class_float.md#class-float)                | min_volume_per_convex_hull             | `0.0001` |
| Mode | mode                                                         | `0`      |
| [bool](class_bool.md#class-bool)                   | normalize_mesh                                     | `false`  |
| [int](class_int.md#class-int)                      | plane_downsampling                             | `4`      |
| [bool](class_bool.md#class-bool)                   | project_hull_vertices                       | `true`   |
| [int](class_int.md#class-int)                      | resolution                                             | `10000`  |
| [float](class_float.md#class-float)                | revolution_axes_clipping_bias       | `0.05`   |
| [float](class_float.md#class-float)                | symmetry_planes_clipping_bias       | `0.05`   |

---

## Enumerations

enum **Mode**:

Mode **CONVEX_DECOMPOSITION_MODE_VOXEL** = `0`

Constant for voxel-based approximate convex decomposition.

Mode **CONVEX_DECOMPOSITION_MODE_TETRAHEDRON** = `1`

Constant for tetrahedron-based approximate convex decomposition.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **convex_hull_approximation** = `true`

-  **set_convex_hull_approximation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_convex_hull_approximation**()

If `true`, uses approximation for computing convex hulls.

---

[int](class_int.md#class-int) **convex_hull_downsampling** = `4`

-  **set_convex_hull_downsampling**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_convex_hull_downsampling**()

Controls the precision of the convex-hull generation process during the clipping plane selection stage. Ranges from `1` to `16`.

---

[float](class_float.md#class-float) **max_concavity** = `1.0`

-  **set_max_concavity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_concavity**()

Maximum concavity. Ranges from `0.0` to `1.0`.

---

[int](class_int.md#class-int) **max_convex_hulls** = `1`

-  **set_max_convex_hulls**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_convex_hulls**()

The maximum number of convex hulls to produce from the merge operation.

---

[int](class_int.md#class-int) **max_num_vertices_per_convex_hull** = `32`

-  **set_max_num_vertices_per_convex_hull**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_num_vertices_per_convex_hull**()

Controls the maximum number of triangles per convex-hull. Ranges from `4` to `1024`.

---

[float](class_float.md#class-float) **min_volume_per_convex_hull** = `0.0001`

-  **set_min_volume_per_convex_hull**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_volume_per_convex_hull**()

Controls the adaptive sampling of the generated convex-hulls. Ranges from `0.0` to `0.01`.

---

Mode **mode** = `0`

-  **set_mode**(value: Mode)
- Mode **get_mode**()

Mode for the approximate convex decomposition.

---

[bool](class_bool.md#class-bool) **normalize_mesh** = `false`

-  **set_normalize_mesh**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_normalize_mesh**()

If `true`, normalizes the mesh before applying the convex decomposition.

---

[int](class_int.md#class-int) **plane_downsampling** = `4`

-  **set_plane_downsampling**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_plane_downsampling**()

Controls the granularity of the search for the "best" clipping plane. Ranges from `1` to `16`.

---

[bool](class_bool.md#class-bool) **project_hull_vertices** = `true`

-  **set_project_hull_vertices**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_project_hull_vertices**()

If `true`, projects output convex hull vertices onto the original source mesh to increase floating-point accuracy of the results.

---

[int](class_int.md#class-int) **resolution** = `10000`

-  **set_resolution**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_resolution**()

Maximum number of voxels generated during the voxelization stage.

---

[float](class_float.md#class-float) **revolution_axes_clipping_bias** = `0.05`

-  **set_revolution_axes_clipping_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_revolution_axes_clipping_bias**()

Controls the bias toward clipping along revolution axes. Ranges from `0.0` to `1.0`.

---

[float](class_float.md#class-float) **symmetry_planes_clipping_bias** = `0.05`

-  **set_symmetry_planes_clipping_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_symmetry_planes_clipping_bias**()

Controls the bias toward clipping along symmetry planes. Ranges from `0.0` to `1.0`.
