# MeshLibrary

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Library of meshes.

## Description

A library of meshes. Contains a list of [Mesh](class_mesh.md#class-mesh) resources, each with a name and ID. Each item can also include collision and navigation shapes. This resource is used in [GridMap](class_gridmap.md#class-gridmap).

## Tutorials

- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)

## Methods

|                                                                                            | clear()                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                            | create_item(id: [int](class_int.md#class-int))                                                                                                                                                 |
| [int](class_int.md#class-int)                                                              | find_item_by_name(name: [String](class_string.md#class-string))                                                                                                                          |
| [int](class_int.md#class-int)                                                              | get_item_count()                                                                                                                                                                            |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                       | get_item_list()                                                                                                                                                                              |
| [Mesh](class_mesh.md#class-mesh)                                                           | get_item_mesh(id: [int](class_int.md#class-int))                                                                                                                                             |
| [ShadowCastingSetting](class_renderingserver.md#enum-renderingserver-shadowcastingsetting) | get_item_mesh_cast_shadow(id: [int](class_int.md#class-int))                                                                                                                     |
| [Transform3D](class_transform3d.md#class-transform3d)                                      | get_item_mesh_transform(id: [int](class_int.md#class-int))                                                                                                                         |
| [String](class_string.md#class-string)                                                     | get_item_name(id: [int](class_int.md#class-int))                                                                                                                                             |
| [int](class_int.md#class-int)                                                              | get_item_navigation_layers(id: [int](class_int.md#class-int))                                                                                                                   |
| [NavigationMesh](class_navigationmesh.md#class-navigationmesh)                             | get_item_navigation_mesh(id: [int](class_int.md#class-int))                                                                                                                       |
| [Transform3D](class_transform3d.md#class-transform3d)                                      | get_item_navigation_mesh_transform(id: [int](class_int.md#class-int))                                                                                                   |
| [Texture2D](class_texture2d.md#class-texture2d)                                            | get_item_preview(id: [int](class_int.md#class-int))                                                                                                                                       |
| [Array](class_array.md#class-array)                                                        | get_item_shapes(id: [int](class_int.md#class-int))                                                                                                                                         |
| [int](class_int.md#class-int)                                                              | get_last_unused_item_id()                                                                                                                                                          |
|                                                                                            | remove_item(id: [int](class_int.md#class-int))                                                                                                                                                 |
|                                                                                            | set_item_mesh(id: [int](class_int.md#class-int), mesh: [Mesh](class_mesh.md#class-mesh))                                                                                                     |
|                                                                                            | set_item_mesh_cast_shadow(id: [int](class_int.md#class-int), shadow_casting_setting: [ShadowCastingSetting](class_renderingserver.md#enum-renderingserver-shadowcastingsetting)) |
|                                                                                            | set_item_mesh_transform(id: [int](class_int.md#class-int), mesh_transform: [Transform3D](class_transform3d.md#class-transform3d))                                                  |
|                                                                                            | set_item_name(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                                               |
|                                                                                            | set_item_navigation_layers(id: [int](class_int.md#class-int), navigation_layers: [int](class_int.md#class-int))                                                                 |
|                                                                                            | set_item_navigation_mesh(id: [int](class_int.md#class-int), navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh))                                      |
|                                                                                            | set_item_navigation_mesh_transform(id: [int](class_int.md#class-int), navigation_mesh: [Transform3D](class_transform3d.md#class-transform3d))                           |
|                                                                                            | set_item_preview(id: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))                                                                             |
|                                                                                            | set_item_shapes(id: [int](class_int.md#class-int), shapes: [Array](class_array.md#class-array))                                                                                            |

---

## Method Descriptions

 **clear**()

Clears the library.

---

 **create_item**(id: [int](class_int.md#class-int))

Creates a new item in the library with the given ID.

You can get an unused ID from get_last_unused_item_id().

---

[int](class_int.md#class-int) **find_item_by_name**(name: [String](class_string.md#class-string))

Returns the first item with the given name, or `-1` if no item is found.

---

[int](class_int.md#class-int) **get_item_count**()

Returns the number of items present in the library.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_item_list**()

Returns the list of item IDs in use.

---

[Mesh](class_mesh.md#class-mesh) **get_item_mesh**(id: [int](class_int.md#class-int))

Returns the item's mesh.

---

[ShadowCastingSetting](class_renderingserver.md#enum-renderingserver-shadowcastingsetting) **get_item_mesh_cast_shadow**(id: [int](class_int.md#class-int))

Returns the item's shadow casting mode.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_item_mesh_transform**(id: [int](class_int.md#class-int))

Returns the transform applied to the item's mesh.

---

[String](class_string.md#class-string) **get_item_name**(id: [int](class_int.md#class-int))

Returns the item's name.

---

[int](class_int.md#class-int) **get_item_navigation_layers**(id: [int](class_int.md#class-int))

Returns the item's navigation layers bitmask.

---

[NavigationMesh](class_navigationmesh.md#class-navigationmesh) **get_item_navigation_mesh**(id: [int](class_int.md#class-int))

Returns the item's navigation mesh.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_item_navigation_mesh_transform**(id: [int](class_int.md#class-int))

Returns the transform applied to the item's navigation mesh.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_item_preview**(id: [int](class_int.md#class-int))

When running in the editor, returns a generated item preview (a 3D rendering in isometric perspective). When used in a running project, returns the manually-defined item preview which can be set using set_item_preview(). Returns an empty [Texture2D](class_texture2d.md#class-texture2d) if no preview was manually set in a running project.

---

[Array](class_array.md#class-array) **get_item_shapes**(id: [int](class_int.md#class-int))

Returns an item's collision shapes.

The array consists of each [Shape3D](class_shape3d.md#class-shape3d) followed by its [Transform3D](class_transform3d.md#class-transform3d).

---

[int](class_int.md#class-int) **get_last_unused_item_id**()

Gets an unused ID for a new item.

---

 **remove_item**(id: [int](class_int.md#class-int))

Removes the item.

---

 **set_item_mesh**(id: [int](class_int.md#class-int), mesh: [Mesh](class_mesh.md#class-mesh))

Sets the item's mesh.

---

 **set_item_mesh_cast_shadow**(id: [int](class_int.md#class-int), shadow_casting_setting: [ShadowCastingSetting](class_renderingserver.md#enum-renderingserver-shadowcastingsetting))

Sets the item's shadow casting mode to `shadow_casting_setting`.

---

 **set_item_mesh_transform**(id: [int](class_int.md#class-int), mesh_transform: [Transform3D](class_transform3d.md#class-transform3d))

Sets the transform to apply to the item's mesh.

---

 **set_item_name**(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets the item's name.

This name is shown in the editor. It can also be used to look up the item later using find_item_by_name().

---

 **set_item_navigation_layers**(id: [int](class_int.md#class-int), navigation_layers: [int](class_int.md#class-int))

Sets the item's navigation layers bitmask.

---

 **set_item_navigation_mesh**(id: [int](class_int.md#class-int), navigation_mesh: [NavigationMesh](class_navigationmesh.md#class-navigationmesh))

Sets the item's navigation mesh.

---

 **set_item_navigation_mesh_transform**(id: [int](class_int.md#class-int), navigation_mesh: [Transform3D](class_transform3d.md#class-transform3d))

Sets the transform to apply to the item's navigation mesh.

---

 **set_item_preview**(id: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))

Sets a texture to use as the item's preview icon in the editor.

---

 **set_item_shapes**(id: [int](class_int.md#class-int), shapes: [Array](class_array.md#class-array))

Sets an item's collision shapes.

The array should consist of [Shape3D](class_shape3d.md#class-shape3d) objects, each followed by a [Transform3D](class_transform3d.md#class-transform3d) that will be applied to it. For shapes that should not have a transform, use [Transform3D.IDENTITY](class_transform3d.md#class-transform3d-constant-identity).
