# Occluder3D

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [ArrayOccluder3D](class_arrayoccluder3d.md#class-arrayoccluder3d), [BoxOccluder3D](class_boxoccluder3d.md#class-boxoccluder3d), [PolygonOccluder3D](class_polygonoccluder3d.md#class-polygonoccluder3d), [QuadOccluder3D](class_quadoccluder3d.md#class-quadoccluder3d), [SphereOccluder3D](class_sphereoccluder3d.md#class-sphereoccluder3d)

Occluder shape resource for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d).

## Description

**Occluder3D** stores an occluder shape that can be used by the engine's occlusion culling system.

See [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d)'s documentation for instructions on setting up occlusion culling.

## Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

## Methods

| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | get_indices()    |
|----------------------------------------------------------------------------|----------------------------------------------------------|
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | get_vertices()  |

---

## Method Descriptions

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_indices**()

Returns the occluder shape's vertex indices.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_vertices**()

Returns the occluder shape's vertex positions.
