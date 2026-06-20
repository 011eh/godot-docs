# GLTFSkin

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

## Properties

| [Skin](class_skin.md#class-skin)                                     | godot_skin           |                      |
|----------------------------------------------------------------------|-------------------------------------------------------------|----------------------|
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | joints                   | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | joints_original | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | non_joints           | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | roots                     | `PackedInt32Array()` |
| [int](class_int.md#class-int)                                        | skeleton               | `-1`                 |
| [int](class_int.md#class-int)                                        | skin_root             | `-1`                 |

## Methods

| [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)]   | get_inverse_binds()                                                                                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Dictionary](class_dictionary.md#class-dictionary)                                           | get_joint_i_to_bone_i()                                                                                                  |
| [Dictionary](class_dictionary.md#class-dictionary)                                           | get_joint_i_to_name()                                                                                                      |
|                                                                                              | set_inverse_binds(inverse_binds: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)]) |
|                                                                                              | set_joint_i_to_bone_i(joint_i_to_bone_i: [Dictionary](class_dictionary.md#class-dictionary))                             |
|                                                                                              | set_joint_i_to_name(joint_i_to_name: [Dictionary](class_dictionary.md#class-dictionary))                                   |

---

## Property Descriptions

[Skin](class_skin.md#class-skin) **godot_skin**

-  **set_godot_skin**(value: [Skin](class_skin.md#class-skin))
- [Skin](class_skin.md#class-skin) **get_godot_skin**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **joints** = `PackedInt32Array()`

-  **set_joints**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_joints**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **joints_original** = `PackedInt32Array()`

-  **set_joints_original**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_joints_original**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **non_joints** = `PackedInt32Array()`

-  **set_non_joints**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_non_joints**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **roots** = `PackedInt32Array()`

-  **set_roots**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_roots**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[int](class_int.md#class-int) **skeleton** = `-1`

-  **set_skeleton**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_skeleton**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **skin_root** = `-1`

-  **set_skin_root**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_skin_root**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

## Method Descriptions

[Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)] **get_inverse_binds**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **get_joint_i_to_bone_i**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **get_joint_i_to_name**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_inverse_binds**(inverse_binds: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)])

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_joint_i_to_bone_i**(joint_i_to_bone_i: [Dictionary](class_dictionary.md#class-dictionary))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_joint_i_to_name**(joint_i_to_name: [Dictionary](class_dictionary.md#class-dictionary))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
