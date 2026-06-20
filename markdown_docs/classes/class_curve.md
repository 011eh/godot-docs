# Curve

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A mathematical curve.

## Description

This resource describes a mathematical curve by defining a set of points and tangents at each point. By default, it ranges between `0` and `1` on the X and Y axes, but these ranges can be changed.

Please note that many resources and nodes assume they are given *unit curves*. A unit curve is a curve whose domain (the X axis) is between `0` and `1`. Some examples of unit curve usage are [CPUParticles2D.angle_curve](class_cpuparticles2d.md#class-cpuparticles2d-property-angle-curve) and [Line2D.width_curve](class_line2d.md#class-line2d-property-width-curve).

## Properties

| [int](class_int.md#class-int)             | bake_resolution                       | `100`           |
|-------------------------------------------|--------------------------------------------------------------------------------|-----------------|
| [float](class_float.md#class-float)       | max_domain                                 | `1.0`           |
| [float](class_float.md#class-float)       | max_value                                   | `1.0`           |
| [float](class_float.md#class-float)       | min_domain                                 | `0.0`           |
| [float](class_float.md#class-float)       | min_value                                   | `0.0`           |
| [int](class_int.md#class-int)             | point_count                               | `0`             |
| [int](class_int.md#class-int)             | point_{index}/left_mode         | `0`             |
| [float](class_float.md#class-float)       | point_{index}/left_tangent   | `0.0`           |
| [Vector2](class_vector2.md#class-vector2) | point_{index}/position           | `Vector2(0, 0)` |
| [int](class_int.md#class-int)             | point_{index}/right_mode       | `0`             |
| [float](class_float.md#class-float)       | point_{index}/right_tangent | `0.0`           |

## Methods

| [int](class_int.md#class-int)             | add_point(position: [Vector2](class_vector2.md#class-vector2), left_tangent: [float](class_float.md#class-float) = 0, right_tangent: [float](class_float.md#class-float) = 0, left_mode: TangentMode = 0, right_mode: TangentMode = 0)   |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           | bake()                                                                                                                                                                                                                                                                                              |
|                                           | clean_dupes()                                                                                                                                                                                                                                                                                |
|                                           | clear_points()                                                                                                                                                                                                                                                                              |
| [float](class_float.md#class-float)       | get_domain_range()                                                                                                                                                                                                                                                                      |
| TangentMode    | get_point_left_mode(index: [int](class_int.md#class-int))                                                                                                                                                                                                                            |
| [float](class_float.md#class-float)       | get_point_left_tangent(index: [int](class_int.md#class-int))                                                                                                                                                                                                                      |
| [Vector2](class_vector2.md#class-vector2) | get_point_position(index: [int](class_int.md#class-int))                                                                                                                                                                                                                              |
| TangentMode    | get_point_right_mode(index: [int](class_int.md#class-int))                                                                                                                                                                                                                          |
| [float](class_float.md#class-float)       | get_point_right_tangent(index: [int](class_int.md#class-int))                                                                                                                                                                                                                    |
| [float](class_float.md#class-float)       | get_value_range()                                                                                                                                                                                                                                                                        |
|                                           | remove_point(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                          |
| [float](class_float.md#class-float)       | sample(offset: [float](class_float.md#class-float))                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)       | sample_baked(offset: [float](class_float.md#class-float))                                                                                                                                                                                                                                   |
|                                           | set_point_left_mode(index: [int](class_int.md#class-int), mode: TangentMode)                                                                                                                                                                              |
|                                           | set_point_left_tangent(index: [int](class_int.md#class-int), tangent: [float](class_float.md#class-float))                                                                                                                                                                        |
| [int](class_int.md#class-int)             | set_point_offset(index: [int](class_int.md#class-int), offset: [float](class_float.md#class-float))                                                                                                                                                                                     |
|                                           | set_point_right_mode(index: [int](class_int.md#class-int), mode: TangentMode)                                                                                                                                                                            |
|                                           | set_point_right_tangent(index: [int](class_int.md#class-int), tangent: [float](class_float.md#class-float))                                                                                                                                                                      |
|                                           | set_point_value(index: [int](class_int.md#class-int), y: [float](class_float.md#class-float))                                                                                                                                                                                            |

---

## Signals

**domain_changed**()

Emitted when max_domain or min_domain is changed.

---

**range_changed**()

Emitted when max_value or min_value is changed.

---

## Enumerations

enum **TangentMode**:

TangentMode **TANGENT_FREE** = `0`

The tangent on this side of the point is user-defined.

TangentMode **TANGENT_LINEAR** = `1`

The curve calculates the tangent on this side of the point as the slope halfway towards the adjacent point.

TangentMode **TANGENT_MODE_COUNT** = `2`

The total number of available tangent modes.

---

## Property Descriptions

[int](class_int.md#class-int) **bake_resolution** = `100`

-  **set_bake_resolution**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bake_resolution**()

The number of points to include in the baked (i.e. cached) curve data.

---

[float](class_float.md#class-float) **max_domain** = `1.0`

-  **set_max_domain**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_domain**()

The maximum domain (x-coordinate) that points can have.

---

[float](class_float.md#class-float) **max_value** = `1.0`

-  **set_max_value**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_value**()

The maximum value (y-coordinate) that points can have. Tangents can cause higher values between points.

---

[float](class_float.md#class-float) **min_domain** = `0.0`

-  **set_min_domain**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_domain**()

The minimum domain (x-coordinate) that points can have.

---

[float](class_float.md#class-float) **min_value** = `0.0`

-  **set_min_value**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_value**()

The minimum value (y-coordinate) that points can have. Tangents can cause lower values between points.

---

[int](class_int.md#class-int) **point_count** = `0`

-  **set_point_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_point_count**()

The number of points describing the curve.

---

[int](class_int.md#class-int) **point_{index}/left_mode** = `0`

The left TangentMode for the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

---

[float](class_float.md#class-float) **point_{index}/left_tangent** = `0.0`

The left tangent angle (in degrees) for the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

---

[Vector2](class_vector2.md#class-vector2) **point_{index}/position** = `Vector2(0, 0)`

The position of the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

---

[int](class_int.md#class-int) **point_{index}/right_mode** = `0`

The right TangentMode for the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

---

[float](class_float.md#class-float) **point_{index}/right_tangent** = `0.0`

The right tangent angle (in degrees) for the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

---

## Method Descriptions

[int](class_int.md#class-int) **add_point**(position: [Vector2](class_vector2.md#class-vector2), left_tangent: [float](class_float.md#class-float) = 0, right_tangent: [float](class_float.md#class-float) = 0, left_mode: TangentMode = 0, right_mode: TangentMode = 0)

Adds a point to the curve. For each side, if the `*_mode` is TANGENT_LINEAR, the `*_tangent` angle (in degrees) uses the slope of the curve halfway to the adjacent point. Allows custom assignments to the `*_tangent` angle if `*_mode` is set to TANGENT_FREE.

---

 **bake**()

Recomputes the baked cache of points for the curve.

---

 **clean_dupes**()

Removes duplicate points, i.e. points that are less than 0.00001 units (engine epsilon value) away from their neighbor on the curve.

---

 **clear_points**()

Removes all points from the curve.

---

[float](class_float.md#class-float) **get_domain_range**()

Returns the difference between min_domain and max_domain.

---

TangentMode **get_point_left_mode**(index: [int](class_int.md#class-int))

Returns the left TangentMode for the point at `index`.

---

[float](class_float.md#class-float) **get_point_left_tangent**(index: [int](class_int.md#class-int))

Returns the left tangent angle (in degrees) for the point at `index`.

---

[Vector2](class_vector2.md#class-vector2) **get_point_position**(index: [int](class_int.md#class-int))

Returns the curve coordinates for the point at `index`.

---

TangentMode **get_point_right_mode**(index: [int](class_int.md#class-int))

Returns the right TangentMode for the point at `index`.

---

[float](class_float.md#class-float) **get_point_right_tangent**(index: [int](class_int.md#class-int))

Returns the right tangent angle (in degrees) for the point at `index`.

---

[float](class_float.md#class-float) **get_value_range**()

Returns the difference between min_value and max_value.

---

 **remove_point**(index: [int](class_int.md#class-int))

Removes the point at `index` from the curve.

---

[float](class_float.md#class-float) **sample**(offset: [float](class_float.md#class-float))

Returns the Y value for the point that would exist at the X position `offset` along the curve.

---

[float](class_float.md#class-float) **sample_baked**(offset: [float](class_float.md#class-float))

Returns the Y value for the point that would exist at the X position `offset` along the curve using the baked cache. Bakes the curve's points if not already baked.

---

 **set_point_left_mode**(index: [int](class_int.md#class-int), mode: TangentMode)

Sets the left TangentMode for the point at `index` to `mode`.

---

 **set_point_left_tangent**(index: [int](class_int.md#class-int), tangent: [float](class_float.md#class-float))

Sets the left tangent angle for the point at `index` to `tangent`.

---

[int](class_int.md#class-int) **set_point_offset**(index: [int](class_int.md#class-int), offset: [float](class_float.md#class-float))

Assigns the horizontal position `offset` to the point at `index`.

---

 **set_point_right_mode**(index: [int](class_int.md#class-int), mode: TangentMode)

Sets the right TangentMode for the point at `index` to `mode`.

---

 **set_point_right_tangent**(index: [int](class_int.md#class-int), tangent: [float](class_float.md#class-float))

Sets the right tangent angle for the point at `index` to `tangent`.

---

 **set_point_value**(index: [int](class_int.md#class-int), y: [float](class_float.md#class-float))

Assigns the vertical position `y` to the point at `index`.
