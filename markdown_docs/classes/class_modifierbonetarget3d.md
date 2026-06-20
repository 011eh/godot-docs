# ModifierBoneTarget3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

А node that dynamically copies the 3D transform of a bone in its parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

## Description

This node selects a bone in a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) and attaches to it. This means that the **ModifierBoneTarget3D** node will dynamically copy the 3D transform of the selected bone.

The functionality is similar to [BoneAttachment3D](class_boneattachment3d.md#class-boneattachment3d), but this node adopts the [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) cycle and is intended to be used as another [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d)'s target.

## Properties

| [int](class_int.md#class-int)          | bone           | `-1`   |
|----------------------------------------|-------------------------------------------------------------|--------|
| [String](class_string.md#class-string) | bone_name | `""`   |

---

## Property Descriptions

[int](class_int.md#class-int) **bone** = `-1`

-  **set_bone**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone**()

The index of the attached bone.

---

[String](class_string.md#class-string) **bone_name** = `""`

-  **set_bone_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_bone_name**()

The name of the attached bone.
