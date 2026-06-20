# NavigationMesh

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A navigation mesh that defines traversable areas and obstacles.

## Description

A navigation mesh is a collection of polygons that define which areas of an environment are traversable to aid agents in pathfinding through complicated spaces.

## Tutorials

- [Using NavigationMeshes](../tutorials/navigation/navigation_using_navigationmeshes.md)
- [3D Navigation Demo](https://godotengine.org/asset-library/asset/2743)

## Properties

| [float](class_float.md#class-float)                             | agent_height                                         | `1.5`                             |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------|
| [float](class_float.md#class-float)                             | agent_max_climb                                   | `0.25`                            |
| [float](class_float.md#class-float)                             | agent_max_slope                                   | `45.0`                            |
| [float](class_float.md#class-float)                             | agent_radius                                         | `0.5`                             |
| [float](class_float.md#class-float)                             | border_size                                           | `0.0`                             |
| [float](class_float.md#class-float)                             | cell_height                                           | `0.25`                            |
| [float](class_float.md#class-float)                             | cell_size                                               | `0.25`                            |
| [float](class_float.md#class-float)                             | detail_sample_distance                     | `6.0`                             |
| [float](class_float.md#class-float)                             | detail_sample_max_error                   | `1.0`                             |
| [float](class_float.md#class-float)                             | edge_max_error                                     | `1.3`                             |
| [float](class_float.md#class-float)                             | edge_max_length                                   | `0.0`                             |
| [AABB](class_aabb.md#class-aabb)                                | filter_baking_aabb                             | `AABB(0, 0, 0, 0, 0, 0)`          |
| [Vector3](class_vector3.md#class-vector3)                       | filter_baking_aabb_offset               | `Vector3(0, 0, 0)`                |
| [bool](class_bool.md#class-bool)                                | filter_ledge_spans                             | `false`                           |
| [bool](class_bool.md#class-bool)                                | filter_low_hanging_obstacles         | `false`                           |
| [bool](class_bool.md#class-bool)                                | filter_walkable_low_height_spans | `false`                           |
| [int](class_int.md#class-int)                                   | geometry_collision_mask                   | `4294967295`                      |
| ParsedGeometryType   | geometry_parsed_geometry_type       | `2`                               |
| SourceGeometryMode   | geometry_source_geometry_mode       | `0`                               |
| [StringName](class_stringname.md#class-stringname)              | geometry_source_group_name             | `&"navigation_mesh_source_group"` |
| [float](class_float.md#class-float)                             | region_merge_size                               | `20.0`                            |
| [float](class_float.md#class-float)                             | region_min_size                                   | `2.0`                             |
| SamplePartitionType | sample_partition_type                       | `0`                               |
| [float](class_float.md#class-float)                             | vertices_per_polygon                         | `6.0`                             |

## Methods

|                                                                            | add_polygon(polygon: [PackedInt32Array](class_packedint32array.md#class-packedint32array))                                  |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                            | clear()                                                                                                                           |
|                                                                            | clear_polygons()                                                                                                         |
|                                                                            | create_from_mesh(mesh: [Mesh](class_mesh.md#class-mesh))                                                               |
| [bool](class_bool.md#class-bool)                                           | get_collision_mask_value(layer_number: [int](class_int.md#class-int))                                          |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | get_polygon(idx: [int](class_int.md#class-int))                                                                             |
| [int](class_int.md#class-int)                                              | get_polygon_count()                                                                                                   |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | get_vertices()                                                                                                             |
|                                                                            | set_collision_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
|                                                                            | set_vertices(vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))                         |

---

## Enumerations

enum **SamplePartitionType**:

SamplePartitionType **SAMPLE_PARTITION_WATERSHED** = `0`

Watershed partitioning. Generally the best choice if you precompute the navigation mesh, use this if you have large open areas.

SamplePartitionType **SAMPLE_PARTITION_MONOTONE** = `1`

Monotone partitioning. Use this if you want fast navigation mesh generation.

SamplePartitionType **SAMPLE_PARTITION_LAYERS** = `2`

Layer partitioning. Good choice to use for tiled navigation mesh with medium and small sized tiles.

SamplePartitionType **SAMPLE_PARTITION_MAX** = `3`

Represents the size of the SamplePartitionType enum.

---

enum **ParsedGeometryType**:

ParsedGeometryType **PARSED_GEOMETRY_MESH_INSTANCES** = `0`

Parses mesh instances as geometry. This includes [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d), [CSGShape3D](class_csgshape3d.md#class-csgshape3d), and [GridMap](class_gridmap.md#class-gridmap) nodes.

ParsedGeometryType **PARSED_GEOMETRY_STATIC_COLLIDERS** = `1`

Parses [StaticBody3D](class_staticbody3d.md#class-staticbody3d) colliders as geometry. The collider should be in any of the layers specified by geometry_collision_mask.

ParsedGeometryType **PARSED_GEOMETRY_BOTH** = `2`

Both PARSED_GEOMETRY_MESH_INSTANCES and PARSED_GEOMETRY_STATIC_COLLIDERS.

ParsedGeometryType **PARSED_GEOMETRY_MAX** = `3`

Represents the size of the ParsedGeometryType enum.

---

enum **SourceGeometryMode**:

SourceGeometryMode **SOURCE_GEOMETRY_ROOT_NODE_CHILDREN** = `0`

Scans the child nodes of the root node recursively for geometry.

SourceGeometryMode **SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN** = `1`

Scans nodes in a group and their child nodes recursively for geometry. The group is specified by geometry_source_group_name.

SourceGeometryMode **SOURCE_GEOMETRY_GROUPS_EXPLICIT** = `2`

Uses nodes in a group for geometry. The group is specified by geometry_source_group_name.

SourceGeometryMode **SOURCE_GEOMETRY_MAX** = `3`

Represents the size of the SourceGeometryMode enum.

---

## Property Descriptions

[float](class_float.md#class-float) **agent_height** = `1.5`

-  **set_agent_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_agent_height**()

The minimum floor to ceiling height that will still allow the floor area to be considered walkable.

**Note:** While baking, this value will be rounded up to the nearest multiple of cell_height.

---

[float](class_float.md#class-float) **agent_max_climb** = `0.25`

-  **set_agent_max_climb**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_agent_max_climb**()

The minimum ledge height that is considered to still be traversable.

**Note:** While baking, this value will be rounded down to the nearest multiple of cell_height.

---

[float](class_float.md#class-float) **agent_max_slope** = `45.0`

-  **set_agent_max_slope**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_agent_max_slope**()

The maximum slope that is considered walkable, in degrees.

---

[float](class_float.md#class-float) **agent_radius** = `0.5`

-  **set_agent_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_agent_radius**()

The distance to erode/shrink the walkable area of the heightfield away from obstructions.

**Note:** While baking, this value will be rounded up to the nearest multiple of cell_size.

**Note:** The radius must be equal or higher than `0.0`. If the radius is `0.0`, it won't be possible to fix invalid outline overlaps and other precision errors during the baking process. As a result, some obstacles may be excluded incorrectly from the final navigation mesh, or may delete the navigation mesh's polygons.

---

[float](class_float.md#class-float) **border_size** = `0.0`

-  **set_border_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_border_size**()

The size of the non-navigable border around the bake bounding area.

In conjunction with the filter_baking_aabb and a edge_max_error value at `1.0` or below the border size can be used to bake tile aligned navigation meshes without the tile edges being shrunk by agent_radius.

**Note:** If this value is not `0.0`, it will be rounded up to the nearest multiple of cell_size during baking.

---

[float](class_float.md#class-float) **cell_height** = `0.25`

-  **set_cell_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cell_height**()

The cell height used to rasterize the navigation mesh vertices on the Y axis. Must match with the cell height on the navigation map.

---

[float](class_float.md#class-float) **cell_size** = `0.25`

-  **set_cell_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cell_size**()

The cell size used to rasterize the navigation mesh vertices on the XZ plane. Must match with the cell size on the navigation map.

---

[float](class_float.md#class-float) **detail_sample_distance** = `6.0`

-  **set_detail_sample_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_detail_sample_distance**()

The sampling distance to use when generating the detail mesh, in cell unit.

---

[float](class_float.md#class-float) **detail_sample_max_error** = `1.0`

-  **set_detail_sample_max_error**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_detail_sample_max_error**()

The maximum distance the detail mesh surface should deviate from heightfield, in cell unit.

---

[float](class_float.md#class-float) **edge_max_error** = `1.3`

-  **set_edge_max_error**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_edge_max_error**()

The maximum distance a simplified contour's border edges should deviate the original raw contour.

---

[float](class_float.md#class-float) **edge_max_length** = `0.0`

-  **set_edge_max_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_edge_max_length**()

The maximum allowed length for contour edges along the border of the mesh. A value of `0.0` disables this feature.

**Note:** While baking, this value will be rounded up to the nearest multiple of cell_size.

---

[AABB](class_aabb.md#class-aabb) **filter_baking_aabb** = `AABB(0, 0, 0, 0, 0, 0)`

-  **set_filter_baking_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_filter_baking_aabb**()

If the baking [AABB](class_aabb.md#class-aabb) has a volume the navigation mesh baking will be restricted to its enclosing area.

---

[Vector3](class_vector3.md#class-vector3) **filter_baking_aabb_offset** = `Vector3(0, 0, 0)`

-  **set_filter_baking_aabb_offset**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_filter_baking_aabb_offset**()

The position offset applied to the filter_baking_aabb [AABB](class_aabb.md#class-aabb).

---

[bool](class_bool.md#class-bool) **filter_ledge_spans** = `false`

-  **set_filter_ledge_spans**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_filter_ledge_spans**()

If `true`, marks spans that are ledges as non-walkable.

---

[bool](class_bool.md#class-bool) **filter_low_hanging_obstacles** = `false`

-  **set_filter_low_hanging_obstacles**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_filter_low_hanging_obstacles**()

If `true`, marks non-walkable spans as walkable if their maximum is within agent_max_climb of a walkable neighbor.

---

[bool](class_bool.md#class-bool) **filter_walkable_low_height_spans** = `false`

-  **set_filter_walkable_low_height_spans**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_filter_walkable_low_height_spans**()

If `true`, marks walkable spans as not walkable if the clearance above the span is less than agent_height.

---

[int](class_int.md#class-int) **geometry_collision_mask** = `4294967295`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers to scan for static colliders.

Only used when geometry_parsed_geometry_type is PARSED_GEOMETRY_STATIC_COLLIDERS or PARSED_GEOMETRY_BOTH.

---

ParsedGeometryType **geometry_parsed_geometry_type** = `2`

-  **set_parsed_geometry_type**(value: ParsedGeometryType)
- ParsedGeometryType **get_parsed_geometry_type**()

Determines which type of nodes will be parsed as geometry.

---

SourceGeometryMode **geometry_source_geometry_mode** = `0`

-  **set_source_geometry_mode**(value: SourceGeometryMode)
- SourceGeometryMode **get_source_geometry_mode**()

The source of the geometry used when baking.

---

[StringName](class_stringname.md#class-stringname) **geometry_source_group_name** = `&"navigation_mesh_source_group"`

-  **set_source_group_name**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_source_group_name**()

The name of the group to scan for geometry.

Only used when geometry_source_geometry_mode is SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN or SOURCE_GEOMETRY_GROUPS_EXPLICIT.

---

[float](class_float.md#class-float) **region_merge_size** = `20.0`

-  **set_region_merge_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_region_merge_size**()

Any regions with a size smaller than this will be merged with larger regions if possible.

**Note:** This value will be squared to calculate the number of cells. For example, a value of 20 will set the number of cells to 400.

---

[float](class_float.md#class-float) **region_min_size** = `2.0`

-  **set_region_min_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_region_min_size**()

The minimum size of a region for it to be created.

**Note:** This value will be squared to calculate the minimum number of cells allowed to form isolated island areas. For example, a value of 8 will set the number of cells to 64.

---

SamplePartitionType **sample_partition_type** = `0`

-  **set_sample_partition_type**(value: SamplePartitionType)
- SamplePartitionType **get_sample_partition_type**()

Partitioning algorithm for creating the navigation mesh polys.

---

[float](class_float.md#class-float) **vertices_per_polygon** = `6.0`

-  **set_vertices_per_polygon**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_vertices_per_polygon**()

The maximum number of vertices allowed for polygons generated during the contour to polygon conversion process.

---

## Method Descriptions

 **add_polygon**(polygon: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Adds a polygon using the indices of the vertices you get when calling get_vertices().

---

 **clear**()

Clears the internal arrays for vertices and polygon indices.

---

 **clear_polygons**()

Clears the array of polygons, but it doesn't clear the array of vertices.

---

 **create_from_mesh**(mesh: [Mesh](class_mesh.md#class-mesh))

Initializes the navigation mesh by setting the vertices and indices according to a [Mesh](class_mesh.md#class-mesh).

**Note:** The given `mesh` must be of type [Mesh.PRIMITIVE_TRIANGLES](class_mesh.md#class-mesh-constant-primitive-triangles) and have an index array.

---

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the geometry_collision_mask is enabled, given a `layer_number` between 1 and 32.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_polygon**(idx: [int](class_int.md#class-int))

Returns a [PackedInt32Array](class_packedint32array.md#class-packedint32array) containing the indices of the vertices of a created polygon.

---

[int](class_int.md#class-int) **get_polygon_count**()

Returns the number of polygons in the navigation mesh.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_vertices**()

Returns a [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) containing all the vertices being used to create the polygons.

---

 **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the geometry_collision_mask, given a `layer_number` between 1 and 32.

---

 **set_vertices**(vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))

Sets the vertices that can be then indexed to create polygons with the add_polygon() method.
