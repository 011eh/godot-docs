# AnimationNodeBlendSpace2D

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A set of [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s placed on 2D coordinates, crossfading between the three adjacent ones. Used by [AnimationTree](class_animationtree.md#class-animationtree).

## Description

A resource used by [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

**AnimationNodeBlendSpace2D** represents a virtual 2D space on which [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s are placed. Outputs the linear blend of the three adjacent animations using a [Vector2](class_vector2.md#class-vector2) weight. Adjacent in this context means the three [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s making up the triangle that contains the current value.

You can add vertices to the blend space with add_blend_point() and automatically triangulate it by setting auto_triangles to `true`. Otherwise, use add_triangle() and remove_triangle() to triangulate the blend space by hand.

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [bool](class_bool.md#class-bool)                       | auto_triangles   | `true`              |
|--------------------------------------------------------|------------------------------------------------------------------------------|---------------------|
| BlendMode | blend_mode           | `0`                 |
| [float](class_float.md#class-float)                    | cyclic_length     | `0.0`               |
| [Vector2](class_vector2.md#class-vector2)              | max_space             | `Vector2(1, 1)`     |
| [Vector2](class_vector2.md#class-vector2)              | min_space             | `Vector2(-1, -1)`   |
| [Vector2](class_vector2.md#class-vector2)              | snap                       | `Vector2(0.1, 0.1)` |
| [bool](class_bool.md#class-bool)                       | sync                       |                     |
| SyncMode   | sync_mode             | `0`                 |
| [String](class_string.md#class-string)                 | x_label                 | `"x"`               |
| [String](class_string.md#class-string)                 | y_label                 | `"y"`               |

## Methods

|                                                                         | add_blend_point(node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), pos: [Vector2](class_vector2.md#class-vector2), at_index: [int](class_int.md#class-int) = -1, name: [StringName](class_stringname.md#class-stringname) = &"")   |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                         | add_triangle(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), z: [int](class_int.md#class-int), at_index: [int](class_int.md#class-int) = -1)                                                                                                  |
| [int](class_int.md#class-int)                                           | find_blend_point_by_name(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                    |
| [int](class_int.md#class-int)                                           | get_blend_point_count()                                                                                                                                                                                                                                  |
| [StringName](class_stringname.md#class-stringname)                      | get_blend_point_name(point: [int](class_int.md#class-int))                                                                                                                                                                                                |
| [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) | get_blend_point_node(point: [int](class_int.md#class-int))                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                               | get_blend_point_position(point: [int](class_int.md#class-int))                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                           | get_triangle_count()                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                           | get_triangle_point(triangle: [int](class_int.md#class-int), point: [int](class_int.md#class-int))                                                                                                                                                           |
|                                                                         | remove_blend_point(point: [int](class_int.md#class-int))                                                                                                                                                                                                    |
|                                                                         | remove_triangle(triangle: [int](class_int.md#class-int))                                                                                                                                                                                                       |
|                                                                         | reorder_blend_point(from_index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int))                                                                                                                                                    |
|                                                                         | set_blend_point_name(point: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname))                                                                                                                                      |
|                                                                         | set_blend_point_node(point: [int](class_int.md#class-int), node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode))                                                                                                                 |
|                                                                         | set_blend_point_position(point: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2))                                                                                                                                        |

---

## Signals

**triangles_updated**()

Emitted every time the blend space's triangles are created, removed, or when one of their vertices changes position.

---

## Enumerations

enum **BlendMode**:

BlendMode **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

BlendMode **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.

BlendMode **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to BLEND_MODE_DISCRETE, but starts the new animation at the last animation's playback position.

---

enum **SyncMode**:

SyncMode **SYNC_MODE_NONE** = `0`

Inactive animations are frozen and do not advance.

SyncMode **SYNC_MODE_INDEPENDENT** = `1`

Inactive animations advance with a weight of `0`. This is equivalent to the previous `sync = true` behavior.

SyncMode **SYNC_MODE_CYCLIC_MUTABLE** = `2`

All animations are time-scaled so they stay in sync, with the cycle length dynamically computed from active blend weights. This is self-normalizing: a solo animation plays at normal speed.

**Note:** If you apply [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class-animationnodetimeseek) to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use [AnimationNodeAnimation.use_custom_timeline](class_animationnodeanimation.md#class-animationnodeanimation-property-use-custom-timeline) to align the animation lengths.

SyncMode **SYNC_MODE_CYCLIC_CONSTANT** = `3`

All animations are time-scaled so they complete one cycle in cyclic_length seconds, keeping them in sync regardless of their individual lengths.

**Note:** If you apply [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class-animationnodetimeseek) to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use [AnimationNodeAnimation.use_custom_timeline](class_animationnodeanimation.md#class-animationnodeanimation-property-use-custom-timeline) to align the animation lengths.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **auto_triangles** = `true`

-  **set_auto_triangles**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_auto_triangles**()

If `true`, the blend space is triangulated automatically. The mesh updates every time you add or remove points with add_blend_point() and remove_blend_point().

---

BlendMode **blend_mode** = `0`

-  **set_blend_mode**(value: BlendMode)
- BlendMode **get_blend_mode**()

Controls the interpolation between animations.

---

[float](class_float.md#class-float) **cyclic_length** = `0.0`

-  **set_cyclic_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cyclic_length**()

The cycle length in seconds used by SYNC_MODE_CYCLIC_CONSTANT. All animations are time-scaled so they complete one full cycle in this duration. Must be greater than `0` for cyclic sync to take effect.

---

[Vector2](class_vector2.md#class-vector2) **max_space** = `Vector2(1, 1)`

-  **set_max_space**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_max_space**()

The blend space's X and Y axes' upper limit for the points' position. See add_blend_point().

---

[Vector2](class_vector2.md#class-vector2) **min_space** = `Vector2(-1, -1)`

-  **set_min_space**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_min_space**()

The blend space's X and Y axes' lower limit for the points' position. See add_blend_point().

---

[Vector2](class_vector2.md#class-vector2) **snap** = `Vector2(0.1, 0.1)`

-  **set_snap**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_snap**()

Position increment to snap to when moving a point.

---

[bool](class_bool.md#class-bool) **sync**

-  **set_use_sync**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_sync**()

**Deprecated:** Use sync_mode instead.

If `true`, sync mode is enabled (equivalent to SYNC_MODE_INDEPENDENT). This property is kept for backward compatibility.

---

SyncMode **sync_mode** = `0`

-  **set_sync_mode**(value: SyncMode)
- SyncMode **get_sync_mode**()

Controls how animations are synced when blended. See SyncMode for available options.

---

[String](class_string.md#class-string) **x_label** = `"x"`

-  **set_x_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_x_label**()

Name of the blend space's X axis.

---

[String](class_string.md#class-string) **y_label** = `"y"`

-  **set_y_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_y_label**()

Name of the blend space's Y axis.

---

## Method Descriptions

 **add_blend_point**(node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), pos: [Vector2](class_vector2.md#class-vector2), at_index: [int](class_int.md#class-int) = -1, name: [StringName](class_stringname.md#class-stringname) = &"")

Adds a new point with `name` that represents a `node` at the position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

**Note:** If no name is provided, safe index is used as reference. In the future, empty names will be deprecated, so explicitly passing a name is recommended.

---

 **add_triangle**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), z: [int](class_int.md#class-int), at_index: [int](class_int.md#class-int) = -1)

Creates a new triangle using three points `x`, `y`, and `z`. Triangles can overlap. You can insert the triangle at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

---

[int](class_int.md#class-int) **find_blend_point_by_name**(name: [StringName](class_stringname.md#class-stringname))

Returns the index of the blend point with the given `name`. Returns `-1` if no blend point with that name is found.

---

[int](class_int.md#class-int) **get_blend_point_count**()

Returns the number of points in the blend space.

---

[StringName](class_stringname.md#class-stringname) **get_blend_point_name**(point: [int](class_int.md#class-int))

Returns the name of the blend point at index `point`.

---

[AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **get_blend_point_node**(point: [int](class_int.md#class-int))

Returns the [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) referenced by the point at index `point`.

---

[Vector2](class_vector2.md#class-vector2) **get_blend_point_position**(point: [int](class_int.md#class-int))

Returns the position of the point at index `point`.

---

[int](class_int.md#class-int) **get_triangle_count**()

Returns the number of triangles in the blend space.

---

[int](class_int.md#class-int) **get_triangle_point**(triangle: [int](class_int.md#class-int), point: [int](class_int.md#class-int))

Returns the position of the point at index `point` in the triangle of index `triangle`.

---

 **remove_blend_point**(point: [int](class_int.md#class-int))

Removes the point at index `point` from the blend space.

---

 **remove_triangle**(triangle: [int](class_int.md#class-int))

Removes the triangle at index `triangle` from the blend space.

---

 **reorder_blend_point**(from_index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int))

Swaps the blend points at indices `from_index` and `to_index`, exchanging their positions and properties.

---

 **set_blend_point_name**(point: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname))

Sets the name of the blend point at index `point`. If the name conflicts with an existing point, a unique name will be generated automatically.

---

 **set_blend_point_node**(point: [int](class_int.md#class-int), node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode))

Changes the [AnimationNode](class_animationnode.md#class-animationnode) referenced by the point at index `point`.

---

 **set_blend_point_position**(point: [int](class_int.md#class-int), pos: [Vector2](class_vector2.md#class-vector2))

Updates the position of the point at index `point` in the blend space.
