# CheckButton

**Inherits:** [Button](class_button.md#class-button) **<** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that represents a binary choice.

## Description

**CheckButton** is a toggle button displayed as a check field. It's similar to [CheckBox](class_checkbox.md#class-checkbox) in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use **CheckButton** when toggling it has an **immediate** effect on something. For example, it can be used when pressing it shows or hides advanced settings, without asking the user to confirm this action.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

## Properties

| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)   | alignment   | `0` (overrides [Button](class_button.md#class-button-property-alignment))                  |
|-------------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                    | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-toggle-mode)) |

## Theme Properties

| [Color](class_color.md#class-color)             | button_checked_color              | `Color(1, 1, 1, 1)`   |
|-------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------|
| [Color](class_color.md#class-color)             | button_unchecked_color          | `Color(1, 1, 1, 1)`   |
| [int](class_int.md#class-int)                   | check_v_offset                       | `0`                   |
| [Texture2D](class_texture2d.md#class-texture2d) | checked                                         |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | checked_disabled                       |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | checked_disabled_mirrored     |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | checked_mirrored                       |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | unchecked                                     |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | unchecked_disabled                   |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | unchecked_disabled_mirrored |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | unchecked_mirrored                   |                       |

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **button_checked_color** = `Color(1, 1, 1, 1)`

The color of the checked icon when the checkbox is pressed.

---

[Color](class_color.md#class-color) **button_unchecked_color** = `Color(1, 1, 1, 1)`

The color of the unchecked icon when the checkbox is not pressed.

---

[int](class_int.md#class-int) **check_v_offset** = `0`

The vertical offset used when rendering the toggle icons (in pixels).

---

[Texture2D](class_texture2d.md#class-texture2d) **checked**

The icon to display when the **CheckButton** is checked (for left-to-right layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **checked_disabled**

The icon to display when the **CheckButton** is checked and disabled (for left-to-right layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **checked_disabled_mirrored**

The icon to display when the **CheckButton** is checked and disabled (for right-to-left layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **checked_mirrored**

The icon to display when the **CheckButton** is checked (for right-to-left layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **unchecked**

The icon to display when the **CheckButton** is unchecked (for left-to-right layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **unchecked_disabled**

The icon to display when the **CheckButton** is unchecked and disabled (for left-to-right layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **unchecked_disabled_mirrored**

The icon to display when the **CheckButton** is unchecked and disabled (for right-to-left layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **unchecked_mirrored**

The icon to display when the **CheckButton** is unchecked (for right-to-left layouts).
