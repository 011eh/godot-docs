# QuadOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class-occluder3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Flat plane shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d).

## Description

**QuadOccluder3D** stores a flat plane shape that can be used by the engine's occlusion culling system. See also [PolygonOccluder3D](class_polygonoccluder3d.md#class-polygonoccluder3d) if you need to customize the quad's shape.

See [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d)'s documentation for instructions on setting up occlusion culling.

## Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

## Properties

| [Vector2](class_vector2.md#class-vector2)   | size   | `Vector2(1, 1)`   |
|---------------------------------------------|-----------------------------------------------|-------------------|

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **size** = `Vector2(1, 1)`

-  **set_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_size**()

The quad's size in 3D units.
