# PhysicsDirectBodyState3DExtension

**Inherits:** [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) implementations.

## Description

This class extends [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d).

## Methods

|                                                                                                 | \_add_constant_central_force(force: [Vector3](class_vector3.md#class-vector3))                                      |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                 | \_add_constant_force(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3)) |
|                                                                                                 | \_add_constant_torque(torque: [Vector3](class_vector3.md#class-vector3))                                                   |
|                                                                                                 | \_apply_central_force(force: [Vector3](class_vector3.md#class-vector3))                                                    |
|                                                                                                 | \_apply_central_impulse(impulse: [Vector3](class_vector3.md#class-vector3))                                              |
|                                                                                                 | \_apply_force(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))               |
|                                                                                                 | \_apply_impulse(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))         |
|                                                                                                 | \_apply_torque(torque: [Vector3](class_vector3.md#class-vector3))                                                                 |
|                                                                                                 | \_apply_torque_impulse(impulse: [Vector3](class_vector3.md#class-vector3))                                                |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_angular_velocity()                                                                                                  |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_center_of_mass()                                                                                                      |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_center_of_mass_local()                                                                                          |
| [int](class_int.md#class-int)                                                                   | \_get_collision_layer()                                                                                                    |
| [int](class_int.md#class-int)                                                                   | \_get_collision_mask()                                                                                                      |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_constant_force()                                                                                                      |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_constant_torque()                                                                                                    |
| [RID](class_rid.md#class-rid)                                                                   | \_get_contact_collider(contact_idx: [int](class_int.md#class-int))                                                        |
| [int](class_int.md#class-int)                                                                   | \_get_contact_collider_id(contact_idx: [int](class_int.md#class-int))                                                  |
| [Object](class_object.md#class-object)                                                          | \_get_contact_collider_object(contact_idx: [int](class_int.md#class-int))                                          |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_contact_collider_position(contact_idx: [int](class_int.md#class-int))                                      |
| [int](class_int.md#class-int)                                                                   | \_get_contact_collider_shape(contact_idx: [int](class_int.md#class-int))                                            |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_contact_collider_velocity_at_position(contact_idx: [int](class_int.md#class-int))              |
| [int](class_int.md#class-int)                                                                   | \_get_contact_count()                                                                                                        |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_contact_impulse(contact_idx: [int](class_int.md#class-int))                                                          |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_contact_local_normal(contact_idx: [int](class_int.md#class-int))                                                |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_contact_local_position(contact_idx: [int](class_int.md#class-int))                                            |
| [int](class_int.md#class-int)                                                                   | \_get_contact_local_shape(contact_idx: [int](class_int.md#class-int))                                                  |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_contact_local_velocity_at_position(contact_idx: [int](class_int.md#class-int))                    |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_inverse_inertia()                                                                                                    |
| [Basis](class_basis.md#class-basis)                                                             | \_get_inverse_inertia_tensor()                                                                                      |
| [float](class_float.md#class-float)                                                             | \_get_inverse_mass()                                                                                                          |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_linear_velocity()                                                                                                    |
| [Basis](class_basis.md#class-basis)                                                             | \_get_principal_inertia_axes()                                                                                      |
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) | \_get_space_state()                                                                                                            |
| [float](class_float.md#class-float)                                                             | \_get_step()                                                                                                                          |
| [float](class_float.md#class-float)                                                             | \_get_total_angular_damp()                                                                                              |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_total_gravity()                                                                                                        |
| [float](class_float.md#class-float)                                                             | \_get_total_linear_damp()                                                                                                |
| [Transform3D](class_transform3d.md#class-transform3d)                                           | \_get_transform()                                                                                                                |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_get_velocity_at_local_position(local_position: [Vector3](class_vector3.md#class-vector3))                     |
|                                                                                                 | \_integrate_forces()                                                                                                          |
| [bool](class_bool.md#class-bool)                                                                | \_is_sleeping()                                                                                                                    |
|                                                                                                 | \_set_angular_velocity(velocity: [Vector3](class_vector3.md#class-vector3))                                               |
|                                                                                                 | \_set_collision_layer(layer: [int](class_int.md#class-int))                                                                |
|                                                                                                 | \_set_collision_mask(mask: [int](class_int.md#class-int))                                                                   |
|                                                                                                 | \_set_constant_force(force: [Vector3](class_vector3.md#class-vector3))                                                      |
|                                                                                                 | \_set_constant_torque(torque: [Vector3](class_vector3.md#class-vector3))                                                   |
|                                                                                                 | \_set_linear_velocity(velocity: [Vector3](class_vector3.md#class-vector3))                                                 |
|                                                                                                 | \_set_sleep_state(enabled: [bool](class_bool.md#class-bool))                                                                   |
|                                                                                                 | \_set_transform(transform: [Transform3D](class_transform3d.md#class-transform3d))                                                |

---

## Method Descriptions

 **\_add_constant_central_force**(force: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_add_constant_force**(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_add_constant_torque**(torque: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_apply_central_force**(force: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_apply_central_impulse**(impulse: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_apply_force**(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_apply_impulse**(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_apply_torque**(torque: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_apply_torque_impulse**(impulse: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_angular_velocity**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_center_of_mass**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_center_of_mass_local**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_get_collision_layer**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_get_collision_mask**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_constant_force**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_constant_torque**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_get_contact_collider**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_get_contact_collider_id**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Object](class_object.md#class-object) **\_get_contact_collider_object**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_contact_collider_position**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_get_contact_collider_shape**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_contact_collider_velocity_at_position**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_get_contact_count**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_contact_impulse**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_contact_local_normal**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_contact_local_position**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_get_contact_local_shape**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_contact_local_velocity_at_position**(contact_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_inverse_inertia**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Basis](class_basis.md#class-basis) **\_get_inverse_inertia_tensor**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_get_inverse_mass**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_linear_velocity**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Basis](class_basis.md#class-basis) **\_get_principal_inertia_axes**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **\_get_space_state**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_get_step**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_get_total_angular_damp**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_total_gravity**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_get_total_linear_damp**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Transform3D](class_transform3d.md#class-transform3d) **\_get_transform**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_velocity_at_local_position**(local_position: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_integrate_forces**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_is_sleeping**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_angular_velocity**(velocity: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_collision_layer**(layer: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_collision_mask**(mask: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_constant_force**(force: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_constant_torque**(torque: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_linear_velocity**(velocity: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_sleep_state**(enabled: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_transform**(transform: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
