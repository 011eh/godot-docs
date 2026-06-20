# RetargetModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A modifier to transfer parent skeleton poses (or global poses) to child skeletons in model space with different rests.

## Description

Retrieves the pose (or global pose) relative to the parent Skeleton's rest in model space and transfers it to the child Skeleton.

This modifier rewrites the pose of the child skeleton directly in the parent skeleton's update process. This means that it overwrites the mapped bone pose set in the normal process on the target skeleton. If you want to set the target skeleton bone pose after retargeting, you will need to add a [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) child to the target skeleton and thereby modify the pose.

**Note:** When the use_global_pose is enabled, even if it is an unmapped bone, it can cause visual problems because the global pose is applied ignoring the parent bone's pose **if it has mapped bone children**. See also use_global_pose.

## Properties

| [TransformFlag]         | enable                   | `7`     |
|-------------------------------------------------------------------|-----------------------------------------------------------------------|---------|
| [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) | profile                 |         |
| [bool](class_bool.md#class-bool)                                  | use_global_pose | `false` |

## Methods

| [bool](class_bool.md#class-bool)   | is_position_enabled()                                            |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)   | is_rotation_enabled()                                            |
| [bool](class_bool.md#class-bool)   | is_scale_enabled()                                                  |
|                                    | set_position_enabled(enabled: [bool](class_bool.md#class-bool)) |
|                                    | set_rotation_enabled(enabled: [bool](class_bool.md#class-bool)) |
|                                    | set_scale_enabled(enabled: [bool](class_bool.md#class-bool))       |

---

## Enumerations

flags **TransformFlag**:

TransformFlag **TRANSFORM_FLAG_POSITION** = `1`

If set, allows to retarget the position.

TransformFlag **TRANSFORM_FLAG_ROTATION** = `2`

If set, allows to retarget the rotation.

TransformFlag **TRANSFORM_FLAG_SCALE** = `4`

If set, allows to retarget the scale.

TransformFlag **TRANSFORM_FLAG_ALL** = `7`

If set, allows to retarget the position/rotation/scale.

---

## Property Descriptions

[TransformFlag] **enable** = `7`

-  **set_enable_flags**(value: [TransformFlag])
- [TransformFlag] **get_enable_flags**()

Flags to control the process of the transform elements individually when use_global_pose is disabled.

---

[SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) **profile**

-  **set_profile**(value: [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile))
- [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) **get_profile**()

[SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) for retargeting bones with names matching the bone list.

---

[bool](class_bool.md#class-bool) **use_global_pose** = `false`

-  **set_use_global_pose**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_global_pose**()

If `false`, in case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform will be ignored.

Instead, it is possible to retarget between models with different body shapes, and position, rotation, and scale can be retargeted separately.

If `true`, retargeting is performed taking into account global pose.

In case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform is taken into account. However, bone length between skeletons must match exactly, if not, the bones will be forced to expand or shrink.

This is useful for using dummy bone with length `0` to match postures when retargeting between models with different number of bones.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **is_position_enabled**()

Returns `true` if enable has TRANSFORM_FLAG_POSITION.

---

[bool](class_bool.md#class-bool) **is_rotation_enabled**()

Returns `true` if enable has TRANSFORM_FLAG_ROTATION.

---

[bool](class_bool.md#class-bool) **is_scale_enabled**()

Returns `true` if enable has TRANSFORM_FLAG_SCALE.

---

 **set_position_enabled**(enabled: [bool](class_bool.md#class-bool))

Sets TRANSFORM_FLAG_POSITION into enable.

---

 **set_rotation_enabled**(enabled: [bool](class_bool.md#class-bool))

Sets TRANSFORM_FLAG_ROTATION into enable.

---

 **set_scale_enabled**(enabled: [bool](class_bool.md#class-bool))

Sets TRANSFORM_FLAG_SCALE into enable.
