# TileSet

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Tile library for tilemaps.

## Description

A TileSet is a library of tiles for a [TileMapLayer](class_tilemaplayer.md#class-tilemaplayer). A TileSet handles a list of [TileSetSource](class_tilesetsource.md#class-tilesetsource), each of them storing a set of tiles.

Tiles can either be from a [TileSetAtlasSource](class_tilesetatlassource.md#class-tilesetatlassource), which renders tiles out of a texture with support for physics, navigation, etc., or from a [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class-tilesetscenescollectionsource), which exposes scene-based tiles.

Tiles are referenced by using three IDs: their source ID, their atlas coordinates ID, and their alternative tile ID.

A TileSet can be configured so that its tiles expose more or fewer properties. To do so, the TileSet resources use property layers, which you can add or remove depending on your needs.

For example, adding a physics layer allows giving collision shapes to your tiles. Each layer has dedicated properties (physics layer and mask), so you may add several TileSet physics layers for each type of collision you need.

See the functions to add new layers for more information.

## Tutorials

- [Using Tilemaps](../tutorials/2d/using_tilemaps.md)
- [2D Platformer Demo](https://godotengine.org/asset-library/asset/2727)
- [2D Isometric Demo](https://godotengine.org/asset-library/asset/2718)
- [2D Hexagonal Demo](https://godotengine.org/asset-library/asset/2717)
- [2D Grid-based Navigation with AStarGrid2D Demo](https://godotengine.org/asset-library/asset/2723)
- [2D Role Playing Game (RPG) Demo](https://godotengine.org/asset-library/asset/2729)
- [2D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2719)

## Properties

| TileLayout         | tile_layout           | `0`                |
|------------------------------------------------|--------------------------------------------------------------|--------------------|
| TileOffsetAxis | tile_offset_axis | `0`                |
| TileShape           | tile_shape             | `0`                |
| [Vector2i](class_vector2i.md#class-vector2i)   | tile_size               | `Vector2i(16, 16)` |
| [bool](class_bool.md#class-bool)               | uv_clipping           | `false`            |

## Methods

|                                                                     | add_custom_data_layer(to_position: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                     | add_navigation_layer(to_position: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                  |
|                                                                     | add_occlusion_layer(to_position: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                       | add_pattern(pattern: [TileMapPattern](class_tilemappattern.md#class-tilemappattern), index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                 |
|                                                                     | add_physics_layer(to_position: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                       | add_source(source: [TileSetSource](class_tilesetsource.md#class-tilesetsource), atlas_source_id_override: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                    |
|                                                                     | add_terrain(terrain_set: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                        |
|                                                                     | add_terrain_set(to_position: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                            |
|                                                                     | cleanup_invalid_tile_proxies()                                                                                                                                                                                                                                                                                                                 |
|                                                                     | clear_terrains(terrain_set: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                   |
|                                                                     | clear_tile_proxies()                                                                                                                                                                                                                                                                                                                                     |
| [Array](class_array.md#class-array)                                 | get_alternative_level_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int))                                                                                                                                                   |
| [Array](class_array.md#class-array)                                 | get_coords_level_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                       | get_custom_data_layer_by_name(layer_name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                              | get_custom_data_layer_name(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                           |
| [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type) | get_custom_data_layer_type(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                       | get_custom_data_layers_count()                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                    | get_navigation_layer_layer_value(layer_index: [int](class_int.md#class-int), layer_number: [int](class_int.md#class-int))                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                       | get_navigation_layer_layers(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                       | get_navigation_layers_count()                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                       | get_next_source_id()                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                       | get_occlusion_layer_light_mask(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                    | get_occlusion_layer_sdf_collision(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                       | get_occlusion_layers_count()                                                                                                                                                                                                                                                                                                                     |
| [TileMapPattern](class_tilemappattern.md#class-tilemappattern)      | get_pattern(index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                       | get_patterns_count()                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                       | get_physics_layer_collision_layer(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                       | get_physics_layer_collision_mask(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                 | get_physics_layer_collision_priority(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                       |
| [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial)   | get_physics_layer_physics_material(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                       | get_physics_layers_count()                                                                                                                                                                                                                                                                                                                         |
| [TileSetSource](class_tilesetsource.md#class-tilesetsource)         | get_source(source_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                       | get_source_count()                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                       | get_source_id(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                       | get_source_level_tile_proxy(source_from: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                         |
| [Color](class_color.md#class-color)                                 | get_terrain_color(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                               |
| [String](class_string.md#class-string)                              | get_terrain_name(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                 |
| TerrainMode                            | get_terrain_set_mode(terrain_set: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                       | get_terrain_sets_count()                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                       | get_terrains_count(terrain_set: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                    | has_alternative_level_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int))                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                    | has_coords_level_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                    | has_custom_data_layer_by_name(layer_name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                    | has_source(source_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                    | has_source_level_tile_proxy(source_from: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                         |
| [Array](class_array.md#class-array)                                 | map_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int))                                                                                                                                                                                       |
|                                                                     | move_custom_data_layer(layer_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))                                                                                                                                                                                                                                       |
|                                                                     | move_navigation_layer(layer_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))                                                                                                                                                                                                                                         |
|                                                                     | move_occlusion_layer(layer_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))                                                                                                                                                                                                                                           |
|                                                                     | move_physics_layer(layer_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))                                                                                                                                                                                                                                               |
|                                                                     | move_terrain(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))                                                                                                                                                                                                             |
|                                                                     | move_terrain_set(terrain_set: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))                                                                                                                                                                                                                                                   |
|                                                                     | remove_alternative_level_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int))                                                                                                                                             |
|                                                                     | remove_coords_level_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                        |
|                                                                     | remove_custom_data_layer(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                               |
|                                                                     | remove_navigation_layer(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                 |
|                                                                     | remove_occlusion_layer(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                   |
|                                                                     | remove_pattern(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                         |
|                                                                     | remove_physics_layer(layer_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                       |
|                                                                     | remove_source(source_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                       |
|                                                                     | remove_source_level_tile_proxy(source_from: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                   |
|                                                                     | remove_terrain(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                     |
|                                                                     | remove_terrain_set(terrain_set: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                           |
|                                                                     | set_alternative_level_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int), source_to: [int](class_int.md#class-int), coords_to: [Vector2i](class_vector2i.md#class-vector2i), alternative_to: [int](class_int.md#class-int)) |
|                                                                     | set_coords_level_tile_proxy(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), source_to: [int](class_int.md#class-int), coords_to: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                           |
|                                                                     | set_custom_data_layer_name(layer_index: [int](class_int.md#class-int), layer_name: [String](class_string.md#class-string))                                                                                                                                                                                                                       |
|                                                                     | set_custom_data_layer_type(layer_index: [int](class_int.md#class-int), layer_type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type))                                                                                                                                                                                          |
|                                                                     | set_navigation_layer_layer_value(layer_index: [int](class_int.md#class-int), layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))                                                                                                                                                                         |
|                                                                     | set_navigation_layer_layers(layer_index: [int](class_int.md#class-int), layers: [int](class_int.md#class-int))                                                                                                                                                                                                                                  |
|                                                                     | set_occlusion_layer_light_mask(layer_index: [int](class_int.md#class-int), light_mask: [int](class_int.md#class-int))                                                                                                                                                                                                                        |
|                                                                     | set_occlusion_layer_sdf_collision(layer_index: [int](class_int.md#class-int), sdf_collision: [bool](class_bool.md#class-bool))                                                                                                                                                                                                            |
|                                                                     | set_physics_layer_collision_layer(layer_index: [int](class_int.md#class-int), layer: [int](class_int.md#class-int))                                                                                                                                                                                                                       |
|                                                                     | set_physics_layer_collision_mask(layer_index: [int](class_int.md#class-int), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                          |
|                                                                     | set_physics_layer_collision_priority(layer_index: [int](class_int.md#class-int), priority: [float](class_float.md#class-float))                                                                                                                                                                                                        |
|                                                                     | set_physics_layer_physics_material(layer_index: [int](class_int.md#class-int), physics_material: [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial))                                                                                                                                                                      |
|                                                                     | set_source_id(source_id: [int](class_int.md#class-int), new_source_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                         |
|                                                                     | set_source_level_tile_proxy(source_from: [int](class_int.md#class-int), source_to: [int](class_int.md#class-int))                                                                                                                                                                                                                               |
|                                                                     | set_terrain_color(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                                                                   |
|                                                                     | set_terrain_name(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                                                                                                                                                   |
|                                                                     | set_terrain_set_mode(terrain_set: [int](class_int.md#class-int), mode: TerrainMode)                                                                                                                                                                                                                                       |

---

## Enumerations

enum **TileShape**:

TileShape **TILE_SHAPE_SQUARE** = `0`

Rectangular tile shape.

TileShape **TILE_SHAPE_ISOMETRIC** = `1`

Diamond tile shape (for isometric look).

**Note:** Isometric **TileSet** works best if all sibling [TileMapLayer](class_tilemaplayer.md#class-tilemaplayer)s and their parent inheriting from [Node2D](class_node2d.md#class-node2d) have Y-sort enabled.

TileShape **TILE_SHAPE_HALF_OFFSET_SQUARE** = `2`

Rectangular tile shape with one row/column out of two offset by half a tile.

TileShape **TILE_SHAPE_HEXAGON** = `3`

Hexagonal tile shape.

---

enum **TileLayout**:

TileLayout **TILE_LAYOUT_STACKED** = `0`

Tile coordinates layout where both axis stay consistent with their respective local horizontal and vertical axis.

TileLayout **TILE_LAYOUT_STACKED_OFFSET** = `1`

Same as TILE_LAYOUT_STACKED, but the first half-offset is negative instead of positive.

TileLayout **TILE_LAYOUT_STAIRS_RIGHT** = `2`

Tile coordinates layout where the horizontal axis stay horizontal, and the vertical one goes down-right.

TileLayout **TILE_LAYOUT_STAIRS_DOWN** = `3`

Tile coordinates layout where the vertical axis stay vertical, and the horizontal one goes down-right.

TileLayout **TILE_LAYOUT_DIAMOND_RIGHT** = `4`

Tile coordinates layout where the horizontal axis goes up-right, and the vertical one goes down-right.

TileLayout **TILE_LAYOUT_DIAMOND_DOWN** = `5`

Tile coordinates layout where the horizontal axis goes down-right, and the vertical one goes down-left.

---

enum **TileOffsetAxis**:

TileOffsetAxis **TILE_OFFSET_AXIS_HORIZONTAL** = `0`

Horizontal half-offset.

TileOffsetAxis **TILE_OFFSET_AXIS_VERTICAL** = `1`

Vertical half-offset.

---

enum **CellNeighbor**:

CellNeighbor **CELL_NEIGHBOR_RIGHT_SIDE** = `0`

Neighbor on the right side.

CellNeighbor **CELL_NEIGHBOR_RIGHT_CORNER** = `1`

Neighbor in the right corner.

CellNeighbor **CELL_NEIGHBOR_BOTTOM_RIGHT_SIDE** = `2`

Neighbor on the bottom right side.

CellNeighbor **CELL_NEIGHBOR_BOTTOM_RIGHT_CORNER** = `3`

Neighbor in the bottom right corner.

CellNeighbor **CELL_NEIGHBOR_BOTTOM_SIDE** = `4`

Neighbor on the bottom side.

CellNeighbor **CELL_NEIGHBOR_BOTTOM_CORNER** = `5`

Neighbor in the bottom corner.

CellNeighbor **CELL_NEIGHBOR_BOTTOM_LEFT_SIDE** = `6`

Neighbor on the bottom left side.

CellNeighbor **CELL_NEIGHBOR_BOTTOM_LEFT_CORNER** = `7`

Neighbor in the bottom left corner.

CellNeighbor **CELL_NEIGHBOR_LEFT_SIDE** = `8`

Neighbor on the left side.

CellNeighbor **CELL_NEIGHBOR_LEFT_CORNER** = `9`

Neighbor in the left corner.

CellNeighbor **CELL_NEIGHBOR_TOP_LEFT_SIDE** = `10`

Neighbor on the top left side.

CellNeighbor **CELL_NEIGHBOR_TOP_LEFT_CORNER** = `11`

Neighbor in the top left corner.

CellNeighbor **CELL_NEIGHBOR_TOP_SIDE** = `12`

Neighbor on the top side.

CellNeighbor **CELL_NEIGHBOR_TOP_CORNER** = `13`

Neighbor in the top corner.

CellNeighbor **CELL_NEIGHBOR_TOP_RIGHT_SIDE** = `14`

Neighbor on the top right side.

CellNeighbor **CELL_NEIGHBOR_TOP_RIGHT_CORNER** = `15`

Neighbor in the top right corner.

---

enum **TerrainMode**:

TerrainMode **TERRAIN_MODE_MATCH_CORNERS_AND_SIDES** = `0`

Requires both corners and side to match with neighboring tiles' terrains.

TerrainMode **TERRAIN_MODE_MATCH_CORNERS** = `1`

Requires corners to match with neighboring tiles' terrains.

TerrainMode **TERRAIN_MODE_MATCH_SIDES** = `2`

Requires sides to match with neighboring tiles' terrains.

---

## Property Descriptions

TileLayout **tile_layout** = `0`

-  **set_tile_layout**(value: TileLayout)
- TileLayout **get_tile_layout**()

For all half-offset shapes (Isometric, Hexagonal and Half-Offset square), changes the way tiles are indexed in the [TileMapLayer](class_tilemaplayer.md#class-tilemaplayer) grid.

---

TileOffsetAxis **tile_offset_axis** = `0`

-  **set_tile_offset_axis**(value: TileOffsetAxis)
- TileOffsetAxis **get_tile_offset_axis**()

For all half-offset shapes (Isometric, Hexagonal and Half-Offset square), determines the offset axis.

---

TileShape **tile_shape** = `0`

-  **set_tile_shape**(value: TileShape)
- TileShape **get_tile_shape**()

The tile shape.

---

[Vector2i](class_vector2i.md#class-vector2i) **tile_size** = `Vector2i(16, 16)`

-  **set_tile_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_tile_size**()

The tile size, in pixels. For all tile shapes, this size corresponds to the encompassing rectangle of the tile shape. This is thus the minimal cell size required in an atlas.

---

[bool](class_bool.md#class-bool) **uv_clipping** = `false`

-  **set_uv_clipping**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_uv_clipping**()

Enables/Disable uv clipping when rendering the tiles.

---

## Method Descriptions

 **add_custom_data_layer**(to_position: [int](class_int.md#class-int) = -1)

Adds a custom data layer to the TileSet at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

Custom data layers allow assigning custom properties to atlas tiles.

---

 **add_navigation_layer**(to_position: [int](class_int.md#class-int) = -1)

Adds a navigation layer to the TileSet at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

Navigation layers allow assigning a navigable area to atlas tiles.

---

 **add_occlusion_layer**(to_position: [int](class_int.md#class-int) = -1)

Adds an occlusion layer to the TileSet at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

Occlusion layers allow assigning occlusion polygons to atlas tiles.

---

[int](class_int.md#class-int) **add_pattern**(pattern: [TileMapPattern](class_tilemappattern.md#class-tilemappattern), index: [int](class_int.md#class-int) = -1)

Adds a [TileMapPattern](class_tilemappattern.md#class-tilemappattern) to be stored in the TileSet resource. If provided, insert it at the given `index`.

---

 **add_physics_layer**(to_position: [int](class_int.md#class-int) = -1)

Adds a physics layer to the TileSet at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

Physics layers allow assigning collision polygons to atlas tiles.

---

[int](class_int.md#class-int) **add_source**(source: [TileSetSource](class_tilesetsource.md#class-tilesetsource), atlas_source_id_override: [int](class_int.md#class-int) = -1)

Adds a [TileSetSource](class_tilesetsource.md#class-tilesetsource) to the TileSet. If `atlas_source_id_override` is not -1, also set its source ID. Otherwise, a unique identifier is automatically generated.

The function returns the added source ID or -1 if the source could not be added.

**Warning:** A source cannot belong to two TileSets at the same time. If the added source was attached to another **TileSet**, it will be removed from that one.

---

 **add_terrain**(terrain_set: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int) = -1)

Adds a new terrain to the given terrain set `terrain_set` at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

---

 **add_terrain_set**(to_position: [int](class_int.md#class-int) = -1)

Adds a new terrain set at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

---

 **cleanup_invalid_tile_proxies**()

Clears tile proxies pointing to invalid tiles.

---

 **clear_terrains**(terrain_set: [int](class_int.md#class-int))

Clears all terrain properties for the given terrain set.

---

 **clear_tile_proxies**()

Clears all tile proxies.

---

[Array](class_array.md#class-array) **get_alternative_level_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int))

Returns the alternative-level proxy for the given identifiers. The returned array contains the three proxie's target identifiers (source ID, atlas coords ID and alternative tile ID).

If the TileSet has no proxy for the given identifiers, returns an empty Array.

---

[Array](class_array.md#class-array) **get_coords_level_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i))

Returns the coordinate-level proxy for the given identifiers. The returned array contains the two target identifiers of the proxy (source ID and atlas coordinates ID).

If the TileSet has no proxy for the given identifiers, returns an empty Array.

---

[int](class_int.md#class-int) **get_custom_data_layer_by_name**(layer_name: [String](class_string.md#class-string))

Returns the index of the custom data layer identified by the given name.

---

[String](class_string.md#class-string) **get_custom_data_layer_name**(layer_index: [int](class_int.md#class-int))

Returns the name of the custom data layer identified by the given index.

---

[Variant.Type](class_@globalscope.md#enum-globalscope-variant-type) **get_custom_data_layer_type**(layer_index: [int](class_int.md#class-int))

Returns the type of the custom data layer identified by the given index.

---

[int](class_int.md#class-int) **get_custom_data_layers_count**()

Returns the custom data layers count.

---

[bool](class_bool.md#class-bool) **get_navigation_layer_layer_value**(layer_index: [int](class_int.md#class-int), layer_number: [int](class_int.md#class-int))

Returns whether or not the specified navigation layer of the TileSet navigation data layer identified by the given `layer_index` is enabled, given a navigation_layers `layer_number` between 1 and 32.

---

[int](class_int.md#class-int) **get_navigation_layer_layers**(layer_index: [int](class_int.md#class-int))

Returns the navigation layers (as in the Navigation server) of the given TileSet navigation layer.

---

[int](class_int.md#class-int) **get_navigation_layers_count**()

Returns the navigation layers count.

---

[int](class_int.md#class-int) **get_next_source_id**()

Returns a new unused source ID. This generated ID is the same that a call to add_source() would return.

---

[int](class_int.md#class-int) **get_occlusion_layer_light_mask**(layer_index: [int](class_int.md#class-int))

Returns the light mask of the occlusion layer.

---

[bool](class_bool.md#class-bool) **get_occlusion_layer_sdf_collision**(layer_index: [int](class_int.md#class-int))

Returns if the occluders from this layer use `sdf_collision`.

---

[int](class_int.md#class-int) **get_occlusion_layers_count**()

Returns the occlusion layers count.

---

[TileMapPattern](class_tilemappattern.md#class-tilemappattern) **get_pattern**(index: [int](class_int.md#class-int) = -1)

Returns the [TileMapPattern](class_tilemappattern.md#class-tilemappattern) at the given `index`.

---

[int](class_int.md#class-int) **get_patterns_count**()

Returns the number of [TileMapPattern](class_tilemappattern.md#class-tilemappattern) this tile set handles.

---

[int](class_int.md#class-int) **get_physics_layer_collision_layer**(layer_index: [int](class_int.md#class-int))

Returns the collision layer (as in the physics server) bodies on the given TileSet's physics layer are in.

---

[int](class_int.md#class-int) **get_physics_layer_collision_mask**(layer_index: [int](class_int.md#class-int))

Returns the collision mask of bodies on the given TileSet's physics layer.

---

[float](class_float.md#class-float) **get_physics_layer_collision_priority**(layer_index: [int](class_int.md#class-int))

Returns the collision priority of bodies on the given TileSet's physics layer.

---

[PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial) **get_physics_layer_physics_material**(layer_index: [int](class_int.md#class-int))

Returns the physics material of bodies on the given TileSet's physics layer.

---

[int](class_int.md#class-int) **get_physics_layers_count**()

Returns the physics layers count.

---

[TileSetSource](class_tilesetsource.md#class-tilesetsource) **get_source**(source_id: [int](class_int.md#class-int))

Returns the [TileSetSource](class_tilesetsource.md#class-tilesetsource) with ID `source_id`.

---

[int](class_int.md#class-int) **get_source_count**()

Returns the number of [TileSetSource](class_tilesetsource.md#class-tilesetsource) in this TileSet.

---

[int](class_int.md#class-int) **get_source_id**(index: [int](class_int.md#class-int))

Returns the source ID for source with index `index`.

---

[int](class_int.md#class-int) **get_source_level_tile_proxy**(source_from: [int](class_int.md#class-int))

Returns the source-level proxy for the given source identifier.

If the TileSet has no proxy for the given identifier, returns -1.

---

[Color](class_color.md#class-color) **get_terrain_color**(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int))

Returns a terrain's color.

---

[String](class_string.md#class-string) **get_terrain_name**(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int))

Returns a terrain's name.

---

TerrainMode **get_terrain_set_mode**(terrain_set: [int](class_int.md#class-int))

Returns a terrain set mode.

---

[int](class_int.md#class-int) **get_terrain_sets_count**()

Returns the terrain sets count.

---

[int](class_int.md#class-int) **get_terrains_count**(terrain_set: [int](class_int.md#class-int))

Returns the number of terrains in the given terrain set.

---

[bool](class_bool.md#class-bool) **has_alternative_level_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int))

Returns if there is an alternative-level proxy for the given identifiers.

---

[bool](class_bool.md#class-bool) **has_coords_level_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i))

Returns if there is a coodinates-level proxy for the given identifiers.

---

[bool](class_bool.md#class-bool) **has_custom_data_layer_by_name**(layer_name: [String](class_string.md#class-string))

Returns if there is a custom data layer named `layer_name`.

---

[bool](class_bool.md#class-bool) **has_source**(source_id: [int](class_int.md#class-int))

Returns if this TileSet has a source for the given source ID.

---

[bool](class_bool.md#class-bool) **has_source_level_tile_proxy**(source_from: [int](class_int.md#class-int))

Returns if there is a source-level proxy for the given source ID.

---

[Array](class_array.md#class-array) **map_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int))

According to the configured proxies, maps the provided identifiers to a new set of identifiers. The source ID, atlas coordinates ID and alternative tile ID are returned as a 3 elements Array.

This function first look for matching alternative-level proxies, then coordinates-level proxies, then source-level proxies.

If no proxy corresponding to provided identifiers are found, returns the same values the ones used as arguments.

---

 **move_custom_data_layer**(layer_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))

Moves the custom data layer at index `layer_index` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

 **move_navigation_layer**(layer_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))

Moves the navigation layer at index `layer_index` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

 **move_occlusion_layer**(layer_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))

Moves the occlusion layer at index `layer_index` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

 **move_physics_layer**(layer_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))

Moves the physics layer at index `layer_index` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

 **move_terrain**(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))

Moves the terrain at index `terrain_index` for terrain set `terrain_set` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

 **move_terrain_set**(terrain_set: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))

Moves the terrain set at index `terrain_set` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

 **remove_alternative_level_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int))

Removes an alternative-level proxy for the given identifiers.

---

 **remove_coords_level_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i))

Removes a coordinates-level proxy for the given identifiers.

---

 **remove_custom_data_layer**(layer_index: [int](class_int.md#class-int))

Removes the custom data layer at index `layer_index`. Also updates the atlas tiles accordingly.

---

 **remove_navigation_layer**(layer_index: [int](class_int.md#class-int))

Removes the navigation layer at index `layer_index`. Also updates the atlas tiles accordingly.

---

 **remove_occlusion_layer**(layer_index: [int](class_int.md#class-int))

Removes the occlusion layer at index `layer_index`. Also updates the atlas tiles accordingly.

---

 **remove_pattern**(index: [int](class_int.md#class-int))

Remove the [TileMapPattern](class_tilemappattern.md#class-tilemappattern) at the given index.

---

 **remove_physics_layer**(layer_index: [int](class_int.md#class-int))

Removes the physics layer at index `layer_index`. Also updates the atlas tiles accordingly.

---

 **remove_source**(source_id: [int](class_int.md#class-int))

Removes the source with the given source ID.

---

 **remove_source_level_tile_proxy**(source_from: [int](class_int.md#class-int))

Removes a source-level tile proxy.

---

 **remove_terrain**(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int))

Removes the terrain at index `terrain_index` in the given terrain set `terrain_set`. Also updates the atlas tiles accordingly.

---

 **remove_terrain_set**(terrain_set: [int](class_int.md#class-int))

Removes the terrain set at index `terrain_set`. Also updates the atlas tiles accordingly.

---

 **set_alternative_level_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), alternative_from: [int](class_int.md#class-int), source_to: [int](class_int.md#class-int), coords_to: [Vector2i](class_vector2i.md#class-vector2i), alternative_to: [int](class_int.md#class-int))

Create an alternative-level proxy for the given identifiers. A proxy will map set of tile identifiers to another set of identifiers.

Proxied tiles can be automatically replaced in TileMapLayer nodes using the editor.

---

 **set_coords_level_tile_proxy**(source_from: [int](class_int.md#class-int), coords_from: [Vector2i](class_vector2i.md#class-vector2i), source_to: [int](class_int.md#class-int), coords_to: [Vector2i](class_vector2i.md#class-vector2i))

Creates a coordinates-level proxy for the given identifiers. A proxy will map set of tile identifiers to another set of identifiers. The alternative tile ID is kept the same when using coordinates-level proxies.

Proxied tiles can be automatically replaced in TileMapLayer nodes using the editor.

---

 **set_custom_data_layer_name**(layer_index: [int](class_int.md#class-int), layer_name: [String](class_string.md#class-string))

Sets the name of the custom data layer identified by the given index. Names are identifiers of the layer therefore if the name is already taken it will fail and raise an error.

---

 **set_custom_data_layer_type**(layer_index: [int](class_int.md#class-int), layer_type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type))

Sets the type of the custom data layer identified by the given index.

---

 **set_navigation_layer_layer_value**(layer_index: [int](class_int.md#class-int), layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified navigation layer of the TileSet navigation data layer identified by the given `layer_index`, given a navigation_layers `layer_number` between 1 and 32.

---

 **set_navigation_layer_layers**(layer_index: [int](class_int.md#class-int), layers: [int](class_int.md#class-int))

Sets the navigation layers (as in the navigation server) for navigation regions in the given TileSet navigation layer.

---

 **set_occlusion_layer_light_mask**(layer_index: [int](class_int.md#class-int), light_mask: [int](class_int.md#class-int))

Sets the occlusion layer (as in the rendering server) for occluders in the given TileSet occlusion layer.

---

 **set_occlusion_layer_sdf_collision**(layer_index: [int](class_int.md#class-int), sdf_collision: [bool](class_bool.md#class-bool))

Enables or disables SDF collision for occluders in the given TileSet occlusion layer.

---

 **set_physics_layer_collision_layer**(layer_index: [int](class_int.md#class-int), layer: [int](class_int.md#class-int))

Sets the collision layer (as in the physics server) for bodies in the given TileSet physics layer.

---

 **set_physics_layer_collision_mask**(layer_index: [int](class_int.md#class-int), mask: [int](class_int.md#class-int))

Sets the collision mask for bodies in the given TileSet physics layer.

---

 **set_physics_layer_collision_priority**(layer_index: [int](class_int.md#class-int), priority: [float](class_float.md#class-float))

Sets the collision priority for bodies in the given TileSet physics layer.

---

 **set_physics_layer_physics_material**(layer_index: [int](class_int.md#class-int), physics_material: [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial))

Sets the physics material for bodies in the given TileSet physics layer.

---

 **set_source_id**(source_id: [int](class_int.md#class-int), new_source_id: [int](class_int.md#class-int))

Changes a source's ID.

---

 **set_source_level_tile_proxy**(source_from: [int](class_int.md#class-int), source_to: [int](class_int.md#class-int))

Creates a source-level proxy for the given source ID. A proxy will map set of tile identifiers to another set of identifiers. Both the atlas coordinates ID and the alternative tile ID are kept the same when using source-level proxies.

Proxied tiles can be automatically replaced in TileMapLayer nodes using the editor.

---

 **set_terrain_color**(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets a terrain's color. This color is used for identifying the different terrains in the TileSet editor.

---

 **set_terrain_name**(terrain_set: [int](class_int.md#class-int), terrain_index: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets a terrain's name.

---

 **set_terrain_set_mode**(terrain_set: [int](class_int.md#class-int), mode: TerrainMode)

Sets a terrain mode. Each mode determines which bits of a tile shape is used to match the neighboring tiles' terrains.
