# OpenXRSpatialComponentAnchorList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries anchor result data.

## Description

Object for storing the queries anchor result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

## Methods

| [Transform3D](class_transform3d.md#class-transform3d)   | get_entity_pose(index: [int](class_int.md#class-int))    |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|

---

## Method Descriptions

[Transform3D](class_transform3d.md#class-transform3d) **get_entity_pose**(index: [int](class_int.md#class-int))

Returns the transform for the entity at this `index`.
