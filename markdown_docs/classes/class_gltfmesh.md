# GLTFMesh

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

GLTFMesh represents a glTF mesh.

## Description

GLTFMesh handles 3D mesh data imported from glTF files. It includes properties for blend channels, blend weights, instance materials, and the mesh itself.

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

## Properties

| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)        | blend_weights           | `PackedFloat32Array()`   |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------|
| [Array](class_array.md#class-array)[[Material](class_material.md#class-material)] | instance_materials | `[]`                     |
| [ImporterMesh](class_importermesh.md#class-importermesh)                          | mesh                             |                          |
| [String](class_string.md#class-string)                                            | original_name           | `""`                     |

## Methods

| [Variant](class_variant.md#class-variant)   | get_additional_data(extension_name: [StringName](class_stringname.md#class-stringname))                                                             |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                             | set_additional_data(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) |

---

## Property Descriptions

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **blend_weights** = `PackedFloat32Array()`

-  **set_blend_weights**(value: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))
- [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_blend_weights**()

An array of floats representing the blend weights of the mesh.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) for more details.

---

[Array](class_array.md#class-array)[[Material](class_material.md#class-material)] **instance_materials** = `[]`

-  **set_instance_materials**(value: [Array](class_array.md#class-array)[[Material](class_material.md#class-material)])
- [Array](class_array.md#class-array)[[Material](class_material.md#class-material)] **get_instance_materials**()

An array of Material objects representing the materials used in the mesh.

---

[ImporterMesh](class_importermesh.md#class-importermesh) **mesh**

-  **set_mesh**(value: [ImporterMesh](class_importermesh.md#class-importermesh))
- [ImporterMesh](class_importermesh.md#class-importermesh) **get_mesh**()

The [ImporterMesh](class_importermesh.md#class-importermesh) object representing the mesh itself.

---

[String](class_string.md#class-string) **original_name** = `""`

-  **set_original_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_name**()

The original name of the mesh.

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **get_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname))

Gets additional arbitrary data in this **GLTFMesh** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

---

 **set_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant))

Sets additional arbitrary data in this **GLTFMesh** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class-gltfdocumentextension) name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.
