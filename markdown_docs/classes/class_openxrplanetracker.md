# OpenXRPlaneTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Spatial entity tracker for our spatial entity plane tracking extension.

## Description

Spatial entity tracker for our OpenXR spatial entity plane tracking extension. These trackers identify entities in our real space such as walls, floors, tables, etc. and map their location to our virtual space.

## Properties

| [Vector2](class_vector2.md#class-vector2)                                                                                        | bounds_size         | `Vector2(0, 0)`   |
|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------|
| [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) | plane_alignment | `0`               |
| [String](class_string.md#class-string)                                                                                           | plane_label         | `""`              |

## Methods

|                                                       | clear_mesh_data()                                                                                                                                                                                                                                                    |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Mesh](class_mesh.md#class-mesh)                      | get_mesh()                                                                                                                                                                                                                                                                  |
| [Transform3D](class_transform3d.md#class-transform3d) | get_mesh_offset()                                                                                                                                                                                                                                                    |
| [Shape3D](class_shape3d.md#class-shape3d)             | get_shape(thickness: [float](class_float.md#class-float) = 0.01)                                                                                                                                                                                                           |
|                                                       | set_mesh_data(origin: [Transform3D](class_transform3d.md#class-transform3d), vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array) = PackedInt32Array()) |

---

## Signals

**mesh_changed**()

Emitted when our mesh data has changed the mesh instance and collision needs to be updated.

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **bounds_size** = `Vector2(0, 0)`

-  **set_bounds_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_bounds_size**()

The bounding size of the plane. This is a 2D size.

---

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **plane_alignment** = `0`

-  **set_plane_alignment**(value: [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment))
- [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum-openxrspatialcomponentplanealignmentlist-planealignment) **get_plane_alignment**()

The main alignment in space of this plane.

---

[String](class_string.md#class-string) **plane_label** = `""`

-  **set_plane_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_plane_label**()

The semantic label for this plane.

---

## Method Descriptions

 **clear_mesh_data**()

Clears the mesh data for this tracker. You should only call this if you are handling your own discovery logic.

---

[Mesh](class_mesh.md#class-mesh) **get_mesh**()

Gets a mesh created from either the mesh data or from our bounding size for this plane.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_mesh_offset**()

Gets the transform by which to offset the mesh and collision shape from our pose to display these correctly.

---

[Shape3D](class_shape3d.md#class-shape3d) **get_shape**(thickness: [float](class_float.md#class-float) = 0.01)

Gets a collision shape built either from the mesh data or from our bounding size for this plane.

---

 **set_mesh_data**(origin: [Transform3D](class_transform3d.md#class-transform3d), vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array) = PackedInt32Array())

Sets the mesh data for this plane. You should only call this if you are handling your own discovery logic.
