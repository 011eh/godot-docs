# InputEventJoypadButton

**Inherits:** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a gamepad button being pressed or released.

## Description

Input event type for gamepad buttons. For gamepad analog sticks and joysticks, see [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion).

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

## Properties

| [JoyButton](class_@globalscope.md#enum-globalscope-joybutton)   | button_index   | `0`     |
|-----------------------------------------------------------------|-----------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)                                | pressed             | `false` |
| [float](class_float.md#class-float)                             | pressure           | `0.0`   |

---

## Property Descriptions

[JoyButton](class_@globalscope.md#enum-globalscope-joybutton) **button_index** = `0`

-  **set_button_index**(value: [JoyButton](class_@globalscope.md#enum-globalscope-joybutton))
- [JoyButton](class_@globalscope.md#enum-globalscope-joybutton) **get_button_index**()

Button identifier. One of the [JoyButton](class_@globalscope.md#enum-globalscope-joybutton) button constants.

---

[bool](class_bool.md#class-bool) **pressed** = `false`

-  **set_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pressed**()

If `true`, the button's state is pressed. If `false`, the button's state is released.

---

[float](class_float.md#class-float) **pressure** = `0.0`

-  **set_pressure**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pressure**()

**Deprecated:** This property is never set by the engine and is always `0`.
