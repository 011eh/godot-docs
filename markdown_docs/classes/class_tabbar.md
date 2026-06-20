# TabBar

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control that provides a horizontal bar with tabs.

## Description

A control that provides a horizontal bar with tabs. Similar to [TabContainer](class_tabcontainer.md#class-tabcontainer) but is only in charge of drawing tabs, not interacting with children.

## Properties

| [bool](class_bool.md#class-bool)                                  | clip_tabs                                 | `true`                                                                        |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                  | close_with_middle_mouse     | `true`                                                                        |
| [int](class_int.md#class-int)                                     | current_tab                             | `-1`                                                                          |
| [bool](class_bool.md#class-bool)                                  | deselect_enabled                   | `false`                                                                       |
| [bool](class_bool.md#class-bool)                                  | drag_to_rearrange_enabled | `false`                                                                       |
| [FocusMode](class_control.md#enum-control-focusmode)              | focus_mode                                                                    | `2` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [int](class_int.md#class-int)                                     | max_tab_width                         | `0`                                                                           |
| [bool](class_bool.md#class-bool)                                  | scroll_to_selected               | `true`                                                                        |
| [bool](class_bool.md#class-bool)                                  | scrolling_enabled                 | `true`                                                                        |
| [bool](class_bool.md#class-bool)                                  | select_with_rmb                     | `false`                                                                       |
| [bool](class_bool.md#class-bool)                                  | switch_on_drag_hover           | `true`                                                                        |
| AlignmentMode                       | tab_alignment                         | `0`                                                                           |
| CloseButtonDisplayPolicy | tab_close_display_policy   | `0`                                                                           |
| [int](class_int.md#class-int)                                     | tab_count                                 | `0`                                                                           |
| [bool](class_bool.md#class-bool)                                  | tab_{index}/disabled             | `false`                                                                       |
| [Texture2D](class_texture2d.md#class-texture2d)                   | tab_{index}/icon                     |                                                                               |
| [String](class_string.md#class-string)                            | tab_{index}/title                   | `""`                                                                          |
| [String](class_string.md#class-string)                            | tab_{index}/tooltip               | `""`                                                                          |
| [int](class_int.md#class-int)                                     | tabs_rearrange_group           | `-1`                                                                          |

## Methods

|                                                              | add_tab(title: [String](class_string.md#class-string) = "", icon: [Texture2D](class_texture2d.md#class-texture2d) = null)                              |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                              | clear_tabs()                                                                                                                                        |
|                                                              | ensure_tab_visible(idx: [int](class_int.md#class-int))                                                                                      |
| [bool](class_bool.md#class-bool)                             | get_offset_buttons_visible()                                                                                                        |
| [int](class_int.md#class-int)                                | get_previous_tab()                                                                                                                            |
| [Texture2D](class_texture2d.md#class-texture2d)              | get_tab_button_icon(tab_idx: [int](class_int.md#class-int))                                                                                |
| [Texture2D](class_texture2d.md#class-texture2d)              | get_tab_icon(tab_idx: [int](class_int.md#class-int))                                                                                              |
| [int](class_int.md#class-int)                                | get_tab_icon_max_width(tab_idx: [int](class_int.md#class-int))                                                                          |
| [int](class_int.md#class-int)                                | get_tab_idx_at_point(point: [Vector2](class_vector2.md#class-vector2))                                                                    |
| [String](class_string.md#class-string)                       | get_tab_language(tab_idx: [int](class_int.md#class-int))                                                                                      |
| [Variant](class_variant.md#class-variant)                    | get_tab_metadata(tab_idx: [int](class_int.md#class-int))                                                                                      |
| [int](class_int.md#class-int)                                | get_tab_offset()                                                                                                                                |
| [Rect2](class_rect2.md#class-rect2)                          | get_tab_rect(tab_idx: [int](class_int.md#class-int))                                                                                              |
| [TextDirection](class_control.md#enum-control-textdirection) | get_tab_text_direction(tab_idx: [int](class_int.md#class-int))                                                                          |
| [String](class_string.md#class-string)                       | get_tab_title(tab_idx: [int](class_int.md#class-int))                                                                                            |
| [String](class_string.md#class-string)                       | get_tab_tooltip(tab_idx: [int](class_int.md#class-int))                                                                                        |
| [bool](class_bool.md#class-bool)                             | is_tab_disabled(tab_idx: [int](class_int.md#class-int))                                                                                        |
| [bool](class_bool.md#class-bool)                             | is_tab_hidden(tab_idx: [int](class_int.md#class-int))                                                                                            |
|                                                              | move_tab(from: [int](class_int.md#class-int), to: [int](class_int.md#class-int))                                                                      |
|                                                              | remove_tab(tab_idx: [int](class_int.md#class-int))                                                                                                  |
| [bool](class_bool.md#class-bool)                             | select_next_available()                                                                                                                  |
| [bool](class_bool.md#class-bool)                             | select_previous_available()                                                                                                          |
|                                                              | set_tab_button_icon(tab_idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))                         |
|                                                              | set_tab_disabled(tab_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                          |
|                                                              | set_tab_hidden(tab_idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))                                                |
|                                                              | set_tab_icon(tab_idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))                                       |
|                                                              | set_tab_icon_max_width(tab_idx: [int](class_int.md#class-int), width: [int](class_int.md#class-int))                                    |
|                                                              | set_tab_language(tab_idx: [int](class_int.md#class-int), language: [String](class_string.md#class-string))                                    |
|                                                              | set_tab_metadata(tab_idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))                                 |
|                                                              | set_tab_text_direction(tab_idx: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection)) |
|                                                              | set_tab_title(tab_idx: [int](class_int.md#class-int), title: [String](class_string.md#class-string))                                             |
|                                                              | set_tab_tooltip(tab_idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                       |

## Theme Properties

| [Color](class_color.md#class-color)             | drop_mark_color                  | `Color(1, 1, 1, 1)`               |
|-------------------------------------------------|-------------------------------------------------------------------------------|-----------------------------------|
| [Color](class_color.md#class-color)             | font_disabled_color          | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class-color)             | font_hovered_color            | `Color(0.95, 0.95, 0.95, 1)`      |
| [Color](class_color.md#class-color)             | font_outline_color            | `Color(0, 0, 0, 1)`               |
| [Color](class_color.md#class-color)             | font_selected_color          | `Color(0.95, 0.95, 0.95, 1)`      |
| [Color](class_color.md#class-color)             | font_unselected_color      | `Color(0.7, 0.7, 0.7, 1)`         |
| [Color](class_color.md#class-color)             | icon_disabled_color          | `Color(1, 1, 1, 1)`               |
| [Color](class_color.md#class-color)             | icon_hovered_color            | `Color(1, 1, 1, 1)`               |
| [Color](class_color.md#class-color)             | icon_selected_color          | `Color(1, 1, 1, 1)`               |
| [Color](class_color.md#class-color)             | icon_unselected_color      | `Color(1, 1, 1, 1)`               |
| [int](class_int.md#class-int)                   | h_separation                     | `4`                               |
| [int](class_int.md#class-int)                   | hover_switch_wait_msec | `500`                             |
| [int](class_int.md#class-int)                   | icon_max_width                 | `0`                               |
| [int](class_int.md#class-int)                   | outline_size                     | `0`                               |
| [int](class_int.md#class-int)                   | tab_separation                 | `0`                               |
| [Font](class_font.md#class-font)                | font                                         |                                   |
| [int](class_int.md#class-int)                   | font_size                          |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | close                                       |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | decrement                               |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | decrement_highlight           |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | drop_mark                               |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | increment                               |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | increment_highlight           |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | button_highlight                |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | button_pressed                    |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_disabled                        |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_focus                              |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_hovered                          |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_selected                        |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_unselected                    |                                   |

---

## Signals

**active_tab_rearranged**(idx_to: [int](class_int.md#class-int))

Emitted when the active tab is rearranged via mouse drag. See drag_to_rearrange_enabled.

---

**tab_button_pressed**(tab: [int](class_int.md#class-int))

Emitted when a tab's right button is pressed. See set_tab_button_icon().

---

**tab_changed**(tab: [int](class_int.md#class-int))

Emitted when switching to another tab.

---

**tab_clicked**(tab: [int](class_int.md#class-int))

Emitted when a tab is clicked, even if it is the current tab.

---

**tab_close_pressed**(tab: [int](class_int.md#class-int))

Emitted when a tab's close button is pressed or, if close_with_middle_mouse is `true`, when middle-clicking on a tab.

**Note:** Tabs are not removed automatically; this behavior needs to be coded manually. For example:

GDScript

```gdscript
$TabBar.tab_close_pressed.connect($TabBar.remove_tab)
```

C#

```csharp
GetNode<TabBar>("TabBar").TabClosePressed += GetNode<TabBar>("TabBar").RemoveTab;
```

---

**tab_hovered**(tab: [int](class_int.md#class-int))

Emitted when a tab is hovered by the mouse.

---

**tab_rmb_clicked**(tab: [int](class_int.md#class-int))

Emitted when a tab is right-clicked.

---

**tab_selected**(tab: [int](class_int.md#class-int))

Emitted when a tab is selected via click, directional input, or script, even if it is the current tab.

---

## Enumerations

enum **AlignmentMode**:

AlignmentMode **ALIGNMENT_LEFT** = `0`

Aligns tabs to the left.

AlignmentMode **ALIGNMENT_CENTER** = `1`

Aligns tabs in the middle.

AlignmentMode **ALIGNMENT_RIGHT** = `2`

Aligns tabs to the right.

AlignmentMode **ALIGNMENT_MAX** = `3`

Represents the size of the AlignmentMode enum.

---

enum **CloseButtonDisplayPolicy**:

CloseButtonDisplayPolicy **CLOSE_BUTTON_SHOW_NEVER** = `0`

Never show the close buttons.

CloseButtonDisplayPolicy **CLOSE_BUTTON_SHOW_ACTIVE_ONLY** = `1`

Only show the close button on the currently active tab.

CloseButtonDisplayPolicy **CLOSE_BUTTON_SHOW_ALWAYS** = `2`

Show the close button on all tabs.

CloseButtonDisplayPolicy **CLOSE_BUTTON_MAX** = `3`

Represents the size of the CloseButtonDisplayPolicy enum.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **clip_tabs** = `true`

-  **set_clip_tabs**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_clip_tabs**()

If `true`, tabs overflowing this node's width will be hidden, displaying two navigation buttons instead. Otherwise, this node's minimum size is updated so that all tabs are visible.

---

[bool](class_bool.md#class-bool) **close_with_middle_mouse** = `true`

-  **set_close_with_middle_mouse**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_close_with_middle_mouse**()

If `true`, middle-clicking on a tab will emit the tab_close_pressed signal.

---

[int](class_int.md#class-int) **current_tab** = `-1`

-  **set_current_tab**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_current_tab**()

The index of the current selected tab. A value of `-1` means that no tab is selected and can only be set when deselect_enabled is `true` or if all tabs are hidden or disabled.

---

[bool](class_bool.md#class-bool) **deselect_enabled** = `false`

-  **set_deselect_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_deselect_enabled**()

If `true`, all tabs can be deselected so that no tab is selected. Click on the current tab to deselect it.

---

[bool](class_bool.md#class-bool) **drag_to_rearrange_enabled** = `false`

-  **set_drag_to_rearrange_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_drag_to_rearrange_enabled**()

If `true`, tabs can be rearranged with mouse drag.

---

[int](class_int.md#class-int) **max_tab_width** = `0`

-  **set_max_tab_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_tab_width**()

Sets the maximum width which all tabs should be limited to. Unlimited if set to `0`.

---

[bool](class_bool.md#class-bool) **scroll_to_selected** = `true`

-  **set_scroll_to_selected**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_scroll_to_selected**()

If `true`, the tab offset will be changed to keep the currently selected tab visible.

---

[bool](class_bool.md#class-bool) **scrolling_enabled** = `true`

-  **set_scrolling_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_scrolling_enabled**()

if `true`, the mouse's scroll wheel can be used to navigate the scroll view.

---

[bool](class_bool.md#class-bool) **select_with_rmb** = `false`

-  **set_select_with_rmb**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_select_with_rmb**()

If `true`, enables selecting a tab with the right mouse button.

---

[bool](class_bool.md#class-bool) **switch_on_drag_hover** = `true`

-  **set_switch_on_drag_hover**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_switch_on_drag_hover**()

If `true`, hovering over a tab while dragging something will switch to that tab. Does not have effect when hovering another tab to rearrange. The delay for when this happens is dictated by hover_switch_wait_msec.

---

AlignmentMode **tab_alignment** = `0`

-  **set_tab_alignment**(value: AlignmentMode)
- AlignmentMode **get_tab_alignment**()

The horizontal alignment of the tabs.

---

CloseButtonDisplayPolicy **tab_close_display_policy** = `0`

-  **set_tab_close_display_policy**(value: CloseButtonDisplayPolicy)
- CloseButtonDisplayPolicy **get_tab_close_display_policy**()

When the close button will appear on the tabs.

---

[int](class_int.md#class-int) **tab_count** = `0`

-  **set_tab_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_tab_count**()

The number of tabs currently in the bar.

---

[bool](class_bool.md#class-bool) **tab_{index}/disabled** = `false`

If `true`, the tab at `index` is disabled.

**Note:** `index` is a value in the `0 .. tab_count - 1` range.

---

[Texture2D](class_texture2d.md#class-texture2d) **tab_{index}/icon**

If `true`, the tab at `index` is hidden.

**Note:** `index` is a value in the `0 .. tab_count - 1` range.

---

[String](class_string.md#class-string) **tab_{index}/title** = `""`

The title text of the tab at `index`.

**Note:** `index` is a value in the `0 .. tab_count - 1` range.

---

[String](class_string.md#class-string) **tab_{index}/tooltip** = `""`

The tooltip text of the tab at `index`.

**Note:** `index` is a value in the `0 .. tab_count - 1` range.

---

[int](class_int.md#class-int) **tabs_rearrange_group** = `-1`

-  **set_tabs_rearrange_group**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_tabs_rearrange_group**()

**TabBar**s with the same rearrange group ID will allow dragging the tabs between them. Enable drag with drag_to_rearrange_enabled.

Setting this to `-1` will disable rearranging between **TabBar**s.

---

## Method Descriptions

 **add_tab**(title: [String](class_string.md#class-string) = "", icon: [Texture2D](class_texture2d.md#class-texture2d) = null)

Adds a new tab.

---

 **clear_tabs**()

Clears all tabs.

---

 **ensure_tab_visible**(idx: [int](class_int.md#class-int))

Moves the scroll view to make the tab visible.

---

[bool](class_bool.md#class-bool) **get_offset_buttons_visible**()

Returns `true` if the offset buttons (the ones that appear when there's not enough space for all tabs) are visible.

---

[int](class_int.md#class-int) **get_previous_tab**()

Returns the previously active tab index.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_tab_button_icon**(tab_idx: [int](class_int.md#class-int))

Returns the icon for the right button of the tab at index `tab_idx` or `null` if the right button has no icon.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_tab_icon**(tab_idx: [int](class_int.md#class-int))

Returns the icon for the tab at index `tab_idx` or `null` if the tab has no icon.

---

[int](class_int.md#class-int) **get_tab_icon_max_width**(tab_idx: [int](class_int.md#class-int))

Returns the maximum allowed width of the icon for the tab at index `tab_idx`.

---

[int](class_int.md#class-int) **get_tab_idx_at_point**(point: [Vector2](class_vector2.md#class-vector2))

Returns the index of the tab at local coordinates `point`. Returns `-1` if the point is outside the control boundaries or if there's no tab at the queried position.

---

[String](class_string.md#class-string) **get_tab_language**(tab_idx: [int](class_int.md#class-int))

Returns tab title language code.

---

[Variant](class_variant.md#class-variant) **get_tab_metadata**(tab_idx: [int](class_int.md#class-int))

Returns the metadata value set to the tab at index `tab_idx` using set_tab_metadata(). If no metadata was previously set, returns `null` by default.

---

[int](class_int.md#class-int) **get_tab_offset**()

Returns the number of hidden tabs offsetted to the left.

---

[Rect2](class_rect2.md#class-rect2) **get_tab_rect**(tab_idx: [int](class_int.md#class-int))

Returns tab [Rect2](class_rect2.md#class-rect2) with local position and size.

---

[TextDirection](class_control.md#enum-control-textdirection) **get_tab_text_direction**(tab_idx: [int](class_int.md#class-int))

Returns tab title text base writing direction.

---

[String](class_string.md#class-string) **get_tab_title**(tab_idx: [int](class_int.md#class-int))

Returns the title of the tab at index `tab_idx`.

---

[String](class_string.md#class-string) **get_tab_tooltip**(tab_idx: [int](class_int.md#class-int))

Returns the tooltip text of the tab at index `tab_idx`.

---

[bool](class_bool.md#class-bool) **is_tab_disabled**(tab_idx: [int](class_int.md#class-int))

Returns `true` if the tab at index `tab_idx` is disabled.

---

[bool](class_bool.md#class-bool) **is_tab_hidden**(tab_idx: [int](class_int.md#class-int))

Returns `true` if the tab at index `tab_idx` is hidden.

---

 **move_tab**(from: [int](class_int.md#class-int), to: [int](class_int.md#class-int))

Moves a tab from `from` to `to`.

---

 **remove_tab**(tab_idx: [int](class_int.md#class-int))

Removes the tab at index `tab_idx`.

---

[bool](class_bool.md#class-bool) **select_next_available**()

Selects the first available tab with greater index than the currently selected. Returns `true` if tab selection changed.

---

[bool](class_bool.md#class-bool) **select_previous_available**()

Selects the first available tab with lower index than the currently selected. Returns `true` if tab selection changed.

---

 **set_tab_button_icon**(tab_idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets an `icon` for the button of the tab at index `tab_idx` (located to the right, before the close button), making it visible and clickable (See tab_button_pressed). Giving it a `null` value will hide the button.

---

 **set_tab_disabled**(tab_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

If `disabled` is `true`, disables the tab at index `tab_idx`, making it non-interactable.

---

 **set_tab_hidden**(tab_idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))

If `hidden` is `true`, hides the tab at index `tab_idx`, making it disappear from the tab area.

---

 **set_tab_icon**(tab_idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets an `icon` for the tab at index `tab_idx`.

---

 **set_tab_icon_max_width**(tab_idx: [int](class_int.md#class-int), width: [int](class_int.md#class-int))

Sets the maximum allowed width of the icon for the tab at index `tab_idx`. This limit is applied on top of the default size of the icon and on top of icon_max_width. The height is adjusted according to the icon's ratio.

---

 **set_tab_language**(tab_idx: [int](class_int.md#class-int), language: [String](class_string.md#class-string))

Sets the language code of the title for the tab at index `tab_idx` to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---

 **set_tab_metadata**(tab_idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))

Sets the metadata value for the tab at index `tab_idx`, which can be retrieved later using get_tab_metadata().

---

 **set_tab_text_direction**(tab_idx: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection))

Sets tab title base writing direction.

---

 **set_tab_title**(tab_idx: [int](class_int.md#class-int), title: [String](class_string.md#class-string))

Sets a `title` for the tab at index `tab_idx`.

---

 **set_tab_tooltip**(tab_idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets a `tooltip` for tab at index `tab_idx`.

**Note:** By default, if the `tooltip` is empty and the tab text is truncated (not all characters fit into the tab), the title will be displayed as a tooltip. To hide the tooltip, assign `" "` as the `tooltip` text.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **drop_mark_color** = `Color(1, 1, 1, 1)`

Modulation color for the drop_mark icon.

---

[Color](class_color.md#class-color) **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)`

Font color of disabled tabs.

---

[Color](class_color.md#class-color) **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)`

Font color of the currently hovered tab. Does not apply to the selected tab.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The tint of text outline of the tab name.

---

[Color](class_color.md#class-color) **font_selected_color** = `Color(0.95, 0.95, 0.95, 1)`

Font color of the currently selected tab.

---

[Color](class_color.md#class-color) **font_unselected_color** = `Color(0.7, 0.7, 0.7, 1)`

Font color of the other, unselected tabs.

---

[Color](class_color.md#class-color) **icon_disabled_color** = `Color(1, 1, 1, 1)`

Icon color of disabled tabs.

---

[Color](class_color.md#class-color) **icon_hovered_color** = `Color(1, 1, 1, 1)`

Icon color of the currently hovered tab. Does not apply to the selected tab.

---

[Color](class_color.md#class-color) **icon_selected_color** = `Color(1, 1, 1, 1)`

Icon color of the currently selected tab.

---

[Color](class_color.md#class-color) **icon_unselected_color** = `Color(1, 1, 1, 1)`

Icon color of the other, unselected tabs.

---

[int](class_int.md#class-int) **h_separation** = `4`

The horizontal separation between the elements inside tabs.

---

[int](class_int.md#class-int) **hover_switch_wait_msec** = `500`

During a drag-and-drop, this is how many milliseconds to wait before switching the tab.

---

[int](class_int.md#class-int) **icon_max_width** = `0`

The maximum allowed width of the tab's icon. This limit is applied on top of the default size of the icon, but before the value set with set_tab_icon_max_width(). The height is adjusted according to the icon's ratio.

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the tab text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[int](class_int.md#class-int) **tab_separation** = `0`

The space between tabs in the tab bar.

---

[Font](class_font.md#class-font) **font**

The font used to draw tab names.

---

[int](class_int.md#class-int) **font_size**

Font size of the tab names.

---

[Texture2D](class_texture2d.md#class-texture2d) **close**

The icon for the close button (see tab_close_display_policy).

---

[Texture2D](class_texture2d.md#class-texture2d) **decrement**

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.

---

[Texture2D](class_texture2d.md#class-texture2d) **decrement_highlight**

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

---

[Texture2D](class_texture2d.md#class-texture2d) **drop_mark**

Icon shown to indicate where a dragged tab will be dropped (see drag_to_rearrange_enabled).

---

[Texture2D](class_texture2d.md#class-texture2d) **increment**

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.

---

[Texture2D](class_texture2d.md#class-texture2d) **increment_highlight**

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

---

[StyleBox](class_stylebox.md#class-stylebox) **button_highlight**

Background of the tab and close buttons when they're being hovered with the cursor.

---

[StyleBox](class_stylebox.md#class-stylebox) **button_pressed**

Background of the tab and close buttons when it's being pressed.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_disabled**

The style of disabled tabs.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_focus**

[StyleBox](class_stylebox.md#class-stylebox) used when the **TabBar** is focused. The tab_focus [StyleBox](class_stylebox.md#class-stylebox) is displayed *over* the base [StyleBox](class_stylebox.md#class-stylebox) of the selected tab, so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the base [StyleBox](class_stylebox.md#class-stylebox) remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_hovered**

The style of the currently hovered tab. Does not apply to the selected tab.

**Note:** This style will be drawn with the same width as tab_unselected at minimum.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_selected**

The style of the currently selected tab.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_unselected**

The style of the other, unselected tabs.
