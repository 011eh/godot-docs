# GLTFTexture

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

GLTFTexture represents a texture in a glTF file.

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

## Properties

| [int](class_int.md#class-int)   | sampler     | `-1`   |
|---------------------------------|----------------------------------------------------|--------|
| [int](class_int.md#class-int)   | src_image | `-1`   |

---

## Property Descriptions

[int](class_int.md#class-int) **sampler** = `-1`

-  **set_sampler**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sampler**()

ID of the texture sampler to use when sampling the image. If -1, then the default texture sampler is used (linear filtering, and repeat wrapping in both axes).

---

[int](class_int.md#class-int) **src_image** = `-1`

-  **set_src_image**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_src_image**()

The index of the image associated with this texture, see [GLTFState.get_images()](class_gltfstate.md#class-gltfstate-method-get-images). If -1, then this texture does not have an image assigned.
