# CollisionObject3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [Area3D](class_area3d.md#class-area3d), [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d)

Abstract base class for 3D physics objects.

## Description

Abstract base class for 3D physics objects. **CollisionObject3D** can hold any number of [Shape3D](class_shape3d.md#class-shape3d)s for collision. Each shape must be assigned to a *shape owner*. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the `shape_owner_*` methods.

**Warning:** With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.

## Properties

| [int](class_int.md#class-int)                      | collision_layer             | `1`     |
|----------------------------------------------------|----------------------------------------------------------------------------------|---------|
| [int](class_int.md#class-int)                      | collision_mask               | `1`     |
| [float](class_float.md#class-float)                | collision_priority       | `1.0`   |
| DisableMode | disable_mode                   | `0`     |
| [bool](class_bool.md#class-bool)                   | input_capture_on_drag | `false` |
| [bool](class_bool.md#class-bool)                   | input_ray_pickable       | `true`  |

## Methods

|                                                                      | \_input_event(camera: [Camera3D](class_camera3d.md#class-camera3d), event: [InputEvent](class_inputevent.md#class-inputevent), event_position: [Vector3](class_vector3.md#class-vector3), normal: [Vector3](class_vector3.md#class-vector3), shape_idx: [int](class_int.md#class-int))    |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                      | \_mouse_enter()                                                                                                                                                                                                                                                                           |
|                                                                      | \_mouse_exit()                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                        | create_shape_owner(owner: [Object](class_object.md#class-object))                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                     | get_collision_layer_value(layer_number: [int](class_int.md#class-int))                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                     | get_collision_mask_value(layer_number: [int](class_int.md#class-int))                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)                                        | get_rid()                                                                                                                                                                                                                                                                                             |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | get_shape_owners()                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                     | is_shape_owner_disabled(owner_id: [int](class_int.md#class-int))                                                                                                                                                                                                                      |
|                                                                      | remove_shape_owner(owner_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                |
|                                                                      | set_collision_layer_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))                                                                                                                                                                     |
|                                                                      | set_collision_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))                                                                                                                                                                       |
| [int](class_int.md#class-int)                                        | shape_find_owner(shape_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                 |
|                                                                      | shape_owner_add_shape(owner_id: [int](class_int.md#class-int), shape: [Shape3D](class_shape3d.md#class-shape3d))                                                                                                                                                                        |
|                                                                      | shape_owner_clear_shapes(owner_id: [int](class_int.md#class-int))                                                                                                                                                                                                                    |
| [Object](class_object.md#class-object)                               | shape_owner_get_owner(owner_id: [int](class_int.md#class-int))                                                                                                                                                                                                                          |
| [Shape3D](class_shape3d.md#class-shape3d)                            | shape_owner_get_shape(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                        | shape_owner_get_shape_count(owner_id: [int](class_int.md#class-int))                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                        | shape_owner_get_shape_index(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))                                                                                                                                                                     |
| [Transform3D](class_transform3d.md#class-transform3d)                | shape_owner_get_transform(owner_id: [int](class_int.md#class-int))                                                                                                                                                                                                                  |
|                                                                      | shape_owner_remove_shape(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))                                                                                                                                                                           |
|                                                                      | shape_owner_set_disabled(owner_id: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                        |
|                                                                      | shape_owner_set_transform(owner_id: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                |

---

## Signals

**input_event**(camera: [Node](class_node.md#class-node), event: [InputEvent](class_inputevent.md#class-inputevent), event_position: [Vector3](class_vector3.md#class-vector3), normal: [Vector3](class_vector3.md#class-vector3), shape_idx: [int](class_int.md#class-int))

Emitted when the object receives an unhandled [InputEvent](class_inputevent.md#class-inputevent). `event_position` is the location in world space of the mouse pointer on the surface of the shape with index `shape_idx` and `normal` is the normal vector of the surface at that point.

---

**mouse_entered**()

Emitted when the mouse pointer enters any of this object's shapes. Requires input_ray_pickable to be `true` and at least one collision_layer bit to be set.

**Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject3D**'s area is small. This signal may also not be emitted if another **CollisionObject3D** is overlapping the **CollisionObject3D** in question.

---

**mouse_exited**()

Emitted when the mouse pointer exits all this object's shapes. Requires input_ray_pickable to be `true` and at least one collision_layer bit to be set.

**Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject3D**'s area is small. This signal may also not be emitted if another **CollisionObject3D** is overlapping the **CollisionObject3D** in question.

---

## Enumerations

enum **DisableMode**:

DisableMode **DISABLE_MODE_REMOVE** = `0`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), remove from the physics simulation to stop all physics interactions with this **CollisionObject3D**.

Automatically re-added to the physics simulation when the [Node](class_node.md#class-node) is processed again.

DisableMode **DISABLE_MODE_MAKE_STATIC** = `1`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), make the body static. Doesn't affect [Area3D](class_area3d.md#class-area3d). [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) can't be affected by forces or other bodies while static.

Automatically set [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) back to its original mode when the [Node](class_node.md#class-node) is processed again.

DisableMode **DISABLE_MODE_KEEP_ACTIVE** = `2`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), do not affect the physics simulation.

---

## Property Descriptions

[int](class_int.md#class-int) **collision_layer** = `1`

-  **set_collision_layer**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_layer**()

The physics layers this CollisionObject3D **is in**. Collision objects can exist in one or more of 32 different layers. See also collision_mask.

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[int](class_int.md#class-int) **collision_mask** = `1`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers this CollisionObject3D **scans**. Collision objects can scan one or more of 32 different layers. See also collision_layer.

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[float](class_float.md#class-float) **collision_priority** = `1.0`

-  **set_collision_priority**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_collision_priority**()

The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.

---

DisableMode **disable_mode** = `0`

-  **set_disable_mode**(value: DisableMode)
- DisableMode **get_disable_mode**()

Defines the behavior in physics when [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled).

---

[bool](class_bool.md#class-bool) **input_capture_on_drag** = `false`

-  **set_capture_input_on_drag**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_capture_input_on_drag**()

If `true`, the **CollisionObject3D** will continue to receive input events as the mouse is dragged across its shapes.

---

[bool](class_bool.md#class-bool) **input_ray_pickable** = `true`

-  **set_ray_pickable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ray_pickable**()

If `true`, this object is pickable. A pickable object can detect the mouse pointer entering/leaving, and if the mouse is inside it, report input events. Requires at least one collision_layer bit to be set.

---

## Method Descriptions

 **\_input_event**(camera: [Camera3D](class_camera3d.md#class-camera3d), event: [InputEvent](class_inputevent.md#class-inputevent), event_position: [Vector3](class_vector3.md#class-vector3), normal: [Vector3](class_vector3.md#class-vector3), shape_idx: [int](class_int.md#class-int))

Receives unhandled [InputEvent](class_inputevent.md#class-inputevent)s. `event_position` is the location in world space of the mouse pointer on the surface of the shape with index `shape_idx` and `normal` is the normal vector of the surface at that point. Connect to the input_event signal to easily pick up these events.

**Note:** \_input_event() requires input_ray_pickable to be `true` and at least one collision_layer bit to be set.

---

 **\_mouse_enter**()

Called when the mouse pointer enters any of this object's shapes. Requires input_ray_pickable to be `true` and at least one collision_layer bit to be set. Note that moving between different shapes within a single **CollisionObject3D** won't cause this function to be called.

---

 **\_mouse_exit**()

Called when the mouse pointer exits all this object's shapes. Requires input_ray_pickable to be `true` and at least one collision_layer bit to be set. Note that moving between different shapes within a single **CollisionObject3D** won't cause this function to be called.

---

[int](class_int.md#class-int) **create_shape_owner**(owner: [Object](class_object.md#class-object))

Creates a new shape owner for the given object. Returns `owner_id` of the new owner for future reference.

---

[bool](class_bool.md#class-bool) **get_collision_layer_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the collision_layer is enabled, given a `layer_number` between 1 and 32.

---

[bool](class_bool.md#class-bool) **get_collision_mask_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the collision_mask is enabled, given a `layer_number` between 1 and 32.

---

[RID](class_rid.md#class-rid) **get_rid**()

Returns the object's [RID](class_rid.md#class-rid).

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_shape_owners**()

Returns an [Array](class_array.md#class-array) of `owner_id` identifiers. You can use these ids in other methods that take `owner_id` as an argument.

---

[bool](class_bool.md#class-bool) **is_shape_owner_disabled**(owner_id: [int](class_int.md#class-int))

If `true`, the shape owner and its shapes are disabled.

---

 **remove_shape_owner**(owner_id: [int](class_int.md#class-int))

Removes the given shape owner.

---

 **set_collision_layer_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the collision_layer, given a `layer_number` between 1 and 32.

---

 **set_collision_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the collision_mask, given a `layer_number` between 1 and 32.

---

[int](class_int.md#class-int) **shape_find_owner**(shape_index: [int](class_int.md#class-int))

Returns the `owner_id` of the given shape.

---

 **shape_owner_add_shape**(owner_id: [int](class_int.md#class-int), shape: [Shape3D](class_shape3d.md#class-shape3d))

Adds a [Shape3D](class_shape3d.md#class-shape3d) to the shape owner.

---

 **shape_owner_clear_shapes**(owner_id: [int](class_int.md#class-int))

Removes all shapes from the shape owner.

---

[Object](class_object.md#class-object) **shape_owner_get_owner**(owner_id: [int](class_int.md#class-int))

Returns the parent object of the given shape owner.

---

[Shape3D](class_shape3d.md#class-shape3d) **shape_owner_get_shape**(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))

Returns the [Shape3D](class_shape3d.md#class-shape3d) with the given ID from the given shape owner.

---

[int](class_int.md#class-int) **shape_owner_get_shape_count**(owner_id: [int](class_int.md#class-int))

Returns the number of shapes the given shape owner contains.

---

[int](class_int.md#class-int) **shape_owner_get_shape_index**(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))

Returns the child index of the [Shape3D](class_shape3d.md#class-shape3d) with the given ID from the given shape owner.

---

[Transform3D](class_transform3d.md#class-transform3d) **shape_owner_get_transform**(owner_id: [int](class_int.md#class-int))

Returns the shape owner's [Transform3D](class_transform3d.md#class-transform3d).

---

 **shape_owner_remove_shape**(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))

Removes a shape from the given shape owner.

---

 **shape_owner_set_disabled**(owner_id: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

If `true`, disables the given shape owner.

---

 **shape_owner_set_transform**(owner_id: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))

Sets the [Transform3D](class_transform3d.md#class-transform3d) of the given shape owner.
