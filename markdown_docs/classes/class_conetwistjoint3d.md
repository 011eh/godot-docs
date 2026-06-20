# ConeTwistJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class-joint3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint.

## Description

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint. The twist axis is initiated as the X axis of the **ConeTwistJoint3D**. Once the physics bodies swing, the twist axis is calculated as the middle of the X axes of the joint in the local space of the two physics bodies. Useful for limbs like shoulders and hips, lamps hanging off a ceiling, etc.

## Properties

| [float](class_float.md#class-float)   | bias             | `0.3`       |
|---------------------------------------|-----------------------------------------------------------|-------------|
| [float](class_float.md#class-float)   | relaxation | `1.0`       |
| [float](class_float.md#class-float)   | softness     | `0.8`       |
| [float](class_float.md#class-float)   | swing_span | `0.7853982` |
| [float](class_float.md#class-float)   | twist_span | `3.1415927` |

## Methods

| [float](class_float.md#class-float)   | get_param(param: Param)                                             |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
|                                       | set_param(param: Param, value: [float](class_float.md#class-float)) |

---

## Enumerations

enum **Param**:

Param **PARAM_SWING_SPAN** = `0`

Swing is rotation from side to side, around the axis perpendicular to the twist axis.

The swing span defines, how much rotation will not get corrected along the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.

Param **PARAM_TWIST_SPAN** = `1`

Twist is the rotation around the twist axis, this value defined how far the joint can twist.

Twist is locked if below 0.05.

Param **PARAM_BIAS** = `2`

The speed with which the swing or twist will take place.

The higher, the faster.

Param **PARAM_SOFTNESS** = `3`

The ease with which the joint starts to twist. If it's too low, it takes more force to start twisting the joint.

Param **PARAM_RELAXATION** = `4`

Defines, how fast the swing- and twist-speed-difference on both sides gets synced.

Param **PARAM_MAX** = `5`

Represents the size of the Param enum.

---

## Property Descriptions

[float](class_float.md#class-float) **bias** = `0.3`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The speed with which the swing or twist will take place.

The higher, the faster.

---

[float](class_float.md#class-float) **relaxation** = `1.0`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

Defines, how fast the swing- and twist-speed-difference on both sides gets synced.

---

[float](class_float.md#class-float) **softness** = `0.8`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The ease with which the joint starts to twist. If it's too low, it takes more force to start twisting the joint.

---

[float](class_float.md#class-float) **swing_span** = `0.7853982`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

Swing is rotation from side to side, around the axis perpendicular to the twist axis.

The swing span defines, how much rotation will not get corrected along the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.

---

[float](class_float.md#class-float) **twist_span** = `3.1415927`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

Twist is the rotation around the twist axis, this value defined how far the joint can twist.

Twist is locked if below 0.05.

---

## Method Descriptions

[float](class_float.md#class-float) **get_param**(param: Param)

Returns the value of the specified parameter.

---

 **set_param**(param: Param, value: [float](class_float.md#class-float))

Sets the value of the specified parameter.
