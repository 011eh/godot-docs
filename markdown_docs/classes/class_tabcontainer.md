# TabContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A container that creates a tab for each child control, displaying only the active tab's control.

## Description

Arranges child controls into a tabbed view, creating a tab for each one. The active tab's corresponding control is made visible, while all other child controls are hidden. Ignores non-control children.

**Note:** The drawing of the clickable tabs is handled by this node; [TabBar](class_tabbar.md#class-tabbar) is not needed.

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

## Properties

| [bool](class_bool.md#class-bool)                           | all_tabs_in_front                       |         |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)                           | clip_tabs                                       | `true`  |
| [int](class_int.md#class-int)                              | current_tab                                   | `-1`    |
| [bool](class_bool.md#class-bool)                           | deselect_enabled                         | `false` |
| [bool](class_bool.md#class-bool)                           | drag_to_rearrange_enabled       | `false` |
| [bool](class_bool.md#class-bool)                           | switch_on_drag_hover                 | `true`  |
| [AlignmentMode](class_tabbar.md#enum-tabbar-alignmentmode) | tab_alignment                               | `0`     |
| [FocusMode](class_control.md#enum-control-focusmode)       | tab_focus_mode                             | `2`     |
| [bool](class_bool.md#class-bool)                           | tab_{index}/disabled                   | `false` |
| [bool](class_bool.md#class-bool)                           | tab_{index}/hidden                       | `false` |
| [Texture2D](class_texture2d.md#class-texture2d)            | tab_{index}/icon                           |         |
| [String](class_string.md#class-string)                     | tab_{index}/title                         | `""`    |
| TabPosition              | tabs_position                               | `0`     |
| [int](class_int.md#class-int)                              | tabs_rearrange_group                 | `-1`    |
| [bool](class_bool.md#class-bool)                           | tabs_visible                                 | `true`  |
| [bool](class_bool.md#class-bool)                           | use_hidden_tabs_for_min_size | `false` |

## Methods

| [Control](class_control.md#class-control)       | get_current_tab_control()                                                                                      |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Popup](class_popup.md#class-popup)             | get_popup()                                                                                                                  |
| [int](class_int.md#class-int)                   | get_previous_tab()                                                                                                    |
| [TabBar](class_tabbar.md#class-tabbar)          | get_tab_bar()                                                                                                              |
| [Texture2D](class_texture2d.md#class-texture2d) | get_tab_button_icon(tab_idx: [int](class_int.md#class-int))                                                        |
| [Control](class_control.md#class-control)       | get_tab_control(tab_idx: [int](class_int.md#class-int))                                                                |
| [int](class_int.md#class-int)                   | get_tab_count()                                                                                                          |
| [Texture2D](class_texture2d.md#class-texture2d) | get_tab_icon(tab_idx: [int](class_int.md#class-int))                                                                      |
| [int](class_int.md#class-int)                   | get_tab_icon_max_width(tab_idx: [int](class_int.md#class-int))                                                  |
| [int](class_int.md#class-int)                   | get_tab_idx_at_point(point: [Vector2](class_vector2.md#class-vector2))                                            |
| [int](class_int.md#class-int)                   | get_tab_idx_from_control(control: [Control](class_control.md#class-control))                                  |
| [Variant](class_variant.md#class-variant)       | get_tab_metadata(tab_idx: [int](class_int.md#class-int))                                                              |
| [String](class_string.md#class-string)          | get_tab_title(tab_idx: [int](class_int.md#class-int))                                                                    |
| [String](class_string.md#class-string)          | get_tab_tooltip(tab_idx: [int](class_int.md#class-int))                                                                |
| [bool](class_bool.md#class-bool)                | is_tab_disabled(tab_idx: [int](class_int.md#class-int))                                                                |
| [bool](class_bool.md#class-bool)                | is_tab_hidden(tab_idx: [int](class_int.md#class-int))                                                                    |
| [bool](class_bool.md#class-bool)                | select_next_available()                                                                                          |
| [bool](class_bool.md#class-bool)                | select_previous_available()                                                                                  |
|                                                 | set_popup(popup: [Node](class_node.md#class-node))                                                                           |
|                                                 | set_tab_button_icon(tab_idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d)) |
|                                                 | set_tab_disabled(tab_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                  |
|                                                 | set_tab_hidden(tab_idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))                        |
|                                                 | set_tab_icon(tab_idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))               |
|                                                 | set_tab_icon_max_width(tab_idx: [int](class_int.md#class-int), width: [int](class_int.md#class-int))            |
|                                                 | set_tab_metadata(tab_idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))         |
|                                                 | set_tab_title(tab_idx: [int](class_int.md#class-int), title: [String](class_string.md#class-string))                     |
|                                                 | set_tab_tooltip(tab_idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))               |

## Theme Properties

| [Color](class_color.md#class-color)             | drop_mark_color             | `Color(1, 1, 1, 1)`               |
|-------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------|
| [Color](class_color.md#class-color)             | font_disabled_color     | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class-color)             | font_hovered_color       | `Color(0.95, 0.95, 0.95, 1)`      |
| [Color](class_color.md#class-color)             | font_outline_color       | `Color(0, 0, 0, 1)`               |
| [Color](class_color.md#class-color)             | font_selected_color     | `Color(0.95, 0.95, 0.95, 1)`      |
| [Color](class_color.md#class-color)             | font_unselected_color | `Color(0.7, 0.7, 0.7, 1)`         |
| [Color](class_color.md#class-color)             | icon_disabled_color     | `Color(1, 1, 1, 1)`               |
| [Color](class_color.md#class-color)             | icon_hovered_color       | `Color(1, 1, 1, 1)`               |
| [Color](class_color.md#class-color)             | icon_selected_color     | `Color(1, 1, 1, 1)`               |
| [Color](class_color.md#class-color)             | icon_unselected_color | `Color(1, 1, 1, 1)`               |
| [int](class_int.md#class-int)                   | icon_max_width            | `0`                               |
| [int](class_int.md#class-int)                   | icon_separation          | `4`                               |
| [int](class_int.md#class-int)                   | outline_size                | `0`                               |
| [int](class_int.md#class-int)                   | side_margin                  | `8`                               |
| [int](class_int.md#class-int)                   | tab_separation            | `0`                               |
| [Font](class_font.md#class-font)                | font                                    |                                   |
| [int](class_int.md#class-int)                   | font_size                     |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | decrement                          |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | decrement_highlight      |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | drop_mark                          |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | increment                          |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | increment_highlight      |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | menu                                    |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | menu_highlight                |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel                                 |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_disabled                   |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_focus                         |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_hovered                     |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_selected                   |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tab_unselected               |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | tabbar_background         |                                   |

---

## Signals

**active_tab_rearranged**(idx_to: [int](class_int.md#class-int))

Emitted when the active tab is rearranged via mouse drag. See drag_to_rearrange_enabled.

---

**pre_popup_pressed**()

Emitted when the **TabContainer**'s [Popup](class_popup.md#class-popup) button is clicked. See set_popup() for details.

---

**tab_button_pressed**(tab: [int](class_int.md#class-int))

Emitted when the user clicks on the button icon on this tab.

---

**tab_changed**(tab: [int](class_int.md#class-int))

Emitted when switching to another tab.

---

**tab_clicked**(tab: [int](class_int.md#class-int))

Emitted when a tab is clicked, even if it is the current tab.

---

**tab_hovered**(tab: [int](class_int.md#class-int))

Emitted when a tab is hovered by the mouse.

---

**tab_selected**(tab: [int](class_int.md#class-int))

Emitted when a tab is selected via click, directional input, or script, even if it is the current tab.

---

## Enumerations

enum **TabPosition**:

TabPosition **POSITION_TOP** = `0`

Places the tab bar at the top.

TabPosition **POSITION_BOTTOM** = `1`

Places the tab bar at the bottom. The tab bar's [StyleBox](class_stylebox.md#class-stylebox) will be flipped vertically.

TabPosition **POSITION_MAX** = `2`

Represents the size of the TabPosition enum.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **all_tabs_in_front**

-  **set_all_tabs_in_front**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_all_tabs_in_front**()

**Deprecated:** Due to internal changes this doesn't do anything anymore, as they're always in front.

This doesn't do anything.

---

[bool](class_bool.md#class-bool) **clip_tabs** = `true`

-  **set_clip_tabs**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_clip_tabs**()

If `true`, tabs overflowing this node's width will be hidden, displaying two navigation buttons instead. Otherwise, this node's minimum size is updated so that all tabs are visible.

---

[int](class_int.md#class-int) **current_tab** = `-1`

-  **set_current_tab**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_current_tab**()

The current tab index. When set, this index's [Control](class_control.md#class-control) node's `visible` property is set to `true` and all others are set to `false`.

A value of `-1` means that no tab is selected.

---

[bool](class_bool.md#class-bool) **deselect_enabled** = `false`

-  **set_deselect_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_deselect_enabled**()

If `true`, all tabs can be deselected so that no tab is selected. Click on the current_tab to deselect it.

Only the tab header will be shown if no tabs are selected.

---

[bool](class_bool.md#class-bool) **drag_to_rearrange_enabled** = `false`

-  **set_drag_to_rearrange_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_drag_to_rearrange_enabled**()

If `true`, tabs can be rearranged with mouse drag.

---

[bool](class_bool.md#class-bool) **switch_on_drag_hover** = `true`

-  **set_switch_on_drag_hover**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_switch_on_drag_hover**()

If `true`, hovering over a tab while dragging something will switch to that tab. Does not have effect when hovering another tab to rearrange.

---

[AlignmentMode](class_tabbar.md#enum-tabbar-alignmentmode) **tab_alignment** = `0`

-  **set_tab_alignment**(value: [AlignmentMode](class_tabbar.md#enum-tabbar-alignmentmode))
- [AlignmentMode](class_tabbar.md#enum-tabbar-alignmentmode) **get_tab_alignment**()

The position at which tabs will be placed.

---

[FocusMode](class_control.md#enum-control-focusmode) **tab_focus_mode** = `2`

-  **set_tab_focus_mode**(value: [FocusMode](class_control.md#enum-control-focusmode))
- [FocusMode](class_control.md#enum-control-focusmode) **get_tab_focus_mode**()

The focus access mode for the internal [TabBar](class_tabbar.md#class-tabbar) node.

---

[bool](class_bool.md#class-bool) **tab_{index}/disabled** = `false`

If `true`, the tab at `index` is disabled.

**Note:** `index` is a value in the `0 .. get_tab_count() - 1` range.

---

[bool](class_bool.md#class-bool) **tab_{index}/hidden** = `false`

If `true`, the tab at `index` is hidden.

**Note:** `index` is a value in the `0 .. get_tab_count() - 1` range.

---

[Texture2D](class_texture2d.md#class-texture2d) **tab_{index}/icon**

The title text of the tab at `index`.

**Note:** `index` is a value in the `0 .. get_tab_count() - 1` range.

---

[String](class_string.md#class-string) **tab_{index}/title** = `""`

The tooltip text of the tab at `index`.

**Note:** `index` is a value in the `0 .. get_tab_count() - 1` range.

---

TabPosition **tabs_position** = `0`

-  **set_tabs_position**(value: TabPosition)
- TabPosition **get_tabs_position**()

The horizontal alignment of the tabs.

---

[int](class_int.md#class-int) **tabs_rearrange_group** = `-1`

-  **set_tabs_rearrange_group**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_tabs_rearrange_group**()

**TabContainer**s with the same rearrange group ID will allow dragging the tabs between them. Enable drag with drag_to_rearrange_enabled.

Setting this to `-1` will disable rearranging between **TabContainer**s.

---

[bool](class_bool.md#class-bool) **tabs_visible** = `true`

-  **set_tabs_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_tabs_visible**()

If `true`, tabs are visible. If `false`, tabs' content and titles are hidden.

---

[bool](class_bool.md#class-bool) **use_hidden_tabs_for_min_size** = `false`

-  **set_use_hidden_tabs_for_min_size**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_hidden_tabs_for_min_size**()

If `true`, child [Control](class_control.md#class-control) nodes that are hidden have their minimum size take into account in the total, instead of only the currently visible one.

---

## Method Descriptions

[Control](class_control.md#class-control) **get_current_tab_control**()

Returns the child [Control](class_control.md#class-control) node located at the active tab index.

---

[Popup](class_popup.md#class-popup) **get_popup**()

Returns the [Popup](class_popup.md#class-popup) node instance if one has been set already with set_popup().

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---

[int](class_int.md#class-int) **get_previous_tab**()

Returns the previously active tab index.

---

[TabBar](class_tabbar.md#class-tabbar) **get_tab_bar**()

Returns the [TabBar](class_tabbar.md#class-tabbar) contained in this container.

**Warning:** This is a required internal node, removing and freeing it or editing its tabs may cause a crash. If you wish to edit the tabs, use the methods provided in **TabContainer**.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_tab_button_icon**(tab_idx: [int](class_int.md#class-int))

Returns the button icon from the tab at index `tab_idx`.

---

[Control](class_control.md#class-control) **get_tab_control**(tab_idx: [int](class_int.md#class-int))

Returns the [Control](class_control.md#class-control) node from the tab at index `tab_idx`.

---

[int](class_int.md#class-int) **get_tab_count**()

Returns the number of tabs.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_tab_icon**(tab_idx: [int](class_int.md#class-int))

Returns the [Texture2D](class_texture2d.md#class-texture2d) for the tab at index `tab_idx` or `null` if the tab has no [Texture2D](class_texture2d.md#class-texture2d).

---

[int](class_int.md#class-int) **get_tab_icon_max_width**(tab_idx: [int](class_int.md#class-int))

Returns the maximum allowed width of the icon for the tab at index `tab_idx`.

---

[int](class_int.md#class-int) **get_tab_idx_at_point**(point: [Vector2](class_vector2.md#class-vector2))

Returns the index of the tab at local coordinates `point`. Returns `-1` if the point is outside the control boundaries or if there's no tab at the queried position.

---

[int](class_int.md#class-int) **get_tab_idx_from_control**(control: [Control](class_control.md#class-control))

Returns the index of the tab tied to the given `control`. The control must be a child of the **TabContainer**.

---

[Variant](class_variant.md#class-variant) **get_tab_metadata**(tab_idx: [int](class_int.md#class-int))

Returns the metadata value set to the tab at index `tab_idx` using set_tab_metadata(). If no metadata was previously set, returns `null` by default.

---

[String](class_string.md#class-string) **get_tab_title**(tab_idx: [int](class_int.md#class-int))

Returns the title of the tab at index `tab_idx`. Tab titles default to the name of the indexed child node, but this can be overridden with set_tab_title().

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

[bool](class_bool.md#class-bool) **select_next_available**()

Selects the first available tab with greater index than the currently selected. Returns `true` if tab selection changed.

---

[bool](class_bool.md#class-bool) **select_previous_available**()

Selects the first available tab with lower index than the currently selected. Returns `true` if tab selection changed.

---

 **set_popup**(popup: [Node](class_node.md#class-node))

If set on a [Popup](class_popup.md#class-popup) node instance, a popup menu icon appears in the top-right corner of the **TabContainer** (setting it to `null` will make it go away). Clicking it will expand the [Popup](class_popup.md#class-popup) node.

---

 **set_tab_button_icon**(tab_idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets the button icon from the tab at index `tab_idx`.

---

 **set_tab_disabled**(tab_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

If `disabled` is `true`, disables the tab at index `tab_idx`, making it non-interactable.

---

 **set_tab_hidden**(tab_idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))

If `hidden` is `true`, hides the tab at index `tab_idx`, making it disappear from the tab area.

---

 **set_tab_icon**(tab_idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets an icon for the tab at index `tab_idx`.

---

 **set_tab_icon_max_width**(tab_idx: [int](class_int.md#class-int), width: [int](class_int.md#class-int))

Sets the maximum allowed width of the icon for the tab at index `tab_idx`. This limit is applied on top of the default size of the icon and on top of icon_max_width. The height is adjusted according to the icon's ratio.

---

 **set_tab_metadata**(tab_idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))

Sets the metadata value for the tab at index `tab_idx`, which can be retrieved later using get_tab_metadata().

---

 **set_tab_title**(tab_idx: [int](class_int.md#class-int), title: [String](class_string.md#class-string))

Sets a custom title for the tab at index `tab_idx` (tab titles default to the name of the indexed child node). Set it back to the child's name to make the tab default to it again.

---

 **set_tab_tooltip**(tab_idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets a custom tooltip text for tab at index `tab_idx`.

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

[int](class_int.md#class-int) **icon_max_width** = `0`

The maximum allowed width of the tab's icon. This limit is applied on top of the default size of the icon, but before the value set with [TabBar.set_tab_icon_max_width()](class_tabbar.md#class-tabbar-method-set-tab-icon-max-width). The height is adjusted according to the icon's ratio.

---

[int](class_int.md#class-int) **icon_separation** = `4`

Space between tab's name and its icon.

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the tab text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[int](class_int.md#class-int) **side_margin** = `8`

The space at the left or right edges of the tab bar, accordingly with the current tab_alignment.

The margin is ignored with [TabBar.ALIGNMENT_RIGHT](class_tabbar.md#class-tabbar-constant-alignment-right) if the tabs are clipped (see clip_tabs) or a popup has been set (see set_popup()). The margin is always ignored with [TabBar.ALIGNMENT_CENTER](class_tabbar.md#class-tabbar-constant-alignment-center).

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

[Texture2D](class_texture2d.md#class-texture2d) **menu**

The icon for the menu button (see set_popup()).

---

[Texture2D](class_texture2d.md#class-texture2d) **menu_highlight**

The icon for the menu button (see set_popup()) when it's being hovered with the cursor.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

The style for the background fill.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_disabled**

The style of disabled tabs.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_focus**

[StyleBox](class_stylebox.md#class-stylebox) used when the [TabBar](class_tabbar.md#class-tabbar) is focused. The tab_focus [StyleBox](class_stylebox.md#class-stylebox) is displayed *over* the base [StyleBox](class_stylebox.md#class-stylebox) of the selected tab, so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the base [StyleBox](class_stylebox.md#class-stylebox) remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_hovered**

The style of the currently hovered tab.

**Note:** This style will be drawn with the same width as tab_unselected at minimum.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_selected**

The style of the currently selected tab.

---

[StyleBox](class_stylebox.md#class-stylebox) **tab_unselected**

The style of the other, unselected tabs.

---

[StyleBox](class_stylebox.md#class-stylebox) **tabbar_background**

The style for the background fill of the [TabBar](class_tabbar.md#class-tabbar) area.
