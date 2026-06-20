# TextureLayered

**Inherits:** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [CompressedTextureLayered](class_compressedtexturelayered.md#class-compressedtexturelayered), [ImageTextureLayered](class_imagetexturelayered.md#class-imagetexturelayered), [PlaceholderTextureLayered](class_placeholdertexturelayered.md#class-placeholdertexturelayered), [TextureLayeredRD](class_texturelayeredrd.md#class-texturelayeredrd)

Base class for texture types which contain the data of multiple [Image](class_image.md#class-image)s. Each image is of the same size and format.

## Description

Base class for [ImageTextureLayered](class_imagetexturelayered.md#class-imagetexturelayered) and [CompressedTextureLayered](class_compressedtexturelayered.md#class-compressedtexturelayered). Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also [Texture3D](class_texture3d.md#class-texture3d).

Data is set on a per-layer basis. For [Texture2DArray](class_texture2darray.md#class-texture2darray)s, the layer specifies the array layer.

All images need to have the same width, height and number of mipmap levels.

A **TextureLayered** can be loaded with [ResourceLoader.load()](class_resourceloader.md#class-resourceloader-method-load).

Internally, Godot maps these files to their respective counterparts in the target rendering driver (Vulkan, OpenGL3).

## Methods

| [Format](class_image.md#enum-image-format)      | \_get_format()                                                   |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                   | \_get_height()                                                   |
| [Image](class_image.md#class-image)             | \_get_layer_data(layer_index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int)                   | \_get_layered_type()                                       |
| [int](class_int.md#class-int)                   | \_get_layers()                                                   |
| [int](class_int.md#class-int)                   | \_get_width()                                                     |
| [bool](class_bool.md#class-bool)                | \_has_mipmaps()                                                 |
| [Format](class_image.md#enum-image-format)      | get_format()                                                             |
| [int](class_int.md#class-int)                   | get_height()                                                             |
| [Image](class_image.md#class-image)             | get_layer_data(layer: [int](class_int.md#class-int))                 |
| LayeredType | get_layered_type()                                                 |
| [int](class_int.md#class-int)                   | get_layers()                                                             |
| [int](class_int.md#class-int)                   | get_width()                                                               |
| [bool](class_bool.md#class-bool)                | has_mipmaps()                                                           |

---

## Enumerations

enum **LayeredType**:

LayeredType **LAYERED_TYPE_2D_ARRAY** = `0`

Texture is a generic [Texture2DArray](class_texture2darray.md#class-texture2darray).

LayeredType **LAYERED_TYPE_CUBEMAP** = `1`

Texture is a [Cubemap](class_cubemap.md#class-cubemap), with each side in its own layer (6 in total).

LayeredType **LAYERED_TYPE_CUBEMAP_ARRAY** = `2`

Texture is a [CubemapArray](class_cubemaparray.md#class-cubemaparray), with each cubemap being made of 6 layers.

---

## Method Descriptions

[Format](class_image.md#enum-image-format) **\_get_format**()

Called when the **TextureLayered**'s format is queried.

---

[int](class_int.md#class-int) **\_get_height**()

Called when the **TextureLayered**'s height is queried.

---

[Image](class_image.md#class-image) **\_get_layer_data**(layer_index: [int](class_int.md#class-int))

Called when the data for a layer in the **TextureLayered** is queried.

---

[int](class_int.md#class-int) **\_get_layered_type**()

Called when the layers' type in the **TextureLayered** is queried.

---

[int](class_int.md#class-int) **\_get_layers**()

Called when the number of layers in the **TextureLayered** is queried.

---

[int](class_int.md#class-int) **\_get_width**()

Called when the **TextureLayered**'s width queried.

---

[bool](class_bool.md#class-bool) **\_has_mipmaps**()

Called when the presence of mipmaps in the **TextureLayered** is queried.

---

[Format](class_image.md#enum-image-format) **get_format**()

Returns the current format being used by this texture.

---

[int](class_int.md#class-int) **get_height**()

Returns the height of the texture in pixels. Height is typically represented by the Y axis.

---

[Image](class_image.md#class-image) **get_layer_data**(layer: [int](class_int.md#class-int))

Returns an [Image](class_image.md#class-image) resource with the data from specified `layer`.

---

LayeredType **get_layered_type**()

Returns the **TextureLayered**'s type. The type determines how the data is accessed, with cubemaps having special types.

---

[int](class_int.md#class-int) **get_layers**()

Returns the number of referenced [Image](class_image.md#class-image)s.

---

[int](class_int.md#class-int) **get_width**()

Returns the width of the texture in pixels. Width is typically represented by the X axis.

---

[bool](class_bool.md#class-bool) **has_mipmaps**()

Returns `true` if the layers have generated mipmaps.
