# OpenXRSpatialComponentMesh2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries mesh2d result data.

## Description

Object for storing the queries 2D mesh result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

## Methods

| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | get_indices(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))    |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Transform3D](class_transform3d.md#class-transform3d)                      | get_transform(index: [int](class_int.md#class-int))                                         |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | get_vertices(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))  |

---

## Method Descriptions

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_indices**(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the mesh indices for the entity at this `index`.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_transform**(index: [int](class_int.md#class-int))

Returns the transform for positioning our mesh for the entity at this `index`.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_vertices**(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the mesh vertices for the entity at this `index`.
