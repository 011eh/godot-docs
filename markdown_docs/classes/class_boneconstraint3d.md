# BoneConstraint3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [AimModifier3D](class_aimmodifier3d.md#class-aimmodifier3d), [ConvertTransformModifier3D](class_converttransformmodifier3d.md#class-converttransformmodifier3d), [CopyTransformModifier3D](class_copytransformmodifier3d.md#class-copytransformmodifier3d)

A node that may modify Skeleton3D's bone with associating the two bones.

## Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) that modifies the bone set in set_apply_bone() based on the transform of the bone retrieved by get_reference_bone().

**Note:** Most methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/amount`).

## Methods

|                                                       | clear_setting()                                                                                                            |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float)                   | get_amount(index: [int](class_int.md#class-int))                                                                              |
| [int](class_int.md#class-int)                         | get_apply_bone(index: [int](class_int.md#class-int))                                                                      |
| [String](class_string.md#class-string)                | get_apply_bone_name(index: [int](class_int.md#class-int))                                                            |
| [int](class_int.md#class-int)                         | get_reference_bone(index: [int](class_int.md#class-int))                                                              |
| [String](class_string.md#class-string)                | get_reference_bone_name(index: [int](class_int.md#class-int))                                                    |
| [NodePath](class_nodepath.md#class-nodepath)          | get_reference_node(index: [int](class_int.md#class-int))                                                              |
| ReferenceType | get_reference_type(index: [int](class_int.md#class-int))                                                              |
| [int](class_int.md#class-int)                         | get_setting_count()                                                                                                    |
|                                                       | set_amount(index: [int](class_int.md#class-int), amount: [float](class_float.md#class-float))                                 |
|                                                       | set_apply_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                                 |
|                                                       | set_apply_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))         |
|                                                       | set_reference_bone(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))                         |
|                                                       | set_reference_bone_name(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string)) |
|                                                       | set_reference_node(index: [int](class_int.md#class-int), node: [NodePath](class_nodepath.md#class-nodepath))          |
|                                                       | set_reference_type(index: [int](class_int.md#class-int), type: ReferenceType) |
|                                                       | set_setting_count(count: [int](class_int.md#class-int))                                                                |

---

## Enumerations

enum **ReferenceType**:

ReferenceType **REFERENCE_TYPE_BONE** = `0`

The reference target is a bone. In this case, the reference target spaces is local space.

ReferenceType **REFERENCE_TYPE_NODE** = `1`

The reference target is a [Node3D](class_node3d.md#class-node3d). In this case, the reference target spaces is model space.

In other words, the reference target's coordinates are treated as if it were placed directly under [Skeleton3D](class_skeleton3d.md#class-skeleton3d) which parent of the **BoneConstraint3D**.

---

## Method Descriptions

 **clear_setting**()

Clear all settings.

---

[float](class_float.md#class-float) **get_amount**(index: [int](class_int.md#class-int))

Returns the apply amount of the setting at `index`.

---

[int](class_int.md#class-int) **get_apply_bone**(index: [int](class_int.md#class-int))

Returns the apply bone of the setting at `index`. This bone will be modified.

---

[String](class_string.md#class-string) **get_apply_bone_name**(index: [int](class_int.md#class-int))

Returns the apply bone name of the setting at `index`. This bone will be modified.

---

[int](class_int.md#class-int) **get_reference_bone**(index: [int](class_int.md#class-int))

Returns the reference bone of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

---

[String](class_string.md#class-string) **get_reference_bone_name**(index: [int](class_int.md#class-int))

Returns the reference bone name of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

---

[NodePath](class_nodepath.md#class-nodepath) **get_reference_node**(index: [int](class_int.md#class-int))

Returns the reference node path of the setting at `index`.

This node will be only referenced and not modified by this modifier.

---

ReferenceType **get_reference_type**(index: [int](class_int.md#class-int))

Returns the reference target type of the setting at `index`. See also ReferenceType.

---

[int](class_int.md#class-int) **get_setting_count**()

Returns the number of settings in the modifier.

---

 **set_amount**(index: [int](class_int.md#class-int), amount: [float](class_float.md#class-float))

Sets the apply amount of the setting at `index` to `amount`.

---

 **set_apply_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the apply bone of the setting at `index` to `bone`. This bone will be modified.

---

 **set_apply_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the apply bone of the setting at `index` to `bone_name`. This bone will be modified.

---

 **set_reference_bone**(index: [int](class_int.md#class-int), bone: [int](class_int.md#class-int))

Sets the reference bone of the setting at `index` to `bone`.

This bone will be only referenced and not modified by this modifier.

---

 **set_reference_bone_name**(index: [int](class_int.md#class-int), bone_name: [String](class_string.md#class-string))

Sets the reference bone of the setting at `index` to `bone_name`.

This bone will be only referenced and not modified by this modifier.

---

 **set_reference_node**(index: [int](class_int.md#class-int), node: [NodePath](class_nodepath.md#class-nodepath))

Sets the reference node path of the setting at `index` to `node`.

This node will be only referenced and not modified by this modifier.

---

 **set_reference_type**(index: [int](class_int.md#class-int), type: ReferenceType)

Sets the reference target type of the setting at `index` to `type`. See also ReferenceType.

---

 **set_setting_count**(count: [int](class_int.md#class-int))

Sets the number of settings in the modifier.
