# OpenXRHand

**Deprecated:** Use [XRHandModifier3D](class_xrhandmodifier3d.md#class-xrhandmodifier3d) instead.

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Node supporting hand and finger tracking in OpenXR.

## Description

This node enables OpenXR's hand tracking functionality. The node should be a child node of an [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d) node, tracking will update its position to the player's tracked hand Palm joint location (the center of the middle finger's metacarpal bone). This node also updates the skeleton of a properly skinned hand or avatar model.

If the skeleton is a hand (one of the hand bones is the root node of the skeleton), then the skeleton will be placed relative to the hand palm location and the hand mesh and skeleton should be children of the OpenXRHand node.

If the hand bones are part of a full skeleton, then the root of the hand will keep its location with the assumption that IK is used to position the hand and arm.

By default the skeleton hand bones are repositioned to match the size of the tracked hand. To preserve the modeled bone sizes change bone_update to apply rotation only.

## Properties

| BoneUpdate    | bone_update     | `0`            |
|----------------------------------------------|-----------------------------------------------------------|----------------|
| Hands              | hand                   | `0`            |
| [NodePath](class_nodepath.md#class-nodepath) | hand_skeleton | `NodePath("")` |
| MotionRange  | motion_range   | `0`            |
| SkeletonRig  | skeleton_rig   | `0`            |

---

## Enumerations

enum **Hands**:

Hands **HAND_LEFT** = `0`

Tracking the player's left hand.

Hands **HAND_RIGHT** = `1`

Tracking the player's right hand.

Hands **HAND_MAX** = `2`

Maximum supported hands.

---

enum **MotionRange**:

MotionRange **MOTION_RANGE_UNOBSTRUCTED** = `0`

When player grips, hand skeleton will form a full fist.

MotionRange **MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

When player grips, hand skeleton conforms to the controller the player is holding.

MotionRange **MOTION_RANGE_MAX** = `2`

Maximum supported motion ranges.

---

enum **SkeletonRig**:

SkeletonRig **SKELETON_RIG_OPENXR** = `0`

An OpenXR compliant skeleton.

SkeletonRig **SKELETON_RIG_HUMANOID** = `1`

A [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid) compliant skeleton.

SkeletonRig **SKELETON_RIG_MAX** = `2`

Maximum supported hands.

---

enum **BoneUpdate**:

BoneUpdate **BONE_UPDATE_FULL** = `0`

The skeletons bones are fully updated (both position and rotation) to match the tracked bones.

BoneUpdate **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeletons bones are only rotated to align with the tracked bones, preserving bone length.

BoneUpdate **BONE_UPDATE_MAX** = `2`

Maximum supported bone update mode.

---

## Property Descriptions

BoneUpdate **bone_update** = `0`

-  **set_bone_update**(value: BoneUpdate)
- BoneUpdate **get_bone_update**()

Specify the type of updates to perform on the bone.

---

Hands **hand** = `0`

-  **set_hand**(value: Hands)
- Hands **get_hand**()

Specifies whether this node tracks the left or right hand of the player.

---

[NodePath](class_nodepath.md#class-nodepath) **hand_skeleton** = `NodePath("")`

-  **set_hand_skeleton**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_hand_skeleton**()

Set a [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node for which the pose positions will be updated.

---

MotionRange **motion_range** = `0`

-  **set_motion_range**(value: MotionRange)
- MotionRange **get_motion_range**()

Set the motion range (if supported) limiting the hand motion.

---

SkeletonRig **skeleton_rig** = `0`

-  **set_skeleton_rig**(value: SkeletonRig)
- SkeletonRig **get_skeleton_rig**()

Set the type of skeleton rig the hand_skeleton is compliant with.
