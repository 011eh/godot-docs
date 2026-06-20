# PhysicsDirectBodyState2D

**Inherits:** [Object](class_object.md#class-object)

**Inherited By:** [PhysicsDirectBodyState2DExtension](class_physicsdirectbodystate2dextension.md#class-physicsdirectbodystate2dextension)

Provides direct access to a physics body in the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d).

## Description

Provides direct access to a physics body in the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d), allowing safe changes to physics properties. This object is passed via the direct state callback of [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d), and is intended for changing the direct state of that body. See [RigidBody2D._integrate_forces()](class_rigidbody2d.md#class-rigidbody2d-private-method-integrate-forces).

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [Ray-casting](../tutorials/physics/ray-casting.md)

## Properties

| [float](class_float.md#class-float)                   | angular_velocity         |
|-------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Vector2](class_vector2.md#class-vector2)             | center_of_mass             |
| [Vector2](class_vector2.md#class-vector2)             | center_of_mass_local |
| [int](class_int.md#class-int)                         | collision_layer           |
| [int](class_int.md#class-int)                         | collision_mask             |
| [float](class_float.md#class-float)                   | inverse_inertia           |
| [float](class_float.md#class-float)                   | inverse_mass                 |
| [Vector2](class_vector2.md#class-vector2)             | linear_velocity           |
| [bool](class_bool.md#class-bool)                      | sleeping                         |
| [float](class_float.md#class-float)                   | step                                 |
| [float](class_float.md#class-float)                   | total_angular_damp     |
| [Vector2](class_vector2.md#class-vector2)             | total_gravity               |
| [float](class_float.md#class-float)                   | total_linear_damp       |
| [Transform2D](class_transform2d.md#class-transform2d) | transform                       |

## Methods

|                                                                                                 | add_constant_central_force(force: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))                                      |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                 | add_constant_force(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0)) |
|                                                                                                 | add_constant_torque(torque: [float](class_float.md#class-float))                                                                         |
|                                                                                                 | apply_central_force(force: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))                                                    |
|                                                                                                 | apply_central_impulse(impulse: [Vector2](class_vector2.md#class-vector2))                                                              |
|                                                                                                 | apply_force(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))               |
|                                                                                                 | apply_impulse(impulse: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))         |
|                                                                                                 | apply_torque(torque: [float](class_float.md#class-float))                                                                                       |
|                                                                                                 | apply_torque_impulse(impulse: [float](class_float.md#class-float))                                                                      |
| [Vector2](class_vector2.md#class-vector2)                                                       | get_constant_force()                                                                                                                      |
| [float](class_float.md#class-float)                                                             | get_constant_torque()                                                                                                                    |
| [RID](class_rid.md#class-rid)                                                                   | get_contact_collider(contact_idx: [int](class_int.md#class-int))                                                                        |
| [int](class_int.md#class-int)                                                                   | get_contact_collider_id(contact_idx: [int](class_int.md#class-int))                                                                  |
| [Object](class_object.md#class-object)                                                          | get_contact_collider_object(contact_idx: [int](class_int.md#class-int))                                                          |
| [Vector2](class_vector2.md#class-vector2)                                                       | get_contact_collider_position(contact_idx: [int](class_int.md#class-int))                                                      |
| [int](class_int.md#class-int)                                                                   | get_contact_collider_shape(contact_idx: [int](class_int.md#class-int))                                                            |
| [Vector2](class_vector2.md#class-vector2)                                                       | get_contact_collider_velocity_at_position(contact_idx: [int](class_int.md#class-int))                              |
| [int](class_int.md#class-int)                                                                   | get_contact_count()                                                                                                                        |
| [Vector2](class_vector2.md#class-vector2)                                                       | get_contact_impulse(contact_idx: [int](class_int.md#class-int))                                                                          |
| [Vector2](class_vector2.md#class-vector2)                                                       | get_contact_local_normal(contact_idx: [int](class_int.md#class-int))                                                                |
| [Vector2](class_vector2.md#class-vector2)                                                       | get_contact_local_position(contact_idx: [int](class_int.md#class-int))                                                            |
| [int](class_int.md#class-int)                                                                   | get_contact_local_shape(contact_idx: [int](class_int.md#class-int))                                                                  |
| [Vector2](class_vector2.md#class-vector2)                                                       | get_contact_local_velocity_at_position(contact_idx: [int](class_int.md#class-int))                                    |
| [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) | get_space_state()                                                                                                                            |
| [Vector2](class_vector2.md#class-vector2)                                                       | get_velocity_at_local_position(local_position: [Vector2](class_vector2.md#class-vector2))                                     |
|                                                                                                 | integrate_forces()                                                                                                                          |
|                                                                                                 | set_constant_force(force: [Vector2](class_vector2.md#class-vector2))                                                                      |
|                                                                                                 | set_constant_torque(torque: [float](class_float.md#class-float))                                                                         |

---

## Property Descriptions

[float](class_float.md#class-float) **angular_velocity**

-  **set_angular_velocity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_angular_velocity**()

The body's rotational velocity in *radians* per second.

---

[Vector2](class_vector2.md#class-vector2) **center_of_mass**

- [Vector2](class_vector2.md#class-vector2) **get_center_of_mass**()

The body's center of mass position relative to the body's center in the global coordinate system.

---

[Vector2](class_vector2.md#class-vector2) **center_of_mass_local**

- [Vector2](class_vector2.md#class-vector2) **get_center_of_mass_local**()

The body's center of mass position in the body's local coordinate system.

---

[int](class_int.md#class-int) **collision_layer**

-  **set_collision_layer**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_layer**()

The body's collision layer.

---

[int](class_int.md#class-int) **collision_mask**

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The body's collision mask.

---

[float](class_float.md#class-float) **inverse_inertia**

- [float](class_float.md#class-float) **get_inverse_inertia**()

The inverse of the inertia of the body.

---

[float](class_float.md#class-float) **inverse_mass**

- [float](class_float.md#class-float) **get_inverse_mass**()

The inverse of the mass of the body.

---

[Vector2](class_vector2.md#class-vector2) **linear_velocity**

-  **set_linear_velocity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_linear_velocity**()

The body's linear velocity in pixels per second.

---

[bool](class_bool.md#class-bool) **sleeping**

-  **set_sleep_state**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_sleeping**()

If `true`, this body is currently sleeping (not active).

---

[float](class_float.md#class-float) **step**

- [float](class_float.md#class-float) **get_step**()

The timestep (delta) used for the simulation.

---

[float](class_float.md#class-float) **total_angular_damp**

- [float](class_float.md#class-float) **get_total_angular_damp**()

The rate at which the body stops rotating, if there are not any other forces moving it.

---

[Vector2](class_vector2.md#class-vector2) **total_gravity**

- [Vector2](class_vector2.md#class-vector2) **get_total_gravity**()

The total gravity vector being currently applied to this body.

---

[float](class_float.md#class-float) **total_linear_damp**

- [float](class_float.md#class-float) **get_total_linear_damp**()

The rate at which the body stops moving, if there are not any other forces moving it.

---

[Transform2D](class_transform2d.md#class-transform2d) **transform**

-  **set_transform**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_transform**()

The body's transformation matrix.

---

## Method Descriptions

 **add_constant_central_force**(force: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Adds a constant directional force without affecting rotation that keeps being applied over time until cleared with `constant_force = Vector2(0, 0)`.

This is equivalent to using add_constant_force() at the body's center of mass.

---

 **add_constant_force**(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Adds a constant positioned force to the body that keeps being applied over time until cleared with `constant_force = Vector2(0, 0)`.

`position` is the offset from the body origin in global coordinates.

---

 **add_constant_torque**(torque: [float](class_float.md#class-float))

Adds a constant rotational force without affecting position that keeps being applied over time until cleared with `constant_torque = 0`.

---

 **apply_central_force**(force: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.

This is equivalent to using apply_force() at the body's center of mass.

---

 **apply_central_impulse**(impulse: [Vector2](class_vector2.md#class-vector2))

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

This is equivalent to using apply_impulse() at the body's center of mass.

---

 **apply_force**(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Applies a positioned force to the body. A force is time dependent and meant to be applied every physics update.

`position` is the offset from the body origin in global coordinates.

---

 **apply_impulse**(impulse: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

`position` is the offset from the body origin in global coordinates.

---

 **apply_torque**(torque: [float](class_float.md#class-float))

Applies a rotational force without affecting position. A force is time dependent and meant to be applied every physics update.

**Note:** inverse_inertia is required for this to work. To have inverse_inertia, an active [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d) must be a child of the node, or you can manually set inverse_inertia.

---

 **apply_torque_impulse**(impulse: [float](class_float.md#class-float))

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

**Note:** inverse_inertia is required for this to work. To have inverse_inertia, an active [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d) must be a child of the node, or you can manually set inverse_inertia.

---

[Vector2](class_vector2.md#class-vector2) **get_constant_force**()

Returns the body's total constant positional forces applied during each physics update.

See add_constant_force() and add_constant_central_force().

---

[float](class_float.md#class-float) **get_constant_torque**()

Returns the body's total constant rotational forces applied during each physics update.

See add_constant_torque().

---

[RID](class_rid.md#class-rid) **get_contact_collider**(contact_idx: [int](class_int.md#class-int))

Returns the collider's [RID](class_rid.md#class-rid).

---

[int](class_int.md#class-int) **get_contact_collider_id**(contact_idx: [int](class_int.md#class-int))

Returns the collider's object id.

---

[Object](class_object.md#class-object) **get_contact_collider_object**(contact_idx: [int](class_int.md#class-int))

Returns the collider object. This depends on how it was created (will return a scene node if such was used to create it).

---

[Vector2](class_vector2.md#class-vector2) **get_contact_collider_position**(contact_idx: [int](class_int.md#class-int))

Returns the position of the contact point on the collider in the global coordinate system.

---

[int](class_int.md#class-int) **get_contact_collider_shape**(contact_idx: [int](class_int.md#class-int))

Returns the collider's shape index.

---

[Vector2](class_vector2.md#class-vector2) **get_contact_collider_velocity_at_position**(contact_idx: [int](class_int.md#class-int))

Returns the velocity vector at the collider's contact point.

---

[int](class_int.md#class-int) **get_contact_count**()

Returns the number of contacts this body has with other bodies.

**Note:** By default, this returns 0 unless bodies are configured to monitor contacts. See [RigidBody2D.contact_monitor](class_rigidbody2d.md#class-rigidbody2d-property-contact-monitor).

---

[Vector2](class_vector2.md#class-vector2) **get_contact_impulse**(contact_idx: [int](class_int.md#class-int))

Returns the impulse created by the contact.

---

[Vector2](class_vector2.md#class-vector2) **get_contact_local_normal**(contact_idx: [int](class_int.md#class-int))

Returns the local normal at the contact point.

---

[Vector2](class_vector2.md#class-vector2) **get_contact_local_position**(contact_idx: [int](class_int.md#class-int))

Returns the position of the contact point on the body in the global coordinate system.

---

[int](class_int.md#class-int) **get_contact_local_shape**(contact_idx: [int](class_int.md#class-int))

Returns the local shape index of the collision.

---

[Vector2](class_vector2.md#class-vector2) **get_contact_local_velocity_at_position**(contact_idx: [int](class_int.md#class-int))

Returns the velocity vector at the body's contact point.

---

[PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) **get_space_state**()

Returns the current state of the space, useful for queries.

---

[Vector2](class_vector2.md#class-vector2) **get_velocity_at_local_position**(local_position: [Vector2](class_vector2.md#class-vector2))

Returns the body's velocity at the given relative position.

`local_position` is the offset from the body origin in global coordinates.

---

 **integrate_forces**()

Updates the body's linear and angular velocity by applying gravity and damping for the equivalent of one physics tick.

---

 **set_constant_force**(force: [Vector2](class_vector2.md#class-vector2))

Sets the body's total constant positional forces applied during each physics update.

See add_constant_force() and add_constant_central_force().

---

 **set_constant_torque**(torque: [float](class_float.md#class-float))

Sets the body's total constant rotational forces applied during each physics update.

See add_constant_torque().
