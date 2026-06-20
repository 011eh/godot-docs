# OptionButton

**Inherits:** [Button](class_button.md#class-button) **<** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that brings up a dropdown with selectable options when pressed.

## Description

**OptionButton** is a type of button that brings up a dropdown with selectable items when pressed. The item selected becomes the "current" item and is displayed as the button text.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

**Note:** The IDs used for items are limited to signed 32-bit integers, not the full 64 bits of [int](class_int.md#class-int). These have a range of `-2^31` to `2^31 - 1`, that is, `-2147483648` to `2147483647`.

**Note:** The [Button.text](class_button.md#class-button-property-text) and [Button.icon](class_button.md#class-button-property-icon) properties are set automatically based on the selected item. They shouldn't be changed manually.

## Properties

| [ActionMode](class_basebutton.md#enum-basebutton-actionmode)                      | action_mode                                                                                           | `0` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-action-mode))    |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | alignment                                                                                             | `0` (overrides [Button](class_button.md#class-button-property-alignment))                  |
| [bool](class_bool.md#class-bool)                                                  | allow_reselect                                         | `false`                                                                                    |
| [bool](class_bool.md#class-bool)                                                  | fit_to_longest_item                               | `true`                                                                                     |
| [int](class_int.md#class-int)                                                     | item_count                                                 | `0`                                                                                        |
| [bool](class_bool.md#class-bool)                                                  | popup/item_{index}/disabled                 | `false`                                                                                    |
| [Texture2D](class_texture2d.md#class-texture2d)                                   | popup/item_{index}/icon                         |                                                                                            |
| [int](class_int.md#class-int)                                                     | popup/item_{index}/id                             | `0`                                                                                        |
| [bool](class_bool.md#class-bool)                                                  | popup/item_{index}/separator               | `false`                                                                                    |
| [String](class_string.md#class-string)                                            | popup/item_{index}/text                         | `""`                                                                                       |
| [bool](class_bool.md#class-bool)                                                  | search_bar_enabled                                 | `false`                                                                                    |
| [bool](class_bool.md#class-bool)                                                  | search_bar_fuzzy_search_enabled       | `true`                                                                                     |
| [int](class_int.md#class-int)                                                     | search_bar_fuzzy_search_max_misses | `2`                                                                                        |
| [int](class_int.md#class-int)                                                     | search_bar_min_item_count                   | `0`                                                                                        |
| [int](class_int.md#class-int)                                                     | selected                                                     | `-1`                                                                                       |
| [bool](class_bool.md#class-bool)                                                  | toggle_mode                                                                                           | `true` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-toggle-mode)) |

## Methods

|                                                                | add_icon_item(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1)   |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                | add_item(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1)                                                                       |
|                                                                | add_separator(text: [String](class_string.md#class-string) = "")                                                                                                 |
|                                                                | clear()                                                                                                                                                                  |
| [AutoTranslateMode](class_node.md#enum-node-autotranslatemode) | get_item_auto_translate_mode(idx: [int](class_int.md#class-int))                                                                                  |
| [Texture2D](class_texture2d.md#class-texture2d)                | get_item_icon(idx: [int](class_int.md#class-int))                                                                                                                |
| [int](class_int.md#class-int)                                  | get_item_id(idx: [int](class_int.md#class-int))                                                                                                                    |
| [int](class_int.md#class-int)                                  | get_item_index(id: [int](class_int.md#class-int))                                                                                                               |
| [Variant](class_variant.md#class-variant)                      | get_item_metadata(idx: [int](class_int.md#class-int))                                                                                                        |
| [String](class_string.md#class-string)                         | get_item_text(idx: [int](class_int.md#class-int))                                                                                                                |
| [String](class_string.md#class-string)                         | get_item_tooltip(idx: [int](class_int.md#class-int))                                                                                                          |
| [PopupMenu](class_popupmenu.md#class-popupmenu)                | get_popup()                                                                                                                                                          |
| [int](class_int.md#class-int)                                  | get_selectable_item(from_last: [bool](class_bool.md#class-bool) = false)                                                                                   |
| [int](class_int.md#class-int)                                  | get_selected_id()                                                                                                                                              |
| [Variant](class_variant.md#class-variant)                      | get_selected_metadata()                                                                                                                                  |
| [bool](class_bool.md#class-bool)                               | has_selectable_items()                                                                                                                                    |
| [bool](class_bool.md#class-bool)                               | is_item_disabled(idx: [int](class_int.md#class-int))                                                                                                          |
| [bool](class_bool.md#class-bool)                               | is_item_separator(idx: [int](class_int.md#class-int))                                                                                                        |
|                                                                | remove_item(idx: [int](class_int.md#class-int))                                                                                                                    |
|                                                                | select(idx: [int](class_int.md#class-int))                                                                                                                              |
|                                                                | set_disable_shortcuts(disabled: [bool](class_bool.md#class-bool))                                                                                        |
|                                                                | set_item_auto_translate_mode(idx: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode))            |
|                                                                | set_item_disabled(idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                            |
|                                                                | set_item_icon(idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))                                                      |
|                                                                | set_item_id(idx: [int](class_int.md#class-int), id: [int](class_int.md#class-int))                                                                                 |
|                                                                | set_item_metadata(idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))                                                   |
|                                                                | set_item_text(idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                  |
|                                                                | set_item_tooltip(idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                                         |
|                                                                | show_popup()                                                                                                                                                        |

## Theme Properties

| [int](class_int.md#class-int)                   | arrow_margin     | `4`   |
|-------------------------------------------------|---------------------------------------------------------------------|-------|
| [int](class_int.md#class-int)                   | modulate_arrow | `0`   |
| [Texture2D](class_texture2d.md#class-texture2d) | arrow                       |       |

---

## Signals

**item_focused**(index: [int](class_int.md#class-int))

Emitted when the user navigates to an item using the [ProjectSettings.input/ui_up](class_projectsettings.md#class-projectsettings-property-input-ui-up) or [ProjectSettings.input/ui_down](class_projectsettings.md#class-projectsettings-property-input-ui-down) input actions. The index of the item focused is passed as argument.

---

**item_selected**(index: [int](class_int.md#class-int))

Emitted when the current item has been changed by the user. The index of the item selected is passed as argument.

allow_reselect must be enabled to reselect an item.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_reselect** = `false`

-  **set_allow_reselect**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_allow_reselect**()

If `true`, the currently selected item can be selected again.

---

[bool](class_bool.md#class-bool) **fit_to_longest_item** = `true`

-  **set_fit_to_longest_item**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_fit_to_longest_item**()

If `true`, minimum size will be determined by the longest item's text, instead of the currently selected one's.

**Note:** For performance reasons, the minimum size doesn't update immediately when adding, removing or modifying items.

---

[int](class_int.md#class-int) **item_count** = `0`

-  **set_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_count**()

The number of items to select from.

---

[bool](class_bool.md#class-bool) **popup/item_{index}/disabled** = `false`

If `true`, the item at `index` is disabled.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[Texture2D](class_texture2d.md#class-texture2d) **popup/item_{index}/icon**

The icon of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[int](class_int.md#class-int) **popup/item_{index}/id** = `0`

The ID of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[bool](class_bool.md#class-bool) **popup/item_{index}/separator** = `false`

If `true`, the item at `index` is a separator.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[String](class_string.md#class-string) **popup/item_{index}/text** = `""`

The text of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[bool](class_bool.md#class-bool) **search_bar_enabled** = `false`

-  **set_search_bar_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_search_bar_enabled**()

If `true`, shows a search bar at the top of the [PopupMenu](class_popupmenu.md#class-popupmenu) for filtering items. See search_bar_min_item_count for dynamically controlling its visibility based on the number of items.

---

[bool](class_bool.md#class-bool) **search_bar_fuzzy_search_enabled** = `true`

-  **set_search_bar_fuzzy_search_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_search_bar_fuzzy_search_enabled**()

If `true`, enables fuzzy searching in the [PopupMenu](class_popupmenu.md#class-popupmenu) search bar. This allows the search results to include items that almost match the search query, as well items that match the individual characters of the search query, but not in sequence.

Use search_bar_fuzzy_search_max_misses to set the maximum number of mismatches allowed in the search results.

---

[int](class_int.md#class-int) **search_bar_fuzzy_search_max_misses** = `2`

-  **set_search_bar_fuzzy_search_max_misses**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_search_bar_fuzzy_search_max_misses**()

Sets the maximum number of mismatches allowed in each search result when fuzzy searching is enabled for the [PopupMenu](class_popupmenu.md#class-popupmenu) search bar. Any item with more mismatches will be hidden from the search results.

---

[int](class_int.md#class-int) **search_bar_min_item_count** = `0`

-  **set_search_bar_min_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_search_bar_min_item_count**()

Sets the minimum number of items required for the [PopupMenu](class_popupmenu.md#class-popupmenu) search bar to be visible. search_bar_enabled must be `true` for this to have any effect.

---

[int](class_int.md#class-int) **selected** = `-1`

- [int](class_int.md#class-int) **get_selected**()

The index of the currently selected item, or `-1` if no item is selected.

---

## Method Descriptions

 **add_icon_item**(texture: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1)

Adds an item, with a `texture` icon, text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

**Note:** The item will be selected if there are no other items.

---

 **add_item**(label: [String](class_string.md#class-string), id: [int](class_int.md#class-int) = -1)

Adds an item, with text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

**Note:** The item will be selected if there are no other items.

---

 **add_separator**(text: [String](class_string.md#class-string) = "")

Adds a separator to the list of items. Separators help to group items, and can optionally be given a `text` header. A separator also gets an index assigned, and is appended at the end of the item list.

---

 **clear**()

Clears all the items in the **OptionButton**.

---

[AutoTranslateMode](class_node.md#enum-node-autotranslatemode) **get_item_auto_translate_mode**(idx: [int](class_int.md#class-int))

Returns the auto translate mode of the item at index `idx`.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_item_icon**(idx: [int](class_int.md#class-int))

Returns the icon of the item at index `idx`.

---

[int](class_int.md#class-int) **get_item_id**(idx: [int](class_int.md#class-int))

Returns the ID of the item at index `idx`.

---

[int](class_int.md#class-int) **get_item_index**(id: [int](class_int.md#class-int))

Returns the index of the item with the given `id`.

---

[Variant](class_variant.md#class-variant) **get_item_metadata**(idx: [int](class_int.md#class-int))

Retrieves the metadata of an item. Metadata may be any type and can be used to store extra information about an item, such as an external string ID.

---

[String](class_string.md#class-string) **get_item_text**(idx: [int](class_int.md#class-int))

Returns the text of the item at index `idx`.

---

[String](class_string.md#class-string) **get_item_tooltip**(idx: [int](class_int.md#class-int))

Returns the tooltip of the item at index `idx`.

---

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_popup**()

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) contained in this button.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---

[int](class_int.md#class-int) **get_selectable_item**(from_last: [bool](class_bool.md#class-bool) = false)

Returns the index of the first item which is not disabled, or marked as a separator. If `from_last` is `true`, the items will be searched in reverse order.

Returns `-1` if no item is found.

---

[int](class_int.md#class-int) **get_selected_id**()

Returns the ID of the selected item, or `-1` if no item is selected.

---

[Variant](class_variant.md#class-variant) **get_selected_metadata**()

Gets the metadata of the selected item. Metadata for items can be set using set_item_metadata().

---

[bool](class_bool.md#class-bool) **has_selectable_items**()

Returns `true` if this button contains at least one item which is not disabled, or marked as a separator.

---

[bool](class_bool.md#class-bool) **is_item_disabled**(idx: [int](class_int.md#class-int))

Returns `true` if the item at index `idx` is disabled.

---

[bool](class_bool.md#class-bool) **is_item_separator**(idx: [int](class_int.md#class-int))

Returns `true` if the item at index `idx` is marked as a separator.

---

 **remove_item**(idx: [int](class_int.md#class-int))

Removes the item at index `idx`.

---

 **select**(idx: [int](class_int.md#class-int))

Selects an item by index and makes it the current item. This will work even if the item is disabled.

Passing `-1` as the index deselects any currently selected item.

---

 **set_disable_shortcuts**(disabled: [bool](class_bool.md#class-bool))

If `true`, shortcuts are disabled and cannot be used to trigger the button.

---

 **set_item_auto_translate_mode**(idx: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode))

Sets the auto translate mode of the item at index `idx`.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class-node-constant-auto-translate-mode-inherit) by default, which uses the same auto translate mode as the **OptionButton** itself.

---

 **set_item_disabled**(idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

Sets whether the item at index `idx` is disabled.

Disabled items are drawn differently in the dropdown and are not selectable by the user. If the current selected item is set as disabled, it will remain selected.

---

 **set_item_icon**(idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))

Sets the icon of the item at index `idx`.

---

 **set_item_id**(idx: [int](class_int.md#class-int), id: [int](class_int.md#class-int))

Sets the ID of the item at index `idx`.

---

 **set_item_metadata**(idx: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))

Sets the metadata of an item. Metadata may be of any type and can be used to store extra information about an item, such as an external string ID.

---

 **set_item_text**(idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

Sets the text of the item at index `idx`.

---

 **set_item_tooltip**(idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets the tooltip of the item at index `idx`.

---

 **show_popup**()

Adjusts popup position and sizing for the **OptionButton**, then shows the [PopupMenu](class_popupmenu.md#class-popupmenu). Prefer this over using `get_popup().popup()`.

---

## Theme Property Descriptions

[int](class_int.md#class-int) **arrow_margin** = `4`

The horizontal space between the arrow icon and the right edge of the button.

---

[int](class_int.md#class-int) **modulate_arrow** = `0`

If different than `0`, the arrow icon will be modulated to the font color.

---

[Texture2D](class_texture2d.md#class-texture2d) **arrow**

The arrow icon to be drawn on the right end of the button.
