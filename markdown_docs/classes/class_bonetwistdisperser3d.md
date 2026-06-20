# BoneTwistDisperser3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node that propagates and disperses the child bone's twist to the parent bones.

## Description

This **BoneTwistDisperser3D** allows for smooth twist interpolation between multiple bones by dispersing the end bone's twist to the parents. This only changes the twist without changing the global position of each joint.

This is useful for smoothly twisting bones in combination with [CopyTransformModifier3D](class_copytransformmodifier3d.md#class-copytransformmodifier3d) and IK.

**Note:** If an extracted twist is greater than 180 degrees, flipping occurs. This is similar to [ConvertTransformModifier3D](class_converttransformmodifier3d.md#class-converttransformmodifier3d).

**Note:** Most methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

## Properties

| [bool](class_bool.md#class-bool)   | mutable_bone_axes   | `true`   |
|------------------------------------|-------------------------------------------------------------------------------|----------|
| [int](class_int.md#class-int)      | setting_count           | `0`      |

## Methods

|                                                                                    | clear_settings()                                                                                                                                                         |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Curve](class_curve.md#class-curve)                                                | get_damping_curve(index: [int](class_int.md#class-int))                                                                                                               |
| DisperseMode                            | get_disperse_mode(index: [int](class_int.md#class-int))                                                                                                               |
| [int](class_int.md#class-int)                                                      | get_end_bone(index: [int](class_int.md#class-int))                                                                                                                         |
| [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) | get_end_bone_direction(index: [int](class_int.md#class-int))                                                                                                     |
| [String](class_string.md#class-string)                                             | get_end_bone_name(index: [int](class_int.md#class-int))                                                                                                               |
| [int](class_int.md#class-int)                                                      | get_joint_bone(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                               |
| [String](class_string.md#class-string)                                             | get_joint_bone_name(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                     |
| [int](class_int.md#class-int)                                                      | get_joint_count(index: [int](class_int.md#class-int))                                                                                                                   |
| [float](class_float.md#class-float)                                                | get_joint_twist_amount(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                               |
| [int](class_int.md#class-int)                                                      | get_reference_bone(index: [int](class_int.md#class-int))                                                                                                             |
| [String](class_string.md#class-string)                                             | get_reference_bone_name(index: [int](class_int.md#class-int))                                                                                                   |
| [int](class_int.md#class-int)                                                      | get_root_bone(index: [int](class_int.md#class-int))                                                                                                                       |
| [String](class_string.md#class-string)                                             | get_root_bone_name(index: [int](class_int.md#class-int))                                                                                                             |
| [Quaternion](class_quaternion.md#class-quaternion)                                 | get_twist_from(index: [int](class_int.md#class-int))                                                                                                                     |
| [float](class_float.md#class-float)                                                | get_weight_position(index: [int](class_int.md#class-int))                                                                                                           |
| [bool](class_bool.md#class-bool)                                                   | is_end_bone_extended(index: [int](class_int.md#class-int))                                                                                                         |
| [bool](class_bool.md#class-bool)                                                   | is_twist_from_rest(index: [int](class_int.md#class-int))                                                                                                             |
|                                                                                    | set_damping_curve(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))                                                                   |
|                                                                                    | set_disperse_mode(index: [int](class_int.md#class-int), disperse_mode: DisperseMode)                                       |
|                                                                                    | set_end_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                    |
|                                                                                    | set_end_bone_direction(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)) |
|                                                                                    | set_end_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                            |
|                                                                                    | set_extend_end_bone(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                |
|                                                                                    | set_joint_twist_amount(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), twist_amount: [float](class_float.md#class-float))            |
|                                                                                    | set_root_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                  |
|                                                                                    | set_root_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                          |
|                                                                                    | set_twist_from(index: [int](class_int.md#class-int), from: [Quaternion](class_quaternion.md#class-quaternion))                                                           |
|                                                                                    | set_twist_from_rest(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                |
|                                                                                    | set_weight_position(index: [int](class_int.md#class-int), weight_position: [float](class_float.md#class-float))                                                     |

---

## Enumerations

enum **DisperseMode**:

DisperseMode **DISPERSE_MODE_EVEN** = `0`

Assign amounts so that they monotonically increase from `0.0` to `1.0`, ensuring all weights are equal. For example, with five joints, the amounts would be `0.2`, `0.4`, `0.6`, `0.8`, and `1.0` starting from the root bone.

DisperseMode **DISPERSE_MODE_WEIGHTED** = `1`

Assign amounts so that they monotonically increase from `0.0` to `1.0`, based on the length of the bones between joint segments. See also set_weight_position().

DisperseMode **DISPERSE_MODE_CUSTOM** = `2`

You can assign arbitrary amounts to the joint list. See also set_joint_twist_amount().

When is_end_bone_extended() is `false`, a child of the reference bone exists solely to determine the twist axis, so its custom amount has absolutely no effect at all.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **mutable_bone_axes** = `true`

-  **set_mutable_bone_axes**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_bone_axes_mutable**()

If `true`, the solver retrieves the bone axis from the bone pose every frame.

If `false`, the solver retrieves the bone axis from the bone rest and caches it.

---

[int](class_int.md#class-int) **setting_count** = `0`

-  **set_setting_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_setting_count**()

The number of settings.

---

## Method Descriptions

 **clear_settings**()

Clears all settings.

---

[Curve](class_curve.md#class-curve) **get_damping_curve**(index: [int](class_int.md#class-int))

Returns the damping curve when get_disperse_mode() is DISPERSE_MODE_CUSTOM.

---

DisperseMode **get_disperse_mode**(index: [int](class_int.md#class-int))

Returns whether to use automatic amount assignment or to allow manual assignment.

---

[int](class_int.md#class-int) **get_end_bone**(index: [int](class_int.md#class-int))

Returns the end bone index of the bone chain.

---

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **get_end_bone_direction**(index: [int](class_int.md#class-int))

Returns the tail direction of the end bone of the bone chain when is_end_bone_extended() is `true`.

---

[String](class_string.md#class-string) **get_end_bone_name**(index: [int](class_int.md#class-int))

Returns the end bone name of the bone chain.

---

[int](class_int.md#class-int) **get_joint_bone**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the bone index at `joint` in the bone chain's joint list.

---

[String](class_string.md#class-string) **get_joint_bone_name**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the bone name at `joint` in the bone chain's joint list.

---

[int](class_int.md#class-int) **get_joint_count**(index: [int](class_int.md#class-int))

Returns the joint count of the bone chain's joint list.

---

[float](class_float.md#class-float) **get_joint_twist_amount**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the twist amount at `joint` in the bone chain's joint list when get_disperse_mode() is DISPERSE_MODE_CUSTOM.

---

[int](class_int.md#class-int) **get_reference_bone**(index: [int](class_int.md#class-int))

Returns the reference bone to extract twist of the setting at `index`.

This bone is either the end of the chain or its parent, depending on is_end_bone_extended().

---

[String](class_string.md#class-string) **get_reference_bone_name**(index: [int](class_int.md#class-int))

Returns the reference bone name to extract twist of the setting at `index`.

This bone is either the end of the chain or its parent, depending on is_end_bone_extended().

---

[int](class_int.md#class-int) **get_root_bone**(index: [int](class_int.md#class-int))

Returns the root bone index of the bone chain.

---

[String](class_string.md#class-string) **get_root_bone_name**(index: [int](class_int.md#class-int))

Returns the root bone name of the bone chain.

---

[Quaternion](class_quaternion.md#class-quaternion) **get_twist_from**(index: [int](class_int.md#class-int))

Returns the rotation to an arbitrary state before twisting for the current bone pose to extract the twist when is_twist_from_rest() is `false`.

---

[float](class_float.md#class-float) **get_weight_position**(index: [int](class_int.md#class-int))

Returns the position at which to divide the segment between joints for weight assignment when get_disperse_mode() is DISPERSE_MODE_WEIGHTED.

---

[bool](class_bool.md#class-bool) **is_end_bone_extended**(index: [int](class_int.md#class-int))

Returns `true` if the end bone is extended to have a tail.

---

[bool](class_bool.md#class-bool) **is_twist_from_rest**(index: [int](class_int.md#class-int))

Returns `true` if extracting the twist amount from the difference between the bone rest and the current bone pose.

---

 **set_damping_curve**(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))

Sets the damping curve when get_disperse_mode() is DISPERSE_MODE_CUSTOM.

---

 **set_disperse_mode**(index: [int](class_int.md#class-int), disperse_mode: DisperseMode)

Sets whether to use automatic amount assignment or to allow manual assignment.

---

 **set_end_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the end bone index of the bone chain.

---

 **set_end_bone_direction**(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection))

Sets the end bone tail direction of the bone chain when is_end_bone_extended() is `true`.

---

 **set_end_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the end bone name of the bone chain.

**Note:** The end bone must be a child of the root bone.

---

 **set_extend_end_bone**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the end bone is extended to have a tail.

If `enabled` is `false`, get_reference_bone() becomes a parent of the end bone and it uses the vector to the end bone as a twist axis.

---

 **set_joint_twist_amount**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), twist_amount: [float](class_float.md#class-float))

Sets the twist amount at `joint` in the bone chain's joint list when get_disperse_mode() is DISPERSE_MODE_CUSTOM.

---

 **set_root_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the root bone index of the bone chain.

---

 **set_root_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the root bone name of the bone chain.

---

 **set_twist_from**(index: [int](class_int.md#class-int), from: [Quaternion](class_quaternion.md#class-quaternion))

Sets the rotation to an arbitrary state before twisting for the current bone pose to extract the twist when is_twist_from_rest() is `false`.

In other words, by calling set_twist_from() by [SkeletonModifier3D.modification_processed](class_skeletonmodifier3d.md#class-skeletonmodifier3d-signal-modification-processed) of a specific [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d), you can extract only the twists generated by modifiers processed after that but before this **BoneTwistDisperser3D**.

---

 **set_twist_from_rest**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, it extracts the twist amount from the difference between the bone rest and the current bone pose.

If `enabled` is `false`, it extracts the twist amount from the difference between get_twist_from() and the current bone pose. See also set_twist_from().

---

 **set_weight_position**(index: [int](class_int.md#class-int), weight_position: [float](class_float.md#class-float))

Sets the position at which to divide the segment between joints for weight assignment when get_disperse_mode() is DISPERSE_MODE_WEIGHTED.

For example, when `weight_position` is `0.5`, if two bone segments with a length of `1.0` exist between three joints, weights are assigned to each joint from root to end at ratios of `0.5`, `1.0`, and `0.5`. Then amounts become `0.25`, `0.75`, and `1.0` respectively.
