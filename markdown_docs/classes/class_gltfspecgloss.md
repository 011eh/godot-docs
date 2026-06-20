# GLTFSpecGloss

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Archived glTF extension for specular/glossy materials.

## Description

KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This means that it is deprecated and not recommended for new files. However, it is still supported for loading old files.

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [KHR_materials_pbrSpecularGlossiness glTF extension spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Archived/KHR_materials_pbrSpecularGlossiness)

## Properties

| [Color](class_color.md#class-color)   | diffuse_factor   | `Color(1, 1, 1, 1)`   |
|---------------------------------------|------------------------------------------------------------------|-----------------------|
| [Image](class_image.md#class-image)   | diffuse_img         |                       |
| [float](class_float.md#class-float)   | gloss_factor       | `1.0`                 |
| [Image](class_image.md#class-image)   | spec_gloss_img   |                       |
| [Color](class_color.md#class-color)   | specular_factor | `Color(1, 1, 1, 1)`   |

---

## Property Descriptions

[Color](class_color.md#class-color) **diffuse_factor** = `Color(1, 1, 1, 1)`

-  **set_diffuse_factor**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_diffuse_factor**()

The reflected diffuse factor of the material.

---

[Image](class_image.md#class-image) **diffuse_img**

-  **set_diffuse_img**(value: [Image](class_image.md#class-image))
- [Image](class_image.md#class-image) **get_diffuse_img**()

The diffuse texture.

---

[float](class_float.md#class-float) **gloss_factor** = `1.0`

-  **set_gloss_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gloss_factor**()

The glossiness or smoothness of the material.

---

[Image](class_image.md#class-image) **spec_gloss_img**

-  **set_spec_gloss_img**(value: [Image](class_image.md#class-image))
- [Image](class_image.md#class-image) **get_spec_gloss_img**()

The specular-glossiness texture.

---

[Color](class_color.md#class-color) **specular_factor** = `Color(1, 1, 1, 1)`

-  **set_specular_factor**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_specular_factor**()

The specular RGB color of the material. The alpha channel is unused.
