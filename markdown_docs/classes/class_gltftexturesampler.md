# GLTFTextureSampler

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a glTF texture sampler

## Description

Represents a texture sampler as defined by the base glTF spec. Texture samplers in glTF specify how to sample data from the texture's base image, when rendering the texture on an object.

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

## Properties

| [int](class_int.md#class-int)   | mag_filter   | `9729`   |
|---------------------------------|---------------------------------------------------------------|----------|
| [int](class_int.md#class-int)   | min_filter   | `9987`   |
| [int](class_int.md#class-int)   | wrap_s           | `10497`  |
| [int](class_int.md#class-int)   | wrap_t           | `10497`  |

---

## Property Descriptions

[int](class_int.md#class-int) **mag_filter** = `9729`

-  **set_mag_filter**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_mag_filter**()

Texture's magnification filter, used when texture appears larger on screen than the source image.

---

[int](class_int.md#class-int) **min_filter** = `9987`

-  **set_min_filter**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_min_filter**()

Texture's minification filter, used when the texture appears smaller on screen than the source image.

---

[int](class_int.md#class-int) **wrap_s** = `10497`

-  **set_wrap_s**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_wrap_s**()

Wrapping mode to use for S-axis (horizontal) texture coordinates.

---

[int](class_int.md#class-int) **wrap_t** = `10497`

-  **set_wrap_t**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_wrap_t**()

Wrapping mode to use for T-axis (vertical) texture coordinates.
