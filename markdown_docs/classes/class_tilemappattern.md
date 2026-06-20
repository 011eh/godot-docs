# TileMapPattern

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds a pattern to be copied from or pasted into [TileMap](class_tilemap.md#class-tilemap)s.

## Description

This resource holds a set of cells to help bulk manipulations of [TileMap](class_tilemap.md#class-tilemap).

A pattern always starts at the `(0, 0)` coordinates and cannot have cells with negative coordinates.

## Methods

| [int](class_int.md#class-int)                                                     | get_cell_alternative_tile(coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Vector2i](class_vector2i.md#class-vector2i)                                      | get_cell_atlas_coords(coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                           |
| [int](class_int.md#class-int)                                                     | get_cell_source_id(coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                 |
| [Vector2i](class_vector2i.md#class-vector2i)                                      | get_size()                                                                                                                                                                                                                                         |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | get_used_cells()                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                  | has_cell(coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                  | is_empty()                                                                                                                                                                                                                                         |
|                                                                                   | remove_cell(coords: [Vector2i](class_vector2i.md#class-vector2i), update_size: [bool](class_bool.md#class-bool))                                                                                                                                |
|                                                                                   | set_cell(coords: [Vector2i](class_vector2i.md#class-vector2i), source_id: [int](class_int.md#class-int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class-int) = -1) |
|                                                                                   | set_size(size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                       |

---

## Method Descriptions

[int](class_int.md#class-int) **get_cell_alternative_tile**(coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the tile alternative ID of the cell at `coords`.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_cell_atlas_coords**(coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the tile atlas coordinates ID of the cell at `coords`.

---

[int](class_int.md#class-int) **get_cell_source_id**(coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the tile source ID of the cell at `coords`.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_size**()

Returns the size, in cells, of the pattern.

---

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **get_used_cells**()

Returns the list of used cell coordinates in the pattern.

---

[bool](class_bool.md#class-bool) **has_cell**(coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns whether the pattern has a tile at the given coordinates.

---

[bool](class_bool.md#class-bool) **is_empty**()

Returns whether the pattern is empty or not.

---

 **remove_cell**(coords: [Vector2i](class_vector2i.md#class-vector2i), update_size: [bool](class_bool.md#class-bool))

Remove the cell at the given coordinates.

---

 **set_cell**(coords: [Vector2i](class_vector2i.md#class-vector2i), source_id: [int](class_int.md#class-int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class-int) = -1)

Sets the tile identifiers for the cell at coordinates `coords`. See [TileMap.set_cell()](class_tilemap.md#class-tilemap-method-set-cell).

---

 **set_size**(size: [Vector2i](class_vector2i.md#class-vector2i))

Sets the size of the pattern.
