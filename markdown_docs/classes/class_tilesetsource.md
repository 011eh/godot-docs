# TileSetSource

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [TileSetAtlasSource](class_tilesetatlassource.md#class-tilesetatlassource), [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class-tilesetscenescollectionsource)

Exposes a set of tiles for a [TileSet](class_tileset.md#class-tileset) resource.

## Description

Exposes a set of tiles for a [TileSet](class_tileset.md#class-tileset) resource.

Tiles in a source are indexed with two IDs, coordinates ID (of type Vector2i) and an alternative ID (of type int), named according to their use in the [TileSetAtlasSource](class_tilesetatlassource.md#class-tilesetatlassource) class.

Depending on the TileSet source type, those IDs might have restrictions on their values, this is why the base **TileSetSource** class only exposes getters for them.

You can iterate over all tiles exposed by a TileSetSource by first iterating over coordinates IDs using get_tiles_count() and get_tile_id(), then over alternative IDs using get_alternative_tiles_count() and get_alternative_tile_id().

**Warning:** **TileSetSource** can only be added to one TileSet at the same time. Calling [TileSet.add_source()](class_tileset.md#class-tileset-method-add-source) on a second [TileSet](class_tileset.md#class-tileset) will remove the source from the first one.

## Methods

| [int](class_int.md#class-int)                | get_alternative_tile_id(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int))      |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                | get_alternative_tiles_count(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                    |
| [Vector2i](class_vector2i.md#class-vector2i) | get_tile_id(index: [int](class_int.md#class-int))                                                                                          |
| [int](class_int.md#class-int)                | get_tiles_count()                                                                                                                      |
| [bool](class_bool.md#class-bool)             | has_alternative_tile(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool)             | has_tile(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                          |

---

## Method Descriptions

[int](class_int.md#class-int) **get_alternative_tile_id**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), index: [int](class_int.md#class-int))

Returns the alternative ID for the tile with coordinates ID `atlas_coords` at index `index`.

---

[int](class_int.md#class-int) **get_alternative_tiles_count**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the number of alternatives tiles for the coordinates ID `atlas_coords`.

For [TileSetAtlasSource](class_tilesetatlassource.md#class-tilesetatlassource), this always return at least 1, as the base tile with ID 0 is always part of the alternatives list.

Returns -1 if there is not tile at the given coords.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_tile_id**(index: [int](class_int.md#class-int))

Returns the tile coordinates ID of the tile with index `index`.

---

[int](class_int.md#class-int) **get_tiles_count**()

Returns how many tiles this atlas source defines (not including alternative tiles).

---

[bool](class_bool.md#class-bool) **has_alternative_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int))

Returns if the base tile at coordinates `atlas_coords` has an alternative with ID `alternative_tile`.

---

[bool](class_bool.md#class-bool) **has_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns if this atlas has a tile with coordinates ID `atlas_coords`.
