# HingeJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class-joint3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body.

## Description

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body. For example, Body A can be a [StaticBody3D](class_staticbody3d.md#class-staticbody3d) representing a door hinge that a [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) rotates around.

## Properties

| [float](class_float.md#class-float)   | angular_limit/bias             | `0.3`        |
|---------------------------------------|-----------------------------------------------------------------------------------|--------------|
| [bool](class_bool.md#class-bool)      | angular_limit/enable         | `false`      |
| [float](class_float.md#class-float)   | angular_limit/lower           | `-1.5707964` |
| [float](class_float.md#class-float)   | angular_limit/relaxation | `1.0`        |
| [float](class_float.md#class-float)   | angular_limit/softness     | `0.9`        |
| [float](class_float.md#class-float)   | angular_limit/upper           | `1.5707964`  |
| [bool](class_bool.md#class-bool)      | motor/enable                         | `false`      |
| [float](class_float.md#class-float)   | motor/max_impulse               | `1.0`        |
| [float](class_float.md#class-float)   | motor/target_velocity       | `1.0`        |
| [float](class_float.md#class-float)   | params/bias                           | `0.3`        |

## Methods

| [bool](class_bool.md#class-bool)    | get_flag(flag: Flag)                                                  |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float) | get_param(param: Param)                                             |
|                                     | set_flag(flag: Flag, enabled: [bool](class_bool.md#class-bool))       |
|                                     | set_param(param: Param, value: [float](class_float.md#class-float)) |

---

## Enumerations

enum **Param**:

Param **PARAM_BIAS** = `0`

The speed with which the two bodies get pulled together when they move in different directions.

Param **PARAM_LIMIT_UPPER** = `1`

The maximum rotation. Only active if angular_limit/enable is `true`.

Param **PARAM_LIMIT_LOWER** = `2`

The minimum rotation. Only active if angular_limit/enable is `true`.

Param **PARAM_LIMIT_BIAS** = `3`

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.

Param **PARAM_LIMIT_SOFTNESS** = `4`

**Deprecated:** This property is never used by the engine and is kept for compatibility purpose.

Param **PARAM_LIMIT_RELAXATION** = `5`

The lower this value, the more the rotation gets slowed down.

Param **PARAM_MOTOR_TARGET_VELOCITY** = `6`

Target speed for the motor.

Param **PARAM_MOTOR_MAX_IMPULSE** = `7`

Maximum acceleration for the motor.

Param **PARAM_MAX** = `8`

Represents the size of the Param enum.

---

enum **Flag**:

Flag **FLAG_USE_LIMIT** = `0`

If `true`, the hinges maximum and minimum rotation, defined by angular_limit/lower and angular_limit/upper has effects.

Flag **FLAG_ENABLE_MOTOR** = `1`

When activated, a motor turns the hinge.

Flag **FLAG_MAX** = `2`

Represents the size of the Flag enum.

---

## Property Descriptions

[float](class_float.md#class-float) **angular_limit/bias** = `0.3`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.

---

[bool](class_bool.md#class-bool) **angular_limit/enable** = `false`

-  **set_flag**(flag: Flag, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag**(flag: Flag) 

If `true`, the hinges maximum and minimum rotation, defined by angular_limit/lower and angular_limit/upper has effects.

---

[float](class_float.md#class-float) **angular_limit/lower** = `-1.5707964`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The minimum rotation. Only active if angular_limit/enable is `true`.

---

[float](class_float.md#class-float) **angular_limit/relaxation** = `1.0`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The lower this value, the more the rotation gets slowed down.

---

[float](class_float.md#class-float) **angular_limit/softness** = `0.9`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

**Deprecated:** This property is never set by the engine and is kept for compatibility purposes.

---

[float](class_float.md#class-float) **angular_limit/upper** = `1.5707964`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The maximum rotation. Only active if angular_limit/enable is `true`.

---

[bool](class_bool.md#class-bool) **motor/enable** = `false`

-  **set_flag**(flag: Flag, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag**(flag: Flag) 

When activated, a motor turns the hinge.

---

[float](class_float.md#class-float) **motor/max_impulse** = `1.0`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

Maximum acceleration for the motor.

---

[float](class_float.md#class-float) **motor/target_velocity** = `1.0`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

Target speed for the motor.

---

[float](class_float.md#class-float) **params/bias** = `0.3`

-  **set_param**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param**(param: Param) 

The speed with which the two bodies get pulled together when they move in different directions.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **get_flag**(flag: Flag)

Returns the value of the specified flag.

---

[float](class_float.md#class-float) **get_param**(param: Param)

Returns the value of the specified parameter.

---

 **set_flag**(flag: Flag, enabled: [bool](class_bool.md#class-bool))

If `true`, enables the specified flag.

---

 **set_param**(param: Param, value: [float](class_float.md#class-float))

Sets the value of the specified parameter.
