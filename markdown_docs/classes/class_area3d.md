# Area3D

**Inherits:** [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A region of 3D space that detects other [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)s entering or exiting it.

## Description

**Area3D** is a region of 3D space defined by one or multiple [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) or [CollisionPolygon3D](class_collisionpolygon3d.md#class-collisionpolygon3d) child nodes. It detects when other [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d)s enter or exit it, and it also keeps track of which collision objects haven't exited it yet (i.e. which one are overlapping it).

This node can also locally alter or override physics parameters (gravity, damping) and route audio to custom audio buses.

**Note:** Areas and bodies created with [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) might not interact as expected with **Area3D**s, and might not emit signals or track objects correctly.

**Warning:** Using a [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d) inside a [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) child of this node (created e.g. by using the **Create Trimesh Collision Sibling** option in the **Mesh** menu that appears when selecting a [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) node) may give unexpected results, since this collision shape is hollow. If this is not desired, it has to be split into multiple [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class-convexpolygonshape3d)s or primitive shapes like [BoxShape3D](class_boxshape3d.md#class-boxshape3d), or in some cases it may be replaceable by a [CollisionPolygon3D](class_collisionpolygon3d.md#class-collisionpolygon3d).

## Tutorials

- [Using Area2D](../tutorials/physics/using_area_2d.md)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [GUI in 3D Viewport Demo](https://godotengine.org/asset-library/asset/2807)

## Properties

| [float](class_float.md#class-float)                | angular_damp                               | `0.1`               |
|----------------------------------------------------|-----------------------------------------------------------------------------------|---------------------|
| SpaceOverride        | angular_damp_space_override | `0`                 |
| [StringName](class_stringname.md#class-stringname) | audio_bus_name                           | `&"Master"`         |
| [bool](class_bool.md#class-bool)                   | audio_bus_override                   | `false`             |
| [float](class_float.md#class-float)                | gravity                                         | `9.8`               |
| [Vector3](class_vector3.md#class-vector3)          | gravity_direction                     | `Vector3(0, -1, 0)` |
| [bool](class_bool.md#class-bool)                   | gravity_point                             | `false`             |
| [Vector3](class_vector3.md#class-vector3)          | gravity_point_center               | `Vector3(0, -1, 0)` |
| [float](class_float.md#class-float)                | gravity_point_unit_distance | `0.0`               |
| SpaceOverride        | gravity_space_override           | `0`                 |
| [float](class_float.md#class-float)                | linear_damp                                 | `0.1`               |
| SpaceOverride        | linear_damp_space_override   | `0`                 |
| [bool](class_bool.md#class-bool)                   | monitorable                                 | `true`              |
| [bool](class_bool.md#class-bool)                   | monitoring                                   | `true`              |
| [int](class_int.md#class-int)                      | priority                                       | `0`                 |
| [float](class_float.md#class-float)                | reverb_bus_amount                     | `0.0`               |
| [bool](class_bool.md#class-bool)                   | reverb_bus_enabled                   | `false`             |
| [StringName](class_stringname.md#class-stringname) | reverb_bus_name                         | `&"Master"`         |
| [float](class_float.md#class-float)                | reverb_bus_uniformity             | `0.0`               |
| [float](class_float.md#class-float)                | wind_attenuation_factor         | `0.0`               |
| [float](class_float.md#class-float)                | wind_force_magnitude               | `0.0`               |
| [NodePath](class_nodepath.md#class-nodepath)       | wind_source_path                       | `NodePath("")`      |

## Methods

| [Array](class_array.md#class-array)[Area3D]                | get_overlapping_areas()                       |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)[[Node3D](class_node3d.md#class-node3d)] | get_overlapping_bodies()                     |
| [bool](class_bool.md#class-bool)                                            | has_overlapping_areas()                       |
| [bool](class_bool.md#class-bool)                                            | has_overlapping_bodies()                     |
| [bool](class_bool.md#class-bool)                                            | overlaps_area(area: [Node](class_node.md#class-node)) |
| [bool](class_bool.md#class-bool)                                            | overlaps_body(body: [Node](class_node.md#class-node)) |

---

## Signals

**area_entered**(area: Area3D)

Emitted when the received `area` enters this area. Requires monitoring to be set to `true`.

---

**area_exited**(area: Area3D)

Emitted when the received `area` exits this area. Requires monitoring to be set to `true`.

---

**area_shape_entered**(area_rid: [RID](class_rid.md#class-rid), area: Area3D, area_shape_index: [int](class_int.md#class-int), local_shape_index: [int](class_int.md#class-int))

Emitted when a [Shape3D](class_shape3d.md#class-shape3d) of the received `area` enters a shape of this area. Requires monitoring to be set to `true`.

`local_shape_index` and `area_shape_index` contain indices of the interacting shapes from this area and the other area, respectively. `area_rid` contains the [RID](class_rid.md#class-rid) of the other area. These values can be used with the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d).

**Example:** Get the [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) node from the shape index:

GDScript

```gdscript
var other_shape_owner = area.shape_find_owner(area_shape_index)
var other_shape_node = area.shape_owner_get_owner(other_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index)
var local_shape_node = shape_owner_get_owner(local_shape_owner)
```

---

**area_shape_exited**(area_rid: [RID](class_rid.md#class-rid), area: Area3D, area_shape_index: [int](class_int.md#class-int), local_shape_index: [int](class_int.md#class-int))

Emitted when a [Shape3D](class_shape3d.md#class-shape3d) of the received `area` exits a shape of this area. Requires monitoring to be set to `true`.

See also area_shape_entered.

---

**body_entered**(body: [Node3D](class_node3d.md#class-node3d))

Emitted when the received `body` enters this area. `body` can be a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d), [SoftBody3D](class_softbody3d.md#class-softbody3d) or [GridMap](class_gridmap.md#class-gridmap). [GridMap](class_gridmap.md#class-gridmap)s are detected if their [MeshLibrary](class_meshlibrary.md#class-meshlibrary) has collision shapes configured. Requires monitoring to be set to `true`.

**Note:** Godot Physics does not support reporting overlaps with [SoftBody3D](class_softbody3d.md#class-softbody3d), so will not emit this signal in such cases.

---

**body_exited**(body: [Node3D](class_node3d.md#class-node3d))

Emitted when the received `body` exits this area. `body` can be a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d), [SoftBody3D](class_softbody3d.md#class-softbody3d) or [GridMap](class_gridmap.md#class-gridmap). [GridMap](class_gridmap.md#class-gridmap)s are detected if their [MeshLibrary](class_meshlibrary.md#class-meshlibrary) has collision shapes configured. Requires monitoring to be set to `true`.

**Note:** Godot Physics does not support reporting overlaps with [SoftBody3D](class_softbody3d.md#class-softbody3d), so will not emit this signal in such cases.

---

**body_shape_entered**(body_rid: [RID](class_rid.md#class-rid), body: [Node3D](class_node3d.md#class-node3d), body_shape_index: [int](class_int.md#class-int), local_shape_index: [int](class_int.md#class-int))

Emitted when a [Shape3D](class_shape3d.md#class-shape3d) of the received `body` enters a shape of this area. `body` can be a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d), [SoftBody3D](class_softbody3d.md#class-softbody3d) or [GridMap](class_gridmap.md#class-gridmap). [GridMap](class_gridmap.md#class-gridmap)s are detected if their [MeshLibrary](class_meshlibrary.md#class-meshlibrary) has collision shapes configured. Requires monitoring to be set to `true`.

`local_shape_index` and `body_shape_index` contain indices of the interacting shapes from this area and the interacting body, respectively. `body_rid` contains the [RID](class_rid.md#class-rid) of the body. These values can be used with the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d).

**Note:** Godot Physics does not support reporting overlaps with [SoftBody3D](class_softbody3d.md#class-softbody3d), so will not emit this signal in such cases.

**Example:** Get the [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) node from the shape index:

GDScript

```gdscript
var body_shape_owner = body.shape_find_owner(body_shape_index)
var body_shape_node = body.shape_owner_get_owner(body_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index)
var local_shape_node = shape_owner_get_owner(local_shape_owner)
```

---

**body_shape_exited**(body_rid: [RID](class_rid.md#class-rid), body: [Node3D](class_node3d.md#class-node3d), body_shape_index: [int](class_int.md#class-int), local_shape_index: [int](class_int.md#class-int))

Emitted when a [Shape3D](class_shape3d.md#class-shape3d) of the received `body` exits a shape of this area. `body` can be a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d), [SoftBody3D](class_softbody3d.md#class-softbody3d) or [GridMap](class_gridmap.md#class-gridmap). [GridMap](class_gridmap.md#class-gridmap)s are detected if their [MeshLibrary](class_meshlibrary.md#class-meshlibrary) has collision shapes configured. Requires monitoring to be set to `true`.

See also body_shape_entered.

**Note:** Godot Physics does not support reporting overlaps with [SoftBody3D](class_softbody3d.md#class-softbody3d), so will not emit this signal in such cases.

---

## Enumerations

enum **SpaceOverride**:

SpaceOverride **SPACE_OVERRIDE_DISABLED** = `0`

This area does not affect gravity/damping.

SpaceOverride **SPACE_OVERRIDE_COMBINE** = `1`

This area adds its gravity/damping values to whatever has been calculated so far (in priority order).

SpaceOverride **SPACE_OVERRIDE_COMBINE_REPLACE** = `2`

This area adds its gravity/damping values to whatever has been calculated so far (in priority order), ignoring any lower priority areas.

SpaceOverride **SPACE_OVERRIDE_REPLACE** = `3`

This area replaces any gravity/damping, even the defaults, ignoring any lower priority areas.

SpaceOverride **SPACE_OVERRIDE_REPLACE_COMBINE** = `4`

This area replaces any gravity/damping calculated so far (in priority order), but keeps calculating the rest of the areas.

---

## Property Descriptions

[float](class_float.md#class-float) **angular_damp** = `0.1`

-  **set_angular_damp**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_angular_damp**()

The rate at which objects stop spinning in this area. Represents the angular velocity lost per second.

See [ProjectSettings.physics/3d/default_angular_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-angular-damp) for more details about damping.

---

SpaceOverride **angular_damp_space_override** = `0`

-  **set_angular_damp_space_override_mode**(value: SpaceOverride)
- SpaceOverride **get_angular_damp_space_override_mode**()

Override mode for angular damping calculations within this area.

---

[StringName](class_stringname.md#class-stringname) **audio_bus_name** = `&"Master"`

-  **set_audio_bus_name**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_audio_bus_name**()

The name of the area's audio bus.

---

[bool](class_bool.md#class-bool) **audio_bus_override** = `false`

-  **set_audio_bus_override**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_overriding_audio_bus**()

If `true`, the area's audio bus overrides the default audio bus.

---

[float](class_float.md#class-float) **gravity** = `9.8`

-  **set_gravity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gravity**()

The area's gravity intensity (in meters per second squared). This value multiplies the gravity direction. This is useful to alter the force of gravity without altering its direction.

---

[Vector3](class_vector3.md#class-vector3) **gravity_direction** = `Vector3(0, -1, 0)`

-  **set_gravity_direction**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_gravity_direction**()

The area's gravity vector (not normalized).

---

[bool](class_bool.md#class-bool) **gravity_point** = `false`

-  **set_gravity_is_point**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_gravity_a_point**()

If `true`, gravity is calculated from a point (set via gravity_point_center). See also gravity_space_override.

---

[Vector3](class_vector3.md#class-vector3) **gravity_point_center** = `Vector3(0, -1, 0)`

-  **set_gravity_point_center**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_gravity_point_center**()

If gravity is a point (see gravity_point), this will be the point of attraction.

---

[float](class_float.md#class-float) **gravity_point_unit_distance** = `0.0`

-  **set_gravity_point_unit_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gravity_point_unit_distance**()

The distance at which the gravity strength is equal to gravity. For example, on a planet 100 meters in radius with a surface gravity of 4.0 m/s², set the gravity to 4.0 and the unit distance to 100.0. The gravity will have falloff according to the inverse square law, so in the example, at 200 meters from the center the gravity will be 1.0 m/s² (twice the distance, 1/4th the gravity), at 50 meters it will be 16.0 m/s² (half the distance, 4x the gravity), and so on.

The above is true only when the unit distance is a positive number. When this is set to 0.0, the gravity will be constant regardless of distance.

---

SpaceOverride **gravity_space_override** = `0`

-  **set_gravity_space_override_mode**(value: SpaceOverride)
- SpaceOverride **get_gravity_space_override_mode**()

Override mode for gravity calculations within this area.

---

[float](class_float.md#class-float) **linear_damp** = `0.1`

-  **set_linear_damp**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_linear_damp**()

The rate at which objects stop moving in this area. Represents the linear velocity lost per second.

See [ProjectSettings.physics/3d/default_linear_damp](class_projectsettings.md#class-projectsettings-property-physics-3d-default-linear-damp) for more details about damping.

---

SpaceOverride **linear_damp_space_override** = `0`

-  **set_linear_damp_space_override_mode**(value: SpaceOverride)
- SpaceOverride **get_linear_damp_space_override_mode**()

Override mode for linear damping calculations within this area.

---

[bool](class_bool.md#class-bool) **monitorable** = `true`

-  **set_monitorable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_monitorable**()

If `true`, other monitoring areas can detect this area.

---

[bool](class_bool.md#class-bool) **monitoring** = `true`

-  **set_monitoring**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_monitoring**()

If `true`, the area detects bodies or areas entering and exiting it.

---

[int](class_int.md#class-int) **priority** = `0`

-  **set_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_priority**()

The area's priority. Higher priority areas are processed first. The [World3D](class_world3d.md#class-world3d)'s physics is always processed last, after all areas.

---

[float](class_float.md#class-float) **reverb_bus_amount** = `0.0`

-  **set_reverb_amount**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_reverb_amount**()

The degree to which this area applies reverb to its associated audio. Ranges from `0` to `1` with `0.1` precision.

---

[bool](class_bool.md#class-bool) **reverb_bus_enabled** = `false`

-  **set_use_reverb_bus**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_reverb_bus**()

If `true`, the area applies reverb to its associated audio.

---

[StringName](class_stringname.md#class-stringname) **reverb_bus_name** = `&"Master"`

-  **set_reverb_bus_name**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_reverb_bus_name**()

The name of the reverb bus to use for this area's associated audio.

---

[float](class_float.md#class-float) **reverb_bus_uniformity** = `0.0`

-  **set_reverb_uniformity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_reverb_uniformity**()

The degree to which this area's reverb is a uniform effect. Ranges from `0` to `1` with `0.1` precision.

---

[float](class_float.md#class-float) **wind_attenuation_factor** = `0.0`

-  **set_wind_attenuation_factor**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_wind_attenuation_factor**()

The exponential rate at which wind force decreases with distance from its origin.

**Note:** This wind force only applies to [SoftBody3D](class_softbody3d.md#class-softbody3d) nodes. Other physics bodies are currently not affected by wind.

---

[float](class_float.md#class-float) **wind_force_magnitude** = `0.0`

-  **set_wind_force_magnitude**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_wind_force_magnitude**()

The magnitude of area-specific wind force.

**Note:** This wind force only applies to [SoftBody3D](class_softbody3d.md#class-softbody3d) nodes. Other physics bodies are currently not affected by wind.

---

[NodePath](class_nodepath.md#class-nodepath) **wind_source_path** = `NodePath("")`

-  **set_wind_source_path**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_wind_source_path**()

The [Node3D](class_node3d.md#class-node3d) which is used to specify the direction and origin of an area-specific wind force. The direction is opposite to the z-axis of the [Node3D](class_node3d.md#class-node3d)'s local transform, and its origin is the origin of the [Node3D](class_node3d.md#class-node3d)'s local transform.

**Note:** This wind force only applies to [SoftBody3D](class_softbody3d.md#class-softbody3d) nodes. Other physics bodies are currently not affected by wind.

---

## Method Descriptions

[Array](class_array.md#class-array)[Area3D] **get_overlapping_areas**()

Returns a list of intersecting **Area3D**s. The overlapping area's [CollisionObject3D.collision_layer](class_collisionobject3d.md#class-collisionobject3d-property-collision-layer) must be part of this area's [CollisionObject3D.collision_mask](class_collisionobject3d.md#class-collisionobject3d-property-collision-mask) in order to be detected.

For performance reasons (collisions are all processed at the same time) this list is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.

---

[Array](class_array.md#class-array)[[Node3D](class_node3d.md#class-node3d)] **get_overlapping_bodies**()

Returns a list of intersecting [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)s, [SoftBody3D](class_softbody3d.md#class-softbody3d)s, and [GridMap](class_gridmap.md#class-gridmap)s. The overlapping body's [CollisionObject3D.collision_layer](class_collisionobject3d.md#class-collisionobject3d-property-collision-layer) must be part of this area's [CollisionObject3D.collision_mask](class_collisionobject3d.md#class-collisionobject3d-property-collision-mask) in order to be detected.

For performance reasons (collisions are all processed at the same time) this list is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.

**Note:** Godot Physics does not support reporting overlaps with [SoftBody3D](class_softbody3d.md#class-softbody3d), so will not return any such bodies.

---

[bool](class_bool.md#class-bool) **has_overlapping_areas**()

Returns `true` if intersecting any **Area3D**s, otherwise returns `false`. The overlapping area's [CollisionObject3D.collision_layer](class_collisionobject3d.md#class-collisionobject3d-property-collision-layer) must be part of this area's [CollisionObject3D.collision_mask](class_collisionobject3d.md#class-collisionobject3d-property-collision-mask) in order to be detected.

For performance reasons (collisions are all processed at the same time) the list of overlapping areas is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.

---

[bool](class_bool.md#class-bool) **has_overlapping_bodies**()

Returns `true` if intersecting any [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)s, [SoftBody3D](class_softbody3d.md#class-softbody3d)s, or [GridMap](class_gridmap.md#class-gridmap)s, otherwise returns `false`. The overlapping body's [CollisionObject3D.collision_layer](class_collisionobject3d.md#class-collisionobject3d-property-collision-layer) must be part of this area's [CollisionObject3D.collision_mask](class_collisionobject3d.md#class-collisionobject3d-property-collision-mask) in order to be detected.

For performance reasons (collisions are all processed at the same time) the list of overlapping bodies is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.

**Note:** Godot Physics does not support reporting overlaps with [SoftBody3D](class_softbody3d.md#class-softbody3d), so will not consider such bodies.

---

[bool](class_bool.md#class-bool) **overlaps_area**(area: [Node](class_node.md#class-node))

Returns `true` if the given **Area3D** intersects or overlaps this **Area3D**, `false` otherwise.

**Note:** The result of this test is not immediate after moving objects. For performance, list of overlaps is updated once per frame and before the physics step. Consider using signals instead.

---

[bool](class_bool.md#class-bool) **overlaps_body**(body: [Node](class_node.md#class-node))

Returns `true` if the given physics body intersects or overlaps this **Area3D**, `false` otherwise.

`body` argument can either be a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d), [SoftBody3D](class_softbody3d.md#class-softbody3d), or a [GridMap](class_gridmap.md#class-gridmap) instance. While GridMaps are not physics body themselves, they register their tiles with collision shapes as a virtual physics body.

**Note:** The result of this test is not immediate after moving objects. For performance, list of overlaps is updated once per frame and before the physics step. Consider using signals instead.

**Note:** Godot Physics does not support reporting overlaps with [SoftBody3D](class_softbody3d.md#class-softbody3d), so will return `false` in such cases.
