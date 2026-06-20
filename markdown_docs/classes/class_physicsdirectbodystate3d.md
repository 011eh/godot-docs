# PhysicsDirectBodyState3D

**Inherits:** [Object](class_object.md#class-object)

**Inherited By:** [PhysicsDirectBodyState3DExtension](class_physicsdirectbodystate3dextension.md#class-physicsdirectbodystate3dextension)

Provides direct access to a physics body in the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d).

## Description

Provides direct access to a physics body in the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d), allowing safe changes to physics properties. This object is passed via the direct state callback of [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d), and is intended for changing the direct state of that body. See [RigidBody3D._integrate_forces()](class_rigidbody3d.md#class-rigidbody3d-private-method-integrate-forces).

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [Ray-casting](../tutorials/physics/ray-casting.md)

## Properties

| [Vector3](class_vector3.md#class-vector3)             | angular_velocity             |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [Vector3](class_vector3.md#class-vector3)             | center_of_mass                 |
| [Vector3](class_vector3.md#class-vector3)             | center_of_mass_local     |
| [int](class_int.md#class-int)                         | collision_layer               |
| [int](class_int.md#class-int)                         | collision_mask                 |
| [Vector3](class_vector3.md#class-vector3)             | inverse_inertia               |
| [Basis](class_basis.md#class-basis)                   | inverse_inertia_tensor |
| [float](class_float.md#class-float)                   | inverse_mass                     |
| [Vector3](class_vector3.md#class-vector3)             | linear_velocity               |
| [Basis](class_basis.md#class-basis)                   | principal_inertia_axes |
| [bool](class_bool.md#class-bool)                      | sleeping                             |
| [float](class_float.md#class-float)                   | step                                     |
| [float](class_float.md#class-float)                   | total_angular_damp         |
| [Vector3](class_vector3.md#class-vector3)             | total_gravity                   |
| [float](class_float.md#class-float)                   | total_linear_damp           |
| [Transform3D](class_transform3d.md#class-transform3d) | transform                           |

## Methods

|                                                                                                 | add_constant_central_force(force: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))                                      |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                 | add_constant_force(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0)) |
|                                                                                                 | add_constant_torque(torque: [Vector3](class_vector3.md#class-vector3))                                                                      |
|                                                                                                 | apply_central_force(force: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))                                                    |
|                                                                                                 | apply_central_impulse(impulse: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))                                              |
|                                                                                                 | apply_force(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))               |
|                                                                                                 | apply_impulse(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))         |
|                                                                                                 | apply_torque(torque: [Vector3](class_vector3.md#class-vector3))                                                                                    |
|                                                                                                 | apply_torque_impulse(impulse: [Vector3](class_vector3.md#class-vector3))                                                                   |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_constant_force()                                                                                                                         |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_constant_torque()                                                                                                                       |
| [RID](class_rid.md#class-rid)                                                                   | get_contact_collider(contact_idx: [int](class_int.md#class-int))                                                                           |
| [int](class_int.md#class-int)                                                                   | get_contact_collider_id(contact_idx: [int](class_int.md#class-int))                                                                     |
| [Object](class_object.md#class-object)                                                          | get_contact_collider_object(contact_idx: [int](class_int.md#class-int))                                                             |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_contact_collider_position(contact_idx: [int](class_int.md#class-int))                                                         |
| [int](class_int.md#class-int)                                                                   | get_contact_collider_shape(contact_idx: [int](class_int.md#class-int))                                                               |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_contact_collider_velocity_at_position(contact_idx: [int](class_int.md#class-int))                                 |
| [int](class_int.md#class-int)                                                                   | get_contact_count()                                                                                                                           |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_contact_impulse(contact_idx: [int](class_int.md#class-int))                                                                             |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_contact_local_normal(contact_idx: [int](class_int.md#class-int))                                                                   |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_contact_local_position(contact_idx: [int](class_int.md#class-int))                                                               |
| [int](class_int.md#class-int)                                                                   | get_contact_local_shape(contact_idx: [int](class_int.md#class-int))                                                                     |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_contact_local_velocity_at_position(contact_idx: [int](class_int.md#class-int))                                       |
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) | get_space_state()                                                                                                                               |
| [Vector3](class_vector3.md#class-vector3)                                                       | get_velocity_at_local_position(local_position: [Vector3](class_vector3.md#class-vector3))                                        |
|                                                                                                 | integrate_forces()                                                                                                                             |
|                                                                                                 | set_constant_force(force: [Vector3](class_vector3.md#class-vector3))                                                                         |
|                                                                                                 | set_constant_torque(torque: [Vector3](class_vector3.md#class-vector3))                                                                      |

---

## Property Descriptions

[Vector3](class_vector3.md#class-vector3) **angular_velocity**

-  **set_angular_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_angular_velocity**()

The body's rotational velocity in *radians* per second.

---

[Vector3](class_vector3.md#class-vector3) **center_of_mass**

- [Vector3](class_vector3.md#class-vector3) **get_center_of_mass**()

The body's center of mass position relative to the body's center in the global coordinate system.

---

[Vector3](class_vector3.md#class-vector3) **center_of_mass_local**

- [Vector3](class_vector3.md#class-vector3) **get_center_of_mass_local**()

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

[Vector3](class_vector3.md#class-vector3) **inverse_inertia**

- [Vector3](class_vector3.md#class-vector3) **get_inverse_inertia**()

The inverse of the inertia of the body.

---

[Basis](class_basis.md#class-basis) **inverse_inertia_tensor**

- [Basis](class_basis.md#class-basis) **get_inverse_inertia_tensor**()

The inverse of the inertia tensor of the body.

---

[float](class_float.md#class-float) **inverse_mass**

- [float](class_float.md#class-float) **get_inverse_mass**()

The inverse of the mass of the body.

---

[Vector3](class_vector3.md#class-vector3) **linear_velocity**

-  **set_linear_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_linear_velocity**()

The body's linear velocity in units per second.

---

[Basis](class_basis.md#class-basis) **principal_inertia_axes**

- [Basis](class_basis.md#class-basis) **get_principal_inertia_axes**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

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

[Vector3](class_vector3.md#class-vector3) **total_gravity**

- [Vector3](class_vector3.md#class-vector3) **get_total_gravity**()

The total gravity vector being currently applied to this body.

---

[float](class_float.md#class-float) **total_linear_damp**

- [float](class_float.md#class-float) **get_total_linear_damp**()

The rate at which the body stops moving, if there are not any other forces moving it.

---

[Transform3D](class_transform3d.md#class-transform3d) **transform**

-  **set_transform**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_transform**()

The body's transformation matrix.

---

## Method Descriptions

 **add_constant_central_force**(force: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))

Adds a constant directional force without affecting rotation that keeps being applied over time until cleared with `constant_force = Vector3(0, 0, 0)`.

This is equivalent to using add_constant_force() at the body's center of mass.

---

 **add_constant_force**(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))

Adds a constant positioned force to the body that keeps being applied over time until cleared with `constant_force = Vector3(0, 0, 0)`.

`position` is the offset from the body origin in global coordinates.

---

 **add_constant_torque**(torque: [Vector3](class_vector3.md#class-vector3))

Adds a constant rotational force without affecting position that keeps being applied over time until cleared with `constant_torque = Vector3(0, 0, 0)`.

---

 **apply_central_force**(force: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))

Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.

This is equivalent to using apply_force() at the body's center of mass.

---

 **apply_central_impulse**(impulse: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

This is equivalent to using apply_impulse() at the body's center of mass.

---

 **apply_force**(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))

Applies a positioned force to the body. A force is time dependent and meant to be applied every physics update.

`position` is the offset from the body origin in global coordinates.

---

 **apply_impulse**(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

`position` is the offset from the body origin in global coordinates.

---

 **apply_torque**(torque: [Vector3](class_vector3.md#class-vector3))

Applies a rotational force without affecting position. A force is time dependent and meant to be applied every physics update.

**Note:** inverse_inertia is required for this to work. To have inverse_inertia, an active [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) must be a child of the node, or you can manually set inverse_inertia.

---

 **apply_torque_impulse**(impulse: [Vector3](class_vector3.md#class-vector3))

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

**Note:** inverse_inertia is required for this to work. To have inverse_inertia, an active [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) must be a child of the node, or you can manually set inverse_inertia.

---

[Vector3](class_vector3.md#class-vector3) **get_constant_force**()

Returns the body's total constant positional forces applied during each physics update.

See add_constant_force() and add_constant_central_force().

---

[Vector3](class_vector3.md#class-vector3) **get_constant_torque**()

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

Returns the collider object.

---

[Vector3](class_vector3.md#class-vector3) **get_contact_collider_position**(contact_idx: [int](class_int.md#class-int))

Returns the position of the contact point on the collider in the global coordinate system.

---

[int](class_int.md#class-int) **get_contact_collider_shape**(contact_idx: [int](class_int.md#class-int))

Returns the collider's shape index.

---

[Vector3](class_vector3.md#class-vector3) **get_contact_collider_velocity_at_position**(contact_idx: [int](class_int.md#class-int))

Returns the linear velocity vector at the collider's contact point.

---

[int](class_int.md#class-int) **get_contact_count**()

Returns the number of contacts this body has with other bodies.

**Note:** By default, this returns 0 unless bodies are configured to monitor contacts. See [RigidBody3D.contact_monitor](class_rigidbody3d.md#class-rigidbody3d-property-contact-monitor).

---

[Vector3](class_vector3.md#class-vector3) **get_contact_impulse**(contact_idx: [int](class_int.md#class-int))

Impulse created by the contact.

---

[Vector3](class_vector3.md#class-vector3) **get_contact_local_normal**(contact_idx: [int](class_int.md#class-int))

Returns the local normal at the contact point.

---

[Vector3](class_vector3.md#class-vector3) **get_contact_local_position**(contact_idx: [int](class_int.md#class-int))

Returns the position of the contact point on the body in the global coordinate system.

---

[int](class_int.md#class-int) **get_contact_local_shape**(contact_idx: [int](class_int.md#class-int))

Returns the local shape index of the collision.

---

[Vector3](class_vector3.md#class-vector3) **get_contact_local_velocity_at_position**(contact_idx: [int](class_int.md#class-int))

Returns the linear velocity vector at the body's contact point.

---

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **get_space_state**()

Returns the current state of the space, useful for queries.

---

[Vector3](class_vector3.md#class-vector3) **get_velocity_at_local_position**(local_position: [Vector3](class_vector3.md#class-vector3))

Returns the body's velocity at the given relative position.

`local_position` is the offset from the body origin in global coordinates.

---

 **integrate_forces**()

Updates the body's linear and angular velocity by applying gravity and damping for the equivalent of one physics tick.

---

 **set_constant_force**(force: [Vector3](class_vector3.md#class-vector3))

Sets the body's total constant positional forces applied during each physics update.

See add_constant_force() and add_constant_central_force().

---

 **set_constant_torque**(torque: [Vector3](class_vector3.md#class-vector3))

Sets the body's total constant rotational forces applied during each physics update.

See add_constant_torque().
