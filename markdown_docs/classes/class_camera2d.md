# Camera2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Camera node for 2D scenes.

## Description

Camera node for 2D scenes. It forces the screen (current layer) to scroll following this node. This makes it easier (and faster) to program scrollable scenes than manually changing the position of [CanvasItem](class_canvasitem.md#class-canvasitem)-based nodes.

Cameras register themselves in the nearest [Viewport](class_viewport.md#class-viewport) node (when ascending the tree). Only one camera can be active per viewport. If no viewport is available ascending the tree, the camera will register in the global viewport.

This node is intended to be a simple helper to get things going quickly, but more functionality may be desired to change how the camera works. To make your own custom camera node, inherit it from [Node2D](class_node2d.md#class-node2d) and change the transform of the canvas by setting [Viewport.canvas_transform](class_viewport.md#class-viewport-property-canvas-transform) in [Viewport](class_viewport.md#class-viewport) (you can obtain the current [Viewport](class_viewport.md#class-viewport) by using [Node.get_viewport()](class_node.md#class-node-method-get-viewport)).

Note that the **Camera2D** node's [Node2D.global_position](class_node2d.md#class-node2d-property-global-position) doesn't represent the actual position of the screen, which may differ due to applied smoothing or limits. You can use get_screen_center_position() to get the real position. Same for the node's [Node2D.global_rotation](class_node2d.md#class-node2d-property-global-rotation) which may be different due to applied rotation smoothing. You can use get_screen_rotation() to get the current rotation of the screen.

## Tutorials

- [2D Platformer Demo](https://godotengine.org/asset-library/asset/2727)
- [2D Isometric Demo](https://godotengine.org/asset-library/asset/2718)

## Properties

| AnchorMode                           | anchor_mode                               | `1`             |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------|
| [Node](class_node.md#class-node)                                  | custom_viewport                       |                 |
| [float](class_float.md#class-float)                               | drag_bottom_margin                 | `0.2`           |
| [bool](class_bool.md#class-bool)                                  | drag_horizontal_enabled       | `false`         |
| [float](class_float.md#class-float)                               | drag_horizontal_offset         | `0.0`           |
| [float](class_float.md#class-float)                               | drag_left_margin                     | `0.2`           |
| [float](class_float.md#class-float)                               | drag_right_margin                   | `0.2`           |
| [float](class_float.md#class-float)                               | drag_top_margin                       | `0.2`           |
| [bool](class_bool.md#class-bool)                                  | drag_vertical_enabled           | `false`         |
| [float](class_float.md#class-float)                               | drag_vertical_offset             | `0.0`           |
| [bool](class_bool.md#class-bool)                                  | editor_draw_drag_margin       | `false`         |
| [bool](class_bool.md#class-bool)                                  | editor_draw_limits                 | `false`         |
| [bool](class_bool.md#class-bool)                                  | editor_draw_screen                 | `true`          |
| [bool](class_bool.md#class-bool)                                  | enabled                                       | `true`          |
| [bool](class_bool.md#class-bool)                                  | ignore_rotation                       | `true`          |
| [int](class_int.md#class-int)                                     | limit_bottom                             | `10000000`      |
| [bool](class_bool.md#class-bool)                                  | limit_enabled                           | `true`          |
| [int](class_int.md#class-int)                                     | limit_left                                 | `-10000000`     |
| [int](class_int.md#class-int)                                     | limit_right                               | `10000000`      |
| [bool](class_bool.md#class-bool)                                  | limit_smoothed                         | `false`         |
| [int](class_int.md#class-int)                                     | limit_top                                   | `-10000000`     |
| [Vector2](class_vector2.md#class-vector2)                         | offset                                         | `Vector2(0, 0)` |
| [bool](class_bool.md#class-bool)                                  | position_smoothing_enabled | `false`         |
| [float](class_float.md#class-float)                               | position_smoothing_speed     | `5.0`           |
| Camera2DProcessCallback | process_callback                     | `1`             |
| [bool](class_bool.md#class-bool)                                  | rotation_smoothing_enabled | `false`         |
| [float](class_float.md#class-float)                               | rotation_smoothing_speed     | `5.0`           |
| [Vector2](class_vector2.md#class-vector2)                         | zoom                                             | `Vector2(1, 1)` |

## Methods

|                                           | align()                                                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           | force_update_scroll()                                                                                                      |
| [float](class_float.md#class-float)       | get_drag_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                                   |
| [int](class_int.md#class-int)             | get_limit(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                                               |
| [Vector2](class_vector2.md#class-vector2) | get_screen_center_position()                                                                                        |
| [float](class_float.md#class-float)       | get_screen_rotation()                                                                                                      |
| [Vector2](class_vector2.md#class-vector2) | get_target_position()                                                                                                      |
| [bool](class_bool.md#class-bool)          | is_current()                                                                                                                        |
|                                           | make_current()                                                                                                                    |
|                                           | reset_smoothing()                                                                                                              |
|                                           | set_drag_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float)) |
|                                           | set_limit(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))                         |

---

## Enumerations

enum **AnchorMode**:

AnchorMode **ANCHOR_MODE_FIXED_TOP_LEFT** = `0`

The camera's position is fixed so that the top-left corner is always at the origin.

AnchorMode **ANCHOR_MODE_DRAG_CENTER** = `1`

The camera's position takes into account vertical/horizontal offsets and the screen size.

---

enum **Camera2DProcessCallback**:

Camera2DProcessCallback **CAMERA2D_PROCESS_PHYSICS** = `0`

The camera updates during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class-node-constant-notification-internal-physics-process)).

Camera2DProcessCallback **CAMERA2D_PROCESS_IDLE** = `1`

The camera updates during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class-node-constant-notification-internal-process)).

---

## Property Descriptions

AnchorMode **anchor_mode** = `1`

-  **set_anchor_mode**(value: AnchorMode)
- AnchorMode **get_anchor_mode**()

The Camera2D's anchor point.

---

[Node](class_node.md#class-node) **custom_viewport**

-  **set_custom_viewport**(value: [Node](class_node.md#class-node))
- [Node](class_node.md#class-node) **get_custom_viewport**()

The custom [Viewport](class_viewport.md#class-viewport) node attached to the **Camera2D**. If `null` or not a [Viewport](class_viewport.md#class-viewport), uses the default viewport instead.

---

[float](class_float.md#class-float) **drag_bottom_margin** = `0.2`

-  **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Bottom margin needed to drag the camera. A value of `1` makes the camera move only when reaching the bottom edge of the screen.

---

[bool](class_bool.md#class-bool) **drag_horizontal_enabled** = `false`

-  **set_drag_horizontal_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drag_horizontal_enabled**()

If `true`, the camera only moves when reaching the horizontal (left and right) drag margins. If `false`, the camera moves horizontally regardless of margins.

---

[float](class_float.md#class-float) **drag_horizontal_offset** = `0.0`

-  **set_drag_horizontal_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_horizontal_offset**()

The relative horizontal drag offset of the camera between the right (`-1`) and left (`1`) drag margins.

**Note:** Used to set the initial horizontal drag offset; determine the current offset; or force the current offset. It's not automatically updated when drag_horizontal_enabled is `true` or the drag margins are changed.

---

[float](class_float.md#class-float) **drag_left_margin** = `0.2`

-  **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Left margin needed to drag the camera. A value of `1` makes the camera move only when reaching the left edge of the screen.

---

[float](class_float.md#class-float) **drag_right_margin** = `0.2`

-  **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Right margin needed to drag the camera. A value of `1` makes the camera move only when reaching the right edge of the screen.

---

[float](class_float.md#class-float) **drag_top_margin** = `0.2`

-  **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Top margin needed to drag the camera. A value of `1` makes the camera move only when reaching the top edge of the screen.

---

[bool](class_bool.md#class-bool) **drag_vertical_enabled** = `false`

-  **set_drag_vertical_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drag_vertical_enabled**()

If `true`, the camera only moves when reaching the vertical (top and bottom) drag margins. If `false`, the camera moves vertically regardless of the drag margins.

---

[float](class_float.md#class-float) **drag_vertical_offset** = `0.0`

-  **set_drag_vertical_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_vertical_offset**()

The relative vertical drag offset of the camera between the bottom (`-1`) and top (`1`) drag margins.

**Note:** Used to set the initial vertical drag offset; determine the current offset; or force the current offset. It's not automatically updated when drag_vertical_enabled is `true` or the drag margins are changed.

---

[bool](class_bool.md#class-bool) **editor_draw_drag_margin** = `false`

-  **set_margin_drawing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_margin_drawing_enabled**()

If `true`, draws the camera's drag margin rectangle in the editor.

---

[bool](class_bool.md#class-bool) **editor_draw_limits** = `false`

-  **set_limit_drawing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_limit_drawing_enabled**()

If `true`, draws the camera's limits rectangle in the editor.

---

[bool](class_bool.md#class-bool) **editor_draw_screen** = `true`

-  **set_screen_drawing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_screen_drawing_enabled**()

If `true`, draws the camera's screen rectangle in the editor.

---

[bool](class_bool.md#class-bool) **enabled** = `true`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

Controls whether the camera can be active or not. If `true`, the **Camera2D** will become the main camera when it enters the scene tree and there is no active camera currently (see [Viewport.get_camera_2d()](class_viewport.md#class-viewport-method-get-camera-2d)).

When the camera is currently active and enabled is set to `false`, the next enabled **Camera2D** in the scene tree will become active.

---

[bool](class_bool.md#class-bool) **ignore_rotation** = `true`

-  **set_ignore_rotation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ignoring_rotation**()

If `true`, the camera's rendered view is not affected by its [Node2D.rotation](class_node2d.md#class-node2d-property-rotation) and [Node2D.global_rotation](class_node2d.md#class-node2d-property-global-rotation).

---

[int](class_int.md#class-int) **limit_bottom** = `10000000`

-  **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Bottom scroll limit in pixels. The camera stops moving when reaching this value, but offset can push the view past the limit.

---

[bool](class_bool.md#class-bool) **limit_enabled** = `true`

-  **set_limit_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_limit_enabled**()

If `true`, the limits will be enabled. Disabling this will allow the camera to focus anywhere, when the four `limit_*` properties will not work.

---

[int](class_int.md#class-int) **limit_left** = `-10000000`

-  **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Left scroll limit in pixels. The camera stops moving when reaching this value, but offset can push the view past the limit.

---

[int](class_int.md#class-int) **limit_right** = `10000000`

-  **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Right scroll limit in pixels. The camera stops moving when reaching this value, but offset can push the view past the limit.

---

[bool](class_bool.md#class-bool) **limit_smoothed** = `false`

-  **set_limit_smoothing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_limit_smoothing_enabled**()

If `true`, the camera smoothly stops when reaches its limits.

This property has no effect if position_smoothing_enabled is `false`.

**Note:** To immediately update the camera's position to be within limits without smoothing, even with this setting enabled, invoke reset_smoothing().

---

[int](class_int.md#class-int) **limit_top** = `-10000000`

-  **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Top scroll limit in pixels. The camera stops moving when reaching this value, but offset can push the view past the limit.

---

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)`

-  **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The camera's relative offset. Useful for looking around or camera shake animations. The offsetted camera can go past the limits defined in limit_top, limit_bottom, limit_left and limit_right.

---

[bool](class_bool.md#class-bool) **position_smoothing_enabled** = `false`

-  **set_position_smoothing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_position_smoothing_enabled**()

If `true`, the camera's view smoothly moves towards its target position at position_smoothing_speed.

---

[float](class_float.md#class-float) **position_smoothing_speed** = `5.0`

-  **set_position_smoothing_speed**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_position_smoothing_speed**()

Speed in pixels per second of the camera's smoothing effect when position_smoothing_enabled is `true`.

---

Camera2DProcessCallback **process_callback** = `1`

-  **set_process_callback**(value: Camera2DProcessCallback)
- Camera2DProcessCallback **get_process_callback**()

The camera's process callback.

---

[bool](class_bool.md#class-bool) **rotation_smoothing_enabled** = `false`

-  **set_rotation_smoothing_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_rotation_smoothing_enabled**()

If `true`, the camera's view smoothly rotates, via asymptotic smoothing, to align with its target rotation at rotation_smoothing_speed.

**Note:** This property has no effect if ignore_rotation is `true`.

---

[float](class_float.md#class-float) **rotation_smoothing_speed** = `5.0`

-  **set_rotation_smoothing_speed**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_rotation_smoothing_speed**()

The angular, asymptotic speed of the camera's rotation smoothing effect when rotation_smoothing_enabled is `true`.

---

[Vector2](class_vector2.md#class-vector2) **zoom** = `Vector2(1, 1)`

-  **set_zoom**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_zoom**()

The camera's zoom. Higher values are more zoomed in. For example, a zoom of `Vector2(2.0, 2.0)` will be twice as zoomed in on each axis (the view covers an area four times smaller). In contrast, a zoom of `Vector2(0.5, 0.5)` will be twice as zoomed out on each axis (the view covers an area four times larger). The X and Y components should generally always be set to the same value, unless you wish to stretch the camera view.

**Note:** [FontFile.oversampling](class_fontfile.md#class-fontfile-property-oversampling) does *not* take **Camera2D** zoom into account. This means that zooming in/out will cause bitmap fonts and rasterized (non-MSDF) dynamic fonts to appear blurry or pixelated unless the font is part of a [CanvasLayer](class_canvaslayer.md#class-canvaslayer) that makes it ignore camera zoom. To ensure text remains crisp regardless of zoom, you can enable MSDF font rendering by enabling [ProjectSettings.gui/theme/default_font_multichannel_signed_distance_field](class_projectsettings.md#class-projectsettings-property-gui-theme-default-font-multichannel-signed-distance-field) (applies to the default project font only), or enabling **Multichannel Signed Distance Field** in the import options of a DynamicFont for custom fonts. On system fonts, [SystemFont.multichannel_signed_distance_field](class_systemfont.md#class-systemfont-property-multichannel-signed-distance-field) can be enabled in the inspector.

---

## Method Descriptions

 **align**()

Aligns the camera to the tracked node.

**Note:** Calling force_update_scroll() after this method is not required.

---

 **force_update_scroll**()

Forces the camera to update scroll immediately.

---

[float](class_float.md#class-float) **get_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the specified [Side](class_@globalscope.md#enum-globalscope-side)'s margin. See also drag_bottom_margin, drag_top_margin, drag_left_margin, and drag_right_margin.

---

[int](class_int.md#class-int) **get_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the camera limit for the specified [Side](class_@globalscope.md#enum-globalscope-side). See also limit_bottom, limit_top, limit_left, and limit_right.

---

[Vector2](class_vector2.md#class-vector2) **get_screen_center_position**()

Returns the center of the screen from this camera's point of view, in global coordinates.

**Note:** The exact targeted position of the camera may be different. See get_target_position().

---

[float](class_float.md#class-float) **get_screen_rotation**()

Returns the current screen rotation from this camera's point of view.

**Note:** The screen rotation can be different from [Node2D.global_rotation](class_node2d.md#class-node2d-property-global-rotation) if the camera is rotating smoothly due to rotation_smoothing_enabled.

---

[Vector2](class_vector2.md#class-vector2) **get_target_position**()

Returns this camera's target position, in global coordinates.

**Note:** The returned value is not the same as [Node2D.global_position](class_node2d.md#class-node2d-property-global-position), as it is affected by the drag properties. It is also not the same as the current position if position_smoothing_enabled is `true` (see get_screen_center_position()).

---

[bool](class_bool.md#class-bool) **is_current**()

Returns `true` if this **Camera2D** is the active camera (see [Viewport.get_camera_2d()](class_viewport.md#class-viewport-method-get-camera-2d)).

---

 **make_current**()

Forces this **Camera2D** to become the current active one. enabled must be `true`.

---

 **reset_smoothing**()

Sets the camera's position immediately to its current smoothing destination.

This method has no effect if position_smoothing_enabled is `false`.

---

 **set_drag_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), drag_margin: [float](class_float.md#class-float))

Sets the specified [Side](class_@globalscope.md#enum-globalscope-side)'s margin. See also drag_bottom_margin, drag_top_margin, drag_left_margin, and drag_right_margin.

---

 **set_limit**(margin: [Side](class_@globalscope.md#enum-globalscope-side), limit: [int](class_int.md#class-int))

Sets the camera limit for the specified [Side](class_@globalscope.md#enum-globalscope-side). See also limit_bottom, limit_top, limit_left, and limit_right.
