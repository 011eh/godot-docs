# Generic6DOFJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class-joint3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A physics joint that allows for complex movement and rotation between two 3D physics bodies.

## Description

The **Generic6DOFJoint3D** (6 Degrees Of Freedom) joint allows for implementing custom types of joints by locking the rotation and translation of certain axes.

The first 3 DOF represent the linear motion of the physics bodies and the last 3 DOF represent the angular motion of the physics bodies. Each axis can be either locked, or limited.

## Properties

| [float](class_float.md#class-float)   | angular_limit_x/damping                       | `1.0`   |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)      | angular_limit_x/enabled                       | `true`  |
| [float](class_float.md#class-float)   | angular_limit_x/erp                               | `0.5`   |
| [float](class_float.md#class-float)   | angular_limit_x/force_limit               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_x/lower_angle               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_x/restitution               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_x/softness                     | `0.5`   |
| [float](class_float.md#class-float)   | angular_limit_x/upper_angle               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_y/damping                       | `1.0`   |
| [bool](class_bool.md#class-bool)      | angular_limit_y/enabled                       | `true`  |
| [float](class_float.md#class-float)   | angular_limit_y/erp                               | `0.5`   |
| [float](class_float.md#class-float)   | angular_limit_y/force_limit               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_y/lower_angle               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_y/restitution               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_y/softness                     | `0.5`   |
| [float](class_float.md#class-float)   | angular_limit_y/upper_angle               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_z/damping                       | `1.0`   |
| [bool](class_bool.md#class-bool)      | angular_limit_z/enabled                       | `true`  |
| [float](class_float.md#class-float)   | angular_limit_z/erp                               | `0.5`   |
| [float](class_float.md#class-float)   | angular_limit_z/force_limit               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_z/lower_angle               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_z/restitution               | `0.0`   |
| [float](class_float.md#class-float)   | angular_limit_z/softness                     | `0.5`   |
| [float](class_float.md#class-float)   | angular_limit_z/upper_angle               | `0.0`   |
| [bool](class_bool.md#class-bool)      | angular_motor_x/enabled                       | `false` |
| [float](class_float.md#class-float)   | angular_motor_x/force_limit               | `300.0` |
| [float](class_float.md#class-float)   | angular_motor_x/target_velocity       | `0.0`   |
| [bool](class_bool.md#class-bool)      | angular_motor_y/enabled                       | `false` |
| [float](class_float.md#class-float)   | angular_motor_y/force_limit               | `300.0` |
| [float](class_float.md#class-float)   | angular_motor_y/target_velocity       | `0.0`   |
| [bool](class_bool.md#class-bool)      | angular_motor_z/enabled                       | `false` |
| [float](class_float.md#class-float)   | angular_motor_z/force_limit               | `300.0` |
| [float](class_float.md#class-float)   | angular_motor_z/target_velocity       | `0.0`   |
| [float](class_float.md#class-float)   | angular_spring_x/damping                     | `0.0`   |
| [bool](class_bool.md#class-bool)      | angular_spring_x/enabled                     | `false` |
| [float](class_float.md#class-float)   | angular_spring_x/equilibrium_point | `0.0`   |
| [float](class_float.md#class-float)   | angular_spring_x/stiffness                 | `0.0`   |
| [float](class_float.md#class-float)   | angular_spring_y/damping                     | `0.0`   |
| [bool](class_bool.md#class-bool)      | angular_spring_y/enabled                     | `false` |
| [float](class_float.md#class-float)   | angular_spring_y/equilibrium_point | `0.0`   |
| [float](class_float.md#class-float)   | angular_spring_y/stiffness                 | `0.0`   |
| [float](class_float.md#class-float)   | angular_spring_z/damping                     | `0.0`   |
| [bool](class_bool.md#class-bool)      | angular_spring_z/enabled                     | `false` |
| [float](class_float.md#class-float)   | angular_spring_z/equilibrium_point | `0.0`   |
| [float](class_float.md#class-float)   | angular_spring_z/stiffness                 | `0.0`   |
| [float](class_float.md#class-float)   | linear_limit_x/damping                         | `1.0`   |
| [bool](class_bool.md#class-bool)      | linear_limit_x/enabled                         | `true`  |
| [float](class_float.md#class-float)   | linear_limit_x/lower_distance           | `0.0`   |
| [float](class_float.md#class-float)   | linear_limit_x/restitution                 | `0.5`   |
| [float](class_float.md#class-float)   | linear_limit_x/softness                       | `0.7`   |
| [float](class_float.md#class-float)   | linear_limit_x/upper_distance           | `0.0`   |
| [float](class_float.md#class-float)   | linear_limit_y/damping                         | `1.0`   |
| [bool](class_bool.md#class-bool)      | linear_limit_y/enabled                         | `true`  |
| [float](class_float.md#class-float)   | linear_limit_y/lower_distance           | `0.0`   |
| [float](class_float.md#class-float)   | linear_limit_y/restitution                 | `0.5`   |
| [float](class_float.md#class-float)   | linear_limit_y/softness                       | `0.7`   |
| [float](class_float.md#class-float)   | linear_limit_y/upper_distance           | `0.0`   |
| [float](class_float.md#class-float)   | linear_limit_z/damping                         | `1.0`   |
| [bool](class_bool.md#class-bool)      | linear_limit_z/enabled                         | `true`  |
| [float](class_float.md#class-float)   | linear_limit_z/lower_distance           | `0.0`   |
| [float](class_float.md#class-float)   | linear_limit_z/restitution                 | `0.5`   |
| [float](class_float.md#class-float)   | linear_limit_z/softness                       | `0.7`   |
| [float](class_float.md#class-float)   | linear_limit_z/upper_distance           | `0.0`   |
| [bool](class_bool.md#class-bool)      | linear_motor_x/enabled                         | `false` |
| [float](class_float.md#class-float)   | linear_motor_x/force_limit                 | `0.0`   |
| [float](class_float.md#class-float)   | linear_motor_x/target_velocity         | `0.0`   |
| [bool](class_bool.md#class-bool)      | linear_motor_y/enabled                         | `false` |
| [float](class_float.md#class-float)   | linear_motor_y/force_limit                 | `0.0`   |
| [float](class_float.md#class-float)   | linear_motor_y/target_velocity         | `0.0`   |
| [bool](class_bool.md#class-bool)      | linear_motor_z/enabled                         | `false` |
| [float](class_float.md#class-float)   | linear_motor_z/force_limit                 | `0.0`   |
| [float](class_float.md#class-float)   | linear_motor_z/target_velocity         | `0.0`   |
| [float](class_float.md#class-float)   | linear_spring_x/damping                       | `0.01`  |
| [bool](class_bool.md#class-bool)      | linear_spring_x/enabled                       | `false` |
| [float](class_float.md#class-float)   | linear_spring_x/equilibrium_point   | `0.0`   |
| [float](class_float.md#class-float)   | linear_spring_x/stiffness                   | `0.01`  |
| [float](class_float.md#class-float)   | linear_spring_y/damping                       | `0.01`  |
| [bool](class_bool.md#class-bool)      | linear_spring_y/enabled                       | `false` |
| [float](class_float.md#class-float)   | linear_spring_y/equilibrium_point   | `0.0`   |
| [float](class_float.md#class-float)   | linear_spring_y/stiffness                   | `0.01`  |
| [float](class_float.md#class-float)   | linear_spring_z/damping                       | `0.01`  |
| [bool](class_bool.md#class-bool)      | linear_spring_z/enabled                       | `false` |
| [float](class_float.md#class-float)   | linear_spring_z/equilibrium_point   | `0.0`   |
| [float](class_float.md#class-float)   | linear_spring_z/stiffness                   | `0.01`  |

## Methods

| [bool](class_bool.md#class-bool)    | get_flag_x(flag: Flag)                                                  |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)    | get_flag_y(flag: Flag)                                                  |
| [bool](class_bool.md#class-bool)    | get_flag_z(flag: Flag)                                                  |
| [float](class_float.md#class-float) | get_param_x(param: Param)                                             |
| [float](class_float.md#class-float) | get_param_y(param: Param)                                             |
| [float](class_float.md#class-float) | get_param_z(param: Param)                                             |
|                                     | set_flag_x(flag: Flag, value: [bool](class_bool.md#class-bool))         |
|                                     | set_flag_y(flag: Flag, value: [bool](class_bool.md#class-bool))         |
|                                     | set_flag_z(flag: Flag, value: [bool](class_bool.md#class-bool))         |
|                                     | set_param_x(param: Param, value: [float](class_float.md#class-float)) |
|                                     | set_param_y(param: Param, value: [float](class_float.md#class-float)) |
|                                     | set_param_z(param: Param, value: [float](class_float.md#class-float)) |

---

## Enumerations

enum **Param**:

Param **PARAM_LINEAR_LOWER_LIMIT** = `0`

The minimum difference between the pivot points' axes.

Param **PARAM_LINEAR_UPPER_LIMIT** = `1`

The maximum difference between the pivot points' axes.

Param **PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

A factor applied to the movement across the axes. The lower, the slower the movement.

Param **PARAM_LINEAR_RESTITUTION** = `3`

The amount of restitution on the axes' movement. The lower, the more momentum gets lost.

Param **PARAM_LINEAR_DAMPING** = `4`

The amount of damping that happens at the linear motion across the axes.

Param **PARAM_LINEAR_MOTOR_TARGET_VELOCITY** = `5`

The velocity the linear motor will try to reach.

Param **PARAM_LINEAR_MOTOR_FORCE_LIMIT** = `6`

The maximum force the linear motor will apply while trying to reach the velocity target.

Param **PARAM_LINEAR_SPRING_STIFFNESS** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

Param **PARAM_LINEAR_SPRING_DAMPING** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

Param **PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

Param **PARAM_ANGULAR_LOWER_LIMIT** = `10`

The minimum rotation in negative direction to break loose and rotate around the axes.

Param **PARAM_ANGULAR_UPPER_LIMIT** = `11`

The minimum rotation in positive direction to break loose and rotate around the axes.

Param **PARAM_ANGULAR_LIMIT_SOFTNESS** = `12`

The speed of all rotations across the axes.

Param **PARAM_ANGULAR_DAMPING** = `13`

The amount of rotational damping across the axes. The lower, the more damping occurs.

Param **PARAM_ANGULAR_RESTITUTION** = `14`

The amount of rotational restitution across the axes. The lower, the more restitution occurs.

Param **PARAM_ANGULAR_FORCE_LIMIT** = `15`

The maximum amount of force that can occur, when rotating around the axes.

Param **PARAM_ANGULAR_ERP** = `16`

When rotating across the axes, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

Param **PARAM_ANGULAR_MOTOR_TARGET_VELOCITY** = `17`

Target speed for the motor at the axes.

Param **PARAM_ANGULAR_MOTOR_FORCE_LIMIT** = `18`

Maximum acceleration for the motor at the axes.

Param **PARAM_ANGULAR_SPRING_STIFFNESS** = `19`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

Param **PARAM_ANGULAR_SPRING_DAMPING** = `20`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

Param **PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT** = `21`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

Param **PARAM_MAX** = `22`

Represents the size of the Param enum.

---

enum **Flag**:

Flag **FLAG_ENABLE_LINEAR_LIMIT** = `0`

If enabled, linear motion is possible within the given limits.

Flag **FLAG_ENABLE_ANGULAR_LIMIT** = `1`

If enabled, rotational motion is possible within the given limits.

Flag **FLAG_ENABLE_LINEAR_SPRING** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

Flag **FLAG_ENABLE_ANGULAR_SPRING** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

Flag **FLAG_ENABLE_MOTOR** = `4`

If enabled, there is a rotational motor across these axes.

Flag **FLAG_ENABLE_LINEAR_MOTOR** = `5`

If enabled, there is a linear motor across these axes.

Flag **FLAG_MAX** = `6`

Represents the size of the Flag enum.

---

## Property Descriptions

[float](class_float.md#class-float) **angular_limit_x/damping** = `1.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The amount of rotational damping across the X axis.

The lower, the longer an impulse from one side takes to travel to the other side.

---

[bool](class_bool.md#class-bool) **angular_limit_x/enabled** = `true`

-  **set_flag_x**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: Flag) 

If `true`, rotation across the X axis is limited.

---

[float](class_float.md#class-float) **angular_limit_x/erp** = `0.5`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

When rotating across the X axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---

[float](class_float.md#class-float) **angular_limit_x/force_limit** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The maximum amount of force that can occur, when rotating around the X axis.

---

[float](class_float.md#class-float) **angular_limit_x/lower_angle** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The minimum rotation in negative direction to break loose and rotate around the X axis.

---

[float](class_float.md#class-float) **angular_limit_x/restitution** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The amount of rotational restitution across the X axis. The lower, the more restitution occurs.

---

[float](class_float.md#class-float) **angular_limit_x/softness** = `0.5`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The speed of all rotations across the X axis.

---

[float](class_float.md#class-float) **angular_limit_x/upper_angle** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The minimum rotation in positive direction to break loose and rotate around the X axis.

---

[float](class_float.md#class-float) **angular_limit_y/damping** = `1.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The amount of rotational damping across the Y axis. The lower, the more damping occurs.

---

[bool](class_bool.md#class-bool) **angular_limit_y/enabled** = `true`

-  **set_flag_y**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: Flag) 

If `true`, rotation across the Y axis is limited.

---

[float](class_float.md#class-float) **angular_limit_y/erp** = `0.5`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

When rotating across the Y axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---

[float](class_float.md#class-float) **angular_limit_y/force_limit** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The maximum amount of force that can occur, when rotating around the Y axis.

---

[float](class_float.md#class-float) **angular_limit_y/lower_angle** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The minimum rotation in negative direction to break loose and rotate around the Y axis.

---

[float](class_float.md#class-float) **angular_limit_y/restitution** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The amount of rotational restitution across the Y axis. The lower, the more restitution occurs.

---

[float](class_float.md#class-float) **angular_limit_y/softness** = `0.5`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The speed of all rotations across the Y axis.

---

[float](class_float.md#class-float) **angular_limit_y/upper_angle** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The minimum rotation in positive direction to break loose and rotate around the Y axis.

---

[float](class_float.md#class-float) **angular_limit_z/damping** = `1.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The amount of rotational damping across the Z axis. The lower, the more damping occurs.

---

[bool](class_bool.md#class-bool) **angular_limit_z/enabled** = `true`

-  **set_flag_z**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: Flag) 

If `true`, rotation across the Z axis is limited.

---

[float](class_float.md#class-float) **angular_limit_z/erp** = `0.5`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

When rotating across the Z axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---

[float](class_float.md#class-float) **angular_limit_z/force_limit** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The maximum amount of force that can occur, when rotating around the Z axis.

---

[float](class_float.md#class-float) **angular_limit_z/lower_angle** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The minimum rotation in negative direction to break loose and rotate around the Z axis.

---

[float](class_float.md#class-float) **angular_limit_z/restitution** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The amount of rotational restitution across the Z axis. The lower, the more restitution occurs.

---

[float](class_float.md#class-float) **angular_limit_z/softness** = `0.5`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The speed of all rotations across the Z axis.

---

[float](class_float.md#class-float) **angular_limit_z/upper_angle** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The minimum rotation in positive direction to break loose and rotate around the Z axis.

---

[bool](class_bool.md#class-bool) **angular_motor_x/enabled** = `false`

-  **set_flag_x**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: Flag) 

If `true`, a rotating motor at the X axis is enabled.

---

[float](class_float.md#class-float) **angular_motor_x/force_limit** = `300.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

Maximum acceleration for the motor at the X axis.

---

[float](class_float.md#class-float) **angular_motor_x/target_velocity** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

Target speed for the motor at the X axis.

---

[bool](class_bool.md#class-bool) **angular_motor_y/enabled** = `false`

-  **set_flag_y**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: Flag) 

If `true`, a rotating motor at the Y axis is enabled.

---

[float](class_float.md#class-float) **angular_motor_y/force_limit** = `300.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

Maximum acceleration for the motor at the Y axis.

---

[float](class_float.md#class-float) **angular_motor_y/target_velocity** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

Target speed for the motor at the Y axis.

---

[bool](class_bool.md#class-bool) **angular_motor_z/enabled** = `false`

-  **set_flag_z**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: Flag) 

If `true`, a rotating motor at the Z axis is enabled.

---

[float](class_float.md#class-float) **angular_motor_z/force_limit** = `300.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

Maximum acceleration for the motor at the Z axis.

---

[float](class_float.md#class-float) **angular_motor_z/target_velocity** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

Target speed for the motor at the Z axis.

---

[float](class_float.md#class-float) **angular_spring_x/damping** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **angular_spring_x/enabled** = `false`

-  **set_flag_x**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: Flag) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **angular_spring_x/equilibrium_point** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **angular_spring_x/stiffness** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **angular_spring_y/damping** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **angular_spring_y/enabled** = `false`

-  **set_flag_y**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: Flag) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **angular_spring_y/equilibrium_point** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **angular_spring_y/stiffness** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **angular_spring_z/damping** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **angular_spring_z/enabled** = `false`

-  **set_flag_z**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: Flag) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **angular_spring_z/equilibrium_point** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **angular_spring_z/stiffness** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_limit_x/damping** = `1.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The amount of damping that happens at the X motion.

---

[bool](class_bool.md#class-bool) **linear_limit_x/enabled** = `true`

-  **set_flag_x**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: Flag) 

If `true`, the linear motion across the X axis is limited.

---

[float](class_float.md#class-float) **linear_limit_x/lower_distance** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The minimum difference between the pivot points' X axis.

---

[float](class_float.md#class-float) **linear_limit_x/restitution** = `0.5`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The amount of restitution on the X axis movement. The lower, the more momentum gets lost.

---

[float](class_float.md#class-float) **linear_limit_x/softness** = `0.7`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

A factor applied to the movement across the X axis. The lower, the slower the movement.

---

[float](class_float.md#class-float) **linear_limit_x/upper_distance** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The maximum difference between the pivot points' X axis.

---

[float](class_float.md#class-float) **linear_limit_y/damping** = `1.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The amount of damping that happens at the Y motion.

---

[bool](class_bool.md#class-bool) **linear_limit_y/enabled** = `true`

-  **set_flag_y**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: Flag) 

If `true`, the linear motion across the Y axis is limited.

---

[float](class_float.md#class-float) **linear_limit_y/lower_distance** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The minimum difference between the pivot points' Y axis.

---

[float](class_float.md#class-float) **linear_limit_y/restitution** = `0.5`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The amount of restitution on the Y axis movement. The lower, the more momentum gets lost.

---

[float](class_float.md#class-float) **linear_limit_y/softness** = `0.7`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

A factor applied to the movement across the Y axis. The lower, the slower the movement.

---

[float](class_float.md#class-float) **linear_limit_y/upper_distance** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The maximum difference between the pivot points' Y axis.

---

[float](class_float.md#class-float) **linear_limit_z/damping** = `1.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The amount of damping that happens at the Z motion.

---

[bool](class_bool.md#class-bool) **linear_limit_z/enabled** = `true`

-  **set_flag_z**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: Flag) 

If `true`, the linear motion across the Z axis is limited.

---

[float](class_float.md#class-float) **linear_limit_z/lower_distance** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The minimum difference between the pivot points' Z axis.

---

[float](class_float.md#class-float) **linear_limit_z/restitution** = `0.5`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The amount of restitution on the Z axis movement. The lower, the more momentum gets lost.

---

[float](class_float.md#class-float) **linear_limit_z/softness** = `0.7`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

A factor applied to the movement across the Z axis. The lower, the slower the movement.

---

[float](class_float.md#class-float) **linear_limit_z/upper_distance** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The maximum difference between the pivot points' Z axis.

---

[bool](class_bool.md#class-bool) **linear_motor_x/enabled** = `false`

-  **set_flag_x**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: Flag) 

If `true`, then there is a linear motor on the X axis. It will attempt to reach the target velocity while staying within the force limits.

---

[float](class_float.md#class-float) **linear_motor_x/force_limit** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The maximum force the linear motor can apply on the X axis while trying to reach the target velocity.

---

[float](class_float.md#class-float) **linear_motor_x/target_velocity** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

The speed that the linear motor will attempt to reach on the X axis.

---

[bool](class_bool.md#class-bool) **linear_motor_y/enabled** = `false`

-  **set_flag_y**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: Flag) 

If `true`, then there is a linear motor on the Y axis. It will attempt to reach the target velocity while staying within the force limits.

---

[float](class_float.md#class-float) **linear_motor_y/force_limit** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The maximum force the linear motor can apply on the Y axis while trying to reach the target velocity.

---

[float](class_float.md#class-float) **linear_motor_y/target_velocity** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

The speed that the linear motor will attempt to reach on the Y axis.

---

[bool](class_bool.md#class-bool) **linear_motor_z/enabled** = `false`

-  **set_flag_z**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: Flag) 

If `true`, then there is a linear motor on the Z axis. It will attempt to reach the target velocity while staying within the force limits.

---

[float](class_float.md#class-float) **linear_motor_z/force_limit** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The maximum force the linear motor can apply on the Z axis while trying to reach the target velocity.

---

[float](class_float.md#class-float) **linear_motor_z/target_velocity** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

The speed that the linear motor will attempt to reach on the Z axis.

---

[float](class_float.md#class-float) **linear_spring_x/damping** = `0.01`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **linear_spring_x/enabled** = `false`

-  **set_flag_x**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_x**(flag: Flag) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_spring_x/equilibrium_point** = `0.0`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_spring_x/stiffness** = `0.01`

-  **set_param_x**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_x**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_spring_y/damping** = `0.01`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **linear_spring_y/enabled** = `false`

-  **set_flag_y**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_y**(flag: Flag) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_spring_y/equilibrium_point** = `0.0`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_spring_y/stiffness** = `0.01`

-  **set_param_y**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_y**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_spring_z/damping** = `0.01`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **linear_spring_z/enabled** = `false`

-  **set_flag_z**(flag: Flag, value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_flag_z**(flag: Flag) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_spring_z/equilibrium_point** = `0.0`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **linear_spring_z/stiffness** = `0.01`

-  **set_param_z**(param: Param, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_z**(param: Param) 

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

## Method Descriptions

[bool](class_bool.md#class-bool) **get_flag_x**(flag: Flag)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **get_flag_y**(flag: Flag)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **get_flag_z**(flag: Flag)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **get_param_x**(param: Param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **get_param_y**(param: Param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **get_param_z**(param: Param)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_flag_x**(flag: Flag, value: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_flag_y**(flag: Flag, value: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_flag_z**(flag: Flag, value: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_param_x**(param: Param, value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_param_y**(param: Param, value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_param_z**(param: Param, value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
