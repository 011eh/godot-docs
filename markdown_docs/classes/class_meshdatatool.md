# MeshDataTool

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Helper tool to access and edit [Mesh](class_mesh.md#class-mesh) data.

## Description

MeshDataTool provides access to individual vertices in a [Mesh](class_mesh.md#class-mesh). It allows users to read and edit vertex data of meshes. It also creates an array of faces and edges.

To use MeshDataTool, load a mesh with create_from_surface(). When you are finished editing the data commit the data to a mesh with commit_to_surface().

Below is an example of how MeshDataTool may be used.

GDScript

```gdscript
var mesh = ArrayMesh.new()
mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, BoxMesh.new().get_mesh_arrays())
var mdt = MeshDataTool.new()
mdt.create_from_surface(mesh, 0)
for i in range(mdt.get_vertex_count()):
    var vertex = mdt.get_vertex(i)
    # In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded.
    vertex += mdt.get_vertex_normal(i)
    # Save your change.
    mdt.set_vertex(i, vertex)
mesh.clear_surfaces()
mdt.commit_to_surface(mesh)
var mi = MeshInstance.new()
mi.mesh = mesh
add_child(mi)
```

C#

```csharp
var mesh = new ArrayMesh();
mesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, new BoxMesh().GetMeshArrays());
var mdt = new MeshDataTool();
mdt.CreateFromSurface(mesh, 0);
for (var i = 0; i < mdt.GetVertexCount(); i++)
{
    Vector3 vertex = mdt.GetVertex(i);
    // In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded.
    vertex += mdt.GetVertexNormal(i);
    // Save your change.
    mdt.SetVertex(i, vertex);
}
mesh.ClearSurfaces();
mdt.CommitToSurface(mesh);
var mi = new MeshInstance();
mi.Mesh = mesh;
AddChild(mi);
```

See also [ArrayMesh](class_arraymesh.md#class-arraymesh), [ImmediateMesh](class_immediatemesh.md#class-immediatemesh) and [SurfaceTool](class_surfacetool.md#class-surfacetool) for procedural geometry generation.

**Note:** Godot uses clockwise [winding order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front faces of triangle primitive modes.

## Tutorials

- [Using the MeshDataTool](../tutorials/3d/procedural_geometry/meshdatatool.md)

## Methods

|                                                                            | clear()                                                                                                                                                  |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)                      | commit_to_surface(mesh: [ArrayMesh](class_arraymesh.md#class-arraymesh), compression_flags: [int](class_int.md#class-int) = 0)               |
| [Error](class_@globalscope.md#enum-globalscope-error)                      | create_from_surface(mesh: [ArrayMesh](class_arraymesh.md#class-arraymesh), surface: [int](class_int.md#class-int))                         |
| [int](class_int.md#class-int)                                              | get_edge_count()                                                                                                                                |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | get_edge_faces(idx: [int](class_int.md#class-int))                                                                                              |
| [Variant](class_variant.md#class-variant)                                  | get_edge_meta(idx: [int](class_int.md#class-int))                                                                                                |
| [int](class_int.md#class-int)                                              | get_edge_vertex(idx: [int](class_int.md#class-int), vertex: [int](class_int.md#class-int))                                                     |
| [int](class_int.md#class-int)                                              | get_face_count()                                                                                                                                |
| [int](class_int.md#class-int)                                              | get_face_edge(idx: [int](class_int.md#class-int), edge: [int](class_int.md#class-int))                                                           |
| [Variant](class_variant.md#class-variant)                                  | get_face_meta(idx: [int](class_int.md#class-int))                                                                                                |
| [Vector3](class_vector3.md#class-vector3)                                  | get_face_normal(idx: [int](class_int.md#class-int))                                                                                            |
| [int](class_int.md#class-int)                                              | get_face_vertex(idx: [int](class_int.md#class-int), vertex: [int](class_int.md#class-int))                                                     |
| [int](class_int.md#class-int)                                              | get_format()                                                                                                                                        |
| [Material](class_material.md#class-material)                               | get_material()                                                                                                                                    |
| [Vector3](class_vector3.md#class-vector3)                                  | get_vertex(idx: [int](class_int.md#class-int))                                                                                                      |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | get_vertex_bones(idx: [int](class_int.md#class-int))                                                                                          |
| [Color](class_color.md#class-color)                                        | get_vertex_color(idx: [int](class_int.md#class-int))                                                                                          |
| [int](class_int.md#class-int)                                              | get_vertex_count()                                                                                                                            |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | get_vertex_edges(idx: [int](class_int.md#class-int))                                                                                          |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | get_vertex_faces(idx: [int](class_int.md#class-int))                                                                                          |
| [Variant](class_variant.md#class-variant)                                  | get_vertex_meta(idx: [int](class_int.md#class-int))                                                                                            |
| [Vector3](class_vector3.md#class-vector3)                                  | get_vertex_normal(idx: [int](class_int.md#class-int))                                                                                        |
| [Plane](class_plane.md#class-plane)                                        | get_vertex_tangent(idx: [int](class_int.md#class-int))                                                                                      |
| [Vector2](class_vector2.md#class-vector2)                                  | get_vertex_uv(idx: [int](class_int.md#class-int))                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                                  | get_vertex_uv2(idx: [int](class_int.md#class-int))                                                                                              |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | get_vertex_weights(idx: [int](class_int.md#class-int))                                                                                      |
|                                                                            | set_edge_meta(idx: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant))                                               |
|                                                                            | set_face_meta(idx: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant))                                               |
|                                                                            | set_material(material: [Material](class_material.md#class-material))                                                                              |
|                                                                            | set_vertex(idx: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3))                                                   |
|                                                                            | set_vertex_bones(idx: [int](class_int.md#class-int), bones: [PackedInt32Array](class_packedint32array.md#class-packedint32array))             |
|                                                                            | set_vertex_color(idx: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                              |
|                                                                            | set_vertex_meta(idx: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant))                                           |
|                                                                            | set_vertex_normal(idx: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3))                                     |
|                                                                            | set_vertex_tangent(idx: [int](class_int.md#class-int), tangent: [Plane](class_plane.md#class-plane))                                        |
|                                                                            | set_vertex_uv(idx: [int](class_int.md#class-int), uv: [Vector2](class_vector2.md#class-vector2))                                                 |
|                                                                            | set_vertex_uv2(idx: [int](class_int.md#class-int), uv2: [Vector2](class_vector2.md#class-vector2))                                              |
|                                                                            | set_vertex_weights(idx: [int](class_int.md#class-int), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |

---

## Method Descriptions

 **clear**()

Clears all data currently in MeshDataTool.

---

[Error](class_@globalscope.md#enum-globalscope-error) **commit_to_surface**(mesh: [ArrayMesh](class_arraymesh.md#class-arraymesh), compression_flags: [int](class_int.md#class-int) = 0)

Adds a new surface to specified [Mesh](class_mesh.md#class-mesh) with edited data.

---

[Error](class_@globalscope.md#enum-globalscope-error) **create_from_surface**(mesh: [ArrayMesh](class_arraymesh.md#class-arraymesh), surface: [int](class_int.md#class-int))

Uses specified surface of given [Mesh](class_mesh.md#class-mesh) to populate data for MeshDataTool.

Requires [Mesh](class_mesh.md#class-mesh) with primitive type [Mesh.PRIMITIVE_TRIANGLES](class_mesh.md#class-mesh-constant-primitive-triangles).

---

[int](class_int.md#class-int) **get_edge_count**()

Returns the number of edges in this [Mesh](class_mesh.md#class-mesh).

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_edge_faces**(idx: [int](class_int.md#class-int))

Returns array of faces that touch given edge.

---

[Variant](class_variant.md#class-variant) **get_edge_meta**(idx: [int](class_int.md#class-int))

Returns meta information assigned to given edge.

---

[int](class_int.md#class-int) **get_edge_vertex**(idx: [int](class_int.md#class-int), vertex: [int](class_int.md#class-int))

Returns the index of the specified `vertex` connected to the edge at index `idx`.

`vertex` can only be `0` or `1`, as edges are composed of two vertices.

---

[int](class_int.md#class-int) **get_face_count**()

Returns the number of faces in this [Mesh](class_mesh.md#class-mesh).

---

[int](class_int.md#class-int) **get_face_edge**(idx: [int](class_int.md#class-int), edge: [int](class_int.md#class-int))

Returns the edge associated with the face at index `idx`.

`edge` argument must be either `0`, `1`, or `2` because a face only has three edges.

---

[Variant](class_variant.md#class-variant) **get_face_meta**(idx: [int](class_int.md#class-int))

Returns the metadata associated with the given face.

---

[Vector3](class_vector3.md#class-vector3) **get_face_normal**(idx: [int](class_int.md#class-int))

Calculates and returns the face normal of the given face.

---

[int](class_int.md#class-int) **get_face_vertex**(idx: [int](class_int.md#class-int), vertex: [int](class_int.md#class-int))

Returns the specified vertex index of the given face.

`vertex` must be either `0`, `1`, or `2` because faces contain three vertices.

GDScript

```gdscript
var index = mesh_data_tool.get_face_vertex(0, 1) # Gets the index of the second vertex of the first face.
var position = mesh_data_tool.get_vertex(index)
var normal = mesh_data_tool.get_vertex_normal(index)
```

C#

```csharp
int index = meshDataTool.GetFaceVertex(0, 1); // Gets the index of the second vertex of the first face.
Vector3 position = meshDataTool.GetVertex(index);
Vector3 normal = meshDataTool.GetVertexNormal(index);
```

---

[int](class_int.md#class-int) **get_format**()

Returns the [Mesh](class_mesh.md#class-mesh)'s format as a combination of the [ArrayFormat](class_mesh.md#enum-mesh-arrayformat) flags. For example, a mesh containing both vertices and normals would return a format of `3` because [Mesh.ARRAY_FORMAT_VERTEX](class_mesh.md#class-mesh-constant-array-format-vertex) is `1` and [Mesh.ARRAY_FORMAT_NORMAL](class_mesh.md#class-mesh-constant-array-format-normal) is `2`.

---

[Material](class_material.md#class-material) **get_material**()

Returns the material assigned to the [Mesh](class_mesh.md#class-mesh).

---

[Vector3](class_vector3.md#class-vector3) **get_vertex**(idx: [int](class_int.md#class-int))

Returns the position of the given vertex.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_vertex_bones**(idx: [int](class_int.md#class-int))

Returns the bones of the given vertex.

---

[Color](class_color.md#class-color) **get_vertex_color**(idx: [int](class_int.md#class-int))

Returns the color of the given vertex.

---

[int](class_int.md#class-int) **get_vertex_count**()

Returns the total number of vertices in [Mesh](class_mesh.md#class-mesh).

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_vertex_edges**(idx: [int](class_int.md#class-int))

Returns an array of edges that share the given vertex.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_vertex_faces**(idx: [int](class_int.md#class-int))

Returns an array of faces that share the given vertex.

---

[Variant](class_variant.md#class-variant) **get_vertex_meta**(idx: [int](class_int.md#class-int))

Returns the metadata associated with the given vertex.

---

[Vector3](class_vector3.md#class-vector3) **get_vertex_normal**(idx: [int](class_int.md#class-int))

Returns the normal of the given vertex.

---

[Plane](class_plane.md#class-plane) **get_vertex_tangent**(idx: [int](class_int.md#class-int))

Returns the tangent of the given vertex.

---

[Vector2](class_vector2.md#class-vector2) **get_vertex_uv**(idx: [int](class_int.md#class-int))

Returns the UV of the given vertex.

---

[Vector2](class_vector2.md#class-vector2) **get_vertex_uv2**(idx: [int](class_int.md#class-int))

Returns the UV2 of the given vertex.

---

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_vertex_weights**(idx: [int](class_int.md#class-int))

Returns bone weights of the given vertex.

---

 **set_edge_meta**(idx: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant))

Sets the metadata of the given edge.

---

 **set_face_meta**(idx: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant))

Sets the metadata of the given face.

---

 **set_material**(material: [Material](class_material.md#class-material))

Sets the material to be used by newly-constructed [Mesh](class_mesh.md#class-mesh).

---

 **set_vertex**(idx: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3))

Sets the position of the given vertex.

---

 **set_vertex_bones**(idx: [int](class_int.md#class-int), bones: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Sets the bones of the given vertex.

---

 **set_vertex_color**(idx: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the color of the given vertex.

---

 **set_vertex_meta**(idx: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant))

Sets the metadata associated with the given vertex.

---

 **set_vertex_normal**(idx: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3))

Sets the normal of the given vertex.

---

 **set_vertex_tangent**(idx: [int](class_int.md#class-int), tangent: [Plane](class_plane.md#class-plane))

Sets the tangent of the given vertex.

**Note:** Even though `tangent` is a [Plane](class_plane.md#class-plane), it does not directly represent the tangent plane. Its [Plane.x](class_plane.md#class-plane-property-x), [Plane.y](class_plane.md#class-plane-property-y), and [Plane.z](class_plane.md#class-plane-property-z) represent the tangent vector and [Plane.d](class_plane.md#class-plane-property-d) should be either `-1` or `1`. See also [Mesh.ARRAY_TANGENT](class_mesh.md#class-mesh-constant-array-tangent).

---

 **set_vertex_uv**(idx: [int](class_int.md#class-int), uv: [Vector2](class_vector2.md#class-vector2))

Sets the UV of the given vertex.

---

 **set_vertex_uv2**(idx: [int](class_int.md#class-int), uv2: [Vector2](class_vector2.md#class-vector2))

Sets the UV2 of the given vertex.

---

 **set_vertex_weights**(idx: [int](class_int.md#class-int), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Sets the bone weights of the given vertex.
