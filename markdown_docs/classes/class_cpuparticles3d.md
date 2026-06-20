# CPUParticles3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A CPU-based 3D particle emitter.

## Description

CPU-based 3D particle node used to create a variety of particle systems and effects.

See also [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), which provides the same functionality with hardware acceleration, but may not run on older devices.

## Tutorials

- [Particle systems (3D)](../tutorials/3d/particles/index.md)

## Properties

| [int](class_int.md#class-int)                                              | amount                                         | `8`                      |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------|
| [Curve](class_curve.md#class-curve)                                        | angle_curve                               |                          |
| [float](class_float.md#class-float)                                        | angle_max                                   | `0.0`                    |
| [float](class_float.md#class-float)                                        | angle_min                                   | `0.0`                    |
| [Curve](class_curve.md#class-curve)                                        | angular_velocity_curve         |                          |
| [float](class_float.md#class-float)                                        | angular_velocity_max             | `0.0`                    |
| [float](class_float.md#class-float)                                        | angular_velocity_min             | `0.0`                    |
| [Curve](class_curve.md#class-curve)                                        | anim_offset_curve                   |                          |
| [float](class_float.md#class-float)                                        | anim_offset_max                       | `0.0`                    |
| [float](class_float.md#class-float)                                        | anim_offset_min                       | `0.0`                    |
| [Curve](class_curve.md#class-curve)                                        | anim_speed_curve                     |                          |
| [float](class_float.md#class-float)                                        | anim_speed_max                         | `0.0`                    |
| [float](class_float.md#class-float)                                        | anim_speed_min                         | `0.0`                    |
| [Color](class_color.md#class-color)                                        | color                                           | `Color(1, 1, 1, 1)`      |
| [Gradient](class_gradient.md#class-gradient)                               | color_initial_ramp                 |                          |
| [Gradient](class_gradient.md#class-gradient)                               | color_ramp                                 |                          |
| [Curve](class_curve.md#class-curve)                                        | damping_curve                           |                          |
| [float](class_float.md#class-float)                                        | damping_max                               | `0.0`                    |
| [float](class_float.md#class-float)                                        | damping_min                               | `0.0`                    |
| [Vector3](class_vector3.md#class-vector3)                                  | direction                                   | `Vector3(1, 0, 0)`       |
| DrawOrder                                | draw_order                                 | `0`                      |
| [Vector3](class_vector3.md#class-vector3)                                  | emission_box_extents             |                          |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)       | emission_colors                       | `PackedColorArray()`     |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | emission_normals                     |                          |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | emission_points                       |                          |
| [Vector3](class_vector3.md#class-vector3)                                  | emission_ring_axis                 |                          |
| [float](class_float.md#class-float)                                        | emission_ring_cone_angle     |                          |
| [float](class_float.md#class-float)                                        | emission_ring_height             |                          |
| [float](class_float.md#class-float)                                        | emission_ring_inner_radius |                          |
| [float](class_float.md#class-float)                                        | emission_ring_radius             |                          |
| EmissionShape                        | emission_shape                         | `0`                      |
| [float](class_float.md#class-float)                                        | emission_sphere_radius         |                          |
| [bool](class_bool.md#class-bool)                                           | emitting                                     | `true`                   |
| [float](class_float.md#class-float)                                        | explosiveness                           | `0.0`                    |
| [int](class_int.md#class-int)                                              | fixed_fps                                   | `0`                      |
| [float](class_float.md#class-float)                                        | flatness                                     | `0.0`                    |
| [bool](class_bool.md#class-bool)                                           | fract_delta                               | `true`                   |
| [Vector3](class_vector3.md#class-vector3)                                  | gravity                                       | `Vector3(0, -9.8, 0)`    |
| [Curve](class_curve.md#class-curve)                                        | hue_variation_curve               |                          |
| [float](class_float.md#class-float)                                        | hue_variation_max                   | `0.0`                    |
| [float](class_float.md#class-float)                                        | hue_variation_min                   | `0.0`                    |
| [float](class_float.md#class-float)                                        | initial_velocity_max             | `0.0`                    |
| [float](class_float.md#class-float)                                        | initial_velocity_min             | `0.0`                    |
| [float](class_float.md#class-float)                                        | lifetime                                     | `1.0`                    |
| [float](class_float.md#class-float)                                        | lifetime_randomness               | `0.0`                    |
| [Curve](class_curve.md#class-curve)                                        | linear_accel_curve                 |                          |
| [float](class_float.md#class-float)                                        | linear_accel_max                     | `0.0`                    |
| [float](class_float.md#class-float)                                        | linear_accel_min                     | `0.0`                    |
| [bool](class_bool.md#class-bool)                                           | local_coords                             | `false`                  |
| [Mesh](class_mesh.md#class-mesh)                                           | mesh                                             |                          |
| [bool](class_bool.md#class-bool)                                           | one_shot                                     | `false`                  |
| [Curve](class_curve.md#class-curve)                                        | orbit_velocity_curve             |                          |
| [float](class_float.md#class-float)                                        | orbit_velocity_max                 |                          |
| [float](class_float.md#class-float)                                        | orbit_velocity_min                 |                          |
| [bool](class_bool.md#class-bool)                                           | particle_flag_align_y           | `false`                  |
| [bool](class_bool.md#class-bool)                                           | particle_flag_disable_z       | `false`                  |
| [bool](class_bool.md#class-bool)                                           | particle_flag_rotate_y         | `false`                  |
| [float](class_float.md#class-float)                                        | preprocess                                 | `0.0`                    |
| [Curve](class_curve.md#class-curve)                                        | radial_accel_curve                 |                          |
| [float](class_float.md#class-float)                                        | radial_accel_max                     | `0.0`                    |
| [float](class_float.md#class-float)                                        | radial_accel_min                     | `0.0`                    |
| [float](class_float.md#class-float)                                        | randomness                                 | `0.0`                    |
| [Curve](class_curve.md#class-curve)                                        | scale_amount_curve                 |                          |
| [float](class_float.md#class-float)                                        | scale_amount_max                     | `1.0`                    |
| [float](class_float.md#class-float)                                        | scale_amount_min                     | `1.0`                    |
| [Curve](class_curve.md#class-curve)                                        | scale_curve_x                           |                          |
| [Curve](class_curve.md#class-curve)                                        | scale_curve_y                           |                          |
| [Curve](class_curve.md#class-curve)                                        | scale_curve_z                           |                          |
| [int](class_int.md#class-int)                                              | seed                                             | `0`                      |
| [float](class_float.md#class-float)                                        | speed_scale                               | `1.0`                    |
| [bool](class_bool.md#class-bool)                                           | split_scale                               | `false`                  |
| [float](class_float.md#class-float)                                        | spread                                         | `45.0`                   |
| [Curve](class_curve.md#class-curve)                                        | tangential_accel_curve         |                          |
| [float](class_float.md#class-float)                                        | tangential_accel_max             | `0.0`                    |
| [float](class_float.md#class-float)                                        | tangential_accel_min             | `0.0`                    |
| [bool](class_bool.md#class-bool)                                           | use_fixed_seed                         | `false`                  |
| [AABB](class_aabb.md#class-aabb)                                           | visibility_aabb                       | `AABB(0, 0, 0, 0, 0, 0)` |

## Methods

| [AABB](class_aabb.md#class-aabb)    | capture_aabb()                                                                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                     | convert_from_particles(particles: [Node](class_node.md#class-node))                                                                               |
| [Curve](class_curve.md#class-curve) | get_param_curve(param: Parameter)                                                                                      |
| [float](class_float.md#class-float) | get_param_max(param: Parameter)                                                                                          |
| [float](class_float.md#class-float) | get_param_min(param: Parameter)                                                                                          |
| [bool](class_bool.md#class-bool)    | get_particle_flag(particle_flag: ParticleFlags)                                                                  |
|                                     | request_particles_process(process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0.0) |
|                                     | restart(keep_seed: [bool](class_bool.md#class-bool) = false)                                                                                                     |
|                                     | set_param_curve(param: Parameter, curve: [Curve](class_curve.md#class-curve))                                          |
|                                     | set_param_max(param: Parameter, value: [float](class_float.md#class-float))                                              |
|                                     | set_param_min(param: Parameter, value: [float](class_float.md#class-float))                                              |
|                                     | set_particle_flag(particle_flag: ParticleFlags, enable: [bool](class_bool.md#class-bool))                        |

---

## Signals

**finished**()

Emitted when all active particles have finished processing. When one_shot is disabled, particles will process continuously, so this is never emitted.

---

## Enumerations

enum **DrawOrder**:

DrawOrder **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

DrawOrder **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.

DrawOrder **DRAW_ORDER_VIEW_DEPTH** = `2`

Particles are drawn in order of depth.

---

enum **Parameter**:

Parameter **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with set_param_min(), set_param_max(), and set_param_curve() to set initial velocity properties.

Parameter **PARAM_ANGULAR_VELOCITY** = `1`

Use with set_param_min(), set_param_max(), and set_param_curve() to set angular velocity properties.

Parameter **PARAM_ORBIT_VELOCITY** = `2`

Use with set_param_min(), set_param_max(), and set_param_curve() to set orbital velocity properties.

Parameter **PARAM_LINEAR_ACCEL** = `3`

Use with set_param_min(), set_param_max(), and set_param_curve() to set linear acceleration properties.

Parameter **PARAM_RADIAL_ACCEL** = `4`

Use with set_param_min(), set_param_max(), and set_param_curve() to set radial acceleration properties.

Parameter **PARAM_TANGENTIAL_ACCEL** = `5`

Use with set_param_min(), set_param_max(), and set_param_curve() to set tangential acceleration properties.

Parameter **PARAM_DAMPING** = `6`

Use with set_param_min(), set_param_max(), and set_param_curve() to set damping properties.

Parameter **PARAM_ANGLE** = `7`

Use with set_param_min(), set_param_max(), and set_param_curve() to set angle properties.

Parameter **PARAM_SCALE** = `8`

Use with set_param_min(), set_param_max(), and set_param_curve() to set scale properties.

Parameter **PARAM_HUE_VARIATION** = `9`

Use with set_param_min(), set_param_max(), and set_param_curve() to set hue variation properties.

Parameter **PARAM_ANIM_SPEED** = `10`

Use with set_param_min(), set_param_max(), and set_param_curve() to set animation speed properties.

Parameter **PARAM_ANIM_OFFSET** = `11`

Use with set_param_min(), set_param_max(), and set_param_curve() to set animation offset properties.

Parameter **PARAM_MAX** = `12`

Represents the size of the Parameter enum.

---

enum **ParticleFlags**:

ParticleFlags **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with set_particle_flag() to set particle_flag_align_y.

ParticleFlags **PARTICLE_FLAG_ROTATE_Y** = `1`

Use with set_particle_flag() to set particle_flag_rotate_y.

ParticleFlags **PARTICLE_FLAG_DISABLE_Z** = `2`

Use with set_particle_flag() to set particle_flag_disable_z.

ParticleFlags **PARTICLE_FLAG_MAX** = `3`

Represents the size of the ParticleFlags enum.

---

enum **EmissionShape**:

EmissionShape **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

EmissionShape **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere.

EmissionShape **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere.

EmissionShape **EMISSION_SHAPE_BOX** = `3`

Particles will be emitted in the volume of a box.

EmissionShape **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position chosen randomly among emission_points. Particle color will be modulated by emission_colors.

EmissionShape **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position chosen randomly among emission_points. Particle velocity and rotation will be set based on emission_normals. Particle color will be modulated by emission_colors.

EmissionShape **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in a ring or cylinder.

EmissionShape **EMISSION_SHAPE_MAX** = `7`

Represents the size of the EmissionShape enum.

---

## Property Descriptions

[int](class_int.md#class-int) **amount** = `8`

-  **set_amount**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_amount**()

Number of particles emitted in one emission cycle.

---

[Curve](class_curve.md#class-curve) **angle_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's rotation will be animated along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **angle_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum angle.

---

[float](class_float.md#class-float) **angle_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum angle.

---

[Curve](class_curve.md#class-curve) **angular_velocity_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's angular velocity (rotation speed) will vary along this [Curve](class_curve.md#class-curve) over its lifetime. Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **angular_velocity_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

---

[float](class_float.md#class-float) **angular_velocity_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

---

[Curve](class_curve.md#class-curve) **anim_offset_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's animation offset will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **anim_offset_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum animation offset.

---

[float](class_float.md#class-float) **anim_offset_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum animation offset.

---

[Curve](class_curve.md#class-curve) **anim_speed_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's animation speed will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **anim_speed_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum particle animation speed.

---

[float](class_float.md#class-float) **anim_speed_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum particle animation speed.

---

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)`

-  **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

Each particle's initial color.

**Note:** color multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, color will have no visible effect.

---

[Gradient](class_gradient.md#class-gradient) **color_initial_ramp**

-  **set_color_initial_ramp**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_color_initial_ramp**()

Each particle's initial color will vary along this [Gradient](class_gradient.md#class-gradient) (multiplied with color).

**Note:** color_initial_ramp multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, color_initial_ramp will have no visible effect.

---

[Gradient](class_gradient.md#class-gradient) **color_ramp**

-  **set_color_ramp**(value: [Gradient](class_gradient.md#class-gradient))
- [Gradient](class_gradient.md#class-gradient) **get_color_ramp**()

Each particle's color will vary along this [Gradient](class_gradient.md#class-gradient) over its lifetime (multiplied with color).

**Note:** color_ramp multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, color_ramp will have no visible effect.

---

[Curve](class_curve.md#class-curve) **damping_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Damping will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **damping_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum damping.

---

[float](class_float.md#class-float) **damping_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum damping.

---

[Vector3](class_vector3.md#class-vector3) **direction** = `Vector3(1, 0, 0)`

-  **set_direction**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_direction**()

Unit vector specifying the particles' emission direction.

---

DrawOrder **draw_order** = `0`

-  **set_draw_order**(value: DrawOrder)
- DrawOrder **get_draw_order**()

Particle draw order.

---

[Vector3](class_vector3.md#class-vector3) **emission_box_extents**

-  **set_emission_box_extents**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_emission_box_extents**()

The rectangle's extents if emission_shape is set to EMISSION_SHAPE_BOX.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **emission_colors** = `PackedColorArray()`

-  **set_emission_colors**(value: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))
- [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_emission_colors**()

Sets the [Color](class_color.md#class-color)s to modulate particles by when using EMISSION_SHAPE_POINTS or EMISSION_SHAPE_DIRECTED_POINTS.

**Note:** emission_colors multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, emission_colors will have no visible effect.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **emission_normals**

-  **set_emission_normals**(value: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))
- [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_emission_normals**()

Sets the direction the particles will be emitted in when using EMISSION_SHAPE_DIRECTED_POINTS.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) for more details.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **emission_points**

-  **set_emission_points**(value: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))
- [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_emission_points**()

Sets the initial positions to spawn particles when using EMISSION_SHAPE_POINTS or EMISSION_SHAPE_DIRECTED_POINTS.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) for more details.

---

[Vector3](class_vector3.md#class-vector3) **emission_ring_axis**

-  **set_emission_ring_axis**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_emission_ring_axis**()

The axis of the ring when using the emitter EMISSION_SHAPE_RING.

---

[float](class_float.md#class-float) **emission_ring_cone_angle**

-  **set_emission_ring_cone_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_cone_angle**()

The angle of the cone when using the emitter EMISSION_SHAPE_RING. The default angle of 90 degrees results in a ring, while an angle of 0 degrees results in a cone. Intermediate values will result in a ring where one end is larger than the other.

**Note:** Depending on emission_ring_height, the angle may be clamped if the ring's end is reached to form a perfect cone.

---

[float](class_float.md#class-float) **emission_ring_height**

-  **set_emission_ring_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_height**()

The height of the ring when using the emitter EMISSION_SHAPE_RING.

---

[float](class_float.md#class-float) **emission_ring_inner_radius**

-  **set_emission_ring_inner_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_inner_radius**()

The inner radius of the ring when using the emitter EMISSION_SHAPE_RING.

---

[float](class_float.md#class-float) **emission_ring_radius**

-  **set_emission_ring_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_ring_radius**()

The radius of the ring when using the emitter EMISSION_SHAPE_RING.

---

EmissionShape **emission_shape** = `0`

-  **set_emission_shape**(value: EmissionShape)
- EmissionShape **get_emission_shape**()

Particles will be emitted inside this region.

---

[float](class_float.md#class-float) **emission_sphere_radius**

-  **set_emission_sphere_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_sphere_radius**()

The sphere's radius if EmissionShape is set to EMISSION_SHAPE_SPHERE.

---

[bool](class_bool.md#class-bool) **emitting** = `true`

-  **set_emitting**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_emitting**()

If `true`, particles are being emitted. emitting can be used to start and stop particles from emitting. However, if one_shot is `true` setting emitting to `true` will not restart the emission cycle until after all active particles finish processing. You can use the finished signal to be notified once all active particles finish processing.

---

[float](class_float.md#class-float) **explosiveness** = `0.0`

-  **set_explosiveness_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_explosiveness_ratio**()

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.

---

[int](class_int.md#class-int) **fixed_fps** = `0`

-  **set_fixed_fps**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fixed_fps**()

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the particle system itself.

---

[float](class_float.md#class-float) **flatness** = `0.0`

-  **set_flatness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_flatness**()

Amount of spread in Y/Z plane. A value of `1` restricts particles to X/Z plane.

---

[bool](class_bool.md#class-bool) **fract_delta** = `true`

-  **set_fractional_delta**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_fractional_delta**()

If `true`, results in fractional delta calculation which has a smoother particles display effect.

---

[Vector3](class_vector3.md#class-vector3) **gravity** = `Vector3(0, -9.8, 0)`

-  **set_gravity**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_gravity**()

Gravity applied to every particle.

---

[Curve](class_curve.md#class-curve) **hue_variation_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's hue will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **hue_variation_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum hue variation.

---

[float](class_float.md#class-float) **hue_variation_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum hue variation.

---

[float](class_float.md#class-float) **initial_velocity_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum value of the initial velocity.

---

[float](class_float.md#class-float) **initial_velocity_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum value of the initial velocity.

---

[float](class_float.md#class-float) **lifetime** = `1.0`

-  **set_lifetime**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lifetime**()

Amount of time each particle will exist.

---

[float](class_float.md#class-float) **lifetime_randomness** = `0.0`

-  **set_lifetime_randomness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lifetime_randomness**()

Particle lifetime randomness ratio.

---

[Curve](class_curve.md#class-curve) **linear_accel_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's linear acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **linear_accel_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum linear acceleration.

---

[float](class_float.md#class-float) **linear_accel_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum linear acceleration.

---

[bool](class_bool.md#class-bool) **local_coords** = `false`

-  **set_use_local_coordinates**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_local_coordinates**()

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **CPUParticles3D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **CPUParticles3D** node (and its parents) when it is moved or rotated.

---

[Mesh](class_mesh.md#class-mesh) **mesh**

-  **set_mesh**(value: [Mesh](class_mesh.md#class-mesh))
- [Mesh](class_mesh.md#class-mesh) **get_mesh**()

The [Mesh](class_mesh.md#class-mesh) used for each particle. If `null`, particles will be spheres.

---

[bool](class_bool.md#class-bool) **one_shot** = `false`

-  **set_one_shot**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_one_shot**()

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.

---

[Curve](class_curve.md#class-curve) **orbit_velocity_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's orbital velocity will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **orbit_velocity_max**

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum orbit velocity.

---

[float](class_float.md#class-float) **orbit_velocity_min**

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum orbit velocity.

---

[bool](class_bool.md#class-bool) **particle_flag_align_y** = `false`

-  **set_particle_flag**(particle_flag: ParticleFlags, enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: ParticleFlags) 

Align Y axis of particle with the direction of its velocity.

---

[bool](class_bool.md#class-bool) **particle_flag_disable_z** = `false`

-  **set_particle_flag**(particle_flag: ParticleFlags, enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: ParticleFlags) 

If `true`, particles will not move on the Z axis.

---

[bool](class_bool.md#class-bool) **particle_flag_rotate_y** = `false`

-  **set_particle_flag**(particle_flag: ParticleFlags, enable: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: ParticleFlags) 

If `true`, particles rotate around Y axis by angle_min.

---

[float](class_float.md#class-float) **preprocess** = `0.0`

-  **set_pre_process_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pre_process_time**()

Particle system starts as if it had already run for this many seconds.

---

[Curve](class_curve.md#class-curve) **radial_accel_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's radial acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **radial_accel_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum radial acceleration.

---

[float](class_float.md#class-float) **radial_accel_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum radial acceleration.

---

[float](class_float.md#class-float) **randomness** = `0.0`

-  **set_randomness_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_randomness_ratio**()

Emission lifetime randomness ratio.

---

[Curve](class_curve.md#class-curve) **scale_amount_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's scale will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **scale_amount_max** = `1.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum scale.

---

[float](class_float.md#class-float) **scale_amount_min** = `1.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum scale.

---

[Curve](class_curve.md#class-curve) **scale_curve_x**

-  **set_scale_curve_x**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_scale_curve_x**()

Curve for the scale over life, along the x axis.

---

[Curve](class_curve.md#class-curve) **scale_curve_y**

-  **set_scale_curve_y**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_scale_curve_y**()

Curve for the scale over life, along the y axis.

---

[Curve](class_curve.md#class-curve) **scale_curve_z**

-  **set_scale_curve_z**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_scale_curve_z**()

Curve for the scale over life, along the z axis.

---

[int](class_int.md#class-int) **seed** = `0`

-  **set_seed**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_seed**()

Sets the random seed used by the particle system. Only effective if use_fixed_seed is `true`.

---

[float](class_float.md#class-float) **speed_scale** = `1.0`

-  **set_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_speed_scale**()

Particle system's running speed scaling ratio. A value of `0` can be used to pause the particles.

---

[bool](class_bool.md#class-bool) **split_scale** = `false`

-  **set_split_scale**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_split_scale**()

If set to `true`, three different scale curves can be specified, one per scale axis.

---

[float](class_float.md#class-float) **spread** = `45.0`

-  **set_spread**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_spread**()

Each particle's initial direction range from `+spread` to `-spread` degrees. Applied to X/Z plane and Y/Z planes.

---

[Curve](class_curve.md#class-curve) **tangential_accel_curve**

-  **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter) 

Each particle's tangential acceleration will vary along this [Curve](class_curve.md#class-curve). Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **tangential_accel_max** = `0.0`

-  **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_max**(param: Parameter) 

Maximum tangent acceleration.

---

[float](class_float.md#class-float) **tangential_accel_min** = `0.0`

-  **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_param_min**(param: Parameter) 

Minimum tangent acceleration.

---

[bool](class_bool.md#class-bool) **use_fixed_seed** = `false`

-  **set_use_fixed_seed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_fixed_seed**()

If `true`, particles will use the same seed for every simulation using the seed defined in seed. This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.

---

[AABB](class_aabb.md#class-aabb) **visibility_aabb** = `AABB(0, 0, 0, 0, 0, 0)`

-  **set_visibility_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_visibility_aabb**()

The [AABB](class_aabb.md#class-aabb) that determines the node's region which needs to be visible on screen for the particle system to be active.

Grow the box if particles suddenly appear/disappear when the node enters/exits the screen. The [AABB](class_aabb.md#class-aabb) can be grown via code or with the **Particles → Generate AABB** editor tool.

---

## Method Descriptions

[AABB](class_aabb.md#class-aabb) **capture_aabb**()

Returns the axis-aligned bounding box that contains all the particles that are active in the current frame.

---

 **convert_from_particles**(particles: [Node](class_node.md#class-node))

Sets this node's properties to match a given [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) node with an assigned [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial).

---

[Curve](class_curve.md#class-curve) **get_param_curve**(param: Parameter)

Returns the [Curve](class_curve.md#class-curve) of the parameter specified by Parameter.

---

[float](class_float.md#class-float) **get_param_max**(param: Parameter)

Returns the maximum value range for the given parameter.

---

[float](class_float.md#class-float) **get_param_min**(param: Parameter)

Returns the minimum value range for the given parameter.

---

[bool](class_bool.md#class-bool) **get_particle_flag**(particle_flag: ParticleFlags)

Returns the enabled state of the given particle flag.

---

 **request_particles_process**(process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0.0)

Requests the particles to process for extra process time during a single frame.

`process_time` defines the time that the particles will process while emitting is on. `process_time_residual` defines the time that particles will process with emitting turned off for the simulation. When combined with speed_scale set to `0.0`, this is useful to be able to seek a particle system timeline.

---

 **restart**(keep_seed: [bool](class_bool.md#class-bool) = false)

Restarts the particle emitter.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.

---

 **set_param_curve**(param: Parameter, curve: [Curve](class_curve.md#class-curve))

Sets the [Curve](class_curve.md#class-curve) of the parameter specified by Parameter. Should be a unit [Curve](class_curve.md#class-curve).

---

 **set_param_max**(param: Parameter, value: [float](class_float.md#class-float))

Sets the maximum value for the given parameter.

---

 **set_param_min**(param: Parameter, value: [float](class_float.md#class-float))

Sets the minimum value for the given parameter.

---

 **set_particle_flag**(particle_flag: ParticleFlags, enable: [bool](class_bool.md#class-bool))

Enables or disables the given particle flag.
