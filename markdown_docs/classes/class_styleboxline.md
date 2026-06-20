# StyleBoxLine

**Inherits:** [StyleBox](class_stylebox.md#class-stylebox) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [StyleBox](class_stylebox.md#class-stylebox) that displays a single line of a given color and thickness.

## Description

A [StyleBox](class_stylebox.md#class-stylebox) that displays a single line of a given color and thickness. The line can be either horizontal or vertical. Useful for separators.

## Properties

| [Color](class_color.md#class-color)   | color           | `Color(0, 0, 0, 1)`   |
|---------------------------------------|-------------------------------------------------------|-----------------------|
| [float](class_float.md#class-float)   | grow_begin | `1.0`                 |
| [float](class_float.md#class-float)   | grow_end     | `1.0`                 |
| [int](class_int.md#class-int)         | thickness   | `1`                   |
| [bool](class_bool.md#class-bool)      | vertical     | `false`               |

---

## Property Descriptions

[Color](class_color.md#class-color) **color** = `Color(0, 0, 0, 1)`

-  **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The line's color.

---

[float](class_float.md#class-float) **grow_begin** = `1.0`

-  **set_grow_begin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_grow_begin**()

The number of pixels the line will extend before the **StyleBoxLine**'s bounds. If set to a negative value, the line will begin inside the **StyleBoxLine**'s bounds.

---

[float](class_float.md#class-float) **grow_end** = `1.0`

-  **set_grow_end**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_grow_end**()

The number of pixels the line will extend past the **StyleBoxLine**'s bounds. If set to a negative value, the line will end inside the **StyleBoxLine**'s bounds.

---

[int](class_int.md#class-int) **thickness** = `1`

-  **set_thickness**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_thickness**()

The line's thickness in pixels.

---

[bool](class_bool.md#class-bool) **vertical** = `false`

-  **set_vertical**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_vertical**()

If `true`, the line will be vertical. If `false`, the line will be horizontal.
