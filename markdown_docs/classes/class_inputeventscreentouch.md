# InputEventScreenTouch

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a screen touch event.

## Description

Stores information about multi-touch press/release input events. Supports touch press, touch release and index for multi-touch count and order.

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

## Properties

| [bool](class_bool.md#class-bool)          | canceled     | `false`         |
|-------------------------------------------|----------------------------------------------------------------|-----------------|
| [bool](class_bool.md#class-bool)          | double_tap | `false`         |
| [int](class_int.md#class-int)             | index           | `0`             |
| [Vector2](class_vector2.md#class-vector2) | position     | `Vector2(0, 0)` |
| [bool](class_bool.md#class-bool)          | pressed       | `false`         |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **canceled** = `false`

-  **set_canceled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_canceled**()

If `true`, the touch event has been canceled.

---

[bool](class_bool.md#class-bool) **double_tap** = `false`

-  **set_double_tap**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_double_tap**()

If `true`, the touch's state is a double tap.

---

[int](class_int.md#class-int) **index** = `0`

-  **set_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_index**()

The touch index in the case of a multi-touch event. One index = one finger.

---

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)`

-  **set_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position**()

The touch position in the viewport the node is in, using the coordinate system of this viewport.

---

[bool](class_bool.md#class-bool) **pressed** = `false`

-  **set_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pressed**()

If `true`, the touch's state is pressed. If `false`, the touch's state is released.
