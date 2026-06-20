# Mesh

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [ArrayMesh](class_arraymesh.md#class-arraymesh), [ImmediateMesh](class_immediatemesh.md#class-immediatemesh), [PlaceholderMesh](class_placeholdermesh.md#class-placeholdermesh), [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh)

A [Resource](class_resource.md#class-resource) that contains vertex array-based geometry.

## Description

Mesh is a type of [Resource](class_resource.md#class-resource) that contains vertex array-based geometry, divided in *surfaces*. Each surface contains a completely separate array and a material used to draw it. Design wise, a mesh with multiple surfaces is preferred to a single surface, because objects created in 3D editing software commonly contain multiple materials. The maximum number of surfaces per mesh is [RenderingServer.MAX_MESH_SURFACES](class_renderingserver.md#class-renderingserver-constant-max-mesh-surfaces).

## Tutorials

- [3D Material Testers Demo](https://godotengine.org/asset-library/asset/2742)
- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [Vector2i](class_vector2i.md#class-vector2i)   | lightmap_size_hint   | `Vector2i(0, 0)`   |
|------------------------------------------------|-----------------------------------------------------------------|--------------------|

## Methods

| [AABB](class_aabb.md#class-aabb)                                                    | \_get_aabb()                                                                                                                       |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                                       | \_get_blend_shape_count()                                                                                             |
| [StringName](class_stringname.md#class-stringname)                                  | \_get_blend_shape_name(index: [int](class_int.md#class-int))                                                           |
| [int](class_int.md#class-int)                                                       | \_get_surface_count()                                                                                                     |
|                                                                                     | \_set_blend_shape_name(index: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname)) |
| [int](class_int.md#class-int)                                                       | \_surface_get_array_index_len(index: [int](class_int.md#class-int))                                             |
| [int](class_int.md#class-int)                                                       | \_surface_get_array_len(index: [int](class_int.md#class-int))                                                         |
| [Array](class_array.md#class-array)                                                 | \_surface_get_arrays(index: [int](class_int.md#class-int))                                                               |
| [Array](class_array.md#class-array)[[Array](class_array.md#class-array)]            | \_surface_get_blend_shape_arrays(index: [int](class_int.md#class-int))                                       |
| [int](class_int.md#class-int)                                                       | \_surface_get_format(index: [int](class_int.md#class-int))                                                               |
| [Dictionary](class_dictionary.md#class-dictionary)                                  | \_surface_get_lods(index: [int](class_int.md#class-int))                                                                   |
| [Material](class_material.md#class-material)                                        | \_surface_get_material(index: [int](class_int.md#class-int))                                                           |
| [int](class_int.md#class-int)                                                       | \_surface_get_primitive_type(index: [int](class_int.md#class-int))                                               |
|                                                                                     | \_surface_set_material(index: [int](class_int.md#class-int), material: [Material](class_material.md#class-material))   |
| [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class-convexpolygonshape3d)    | create_convex_shape(clean: [bool](class_bool.md#class-bool) = true, simplify: [bool](class_bool.md#class-bool) = false)         |
| Mesh                                                                 | create_outline(margin: [float](class_float.md#class-float))                                                                          |
| [Resource](class_resource.md#class-resource)                                        | create_placeholder()                                                                                                             |
| [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d) | create_trimesh_shape()                                                                                                         |
| [TriangleMesh](class_trianglemesh.md#class-trianglemesh)                            | generate_triangle_mesh()                                                                                                     |
| [AABB](class_aabb.md#class-aabb)                                                    | get_aabb()                                                                                                                                 |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)          | get_faces()                                                                                                                               |
| [int](class_int.md#class-int)                                                       | get_surface_count()                                                                                                               |
| [Array](class_array.md#class-array)                                                 | surface_get_arrays(surf_idx: [int](class_int.md#class-int))                                                                      |
| [Array](class_array.md#class-array)[[Array](class_array.md#class-array)]            | surface_get_blend_shape_arrays(surf_idx: [int](class_int.md#class-int))                                              |
| [Material](class_material.md#class-material)                                        | surface_get_material(surf_idx: [int](class_int.md#class-int))                                                                  |
|                                                                                     | surface_set_material(surf_idx: [int](class_int.md#class-int), material: [Material](class_material.md#class-material))          |

---

## Enumerations

enum **PrimitiveType**:

PrimitiveType **PRIMITIVE_POINTS** = `0`

Render array as points (one vertex equals one point).

PrimitiveType **PRIMITIVE_LINES** = `1`

Render array as lines (every two vertices a line is created).

PrimitiveType **PRIMITIVE_LINE_STRIP** = `2`

Render array as line strip.

PrimitiveType **PRIMITIVE_TRIANGLES** = `3`

Render array as triangles (every three vertices a triangle is created).

PrimitiveType **PRIMITIVE_TRIANGLE_STRIP** = `4`

Render array as triangle strips.

---

enum **ArrayType**:

ArrayType **ARRAY_VERTEX** = `0`

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array), [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), or [Array](class_array.md#class-array) of vertex positions.

ArrayType **ARRAY_NORMAL** = `1`

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of vertex normals.

**Note:** The array has to consist of normal vectors, otherwise they will be normalized by the engine, potentially causing visual discrepancies.

ArrayType **ARRAY_TANGENT** = `2`

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) of vertex tangents. Each element in groups of 4 floats, first 3 floats determine the tangent, and the last the binormal direction as -1 or 1.

ArrayType **ARRAY_COLOR** = `3`

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) of vertex colors.

ArrayType **ARRAY_TEX_UV** = `4`

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for UV coordinates.

ArrayType **ARRAY_TEX_UV2** = `5`

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for second UV coordinates.

ArrayType **ARRAY_CUSTOM0** = `6`

Contains custom color channel 0. [PackedByteArray](class_packedbytearray.md#class-packedbytearray) if `(format >> Mesh.ARRAY_FORMAT_CUSTOM0_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK` is ARRAY_CUSTOM_RGBA8_UNORM, ARRAY_CUSTOM_RGBA8_SNORM, ARRAY_CUSTOM_RG_HALF, or ARRAY_CUSTOM_RGBA_HALF. [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) otherwise.

ArrayType **ARRAY_CUSTOM1** = `7`

Contains custom color channel 1. [PackedByteArray](class_packedbytearray.md#class-packedbytearray) if `(format >> Mesh.ARRAY_FORMAT_CUSTOM1_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK` is ARRAY_CUSTOM_RGBA8_UNORM, ARRAY_CUSTOM_RGBA8_SNORM, ARRAY_CUSTOM_RG_HALF, or ARRAY_CUSTOM_RGBA_HALF. [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) otherwise.

ArrayType **ARRAY_CUSTOM2** = `8`

Contains custom color channel 2. [PackedByteArray](class_packedbytearray.md#class-packedbytearray) if `(format >> Mesh.ARRAY_FORMAT_CUSTOM2_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK` is ARRAY_CUSTOM_RGBA8_UNORM, ARRAY_CUSTOM_RGBA8_SNORM, ARRAY_CUSTOM_RG_HALF, or ARRAY_CUSTOM_RGBA_HALF. [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) otherwise.

ArrayType **ARRAY_CUSTOM3** = `9`

Contains custom color channel 3. [PackedByteArray](class_packedbytearray.md#class-packedbytearray) if `(format >> Mesh.ARRAY_FORMAT_CUSTOM3_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK` is ARRAY_CUSTOM_RGBA8_UNORM, ARRAY_CUSTOM_RGBA8_SNORM, ARRAY_CUSTOM_RG_HALF, or ARRAY_CUSTOM_RGBA_HALF. [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) otherwise.

ArrayType **ARRAY_BONES** = `10`

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) or [PackedInt32Array](class_packedint32array.md#class-packedint32array) of bone indices. Contains either 4 or 8 numbers per vertex depending on the presence of the ARRAY_FLAG_USE_8_BONE_WEIGHTS flag.

ArrayType **ARRAY_WEIGHTS** = `11`

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) or [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) of bone weights in the range `0.0` to `1.0` (inclusive). Contains either 4 or 8 numbers per vertex depending on the presence of the ARRAY_FLAG_USE_8_BONE_WEIGHTS flag.

ArrayType **ARRAY_INDEX** = `12`

[PackedInt32Array](class_packedint32array.md#class-packedint32array) of integers used as indices referencing vertices, colors, normals, tangents, and textures. All of those arrays must have the same number of elements as the vertex array. No index can be beyond the vertex array size. When this index array is present, it puts the function into "index mode," where the index selects the *i*'th vertex, normal, tangent, color, UV, etc. This means if you want to have different normals or colors along an edge, you have to duplicate the vertices.

For triangles, the index array is interpreted as triples, referring to the vertices of each triangle. For lines, the index array is in pairs indicating the start and end of each line.

ArrayType **ARRAY_MAX** = `13`

Represents the size of the ArrayType enum.

---

enum **ArrayCustomFormat**:

ArrayCustomFormat **ARRAY_CUSTOM_RGBA8_UNORM** = `0`

Indicates this custom channel contains unsigned normalized byte colors from 0 to 1, encoded as [PackedByteArray](class_packedbytearray.md#class-packedbytearray).

ArrayCustomFormat **ARRAY_CUSTOM_RGBA8_SNORM** = `1`

Indicates this custom channel contains signed normalized byte colors from -1 to 1, encoded as [PackedByteArray](class_packedbytearray.md#class-packedbytearray).

ArrayCustomFormat **ARRAY_CUSTOM_RG_HALF** = `2`

Indicates this custom channel contains half precision float colors, encoded as [PackedByteArray](class_packedbytearray.md#class-packedbytearray). Only red and green channels are used.

ArrayCustomFormat **ARRAY_CUSTOM_RGBA_HALF** = `3`

Indicates this custom channel contains half precision float colors, encoded as [PackedByteArray](class_packedbytearray.md#class-packedbytearray).

ArrayCustomFormat **ARRAY_CUSTOM_R_FLOAT** = `4`

Indicates this custom channel contains full float colors, in a [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array). Only the red channel is used.

ArrayCustomFormat **ARRAY_CUSTOM_RG_FLOAT** = `5`

Indicates this custom channel contains full float colors, in a [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array). Only red and green channels are used.

ArrayCustomFormat **ARRAY_CUSTOM_RGB_FLOAT** = `6`

Indicates this custom channel contains full float colors, in a [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array). Only red, green and blue channels are used.

ArrayCustomFormat **ARRAY_CUSTOM_RGBA_FLOAT** = `7`

Indicates this custom channel contains full float colors, in a [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array).

ArrayCustomFormat **ARRAY_CUSTOM_MAX** = `8`

Represents the size of the ArrayCustomFormat enum.

---

flags **ArrayFormat**:

ArrayFormat **ARRAY_FORMAT_VERTEX** = `1`

Mesh array contains vertices. All meshes require a vertex array so this should always be present.

ArrayFormat **ARRAY_FORMAT_NORMAL** = `2`

Mesh array contains normals.

ArrayFormat **ARRAY_FORMAT_TANGENT** = `4`

Mesh array contains tangents.

ArrayFormat **ARRAY_FORMAT_COLOR** = `8`

Mesh array contains colors.

ArrayFormat **ARRAY_FORMAT_TEX_UV** = `16`

Mesh array contains UVs.

ArrayFormat **ARRAY_FORMAT_TEX_UV2** = `32`

Mesh array contains second UV.

ArrayFormat **ARRAY_FORMAT_CUSTOM0** = `64`

Mesh array contains custom channel index 0.

ArrayFormat **ARRAY_FORMAT_CUSTOM1** = `128`

Mesh array contains custom channel index 1.

ArrayFormat **ARRAY_FORMAT_CUSTOM2** = `256`

Mesh array contains custom channel index 2.

ArrayFormat **ARRAY_FORMAT_CUSTOM3** = `512`

Mesh array contains custom channel index 3.

ArrayFormat **ARRAY_FORMAT_BONES** = `1024`

Mesh array contains bones.

ArrayFormat **ARRAY_FORMAT_WEIGHTS** = `2048`

Mesh array contains bone weights.

ArrayFormat **ARRAY_FORMAT_INDEX** = `4096`

Mesh array uses indices.

ArrayFormat **ARRAY_FORMAT_BLEND_SHAPE_MASK** = `7`

Mask of mesh channels permitted in blend shapes.

ArrayFormat **ARRAY_FORMAT_CUSTOM_BASE** = `13`

Shift of first custom channel.

ArrayFormat **ARRAY_FORMAT_CUSTOM_BITS** = `3`

Number of format bits per custom channel. See ArrayCustomFormat.

ArrayFormat **ARRAY_FORMAT_CUSTOM0_SHIFT** = `13`

Amount to shift ArrayCustomFormat for custom channel index 0.

ArrayFormat **ARRAY_FORMAT_CUSTOM1_SHIFT** = `16`

Amount to shift ArrayCustomFormat for custom channel index 1.

ArrayFormat **ARRAY_FORMAT_CUSTOM2_SHIFT** = `19`

Amount to shift ArrayCustomFormat for custom channel index 2.

ArrayFormat **ARRAY_FORMAT_CUSTOM3_SHIFT** = `22`

Amount to shift ArrayCustomFormat for custom channel index 3.

ArrayFormat **ARRAY_FORMAT_CUSTOM_MASK** = `7`

Mask of custom format bits per custom channel. Must be shifted by one of the SHIFT constants. See ArrayCustomFormat.

ArrayFormat **ARRAY_COMPRESS_FLAGS_BASE** = `25`

Shift of first compress flag. Compress flags should be passed to [ArrayMesh.add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays) and [SurfaceTool.commit()](class_surfacetool.md#class-surfacetool-method-commit).

ArrayFormat **ARRAY_FLAG_USE_2D_VERTICES** = `33554432`

Flag used to mark that the array contains 2D vertices.

ArrayFormat **ARRAY_FLAG_USE_DYNAMIC_UPDATE** = `67108864`

Flag used to mark that the mesh data will use `GL_DYNAMIC_DRAW` on GLES. Unused on Vulkan.

ArrayFormat **ARRAY_FLAG_USE_8_BONE_WEIGHTS** = `134217728`

Flag used to mark that the mesh contains up to 8 bone influences per vertex. This flag indicates that ARRAY_BONES and ARRAY_WEIGHTS elements will have double length.

ArrayFormat **ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY** = `268435456`

Flag used to mark that the mesh intentionally contains no vertex array.

ArrayFormat **ARRAY_FLAG_COMPRESS_ATTRIBUTES** = `536870912`

Flag used to mark that a mesh is using compressed attributes (vertices, normals, tangents, UVs). When this form of compression is enabled, vertex positions will be packed into an RGBA16UNORM attribute and scaled in the vertex shader. The normal and tangent will be packed into an RG16UNORM representing an axis, and a 16-bit float stored in the A-channel of the vertex. UVs will use 16-bit normalized floats instead of full 32-bit signed floats. When using this compression mode you must use either vertices, normals, and tangents or only vertices. You cannot use normals without tangents. Importers will automatically enable this compression if they can.

---

enum **BlendShapeMode**:

BlendShapeMode **BLEND_SHAPE_MODE_NORMALIZED** = `0`

Blend shapes are normalized.

BlendShapeMode **BLEND_SHAPE_MODE_RELATIVE** = `1`

Blend shapes are relative to base weight.

---

## Property Descriptions

[Vector2i](class_vector2i.md#class-vector2i) **lightmap_size_hint** = `Vector2i(0, 0)`

-  **set_lightmap_size_hint**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_lightmap_size_hint**()

Sets a hint to be used for lightmap resolution.

---

## Method Descriptions

[AABB](class_aabb.md#class-aabb) **\_get_aabb**()

Virtual method to override the [AABB](class_aabb.md#class-aabb) for a custom class extending **Mesh**.

---

[int](class_int.md#class-int) **\_get_blend_shape_count**()

Virtual method to override the number of blend shapes for a custom class extending **Mesh**.

---

[StringName](class_stringname.md#class-stringname) **\_get_blend_shape_name**(index: [int](class_int.md#class-int))

Virtual method to override the retrieval of blend shape names for a custom class extending **Mesh**.

---

[int](class_int.md#class-int) **\_get_surface_count**()

Virtual method to override the surface count for a custom class extending **Mesh**.

---

 **\_set_blend_shape_name**(index: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname))

Virtual method to override the names of blend shapes for a custom class extending **Mesh**.

---

[int](class_int.md#class-int) **\_surface_get_array_index_len**(index: [int](class_int.md#class-int))

Virtual method to override the surface array index length for a custom class extending **Mesh**.

---

[int](class_int.md#class-int) **\_surface_get_array_len**(index: [int](class_int.md#class-int))

Virtual method to override the surface array length for a custom class extending **Mesh**.

---

[Array](class_array.md#class-array) **\_surface_get_arrays**(index: [int](class_int.md#class-int))

Virtual method to override the surface arrays for a custom class extending **Mesh**.

---

[Array](class_array.md#class-array)[[Array](class_array.md#class-array)] **\_surface_get_blend_shape_arrays**(index: [int](class_int.md#class-int))

Virtual method to override the blend shape arrays for a custom class extending **Mesh**.

---

[int](class_int.md#class-int) **\_surface_get_format**(index: [int](class_int.md#class-int))

Virtual method to override the surface format for a custom class extending **Mesh**.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_surface_get_lods**(index: [int](class_int.md#class-int))

Virtual method to override the surface LODs for a custom class extending **Mesh**.

---

[Material](class_material.md#class-material) **\_surface_get_material**(index: [int](class_int.md#class-int))

Virtual method to override the surface material for a custom class extending **Mesh**.

---

[int](class_int.md#class-int) **\_surface_get_primitive_type**(index: [int](class_int.md#class-int))

Virtual method to override the surface primitive type for a custom class extending **Mesh**.

---

 **\_surface_set_material**(index: [int](class_int.md#class-int), material: [Material](class_material.md#class-material))

Virtual method to override the setting of a `material` at the given `index` for a custom class extending **Mesh**.

---

[ConvexPolygonShape3D](class_convexpolygonshape3d.md#class-convexpolygonshape3d) **create_convex_shape**(clean: [bool](class_bool.md#class-bool) = true, simplify: [bool](class_bool.md#class-bool) = false)

Calculate a [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class-convexpolygonshape3d) from the mesh.

If `clean` is `true` (default), duplicate and interior vertices are removed automatically. You can set it to `false` to make the process faster if not needed.

If `simplify` is `true`, the geometry can be further simplified to reduce the number of vertices. Disabled by default.

---

Mesh **create_outline**(margin: [float](class_float.md#class-float))

Calculate an outline mesh at a defined offset (margin) from the original mesh.

**Note:** This method typically returns the vertices in reverse order (e.g. clockwise to counterclockwise).

---

[Resource](class_resource.md#class-resource) **create_placeholder**()

Creates a placeholder version of this resource ([PlaceholderMesh](class_placeholdermesh.md#class-placeholdermesh)).

---

[ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d) **create_trimesh_shape**()

Calculate a [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d) from the mesh.

---

[TriangleMesh](class_trianglemesh.md#class-trianglemesh) **generate_triangle_mesh**()

Generate a [TriangleMesh](class_trianglemesh.md#class-trianglemesh) from the mesh. Considers only surfaces using one of these primitive types: PRIMITIVE_TRIANGLES, PRIMITIVE_TRIANGLE_STRIP.

---

[AABB](class_aabb.md#class-aabb) **get_aabb**()

Returns the smallest [AABB](class_aabb.md#class-aabb) enclosing this mesh in local space. Not affected by `custom_aabb`.

**Note:** This is only implemented for [ArrayMesh](class_arraymesh.md#class-arraymesh) and [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh).

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_faces**()

Returns all the vertices that make up the faces of the mesh. Each three vertices represent one triangle.

---

[int](class_int.md#class-int) **get_surface_count**()

Returns the number of surfaces that the **Mesh** holds. This is equivalent to [MeshInstance3D.get_surface_override_material_count()](class_meshinstance3d.md#class-meshinstance3d-method-get-surface-override-material-count).

---

[Array](class_array.md#class-array) **surface_get_arrays**(surf_idx: [int](class_int.md#class-int))

Returns the arrays for the vertices, normals, UVs, etc. that make up the requested surface (see [ArrayMesh.add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays)).

---

[Array](class_array.md#class-array)[[Array](class_array.md#class-array)] **surface_get_blend_shape_arrays**(surf_idx: [int](class_int.md#class-int))

Returns the blend shape arrays for the requested surface.

---

[Material](class_material.md#class-material) **surface_get_material**(surf_idx: [int](class_int.md#class-int))

Returns a [Material](class_material.md#class-material) in a given surface. Surface is rendered using this material.

**Note:** This returns the material within the **Mesh** resource, not the [Material](class_material.md#class-material) associated to the [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d)'s Surface Material Override properties. To get the [Material](class_material.md#class-material) associated to the [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d)'s Surface Material Override properties, use [MeshInstance3D.get_surface_override_material()](class_meshinstance3d.md#class-meshinstance3d-method-get-surface-override-material) instead.

---

 **surface_set_material**(surf_idx: [int](class_int.md#class-int), material: [Material](class_material.md#class-material))

Sets a [Material](class_material.md#class-material) for a given surface. Surface will be rendered using this material.

**Note:** This assigns the material within the **Mesh** resource, not the [Material](class_material.md#class-material) associated to the [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d)'s Surface Material Override properties. To set the [Material](class_material.md#class-material) associated to the [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d)'s Surface Material Override properties, use [MeshInstance3D.set_surface_override_material()](class_meshinstance3d.md#class-meshinstance3d-method-set-surface-override-material) instead.
