# SkeletonIK3D

**Deprecated:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node used to rotate all bones of a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) bone chain a way that places the end bone at a desired 3D position.

## Description

SkeletonIK3D is used to rotate all bones of a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) bone chain a way that places the end bone at a desired 3D position. A typical scenario for IK in games is to place a character's feet on the ground or a character's hands on a currently held object. SkeletonIK uses FabrikInverseKinematic internally to solve the bone chain and applies the results to the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) `bones_global_pose_override` property for all affected bones in the chain. If fully applied, this overwrites any bone transform from [Animation](class_animation.md#class-animation)s or bone custom poses set by users. The applied amount can be controlled with the [SkeletonModifier3D.influence](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-influence) property.

```gdscript
# Apply IK effect automatically on every new frame (not the current)
skeleton_ik_node.start()

# Apply IK effect only on the current frame
skeleton_ik_node.start(true)

# Stop IK effect and reset bones_global_pose_override on Skeleton
skeleton_ik_node.stop()

# Apply full IK effect
skeleton_ik_node.set_influence(1.0)

# Apply half IK effect
skeleton_ik_node.set_influence(0.5)

# Apply zero IK effect (a value at or below 0.01 also removes bones_global_pose_override on Skeleton)
skeleton_ik_node.set_influence(0.0)
```

## Properties

| [float](class_float.md#class-float)                   | interpolation           |                                                   |
|-------------------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------|
| [Vector3](class_vector3.md#class-vector3)             | magnet                         | `Vector3(0, 0, 0)`                                |
| [int](class_int.md#class-int)                         | max_iterations         | `10`                                              |
| [float](class_float.md#class-float)                   | min_distance             | `0.01`                                            |
| [bool](class_bool.md#class-bool)                      | override_tip_basis | `true`                                            |
| [StringName](class_stringname.md#class-stringname)    | root_bone                   | `&""`                                             |
| [Transform3D](class_transform3d.md#class-transform3d) | target                         | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| [NodePath](class_nodepath.md#class-nodepath)          | target_node               | `NodePath("")`                                    |
| [StringName](class_stringname.md#class-stringname)    | tip_bone                     | `&""`                                             |
| [bool](class_bool.md#class-bool)                      | use_magnet                 | `false`                                           |

## Methods

| [Skeleton3D](class_skeleton3d.md#class-skeleton3d)   | get_parent_skeleton()                       |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                     | is_running()                                         |
|                                                      | start(one_time: [bool](class_bool.md#class-bool) = false) |
|                                                      | stop()                                                     |

---

## Property Descriptions

[float](class_float.md#class-float) **interpolation**

-  **set_interpolation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_interpolation**()

**Deprecated:** Use [SkeletonModifier3D.influence](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-influence) instead.

Interpolation value for how much the IK results are applied to the current skeleton bone chain. A value of `1.0` will overwrite all skeleton bone transforms completely while a value of `0.0` will visually disable the SkeletonIK.

---

[Vector3](class_vector3.md#class-vector3) **magnet** = `Vector3(0, 0, 0)`

-  **set_magnet_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_magnet_position**()

Secondary target position (first is target property or target_node) for the IK chain. Use magnet position (pole target) to control the bending of the IK chain. Only works if the bone chain has more than 2 bones. The middle chain bone position will be linearly interpolated with the magnet position.

---

[int](class_int.md#class-int) **max_iterations** = `10`

-  **set_max_iterations**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_iterations**()

Number of iteration loops used by the IK solver to produce more accurate (and elegant) bone chain results.

---

[float](class_float.md#class-float) **min_distance** = `0.01`

-  **set_min_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_distance**()

The minimum distance between bone and goal target. If the distance is below this value, the IK solver stops further iterations.

---

[bool](class_bool.md#class-bool) **override_tip_basis** = `true`

-  **set_override_tip_basis**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_override_tip_basis**()

If `true` overwrites the rotation of the tip bone with the rotation of the target (or target_node if defined).

---

[StringName](class_stringname.md#class-stringname) **root_bone** = `&""`

-  **set_root_bone**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_root_bone**()

The name of the current root bone, the first bone in the IK chain.

---

[Transform3D](class_transform3d.md#class-transform3d) **target** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

-  **set_target_transform**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_target_transform**()

First target of the IK chain where the tip bone is placed and, if override_tip_basis is `true`, how the tip bone is rotated. If a target_node path is available the nodes transform is used instead and this property is ignored.

---

[NodePath](class_nodepath.md#class-nodepath) **target_node** = `NodePath("")`

-  **set_target_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target_node**()

Target node [NodePath](class_nodepath.md#class-nodepath) for the IK chain. If available, the node's current [Transform3D](class_transform3d.md#class-transform3d) is used instead of the target property.

---

[StringName](class_stringname.md#class-stringname) **tip_bone** = `&""`

-  **set_tip_bone**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_tip_bone**()

The name of the current tip bone, the last bone in the IK chain placed at the target transform (or target_node if defined).

---

[bool](class_bool.md#class-bool) **use_magnet** = `false`

-  **set_use_magnet**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_magnet**()

If `true`, instructs the IK solver to consider the secondary magnet target (pole target) when calculating the bone chain. Use the magnet position (pole target) to control the bending of the IK chain.

---

## Method Descriptions

[Skeleton3D](class_skeleton3d.md#class-skeleton3d) **get_parent_skeleton**()

Returns the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node that was present when SkeletonIK entered the scene tree. Returns `null` if the parent node was not a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node when SkeletonIK3D entered the scene tree.

---

[bool](class_bool.md#class-bool) **is_running**()

Returns `true` if SkeletonIK is applying IK effects on continues frames to the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) bones. Returns `false` if SkeletonIK is stopped or start() was used with the `one_time` parameter set to `true`.

---

 **start**(one_time: [bool](class_bool.md#class-bool) = false)

Starts applying IK effects on each frame to the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) bones but will only take effect starting on the next frame. If `one_time` is `true`, this will take effect immediately but also reset on the next frame.

---

 **stop**()

Stops applying IK effects on each frame to the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) bones and also calls [Skeleton3D.clear_bones_global_pose_override()](class_skeleton3d.md#class-skeleton3d-method-clear-bones-global-pose-override) to remove existing overrides on all bones.
