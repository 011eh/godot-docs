# TwoBoneIK3D

**Inherits:** [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Rotation based intersection of two circles inverse kinematics solver.

## Description

This [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) requires a pole target. It provides deterministic results by constructing a plane from each joint and pole target and finding the intersection of two circles (disks in 3D).

This IK can handle twist by setting the pole direction. If there are more than one bone between each set bone, their rotations are ignored, and the straight line connecting the root-middle and middle-end joints are treated as virtual bones.

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

## Properties

| [int](class_int.md#class-int)   | setting_count   | `0`   |
|---------------------------------|--------------------------------------------------------------|-------|

## Methods

| [int](class_int.md#class-int)                                                                | get_end_bone(index: [int](class_int.md#class-int))                                                                                                                         |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)           | get_end_bone_direction(index: [int](class_int.md#class-int))                                                                                                     |
| [float](class_float.md#class-float)                                                          | get_end_bone_length(index: [int](class_int.md#class-int))                                                                                                           |
| [String](class_string.md#class-string)                                                       | get_end_bone_name(index: [int](class_int.md#class-int))                                                                                                               |
| [int](class_int.md#class-int)                                                                | get_middle_bone(index: [int](class_int.md#class-int))                                                                                                                   |
| [String](class_string.md#class-string)                                                       | get_middle_bone_name(index: [int](class_int.md#class-int))                                                                                                         |
| [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) | get_pole_direction(index: [int](class_int.md#class-int))                                                                                                             |
| [Vector3](class_vector3.md#class-vector3)                                                    | get_pole_direction_vector(index: [int](class_int.md#class-int))                                                                                               |
| [NodePath](class_nodepath.md#class-nodepath)                                                 | get_pole_node(index: [int](class_int.md#class-int))                                                                                                                       |
| [int](class_int.md#class-int)                                                                | get_root_bone(index: [int](class_int.md#class-int))                                                                                                                       |
| [String](class_string.md#class-string)                                                       | get_root_bone_name(index: [int](class_int.md#class-int))                                                                                                             |
| [NodePath](class_nodepath.md#class-nodepath)                                                 | get_target_node(index: [int](class_int.md#class-int))                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                             | is_end_bone_extended(index: [int](class_int.md#class-int))                                                                                                         |
| [bool](class_bool.md#class-bool)                                                             | is_using_virtual_end(index: [int](class_int.md#class-int))                                                                                                         |
|                                                                                              | set_end_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                    |
|                                                                                              | set_end_bone_direction(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection)) |
|                                                                                              | set_end_bone_length(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float))                                                              |
|                                                                                              | set_end_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                            |
|                                                                                              | set_extend_end_bone(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                |
|                                                                                              | set_middle_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                              |
|                                                                                              | set_middle_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                      |
|                                                                                              | set_pole_direction(index: [int](class_int.md#class-int), direction: [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection))    |
|                                                                                              | set_pole_direction_vector(index: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3))                                            |
|                                                                                              | set_pole_node(index: [int](class_int.md#class-int), pole_node: [NodePath](class_nodepath.md#class-nodepath))                                                              |
|                                                                                              | set_root_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                  |
|                                                                                              | set_root_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                          |
|                                                                                              | set_target_node(index: [int](class_int.md#class-int), target_node: [NodePath](class_nodepath.md#class-nodepath))                                                        |
|                                                                                              | set_use_virtual_end(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                |

---

## Property Descriptions

[int](class_int.md#class-int) **setting_count** = `0`

-  **set_setting_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_setting_count**()

The number of settings.

---

## Method Descriptions

[int](class_int.md#class-int) **get_end_bone**(index: [int](class_int.md#class-int))

Returns the end bone index.

---

[BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) **get_end_bone_direction**(index: [int](class_int.md#class-int))

Returns the end bone's tail direction when is_end_bone_extended() is `true`.

---

[float](class_float.md#class-float) **get_end_bone_length**(index: [int](class_int.md#class-int))

Returns the end bone tail length of the bone chain when is_end_bone_extended() is `true`.

---

[String](class_string.md#class-string) **get_end_bone_name**(index: [int](class_int.md#class-int))

Returns the end bone name.

---

[int](class_int.md#class-int) **get_middle_bone**(index: [int](class_int.md#class-int))

Returns the middle bone index.

---

[String](class_string.md#class-string) **get_middle_bone_name**(index: [int](class_int.md#class-int))

Returns the middle bone name.

---

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **get_pole_direction**(index: [int](class_int.md#class-int))

Returns the pole direction.

---

[Vector3](class_vector3.md#class-vector3) **get_pole_direction_vector**(index: [int](class_int.md#class-int))

Returns the pole direction vector.

If get_pole_direction() is [SkeletonModifier3D.SECONDARY_DIRECTION_NONE](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-secondary-direction-none), this method returns `Vector3(0, 0, 0)`.

---

[NodePath](class_nodepath.md#class-nodepath) **get_pole_node**(index: [int](class_int.md#class-int))

Returns the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.

---

[int](class_int.md#class-int) **get_root_bone**(index: [int](class_int.md#class-int))

Returns the root bone index.

---

[String](class_string.md#class-string) **get_root_bone_name**(index: [int](class_int.md#class-int))

Returns the root bone name.

---

[NodePath](class_nodepath.md#class-nodepath) **get_target_node**(index: [int](class_int.md#class-int))

Returns the target node that the end bone is trying to reach.

---

[bool](class_bool.md#class-bool) **is_end_bone_extended**(index: [int](class_int.md#class-int))

Returns `true` if the end bone is extended to have a tail.

---

[bool](class_bool.md#class-bool) **is_using_virtual_end**(index: [int](class_int.md#class-int))

Returns `true` if the end bone is extended from the middle bone as a virtual bone.

---

 **set_end_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the end bone index.

---

 **set_end_bone_direction**(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection))

Sets the end bone tail direction when is_end_bone_extended() is `true`.

---

 **set_end_bone_length**(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float))

Sets the end bone tail length when is_end_bone_extended() is `true`.

---

 **set_end_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the end bone name.

**Note:** The end bone must be a child of the middle bone.

---

 **set_extend_end_bone**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the end bone is extended to have a tail.

---

 **set_middle_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the middle bone index.

---

 **set_middle_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the middle bone name.

**Note:** The middle bone must be a child of the root bone.

---

 **set_pole_direction**(index: [int](class_int.md#class-int), direction: [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection))

Sets the pole direction.

The pole is on the middle bone and will direct to the pole target.

The rotation axis is a vector that is orthogonal to this and the forward vector.

**Note:** The pole direction and the forward vector shouldn't be colinear to avoid unintended rotation.

---

 **set_pole_direction_vector**(index: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3))

Sets the pole direction vector.

This vector is normalized by an internal process.

If the vector length is `0`, it is considered synonymous with [SkeletonModifier3D.SECONDARY_DIRECTION_NONE](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-secondary-direction-none).

---

 **set_pole_node**(index: [int](class_int.md#class-int), pole_node: [NodePath](class_nodepath.md#class-nodepath))

Sets the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.

---

 **set_root_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the root bone index.

---

 **set_root_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the root bone name.

---

 **set_target_node**(index: [int](class_int.md#class-int), target_node: [NodePath](class_nodepath.md#class-nodepath))

Sets the target node that the end bone is trying to reach.

---

 **set_use_virtual_end**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the end bone is extended from the middle bone as a virtual bone.
