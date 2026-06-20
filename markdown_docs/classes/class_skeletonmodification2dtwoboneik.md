# SkeletonModification2DTwoBoneIK

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that rotates two bones using the law of cosines to reach the target.

## Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) uses an algorithm typically called TwoBoneIK. This algorithm works by leveraging the law of cosines and the lengths of the bones to figure out what rotation the bones currently have, and what rotation they need to make a complete triangle, where the first bone, the second bone, and the target form the three vertices of the triangle. Because the algorithm works by making a triangle, it can only operate on two bones.

TwoBoneIK is great for arms, legs, and really any joints that can be represented by just two bones that bend to reach a target. This solver is more lightweight than [SkeletonModification2DFABRIK](class_skeletonmodification2dfabrik.md#class-skeletonmodification2dfabrik), but gives similar, natural looking results.

## Properties

| [bool](class_bool.md#class-bool)             | flip_bend_direction         | `false`        |
|----------------------------------------------|----------------------------------------------------------------------------------------------------|----------------|
| [float](class_float.md#class-float)          | target_maximum_distance | `0.0`          |
| [float](class_float.md#class-float)          | target_minimum_distance | `0.0`          |
| [NodePath](class_nodepath.md#class-nodepath) | target_nodepath                 | `NodePath("")` |

## Methods

| [NodePath](class_nodepath.md#class-nodepath)   | get_joint_one_bone2d_node()                                                          |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                  | get_joint_one_bone_idx()                                                                |
| [NodePath](class_nodepath.md#class-nodepath)   | get_joint_two_bone2d_node()                                                          |
| [int](class_int.md#class-int)                  | get_joint_two_bone_idx()                                                                |
|                                                | set_joint_one_bone2d_node(bone2d_node: [NodePath](class_nodepath.md#class-nodepath)) |
|                                                | set_joint_one_bone_idx(bone_idx: [int](class_int.md#class-int))                         |
|                                                | set_joint_two_bone2d_node(bone2d_node: [NodePath](class_nodepath.md#class-nodepath)) |
|                                                | set_joint_two_bone_idx(bone_idx: [int](class_int.md#class-int))                         |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **flip_bend_direction** = `false`

-  **set_flip_bend_direction**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flip_bend_direction**()

If `true`, the bones in the modification will bend outward as opposed to inwards when contracting. If `false`, the bones will bend inwards when contracting.

---

[float](class_float.md#class-float) **target_maximum_distance** = `0.0`

-  **set_target_maximum_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_target_maximum_distance**()

The maximum distance the target can be at. If the target is farther than this distance, the modification will solve as if it's at this maximum distance. When set to `0`, the modification will solve without distance constraints.

---

[float](class_float.md#class-float) **target_minimum_distance** = `0.0`

-  **set_target_minimum_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_target_minimum_distance**()

The minimum distance the target can be at. If the target is closer than this distance, the modification will solve as if it's at this minimum distance. When set to `0`, the modification will solve without distance constraints.

---

[NodePath](class_nodepath.md#class-nodepath) **target_nodepath** = `NodePath("")`

-  **set_target_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target_node**()

The NodePath to the node that is the target for the TwoBoneIK modification. This node is what the modification will use when bending the [Bone2D](class_bone2d.md#class-bone2d) nodes.

---

## Method Descriptions

[NodePath](class_nodepath.md#class-nodepath) **get_joint_one_bone2d_node**()

Returns the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the first bone in the TwoBoneIK modification.

---

[int](class_int.md#class-int) **get_joint_one_bone_idx**()

Returns the index of the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the first bone in the TwoBoneIK modification.

---

[NodePath](class_nodepath.md#class-nodepath) **get_joint_two_bone2d_node**()

Returns the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the second bone in the TwoBoneIK modification.

---

[int](class_int.md#class-int) **get_joint_two_bone_idx**()

Returns the index of the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the second bone in the TwoBoneIK modification.

---

 **set_joint_one_bone2d_node**(bone2d_node: [NodePath](class_nodepath.md#class-nodepath))

Sets the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the first bone in the TwoBoneIK modification.

---

 **set_joint_one_bone_idx**(bone_idx: [int](class_int.md#class-int))

Sets the index of the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the first bone in the TwoBoneIK modification.

---

 **set_joint_two_bone2d_node**(bone2d_node: [NodePath](class_nodepath.md#class-nodepath))

Sets the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the second bone in the TwoBoneIK modification.

---

 **set_joint_two_bone_idx**(bone_idx: [int](class_int.md#class-int))

Sets the index of the [Bone2D](class_bone2d.md#class-bone2d) node that is being used as the second bone in the TwoBoneIK modification.
