# CollisionObject2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [Area2D](class_area2d.md#class-area2d), [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d)

Abstract base class for 2D physics objects.

## Description

Abstract base class for 2D physics objects. **CollisionObject2D** can hold any number of [Shape2D](class_shape2d.md#class-shape2d)s for collision. Each shape must be assigned to a *shape owner*. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the `shape_owner_*` methods.

**Note:** Only collisions between objects within the same canvas ([Viewport](class_viewport.md#class-viewport) canvas or [CanvasLayer](class_canvaslayer.md#class-canvaslayer)) are supported. The behavior of collisions between objects in different canvases is undefined.

## Properties

| [int](class_int.md#class-int)                      | collision_layer       | `1`    |
|----------------------------------------------------|----------------------------------------------------------------------------|--------|
| [int](class_int.md#class-int)                      | collision_mask         | `1`    |
| [float](class_float.md#class-float)                | collision_priority | `1.0`  |
| DisableMode | disable_mode             | `0`    |
| [bool](class_bool.md#class-bool)                   | input_pickable         | `true` |

## Methods

|                                                                      | \_input_event(viewport: [Viewport](class_viewport.md#class-viewport), event: [InputEvent](class_inputevent.md#class-inputevent), shape_idx: [int](class_int.md#class-int))    |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                      | \_mouse_enter()                                                                                                                                                               |
|                                                                      | \_mouse_exit()                                                                                                                                                                 |
|                                                                      | \_mouse_shape_enter(shape_idx: [int](class_int.md#class-int))                                                                                                           |
|                                                                      | \_mouse_shape_exit(shape_idx: [int](class_int.md#class-int))                                                                                                             |
| [int](class_int.md#class-int)                                        | create_shape_owner(owner: [Object](class_object.md#class-object))                                                                                                              |
| [bool](class_bool.md#class-bool)                                     | get_collision_layer_value(layer_number: [int](class_int.md#class-int))                                                                                                  |
| [bool](class_bool.md#class-bool)                                     | get_collision_mask_value(layer_number: [int](class_int.md#class-int))                                                                                                    |
| [RID](class_rid.md#class-rid)                                        | get_rid()                                                                                                                                                                                 |
| [Vector2](class_vector2.md#class-vector2)                            | get_shape_owner_one_way_collision_direction(owner_id: [int](class_int.md#class-int))                                                                  |
| [float](class_float.md#class-float)                                  | get_shape_owner_one_way_collision_margin(owner_id: [int](class_int.md#class-int))                                                                        |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | get_shape_owners()                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                     | is_shape_owner_disabled(owner_id: [int](class_int.md#class-int))                                                                                                          |
| [bool](class_bool.md#class-bool)                                     | is_shape_owner_one_way_collision_enabled(owner_id: [int](class_int.md#class-int))                                                                        |
|                                                                      | remove_shape_owner(owner_id: [int](class_int.md#class-int))                                                                                                                    |
|                                                                      | set_collision_layer_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))                                                         |
|                                                                      | set_collision_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))                                                           |
| [int](class_int.md#class-int)                                        | shape_find_owner(shape_index: [int](class_int.md#class-int))                                                                                                                     |
|                                                                      | shape_owner_add_shape(owner_id: [int](class_int.md#class-int), shape: [Shape2D](class_shape2d.md#class-shape2d))                                                            |
|                                                                      | shape_owner_clear_shapes(owner_id: [int](class_int.md#class-int))                                                                                                        |
| [Object](class_object.md#class-object)                               | shape_owner_get_owner(owner_id: [int](class_int.md#class-int))                                                                                                              |
| [Shape2D](class_shape2d.md#class-shape2d)                            | shape_owner_get_shape(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))                                                                     |
| [int](class_int.md#class-int)                                        | shape_owner_get_shape_count(owner_id: [int](class_int.md#class-int))                                                                                                  |
| [int](class_int.md#class-int)                                        | shape_owner_get_shape_index(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))                                                         |
| [Transform2D](class_transform2d.md#class-transform2d)                | shape_owner_get_transform(owner_id: [int](class_int.md#class-int))                                                                                                      |
|                                                                      | shape_owner_remove_shape(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))                                                               |
|                                                                      | shape_owner_set_disabled(owner_id: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                            |
|                                                                      | shape_owner_set_one_way_collision(owner_id: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                            |
|                                                                      | shape_owner_set_one_way_collision_direction(owner_id: [int](class_int.md#class-int), direction: [Vector2](class_vector2.md#class-vector2))            |
|                                                                      | shape_owner_set_one_way_collision_margin(owner_id: [int](class_int.md#class-int), margin: [float](class_float.md#class-float))                           |
|                                                                      | shape_owner_set_transform(owner_id: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))                                    |

---

## Signals

**input_event**(viewport: [Node](class_node.md#class-node), event: [InputEvent](class_inputevent.md#class-inputevent), shape_idx: [int](class_int.md#class-int))

Emitted when an input event occurs. Requires input_pickable to be `true` and at least one collision_layer bit to be set. See \_input_event() for details.

---

**mouse_entered**()

Emitted when the mouse pointer enters any of this object's shapes. Requires input_pickable to be `true` and at least one collision_layer bit to be set. Note that moving between different shapes within a single **CollisionObject2D** won't cause this signal to be emitted.

**Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject2D**'s area is small. This signal may also not be emitted if another **CollisionObject2D** is overlapping the **CollisionObject2D** in question.

---

**mouse_exited**()

Emitted when the mouse pointer exits all this object's shapes. Requires input_pickable to be `true` and at least one collision_layer bit to be set. Note that moving between different shapes within a single **CollisionObject2D** won't cause this signal to be emitted.

**Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject2D**'s area is small. This signal may also not be emitted if another **CollisionObject2D** is overlapping the **CollisionObject2D** in question.

---

**mouse_shape_entered**(shape_idx: [int](class_int.md#class-int))

Emitted when the mouse pointer enters any of this object's shapes or moves from one shape to another. `shape_idx` is the child index of the newly entered [Shape2D](class_shape2d.md#class-shape2d). Requires input_pickable to be `true` and at least one collision_layer bit to be set.

---

**mouse_shape_exited**(shape_idx: [int](class_int.md#class-int))

Emitted when the mouse pointer exits any of this object's shapes. `shape_idx` is the child index of the exited [Shape2D](class_shape2d.md#class-shape2d). Requires input_pickable to be `true` and at least one collision_layer bit to be set.

---

## Enumerations

enum **DisableMode**:

DisableMode **DISABLE_MODE_REMOVE** = `0`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), remove from the physics simulation to stop all physics interactions with this **CollisionObject2D**.

Automatically re-added to the physics simulation when the [Node](class_node.md#class-node) is processed again.

DisableMode **DISABLE_MODE_MAKE_STATIC** = `1`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), make the body static. Doesn't affect [Area2D](class_area2d.md#class-area2d). [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) can't be affected by forces or other bodies while static.

Automatically set [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) back to its original mode when the [Node](class_node.md#class-node) is processed again.

DisableMode **DISABLE_MODE_KEEP_ACTIVE** = `2`

When [Node.process_mode](class_node.md#class-node-property-process-mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class-node-constant-process-mode-disabled), do not affect the physics simulation.

---

## Property Descriptions

[int](class_int.md#class-int) **collision_layer** = `1`

-  **set_collision_layer**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_layer**()

The physics layers this CollisionObject2D is in. Collision objects can exist in one or more of 32 different layers. See also collision_mask.

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[int](class_int.md#class-int) **collision_mask** = `1`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The physics layers this CollisionObject2D scans. Collision objects can scan one or more of 32 different layers. See also collision_layer.

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

[bool](class_bool.md#class-bool) **input_pickable** = `true`

-  **set_pickable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pickable**()

If `true`, this object is pickable. A pickable object can detect the mouse pointer entering/leaving, and if the mouse is inside it, report input events. Requires at least one collision_layer bit to be set.

---

## Method Descriptions

 **\_input_event**(viewport: [Viewport](class_viewport.md#class-viewport), event: [InputEvent](class_inputevent.md#class-inputevent), shape_idx: [int](class_int.md#class-int))

Accepts unhandled [InputEvent](class_inputevent.md#class-inputevent)s. `shape_idx` is the child index of the clicked [Shape2D](class_shape2d.md#class-shape2d). Connect to input_event to easily pick up these events.

**Note:** \_input_event() requires input_pickable to be `true` and at least one collision_layer bit to be set.

---

 **\_mouse_enter**()

Called when the mouse pointer enters any of this object's shapes. Requires input_pickable to be `true` and at least one collision_layer bit to be set. Note that moving between different shapes within a single **CollisionObject2D** won't cause this function to be called.

---

 **\_mouse_exit**()

Called when the mouse pointer exits all this object's shapes. Requires input_pickable to be `true` and at least one collision_layer bit to be set. Note that moving between different shapes within a single **CollisionObject2D** won't cause this function to be called.

---

 **\_mouse_shape_enter**(shape_idx: [int](class_int.md#class-int))

Called when the mouse pointer enters any of this object's shapes or moves from one shape to another. `shape_idx` is the child index of the newly entered [Shape2D](class_shape2d.md#class-shape2d). Requires input_pickable to be `true` and at least one collision_layer bit to be called.

---

 **\_mouse_shape_exit**(shape_idx: [int](class_int.md#class-int))

Called when the mouse pointer exits any of this object's shapes. `shape_idx` is the child index of the exited [Shape2D](class_shape2d.md#class-shape2d). Requires input_pickable to be `true` and at least one collision_layer bit to be called.

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

[Vector2](class_vector2.md#class-vector2) **get_shape_owner_one_way_collision_direction**(owner_id: [int](class_int.md#class-int))

Returns the `one_way_collision_direction` of the shape owner identified by the given `owner_id`.

---

[float](class_float.md#class-float) **get_shape_owner_one_way_collision_margin**(owner_id: [int](class_int.md#class-int))

Returns the `one_way_collision_margin` of the shape owner identified by given `owner_id`.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_shape_owners**()

Returns an [Array](class_array.md#class-array) of `owner_id` identifiers. You can use these ids in other methods that take `owner_id` as an argument.

---

[bool](class_bool.md#class-bool) **is_shape_owner_disabled**(owner_id: [int](class_int.md#class-int))

If `true`, the shape owner and its shapes are disabled.

---

[bool](class_bool.md#class-bool) **is_shape_owner_one_way_collision_enabled**(owner_id: [int](class_int.md#class-int))

Returns `true` if collisions for the shape owner originating from this **CollisionObject2D** will not be reported to collided with **CollisionObject2D**s.

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

 **shape_owner_add_shape**(owner_id: [int](class_int.md#class-int), shape: [Shape2D](class_shape2d.md#class-shape2d))

Adds a [Shape2D](class_shape2d.md#class-shape2d) to the shape owner.

---

 **shape_owner_clear_shapes**(owner_id: [int](class_int.md#class-int))

Removes all shapes from the shape owner.

---

[Object](class_object.md#class-object) **shape_owner_get_owner**(owner_id: [int](class_int.md#class-int))

Returns the parent object of the given shape owner.

---

[Shape2D](class_shape2d.md#class-shape2d) **shape_owner_get_shape**(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))

Returns the [Shape2D](class_shape2d.md#class-shape2d) with the given ID from the given shape owner.

---

[int](class_int.md#class-int) **shape_owner_get_shape_count**(owner_id: [int](class_int.md#class-int))

Returns the number of shapes the given shape owner contains.

---

[int](class_int.md#class-int) **shape_owner_get_shape_index**(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))

Returns the child index of the [Shape2D](class_shape2d.md#class-shape2d) with the given ID from the given shape owner.

---

[Transform2D](class_transform2d.md#class-transform2d) **shape_owner_get_transform**(owner_id: [int](class_int.md#class-int))

Returns the shape owner's [Transform2D](class_transform2d.md#class-transform2d).

---

 **shape_owner_remove_shape**(owner_id: [int](class_int.md#class-int), shape_id: [int](class_int.md#class-int))

Removes a shape from the given shape owner.

---

 **shape_owner_set_disabled**(owner_id: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

If `true`, disables the given shape owner.

---

 **shape_owner_set_one_way_collision**(owner_id: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

If `enable` is `true`, collisions for the shape owner originating from this **CollisionObject2D** will not be reported to collided with **CollisionObject2D**s.

---

 **shape_owner_set_one_way_collision_direction**(owner_id: [int](class_int.md#class-int), direction: [Vector2](class_vector2.md#class-vector2))

Sets the `one_way_collision_direction` of the shape owner identified by the given `owner_id` to `direction`.

---

 **shape_owner_set_one_way_collision_margin**(owner_id: [int](class_int.md#class-int), margin: [float](class_float.md#class-float))

Sets the `one_way_collision_margin` of the shape owner identified by given `owner_id` to `margin` pixels.

---

 **shape_owner_set_transform**(owner_id: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the [Transform2D](class_transform2d.md#class-transform2d) of the given shape owner.
