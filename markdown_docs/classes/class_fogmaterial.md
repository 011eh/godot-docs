# FogMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material that controls how volumetric fog is rendered, to be assigned to a [FogVolume](class_fogvolume.md#class-fogvolume).

## Description

A [Material](class_material.md#class-material) resource that can be used by [FogVolume](class_fogvolume.md#class-fogvolume)s to draw volumetric effects.

If you need more advanced effects, use a custom [fog shader](../tutorials/shaders/shader_reference/fog_shader.md).

## Properties

| [Color](class_color.md#class-color)             | albedo                   | `Color(1, 1, 1, 1)`   |
|-------------------------------------------------|----------------------------------------------------------------|-----------------------|
| [float](class_float.md#class-float)             | density                 | `1.0`                 |
| [Texture3D](class_texture3d.md#class-texture3d) | density_texture |                       |
| [float](class_float.md#class-float)             | edge_fade             | `0.1`                 |
| [Color](class_color.md#class-color)             | emission               | `Color(0, 0, 0, 1)`   |
| [float](class_float.md#class-float)             | height_falloff   | `0.0`                 |

---

## Property Descriptions

[Color](class_color.md#class-color) **albedo** = `Color(1, 1, 1, 1)`

-  **set_albedo**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_albedo**()

The single-scattering [Color](class_color.md#class-color) of the [FogVolume](class_fogvolume.md#class-fogvolume). Internally, albedo is converted into single-scattering, which is additively blended with other [FogVolume](class_fogvolume.md#class-fogvolume)s and the [Environment.volumetric_fog_albedo](class_environment.md#class-environment-property-volumetric-fog-albedo).

---

[float](class_float.md#class-float) **density** = `1.0`

-  **set_density**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_density**()

The density of the [FogVolume](class_fogvolume.md#class-fogvolume). Denser objects are more opaque, but may suffer from under-sampling artifacts that look like stripes. Negative values can be used to subtract fog from other [FogVolume](class_fogvolume.md#class-fogvolume)s or global volumetric fog.

**Note:** Due to limited precision, density values between `-0.001` and `0.001` (exclusive) act like `0.0`. This does not apply to [Environment.volumetric_fog_density](class_environment.md#class-environment-property-volumetric-fog-density).

---

[Texture3D](class_texture3d.md#class-texture3d) **density_texture**

-  **set_density_texture**(value: [Texture3D](class_texture3d.md#class-texture3d))
- [Texture3D](class_texture3d.md#class-texture3d) **get_density_texture**()

The 3D texture that is used to scale the density of the [FogVolume](class_fogvolume.md#class-fogvolume). This can be used to vary fog density within the [FogVolume](class_fogvolume.md#class-fogvolume) with any kind of static pattern. For animated effects, consider using a custom [fog shader](../tutorials/shaders/shader_reference/fog_shader.md).

---

[float](class_float.md#class-float) **edge_fade** = `0.1`

-  **set_edge_fade**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_edge_fade**()

The hardness of the edges of the [FogVolume](class_fogvolume.md#class-fogvolume). A higher value will result in softer edges, while a lower value will result in harder edges.

---

[Color](class_color.md#class-color) **emission** = `Color(0, 0, 0, 1)`

-  **set_emission**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_emission**()

The [Color](class_color.md#class-color) of the light emitted by the [FogVolume](class_fogvolume.md#class-fogvolume). Emitted light will not cast light or shadows on other objects, but can be useful for modulating the [Color](class_color.md#class-color) of the [FogVolume](class_fogvolume.md#class-fogvolume) independently from light sources.

---

[float](class_float.md#class-float) **height_falloff** = `0.0`

-  **set_height_falloff**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height_falloff**()

The rate by which the height-based fog decreases in density as height increases in world space. A high falloff will result in a sharp transition, while a low falloff will result in a smoother transition. A value of `0.0` results in uniform-density fog. The height threshold is determined by the height of the associated [FogVolume](class_fogvolume.md#class-fogvolume).
