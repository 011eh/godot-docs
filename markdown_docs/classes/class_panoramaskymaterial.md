# PanoramaSkyMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material that provides a special texture to a [Sky](class_sky.md#class-sky), usually an HDR panorama.

## Description

A resource referenced in a [Sky](class_sky.md#class-sky) that is used to draw a background. **PanoramaSkyMaterial** functions similar to skyboxes in other engines, except it uses an equirectangular sky map instead of a [Cubemap](class_cubemap.md#class-cubemap).

Using an HDR panorama is strongly recommended for accurate, high-quality reflections. Godot supports the Radiance HDR (`.hdr`) and OpenEXR (`.exr`) image formats for this purpose.

You can use [this tool](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html) to convert a cubemap to an equirectangular sky map.

## Properties

| [float](class_float.md#class-float)             | energy_multiplier   | `1.0`   |
|-------------------------------------------------|------------------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)                | filter                         | `true`  |
| [Texture2D](class_texture2d.md#class-texture2d) | panorama                     |         |

---

## Property Descriptions

[float](class_float.md#class-float) **energy_multiplier** = `1.0`

-  **set_energy_multiplier**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_energy_multiplier**()

The sky's overall brightness multiplier. Higher values result in a brighter sky.

---

[bool](class_bool.md#class-bool) **filter** = `true`

-  **set_filtering_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_filtering_enabled**()

A boolean value to determine if the background texture should be filtered or not.

---

[Texture2D](class_texture2d.md#class-texture2d) **panorama**

-  **set_panorama**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_panorama**()

[Texture2D](class_texture2d.md#class-texture2d) to be applied to the **PanoramaSkyMaterial**.
