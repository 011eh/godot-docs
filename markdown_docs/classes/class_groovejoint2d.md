# GrooveJoint2D

**Inherits:** [Joint2D](class_joint2d.md#class-joint2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that restricts the movement of two 2D physics bodies to a fixed axis.

## Description

A physics joint that restricts the movement of two 2D physics bodies to a fixed axis. For example, a [StaticBody2D](class_staticbody2d.md#class-staticbody2d) representing a piston base can be attached to a [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d) representing the piston head, moving up and down.

## Properties

| [float](class_float.md#class-float)   | initial_offset   | `25.0`   |
|---------------------------------------|------------------------------------------------------------------|----------|
| [float](class_float.md#class-float)   | length                   | `50.0`   |

---

## Property Descriptions

[float](class_float.md#class-float) **initial_offset** = `25.0`

-  **set_initial_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_initial_offset**()

The body B's initial anchor position defined by the joint's origin and a local offset initial_offset along the joint's Y axis (along the groove).

---

[float](class_float.md#class-float) **length** = `50.0`

-  **set_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_length**()

The groove's length. The groove is from the joint's origin towards length along the joint's local Y axis.
