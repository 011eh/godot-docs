# OpenXRSpatialComponentMesh3DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries mesh3d result data.

## Description

Object for storing the queries 3d mesh result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

## Methods

| [Mesh](class_mesh.md#class-mesh)                      | get_mesh(index: [int](class_int.md#class-int))           |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [Transform3D](class_transform3d.md#class-transform3d) | get_transform(index: [int](class_int.md#class-int)) |

---

## Method Descriptions

[Mesh](class_mesh.md#class-mesh) **get_mesh**(index: [int](class_int.md#class-int))

Returns the mesh for the entity at this `index`.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_transform**(index: [int](class_int.md#class-int))

Returns the transform for positioning our mesh for the entity at this `index`.
