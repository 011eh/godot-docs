# SkeletonModification2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [SkeletonModification2DCCDIK](class_skeletonmodification2dccdik.md#class-skeletonmodification2dccdik), [SkeletonModification2DFABRIK](class_skeletonmodification2dfabrik.md#class-skeletonmodification2dfabrik), [SkeletonModification2DJiggle](class_skeletonmodification2djiggle.md#class-skeletonmodification2djiggle), [SkeletonModification2DLookAt](class_skeletonmodification2dlookat.md#class-skeletonmodification2dlookat), [SkeletonModification2DPhysicalBones](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones), [SkeletonModification2DStackHolder](class_skeletonmodification2dstackholder.md#class-skeletonmodification2dstackholder), [SkeletonModification2DTwoBoneIK](class_skeletonmodification2dtwoboneik.md#class-skeletonmodification2dtwoboneik)

Base class for resources that operate on [Bone2D](class_bone2d.md#class-bone2d)s in a [Skeleton2D](class_skeleton2d.md#class-skeleton2d).

## Description

This resource provides an interface that can be expanded so code that operates on [Bone2D](class_bone2d.md#class-bone2d) nodes in a [Skeleton2D](class_skeleton2d.md#class-skeleton2d) can be mixed and matched together to create complex interactions.

This is used to provide Godot with a flexible and powerful Inverse Kinematics solution that can be adapted for many different uses.

## Properties

| [bool](class_bool.md#class-bool)   | enabled               | `true`   |
|------------------------------------|-------------------------------------------------------------------------|----------|
| [int](class_int.md#class-int)      | execution_mode | `0`      |

## Methods

|                                                                                                       | \_draw_editor_gizmo()                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                       | \_execute(delta: [float](class_float.md#class-float))                                                                                                                             |
|                                                                                                       | \_setup_modification(modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d))                        |
| [float](class_float.md#class-float)                                                                   | clamp_angle(angle: [float](class_float.md#class-float), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float), invert: [bool](class_bool.md#class-bool)) |
| [bool](class_bool.md#class-bool)                                                                      | get_editor_draw_gizmo()                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                                      | get_is_setup()                                                                                                                                                                       |
| [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) | get_modification_stack()                                                                                                                                                   |
|                                                                                                       | set_editor_draw_gizmo(draw_gizmo: [bool](class_bool.md#class-bool))                                                                                                         |
|                                                                                                       | set_is_setup(is_setup: [bool](class_bool.md#class-bool))                                                                                                                             |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **enabled** = `true`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enabled**()

If `true`, the modification's \_execute() function will be called by the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d).

---

[int](class_int.md#class-int) **execution_mode** = `0`

-  **set_execution_mode**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_execution_mode**()

The execution mode for the modification. This tells the modification stack when to execute the modification. Some modifications have settings that are only available in certain execution modes.

---

## Method Descriptions

 **\_draw_editor_gizmo**()

Used for drawing **editor-only** modification gizmos. This function will only be called in the Godot editor and can be overridden to draw custom gizmos.

**Note:** You will need to use the Skeleton2D from [SkeletonModificationStack2D.get_skeleton()](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d-method-get-skeleton) and it's draw functions, as the **SkeletonModification2D** resource cannot draw on its own.

---

 **\_execute**(delta: [float](class_float.md#class-float))

Executes the given modification. This is where the modification performs whatever function it is designed to do.

---

 **\_setup_modification**(modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d))

Called when the modification is setup. This is where the modification performs initialization.

---

[float](class_float.md#class-float) **clamp_angle**(angle: [float](class_float.md#class-float), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float), invert: [bool](class_bool.md#class-bool))

Takes an angle and clamps it so it is within the passed-in `min` and `max` range. `invert` will inversely clamp the angle, clamping it to the range outside of the given bounds.

---

[bool](class_bool.md#class-bool) **get_editor_draw_gizmo**()

Returns whether this modification will call \_draw_editor_gizmo() in the Godot editor to draw modification-specific gizmos.

---

[bool](class_bool.md#class-bool) **get_is_setup**()

Returns whether this modification has been successfully setup or not.

---

[SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) **get_modification_stack**()

Returns the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) that this modification is bound to. Through the modification stack, you can access the Skeleton2D the modification is operating on.

---

 **set_editor_draw_gizmo**(draw_gizmo: [bool](class_bool.md#class-bool))

Sets whether this modification will call \_draw_editor_gizmo() in the Godot editor to draw modification-specific gizmos.

---

 **set_is_setup**(is_setup: [bool](class_bool.md#class-bool))

Manually allows you to set the setup state of the modification. This function should only rarely be used, as the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class-skeletonmodificationstack2d) the modification is bound to should handle setting the modification up.
