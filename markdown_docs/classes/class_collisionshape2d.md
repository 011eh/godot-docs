# CollisionShape2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node that provides a [Shape2D](class_shape2d.md#class-shape2d) to a [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d) parent.

## Description

A node that provides a [Shape2D](class_shape2d.md#class-shape2d) to a [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d) parent and allows it to be edited. This can give a detection shape to an [Area2D](class_area2d.md#class-area2d) or turn a [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) into a solid object.

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)
- [2D Pong Demo](https://godotengine.org/asset-library/asset/2728)
- [2D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2719)

## Properties

| [Color](class_color.md#class-color)       | debug_color                                 | `Color(0, 0, 0, 0)`   |
|-------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------|
| [bool](class_bool.md#class-bool)          | disabled                                       | `false`               |
| [bool](class_bool.md#class-bool)          | one_way_collision                     | `false`               |
| [Vector2](class_vector2.md#class-vector2) | one_way_collision_direction | `Vector2(0, 1)`       |
| [float](class_float.md#class-float)       | one_way_collision_margin       | `1.0`                 |
| [Shape2D](class_shape2d.md#class-shape2d) | shape                                             |                       |

---

## Property Descriptions

[Color](class_color.md#class-color) **debug_color** = `Color(0, 0, 0, 0)`

-  **set_debug_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_debug_color**()

The collision shape color that is displayed in the editor, or in the running project if **Debug > Visible Collision Shapes** is checked at the top of the editor.

**Note:** The default value is [ProjectSettings.debug/shapes/collision/shape_color](class_projectsettings.md#class-projectsettings-property-debug-shapes-collision-shape-color). The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.

---

[bool](class_bool.md#class-bool) **disabled** = `false`

-  **set_disabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_disabled**()

A disabled collision shape has no effect in the world. This property should be changed with [Object.set_deferred()](class_object.md#class-object-method-set-deferred).

---

[bool](class_bool.md#class-bool) **one_way_collision** = `false`

-  **set_one_way_collision**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_one_way_collision_enabled**()

Sets whether this collision shape should only detect collision on one side (top or bottom).

**Note:** This property has no effect if this **CollisionShape2D** is a child of an [Area2D](class_area2d.md#class-area2d) node.

**Note:** The one way collision direction can be configured by setting one_way_collision_direction.

---

[Vector2](class_vector2.md#class-vector2) **one_way_collision_direction** = `Vector2(0, 1)`

-  **set_one_way_collision_direction**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_one_way_collision_direction**()

The direction used for one-way collision.

---

[float](class_float.md#class-float) **one_way_collision_margin** = `1.0`

-  **set_one_way_collision_margin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_one_way_collision_margin**()

The margin used for one-way collision (in pixels). Higher values will make the shape thicker, and work better for colliders that enter the shape at a high velocity.

---

[Shape2D](class_shape2d.md#class-shape2d) **shape**

-  **set_shape**(value: [Shape2D](class_shape2d.md#class-shape2d))
- [Shape2D](class_shape2d.md#class-shape2d) **get_shape**()

The actual shape owned by this collision shape.
