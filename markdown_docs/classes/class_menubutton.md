# MenuButton

**Inherits:** [Button](class_button.md#class-button) **<** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that brings up a [PopupMenu](class_popupmenu.md#class-popupmenu) when clicked.

## Description

A button that brings up a [PopupMenu](class_popupmenu.md#class-popupmenu) when clicked. To create new items inside this [PopupMenu](class_popupmenu.md#class-popupmenu), use `get_popup().add_item("My Item Name")`. You can also create them directly from Godot editor's inspector.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

## Properties

| [ActionMode](class_basebutton.md#enum-basebutton-actionmode)   | action_mode                                                                           | `0` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-action-mode))    |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                               | flat                                                                                  | `true` (overrides [Button](class_button.md#class-button-property-flat))                    |
| [FocusMode](class_control.md#enum-control-focusmode)           | focus_mode                                                                            | `3` (overrides [Control](class_control.md#class-control-property-focus-mode))              |
| [int](class_int.md#class-int)                                  | item_count                                   | `0`                                                                                        |
| [int](class_int.md#class-int)                                  | popup/item_{index}/checkable | `0`                                                                                        |
| [bool](class_bool.md#class-bool)                               | popup/item_{index}/checked     | `false`                                                                                    |
| [bool](class_bool.md#class-bool)                               | popup/item_{index}/disabled   | `false`                                                                                    |
| [Texture2D](class_texture2d.md#class-texture2d)                | popup/item_{index}/icon           |                                                                                            |
| [int](class_int.md#class-int)                                  | popup/item_{index}/id               | `0`                                                                                        |
| [bool](class_bool.md#class-bool)                               | popup/item_{index}/separator | `false`                                                                                    |
| [String](class_string.md#class-string)                         | popup/item_{index}/text           | `""`                                                                                       |
| [bool](class_bool.md#class-bool)                               | switch_on_hover                         | `false`                                                                                    |
| [bool](class_bool.md#class-bool)                               | toggle_mode                                                                           | `true` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-toggle-mode)) |

## Methods

| [PopupMenu](class_popupmenu.md#class-popupmenu)   | get_popup()                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|                                                   | set_disable_shortcuts(disabled: [bool](class_bool.md#class-bool)) |
|                                                   | show_popup()                                                                 |

---

## Signals

**about_to_popup**()

Emitted when the [PopupMenu](class_popupmenu.md#class-popupmenu) of this MenuButton is about to show.

---

## Property Descriptions

[int](class_int.md#class-int) **item_count** = `0`

-  **set_item_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_item_count**()

The number of items currently in the list.

---

[int](class_int.md#class-int) **popup/item_{index}/checkable** = `0`

The checkable item type of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

---

[bool](class_bool.md#class-bool) **popup/item_{index}/checked** = `false`

If `true`, the item at `index` is checked.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

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

[bool](class_bool.md#class-bool) **switch_on_hover** = `false`

-  **set_switch_on_hover**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_switch_on_hover**()

If `true`, when the cursor hovers above another **MenuButton** within the same parent which also has switch_on_hover enabled, it will close the current **MenuButton** and open the other one.

---

## Method Descriptions

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_popup**()

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) contained in this button.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---

 **set_disable_shortcuts**(disabled: [bool](class_bool.md#class-bool))

If `true`, shortcuts are disabled and cannot be used to trigger the button.

---

 **show_popup**()

Adjusts popup position and sizing for the **MenuButton**, then shows the [PopupMenu](class_popupmenu.md#class-popupmenu). Prefer this over using `get_popup().popup()`.
