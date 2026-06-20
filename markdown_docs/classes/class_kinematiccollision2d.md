# KinematicCollision2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds collision data from the movement of a [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d).

## Description

Holds collision data from the movement of a [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d), usually from [PhysicsBody2D.move_and_collide()](class_physicsbody2d.md#class-physicsbody2d-method-move-and-collide). When a [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision2D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.

## Methods

| [float](class_float.md#class-float)       | get_angle(up_direction: [Vector2](class_vector2.md#class-vector2) = Vector2(0, -1))    |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [Object](class_object.md#class-object)    | get_collider()                                                                      |
| [int](class_int.md#class-int)             | get_collider_id()                                                                |
| [RID](class_rid.md#class-rid)             | get_collider_rid()                                                              |
| [Object](class_object.md#class-object)    | get_collider_shape()                                                          |
| [int](class_int.md#class-int)             | get_collider_shape_index()                                              |
| [Vector2](class_vector2.md#class-vector2) | get_collider_velocity()                                                    |
| [float](class_float.md#class-float)       | get_depth()                                                                            |
| [Object](class_object.md#class-object)    | get_local_shape()                                                                |
| [Vector2](class_vector2.md#class-vector2) | get_normal()                                                                          |
| [Vector2](class_vector2.md#class-vector2) | get_position()                                                                      |
| [Vector2](class_vector2.md#class-vector2) | get_remainder()                                                                    |
| [Vector2](class_vector2.md#class-vector2) | get_travel()                                                                          |

---

## Method Descriptions

[float](class_float.md#class-float) **get_angle**(up_direction: [Vector2](class_vector2.md#class-vector2) = Vector2(0, -1))

Returns the collision angle according to `up_direction`, which is [Vector2.UP](class_vector2.md#class-vector2-constant-up) by default. This value is always positive.

---

[Object](class_object.md#class-object) **get_collider**()

Returns the colliding body's attached [Object](class_object.md#class-object).

---

[int](class_int.md#class-int) **get_collider_id**()

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class-object). See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---

[RID](class_rid.md#class-rid) **get_collider_rid**()

Returns the colliding body's [RID](class_rid.md#class-rid) used by the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d).

---

[Object](class_object.md#class-object) **get_collider_shape**()

Returns the colliding body's shape.

---

[int](class_int.md#class-int) **get_collider_shape_index**()

Returns the colliding body's shape index. See [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d).

---

[Vector2](class_vector2.md#class-vector2) **get_collider_velocity**()

Returns the colliding body's velocity.

---

[float](class_float.md#class-float) **get_depth**()

Returns the colliding body's length of overlap along the collision normal.

---

[Object](class_object.md#class-object) **get_local_shape**()

Returns the moving object's colliding shape.

---

[Vector2](class_vector2.md#class-vector2) **get_normal**()

Returns the colliding body's shape's normal at the point of collision.

---

[Vector2](class_vector2.md#class-vector2) **get_position**()

Returns the point of collision in global coordinates.

---

[Vector2](class_vector2.md#class-vector2) **get_remainder**()

Returns the moving object's remaining movement vector.

---

[Vector2](class_vector2.md#class-vector2) **get_travel**()

Returns the moving object's travel before collision.
