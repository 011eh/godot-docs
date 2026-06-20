# InputEventMouse

**Inherits:** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton), [InputEventMouseMotion](class_inputeventmousemotion.md#class-inputeventmousemotion)

Base input event type for mouse events.

## Description

Stores general information about mouse events.

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

## Properties

| [[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)]   | button_mask         | `0`                                                                                 |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                                 | device                                                             | `32` (overrides [InputEvent](class_inputevent.md#class-inputevent-property-device)) |
| [Vector2](class_vector2.md#class-vector2)                                     | global_position | `Vector2(0, 0)`                                                                     |
| [Vector2](class_vector2.md#class-vector2)                                     | position               | `Vector2(0, 0)`                                                                     |

---

## Property Descriptions

[[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] **button_mask** = `0`

-  **set_button_mask**(value: [[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)])
- [[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] **get_button_mask**()

The mouse button mask identifier, one of or a bitwise combination of the [MouseButton](class_@globalscope.md#enum-globalscope-mousebutton) button masks.

---

[Vector2](class_vector2.md#class-vector2) **global_position** = `Vector2(0, 0)`

-  **set_global_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_global_position**()

When received in [Node._input()](class_node.md#class-node-private-method-input) or [Node._unhandled_input()](class_node.md#class-node-private-method-unhandled-input), returns the mouse's position in the root [Viewport](class_viewport.md#class-viewport) using the coordinate system of the root [Viewport](class_viewport.md#class-viewport).

When received in [Control._gui_input()](class_control.md#class-control-private-method-gui-input), returns the mouse's position in the [CanvasLayer](class_canvaslayer.md#class-canvaslayer) that the [Control](class_control.md#class-control) is in using the coordinate system of the [CanvasLayer](class_canvaslayer.md#class-canvaslayer).

---

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)`

-  **set_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position**()

When received in [Node._input()](class_node.md#class-node-private-method-input) or [Node._unhandled_input()](class_node.md#class-node-private-method-unhandled-input), returns the mouse's position in the [Viewport](class_viewport.md#class-viewport) this [Node](class_node.md#class-node) is in using the coordinate system of this [Viewport](class_viewport.md#class-viewport).

When received in [Control._gui_input()](class_control.md#class-control-private-method-gui-input), returns the mouse's position in the [Control](class_control.md#class-control) using the local coordinate system of the [Control](class_control.md#class-control).
