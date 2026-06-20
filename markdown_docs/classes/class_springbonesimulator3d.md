# SpringBoneSimulator3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) to apply inertial wavering to bone chains.

## Description

This [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) can be used to wiggle hair, cloth, and tails. This modifier behaves differently from [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d) as it attempts to return the original pose after modification.

If you setup set_root_bone() and set_end_bone(), it is treated as one bone chain. Note that it does not support a branched chain like Y-shaped chains.

When a bone chain is created, an array is generated from the bones that exist in between and listed in the joint list.

Several properties can be applied to each joint, such as set_joint_stiffness(), set_joint_drag(), and set_joint_gravity().

For simplicity, you can set values to all joints at the same time by using a [Curve](class_curve.md#class-curve). If you want to specify detailed values individually, set set_individual_config() to `true`.

For physical simulation, **SpringBoneSimulator3D** can have children as self-standing collisions that are not related to [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d), see also [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d).

**Warning:** A scaled **SpringBoneSimulator3D** will likely not behave as expected. Make sure that the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) and its bones are not scaled.

**Note:** Most methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

## Properties

| [Vector3](class_vector3.md#class-vector3)   | external_force       | `Vector3(0, 0, 0)`   |
|---------------------------------------------|------------------------------------------------------------------------------|----------------------|
| [bool](class_bool.md#class-bool)            | mutable_bone_axes | `true`               |
| [int](class_int.md#class-int)               | setting_count         | `0`                  |

## Methods

| [bool](class_bool.md#class-bool)                                                   | are_all_child_collisions_enabled(index: [int](class_int.md#class-int))                                                                                                             |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                    | clear_collisions(index: [int](class_int.md#class-int))                                                                                                                                             |
|                                                                                    | clear_exclude_collisions(index: [int](class_int.md#class-int))                                                                                                                             |
|                                                                                    | clear_settings()                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                      | get_center_bone(index: [int](class_int.md#class-int))                                                                                                                                               |
| [String](class_string.md#class-string)                                             | get_center_bone_name(index: [int](class_int.md#class-int))                                                                                                                                     |
| CenterFrom                               | get_center_from(index: [int](class_int.md#class-int))                                                                                                                                               |
| [NodePath](class_nodepath.md#class-nodepath)                                       | get_center_node(index: [int](class_int.md#class-int))                                                                                                                                               |
| [int](class_int.md#class-int)                                                      | get_collision_count(index: [int](class_int.md#class-int))                                                                                                                                       |
| [NodePath](class_nodepath.md#class-nodepath)                                       | get_collision_path(index: [int](class_int.md#class-int), collision: [int](class_int.md#class-int))                                                                                               |
| [float](class_float.md#class-float)                                                | get_drag(index: [int](class_int.md#class-int))                                                                                                                                                             |
| [Curve](class_curve.md#class-curve)                                                | get_drag_damping_curve(index: [int](class_int.md#class-int))                                                                                                                                 |
| [int](class_int.md#class-int)                                                      | get_end_bone(index: [int](class_int.md#class-int))                                                                                                                                                     |
| [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection) | get_end_bone_direction(index: [int](class_int.md#class-int))                                                                                                                                 |
| [float](class_float.md#class-float)                                                | get_end_bone_length(index: [int](class_int.md#class-int))                                                                                                                                       |
| [String](class_string.md#class-string)                                             | get_end_bone_name(index: [int](class_int.md#class-int))                                                                                                                                           |
| [int](class_int.md#class-int)                                                      | get_exclude_collision_count(index: [int](class_int.md#class-int))                                                                                                                       |
| [NodePath](class_nodepath.md#class-nodepath)                                       | get_exclude_collision_path(index: [int](class_int.md#class-int), collision: [int](class_int.md#class-int))                                                                               |
| [float](class_float.md#class-float)                                                | get_gravity(index: [int](class_int.md#class-int))                                                                                                                                                       |
| [Curve](class_curve.md#class-curve)                                                | get_gravity_damping_curve(index: [int](class_int.md#class-int))                                                                                                                           |
| [Vector3](class_vector3.md#class-vector3)                                          | get_gravity_direction(index: [int](class_int.md#class-int))                                                                                                                                   |
| [int](class_int.md#class-int)                                                      | get_joint_bone(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                           |
| [String](class_string.md#class-string)                                             | get_joint_bone_name(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                 |
| [int](class_int.md#class-int)                                                      | get_joint_count(index: [int](class_int.md#class-int))                                                                                                                                               |
| [float](class_float.md#class-float)                                                | get_joint_drag(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                           |
| [float](class_float.md#class-float)                                                | get_joint_gravity(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                     |
| [Vector3](class_vector3.md#class-vector3)                                          | get_joint_gravity_direction(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                 |
| [float](class_float.md#class-float)                                                | get_joint_radius(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                       |
| [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis)   | get_joint_rotation_axis(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                         |
| [Vector3](class_vector3.md#class-vector3)                                          | get_joint_rotation_axis_vector(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                           |
| [float](class_float.md#class-float)                                                | get_joint_stiffness(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))                                                                                                 |
| [float](class_float.md#class-float)                                                | get_radius(index: [int](class_int.md#class-int))                                                                                                                                                         |
| [Curve](class_curve.md#class-curve)                                                | get_radius_damping_curve(index: [int](class_int.md#class-int))                                                                                                                             |
| [int](class_int.md#class-int)                                                      | get_root_bone(index: [int](class_int.md#class-int))                                                                                                                                                   |
| [String](class_string.md#class-string)                                             | get_root_bone_name(index: [int](class_int.md#class-int))                                                                                                                                         |
| [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis)   | get_rotation_axis(index: [int](class_int.md#class-int))                                                                                                                                           |
| [Vector3](class_vector3.md#class-vector3)                                          | get_rotation_axis_vector(index: [int](class_int.md#class-int))                                                                                                                             |
| [float](class_float.md#class-float)                                                | get_stiffness(index: [int](class_int.md#class-int))                                                                                                                                                   |
| [Curve](class_curve.md#class-curve)                                                | get_stiffness_damping_curve(index: [int](class_int.md#class-int))                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                   | is_config_individual(index: [int](class_int.md#class-int))                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                   | is_end_bone_extended(index: [int](class_int.md#class-int))                                                                                                                                     |
|                                                                                    | reset()                                                                                                                                                                                                       |
|                                                                                    | set_center_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                                          |
|                                                                                    | set_center_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                                                  |
|                                                                                    | set_center_from(index: [int](class_int.md#class-int), center_from: CenterFrom)                                                                            |
|                                                                                    | set_center_node(index: [int](class_int.md#class-int), node_path: [NodePath](class_nodepath.md#class-nodepath))                                                                                      |
|                                                                                    | set_collision_count(index: [int](class_int.md#class-int), count: [int](class_int.md#class-int))                                                                                                 |
|                                                                                    | set_collision_path(index: [int](class_int.md#class-int), collision: [int](class_int.md#class-int), node_path: [NodePath](class_nodepath.md#class-nodepath))                                      |
|                                                                                    | set_drag(index: [int](class_int.md#class-int), drag: [float](class_float.md#class-float))                                                                                                                  |
|                                                                                    | set_drag_damping_curve(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))                                                                                     |
|                                                                                    | set_enable_all_child_collisions(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                    |
|                                                                                    | set_end_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                                                |
|                                                                                    | set_end_bone_direction(index: [int](class_int.md#class-int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-bonedirection))                             |
|                                                                                    | set_end_bone_length(index: [int](class_int.md#class-int), length: [float](class_float.md#class-float))                                                                                          |
|                                                                                    | set_end_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                                                        |
|                                                                                    | set_exclude_collision_count(index: [int](class_int.md#class-int), count: [int](class_int.md#class-int))                                                                                 |
|                                                                                    | set_exclude_collision_path(index: [int](class_int.md#class-int), collision: [int](class_int.md#class-int), node_path: [NodePath](class_nodepath.md#class-nodepath))                      |
|                                                                                    | set_extend_end_bone(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                                            |
|                                                                                    | set_gravity(index: [int](class_int.md#class-int), gravity: [float](class_float.md#class-float))                                                                                                         |
|                                                                                    | set_gravity_damping_curve(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))                                                                               |
|                                                                                    | set_gravity_direction(index: [int](class_int.md#class-int), gravity_direction: [Vector3](class_vector3.md#class-vector3))                                                                     |
|                                                                                    | set_individual_config(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                                        |
|                                                                                    | set_joint_drag(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), drag: [float](class_float.md#class-float))                                                                |
|                                                                                    | set_joint_gravity(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), gravity: [float](class_float.md#class-float))                                                       |
|                                                                                    | set_joint_gravity_direction(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), gravity_direction: [Vector3](class_vector3.md#class-vector3))                   |
|                                                                                    | set_joint_radius(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), radius: [float](class_float.md#class-float))                                                          |
|                                                                                    | set_joint_rotation_axis(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), axis: [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis)) |
|                                                                                    | set_joint_rotation_axis_vector(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3))                        |
|                                                                                    | set_joint_stiffness(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), stiffness: [float](class_float.md#class-float))                                                 |
|                                                                                    | set_radius(index: [int](class_int.md#class-int), radius: [float](class_float.md#class-float))                                                                                                            |
|                                                                                    | set_radius_damping_curve(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))                                                                                 |
|                                                                                    | set_root_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                                                                                              |
|                                                                                    | set_root_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))                                                                                      |
|                                                                                    | set_rotation_axis(index: [int](class_int.md#class-int), axis: [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis))                                                   |
|                                                                                    | set_rotation_axis_vector(index: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3))                                                                          |
|                                                                                    | set_stiffness(index: [int](class_int.md#class-int), stiffness: [float](class_float.md#class-float))                                                                                                   |
|                                                                                    | set_stiffness_damping_curve(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))                                                                           |

---

## Enumerations

enum **CenterFrom**:

CenterFrom **CENTER_FROM_WORLD_ORIGIN** = `0`

The world origin is defined as center.

CenterFrom **CENTER_FROM_NODE** = `1`

The [Node3D](class_node3d.md#class-node3d) specified by set_center_node() is defined as center.

If [Node3D](class_node3d.md#class-node3d) is not found, the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) is treated as center.

CenterFrom **CENTER_FROM_BONE** = `2`

The bone pose origin of the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) specified by set_center_bone() is defined as center.

If [Node3D](class_node3d.md#class-node3d) is not found, the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) is treated as center.

---

## Property Descriptions

[Vector3](class_vector3.md#class-vector3) **external_force** = `Vector3(0, 0, 0)`

-  **set_external_force**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_external_force**()

The constant force that always affected bones. It is equal to the result when the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) moves at this speed in the opposite direction.

This is useful for effects such as wind and anti-gravity.

---

[bool](class_bool.md#class-bool) **mutable_bone_axes** = `true`

-  **set_mutable_bone_axes**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_bone_axes_mutable**()

If `true`, the solver retrieves the bone axis from the bone pose every frame.

If `false`, the solver retrieves the bone axis from the bone rest and caches it, which increases performance slightly, but position changes in the bone pose made before processing this **SpringBoneSimulator3D** are ignored.

---

[int](class_int.md#class-int) **setting_count** = `0`

-  **set_setting_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_setting_count**()

The number of settings.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **are_all_child_collisions_enabled**(index: [int](class_int.md#class-int))

Returns `true` if all child [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d)s are contained in the collision list at `index` in the settings.

---

 **clear_collisions**(index: [int](class_int.md#class-int))

Clears all collisions from the collision list at `index` in the settings when are_all_child_collisions_enabled() is `false`.

---

 **clear_exclude_collisions**(index: [int](class_int.md#class-int))

Clears all exclude collisions from the collision list at `index` in the settings when are_all_child_collisions_enabled() is `true`.

---

 **clear_settings**()

Clears all settings.

---

[int](class_int.md#class-int) **get_center_bone**(index: [int](class_int.md#class-int))

Returns the center bone index of the bone chain.

---

[String](class_string.md#class-string) **get_center_bone_name**(index: [int](class_int.md#class-int))

Returns the center bone name of the bone chain.

---

CenterFrom **get_center_from**(index: [int](class_int.md#class-int))

Returns what the center originates from in the bone chain.

---

[NodePath](class_nodepath.md#class-nodepath) **get_center_node**(index: [int](class_int.md#class-int))

Returns the center node path of the bone chain.

---

[int](class_int.md#class-int) **get_collision_count**(index: [int](class_int.md#class-int))

Returns the collision count of the bone chain's collision list when are_all_child_collisions_enabled() is `false`.

---

[NodePath](class_nodepath.md#class-nodepath) **get_collision_path**(index: [int](class_int.md#class-int), collision: [int](class_int.md#class-int))

Returns the node path of the [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d) at `collision` in the bone chain's collision list when are_all_child_collisions_enabled() is `false`.

---

[float](class_float.md#class-float) **get_drag**(index: [int](class_int.md#class-int))

Returns the drag force damping curve of the bone chain.

---

[Curve](class_curve.md#class-curve) **get_drag_damping_curve**(index: [int](class_int.md#class-int))

Returns the drag force damping curve of the bone chain.

---

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

[int](class_int.md#class-int) **get_exclude_collision_count**(index: [int](class_int.md#class-int))

Returns the exclude collision count of the bone chain's exclude collision list when are_all_child_collisions_enabled() is `true`.

---

[NodePath](class_nodepath.md#class-nodepath) **get_exclude_collision_path**(index: [int](class_int.md#class-int), collision: [int](class_int.md#class-int))

Returns the node path of the [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d) at `collision` in the bone chain's exclude collision list when are_all_child_collisions_enabled() is `true`.

---

[float](class_float.md#class-float) **get_gravity**(index: [int](class_int.md#class-int))

Returns the gravity amount of the bone chain.

---

[Curve](class_curve.md#class-curve) **get_gravity_damping_curve**(index: [int](class_int.md#class-int))

Returns the gravity amount damping curve of the bone chain.

---

[Vector3](class_vector3.md#class-vector3) **get_gravity_direction**(index: [int](class_int.md#class-int))

Returns the gravity direction of the bone chain.

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

[float](class_float.md#class-float) **get_joint_drag**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the drag force at `joint` in the bone chain's joint list.

---

[float](class_float.md#class-float) **get_joint_gravity**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the gravity amount at `joint` in the bone chain's joint list.

---

[Vector3](class_vector3.md#class-vector3) **get_joint_gravity_direction**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the gravity direction at `joint` in the bone chain's joint list.

---

[float](class_float.md#class-float) **get_joint_radius**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the radius at `joint` in the bone chain's joint list.

---

[RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis) **get_joint_rotation_axis**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the rotation axis at `joint` in the bone chain's joint list.

---

[Vector3](class_vector3.md#class-vector3) **get_joint_rotation_axis_vector**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the rotation axis vector for the specified joint in the bone chain. This vector represents the axis around which the joint can rotate. It is determined based on the rotation axis set for the joint.

If get_joint_rotation_axis() is [SkeletonModifier3D.ROTATION_AXIS_ALL](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-all), this method returns `Vector3(0, 0, 0)`.

---

[float](class_float.md#class-float) **get_joint_stiffness**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int))

Returns the stiffness force at `joint` in the bone chain's joint list.

---

[float](class_float.md#class-float) **get_radius**(index: [int](class_int.md#class-int))

Returns the joint radius of the bone chain.

---

[Curve](class_curve.md#class-curve) **get_radius_damping_curve**(index: [int](class_int.md#class-int))

Returns the joint radius damping curve of the bone chain.

---

[int](class_int.md#class-int) **get_root_bone**(index: [int](class_int.md#class-int))

Returns the root bone index of the bone chain.

---

[String](class_string.md#class-string) **get_root_bone_name**(index: [int](class_int.md#class-int))

Returns the root bone name of the bone chain.

---

[RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis) **get_rotation_axis**(index: [int](class_int.md#class-int))

Returns the rotation axis of the bone chain.

---

[Vector3](class_vector3.md#class-vector3) **get_rotation_axis_vector**(index: [int](class_int.md#class-int))

Returns the rotation axis vector of the bone chain. This vector represents the axis around which the bone chain can rotate. It is determined based on the rotation axis set for the bone chain.

If get_rotation_axis() is [SkeletonModifier3D.ROTATION_AXIS_ALL](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-all), this method returns `Vector3(0, 0, 0)`.

---

[float](class_float.md#class-float) **get_stiffness**(index: [int](class_int.md#class-int))

Returns the stiffness force of the bone chain.

---

[Curve](class_curve.md#class-curve) **get_stiffness_damping_curve**(index: [int](class_int.md#class-int))

Returns the stiffness force damping curve of the bone chain.

---

[bool](class_bool.md#class-bool) **is_config_individual**(index: [int](class_int.md#class-int))

Returns `true` if the config can be edited individually for each joint.

---

[bool](class_bool.md#class-bool) **is_end_bone_extended**(index: [int](class_int.md#class-int))

Returns `true` if the end bone is extended to have a tail.

---

 **reset**()

Resets a simulating state with respect to the current bone pose.

It is useful to prevent the simulation result getting violent. For example, calling this immediately after a call to [AnimationPlayer.play()](class_animationplayer.md#class-animationplayer-method-play) without a fading, or within the previous [SkeletonModifier3D.modification_processed](class_skeletonmodifier3d.md#class-skeletonmodifier3d-signal-modification-processed) signal if it's condition changes significantly.

---

 **set_center_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the center bone index of the bone chain.

---

 **set_center_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the center bone name of the bone chain.

---

 **set_center_from**(index: [int](class_int.md#class-int), center_from: CenterFrom)

Sets what the center originates from in the bone chain.

Bone movement is calculated based on the difference in relative distance between center and bone in the previous and next frames.

For example, if the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) is used as the center, the bones are considered to have not moved if the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) moves in the world.

In this case, only a change in the bone pose is considered to be a bone movement.

---

 **set_center_node**(index: [int](class_int.md#class-int), node_path: [NodePath](class_nodepath.md#class-nodepath))

Sets the center node path of the bone chain.

---

 **set_collision_count**(index: [int](class_int.md#class-int), count: [int](class_int.md#class-int))

Sets the number of collisions in the collision list at `index` in the settings when are_all_child_collisions_enabled() is `false`.

---

 **set_collision_path**(index: [int](class_int.md#class-int), collision: [int](class_int.md#class-int), node_path: [NodePath](class_nodepath.md#class-nodepath))

Sets the node path of the [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d) at `collision` in the bone chain's collision list when are_all_child_collisions_enabled() is `false`.

---

 **set_drag**(index: [int](class_int.md#class-int), drag: [float](class_float.md#class-float))

Sets the drag force of the bone chain. The greater the value, the more suppressed the wiggling.

The value is scaled by set_drag_damping_curve() and cached in each joint setting in the joint list.

---

 **set_drag_damping_curve**(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))

Sets the drag force damping curve of the bone chain.

---

 **set_enable_all_child_collisions**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, all child [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d)s are colliding and set_exclude_collision_path() is enabled as an exclusion list at `index` in the settings.

If `enabled` is `false`, you need to manually register all valid collisions with set_collision_path().

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

**Note:** End bone must be the root bone or a child of the root bone. If they are the same, the tail must be extended by set_extend_end_bone() to jiggle the bone.

---

 **set_exclude_collision_count**(index: [int](class_int.md#class-int), count: [int](class_int.md#class-int))

Sets the number of exclude collisions in the exclude collision list at `index` in the settings when are_all_child_collisions_enabled() is `true`.

---

 **set_exclude_collision_path**(index: [int](class_int.md#class-int), collision: [int](class_int.md#class-int), node_path: [NodePath](class_nodepath.md#class-nodepath))

Sets the node path of the [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d) at `collision` in the bone chain's exclude collision list when are_all_child_collisions_enabled() is `true`.

---

 **set_extend_end_bone**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the end bone is extended to have a tail.

The extended tail config is allocated to the last element in the joint list. In other words, if you set `enabled` to `false`, the config of the last element in the joint list has no effect in the simulated result.

---

 **set_gravity**(index: [int](class_int.md#class-int), gravity: [float](class_float.md#class-float))

Sets the gravity amount of the bone chain. This value is not an acceleration, but a constant velocity of movement in set_gravity_direction().

If `gravity` is not `0`, the modified pose will not return to the original pose since it is always affected by gravity.

The value is scaled by set_gravity_damping_curve() and cached in each joint setting in the joint list.

---

 **set_gravity_damping_curve**(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))

Sets the gravity amount damping curve of the bone chain.

---

 **set_gravity_direction**(index: [int](class_int.md#class-int), gravity_direction: [Vector3](class_vector3.md#class-vector3))

Sets the gravity direction of the bone chain. This value is internally normalized and then multiplied by set_gravity().

The value is cached in each joint setting in the joint list.

---

 **set_individual_config**(index: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the config can be edited individually for each joint.

---

 **set_joint_drag**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), drag: [float](class_float.md#class-float))

Sets the drag force at `joint` in the bone chain's joint list when is_config_individual() is `true`.

---

 **set_joint_gravity**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), gravity: [float](class_float.md#class-float))

Sets the gravity amount at `joint` in the bone chain's joint list when is_config_individual() is `true`.

---

 **set_joint_gravity_direction**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), gravity_direction: [Vector3](class_vector3.md#class-vector3))

Sets the gravity direction at `joint` in the bone chain's joint list when is_config_individual() is `true`.

---

 **set_joint_radius**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), radius: [float](class_float.md#class-float))

Sets the joint radius at `joint` in the bone chain's joint list when is_config_individual() is `true`.

---

 **set_joint_rotation_axis**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), axis: [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis))

Sets the rotation axis at `joint` in the bone chain's joint list when is_config_individual() is `true`.

The axes are based on the reference pose's space, if `axis` is [SkeletonModifier3D.ROTATION_AXIS_CUSTOM](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-custom), you can specify any axis.

In here, the reference pose is the bone pose immediately before the simulation.

**Note:** The rotation axis and the forward vector shouldn't be colinear to avoid unintended rotation since **SpringBoneSimulator3D** does not factor in twisting forces.

---

 **set_joint_rotation_axis_vector**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3))

Sets the rotation axis vector for the specified joint in the bone chain.

This vector is normalized by an internal process and represents the axis around which the bone chain can rotate.

If the vector length is `0`, it is considered synonymous with [SkeletonModifier3D.ROTATION_AXIS_ALL](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-all).

---

 **set_joint_stiffness**(index: [int](class_int.md#class-int), joint: [int](class_int.md#class-int), stiffness: [float](class_float.md#class-float))

Sets the stiffness force at `joint` in the bone chain's joint list when is_config_individual() is `true`.

---

 **set_radius**(index: [int](class_int.md#class-int), radius: [float](class_float.md#class-float))

Sets the joint radius of the bone chain. It is used to move and slide with the [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d) in the collision list.

The value is scaled by set_radius_damping_curve() and cached in each joint setting in the joint list.

---

 **set_radius_damping_curve**(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))

Sets the joint radius damping curve of the bone chain.

---

 **set_root_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the root bone index of the bone chain.

---

 **set_root_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the root bone name of the bone chain.

---

 **set_rotation_axis**(index: [int](class_int.md#class-int), axis: [RotationAxis](class_skeletonmodifier3d.md#enum-skeletonmodifier3d-rotationaxis))

Sets the rotation axis of the bone chain. If set to a specific axis, it acts like a hinge joint. The value is cached in each joint setting in the joint list.

The axes are based on the reference pose's space, if `axis` is [SkeletonModifier3D.ROTATION_AXIS_CUSTOM](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-custom), you can specify any axis.

In here, the reference pose is the bone pose immediately before the simulation.

**Note:** The rotation axis vector and the forward vector shouldn't be colinear to avoid unintended rotation since **SpringBoneSimulator3D** does not factor in twisting forces.

---

 **set_rotation_axis_vector**(index: [int](class_int.md#class-int), vector: [Vector3](class_vector3.md#class-vector3))

Sets the rotation axis vector of the bone chain. The value is cached in each joint setting in the joint list.

This vector is normalized by an internal process and represents the axis around which the bone chain can rotate.

If the vector length is `0`, it is considered synonymous with [SkeletonModifier3D.ROTATION_AXIS_ALL](class_skeletonmodifier3d.md#class-skeletonmodifier3d-constant-rotation-axis-all).

---

 **set_stiffness**(index: [int](class_int.md#class-int), stiffness: [float](class_float.md#class-float))

Sets the stiffness force of the bone chain. The greater the value, the faster it recovers to its initial pose.

If `stiffness` is `0`, the modified pose will not return to the original pose.

The value is scaled by set_stiffness_damping_curve() and cached in each joint setting in the joint list.

---

 **set_stiffness_damping_curve**(index: [int](class_int.md#class-int), curve: [Curve](class_curve.md#class-curve))

Sets the stiffness force damping curve of the bone chain.
