# InputEventMouseMotion

**Inherits:** [InputEventMouse](class_inputeventmouse.md#class-inputeventmouse) **<** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a mouse or a pen movement.

## Description

Stores information about a mouse or a pen motion. This includes relative position, absolute position, and velocity. See [Node._input()](class_node.md#class-node-private-method-input).

**Note:** By default, this event is only emitted once per frame rendered at most. If you need more precise input reporting, set [Input.use_accumulated_input](class_input.md#class-input-property-use-accumulated-input) to `false` to make events emitted as often as possible. If you use InputEventMouseMotion to draw lines, consider using [Geometry2D.bresenham_line()](class_geometry2d.md#class-geometry2d-method-bresenham-line) as well to avoid visible gaps in lines if the user is moving the mouse quickly.

**Note:** This event may be emitted even when the mouse hasn't moved, either by the operating system or by Godot itself. If you really need to know if the mouse has moved (e.g. to suppress displaying a tooltip), you should check that `relative.is_zero_approx()` is `false`.

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)
- [Mouse and input coordinates](../tutorials/inputs/mouse_and_input_coordinates.md)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

## Properties

| [bool](class_bool.md#class-bool)          | pen_inverted       | `false`         |
|-------------------------------------------|--------------------------------------------------------------------------|-----------------|
| [float](class_float.md#class-float)       | pressure               | `0.0`           |
| [Vector2](class_vector2.md#class-vector2) | relative               | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | screen_relative | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | screen_velocity | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | tilt                       | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | velocity               | `Vector2(0, 0)` |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **pen_inverted** = `false`

-  **set_pen_inverted**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_pen_inverted**()

Returns `true` when using the eraser end of a stylus pen.

**Note:** This property is implemented on Linux, macOS and Windows.

---

[float](class_float.md#class-float) **pressure** = `0.0`

-  **set_pressure**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pressure**()

Represents the pressure the user puts on the pen. Ranges from `0.0` to `1.0`.

---

[Vector2](class_vector2.md#class-vector2) **relative** = `Vector2(0, 0)`

-  **set_relative**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_relative**()

The mouse position relative to the previous position (position at the last frame).

**Note:** Since **InputEventMouseMotion** may only be emitted when the mouse moves, it is not possible to reliably detect when the mouse has stopped moving by checking this property. A separate, short timer may be necessary.

**Note:** relative is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means mouse sensitivity will appear different depending on resolution when using relative in a script that handles mouse aiming with the [Input.MOUSE_MODE_CAPTURED](class_input.md#class-input-constant-mouse-mode-captured) mouse mode. To avoid this, use screen_relative instead.

---

[Vector2](class_vector2.md#class-vector2) **screen_relative** = `Vector2(0, 0)`

-  **set_screen_relative**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_screen_relative**()

The unscaled mouse position relative to the previous position in the coordinate system of the screen (position at the last frame).

**Note:** Since **InputEventMouseMotion** may only be emitted when the mouse moves, it is not possible to reliably detect when the mouse has stopped moving by checking this property. A separate, short timer may be necessary.

**Note:** This coordinate is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()](class_inputevent.md#class-inputevent-method-xformed-by). This should be preferred over relative for mouse aiming when using the [Input.MOUSE_MODE_CAPTURED](class_input.md#class-input-constant-mouse-mode-captured) mouse mode, regardless of the project's stretch mode.

---

[Vector2](class_vector2.md#class-vector2) **screen_velocity** = `Vector2(0, 0)`

-  **set_screen_velocity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_screen_velocity**()

The unscaled mouse velocity in pixels per second in screen coordinates. This velocity is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()](class_inputevent.md#class-inputevent-method-xformed-by).

**Note:** In [Input.MOUSE_MODE_CAPTURED](class_input.md#class-input-constant-mouse-mode-captured) mode, screen_velocity returns `(0, 0)` because the mouse cursor is hidden and locked. Use screen_relative for mouse aiming using the [Input.MOUSE_MODE_CAPTURED](class_input.md#class-input-constant-mouse-mode-captured) mouse mode.

---

[Vector2](class_vector2.md#class-vector2) **tilt** = `Vector2(0, 0)`

-  **set_tilt**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_tilt**()

Represents the angles of tilt of the pen. Positive X-coordinate value indicates a tilt to the right. Positive Y-coordinate value indicates a tilt toward the user. Ranges from `-1.0` to `1.0` for both axes.

---

[Vector2](class_vector2.md#class-vector2) **velocity** = `Vector2(0, 0)`

-  **set_velocity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_velocity**()

The mouse velocity in pixels per second.

**Note:** velocity is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. That means mouse sensitivity may appear different depending on resolution.

**Note:** In [Input.MOUSE_MODE_CAPTURED](class_input.md#class-input-constant-mouse-mode-captured) mode, velocity returns `(0, 0)` because the mouse cursor is hidden and locked. Use screen_relative for mouse aiming using the [Input.MOUSE_MODE_CAPTURED](class_input.md#class-input-constant-mouse-mode-captured) mouse mode.
