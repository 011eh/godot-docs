# PhysicsBody3D

**Inherits:** [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [CharacterBody3D](class_characterbody3d.md#class-characterbody3d), [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d), [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d), [StaticBody3D](class_staticbody3d.md#class-staticbody3d)

Abstract base class for 3D game objects affected by physics.

## Description

**PhysicsBody3D** is an abstract base class for 3D game objects affected by physics. All 3D physics bodies inherit from it.

**Warning:** With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

## Properties

| [bool](class_bool.md#class-bool)   | axis_lock_angular_x   | `false`   |
|------------------------------------|----------------------------------------------------------------------------|-----------|
| [bool](class_bool.md#class-bool)   | axis_lock_angular_y   | `false`   |
| [bool](class_bool.md#class-bool)   | axis_lock_angular_z   | `false`   |
| [bool](class_bool.md#class-bool)   | axis_lock_linear_x     | `false`   |
| [bool](class_bool.md#class-bool)   | axis_lock_linear_y     | `false`   |
| [bool](class_bool.md#class-bool)   | axis_lock_linear_z     | `false`   |

## Methods

|                                                                                  | add_collision_exception_with(body: [Node](class_node.md#class-node))                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                 | get_axis_lock(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis))                                                                                                                                                                                                                                                                                                                 |
| [Array](class_array.md#class-array)[PhysicsBody3D]       | get_collision_exceptions()                                                                                                                                                                                                                                                                                                                                                                   |
| [Vector3](class_vector3.md#class-vector3)                                        | get_gravity()                                                                                                                                                                                                                                                                                                                                                                                             |
| [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d) | move_and_collide(motion: [Vector3](class_vector3.md#class-vector3), test_only: [bool](class_bool.md#class-bool) = false, safe_margin: [float](class_float.md#class-float) = 0.001, recovery_as_collision: [bool](class_bool.md#class-bool) = false, max_collisions: [int](class_int.md#class-int) = 1)                                                                                               |
|                                                                                  | remove_collision_exception_with(body: [Node](class_node.md#class-node))                                                                                                                                                                                                                                                                                                               |
|                                                                                  | set_axis_lock(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                 | test_move(from: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), collision: [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d) = null, safe_margin: [float](class_float.md#class-float) = 0.001, recovery_as_collision: [bool](class_bool.md#class-bool) = false, max_collisions: [int](class_int.md#class-int) = 1) |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **axis_lock_angular_x** = `false`

-  **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) 

Lock the body's rotation in the X axis.

---

[bool](class_bool.md#class-bool) **axis_lock_angular_y** = `false`

-  **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) 

Lock the body's rotation in the Y axis.

---

[bool](class_bool.md#class-bool) **axis_lock_angular_z** = `false`

-  **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) 

Lock the body's rotation in the Z axis.

---

[bool](class_bool.md#class-bool) **axis_lock_linear_x** = `false`

-  **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) 

Lock the body's linear movement in the X axis.

---

[bool](class_bool.md#class-bool) **axis_lock_linear_y** = `false`

-  **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) 

Lock the body's linear movement in the Y axis.

---

[bool](class_bool.md#class-bool) **axis_lock_linear_z** = `false`

-  **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis)) 

Lock the body's linear movement in the Z axis.

---

## Method Descriptions

 **add_collision_exception_with**(body: [Node](class_node.md#class-node))

Adds a body to the list of bodies that this body can't collide with.

---

[bool](class_bool.md#class-bool) **get_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis))

Returns `true` if the specified linear or rotational `axis` is locked.

---

[Array](class_array.md#class-array)[PhysicsBody3D] **get_collision_exceptions**()

Returns an array of nodes that were added as collision exceptions for this body.

---

[Vector3](class_vector3.md#class-vector3) **get_gravity**()

Returns the gravity vector computed from all sources that can affect the body, including all gravity overrides from [Area3D](class_area3d.md#class-area3d) nodes and the global world gravity.

---

[KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d) **move_and_collide**(motion: [Vector3](class_vector3.md#class-vector3), test_only: [bool](class_bool.md#class-bool) = false, safe_margin: [float](class_float.md#class-float) = 0.001, recovery_as_collision: [bool](class_bool.md#class-bool) = false, max_collisions: [int](class_int.md#class-int) = 1)

Moves the body along the vector `motion`. In order to be frame rate independent in [Node._physics_process()](class_node.md#class-node-private-method-physics-process) or [Node._process()](class_node.md#class-node-private-method-process), `motion` should be computed using `delta`.

The body will stop if it collides. Returns a [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d), which contains information about the collision when stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be collision information is given.

`safe_margin` is the extra margin used for collision recovery (see [CharacterBody3D.safe_margin](class_characterbody3d.md#class-characterbody3d-property-safe-margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is used e.g. by [CharacterBody3D](class_characterbody3d.md#class-characterbody3d) for improving floor detection during floor snapping.

`max_collisions` allows to retrieve more than one collision result.

---

 **remove_collision_exception_with**(body: [Node](class_node.md#class-node))

Removes a body from the list of bodies that this body can't collide with.

---

 **set_axis_lock**(axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))

Locks or unlocks the specified linear or rotational `axis` depending on the value of `lock`.

---

[bool](class_bool.md#class-bool) **test_move**(from: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), collision: [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d) = null, safe_margin: [float](class_float.md#class-float) = 0.001, recovery_as_collision: [bool](class_bool.md#class-bool) = false, max_collisions: [int](class_int.md#class-int) = 1)

Checks for collisions without moving the body. In order to be frame rate independent in [Node._physics_process()](class_node.md#class-node-private-method-physics-process) or [Node._process()](class_node.md#class-node-private-method-process), `motion` should be computed using `delta`.

Virtually sets the node's position, scale and rotation to that of the given [Transform3D](class_transform3d.md#class-transform3d), then tries to move the body along the vector `motion`. Returns `true` if a collision would stop the body from moving along the whole path.

`collision` is an optional object of type [KinematicCollision3D](class_kinematiccollision3d.md#class-kinematiccollision3d), which contains additional information about the collision when stopped, or when touching another body along the motion.

`safe_margin` is the extra margin used for collision recovery (see [CharacterBody3D.safe_margin](class_characterbody3d.md#class-characterbody3d-property-safe-margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is useful for checking whether the body would *touch* any other bodies.

`max_collisions` allows to retrieve more than one collision result.
