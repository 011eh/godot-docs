# AimModifier3D

**Inherits:** [BoneConstraint3D](class_boneconstraint3d.md#class-boneconstraint3d) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

The **AimModifier3D** rotates a bone to look at a reference bone.

## Description

This is a simple version of [LookAtModifier3D](class_lookatmodifier3d.md#class-lookatmodifier3d) that only allows bone to the reference without advanced options such as angle limitation or time-based interpolation.

The feature is simplified, but instead it is implemented with smooth tracking without euler, see set_use_euler().

## Properties

| [int](class_int.md#class-int)   | setting_count   | `0`   |
|---------------------------------|----------------------------------------------------------------|-------|

## Methods

| [BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis)   | get_forward_axis(index: [int](class_int.md#class-int))                                                                                 |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Axis](class_vector3.md#enum-vector3-axis)                                 | get_primary_rotation_axis(index: [int](class_int.md#class-int))                                                               |
| [bool](class_bool.md#class-bool)                                           | is_relative(index: [int](class_int.md#class-int))                                                                                           |
| [bool](class_bool.md#class-bool)                                           | is_using_euler(index: [int](class_int.md#class-int))                                                                                     |
| [bool](class_bool.md#class-bool)                                           | is_using_secondary_rotation(index: [int](class_int.md#class-int))                                                           |
|                                                                            | set_forward_axis(index: [int](class_int.md#class-int), axis: [BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis)) |
|                                                                            | set_primary_rotation_axis(index: [int](class_int.md#class-int), axis: [Axis](class_vector3.md#enum-vector3-axis))             |
|                                                                            | set_relative(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                              |
|                                                                            | set_use_euler(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                            |
|                                                                            | set_use_secondary_rotation(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                  |

---

## Property Descriptions

[int](class_int.md#class-int) **setting_count** = `0`

-  **set_setting_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_setting_count**()

The number of settings in the modifier.

---

## Method Descriptions

[BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **get_forward_axis**(index: [int](class_int.md#class-int))

Returns the forward axis of the bone.

---

[Axis](class_vector3.md#enum-vector3-axis) **get_primary_rotation_axis**(index: [int](class_int.md#class-int))

Returns the axis of the first rotation. It is enabled only if is_using_euler() is `true`.

---

[bool](class_bool.md#class-bool) **is_relative**(index: [int](class_int.md#class-int))

Returns `true` if the relative option is enabled in the setting at `index`.

---

[bool](class_bool.md#class-bool) **is_using_euler**(index: [int](class_int.md#class-int))

Returns `true` if it provides rotation with using euler.

---

[bool](class_bool.md#class-bool) **is_using_secondary_rotation**(index: [int](class_int.md#class-int))

Returns `true` if it provides rotation by two axes. It is enabled only if is_using_euler() is `true`.

---

 **set_forward_axis**(index: [int](class_int.md#class-int), axis: [BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis))

Sets the forward axis of the bone.

---

 **set_primary_rotation_axis**(index: [int](class_int.md#class-int), axis: [Axis](class_vector3.md#enum-vector3-axis))

Sets the axis of the first rotation. It is enabled only if is_using_euler() is `true`.

---

 **set_relative**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

Sets relative option in the setting at `index` to `enabled`.

If sets `enabled` to `true`, the rotation is applied relative to the pose.

If sets `enabled` to `false`, the rotation is applied relative to the rest. It means to replace the current pose with the **AimModifier3D**'s result.

---

 **set_use_euler**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If sets `enabled` to `true`, it provides rotation with using euler.

If sets `enabled` to `false`, it provides rotation with using rotation by arc generated from the forward axis vector and the vector toward the reference.

---

 **set_use_secondary_rotation**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If sets `enabled` to `true`, it provides rotation by two axes. It is enabled only if is_using_euler() is `true`.
