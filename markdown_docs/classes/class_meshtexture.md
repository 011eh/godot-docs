# MeshTexture

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Simple texture that uses a mesh to draw itself.

## Description

Simple texture that uses a mesh to draw itself. It's limited because flags can't be changed and region drawing is not supported.

## Properties

| [Texture2D](class_texture2d.md#class-texture2d)   | base_texture   |                                                                                                   |
|---------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [Vector2](class_vector2.md#class-vector2)         | image_size       | `Vector2(0, 0)`                                                                                   |
| [Mesh](class_mesh.md#class-mesh)                  | mesh                   |                                                                                                   |
| [bool](class_bool.md#class-bool)                  | resource_local_to_scene                                    | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

---

## Property Descriptions

[Texture2D](class_texture2d.md#class-texture2d) **base_texture**

-  **set_base_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_base_texture**()

Sets the base texture that the Mesh will use to draw.

---

[Vector2](class_vector2.md#class-vector2) **image_size** = `Vector2(0, 0)`

-  **set_image_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_image_size**()

Sets the size of the image, needed for reference.

---

[Mesh](class_mesh.md#class-mesh) **mesh**

-  **set_mesh**(value: [Mesh](class_mesh.md#class-mesh))
- [Mesh](class_mesh.md#class-mesh) **get_mesh**()

Sets the mesh used to draw. It must be a mesh using 2D vertices.
