# PhysicsDirectBodyState2DExtension

**Inherits:** [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d) implementations.

## Description

This class extends [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d).

## Methods

|                                                                                                 | \_add_constant_central_force(force: [Vector2](class_vector2.md#class-vector2))                                      |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                 | \_add_constant_force(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2)) |
|                                                                                                 | \_add_constant_torque(torque: [float](class_float.md#class-float))                                                         |
|                                                                                                 | \_apply_central_force(force: [Vector2](class_vector2.md#class-vector2))                                                    |
|                                                                                                 | \_apply_central_impulse(impulse: [Vector2](class_vector2.md#class-vector2))                                              |
|                                                                                                 | \_apply_force(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))               |
|                                                                                                 | \_apply_impulse(impulse: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))         |
|                                                                                                 | \_apply_torque(torque: [float](class_float.md#class-float))                                                                       |
|                                                                                                 | \_apply_torque_impulse(impulse: [float](class_float.md#class-float))                                                      |
| [float](class_float.md#class-float)                                                             | \_get_angular_velocity()                                                                                                  |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_center_of_mass()                                                                                                      |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_center_of_mass_local()                                                                                          |
| [int](class_int.md#class-int)                                                                   | \_get_collision_layer()                                                                                                    |
| [int](class_int.md#class-int)                                                                   | \_get_collision_mask()                                                                                                      |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_constant_force()                                                                                                      |
| [float](class_float.md#class-float)                                                             | \_get_constant_torque()                                                                                                    |
| [RID](class_rid.md#class-rid)                                                                   | \_get_contact_collider(contact_idx: [int](class_int.md#class-int))                                                        |
| [int](class_int.md#class-int)                                                                   | \_get_contact_collider_id(contact_idx: [int](class_int.md#class-int))                                                  |
| [Object](class_object.md#class-object)                                                          | \_get_contact_collider_object(contact_idx: [int](class_int.md#class-int))                                          |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_contact_collider_position(contact_idx: [int](class_int.md#class-int))                                      |
| [int](class_int.md#class-int)                                                                   | \_get_contact_collider_shape(contact_idx: [int](class_int.md#class-int))                                            |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_contact_collider_velocity_at_position(contact_idx: [int](class_int.md#class-int))              |
| [int](class_int.md#class-int)                                                                   | \_get_contact_count()                                                                                                        |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_contact_impulse(contact_idx: [int](class_int.md#class-int))                                                          |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_contact_local_normal(contact_idx: [int](class_int.md#class-int))                                                |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_contact_local_position(contact_idx: [int](class_int.md#class-int))                                            |
| [int](class_int.md#class-int)                                                                   | \_get_contact_local_shape(contact_idx: [int](class_int.md#class-int))                                                  |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_contact_local_velocity_at_position(contact_idx: [int](class_int.md#class-int))                    |
| [float](class_float.md#class-float)                                                             | \_get_inverse_inertia()                                                                                                    |
| [float](class_float.md#class-float)                                                             | \_get_inverse_mass()                                                                                                          |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_linear_velocity()                                                                                                    |
| [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) | \_get_space_state()                                                                                                            |
| [float](class_float.md#class-float)                                                             | \_get_step()                                                                                                                          |
| [float](class_float.md#class-float)                                                             | \_get_total_angular_damp()                                                                                              |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_total_gravity()                                                                                                        |
| [float](class_float.md#class-float)                                                             | \_get_total_linear_damp()                                                                                                |
| [Transform2D](class_transform2d.md#class-transform2d)                                           | \_get_transform()                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_get_velocity_at_local_position(local_position: [Vector2](class_vector2.md#class-vector2))                     |
|                                                                                                 | \_integrate_forces()                                                                                                          |
| [bool](class_bool.md#class-bool)                                                                | \_is_sleeping()                                                                                                                    |
|                                                                                                 | \_set_angular_velocity(velocity: [float](class_float.md#class-float))                                                     |
|                                                                                                 | \_set_collision_layer(layer: [int](class_int.md#class-int))                                                                |
|                                                                                                 | \_set_collision_mask(mask: [int](class_int.md#class-int))                                                                   |
|                                                                                                 | \_set_constant_force(force: [Vector2](class_vector2.md#class-vector2))                                                      |
|                                                                                                 | \_set_constant_torque(torque: [float](class_float.md#class-float))                                                         |
|                                                                                                 | \_set_linear_velocity(velocity: [Vector2](class_vector2.md#class-vector2))                                                 |
|                                                                                                 | \_set_sleep_state(enabled: [bool](class_bool.md#class-bool))                                                                   |
|                                                                                                 | \_set_transform(transform: [Transform2D](class_transform2d.md#class-transform2d))                                                |

---

## Method Descriptions

 **\_add_constant_central_force**(force: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsDirectBodyState2D.add_constant_central_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-add-constant-central-force).

---

 **\_add_constant_force**(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsDirectBodyState2D.add_constant_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-add-constant-force).

---

 **\_add_constant_torque**(torque: [float](class_float.md#class-float))

Overridable version of [PhysicsDirectBodyState2D.add_constant_torque()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-add-constant-torque).

---

 **\_apply_central_force**(force: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsDirectBodyState2D.apply_central_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-central-force).

---

 **\_apply_central_impulse**(impulse: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsDirectBodyState2D.apply_central_impulse()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-central-impulse).

---

 **\_apply_force**(force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsDirectBodyState2D.apply_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-force).

---

 **\_apply_impulse**(impulse: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsDirectBodyState2D.apply_impulse()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-impulse).

---

 **\_apply_torque**(torque: [float](class_float.md#class-float))

Overridable version of [PhysicsDirectBodyState2D.apply_torque()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-torque).

---

 **\_apply_torque_impulse**(impulse: [float](class_float.md#class-float))

Overridable version of [PhysicsDirectBodyState2D.apply_torque_impulse()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-apply-torque-impulse).

---

[float](class_float.md#class-float) **\_get_angular_velocity**()

Implement to override the behavior of [PhysicsDirectBodyState2D.angular_velocity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-angular-velocity) and its respective getter.

---

[Vector2](class_vector2.md#class-vector2) **\_get_center_of_mass**()

Implement to override the behavior of [PhysicsDirectBodyState2D.center_of_mass](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-center-of-mass) and its respective getter.

---

[Vector2](class_vector2.md#class-vector2) **\_get_center_of_mass_local**()

Implement to override the behavior of [PhysicsDirectBodyState2D.center_of_mass_local](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-center-of-mass-local) and its respective getter.

---

[int](class_int.md#class-int) **\_get_collision_layer**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_get_collision_mask**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector2](class_vector2.md#class-vector2) **\_get_constant_force**()

Overridable version of [PhysicsDirectBodyState2D.get_constant_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-constant-force).

---

[float](class_float.md#class-float) **\_get_constant_torque**()

Overridable version of [PhysicsDirectBodyState2D.get_constant_torque()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-constant-torque).

---

[RID](class_rid.md#class-rid) **\_get_contact_collider**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider).

---

[int](class_int.md#class-int) **\_get_contact_collider_id**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_id()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-id).

---

[Object](class_object.md#class-object) **\_get_contact_collider_object**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_object()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-object).

---

[Vector2](class_vector2.md#class-vector2) **\_get_contact_collider_position**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-position).

---

[int](class_int.md#class-int) **\_get_contact_collider_shape**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_shape()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-shape).

---

[Vector2](class_vector2.md#class-vector2) **\_get_contact_collider_velocity_at_position**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_collider_velocity_at_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-collider-velocity-at-position).

---

[int](class_int.md#class-int) **\_get_contact_count**()

Overridable version of [PhysicsDirectBodyState2D.get_contact_count()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-count).

---

[Vector2](class_vector2.md#class-vector2) **\_get_contact_impulse**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_impulse()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-impulse).

---

[Vector2](class_vector2.md#class-vector2) **\_get_contact_local_normal**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_local_normal()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-local-normal).

---

[Vector2](class_vector2.md#class-vector2) **\_get_contact_local_position**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_local_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-local-position).

---

[int](class_int.md#class-int) **\_get_contact_local_shape**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_local_shape()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-local-shape).

---

[Vector2](class_vector2.md#class-vector2) **\_get_contact_local_velocity_at_position**(contact_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsDirectBodyState2D.get_contact_local_velocity_at_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-contact-local-velocity-at-position).

---

[float](class_float.md#class-float) **\_get_inverse_inertia**()

Implement to override the behavior of [PhysicsDirectBodyState2D.inverse_inertia](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-inverse-inertia) and its respective getter.

---

[float](class_float.md#class-float) **\_get_inverse_mass**()

Implement to override the behavior of [PhysicsDirectBodyState2D.inverse_mass](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-inverse-mass) and its respective getter.

---

[Vector2](class_vector2.md#class-vector2) **\_get_linear_velocity**()

Implement to override the behavior of [PhysicsDirectBodyState2D.linear_velocity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-linear-velocity) and its respective getter.

---

[PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) **\_get_space_state**()

Overridable version of [PhysicsDirectBodyState2D.get_space_state()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-space-state).

---

[float](class_float.md#class-float) **\_get_step**()

Implement to override the behavior of [PhysicsDirectBodyState2D.step](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-step) and its respective getter.

---

[float](class_float.md#class-float) **\_get_total_angular_damp**()

Implement to override the behavior of [PhysicsDirectBodyState2D.total_angular_damp](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-total-angular-damp) and its respective getter.

---

[Vector2](class_vector2.md#class-vector2) **\_get_total_gravity**()

Implement to override the behavior of [PhysicsDirectBodyState2D.total_gravity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-total-gravity) and its respective getter.

---

[float](class_float.md#class-float) **\_get_total_linear_damp**()

Implement to override the behavior of [PhysicsDirectBodyState2D.total_linear_damp](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-total-linear-damp) and its respective getter.

---

[Transform2D](class_transform2d.md#class-transform2d) **\_get_transform**()

Implement to override the behavior of [PhysicsDirectBodyState2D.transform](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-transform) and its respective getter.

---

[Vector2](class_vector2.md#class-vector2) **\_get_velocity_at_local_position**(local_position: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsDirectBodyState2D.get_velocity_at_local_position()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-get-velocity-at-local-position).

---

 **\_integrate_forces**()

Overridable version of [PhysicsDirectBodyState2D.integrate_forces()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-integrate-forces).

---

[bool](class_bool.md#class-bool) **\_is_sleeping**()

Implement to override the behavior of [PhysicsDirectBodyState2D.sleeping](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-sleeping) and its respective getter.

---

 **\_set_angular_velocity**(velocity: [float](class_float.md#class-float))

Implement to override the behavior of [PhysicsDirectBodyState2D.angular_velocity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-angular-velocity) and its respective setter.

---

 **\_set_collision_layer**(layer: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_collision_mask**(mask: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_constant_force**(force: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsDirectBodyState2D.set_constant_force()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-set-constant-force).

---

 **\_set_constant_torque**(torque: [float](class_float.md#class-float))

Overridable version of [PhysicsDirectBodyState2D.set_constant_torque()](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-method-set-constant-torque).

---

 **\_set_linear_velocity**(velocity: [Vector2](class_vector2.md#class-vector2))

Implement to override the behavior of [PhysicsDirectBodyState2D.linear_velocity](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-linear-velocity) and its respective setter.

---

 **\_set_sleep_state**(enabled: [bool](class_bool.md#class-bool))

Implement to override the behavior of [PhysicsDirectBodyState2D.sleeping](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-sleeping) and its respective setter.

---

 **\_set_transform**(transform: [Transform2D](class_transform2d.md#class-transform2d))

Implement to override the behavior of [PhysicsDirectBodyState2D.transform](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d-property-transform) and its respective setter.
