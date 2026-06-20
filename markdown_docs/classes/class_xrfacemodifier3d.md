# XRFaceModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node for driving standard face meshes from [XRFaceTracker](class_xrfacetracker.md#class-xrfacetracker) weights.

## Description

This node applies weights from an [XRFaceTracker](class_xrfacetracker.md#class-xrfacetracker) to a mesh with supporting face blend shapes.

The [Unified Expressions](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/unified-blendshapes) blend shapes are supported, as well as ARKit and SRanipal blend shapes.

The node attempts to identify blend shapes based on name matching. Blend shapes should match the names listed in the [Unified Expressions Compatibility](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/compatibility/overview) chart.

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

## Properties

| [StringName](class_stringname.md#class-stringname)   | face_tracker   | `&"/user/face_tracker"`   |
|------------------------------------------------------|-----------------------------------------------------------------|---------------------------|
| [NodePath](class_nodepath.md#class-nodepath)         | target               | `NodePath("")`            |

---

## Property Descriptions

[StringName](class_stringname.md#class-stringname) **face_tracker** = `&"/user/face_tracker"`

-  **set_face_tracker**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_face_tracker**()

The [XRFaceTracker](class_xrfacetracker.md#class-xrfacetracker) path.

---

[NodePath](class_nodepath.md#class-nodepath) **target** = `NodePath("")`

-  **set_target**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_target**()

The [NodePath](class_nodepath.md#class-nodepath) of the face [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d).
