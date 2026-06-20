# PinJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class-joint3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate.

## Description

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate. For example, a [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) can be attached to a [StaticBody3D](class_staticbody3d.md#class-staticbody3d) to create a pendulum or a seesaw.

## Properties

| [float](class_float.md#class-float)   | params/bias                   | `0.3`   |
|---------------------------------------|-------------------------------------------------------------------------|---------|
| [float](class_float.md#class-float)   | params/damping             | `1.0`   |
| [float](class_float.md#class-float)   | params/impulse_clamp | `0.0`   |

## Methods

| [float](class_float.md#class-float)   | get_param(param: Param)                                             |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
|                                       | set_param(param: Param, value: [float](class_float.md#class-float)) |

---

## Enumerations

enum **Param**:

Param **PARAM_BIAS** = `0`

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.

Param **PARAM_DAMPING** = `1`

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.

Param **PARAM_IMPULSE_CLAMP** = `2`

If above 0, this value is the maximum value for an impulse that this Joint3D produces.

---

## Property Descriptions

[float](class_float.md#class-float) **params/bias** = `0.3`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.

---

[float](class_float.md#class-float) **params/damping** = `1.0`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.

---

[float](class_float.md#class-float) **params/impulse_clamp** = `0.0`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

If above 0, this value is the maximum value for an impulse that this Joint3D produces.

---

## Method Descriptions

[float](class_float.md#class-float) **get_param**(param: Param)

Returns the value of the specified parameter.

---

 **set_param**(param: Param, value: [float](class_float.md#class-float))

Sets the value of the specified parameter.
