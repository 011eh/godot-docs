# ScrollContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorInspector](class_editorinspector.md#class-editorinspector)

A container used to provide scrollbars to a child control when needed.

## Description

A container used to provide a child control with scrollbars when needed. Scrollbars will automatically be drawn at the right (for vertical) or bottom (for horizontal) and will enable dragging to move the viewable Control (and its children) within the ScrollContainer. Scrollbars will also automatically resize the grabber based on the [Control.custom_minimum_size](class_control.md#class-control-property-custom-minimum-size) of the Control relative to the ScrollContainer.

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

## Properties

| [bool](class_bool.md#class-bool)                       | clip_contents                                                                                  | `true` (overrides [Control](class_control.md#class-control-property-clip-contents))           |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                       | draw_focus_border                         | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                       | follow_focus                                   | `false`                                                                                       |
| ScrollMode         | horizontal_scroll_mode               | `1`                                                                                           |
| [bool](class_bool.md#class-bool)                       | propagate_maximum_size                                                                         | `false` (overrides [Control](class_control.md#class-control-property-propagate-maximum-size)) |
| [int](class_int.md#class-int)                          | scroll_deadzone                             | `0`                                                                                           |
| ScrollHintMode | scroll_hint_mode                           | `0`                                                                                           |
| [int](class_int.md#class-int)                          | scroll_horizontal                         | `0`                                                                                           |
| [bool](class_bool.md#class-bool)                       | scroll_horizontal_by_default   | `false`                                                                                       |
| [float](class_float.md#class-float)                    | scroll_horizontal_custom_step | `-1.0`                                                                                        |
| [int](class_int.md#class-int)                          | scroll_vertical                             | `0`                                                                                           |
| [float](class_float.md#class-float)                    | scroll_vertical_custom_step     | `-1.0`                                                                                        |
| [bool](class_bool.md#class-bool)                       | tile_scroll_hint                           | `false`                                                                                       |
| ScrollMode         | vertical_scroll_mode                   | `1`                                                                                           |

## Methods

|                                                    | ensure_control_visible(control: [Control](class_control.md#class-control))   |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [HScrollBar](class_hscrollbar.md#class-hscrollbar) | get_h_scroll_bar()                                                                 |
| [VScrollBar](class_vscrollbar.md#class-vscrollbar) | get_v_scroll_bar()                                                                 |

## Theme Properties

| [Color](class_color.md#class-color)             | scroll_hint_horizontal_color   | `Color(0, 0, 0, 1)`   |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------|
| [Color](class_color.md#class-color)             | scroll_hint_vertical_color       | `Color(0, 0, 0, 1)`   |
| [int](class_int.md#class-int)                   | scrollbar_h_separation            | `0`                   |
| [int](class_int.md#class-int)                   | scrollbar_v_separation            | `0`                   |
| [Texture2D](class_texture2d.md#class-texture2d) | scroll_hint_horizontal                |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | scroll_hint_vertical                    |                       |
| [StyleBox](class_stylebox.md#class-stylebox)    | focus                                                 |                       |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel                                                 |                       |

---

## Signals

**scroll_ended**()

Emitted when scrolling stops when dragging the scrollable area *with a touch event*. This signal is *not* emitted when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

**Note:** This signal is only emitted on Android or iOS, or on desktop/web platforms when [ProjectSettings.input_devices/pointing/emulate_touch_from_mouse](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-emulate-touch-from-mouse) is enabled.

---

**scroll_started**()

Emitted when scrolling starts when dragging the scrollable area *with a touch event*. This signal is *not* emitted when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

**Note:** This signal is only emitted on Android or iOS, or on desktop/web platforms when [ProjectSettings.input_devices/pointing/emulate_touch_from_mouse](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-emulate-touch-from-mouse) is enabled.

---

## Enumerations

enum **ScrollMode**:

ScrollMode **SCROLL_MODE_DISABLED** = `0`

Scrolling disabled, scrollbar will be invisible.

ScrollMode **SCROLL_MODE_AUTO** = `1`

Scrolling enabled, scrollbar will be visible only if necessary, i.e. container's content is bigger than the container.

ScrollMode **SCROLL_MODE_SHOW_ALWAYS** = `2`

Scrolling enabled, scrollbar will be always visible.

ScrollMode **SCROLL_MODE_SHOW_NEVER** = `3`

Scrolling enabled, scrollbar will be hidden.

ScrollMode **SCROLL_MODE_RESERVE** = `4`

Combines SCROLL_MODE_AUTO and SCROLL_MODE_SHOW_ALWAYS. The scrollbar is only visible if necessary, but the content size is adjusted as if it was always visible. It's useful for ensuring that content size stays the same regardless if the scrollbar is visible.

ScrollMode **SCROLL_MODE_MAXIMIZE_FIRST** = `5`

Behaves like SCROLL_MODE_AUTO, but makes the **ScrollContainer** report a minimum size based on its content (limited by [Control.custom_maximum_size](class_control.md#class-control-property-custom-maximum-size) when set on the corresponding axis). This allows it to grow first and only start scrolling once constrained.

---

enum **ScrollHintMode**:

ScrollHintMode **SCROLL_HINT_MODE_DISABLED** = `0`

Scroll hints will never be shown.

ScrollHintMode **SCROLL_HINT_MODE_ALL** = `1`

Scroll hints will be shown at the top and bottom (if vertical), or left and right (if horizontal).

ScrollHintMode **SCROLL_HINT_MODE_TOP_AND_LEFT** = `2`

Scroll hints will be shown at the top (if vertical), or the left (if horizontal).

ScrollHintMode **SCROLL_HINT_MODE_BOTTOM_AND_RIGHT** = `3`

Scroll hints will be shown at the bottom (if horizontal), or the right (if horizontal).

---

## Property Descriptions

[bool](class_bool.md#class-bool) **draw_focus_border** = `false`

-  **set_draw_focus_border**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_focus_border**()

If `true`, focus is drawn when the ScrollContainer or one of its descendant nodes is focused.

---

[bool](class_bool.md#class-bool) **follow_focus** = `false`

-  **set_follow_focus**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_following_focus**()

If `true`, the ScrollContainer will automatically scroll to focused children (including indirect children) to make sure they are fully visible.

---

ScrollMode **horizontal_scroll_mode** = `1`

-  **set_horizontal_scroll_mode**(value: ScrollMode)
- ScrollMode **get_horizontal_scroll_mode**()

Controls whether horizontal scrollbar can be used and when it should be visible.

---

[int](class_int.md#class-int) **scroll_deadzone** = `0`

-  **set_deadzone**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_deadzone**()

Deadzone for touch scrolling. Lower deadzone makes the scrolling more sensitive.

---

ScrollHintMode **scroll_hint_mode** = `0`

-  **set_scroll_hint_mode**(value: ScrollHintMode)
- ScrollHintMode **get_scroll_hint_mode**()

The way which scroll hints (indicators that show that the content can still be scrolled in a certain direction) will be shown.

**Note:** Hints won't be shown if the content can be scrolled both vertically and horizontally.

---

[int](class_int.md#class-int) **scroll_horizontal** = `0`

-  **set_h_scroll**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_h_scroll**()

The current horizontal scroll value.

**Note:** If you are setting this value in the [Node._ready()](class_node.md#class-node-private-method-ready) function or earlier, it needs to be wrapped with [Object.set_deferred()](class_object.md#class-object-method-set-deferred), since scroll bar's [Range.max_value](class_range.md#class-range-property-max-value) is not initialized yet.

```gdscript
func _ready():
    set_deferred("scroll_horizontal", 600)
```

---

[bool](class_bool.md#class-bool) **scroll_horizontal_by_default** = `false`

-  **set_scroll_horizontal_by_default**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_horizontal_by_default**()

If `true`, the mouse wheel scrolls the view horizontally, and holding `Shift` scrolls vertically.

If `false` (default), the mouse wheel scrolls the view vertically, and holding `Shift` scrolls horizontally.

---

[float](class_float.md#class-float) **scroll_horizontal_custom_step** = `-1.0`

-  **set_horizontal_custom_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_horizontal_custom_step**()

Overrides the [ScrollBar.custom_step](class_scrollbar.md#class-scrollbar-property-custom-step) used when clicking the internal scroll bar's horizontal increment and decrement buttons or when using arrow keys when the [ScrollBar](class_scrollbar.md#class-scrollbar) is focused.

---

[int](class_int.md#class-int) **scroll_vertical** = `0`

-  **set_v_scroll**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_v_scroll**()

The current vertical scroll value.

**Note:** Setting it early needs to be deferred, just like in scroll_horizontal.

```gdscript
func _ready():
    set_deferred("scroll_vertical", 600)
```

---

[float](class_float.md#class-float) **scroll_vertical_custom_step** = `-1.0`

-  **set_vertical_custom_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_vertical_custom_step**()

Overrides the [ScrollBar.custom_step](class_scrollbar.md#class-scrollbar-property-custom-step) used when clicking the internal scroll bar's vertical increment and decrement buttons or when using arrow keys when the [ScrollBar](class_scrollbar.md#class-scrollbar) is focused.

---

[bool](class_bool.md#class-bool) **tile_scroll_hint** = `false`

-  **set_tile_scroll_hint**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_hint_tiled**()

If `true`, the scroll hint texture will be tiled instead of stretched. See scroll_hint_mode.

---

ScrollMode **vertical_scroll_mode** = `1`

-  **set_vertical_scroll_mode**(value: ScrollMode)
- ScrollMode **get_vertical_scroll_mode**()

Controls whether vertical scrollbar can be used and when it should be visible.

---

## Method Descriptions

 **ensure_control_visible**(control: [Control](class_control.md#class-control))

Ensures the given `control` is visible (must be a direct or indirect child of the ScrollContainer). Used by follow_focus.

**Note:** This will not work on a node that was just added during the same frame. If you want to scroll to a newly added child, you must wait until the next frame using [SceneTree.process_frame](class_scenetree.md#class-scenetree-signal-process-frame):

```gdscript
add_child(child_node)
await get_tree().process_frame
ensure_control_visible(child_node)
```

---

[HScrollBar](class_hscrollbar.md#class-hscrollbar) **get_h_scroll_bar**()

Returns the horizontal scrollbar [HScrollBar](class_hscrollbar.md#class-hscrollbar) of this **ScrollContainer**.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to disable or hide a scrollbar, you can use horizontal_scroll_mode.

---

[VScrollBar](class_vscrollbar.md#class-vscrollbar) **get_v_scroll_bar**()

Returns the vertical scrollbar [VScrollBar](class_vscrollbar.md#class-vscrollbar) of this **ScrollContainer**.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to disable or hide a scrollbar, you can use vertical_scroll_mode.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **scroll_hint_horizontal_color** = `Color(0, 0, 0, 1)`

[Color](class_color.md#class-color) used to modulate the scroll_hint_horizontal texture.

---

[Color](class_color.md#class-color) **scroll_hint_vertical_color** = `Color(0, 0, 0, 1)`

[Color](class_color.md#class-color) used to modulate the scroll_hint_vertical texture.

---

[int](class_int.md#class-int) **scrollbar_h_separation** = `0`

The space between the ScrollContainer's vertical scroll bar and its content, in pixels. No space will be added when the content's minimum size is larger than the ScrollContainer's size.

---

[int](class_int.md#class-int) **scrollbar_v_separation** = `0`

The space between the ScrollContainer's horizontal scroll bar and its content, in pixels. No space will be added when the content's minimum size is larger than the ScrollContainer's size.

---

[Texture2D](class_texture2d.md#class-texture2d) **scroll_hint_horizontal**

The indicator that will be shown when the content can still be scrolled horizontally. See scroll_hint_mode.

---

[Texture2D](class_texture2d.md#class-texture2d) **scroll_hint_vertical**

The indicator that will be shown when the content can still be scrolled vertically. See scroll_hint_mode.

---

[StyleBox](class_stylebox.md#class-stylebox) **focus**

The focus border [StyleBox](class_stylebox.md#class-stylebox) of the **ScrollContainer**. Only used if draw_focus_border is `true`.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

The background [StyleBox](class_stylebox.md#class-stylebox) of the **ScrollContainer**.
