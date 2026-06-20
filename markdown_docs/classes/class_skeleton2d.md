# Skeleton2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

The parent of a hierarchy of [Bone2D](class_bone2d.md#class-bone2d)s, used to create a 2D skeletal animation.

## Description

**Skeleton2D** parents a hierarchy of [Bone2D](class_bone2d.md#class-bone2d) nodes. It holds a reference to each [Bone2D](class_bone2d.md#class-bone2d)'s rest pose and acts as a single point of access to its bones.

To set up different types of inverse kinematics for the given Skeleton2D, a [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) should be created. The inverse kinematics be applied by increasing [SkeletonModificationStack2D.modification_count](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-property-modification-count) and creating the desired number of modifications.

## Tutorials

- [2D skeletons](../tutorials/animation/2d_skeletons.md)

## Methods

|                                                                                                       | execute_modifications(delta: [float](class_float.md#class-float), execution_mode: [int](class_int.md#class-int))                                                                                                                                |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bone2D](class_bone2d.md#class-bone2d)                                                                | get_bone(idx: [int](class_int.md#class-int))                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                                         | get_bone_count()                                                                                                                                                                                                                                       |
| [Transform2D](class_transform2d.md#class-transform2d)                                                 | get_bone_local_pose_override(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                    |
| [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) | get_modification_stack()                                                                                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                                                         | get_skeleton()                                                                                                                                                                                                                                           |
|                                                                                                       | set_bone_local_pose_override(bone_idx: [int](class_int.md#class-int), override_pose: [Transform2D](class_transform2d.md#class-transform2d), strength: [float](class_float.md#class-float), persistent: [bool](class_bool.md#class-bool)) |
|                                                                                                       | set_modification_stack(modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d))                                                                                              |

---

## Signals

**bone_setup_changed**()

Emitted when the [Bone2D](class_bone2d.md#class-bone2d) setup attached to this skeletons changes. This is primarily used internally within the skeleton.

---

## Method Descriptions

 **execute_modifications**(delta: [float](class_float.md#class-float), execution_mode: [int](class_int.md#class-int))

Executes all the modifications on the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d), if the Skeleton2D has one assigned.

---

[Bone2D](class_bone2d.md#class-bone2d) **get_bone**(idx: [int](class_int.md#class-int))

Returns a [Bone2D](class_bone2d.md#class-bone2d) from the node hierarchy parented by Skeleton2D. The object to return is identified by the parameter `idx`. Bones are indexed by descending the node hierarchy from top to bottom, adding the children of each branch before moving to the next sibling.

---

[int](class_int.md#class-int) **get_bone_count**()

Returns the number of [Bone2D](class_bone2d.md#class-bone2d) nodes in the node hierarchy parented by Skeleton2D.

---

[Transform2D](class_transform2d.md#class-transform2d) **get_bone_local_pose_override**(bone_idx: [int](class_int.md#class-int))

Returns the local pose override transform for `bone_idx`.

---

[SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) **get_modification_stack**()

Returns the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) attached to this skeleton, if one exists.

---

[RID](class_rid.md#class-rid) **get_skeleton**()

Returns the [RID](class_rid.md#class-rid) of a Skeleton2D instance.

---

 **set_bone_local_pose_override**(bone_idx: [int](class_int.md#class-int), override_pose: [Transform2D](class_transform2d.md#class-transform2d), strength: [float](class_float.md#class-float), persistent: [bool](class_bool.md#class-bool))

Sets the local pose transform, `override_pose`, for the bone at `bone_idx`.

`strength` is the interpolation strength that will be used when applying the pose, and `persistent` determines if the applied pose will remain.

**Note:** The pose transform needs to be a local transform relative to the [Bone2D](class_bone2d.md#class-bone2d) node at `bone_idx`!

---

 **set_modification_stack**(modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d))

Sets the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) attached to this skeleton.
