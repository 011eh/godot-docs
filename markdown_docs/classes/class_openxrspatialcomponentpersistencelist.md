# OpenXRSpatialComponentPersistenceList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the query persistence result data.

## Description

Object for storing the query persistence result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

## Methods

| [int](class_int.md#class-int)          | get_persistent_state(index: [int](class_int.md#class-int))    |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string) | get_persistent_uuid(index: [int](class_int.md#class-int))      |

---

## Method Descriptions

[int](class_int.md#class-int) **get_persistent_state**(index: [int](class_int.md#class-int))

Returns the persistent state (`XrSpatialPersistenceStateEXT`) for the entity at this `index`.

---

[String](class_string.md#class-string) **get_persistent_uuid**(index: [int](class_int.md#class-int))

Returns the persistent uuid for the entity at this `index`.
