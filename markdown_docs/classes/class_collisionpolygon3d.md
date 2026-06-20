# CollisionPolygon3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node that provides a thickened polygon shape (a prism) to a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) parent.

## Description

A node that provides a thickened polygon shape (a prism) to a [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an [Area3D](class_area3d.md#class-area3d) or turn a [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d) into a solid object.

**Warning:** A non-uniformly scaled [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its shape resource instead.

## Properties

| [Color](class_color.md#class-color)                                        | debug_color   | `Color(0, 0, 0, 0)`    |
|----------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| [bool](class_bool.md#class-bool)                                           | debug_fill     | `true`                 |
| [float](class_float.md#class-float)                                        | depth               | `1.0`                  |
| [bool](class_bool.md#class-bool)                                           | disabled         | `false`                |
| [float](class_float.md#class-float)                                        | margin             | `0.04`                 |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | polygon           | `PackedVector2Array()` |

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

[float](class_float.md#class-float) **depth** = `1.0`

-  **set_depth**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth**()

Length that the resulting collision extends in either direction perpendicular to its 2D polygon.

---

[bool](class_bool.md#class-bool) **disabled** = `false`

-  **set_disabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_disabled**()

If `true`, no collision will be produced. This property should be changed with [Object.set_deferred()](class_object.md#class-object-method-set-deferred).

---

[float](class_float.md#class-float) **margin** = `0.04`

-  **set_margin**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_margin**()

The collision margin for the generated [Shape3D](class_shape3d.md#class-shape3d). See [Shape3D.margin](class_shape3d.md#class-shape3d-property-margin) for more details.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **polygon** = `PackedVector2Array()`

-  **set_polygon**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_polygon**()

Array of vertices which define the 2D polygon in the local XY plane.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.
