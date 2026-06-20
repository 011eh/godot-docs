# InputEventWithModifiers

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [InputEventGesture](class_inputeventgesture.md#class-inputeventgesture), [InputEventKey](class_inputeventkey.md#class-inputeventkey), [InputEventMouse](class_inputeventmouse.md#class-inputeventmouse)

Abstract base class for input events affected by modifier keys like `Shift` and `Alt`.

## Description

Stores information about mouse, keyboard, and touch gesture input events. This includes information about which modifier keys are pressed, such as `Shift` or `Alt`. See [Node._input()](class_node.md#class-node-private-method-input).

**Note:** Modifier keys are considered modifiers only when used in combination with another key. As a result, their corresponding member variables, such as ctrl_pressed, will return `false` if the key is pressed on its own.

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

## Properties

| [bool](class_bool.md#class-bool)   | alt_pressed                                   | `false`                                                                             |
|------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)   | command_or_control_autoremap | `false`                                                                             |
| [bool](class_bool.md#class-bool)   | ctrl_pressed                                 | `false`                                                                             |
| [int](class_int.md#class-int)      | device                                                                                               | `16` (overrides [InputEvent](class_inputevent.md#class-inputevent-property-device)) |
| [bool](class_bool.md#class-bool)   | meta_pressed                                 | `false`                                                                             |
| [bool](class_bool.md#class-bool)   | shift_pressed                               | `false`                                                                             |

## Methods

| [[KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)]   | get_modifiers_mask()                       |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                              | is_command_or_control_pressed() |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **alt_pressed** = `false`

-  **set_alt_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_alt_pressed**()

State of the `Alt` modifier.

---

[bool](class_bool.md#class-bool) **command_or_control_autoremap** = `false`

-  **set_command_or_control_autoremap**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_command_or_control_autoremap**()

Automatically use `Meta` (`Cmd`) on macOS and `Ctrl` on other platforms. If `true`, ctrl_pressed and meta_pressed cannot be set.

---

[bool](class_bool.md#class-bool) **ctrl_pressed** = `false`

-  **set_ctrl_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ctrl_pressed**()

State of the `Ctrl` modifier.

---

[bool](class_bool.md#class-bool) **meta_pressed** = `false`

-  **set_meta_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_meta_pressed**()

State of the `Meta` modifier. On Windows and Linux, this represents the Windows key (sometimes called "meta" or "super" on Linux). On macOS, this represents the Command key.

---

[bool](class_bool.md#class-bool) **shift_pressed** = `false`

-  **set_shift_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shift_pressed**()

State of the `Shift` modifier.

---

## Method Descriptions

[[KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)] **get_modifiers_mask**()

Returns the keycode combination of modifier keys.

---

[bool](class_bool.md#class-bool) **is_command_or_control_pressed**()

On macOS, returns `true` if `Meta` (`Cmd`) is pressed.

On other platforms, returns `true` if `Ctrl` is pressed.
