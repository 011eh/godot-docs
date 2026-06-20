# ArrayMesh

**Inherits:** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

[Mesh](class_mesh.md#class-mesh) type that provides utility for constructing a surface from arrays.

## Description

The **ArrayMesh** is used to construct a [Mesh](class_mesh.md#class-mesh) by specifying the attributes as arrays.

The most basic example is the creation of a single triangle:

GDScript

```gdscript
var vertices = PackedVector3Array()
vertices.push_back(Vector3(0, 1, 0))
vertices.push_back(Vector3(1, 0, 0))
vertices.push_back(Vector3(0, 0, 1))

# Initialize the ArrayMesh.
var arr_mesh = ArrayMesh.new()
var arrays = []
arrays.resize(Mesh.ARRAY_MAX)
arrays[Mesh.ARRAY_VERTEX] = vertices

# Create the Mesh.
arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
var m = MeshInstance3D.new()
m.mesh = arr_mesh
```

C#

```csharp
Vector3[] vertices =
[
    new Vector3(0, 1, 0),
    new Vector3(1, 0, 0),
    new Vector3(0, 0, 1),
];

// Initialize the ArrayMesh.
var arrMesh = new ArrayMesh();
Godot.Collections.Array arrays = [];
arrays.Resize((int)Mesh.ArrayType.Max);
arrays[(int)Mesh.ArrayType.Vertex] = vertices;

// Create the Mesh.
arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, arrays);
var m = new MeshInstance3D();
m.Mesh = arrMesh;
```

The [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) is ready to be added to the [SceneTree](class_scenetree.md#class-scenetree) to be shown.

See also [ImmediateMesh](class_immediatemesh.md#class-immediatemesh), [MeshDataTool](class_meshdatatool.md#class-meshdatatool) and [SurfaceTool](class_surfacetool.md#class-surfacetool) for procedural geometry generation.

**Note:** Godot uses clockwise [winding order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front faces of triangle primitive modes.

## Tutorials

- [Procedural geometry using the ArrayMesh](../tutorials/3d/procedural_geometry/arraymesh.md)

## Properties

| [BlendShapeMode](class_mesh.md#enum-mesh-blendshapemode)   | blend_shape_mode   | `1`                      |
|------------------------------------------------------------|------------------------------------------------------------------|--------------------------|
| [AABB](class_aabb.md#class-aabb)                           | custom_aabb             | `AABB(0, 0, 0, 0, 0, 0)` |
| ArrayMesh                              | shadow_mesh             |                          |

## Methods

|                                                        | add_blend_shape(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                        | add_surface_from_arrays(primitive: [PrimitiveType](class_mesh.md#enum-mesh-primitivetype), arrays: [Array](class_array.md#class-array), blend_shapes: [Array](class_array.md#class-array)[[Array](class_array.md#class-array)] = [], lods: [Dictionary](class_dictionary.md#class-dictionary) = {}, flags: [[ArrayFormat](class_mesh.md#enum-mesh-arrayformat)] = 0) |
|                                                        | clear_blend_shapes()                                                                                                                                                                                                                                                                                                                                                      |
|                                                        | clear_surfaces()                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                          | get_blend_shape_count()                                                                                                                                                                                                                                                                                                                                                |
| [StringName](class_stringname.md#class-stringname)     | get_blend_shape_name(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                              |
| [Error](class_@globalscope.md#enum-globalscope-error)  | lightmap_unwrap(transform: [Transform3D](class_transform3d.md#class-transform3d), texel_size: [float](class_float.md#class-float))                                                                                                                                                                                                                                           |
|                                                        | regen_normal_maps()                                                                                                                                                                                                                                                                                                                                                        |
|                                                        | set_blend_shape_name(index: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                          | surface_find_by_name(name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                          | surface_get_array_index_len(surf_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                          | surface_get_array_len(surf_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                         |
| [[ArrayFormat](class_mesh.md#enum-mesh-arrayformat)]   | surface_get_format(surf_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                               |
| [String](class_string.md#class-string)                 | surface_get_name(surf_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                   |
| [PrimitiveType](class_mesh.md#enum-mesh-primitivetype) | surface_get_primitive_type(surf_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                               |
|                                                        | surface_remove(surf_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                       |
|                                                        | surface_set_name(surf_idx: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                     |
|                                                        | surface_update_attribute_region(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                     |
|                                                        | surface_update_skin_region(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                               |
|                                                        | surface_update_vertex_region(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                           |

---

## Property Descriptions

[BlendShapeMode](class_mesh.md#enum-mesh-blendshapemode) **blend_shape_mode** = `1`

-  **set_blend_shape_mode**(value: [BlendShapeMode](class_mesh.md#enum-mesh-blendshapemode))
- [BlendShapeMode](class_mesh.md#enum-mesh-blendshapemode) **get_blend_shape_mode**()

The blend shape mode.

---

[AABB](class_aabb.md#class-aabb) **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)`

-  **set_custom_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_custom_aabb**()

Overrides the [AABB](class_aabb.md#class-aabb) with one defined by user for use with frustum culling. Especially useful to avoid unexpected culling when using a shader to offset vertices.

---

ArrayMesh **shadow_mesh**

-  **set_shadow_mesh**(value: ArrayMesh)
- ArrayMesh **get_shadow_mesh**()

An optional mesh which can be used for rendering shadows and the depth prepass. Can be used to increase performance by supplying a mesh with fused vertices and only vertex position data (without normals, UVs, colors, etc.).

**Note:** This mesh must have exactly the same vertex positions as the source mesh (including the source mesh's LODs, if present). If vertex positions differ, then the mesh will not draw correctly.

---

## Method Descriptions

 **add_blend_shape**(name: [StringName](class_stringname.md#class-stringname))

Adds name for a blend shape that will be added with add_surface_from_arrays(). Must be called before surface is added.

---

 **add_surface_from_arrays**(primitive: [PrimitiveType](class_mesh.md#enum-mesh-primitivetype), arrays: [Array](class_array.md#class-array), blend_shapes: [Array](class_array.md#class-array)[[Array](class_array.md#class-array)] = [], lods: [Dictionary](class_dictionary.md#class-dictionary) = {}, flags: [[ArrayFormat](class_mesh.md#enum-mesh-arrayformat)] = 0)

Creates a new surface. [Mesh.get_surface_count()](class_mesh.md#class-mesh-method-get-surface-count) will become the `surf_idx` for this new surface.

Surfaces are created to be rendered using a `primitive`, which may be any of the values defined in [PrimitiveType](class_mesh.md#enum-mesh-primitivetype).

The `arrays` argument is an array of arrays. Each of the [Mesh.ARRAY_MAX](class_mesh.md#class-mesh-constant-array-max) elements contains an array with some of the mesh data for this surface as described by the corresponding member of [ArrayType](class_mesh.md#enum-mesh-arraytype) or `null` if it is not used by the surface. For example, `arrays[0]` is the array of vertices. That first vertex sub-array is always required; the others are optional. Adding an index array puts this surface into "index mode" where the vertex and other arrays become the sources of data and the index array defines the vertex order. All sub-arrays must have the same length as the vertex array (or be an exact multiple of the vertex array's length, when multiple elements of a sub-array correspond to a single vertex) or be empty, except for [Mesh.ARRAY_INDEX](class_mesh.md#class-mesh-constant-array-index) if it is used.

The `blend_shapes` argument is an array of vertex data for each blend shape. Each element is an array of the same structure as `arrays`, but [Mesh.ARRAY_VERTEX](class_mesh.md#class-mesh-constant-array-vertex), [Mesh.ARRAY_NORMAL](class_mesh.md#class-mesh-constant-array-normal), and [Mesh.ARRAY_TANGENT](class_mesh.md#class-mesh-constant-array-tangent) are set if and only if they are set in `arrays` and all other entries are `null`.

The `lods` argument is a dictionary with [float](class_float.md#class-float) keys and [PackedInt32Array](class_packedint32array.md#class-packedint32array) values. Each entry in the dictionary represents an LOD level of the surface, where the value is the [Mesh.ARRAY_INDEX](class_mesh.md#class-mesh-constant-array-index) array to use for the LOD level and the key is roughly proportional to the distance at which the LOD stats being used. I.e., increasing the key of an LOD also increases the distance that the objects has to be from the camera before the LOD is used.

The `flags` argument is the bitwise OR of, as required: One value of [ArrayCustomFormat](class_mesh.md#enum-mesh-arraycustomformat) left shifted by `ARRAY_FORMAT_CUSTOMn_SHIFT` for each custom channel in use, [Mesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE](class_mesh.md#class-mesh-constant-array-flag-use-dynamic-update), [Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS](class_mesh.md#class-mesh-constant-array-flag-use-8-bone-weights), or [Mesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY](class_mesh.md#class-mesh-constant-array-flag-uses-empty-vertex-array).

**Note:** When using indices, it is recommended to only use points, lines, or triangles.

---

 **clear_blend_shapes**()

Removes all blend shapes from this **ArrayMesh**.

---

 **clear_surfaces**()

Removes all surfaces from this **ArrayMesh**.

---

[int](class_int.md#class-int) **get_blend_shape_count**()

Returns the number of blend shapes that the **ArrayMesh** holds.

---

[StringName](class_stringname.md#class-stringname) **get_blend_shape_name**(index: [int](class_int.md#class-int))

Returns the name of the blend shape at this index.

---

[Error](class_@globalscope.md#enum-globalscope-error) **lightmap_unwrap**(transform: [Transform3D](class_transform3d.md#class-transform3d), texel_size: [float](class_float.md#class-float))

Performs a UV unwrap on the **ArrayMesh** to prepare the mesh for lightmapping.

---

 **regen_normal_maps**()

Regenerates tangents for each of the **ArrayMesh**'s surfaces.

---

 **set_blend_shape_name**(index: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname))

Sets the name of the blend shape at this index.

---

[int](class_int.md#class-int) **surface_find_by_name**(name: [String](class_string.md#class-string))

Returns the index of the first surface with this name held within this **ArrayMesh**. If none are found, -1 is returned.

---

[int](class_int.md#class-int) **surface_get_array_index_len**(surf_idx: [int](class_int.md#class-int))

Returns the length in indices of the index array in the requested surface (see add_surface_from_arrays()).

---

[int](class_int.md#class-int) **surface_get_array_len**(surf_idx: [int](class_int.md#class-int))

Returns the length in vertices of the vertex array in the requested surface (see add_surface_from_arrays()).

---

[[ArrayFormat](class_mesh.md#enum-mesh-arrayformat)] **surface_get_format**(surf_idx: [int](class_int.md#class-int))

Returns the format mask of the requested surface (see add_surface_from_arrays()).

---

[String](class_string.md#class-string) **surface_get_name**(surf_idx: [int](class_int.md#class-int))

Gets the name assigned to this surface.

---

[PrimitiveType](class_mesh.md#enum-mesh-primitivetype) **surface_get_primitive_type**(surf_idx: [int](class_int.md#class-int))

Returns the primitive type of the requested surface (see add_surface_from_arrays()).

---

 **surface_remove**(surf_idx: [int](class_int.md#class-int))

Removes the surface at the given index from the Mesh, shifting surfaces with higher index down by one.

---

 **surface_set_name**(surf_idx: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets a name for a given surface.

---

 **surface_update_attribute_region**(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Updates the attribute buffer of this mesh's surface with the given `data`. The expected data per attribute is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class-vector3) or [Vector2](class_vector2.md#class-vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_attribute_stride()](class_renderingserver.md#class-renderingserver-method-mesh-surface-get-format-attribute-stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each attribute.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of attribute locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.

---

 **surface_update_skin_region**(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Updates the skin buffer of this mesh's surface with the given `data`. The expected data per skin is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class-vector3) or [Vector2](class_vector2.md#class-vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_skin_stride()](class_renderingserver.md#class-renderingserver-method-mesh-surface-get-format-skin-stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each skin.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of skin locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.

---

 **surface_update_vertex_region**(surf_idx: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Updates the vertex buffer of this mesh's surface with the given `data`. The expected data per vertex is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class-vector3) or [Vector2](class_vector2.md#class-vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_vertex_stride()](class_renderingserver.md#class-renderingserver-method-mesh-surface-get-format-vertex-stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each vertex.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of vertex locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.
