# SplitContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [HSplitContainer](class_hsplitcontainer.md#class-hsplitcontainer), [VSplitContainer](class_vsplitcontainer.md#class-vsplitcontainer)

A container that arranges child controls horizontally or vertically and provides grabbers for adjusting the split ratios between them.

## Description

A container that arranges child controls horizontally or vertically and creates grabbers between them. The grabbers can be dragged around to change the size relations between the child controls.

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

## Properties

| [bool](class_bool.md#class-bool)                                     | collapsed                                         | `false`               |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------|
| [bool](class_bool.md#class-bool)                                     | drag_area_highlight_in_editor | `false`               |
| [int](class_int.md#class-int)                                        | drag_area_margin_begin               | `0`                   |
| [int](class_int.md#class-int)                                        | drag_area_margin_end                   | `0`                   |
| [int](class_int.md#class-int)                                        | drag_area_offset                           | `0`                   |
| [bool](class_bool.md#class-bool)                                     | drag_nested_intersections         | `false`               |
| DraggerVisibility          | dragger_visibility                       | `0`                   |
| [bool](class_bool.md#class-bool)                                     | dragging_enabled                           | `true`                |
| [int](class_int.md#class-int)                                        | split_offset                                   | `0`                   |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | split_offsets                                 | `PackedInt32Array(0)` |
| [bool](class_bool.md#class-bool)                                     | touch_dragger_enabled                 | `false`               |
| [bool](class_bool.md#class-bool)                                     | vertical                                           | `false`               |

## Methods

|                                                                                | clamp_split_offset(priority_index: [int](class_int.md#class-int) = 0)   |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [Control](class_control.md#class-control)                                      | get_drag_area_control()                                              |
| [Array](class_array.md#class-array)[[Control](class_control.md#class-control)] | get_drag_area_controls()                                            |

## Theme Properties

| [Color](class_color.md#class-color)             | touch_dragger_color                 | `Color(1, 1, 1, 0.3)`   |
|-------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------|
| [Color](class_color.md#class-color)             | touch_dragger_hover_color     | `Color(1, 1, 1, 0.6)`   |
| [Color](class_color.md#class-color)             | touch_dragger_pressed_color | `Color(1, 1, 1, 1)`     |
| [int](class_int.md#class-int)                   | autohide                                    | `1`                     |
| [int](class_int.md#class-int)                   | minimum_grab_thickness        | `6`                     |
| [int](class_int.md#class-int)                   | separation                                | `12`                    |
| [Texture2D](class_texture2d.md#class-texture2d) | grabber                                          |                         |
| [Texture2D](class_texture2d.md#class-texture2d) | h_grabber                                      |                         |
| [Texture2D](class_texture2d.md#class-texture2d) | h_touch_dragger                          |                         |
| [Texture2D](class_texture2d.md#class-texture2d) | touch_dragger                              |                         |
| [Texture2D](class_texture2d.md#class-texture2d) | v_grabber                                      |                         |
| [Texture2D](class_texture2d.md#class-texture2d) | v_touch_dragger                          |                         |
| [StyleBox](class_stylebox.md#class-stylebox)    | split_bar_background               |                         |

---

## Signals

**drag_ended**()

Emitted when the user ends dragging.

---

**drag_started**()

Emitted when the user starts dragging.

---

**dragged**(offset: [int](class_int.md#class-int))

Emitted when any dragger is dragged by user.

---

## Enumerations

enum **DraggerVisibility**:

DraggerVisibility **DRAGGER_VISIBLE** = `0`

The split dragger icon is always visible when autohide is `false`, otherwise visible only when the cursor hovers it.

The size of the grabber icon determines the minimum separation.

The dragger icon is automatically hidden if the length of the grabber icon is longer than the split bar.

DraggerVisibility **DRAGGER_HIDDEN** = `1`

The split dragger icon is never visible regardless of the value of autohide.

The size of the grabber icon determines the minimum separation.

DraggerVisibility **DRAGGER_HIDDEN_COLLAPSED** = `2`

The split dragger icon is not visible, and the split bar is collapsed to zero thickness.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **collapsed** = `false`

-  **set_collapsed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collapsed**()

If `true`, the draggers will be disabled and the children will be sized as if all split_offsets were `0`.

---

[bool](class_bool.md#class-bool) **drag_area_highlight_in_editor** = `false`

-  **set_drag_area_highlight_in_editor**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drag_area_highlight_in_editor_enabled**()

Highlights the drag area [Rect2](class_rect2.md#class-rect2) so you can see where it is during development. The drag area is gold if dragging_enabled is `true`, and red if `false`.

---

[int](class_int.md#class-int) **drag_area_margin_begin** = `0`

-  **set_drag_area_margin_begin**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_drag_area_margin_begin**()

Reduces the size of the drag area and split bar split_bar_background at the beginning of the container.

---

[int](class_int.md#class-int) **drag_area_margin_end** = `0`

-  **set_drag_area_margin_end**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_drag_area_margin_end**()

Reduces the size of the drag area and split bar split_bar_background at the end of the container.

---

[int](class_int.md#class-int) **drag_area_offset** = `0`

-  **set_drag_area_offset**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_drag_area_offset**()

Shifts the drag area in the axis of the container to prevent the drag area from overlapping the [ScrollBar](class_scrollbar.md#class-scrollbar) or other selectable [Control](class_control.md#class-control) of a child node.

---

[bool](class_bool.md#class-bool) **drag_nested_intersections** = `false`

-  **set_drag_nested_intersections**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_dragging_nested_intersections**()

Adds extra draggers at the intersection of the draggers of two SplitContainers to allow dragging both at once. This must be set to `true` for both SplitContainers, and one needs to be a descendant of the other. They also must be orthogonal (their vertical are different) and the descendant must be next to at least one of the ancestor's draggers (within minimum_grab_thickness).

---

DraggerVisibility **dragger_visibility** = `0`

-  **set_dragger_visibility**(value: DraggerVisibility)
- DraggerVisibility **get_dragger_visibility**()

Determines the dragger's visibility. This property does not determine whether dragging is enabled or not. Use dragging_enabled for that.

---

[bool](class_bool.md#class-bool) **dragging_enabled** = `true`

-  **set_dragging_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_dragging_enabled**()

Enables or disables split dragging.

---

[int](class_int.md#class-int) **split_offset** = `0`

-  **set_split_offset**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_split_offset**()

**Deprecated:** Use split_offsets instead. The first element of the array is the split offset between the first two children.

The first element of split_offsets.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **split_offsets** = `PackedInt32Array(0)`

-  **set_split_offsets**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_split_offsets**()

Offsets for each dragger in pixels. Each one is the offset of the split between the [Control](class_control.md#class-control) nodes before and after the dragger, with `0` being the default position. The default position is based on the [Control](class_control.md#class-control) nodes expand flags and minimum sizes. See [Control.size_flags_horizontal](class_control.md#class-control-property-size-flags-horizontal), [Control.size_flags_vertical](class_control.md#class-control-property-size-flags-vertical), and [Control.size_flags_stretch_ratio](class_control.md#class-control-property-size-flags-stretch-ratio).

If none of the [Control](class_control.md#class-control) nodes before the dragger are expanded, the default position will be at the start of the **SplitContainer**. If none of the [Control](class_control.md#class-control) nodes after the dragger are expanded, the default position will be at the end of the **SplitContainer**. If the dragger is in between expanded [Control](class_control.md#class-control) nodes, the default position will be in the middle, based on the [Control.size_flags_stretch_ratio](class_control.md#class-control-property-size-flags-stretch-ratio)s and minimum sizes.

**Note:** If the split offsets cause [Control](class_control.md#class-control) nodes to overlap, the first split will take priority when resolving the positions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[bool](class_bool.md#class-bool) **touch_dragger_enabled** = `false`

-  **set_touch_dragger_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_touch_dragger_enabled**()

If `true`, a touch-friendly drag handle will be enabled for better usability on smaller screens. Unlike the standard grabber, this drag handle overlaps the **SplitContainer**'s children and does not affect their minimum separation. The standard grabber will no longer be drawn when this option is enabled.

---

[bool](class_bool.md#class-bool) **vertical** = `false`

-  **set_vertical**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_vertical**()

If `true`, the **SplitContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HSplitContainer](class_hsplitcontainer.md#class-hsplitcontainer) and [VSplitContainer](class_vsplitcontainer.md#class-vsplitcontainer).

---

## Method Descriptions

 **clamp_split_offset**(priority_index: [int](class_int.md#class-int) = 0)

Clamps the split_offsets values to ensure they are within valid ranges and do not overlap with each other. When overlaps occur, this method prioritizes one split offset (at index `priority_index`) by clamping any overlapping split offsets to it.

---

[Control](class_control.md#class-control) **get_drag_area_control**()

**Deprecated:** Use the first element of get_drag_area_controls() instead.

Returns the drag area [Control](class_control.md#class-control). For example, you can move a pre-configured button into the drag area [Control](class_control.md#class-control) so that it rides along with the split bar. Try setting the [Button](class_button.md#class-button) anchors to `center` prior to the `reparent()` call.

```gdscript
$BarnacleButton.reparent($SplitContainer.get_drag_area_control())
```

**Note:** The drag area [Control](class_control.md#class-control) is drawn over the **SplitContainer**'s children, so [CanvasItem](class_canvasitem.md#class-canvasitem) draw objects called from the [Control](class_control.md#class-control) and children added to the [Control](class_control.md#class-control) will also appear over the **SplitContainer**'s children. Try setting [Control.mouse_filter](class_control.md#class-control-property-mouse-filter) of custom children to [Control.MOUSE_FILTER_IGNORE](class_control.md#class-control-constant-mouse-filter-ignore) to prevent blocking the mouse from dragging if desired.

**Warning:** This is a required internal node, removing and freeing it may cause a crash.

---

[Array](class_array.md#class-array)[[Control](class_control.md#class-control)] **get_drag_area_controls**()

Returns an [Array](class_array.md#class-array) of the drag area [Control](class_control.md#class-control)s. These are the interactable [Control](class_control.md#class-control) nodes between each child. For example, this can be used to add a pre-configured button to a drag area [Control](class_control.md#class-control) so that it rides along with the split bar. Try setting the [Button](class_button.md#class-button) anchors to `center` prior to the [Node.reparent()](class_node.md#class-node-method-reparent) call.

```gdscript
$BarnacleButton.reparent($SplitContainer.get_drag_area_controls()[0])
```

**Note:** The drag area [Control](class_control.md#class-control)s are drawn over the **SplitContainer**'s children, so [CanvasItem](class_canvasitem.md#class-canvasitem) draw objects called from a drag area and children added to it will also appear over the **SplitContainer**'s children. Try setting [Control.mouse_filter](class_control.md#class-control-property-mouse-filter) of custom children to [Control.MOUSE_FILTER_IGNORE](class_control.md#class-control-constant-mouse-filter-ignore) to prevent blocking the mouse from dragging if desired.

**Warning:** These are required internal nodes, removing or freeing them may cause a crash.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **touch_dragger_color** = `Color(1, 1, 1, 0.3)`

The color of the touch dragger.

---

[Color](class_color.md#class-color) **touch_dragger_hover_color** = `Color(1, 1, 1, 0.6)`

The color of the touch dragger when hovered.

---

[Color](class_color.md#class-color) **touch_dragger_pressed_color** = `Color(1, 1, 1, 1)`

The color of the touch dragger when pressed.

---

[int](class_int.md#class-int) **autohide** = `1`

Boolean value. If `1` (`true`), the grabbers will hide automatically when they aren't under the cursor. If `0` (`false`), the grabbers are always visible. The dragger_visibility must be DRAGGER_VISIBLE.

---

[int](class_int.md#class-int) **minimum_grab_thickness** = `6`

The minimum thickness of the area users can click on to grab a split bar. This ensures that the split bar can still be dragged if separation or h_grabber / v_grabber's size is too narrow to easily select.

---

[int](class_int.md#class-int) **separation** = `12`

The split bar thickness, i.e., the gap between each child of the container. This is overridden by the size of the grabber icon if dragger_visibility is set to DRAGGER_VISIBLE, or DRAGGER_HIDDEN, and separation is smaller than the size of the grabber icon in the same axis.

**Note:** To obtain separation values less than the size of the grabber icon, for example a `1 px` hairline, set h_grabber or v_grabber to a new [ImageTexture](class_imagetexture.md#class-imagetexture), which effectively sets the grabber icon size to `0 px`.

---

[Texture2D](class_texture2d.md#class-texture2d) **grabber**

The icon used for the grabbers drawn in the separations. This is only used in [HSplitContainer](class_hsplitcontainer.md#class-hsplitcontainer) and [VSplitContainer](class_vsplitcontainer.md#class-vsplitcontainer). For **SplitContainer**, see h_grabber and v_grabber instead.

---

[Texture2D](class_texture2d.md#class-texture2d) **h_grabber**

The icon used for the grabbers drawn in the separations when vertical is `false`.

---

[Texture2D](class_texture2d.md#class-texture2d) **h_touch_dragger**

The icon used for the drag handle when touch_dragger_enabled is `true` and vertical is `false`.

---

[Texture2D](class_texture2d.md#class-texture2d) **touch_dragger**

The icon used for the drag handle when touch_dragger_enabled is `true`. This is only used in [HSplitContainer](class_hsplitcontainer.md#class-hsplitcontainer) and [VSplitContainer](class_vsplitcontainer.md#class-vsplitcontainer). For **SplitContainer**, see h_touch_dragger and v_touch_dragger instead.

---

[Texture2D](class_texture2d.md#class-texture2d) **v_grabber**

The icon used for the grabbers drawn in the separations when vertical is `true`.

---

[Texture2D](class_texture2d.md#class-texture2d) **v_touch_dragger**

The icon used for the drag handle when touch_dragger_enabled is `true` and vertical is `true`.

---

[StyleBox](class_stylebox.md#class-stylebox) **split_bar_background**

Determines the background of the split bar if its thickness is greater than zero.
