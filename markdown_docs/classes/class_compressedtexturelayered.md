# CompressedTextureLayered

**Inherits:** [TextureLayered](class_texturelayered.md#class-texturelayered) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [CompressedCubemap](class_compressedcubemap.md#class-compressedcubemap), [CompressedCubemapArray](class_compressedcubemaparray.md#class-compressedcubemaparray), [CompressedTexture2DArray](class_compressedtexture2darray.md#class-compressedtexture2darray)

Base class for texture arrays that can optionally be compressed.

## Description

Base class for [CompressedTexture2DArray](class_compressedtexture2darray.md#class-compressedtexture2darray) and [CompressedTexture3D](class_compressedtexture3d.md#class-compressedtexture3d). Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also [TextureLayered](class_texturelayered.md#class-texturelayered).

## Properties

| [String](class_string.md#class-string)   | load_path   | `""`   |
|------------------------------------------|-------------------------------------------------------------------|--------|

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | load(path: [String](class_string.md#class-string))   |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------|

---

## Property Descriptions

[String](class_string.md#class-string) **load_path** = `""`

- [Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_load_path**()

The path the texture should be loaded from.

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **load**(path: [String](class_string.md#class-string))

Loads the texture at `path`.
