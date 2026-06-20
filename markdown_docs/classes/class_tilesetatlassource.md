# TileSetAtlasSource

**Inherits:** [TileSetSource](class_tilesetsource.md#class-tilesetsource) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Exposes a 2D atlas texture as a set of tiles for a [TileSet](class_tileset.md#class-tileset) resource.

## Description

An atlas is a grid of tiles laid out on a texture. Each tile in the grid must be exposed using create_tile(). Those tiles are then indexed using their coordinates in the grid.

Each tile can also have a size in the grid coordinates, making it more or less cells in the atlas.

Alternatives version of a tile can be created using create_alternative_tile(), which are then indexed using an alternative ID. The main tile (the one in the grid), is accessed with an alternative ID equal to 0.

Each tile alternate has a set of properties that is defined by the source's [TileSet](class_tileset.md#class-tileset) layers. Those properties are stored in a TileData object that can be accessed and modified using get_tile_data().

As TileData properties are stored directly in the TileSetAtlasSource resource, their properties might also be set using `TileSetAtlasSource.set("<coords_x>:<coords_y>/<alternative_id>/<tile_data_property>")`.

## Properties

| [Vector2i](class_vector2i.md#class-vector2i)    | margins                         | `Vector2i(0, 0)`   |
|-------------------------------------------------|-------------------------------------------------------------------------------|--------------------|
| [Vector2i](class_vector2i.md#class-vector2i)    | separation                   | `Vector2i(0, 0)`   |
| [Texture2D](class_texture2d.md#class-texture2d) | texture                         |                    |
| [Vector2i](class_vector2i.md#class-vector2i)    | texture_region_size | `Vector2i(16, 16)` |
| [bool](class_bool.md#class-bool)                | use_texture_padding | `true`             |

## Methods

|                                                                            | clear_tiles_outside_texture()                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                              | create_alternative_tile(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_id_override: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                              |
|                                                                            | create_tile(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(1, 1))                                                                                                                                                                                                                                              |
| [Vector2i](class_vector2i.md#class-vector2i)                               | get_atlas_grid_size()                                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                              | get_next_alternative_tile_id(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                 |
| [Texture2D](class_texture2d.md#class-texture2d)                            | get_runtime_texture()                                                                                                                                                                                                                                                                                                                                                             |
| [Rect2i](class_rect2i.md#class-rect2i)                                     | get_runtime_tile_texture_region(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                              | get_tile_animation_columns(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                     |
| [float](class_float.md#class-float)                                        | get_tile_animation_frame_duration(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_index: [int](class_int.md#class-int))                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                              | get_tile_animation_frames_count(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                           |
| TileAnimationMode            | get_tile_animation_mode(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                           |
| [Vector2i](class_vector2i.md#class-vector2i)                               | get_tile_animation_separation(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                        | get_tile_animation_speed(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                         |
| [float](class_float.md#class-float)                                        | get_tile_animation_total_duration(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                       |
| [Vector2i](class_vector2i.md#class-vector2i)                               | get_tile_at_coords(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                     |
| [TileData](class_tiledata.md#class-tiledata)                               | get_tile_data(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int))                                                                                                                                                                                                                                                              |
| [Vector2i](class_vector2i.md#class-vector2i)                               | get_tile_size_in_atlas(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                             |
| [Rect2i](class_rect2i.md#class-rect2i)                                     | get_tile_texture_region(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                 |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | get_tiles_to_be_removed_on_change(texture: [Texture2D](class_texture2d.md#class-texture2d), margins: [Vector2i](class_vector2i.md#class-vector2i), separation: [Vector2i](class_vector2i.md#class-vector2i), texture_region_size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                     |
| [bool](class_bool.md#class-bool)                                           | has_room_for_tile(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i), animation_columns: [int](class_int.md#class-int), animation_separation: [Vector2i](class_vector2i.md#class-vector2i), frames_count: [int](class_int.md#class-int), ignored_tile: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1)) |
| [bool](class_bool.md#class-bool)                                           | has_tiles_outside_texture()                                                                                                                                                                                                                                                                                                                                                 |
|                                                                            | move_tile_in_atlas(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), new_atlas_coords: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1), new_size: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1))                                                                                                                                       |
|                                                                            | remove_alternative_tile(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int))                                                                                                                                                                                                                                          |
|                                                                            | remove_tile(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                   |
|                                                                            | set_alternative_tile_id(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int), new_id: [int](class_int.md#class-int))                                                                                                                                                                                                   |
|                                                                            | set_tile_animation_columns(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_columns: [int](class_int.md#class-int))                                                                                                                                                                                                                                       |
|                                                                            | set_tile_animation_frame_duration(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_index: [int](class_int.md#class-int), duration: [float](class_float.md#class-float))                                                                                                                                                                            |
|                                                                            | set_tile_animation_frames_count(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frames_count: [int](class_int.md#class-int))                                                                                                                                                                                                                              |
|                                                                            | set_tile_animation_mode(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), mode: TileAnimationMode)                                                                                                                                                                                                                    |
|                                                                            | set_tile_animation_separation(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), separation: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                     |
|                                                                            | set_tile_animation_speed(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), speed: [float](class_float.md#class-float))                                                                                                                                                                                                                                             |

---

## Enumerations

enum **TileAnimationMode**:

TileAnimationMode **TILE_ANIMATION_MODE_DEFAULT** = `0`

Tile animations start at same time, looking identical.

TileAnimationMode **TILE_ANIMATION_MODE_RANDOM_START_TIMES** = `1`

Tile animations start at random times, looking varied.

TileAnimationMode **TILE_ANIMATION_MODE_MAX** = `2`

Represents the size of the TileAnimationMode enum.

---

## Constants

**TRANSFORM_FLIP_H** = `4096`

Represents cell's horizontal flip flag. Should be used directly with [TileMapLayer](class_tilemaplayer.md#class-tilemaplayer) to flip placed tiles by altering their alternative IDs.

```gdscript
var alternate_id = $TileMapLayer.get_cell_alternative_tile(Vector2i(2, 2))
if not alternate_id & TileSetAtlasSource.TRANSFORM_FLIP_H:
    # If tile is not already flipped, flip it.
    $TileMapLayer.set_cell(Vector2i(2, 2), source_id, atlas_coords, alternate_id | TileSetAtlasSource.TRANSFORM_FLIP_H)
```

**Note:** These transformations can be combined to do the equivalent of 0, 90, 180, and 270 degree rotations, as shown below:

```gdscript
enum TileTransform {
    ROTATE_0 = 0,
    ROTATE_90 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_H,
    ROTATE_180 = TileSetAtlasSource.TRANSFORM_FLIP_H | TileSetAtlasSource.TRANSFORM_FLIP_V,
    ROTATE_270 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_V,
}
```

**TRANSFORM_FLIP_V** = `8192`

Represents cell's vertical flip flag. See TRANSFORM_FLIP_H for usage.

**TRANSFORM_TRANSPOSE** = `16384`

Represents cell's transposed flag. See TRANSFORM_FLIP_H for usage.

---

## Property Descriptions

[Vector2i](class_vector2i.md#class-vector2i) **margins** = `Vector2i(0, 0)`

-  **set_margins**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_margins**()

Margins, in pixels, to offset the origin of the grid in the texture.

---

[Vector2i](class_vector2i.md#class-vector2i) **separation** = `Vector2i(0, 0)`

-  **set_separation**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_separation**()

Separation, in pixels, between each tile texture region of the grid.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The atlas texture.

---

[Vector2i](class_vector2i.md#class-vector2i) **texture_region_size** = `Vector2i(16, 16)`

-  **set_texture_region_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_texture_region_size**()

The base tile size in the texture (in pixel). This size must be bigger than or equal to the TileSet's `tile_size` value.

---

[bool](class_bool.md#class-bool) **use_texture_padding** = `true`

-  **set_use_texture_padding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_texture_padding**()

If `true`, generates an internal texture with an additional one pixel padding around each tile. Texture padding avoids a common artifact where lines appear between tiles.

Disabling this setting might lead a small performance improvement, as generating the internal texture requires both memory and processing time when the TileSetAtlasSource resource is modified.

---

## Method Descriptions

 **clear_tiles_outside_texture**()

Removes all tiles that don't fit the available texture area. This method iterates over all the source's tiles, so it's advised to use has_tiles_outside_texture() beforehand.

---

[int](class_int.md#class-int) **create_alternative_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_id_override: [int](class_int.md#class-int) = -1)

Creates an alternative tile for the tile at coordinates `atlas_coords`. If `alternative_id_override` is -1, give it an automatically generated unique ID, or assigns it the given ID otherwise.

Returns the new alternative identifier, or -1 if the alternative could not be created with a provided `alternative_id_override`.

---

 **create_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(1, 1))

Creates a new tile at coordinates `atlas_coords` with the given `size`.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_atlas_grid_size**()

Returns the atlas grid size, which depends on how many tiles can fit in the texture. It thus depends on the texture's size, the atlas margins, and the tiles' texture_region_size.

---

[int](class_int.md#class-int) **get_next_alternative_tile_id**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the alternative ID a following call to create_alternative_tile() would return.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_runtime_texture**()

If use_texture_padding is `false`, returns texture. Otherwise, returns an internal [ImageTexture](class_imagetexture.md#class-imagetexture) created that includes the padding.

---

[Rect2i](class_rect2i.md#class-rect2i) **get_runtime_tile_texture_region**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame: [int](class_int.md#class-int))

Returns the region of the tile at coordinates `atlas_coords` for the given `frame` inside the texture returned by get_runtime_texture().

**Note:** If use_texture_padding is `false`, returns the same as get_tile_texture_region().

---

[int](class_int.md#class-int) **get_tile_animation_columns**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns how many columns the tile at `atlas_coords` has in its animation layout.

---

[float](class_float.md#class-float) **get_tile_animation_frame_duration**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_index: [int](class_int.md#class-int))

Returns the animation frame duration of frame `frame_index` for the tile at coordinates `atlas_coords`.

---

[int](class_int.md#class-int) **get_tile_animation_frames_count**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns how many animation frames has the tile at coordinates `atlas_coords`.

---

TileAnimationMode **get_tile_animation_mode**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the tile animation mode of the tile at `atlas_coords`. See also set_tile_animation_mode().

---

[Vector2i](class_vector2i.md#class-vector2i) **get_tile_animation_separation**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the separation (as in the atlas grid) between each frame of an animated tile at coordinates `atlas_coords`.

---

[float](class_float.md#class-float) **get_tile_animation_speed**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the animation speed of the tile at coordinates `atlas_coords`.

---

[float](class_float.md#class-float) **get_tile_animation_total_duration**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the sum of the sum of the frame durations of the tile at coordinates `atlas_coords`. This value needs to be divided by the animation speed to get the actual animation loop duration.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_tile_at_coords**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

If there is a tile covering the `atlas_coords` coordinates, returns the top-left coordinates of the tile (thus its coordinate ID). Returns `Vector2i(-1, -1)` otherwise.

---

[TileData](class_tiledata.md#class-tiledata) **get_tile_data**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int))

Returns the [TileData](class_tiledata.md#class-tiledata) object for the given atlas coordinates and alternative ID.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_tile_size_in_atlas**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Returns the size of the tile (in the grid coordinates system) at coordinates `atlas_coords`.

---

[Rect2i](class_rect2i.md#class-rect2i) **get_tile_texture_region**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame: [int](class_int.md#class-int) = 0)

Returns a tile's texture region in the atlas texture. For animated tiles, a `frame` argument might be provided for the different frames of the animation.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_tiles_to_be_removed_on_change**(texture: [Texture2D](class_texture2d.md#class-texture2d), margins: [Vector2i](class_vector2i.md#class-vector2i), separation: [Vector2i](class_vector2i.md#class-vector2i), texture_region_size: [Vector2i](class_vector2i.md#class-vector2i))

Returns an array of tiles coordinates ID that will be automatically removed when modifying one or several of those properties: `texture`, `margins`, `separation` or `texture_region_size`. This can be used to undo changes that would have caused tiles data loss.

---

[bool](class_bool.md#class-bool) **has_room_for_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i), animation_columns: [int](class_int.md#class-int), animation_separation: [Vector2i](class_vector2i.md#class-vector2i), frames_count: [int](class_int.md#class-int), ignored_tile: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1))

Returns whether there is enough room in an atlas to create/modify a tile with the given properties. If `ignored_tile` is provided, act as is the given tile was not present in the atlas. This may be used when you want to modify a tile's properties.

---

[bool](class_bool.md#class-bool) **has_tiles_outside_texture**()

Checks if the source has any tiles that don't fit the texture area (either partially or completely).

---

 **move_tile_in_atlas**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), new_atlas_coords: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1), new_size: [Vector2i](class_vector2i.md#class-vector2i) = Vector2i(-1, -1))

Move the tile and its alternatives at the `atlas_coords` coordinates to the `new_atlas_coords` coordinates with the `new_size` size. This functions will fail if a tile is already present in the given area.

If `new_atlas_coords` is `Vector2i(-1, -1)`, keeps the tile's coordinates. If `new_size` is `Vector2i(-1, -1)`, keeps the tile's size.

To avoid an error, first check if a move is possible using has_room_for_tile().

---

 **remove_alternative_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int))

Remove a tile's alternative with alternative ID `alternative_tile`.

Calling this function with `alternative_tile` equals to 0 will fail, as the base tile alternative cannot be removed.

---

 **remove_tile**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i))

Remove a tile and its alternative at coordinates `atlas_coords`.

---

 **set_alternative_tile_id**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), alternative_tile: [int](class_int.md#class-int), new_id: [int](class_int.md#class-int))

Change a tile's alternative ID from `alternative_tile` to `new_id`.

Calling this function with `new_id` of 0 will fail, as the base tile alternative cannot be moved.

---

 **set_tile_animation_columns**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_columns: [int](class_int.md#class-int))

Sets the number of columns in the animation layout of the tile at coordinates `atlas_coords`. If set to 0, then the different frames of the animation are laid out as a single horizontal line in the atlas.

---

 **set_tile_animation_frame_duration**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frame_index: [int](class_int.md#class-int), duration: [float](class_float.md#class-float))

Sets the animation frame `duration` of frame `frame_index` for the tile at coordinates `atlas_coords`.

---

 **set_tile_animation_frames_count**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), frames_count: [int](class_int.md#class-int))

Sets how many animation frames the tile at coordinates `atlas_coords` has.

---

 **set_tile_animation_mode**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), mode: TileAnimationMode)

Sets the tile animation mode of the tile at `atlas_coords` to `mode`. See also get_tile_animation_mode().

---

 **set_tile_animation_separation**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), separation: [Vector2i](class_vector2i.md#class-vector2i))

Sets the margin (in grid tiles) between each tile in the animation layout of the tile at coordinates `atlas_coords` has.

---

 **set_tile_animation_speed**(atlas_coords: [Vector2i](class_vector2i.md#class-vector2i), speed: [float](class_float.md#class-float))

Sets the animation speed of the tile at coordinates `atlas_coords` has.
