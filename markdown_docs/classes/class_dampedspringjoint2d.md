# DampedSpringJoint2D

**Inherits:** [Joint2D](class_joint2d.md#class-joint2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that connects two 2D physics bodies with a spring-like force.

## Description

A physics joint that connects two 2D physics bodies with a spring-like force. This behaves like a spring that always wants to stretch to a given length.

## Properties

| [float](class_float.md#class-float)   | damping         | `1.0`   |
|---------------------------------------|----------------------------------------------------------------|---------|
| [float](class_float.md#class-float)   | length           | `50.0`  |
| [float](class_float.md#class-float)   | rest_length | `0.0`   |
| [float](class_float.md#class-float)   | stiffness     | `20.0`  |

---

## Property Descriptions

[float](class_float.md#class-float) **damping** = `1.0`

-  **set_damping**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_damping**()

The spring joint's damping ratio. A value between `0` and `1`. When the two bodies move into different directions the system tries to align them to the spring axis again. A high damping value forces the attached bodies to align faster.

---

[float](class_float.md#class-float) **length** = `50.0`

-  **set_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_length**()

The spring joint's maximum length. The two attached bodies cannot stretch it past this value.

---

[float](class_float.md#class-float) **rest_length** = `0.0`

-  **set_rest_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_rest_length**()

When the bodies attached to the spring joint move they stretch or squash it. The joint always tries to resize towards this length.

---

[float](class_float.md#class-float) **stiffness** = `20.0`

-  **set_stiffness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_stiffness**()

The higher the value, the less the bodies attached to the joint will deform it. The joint applies an opposing force to the bodies, the product of the stiffness multiplied by the size difference from its resting length.
