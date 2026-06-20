# Texture3DRD

**Inherits:** [Texture3D](class_texture3d.md#class-texture3d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture for 3D that is bound to a texture created on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Description

This texture class allows you to use a 3D texture created directly on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) as a texture for materials, meshes, etc.

**Note:** **Texture3DRD** is intended for low-level usage with [RenderingDevice](class_renderingdevice.md#class-renderingdevice). For most use cases, use [Texture3D](class_texture3d.md#class-texture3d) instead.

## Tutorials

- [Compute Texture demo](https://godotengine.org/asset-library/asset/2764)

## Properties

| [RID](class_rid.md#class-rid)   | texture_rd_rid   |
|---------------------------------|----------------------------------------------------------------|

---

## Property Descriptions

[RID](class_rid.md#class-rid) **texture_rd_rid**

-  **set_texture_rd_rid**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_texture_rd_rid**()

The RID of the texture object created on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice).
