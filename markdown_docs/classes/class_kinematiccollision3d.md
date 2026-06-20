# KinematicCollision3D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds collision data from the movement of a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d).

## Description

Holds collision data from the movement of a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d), usually from [PhysicsBody3D.move_and_collide()](class_physicsbody3d.md#class-physicsbody3d-method-move-and-collide). When a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision3D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.

## Methods

| [float](class_float.md#class-float)       | get_angle(collision_index: [int](class_int.md#class-int) = 0, up_direction: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0))    |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Object](class_object.md#class-object)    | get_collider(collision_index: [int](class_int.md#class-int) = 0)                                                                          |
| [int](class_int.md#class-int)             | get_collider_id(collision_index: [int](class_int.md#class-int) = 0)                                                                    |
| [RID](class_rid.md#class-rid)             | get_collider_rid(collision_index: [int](class_int.md#class-int) = 0)                                                                  |
| [Object](class_object.md#class-object)    | get_collider_shape(collision_index: [int](class_int.md#class-int) = 0)                                                              |
| [int](class_int.md#class-int)             | get_collider_shape_index(collision_index: [int](class_int.md#class-int) = 0)                                                  |
| [Vector3](class_vector3.md#class-vector3) | get_collider_velocity(collision_index: [int](class_int.md#class-int) = 0)                                                        |
| [int](class_int.md#class-int)             | get_collision_count()                                                                                                              |
| [float](class_float.md#class-float)       | get_depth()                                                                                                                                  |
| [Object](class_object.md#class-object)    | get_local_shape(collision_index: [int](class_int.md#class-int) = 0)                                                                    |
| [Vector3](class_vector3.md#class-vector3) | get_normal(collision_index: [int](class_int.md#class-int) = 0)                                                                              |
| [Vector3](class_vector3.md#class-vector3) | get_position(collision_index: [int](class_int.md#class-int) = 0)                                                                          |
| [Vector3](class_vector3.md#class-vector3) | get_remainder()                                                                                                                          |
| [Vector3](class_vector3.md#class-vector3) | get_travel()                                                                                                                                |

---

## Method Descriptions

[float](class_float.md#class-float) **get_angle**(collision_index: [int](class_int.md#class-int) = 0, up_direction: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0))

Returns the collision angle according to `up_direction`, which is [Vector3.UP](class_vector3.md#class-vector3-constant-up) by default. This value is always positive.

---

[Object](class_object.md#class-object) **get_collider**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's attached [Object](class_object.md#class-object) given a collision index (the deepest collision by default).

---

[int](class_int.md#class-int) **get_collider_id**(collision_index: [int](class_int.md#class-int) = 0)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class-object) given a collision index (the deepest collision by default). See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---

[RID](class_rid.md#class-rid) **get_collider_rid**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's [RID](class_rid.md#class-rid) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) given a collision index (the deepest collision by default).

---

[Object](class_object.md#class-object) **get_collider_shape**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's shape given a collision index (the deepest collision by default).

---

[int](class_int.md#class-int) **get_collider_shape_index**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's shape index given a collision index (the deepest collision by default). See [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d).

---

[Vector3](class_vector3.md#class-vector3) **get_collider_velocity**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's velocity given a collision index (the deepest collision by default).

---

[int](class_int.md#class-int) **get_collision_count**()

Returns the number of detected collisions.

---

[float](class_float.md#class-float) **get_depth**()

Returns the colliding body's length of overlap along the collision normal.

---

[Object](class_object.md#class-object) **get_local_shape**(collision_index: [int](class_int.md#class-int) = 0)

Returns the moving object's colliding shape given a collision index (the deepest collision by default).

---

[Vector3](class_vector3.md#class-vector3) **get_normal**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default).

---

[Vector3](class_vector3.md#class-vector3) **get_position**(collision_index: [int](class_int.md#class-int) = 0)

Returns the point of collision in global coordinates given a collision index (the deepest collision by default).

---

[Vector3](class_vector3.md#class-vector3) **get_remainder**()

Returns the moving object's remaining movement vector.

---

[Vector3](class_vector3.md#class-vector3) **get_travel**()

Returns the moving object's travel before collision.
