# SkeletonModification2DLookAt

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that rotates a [Bone2D](class_bone2d.md#class-bone2d) node to look at a target.

## Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) rotates a bone to look a target. This is extremely helpful for moving character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

## Properties

| [NodePath](class_nodepath.md#class-nodepath)   | bone2d_node         | `NodePath("")`   |
|------------------------------------------------|---------------------------------------------------------------------------------|------------------|
| [int](class_int.md#class-int)                  | bone_index           | `-1`             |
| [NodePath](class_nodepath.md#class-nodepath)   | target_nodepath | `NodePath("")`   |

## Methods

| [float](class_float.md#class-float)   | get_additional_rotation()                                                 |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)      | get_constraint_angle_invert()                                         |
| [float](class_float.md#class-float)   | get_constraint_angle_max()                                               |
| [float](class_float.md#class-float)   | get_constraint_angle_min()                                               |
| [bool](class_bool.md#class-bool)      | get_enable_constraint()                                                     |
|                                       | set_additional_rotation(rotation: [float](class_float.md#class-float))    |
|                                       | set_constraint_angle_invert(invert: [bool](class_bool.md#class-bool)) |
|                                       | set_constraint_angle_max(angle_max: [float](class_float.md#class-float)) |
|                                       | set_constraint_angle_min(angle_min: [float](class_float.md#class-float)) |
|                                       | set_enable_constraint(enable_constraint: [bool](class_bool.md#class-bool))  |

---

## Property Descriptions

[NodePath](class_nodepath.md#class-nodepath) **bone2d_node** = `NodePath("")`

-  **set_bone2d_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_bone2d_node**()

The [Bone2D](class_bone2d.md#class-bone2d) node that the modification will operate on.

---

[int](class_int.md#class-int) **bone_index** = `-1`

-  **set_bone_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone_index**()

The index of the [Bone2D](class_bone2d.md#class-bone2d) node that the modification will operate on.

---

[NodePath](class_nodepath.md#class-nodepath) **target_nodepath** = `NodePath("")`

-  **set_target_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target_node**()

The NodePath to the node that is the target for the LookAt modification. This node is what the modification will rotate the [Bone2D](class_bone2d.md#class-bone2d) to.

---

## Method Descriptions

[float](class_float.md#class-float) **get_additional_rotation**()

Returns the amount of additional rotation that is applied after the LookAt modification executes.

---

[bool](class_bool.md#class-bool) **get_constraint_angle_invert**()

Returns whether the constraints to this modification are inverted or not.

---

[float](class_float.md#class-float) **get_constraint_angle_max**()

Returns the constraint's maximum allowed angle.

---

[float](class_float.md#class-float) **get_constraint_angle_min**()

Returns the constraint's minimum allowed angle.

---

[bool](class_bool.md#class-bool) **get_enable_constraint**()

Returns `true` if the LookAt modification is using constraints.

---

 **set_additional_rotation**(rotation: [float](class_float.md#class-float))

Sets the amount of additional rotation that is to be applied after executing the modification. This allows for offsetting the results by the inputted rotation amount.

---

 **set_constraint_angle_invert**(invert: [bool](class_bool.md#class-bool))

When `true`, the modification will use an inverted joint constraint.

An inverted joint constraint only constraints the [Bone2D](class_bone2d.md#class-bone2d) to the angles *outside of* the inputted minimum and maximum angles. For this reason, it is referred to as an inverted joint constraint, as it constraints the joint to the outside of the inputted values.

---

 **set_constraint_angle_max**(angle_max: [float](class_float.md#class-float))

Sets the constraint's maximum allowed angle.

---

 **set_constraint_angle_min**(angle_min: [float](class_float.md#class-float))

Sets the constraint's minimum allowed angle.

---

 **set_enable_constraint**(enable_constraint: [bool](class_bool.md#class-bool))

Sets whether this modification will use constraints or not. When `true`, constraints will be applied when solving the LookAt modification.
