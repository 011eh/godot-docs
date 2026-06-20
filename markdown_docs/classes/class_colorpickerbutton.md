# ColorPickerButton

**Inherits:** [Button](class_button.md#class-button) **<** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that brings up a [ColorPicker](class_colorpicker.md#class-colorpicker) when pressed.

## Description

Encapsulates a [ColorPicker](class_colorpicker.md#class-colorpicker), making it accessible by pressing a button. Pressing the button will toggle the [ColorPicker](class_colorpicker.md#class-colorpicker)'s visibility.

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

**Note:** By default, the button may not be wide enough for the color preview swatch to be visible. Make sure to set [Control.custom_minimum_size](class_control.md#class-control-property-custom-minimum-size) to a big enough value to give the button enough space.

## Tutorials

- [2D GD Paint Demo](https://godotengine.org/asset-library/asset/2768)
- [GUI Drag And Drop Demo](https://godotengine.org/asset-library/asset/2767)

## Properties

| [Color](class_color.md#class-color)   | color                   | `Color(0, 0, 0, 1)`                                                                        |
|---------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)      | edit_alpha         | `true`                                                                                     |
| [bool](class_bool.md#class-bool)      | edit_intensity | `true`                                                                                     |
| [bool](class_bool.md#class-bool)      | toggle_mode                                                        | `true` (overrides [BaseButton](class_basebutton.md#class-basebutton-property-toggle-mode)) |

## Methods

| [ColorPicker](class_colorpicker.md#class-colorpicker)   | get_picker()   |
|---------------------------------------------------------|--------------------------------------------------------------|
| [PopupPanel](class_popuppanel.md#class-popuppanel)      | get_popup()     |

## Theme Properties

| [Texture2D](class_texture2d.md#class-texture2d)   | bg   |
|---------------------------------------------------|------------------------------------------------|

---

## Signals

**color_changed**(color: [Color](class_color.md#class-color))

Emitted when the color changes.

---

**picker_created**()

Emitted when the [ColorPicker](class_colorpicker.md#class-colorpicker) is created (the button is pressed for the first time).

---

**popup_closed**()

Emitted when the [ColorPicker](class_colorpicker.md#class-colorpicker) is closed.

---

## Property Descriptions

[Color](class_color.md#class-color) **color** = `Color(0, 0, 0, 1)`

-  **set_pick_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_pick_color**()

The currently selected color.

---

[bool](class_bool.md#class-bool) **edit_alpha** = `true`

-  **set_edit_alpha**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_alpha**()

If `true`, the alpha channel in the displayed [ColorPicker](class_colorpicker.md#class-colorpicker) will be visible.

---

[bool](class_bool.md#class-bool) **edit_intensity** = `true`

-  **set_edit_intensity**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_intensity**()

If `true`, the intensity slider in the displayed [ColorPicker](class_colorpicker.md#class-colorpicker) will be visible.

---

## Method Descriptions

[ColorPicker](class_colorpicker.md#class-colorpicker) **get_picker**()

Returns the [ColorPicker](class_colorpicker.md#class-colorpicker) that this node toggles.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

[PopupPanel](class_popuppanel.md#class-popuppanel) **get_popup**()

Returns the control's [PopupPanel](class_popuppanel.md#class-popuppanel) which allows you to connect to popup signals. This allows you to handle events when the ColorPicker is shown or hidden.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---

## Theme Property Descriptions

[Texture2D](class_texture2d.md#class-texture2d) **bg**

The background of the color preview rect on the button.
