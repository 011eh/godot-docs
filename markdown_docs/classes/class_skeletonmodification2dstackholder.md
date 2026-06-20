# SkeletonModification2DStackHolder

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A modification that holds and executes a [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d).

## Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class-skeletonmodification2d) holds a reference to a [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d), allowing you to use multiple modification stacks on a single [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

**Note:** The modifications in the held [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) will only be executed if their execution mode matches the execution mode of the SkeletonModification2DStackHolder.

## Methods

| [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d)   | get_held_modification_stack()                                                                                                                               |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                         | set_held_modification_stack(held_modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d)) |

---

## Method Descriptions

[SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) **get_held_modification_stack**()

Returns the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) that this modification is holding.

---

 **set_held_modification_stack**(held_modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d))

Sets the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) that this modification is holding. This modification stack will then be executed when this modification is executed.
