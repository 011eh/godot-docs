# Gradient

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A color transition.

## Description

This resource describes a color transition by defining a set of colored points and how to interpolate between them.

See also [Curve](class_curve.md#class-curve) which supports more complex easing methods, but does not support colors.

## Properties

| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)       | colors                                       | `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)`   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------|----------------------------------------------|
| ColorSpace                                    | interpolation_color_space | `0`                                          |
| InterpolationMode                      | interpolation_mode               | `0`                                          |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | offsets                                     | `PackedFloat32Array(0, 1)`                   |

## Methods

|                                     | add_point(offset: [float](class_float.md#class-float), color: [Color](class_color.md#class-color))   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [Color](class_color.md#class-color) | get_color(point: [int](class_int.md#class-int))                                                      |
| [float](class_float.md#class-float) | get_offset(point: [int](class_int.md#class-int))                                                    |
| [int](class_int.md#class-int)       | get_point_count()                                                                              |
|                                     | remove_point(point: [int](class_int.md#class-int))                                                |
|                                     | reverse()                                                                                              |
| [Color](class_color.md#class-color) | sample(offset: [float](class_float.md#class-float))                                                     |
|                                     | set_color(point: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))          |
|                                     | set_offset(point: [int](class_int.md#class-int), offset: [float](class_float.md#class-float))       |

---

## Enumerations

enum **InterpolationMode**:

InterpolationMode **GRADIENT_INTERPOLATE_LINEAR** = `0`

Linear interpolation.

InterpolationMode **GRADIENT_INTERPOLATE_CONSTANT** = `1`

Constant interpolation, color changes abruptly at each point and stays uniform between. This might cause visible aliasing when used for a gradient texture in some cases.

InterpolationMode **GRADIENT_INTERPOLATE_CUBIC** = `2`

Cubic interpolation.

---

enum **ColorSpace**:

ColorSpace **GRADIENT_COLOR_SPACE_SRGB** = `0`

sRGB color space.

ColorSpace **GRADIENT_COLOR_SPACE_LINEAR_SRGB** = `1`

Linear sRGB color space.

ColorSpace **GRADIENT_COLOR_SPACE_OKLAB** = `2`

[Oklab](https://bottosson.github.io/posts/oklab/) color space. This color space provides a smooth and uniform-looking transition between colors.

---

## Property Descriptions

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **colors** = `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)`

-  **set_colors**(value: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))
- [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_colors**()

Gradient's colors as a [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray).

**Note:** Setting this property updates all colors at once. To update any color individually use set_color().

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---

ColorSpace **interpolation_color_space** = `0`

-  **set_interpolation_color_space**(value: ColorSpace)
- ColorSpace **get_interpolation_color_space**()

The color space used to interpolate between points of the gradient. It does not affect the returned colors, which will always use nonlinear sRGB encoding.

**Note:** This setting has no effect when interpolation_mode is set to GRADIENT_INTERPOLATE_CONSTANT.

---

InterpolationMode **interpolation_mode** = `0`

-  **set_interpolation_mode**(value: InterpolationMode)
- InterpolationMode **get_interpolation_mode**()

The algorithm used to interpolate between points of the gradient.

---

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **offsets** = `PackedFloat32Array(0, 1)`

-  **set_offsets**(value: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))
- [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_offsets**()

Gradient's offsets as a [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array).

**Note:** Setting this property updates all offsets at once. To update any offset individually use set_offset().

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) for more details.

---

## Method Descriptions

 **add_point**(offset: [float](class_float.md#class-float), color: [Color](class_color.md#class-color))

Adds the specified color to the gradient, with the specified offset.

---

[Color](class_color.md#class-color) **get_color**(point: [int](class_int.md#class-int))

Returns the color of the gradient color at index `point`.

---

[float](class_float.md#class-float) **get_offset**(point: [int](class_int.md#class-int))

Returns the offset of the gradient color at index `point`.

---

[int](class_int.md#class-int) **get_point_count**()

Returns the number of colors in the gradient.

---

 **remove_point**(point: [int](class_int.md#class-int))

Removes the color at index `point`.

---

 **reverse**()

Reverses/mirrors the gradient.

**Note:** This method mirrors all points around the middle of the gradient, which may produce unexpected results when interpolation_mode is set to GRADIENT_INTERPOLATE_CONSTANT.

---

[Color](class_color.md#class-color) **sample**(offset: [float](class_float.md#class-float))

Returns the interpolated color specified by `offset`. `offset` should be between `0.0` and `1.0` (inclusive). Using a value lower than `0.0` will return the same color as `0.0`, and using a value higher than `1.0` will return the same color as `1.0`. If your input value is not within this range, consider using [@GlobalScope.remap()](class_@globalscope.md#class-globalscope-method-remap) on the input value with output values set to `0.0` and `1.0`.

---

 **set_color**(point: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the color of the gradient color at index `point`.

---

 **set_offset**(point: [int](class_int.md#class-int), offset: [float](class_float.md#class-float))

Sets the offset for the gradient color at index `point`.
