# SkeletonModificationStack2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A resource that holds a stack of [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)s.

## Description

This resource is used by the Skeleton and holds a stack of [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)s.

This controls the order of the modifications and how they are applied. Modification order is especially important for full-body IK setups, as you need to execute the modifications in the correct order to get the desired results. For example, you want to execute a modification on the spine *before* the arms on a humanoid skeleton.

This resource also controls how strongly all of the modifications are applied to the [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

## Properties

| [bool](class_bool.md#class-bool)    | enabled                       | `false`   |
|-------------------------------------|--------------------------------------------------------------------------------------|-----------|
| [int](class_int.md#class-int)       | modification_count | `0`       |
| [float](class_float.md#class-float) | strength                     | `1.0`     |

## Methods

|                                                                                        | add_modification(modification: [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d))                                         |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                        | delete_modification(mod_idx: [int](class_int.md#class-int))                                                                                                 |
|                                                                                        | enable_all_modifications(enabled: [bool](class_bool.md#class-bool))                                                                                    |
|                                                                                        | execute(delta: [float](class_float.md#class-float), execution_mode: [int](class_int.md#class-int))                                                                      |
| [bool](class_bool.md#class-bool)                                                       | get_is_setup()                                                                                                                                                     |
| [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) | get_modification(mod_idx: [int](class_int.md#class-int))                                                                                                       |
| [Skeleton2D](class_skeleton2d.md#class-skeleton2d)                                     | get_skeleton()                                                                                                                                                     |
|                                                                                        | set_modification(mod_idx: [int](class_int.md#class-int), modification: [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)) |
|                                                                                        | setup()                                                                                                                                                                   |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **enabled** = `false`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enabled**()

If `true`, the modification's in the stack will be called. This is handled automatically through the [Skeleton2D](class_skeleton2d.md#class-skeleton2d) node.

---

[int](class_int.md#class-int) **modification_count** = `0`

-  **set_modification_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_modification_count**()

The number of modifications in the stack.

---

[float](class_float.md#class-float) **strength** = `1.0`

-  **set_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_strength**()

The interpolation strength of the modifications in stack. A value of `0` will make it where the modifications are not applied, a strength of `0.5` will be half applied, and a strength of `1` will allow the modifications to be fully applied and override the [Skeleton2D](class_skeleton2d.md#class-skeleton2d) [Bone2D](class_bone2d.md#class-bone2d) poses.

---

## Method Descriptions

 **add_modification**(modification: [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d))

Adds the passed-in [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) to the stack.

---

 **delete_modification**(mod_idx: [int](class_int.md#class-int))

Deletes the [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) at the index position `mod_idx`, if it exists.

---

 **enable_all_modifications**(enabled: [bool](class_bool.md#class-bool))

Enables all [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)s in the stack.

---

 **execute**(delta: [float](class_float.md#class-float), execution_mode: [int](class_int.md#class-int))

Executes all of the [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d)s in the stack that use the same execution mode as the passed-in `execution_mode`, starting from index `0` to modification_count.

**Note:** The order of the modifications can matter depending on the modifications. For example, modifications on a spine should operate before modifications on the arms in order to get proper results.

---

[bool](class_bool.md#class-bool) **get_is_setup**()

Returns a boolean that indicates whether the modification stack is setup and can execute.

---

[SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **get_modification**(mod_idx: [int](class_int.md#class-int))

Returns the [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) at the passed-in index, `mod_idx`.

---

[Skeleton2D](class_skeleton2d.md#class-skeleton2d) **get_skeleton**()

Returns the [Skeleton2D](class_skeleton2d.md#class-skeleton2d) node that the SkeletonModificationStack2D is bound to.

---

 **set_modification**(mod_idx: [int](class_int.md#class-int), modification: [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d))

Sets the modification at `mod_idx` to the passed-in modification, `modification`.

---

 **setup**()

Sets up the modification stack so it can execute. This function should be called by [Skeleton2D](class_skeleton2d.md#class-skeleton2d) and shouldn't be manually called unless you know what you are doing.
