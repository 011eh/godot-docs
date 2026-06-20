# CanvasItemMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material for [CanvasItem](class_canvasitem.md#class-canvasitem)s.

## Description

**CanvasItemMaterial**s provide a means of modifying the textures associated with a CanvasItem. They specialize in describing blend and lighting behaviors for textures. Use a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) to more fully customize a material's interactions with a [CanvasItem](class_canvasitem.md#class-canvasitem).

## Properties

| BlendMode   | blend_mode                           | `0`     |
|---------------------------------------------------|---------------------------------------------------------------------------------------|---------|
| LightMode   | light_mode                           | `0`     |
| [int](class_int.md#class-int)                     | particles_anim_h_frames |         |
| [bool](class_bool.md#class-bool)                  | particles_anim_loop         |         |
| [int](class_int.md#class-int)                     | particles_anim_v_frames |         |
| [bool](class_bool.md#class-bool)                  | particles_animation         | `false` |

---

## Enumerations

enum **BlendMode**:

BlendMode **BLEND_MODE_MIX** = `0`

Mix blending mode. Colors are assumed to be independent of the alpha (opacity) value.

BlendMode **BLEND_MODE_ADD** = `1`

Additive blending mode.

BlendMode **BLEND_MODE_SUB** = `2`

Subtractive blending mode.

BlendMode **BLEND_MODE_MUL** = `3`

Multiplicative blending mode.

BlendMode **BLEND_MODE_PREMULT_ALPHA** = `4`

Mix blending mode. Colors are assumed to be premultiplied by the alpha (opacity) value.

---

enum **LightMode**:

LightMode **LIGHT_MODE_NORMAL** = `0`

Render the material using both light and non-light sensitive material properties.

LightMode **LIGHT_MODE_UNSHADED** = `1`

Render the material as if there were no light.

LightMode **LIGHT_MODE_LIGHT_ONLY** = `2`

Render the material as if there were only light.

---

## Property Descriptions

BlendMode **blend_mode** = `0`

-  **set_blend_mode**(value: BlendMode)
- BlendMode **get_blend_mode**()

The manner in which a material's rendering is applied to underlying textures.

---

LightMode **light_mode** = `0`

-  **set_light_mode**(value: LightMode)
- LightMode **get_light_mode**()

The manner in which material reacts to lighting.

---

[int](class_int.md#class-int) **particles_anim_h_frames**

-  **set_particles_anim_h_frames**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_particles_anim_h_frames**()

The number of columns in the spritesheet assigned as [Texture2D](class_texture2d.md#class-texture2d) for a [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) or [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d).

**Note:** This property is only used and visible in the editor if particles_animation is `true`.

---

[bool](class_bool.md#class-bool) **particles_anim_loop**

-  **set_particles_anim_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particles_anim_loop**()

If `true`, the particles animation will loop.

**Note:** This property is only used and visible in the editor if particles_animation is `true`.

---

[int](class_int.md#class-int) **particles_anim_v_frames**

-  **set_particles_anim_v_frames**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_particles_anim_v_frames**()

The number of rows in the spritesheet assigned as [Texture2D](class_texture2d.md#class-texture2d) for a [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) or [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d).

**Note:** This property is only used and visible in the editor if particles_animation is `true`.

---

[bool](class_bool.md#class-bool) **particles_animation** = `false`

-  **set_particles_animation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_particles_animation**()

If `true`, enable spritesheet-based animation features when assigned to [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) and [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d) nodes. The [ParticleProcessMaterial.anim_speed_max](class_particleprocessmaterial.md#class-particleprocessmaterial-property-anim-speed-max) or [CPUParticles2D.anim_speed_max](class_cpuparticles2d.md#class-cpuparticles2d-property-anim-speed-max) should also be set to a positive value for the animation to play.

This property (and other `particles_anim_*` properties that depend on it) has no effect on other types of nodes.
