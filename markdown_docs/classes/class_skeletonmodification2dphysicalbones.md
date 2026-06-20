# SkeletonModification2DPhysicalBones

**Experimental:** Physical bones may be changed in the future to perform the position update of [Bone2D](class_bone2d.md#class-bone2d) on their own, without needing this resource.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that applies the transforms of [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes to [Bone2D](class_bone2d.md#class-bone2d) nodes.

## Description

This modification takes the transforms of [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes and applies them to [Bone2D](class_bone2d.md#class-bone2d) nodes. This allows the [Bone2D](class_bone2d.md#class-bone2d) nodes to react to physics thanks to the linked [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes.

## Properties

| [int](class_int.md#class-int)   | physical_bone_chain_length   | `0`   |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|-------|

## Methods

|                                              | fetch_physical_bones()                                                                                                                |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NodePath](class_nodepath.md#class-nodepath) | get_physical_bone_node(joint_idx: [int](class_int.md#class-int))                                                                    |
|                                              | set_physical_bone_node(joint_idx: [int](class_int.md#class-int), physicalbone2d_node: [NodePath](class_nodepath.md#class-nodepath)) |
|                                              | start_simulation(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = [])                     |
|                                              | stop_simulation(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = [])                       |

---

## Property Descriptions

[int](class_int.md#class-int) **physical_bone_chain_length** = `0`

-  **set_physical_bone_chain_length**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_physical_bone_chain_length**()

The number of [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes linked in this modification.

---

## Method Descriptions

 **fetch_physical_bones**()

Empties the list of [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes and populates it with all [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes that are children of the [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

---

[NodePath](class_nodepath.md#class-nodepath) **get_physical_bone_node**(joint_idx: [int](class_int.md#class-int))

Returns the [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) node at `joint_idx`.

---

 **set_physical_bone_node**(joint_idx: [int](class_int.md#class-int), physicalbone2d_node: [NodePath](class_nodepath.md#class-nodepath))

Sets the [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) node at `joint_idx`.

**Note:** This is just the index used for this modification, not the bone index used in the [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

---

 **start_simulation**(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = [])

Tell the [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes to start simulating and interacting with the physics world.

Optionally, an array of bone names can be passed to this function, and that will cause only [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes with those names to start simulating.

---

 **stop_simulation**(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = [])

Tell the [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes to stop simulating and interacting with the physics world.

Optionally, an array of bone names can be passed to this function, and that will cause only [PhysicalBone2D](class_physicalbone2d.md#class-physicalbone2d) nodes with those names to stop simulating.
