# CollisionShape3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node that provides a [Shape3D](class_shape3d.md#class-shape3d) to a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) parent.

## Description

A node that provides a [Shape3D](class_shape3d.md#class-shape3d) to a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) parent and allows it to be edited. This can give a detection shape to an [Area3D](class_area3d.md#class-area3d) or turn a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) into a solid object.

**Warning:** A non-uniformly scaled **CollisionShape3D** will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its shape resource instead.

## Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)
- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [Color](class_color.md#class-color)       | debug_color   | `Color(0, 0, 0, 0)`   |
|-------------------------------------------|---------------------------------------------------------------|-----------------------|
| [bool](class_bool.md#class-bool)          | debug_fill     | `true`                |
| [bool](class_bool.md#class-bool)          | disabled         | `false`               |
| [Shape3D](class_shape3d.md#class-shape3d) | shape               |                       |

## Methods

|    | make_convex_from_siblings()                                     |
|----|-----------------------------------------------------------------------------------------------------------------------------|
|    | resource_changed(resource: [Resource](class_resource.md#class-resource)) |

---

## Property Descriptions

[Color](class_color.md#class-color) **debug_color** = `Color(0, 0, 0, 0)`

-  **set_debug_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_debug_color**()

The collision shape color that is displayed in the editor, or in the running project if **Debug > Visible Collision Shapes** is checked at the top of the editor.

**Note:** The default value is [ProjectSettings.debug/shapes/collision/shape_color](class_projectsettings.md#class-projectsettings-property-debug-shapes-collision-shape-color). The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.

---

[bool](class_bool.md#class-bool) **debug_fill** = `true`

-  **set_enable_debug_fill**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_debug_fill**()

If `true`, when the shape is displayed, it will show a solid fill color in addition to its wireframe.

---

[bool](class_bool.md#class-bool) **disabled** = `false`

-  **set_disabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_disabled**()

A disabled collision shape has no effect in the world. This property should be changed with [Object.set_deferred()](class_object.md#class-object-method-set-deferred).

---

[Shape3D](class_shape3d.md#class-shape3d) **shape**

-  **set_shape**(value: [Shape3D](class_shape3d.md#class-shape3d))
- [Shape3D](class_shape3d.md#class-shape3d) **get_shape**()

The actual shape owned by this collision shape.

---

## Method Descriptions

 **make_convex_from_siblings**()

Sets the collision shape's shape to the addition of all its convexed [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) siblings geometry.

---

 **resource_changed**(resource: [Resource](class_resource.md#class-resource))

**Deprecated:** Use [Resource.changed](class_resource.md#class-resource-signal-changed) instead.

This method does nothing.
