# SkeletonModifier3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [BoneConstraint3D](class_boneconstraint3d.md#class-boneconstraint3d), [BoneTwistDisperser3D](class_bonetwistdisperser3d.md#class-bonetwistdisperser3d), [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d), [LimitAngularVelocityModifier3D](class_limitangularvelocitymodifier3d.md#class-limitangularvelocitymodifier3d), [LookAtModifier3D](class_lookatmodifier3d.md#class-lookatmodifier3d), [ModifierBoneTarget3D](class_modifierbonetarget3d.md#class-modifierbonetarget3d), [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d), [RetargetModifier3D](class_retargetmodifier3d.md#class-retargetmodifier3d), [SkeletonIK3D](class_skeletonik3d.md#class-skeletonik3d), [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d), [XRBodyModifier3D](class_xrbodymodifier3d.md#class-xrbodymodifier3d), [XRHandModifier3D](class_xrhandmodifier3d.md#class-xrhandmodifier3d)

A node that may modify a Skeleton3D's bones.

## Description

**SkeletonModifier3D** retrieves a target [Skeleton3D](class_skeleton3d.md#class-skeleton3d) by having a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) parent.

If there is an [AnimationMixer](class_animationmixer.md#class-animationmixer), a modification always performs after playback process of the [AnimationMixer](class_animationmixer.md#class-animationmixer).

This node should be used to implement custom IK solvers, constraints, or skeleton physics.

## Tutorials

- [Design of the Skeleton Modifier 3D](https://godotengine.org/article/design-of-the-skeleton-modifier-3d/)

## Properties

| [bool](class_bool.md#class-bool)    | active       | `true`   |
|-------------------------------------|-----------------------------------------------------------|----------|
| [float](class_float.md#class-float) | influence | `1.0`    |

## Methods

|                                                    | \_process_modification()                                                                                                                           |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                    | \_process_modification_with_delta(delta: [float](class_float.md#class-float))                                                           |
|                                                    | \_skeleton_changed(old_skeleton: [Skeleton3D](class_skeleton3d.md#class-skeleton3d), new_skeleton: [Skeleton3D](class_skeleton3d.md#class-skeleton3d)) |
|                                                    | \_validate_bone_names()                                                                                                                             |
| [Skeleton3D](class_skeleton3d.md#class-skeleton3d) | get_skeleton()                                                                                                                                                     |

---

## Signals

**modification_processed**()

Notifies when the modification have been finished.

**Note:** If you want to get the modified bone pose by the modifier, you must use [Skeleton3D.get_bone_pose()](class_skeleton3d.md#class-skeleton3d-method-get-bone-pose) or [Skeleton3D.get_bone_global_pose()](class_skeleton3d.md#class-skeleton3d-method-get-bone-global-pose) at the moment this signal is fired.

---

## Enumerations

enum **BoneAxis**:

BoneAxis **BONE_AXIS_PLUS_X** = `0`

Enumerated value for the +X axis.

BoneAxis **BONE_AXIS_MINUS_X** = `1`

Enumerated value for the -X axis.

BoneAxis **BONE_AXIS_PLUS_Y** = `2`

Enumerated value for the +Y axis.

BoneAxis **BONE_AXIS_MINUS_Y** = `3`

Enumerated value for the -Y axis.

BoneAxis **BONE_AXIS_PLUS_Z** = `4`

Enumerated value for the +Z axis.

BoneAxis **BONE_AXIS_MINUS_Z** = `5`

Enumerated value for the -Z axis.

---

enum **BoneDirection**:

BoneDirection **BONE_DIRECTION_PLUS_X** = `0`

Enumerated value for the +X axis.

BoneDirection **BONE_DIRECTION_MINUS_X** = `1`

Enumerated value for the -X axis.

BoneDirection **BONE_DIRECTION_PLUS_Y** = `2`

Enumerated value for the +Y axis.

BoneDirection **BONE_DIRECTION_MINUS_Y** = `3`

Enumerated value for the -Y axis.

BoneDirection **BONE_DIRECTION_PLUS_Z** = `4`

Enumerated value for the +Z axis.

BoneDirection **BONE_DIRECTION_MINUS_Z** = `5`

Enumerated value for the -Z axis.

BoneDirection **BONE_DIRECTION_FROM_PARENT** = `6`

Enumerated value for the axis from a parent bone to the child bone.

---

enum **SecondaryDirection**:

SecondaryDirection **SECONDARY_DIRECTION_NONE** = `0`

Enumerated value for the case when the axis is undefined.

SecondaryDirection **SECONDARY_DIRECTION_PLUS_X** = `1`

Enumerated value for the +X axis.

SecondaryDirection **SECONDARY_DIRECTION_MINUS_X** = `2`

Enumerated value for the -X axis.

SecondaryDirection **SECONDARY_DIRECTION_PLUS_Y** = `3`

Enumerated value for the +Y axis.

SecondaryDirection **SECONDARY_DIRECTION_MINUS_Y** = `4`

Enumerated value for the -Y axis.

SecondaryDirection **SECONDARY_DIRECTION_PLUS_Z** = `5`

Enumerated value for the +Z axis.

SecondaryDirection **SECONDARY_DIRECTION_MINUS_Z** = `6`

Enumerated value for the -Z axis.

SecondaryDirection **SECONDARY_DIRECTION_CUSTOM** = `7`

Enumerated value for an optional axis.

---

enum **RotationAxis**:

RotationAxis **ROTATION_AXIS_X** = `0`

Enumerated value for the rotation of the X axis.

RotationAxis **ROTATION_AXIS_Y** = `1`

Enumerated value for the rotation of the Y axis.

RotationAxis **ROTATION_AXIS_Z** = `2`

Enumerated value for the rotation of the Z axis.

RotationAxis **ROTATION_AXIS_ALL** = `3`

Enumerated value for the unconstrained rotation.

RotationAxis **ROTATION_AXIS_CUSTOM** = `4`

Enumerated value for an optional rotation axis.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **active** = `true`

-  **set_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_active**()

If `true`, the **SkeletonModifier3D** will be processing.

---

[float](class_float.md#class-float) **influence** = `1.0`

-  **set_influence**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_influence**()

Sets the influence of the modification.

**Note:** This value is used by [Skeleton3D](class_skeleton3d.md#class-skeleton3d) to blend, so the **SkeletonModifier3D** should always apply only 100% of the result without interpolation.

---

## Method Descriptions

 **\_process_modification**()

**Deprecated:** Use \_process_modification_with_delta() instead.

Override this virtual method to implement a custom skeleton modifier. You should do things like get the [Skeleton3D](class_skeleton3d.md#class-skeleton3d)'s current pose and apply the pose here.

\_process_modification() must not apply influence to bone poses because the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) automatically applies influence to all bone poses set by the modifier.

---

 **\_process_modification_with_delta**(delta: [float](class_float.md#class-float))

Override this virtual method to implement a custom skeleton modifier. You should do things like get the [Skeleton3D](class_skeleton3d.md#class-skeleton3d)'s current pose and apply the pose here.

\_process_modification_with_delta() must not apply influence to bone poses because the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) automatically applies influence to all bone poses set by the modifier.

`delta` is passed from parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d). See also [Skeleton3D.advance()](class_skeleton3d.md#class-skeleton3d-method-advance).

**Note:** This method may be called outside [Node._process()](class_node.md#class-node-private-method-process) and [Node._physics_process()](class_node.md#class-node-private-method-physics-process) with `delta` is `0.0`, since the modification should be processed immediately after initialization of the [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

---

 **\_skeleton_changed**(old_skeleton: [Skeleton3D](class_skeleton3d.md#class-skeleton3d), new_skeleton: [Skeleton3D](class_skeleton3d.md#class-skeleton3d))

Called when the skeleton is changed.

---

 **\_validate_bone_names**()

Called when bone names and indices need to be validated, such as when entering the scene tree or changing skeleton.

---

[Skeleton3D](class_skeleton3d.md#class-skeleton3d) **get_skeleton**()

Returns the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node if it exists. Otherwise, returns `null`.
