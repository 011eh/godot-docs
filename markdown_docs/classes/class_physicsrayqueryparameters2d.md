# PhysicsRayQueryParameters2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides parameters for [PhysicsDirectSpaceState2D.intersect_ray()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-intersect-ray).

## Description

By changing various properties of this object, such as the ray position, you can configure the parameters for [PhysicsDirectSpaceState2D.intersect_ray()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-intersect-ray).

## Properties

| [bool](class_bool.md#class-bool)                                   | collide_with_areas   | `false`         |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|-----------------|
| [bool](class_bool.md#class-bool)                                   | collide_with_bodies | `true`          |
| [int](class_int.md#class-int)                                      | collision_mask           | `4294967295`    |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | exclude                         | `[]`            |
| [Vector2](class_vector2.md#class-vector2)                          | from                               | `Vector2(0, 0)` |
| [bool](class_bool.md#class-bool)                                   | hit_from_inside         | `false`         |
| [Vector2](class_vector2.md#class-vector2)                          | to                                   | `Vector2(0, 0)` |

## Methods

| PhysicsRayQueryParameters2D   | create(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), collision_mask: [int](class_int.md#class-int) = 4294967295, exclude: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] = [])    |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

## Property Descriptions

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

[Vector2](class_vector2.md#class-vector2) **from** = `Vector2(0, 0)`

-  **set_from**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_from**()

The starting point of the ray being queried for, in global coordinates.

---

[bool](class_bool.md#class-bool) **hit_from_inside** = `false`

-  **set_hit_from_inside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hit_from_inside_enabled**()

If `true`, the query will detect a hit when starting inside shapes. In this case the collision normal will be `Vector2(0, 0)`. Does not affect concave polygon shapes.

---

[Vector2](class_vector2.md#class-vector2) **to** = `Vector2(0, 0)`

-  **set_to**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_to**()

The ending point of the ray being queried for, in global coordinates.

---

## Method Descriptions

PhysicsRayQueryParameters2D **create**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), collision_mask: [int](class_int.md#class-int) = 4294967295, exclude: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] = [])

Returns a new, pre-configured **PhysicsRayQueryParameters2D** object. Use it to quickly create query parameters using the most common options.

```gdscript
var query = PhysicsRayQueryParameters2D.create(global_position, global_position + Vector2(0, 100))
var collision = get_world_2d().direct_space_state.intersect_ray(query)
```
