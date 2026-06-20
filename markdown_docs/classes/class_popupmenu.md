# PopupMenu

**Inherits:** [Popup](class_popup.md#class-popup) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A modal window used to display a list of options.

## Description

**PopupMenu** is a modal window used to display a list of options. Useful for toolbars and context menus.

The size of a **PopupMenu** can be limited by using [Window.max_size](class_window.md#class-window-property-max-size). If the height of the list of items is larger than the maximum height of the **PopupMenu**, a [ScrollContainer](class_scrollcontainer.md#class-scrollcontainer) within the popup will allow the user to scroll the contents. If no maximum size is set, or if it is set to `0`, the **PopupMenu** height will be limited by its parent rect.

All `set_*` methods allow negative item indices, i.e. `-1` to access the last item, `-2` to select the second-to-last item, and so on.

**Incremental search:** Like [ItemList](class_itemlist.md#class-itemlist) and [Tree](class_tree.md#class-tree), **PopupMenu** supports searching within the list while the control is focused. Press a key that matches the first letter of an item's name to select the first item starting with the given letter. After that point, there are two ways to perform incremental search: 1) Press the same key again before the timeout duration to select the next item starting with the same letter. 2) Press letter keys that match the rest of the word before the timeout duration to match to select the item in question directly. Both of these actions will be reset to the beginning of the list if the timeout duration has passed since the last keystroke was registered. You can adjust the timeout duration by changing [ProjectSettings.gui/timers/incremental_search_max_interval_msec](class_projectsettings.md#class-projectsettings-property-gui-timers-incremental-search-max-interval-msec).

**Note:** **PopupMenu** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class-window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class-window-method-popup-centered-clamped).

**Note:** The ID values used for items are limited to 32 bits, not full 64 bits of [int](class_int.md#class-int). This has a range of `-2^32` to `2^32 - 1`, i.e. `-2147483648` to `2147483647`.

## Properties

| [bool](class_bool.md#class-bool)                                                                 | allow_search                                             | `true`                                                                                                   |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [DefaultCanvasItemTextureFilter](class_viewport.md#enum-viewport-defaultcanvasitemtexturefilter) | canvas_item_default_texture_filter                                                                 | `4` (overrides [Viewport](class_viewport.md#class-viewport-property-canvas-item-default-texture-filter)) |
| [DefaultCanvasItemTextureRepeat](class_viewport.md#enum-viewport-defaultcanvasitemtexturerepeat) | canvas_item_default_texture_repeat                                                                 | `3` (overrides [Viewport](class_viewport.md#class-viewport-property-canvas-item-default-texture-repeat)) |
| [bool](class_bool.md#class-bool)                                                                 | hide_on_checkable_item_selection     | `true`                                                                                                   |
| [bool](class_bool.md#class-bool)                                                                 | hide_on_item_selection                         | `true`                                                                                                   |
| [bool](class_bool.md#class-bool)                                                                 | hide_on_state_item_selection             | `false`                                                                                                  |
| [int](class_int.md#class-int)                                                                    | item_count                                                 | `0`                                                                                                      |
| [int](class_int.md#class-int)                                                                    | item_{index}/checkable                           | `0`                                                                                                      |
| [bool](class_bool.md#class-bool)                                                                 | item_{index}/checked                               | `false`                                                                                                  |
| [bool](class_bool.md#class-bool)                                                                 | item_{index}/disabled                             | `false`                                                                                                  |
| [Texture2D](class_texture2d.md#class-texture2d)                                                  | item_{index}/icon                                     |                                                                                                          |
| [int](class_int.md#class-int)                                                                    | item_{index}/id                                         | `0`                                                                                                      |
| [bool](class_bool.md#class-bool)                                                                 | item_{index}/separator                           | `false`                                                                                                  |
| [String](class_string.md#class-string)                                                           | item_{index}/text                                     | `""`                                                                                                     |
| [bool](class_bool.md#class-bool)                                                                 | prefer_native_menu                                 | `false`                                                                                                  |
| [bool](class_bool.md#class-bool)                                                                 | search_bar_enabled                                 | `false`                                                                                                  |
| [bool](class_bool.md#class-bool)                                                                 | search_bar_fuzzy_search_enabled       | `true`                                                                                                   |
| [int](class_int.md#class-int)                                                                    | search_bar_fuzzy_search_max_misses | `2`                                                                                                      |
| [int](class_int.md#class-int)                                                                    | search_bar_min_item_count                   | `0`                                                                                                      |
| [bool](class_bool.md#class-bool)                                                                 | shrink_height                                           | `true`                                                                                                   |
| [bool](class_bool.md#class-bool)                                                                 | shrink_width                                             | `true`                                                                                                   |
| [float](class_float.md#class-float)                                                              | submenu_popup_delay                               | `0.2`                                                                                                    |
| [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus)                                   | system_menu_id                                         | `0`                                                                                                      |
| [bool](class_bool.md#class-bool)                                                                 | transparent                                                                                        | `true` (overrides [Window](class_window.md#class-window-property-transparent))                           |
| [bool](class_bool.md#class-bool)                                                                 | transparent_bg                                                                                     | `true` (overrides [Viewport](class_viewport.md#class-viewport-property-transparent-bg))                  |

## Methods

| [bool](class_bool.md#class-bool)                               | activate_item_by_event(event: [InputEvent](class_inputevent.md#class-inputevent), for_global_only: [bool](class_bool.md#class-bool) = false)                                                                                                                                   |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                | add_check_item(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)                                                                                                                    |
|                                                                | add_check_shortcut(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false)                                                                                                               |
|                                                                | add_icon_check_item(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)                                                |
|                                                                | add_icon_check_shortcut(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false)                                           |
|                                                                | add_icon_item(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)                                                            |
|                                                                | add_icon_radio_check_item(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)                                    |
|                                                                | add_icon_radio_check_shortcut(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false)                               |
|                                                                | add_icon_shortcut(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false, allow_echo: [bool](class_bool.md#class-bool) = false) |
|                                                                | add_item(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)                                                                                                                                |
|                                                                | add_multistate_item(label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int) = 0, id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)             |
|                                                                | add_radio_check_item(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)                                                                                                        |
|                                                                | add_radio_check_shortcut(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false)                                                                                                   |
|                                                                | add_separator(label: [String](class_string.md#class-string) = "", id: [int](class_int.md#class-int) = -1)                                                                                                                                                                               |
|                                                                | add_shortcut(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false, allow_echo: [bool](class_bool.md#class-bool) = false)                                                                     |
|                                                                | add_submenu_item(label: [String](class_string.md#class-string), submenu: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1)                                                                                                                             |
|                                                                | add_submenu_node_item(label: [String](class_string.md#class-string), submenu: PopupMenu, id: [int](class_int.md#class-int) = -1)                                                                                                                            |
|                                                                | clear(free_submenus: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                  | get_focused_item()                                                                                                                                                                                                                                                                   |
| [Key](class_@globalscope.md#enum-globalscope-key)              | get_item_accelerator(index: [int](class_int.md#class-int))                                                                                                                                                                                                                       |
| [AutoTranslateMode](class_node.md#enum-node-autotranslatemode) | get_item_auto_translate_mode(index: [int](class_int.md#class-int))                                                                                                                                                                                                       |
| [Texture2D](class_texture2d.md#class-texture2d)                | get_item_icon(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                  | get_item_icon_max_width(index: [int](class_int.md#class-int))                                                                                                                                                                                                                 |
| [Color](class_color.md#class-color)                            | get_item_icon_modulate(index: [int](class_int.md#class-int))                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                  | get_item_id(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                  | get_item_indent(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                  | get_item_index(id: [int](class_int.md#class-int))                                                                                                                                                                                                                                      |
| [String](class_string.md#class-string)                         | get_item_language(index: [int](class_int.md#class-int))                                                                                                                                                                                                                             |
| [Variant](class_variant.md#class-variant)                      | get_item_metadata(index: [int](class_int.md#class-int))                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                  | get_item_multistate(index: [int](class_int.md#class-int))                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                  | get_item_multistate_max(index: [int](class_int.md#class-int))                                                                                                                                                                                                                 |
| [Shortcut](class_shortcut.md#class-shortcut)                   | get_item_shortcut(index: [int](class_int.md#class-int))                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                         | get_item_submenu(index: [int](class_int.md#class-int))                                                                                                                                                                                                                               |
| PopupMenu                                  | get_item_submenu_node(index: [int](class_int.md#class-int))                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)                         | get_item_text(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [TextDirection](class_control.md#enum-control-textdirection)   | get_item_text_direction(index: [int](class_int.md#class-int))                                                                                                                                                                                                                 |
| [String](class_string.md#class-string)                         | get_item_tooltip(index: [int](class_int.md#class-int))                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                               | is_item_checkable(index: [int](class_int.md#class-int))                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                               | is_item_checked(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                               | is_item_disabled(index: [int](class_int.md#class-int))                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                               | is_item_radio_checkable(index: [int](class_int.md#class-int))                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                               | is_item_separator(index: [int](class_int.md#class-int))                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                               | is_item_shortcut_disabled(index: [int](class_int.md#class-int))                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                               | is_native_menu()                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                               | is_system_menu()                                                                                                                                                                                                                                                                       |
|                                                                | remove_item(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                         |
|                                                                | scroll_to_item(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                   |
|                                                                | set_focused_item(index: [int](class_int.md#class-int))                                                                                                                                                                                                                               |
|                                                                | set_item_accelerator(index: [int](class_int.md#class-int), accel: [Key](class_@globalscope.md#enum-globalscope-key))                                                                                                                                                             |
|                                                                | set_item_as_checkable(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                           |
|                                                                | set_item_as_radio_checkable(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                                                                                                               |
|                                                                | set_item_as_separator(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                           |
|                                                                | set_item_auto_translate_mode(index: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode))                                                                                                                                 |
|                                                                | set_item_checked(index: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool))                                                                                                                                                                                    |
|                                                                | set_item_disabled(index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                 |
|                                                                | set_item_icon(index: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                              |
|                                                                | set_item_icon_max_width(index: [int](class_int.md#class-int), width: [int](class_int.md#class-int))                                                                                                                                                                           |
|                                                                | set_item_icon_modulate(index: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color))                                                                                                                                                                    |
|                                                                | set_item_id(index: [int](class_int.md#class-int), id: [int](class_int.md#class-int))                                                                                                                                                                                                      |
|                                                                | set_item_indent(index: [int](class_int.md#class-int), indent: [int](class_int.md#class-int))                                                                                                                                                                                          |
|                                                                | set_item_index(index: [int](class_int.md#class-int), target_index: [int](class_int.md#class-int))                                                                                                                                                                                      |
|                                                                | set_item_language(index: [int](class_int.md#class-int), language: [String](class_string.md#class-string))                                                                                                                                                                           |
|                                                                | set_item_metadata(index: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))                                                                                                                                                                        |
|                                                                | set_item_multistate(index: [int](class_int.md#class-int), state: [int](class_int.md#class-int))                                                                                                                                                                                   |
|                                                                | set_item_multistate_max(index: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int))                                                                                                                                                                      |
|                                                                | set_item_shortcut(index: [int](class_int.md#class-int), shortcut: [Shortcut](class_shortcut.md#class-shortcut), global: [bool](class_bool.md#class-bool) = false)                                                                                                                   |
|                                                                | set_item_shortcut_disabled(index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                               |
|                                                                | set_item_submenu(index: [int](class_int.md#class-int), submenu: [String](class_string.md#class-string))                                                                                                                                                                              |
|                                                                | set_item_submenu_node(index: [int](class_int.md#class-int), submenu: PopupMenu)                                                                                                                                                                             |
|                                                                | set_item_text(index: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                                                                                                                                       |
|                                                                | set_item_text_direction(index: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection))                                                                                                                                        |
|                                                                | set_item_tooltip(index: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                                                                                                                                                              |
|                                                                | toggle_item_checked(index: [int](class_int.md#class-int))                                                                                                                                                                                                                         |
|                                                                | toggle_item_multistate(index: [int](class_int.md#class-int))                                                                                                                                                                                                                   |

## Theme Properties

| [Color](class_color.md#class-color)             | font_accelerator_color             | `Color(0.7, 0.7, 0.7, 0.8)`     |
|-------------------------------------------------|-------------------------------------------------------------------------------------------|---------------------------------|
| [Color](class_color.md#class-color)             | font_color                                     | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color)             | font_disabled_color                   | `Color(0.4, 0.4, 0.4, 0.8)`     |
| [Color](class_color.md#class-color)             | font_hover_color                         | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color)             | font_outline_color                     | `Color(0, 0, 0, 1)`             |
| [Color](class_color.md#class-color)             | font_separator_color                 | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color)             | font_separator_outline_color | `Color(0, 0, 0, 1)`             |
| [int](class_int.md#class-int)                   | gutter_compact                          | `1`                             |
| [int](class_int.md#class-int)                   | h_separation                              | `4`                             |
| [int](class_int.md#class-int)                   | icon_max_width                          | `0`                             |
| [int](class_int.md#class-int)                   | indent                                          | `10`                            |
| [int](class_int.md#class-int)                   | item_end_padding                      | `2`                             |
| [int](class_int.md#class-int)                   | item_start_padding                  | `2`                             |
| [int](class_int.md#class-int)                   | outline_size                              | `0`                             |
| [int](class_int.md#class-int)                   | search_bar_separation            | `4`                             |
| [int](class_int.md#class-int)                   | separator_outline_size          | `0`                             |
| [int](class_int.md#class-int)                   | v_separation                              | `4`                             |
| [Font](class_font.md#class-font)                | font                                                  |                                 |
| [Font](class_font.md#class-font)                | font_separator                              |                                 |
| [int](class_int.md#class-int)                   | font_separator_size               |                                 |
| [int](class_int.md#class-int)                   | font_size                                   |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | checked                                            |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | checked_disabled                          |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | radio_checked                                |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | radio_checked_disabled              |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | radio_unchecked                            |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | radio_unchecked_disabled          |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | search                                              |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | submenu                                            |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | submenu_mirrored                          |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | unchecked                                        |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | unchecked_disabled                      |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | hover                                               |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | labeled_separator_left             |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | labeled_separator_right           |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel                                               |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | separator                                       |                                 |

---

## Signals

**id_focused**(id: [int](class_int.md#class-int))

Emitted when the user navigated to an item of some `id` using the [ProjectSettings.input/ui_up](class_projectsettings.md#class-projectsettings-property-input-ui-up) or [ProjectSettings.input/ui_down](class_projectsettings.md#class-projectsettings-property-input-ui-down) input action.

---

**id_pressed**(id: [int](class_int.md#class-int))

Emitted when an item of some `id` is pressed. Also emitted when its accelerator is activated on macOS.

**Note:** If `id` is negative (either explicitly or due to overflow), this will return the corresponding index instead.

---

**index_pressed**(index: [int](class_int.md#class-int))

Emitted when an item of some `index` is pressed. Also emitted when its accelerator is activated on macOS.

---

**menu_changed**()

Emitted when any item is added, modified or removed.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_search** = `true`

-  **set_allow_search**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_search**()

If `true`, allows navigating **PopupMenu** with letter keys.

---

[bool](class_bool.md#class-bool) **hide_on_checkable_item_selection** = `true`

-  **set_hide_on_checkable_item_selection**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hide_on_checkable_item_selection**()

If `true`, hides the **PopupMenu** when a checkbox or radio button is selected.

---

[bool](class_bool.md#class-bool) **hide_on_item_selection** = `true`

-  **set_hide_on_item_selection**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hide_on_item_selection**()

If `true`, hides the **PopupMenu** when an item is selected.

---

[bool](class_bool.md#class-bool) **hide_on_state_item_selection** = `false`

-  **set_hide_on_state_item_selection**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hide_on_state_item_selection**()

If `true`, hides the **PopupMenu** when a state item is selected.

---

[int](class_int.md#class-int) **item_count** = `0`

-  **set_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_count**()

The number of items currently in the list.

---

[int](class_int.md#class-int) **item_{index}/checkable** = `0`

The checkable item type of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[bool](class_bool.md#class-bool) **item_{index}/checked** = `false`

If `true`, the item at `index` is checked.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[bool](class_bool.md#class-bool) **item_{index}/disabled** = `false`

If `true`, the item at `index` is disabled.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[Texture2D](class_texture2d.md#class-texture2d) **item_{index}/icon**

The icon of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[int](class_int.md#class-int) **item_{index}/id** = `0`

The ID of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[bool](class_bool.md#class-bool) **item_{index}/separator** = `false`

If `true`, the item at `index` is a separator.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[String](class_string.md#class-string) **item_{index}/text** = `""`

The text of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[bool](class_bool.md#class-bool) **prefer_native_menu** = `false`

-  **set_prefer_native_menu**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_prefer_native_menu**()

If `true`, [MenuBar](class_menubar.md#class-menubar) will use native menu when supported.

**Note:** If **PopupMenu** is linked to [StatusIndicator](class_statusindicator.md#class-statusindicator), [MenuBar](class_menubar.md#class-menubar), or another **PopupMenu** item it can use native menu regardless of this property, use is_native_menu() to check it.

---

[bool](class_bool.md#class-bool) **search_bar_enabled** = `false`

-  **set_search_bar_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_search_bar_enabled**()

If `true`, shows a search bar at the top of the **PopupMenu** for filtering items. See search_bar_min_item_count for dynamically controlling its visibility based on the number of items.

**Note:** When enabled, allow_search is ignored.

---

[bool](class_bool.md#class-bool) **search_bar_fuzzy_search_enabled** = `true`

-  **set_search_bar_fuzzy_search_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_search_bar_fuzzy_search_enabled**()

If `true`, enables fuzzy searching in the **PopupMenu** search bar. This allows the search results to include items that almost match the search query, as well items that match the individual characters of the search query, but not in sequence.

Use search_bar_fuzzy_search_max_misses to set the maximum number of mismatches allowed in the search results.

---

[int](class_int.md#class-int) **search_bar_fuzzy_search_max_misses** = `2`

-  **set_search_bar_fuzzy_search_max_misses**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_search_bar_fuzzy_search_max_misses**()

Sets the maximum number of mismatches allowed in each search result when fuzzy searching is enabled for the **PopupMenu** search bar. Any item with more mismatches will be hidden from the search results.

---

[int](class_int.md#class-int) **search_bar_min_item_count** = `0`

-  **set_search_bar_min_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_search_bar_min_item_count**()

Sets the minimum number of items required for the search bar to be visible. search_bar_enabled must be `true` for this to have any effect. Separator items are not counted.

---

[bool](class_bool.md#class-bool) **shrink_height** = `true`

-  **set_shrink_height**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_shrink_height**()

If `true`, shrinks **PopupMenu** to minimum height when it's shown.

---

[bool](class_bool.md#class-bool) **shrink_width** = `true`

-  **set_shrink_width**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_shrink_width**()

If `true`, shrinks **PopupMenu** to minimum width when it's shown.

---

[float](class_float.md#class-float) **submenu_popup_delay** = `0.2`

-  **set_submenu_popup_delay**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_submenu_popup_delay**()

Sets the delay time in seconds for the submenu item to popup on mouse hovering. If the popup menu is added as a child of another (acting as a submenu), it will inherit the delay time of the parent menu item.

**Note:** If the mouse is exiting a submenu item with an open submenu and enters a different submenu item, the submenu popup delay time is affected by the direction of the mouse movement toward the open submenu. If the mouse is moving toward the submenu, the open submenu will wait approximately `0.5` seconds before closing, which then allows the hovered submenu item to open. This additional delay allows the mouse time to move to the open submenu across other menu items without prematurely closing. If the mouse is not moving toward the open submenu, for example in a downward direction, the open submenu will close immediately.

---

[SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **system_menu_id** = `0`

-  **set_system_menu**(value: [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus))
- [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus) **get_system_menu**()

If set to one of the values of [SystemMenus](class_nativemenu.md#enum-nativemenu-systemmenus), this **PopupMenu** is bound to the special system menu. Only one **PopupMenu** can be bound to each special menu at a time.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **activate_item_by_event**(event: [InputEvent](class_inputevent.md#class-inputevent), for_global_only: [bool](class_bool.md#class-bool) = false)

Checks the provided `event` against the **PopupMenu**'s shortcuts and accelerators, and activates the first item with matching events. If `for_global_only` is `true`, only shortcuts and accelerators with `global` set to `true` will be called.

Returns `true` if an item was successfully activated.

**Note:** Certain [Control](class_control.md#class-control)s, such as [MenuButton](class_menubutton.md#class-menubutton), will call this method automatically.

---

 **add_check_item**(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)

Adds a new checkable item with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See get_item_accelerator() for more info on accelerators.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See set_item_checked() for more info on how to control it.

---

 **add_check_shortcut**(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false)

Adds a new checkable item and assigns the specified [Shortcut](class_shortcut.md#class-shortcut) to it. Sets the label of the checkbox to the [Shortcut](class_shortcut.md#class-shortcut)'s name.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See set_item_checked() for more info on how to control it.

---

 **add_icon_check_item**(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)

Adds a new checkable item with text `label` and icon `texture`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See get_item_accelerator() for more info on accelerators.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See set_item_checked() for more info on how to control it.

---

 **add_icon_check_shortcut**(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false)

Adds a new checkable item and assigns the specified [Shortcut](class_shortcut.md#class-shortcut) and icon `texture` to it. Sets the label of the checkbox to the [Shortcut](class_shortcut.md#class-shortcut)'s name.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See set_item_checked() for more info on how to control it.

---

 **add_icon_item**(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)

Adds a new item with text `label` and icon `texture`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See get_item_accelerator() for more info on accelerators.

---

 **add_icon_radio_check_item**(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)

Same as add_icon_check_item(), but uses a radio check button.

---

 **add_icon_radio_check_shortcut**(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false)

Same as add_icon_check_shortcut(), but uses a radio check button.

---

 **add_icon_shortcut**(texture: [Texture2D](class_texture2d.md#class-texture2d), shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false, allow_echo: [bool](class_bool.md#class-bool) = false)

Adds a new item and assigns the specified [Shortcut](class_shortcut.md#class-shortcut) and icon `texture` to it. Sets the label of the checkbox to the [Shortcut](class_shortcut.md#class-shortcut)'s name.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

If `allow_echo` is `true`, the shortcut can be activated with echo events.

---

 **add_item**(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)

Adds a new item with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See get_item_accelerator() for more info on accelerators.

**Note:** The provided `id` is used only in id_pressed and id_focused signals. It's not related to the `index` arguments in e.g. set_item_checked().

---

 **add_multistate_item**(label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int) = 0, id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)

Adds a new multistate item with text `label`.

Contrarily to normal binary items, multistate items can have more than two states, as defined by `max_states`. The default value is defined by `default_state`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See get_item_accelerator() for more info on accelerators.

```gdscript
func _ready():
    add_multistate_item("Item", 3, 0)

    index_pressed.connect(func(index: int):
            toggle_item_multistate(index)
            match get_item_multistate(index):
                0:
                    print("First state")
                1:
                    print("Second state")
                2:
                    print("Third state")
        )
```

**Note:** Multistate items don't update their state automatically and must be done manually. See toggle_item_multistate(), set_item_multistate() and get_item_multistate() for more info on how to control it.

---

 **add_radio_check_item**(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1, accel: [Key](class_@globalscope.md#enum-globalscope-key) = 0)

Adds a new radio check button with text `label`.

An `id` can optionally be provided, as well as an accelerator (`accel`). If no `id` is provided, one will be created from the index. If no `accel` is provided, then the default value of 0 (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)) will be assigned to the item (which means it won't have any accelerator). See get_item_accelerator() for more info on accelerators.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See set_item_checked() for more info on how to control it.

---

 **add_radio_check_shortcut**(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false)

Adds a new radio check button and assigns a [Shortcut](class_shortcut.md#class-shortcut) to it. Sets the label of the checkbox to the [Shortcut](class_shortcut.md#class-shortcut)'s name.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See set_item_checked() for more info on how to control it.

---

 **add_separator**(label: [String](class_string.md#class-string) = "", id: [int](class_int.md#class-int) = -1)

Adds a separator between items. Separators also occupy an index, which you can set by using the `id` parameter.

A `label` can optionally be provided, which will appear at the center of the separator.

---

 **add_shortcut**(shortcut: [Shortcut](class_shortcut.md#class-shortcut), id: [int](class_int.md#class-int) = -1, global: [bool](class_bool.md#class-bool) = false, allow_echo: [bool](class_bool.md#class-bool) = false)

Adds a [Shortcut](class_shortcut.md#class-shortcut).

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

If `allow_echo` is `true`, the shortcut can be activated with echo events.

---

 **add_submenu_item**(label: [String](class_string.md#class-string), submenu: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1)

**Deprecated:** Prefer using add_submenu_node_item() instead.

Adds an item that will act as a submenu of the parent **PopupMenu** node when clicked. The `submenu` argument must be the name of an existing **PopupMenu** that has been added as a child to this node. This submenu will be shown when the item is clicked, hovered for long enough, or activated using the `ui_select` or `ui_right` input actions.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

---

 **add_submenu_node_item**(label: [String](class_string.md#class-string), submenu: PopupMenu, id: [int](class_int.md#class-int) = -1)

Adds an item that will act as a submenu of the parent **PopupMenu** node when clicked. This submenu will be shown when the item is clicked, hovered for long enough, or activated using the `ui_select` or `ui_right` input actions.

`submenu` must be either child of this **PopupMenu** or has no parent node (in which case it will be automatically added as a child). If the `submenu` popup has another parent, this method will fail.

An `id` can optionally be provided. If no `id` is provided, one will be created from the index.

---

 **clear**(free_submenus: [bool](class_bool.md#class-bool) = false)

Removes all items from the **PopupMenu**. If `free_submenus` is `true`, the submenu nodes are automatically freed.

---

[int](class_int.md#class-int) **get_focused_item**()

Returns the index of the currently focused item. Returns `-1` if no item is focused.

---

[Key](class_@globalscope.md#enum-globalscope-key) **get_item_accelerator**(index: [int](class_int.md#class-int))

Returns the accelerator of the item at the given `index`. An accelerator is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The return value is an integer which is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`). If no accelerator is defined for the specified `index`, get_item_accelerator() returns `0` (corresponding to [@GlobalScope.KEY_NONE](class_@globalscope.md#class-globalscope-constant-key-none)).

---

[AutoTranslateMode](class_node.md#enum-node-autotranslatemode) **get_item_auto_translate_mode**(index: [int](class_int.md#class-int))

Returns the auto translate mode of the item at the given `index`.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_item_icon**(index: [int](class_int.md#class-int))

Returns the icon of the item at the given `index`.

---

[int](class_int.md#class-int) **get_item_icon_max_width**(index: [int](class_int.md#class-int))

Returns the maximum allowed width of the icon for the item at the given `index`.

---

[Color](class_color.md#class-color) **get_item_icon_modulate**(index: [int](class_int.md#class-int))

Returns a [Color](class_color.md#class-color) modulating the item's icon at the given `index`.

---

[int](class_int.md#class-int) **get_item_id**(index: [int](class_int.md#class-int))

Returns the ID of the item at the given `index`.

---

[int](class_int.md#class-int) **get_item_indent**(index: [int](class_int.md#class-int))

Returns the horizontal offset of the item at the given `index`.

---

[int](class_int.md#class-int) **get_item_index**(id: [int](class_int.md#class-int))

Returns the index of the item containing the specified `id`. The index is automatically assigned to each item by the engine when added and represents the order items will be displayed.

---

[String](class_string.md#class-string) **get_item_language**(index: [int](class_int.md#class-int))

Returns item's text language code.

---

[Variant](class_variant.md#class-variant) **get_item_metadata**(index: [int](class_int.md#class-int))

Returns the metadata of the specified item, which might be of any type. You can set it with set_item_metadata(), which provides a simple way of assigning context data to items.

---

[int](class_int.md#class-int) **get_item_multistate**(index: [int](class_int.md#class-int))

Returns the state of the item at the given `index`.

---

[int](class_int.md#class-int) **get_item_multistate_max**(index: [int](class_int.md#class-int))

Returns the max states of the item at the given `index`.

---

[Shortcut](class_shortcut.md#class-shortcut) **get_item_shortcut**(index: [int](class_int.md#class-int))

Returns the [Shortcut](class_shortcut.md#class-shortcut) associated with the item at the given `index`.

---

[String](class_string.md#class-string) **get_item_submenu**(index: [int](class_int.md#class-int))

**Deprecated:** Prefer using get_item_submenu_node() instead.

Returns the submenu name of the item at the given `index`. See add_submenu_item() for more info on how to add a submenu.

---

PopupMenu **get_item_submenu_node**(index: [int](class_int.md#class-int))

Returns the submenu of the item at the given `index`, or `null` if no submenu was added. See add_submenu_node_item() for more info on how to add a submenu.

---

[String](class_string.md#class-string) **get_item_text**(index: [int](class_int.md#class-int))

Returns the text of the item at the given `index`.

---

[TextDirection](class_control.md#enum-control-textdirection) **get_item_text_direction**(index: [int](class_int.md#class-int))

Returns item's text base writing direction.

---

[String](class_string.md#class-string) **get_item_tooltip**(index: [int](class_int.md#class-int))

Returns the tooltip associated with the item at the given `index`.

---

[bool](class_bool.md#class-bool) **is_item_checkable**(index: [int](class_int.md#class-int))

Returns `true` if the item at the given `index` is checkable in some way, i.e. if it has a checkbox or radio button.

**Note:** Checkable items just display a checkmark or radio button, but don't have any built-in checking behavior and must be checked/unchecked manually.

---

[bool](class_bool.md#class-bool) **is_item_checked**(index: [int](class_int.md#class-int))

Returns `true` if the item at the given `index` is checked.

---

[bool](class_bool.md#class-bool) **is_item_disabled**(index: [int](class_int.md#class-int))

Returns `true` if the item at the given `index` is disabled. When it is disabled it can't be selected, or its action invoked.

See set_item_disabled() for more info on how to disable an item.

---

[bool](class_bool.md#class-bool) **is_item_radio_checkable**(index: [int](class_int.md#class-int))

Returns `true` if the item at the given `index` has radio button-style checkability.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

---

[bool](class_bool.md#class-bool) **is_item_separator**(index: [int](class_int.md#class-int))

Returns `true` if the item is a separator. If it is, it will be displayed as a line. See add_separator() for more info on how to add a separator.

---

[bool](class_bool.md#class-bool) **is_item_shortcut_disabled**(index: [int](class_int.md#class-int))

Returns `true` if the specified item's shortcut is disabled.

---

[bool](class_bool.md#class-bool) **is_native_menu**()

Returns `true` if the system native menu is supported and currently used by this **PopupMenu**.

---

[bool](class_bool.md#class-bool) **is_system_menu**()

Returns `true` if the menu is bound to the special system menu.

---

 **remove_item**(index: [int](class_int.md#class-int))

Removes the item at the given `index` from the menu.

**Note:** The indices of items after the removed item will be shifted by one.

---

 **scroll_to_item**(index: [int](class_int.md#class-int))

Moves the scroll view to make the item at the given `index` visible.

---

 **set_focused_item**(index: [int](class_int.md#class-int))

Sets the currently focused item as the given `index`.

Passing `-1` as the index makes so that no item is focused.

---

 **set_item_accelerator**(index: [int](class_int.md#class-int), accel: [Key](class_@globalscope.md#enum-globalscope-key))

Sets the accelerator of the item at the given `index`. An accelerator is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. `accel` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

---

 **set_item_as_checkable**(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

Sets whether the item at the given `index` has a checkbox. If `false`, sets the type of the item to plain text.

**Note:** Checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually.

---

 **set_item_as_radio_checkable**(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

Sets the type of the item at the given `index` to radio button. If `false`, sets the type of the item to plain text.

---

 **set_item_as_separator**(index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

Mark the item at the given `index` as a separator, which means that it would be displayed as a line. If `false`, sets the type of the item to plain text.

---

 **set_item_auto_translate_mode**(index: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode))

Sets the auto translate mode of the item at the given `index`.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class-node-constant-auto-translate-mode-inherit) by default, which uses the same auto translate mode as the **PopupMenu** itself.

---

 **set_item_checked**(index: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool))

Sets the checkstate status of the item at the given `index`.

---

 **set_item_disabled**(index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

Enables/disables the item at the given `index`. When it is disabled, it can't be selected and its action can't be invoked.

---

 **set_item_icon**(index: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Replaces the [Texture2D](class_texture2d.md#class-texture2d) icon of the item at the given `index`.

---

 **set_item_icon_max_width**(index: [int](class_int.md#class-int), width: [int](class_int.md#class-int))

Sets the maximum allowed width of the icon for the item at the given `index`. This limit is applied on top of the default size of the icon and on top of icon_max_width. The height is adjusted according to the icon's ratio.

---

 **set_item_icon_modulate**(index: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color))

Sets a modulating [Color](class_color.md#class-color) of the item's icon at the given `index`.

---

 **set_item_id**(index: [int](class_int.md#class-int), id: [int](class_int.md#class-int))

Sets the `id` of the item at the given `index`.

The `id` is used in id_pressed and id_focused signals.

---

 **set_item_indent**(index: [int](class_int.md#class-int), indent: [int](class_int.md#class-int))

Sets the horizontal offset of the item at the given `index`.

---

 **set_item_index**(index: [int](class_int.md#class-int), target_index: [int](class_int.md#class-int))

Changes the index of the item at index `index` to be at index `target_index`. This can be used to move an item above other items. The moved item will keep the same ID, even if it was generated from the original index.

**Note:** The indices of any items between index `index` and index `target_index` will be shifted by one.

---

 **set_item_language**(index: [int](class_int.md#class-int), language: [String](class_string.md#class-string))

Sets the language code of the text for the item at the given index to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---

 **set_item_metadata**(index: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))

Sets the metadata of an item, which may be of any type. You can later get it with get_item_metadata(), which provides a simple way of assigning context data to items.

---

 **set_item_multistate**(index: [int](class_int.md#class-int), state: [int](class_int.md#class-int))

Sets the state of a multistate item. See add_multistate_item() for details.

---

 **set_item_multistate_max**(index: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int))

Sets the max states of a multistate item. See add_multistate_item() for details.

---

 **set_item_shortcut**(index: [int](class_int.md#class-int), shortcut: [Shortcut](class_shortcut.md#class-shortcut), global: [bool](class_bool.md#class-bool) = false)

Sets a [Shortcut](class_shortcut.md#class-shortcut) for the item at the given `index`.

---

 **set_item_shortcut_disabled**(index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

Disables the [Shortcut](class_shortcut.md#class-shortcut) of the item at the given `index`.

---

 **set_item_submenu**(index: [int](class_int.md#class-int), submenu: [String](class_string.md#class-string))

**Deprecated:** Prefer using set_item_submenu_node() instead.

Sets the submenu of the item at the given `index`. The submenu is the name of a child **PopupMenu** node that would be shown when the item is clicked.

---

 **set_item_submenu_node**(index: [int](class_int.md#class-int), submenu: PopupMenu)

Sets the submenu of the item at the given `index`. The submenu is a **PopupMenu** node that would be shown when the item is clicked. It must either be a child of this **PopupMenu** or has no parent (in which case it will be automatically added as a child). If the `submenu` popup has another parent, this method will fail.

---

 **set_item_text**(index: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

Sets the text of the item at the given `index`.

---

 **set_item_text_direction**(index: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection))

Sets item's text base writing direction.

---

 **set_item_tooltip**(index: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets the [String](class_string.md#class-string) tooltip of the item at the given `index`.

---

 **toggle_item_checked**(index: [int](class_int.md#class-int))

Toggles the check state of the item at the given `index`.

---

 **toggle_item_multistate**(index: [int](class_int.md#class-int))

Cycle to the next state of a multistate item. See add_multistate_item() for details.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **font_accelerator_color** = `Color(0.7, 0.7, 0.7, 0.8)`

The text [Color](class_color.md#class-color) used for shortcuts and accelerators that show next to the menu item name when defined. See get_item_accelerator() for more info on accelerators.

---

[Color](class_color.md#class-color) **font_color** = `Color(0.875, 0.875, 0.875, 1)`

The default text [Color](class_color.md#class-color) for menu items' names.

---

[Color](class_color.md#class-color) **font_disabled_color** = `Color(0.4, 0.4, 0.4, 0.8)`

[Color](class_color.md#class-color) used for disabled menu items' text.

---

[Color](class_color.md#class-color) **font_hover_color** = `Color(0.875, 0.875, 0.875, 1)`

[Color](class_color.md#class-color) used for the hovered text.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The tint of text outline of the menu item.

---

[Color](class_color.md#class-color) **font_separator_color** = `Color(0.875, 0.875, 0.875, 1)`

[Color](class_color.md#class-color) used for labeled separators' text. See add_separator().

---

[Color](class_color.md#class-color) **font_separator_outline_color** = `Color(0, 0, 0, 1)`

The tint of text outline of the labeled separator.

---

[int](class_int.md#class-int) **gutter_compact** = `1`

If not `0`, the icon gutter will be merged with the checkbox gutter when possible. This acts as a boolean.

---

[int](class_int.md#class-int) **h_separation** = `4`

The horizontal space between the item's elements.

---

[int](class_int.md#class-int) **icon_max_width** = `0`

The maximum allowed width of the item's icon. This limit is applied on top of the default size of the icon, but before the value set with set_item_icon_max_width(). The height is adjusted according to the icon's ratio.

---

[int](class_int.md#class-int) **indent** = `10`

Width of the single indentation level.

---

[int](class_int.md#class-int) **item_end_padding** = `2`

Horizontal padding to the right of the items (or left, in RTL layout).

---

[int](class_int.md#class-int) **item_start_padding** = `2`

Horizontal padding to the left of the items (or right, in RTL layout).

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the item text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[int](class_int.md#class-int) **search_bar_separation** = `4`

The vertical space between search bar and menu items.

---

[int](class_int.md#class-int) **separator_outline_size** = `0`

The size of the labeled separator text outline.

---

[int](class_int.md#class-int) **v_separation** = `4`

The vertical space between each menu item.

---

[Font](class_font.md#class-font) **font**

[Font](class_font.md#class-font) used for the menu items.

---

[Font](class_font.md#class-font) **font_separator**

[Font](class_font.md#class-font) used for the labeled separator.

---

[int](class_int.md#class-int) **font_separator_size**

Font size of the labeled separator.

---

[int](class_int.md#class-int) **font_size**

Font size of the menu items.

---

[Texture2D](class_texture2d.md#class-texture2d) **checked**

[Texture2D](class_texture2d.md#class-texture2d) icon for the checked checkbox items.

---

[Texture2D](class_texture2d.md#class-texture2d) **checked_disabled**

[Texture2D](class_texture2d.md#class-texture2d) icon for the checked checkbox items when they are disabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **radio_checked**

[Texture2D](class_texture2d.md#class-texture2d) icon for the checked radio button items.

---

[Texture2D](class_texture2d.md#class-texture2d) **radio_checked_disabled**

[Texture2D](class_texture2d.md#class-texture2d) icon for the checked radio button items when they are disabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **radio_unchecked**

[Texture2D](class_texture2d.md#class-texture2d) icon for the unchecked radio button items.

---

[Texture2D](class_texture2d.md#class-texture2d) **radio_unchecked_disabled**

[Texture2D](class_texture2d.md#class-texture2d) icon for the unchecked radio button items when they are disabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **search**

[Texture2D](class_texture2d.md#class-texture2d) icon for the search bar's search icon.

---

[Texture2D](class_texture2d.md#class-texture2d) **submenu**

[Texture2D](class_texture2d.md#class-texture2d) icon for the submenu arrow (for left-to-right layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **submenu_mirrored**

[Texture2D](class_texture2d.md#class-texture2d) icon for the submenu arrow (for right-to-left layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **unchecked**

[Texture2D](class_texture2d.md#class-texture2d) icon for the unchecked checkbox items.

---

[Texture2D](class_texture2d.md#class-texture2d) **unchecked_disabled**

[Texture2D](class_texture2d.md#class-texture2d) icon for the unchecked checkbox items when they are disabled.

---

[StyleBox](class_stylebox.md#class-stylebox) **hover**

[StyleBox](class_stylebox.md#class-stylebox) displayed when the **PopupMenu** item is hovered.

---

[StyleBox](class_stylebox.md#class-stylebox) **labeled_separator_left**

[StyleBox](class_stylebox.md#class-stylebox) for the left side of labeled separator. See add_separator().

---

[StyleBox](class_stylebox.md#class-stylebox) **labeled_separator_right**

[StyleBox](class_stylebox.md#class-stylebox) for the right side of labeled separator. See add_separator().

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

[StyleBox](class_stylebox.md#class-stylebox) for the background panel.

---

[StyleBox](class_stylebox.md#class-stylebox) **separator**

[StyleBox](class_stylebox.md#class-stylebox) used for the separators. See add_separator().
