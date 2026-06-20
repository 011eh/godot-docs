# GLTFSkeleton

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

## Properties

| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | joints   | `PackedInt32Array()`   |
|------------------------------------------------------------------------|-------------------------------------------------|------------------------|
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | roots     | `PackedInt32Array()`   |

## Methods

| [BoneAttachment3D](class_boneattachment3d.md#class-boneattachment3d)        | get_bone_attachment(idx: [int](class_int.md#class-int))                                                  |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                               | get_bone_attachment_count()                                                                        |
| [Dictionary](class_dictionary.md#class-dictionary)                          | get_godot_bone_node()                                                                                    |
| [Skeleton3D](class_skeleton3d.md#class-skeleton3d)                          | get_godot_skeleton()                                                                                      |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)] | get_unique_names()                                                                                          |
|                                                                             | set_godot_bone_node(godot_bone_node: [Dictionary](class_dictionary.md#class-dictionary))                 |
|                                                                             | set_unique_names(unique_names: [Array](class_array.md#class-array)[[String](class_string.md#class-string)]) |

---

## Property Descriptions

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **joints** = `PackedInt32Array()`

-  **set_joints**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_joints**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **roots** = `PackedInt32Array()`

-  **set_roots**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_roots**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

## Method Descriptions

[BoneAttachment3D](class_boneattachment3d.md#class-boneattachment3d) **get_bone_attachment**(idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **get_bone_attachment_count**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **get_godot_bone_node**()

Returns a [Dictionary](class_dictionary.md#class-dictionary) that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

---

[Skeleton3D](class_skeleton3d.md#class-skeleton3d) **get_godot_skeleton**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **get_unique_names**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_godot_bone_node**(godot_bone_node: [Dictionary](class_dictionary.md#class-dictionary))

Sets a [Dictionary](class_dictionary.md#class-dictionary) that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

---

 **set_unique_names**(unique_names: [Array](class_array.md#class-array)[[String](class_string.md#class-string)])

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
