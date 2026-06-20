# PhysicsTestMotionResult2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Describes the motion and collision result from [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class-physicsserver2d-method-body-test-motion).

## Description

Describes the motion and collision result from [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class-physicsserver2d-method-body-test-motion).

## Methods

| [Object](class_object.md#class-object)    | get_collider()                                   |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)             | get_collider_id()                             |
| [RID](class_rid.md#class-rid)             | get_collider_rid()                           |
| [int](class_int.md#class-int)             | get_collider_shape()                       |
| [Vector2](class_vector2.md#class-vector2) | get_collider_velocity()                 |
| [float](class_float.md#class-float)       | get_collision_depth()                     |
| [int](class_int.md#class-int)             | get_collision_local_shape()         |
| [Vector2](class_vector2.md#class-vector2) | get_collision_normal()                   |
| [Vector2](class_vector2.md#class-vector2) | get_collision_point()                     |
| [float](class_float.md#class-float)       | get_collision_safe_fraction()     |
| [float](class_float.md#class-float)       | get_collision_unsafe_fraction() |
| [Vector2](class_vector2.md#class-vector2) | get_remainder()                                 |
| [Vector2](class_vector2.md#class-vector2) | get_travel()                                       |

---

## Method Descriptions

[Object](class_object.md#class-object) **get_collider**()

Returns the colliding body's attached [Object](class_object.md#class-object), if a collision occurred.

---

[int](class_int.md#class-int) **get_collider_id**()

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class-object), if a collision occurred. See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---

[RID](class_rid.md#class-rid) **get_collider_rid**()

Returns the colliding body's [RID](class_rid.md#class-rid) used by the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d), if a collision occurred.

---

[int](class_int.md#class-int) **get_collider_shape**()

Returns the colliding body's shape index, if a collision occurred. See [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d).

---

[Vector2](class_vector2.md#class-vector2) **get_collider_velocity**()

Returns the colliding body's velocity, if a collision occurred.

---

[float](class_float.md#class-float) **get_collision_depth**()

Returns the length of overlap along the collision normal, if a collision occurred.

---

[int](class_int.md#class-int) **get_collision_local_shape**()

Returns the moving object's colliding shape, if a collision occurred.

---

[Vector2](class_vector2.md#class-vector2) **get_collision_normal**()

Returns the colliding body's shape's normal at the point of collision, if a collision occurred.

---

[Vector2](class_vector2.md#class-vector2) **get_collision_point**()

Returns the point of collision in global coordinates, if a collision occurred.

---

[float](class_float.md#class-float) **get_collision_safe_fraction**()

Returns the maximum fraction of the motion that can occur without a collision, between `0` and `1`.

---

[float](class_float.md#class-float) **get_collision_unsafe_fraction**()

Returns the minimum fraction of the motion needed to collide, if a collision occurred, between `0` and `1`.

---

[Vector2](class_vector2.md#class-vector2) **get_remainder**()

Returns the moving object's remaining movement vector.

---

[Vector2](class_vector2.md#class-vector2) **get_travel**()

Returns the moving object's travel before collision.
