# PhysicsTestMotionParameters2D

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides parameters for [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class-physicsserver2d-method-body-test-motion).

## Description

By changing various properties of this object, such as the motion, you can configure the parameters for [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class-physicsserver2d-method-body-test-motion).

## Properties

| [bool](class_bool.md#class-bool)                                   | collide_separation_ray   | `false`                         |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------|
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] | exclude_bodies                   | `[]`                            |
| [Array](class_array.md#class-array)[[int](class_int.md#class-int)] | exclude_objects                 | `[]`                            |
| [Transform2D](class_transform2d.md#class-transform2d)              | from                                       | `Transform2D(1, 0, 0, 1, 0, 0)` |
| [float](class_float.md#class-float)                                | margin                                   | `0.08`                          |
| [Vector2](class_vector2.md#class-vector2)                          | motion                                   | `Vector2(0, 0)`                 |
| [bool](class_bool.md#class-bool)                                   | recovery_as_collision     | `false`                         |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **collide_separation_ray** = `false`

-  **set_collide_separation_ray_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_separation_ray_enabled**()

If set to `true`, shapes of type [PhysicsServer2D.SHAPE_SEPARATION_RAY](class_physicsserver2d.md#class-physicsserver2d-constant-shape-separation-ray) are used to detect collisions and can stop the motion. Can be useful when snapping to the ground.

If set to `false`, shapes of type [PhysicsServer2D.SHAPE_SEPARATION_RAY](class_physicsserver2d.md#class-physicsserver2d-constant-shape-separation-ray) are only used for separation when overlapping with other bodies. That's the main use for separation ray shapes.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **exclude_bodies** = `[]`

-  **set_exclude_bodies**(value: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])
- [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_exclude_bodies**()

Optional array of body [RID](class_rid.md#class-rid) to exclude from collision. Use [CollisionObject2D.get_rid()](class_collisionobject2d.md#class-collisionobject2d-method-get-rid) to get the [RID](class_rid.md#class-rid) associated with a [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d)-derived node.

---

[Array](class_array.md#class-array)[[int](class_int.md#class-int)] **exclude_objects** = `[]`

-  **set_exclude_objects**(value: [Array](class_array.md#class-array)[[int](class_int.md#class-int)])
- [Array](class_array.md#class-array)[[int](class_int.md#class-int)] **get_exclude_objects**()

Optional array of object unique instance ID to exclude from collision. See [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---

[Transform2D](class_transform2d.md#class-transform2d) **from** = `Transform2D(1, 0, 0, 1, 0, 0)`

-  **set_from**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_from**()

Transform in global space where the motion should start. Usually set to [Node2D.global_transform](class_node2d.md#class-node2d-property-global-transform) for the current body's transform.

---

[float](class_float.md#class-float) **margin** = `0.08`

-  **set_margin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_margin**()

Increases the size of the shapes involved in the collision detection.

---

[Vector2](class_vector2.md#class-vector2) **motion** = `Vector2(0, 0)`

-  **set_motion**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_motion**()

Motion vector to define the length and direction of the motion to test.

---

[bool](class_bool.md#class-bool) **recovery_as_collision** = `false`

-  **set_recovery_as_collision_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_recovery_as_collision_enabled**()

If set to `true`, any depenetration from the recovery phase is reported as a collision; this is used e.g. by [CharacterBody2D](class_characterbody2d.md#class-characterbody2d) for improving floor detection during floor snapping.

If set to `false`, only collisions resulting from the motion are reported, which is generally the desired behavior.
