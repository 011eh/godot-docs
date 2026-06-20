# PhysicalSkyMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material that defines a sky for a [Sky](class_sky.md#class-sky) resource by a set of physical properties.

## Description

The **PhysicalSkyMaterial** uses the Preetham analytic daylight model to draw a sky based on physical properties. This results in a substantially more realistic sky than the [ProceduralSkyMaterial](class_proceduralskymaterial.md#class-proceduralskymaterial), but it is slightly slower and less flexible.

The **PhysicalSkyMaterial** only supports one sun. The color, energy, and direction of the sun are taken from the first [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d) in the scene tree.

## Properties

| [float](class_float.md#class-float)             | energy_multiplier       | `1.0`                          |
|-------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------|
| [Color](class_color.md#class-color)             | ground_color                 | `Color(0.1, 0.07, 0.034, 1)`   |
| [float](class_float.md#class-float)             | mie_coefficient           | `0.005`                        |
| [Color](class_color.md#class-color)             | mie_color                       | `Color(0.69, 0.729, 0.812, 1)` |
| [float](class_float.md#class-float)             | mie_eccentricity         | `0.8`                          |
| [Texture2D](class_texture2d.md#class-texture2d) | night_sky                       |                                |
| [float](class_float.md#class-float)             | rayleigh_coefficient | `2.0`                          |
| [Color](class_color.md#class-color)             | rayleigh_color             | `Color(0.3, 0.405, 0.6, 1)`    |
| [float](class_float.md#class-float)             | sun_disk_scale             | `1.0`                          |
| [float](class_float.md#class-float)             | turbidity                       | `10.0`                         |
| [bool](class_bool.md#class-bool)                | use_debanding               | `true`                         |

---

## Property Descriptions

[float](class_float.md#class-float) **energy_multiplier** = `1.0`

-  **set_energy_multiplier**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_energy_multiplier**()

The sky's overall brightness multiplier. Higher values result in a brighter sky.

---

[Color](class_color.md#class-color) **ground_color** = `Color(0.1, 0.07, 0.034, 1)`

-  **set_ground_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_ground_color**()

Modulates the [Color](class_color.md#class-color) on the bottom half of the sky to represent the ground.

---

[float](class_float.md#class-float) **mie_coefficient** = `0.005`

-  **set_mie_coefficient**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mie_coefficient**()

Controls the strength of [Mie scattering](https://en.wikipedia.org/wiki/Mie_scattering) for the sky. Mie scattering results from light colliding with larger particles (like water). On earth, Mie scattering results in a whitish color around the sun and horizon.

---

[Color](class_color.md#class-color) **mie_color** = `Color(0.69, 0.729, 0.812, 1)`

-  **set_mie_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_mie_color**()

Controls the [Color](class_color.md#class-color) of the [Mie scattering](https://en.wikipedia.org/wiki/Mie_scattering) effect. While not physically accurate, this allows for the creation of alien-looking planets.

---

[float](class_float.md#class-float) **mie_eccentricity** = `0.8`

-  **set_mie_eccentricity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mie_eccentricity**()

Controls the direction of the [Mie scattering](https://en.wikipedia.org/wiki/Mie_scattering). A value of `1` means that when light hits a particle it's passing through straight forward. A value of `-1` means that all light is scatter backwards.

---

[Texture2D](class_texture2d.md#class-texture2d) **night_sky**

-  **set_night_sky**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_night_sky**()

[Texture2D](class_texture2d.md#class-texture2d) for the night sky. This is added to the sky, so if it is bright enough, it may be visible during the day.

---

[float](class_float.md#class-float) **rayleigh_coefficient** = `2.0`

-  **set_rayleigh_coefficient**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_rayleigh_coefficient**()

Controls the strength of the [Rayleigh scattering](https://en.wikipedia.org/wiki/Rayleigh_scattering). Rayleigh scattering results from light colliding with small particles. It is responsible for the blue color of the sky.

---

[Color](class_color.md#class-color) **rayleigh_color** = `Color(0.3, 0.405, 0.6, 1)`

-  **set_rayleigh_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_rayleigh_color**()

Controls the [Color](class_color.md#class-color) of the [Rayleigh scattering](https://en.wikipedia.org/wiki/Rayleigh_scattering). While not physically accurate, this allows for the creation of alien-looking planets. For example, setting this to a red [Color](class_color.md#class-color) results in a Mars-looking atmosphere with a corresponding blue sunset.

---

[float](class_float.md#class-float) **sun_disk_scale** = `1.0`

-  **set_sun_disk_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sun_disk_scale**()

Sets the size of the sun disk. Default value is based on Sol's perceived size from Earth.

---

[float](class_float.md#class-float) **turbidity** = `10.0`

-  **set_turbidity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_turbidity**()

Sets the thickness of the atmosphere. High turbidity creates a foggy-looking atmosphere, while a low turbidity results in a clearer atmosphere.

---

[bool](class_bool.md#class-bool) **use_debanding** = `true`

-  **set_use_debanding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_debanding**()

If `true`, enables debanding. Debanding adds a small amount of noise which helps reduce banding that appears from the smooth changes in color in the sky.
