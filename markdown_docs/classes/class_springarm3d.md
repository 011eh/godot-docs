# SpringArm3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A 3D raycast that dynamically moves its children near the collision point.

## Description

**SpringArm3D** casts a ray or a shape along its Z axis and moves all its direct children to the collision point, with an optional margin. This is useful for 3rd person cameras that move closer to the player when inside a tight space (you may need to exclude the player's collider from the **SpringArm3D**'s collision check).

## Tutorials

- [Third-person camera with spring arm](../tutorials/3d/spring_arm.md)

## Properties

| [int](class_int.md#class-int)             | collision_mask   | `1`    |
|-------------------------------------------|----------------------------------------------------------------|--------|
| [float](class_float.md#class-float)       | margin                   | `0.01` |
| [Shape3D](class_shape3d.md#class-shape3d) | shape                     |        |
| [float](class_float.md#class-float)       | spring_length     | `1.0`  |

## Methods

|                                     | add_excluded_object(RID: [RID](class_rid.md#class-rid))       |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
|                                     | clear_excluded_objects()                                   |
| [float](class_float.md#class-float) | get_hit_length()                                                   |
| [bool](class_bool.md#class-bool)    | remove_excluded_object(RID: [RID](class_rid.md#class-rid)) |

---

## Property Descriptions

[int](class_int.md#class-int) **collision_mask** = `1`

-  **set_collision_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_collision_mask**()

The layers against which the collision check will be done. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

---

[float](class_float.md#class-float) **margin** = `0.01`

-  **set_margin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_margin**()

When the collision check is made, a candidate length for the SpringArm3D is given.

The margin is then subtracted to this length and the translation is applied to the child objects of the SpringArm3D.

This margin is useful for when the SpringArm3D has a [Camera3D](class_camera3d.md#class-camera3d) as a child node: without the margin, the [Camera3D](class_camera3d.md#class-camera3d) would be placed on the exact point of collision, while with the margin the [Camera3D](class_camera3d.md#class-camera3d) would be placed close to the point of collision.

---

[Shape3D](class_shape3d.md#class-shape3d) **shape**

-  **set_shape**(value: [Shape3D](class_shape3d.md#class-shape3d))
- [Shape3D](class_shape3d.md#class-shape3d) **get_shape**()

The [Shape3D](class_shape3d.md#class-shape3d) to use for the SpringArm3D.

When the shape is set, the SpringArm3D will cast the [Shape3D](class_shape3d.md#class-shape3d) on its z axis instead of performing a ray cast.

---

[float](class_float.md#class-float) **spring_length** = `1.0`

-  **set_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_length**()

The maximum extent of the SpringArm3D. This is used as a length for both the ray and the shape cast used internally to calculate the desired position of the SpringArm3D's child nodes.

To know more about how to perform a shape cast or a ray cast, please consult the [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) documentation.

---

## Method Descriptions

 **add_excluded_object**(RID: [RID](class_rid.md#class-rid))

Adds the [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) object with the given [RID](class_rid.md#class-rid) to the list of [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) objects excluded from the collision check.

---

 **clear_excluded_objects**()

Clears the list of [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) objects excluded from the collision check.

---

[float](class_float.md#class-float) **get_hit_length**()

Returns the spring arm's current length.

---

[bool](class_bool.md#class-bool) **remove_excluded_object**(RID: [RID](class_rid.md#class-rid))

Removes the given [RID](class_rid.md#class-rid) from the list of [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) objects excluded from the collision check.
