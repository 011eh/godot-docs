# GPUParticles2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A 2D particle emitter.

## Description

2D particle node used to create a variety of particle systems and effects. **GPUParticles2D** features an emitter that generates some number of particles at a given rate.

Use the process_material property to add a [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial) to configure particle appearance and behavior. Alternatively, you can add a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) which will be applied to all particles.

2D particles can optionally collide with [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d), but they don't collide with [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) nodes.

## Tutorials

- [Particle systems (2D)](../tutorials/2d/particle_systems_2d.md)
- [2D Particles Demo](https://godotengine.org/asset-library/asset/2724)
- [2D Dodge The Creeps Demo (uses GPUParticles2D for the trail behind the player)](https://godotengine.org/asset-library/asset/2712)

## Properties

| [int](class_int.md#class-int)                   | amount                                         | `8`                           |
|-------------------------------------------------|-----------------------------------------------------------------------------------------|-------------------------------|
| [float](class_float.md#class-float)             | amount_ratio                             | `1.0`                         |
| [float](class_float.md#class-float)             | collision_base_size               | `1.0`                         |
| DrawOrder     | draw_order                                 | `1`                           |
| [bool](class_bool.md#class-bool)                | emitting                                     | `true`                        |
| [float](class_float.md#class-float)             | explosiveness                           | `0.0`                         |
| [int](class_int.md#class-int)                   | fixed_fps                                   | `30`                          |
| [bool](class_bool.md#class-bool)                | fract_delta                               | `true`                        |
| [float](class_float.md#class-float)             | interp_to_end                           | `0.0`                         |
| [bool](class_bool.md#class-bool)                | interpolate                               | `true`                        |
| [float](class_float.md#class-float)             | lifetime                                     | `1.0`                         |
| [bool](class_bool.md#class-bool)                | local_coords                             | `false`                       |
| [bool](class_bool.md#class-bool)                | one_shot                                     | `false`                       |
| [float](class_float.md#class-float)             | preprocess                                 | `0.0`                         |
| [Material](class_material.md#class-material)    | process_material                     |                               |
| [float](class_float.md#class-float)             | randomness                                 | `0.0`                         |
| [int](class_int.md#class-int)                   | seed                                             | `0`                           |
| [float](class_float.md#class-float)             | speed_scale                               | `1.0`                         |
| [NodePath](class_nodepath.md#class-nodepath)    | sub_emitter                               | `NodePath("")`                |
| [Texture2D](class_texture2d.md#class-texture2d) | texture                                       |                               |
| [bool](class_bool.md#class-bool)                | trail_enabled                           | `false`                       |
| [float](class_float.md#class-float)             | trail_lifetime                         | `0.3`                         |
| [int](class_int.md#class-int)                   | trail_section_subdivisions | `4`                           |
| [int](class_int.md#class-int)                   | trail_sections                         | `8`                           |
| [bool](class_bool.md#class-bool)                | use_fixed_seed                         | `false`                       |
| [Rect2](class_rect2.md#class-rect2)             | visibility_rect                       | `Rect2(-100, -100, 200, 200)` |

## Methods

| [Rect2](class_rect2.md#class-rect2)   | capture_rect()                                                                                                                                                                                                                                                   |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                       | convert_from_particles(particles: [Node](class_node.md#class-node))                                                                                                                                                                                    |
|                                       | emit_particle(xform: [Transform2D](class_transform2d.md#class-transform2d), velocity: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color), custom: [Color](class_color.md#class-color), flags: [int](class_int.md#class-int)) |
|                                       | request_particles_process(process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0)                                                                                                        |
|                                       | restart(keep_seed: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                          |

---

## Signals

**finished**()

Emitted when all active particles have finished processing. To immediately restart the emission cycle, call restart().

This signal is never emitted when one_shot is disabled, as particles will be emitted and processed continuously.

**Note:** For one_shot emitters, due to the particles being computed on the GPU, there may be a short period after receiving the signal during which setting emitting to `true` will not restart the emission cycle. This delay is avoided by instead calling restart().

---

## Enumerations

enum **DrawOrder**:

DrawOrder **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

DrawOrder **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.

DrawOrder **DRAW_ORDER_REVERSE_LIFETIME** = `2`

Particles are drawn in reverse order of remaining lifetime. In other words, the particle with the lowest lifetime is drawn at the front.

---

enum **EmitFlags**:

EmitFlags **EMIT_FLAG_POSITION** = `1`

Particle starts at the specified position.

EmitFlags **EMIT_FLAG_ROTATION_SCALE** = `2`

Particle starts with specified rotation and scale.

EmitFlags **EMIT_FLAG_VELOCITY** = `4`

Particle starts with the specified velocity vector, which defines the emission direction and speed.

EmitFlags **EMIT_FLAG_COLOR** = `8`

Particle starts with specified color.

EmitFlags **EMIT_FLAG_CUSTOM** = `16`

Particle starts with specified `CUSTOM` data.

---

## Property Descriptions

[int](class_int.md#class-int) **amount** = `8`

-  **set_amount**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_amount**()

The number of particles to emit in one emission cycle. The effective emission rate is `(amount * amount_ratio) / lifetime` particles per second. Higher values will increase GPU requirements, even if not all particles are visible at a given time or if amount_ratio is decreased.

**Note:** Changing this value will cause the particle system to restart. To avoid this, change amount_ratio instead.

---

[float](class_float.md#class-float) **amount_ratio** = `1.0`

-  **set_amount_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_amount_ratio**()

The ratio of particles that should actually be emitted. If set to a value lower than `1.0`, this will set the amount of emitted particles throughout the lifetime to `amount * amount_ratio`. Unlike changing amount, changing amount_ratio while emitting does not affect already-emitted particles and doesn't cause the particle system to restart. amount_ratio can be used to create effects that make the number of emitted particles vary over time.

**Note:** Reducing the amount_ratio has no performance benefit, since resources need to be allocated and processed for the total amount of particles regardless of the amount_ratio. If you don't intend to change the number of particles emitted while the particles are emitting, make sure amount_ratio is set to `1` and change amount to your liking instead.

---

[float](class_float.md#class-float) **collision_base_size** = `1.0`

-  **set_collision_base_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_collision_base_size**()

Multiplier for particle's collision radius. `1.0` corresponds to the size of the sprite. If particles appear to sink into the ground when colliding, increase this value. If particles appear to float when colliding, decrease this value. Only effective if [ParticleProcessMaterial.collision_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-mode) is [ParticleProcessMaterial.COLLISION_RIGID](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-rigid) or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-hide-on-contact).

**Note:** Particles always have a spherical collision shape.

---

DrawOrder **draw_order** = `1`

-  **set_draw_order**(value: DrawOrder)
- DrawOrder **get_draw_order**()

Particle draw order.

---

[bool](class_bool.md#class-bool) **emitting** = `true`

-  **set_emitting**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_emitting**()

If `true`, particles are being emitted. emitting can be used to start and stop particles from emitting. However, if one_shot is `true` setting emitting to `true` will not restart the emission cycle unless all active particles have finished processing. Use the finished signal to be notified once all active particles finish processing.

**Note:** For one_shot emitters, due to the particles being computed on the GPU, there may be a short period after receiving the finished signal during which setting this to `true` will not restart the emission cycle.

**Tip:** If your one_shot emitter needs to immediately restart emitting particles once finished signal is received, consider calling restart() instead of setting emitting.

---

[float](class_float.md#class-float) **explosiveness** = `0.0`

-  **set_explosiveness_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_explosiveness_ratio**()

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.

---

[int](class_int.md#class-int) **fixed_fps** = `30`

-  **set_fixed_fps**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fixed_fps**()

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the simulation of the particle system itself.

---

[bool](class_bool.md#class-bool) **fract_delta** = `true`

-  **set_fractional_delta**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_fractional_delta**()

If `true`, results in fractional delta calculation which has a smoother particles display effect.

---

[float](class_float.md#class-float) **interp_to_end** = `0.0`

-  **set_interp_to_end**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_interp_to_end**()

Causes all the particles in this node to interpolate towards the end of their lifetime.

**Note:** This only works when used with a [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial). It needs to be manually implemented for custom process shaders.

---

[bool](class_bool.md#class-bool) **interpolate** = `true`

-  **set_interpolate**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_interpolate**()

Enables particle interpolation, which makes the particle movement smoother when their fixed_fps is lower than the screen refresh rate.

---

[float](class_float.md#class-float) **lifetime** = `1.0`

-  **set_lifetime**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lifetime**()

The amount of time each particle will exist (in seconds). The effective emission rate is `(amount * amount_ratio) / lifetime` particles per second.

---

[bool](class_bool.md#class-bool) **local_coords** = `false`

-  **set_use_local_coordinates**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_local_coordinates**()

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **GPUParticles2D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **GPUParticles2D** node (and its parents) when it is moved or rotated.

---

[bool](class_bool.md#class-bool) **one_shot** = `false`

-  **set_one_shot**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_one_shot**()

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.

---

[float](class_float.md#class-float) **preprocess** = `0.0`

-  **set_pre_process_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pre_process_time**()

Particle system starts as if it had already run for this many seconds.

**Note:** This can be very expensive if set to a high number as it requires running the particle shader a number of times equal to the fixed_fps (or 30, if fixed_fps is 0) for every second. In extreme cases it can even lead to a GPU crash due to the volume of work done in a single frame.

---

[Material](class_material.md#class-material) **process_material**

-  **set_process_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_process_material**()

[Material](class_material.md#class-material) for processing particles. Can be a [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial) or a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial).

---

[float](class_float.md#class-float) **randomness** = `0.0`

-  **set_randomness_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_randomness_ratio**()

Emission lifetime randomness ratio.

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

[NodePath](class_nodepath.md#class-nodepath) **sub_emitter** = `NodePath("")`

-  **set_sub_emitter**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_sub_emitter**()

Path to another **GPUParticles2D** node that will be used as a subemitter (see [ParticleProcessMaterial.sub_emitter_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-sub-emitter-mode)). Subemitters can be used to achieve effects such as fireworks, sparks on collision, bubbles popping into water drops, and more.

**Note:** When sub_emitter is set, the target **GPUParticles2D** node will no longer emit particles on its own.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

Particle texture. If `null`, particles will be squares with a size of 1×1 pixels.

**Note:** To use a flipbook texture, assign a new [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial) to the **GPUParticles2D**'s [CanvasItem.material](class_canvasitem.md#class-canvasitem-property-material) property, then enable [CanvasItemMaterial.particles_animation](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-animation) and set [CanvasItemMaterial.particles_anim_h_frames](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-h-frames), [CanvasItemMaterial.particles_anim_v_frames](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-v-frames), and [CanvasItemMaterial.particles_anim_loop](class_canvasitemmaterial.md#class-canvasitemmaterial-property-particles-anim-loop) to match the flipbook texture.

---

[bool](class_bool.md#class-bool) **trail_enabled** = `false`

-  **set_trail_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_trail_enabled**()

If `true`, enables particle trails using a mesh skinning system.

**Note:** Unlike [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), the number of trail sections and subdivisions is set with the trail_sections and trail_section_subdivisions properties.

---

[float](class_float.md#class-float) **trail_lifetime** = `0.3`

-  **set_trail_lifetime**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_trail_lifetime**()

The amount of time the particle's trail should represent (in seconds). Only effective if trail_enabled is `true`.

---

[int](class_int.md#class-int) **trail_section_subdivisions** = `4`

-  **set_trail_section_subdivisions**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_trail_section_subdivisions**()

The number of subdivisions to use for the particle trail rendering. Higher values can result in smoother trail curves, at the cost of performance due to increased mesh complexity. See also trail_sections. Only effective if trail_enabled is `true`.

---

[int](class_int.md#class-int) **trail_sections** = `8`

-  **set_trail_sections**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_trail_sections**()

The number of sections to use for the particle trail rendering. Higher values can result in smoother trail curves, at the cost of performance due to increased mesh complexity. See also trail_section_subdivisions. Only effective if trail_enabled is `true`.

---

[bool](class_bool.md#class-bool) **use_fixed_seed** = `false`

-  **set_use_fixed_seed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_fixed_seed**()

If `true`, particles will use the same seed for every simulation using the seed defined in seed. This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.

---

[Rect2](class_rect2.md#class-rect2) **visibility_rect** = `Rect2(-100, -100, 200, 200)`

-  **set_visibility_rect**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_visibility_rect**()

The [Rect2](class_rect2.md#class-rect2) that determines the node's region which needs to be visible on screen for the particle system to be active.

Grow the rect if particles suddenly appear/disappear when the node enters/exits the screen. The [Rect2](class_rect2.md#class-rect2) can be grown via code or with the **Particles → Generate Visibility Rect** editor tool.

---

## Method Descriptions

[Rect2](class_rect2.md#class-rect2) **capture_rect**()

Returns a rectangle containing the positions of all existing particles.

**Note:** When using threaded rendering this method synchronizes the rendering thread. Calling it often may have a negative impact on performance.

---

 **convert_from_particles**(particles: [Node](class_node.md#class-node))

Sets this node's properties to match a given [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d) node.

---

 **emit_particle**(xform: [Transform2D](class_transform2d.md#class-transform2d), velocity: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color), custom: [Color](class_color.md#class-color), flags: [int](class_int.md#class-int))

Emits a single particle. Whether `xform`, `velocity`, `color` and `custom` are applied depends on the value of `flags`. See EmitFlags.

The default ParticleProcessMaterial will overwrite `color` and use the contents of `custom` as `(rotation, age, animation, lifetime)`.

**Note:** emit_particle() is only supported on the Forward+ and Mobile rendering methods, not Compatibility.

---

 **request_particles_process**(process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0)

Requests the particles to process for extra process time during a single frame.

`process_time` defines the time that the particles will process while emitting is on. `process_time_residual` defines the time that particles will process with emitting turned off for the simulation. When combined with speed_scale set to `0.0`, this is useful to be able to seek a particle system timeline.

---

 **restart**(keep_seed: [bool](class_bool.md#class-bool) = false)

Restarts the particle emission cycle, clearing existing particles. To avoid particles vanishing from the viewport, wait for the finished signal before calling.

**Note:** The finished signal is only emitted by one_shot emitters.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.
