# ParallaxBackground

**Deprecated:** Use the [Parallax2D](class_parallax2d.md#class-parallax2d) node instead.

**Inherits:** [CanvasLayer](class_canvaslayer.md#class-canvaslayer) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node used to create a parallax scrolling background.

## Description

A ParallaxBackground uses one or more [ParallaxLayer](class_parallaxlayer.md#class-parallaxlayer) child nodes to create a parallax effect. Each [ParallaxLayer](class_parallaxlayer.md#class-parallaxlayer) can move at a different speed using [ParallaxLayer.motion_offset](class_parallaxlayer.md#class-parallaxlayer-property-motion-offset). This creates an illusion of depth in a 2D game. If not used with a [Camera2D](class_camera2d.md#class-camera2d), you must manually calculate the scroll_offset.

**Note:** Each **ParallaxBackground** is drawn on one specific [Viewport](class_viewport.md#class-viewport) and cannot be shared between multiple [Viewport](class_viewport.md#class-viewport)s, see [CanvasLayer.custom_viewport](class_canvaslayer.md#class-canvaslayer-property-custom-viewport). When using multiple [Viewport](class_viewport.md#class-viewport)s, for example in a split-screen game, you need create an individual **ParallaxBackground** for each [Viewport](class_viewport.md#class-viewport) you want it to be drawn on.

## Properties

| [int](class_int.md#class-int)             | layer                                                                                     | `-100` (overrides [CanvasLayer](class_canvaslayer.md#class-canvaslayer-property-layer))   |
|-------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [Vector2](class_vector2.md#class-vector2) | scroll_base_offset               | `Vector2(0, 0)`                                                                           |
| [Vector2](class_vector2.md#class-vector2) | scroll_base_scale                 | `Vector2(1, 1)`                                                                           |
| [bool](class_bool.md#class-bool)          | scroll_ignore_camera_zoom | `false`                                                                                   |
| [Vector2](class_vector2.md#class-vector2) | scroll_limit_begin               | `Vector2(0, 0)`                                                                           |
| [Vector2](class_vector2.md#class-vector2) | scroll_limit_end                   | `Vector2(0, 0)`                                                                           |
| [Vector2](class_vector2.md#class-vector2) | scroll_offset                         | `Vector2(0, 0)`                                                                           |

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **scroll_base_offset** = `Vector2(0, 0)`

-  **set_scroll_base_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_scroll_base_offset**()

The base position offset for all [ParallaxLayer](class_parallaxlayer.md#class-parallaxlayer) children.

---

[Vector2](class_vector2.md#class-vector2) **scroll_base_scale** = `Vector2(1, 1)`

-  **set_scroll_base_scale**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_scroll_base_scale**()

The base motion scale for all [ParallaxLayer](class_parallaxlayer.md#class-parallaxlayer) children.

---

[bool](class_bool.md#class-bool) **scroll_ignore_camera_zoom** = `false`

-  **set_ignore_camera_zoom**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ignore_camera_zoom**()

If `true`, elements in [ParallaxLayer](class_parallaxlayer.md#class-parallaxlayer) child aren't affected by the zoom level of the camera.

---

[Vector2](class_vector2.md#class-vector2) **scroll_limit_begin** = `Vector2(0, 0)`

-  **set_limit_begin**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_limit_begin**()

Top-left limits for scrolling to begin. If the camera is outside of this limit, the background will stop scrolling. Must be lower than scroll_limit_end to work.

---

[Vector2](class_vector2.md#class-vector2) **scroll_limit_end** = `Vector2(0, 0)`

-  **set_limit_end**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_limit_end**()

Bottom-right limits for scrolling to end. If the camera is outside of this limit, the background will stop scrolling. Must be higher than scroll_limit_begin to work.

---

[Vector2](class_vector2.md#class-vector2) **scroll_offset** = `Vector2(0, 0)`

-  **set_scroll_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_scroll_offset**()

The ParallaxBackground's scroll value. Calculated automatically when using a [Camera2D](class_camera2d.md#class-camera2d), but can be used to manually manage scrolling when no camera is present.
