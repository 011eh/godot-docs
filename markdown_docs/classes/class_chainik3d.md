# ChainIK3D

**Inherits:** [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [IterateIK3D](class_iterateik3d.md#class-iterateik3d), [SplineIK3D](class_splineik3d.md#class-splineik3d)

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) to apply inverse kinematics to bone chains containing an arbitrary number of bones.

## Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) that automatically generates a joint list from the bones between the root bone and the end bone.

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

## Methods

| [int](class_int.md#class-int)                                                      | get_end_bone(index: [int](class_int.md#class-int))                                                                                                                         |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) | get_end_bone_direction(index: [int](class_int.md#class-int))                                                                                                     |
| [float](class_float.md#class-float)                                                | get_end_bone_length(index: [int](class_int.md#class-int))                                                                                                           |
| [String](class_string.md#class-string)                                             | get_end_bone_name(index: [int](class_int.md#class-int))                                                                                                               |
| [int](class_int.md#class-int)                                                      | get_joint_bone(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                               |
| [String](class_string.md#class-string)                                             | get_joint_bone_name(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                     |
| [int](class_int.md#class-int)                                                      | get_joint_count(index: [int](class_int.md#class-int))                                                                                                                   |
| [int](class_int.md#class-int)                                                      | get_root_bone(index: [int](class_int.md#class-int))                                                                                                                       |
| [String](class_string.md#class-string)                                             | get_root_bone_name(index: [int](class_int.md#class-int))                                                                                                             |
| [bool](class_bool.md#class-bool)                                                   | is_end_bone_extended(index: [int](class_int.md#class-int))                                                                                                         |
|                                                                                    | set_end_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                    |
|                                                                                    | set_end_bone_direction(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)) |
|                                                                                    | set_end_bone_length(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float))                                                              |
|                                                                                    | set_end_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                            |
|                                                                                    | set_extend_end_bone(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                |
|                                                                                    | set_root_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                  |
|                                                                                    | set_root_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                          |

---

## Method Descriptions

[int](class_int.md#class-int) **get_end_bone**(index: [int](class_int.md#class-int))

Returns the end bone index of the bone chain.

---

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **get_end_bone_direction**(index: [int](class_int.md#class-int))

Returns the tail direction of the end bone of the bone chain when is_end_bone_extended() is `true`.

---

[float](class_float.md#class-float) **get_end_bone_length**(index: [int](class_int.md#class-int))

Returns the end bone tail length of the bone chain when is_end_bone_extended() is `true`.

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

[int](class_int.md#class-int) **get_root_bone**(index: [int](class_int.md#class-int))

Returns the root bone index of the bone chain.

---

[String](class_string.md#class-string) **get_root_bone_name**(index: [int](class_int.md#class-int))

Returns the root bone name of the bone chain.

---

[bool](class_bool.md#class-bool) **is_end_bone_extended**(index: [int](class_int.md#class-int))

Returns `true` if the end bone is extended to have a tail.

---

 **set_end_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the end bone index of the bone chain.

---

 **set_end_bone_direction**(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection))

Sets the end bone tail direction of the bone chain when is_end_bone_extended() is `true`.

---

 **set_end_bone_length**(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float))

Sets the end bone tail length of the bone chain when is_end_bone_extended() is `true`.

---

 **set_end_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the end bone name of the bone chain.

**Note:** The end bone must be the root bone or a child of the root bone. If they are the same, the tail must be extended by set_extend_end_bone() to modify the bone.

---

 **set_extend_end_bone**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the end bone is extended to have a tail.

The extended tail config is allocated to the last element in the joint list. In other words, if you set `enabled` to `false`, the config of the last element in the joint list has no effect in the simulated result.

---

 **set_root_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the root bone index of the bone chain.

---

 **set_root_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the root bone name of the bone chain.
