# IterateIK3D

**Inherits:** [ChainIK3D](class_chainik3d.md#class-chainik3d) **<** [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [CCDIK3D](class_ccdik3d.md#class-ccdik3d), [FABRIK3D](class_fabrik3d.md#class-fabrik3d), [JacobianIK3D](class_jacobianik3d.md#class-jacobianik3d)

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) to approach the goal by repeating small rotations.

## Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) to approach the goal by repeating small rotations.

Each bone chain (setting) has one effector, which is processed in order of the setting list. You can set some limitations for each joint.

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/target_node`).

## Properties

| [float](class_float.md#class-float)   | angular_delta_limit   | `0.034906585`   |
|---------------------------------------|--------------------------------------------------------------------------|-----------------|
| [bool](class_bool.md#class-bool)      | deterministic               | `false`         |
| [int](class_int.md#class-int)         | max_iterations             | `4`             |
| [float](class_float.md#class-float)   | min_distance                 | `0.001`         |
| [int](class_int.md#class-int)         | setting_count               | `0`             |

## Methods

| [JointLimitation3D](class_jointlimitation3d.md#class-jointlimitation3d)                      | get_joint_limitation(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                                                |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) | get_joint_limitation_right_axis(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                          |
| [Vector3](class_vector3.md#class-vector3)                                                    | get_joint_limitation_right_axis_vector(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                            |
| [Quaternion](class_quaternion.md#class-quaternion)                                           | get_joint_limitation_rotation_offset(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                |
| [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis)             | get_joint_rotation_axis(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                                          |
| [Vector3](class_vector3.md#class-vector3)                                                    | get_joint_rotation_axis_vector(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                            |
| [NodePath](class_nodepath.md#class-nodepath)                                                 | get_target_node(index: [int](class_int.md#class-int))                                                                                                                                                                                |
|                                                                                              | set_joint_limitation(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), limitation: [JointLimitation3D](class_jointlimitation3d.md#class-jointlimitation3d))                                           |
|                                                                                              | set_joint_limitation_right_axis(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), direction: [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection)) |
|                                                                                              | set_joint_limitation_right_axis_vector(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3))                                         |
|                                                                                              | set_joint_limitation_rotation_offset(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), offset: [Quaternion](class_quaternion.md#class-quaternion))                                    |
|                                                                                              | set_joint_rotation_axis(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), axis: [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis))                                  |
|                                                                                              | set_joint_rotation_axis_vector(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), axis_vector: [Vector3](class_vector3.md#class-vector3))                                                    |
|                                                                                              | set_target_node(index: [int](class_int.md#class-int), target_node: [NodePath](class_nodepath.md#class-nodepath))                                                                                                                     |

---

## Property Descriptions

[float](class_float.md#class-float) **angular_delta_limit** = `0.034906585`

-  **set_angular_delta_limit**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_angular_delta_limit**()

The maximum amount each bone can rotate in a single iteration.

**Note:** This limitation is applied during each iteration. For example, if max_iterations is `4` and angular_delta_limit is `5` degrees, the maximum rotation possible in a single frame is `20` degrees.

---

[bool](class_bool.md#class-bool) **deterministic** = `false`

-  **set_deterministic**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deterministic**()

If `false`, the result is calculated from the previous frame's **IterateIK3D** result as the initial state.

If `true`, the previous frame's **IterateIK3D** result is discarded. At this point, the new result is calculated from the bone pose excluding the **IterateIK3D** as the initial state. This means the result will be always equal as long as the target position and the previous bone pose are the same. However, if angular_delta_limit and max_iterations are set too small, the end bone of the chain will never reach the target.

---

[int](class_int.md#class-int) **max_iterations** = `4`

-  **set_max_iterations**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_iterations**()

The number of iteration loops used by the IK solver to produce more accurate results.

---

[float](class_float.md#class-float) **min_distance** = `0.001`

-  **set_min_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_distance**()

The minimum distance between the end bone and the target. If the distance is below this value, the IK solver stops any further iterations.

---

[int](class_int.md#class-int) **setting_count** = `0`

-  **set_setting_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_setting_count**()

The number of settings.

---

## Method Descriptions

[JointLimitation3D](class_jointlimitation3d.md#class-jointlimitation3d) **get_joint_limitation**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the joint limitation at `joint` in the bone chain's joint list.

---

[SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection) **get_joint_limitation_right_axis**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the joint limitation right axis at `joint` in the bone chain's joint list.

---

[Vector3](class_vector3.md#class-vector3) **get_joint_limitation_right_axis_vector**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the joint limitation right axis vector at `joint` in the bone chain's joint list.

If get_joint_limitation_right_axis() is [SkeletonModifier3D.SECONDARY_DIRECTION_NONE](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-secondary-direction-none), this method returns `Vector3(0, 0, 0)`.

---

[Quaternion](class_quaternion.md#class-quaternion) **get_joint_limitation_rotation_offset**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the joint limitation rotation offset at `joint` in the bone chain's joint list.

Rotation is done in the local space which is constructed by the bone direction (in general parent to child) as the +Y axis and get_joint_limitation_right_axis_vector() as the +X axis.

If the +X and +Y axes are not orthogonal, the +X axis is implicitly modified to make it orthogonal.

Also, if the length of get_joint_limitation_right_axis_vector() is zero, the space is created by rotating the reference pose using the shortest arc that rotates the +Y axis of the reference pose to match the bone direction.

In here, the reference pose is the bone pose immediately before processing IK.

---

[RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis) **get_joint_rotation_axis**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the rotation axis at `joint` in the bone chain's joint list.

---

[Vector3](class_vector3.md#class-vector3) **get_joint_rotation_axis_vector**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the rotation axis vector for the specified joint in the bone chain. This vector represents the axis around which the joint can rotate. It is determined based on the rotation axis set for the joint.

If get_joint_rotation_axis() is [SkeletonModifier3D.ROTATION_AXIS_ALL](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-all), this method returns `Vector3(0, 0, 0)`.

---

[NodePath](class_nodepath.md#class-nodepath) **get_target_node**(index: [int](class_int.md#class-int))

Returns the target node that the end bone is trying to reach.

---

 **set_joint_limitation**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), limitation: [JointLimitation3D](class_jointlimitation3d.md#class-jointlimitation3d))

Sets the joint limitation at `joint` in the bone chain's joint list.

---

 **set_joint_limitation_right_axis**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), direction: [SecondaryDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-secondarydirection))

Sets the joint limitation right axis at `joint` in the bone chain's joint list.

---

 **set_joint_limitation_right_axis_vector**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3))

Sets the optional joint limitation right axis vector at `joint` in the bone chain's joint list.

---

 **set_joint_limitation_rotation_offset**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), offset: [Quaternion](class_quaternion.md#class-quaternion))

Sets the joint limitation rotation offset at `joint` in the bone chain's joint list.

Rotation is done in the local space which is constructed by the bone direction (in general parent to child) as the +Y axis and get_joint_limitation_right_axis_vector() as the +X axis.

If the +X and +Y axes are not orthogonal, the +X axis is implicitly modified to make it orthogonal.

Also, if the length of get_joint_limitation_right_axis_vector() is zero, the space is created by rotating the reference pose using the shortest arc that rotates the +Y axis of the reference pose to match the bone direction.

In here, the reference pose is the bone pose immediately before processing IK.

---

 **set_joint_rotation_axis**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), axis: [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis))

Sets the rotation axis at `joint` in the bone chain's joint list.

The axes are based on the reference pose's space, if `axis` is [SkeletonModifier3D.ROTATION_AXIS_CUSTOM](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-custom), you can specify any axis.

In here, the reference pose is the bone pose immediately before processing IK.

**Note:** The rotation axis and the forward vector shouldn't be colinear to avoid unintended rotation since [ChainIK3D](class_chainik3d.md#class-chainik3d) does not factor in twisting forces.

---

 **set_joint_rotation_axis_vector**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), axis_vector: [Vector3](class_vector3.md#class-vector3))

Sets the rotation axis vector for the specified joint in the bone chain.

This vector is normalized by an internal process and represents the axis around which the bone chain can rotate.

If the vector length is `0`, it is considered synonymous with [SkeletonModifier3D.ROTATION_AXIS_ALL](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-all).

---

 **set_target_node**(index: [int](class_int.md#class-int), target_node: [NodePath](class_nodepath.md#class-nodepath))

Sets the target node that the end bone is trying to reach.
