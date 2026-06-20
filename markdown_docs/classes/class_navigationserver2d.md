# NavigationServer2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Object](class_object.md#class-object)

A server interface for low-level 2D navigation access.

## Description

NavigationServer2D is the server that handles navigation maps, regions and agents. It does not handle A\* navigation from [AStar2D](class_astar2d.md#class-astar2d) or [AStarGrid2D](class_astargrid2d.md#class-astargrid2d).

Maps are divided into regions, which are composed of navigation polygons. Together, they define the traversable areas in the 2D world.

**Note:** Most **NavigationServer2D** changes take effect after the next physics frame and not immediately. This includes all changes made to maps, regions or agents by navigation-related nodes in the scene tree or made through scripts.

For two regions to be connected to each other, they must share a similar edge. An edge is considered connected to another if both of its two vertices are at a distance less than `edge_connection_margin` to the respective other edge's vertex.

You may assign navigation layers to regions with region_set_navigation_layers(), which then can be checked upon when requesting a path with map_get_path(). This can be used to allow or deny certain areas for some objects.

To use the collision avoidance system, you may use agents. You can set an agent's target velocity, then the servers will emit a callback with a modified velocity.

**Note:** The collision avoidance system ignores regions. Using the modified velocity directly may move an agent outside of the traversable area. This is a limitation of the collision avoidance system, any more complex situation may require the use of the physics engine.

This server keeps tracks of any call and executes them during the sync phase. This means that you can request any change to the map, using any thread, without worrying.

## Tutorials

- [Using NavigationServer](../tutorials/navigation/navigation_using_navigationservers.md)
- [Navigation Polygon 2D Demo](https://godotengine.org/asset-library/asset/2722)

## Methods

| [RID](class_rid.md#class-rid)                                              | agent_create()                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                           | agent_get_avoidance_enabled(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                              | agent_get_avoidance_layers(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                              | agent_get_avoidance_mask(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                |
| [float](class_float.md#class-float)                                        | agent_get_avoidance_priority(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                        |
| [RID](class_rid.md#class-rid)                                              | agent_get_map(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                              | agent_get_max_neighbors(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                  |
| [float](class_float.md#class-float)                                        | agent_get_max_speed(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                          |
| [float](class_float.md#class-float)                                        | agent_get_neighbor_distance(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                           | agent_get_paused(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                                  | agent_get_position(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                            |
| [float](class_float.md#class-float)                                        | agent_get_radius(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                |
| [float](class_float.md#class-float)                                        | agent_get_time_horizon_agents(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)                                        | agent_get_time_horizon_obstacles(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                                  | agent_get_velocity(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                           | agent_has_avoidance_callback(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                           | agent_is_map_changed(agent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                        |
|                                                                            | agent_set_avoidance_callback(agent: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                |
|                                                                            | agent_set_avoidance_enabled(agent: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                               |
|                                                                            | agent_set_avoidance_layers(agent: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                     |
|                                                                            | agent_set_avoidance_mask(agent: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                           |
|                                                                            | agent_set_avoidance_priority(agent: [RID](class_rid.md#class-rid), priority: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                         |
|                                                                            | agent_set_map(agent: [RID](class_rid.md#class-rid), map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                  |
|                                                                            | agent_set_max_neighbors(agent: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                            |
|                                                                            | agent_set_max_speed(agent: [RID](class_rid.md#class-rid), max_speed: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                          |
|                                                                            | agent_set_neighbor_distance(agent: [RID](class_rid.md#class-rid), distance: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                           |
|                                                                            | agent_set_paused(agent: [RID](class_rid.md#class-rid), paused: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                      |
|                                                                            | agent_set_position(agent: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                       |
|                                                                            | agent_set_radius(agent: [RID](class_rid.md#class-rid), radius: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                   |
|                                                                            | agent_set_time_horizon_agents(agent: [RID](class_rid.md#class-rid), time_horizon: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                   |
|                                                                            | agent_set_time_horizon_obstacles(agent: [RID](class_rid.md#class-rid), time_horizon: [float](class_float.md#class-float))                                                                                                                                                                                                                                                             |
|                                                                            | agent_set_velocity(agent: [RID](class_rid.md#class-rid), velocity: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                       |
|                                                                            | agent_set_velocity_forced(agent: [RID](class_rid.md#class-rid), velocity: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                         |
|                                                                            | bake_from_source_geometry_data(navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon), source_geometry_data: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d), callback: [Callable](class_callable.md#class-callable) = Callable())                                      |
|                                                                            | bake_from_source_geometry_data_async(navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon), source_geometry_data: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d), callback: [Callable](class_callable.md#class-callable) = Callable())                          |
|                                                                            | free_rid(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                           | get_debug_enabled()                                                                                                                                                                                                                                                                                                                                                                                  |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]         | get_maps()                                                                                                                                                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                              | get_process_info(process_info: ProcessInfo)                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                           | is_baking_navigation_polygon(navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon))                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                              | link_create()                                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                           | link_get_enabled(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                 |
| [Vector2](class_vector2.md#class-vector2)                                  | link_get_end_position(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
| [float](class_float.md#class-float)                                        | link_get_enter_cost(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                              | link_get_iteration_id(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                              | link_get_map(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                              | link_get_navigation_layers(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                              | link_get_owner_id(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
| [Vector2](class_vector2.md#class-vector2)                                  | link_get_start_position(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [float](class_float.md#class-float)                                        | link_get_travel_cost(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                           | link_is_bidirectional(link: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
|                                                                            | link_set_bidirectional(link: [RID](class_rid.md#class-rid), bidirectional: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                    |
|                                                                            | link_set_enabled(link: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                      |
|                                                                            | link_set_end_position(link: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                  |
|                                                                            | link_set_enter_cost(link: [RID](class_rid.md#class-rid), enter_cost: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                          |
|                                                                            | link_set_map(link: [RID](class_rid.md#class-rid), map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                     |
|                                                                            | link_set_navigation_layers(link: [RID](class_rid.md#class-rid), navigation_layers: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                           |
|                                                                            | link_set_owner_id(link: [RID](class_rid.md#class-rid), owner_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                      |
|                                                                            | link_set_start_position(link: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                              |
|                                                                            | link_set_travel_cost(link: [RID](class_rid.md#class-rid), travel_cost: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                              | map_create()                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                            | map_force_update(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                  |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]         | map_get_agents(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)                                        | map_get_cell_size(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                                  | map_get_closest_point(map: [RID](class_rid.md#class-rid), to_point: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                              | map_get_closest_point_owner(map: [RID](class_rid.md#class-rid), to_point: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                       |
| [float](class_float.md#class-float)                                        | map_get_edge_connection_margin(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                              | map_get_iteration_id(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                          |
| [float](class_float.md#class-float)                                        | map_get_link_connection_radius(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                      |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]         | map_get_links(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                        | map_get_merge_rasterizer_cell_scale(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                            |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]         | map_get_obstacles(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | map_get_path(map: [RID](class_rid.md#class-rid), origin: [Vector2](class_vector2.md#class-vector2), destination: [Vector2](class_vector2.md#class-vector2), optimize: [bool](class_bool.md#class-bool), navigation_layers: [int](class_int.md#class-int) = 1)                                                                                                                                             |
| [Vector2](class_vector2.md#class-vector2)                                  | map_get_random_point(map: [RID](class_rid.md#class-rid), navigation_layers: [int](class_int.md#class-int), uniformly: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                           |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]         | map_get_regions(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                           | map_get_use_async_iterations(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                           | map_get_use_edge_connections(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                           | map_is_active(map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                        |
|                                                                            | map_set_active(map: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                            |
|                                                                            | map_set_cell_size(map: [RID](class_rid.md#class-rid), cell_size: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                |
|                                                                            | map_set_edge_connection_margin(map: [RID](class_rid.md#class-rid), margin: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                         |
|                                                                            | map_set_link_connection_radius(map: [RID](class_rid.md#class-rid), radius: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                         |
|                                                                            | map_set_merge_rasterizer_cell_scale(map: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                |
|                                                                            | map_set_use_async_iterations(map: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                               |
|                                                                            | map_set_use_edge_connections(map: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                              | obstacle_create()                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                           | obstacle_get_avoidance_enabled(obstacle: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                              | obstacle_get_avoidance_layers(obstacle: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                              | obstacle_get_map(obstacle: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                           | obstacle_get_paused(obstacle: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
| [Vector2](class_vector2.md#class-vector2)                                  | obstacle_get_position(obstacle: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [float](class_float.md#class-float)                                        | obstacle_get_radius(obstacle: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
| [Vector2](class_vector2.md#class-vector2)                                  | obstacle_get_velocity(obstacle: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | obstacle_get_vertices(obstacle: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
|                                                                            | obstacle_set_avoidance_enabled(obstacle: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                      |
|                                                                            | obstacle_set_avoidance_layers(obstacle: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                            |
|                                                                            | obstacle_set_map(obstacle: [RID](class_rid.md#class-rid), map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                         |
|                                                                            | obstacle_set_paused(obstacle: [RID](class_rid.md#class-rid), paused: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                             |
|                                                                            | obstacle_set_position(obstacle: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                              |
|                                                                            | obstacle_set_radius(obstacle: [RID](class_rid.md#class-rid), radius: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                          |
|                                                                            | obstacle_set_velocity(obstacle: [RID](class_rid.md#class-rid), velocity: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                              |
|                                                                            | obstacle_set_vertices(obstacle: [RID](class_rid.md#class-rid), vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))                                                                                                                                                                                                                                             |
|                                                                            | parse_source_geometry_data(navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon), source_geometry_data: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d), root_node: [Node](class_node.md#class-node), callback: [Callable](class_callable.md#class-callable) = Callable()) |
|                                                                            | query_path(parameters: [NavigationPathQueryParameters2D](class_navigationpathqueryparameters2d.md#class-navigationpathqueryparameters2d), result: [NavigationPathQueryResult2D](class_navigationpathqueryresult2d.md#class-navigationpathqueryresult2d), callback: [Callable](class_callable.md#class-callable) = Callable())                                                                               |
| [RID](class_rid.md#class-rid)                                              | region_create()                                                                                                                                                                                                                                                                                                                                                                                          |
| [Rect2](class_rect2.md#class-rect2)                                        | region_get_bounds(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                             |
| [Vector2](class_vector2.md#class-vector2)                                  | region_get_closest_point(region: [RID](class_rid.md#class-rid), to_point: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                          |
| [Vector2](class_vector2.md#class-vector2)                                  | region_get_connection_pathway_end(region: [RID](class_rid.md#class-rid), connection: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                  |
| [Vector2](class_vector2.md#class-vector2)                                  | region_get_connection_pathway_start(region: [RID](class_rid.md#class-rid), connection: [int](class_int.md#class-int))                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                              | region_get_connections_count(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                           | region_get_enabled(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                           |
| [float](class_float.md#class-float)                                        | region_get_enter_cost(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                              | region_get_iteration_id(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                              | region_get_map(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                              | region_get_navigation_layers(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                              | region_get_owner_id(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
| [Vector2](class_vector2.md#class-vector2)                                  | region_get_random_point(region: [RID](class_rid.md#class-rid), navigation_layers: [int](class_int.md#class-int), uniformly: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                  |
| [Transform2D](class_transform2d.md#class-transform2d)                      | region_get_transform(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
| [float](class_float.md#class-float)                                        | region_get_travel_cost(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                           | region_get_use_async_iterations(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                           | region_get_use_edge_connections(region: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                           | region_owns_point(region: [RID](class_rid.md#class-rid), point: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                           |
|                                                                            | region_set_enabled(region: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                |
|                                                                            | region_set_enter_cost(region: [RID](class_rid.md#class-rid), enter_cost: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                    |
|                                                                            | region_set_map(region: [RID](class_rid.md#class-rid), map: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                               |
|                                                                            | region_set_navigation_layers(region: [RID](class_rid.md#class-rid), navigation_layers: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                     |
|                                                                            | region_set_navigation_polygon(region: [RID](class_rid.md#class-rid), navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon))                                                                                                                                                                                                                        |
|                                                                            | region_set_owner_id(region: [RID](class_rid.md#class-rid), owner_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                |
|                                                                            | region_set_transform(region: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                     |
|                                                                            | region_set_travel_cost(region: [RID](class_rid.md#class-rid), travel_cost: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                 |
|                                                                            | region_set_use_async_iterations(region: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                      |
|                                                                            | region_set_use_edge_connections(region: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                      |
|                                                                            | set_active(active: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                        |
|                                                                            | set_debug_enabled(enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                         |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | simplify_path(path: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), epsilon: [float](class_float.md#class-float))                                                                                                                                                                                                                                                            |
| [RID](class_rid.md#class-rid)                                              | source_geometry_parser_create()                                                                                                                                                                                                                                                                                                                                                          |
|                                                                            | source_geometry_parser_set_callback(parser: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                 |

---

## Signals

**avoidance_debug_changed**()

Emitted when avoidance debug settings are changed. Only available in debug builds.

---

**map_changed**(map: [RID](class_rid.md#class-rid))

Emitted when a navigation map is updated, when a region moves or is modified.

---

**navigation_debug_changed**()

Emitted when navigation debug settings are changed. Only available in debug builds.

---

## Enumerations

enum **ProcessInfo**:

ProcessInfo **INFO_ACTIVE_MAPS** = `0`

Constant to get the number of active navigation maps.

ProcessInfo **INFO_REGION_COUNT** = `1`

Constant to get the number of active navigation regions.

ProcessInfo **INFO_AGENT_COUNT** = `2`

Constant to get the number of active navigation agents processing avoidance.

ProcessInfo **INFO_LINK_COUNT** = `3`

Constant to get the number of active navigation links.

ProcessInfo **INFO_POLYGON_COUNT** = `4`

Constant to get the number of navigation mesh polygons.

ProcessInfo **INFO_EDGE_COUNT** = `5`

Constant to get the number of navigation mesh polygon edges.

ProcessInfo **INFO_EDGE_MERGE_COUNT** = `6`

Constant to get the number of navigation mesh polygon edges that were merged due to edge key overlap.

ProcessInfo **INFO_EDGE_CONNECTION_COUNT** = `7`

Constant to get the number of navigation mesh polygon edges that are considered connected by edge proximity.

ProcessInfo **INFO_EDGE_FREE_COUNT** = `8`

Constant to get the number of navigation mesh polygon edges that could not be merged but may be still connected by edge proximity or with links.

ProcessInfo **INFO_OBSTACLE_COUNT** = `9`

Constant to get the number of active navigation obstacles.

---

## Method Descriptions

[RID](class_rid.md#class-rid) **agent_create**()

Creates the agent.

---

[bool](class_bool.md#class-bool) **agent_get_avoidance_enabled**(agent: [RID](class_rid.md#class-rid))

Return `true` if the specified `agent` uses avoidance.

---

[int](class_int.md#class-int) **agent_get_avoidance_layers**(agent: [RID](class_rid.md#class-rid))

Returns the `avoidance_layers` bitmask of the specified `agent`.

---

[int](class_int.md#class-int) **agent_get_avoidance_mask**(agent: [RID](class_rid.md#class-rid))

Returns the `avoidance_mask` bitmask of the specified `agent`.

---

[float](class_float.md#class-float) **agent_get_avoidance_priority**(agent: [RID](class_rid.md#class-rid))

Returns the `avoidance_priority` of the specified `agent`.

---

[RID](class_rid.md#class-rid) **agent_get_map**(agent: [RID](class_rid.md#class-rid))

Returns the navigation map [RID](class_rid.md#class-rid) the requested `agent` is currently assigned to.

---

[int](class_int.md#class-int) **agent_get_max_neighbors**(agent: [RID](class_rid.md#class-rid))

Returns the maximum number of other agents the specified `agent` takes into account in the navigation.

---

[float](class_float.md#class-float) **agent_get_max_speed**(agent: [RID](class_rid.md#class-rid))

Returns the maximum speed of the specified `agent`.

---

[float](class_float.md#class-float) **agent_get_neighbor_distance**(agent: [RID](class_rid.md#class-rid))

Returns the maximum distance to other agents the specified `agent` takes into account in the navigation.

---

[bool](class_bool.md#class-bool) **agent_get_paused**(agent: [RID](class_rid.md#class-rid))

Returns `true` if the specified `agent` is paused.

---

[Vector2](class_vector2.md#class-vector2) **agent_get_position**(agent: [RID](class_rid.md#class-rid))

Returns the position of the specified `agent` in world space.

---

[float](class_float.md#class-float) **agent_get_radius**(agent: [RID](class_rid.md#class-rid))

Returns the radius of the specified `agent`.

---

[float](class_float.md#class-float) **agent_get_time_horizon_agents**(agent: [RID](class_rid.md#class-rid))

Returns the minimal amount of time for which the specified `agent`'s velocities that are computed by the simulation are safe with respect to other agents.

---

[float](class_float.md#class-float) **agent_get_time_horizon_obstacles**(agent: [RID](class_rid.md#class-rid))

Returns the minimal amount of time for which the specified `agent`'s velocities that are computed by the simulation are safe with respect to static avoidance obstacles.

---

[Vector2](class_vector2.md#class-vector2) **agent_get_velocity**(agent: [RID](class_rid.md#class-rid))

Returns the velocity of the specified `agent`.

---

[bool](class_bool.md#class-bool) **agent_has_avoidance_callback**(agent: [RID](class_rid.md#class-rid))

Return `true` if the specified `agent` has an avoidance callback.

---

[bool](class_bool.md#class-bool) **agent_is_map_changed**(agent: [RID](class_rid.md#class-rid))

Returns `true` if the map got changed the previous frame.

---

 **agent_set_avoidance_callback**(agent: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))

Sets the callback [Callable](class_callable.md#class-callable) that gets called after each avoidance processing step for the `agent`. The calculated `safe_velocity` will be dispatched with a signal to the object just before the physics calculations.

**Note:** Created callbacks are always processed independently of the SceneTree state as long as the agent is on a navigation map and not freed. To disable the dispatch of a callback from an agent use agent_set_avoidance_callback() again with an empty [Callable](class_callable.md#class-callable).

---

 **agent_set_avoidance_enabled**(agent: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the specified `agent` uses avoidance.

---

 **agent_set_avoidance_layers**(agent: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))

Set the agent's `avoidance_layers` bitmask.

---

 **agent_set_avoidance_mask**(agent: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Set the agent's `avoidance_mask` bitmask.

---

 **agent_set_avoidance_priority**(agent: [RID](class_rid.md#class-rid), priority: [float](class_float.md#class-float))

Set the agent's `avoidance_priority` with a `priority` between 0.0 (lowest priority) to 1.0 (highest priority).

The specified `agent` does not adjust the velocity for other agents that would match the `avoidance_mask` but have a lower `avoidance_priority`. This in turn makes the other agents with lower priority adjust their velocities even more to avoid collision with this agent.

---

 **agent_set_map**(agent: [RID](class_rid.md#class-rid), map: [RID](class_rid.md#class-rid))

Puts the agent in the map.

---

 **agent_set_max_neighbors**(agent: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))

Sets the maximum number of other agents the agent takes into account in the navigation. The larger this number, the longer the running time of the simulation. If the number is too low, the simulation will not be safe.

---

 **agent_set_max_speed**(agent: [RID](class_rid.md#class-rid), max_speed: [float](class_float.md#class-float))

Sets the maximum speed of the agent. Must be positive.

---

 **agent_set_neighbor_distance**(agent: [RID](class_rid.md#class-rid), distance: [float](class_float.md#class-float))

Sets the maximum distance to other agents this agent takes into account in the navigation. The larger this number, the longer the running time of the simulation. If the number is too low, the simulation will not be safe.

---

 **agent_set_paused**(agent: [RID](class_rid.md#class-rid), paused: [bool](class_bool.md#class-bool))

If `paused` is `true` the specified `agent` will not be processed. For example, it will not calculate avoidance velocities or receive avoidance callbacks.

---

 **agent_set_position**(agent: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2))

Sets the position of the agent in world space.

---

 **agent_set_radius**(agent: [RID](class_rid.md#class-rid), radius: [float](class_float.md#class-float))

Sets the radius of the agent.

---

 **agent_set_time_horizon_agents**(agent: [RID](class_rid.md#class-rid), time_horizon: [float](class_float.md#class-float))

The minimal amount of time for which the agent's velocities that are computed by the simulation are safe with respect to other agents. The larger this number, the sooner this agent will respond to the presence of other agents, but the less freedom this agent has in choosing its velocities. A too high value will slow down agents movement considerably. Must be positive.

---

 **agent_set_time_horizon_obstacles**(agent: [RID](class_rid.md#class-rid), time_horizon: [float](class_float.md#class-float))

The minimal amount of time for which the agent's velocities that are computed by the simulation are safe with respect to static avoidance obstacles. The larger this number, the sooner this agent will respond to the presence of static avoidance obstacles, but the less freedom this agent has in choosing its velocities. A too high value will slow down agents movement considerably. Must be positive.

---

 **agent_set_velocity**(agent: [RID](class_rid.md#class-rid), velocity: [Vector2](class_vector2.md#class-vector2))

Sets `velocity` as the new wanted velocity for the specified `agent`. The avoidance simulation will try to fulfill this velocity if possible but will modify it to avoid collision with other agent's and obstacles. When an agent is teleported to a new position far away use agent_set_velocity_forced() instead to reset the internal velocity state.

---

 **agent_set_velocity_forced**(agent: [RID](class_rid.md#class-rid), velocity: [Vector2](class_vector2.md#class-vector2))

Replaces the internal velocity in the collision avoidance simulation with `velocity` for the specified `agent`. When an agent is teleported to a new position far away this function should be used in the same frame. If called frequently this function can get agents stuck.

---

 **bake_from_source_geometry_data**(navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon), source_geometry_data: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d), callback: [Callable](class_callable.md#class-callable) = Callable())

Bakes the provided `navigation_polygon` with the data from the provided `source_geometry_data`. After the process is finished the optional `callback` will be called.

---

 **bake_from_source_geometry_data_async**(navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon), source_geometry_data: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d), callback: [Callable](class_callable.md#class-callable) = Callable())

Bakes the provided `navigation_polygon` with the data from the provided `source_geometry_data` as an async task running on a background thread. After the process is finished the optional `callback` will be called.

---

 **free_rid**(rid: [RID](class_rid.md#class-rid))

Destroys the given RID.

---

[bool](class_bool.md#class-bool) **get_debug_enabled**()

Returns `true` when the NavigationServer has debug enabled.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_maps**()

Returns all created navigation map [RID](class_rid.md#class-rid)s on the NavigationServer. This returns both 2D and 3D created navigation maps as there is technically no distinction between them.

---

[int](class_int.md#class-int) **get_process_info**(process_info: ProcessInfo)

Returns information about the current state of the NavigationServer.

---

[bool](class_bool.md#class-bool) **is_baking_navigation_polygon**(navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon))

Returns `true` when the provided navigation polygon is being baked on a background thread.

---

[RID](class_rid.md#class-rid) **link_create**()

Create a new link between two positions on a map.

---

[bool](class_bool.md#class-bool) **link_get_enabled**(link: [RID](class_rid.md#class-rid))

Returns `true` if the specified `link` is enabled.

---

[Vector2](class_vector2.md#class-vector2) **link_get_end_position**(link: [RID](class_rid.md#class-rid))

Returns the ending position of this `link`.

---

[float](class_float.md#class-float) **link_get_enter_cost**(link: [RID](class_rid.md#class-rid))

Returns the enter cost of this `link`.

---

[int](class_int.md#class-int) **link_get_iteration_id**(link: [RID](class_rid.md#class-rid))

Returns the current iteration ID of the navigation link. Every time the navigation link changes and synchronizes, the iteration ID increases. An iteration ID of `0` means the navigation link has never synchronized.

**Note:** The iteration ID will wrap around to `1` after reaching its range limit.

---

[RID](class_rid.md#class-rid) **link_get_map**(link: [RID](class_rid.md#class-rid))

Returns the navigation map [RID](class_rid.md#class-rid) the requested `link` is currently assigned to.

---

[int](class_int.md#class-int) **link_get_navigation_layers**(link: [RID](class_rid.md#class-rid))

Returns the navigation layers for this `link`.

---

[int](class_int.md#class-int) **link_get_owner_id**(link: [RID](class_rid.md#class-rid))

Returns the `ObjectID` of the object which manages this link.

---

[Vector2](class_vector2.md#class-vector2) **link_get_start_position**(link: [RID](class_rid.md#class-rid))

Returns the starting position of this `link`.

---

[float](class_float.md#class-float) **link_get_travel_cost**(link: [RID](class_rid.md#class-rid))

Returns the travel cost of this `link`.

---

[bool](class_bool.md#class-bool) **link_is_bidirectional**(link: [RID](class_rid.md#class-rid))

Returns whether this `link` can be travelled in both directions.

---

 **link_set_bidirectional**(link: [RID](class_rid.md#class-rid), bidirectional: [bool](class_bool.md#class-bool))

Sets whether this `link` can be travelled in both directions.

---

 **link_set_enabled**(link: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the specified `link` will contribute to its current navigation map.

---

 **link_set_end_position**(link: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2))

Sets the exit position for the `link`.

---

 **link_set_enter_cost**(link: [RID](class_rid.md#class-rid), enter_cost: [float](class_float.md#class-float))

Sets the `enter_cost` for this `link`.

---

 **link_set_map**(link: [RID](class_rid.md#class-rid), map: [RID](class_rid.md#class-rid))

Sets the navigation map [RID](class_rid.md#class-rid) for the link.

---

 **link_set_navigation_layers**(link: [RID](class_rid.md#class-rid), navigation_layers: [int](class_int.md#class-int))

Set the links's navigation layers. This allows selecting links from a path request (when using map_get_path()).

---

 **link_set_owner_id**(link: [RID](class_rid.md#class-rid), owner_id: [int](class_int.md#class-int))

Set the `ObjectID` of the object which manages this link.

---

 **link_set_start_position**(link: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2))

Sets the entry position for this `link`.

---

 **link_set_travel_cost**(link: [RID](class_rid.md#class-rid), travel_cost: [float](class_float.md#class-float))

Sets the `travel_cost` for this `link`.

---

[RID](class_rid.md#class-rid) **map_create**()

Create a new map.

---

 **map_force_update**(map: [RID](class_rid.md#class-rid))

**Deprecated:** This method is no longer supported, as it is incompatible with asynchronous updates. It can only be used in a single-threaded context, at your own risk.

This function immediately forces synchronization of the specified navigation `map` [RID](class_rid.md#class-rid). By default navigation maps are only synchronized at the end of each physics frame. This function can be used to immediately (re)calculate all the navigation meshes and region connections of the navigation map. This makes it possible to query a navigation path for a changed map immediately and in the same frame (multiple times if needed).

Due to technical restrictions the current NavigationServer command queue will be flushed. This means all already queued update commands for this physics frame will be executed, even those intended for other maps, regions and agents not part of the specified map. The expensive computation of the navigation meshes and region connections of a map will only be done for the specified map. Other maps will receive the normal synchronization at the end of the physics frame. Should the specified map receive changes after the forced update it will update again as well when the other maps receive their update.

Avoidance processing and dispatch of the `safe_velocity` signals is unaffected by this function and continues to happen for all maps and agents at the end of the physics frame.

**Note:** With great power comes great responsibility. This function should only be used by users that really know what they are doing and have a good reason for it. Forcing an immediate update of a navigation map requires locking the NavigationServer and flushing the entire NavigationServer command queue. Not only can this severely impact the performance of a game but it can also introduce bugs if used inappropriately without much foresight.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **map_get_agents**(map: [RID](class_rid.md#class-rid))

Returns all navigation agents [RID](class_rid.md#class-rid)s that are currently assigned to the requested navigation `map`.

---

[float](class_float.md#class-float) **map_get_cell_size**(map: [RID](class_rid.md#class-rid))

Returns the map cell size used to rasterize the navigation mesh vertices.

---

[Vector2](class_vector2.md#class-vector2) **map_get_closest_point**(map: [RID](class_rid.md#class-rid), to_point: [Vector2](class_vector2.md#class-vector2))

Returns the navigation mesh surface point closest to the provided `to_point` on the navigation `map`.

---

[RID](class_rid.md#class-rid) **map_get_closest_point_owner**(map: [RID](class_rid.md#class-rid), to_point: [Vector2](class_vector2.md#class-vector2))

Returns the owner region RID for the navigation mesh surface point closest to the provided `to_point` on the navigation `map`.

---

[float](class_float.md#class-float) **map_get_edge_connection_margin**(map: [RID](class_rid.md#class-rid))

Returns the edge connection margin of the map. The edge connection margin is a distance used to connect two regions.

---

[int](class_int.md#class-int) **map_get_iteration_id**(map: [RID](class_rid.md#class-rid))

Returns the current iteration id of the navigation map. Every time the navigation map changes and synchronizes the iteration id increases. An iteration id of 0 means the navigation map has never synchronized.

**Note:** The iteration id will wrap back to 1 after reaching its range limit.

---

[float](class_float.md#class-float) **map_get_link_connection_radius**(map: [RID](class_rid.md#class-rid))

Returns the link connection radius of the map. This distance is the maximum range any link will search for navigation mesh polygons to connect to.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **map_get_links**(map: [RID](class_rid.md#class-rid))

Returns all navigation link [RID](class_rid.md#class-rid)s that are currently assigned to the requested navigation `map`.

---

[float](class_float.md#class-float) **map_get_merge_rasterizer_cell_scale**(map: [RID](class_rid.md#class-rid))

Returns map's internal merge rasterizer cell scale.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **map_get_obstacles**(map: [RID](class_rid.md#class-rid))

Returns all navigation obstacle [RID](class_rid.md#class-rid)s that are currently assigned to the requested navigation `map`.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **map_get_path**(map: [RID](class_rid.md#class-rid), origin: [Vector2](class_vector2.md#class-vector2), destination: [Vector2](class_vector2.md#class-vector2), optimize: [bool](class_bool.md#class-bool), navigation_layers: [int](class_int.md#class-int) = 1)

Returns the navigation path to reach the destination from the origin. `navigation_layers` is a bitmask of all region navigation layers that are allowed to be in the path.

---

[Vector2](class_vector2.md#class-vector2) **map_get_random_point**(map: [RID](class_rid.md#class-rid), navigation_layers: [int](class_int.md#class-int), uniformly: [bool](class_bool.md#class-bool))

Returns a random position picked from all map region polygons with matching `navigation_layers`.

If `uniformly` is `true`, all map regions, polygons, and faces are weighted by their surface area (slower).

If `uniformly` is `false`, just a random region and a random polygon are picked (faster).

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **map_get_regions**(map: [RID](class_rid.md#class-rid))

Returns all navigation regions [RID](class_rid.md#class-rid)s that are currently assigned to the requested navigation `map`.

---

[bool](class_bool.md#class-bool) **map_get_use_async_iterations**(map: [RID](class_rid.md#class-rid))

Returns `true` if the `map` synchronization uses an async process that runs on a background thread.

---

[bool](class_bool.md#class-bool) **map_get_use_edge_connections**(map: [RID](class_rid.md#class-rid))

Returns whether the navigation `map` allows navigation regions to use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

[bool](class_bool.md#class-bool) **map_is_active**(map: [RID](class_rid.md#class-rid))

Returns `true` if the map is active.

---

 **map_set_active**(map: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool))

Sets the map active.

---

 **map_set_cell_size**(map: [RID](class_rid.md#class-rid), cell_size: [float](class_float.md#class-float))

Sets the map cell size used to rasterize the navigation mesh vertices. Must match with the cell size of the used navigation meshes.

---

 **map_set_edge_connection_margin**(map: [RID](class_rid.md#class-rid), margin: [float](class_float.md#class-float))

Set the map edge connection margin used to weld the compatible region edges.

---

 **map_set_link_connection_radius**(map: [RID](class_rid.md#class-rid), radius: [float](class_float.md#class-float))

Set the map's link connection radius used to connect links to navigation polygons.

---

 **map_set_merge_rasterizer_cell_scale**(map: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))

Set the map's internal merge rasterizer cell scale used to control merging sensitivity.

---

 **map_set_use_async_iterations**(map: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true` the `map` synchronization uses an async process that runs on a background thread.

---

 **map_set_use_edge_connections**(map: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

Set the navigation `map` edge connection use. If `enabled` is `true`, the navigation map allows navigation regions to use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

[RID](class_rid.md#class-rid) **obstacle_create**()

Creates a new navigation obstacle.

---

[bool](class_bool.md#class-bool) **obstacle_get_avoidance_enabled**(obstacle: [RID](class_rid.md#class-rid))

Returns `true` if the provided `obstacle` has avoidance enabled.

---

[int](class_int.md#class-int) **obstacle_get_avoidance_layers**(obstacle: [RID](class_rid.md#class-rid))

Returns the `avoidance_layers` bitmask of the specified `obstacle`.

---

[RID](class_rid.md#class-rid) **obstacle_get_map**(obstacle: [RID](class_rid.md#class-rid))

Returns the navigation map [RID](class_rid.md#class-rid) the requested `obstacle` is currently assigned to.

---

[bool](class_bool.md#class-bool) **obstacle_get_paused**(obstacle: [RID](class_rid.md#class-rid))

Returns `true` if the specified `obstacle` is paused.

---

[Vector2](class_vector2.md#class-vector2) **obstacle_get_position**(obstacle: [RID](class_rid.md#class-rid))

Returns the position of the specified `obstacle` in world space.

---

[float](class_float.md#class-float) **obstacle_get_radius**(obstacle: [RID](class_rid.md#class-rid))

Returns the radius of the specified dynamic `obstacle`.

---

[Vector2](class_vector2.md#class-vector2) **obstacle_get_velocity**(obstacle: [RID](class_rid.md#class-rid))

Returns the velocity of the specified dynamic `obstacle`.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **obstacle_get_vertices**(obstacle: [RID](class_rid.md#class-rid))

Returns the outline vertices for the specified `obstacle`.

---

 **obstacle_set_avoidance_enabled**(obstacle: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the provided `obstacle` affects avoidance using agents.

---

 **obstacle_set_avoidance_layers**(obstacle: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))

Set the obstacles's `avoidance_layers` bitmask.

---

 **obstacle_set_map**(obstacle: [RID](class_rid.md#class-rid), map: [RID](class_rid.md#class-rid))

Sets the navigation map [RID](class_rid.md#class-rid) for the obstacle.

---

 **obstacle_set_paused**(obstacle: [RID](class_rid.md#class-rid), paused: [bool](class_bool.md#class-bool))

If `paused` is `true` the specified `obstacle` will not be processed. For example, it will no longer affect avoidance velocities.

---

 **obstacle_set_position**(obstacle: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2))

Sets the position of the obstacle in world space.

---

 **obstacle_set_radius**(obstacle: [RID](class_rid.md#class-rid), radius: [float](class_float.md#class-float))

Sets the radius of the dynamic obstacle.

---

 **obstacle_set_velocity**(obstacle: [RID](class_rid.md#class-rid), velocity: [Vector2](class_vector2.md#class-vector2))

Sets `velocity` of the dynamic `obstacle`. Allows other agents to better predict the movement of the dynamic obstacle. Only works in combination with the radius of the obstacle.

---

 **obstacle_set_vertices**(obstacle: [RID](class_rid.md#class-rid), vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))

Sets the outline vertices for the obstacle. If the vertices are winded in clockwise order agents will be pushed in by the obstacle, else they will be pushed out.

---

 **parse_source_geometry_data**(navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon), source_geometry_data: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d), root_node: [Node](class_node.md#class-node), callback: [Callable](class_callable.md#class-callable) = Callable())

Parses the [SceneTree](class_scenetree.md#class-scenetree) for source geometry according to the properties of `navigation_polygon`. Updates the provided `source_geometry_data` resource with the resulting data. The resource can then be used to bake a navigation mesh with bake_from_source_geometry_data(). After the process is finished the optional `callback` will be called.

**Note:** This function needs to run on the main thread or with a deferred call as the SceneTree is not thread-safe.

**Performance:** While convenient, reading data arrays from [Mesh](class_mesh.md#class-mesh) resources can affect the frame rate negatively. The data needs to be received from the GPU, stalling the [RenderingServer](class_renderingserver.md#class-renderingserver) in the process. For performance prefer the use of e.g. collision shapes or creating the data arrays entirely in code.

---

 **query_path**(parameters: [NavigationPathQueryParameters2D](class_navigationpathqueryparameters2d.md#class-navigationpathqueryparameters2d), result: [NavigationPathQueryResult2D](class_navigationpathqueryresult2d.md#class-navigationpathqueryresult2d), callback: [Callable](class_callable.md#class-callable) = Callable())

Queries a path in a given navigation map. Start and target position and other parameters are defined through [NavigationPathQueryParameters2D](class_navigationpathqueryparameters2d.md#class-navigationpathqueryparameters2d). Updates the provided [NavigationPathQueryResult2D](class_navigationpathqueryresult2d.md#class-navigationpathqueryresult2d) result object with the path among other results requested by the query. After the process is finished the optional `callback` will be called.

---

[RID](class_rid.md#class-rid) **region_create**()

Creates a new region.

---

[Rect2](class_rect2.md#class-rect2) **region_get_bounds**(region: [RID](class_rid.md#class-rid))

Returns the axis-aligned rectangle for the `region`'s transformed navigation mesh.

---

[Vector2](class_vector2.md#class-vector2) **region_get_closest_point**(region: [RID](class_rid.md#class-rid), to_point: [Vector2](class_vector2.md#class-vector2))

Returns the navigation mesh surface point closest to the provided `to_point` on the navigation `region`.

---

[Vector2](class_vector2.md#class-vector2) **region_get_connection_pathway_end**(region: [RID](class_rid.md#class-rid), connection: [int](class_int.md#class-int))

Returns the ending point of a connection door. `connection` is an index between 0 and the return value of region_get_connections_count().

---

[Vector2](class_vector2.md#class-vector2) **region_get_connection_pathway_start**(region: [RID](class_rid.md#class-rid), connection: [int](class_int.md#class-int))

Returns the starting point of a connection door. `connection` is an index between 0 and the return value of region_get_connections_count().

---

[int](class_int.md#class-int) **region_get_connections_count**(region: [RID](class_rid.md#class-rid))

Returns how many connections this `region` has with other regions in the map.

---

[bool](class_bool.md#class-bool) **region_get_enabled**(region: [RID](class_rid.md#class-rid))

Returns `true` if the specified `region` is enabled.

---

[float](class_float.md#class-float) **region_get_enter_cost**(region: [RID](class_rid.md#class-rid))

Returns the enter cost of this `region`.

---

[int](class_int.md#class-int) **region_get_iteration_id**(region: [RID](class_rid.md#class-rid))

Returns the current iteration ID of the navigation region. Every time the navigation region changes and synchronizes, the iteration ID increases. An iteration ID of `0` means the navigation region has never synchronized.

**Note:** The iteration ID will wrap around to `1` after reaching its range limit.

---

[RID](class_rid.md#class-rid) **region_get_map**(region: [RID](class_rid.md#class-rid))

Returns the navigation map [RID](class_rid.md#class-rid) the requested `region` is currently assigned to.

---

[int](class_int.md#class-int) **region_get_navigation_layers**(region: [RID](class_rid.md#class-rid))

Returns the region's navigation layers.

---

[int](class_int.md#class-int) **region_get_owner_id**(region: [RID](class_rid.md#class-rid))

Returns the `ObjectID` of the object which manages this region.

---

[Vector2](class_vector2.md#class-vector2) **region_get_random_point**(region: [RID](class_rid.md#class-rid), navigation_layers: [int](class_int.md#class-int), uniformly: [bool](class_bool.md#class-bool))

Returns a random position picked from all region polygons with matching `navigation_layers`.

If `uniformly` is `true`, all region polygons and faces are weighted by their surface area (slower).

If `uniformly` is `false`, just a random polygon and face is picked (faster).

---

[Transform2D](class_transform2d.md#class-transform2d) **region_get_transform**(region: [RID](class_rid.md#class-rid))

Returns the global transformation of this `region`.

---

[float](class_float.md#class-float) **region_get_travel_cost**(region: [RID](class_rid.md#class-rid))

Returns the travel cost of this `region`.

---

[bool](class_bool.md#class-bool) **region_get_use_async_iterations**(region: [RID](class_rid.md#class-rid))

Returns `true` if the `region` uses an async synchronization process that runs on a background thread.

---

[bool](class_bool.md#class-bool) **region_get_use_edge_connections**(region: [RID](class_rid.md#class-rid))

Returns whether the navigation `region` is set to use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

[bool](class_bool.md#class-bool) **region_owns_point**(region: [RID](class_rid.md#class-rid), point: [Vector2](class_vector2.md#class-vector2))

Returns `true` if the provided `point` in world space is currently owned by the provided navigation `region`. Owned in this context means that one of the region's navigation mesh polygon faces has a possible position at the closest distance to this point compared to all other navigation meshes from other navigation regions that are also registered on the navigation map of the provided region.

If multiple navigation meshes have positions at equal distance the navigation region whose polygons are processed first wins the ownership. Polygons are processed in the same order that navigation regions were registered on the NavigationServer.

**Note:** If navigation meshes from different navigation regions overlap (which should be avoided in general) the result might not be what is expected.

---

 **region_set_enabled**(region: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true` the specified `region` will contribute to its current navigation map.

---

 **region_set_enter_cost**(region: [RID](class_rid.md#class-rid), enter_cost: [float](class_float.md#class-float))

Sets the `enter_cost` for this `region`.

---

 **region_set_map**(region: [RID](class_rid.md#class-rid), map: [RID](class_rid.md#class-rid))

Sets the map for the region.

---

 **region_set_navigation_layers**(region: [RID](class_rid.md#class-rid), navigation_layers: [int](class_int.md#class-int))

Set the region's navigation layers. This allows selecting regions from a path request (when using map_get_path()).

---

 **region_set_navigation_polygon**(region: [RID](class_rid.md#class-rid), navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon))

Sets the `navigation_polygon` for the region.

---

 **region_set_owner_id**(region: [RID](class_rid.md#class-rid), owner_id: [int](class_int.md#class-int))

Set the `ObjectID` of the object which manages this region.

---

 **region_set_transform**(region: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the global transformation for the region.

---

 **region_set_travel_cost**(region: [RID](class_rid.md#class-rid), travel_cost: [float](class_float.md#class-float))

Sets the `travel_cost` for this `region`.

---

 **region_set_use_async_iterations**(region: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true` the `region` uses an async synchronization process that runs on a background thread.

---

 **region_set_use_edge_connections**(region: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the navigation `region` will use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

 **set_active**(active: [bool](class_bool.md#class-bool))

Control activation of this server.

---

 **set_debug_enabled**(enabled: [bool](class_bool.md#class-bool))

If `true` enables debug mode on the NavigationServer.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **simplify_path**(path: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), epsilon: [float](class_float.md#class-float))

Returns a simplified version of `path` with less critical path points removed. The simplification amount is in worlds units and controlled by `epsilon`. The simplification uses a variant of Ramer-Douglas-Peucker algorithm for curve point decimation.

Path simplification can be helpful to mitigate various path following issues that can arise with certain agent types and script behaviors. E.g. "steering" agents or avoidance in "open fields".

---

[RID](class_rid.md#class-rid) **source_geometry_parser_create**()

Creates a new source geometry parser. If a [Callable](class_callable.md#class-callable) is set for the parser with source_geometry_parser_set_callback() the callback will be called for every single node that gets parsed whenever parse_source_geometry_data() is used.

---

 **source_geometry_parser_set_callback**(parser: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))

Sets the `callback` [Callable](class_callable.md#class-callable) for the specific source geometry `parser`. The [Callable](class_callable.md#class-callable) will receive a call with the following parameters:

- `navigation_mesh` - The [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon) reference used to define the parse settings. Do NOT edit or add directly to the navigation mesh.
- `source_geometry_data` - The [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class-navigationmeshsourcegeometrydata2d) reference. Add custom source geometry for navigation mesh baking to this object.
- `node` - The [Node](class_node.md#class-node) that is parsed.
