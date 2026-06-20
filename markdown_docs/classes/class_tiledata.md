# TileData

**Inherits:** [Object](class_object.md#class-object)

Settings for a single tile in a [TileSet](class_tileset.md#class-tileset).

## Description

**TileData** object represents a single tile in a [TileSet](class_tileset.md#class-tileset). It is usually edited using the tileset editor, but it can be modified at runtime using [TileMapLayer._tile_data_runtime_update()](class_tilemaplayer.md#class-tilemaplayer-private-method-tile-data-runtime-update).

## Properties

| [bool](class_bool.md#class-bool)             | flip_h                 | `false`             |
|----------------------------------------------|-----------------------------------------------------------|---------------------|
| [bool](class_bool.md#class-bool)             | flip_v                 | `false`             |
| [Material](class_material.md#class-material) | material             |                     |
| [Color](class_color.md#class-color)          | modulate             | `Color(1, 1, 1, 1)` |
| [float](class_float.md#class-float)          | probability       | `1.0`               |
| [int](class_int.md#class-int)                | terrain               | `-1`                |
| [int](class_int.md#class-int)                | terrain_set       | `-1`                |
| [Vector2i](class_vector2i.md#class-vector2i) | texture_origin | `Vector2i(0, 0)`    |
| [bool](class_bool.md#class-bool)             | transpose           | `false`             |
| [int](class_int.md#class-int)                | y_sort_origin   | `0`                 |
| [int](class_int.md#class-int)                | z_index               | `0`                 |

## Methods

|                                                                            | add_collision_polygon(layer_id: [int](class_int.md#class-int))                                                                                                                                                                                                      |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                            | add_occluder_polygon(layer_id: [int](class_int.md#class-int))                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                        | get_collision_polygon_one_way_margin(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))                                                                                                                          |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | get_collision_polygon_points(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))                                                                                                                                          |
| [int](class_int.md#class-int)                                              | get_collision_polygons_count(layer_id: [int](class_int.md#class-int))                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                        | get_constant_angular_velocity(layer_id: [int](class_int.md#class-int))                                                                                                                                                                                      |
| [Vector2](class_vector2.md#class-vector2)                                  | get_constant_linear_velocity(layer_id: [int](class_int.md#class-int))                                                                                                                                                                                        |
| [Variant](class_variant.md#class-variant)                                  | get_custom_data(layer_name: [String](class_string.md#class-string))                                                                                                                                                                                                       |
| [Variant](class_variant.md#class-variant)                                  | get_custom_data_by_layer_id(layer_id: [int](class_int.md#class-int))                                                                                                                                                                                          |
| [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon)    | get_navigation_polygon(layer_id: [int](class_int.md#class-int), flip_h: [bool](class_bool.md#class-bool) = false, flip_v: [bool](class_bool.md#class-bool) = false, transpose: [bool](class_bool.md#class-bool) = false)                                           |
| [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d)    | get_occluder(layer_id: [int](class_int.md#class-int), flip_h: [bool](class_bool.md#class-bool) = false, flip_v: [bool](class_bool.md#class-bool) = false, transpose: [bool](class_bool.md#class-bool) = false)                                                               |
| [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d)    | get_occluder_polygon(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), flip_h: [bool](class_bool.md#class-bool) = false, flip_v: [bool](class_bool.md#class-bool) = false, transpose: [bool](class_bool.md#class-bool) = false) |
| [int](class_int.md#class-int)                                              | get_occluder_polygons_count(layer_id: [int](class_int.md#class-int))                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                              | get_terrain_peering_bit(peering_bit: [CellNeighbor](class_tileset.md#enum-tileset-cellneighbor))                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                           | has_custom_data(layer_name: [String](class_string.md#class-string))                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                           | is_collision_polygon_one_way(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                           | is_valid_terrain_peering_bit(peering_bit: [CellNeighbor](class_tileset.md#enum-tileset-cellneighbor))                                                                                                                                                        |
|                                                                            | remove_collision_polygon(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))                                                                                                                                                  |
|                                                                            | remove_occluder_polygon(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))                                                                                                                                                    |
|                                                                            | set_collision_polygon_one_way(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), one_way: [bool](class_bool.md#class-bool))                                                                                             |
|                                                                            | set_collision_polygon_one_way_margin(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), one_way_margin: [float](class_float.md#class-float))                                                                     |
|                                                                            | set_collision_polygon_points(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), polygon: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))                                                     |
|                                                                            | set_collision_polygons_count(layer_id: [int](class_int.md#class-int), polygons_count: [int](class_int.md#class-int))                                                                                                                                         |
|                                                                            | set_constant_angular_velocity(layer_id: [int](class_int.md#class-int), velocity: [float](class_float.md#class-float))                                                                                                                                       |
|                                                                            | set_constant_linear_velocity(layer_id: [int](class_int.md#class-int), velocity: [Vector2](class_vector2.md#class-vector2))                                                                                                                                   |
|                                                                            | set_custom_data(layer_name: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))                                                                                                                                                     |
|                                                                            | set_custom_data_by_layer_id(layer_id: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant))                                                                                                                                        |
|                                                                            | set_navigation_polygon(layer_id: [int](class_int.md#class-int), navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon))                                                                                                       |
|                                                                            | set_occluder(layer_id: [int](class_int.md#class-int), occluder_polygon: [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d))                                                                                                                             |
|                                                                            | set_occluder_polygon(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), polygon: [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d))                                                                        |
|                                                                            | set_occluder_polygons_count(layer_id: [int](class_int.md#class-int), polygons_count: [int](class_int.md#class-int))                                                                                                                                           |
|                                                                            | set_terrain_peering_bit(peering_bit: [CellNeighbor](class_tileset.md#enum-tileset-cellneighbor), terrain: [int](class_int.md#class-int))                                                                                                                          |

---

## Signals

**changed**()

Emitted when any of the properties are changed.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **flip_h** = `false`

-  **set_flip_h**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flip_h**()

If `true`, the tile will have its texture flipped horizontally.

---

[bool](class_bool.md#class-bool) **flip_v** = `false`

-  **set_flip_v**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flip_v**()

If `true`, the tile will have its texture flipped vertically.

---

[Material](class_material.md#class-material) **material**

-  **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

The [Material](class_material.md#class-material) to use for this **TileData**. This can be a [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial) to use the default shader, or a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) to use a custom shader.

---

[Color](class_color.md#class-color) **modulate** = `Color(1, 1, 1, 1)`

-  **set_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_modulate**()

Color modulation of the tile.

---

[float](class_float.md#class-float) **probability** = `1.0`

-  **set_probability**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_probability**()

Relative probability of this tile being selected when drawing a pattern of random tiles.

---

[int](class_int.md#class-int) **terrain** = `-1`

-  **set_terrain**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_terrain**()

ID of the terrain from the terrain set that the tile uses.

---

[int](class_int.md#class-int) **terrain_set** = `-1`

-  **set_terrain_set**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_terrain_set**()

ID of the terrain set that the tile uses.

---

[Vector2i](class_vector2i.md#class-vector2i) **texture_origin** = `Vector2i(0, 0)`

-  **set_texture_origin**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_texture_origin**()

Offsets the position of where the tile is drawn.

---

[bool](class_bool.md#class-bool) **transpose** = `false`

-  **set_transpose**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_transpose**()

If `true`, the tile will display transposed, i.e. with horizontal and vertical texture UVs swapped.

---

[int](class_int.md#class-int) **y_sort_origin** = `0`

-  **set_y_sort_origin**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_y_sort_origin**()

Vertical point of the tile used for determining y-sorted order.

---

[int](class_int.md#class-int) **z_index** = `0`

-  **set_z_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_z_index**()

Ordering index of this tile, relative to [TileMapLayer](class_tilemaplayer.md#class-tilemaplayer).

---

## Method Descriptions

 **add_collision_polygon**(layer_id: [int](class_int.md#class-int))

Adds a collision polygon to the tile on the given TileSet physics layer.

---

 **add_occluder_polygon**(layer_id: [int](class_int.md#class-int))

Adds an occlusion polygon to the tile on the TileSet occlusion layer with index `layer_id`.

---

[float](class_float.md#class-float) **get_collision_polygon_one_way_margin**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))

Returns the one-way margin (for one-way platforms) of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_collision_polygon_points**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))

Returns the points of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

[int](class_int.md#class-int) **get_collision_polygons_count**(layer_id: [int](class_int.md#class-int))

Returns how many polygons the tile has for TileSet physics layer with index `layer_id`.

---

[float](class_float.md#class-float) **get_constant_angular_velocity**(layer_id: [int](class_int.md#class-int))

Returns the constant angular velocity applied to objects colliding with this tile.

---

[Vector2](class_vector2.md#class-vector2) **get_constant_linear_velocity**(layer_id: [int](class_int.md#class-int))

Returns the constant linear velocity applied to objects colliding with this tile.

---

[Variant](class_variant.md#class-variant) **get_custom_data**(layer_name: [String](class_string.md#class-string))

Returns the custom data value for custom data layer named `layer_name`. To check if a custom data layer exists, use has_custom_data().

---

[Variant](class_variant.md#class-variant) **get_custom_data_by_layer_id**(layer_id: [int](class_int.md#class-int))

Returns the custom data value for custom data layer with index `layer_id`.

---

[NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon) **get_navigation_polygon**(layer_id: [int](class_int.md#class-int), flip_h: [bool](class_bool.md#class-bool) = false, flip_v: [bool](class_bool.md#class-bool) = false, transpose: [bool](class_bool.md#class-bool) = false)

Returns the navigation polygon of the tile for the TileSet navigation layer with index `layer_id`.

`flip_h`, `flip_v`, and `transpose` allow transforming the returned polygon.

---

[OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d) **get_occluder**(layer_id: [int](class_int.md#class-int), flip_h: [bool](class_bool.md#class-bool) = false, flip_v: [bool](class_bool.md#class-bool) = false, transpose: [bool](class_bool.md#class-bool) = false)

**Deprecated:** Use get_occluder_polygon() instead.

Returns the occluder polygon of the tile for the TileSet occlusion layer with index `layer_id`.

`flip_h`, `flip_v`, and `transpose` allow transforming the returned polygon.

---

[OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d) **get_occluder_polygon**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), flip_h: [bool](class_bool.md#class-bool) = false, flip_v: [bool](class_bool.md#class-bool) = false, transpose: [bool](class_bool.md#class-bool) = false)

Returns the occluder polygon at index `polygon_index` from the TileSet occlusion layer with index `layer_id`.

The `flip_h`, `flip_v`, and `transpose` parameters can be `true` to transform the returned polygon.

---

[int](class_int.md#class-int) **get_occluder_polygons_count**(layer_id: [int](class_int.md#class-int))

Returns the number of occluder polygons of the tile in the TileSet occlusion layer with index `layer_id`.

---

[int](class_int.md#class-int) **get_terrain_peering_bit**(peering_bit: [CellNeighbor](class_tileset.md#enum-tileset-cellneighbor))

Returns the tile's terrain bit for the given `peering_bit` direction. To check that a direction is valid, use is_valid_terrain_peering_bit().

---

[bool](class_bool.md#class-bool) **has_custom_data**(layer_name: [String](class_string.md#class-string))

Returns whether there exists a custom data layer named `layer_name`.

---

[bool](class_bool.md#class-bool) **is_collision_polygon_one_way**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))

Returns whether one-way collisions are enabled for the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

[bool](class_bool.md#class-bool) **is_valid_terrain_peering_bit**(peering_bit: [CellNeighbor](class_tileset.md#enum-tileset-cellneighbor))

Returns whether the given `peering_bit` direction is valid for this tile.

---

 **remove_collision_polygon**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))

Removes the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

 **remove_occluder_polygon**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int))

Removes the polygon at index `polygon_index` for TileSet occlusion layer with index `layer_id`.

---

 **set_collision_polygon_one_way**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), one_way: [bool](class_bool.md#class-bool))

Enables/disables one-way collisions on the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

 **set_collision_polygon_one_way_margin**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), one_way_margin: [float](class_float.md#class-float))

Sets the one-way margin (for one-way platforms) of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

 **set_collision_polygon_points**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), polygon: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))

Sets the points of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

 **set_collision_polygons_count**(layer_id: [int](class_int.md#class-int), polygons_count: [int](class_int.md#class-int))

Sets the polygons count for TileSet physics layer with index `layer_id`.

---

 **set_constant_angular_velocity**(layer_id: [int](class_int.md#class-int), velocity: [float](class_float.md#class-float))

Sets the constant angular velocity. This does not rotate the tile. This angular velocity is applied to objects colliding with this tile.

---

 **set_constant_linear_velocity**(layer_id: [int](class_int.md#class-int), velocity: [Vector2](class_vector2.md#class-vector2))

Sets the constant linear velocity. This does not move the tile. This linear velocity is applied to objects colliding with this tile. This is useful to create conveyor belts.

---

 **set_custom_data**(layer_name: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))

Sets the tile's custom data value for the TileSet custom data layer with name `layer_name`.

---

 **set_custom_data_by_layer_id**(layer_id: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant))

Sets the tile's custom data value for the TileSet custom data layer with index `layer_id`.

---

 **set_navigation_polygon**(layer_id: [int](class_int.md#class-int), navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon))

Sets the navigation polygon for the TileSet navigation layer with index `layer_id`.

---

 **set_occluder**(layer_id: [int](class_int.md#class-int), occluder_polygon: [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d))

**Deprecated:** Use set_occluder_polygon() instead.

Sets the occluder for the TileSet occlusion layer with index `layer_id`.

---

 **set_occluder_polygon**(layer_id: [int](class_int.md#class-int), polygon_index: [int](class_int.md#class-int), polygon: [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d))

Sets the occluder for polygon with index `polygon_index` in the TileSet occlusion layer with index `layer_id`.

---

 **set_occluder_polygons_count**(layer_id: [int](class_int.md#class-int), polygons_count: [int](class_int.md#class-int))

Sets the occluder polygon count in the TileSet occlusion layer with index `layer_id`.

---

 **set_terrain_peering_bit**(peering_bit: [CellNeighbor](class_tileset.md#enum-tileset-cellneighbor), terrain: [int](class_int.md#class-int))

Sets the tile's terrain bit for the given `peering_bit` direction. To check that a direction is valid, use is_valid_terrain_peering_bit().
