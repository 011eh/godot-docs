# IKModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [ChainIK3D](class_chainik3d.md#class-chainik3d), [TwoBoneIK3D](class_twoboneik3d.md#class-twoboneik3d)

A node for inverse kinematics which may modify more than one bone.

## Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d)s that has some joint lists and applies inverse kinematics. This class has some structs, enums, and helper methods which are useful to solve inverse kinematics.

## Tutorials

- [Inverse Kinematics Returns to Godot 4.6 - IKModifier3D](https://godotengine.org/article/inverse-kinematics-returns-to-godot-4-6/#ikmodifier3d-and-7-child-classes)

## Properties

| [bool](class_bool.md#class-bool)   | mutable_bone_axes   | `true`   |
|------------------------------------|-----------------------------------------------------------------------|----------|

## Methods

|                               | clear_settings()                                           |
|-------------------------------|---------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int) | get_setting_count()                                     |
|                               | reset()                                                             |
|                               | set_setting_count(count: [int](class_int.md#class-int)) |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **mutable_bone_axes** = `true`

-  **set_mutable_bone_axes**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_bone_axes_mutable**()

If `true`, the solver retrieves the bone axis from the bone pose every frame.

If `false`, the solver retrieves the bone axis from the bone rest and caches it, which increases performance slightly, but position changes in the bone pose made before processing this **IKModifier3D** are ignored.

---

## Method Descriptions

 **clear_settings**()

Clears all settings.

---

[int](class_int.md#class-int) **get_setting_count**()

Returns the number of settings.

---

 **reset**()

Resets a state with respect to the current bone pose.

---

 **set_setting_count**(count: [int](class_int.md#class-int))

Sets the number of settings.
