# OpenXRSpatialComponentParentList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries parent result data.

## Description

Object for storing the queries parent result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

## Methods

| [RID](class_rid.md#class-rid)   | get_parent(index: [int](class_int.md#class-int))    |
|---------------------------------|------------------------------------------------------------------------------------------------------------------|

---

## Method Descriptions

[RID](class_rid.md#class-rid) **get_parent**(index: [int](class_int.md#class-int))

Returns the RID for the parent entity at this `index`.
