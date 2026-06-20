# PinJoint2D

**Inherits:** [Joint2D](class_joint2d.md#class-joint2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that attaches two 2D physics bodies at a single point, allowing them to freely rotate.

## Description

A physics joint that attaches two 2D physics bodies at a single point, allowing them to freely rotate. For example, a [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d) can be attached to a [StaticBody2D](class_staticbody2d.md#class-staticbody2d) to create a pendulum or a seesaw.

## Properties

| [bool](class_bool.md#class-bool)    | angular_limit_enabled   | `false`   |
|-------------------------------------|-----------------------------------------------------------------------------|-----------|
| [float](class_float.md#class-float) | angular_limit_lower       | `0.0`     |
| [float](class_float.md#class-float) | angular_limit_upper       | `0.0`     |
| [bool](class_bool.md#class-bool)    | motor_enabled                   | `false`   |
| [float](class_float.md#class-float) | motor_target_velocity   | `0.0`     |
| [float](class_float.md#class-float) | softness                             | `0.0`     |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **angular_limit_enabled** = `false`

-  **set_angular_limit_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_angular_limit_enabled**()

If `true`, the pin maximum and minimum rotation, defined by angular_limit_lower and angular_limit_upper are applied.

---

[float](class_float.md#class-float) **angular_limit_lower** = `0.0`

-  **set_angular_limit_lower**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_angular_limit_lower**()

The minimum rotation. Only active if angular_limit_enabled is `true`.

---

[float](class_float.md#class-float) **angular_limit_upper** = `0.0`

-  **set_angular_limit_upper**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_angular_limit_upper**()

The maximum rotation. Only active if angular_limit_enabled is `true`.

---

[bool](class_bool.md#class-bool) **motor_enabled** = `false`

-  **set_motor_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_motor_enabled**()

When activated, a motor turns the pin.

---

[float](class_float.md#class-float) **motor_target_velocity** = `0.0`

-  **set_motor_target_velocity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_motor_target_velocity**()

Target speed for the motor. In radians per second.

---

[float](class_float.md#class-float) **softness** = `0.0`

-  **set_softness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_softness**()

The higher this value, the more the bond to the pinned partner can flex.
