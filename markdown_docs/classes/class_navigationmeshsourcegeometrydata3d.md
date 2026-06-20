# NavigationMeshSourceGeometryData3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Container for parsed source geometry data used in navigation mesh baking.

## Description

Container for parsed source geometry data used in navigation mesh baking.

## Methods

|                                                                            | add_faces(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), xform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                            |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                            | add_mesh(mesh: [Mesh](class_mesh.md#class-mesh), xform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                         |
|                                                                            | add_mesh_array(mesh_array: [Array](class_array.md#class-array), xform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                    |
|                                                                            | add_projected_obstruction(vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), elevation: [float](class_float.md#class-float), height: [float](class_float.md#class-float), carve: [bool](class_bool.md#class-bool)) |
|                                                                            | append_arrays(vertices: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array))                                                                                |
|                                                                            | clear()                                                                                                                                                                                                                                                                   |
|                                                                            | clear_projected_obstructions()                                                                                                                                                                                                                     |
| [AABB](class_aabb.md#class-aabb)                                           | get_bounds()                                                                                                                                                                                                                                                         |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | get_indices()                                                                                                                                                                                                                                                       |
| [Array](class_array.md#class-array)                                        | get_projected_obstructions()                                                                                                                                                                                                                         |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | get_vertices()                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                           | has_data()                                                                                                                                                                                                                                                             |
|                                                                            | merge(other_geometry: NavigationMeshSourceGeometryData3D)                                                                                                                                                                    |
|                                                                            | set_indices(indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array))                                                                                                                                                                          |
|                                                                            | set_projected_obstructions(projected_obstructions: [Array](class_array.md#class-array))                                                                                                                                                              |
|                                                                            | set_vertices(vertices: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))                                                                                                                                                                 |

---

## Method Descriptions

 **add_faces**(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), xform: [Transform3D](class_transform3d.md#class-transform3d))

Adds an array of vertex positions to the geometry data for navigation mesh baking to form triangulated faces. For each face the array must have three vertex positions in clockwise winding order. Since [NavigationMesh](class_navigationmesh.md#class-navigationmesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---

 **add_mesh**(mesh: [Mesh](class_mesh.md#class-mesh), xform: [Transform3D](class_transform3d.md#class-transform3d))

Adds the geometry data of a [Mesh](class_mesh.md#class-mesh) resource to the navigation mesh baking data. The mesh must have valid triangulated mesh data to be considered. Since [NavigationMesh](class_navigationmesh.md#class-navigationmesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---

 **add_mesh_array**(mesh_array: [Array](class_array.md#class-array), xform: [Transform3D](class_transform3d.md#class-transform3d))

Adds an [Array](class_array.md#class-array) the size of [Mesh.ARRAY_MAX](class_mesh.md#class-mesh-constant-array-max) and with vertices at index [Mesh.ARRAY_VERTEX](class_mesh.md#class-mesh-constant-array-vertex) and indices at index [Mesh.ARRAY_INDEX](class_mesh.md#class-mesh-constant-array-index) to the navigation mesh baking data. The array must have valid triangulated mesh data to be considered. Since [NavigationMesh](class_navigationmesh.md#class-navigationmesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---

 **add_projected_obstruction**(vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), elevation: [float](class_float.md#class-float), height: [float](class_float.md#class-float), carve: [bool](class_bool.md#class-bool))

Adds a projected obstruction shape to the source geometry. The `vertices` are considered projected on an xz-axes plane, placed at the global y-axis `elevation` and extruded by `height`. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.

---

 **append_arrays**(vertices: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Appends arrays of `vertices` and `indices` at the end of the existing arrays. Adds the existing index as an offset to the appended indices.

---

 **clear**()

Clears the internal data.

---

 **clear_projected_obstructions**()

Clears all projected obstructions.

---

[AABB](class_aabb.md#class-aabb) **get_bounds**()

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_indices**()

Returns the parsed source geometry data indices array.

---

[Array](class_array.md#class-array) **get_projected_obstructions**()

Returns the projected obstructions as an [Array](class_array.md#class-array) of dictionaries. Each [Dictionary](class_dictionary.md#class-dictionary) contains the following entries:

- `vertices` - A [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) that defines the outline points of the projected shape.
- `elevation` - A [float](class_float.md#class-float) that defines the projected shape placement on the y-axis.
- `height` - A [float](class_float.md#class-float) that defines how much the projected shape is extruded along the y-axis.
- `carve` - A [bool](class_bool.md#class-bool) that defines how the obstacle affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

---

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_vertices**()

Returns the parsed source geometry data vertices array.

---

[bool](class_bool.md#class-bool) **has_data**()

Returns `true` when parsed source geometry data exists.

---

 **merge**(other_geometry: NavigationMeshSourceGeometryData3D)

Adds the geometry data of another **NavigationMeshSourceGeometryData3D** to the navigation mesh baking data.

---

 **set_indices**(indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Sets the parsed source geometry data indices. The indices need to be matched with appropriated vertices.

**Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.

---

 **set_projected_obstructions**(projected_obstructions: [Array](class_array.md#class-array))

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:

GDScript

```gdscript
"vertices" : PackedFloat32Array
"elevation" : float
"height" : float
"carve" : bool
```

---

 **set_vertices**(vertices: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Sets the parsed source geometry data vertices. The vertices need to be matched with appropriated indices.

**Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.
