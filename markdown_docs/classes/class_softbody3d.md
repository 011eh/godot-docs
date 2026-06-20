# SoftBody3D

**Inherits:** [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A deformable 3D physics mesh.

## Description

A deformable 3D physics mesh. Used to create elastic or deformable objects such as cloth, rubber, or other flexible materials.

Additionally, **SoftBody3D** is subject to wind forces defined in [Area3D](class_area3d.md#class-area3d) (see [Area3D.wind_source_path](class_area3d.md#class-area3d-property-wind-source-path), [Area3D.wind_force_magnitude](class_area3d.md#class-area3d-property-wind-force-magnitude), and [Area3D.wind_attenuation_factor](class_area3d.md#class-area3d-property-wind-attenuation-factor)).

**Note:** It's recommended to use Jolt Physics when using **SoftBody3D** instead of the default GodotPhysics3D, as Jolt Physics' soft body implementation is faster and more reliable. You can switch the physics engine using the [ProjectSettings.physics/3d/physics_engine](class_projectsettings.md#class-projectsettings-property-physics-3d-physics-engine) project setting.

## Tutorials

- [SoftBody](../tutorials/physics/soft_body.md)

## Properties

| [int](class_int.md#class-int)                | collision_layer                 | `1`            |
|----------------------------------------------|-------------------------------------------------------------------------------|----------------|
| [int](class_int.md#class-int)                | collision_mask                   | `1`            |
| [float](class_float.md#class-float)          | damping_coefficient         | `0.01`         |
| DisableMode  | disable_mode                       | `0`            |
| [float](class_float.md#class-float)          | drag_coefficient               | `0.0`          |
| [float](class_float.md#class-float)          | linear_stiffness               | `0.5`          |
| [NodePath](class_nodepath.md#class-nodepath) | parent_collision_ignore | `NodePath("")` |
| [float](class_float.md#class-float)          | pressure_coefficient       | `0.0`          |
| [bool](class_bool.md#class-bool)             | ray_pickable                       | `true`         |
| [float](class_float.md#class-float)          | shrinking_factor               | `0.0`          |
| [int](class_int.md#class-int)                | simulation_precision       | `5`            |
| [float](class_float.md#class-float)          | total_mass                           | `1.0`          |

## Methods

|                                                                                                  | add_collision_exception_with(body: [Node](class_node.md#class-node))                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                  | apply_central_force(force: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                            |
|                                                                                                  | apply_central_impulse(impulse: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                      |
|                                                                                                  | apply_force(point_index: [int](class_int.md#class-int), force: [Vector3](class_vector3.md#class-vector3))                                                                                                                                |
|                                                                                                  | apply_impulse(point_index: [int](class_int.md#class-int), impulse: [Vector3](class_vector3.md#class-vector3))                                                                                                                          |
| [Array](class_array.md#class-array)[[PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)] | get_collision_exceptions()                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                                 | get_collision_layer_value(layer_number: [int](class_int.md#class-int))                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                                 | get_collision_mask_value(layer_number: [int](class_int.md#class-int))                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                                                    | get_physics_rid()                                                                                                                                                                                                                    |
| [Vector3](class_vector3.md#class-vector3)                                                        | get_point_transform(point_index: [int](class_int.md#class-int))                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                                 | is_point_pinned(point_index: [int](class_int.md#class-int))                                                                                                                                                                          |
|                                                                                                  | remove_collision_exception_with(body: [Node](class_node.md#class-node))                                                                                                                                              |
|                                                                                                  | set_collision_layer_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))                                                                                                            |
|                                                                                                  | set_collision_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))                                                                                                              |
|                                                                                                  | set_point_pinned(point_index: [int](class_int.md#class-int), pinned: [bool](class_bool.md#class-bool), attachment_path: [NodePath](class_nodepath.md#class-nodepath) = NodePath(""), insert_at: [int](class_int.md#class-int) = -1) |

---

## Enumerations

enum **DisableMode**:

DisableMode **DISABLE_MODE_REMOVE** = `0`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), remove from the physics simulation to stop all physics interactions with this **SoftBody3D**.

Automatically re-added to the physics simulation when the [Node](class_node.md#class-node) is processed again.

DisableMode **DISABLE_MODE_KEEP_ACTIVE** = `1`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), do not affect the physics simulation.

---

## Property Descriptions

[int](class_int.md#class-int) **collision_layer** = `1`

-  **set_collision_layer**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_layer**()

The physics layers this SoftBody3D **is in**. Collision objects can exist in one or more of 32 different layers. See also collision_mask.

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[int](class_int.md#class-int) **collision_mask** = `1`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers this SoftBody3D **scans**. Collision objects can scan one or more of 32 different layers. See also collision_layer.

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[float](class_float.md#class-float) **damping_coefficient** = `0.01`

-  **set_damping_coefficient**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_damping_coefficient**()

The body's damping coefficient. Higher values will slow down the body more noticeably when forces are applied.

---

DisableMode **disable_mode** = `0`

-  **set_disable_mode**(value: DisableMode)
- DisableMode **get_disable_mode**()

Defines the behavior in physics when [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled).

---

[float](class_float.md#class-float) **drag_coefficient** = `0.0`

-  **set_drag_coefficient**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_drag_coefficient**()

The body's drag coefficient. Higher values increase this body's air resistance.

**Note:** This value is currently unused by Godot's default physics implementation.

---

[float](class_float.md#class-float) **linear_stiffness** = `0.5`

-  **set_linear_stiffness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_linear_stiffness**()

Higher values will result in a stiffer body, while lower values will increase the body's ability to bend. The value can be between `0.0` and `1.0` (inclusive).

---

[NodePath](class_nodepath.md#class-nodepath) **parent_collision_ignore** = `NodePath("")`

-  **set_parent_collision_ignore**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_parent_collision_ignore**()

[NodePath](class_nodepath.md#class-nodepath) to a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) this SoftBody3D should avoid clipping.

---

[float](class_float.md#class-float) **pressure_coefficient** = `0.0`

-  **set_pressure_coefficient**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pressure_coefficient**()

The pressure coefficient of this soft body. Simulate pressure build-up from inside this body. Higher values increase the strength of this effect.

---

[bool](class_bool.md#class-bool) **ray_pickable** = `true`

-  **set_ray_pickable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ray_pickable**()

If `true`, the **SoftBody3D** will respond to [RayCast3D](class_raycast3d.md#class-raycast3d)s.

---

[float](class_float.md#class-float) **shrinking_factor** = `0.0`

-  **set_shrinking_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_shrinking_factor**()

Scales the rest lengths of **SoftBody3D**'s edge constraints. Positive values shrink the mesh, while negative values expand it. For example, a value of `0.1` shortens the edges of the mesh by 10%, while `-0.1` expands the edges by 10%.

**Note:** shrinking_factor is best used on surface meshes with pinned points.

---

[int](class_int.md#class-int) **simulation_precision** = `5`

-  **set_simulation_precision**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_simulation_precision**()

Increasing this value will improve the resulting simulation, but can affect performance. Use with care.

---

[float](class_float.md#class-float) **total_mass** = `1.0`

-  **set_total_mass**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_total_mass**()

The SoftBody3D's mass.

---

## Method Descriptions

 **add_collision_exception_with**(body: [Node](class_node.md#class-node))

Adds a body to the list of bodies that this body can't collide with.

---

 **apply_central_force**(force: [Vector3](class_vector3.md#class-vector3))

Distributes and applies a force to all points. A force is time dependent and meant to be applied every physics update.

---

 **apply_central_impulse**(impulse: [Vector3](class_vector3.md#class-vector3))

Distributes and applies an impulse to all points.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

---

 **apply_force**(point_index: [int](class_int.md#class-int), force: [Vector3](class_vector3.md#class-vector3))

Applies a force to a point. A force is time dependent and meant to be applied every physics update.

---

 **apply_impulse**(point_index: [int](class_int.md#class-int), impulse: [Vector3](class_vector3.md#class-vector3))

Applies an impulse to a point.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

---

[Array](class_array.md#class-array)[[PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)] **get_collision_exceptions**()

Returns an array of nodes that were added as collision exceptions for this body.

---

[bool](class_bool.md#class-bool) **get_collision_layer_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the collision_layer is enabled, given a `layer_number` between 1 and 32.

---

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the collision_mask is enabled, given a `layer_number` between 1 and 32.

---

[RID](class_rid.md#class-rid) **get_physics_rid**()

Returns the internal [RID](class_rid.md#class-rid) used by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) for this body.

---

[Vector3](class_vector3.md#class-vector3) **get_point_transform**(point_index: [int](class_int.md#class-int))

Returns local translation of a vertex in the surface array.

---

[bool](class_bool.md#class-bool) **is_point_pinned**(point_index: [int](class_int.md#class-int))

Returns `true` if vertex is set to pinned.

---

 **remove_collision_exception_with**(body: [Node](class_node.md#class-node))

Removes a body from the list of bodies that this body can't collide with.

---

 **set_collision_layer_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the collision_layer, given a `layer_number` between 1 and 32.

---

 **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the collision_mask, given a `layer_number` between 1 and 32.

---

 **set_point_pinned**(point_index: [int](class_int.md#class-int), pinned: [bool](class_bool.md#class-bool), attachment_path: [NodePath](class_nodepath.md#class-nodepath) = NodePath(""), insert_at: [int](class_int.md#class-int) = -1)

Sets the pinned state of a surface vertex. When set to `true`, the optional `attachment_path` can define a [Node3D](class_node3d.md#class-node3d) the pinned vertex will be attached to.
