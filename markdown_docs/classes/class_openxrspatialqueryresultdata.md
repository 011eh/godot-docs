# OpenXRSpatialQueryResultData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the main query result data.

## Description

Object for storing the main query result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot). This must always be the first component requested.

## Methods

| [int](class_int.md#class-int)                                                                                  | get_capacity()                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                                                                  | get_entity_id(index: [int](class_int.md#class-int))       |
| [EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) | get_entity_state(index: [int](class_int.md#class-int)) |

---

## Method Descriptions

[int](class_int.md#class-int) **get_capacity**()

Returns the number of entities that were retrieved.

---

[int](class_int.md#class-int) **get_entity_id**(index: [int](class_int.md#class-int))

Returns the entity id (`XrSpatialEntityIdEXT`) for the entity at this `index`.

---

[EntityTrackingState](class_openxrspatialentitytracker.md#enum-openxrspatialentitytracker-entitytrackingstate) **get_entity_state**(index: [int](class_int.md#class-int))

Returns the entity state for the entity at this `index`.
