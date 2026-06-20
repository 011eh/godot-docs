# LookAtModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

The **LookAtModifier3D** rotates a bone to look at a target.

## Description

This [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) rotates a bone to look at a target. This is helpful for moving a character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

When applying multiple **LookAtModifier3D**s, the **LookAtModifier3D** assigned to the parent bone must be put above the **LookAtModifier3D** assigned to the child bone in the list in order for the child bone results to be correct.

## Properties

| [int](class_int.md#class-int)                                            | bone                                                           | `-1`               |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------|
| [String](class_string.md#class-string)                                   | bone_name                                                 | `""`               |
| [float](class_float.md#class-float)                                      | duration                                                   | `0.0`              |
| [EaseType](class_tween.md#enum-tween-easetype)                           | ease_type                                                 | `0`                |
| [BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) | forward_axis                                           | `4`                |
| [int](class_int.md#class-int)                                            | origin_bone                                             |                    |
| [String](class_string.md#class-string)                                   | origin_bone_name                                   |                    |
| [NodePath](class_nodepath.md#class-nodepath)                             | origin_external_node                           |                    |
| OriginFrom                          | origin_from                                             | `0`                |
| [Vector3](class_vector3.md#class-vector3)                                | origin_offset                                         | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float)                                      | origin_safe_margin                               | `0.1`              |
| [float](class_float.md#class-float)                                      | primary_damp_threshold                       |                    |
| [float](class_float.md#class-float)                                      | primary_limit_angle                             |                    |
| [float](class_float.md#class-float)                                      | primary_negative_damp_threshold     |                    |
| [float](class_float.md#class-float)                                      | primary_negative_limit_angle           |                    |
| [float](class_float.md#class-float)                                      | primary_positive_damp_threshold     |                    |
| [float](class_float.md#class-float)                                      | primary_positive_limit_angle           |                    |
| [Axis](class_vector3.md#enum-vector3-axis)                               | primary_rotation_axis                         | `1`                |
| [bool](class_bool.md#class-bool)                                         | relative                                                   | `false`            |
| [float](class_float.md#class-float)                                      | secondary_damp_threshold                   |                    |
| [float](class_float.md#class-float)                                      | secondary_limit_angle                         |                    |
| [float](class_float.md#class-float)                                      | secondary_negative_damp_threshold |                    |
| [float](class_float.md#class-float)                                      | secondary_negative_limit_angle       |                    |
| [float](class_float.md#class-float)                                      | secondary_positive_damp_threshold |                    |
| [float](class_float.md#class-float)                                      | secondary_positive_limit_angle       |                    |
| [bool](class_bool.md#class-bool)                                         | symmetry_limitation                             |                    |
| [NodePath](class_nodepath.md#class-nodepath)                             | target_node                                             | `NodePath("")`     |
| [TransitionType](class_tween.md#enum-tween-transitiontype)               | transition_type                                     | `0`                |
| [bool](class_bool.md#class-bool)                                         | use_angle_limitation                           | `false`            |
| [bool](class_bool.md#class-bool)                                         | use_secondary_rotation                       | `true`             |

## Methods

| [float](class_float.md#class-float)   | get_interpolation_remaining()    |
|---------------------------------------|------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)      | is_interpolating()                          |
| [bool](class_bool.md#class-bool)      | is_target_within_limitation()    |

---

## Enumerations

enum **OriginFrom**:

OriginFrom **ORIGIN_FROM_SELF** = `0`

The bone rest position of the bone specified in bone is used as origin.

OriginFrom **ORIGIN_FROM_SPECIFIC_BONE** = `1`

The bone global pose position of the bone specified in origin_bone is used as origin.

**Note:** It is recommended that you select only the parent bone unless you are familiar with the bone processing process. The specified bone pose at the time the **LookAtModifier3D** is processed is used as a reference. In other words, if you specify a child bone and the **LookAtModifier3D** causes the child bone to move, the rendered result and direction will not match.

OriginFrom **ORIGIN_FROM_EXTERNAL_NODE** = `2`

The global position of the [Node3D](class_node3d.md#class-node3d) specified in origin_external_node is used as origin.

**Note:** Same as ORIGIN_FROM_SPECIFIC_BONE, when specifying a [BoneAttachment3D](class_boneattachment3d.md#class-boneattachment3d) with a child bone assigned, the rendered result and direction will not match.

---

## Property Descriptions

[int](class_int.md#class-int) **bone** = `-1`

-  **set_bone**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone**()

Index of the bone_name in the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

---

[String](class_string.md#class-string) **bone_name** = `""`

-  **set_bone_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_bone_name**()

The bone name of the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) that the modification will operate on.

---

[float](class_float.md#class-float) **duration** = `0.0`

-  **set_duration**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_duration**()

The duration of the time-based interpolation. Interpolation is triggered at the following cases:

- When the target node is changed
- When an axis is flipped due to angle limitation

**Note:** The flipping occurs when the target is outside the angle limitation and the internally computed secondary rotation axis of the forward vector is flipped. Visually, it occurs when the target is outside the angle limitation and crosses the plane of the forward_axis and primary_rotation_axis.

---

[EaseType](class_tween.md#enum-tween-easetype) **ease_type** = `0`

-  **set_ease_type**(value: [EaseType](class_tween.md#enum-tween-easetype))
- [EaseType](class_tween.md#enum-tween-easetype) **get_ease_type**()

The ease type of the time-based interpolation. See also [EaseType](class_tween.md#enum-tween-easetype).

---

[BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **forward_axis** = `4`

-  **set_forward_axis**(value: [BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis))
- [BoneAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-boneaxis) **get_forward_axis**()

The forward axis of the bone. This [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) modifies the bone so that this axis points toward the target_node.

---

[int](class_int.md#class-int) **origin_bone**

-  **set_origin_bone**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_origin_bone**()

Index of the origin_bone_name in the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

---

[String](class_string.md#class-string) **origin_bone_name**

-  **set_origin_bone_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_origin_bone_name**()

If origin_from is ORIGIN_FROM_SPECIFIC_BONE, the bone global pose position specified for this is used as origin.

---

[NodePath](class_nodepath.md#class-nodepath) **origin_external_node**

-  **set_origin_external_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_origin_external_node**()

If origin_from is ORIGIN_FROM_EXTERNAL_NODE, the global position of the [Node3D](class_node3d.md#class-node3d) specified for this is used as origin.

---

OriginFrom **origin_from** = `0`

-  **set_origin_from**(value: OriginFrom)
- OriginFrom **get_origin_from**()

This value determines from what origin is retrieved for use in the calculation of the forward vector.

---

[Vector3](class_vector3.md#class-vector3) **origin_offset** = `Vector3(0, 0, 0)`

-  **set_origin_offset**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_origin_offset**()

The offset of the bone pose origin. Matching the origins by offset is useful for cases where multiple bones must always face the same direction, such as the eyes.

**Note:** This value indicates the local position of the object set in origin_from.

---

[float](class_float.md#class-float) **origin_safe_margin** = `0.1`

-  **set_origin_safe_margin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_origin_safe_margin**()

If the target passes through too close to the origin than this value, time-based interpolation is used even if the target is within the angular limitations, to prevent the angular velocity from becoming too high.

---

[float](class_float.md#class-float) **primary_damp_threshold**

-  **set_primary_damp_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_primary_damp_threshold**()

The threshold to start damping for primary_limit_angle. It provides non-linear (b-spline) interpolation, let it feel more resistance the more it rotate to the edge limit. This is useful for simulating the limits of human motion.

If `1.0`, no damping is performed. If `0.0`, damping is always performed.

---

[float](class_float.md#class-float) **primary_limit_angle**

-  **set_primary_limit_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_primary_limit_angle**()

The limit angle of the primary rotation when symmetry_limitation is `true`, in radians.

---

[float](class_float.md#class-float) **primary_negative_damp_threshold**

-  **set_primary_negative_damp_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_primary_negative_damp_threshold**()

The threshold to start damping for primary_negative_limit_angle.

---

[float](class_float.md#class-float) **primary_negative_limit_angle**

-  **set_primary_negative_limit_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_primary_negative_limit_angle**()

The limit angle of negative side of the primary rotation when symmetry_limitation is `false`, in radians.

---

[float](class_float.md#class-float) **primary_positive_damp_threshold**

-  **set_primary_positive_damp_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_primary_positive_damp_threshold**()

The threshold to start damping for primary_positive_limit_angle.

---

[float](class_float.md#class-float) **primary_positive_limit_angle**

-  **set_primary_positive_limit_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_primary_positive_limit_angle**()

The limit angle of positive side of the primary rotation when symmetry_limitation is `false`, in radians.

---

[Axis](class_vector3.md#enum-vector3-axis) **primary_rotation_axis** = `1`

-  **set_primary_rotation_axis**(value: [Axis](class_vector3.md#enum-vector3-axis))
- [Axis](class_vector3.md#enum-vector3-axis) **get_primary_rotation_axis**()

The axis of the first rotation. This [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) works by compositing the rotation by Euler angles to prevent to rotate the forward_axis.

---

[bool](class_bool.md#class-bool) **relative** = `false`

-  **set_relative**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_relative**()

The relative option. If `true`, the rotation is applied relative to the pose. If `false`, the rotation is applied relative to the rest. It means to replace the current pose with the **LookAtModifier3D**'s result.

**Note:** This option affects the base angle for use_angle_limitation. Since the **LookAtModifier3D** relies strongly on Euler rotation, the axis that determines the limitation and the actual rotation are strongly tied together.

---

[float](class_float.md#class-float) **secondary_damp_threshold**

-  **set_secondary_damp_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_secondary_damp_threshold**()

The threshold to start damping for secondary_limit_angle.

---

[float](class_float.md#class-float) **secondary_limit_angle**

-  **set_secondary_limit_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_secondary_limit_angle**()

The limit angle of the secondary rotation when symmetry_limitation is `true`, in radians.

---

[float](class_float.md#class-float) **secondary_negative_damp_threshold**

-  **set_secondary_negative_damp_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_secondary_negative_damp_threshold**()

The threshold to start damping for secondary_negative_limit_angle.

---

[float](class_float.md#class-float) **secondary_negative_limit_angle**

-  **set_secondary_negative_limit_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_secondary_negative_limit_angle**()

The limit angle of negative side of the secondary rotation when symmetry_limitation is `false`, in radians.

---

[float](class_float.md#class-float) **secondary_positive_damp_threshold**

-  **set_secondary_positive_damp_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_secondary_positive_damp_threshold**()

The threshold to start damping for secondary_positive_limit_angle.

---

[float](class_float.md#class-float) **secondary_positive_limit_angle**

-  **set_secondary_positive_limit_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_secondary_positive_limit_angle**()

The limit angle of positive side of the secondary rotation when symmetry_limitation is `false`, in radians.

---

[bool](class_bool.md#class-bool) **symmetry_limitation**

-  **set_symmetry_limitation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_limitation_symmetry**()

If `true`, the limitations are spread from the bone symmetrically.

If `false`, the limitation can be specified separately for each side of the bone rest.

---

[NodePath](class_nodepath.md#class-nodepath) **target_node** = `NodePath("")`

-  **set_target_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target_node**()

The [NodePath](class_nodepath.md#class-nodepath) to the node that is the target for the look at modification. This node is what the modification will rotate the bone to.

---

[TransitionType](class_tween.md#enum-tween-transitiontype) **transition_type** = `0`

-  **set_transition_type**(value: [TransitionType](class_tween.md#enum-tween-transitiontype))
- [TransitionType](class_tween.md#enum-tween-transitiontype) **get_transition_type**()

The transition type of the time-based interpolation. See also [TransitionType](class_tween.md#enum-tween-transitiontype).

---

[bool](class_bool.md#class-bool) **use_angle_limitation** = `false`

-  **set_use_angle_limitation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_angle_limitation**()

If `true`, limits the amount of rotation. For example, this helps to prevent a character's neck from rotating 360 degrees.

**Note:** As with [AnimationTree](class_animationtree.md#class-animationtree) blending, interpolation is provided that favors [Skeleton3D.get_bone_rest()](class_skeleton3d.md#class-skeleton3d-method-get-bone-rest) or [Skeleton3D.get_bone_pose()](class_skeleton3d.md#class-skeleton3d-method-get-bone-pose) depends on the relative option. This means that interpolation does not select the shortest path in some cases.

**Note:** Some values for transition_type (such as [Tween.TRANS_BACK](class_tween.md#class-tween-constant-trans-back), [Tween.TRANS_ELASTIC](class_tween.md#class-tween-constant-trans-elastic), and [Tween.TRANS_SPRING](class_tween.md#class-tween-constant-trans-spring)) may exceed the limitations. If interpolation occurs while overshooting the limitations, the result might not respect the bone rest.

---

[bool](class_bool.md#class-bool) **use_secondary_rotation** = `true`

-  **set_use_secondary_rotation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_secondary_rotation**()

If `true`, provides rotation by two axes.

---

## Method Descriptions

[float](class_float.md#class-float) **get_interpolation_remaining**()

Returns the remaining seconds of the time-based interpolation.

---

[bool](class_bool.md#class-bool) **is_interpolating**()

Returns `true` if time-based interpolation is running. If `true`, it is equivalent to get_interpolation_remaining() returning `0.0`.

This is useful to determine whether a **LookAtModifier3D** can be removed safely.

---

[bool](class_bool.md#class-bool) **is_target_within_limitation**()

Returns whether the target is within the angle limitations. It is useful for unsetting the target_node when the target is outside of the angle limitations.

**Note:** The value is updated after [SkeletonModifier3D._process_modification()](class_skeletonmodifier3d.md#class-skeletonmodifier3d-private-method-process-modification). To retrieve this value correctly, we recommend using the signal [SkeletonModifier3D.modification_processed](class_skeletonmodifier3d.md#class-skeletonmodifier3d-signal-modification-processed).
