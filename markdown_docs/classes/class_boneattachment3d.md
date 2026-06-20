# BoneAttachment3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

А node that dynamically copies or overrides the 3D transform of a bone in its parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

## Description

This node selects a bone in a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) and attaches to it. This means that the **BoneAttachment3D** node will either dynamically copy or override the 3D transform of the selected bone.

## Properties

| [int](class_int.md#class-int)                                                | bone_idx                           | `-1`                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                                       | bone_name                         | `""`                                                                                 |
| [NodePath](class_nodepath.md#class-nodepath)                                 | external_skeleton         |                                                                                      |
| [bool](class_bool.md#class-bool)                                             | override_pose                 | `false`                                                                              |
| [PhysicsInterpolationMode](class_node.md#enum-node-physicsinterpolationmode) | physics_interpolation_mode                                                      | `2` (overrides [Node](class_node.md#class-node-property-physics-interpolation-mode)) |
| [bool](class_bool.md#class-bool)                                             | use_external_skeleton | `false`                                                                              |

## Methods

| [Skeleton3D](class_skeleton3d.md#class-skeleton3d)   | get_skeleton()             |
|------------------------------------------------------|---------------------------------------------------------------------------|
|                                                      | on_skeleton_update() |

---

## Property Descriptions

[int](class_int.md#class-int) **bone_idx** = `-1`

-  **set_bone_idx**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone_idx**()

The index of the attached bone.

---

[String](class_string.md#class-string) **bone_name** = `""`

-  **set_bone_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_bone_name**()

The name of the attached bone.

---

[NodePath](class_nodepath.md#class-nodepath) **external_skeleton**

-  **set_external_skeleton**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_external_skeleton**()

The [NodePath](class_nodepath.md#class-nodepath) to the external [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node.

---

[bool](class_bool.md#class-bool) **override_pose** = `false`

-  **set_override_pose**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_override_pose**()

Whether the **BoneAttachment3D** node will override the bone pose of the bone it is attached to. When set to `true`, the **BoneAttachment3D** node can change the pose of the bone. When set to `false`, the **BoneAttachment3D** will always be set to the bone's transform.

**Note:** This override performs interruptively in the skeleton update process using signals due to the old design. It may cause unintended behavior when used at the same time with [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d).

---

[bool](class_bool.md#class-bool) **use_external_skeleton** = `false`

-  **set_use_external_skeleton**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_external_skeleton**()

Whether the **BoneAttachment3D** node will use an external [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node rather than attempting to use its parent node as the [Skeleton3D](class_skeleton3d.md#class-skeleton3d). When set to `true`, the **BoneAttachment3D** node will use the external [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node set in external_skeleton.

---

## Method Descriptions

[Skeleton3D](class_skeleton3d.md#class-skeleton3d) **get_skeleton**()

Returns the parent or external [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node if it exists, otherwise returns `null`.

---

 **on_skeleton_update**()

A function that is called automatically when the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) is updated. This function is where the **BoneAttachment3D** node updates its position so it is correctly bound when it is *not* set to override the bone pose.
