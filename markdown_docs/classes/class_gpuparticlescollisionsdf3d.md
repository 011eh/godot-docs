# GPUParticlesCollisionSDF3D

**Inherits:** [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A baked signed distance field 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

## Description

A baked signed distance field 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

Signed distance fields (SDF) allow for efficiently representing approximate collision shapes for convex and concave objects of any shape. This is more flexible than [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d), but it requires a baking step.

**Baking:** The signed distance field texture can be baked by selecting the **GPUParticlesCollisionSDF3D** node in the editor, then clicking **Bake SDF** at the top of the 3D viewport. Any *visible* [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d)s within the size will be taken into account for baking, regardless of their [GeometryInstance3D.gi_mode](class_geometryinstance3d.md#class-geometryinstance3d-property-gi-mode).

**Note:** Baking a **GPUParticlesCollisionSDF3D**'s texture is only possible within the editor, as there is no bake method exposed for use in exported projects. However, it's still possible to load pre-baked [Texture3D](class_texture3d.md#class-texture3d)s into its texture property in an exported project.

**Note:** [ParticleProcessMaterial.collision_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-mode) must be [ParticleProcessMaterial.COLLISION_RIGID](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-rigid) or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-hide-on-contact) on the [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d)'s process material for collision to work.

**Note:** Particle collision only affects [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), not [CPUParticles3D](class_cpuparticles3d.md#class-cpuparticles3d).

## Properties

| [int](class_int.md#class-int)                             | bake_mask   | `4294967295`       |
|-----------------------------------------------------------|---------------------------------------------------------------------|--------------------|
| Resolution | resolution | `2`                |
| [Vector3](class_vector3.md#class-vector3)                 | size             | `Vector3(2, 2, 2)` |
| [Texture3D](class_texture3d.md#class-texture3d)           | texture       |                    |
| [float](class_float.md#class-float)                       | thickness   | `1.0`              |

## Methods

| [bool](class_bool.md#class-bool)   | get_bake_mask_value(layer_number: [int](class_int.md#class-int))                                          |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                    | set_bake_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |

---

## Enumerations

enum **Resolution**:

Resolution **RESOLUTION_16** = `0`

Bake a 16×16×16 signed distance field. This is the fastest option, but also the least precise.

Resolution **RESOLUTION_32** = `1`

Bake a 32×32×32 signed distance field.

Resolution **RESOLUTION_64** = `2`

Bake a 64×64×64 signed distance field.

Resolution **RESOLUTION_128** = `3`

Bake a 128×128×128 signed distance field.

Resolution **RESOLUTION_256** = `4`

Bake a 256×256×256 signed distance field.

Resolution **RESOLUTION_512** = `5`

Bake a 512×512×512 signed distance field. This is the slowest option, but also the most precise.

Resolution **RESOLUTION_MAX** = `6`

Represents the size of the Resolution enum.

---

## Property Descriptions

[int](class_int.md#class-int) **bake_mask** = `4294967295`

-  **set_bake_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bake_mask**()

The visual layers to account for when baking the particle collision SDF. Only [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d)s whose [VisualInstance3D.layers](class_visualinstance3d.md#class-visualinstance3d-property-layers) match with this bake_mask will be included in the generated particle collision SDF. By default, all objects are taken into account for the particle collision SDF baking.

---

Resolution **resolution** = `2`

-  **set_resolution**(value: Resolution)
- Resolution **get_resolution**()

The bake resolution to use for the signed distance field texture. The texture must be baked again for changes to the resolution property to be effective. Higher resolutions have a greater performance cost and take more time to bake. Higher resolutions also result in larger baked textures, leading to increased VRAM and storage space requirements. To improve performance and reduce bake times, use the lowest resolution possible for the object you're representing the collision of.

---

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(2, 2, 2)`

-  **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The collision SDF's size in 3D units. To improve SDF quality, the size should be set as small as possible while covering the parts of the scene you need.

---

[Texture3D](class_texture3d.md#class-texture3d) **texture**

-  **set_texture**(value: [Texture3D](class_texture3d.md#class-texture3d))
- [Texture3D](class_texture3d.md#class-texture3d) **get_texture**()

The 3D texture representing the signed distance field.

---

[float](class_float.md#class-float) **thickness** = `1.0`

-  **set_thickness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_thickness**()

The collision shape's thickness. Unlike other particle colliders, **GPUParticlesCollisionSDF3D** is actually hollow on the inside. thickness can be increased to prevent particles from tunneling through the collision shape at high speeds, or when the **GPUParticlesCollisionSDF3D** is moved.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **get_bake_mask_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the bake_mask is enabled, given a `layer_number` between 1 and 32.

---

 **set_bake_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the bake_mask, given a `layer_number` between 1 and 32.
