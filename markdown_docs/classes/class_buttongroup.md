# ButtonGroup

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A group of buttons that doesn't allow more than one button to be pressed at a time.

## Description

A group of [BaseButton](class_basebutton.md#class-basebutton)-derived buttons. The buttons in a **ButtonGroup** are treated like radio buttons: No more than one button can be pressed at a time. Some types of buttons (such as [CheckBox](class_checkbox.md#class-checkbox)) may have a special appearance in this state.

Every member of a **ButtonGroup** should have [BaseButton.toggle_mode](class_basebutton.md#class-basebutton-property-toggle-mode) set to `true`.

## Properties

| [bool](class_bool.md#class-bool)   | allow_unpress   | `false`                                                                                          |
|------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)   | resource_local_to_scene                                      | `true` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

## Methods

| [Array](class_array.md#class-array)[[BaseButton](class_basebutton.md#class-basebutton)]   | get_buttons()               |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [BaseButton](class_basebutton.md#class-basebutton)                                        | get_pressed_button() |

---

## Signals

**pressed**(button: [BaseButton](class_basebutton.md#class-basebutton))

Emitted when one of the buttons of the group is pressed.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_unpress** = `false`

-  **set_allow_unpress**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_unpress**()

If `true`, it is possible to unpress all buttons in this **ButtonGroup**.

---

## Method Descriptions

[Array](class_array.md#class-array)[[BaseButton](class_basebutton.md#class-basebutton)] **get_buttons**()

Returns an [Array](class_array.md#class-array) of [Button](class_button.md#class-button)s who have this as their **ButtonGroup** (see [BaseButton.button_group](class_basebutton.md#class-basebutton-property-button-group)).

---

[BaseButton](class_basebutton.md#class-basebutton) **get_pressed_button**()

Returns the current pressed button.
