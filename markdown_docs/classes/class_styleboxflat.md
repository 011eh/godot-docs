# StyleBoxFlat

**Inherits:** [StyleBox](class_stylebox.md#class-stylebox) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A customizable [StyleBox](class_stylebox.md#class-stylebox) that doesn't use a texture.

## Description

By configuring various properties of this style box, you can achieve many common looks without the need of a texture. This includes optionally rounded borders, antialiasing, shadows, and skew.

Setting corner radius to high values is allowed. As soon as corners overlap, the stylebox will switch to a relative system:

```text
height = 30
corner_radius_top_left = 50
corner_radius_bottom_left = 100
```

The relative system now would take the 1:2 ratio of the two left corners to calculate the actual corner width. Both corners added will **never** be more than the height. Result:

```text
corner_radius_top_left: 10
corner_radius_bottom_left: 20
```

## Properties

| [bool](class_bool.md#class-bool)          | anti_aliasing                           | `true`                    |
|-------------------------------------------|---------------------------------------------------------------------------------------|---------------------------|
| [float](class_float.md#class-float)       | anti_aliasing_size                 | `1.0`                     |
| [Color](class_color.md#class-color)       | bg_color                                     | `Color(0.6, 0.6, 0.6, 1)` |
| [bool](class_bool.md#class-bool)          | border_blend                             | `false`                   |
| [Color](class_color.md#class-color)       | border_color                             | `Color(0.8, 0.8, 0.8, 1)` |
| [int](class_int.md#class-int)             | border_width_bottom               | `0`                       |
| [int](class_int.md#class-int)             | border_width_left                   | `0`                       |
| [int](class_int.md#class-int)             | border_width_right                 | `0`                       |
| [int](class_int.md#class-int)             | border_width_top                     | `0`                       |
| [int](class_int.md#class-int)             | corner_detail                           | `8`                       |
| [int](class_int.md#class-int)             | corner_radius_bottom_left   | `0`                       |
| [int](class_int.md#class-int)             | corner_radius_bottom_right | `0`                       |
| [int](class_int.md#class-int)             | corner_radius_top_left         | `0`                       |
| [int](class_int.md#class-int)             | corner_radius_top_right       | `0`                       |
| [bool](class_bool.md#class-bool)          | draw_center                               | `true`                    |
| [float](class_float.md#class-float)       | expand_margin_bottom             | `0.0`                     |
| [float](class_float.md#class-float)       | expand_margin_left                 | `0.0`                     |
| [float](class_float.md#class-float)       | expand_margin_right               | `0.0`                     |
| [float](class_float.md#class-float)       | expand_margin_top                   | `0.0`                     |
| [Color](class_color.md#class-color)       | shadow_color                             | `Color(0, 0, 0, 0.6)`     |
| [Vector2](class_vector2.md#class-vector2) | shadow_offset                           | `Vector2(0, 0)`           |
| [int](class_int.md#class-int)             | shadow_size                               | `0`                       |
| [Vector2](class_vector2.md#class-vector2) | skew                                             | `Vector2(0, 0)`           |

## Methods

| [int](class_int.md#class-int)       | get_border_width(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                              |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)       | get_border_width_min()                                                                                                 |
| [int](class_int.md#class-int)       | get_corner_radius(corner: [Corner](class_@globalscope.md#enum-globalscope-corner))                                        |
| [float](class_float.md#class-float) | get_expand_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                            |
|                                     | set_border_width(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))        |
|                                     | set_border_width_all(width: [int](class_int.md#class-int))                                                             |
|                                     | set_corner_radius(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int)) |
|                                     | set_corner_radius_all(radius: [int](class_int.md#class-int))                                                          |
|                                     | set_expand_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float)) |
|                                     | set_expand_margin_all(size: [float](class_float.md#class-float))                                                      |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **anti_aliasing** = `true`

-  **set_anti_aliased**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_anti_aliased**()

Antialiasing draws a small ring around the edges, which fades to transparency. As a result, edges look much smoother. This is only noticeable when using rounded corners or skew.

**Note:** When using beveled corners with 45-degree angles (corner_detail = 1), it is recommended to set anti_aliasing to `false` to ensure crisp visuals and avoid possible visual glitches.

---

[float](class_float.md#class-float) **anti_aliasing_size** = `1.0`

-  **set_aa_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_aa_size**()

This changes the size of the antialiasing effect. `1.0` is recommended for an optimal result at 100% scale, identical to how rounded rectangles are rendered in web browsers and most vector drawing software.

**Note:** Higher values may produce a blur effect but can also create undesired artifacts on small boxes with large-radius corners.

---

[Color](class_color.md#class-color) **bg_color** = `Color(0.6, 0.6, 0.6, 1)`

-  **set_bg_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_bg_color**()

The background color of the stylebox.

---

[bool](class_bool.md#class-bool) **border_blend** = `false`

-  **set_border_blend**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_border_blend**()

If `true`, the border will fade into the background color.

---

[Color](class_color.md#class-color) **border_color** = `Color(0.8, 0.8, 0.8, 1)`

-  **set_border_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_border_color**()

Sets the color of the border.

---

[int](class_int.md#class-int) **border_width_bottom** = `0`

-  **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Border width for the bottom border.

---

[int](class_int.md#class-int) **border_width_left** = `0`

-  **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Border width for the left border.

---

[int](class_int.md#class-int) **border_width_right** = `0`

-  **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Border width for the right border.

---

[int](class_int.md#class-int) **border_width_top** = `0`

-  **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Border width for the top border.

---

[int](class_int.md#class-int) **corner_detail** = `8`

-  **set_corner_detail**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_detail**()

This sets the number of vertices used for each corner. Higher values result in rounder corners but take more processing power to compute. When choosing a value, you should take the corner radius (set_corner_radius_all()) into account.

For corner radii less than 10, `4` or `5` should be enough. For corner radii less than 30, values between `8` and `12` should be enough.

A corner detail of `1` will result in chamfered corners instead of rounded corners, which is useful for some artistic effects.

---

[int](class_int.md#class-int) **corner_radius_bottom_left** = `0`

-  **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) 

The bottom-left corner's radius. If `0`, the corner is not rounded.

---

[int](class_int.md#class-int) **corner_radius_bottom_right** = `0`

-  **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) 

The bottom-right corner's radius. If `0`, the corner is not rounded.

---

[int](class_int.md#class-int) **corner_radius_top_left** = `0`

-  **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) 

The top-left corner's radius. If `0`, the corner is not rounded.

---

[int](class_int.md#class-int) **corner_radius_top_right** = `0`

-  **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner)) 

The top-right corner's radius. If `0`, the corner is not rounded.

---

[bool](class_bool.md#class-bool) **draw_center** = `true`

-  **set_draw_center**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_center_enabled**()

Toggles drawing of the inner part of the stylebox.

---

[float](class_float.md#class-float) **expand_margin_bottom** = `0.0`

-  **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Expands the stylebox outside of the control rect on the bottom edge. Useful in combination with border_width_bottom to draw a border outside the control rect.

**Note:** Unlike [StyleBox.content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom), expand_margin_bottom does *not* affect the size of the clickable area for [Control](class_control.md#class-control)s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---

[float](class_float.md#class-float) **expand_margin_left** = `0.0`

-  **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Expands the stylebox outside of the control rect on the left edge. Useful in combination with border_width_left to draw a border outside the control rect.

**Note:** Unlike [StyleBox.content_margin_left](class_stylebox.md#class-stylebox-property-content-margin-left), expand_margin_left does *not* affect the size of the clickable area for [Control](class_control.md#class-control)s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---

[float](class_float.md#class-float) **expand_margin_right** = `0.0`

-  **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Expands the stylebox outside of the control rect on the right edge. Useful in combination with border_width_right to draw a border outside the control rect.

**Note:** Unlike [StyleBox.content_margin_right](class_stylebox.md#class-stylebox-property-content-margin-right), expand_margin_right does *not* affect the size of the clickable area for [Control](class_control.md#class-control)s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---

[float](class_float.md#class-float) **expand_margin_top** = `0.0`

-  **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Expands the stylebox outside of the control rect on the top edge. Useful in combination with border_width_top to draw a border outside the control rect.

**Note:** Unlike [StyleBox.content_margin_top](class_stylebox.md#class-stylebox-property-content-margin-top), expand_margin_top does *not* affect the size of the clickable area for [Control](class_control.md#class-control)s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---

[Color](class_color.md#class-color) **shadow_color** = `Color(0, 0, 0, 0.6)`

-  **set_shadow_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_shadow_color**()

The color of the shadow. This has no effect if shadow_size is lower than 1.

---

[Vector2](class_vector2.md#class-vector2) **shadow_offset** = `Vector2(0, 0)`

-  **set_shadow_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_shadow_offset**()

The shadow offset in pixels. Adjusts the position of the shadow relatively to the stylebox.

---

[int](class_int.md#class-int) **shadow_size** = `0`

-  **set_shadow_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_shadow_size**()

The shadow size in pixels.

---

[Vector2](class_vector2.md#class-vector2) **skew** = `Vector2(0, 0)`

-  **set_skew**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_skew**()

If set to a non-zero value on either axis, skew distorts the StyleBox horizontally and/or vertically. This can be used for "futuristic"-style UIs. Positive values skew the StyleBox towards the right (X axis) and upwards (Y axis), while negative values skew the StyleBox towards the left (X axis) and downwards (Y axis).

**Note:** To ensure text does not touch the StyleBox's edges, consider increasing the [StyleBox](class_stylebox.md#class-stylebox)'s content margin (see [StyleBox.content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom)). It is preferable to increase the content margin instead of the expand margin (see expand_margin_bottom), as increasing the expand margin does not increase the size of the clickable area for [Control](class_control.md#class-control)s.

---

## Method Descriptions

[int](class_int.md#class-int) **get_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the specified [Side](class_@globalscope.md#enum-globalscope-side)'s border width.

---

[int](class_int.md#class-int) **get_border_width_min**()

Returns the smallest border width out of all four borders.

---

[int](class_int.md#class-int) **get_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner))

Returns the given `corner`'s radius.

---

[float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the size of the specified [Side](class_@globalscope.md#enum-globalscope-side)'s expand margin.

---

 **set_border_width**(margin: [Side](class_@globalscope.md#enum-globalscope-side), width: [int](class_int.md#class-int))

Sets the specified [Side](class_@globalscope.md#enum-globalscope-side)'s border width to `width` pixels.

---

 **set_border_width_all**(width: [int](class_int.md#class-int))

Sets the border width to `width` pixels for all sides.

---

 **set_corner_radius**(corner: [Corner](class_@globalscope.md#enum-globalscope-corner), radius: [int](class_int.md#class-int))

Sets the corner radius to `radius` pixels for the given `corner`.

---

 **set_corner_radius_all**(radius: [int](class_int.md#class-int))

Sets the corner radius to `radius` pixels for all corners.

---

 **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))

Sets the expand margin to `size` pixels for the specified [Side](class_@globalscope.md#enum-globalscope-side).

---

 **set_expand_margin_all**(size: [float](class_float.md#class-float))

Sets the expand margin to `size` pixels for all sides.
