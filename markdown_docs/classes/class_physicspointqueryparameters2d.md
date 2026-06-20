# PhysicsPointQueryParameters2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides parameters for [PhysicsDirectSpaceState2D.intersect_point()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-intersect-point).

## Description

By changing various properties of this object, such as the point position, you can configure the parameters for [PhysicsDirectSpaceState2D.intersect_point()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-intersect-point).

## Properties

| [int](class_int.md#class-int)                                      | canvas_instance_id   | `0`             |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------|
| [bool](class_bool.md#class-bool)                                   | collide_with_areas   | `false`         |
| [bool](class_bool.md#class-bool)                                   | collide_with_bodies | `true`          |
| [int](class_int.md#class-int)                                      | collision_mask           | `4294967295`    |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | exclude                         | `[]`            |
| [Vector2](class_vector2.md#class-vector2)                          | position                       | `Vector2(0, 0)` |

---

## Property Descriptions

[int](class_int.md#class-int) **canvas_instance_id** = `0`

-  **set_canvas_instance_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_canvas_instance_id**()

If different from `0`, restricts the query to a specific canvas layer specified by its instance ID. See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

If `0`, restricts the query to the Viewport's default canvas layer.

---

[bool](class_bool.md#class-bool) **collide_with_areas** = `false`

-  **set_collide_with_areas**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_areas_enabled**()

If `true`, the query will take [Area2D](class_area2d.md#class-area2d)s into account.

---

[bool](class_bool.md#class-bool) **collide_with_bodies** = `true`

-  **set_collide_with_bodies**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_bodies_enabled**()

If `true`, the query will take [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d)s into account.

---

[int](class_int.md#class-int) **collision_mask** = `4294967295`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **exclude** = `[]`

-  **set_exclude**(value: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])
- [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_exclude**()

The list of object [RID](class_rid.md#class-rid)s that will be excluded from collisions. Use [CollisionObject2D.get_rid()](class_collisionobject2d.md#class-collisionobject2d-method-get-rid) to get the [RID](class_rid.md#class-rid) associated with a [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d)-derived node.

**Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

---

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)`

-  **set_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position**()

The position being queried for, in global coordinates.
