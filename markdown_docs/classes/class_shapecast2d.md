# ShapeCast2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A 2D shape that sweeps a region of space to detect [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d)s.

## Description

Shape casting allows to detect collision objects by sweeping its shape along the cast direction determined by target_position. This is similar to [RayCast2D](class_raycast2d.md#class-raycast2d), but it allows for sweeping a region of space, rather than just a straight line. **ShapeCast2D** can detect multiple collision objects. It is useful for things like wide laser beams or snapping a simple shape to a floor.

Immediate collision overlaps can be done with the target_position set to `Vector2(0, 0)` and by calling force_shapecast_update() within the same physics frame. This helps to overcome some limitations of [Area2D](class_area2d.md#class-area2d) when used as an instantaneous detection area, as collision information isn't immediately available to it.

**Note:** Shape casting is more computationally expensive than ray casting.

## Properties

| [bool](class_bool.md#class-bool)          | collide_with_areas   | `false`          |
|-------------------------------------------|------------------------------------------------------------------------|------------------|
| [bool](class_bool.md#class-bool)          | collide_with_bodies | `true`           |
| [int](class_int.md#class-int)             | collision_mask           | `1`              |
| [Array](class_array.md#class-array)       | collision_result       | `[]`             |
| [bool](class_bool.md#class-bool)          | enabled                         | `true`           |
| [bool](class_bool.md#class-bool)          | exclude_parent           | `true`           |
| [float](class_float.md#class-float)       | margin                           | `0.0`            |
| [int](class_int.md#class-int)             | max_results                 | `32`             |
| [Shape2D](class_shape2d.md#class-shape2d) | shape                             |                  |
| [Vector2](class_vector2.md#class-vector2) | target_position         | `Vector2(0, 50)` |

## Methods

|                                           | add_exception(node: [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d))                              |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           | add_exception_rid(rid: [RID](class_rid.md#class-rid))                                                                 |
|                                           | clear_exceptions()                                                                                                     |
|                                           | force_shapecast_update()                                                                                         |
| [float](class_float.md#class-float)       | get_closest_collision_safe_fraction()                                                               |
| [float](class_float.md#class-float)       | get_closest_collision_unsafe_fraction()                                                           |
| [Object](class_object.md#class-object)    | get_collider(index: [int](class_int.md#class-int))                                                                         |
| [RID](class_rid.md#class-rid)             | get_collider_rid(index: [int](class_int.md#class-int))                                                                 |
| [int](class_int.md#class-int)             | get_collider_shape(index: [int](class_int.md#class-int))                                                             |
| [int](class_int.md#class-int)             | get_collision_count()                                                                                               |
| [bool](class_bool.md#class-bool)          | get_collision_mask_value(layer_number: [int](class_int.md#class-int))                                          |
| [Vector2](class_vector2.md#class-vector2) | get_collision_normal(index: [int](class_int.md#class-int))                                                         |
| [Vector2](class_vector2.md#class-vector2) | get_collision_point(index: [int](class_int.md#class-int))                                                           |
| [bool](class_bool.md#class-bool)          | is_colliding()                                                                                                             |
|                                           | remove_exception(node: [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d))                        |
|                                           | remove_exception_rid(rid: [RID](class_rid.md#class-rid))                                                           |
|                                           | set_collision_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **collide_with_areas** = `false`

-  **set_collide_with_areas**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_areas_enabled**()

If `true`, collisions with [Area2D](class_area2d.md#class-area2d)s will be reported.

---

[bool](class_bool.md#class-bool) **collide_with_bodies** = `true`

-  **set_collide_with_bodies**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_bodies_enabled**()

If `true`, collisions with [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d)s will be reported.

---

[int](class_int.md#class-int) **collision_mask** = `1`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The shape's collision mask. Only objects in at least one collision layer enabled in the mask will be detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[Array](class_array.md#class-array) **collision_result** = `[]`

- [Array](class_array.md#class-array) **get_collision_result**()

Returns the complete collision information from the collision sweep. The data returned is the same as in the [PhysicsDirectSpaceState2D.get_rest_info()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-get-rest-info) method.

---

[bool](class_bool.md#class-bool) **enabled** = `true`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

If `true`, collisions will be reported.

---

[bool](class_bool.md#class-bool) **exclude_parent** = `true`

-  **set_exclude_parent_body**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_exclude_parent_body**()

If `true`, the parent node will be excluded from collision detection.

---

[float](class_float.md#class-float) **margin** = `0.0`

-  **set_margin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_margin**()

The collision margin for the shape. A larger margin helps detecting collisions more consistently, at the cost of precision.

---

[int](class_int.md#class-int) **max_results** = `32`

-  **set_max_results**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_results**()

The number of intersections can be limited with this parameter, to reduce the processing time.

---

[Shape2D](class_shape2d.md#class-shape2d) **shape**

-  **set_shape**(value: [Shape2D](class_shape2d.md#class-shape2d))
- [Shape2D](class_shape2d.md#class-shape2d) **get_shape**()

The shape to be used for collision queries.

---

[Vector2](class_vector2.md#class-vector2) **target_position** = `Vector2(0, 50)`

-  **set_target_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_target_position**()

The shape's destination point, relative to this node's [Node2D.position](class_node2d.md#class-node2d-property-position).

---

## Method Descriptions

 **add_exception**(node: [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d))

Adds a collision exception so the shape does not report collisions with the specified node.

---

 **add_exception_rid**(rid: [RID](class_rid.md#class-rid))

Adds a collision exception so the shape does not report collisions with the specified [RID](class_rid.md#class-rid).

---

 **clear_exceptions**()

Removes all collision exceptions for this shape.

---

 **force_shapecast_update**()

Updates the collision information for the shape immediately, without waiting for the next `_physics_process` call. Use this method, for example, when the shape or its parent has changed state.

**Note:** Setting enabled to `true` is not required for this to work.

---

[float](class_float.md#class-float) **get_closest_collision_safe_fraction**()

Returns the fraction from this cast's origin to its target_position of how far the shape can move without triggering a collision, as a value between `0.0` and `1.0`.

---

[float](class_float.md#class-float) **get_closest_collision_unsafe_fraction**()

Returns the fraction from this cast's origin to its target_position of how far the shape must move to trigger a collision, as a value between `0.0` and `1.0`.

In ideal conditions this would be the same as get_closest_collision_safe_fraction(), however shape casting is calculated in discrete steps, so the precise point of collision can occur between two calculated positions.

---

[Object](class_object.md#class-object) **get_collider**(index: [int](class_int.md#class-int))

Returns the collided [Object](class_object.md#class-object) of one of the multiple collisions at `index`, or `null` if no object is intersecting the shape (i.e. is_colliding() returns `false`).

---

[RID](class_rid.md#class-rid) **get_collider_rid**(index: [int](class_int.md#class-int))

Returns the [RID](class_rid.md#class-rid) of the collided object of one of the multiple collisions at `index`.

---

[int](class_int.md#class-int) **get_collider_shape**(index: [int](class_int.md#class-int))

Returns the shape ID of the colliding shape of one of the multiple collisions at `index`, or `0` if no object is intersecting the shape (i.e. is_colliding() returns `false`).

---

[int](class_int.md#class-int) **get_collision_count**()

The number of collisions detected at the point of impact. Use this to iterate over multiple collisions as provided by get_collider(), get_collider_shape(), get_collision_point(), and get_collision_normal() methods.

---

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the collision_mask is enabled, given a `layer_number` between 1 and 32.

---

[Vector2](class_vector2.md#class-vector2) **get_collision_normal**(index: [int](class_int.md#class-int))

Returns the normal of one of the multiple collisions at `index` of the intersecting object.

---

[Vector2](class_vector2.md#class-vector2) **get_collision_point**(index: [int](class_int.md#class-int))

Returns the collision point of one of the multiple collisions at `index` where the shape intersects the colliding object.

**Note:** This point is in the **global** coordinate system.

---

[bool](class_bool.md#class-bool) **is_colliding**()

Returns whether any object is intersecting with the shape's vector (considering the vector length).

---

 **remove_exception**(node: [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d))

Removes a collision exception so the shape does report collisions with the specified node.

---

 **remove_exception_rid**(rid: [RID](class_rid.md#class-rid))

Removes a collision exception so the shape does report collisions with the specified [RID](class_rid.md#class-rid).

---

 **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the collision_mask, given a `layer_number` between 1 and 32.
