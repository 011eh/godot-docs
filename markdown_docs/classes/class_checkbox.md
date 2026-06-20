# CheckBox

**Inherits:** [Button](class_button.md#class-button) **<** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that represents a binary choice.

## Description

**CheckBox** allows the user to choose one of only two possible options. It's similar to [CheckButton](class_checkbutton.md#class-checkbutton) in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use **CheckBox** when toggling it has **no** immediate effect on something. For example, it could be used when toggling it will only do something once a confirmation button is pressed.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

When [BaseButton.button_group](class_basebutton.md#class-basebutton-property-button-group) specifies a [ButtonGroup](class_buttongroup.md#class-buttongroup), **CheckBox** changes its appearance to that of a radio button and uses the various `radio_*` theme properties.

## Properties

| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)   | alignment   | `0` (overrides [Button](class_button.md#class-button-property-alignment))                  |
|-------------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                    | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-toggle-mode)) |

## Theme Properties

| [Color](class_color.md#class-color)             | checkbox_checked_color     | `Color(1, 1, 1, 1)`   |
|-------------------------------------------------|----------------------------------------------------------------------------------|-----------------------|
| [Color](class_color.md#class-color)             | checkbox_unchecked_color | `Color(1, 1, 1, 1)`   |
| [int](class_int.md#class-int)                   | check_v_offset                  | `0`                   |
| [Texture2D](class_texture2d.md#class-texture2d) | checked                                    |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | checked_disabled                  |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | radio_checked                        |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | radio_checked_disabled      |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | radio_unchecked                    |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | radio_unchecked_disabled  |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | unchecked                                |                       |
| [Texture2D](class_texture2d.md#class-texture2d) | unchecked_disabled              |                       |

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **checkbox_checked_color** = `Color(1, 1, 1, 1)`

The color of the checked icon when the checkbox is pressed.

---

[Color](class_color.md#class-color) **checkbox_unchecked_color** = `Color(1, 1, 1, 1)`

The color of the unchecked icon when the checkbox is not pressed.

---

[int](class_int.md#class-int) **check_v_offset** = `0`

The vertical offset used when rendering the check icons (in pixels).

---

[Texture2D](class_texture2d.md#class-texture2d) **checked**

The check icon to display when the **CheckBox** is checked.

---

[Texture2D](class_texture2d.md#class-texture2d) **checked_disabled**

The check icon to display when the **CheckBox** is checked and is disabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **radio_checked**

The check icon to display when the **CheckBox** is configured as a radio button and is checked.

---

[Texture2D](class_texture2d.md#class-texture2d) **radio_checked_disabled**

The check icon to display when the **CheckBox** is configured as a radio button, is disabled, and is unchecked.

---

[Texture2D](class_texture2d.md#class-texture2d) **radio_unchecked**

The check icon to display when the **CheckBox** is configured as a radio button and is unchecked.

---

[Texture2D](class_texture2d.md#class-texture2d) **radio_unchecked_disabled**

The check icon to display when the **CheckBox** is configured as a radio button, is disabled, and is unchecked.

---

[Texture2D](class_texture2d.md#class-texture2d) **unchecked**

The check icon to display when the **CheckBox** is unchecked.

---

[Texture2D](class_texture2d.md#class-texture2d) **unchecked_disabled**

The check icon to display when the **CheckBox** is unchecked and is disabled.
