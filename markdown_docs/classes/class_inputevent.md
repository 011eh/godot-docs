# InputEvent

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [InputEventAction](class_inputeventaction.md#class-inputeventaction), [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow), [InputEventJoypadButton](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton), [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion), [InputEventMIDI](class_inputeventmidi.md#class-inputeventmidi), [InputEventShortcut](class_inputeventshortcut.md#class-inputeventshortcut)

Abstract base class for input events.

## Description

Abstract base class of all types of input events. See [Node._input()](class_node.md#class-node-private-method-input).

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)
- [Viewport and canvas transforms](../tutorials/2d/2d_transforms.md)
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

## Properties

| [int](class_int.md#class-int)   | device   | `0`   |
|---------------------------------|-----------------------------------------------|-------|

## Methods

| [bool](class_bool.md#class-bool)       | accumulate(with_event: InputEvent)                                                                                                                                           |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string) | as_text()                                                                                                                                                                                            |
| [float](class_float.md#class-float)    | get_action_strength(action: [StringName](class_stringname.md#class-stringname), exact_match: [bool](class_bool.md#class-bool) = false)                                                   |
| [bool](class_bool.md#class-bool)       | is_action(action: [StringName](class_stringname.md#class-stringname), exact_match: [bool](class_bool.md#class-bool) = false)                                                                       |
| [bool](class_bool.md#class-bool)       | is_action_pressed(action: [StringName](class_stringname.md#class-stringname), allow_echo: [bool](class_bool.md#class-bool) = false, exact_match: [bool](class_bool.md#class-bool) = false) |
| [bool](class_bool.md#class-bool)       | is_action_released(action: [StringName](class_stringname.md#class-stringname), exact_match: [bool](class_bool.md#class-bool) = false)                                                     |
| [bool](class_bool.md#class-bool)       | is_action_type()                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)       | is_canceled()                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)       | is_echo()                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)       | is_match(event: InputEvent, exact_match: [bool](class_bool.md#class-bool) = true)                                                                                              |
| [bool](class_bool.md#class-bool)       | is_pressed()                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)       | is_released()                                                                                                                                                                                    |
| InputEvent        | xformed_by(xform: [Transform2D](class_transform2d.md#class-transform2d), local_ofs: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))                                                    |

---

## Constants

**DEVICE_ID_EMULATION** = `-1`

Device ID used for emulated mouse input from a touchscreen, or for emulated touch input from a mouse. This can be used to distinguish emulated mouse input from physical mouse input, or emulated touch input from physical touch input.

**DEVICE_ID_KEYBOARD** = `16`

Device ID used for input from a keyboard. This can be used to distinguish keyboard input events from joypad input events.

**DEVICE_ID_MOUSE** = `32`

Device ID used for input from a mouse. This can be used to distinguish mouse input events from joypad input events.

---

## Property Descriptions

[int](class_int.md#class-int) **device** = `0`

-  **set_device**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_device**()

The event's device ID.

**Note:** device can be negative for special use cases that don't refer to devices physically present on the system. See DEVICE_ID_EMULATION.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **accumulate**(with_event: InputEvent)

Returns `true` if the given input event and this input event can be added together (only for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class-inputeventmousemotion)).

The given input event's position, global position and speed will be copied. The resulting `relative` is a sum of both events. Both events' modifiers have to be identical.

---

[String](class_string.md#class-string) **as_text**()

Returns a [String](class_string.md#class-string) representation of the event.

---

[float](class_float.md#class-float) **get_action_strength**(action: [StringName](class_stringname.md#class-stringname), exact_match: [bool](class_bool.md#class-bool) = false)

Returns a value between 0.0 and 1.0 depending on the given actions' state. Useful for getting the value of events of type [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion).

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class-inputeventkey) and [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion) events.

---

[bool](class_bool.md#class-bool) **is_action**(action: [StringName](class_stringname.md#class-stringname), exact_match: [bool](class_bool.md#class-bool) = false)

Returns `true` if this input event matches a pre-defined action of any type.

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class-inputeventkey) and [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion) events.

---

[bool](class_bool.md#class-bool) **is_action_pressed**(action: [StringName](class_stringname.md#class-stringname), allow_echo: [bool](class_bool.md#class-bool) = false, exact_match: [bool](class_bool.md#class-bool) = false)

Returns `true` if the given action matches this event and is being pressed (and is not an echo event for [InputEventKey](class_inputeventkey.md#class-inputeventkey) events, unless `allow_echo` is `true`). Not relevant for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class-inputeventmousemotion) or [InputEventScreenDrag](class_inputeventscreendrag.md#class-inputeventscreendrag).

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class-inputeventkey) and [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion) events.

**Note:** Due to keyboard ghosting, is_action_pressed() may return `false` even if one of the action's keys is pressed. See [Input examples](../tutorials/inputs/input_examples.html#keyboard-events) in the documentation for more information.

---

[bool](class_bool.md#class-bool) **is_action_released**(action: [StringName](class_stringname.md#class-stringname), exact_match: [bool](class_bool.md#class-bool) = false)

Returns `true` if the given action matches this event and is released (i.e. not pressed). Not relevant for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class-inputeventmousemotion) or [InputEventScreenDrag](class_inputeventscreendrag.md#class-inputeventscreendrag).

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class-inputeventkey) and [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion) events.

---

[bool](class_bool.md#class-bool) **is_action_type**()

Returns `true` if this input event's type is one that can be assigned to an input action: [InputEventKey](class_inputeventkey.md#class-inputeventkey), [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton), [InputEventJoypadButton](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton), [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion), [InputEventAction](class_inputeventaction.md#class-inputeventaction). Returns `false` for all other input event types.

---

[bool](class_bool.md#class-bool) **is_canceled**()

Returns `true` if this input event has been canceled.

---

[bool](class_bool.md#class-bool) **is_echo**()

Returns `true` if this input event is an echo event (only for events of type [InputEventKey](class_inputeventkey.md#class-inputeventkey)). An echo event is a repeated key event sent when the user is holding down the key. Any other event type returns `false`.

**Note:** The rate at which echo events are sent is typically around 20 events per second (after holding down the key for roughly half a second). However, the key repeat delay/speed can be changed by the user or disabled entirely in the operating system settings. To ensure your project works correctly on all configurations, do not assume the user has a specific key repeat configuration in your project's behavior.

---

[bool](class_bool.md#class-bool) **is_match**(event: InputEvent, exact_match: [bool](class_bool.md#class-bool) = true)

Returns `true` if the specified `event` matches this event. Only valid for action events, which include key ([InputEventKey](class_inputeventkey.md#class-inputeventkey)), button ([InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton) or [InputEventJoypadButton](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton)), axis [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion), and action ([InputEventAction](class_inputeventaction.md#class-inputeventaction)) events.

If `exact_match` is `false`, the check ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class-inputeventkey) and [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion) events.

**Note:** This method only considers the event configuration (such as the keyboard key or the joypad axis), not state information like is_pressed(), is_released(), is_echo(), or is_canceled().

---

[bool](class_bool.md#class-bool) **is_pressed**()

Returns `true` if this input event is pressed. Not relevant for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class-inputeventmousemotion) or [InputEventScreenDrag](class_inputeventscreendrag.md#class-inputeventscreendrag).

**Note:** Due to keyboard ghosting, is_pressed() may return `false` even if one of the action's keys is pressed. See [Input examples](../tutorials/inputs/input_examples.html#keyboard-events) in the documentation for more information.

---

[bool](class_bool.md#class-bool) **is_released**()

Returns `true` if this input event is released. Not relevant for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class-inputeventmousemotion) or [InputEventScreenDrag](class_inputeventscreendrag.md#class-inputeventscreendrag).

---

InputEvent **xformed_by**(xform: [Transform2D](class_transform2d.md#class-transform2d), local_ofs: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Returns a copy of the given input event which has been offset by `local_ofs` and transformed by `xform`. Relevant for events of type [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton), [InputEventMouseMotion](class_inputeventmousemotion.md#class-inputeventmousemotion), [InputEventScreenTouch](class_inputeventscreentouch.md#class-inputeventscreentouch), [InputEventScreenDrag](class_inputeventscreendrag.md#class-inputeventscreendrag), [InputEventMagnifyGesture](class_inputeventmagnifygesture.md#class-inputeventmagnifygesture) and [InputEventPanGesture](class_inputeventpangesture.md#class-inputeventpangesture).
