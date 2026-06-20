# AnimationNodeBlendSpace1D

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A set of [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s placed on a virtual axis, crossfading between the two adjacent ones. Used by [AnimationTree](class_animationtree.md#class-animationtree).

## Description

A resource used by [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

**AnimationNodeBlendSpace1D** represents a virtual axis on which any type of [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s can be added using add_blend_point(). Outputs the linear blend of the two [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s adjacent to the current value.

You can set the extents of the axis with min_space and max_space.

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

## Properties

| BlendMode   | blend_mode       | `0`       |
|----------------------------------------------------------|--------------------------------------------------------------------------|-----------|
| [float](class_float.md#class-float)                      | cyclic_length | `0.0`     |
| [float](class_float.md#class-float)                      | max_space         | `1.0`     |
| [float](class_float.md#class-float)                      | min_space         | `-1.0`    |
| [float](class_float.md#class-float)                      | snap                   | `0.1`     |
| [bool](class_bool.md#class-bool)                         | sync                   |           |
| SyncMode     | sync_mode         | `0`       |
| [String](class_string.md#class-string)                   | value_label     | `"value"` |

## Methods

|                                                                         | add_blend_point(node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), pos: [float](class_float.md#class-float), at_index: [int](class_int.md#class-int) = -1, name: [StringName](class_stringname.md#class-stringname) = &"")   |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                           | find_blend_point_by_name(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                              |
| [int](class_int.md#class-int)                                           | get_blend_point_count()                                                                                                                                                                                                                            |
| [StringName](class_stringname.md#class-stringname)                      | get_blend_point_name(point: [int](class_int.md#class-int))                                                                                                                                                                                          |
| [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) | get_blend_point_node(point: [int](class_int.md#class-int))                                                                                                                                                                                          |
| [float](class_float.md#class-float)                                     | get_blend_point_position(point: [int](class_int.md#class-int))                                                                                                                                                                                  |
|                                                                         | remove_blend_point(point: [int](class_int.md#class-int))                                                                                                                                                                                              |
|                                                                         | reorder_blend_point(from_index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int))                                                                                                                                              |
|                                                                         | set_blend_point_name(point: [int](class_int.md#class-int), name: [StringName](class_stringname.md#class-stringname))                                                                                                                                |
|                                                                         | set_blend_point_node(point: [int](class_int.md#class-int), node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode))                                                                                                           |
|                                                                         | set_blend_point_position(point: [int](class_int.md#class-int), pos: [float](class_float.md#class-float))                                                                                                                                        |

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

[float](class_float.md#class-float) **max_space** = `1.0`

-  **set_max_space**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_space**()

The blend space's axis's upper limit for the points' position. See add_blend_point().

---

[float](class_float.md#class-float) **min_space** = `-1.0`

-  **set_min_space**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min_space**()

The blend space's axis's lower limit for the points' position. See add_blend_point().

---

[float](class_float.md#class-float) **snap** = `0.1`

-  **set_snap**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_snap**()

Position increment to snap to when moving a point on the axis.

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

[String](class_string.md#class-string) **value_label** = `"value"`

-  **set_value_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_value_label**()

Label of the virtual axis of the blend space.

---

## Method Descriptions

 **add_blend_point**(node: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), pos: [float](class_float.md#class-float), at_index: [int](class_int.md#class-int) = -1, name: [StringName](class_stringname.md#class-stringname) = &"")

Adds a new point with `name` that represents a `node` on the virtual axis at a given position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

**Note:** If no name is provided, safe index is used as reference. In the future, empty names will be deprecated, so explicitly passing a name is recommended.

---

[int](class_int.md#class-int) **find_blend_point_by_name**(name: [StringName](class_stringname.md#class-stringname))

Returns the index of the blend point with the given `name`. Returns `-1` if no blend point with that name is found.

---

[int](class_int.md#class-int) **get_blend_point_count**()

Returns the number of points on the blend axis.

---

[StringName](class_stringname.md#class-stringname) **get_blend_point_name**(point: [int](class_int.md#class-int))

Returns the name of the blend point at index `point`.

---

[AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **get_blend_point_node**(point: [int](class_int.md#class-int))

Returns the [AnimationNode](class_animationnode.md#class-animationnode) referenced by the point at index `point`.

---

[float](class_float.md#class-float) **get_blend_point_position**(point: [int](class_int.md#class-int))

Returns the position of the point at index `point`.

---

 **remove_blend_point**(point: [int](class_int.md#class-int))

Removes the point at index `point` from the blend axis.

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

 **set_blend_point_position**(point: [int](class_int.md#class-int), pos: [float](class_float.md#class-float))

Updates the position of the point at index `point` on the blend axis.
