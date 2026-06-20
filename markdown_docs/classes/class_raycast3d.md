# RayCast3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A ray in 3D space, used to find the first collision object it intersects.

## Description

A raycast represents a ray from its origin to its target_position that finds the closest object along its path, if it intersects any.

**RayCast3D** can ignore some objects by adding them to an exception list, by making its detection reporting ignore [Area3D](class_area3d.md#class-area3d)s (collide_with_areas) or [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)s (collide_with_bodies), or by configuring physics layers.

**RayCast3D** calculates intersection every physics frame, and it holds the result until the next physics frame. For an immediate raycast, or if you want to configure a **RayCast3D** multiple times within the same physics frame, use force_raycast_update().

To sweep over a region of 3D space, you can approximate the region with multiple **RayCast3D**s or use [ShapeCast3D](class_shapecast3d.md#class-shapecast3d).

## Tutorials

- [Ray-casting](../tutorials/physics/ray-casting.md)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

## Properties

| [bool](class_bool.md#class-bool)          | collide_with_areas             | `false`             |
|-------------------------------------------|--------------------------------------------------------------------------------|---------------------|
| [bool](class_bool.md#class-bool)          | collide_with_bodies           | `true`              |
| [int](class_int.md#class-int)             | collision_mask                     | `1`                 |
| [Color](class_color.md#class-color)       | debug_shape_custom_color | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class-int)             | debug_shape_thickness       | `2`                 |
| [bool](class_bool.md#class-bool)          | enabled                                   | `true`              |
| [bool](class_bool.md#class-bool)          | exclude_parent                     | `true`              |
| [bool](class_bool.md#class-bool)          | hit_back_faces                     | `true`              |
| [bool](class_bool.md#class-bool)          | hit_from_inside                   | `false`             |
| [Vector3](class_vector3.md#class-vector3) | target_position                   | `Vector3(0, -1, 0)` |

## Methods

|                                           | add_exception(node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d))                              |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           | add_exception_rid(rid: [RID](class_rid.md#class-rid))                                                                 |
|                                           | clear_exceptions()                                                                                                     |
|                                           | force_raycast_update()                                                                                             |
| [Object](class_object.md#class-object)    | get_collider()                                                                                                             |
| [RID](class_rid.md#class-rid)             | get_collider_rid()                                                                                                     |
| [int](class_int.md#class-int)             | get_collider_shape()                                                                                                 |
| [int](class_int.md#class-int)             | get_collision_face_index()                                                                                     |
| [bool](class_bool.md#class-bool)          | get_collision_mask_value(layer_number: [int](class_int.md#class-int))                                          |
| [Vector3](class_vector3.md#class-vector3) | get_collision_normal()                                                                                             |
| [Vector3](class_vector3.md#class-vector3) | get_collision_point()                                                                                               |
| [bool](class_bool.md#class-bool)          | is_colliding()                                                                                                             |
|                                           | remove_exception(node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d))                        |
|                                           | remove_exception_rid(rid: [RID](class_rid.md#class-rid))                                                           |
|                                           | set_collision_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **collide_with_areas** = `false`

-  **set_collide_with_areas**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_areas_enabled**()

If `true`, collisions with [Area3D](class_area3d.md#class-area3d)s will be reported.

---

[bool](class_bool.md#class-bool) **collide_with_bodies** = `true`

-  **set_collide_with_bodies**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collide_with_bodies_enabled**()

If `true`, collisions with [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)s will be reported.

---

[int](class_int.md#class-int) **collision_mask** = `1`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The ray's collision mask. Only objects in at least one collision layer enabled in the mask will be detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[Color](class_color.md#class-color) **debug_shape_custom_color** = `Color(0, 0, 0, 1)`

-  **set_debug_shape_custom_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_debug_shape_custom_color**()

The custom color to use to draw the shape in the editor and at run-time if **Visible Collision Shapes** is enabled in the **Debug** menu. This color will be highlighted at run-time if the **RayCast3D** is colliding with something.

If set to `Color(0.0, 0.0, 0.0)` (by default), the color set in [ProjectSettings.debug/shapes/collision/shape_color](class_projectsettings.md#class-projectsettings-property-debug-shapes-collision-shape-color) is used.

---

[int](class_int.md#class-int) **debug_shape_thickness** = `2`

-  **set_debug_shape_thickness**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_debug_shape_thickness**()

If set to `1`, a line is used as the debug shape. Otherwise, a truncated pyramid is drawn to represent the **RayCast3D**. Requires **Visible Collision Shapes** to be enabled in the **Debug** menu for the debug shape to be visible at run-time.

---

[bool](class_bool.md#class-bool) **enabled** = `true`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

If `true`, collisions will be reported.

---

[bool](class_bool.md#class-bool) **exclude_parent** = `true`

-  **set_exclude_parent_body**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_exclude_parent_body**()

If `true`, this raycast will not report collisions with its parent node. This property only has an effect if the parent node is a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d). See also [Node.get_parent()](class_node.md#class-node-method-get-parent) and add_exception().

---

[bool](class_bool.md#class-bool) **hit_back_faces** = `true`

-  **set_hit_back_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hit_back_faces_enabled**()

If `true`, the ray will hit back faces with concave polygon shapes with back face enabled or heightmap shapes.

---

[bool](class_bool.md#class-bool) **hit_from_inside** = `false`

-  **set_hit_from_inside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hit_from_inside_enabled**()

If `true`, the ray will detect a hit when starting inside shapes. In this case the collision normal will be `Vector3(0, 0, 0)`. Does not affect shapes with no volume like concave polygon or heightmap.

---

[Vector3](class_vector3.md#class-vector3) **target_position** = `Vector3(0, -1, 0)`

-  **set_target_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_target_position**()

The ray's destination point, relative to this raycast's [Node3D.position](class_node3d.md#class-node3d-property-position).

---

## Method Descriptions

 **add_exception**(node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d))

Adds a collision exception so the ray does not report collisions with the specified `node`.

---

 **add_exception_rid**(rid: [RID](class_rid.md#class-rid))

Adds a collision exception so the ray does not report collisions with the specified [RID](class_rid.md#class-rid).

---

 **clear_exceptions**()

Removes all collision exceptions for this ray.

---

 **force_raycast_update**()

Updates the collision information for the ray immediately, without waiting for the next `_physics_process` call. Use this method, for example, when the ray or its parent has changed state.

**Note:** enabled does not need to be `true` for this to work.

---

[Object](class_object.md#class-object) **get_collider**()

Returns the first object that the ray intersects, or `null` if no object is intersecting the ray (i.e. is_colliding() returns `false`).

**Note:** This object is not guaranteed to be a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d). For example, if the ray intersects a [CSGShape3D](class_csgshape3d.md#class-csgshape3d) or a [GridMap](class_gridmap.md#class-gridmap), the method will return a [CSGShape3D](class_csgshape3d.md#class-csgshape3d) or [GridMap](class_gridmap.md#class-gridmap) instance.

---

[RID](class_rid.md#class-rid) **get_collider_rid**()

Returns the [RID](class_rid.md#class-rid) of the first object that the ray intersects, or an empty [RID](class_rid.md#class-rid) if no object is intersecting the ray (i.e. is_colliding() returns `false`).

---

[int](class_int.md#class-int) **get_collider_shape**()

Returns the shape ID of the first object that the ray intersects, or `0` if no object is intersecting the ray (i.e. is_colliding() returns `false`).

To get the intersected shape node, for a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) target, use:

GDScript

```gdscript
var target = get_collider() # A CollisionObject3D.
var shape_id = get_collider_shape() # The shape index in the collider.
var owner_id = target.shape_find_owner(shape_id) # The owner ID in the collider.
var shape = target.shape_owner_get_owner(owner_id)
```

C#

```csharp
var target = (CollisionObject3D)GetCollider(); // A CollisionObject3D.
var shapeId = GetColliderShape(); // The shape index in the collider.
var ownerId = target.ShapeFindOwner(shapeId); // The owner ID in the collider.
var shape = target.ShapeOwnerGetOwner(ownerId);
```

---

[int](class_int.md#class-int) **get_collision_face_index**()

Returns the collision object's face index at the collision point, or `-1` if the shape intersecting the ray is not a [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d).

---

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the collision_mask is enabled, given a `layer_number` between 1 and 32.

---

[Vector3](class_vector3.md#class-vector3) **get_collision_normal**()

Returns the normal of the intersecting object's shape at the collision point, or `Vector3(0, 0, 0)` if the ray starts inside the shape and hit_from_inside is `true`.

**Note:** Check that is_colliding() returns `true` before calling this method to ensure the returned normal is valid and up-to-date.

---

[Vector3](class_vector3.md#class-vector3) **get_collision_point**()

Returns the collision point at which the ray intersects the closest object, in the global coordinate system. If hit_from_inside is `true` and the ray starts inside of a collision shape, this function will return the origin point of the ray.

**Note:** Check that is_colliding() returns `true` before calling this method to ensure the returned point is valid and up-to-date.

---

[bool](class_bool.md#class-bool) **is_colliding**()

Returns whether any object is intersecting with the ray's vector (considering the vector length).

---

 **remove_exception**(node: [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d))

Removes a collision exception so the ray can report collisions with the specified `node`.

---

 **remove_exception_rid**(rid: [RID](class_rid.md#class-rid))

Removes a collision exception so the ray can report collisions with the specified [RID](class_rid.md#class-rid).

---

 **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the collision_mask, given a `layer_number` between 1 and 32.
