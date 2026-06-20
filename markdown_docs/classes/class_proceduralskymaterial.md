# ProceduralSkyMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material that defines a simple sky for a [Sky](class_sky.md#class-sky) resource.

## Description

**ProceduralSkyMaterial** provides a way to create an effective background quickly by defining procedural parameters for the sun, the sky and the ground. The sky and ground are defined by a main color, a color at the horizon, and an easing curve to interpolate between them. Suns are described by a position in the sky, a color, and a max angle from the sun at which the easing curve ends. The max angle therefore defines the size of the sun in the sky.

**ProceduralSkyMaterial** supports up to 4 suns, using the color, and energy, direction, and angular distance of the first four [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d) nodes in the scene. This means that the suns are defined individually by the properties of their corresponding [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d)s and globally by sun_angle_max and sun_curve.

**ProceduralSkyMaterial** uses a lightweight shader to draw the sky and is therefore suited for real-time updates. This makes it a great option for a sky that is simple and computationally cheap, but unrealistic. If you need a more realistic procedural option, use [PhysicalSkyMaterial](class_physicalskymaterial.md#class-physicalskymaterial).

## Properties

| [float](class_float.md#class-float)             | energy_multiplier               | `1.0`                              |
|-------------------------------------------------|--------------------------------------------------------------------------------------------|------------------------------------|
| [Color](class_color.md#class-color)             | ground_bottom_color           | `Color(0.2, 0.169, 0.133, 1)`      |
| [float](class_float.md#class-float)             | ground_curve                         | `0.02`                             |
| [float](class_float.md#class-float)             | ground_energy_multiplier | `1.0`                              |
| [Color](class_color.md#class-color)             | ground_horizon_color         | `Color(0.6463, 0.6558, 0.6708, 1)` |
| [Texture2D](class_texture2d.md#class-texture2d) | sky_cover                               |                                    |
| [Color](class_color.md#class-color)             | sky_cover_modulate             | `Color(1, 1, 1, 1)`                |
| [float](class_float.md#class-float)             | sky_curve                               | `0.15`                             |
| [float](class_float.md#class-float)             | sky_energy_multiplier       | `1.0`                              |
| [Color](class_color.md#class-color)             | sky_horizon_color               | `Color(0.6463, 0.6558, 0.6708, 1)` |
| [Color](class_color.md#class-color)             | sky_top_color                       | `Color(0.385, 0.454, 0.55, 1)`     |
| [float](class_float.md#class-float)             | sun_angle_max                       | `30.0`                             |
| [float](class_float.md#class-float)             | sun_curve                               | `0.15`                             |
| [bool](class_bool.md#class-bool)                | use_debanding                       | `true`                             |

---

## Property Descriptions

[float](class_float.md#class-float) **energy_multiplier** = `1.0`

-  **set_energy_multiplier**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_energy_multiplier**()

The sky's overall brightness multiplier. Higher values result in a brighter sky.

---

[Color](class_color.md#class-color) **ground_bottom_color** = `Color(0.2, 0.169, 0.133, 1)`

-  **set_ground_bottom_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_ground_bottom_color**()

Color of the ground at the bottom. Blends with ground_horizon_color.

---

[float](class_float.md#class-float) **ground_curve** = `0.02`

-  **set_ground_curve**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_ground_curve**()

How quickly the ground_horizon_color fades into the ground_bottom_color.

---

[float](class_float.md#class-float) **ground_energy_multiplier** = `1.0`

-  **set_ground_energy_multiplier**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_ground_energy_multiplier**()

Multiplier for ground color. A higher value will make the ground brighter.

---

[Color](class_color.md#class-color) **ground_horizon_color** = `Color(0.6463, 0.6558, 0.6708, 1)`

-  **set_ground_horizon_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_ground_horizon_color**()

Color of the ground at the horizon. Blends with ground_bottom_color.

---

[Texture2D](class_texture2d.md#class-texture2d) **sky_cover**

-  **set_sky_cover**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_sky_cover**()

The sky cover texture to use. This texture must use an equirectangular projection (similar to [PanoramaSkyMaterial](class_panoramaskymaterial.md#class-panoramaskymaterial)). The texture's colors will be *added* to the existing sky color, and will be multiplied by sky_energy_multiplier and sky_cover_modulate. This is mainly suited to displaying stars at night, but it can also be used to display clouds at day or night (with a non-physically-accurate look).

---

[Color](class_color.md#class-color) **sky_cover_modulate** = `Color(1, 1, 1, 1)`

-  **set_sky_cover_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_sky_cover_modulate**()

The tint to apply to the sky_cover texture. This can be used to change the sky cover's colors or opacity independently of the sky energy, which is useful for day/night or weather transitions. Only effective if a texture is defined in sky_cover.

---

[float](class_float.md#class-float) **sky_curve** = `0.15`

-  **set_sky_curve**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sky_curve**()

How quickly the sky_horizon_color fades into the sky_top_color.

---

[float](class_float.md#class-float) **sky_energy_multiplier** = `1.0`

-  **set_sky_energy_multiplier**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sky_energy_multiplier**()

Multiplier for sky color. A higher value will make the sky brighter.

---

[Color](class_color.md#class-color) **sky_horizon_color** = `Color(0.6463, 0.6558, 0.6708, 1)`

-  **set_sky_horizon_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_sky_horizon_color**()

Color of the sky at the horizon. Blends with sky_top_color.

---

[Color](class_color.md#class-color) **sky_top_color** = `Color(0.385, 0.454, 0.55, 1)`

-  **set_sky_top_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_sky_top_color**()

Color of the sky at the top. Blends with sky_horizon_color.

---

[float](class_float.md#class-float) **sun_angle_max** = `30.0`

-  **set_sun_angle_max**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sun_angle_max**()

Distance from center of sun where it fades out completely.

---

[float](class_float.md#class-float) **sun_curve** = `0.15`

-  **set_sun_curve**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sun_curve**()

How quickly the sun fades away between the edge of the sun disk and sun_angle_max.

---

[bool](class_bool.md#class-bool) **use_debanding** = `true`

-  **set_use_debanding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_debanding**()

If `true`, enables debanding. Debanding adds a small amount of noise which helps reduce banding that appears from the smooth changes in color in the sky.
