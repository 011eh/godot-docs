# ItemList

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A vertical list of selectable items with one or multiple columns.

## Description

This control provides a vertical list of selectable items that may be in a single or in multiple columns, with each item having options for text and an icon. Tooltips are supported and may be different for every item in the list.

Selectable items in the list may be selected or deselected and multiple selection may be enabled. Selection with right mouse button may also be enabled to allow use of popup context menus. Items may also be "activated" by double-clicking them or by pressing `Enter`.

Item text only supports single-line strings. Newline characters (e.g. `\n`) in the string won't produce a newline. Text wrapping is enabled in ICON_MODE_TOP mode, but the column's width is adjusted to fully fit its content by default. You need to set fixed_column_width greater than zero to wrap the text.

All `set_*` methods allow negative item indices, i.e. `-1` to access the last item, `-2` to select the second-to-last item, and so on.

**Incremental search:** Like [PopupMenu](class_popupmenu.md#class-popupmenu) and [Tree](class_tree.md#class-tree), **ItemList** supports searching within the list while the control is focused. Press a key that matches the first letter of an item's name to select the first item starting with the given letter. After that point, there are two ways to perform incremental search: 1) Press the same key again before the timeout duration to select the next item starting with the same letter. 2) Press letter keys that match the rest of the word before the timeout duration to match to select the item in question directly. Both of these actions will be reset to the beginning of the list if the timeout duration has passed since the last keystroke was registered. You can adjust the timeout duration by changing [ProjectSettings.gui/timers/incremental_search_max_interval_msec](class_projectsettings.md#class-projectsettings-property-gui-timers-incremental-search-max-interval-msec).

## Properties

| [bool](class_bool.md#class-bool)                                       | allow_reselect                 | `false`                                                                             |
|------------------------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                       | allow_rmb_select             | `false`                                                                             |
| [bool](class_bool.md#class-bool)                                       | allow_search                     | `true`                                                                              |
| [bool](class_bool.md#class-bool)                                       | auto_height                       | `false`                                                                             |
| [bool](class_bool.md#class-bool)                                       | auto_width                         | `false`                                                                             |
| [bool](class_bool.md#class-bool)                                       | clip_contents                                                             | `true` (overrides [Control](class_control.md#class-control-property-clip-contents)) |
| [int](class_int.md#class-int)                                          | fixed_column_width         | `0`                                                                                 |
| [Vector2i](class_vector2i.md#class-vector2i)                           | fixed_icon_size               | `Vector2i(0, 0)`                                                                    |
| [FocusMode](class_control.md#enum-control-focusmode)                   | focus_mode                                                                | `2` (overrides [Control](class_control.md#class-control-property-focus-mode))       |
| IconMode                                    | icon_mode                           | `1`                                                                                 |
| [float](class_float.md#class-float)                                    | icon_scale                         | `1.0`                                                                               |
| [int](class_int.md#class-int)                                          | item_count                         | `0`                                                                                 |
| [bool](class_bool.md#class-bool)                                       | item_{index}/disabled     | `false`                                                                             |
| [Texture2D](class_texture2d.md#class-texture2d)                        | item_{index}/icon             |                                                                                     |
| [bool](class_bool.md#class-bool)                                       | item_{index}/selectable | `true`                                                                              |
| [String](class_string.md#class-string)                                 | item_{index}/text             | `""`                                                                                |
| [int](class_int.md#class-int)                                          | max_columns                       | `1`                                                                                 |
| [int](class_int.md#class-int)                                          | max_text_lines                 | `1`                                                                                 |
| [bool](class_bool.md#class-bool)                                       | same_column_width           | `false`                                                                             |
| ScrollHintMode                        | scroll_hint_mode             | `0`                                                                                 |
| SelectMode                                | select_mode                       | `0`                                                                                 |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) | text_overrun_behavior   | `3`                                                                                 |
| [bool](class_bool.md#class-bool)                                       | tile_scroll_hint             | `false`                                                                             |
| [bool](class_bool.md#class-bool)                                       | wraparound_items             | `true`                                                                              |

## Methods

| [int](class_int.md#class-int)                                        | add_icon_item(icon: [Texture2D](class_texture2d.md#class-texture2d), selectable: [bool](class_bool.md#class-bool) = true)                                            |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                        | add_item(text: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d) = null, selectable: [bool](class_bool.md#class-bool) = true) |
|                                                                      | center_on_current(center_verically: [bool](class_bool.md#class-bool) = true, center_horizontally: [bool](class_bool.md#class-bool) = true)                       |
|                                                                      | clear()                                                                                                                                                                      |
|                                                                      | deselect(idx: [int](class_int.md#class-int))                                                                                                                              |
|                                                                      | deselect_all()                                                                                                                                                        |
|                                                                      | ensure_current_is_visible()                                                                                                                              |
|                                                                      | force_update_list_size()                                                                                                                                    |
| [HScrollBar](class_hscrollbar.md#class-hscrollbar)                   | get_h_scroll_bar()                                                                                                                                                |
| [int](class_int.md#class-int)                                        | get_item_at_position(position: [Vector2](class_vector2.md#class-vector2), exact: [bool](class_bool.md#class-bool) = false)                                    |
| [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)       | get_item_auto_translate_mode(idx: [int](class_int.md#class-int))                                                                                      |
| [Color](class_color.md#class-color)                                  | get_item_custom_bg_color(idx: [int](class_int.md#class-int))                                                                                              |
| [Color](class_color.md#class-color)                                  | get_item_custom_fg_color(idx: [int](class_int.md#class-int))                                                                                              |
| [Texture2D](class_texture2d.md#class-texture2d)                      | get_item_icon(idx: [int](class_int.md#class-int))                                                                                                                    |
| [Color](class_color.md#class-color)                                  | get_item_icon_modulate(idx: [int](class_int.md#class-int))                                                                                                  |
| [Rect2](class_rect2.md#class-rect2)                                  | get_item_icon_region(idx: [int](class_int.md#class-int))                                                                                                      |
| [String](class_string.md#class-string)                               | get_item_language(idx: [int](class_int.md#class-int))                                                                                                            |
| [Variant](class_variant.md#class-variant)                            | get_item_metadata(idx: [int](class_int.md#class-int))                                                                                                            |
| [Rect2](class_rect2.md#class-rect2)                                  | get_item_rect(idx: [int](class_int.md#class-int), expand: [bool](class_bool.md#class-bool) = true)                                                                   |
| [String](class_string.md#class-string)                               | get_item_text(idx: [int](class_int.md#class-int))                                                                                                                    |
| [TextDirection](class_control.md#enum-control-textdirection)         | get_item_text_direction(idx: [int](class_int.md#class-int))                                                                                                |
| [String](class_string.md#class-string)                               | get_item_tooltip(idx: [int](class_int.md#class-int))                                                                                                              |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | get_selected_items()                                                                                                                                            |
| [VScrollBar](class_vscrollbar.md#class-vscrollbar)                   | get_v_scroll_bar()                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                     | is_anything_selected()                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                     | is_item_disabled(idx: [int](class_int.md#class-int))                                                                                                              |
| [bool](class_bool.md#class-bool)                                     | is_item_icon_transposed(idx: [int](class_int.md#class-int))                                                                                                |
| [bool](class_bool.md#class-bool)                                     | is_item_selectable(idx: [int](class_int.md#class-int))                                                                                                          |
| [bool](class_bool.md#class-bool)                                     | is_item_tooltip_enabled(idx: [int](class_int.md#class-int))                                                                                                |
| [bool](class_bool.md#class-bool)                                     | is_selected(idx: [int](class_int.md#class-int))                                                                                                                        |
|                                                                      | move_item(from_idx: [int](class_int.md#class-int), to_idx: [int](class_int.md#class-int))                                                                                |
|                                                                      | remove_item(idx: [int](class_int.md#class-int))                                                                                                                        |
|                                                                      | select(idx: [int](class_int.md#class-int), single: [bool](class_bool.md#class-bool) = true)                                                                                 |
|                                                                      | set_item_auto_translate_mode(idx: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode))                |
|                                                                      | set_item_custom_bg_color(idx: [int](class_int.md#class-int), custom_bg_color: [Color](class_color.md#class-color))                                        |
|                                                                      | set_item_custom_fg_color(idx: [int](class_int.md#class-int), custom_fg_color: [Color](class_color.md#class-color))                                        |
|                                                                      | set_item_disabled(idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                |
|                                                                      | set_item_icon(idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))                                                             |
|                                                                      | set_item_icon_modulate(idx: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color))                                                   |
|                                                                      | set_item_icon_region(idx: [int](class_int.md#class-int), rect: [Rect2](class_rect2.md#class-rect2))                                                           |
|                                                                      | set_item_icon_transposed(idx: [int](class_int.md#class-int), transposed: [bool](class_bool.md#class-bool))                                                |
|                                                                      | set_item_language(idx: [int](class_int.md#class-int), language: [String](class_string.md#class-string))                                                          |
|                                                                      | set_item_metadata(idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))                                                       |
|                                                                      | set_item_selectable(idx: [int](class_int.md#class-int), selectable: [bool](class_bool.md#class-bool))                                                          |
|                                                                      | set_item_text(idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                      |
|                                                                      | set_item_text_direction(idx: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection))                       |
|                                                                      | set_item_tooltip(idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                                             |
|                                                                      | set_item_tooltip_enabled(idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                    |
|                                                                      | sort_items_by_text()                                                                                                                                            |

## Theme Properties

| [Color](class_color.md#class-color)             | font_color                                   | `Color(0.65, 0.65, 0.65, 1)`   |
|-------------------------------------------------|----------------------------------------------------------------------------------------|--------------------------------|
| [Color](class_color.md#class-color)             | font_hovered_color                   | `Color(0.95, 0.95, 0.95, 1)`   |
| [Color](class_color.md#class-color)             | font_hovered_selected_color | `Color(1, 1, 1, 1)`            |
| [Color](class_color.md#class-color)             | font_outline_color                   | `Color(0, 0, 0, 1)`            |
| [Color](class_color.md#class-color)             | font_selected_color                 | `Color(1, 1, 1, 1)`            |
| [Color](class_color.md#class-color)             | guide_color                                 | `Color(0.7, 0.7, 0.7, 0.25)`   |
| [Color](class_color.md#class-color)             | scroll_hint_color                     | `Color(0, 0, 0, 1)`            |
| [int](class_int.md#class-int)                   | h_separation                            | `4`                            |
| [int](class_int.md#class-int)                   | icon_margin                              | `4`                            |
| [int](class_int.md#class-int)                   | line_separation                      | `2`                            |
| [int](class_int.md#class-int)                   | outline_size                            | `0`                            |
| [int](class_int.md#class-int)                   | v_separation                            | `4`                            |
| [Font](class_font.md#class-font)                | font                                                |                                |
| [int](class_int.md#class-int)                   | font_size                                 |                                |
| [Texture2D](class_texture2d.md#class-texture2d) | scroll_hint                                  |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | cursor                                           |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | cursor_unfocused                       |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | focus                                             |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | hovered                                         |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | hovered_selected                       |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | hovered_selected_focus           |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel                                             |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | selected                                       |                                |
| [StyleBox](class_stylebox.md#class-stylebox)    | selected_focus                           |                                |

---

## Signals

**empty_clicked**(at_position: [Vector2](class_vector2.md#class-vector2), mouse_button_index: [int](class_int.md#class-int))

Emitted when any mouse click is issued within the rect of the list but on empty space.

`at_position` is the click position in this control's local coordinate system.

---

**item_activated**(index: [int](class_int.md#class-int))

Emitted when specified list item is activated via double-clicking or by pressing `Enter`.

---

**item_clicked**(index: [int](class_int.md#class-int), at_position: [Vector2](class_vector2.md#class-vector2), mouse_button_index: [int](class_int.md#class-int))

Emitted when specified list item has been clicked with any mouse button.

`at_position` is the click position in this control's local coordinate system.

---

**item_selected**(index: [int](class_int.md#class-int))

Emitted when specified item has been selected. Only applicable in single selection mode.

allow_reselect must be enabled to reselect an item.

---

**multi_selected**(index: [int](class_int.md#class-int), selected: [bool](class_bool.md#class-bool))

Emitted when a multiple selection is altered on a list allowing multiple selection.

---

## Enumerations

enum **IconMode**:

IconMode **ICON_MODE_TOP** = `0`

Icon is drawn above the text.

IconMode **ICON_MODE_LEFT** = `1`

Icon is drawn to the left of the text.

---

enum **SelectMode**:

SelectMode **SELECT_SINGLE** = `0`

Only allow selecting a single item.

SelectMode **SELECT_MULTI** = `1`

Allows selecting multiple items by holding `Ctrl` or `Shift`.

SelectMode **SELECT_TOGGLE** = `2`

Allows selecting multiple items by toggling them on and off.

---

enum **ScrollHintMode**:

ScrollHintMode **SCROLL_HINT_MODE_DISABLED** = `0`

Scroll hints will never be shown.

ScrollHintMode **SCROLL_HINT_MODE_BOTH** = `1`

Scroll hints will be shown at the top and bottom.

ScrollHintMode **SCROLL_HINT_MODE_TOP** = `2`

Only the top scroll hint will be shown.

ScrollHintMode **SCROLL_HINT_MODE_BOTTOM** = `3`

Only the bottom scroll hint will be shown.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_reselect** = `false`

-  **set_allow_reselect**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_reselect**()

If `true`, the currently selected item can be selected again.

---

[bool](class_bool.md#class-bool) **allow_rmb_select** = `false`

-  **set_allow_rmb_select**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_rmb_select**()

If `true`, right mouse button click can select items.

---

[bool](class_bool.md#class-bool) **allow_search** = `true`

-  **set_allow_search**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_search**()

If `true`, allows navigating the **ItemList** with letter keys through incremental search.

---

[bool](class_bool.md#class-bool) **auto_height** = `false`

-  **set_auto_height**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_auto_height**()

If `true`, the control will automatically resize the height to fit its content.

---

[bool](class_bool.md#class-bool) **auto_width** = `false`

-  **set_auto_width**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_auto_width**()

If `true`, the control will automatically resize the width to fit its content.

---

[int](class_int.md#class-int) **fixed_column_width** = `0`

-  **set_fixed_column_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fixed_column_width**()

The width all columns will be adjusted to.

A value of zero disables the adjustment, each item will have a width equal to the width of its content and the columns will have an uneven width.

---

[Vector2i](class_vector2i.md#class-vector2i) **fixed_icon_size** = `Vector2i(0, 0)`

-  **set_fixed_icon_size**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_fixed_icon_size**()

The size all icons will be adjusted to.

If either X or Y component is not greater than zero, icon size won't be affected.

---

IconMode **icon_mode** = `1`

-  **set_icon_mode**(value: IconMode)
- IconMode **get_icon_mode**()

The icon position, whether above or to the left of the text. See the IconMode constants.

---

[float](class_float.md#class-float) **icon_scale** = `1.0`

-  **set_icon_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_icon_scale**()

The scale of icon applied after fixed_icon_size and transposing takes effect.

---

[int](class_int.md#class-int) **item_count** = `0`

-  **set_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_count**()

The number of items currently in the list.

---

[bool](class_bool.md#class-bool) **item_{index}/disabled** = `false`

If `true`, the item at `index` is disabled.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[Texture2D](class_texture2d.md#class-texture2d) **item_{index}/icon**

The icon of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[bool](class_bool.md#class-bool) **item_{index}/selectable** = `true`

If `true`, the item at `index` is selectable.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[String](class_string.md#class-string) **item_{index}/text** = `""`

The text of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[int](class_int.md#class-int) **max_columns** = `1`

-  **set_max_columns**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_columns**()

Maximum columns the list will have.

If greater than zero, the content will be split among the specified columns.

A value of zero means unlimited columns, i.e. all items will be put in the same row.

---

[int](class_int.md#class-int) **max_text_lines** = `1`

-  **set_max_text_lines**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_text_lines**()

Maximum lines of text allowed in each item. Space will be reserved even when there is not enough lines of text to display.

**Note:** This property takes effect only when icon_mode is ICON_MODE_TOP. To make the text wrap, fixed_column_width should be greater than zero.

---

[bool](class_bool.md#class-bool) **same_column_width** = `false`

-  **set_same_column_width**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_same_column_width**()

Whether all columns will have the same width.

If `true`, the width is equal to the largest column width of all columns.

---

ScrollHintMode **scroll_hint_mode** = `0`

-  **set_scroll_hint_mode**(value: ScrollHintMode)
- ScrollHintMode **get_scroll_hint_mode**()

The way which scroll hints (indicators that show that the content can still be scrolled in a certain direction) will be shown.

---

SelectMode **select_mode** = `0`

-  **set_select_mode**(value: SelectMode)
- SelectMode **get_select_mode**()

Allows single or multiple item selection. See the SelectMode constants.

---

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **text_overrun_behavior** = `3`

-  **set_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**()

The clipping behavior when the text exceeds an item's bounding rectangle.

---

[bool](class_bool.md#class-bool) **tile_scroll_hint** = `false`

-  **set_tile_scroll_hint**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_hint_tiled**()

If `true`, the scroll hint texture will be tiled instead of stretched. See scroll_hint_mode.

---

[bool](class_bool.md#class-bool) **wraparound_items** = `true`

-  **set_wraparound_items**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_wraparound_items**()

If `true`, the control will automatically move items into a new row to fit its content. See also [HFlowContainer](class_hflowcontainer.md#class-hflowcontainer) for this behavior.

If `false`, the control will add a horizontal scrollbar to make all items visible.

---

## Method Descriptions

[int](class_int.md#class-int) **add_icon_item**(icon: [Texture2D](class_texture2d.md#class-texture2d), selectable: [bool](class_bool.md#class-bool) = true)

Adds an item to the item list with no text, only an icon. Returns the index of an added item.

---

[int](class_int.md#class-int) **add_item**(text: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d) = null, selectable: [bool](class_bool.md#class-bool) = true)

Adds an item to the item list with specified text. Returns the index of an added item.

Specify an `icon`, or use `null` as the `icon` for a list item with no icon.

If `selectable` is `true`, the list item will be selectable.

---

 **center_on_current**(center_verically: [bool](class_bool.md#class-bool) = true, center_horizontally: [bool](class_bool.md#class-bool) = true)

Ensures the currently selected item (the first selected item if multiple selection is enabled) is visible, adjusting the scroll position as necessary to place the item at the center of the list if possible. See also ensure_current_is_visible().

Fails and prints an error if both arguments are `false`.

---

 **clear**()

Removes all items from the list.

---

 **deselect**(idx: [int](class_int.md#class-int))

Ensures the item associated with the specified index is not selected.

---

 **deselect_all**()

Ensures there are no items selected.

---

 **ensure_current_is_visible**()

Ensures the currently selected item (the first selected item if multiple selection is enabled) is visible, adjusting the scroll position as necessary. See also center_on_current().

---

 **force_update_list_size**()

Forces an update to the list size based on its items. This happens automatically whenever size of the items, or other relevant settings like auto_height, change. The method can be used to trigger the update ahead of next drawing pass.

---

[HScrollBar](class_hscrollbar.md#class-hscrollbar) **get_h_scroll_bar**()

Returns the horizontal scrollbar.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

[int](class_int.md#class-int) **get_item_at_position**(position: [Vector2](class_vector2.md#class-vector2), exact: [bool](class_bool.md#class-bool) = false)

Returns the item index at the given `position`.

When there is no item at that point, -1 will be returned if `exact` is `true`, and the closest item index will be returned otherwise.

**Note:** The returned value is unreliable if called right after modifying the **ItemList**, before it redraws in the next frame.

---

[AutoTranslateMode](class_node.md#enum-node-autotranslatemode) **get_item_auto_translate_mode**(idx: [int](class_int.md#class-int))

Returns item's auto translate mode.

---

[Color](class_color.md#class-color) **get_item_custom_bg_color**(idx: [int](class_int.md#class-int))

Returns the custom background color of the item specified by `idx` index.

---

[Color](class_color.md#class-color) **get_item_custom_fg_color**(idx: [int](class_int.md#class-int))

Returns the custom foreground color of the item specified by `idx` index.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_item_icon**(idx: [int](class_int.md#class-int))

Returns the icon associated with the specified index.

---

[Color](class_color.md#class-color) **get_item_icon_modulate**(idx: [int](class_int.md#class-int))

Returns a [Color](class_color.md#class-color) modulating item's icon at the specified index.

---

[Rect2](class_rect2.md#class-rect2) **get_item_icon_region**(idx: [int](class_int.md#class-int))

Returns the region of item's icon used. The whole icon will be used if the region has no area.

---

[String](class_string.md#class-string) **get_item_language**(idx: [int](class_int.md#class-int))

Returns item's text language code.

---

[Variant](class_variant.md#class-variant) **get_item_metadata**(idx: [int](class_int.md#class-int))

Returns the metadata value of the specified index.

---

[Rect2](class_rect2.md#class-rect2) **get_item_rect**(idx: [int](class_int.md#class-int), expand: [bool](class_bool.md#class-bool) = true)

Returns the position and size of the item with the specified index, in the coordinate system of the **ItemList** node. If `expand` is `true` the last column expands to fill the rest of the row.

**Note:** The returned value is unreliable if called right after modifying the **ItemList**, before it redraws in the next frame.

---

[String](class_string.md#class-string) **get_item_text**(idx: [int](class_int.md#class-int))

Returns the text associated with the specified index.

---

[TextDirection](class_control.md#enum-control-textdirection) **get_item_text_direction**(idx: [int](class_int.md#class-int))

Returns item's text base writing direction.

---

[String](class_string.md#class-string) **get_item_tooltip**(idx: [int](class_int.md#class-int))

Returns the tooltip hint associated with the specified index.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_selected_items**()

Returns an array with the indexes of the selected items.

---

[VScrollBar](class_vscrollbar.md#class-vscrollbar) **get_v_scroll_bar**()

Returns the vertical scrollbar.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

[bool](class_bool.md#class-bool) **is_anything_selected**()

Returns `true` if one or more items are selected.

---

[bool](class_bool.md#class-bool) **is_item_disabled**(idx: [int](class_int.md#class-int))

Returns `true` if the item at the specified index is disabled.

---

[bool](class_bool.md#class-bool) **is_item_icon_transposed**(idx: [int](class_int.md#class-int))

Returns `true` if the item icon will be drawn transposed, i.e. the X and Y axes are swapped.

---

[bool](class_bool.md#class-bool) **is_item_selectable**(idx: [int](class_int.md#class-int))

Returns `true` if the item at the specified index is selectable.

---

[bool](class_bool.md#class-bool) **is_item_tooltip_enabled**(idx: [int](class_int.md#class-int))

Returns `true` if the tooltip is enabled for specified item index.

---

[bool](class_bool.md#class-bool) **is_selected**(idx: [int](class_int.md#class-int))

Returns `true` if the item at the specified index is currently selected.

---

 **move_item**(from_idx: [int](class_int.md#class-int), to_idx: [int](class_int.md#class-int))

Moves item from index `from_idx` to `to_idx`.

---

 **remove_item**(idx: [int](class_int.md#class-int))

Removes the item specified by `idx` index from the list.

---

 **select**(idx: [int](class_int.md#class-int), single: [bool](class_bool.md#class-bool) = true)

Selects the item at the specified index.

**Note:** This method does not trigger the item selection signal.

---

 **set_item_auto_translate_mode**(idx: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode))

Sets the auto translate mode of the item associated with the specified index.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class-node-constant-auto-translate-mode-inherit) by default, which uses the same auto translate mode as the **ItemList** itself.

---

 **set_item_custom_bg_color**(idx: [int](class_int.md#class-int), custom_bg_color: [Color](class_color.md#class-color))

Sets the background color of the item specified by `idx` index to the specified [Color](class_color.md#class-color).

---

 **set_item_custom_fg_color**(idx: [int](class_int.md#class-int), custom_fg_color: [Color](class_color.md#class-color))

Sets the foreground color of the item specified by `idx` index to the specified [Color](class_color.md#class-color).

---

 **set_item_disabled**(idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

Disables (or enables) the item at the specified index.

Disabled items cannot be selected and do not trigger activation signals (when double-clicking or pressing `Enter`).

---

 **set_item_icon**(idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets (or replaces) the icon's [Texture2D](class_texture2d.md#class-texture2d) associated with the specified index.

---

 **set_item_icon_modulate**(idx: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color))

Sets a modulating [Color](class_color.md#class-color) of the item associated with the specified index.

---

 **set_item_icon_region**(idx: [int](class_int.md#class-int), rect: [Rect2](class_rect2.md#class-rect2))

Sets the region of item's icon used. The whole icon will be used if the region has no area.

---

 **set_item_icon_transposed**(idx: [int](class_int.md#class-int), transposed: [bool](class_bool.md#class-bool))

Sets whether the item icon will be drawn transposed.

---

 **set_item_language**(idx: [int](class_int.md#class-int), language: [String](class_string.md#class-string))

Sets the language code of the text for the item at the given index to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---

 **set_item_metadata**(idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))

Sets a value (of any type) to be stored with the item associated with the specified index.

---

 **set_item_selectable**(idx: [int](class_int.md#class-int), selectable: [bool](class_bool.md#class-bool))

Allows or disallows selection of the item associated with the specified index.

---

 **set_item_text**(idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

Sets text of the item associated with the specified index.

---

 **set_item_text_direction**(idx: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection))

Sets item's text base writing direction.

---

 **set_item_tooltip**(idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets the tooltip hint for the item associated with the specified index.

---

 **set_item_tooltip_enabled**(idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

Sets whether the tooltip hint is enabled for specified item index.

---

 **sort_items_by_text**()

Sorts items in the list by their text.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **font_color** = `Color(0.65, 0.65, 0.65, 1)`

Default text [Color](class_color.md#class-color) of the item.

---

[Color](class_color.md#class-color) **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)`

Text [Color](class_color.md#class-color) used when the item is hovered and not selected yet.

---

[Color](class_color.md#class-color) **font_hovered_selected_color** = `Color(1, 1, 1, 1)`

Text [Color](class_color.md#class-color) used when the item is hovered and selected.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The tint of text outline of the item.

---

[Color](class_color.md#class-color) **font_selected_color** = `Color(1, 1, 1, 1)`

Text [Color](class_color.md#class-color) used when the item is selected, but not hovered.

---

[Color](class_color.md#class-color) **guide_color** = `Color(0.7, 0.7, 0.7, 0.25)`

[Color](class_color.md#class-color) of the guideline. The guideline is a line drawn between each row of items.

---

[Color](class_color.md#class-color) **scroll_hint_color** = `Color(0, 0, 0, 1)`

[Color](class_color.md#class-color) used to modulate the scroll_hint texture.

---

[int](class_int.md#class-int) **h_separation** = `4`

The horizontal spacing between items.

---

[int](class_int.md#class-int) **icon_margin** = `4`

The spacing between item's icon and text.

---

[int](class_int.md#class-int) **line_separation** = `2`

The vertical spacing between each line of text.

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the item text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[int](class_int.md#class-int) **v_separation** = `4`

The vertical spacing between items.

---

[Font](class_font.md#class-font) **font**

[Font](class_font.md#class-font) of the item's text.

---

[int](class_int.md#class-int) **font_size**

Font size of the item's text.

---

[Texture2D](class_texture2d.md#class-texture2d) **scroll_hint**

The indicator that will be shown when the content can still be scrolled. See scroll_hint_mode.

---

[StyleBox](class_stylebox.md#class-stylebox) **cursor**

[StyleBox](class_stylebox.md#class-stylebox) used for the cursor, when the **ItemList** is being focused.

---

[StyleBox](class_stylebox.md#class-stylebox) **cursor_unfocused**

[StyleBox](class_stylebox.md#class-stylebox) used for the cursor, when the **ItemList** is not being focused.

---

[StyleBox](class_stylebox.md#class-stylebox) **focus**

The focused style for the **ItemList**, drawn on top of everything.

---

[StyleBox](class_stylebox.md#class-stylebox) **hovered**

[StyleBox](class_stylebox.md#class-stylebox) for the hovered, but not selected items.

---

[StyleBox](class_stylebox.md#class-stylebox) **hovered_selected**

[StyleBox](class_stylebox.md#class-stylebox) for the hovered and selected items, used when the **ItemList** is not being focused.

---

[StyleBox](class_stylebox.md#class-stylebox) **hovered_selected_focus**

[StyleBox](class_stylebox.md#class-stylebox) for the hovered and selected items, used when the **ItemList** is being focused.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

The background style for the **ItemList**.

---

[StyleBox](class_stylebox.md#class-stylebox) **selected**

[StyleBox](class_stylebox.md#class-stylebox) for the selected items, used when the **ItemList** is not being focused.

---

[StyleBox](class_stylebox.md#class-stylebox) **selected_focus**

[StyleBox](class_stylebox.md#class-stylebox) for the selected items, used when the **ItemList** is being focused.
