# OpenXRSpatialComponentData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRSpatialComponentAnchorList](class_openxrspatialcomponentanchorlist.md#class-openxrspatialcomponentanchorlist), [OpenXRSpatialComponentBounded2DList](class_openxrspatialcomponentbounded2dlist.md#class-openxrspatialcomponentbounded2dlist), [OpenXRSpatialComponentBounded3DList](class_openxrspatialcomponentbounded3dlist.md#class-openxrspatialcomponentbounded3dlist), [OpenXRSpatialComponentMarkerList](class_openxrspatialcomponentmarkerlist.md#class-openxrspatialcomponentmarkerlist), [OpenXRSpatialComponentMesh2DList](class_openxrspatialcomponentmesh2dlist.md#class-openxrspatialcomponentmesh2dlist), [OpenXRSpatialComponentMesh3DList](class_openxrspatialcomponentmesh3dlist.md#class-openxrspatialcomponentmesh3dlist), [OpenXRSpatialComponentParentList](class_openxrspatialcomponentparentlist.md#class-openxrspatialcomponentparentlist), [OpenXRSpatialComponentPersistenceList](class_openxrspatialcomponentpersistencelist.md#class-openxrspatialcomponentpersistencelist), [OpenXRSpatialComponentPlaneAlignmentList](class_openxrspatialcomponentplanealignmentlist.md#class-openxrspatialcomponentplanealignmentlist), [OpenXRSpatialComponentPlaneSemanticLabelList](class_openxrspatialcomponentplanesemanticlabellist.md#class-openxrspatialcomponentplanesemanticlabellist), [OpenXRSpatialComponentPolygon2DList](class_openxrspatialcomponentpolygon2dlist.md#class-openxrspatialcomponentpolygon2dlist), [OpenXRSpatialQueryResultData](class_openxrspatialqueryresultdata.md#class-openxrspatialqueryresultdata)

Object for storing OpenXR spatial entity component data.

## Description

Object for storing OpenXR spatial entity component data.

## Methods

| [int](class_int.md#class-int)   | \_get_component_type()                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)   | \_get_structure_data(next: [int](class_int.md#class-int)) |
|                                 | \_set_capacity(capacity: [int](class_int.md#class-int))         |
| [int](class_int.md#class-int)   | get_component_type()                                              |
|                                 | set_capacity(capacity: [int](class_int.md#class-int))                   |

---

## Method Descriptions

[int](class_int.md#class-int) **\_get_component_type**()

Return the component type for the component we store data for.

---

[int](class_int.md#class-int) **\_get_structure_data**(next: [int](class_int.md#class-int))

Return a pointer to the structure data that will be submitted along with the snapshot query. This pointer must remain valid as long as this object is instantiated.

---

 **\_set_capacity**(capacity: [int](class_int.md#class-int))

Sets the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.

---

[int](class_int.md#class-int) **get_component_type**()

Gets this **OpenXRSpatialComponentData**'s `XrSpatialComponentTypeEXT`.

---

 **set_capacity**(capacity: [int](class_int.md#class-int))

Sets the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.
