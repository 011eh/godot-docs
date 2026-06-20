# CSGShape3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [CSGCombiner3D](class_csgcombiner3d.md#class-csgcombiner3d), [CSGPrimitive3D](class_csgprimitive3d.md#class-csgprimitive3d)

The CSG base class.

## Description

This is the CSG base class that provides CSG operation support to the various CSG nodes in Godot.

**Performance:** CSG nodes are only intended for prototyping as they have a significant CPU performance cost. Consider baking final CSG operation results into static geometry that replaces the CSG nodes.

Individual CSG root node results can be baked to nodes with static resources with the editor menu that appears when a CSG root node is selected.

Individual CSG root nodes can also be baked to static resources with scripts by calling bake_static_mesh() for the visual mesh or bake_collision_shape() for the physics collision.

Entire scenes of CSG nodes can be baked to static geometry and exported with the editor glTF scene exporter: **Scene > Export As... > glTF 2.0 Scene...**

## Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

## Properties

| [bool](class_bool.md#class-bool)        | autosmooth                 | `false`   |
|-----------------------------------------|---------------------------------------------------------------------|-----------|
| [bool](class_bool.md#class-bool)        | calculate_tangents | `true`    |
| [int](class_int.md#class-int)           | collision_layer       | `1`       |
| [int](class_int.md#class-int)           | collision_mask         | `1`       |
| [float](class_float.md#class-float)     | collision_priority | `1.0`     |
| Operation | operation                   | `0`       |
| [float](class_float.md#class-float)     | smoothing_angle       | `50.0`    |
| [float](class_float.md#class-float)     | snap                             |           |
| [bool](class_bool.md#class-bool)        | use_collision           | `false`   |

## Methods

| [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d)   | bake_collision_shape()                                                                                               |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ArrayMesh](class_arraymesh.md#class-arraymesh)                                       | bake_static_mesh()                                                                                                       |
| [bool](class_bool.md#class-bool)                                                      | get_collision_layer_value(layer_number: [int](class_int.md#class-int))                                          |
| [bool](class_bool.md#class-bool)                                                      | get_collision_mask_value(layer_number: [int](class_int.md#class-int))                                            |
| [Array](class_array.md#class-array)                                                   | get_meshes()                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                      | is_root_shape()                                                                                                             |
|                                                                                       | set_collision_layer_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
|                                                                                       | set_collision_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))   |

---

## Enumerations

enum **Operation**:

Operation **OPERATION_UNION** = `0`

Geometry of both primitives is merged, intersecting geometry is removed.

Operation **OPERATION_INTERSECTION** = `1`

Only intersecting geometry remains, the rest is removed.

Operation **OPERATION_SUBTRACTION** = `2`

The second shape is subtracted from the first, leaving a dent with its shape.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **autosmooth** = `false`

-  **set_autosmooth**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_autosmooth**()

Enables automatic smoothing. This overrides any smoothing on the CSG node and instead uses smoothing_angle to calculate normals based on the angle between faces.

Children of a [CSGCombiner3D](class_csgcombiner3d.md#class-csgcombiner3d) node will be treated as a single mesh.

---

[bool](class_bool.md#class-bool) **calculate_tangents** = `true`

-  **set_calculate_tangents**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_calculating_tangents**()

Calculate tangents for the CSG shape which allows the use of normal and height maps. This is only applied on the root shape, this setting is ignored on any child. Setting this to `false` can speed up shape generation slightly.

---

[int](class_int.md#class-int) **collision_layer** = `1`

-  **set_collision_layer**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_layer**()

The physics layers this area is in.

Collidable objects can exist in any of 32 different layers. These layers work like a tagging system, and are not visual. A collidable can use these layers to select with which objects it can collide, using the collision_mask property.

A contact is detected if object A is in any of the layers that object B scans, or object B is in any layer scanned by object A. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[int](class_int.md#class-int) **collision_mask** = `1`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers this CSG shape scans for collisions. Only effective if use_collision is `true`. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[float](class_float.md#class-float) **collision_priority** = `1.0`

-  **set_collision_priority**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_collision_priority**()

The priority used to solve colliding when occurring penetration. Only effective if use_collision is `true`. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.

---

Operation **operation** = `0`

-  **set_operation**(value: Operation)
- Operation **get_operation**()

The operation that is performed on this shape. This is ignored for the first CSG child node as the operation is between this node and the previous child of this nodes parent.

---

[float](class_float.md#class-float) **smoothing_angle** = `50.0`

-  **set_smoothing_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_smoothing_angle**()

When autosmooth is enabled, faces with an angle between them greater than this will be smoothed, while faces with a smaller angle will remain sharp.

Note: An angle lower than 0.1 will cause all smoothing to be disabled, this can be used to increase performance.

---

[float](class_float.md#class-float) **snap**

-  **set_snap**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_snap**()

**Deprecated:** The CSG library no longer uses snapping.

This property does nothing.

---

[bool](class_bool.md#class-bool) **use_collision** = `false`

-  **set_use_collision**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_collision**()

Adds a collision shape to the physics engine for our CSG shape. This will always act like a static body. Note that the collision shape is still active even if the CSG shape itself is hidden. See also collision_mask and collision_priority.

---

## Method Descriptions

[ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d) **bake_collision_shape**()

Returns a baked physics [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class-concavepolygonshape3d) of this node's CSG operation result. Returns an empty shape if the node is not a CSG root node or has no valid geometry.

**Performance:** If the CSG operation results in a very detailed geometry with many faces physics performance will be very slow. Concave shapes should in general only be used for static level geometry and not with dynamic objects that are moving.

**Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty shape or outdated mesh data, make sure to call `await get_tree().process_frame` before using bake_collision_shape() in [Node._ready()](class_node.md#class-node-private-method-ready) or after changing properties on the **CSGShape3D**.

---

[ArrayMesh](class_arraymesh.md#class-arraymesh) **bake_static_mesh**()

Returns a baked static [ArrayMesh](class_arraymesh.md#class-arraymesh) of this node's CSG operation result. Materials from involved CSG nodes are added as extra mesh surfaces. Returns an empty mesh if the node is not a CSG root node or has no valid geometry.

**Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty mesh or outdated mesh data, make sure to call `await get_tree().process_frame` before using bake_static_mesh() in [Node._ready()](class_node.md#class-node-private-method-ready) or after changing properties on the **CSGShape3D**.

---

[bool](class_bool.md#class-bool) **get_collision_layer_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the collision_layer is enabled, given a `layer_number` between 1 and 32.

---

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the collision_mask is enabled, given a `layer_number` between 1 and 32.

---

[Array](class_array.md#class-array) **get_meshes**()

Returns an [Array](class_array.md#class-array) with two elements, the first is the [Transform3D](class_transform3d.md#class-transform3d) of this node and the second is the root [Mesh](class_mesh.md#class-mesh) of this node. Only works when this node is the root shape.

**Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty shape or outdated mesh data, make sure to call `await get_tree().process_frame` before using get_meshes() in [Node._ready()](class_node.md#class-node-private-method-ready) or after changing properties on the **CSGShape3D**.

---

[bool](class_bool.md#class-bool) **is_root_shape**()

Returns `true` if this is a root shape and is thus the object that is rendered.

---

 **set_collision_layer_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the collision_layer, given a `layer_number` between 1 and 32.

---

 **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the collision_mask, given a `layer_number` between 1 and 32.
