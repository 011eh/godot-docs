# RigidBody3D

**Inherits:** [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) **<** [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [VehicleBody3D](class_vehiclebody3d.md#class-vehiclebody3d)

A 3D physics body that is moved by a physics simulation.

## Description

**RigidBody3D** implements full 3D physics. It cannot be controlled directly, instead, you must apply forces to it (gravity, impulses, etc.), and the physics simulation will calculate the resulting movement, rotation, react to collisions, and affect other physics bodies in its path.

The body's behavior can be adjusted via lock_rotation, freeze, and freeze_mode. By changing various properties of the object, such as mass, you can control how the physics simulation acts on it.

A rigid body will always maintain its shape and size, even when forces are applied to it. It is useful for objects that can be interacted with in an environment, such as a tree that can be knocked over or a stack of crates that can be pushed around.

If you need to directly affect the body, prefer \_integrate_forces() as it allows you to directly access the physics state.

If you need to override the default physics behavior, you can write a custom force integration function. See custom_integrator.

**Note:** Changing the 3D transform or linear_velocity of a **RigidBody3D** very often may lead to some unpredictable behaviors. This also happens when a **RigidBody3D** is the descendant of a constantly moving node, like another **RigidBody3D**, as that will cause its global transform to be set whenever its ancestor moves.

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)
- [3D Truck Town Demo](https://godotengine.org/asset-library/asset/2752)
- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)

## Properties

| [float](class_float.md#class-float)                               | angular_damp                           | `0.0`              |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------|
| DampMode                            | angular_damp_mode                 | `0`                |
| [Vector3](class_vector3.md#class-vector3)                         | angular_velocity                   | `Vector3(0, 0, 0)` |
| [bool](class_bool.md#class-bool)                                  | can_sleep                                 | `true`             |
| [Vector3](class_vector3.md#class-vector3)                         | center_of_mass                       | `Vector3(0, 0, 0)` |
| CenterOfMassMode            | center_of_mass_mode             | `0`                |
| [Vector3](class_vector3.md#class-vector3)                         | constant_force                       | `Vector3(0, 0, 0)` |
| [Vector3](class_vector3.md#class-vector3)                         | constant_torque                     | `Vector3(0, 0, 0)` |
| [bool](class_bool.md#class-bool)                                  | contact_monitor                     | `false`            |
| [bool](class_bool.md#class-bool)                                  | continuous_cd                         | `false`            |
| [bool](class_bool.md#class-bool)                                  | custom_integrator                 | `false`            |
| [bool](class_bool.md#class-bool)                                  | freeze                                       | `false`            |
| FreezeMode                        | freeze_mode                             | `0`                |
| [float](class_float.md#class-float)                               | gravity_scale                         | `1.0`              |
| [Vector3](class_vector3.md#class-vector3)                         | inertia                                     | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float)                               | linear_damp                             | `0.0`              |
| DampMode                            | linear_damp_mode                   | `0`                |
| [Vector3](class_vector3.md#class-vector3)                         | linear_velocity                     | `Vector3(0, 0, 0)` |
| [bool](class_bool.md#class-bool)                                  | lock_rotation                         | `false`            |
| [float](class_float.md#class-float)                               | mass                                           | `1.0`              |
| [int](class_int.md#class-int)                                     | max_contacts_reported         | `0`                |
| [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial) | physics_material_override |                    |
| [bool](class_bool.md#class-bool)                                  | sleeping                                   | `false`            |

## Methods

|                                                                             | \_integrate_forces(state: [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d))                |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                             | add_constant_central_force(force: [Vector3](class_vector3.md#class-vector3))                                                         |
|                                                                             | add_constant_force(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0)) |
|                                                                             | add_constant_torque(torque: [Vector3](class_vector3.md#class-vector3))                                                                      |
|                                                                             | apply_central_force(force: [Vector3](class_vector3.md#class-vector3))                                                                       |
|                                                                             | apply_central_impulse(impulse: [Vector3](class_vector3.md#class-vector3))                                                                 |
|                                                                             | apply_force(force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))               |
|                                                                             | apply_impulse(impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 0, 0))         |
|                                                                             | apply_torque(torque: [Vector3](class_vector3.md#class-vector3))                                                                                    |
|                                                                             | apply_torque_impulse(impulse: [Vector3](class_vector3.md#class-vector3))                                                                   |
| [Array](class_array.md#class-array)[[Node3D](class_node3d.md#class-node3d)] | get_colliding_bodies()                                                                                                                     |
| [int](class_int.md#class-int)                                               | get_contact_count()                                                                                                                           |
| [Basis](class_basis.md#class-basis)                                         | get_inverse_inertia_tensor()                                                                                                         |
|                                                                             | set_axis_velocity(axis_velocity: [Vector3](class_vector3.md#class-vector3))                                                                   |

---

## Signals

**body_entered**(body: [Node](class_node.md#class-node))

Emitted when a collision with another [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap) occurs. Requires contact_monitor to be set to `true` and max_contacts_reported to be set high enough to detect all the collisions. [GridMap](class_gridmap.md#class-gridmap)s are detected if the [MeshLibrary](class_meshlibrary.md#class-meshlibrary) has Collision [Shape3D](class_shape3d.md#class-shape3d)s.

`body` the [Node](class_node.md#class-node), if it exists in the tree, of the other [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap).

---

**body_exited**(body: [Node](class_node.md#class-node))

Emitted when the collision with another [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap) ends. Requires contact_monitor to be set to `true` and max_contacts_reported to be set high enough to detect all the collisions. [GridMap](class_gridmap.md#class-gridmap)s are detected if the [MeshLibrary](class_meshlibrary.md#class-meshlibrary) has Collision [Shape3D](class_shape3d.md#class-shape3d)s.

`body` the [Node](class_node.md#class-node), if it exists in the tree, of the other [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap).

---

**body_shape_entered**(body_rid: [RID](class_rid.md#class-rid), body: [Node](class_node.md#class-node), body_shape_index: [int](class_int.md#class-int), local_shape_index: [int](class_int.md#class-int))

Emitted when one of this RigidBody3D's [Shape3D](class_shape3d.md#class-shape3d)s collides with another [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap)'s [Shape3D](class_shape3d.md#class-shape3d)s. Requires contact_monitor to be set to `true` and max_contacts_reported to be set high enough to detect all the collisions. [GridMap](class_gridmap.md#class-gridmap)s are detected if the [MeshLibrary](class_meshlibrary.md#class-meshlibrary) has Collision [Shape3D](class_shape3d.md#class-shape3d)s.

`body_rid` the [RID](class_rid.md#class-rid) of the other [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [MeshLibrary](class_meshlibrary.md#class-meshlibrary)'s [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d).

`body` the [Node](class_node.md#class-node), if it exists in the tree, of the other [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap).

`body_shape_index` the index of the [Shape3D](class_shape3d.md#class-shape3d) of the other [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d). Get the [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) node with `body.shape_owner_get_owner(body.shape_find_owner(body_shape_index))`.

`local_shape_index` the index of the [Shape3D](class_shape3d.md#class-shape3d) of this RigidBody3D used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d). Get the [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) node with `self.shape_owner_get_owner(self.shape_find_owner(local_shape_index))`.

---

**body_shape_exited**(body_rid: [RID](class_rid.md#class-rid), body: [Node](class_node.md#class-node), body_shape_index: [int](class_int.md#class-int), local_shape_index: [int](class_int.md#class-int))

Emitted when the collision between one of this RigidBody3D's [Shape3D](class_shape3d.md#class-shape3d)s and another [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap)'s [Shape3D](class_shape3d.md#class-shape3d)s ends. Requires contact_monitor to be set to `true` and max_contacts_reported to be set high enough to detect all the collisions. [GridMap](class_gridmap.md#class-gridmap)s are detected if the [MeshLibrary](class_meshlibrary.md#class-meshlibrary) has Collision [Shape3D](class_shape3d.md#class-shape3d)s.

`body_rid` the [RID](class_rid.md#class-rid) of the other [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [MeshLibrary](class_meshlibrary.md#class-meshlibrary)'s [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d). [GridMap](class_gridmap.md#class-gridmap)s are detected if the Meshes have [Shape3D](class_shape3d.md#class-shape3d)s.

`body` the [Node](class_node.md#class-node), if it exists in the tree, of the other [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap).

`body_shape_index` the index of the [Shape3D](class_shape3d.md#class-shape3d) of the other [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) or [GridMap](class_gridmap.md#class-gridmap) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d). Get the [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) node with `body.shape_owner_get_owner(body.shape_find_owner(body_shape_index))`.

`local_shape_index` the index of the [Shape3D](class_shape3d.md#class-shape3d) of this RigidBody3D used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d). Get the [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) node with `self.shape_owner_get_owner(self.shape_find_owner(local_shape_index))`.

---

**sleeping_state_changed**()

Emitted when the physics engine changes the body's sleeping state.

**Note:** Changing the value sleeping will not trigger this signal. It is only emitted if the sleeping state is changed by the physics engine or `emit_signal("sleeping_state_changed")` is used.

---

## Enumerations

enum **FreezeMode**:

FreezeMode **FREEZE_MODE_STATIC** = `0`

Static body freeze mode (default). The body is not affected by gravity and forces. It can be only moved by user code and doesn't collide with other bodies along its path.

FreezeMode **FREEZE_MODE_KINEMATIC** = `1`

Kinematic body freeze mode. Similar to FREEZE_MODE_STATIC, but collides with other bodies along its path when moved. Useful for a frozen body that needs to be animated.

---

enum **CenterOfMassMode**:

CenterOfMassMode **CENTER_OF_MASS_MODE_AUTO** = `0`

In this mode, the body's center of mass is calculated automatically based on its shapes. This assumes that the shapes' origins are also their center of mass.

CenterOfMassMode **CENTER_OF_MASS_MODE_CUSTOM** = `1`

In this mode, the body's center of mass is set through center_of_mass. Defaults to the body's origin position.

---

enum **DampMode**:

DampMode **DAMP_MODE_COMBINE** = `0`

In this mode, the body's damping value is added to any value set in areas or the default value.

DampMode **DAMP_MODE_REPLACE** = `1`

In this mode, the body's damping value replaces any value set in areas or the default value.

---

## Property Descriptions

[float](class_float.md#class-float) **angular_damp** = `0.0`

-  **set_angular_damp**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_angular_damp**()

Damps the body's rotation. By default, the body will use the [ProjectSettings.physics/3d/default_angular_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-angular-damp) project setting or any value override set by an [Area3D](class_area3d.md#class-area3d) the body is in. Depending on angular_damp_mode, you can set angular_damp to be added to or to replace the body's damping value.

See [ProjectSettings.physics/3d/default_angular_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-angular-damp) for more details about damping.

---

DampMode **angular_damp_mode** = `0`

-  **set_angular_damp_mode**(value: DampMode)
- DampMode **get_angular_damp_mode**()

Defines how angular_damp is applied.

---

[Vector3](class_vector3.md#class-vector3) **angular_velocity** = `Vector3(0, 0, 0)`

-  **set_angular_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_angular_velocity**()

The RigidBody3D's rotational velocity in *radians* per second.

---

[bool](class_bool.md#class-bool) **can_sleep** = `true`

-  **set_can_sleep**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_able_to_sleep**()

If `true`, the body can enter sleep mode when there is no movement. See sleeping.

---

[Vector3](class_vector3.md#class-vector3) **center_of_mass** = `Vector3(0, 0, 0)`

-  **set_center_of_mass**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_center_of_mass**()

The body's custom center of mass, relative to the body's origin position, when center_of_mass_mode is set to CENTER_OF_MASS_MODE_CUSTOM. This is the balanced point of the body, where applied forces only cause linear acceleration. Applying forces outside of the center of mass causes angular acceleration.

When center_of_mass_mode is set to CENTER_OF_MASS_MODE_AUTO (default value), the center of mass is automatically determined, but this does not update the value of center_of_mass.

---

CenterOfMassMode **center_of_mass_mode** = `0`

-  **set_center_of_mass_mode**(value: CenterOfMassMode)
- CenterOfMassMode **get_center_of_mass_mode**()

Defines the way the body's center of mass is set.

---

[Vector3](class_vector3.md#class-vector3) **constant_force** = `Vector3(0, 0, 0)`

-  **set_constant_force**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_constant_force**()

The body's total constant positional forces applied during each physics update.

See add_constant_force() and add_constant_central_force().

---

[Vector3](class_vector3.md#class-vector3) **constant_torque** = `Vector3(0, 0, 0)`

-  **set_constant_torque**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_constant_torque**()

The body's total constant rotational forces applied during each physics update.

See add_constant_torque().

---

[bool](class_bool.md#class-bool) **contact_monitor** = `false`

-  **set_contact_monitor**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_contact_monitor_enabled**()

If `true`, the RigidBody3D will emit signals when it collides with another body.

**Note:** By default the maximum contacts reported is set to 0, meaning nothing will be recorded, see max_contacts_reported.

---

[bool](class_bool.md#class-bool) **continuous_cd** = `false`

-  **set_use_continuous_collision_detection**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_continuous_collision_detection**()

If `true`, continuous collision detection is used.

Continuous collision detection tries to predict where a moving body will collide, instead of moving it and correcting its movement if it collided. Continuous collision detection is more precise, and misses fewer impacts by small, fast-moving objects. Not using continuous collision detection is faster to compute, but can miss small, fast-moving objects.

---

[bool](class_bool.md#class-bool) **custom_integrator** = `false`

-  **set_use_custom_integrator**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_custom_integrator**()

If `true`, the standard force integration (like gravity or damping) will be disabled for this body. Other than collision response, the body will only move as determined by the \_integrate_forces() method, if that virtual method is overridden.

Setting this property will call the method [PhysicsServer3D.body_set_omit_force_integration()](class_physicsserver3d.md#class-physicsserver3d-method-body-set-omit-force-integration) internally.

---

[bool](class_bool.md#class-bool) **freeze** = `false`

-  **set_freeze_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_freeze_enabled**()

If `true`, the body is frozen. Gravity and forces are not applied anymore.

See freeze_mode to set the body's behavior when frozen.

**Note:** For a body that is always frozen, use [StaticBody3D](class_staticbody3d.md#class-staticbody3d) or [AnimatableBody3D](class_animatablebody3d.md#class-animatablebody3d) instead.

---

FreezeMode **freeze_mode** = `0`

-  **set_freeze_mode**(value: FreezeMode)
- FreezeMode **get_freeze_mode**()

The body's freeze mode. Determines the body's behavior when freeze is `true`.

**Note:** For a body that is always frozen, use [StaticBody3D](class_staticbody3d.md#class-staticbody3d) or [AnimatableBody3D](class_animatablebody3d.md#class-animatablebody3d) instead.

---

[float](class_float.md#class-float) **gravity_scale** = `1.0`

-  **set_gravity_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gravity_scale**()

This is multiplied by [ProjectSettings.physics/3d/default_gravity](class_projectsettings.md#class-projectsettings-property-physics-3d-default-gravity) to produce this body's gravity. For example, a value of `1.0` will apply normal gravity, `2.0` will apply double the gravity, and `0.5` will apply half the gravity to this body.

---

[Vector3](class_vector3.md#class-vector3) **inertia** = `Vector3(0, 0, 0)`

-  **set_inertia**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_inertia**()

The body's moment of inertia. This is like mass, but for rotation: it determines how much torque it takes to rotate the body on each axis. The moment of inertia is usually computed automatically from the mass and the shapes, but this property allows you to set a custom value.

If set to [Vector3.ZERO](class_vector3.md#class-vector3-constant-zero), inertia is automatically computed (default value).

**Note:** This value does not change when inertia is automatically computed. Use [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) to get the computed inertia.

GDScript

```gdscript
@onready var ball = $Ball

func get_ball_inertia():
    return PhysicsServer3D.body_get_direct_state(ball.get_rid()).inverse_inertia.inverse()
```

C#

```csharp
private RigidBody3D _ball;

public override void _Ready()
{
    _ball = GetNode<RigidBody3D>("Ball");
}

private Vector3 GetBallInertia()
{
    return PhysicsServer3D.BodyGetDirectState(_ball.GetRid()).InverseInertia.Inverse();
}
```

---

[float](class_float.md#class-float) **linear_damp** = `0.0`

-  **set_linear_damp**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_linear_damp**()

Damps the body's movement. By default, the body will use the [ProjectSettings.physics/3d/default_linear_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-linear-damp) project setting or any value override set by an [Area3D](class_area3d.md#class-area3d) the body is in. Depending on linear_damp_mode, you can set linear_damp to be added to or to replace the body's damping value.

See [ProjectSettings.physics/3d/default_linear_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-linear-damp) for more details about damping.

---

DampMode **linear_damp_mode** = `0`

-  **set_linear_damp_mode**(value: DampMode)
- DampMode **get_linear_damp_mode**()

Defines how linear_damp is applied.

---

[Vector3](class_vector3.md#class-vector3) **linear_velocity** = `Vector3(0, 0, 0)`

-  **set_linear_velocity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_linear_velocity**()

The body's linear velocity in units per second. Can be used sporadically, but **don't set this every frame**, because physics may run in another thread and runs at a different granularity. Use \_integrate_forces() as your process loop for precise control of the body state.

---

[bool](class_bool.md#class-bool) **lock_rotation** = `false`

-  **set_lock_rotation_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_lock_rotation_enabled**()

If `true`, the body cannot rotate. Gravity and forces only apply linear movement.

---

[float](class_float.md#class-float) **mass** = `1.0`

-  **set_mass**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mass**()

The body's mass.

---

[int](class_int.md#class-int) **max_contacts_reported** = `0`

-  **set_max_contacts_reported**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_contacts_reported**()

The maximum number of contacts that will be recorded. Requires a value greater than 0 and contact_monitor to be set to `true` to start to register contacts. Use get_contact_count() to retrieve the count or get_colliding_bodies() to retrieve bodies that have been collided with.

**Note:** The number of contacts is different from the number of collisions. Collisions between parallel edges will result in two contacts (one at each end), and collisions between parallel faces will result in four contacts (one at each corner).

---

[PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial) **physics_material_override**

-  **set_physics_material_override**(value: [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial))
- [PhysicsMaterial](class_physicsmaterial.md#class-physicsmaterial) **get_physics_material_override**()

The physics material override for the body.

If a material is assigned to this property, it will be used instead of any other physics material, such as an inherited one.

---

[bool](class_bool.md#class-bool) **sleeping** = `false`

-  **set_sleeping**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_sleeping**()

If `true`, the body will not move and will not calculate forces until woken up by another body through, for example, a collision, or by using the apply_impulse() or apply_force() methods.

---

## Method Descriptions

 **\_integrate_forces**(state: [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d))

Called during physics processing, allowing you to read and safely modify the simulation state for the object. By default, it is called before the standard force integration, but the custom_integrator property allows you to disable the standard force integration and do fully custom force integration for a body.

---

 **add_constant_central_force**(force: [Vector3](class_vector3.md#class-vector3))

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

 **apply_central_force**(force: [Vector3](class_vector3.md#class-vector3))

Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.

This is equivalent to using apply_force() at the body's center of mass.

---

 **apply_central_impulse**(impulse: [Vector3](class_vector3.md#class-vector3))

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

**Note:** inertia is required for this to work. To have inertia, an active [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) must be a child of the node, or you can manually set inertia.

---

 **apply_torque_impulse**(impulse: [Vector3](class_vector3.md#class-vector3))

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

**Note:** inertia is required for this to work. To have inertia, an active [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) must be a child of the node, or you can manually set inertia.

---

[Array](class_array.md#class-array)[[Node3D](class_node3d.md#class-node3d)] **get_colliding_bodies**()

Returns a list of the bodies colliding with this one. Requires contact_monitor to be set to `true` and max_contacts_reported to be set high enough to detect all the collisions.

**Note:** The result of this test is not immediate after moving objects. For performance, list of collisions is updated once per frame and before the physics step. Consider using signals instead.

---

[int](class_int.md#class-int) **get_contact_count**()

Returns the number of contacts this body has with other bodies. By default, this returns 0 unless bodies are configured to monitor contacts (see contact_monitor).

**Note:** To retrieve the colliding bodies, use get_colliding_bodies().

---

[Basis](class_basis.md#class-basis) **get_inverse_inertia_tensor**()

Returns the inverse inertia tensor basis. This is used to calculate the angular acceleration resulting from a torque applied to the **RigidBody3D**.

---

 **set_axis_velocity**(axis_velocity: [Vector3](class_vector3.md#class-vector3))

Sets an axis velocity. The velocity in the given vector axis will be set as the given vector length. This is useful for jumping behavior.
