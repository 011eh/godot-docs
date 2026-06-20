# Line2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A 2D polyline that can optionally be textured.

## Description

This node draws a 2D polyline, i.e. a shape consisting of several points connected by segments. **Line2D** is not a mathematical polyline, i.e. the segments are not infinitely thin. It is intended for rendering and it can be colored and optionally textured.

**Warning:** Certain configurations may be impossible to draw nicely, such as very sharp angles. In these situations, the node uses fallback drawing logic to look decent.

**Note:** **Line2D** is drawn using a 2D mesh.

## Tutorials

- [Matrix Transform Demo](https://godotengine.org/asset-library/asset/2787)
- [2.5D Game Demo](https://godotengine.org/asset-library/asset/2783)

## Properties

| [bool](class_bool.md#class-bool)                                           | antialiased         | `false`                |
|----------------------------------------------------------------------------|-----------------------------------------------------------|------------------------|
| LineCapMode                                    | begin_cap_mode   | `0`                    |
| [bool](class_bool.md#class-bool)                                           | closed                   | `false`                |
| [Color](class_color.md#class-color)                                        | default_color     | `Color(1, 1, 1, 1)`    |
| LineCapMode                                    | end_cap_mode       | `0`                    |
| [Gradient](class_gradient.md#class-gradient)                               | gradient               |                        |
| LineJointMode                                | joint_mode           | `0`                    |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | points                   | `PackedVector2Array()` |
| [int](class_int.md#class-int)                                              | round_precision | `8`                    |
| [float](class_float.md#class-float)                                        | sharp_limit         | `2.0`                  |
| [Texture2D](class_texture2d.md#class-texture2d)                            | texture                 |                        |
| LineTextureMode                            | texture_mode       | `0`                    |
| [float](class_float.md#class-float)                                        | width                     | `10.0`                 |
| [Curve](class_curve.md#class-curve)                                        | width_curve         |                        |

## Methods

|                                           | add_point(position: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int) = -1)              |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           | clear_points()                                                                                                      |
| [int](class_int.md#class-int)             | get_point_count()                                                                                                |
| [Vector2](class_vector2.md#class-vector2) | get_point_position(index: [int](class_int.md#class-int))                                                      |
|                                           | remove_point(index: [int](class_int.md#class-int))                                                                  |
|                                           | set_point_position(index: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2)) |

---

## Enumerations

enum **LineJointMode**:

LineJointMode **LINE_JOINT_SHARP** = `0`

Makes the polyline's joints pointy, connecting the sides of the two segments by extending them until they intersect. If the rotation of a joint is too big (based on sharp_limit), the joint falls back to LINE_JOINT_BEVEL to prevent very long miters.

LineJointMode **LINE_JOINT_BEVEL** = `1`

Makes the polyline's joints bevelled/chamfered, connecting the sides of the two segments with a simple line.

LineJointMode **LINE_JOINT_ROUND** = `2`

Makes the polyline's joints rounded, connecting the sides of the two segments with an arc. The detail of this arc depends on round_precision.

---

enum **LineCapMode**:

LineCapMode **LINE_CAP_NONE** = `0`

Draws no line cap.

LineCapMode **LINE_CAP_BOX** = `1`

Draws the line cap as a box, slightly extending the first/last segment.

LineCapMode **LINE_CAP_ROUND** = `2`

Draws the line cap as a semicircle attached to the first/last segment.

---

enum **LineTextureMode**:

LineTextureMode **LINE_TEXTURE_NONE** = `0`

Takes the left pixels of the texture and renders them over the whole polyline.

LineTextureMode **LINE_TEXTURE_TILE** = `1`

Tiles the texture over the polyline. [CanvasItem.texture_repeat](class_canvasitem.md#class-canvasitem-property-texture-repeat) of the **Line2D** node must be [CanvasItem.TEXTURE_REPEAT_ENABLED](class_canvasitem.md#class-canvasitem-constant-texture-repeat-enabled) or [CanvasItem.TEXTURE_REPEAT_MIRROR](class_canvasitem.md#class-canvasitem-constant-texture-repeat-mirror) for it to work properly.

LineTextureMode **LINE_TEXTURE_STRETCH** = `2`

Stretches the texture across the polyline. [CanvasItem.texture_repeat](class_canvasitem.md#class-canvasitem-property-texture-repeat) of the **Line2D** node must be [CanvasItem.TEXTURE_REPEAT_DISABLED](class_canvasitem.md#class-canvasitem-constant-texture-repeat-disabled) for best results.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **antialiased** = `false`

-  **set_antialiased**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_antialiased**()

If `true`, the polyline's border will be anti-aliased.

**Note:** **Line2D** is not accelerated by batching when being anti-aliased.

---

LineCapMode **begin_cap_mode** = `0`

-  **set_begin_cap_mode**(value: LineCapMode)
- LineCapMode **get_begin_cap_mode**()

The style of the beginning of the polyline, if closed is `false`.

---

[bool](class_bool.md#class-bool) **closed** = `false`

-  **set_closed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_closed**()

If `true` and the polyline has more than 2 points, the last point and the first one will be connected by a segment.

**Note:** The shape of the closing segment is not guaranteed to be seamless if a width_curve is provided.

**Note:** The joint between the closing segment and the first segment is drawn first and it samples the gradient and the width_curve at the beginning. This is an implementation detail that might change in a future version.

---

[Color](class_color.md#class-color) **default_color** = `Color(1, 1, 1, 1)`

-  **set_default_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_default_color**()

The color of the polyline. Will not be used if a gradient is set.

---

LineCapMode **end_cap_mode** = `0`

-  **set_end_cap_mode**(value: LineCapMode)
- LineCapMode **get_end_cap_mode**()

The style of the end of the polyline, if closed is `false`.

---

[Gradient](class_gradient.md#class-gradient) **gradient**

-  **set_gradient**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_gradient**()

The gradient is drawn through the whole line from start to finish. The default_color will not be used if this property is set.

---

LineJointMode **joint_mode** = `0`

-  **set_joint_mode**(value: LineJointMode)
- LineJointMode **get_joint_mode**()

The style of the connections between segments of the polyline.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **points** = `PackedVector2Array()`

-  **set_points**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_points**()

The points of the polyline, interpreted in local 2D coordinates. Segments are drawn between the adjacent points in this array.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---

[int](class_int.md#class-int) **round_precision** = `8`

-  **set_round_precision**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_round_precision**()

The smoothness used for rounded joints and caps. Higher values result in smoother corners, but are more demanding to render and update.

---

[float](class_float.md#class-float) **sharp_limit** = `2.0`

-  **set_sharp_limit**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sharp_limit**()

Determines the miter limit of the polyline. Normally, when joint_mode is set to LINE_JOINT_SHARP, sharp angles fall back to using the logic of LINE_JOINT_BEVEL joints to prevent very long miters. Higher values of this property mean that the fallback to a bevel joint will happen at sharper angles.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The texture used for the polyline. Uses texture_mode for drawing style.

---

LineTextureMode **texture_mode** = `0`

-  **set_texture_mode**(value: LineTextureMode)
- LineTextureMode **get_texture_mode**()

The style to render the texture of the polyline.

---

[float](class_float.md#class-float) **width** = `10.0`

-  **set_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_width**()

The polyline's width.

---

[Curve](class_curve.md#class-curve) **width_curve**

-  **set_curve**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_curve**()

The polyline's width curve. The width of the polyline over its length will be equivalent to the value of the width curve over its domain. The width curve should be a unit [Curve](class_curve.md#class-curve).

---

## Method Descriptions

 **add_point**(position: [Vector2](class_vector2.md#class-vector2), index: [int](class_int.md#class-int) = -1)

Adds a point with the specified `position` relative to the polyline's own position. If no `index` is provided, the new point will be added to the end of the points array.

If `index` is given, the new point is inserted before the existing point identified by index `index`. The indices of the points after the new point get increased by 1. The provided `index` must not exceed the number of existing points in the polyline. See get_point_count().

---

 **clear_points**()

Removes all points from the polyline, making it empty.

---

[int](class_int.md#class-int) **get_point_count**()

Returns the number of points in the polyline.

---

[Vector2](class_vector2.md#class-vector2) **get_point_position**(index: [int](class_int.md#class-int))

Returns the position of the point at index `index`.

---

 **remove_point**(index: [int](class_int.md#class-int))

Removes the point at index `index` from the polyline.

---

 **set_point_position**(index: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2))

Overwrites the position of the point at the given `index` with the supplied `position`.
