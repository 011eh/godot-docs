# VisualShaderNodeParticleMeshEmitter

**Inherits:** [VisualShaderNodeParticleEmitter](class_visualshadernodeparticleemitter.md#class-visualshadernodeparticleemitter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node that makes particles emitted in a shape defined by a [Mesh](class_mesh.md#class-mesh).

## Description

[VisualShaderNodeParticleEmitter](class_visualshadernodeparticleemitter.md#class-visualshadernodeparticleemitter) that makes the particles emitted in a shape of the assigned mesh. It will emit from the mesh's surfaces, either all or only the specified one.

## Properties

| [Mesh](class_mesh.md#class-mesh)   | mesh                         |        |
|------------------------------------|------------------------------------------------------------------------------------------|--------|
| [int](class_int.md#class-int)      | surface_index       | `0`    |
| [bool](class_bool.md#class-bool)   | use_all_surfaces | `true` |

---

## Property Descriptions

[Mesh](class_mesh.md#class-mesh) **mesh**

-  **set_mesh**(value: [Mesh](class_mesh.md#class-mesh))
- [Mesh](class_mesh.md#class-mesh) **get_mesh**()

The [Mesh](class_mesh.md#class-mesh) that defines emission shape.

---

[int](class_int.md#class-int) **surface_index** = `0`

-  **set_surface_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_surface_index**()

Index of the surface that emits particles. use_all_surfaces must be `false` for this to take effect.

---

[bool](class_bool.md#class-bool) **use_all_surfaces** = `true`

-  **set_use_all_surfaces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_use_all_surfaces**()

If `true`, the particles will emit from all surfaces of the mesh.
