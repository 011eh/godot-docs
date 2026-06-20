# PlaceholderTextureLayered

**Inherits:** [TextureLayered](class_texturelayered.md#class-texturelayered) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [PlaceholderCubemap](class_placeholdercubemap.md#class-placeholdercubemap), [PlaceholderCubemapArray](class_placeholdercubemaparray.md#class-placeholdercubemaparray), [PlaceholderTexture2DArray](class_placeholdertexture2darray.md#class-placeholdertexture2darray)

Placeholder class for a 2-dimensional texture array.

## Description

This class is used when loading a project that uses a [TextureLayered](class_texturelayered.md#class-texturelayered) subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

**Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

## Properties

| [int](class_int.md#class-int)                | layers   | `1`              |
|----------------------------------------------|--------------------------------------------------------------|------------------|
| [Vector2i](class_vector2i.md#class-vector2i) | size       | `Vector2i(1, 1)` |

---

## Property Descriptions

[int](class_int.md#class-int) **layers** = `1`

-  **set_layers**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_layers**()

The number of layers in the texture array.

---

[Vector2i](class_vector2i.md#class-vector2i) **size** = `Vector2i(1, 1)`

-  **set_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_size**()

The size of each texture layer (in pixels).
