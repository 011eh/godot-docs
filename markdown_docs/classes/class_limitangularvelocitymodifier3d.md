# LimitAngularVelocityModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Limit bone rotation angular velocity.

## Description

This modifier limits bone rotation angular velocity by comparing poses between previous and current frame.

You can add bone chains by specifying their root and end bones, then add the bones between them to a list. Modifier processes either that list or the bones excluding those in the list depending on the option exclude.

**Note:** Most methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

## Properties

| [int](class_int.md#class-int)       | chain_count                   | `0`         |
|-------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| [bool](class_bool.md#class-bool)    | exclude                           | `false`     |
| [int](class_int.md#class-int)       | joint_count                   | `0`         |
| [float](class_float.md#class-float) | max_angular_velocity | `6.2831855` |

## Methods

|                                        | clear_chains()                                                                                                    |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)          | get_end_bone(index: [int](class_int.md#class-int))                                                                |
| [String](class_string.md#class-string) | get_end_bone_name(index: [int](class_int.md#class-int))                                                      |
| [int](class_int.md#class-int)          | get_root_bone(index: [int](class_int.md#class-int))                                                              |
| [String](class_string.md#class-string) | get_root_bone_name(index: [int](class_int.md#class-int))                                                    |
|                                        | reset()                                                                                                                  |
|                                        | set_end_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                           |
|                                        | set_end_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))   |
|                                        | set_root_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                         |
|                                        | set_root_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |

---

## Property Descriptions

[int](class_int.md#class-int) **chain_count** = `0`

-  **set_chain_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_chain_count**()

The number of chains.

---

[bool](class_bool.md#class-bool) **exclude** = `false`

-  **set_exclude**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_exclude**()

If `true`, the modifier processes bones not included in the bone list.

If `false`, the bones processed by the modifier are equal to the bone list.

---

[int](class_int.md#class-int) **joint_count** = `0`

The number of joints in the list which created by chains dynamically.

---

[float](class_float.md#class-float) **max_angular_velocity** = `6.2831855`

-  **set_max_angular_velocity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_angular_velocity**()

The maximum angular velocity per second.

---

## Method Descriptions

 **clear_chains**()

Clear all chains.

---

[int](class_int.md#class-int) **get_end_bone**(index: [int](class_int.md#class-int))

Returns the end bone index of the bone chain.

---

[String](class_string.md#class-string) **get_end_bone_name**(index: [int](class_int.md#class-int))

Returns the end bone name of the bone chain.

---

[int](class_int.md#class-int) **get_root_bone**(index: [int](class_int.md#class-int))

Returns the root bone index of the bone chain.

---

[String](class_string.md#class-string) **get_root_bone_name**(index: [int](class_int.md#class-int))

Returns the root bone name of the bone chain.

---

 **reset**()

Sets the reference pose for angle comparison to the current pose with the influence of constraints removed. This function is automatically triggered when joints change or upon activation.

---

 **set_end_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the end bone index of the bone chain.

---

 **set_end_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the end bone name of the bone chain.

**Note:** End bone must be the root bone or a child of the root bone.

---

 **set_root_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the root bone index of the bone chain.

---

 **set_root_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the root bone name of the bone chain.
