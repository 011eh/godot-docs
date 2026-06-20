# VisualShaderNodeCubemap

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Cubemap](class_cubemap.md#class-cubemap) sampling node to be used within the visual shader graph.

## Description

Translated to `texture(cubemap, vec3)` in the shader language. Returns a color vector and alpha channel as scalar.

## Properties

| [TextureLayered](class_texturelayered.md#class-texturelayered)   | cube_map         |     |
|------------------------------------------------------------------|----------------------------------------------------------------------|-----|
| Source                   | source             | `0` |
| TextureType         | texture_type | `0` |

---

## Enumerations

enum **Source**:

Source **SOURCE_TEXTURE** = `0`

Use the [Cubemap](class_cubemap.md#class-cubemap) set via cube_map. If this is set to source, the `samplerCube` port is ignored.

Source **SOURCE_PORT** = `1`

Use the [Cubemap](class_cubemap.md#class-cubemap) sampler reference passed via the `samplerCube` port. If this is set to source, the cube_map texture is ignored.

Source **SOURCE_MAX** = `2`

Represents the size of the Source enum.

---

enum **TextureType**:

TextureType **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

TextureType **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.

TextureType **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally converts the texture for proper usage as normal map.

TextureType **TYPE_MAX** = `3`

Represents the size of the TextureType enum.

---

## Property Descriptions

[TextureLayered](class_texturelayered.md#class-texturelayered) **cube_map**

-  **set_cube_map**(value: [TextureLayered](class_texturelayered.md#class-texturelayered))
- [TextureLayered](class_texturelayered.md#class-texturelayered) **get_cube_map**()

The [Cubemap](class_cubemap.md#class-cubemap) texture to sample when using SOURCE_TEXTURE as source.

---

Source **source** = `0`

-  **set_source**(value: Source)
- Source **get_source**()

Defines which source should be used for the sampling.

---

TextureType **texture_type** = `0`

-  **set_texture_type**(value: TextureType)
- TextureType **get_texture_type**()

Defines the type of data provided by the source texture.
