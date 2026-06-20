# XRBodyModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node for driving body meshes from [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker) data.

## Description

This node uses body tracking data from an [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker) to pose the skeleton of a body mesh.

Positioning of the body is performed by creating an [XRNode3D](class_xrnode3d.md#class-xrnode3d) ancestor of the body mesh driven by the same [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker).

The body tracking position-data is scaled by [Skeleton3D.motion_scale](class_skeleton3d.md#class-skeleton3d-property-motion-scale) when applied to the skeleton, which can be used to adjust the tracked body to match the scale of the body model.

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

## Properties

| [StringName](class_stringname.md#class-stringname)   | body_tracker   | `&"/user/body_tracker"`   |
|------------------------------------------------------|-----------------------------------------------------------------|---------------------------|
| [BodyUpdate]    | body_update     | `7`                       |
| BoneUpdate      | bone_update     | `0`                       |

---

## Enumerations

flags **BodyUpdate**:

BodyUpdate **BODY_UPDATE_UPPER_BODY** = `1`

The skeleton's upper body joints are updated.

BodyUpdate **BODY_UPDATE_LOWER_BODY** = `2`

The skeleton's lower body joints are updated.

BodyUpdate **BODY_UPDATE_HANDS** = `4`

The skeleton's hand joints are updated.

---

enum **BoneUpdate**:

BoneUpdate **BONE_UPDATE_FULL** = `0`

The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.

BoneUpdate **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.

BoneUpdate **BONE_UPDATE_MAX** = `2`

Represents the size of the BoneUpdate enum.

---

## Property Descriptions

[StringName](class_stringname.md#class-stringname) **body_tracker** = `&"/user/body_tracker"`

-  **set_body_tracker**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_body_tracker**()

The name of the [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker) registered with [XRServer](class_xrserver.md#class-xrserver) to obtain the body tracking data from.

---

[BodyUpdate] **body_update** = `7`

-  **set_body_update**(value: [BodyUpdate])
- [BodyUpdate] **get_body_update**()

Specifies the body parts to update.

---

BoneUpdate **bone_update** = `0`

-  **set_bone_update**(value: BoneUpdate)
- BoneUpdate **get_bone_update**()

Specifies the type of updates to perform on the bones.
