# Sprite3D

**Inherits:** [SpriteBase3D](class_spritebase3d.md#class-spritebase3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

2D sprite node in a 3D world.

## Description

A node that displays a 2D texture in a 3D environment. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation. See also [SpriteBase3D](class_spritebase3d.md#class-spritebase3d) where properties such as the billboard mode are defined.

## Properties

| [int](class_int.md#class-int)                   | frame                   | `0`                 |
|-------------------------------------------------|-----------------------------------------------------------|---------------------|
| [Vector2i](class_vector2i.md#class-vector2i)    | frame_coords     | `Vector2i(0, 0)`    |
| [int](class_int.md#class-int)                   | hframes               | `1`                 |
| [bool](class_bool.md#class-bool)                | region_enabled | `false`             |
| [Rect2](class_rect2.md#class-rect2)             | region_rect       | `Rect2(0, 0, 0, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d) | texture               |                     |
| [int](class_int.md#class-int)                   | vframes               | `1`                 |

---

## Signals

**frame_changed**()

Emitted when the frame changes.

---

**texture_changed**()

Emitted when the texture changes.

---

## Property Descriptions

[int](class_int.md#class-int) **frame** = `0`

-  **set_frame**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_frame**()

Current frame to display from sprite sheet. hframes or vframes must be greater than 1. This property is automatically adjusted when hframes or vframes are changed to keep pointing to the same visual frame (same column and row). If that's impossible, this value is reset to `0`.

---

[Vector2i](class_vector2i.md#class-vector2i) **frame_coords** = `Vector2i(0, 0)`

-  **set_frame_coords**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_frame_coords**()

Coordinates of the frame to display from sprite sheet. This is as an alias for the frame property. hframes or vframes must be greater than 1.

---

[int](class_int.md#class-int) **hframes** = `1`

-  **set_hframes**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_hframes**()

The number of columns in the sprite sheet. When this property is changed, frame is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, frame is reset to `0`.

---

[bool](class_bool.md#class-bool) **region_enabled** = `false`

-  **set_region_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_region_enabled**()

If `true`, the sprite will use region_rect and display only the specified part of its texture.

---

[Rect2](class_rect2.md#class-rect2) **region_rect** = `Rect2(0, 0, 0, 0)`

-  **set_region_rect**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_region_rect**()

The region of the atlas texture to display. region_enabled must be `true`.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

[Texture2D](class_texture2d.md#class-texture2d) object to draw. If [GeometryInstance3D.material_override](class_geometryinstance3d.md#class-geometryinstance3d-property-material-override) is used, this will be overridden. The size information is still used.

---

[int](class_int.md#class-int) **vframes** = `1`

-  **set_vframes**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vframes**()

The number of rows in the sprite sheet. When this property is changed, frame is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, frame is reset to `0`.
