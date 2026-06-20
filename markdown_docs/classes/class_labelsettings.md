# LabelSettings

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides common settings to customize the text in a [Label](class_label.md#class-label).

## Description

**LabelSettings** is a resource that provides common settings to customize the text in a [Label](class_label.md#class-label). It will take priority over the properties defined in [Control.theme](class_control.md#class-control-property-theme). The resource can be shared between multiple labels and changed on the fly, so it's convenient and flexible way to setup text style.

## Properties

| [Font](class_font.md#class-font)          | font                                                             |                     |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------|
| [Color](class_color.md#class-color)       | font_color                                                 | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class-int)             | font_size                                                   | `16`                |
| [float](class_float.md#class-float)       | line_spacing                                             | `3.0`               |
| [Color](class_color.md#class-color)       | outline_color                                           | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class-int)             | outline_size                                             | `0`                 |
| [float](class_float.md#class-float)       | paragraph_spacing                                   | `0.0`               |
| [Color](class_color.md#class-color)       | shadow_color                                             | `Color(0, 0, 0, 0)` |
| [Vector2](class_vector2.md#class-vector2) | shadow_offset                                           | `Vector2(1, 1)`     |
| [int](class_int.md#class-int)             | shadow_size                                               | `1`                 |
| [int](class_int.md#class-int)             | stacked_outline_count                           | `0`                 |
| [Color](class_color.md#class-color)       | stacked_outline_{index}/color             | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int)             | stacked_outline_{index}/size               | `0`                 |
| [int](class_int.md#class-int)             | stacked_shadow_count                             | `0`                 |
| [Color](class_color.md#class-color)       | stacked_shadow_{index}/color               | `Color(0, 0, 0, 1)` |
| [Vector2](class_vector2.md#class-vector2) | stacked_shadow_{index}/offset             | `Vector2(1, 1)`     |
| [int](class_int.md#class-int)             | stacked_shadow_{index}/outline_size | `0`                 |

## Methods

|                                           | add_stacked_outline(index: [int](class_int.md#class-int) = -1)                                                           |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           | add_stacked_shadow(index: [int](class_int.md#class-int) = -1)                                                             |
| [Color](class_color.md#class-color)       | get_stacked_outline_color(index: [int](class_int.md#class-int))                                                    |
| [int](class_int.md#class-int)             | get_stacked_outline_size(index: [int](class_int.md#class-int))                                                      |
| [Color](class_color.md#class-color)       | get_stacked_shadow_color(index: [int](class_int.md#class-int))                                                      |
| [Vector2](class_vector2.md#class-vector2) | get_stacked_shadow_offset(index: [int](class_int.md#class-int))                                                    |
| [int](class_int.md#class-int)             | get_stacked_shadow_outline_size(index: [int](class_int.md#class-int))                                        |
|                                           | move_stacked_outline(from_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))             |
|                                           | move_stacked_shadow(from_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))               |
|                                           | remove_stacked_outline(index: [int](class_int.md#class-int))                                                          |
|                                           | remove_stacked_shadow(index: [int](class_int.md#class-int))                                                            |
|                                           | set_stacked_outline_color(index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))        |
|                                           | set_stacked_outline_size(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))                 |
|                                           | set_stacked_shadow_color(index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))          |
|                                           | set_stacked_shadow_offset(index: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2)) |
|                                           | set_stacked_shadow_outline_size(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))   |

---

## Property Descriptions

[Font](class_font.md#class-font) **font**

-  **set_font**(value: [Font](class_font.md#class-font))
- [Font](class_font.md#class-font) **get_font**()

[Font](class_font.md#class-font) used for the text.

---

[Color](class_color.md#class-color) **font_color** = `Color(1, 1, 1, 1)`

-  **set_font_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_font_color**()

Color of the text.

---

[int](class_int.md#class-int) **font_size** = `16`

-  **set_font_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_size**()

Size of the text.

---

[float](class_float.md#class-float) **line_spacing** = `3.0`

-  **set_line_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

[Color](class_color.md#class-color) **outline_color** = `Color(1, 1, 1, 1)`

-  **set_outline_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_outline_color**()

The color of the outline.

---

[int](class_int.md#class-int) **outline_size** = `0`

-  **set_outline_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_outline_size**()

Text outline size.

---

[float](class_float.md#class-float) **paragraph_spacing** = `0.0`

-  **set_paragraph_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_paragraph_spacing**()

Vertical space between paragraphs. Added on top of line_spacing.

---

[Color](class_color.md#class-color) **shadow_color** = `Color(0, 0, 0, 0)`

-  **set_shadow_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_shadow_color**()

Color of the shadow effect. If alpha is `0`, no shadow will be drawn.

---

[Vector2](class_vector2.md#class-vector2) **shadow_offset** = `Vector2(1, 1)`

-  **set_shadow_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_shadow_offset**()

Offset of the shadow effect, in pixels.

---

[int](class_int.md#class-int) **shadow_size** = `1`

-  **set_shadow_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_shadow_size**()

Size of the shadow effect.

---

[int](class_int.md#class-int) **stacked_outline_count** = `0`

-  **set_stacked_outline_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stacked_outline_count**()

The number of stacked outlines.

---

[Color](class_color.md#class-color) **stacked_outline_{index}/color** = `Color(0, 0, 0, 1)`

The color of the outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_outline_count - 1` range.

---

[int](class_int.md#class-int) **stacked_outline_{index}/size** = `0`

The size of the outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_outline_count - 1` range.

---

[int](class_int.md#class-int) **stacked_shadow_count** = `0`

-  **set_stacked_shadow_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stacked_shadow_count**()

The number of stacked shadows.

---

[Color](class_color.md#class-color) **stacked_shadow_{index}/color** = `Color(0, 0, 0, 1)`

The color of the shadow at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

---

[Vector2](class_vector2.md#class-vector2) **stacked_shadow_{index}/offset** = `Vector2(1, 1)`

The offset of the shadow at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

---

[int](class_int.md#class-int) **stacked_shadow_{index}/outline_size** = `0`

The size of the shadow outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

---

## Method Descriptions

 **add_stacked_outline**(index: [int](class_int.md#class-int) = -1)

Adds a new stacked outline to the label at the given `index`. If `index` is `-1`, the new stacked outline will be added at the end of the list.

---

 **add_stacked_shadow**(index: [int](class_int.md#class-int) = -1)

Adds a new stacked shadow to the label at the given `index`. If `index` is `-1`, the new stacked shadow will be added at the end of the list.

---

[Color](class_color.md#class-color) **get_stacked_outline_color**(index: [int](class_int.md#class-int))

Returns the color of the stacked outline at `index`.

---

[int](class_int.md#class-int) **get_stacked_outline_size**(index: [int](class_int.md#class-int))

Returns the size of the stacked outline at `index`.

---

[Color](class_color.md#class-color) **get_stacked_shadow_color**(index: [int](class_int.md#class-int))

Returns the color of the stacked shadow at `index`.

---

[Vector2](class_vector2.md#class-vector2) **get_stacked_shadow_offset**(index: [int](class_int.md#class-int))

Returns the offset of the stacked shadow at `index`.

---

[int](class_int.md#class-int) **get_stacked_shadow_outline_size**(index: [int](class_int.md#class-int))

Returns the outline size of the stacked shadow at `index`.

---

 **move_stacked_outline**(from_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))

Moves the stacked outline at index `from_index` to the given position `to_position` in the array.

---

 **move_stacked_shadow**(from_index: [int](class_int.md#class-int), to_position: [int](class_int.md#class-int))

Moves the stacked shadow at index `from_index` to the given position `to_position` in the array.

---

 **remove_stacked_outline**(index: [int](class_int.md#class-int))

Removes the stacked outline at index `index`.

---

 **remove_stacked_shadow**(index: [int](class_int.md#class-int))

Removes the stacked shadow at index `index`.

---

 **set_stacked_outline_color**(index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the color of the stacked outline identified by the given `index` to `color`.

---

 **set_stacked_outline_size**(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Sets the size of the stacked outline identified by the given `index` to `size`.

---

 **set_stacked_shadow_color**(index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the color of the stacked shadow identified by the given `index` to `color`.

---

 **set_stacked_shadow_offset**(index: [int](class_int.md#class-int), offset: [Vector2](class_vector2.md#class-vector2))

Sets the offset of the stacked shadow identified by the given `index` to `offset`.

---

 **set_stacked_shadow_outline_size**(index: [int](class_int.md#class-int), size: [int](class_int.md#class-int))

Sets the outline size of the stacked shadow identified by the given `index` to `size`.
