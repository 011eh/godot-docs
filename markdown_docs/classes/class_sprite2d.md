# Sprite2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

General-purpose sprite node.

## Description

A node that displays a 2D texture. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation.

## Tutorials

- [Instancing Demo](https://godotengine.org/asset-library/asset/2716)

## Properties

| [bool](class_bool.md#class-bool)                | centered                                     | `true`              |
|-------------------------------------------------|-----------------------------------------------------------------------------------|---------------------|
| [bool](class_bool.md#class-bool)                | flip_h                                         | `false`             |
| [bool](class_bool.md#class-bool)                | flip_v                                         | `false`             |
| [int](class_int.md#class-int)                   | frame                                           | `0`                 |
| [Vector2i](class_vector2i.md#class-vector2i)    | frame_coords                             | `Vector2i(0, 0)`    |
| [int](class_int.md#class-int)                   | hframes                                       | `1`                 |
| [Vector2](class_vector2.md#class-vector2)       | offset                                         | `Vector2(0, 0)`     |
| [bool](class_bool.md#class-bool)                | region_enabled                         | `false`             |
| [bool](class_bool.md#class-bool)                | region_filter_clip_enabled | `false`             |
| [Rect2](class_rect2.md#class-rect2)             | region_rect                               | `Rect2(0, 0, 0, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d) | texture                                       |                     |
| [int](class_int.md#class-int)                   | vframes                                       | `1`                 |

## Methods

| [Rect2](class_rect2.md#class-rect2)   | get_rect()                                                             |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)      | is_pixel_opaque(pos: [Vector2](class_vector2.md#class-vector2)) |

---

## Signals

**frame_changed**()

Emitted when the frame changes.

---

**texture_changed**()

Emitted when the texture changes.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **centered** = `true`

-  **set_centered**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_centered**()

If `true`, texture is centered.

**Note:** For games with a pixel art aesthetic, textures may appear deformed when centered. This is caused by their position being between pixels. To prevent this, set this property to `false`, or consider enabling [ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel](class_projectsettings.md#class-projectsettings-property-rendering-2d-snap-snap-2d-vertices-to-pixel) and [ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel](class_projectsettings.md#class-projectsettings-property-rendering-2d-snap-snap-2d-transforms-to-pixel).

---

[bool](class_bool.md#class-bool) **flip_h** = `false`

-  **set_flip_h**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_h**()

If `true`, texture is flipped horizontally.

---

[bool](class_bool.md#class-bool) **flip_v** = `false`

-  **set_flip_v**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_v**()

If `true`, texture is flipped vertically.

---

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

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)`

-  **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The texture's drawing offset.

**Note:** When you increase offset.y in Sprite2D, the sprite moves downward on screen (i.e., +Y is down).

---

[bool](class_bool.md#class-bool) **region_enabled** = `false`

-  **set_region_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_region_enabled**()

If `true`, texture is cut from a larger atlas texture. See region_rect.

**Note:** When using a custom [Shader](class_shader.md#class-shader) on a **Sprite2D**, the `UV` shader built-in will refer to the entire texture space. Use the `REGION_RECT` built-in to get the currently visible region defined in region_rect instead. See [CanvasItem shaders](../tutorials/shaders/shader_reference/canvas_item_shader.md) for details.

---

[bool](class_bool.md#class-bool) **region_filter_clip_enabled** = `false`

-  **set_region_filter_clip_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_region_filter_clip_enabled**()

If `true`, the area outside of the region_rect is clipped to avoid bleeding of the surrounding texture pixels. region_enabled must be `true`.

---

[Rect2](class_rect2.md#class-rect2) **region_rect** = `Rect2(0, 0, 0, 0)`

-  **set_region_rect**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_region_rect**()

The region of the atlas texture to display. region_enabled must be `true`.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

[Texture2D](class_texture2d.md#class-texture2d) object to draw.

---

[int](class_int.md#class-int) **vframes** = `1`

-  **set_vframes**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_vframes**()

The number of rows in the sprite sheet. When this property is changed, frame is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, frame is reset to `0`.

---

## Method Descriptions

[Rect2](class_rect2.md#class-rect2) **get_rect**()

Returns a [Rect2](class_rect2.md#class-rect2) representing the Sprite2D's boundary in local coordinates.

**Example:** Detect if the Sprite2D was clicked:

GDScript

```gdscript
func _input(event):
    if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
        if get_rect().has_point(to_local(event.position)):
            print("A click!")
```

C#

```csharp
public override void _Input(InputEvent @event)
{
    if (@event is InputEventMouseButton inputEventMouse)
    {
        if (inputEventMouse.Pressed && inputEventMouse.ButtonIndex == MouseButton.Left)
        {
            if (GetRect().HasPoint(ToLocal(inputEventMouse.Position)))
            {
                GD.Print("A click!");
            }
        }
    }
}
```

---

[bool](class_bool.md#class-bool) **is_pixel_opaque**(pos: [Vector2](class_vector2.md#class-vector2))

Returns `true` if the pixel at the given position is opaque, `false` otherwise. Also returns `false` if the given position is out of bounds or this sprite's texture is `null`. `pos` is in local coordinates.
