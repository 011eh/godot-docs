# OpenXRSpatialComponentBounded2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries bounded2d result data.

## Description

Object for storing the queries 2D bounding rectangle result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

## Methods

| [Transform3D](class_transform3d.md#class-transform3d)   | get_center_pose(index: [int](class_int.md#class-int))    |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [Vector2](class_vector2.md#class-vector2)               | get_size(index: [int](class_int.md#class-int))                  |

---

## Method Descriptions

[Transform3D](class_transform3d.md#class-transform3d) **get_center_pose**(index: [int](class_int.md#class-int))

Returns the center of our bounding rectangle for the entity at this `index`.

---

[Vector2](class_vector2.md#class-vector2) **get_size**(index: [int](class_int.md#class-int))

Returns the size of our bounding rectangle for the entity at this `index`.
