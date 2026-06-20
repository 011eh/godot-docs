# InputEventScreenDrag

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a screen drag event.

## Description

Stores information about screen drag events. See [Node._input()](class_node.md#class-node-private-method-input).

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

## Properties

| [int](class_int.md#class-int)             | index                     | `0`             |
|-------------------------------------------|-------------------------------------------------------------------------|-----------------|
| [bool](class_bool.md#class-bool)          | pen_inverted       | `false`         |
| [Vector2](class_vector2.md#class-vector2) | position               | `Vector2(0, 0)` |
| [float](class_float.md#class-float)       | pressure               | `0.0`           |
| [Vector2](class_vector2.md#class-vector2) | relative               | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | screen_relative | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | screen_velocity | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | tilt                       | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | velocity               | `Vector2(0, 0)` |

---

## Property Descriptions

[int](class_int.md#class-int) **index** = `0`

-  **set_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_index**()

The drag event index in the case of a multi-drag event.

---

[bool](class_bool.md#class-bool) **pen_inverted** = `false`

-  **set_pen_inverted**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_pen_inverted**()

Returns `true` when using the eraser end of a stylus pen.

---

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)`

-  **set_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position**()

The drag position in the viewport the node is in, using the coordinate system of this viewport.

---

[float](class_float.md#class-float) **pressure** = `0.0`

-  **set_pressure**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pressure**()

Represents the pressure the user puts on the pen. Ranges from `0.0` to `1.0`.

---

[Vector2](class_vector2.md#class-vector2) **relative** = `Vector2(0, 0)`

-  **set_relative**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_relative**()

The drag position relative to the previous position (position at the last frame).

**Note:** relative is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means touch sensitivity will appear different depending on resolution when using relative in a script that handles touch aiming. To avoid this, use screen_relative instead.

---

[Vector2](class_vector2.md#class-vector2) **screen_relative** = `Vector2(0, 0)`

-  **set_screen_relative**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_screen_relative**()

The unscaled drag position relative to the previous position in screen coordinates (position at the last frame). This position is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()](class_inputevent.md#class-inputevent-method-xformed-by). This should be preferred over relative for touch aiming regardless of the project's stretch mode.

---

[Vector2](class_vector2.md#class-vector2) **screen_velocity** = `Vector2(0, 0)`

-  **set_screen_velocity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_screen_velocity**()

The unscaled drag velocity in pixels per second in screen coordinates. This velocity is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()](class_inputevent.md#class-inputevent-method-xformed-by). This should be preferred over velocity for touch aiming regardless of the project's stretch mode.

---

[Vector2](class_vector2.md#class-vector2) **tilt** = `Vector2(0, 0)`

-  **set_tilt**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_tilt**()

Represents the angles of tilt of the pen. Positive X-coordinate value indicates a tilt to the right. Positive Y-coordinate value indicates a tilt toward the user. Ranges from `-1.0` to `1.0` for both axes.

---

[Vector2](class_vector2.md#class-vector2) **velocity** = `Vector2(0, 0)`

-  **set_velocity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_velocity**()

The drag velocity.

**Note:** velocity is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means touch sensitivity will appear different depending on resolution when using velocity in a script that handles touch aiming. To avoid this, use screen_velocity instead.
