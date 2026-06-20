# GPUParticlesCollisionBox3D

**Inherits:** [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A box-shaped 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

## Description

A box-shaped 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) nodes.

Particle collision shapes work in real-time and can be moved, rotated and scaled during gameplay. Unlike attractors, non-uniform scaling of collision shapes is *not* supported.

**Note:** [ParticleProcessMaterial.collision_mode](class_particleprocessmaterial.md#class-particleprocessmaterial-property-collision-mode) must be [ParticleProcessMaterial.COLLISION_RIGID](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-rigid) or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT](class_particleprocessmaterial.md#class-particleprocessmaterial-constant-collision-hide-on-contact) on the [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d)'s process material for collision to work.

**Note:** Particle collision only affects [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d), not [CPUParticles3D](class_cpuparticles3d.md#class-cpuparticles3d).

## Properties

| [Vector3](class_vector3.md#class-vector3)   | size   | `Vector3(2, 2, 2)`   |
|---------------------------------------------|-----------------------------------------------------------|----------------------|

---

## Property Descriptions

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(2, 2, 2)`

-  **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The collision box's size in 3D units.
