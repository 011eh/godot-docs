# PhysicsTestMotionResult3D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Describes the motion and collision result from [PhysicsServer3D.body_test_motion()](class_physicsserver3d.md#class-physicsserver3d-method-body-test-motion).

## Description

Describes the motion and collision result from [PhysicsServer3D.body_test_motion()](class_physicsserver3d.md#class-physicsserver3d-method-body-test-motion).

## Methods

| [Object](class_object.md#class-object)    | get_collider(collision_index: [int](class_int.md#class-int) = 0)                           |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)             | get_collider_id(collision_index: [int](class_int.md#class-int) = 0)                     |
| [RID](class_rid.md#class-rid)             | get_collider_rid(collision_index: [int](class_int.md#class-int) = 0)                   |
| [int](class_int.md#class-int)             | get_collider_shape(collision_index: [int](class_int.md#class-int) = 0)               |
| [Vector3](class_vector3.md#class-vector3) | get_collider_velocity(collision_index: [int](class_int.md#class-int) = 0)         |
| [int](class_int.md#class-int)             | get_collision_count()                                                               |
| [float](class_float.md#class-float)       | get_collision_depth(collision_index: [int](class_int.md#class-int) = 0)             |
| [int](class_int.md#class-int)             | get_collision_local_shape(collision_index: [int](class_int.md#class-int) = 0) |
| [Vector3](class_vector3.md#class-vector3) | get_collision_normal(collision_index: [int](class_int.md#class-int) = 0)           |
| [Vector3](class_vector3.md#class-vector3) | get_collision_point(collision_index: [int](class_int.md#class-int) = 0)             |
| [float](class_float.md#class-float)       | get_collision_safe_fraction()                                               |
| [float](class_float.md#class-float)       | get_collision_unsafe_fraction()                                           |
| [Vector3](class_vector3.md#class-vector3) | get_remainder()                                                                           |
| [Vector3](class_vector3.md#class-vector3) | get_travel()                                                                                 |

---

## Method Descriptions

[Object](class_object.md#class-object) **get_collider**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's attached [Object](class_object.md#class-object) given a collision index (the deepest collision by default), if a collision occurred.

---

[int](class_int.md#class-int) **get_collider_id**(collision_index: [int](class_int.md#class-int) = 0)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class-object) given a collision index (the deepest collision by default), if a collision occurred. See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---

[RID](class_rid.md#class-rid) **get_collider_rid**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's [RID](class_rid.md#class-rid) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) given a collision index (the deepest collision by default), if a collision occurred.

---

[int](class_int.md#class-int) **get_collider_shape**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's shape index given a collision index (the deepest collision by default), if a collision occurred. See [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d).

---

[Vector3](class_vector3.md#class-vector3) **get_collider_velocity**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's velocity given a collision index (the deepest collision by default), if a collision occurred.

---

[int](class_int.md#class-int) **get_collision_count**()

Returns the number of detected collisions.

---

[float](class_float.md#class-float) **get_collision_depth**(collision_index: [int](class_int.md#class-int) = 0)

Returns the length of overlap along the collision normal given a collision index (the deepest collision by default), if a collision occurred.

---

[int](class_int.md#class-int) **get_collision_local_shape**(collision_index: [int](class_int.md#class-int) = 0)

Returns the moving object's colliding shape given a collision index (the deepest collision by default), if a collision occurred.

---

[Vector3](class_vector3.md#class-vector3) **get_collision_normal**(collision_index: [int](class_int.md#class-int) = 0)

Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default), if a collision occurred.

---

[Vector3](class_vector3.md#class-vector3) **get_collision_point**(collision_index: [int](class_int.md#class-int) = 0)

Returns the point of collision in global coordinates given a collision index (the deepest collision by default), if a collision occurred.

---

[float](class_float.md#class-float) **get_collision_safe_fraction**()

Returns the maximum fraction of the motion that can occur without a collision, between `0` and `1`.

---

[float](class_float.md#class-float) **get_collision_unsafe_fraction**()

Returns the minimum fraction of the motion needed to collide, if a collision occurred, between `0` and `1`.

---

[Vector3](class_vector3.md#class-vector3) **get_remainder**()

Returns the moving object's remaining movement vector.

---

[Vector3](class_vector3.md#class-vector3) **get_travel**()

Returns the moving object's travel before collision.
