# GLTFAnimation

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

## Properties

| [bool](class_bool.md#class-bool)       | loop                   | `false`   |
|----------------------------------------|--------------------------------------------------------------|-----------|
| [String](class_string.md#class-string) | original_name | `""`      |

## Methods

| [Variant](class_variant.md#class-variant)   | get_additional_data(extension_name: [StringName](class_stringname.md#class-stringname))                                                             |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                             | set_additional_data(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **loop** = `false`

-  **set_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_loop**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **original_name** = `""`

-  **set_original_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_name**()

The original name of the animation.

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **get_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname))

Gets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

---

 **set_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant))

Sets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.
