# InputEventJoypadMotion

**Inherits:** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents axis motions (such as joystick or analog triggers) from a gamepad.

## Description

Stores information about joystick motions. One **InputEventJoypadMotion** represents one axis at a time. For gamepad buttons, see [InputEventJoypadButton](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton).

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

## Properties

| [JoyAxis](class_@globalscope.md#enum-globalscope-joyaxis)   | axis             | `0`   |
|-------------------------------------------------------------|-----------------------------------------------------------------|-------|
| [float](class_float.md#class-float)                         | axis_value | `0.0` |

---

## Property Descriptions

[JoyAxis](class_@globalscope.md#enum-globalscope-joyaxis) **axis** = `0`

-  **set_axis**(value: [JoyAxis](class_@globalscope.md#enum-globalscope-joyaxis))
- [JoyAxis](class_@globalscope.md#enum-globalscope-joyaxis) **get_axis**()

Axis identifier.

---

[float](class_float.md#class-float) **axis_value** = `0.0`

-  **set_axis_value**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_axis_value**()

Current position of the joystick on the given axis. The value ranges from `-1.0` to `1.0`. A value of `0` means the axis is in its resting position.
