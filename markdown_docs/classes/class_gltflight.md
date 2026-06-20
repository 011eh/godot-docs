# GLTFLight

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a glTF light.

## Description

Represents a light as defined by the `KHR_lights_punctual` glTF extension.

## Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)
- [KHR_lights_punctual glTF extension spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_lights_punctual)

## Properties

| [Color](class_color.md#class-color)    | color                       | `Color(1, 1, 1, 1)`   |
|----------------------------------------|----------------------------------------------------------------|-----------------------|
| [float](class_float.md#class-float)    | inner_cone_angle | `0.0`                 |
| [float](class_float.md#class-float)    | intensity               | `1.0`                 |
| [String](class_string.md#class-string) | light_type             | `""`                  |
| [float](class_float.md#class-float)    | outer_cone_angle | `0.7853982`           |
| [float](class_float.md#class-float)    | range                       | `inf`                 |

## Methods

| GLTFLight                      | from_dictionary(dictionary: [Dictionary](class_dictionary.md#class-dictionary))                                                                         |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GLTFLight                      | from_node(light_node: [Light3D](class_light3d.md#class-light3d))                                                                                              |
| [Variant](class_variant.md#class-variant)          | get_additional_data(extension_name: [StringName](class_stringname.md#class-stringname))                                                             |
|                                                    | set_additional_data(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant)) |
| [Dictionary](class_dictionary.md#class-dictionary) | to_dictionary()                                                                                                                                           |
| [Light3D](class_light3d.md#class-light3d)          | to_node()                                                                                                                                                       |

---

## Property Descriptions

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)`

-  **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The [Color](class_color.md#class-color) of the light in linear space. Defaults to white. A black color causes the light to have no effect.

This value is linear to match glTF, but will be converted to nonlinear sRGB when creating a Godot [Light3D](class_light3d.md#class-light3d) node upon import, or converted to linear when exporting a Godot [Light3D](class_light3d.md#class-light3d) to glTF.

---

[float](class_float.md#class-float) **inner_cone_angle** = `0.0`

-  **set_inner_cone_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_inner_cone_angle**()

The inner angle of the cone in a spotlight. Must be less than or equal to the outer cone angle.

Within this angle, the light is at full brightness. Between the inner and outer cone angles, there is a transition from full brightness to zero brightness. When creating a Godot [SpotLight3D](class_spotlight3d.md#class-spotlight3d), the ratio between the inner and outer cone angles is used to calculate the attenuation of the light.

---

[float](class_float.md#class-float) **intensity** = `1.0`

-  **set_intensity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_intensity**()

The intensity of the light. This is expressed in candelas (lumens per steradian) for point and spot lights, and lux (lumens per m²) for directional lights. When creating a Godot light, this value is converted to a unitless multiplier.

---

[String](class_string.md#class-string) **light_type** = `""`

-  **set_light_type**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_light_type**()

The type of the light. The values accepted by Godot are "point", "spot", and "directional", which correspond to Godot's [OmniLight3D](class_omnilight3d.md#class-omnilight3d), [SpotLight3D](class_spotlight3d.md#class-spotlight3d), and [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d) respectively.

---

[float](class_float.md#class-float) **outer_cone_angle** = `0.7853982`

-  **set_outer_cone_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_outer_cone_angle**()

The outer angle of the cone in a spotlight. Must be greater than or equal to the inner angle.

At this angle, the light drops off to zero brightness. Between the inner and outer cone angles, there is a transition from full brightness to zero brightness. If this angle is a half turn, then the spotlight emits in all directions. When creating a Godot [SpotLight3D](class_spotlight3d.md#class-spotlight3d), the outer cone angle is used as the angle of the spotlight.

---

[float](class_float.md#class-float) **range** = `inf`

-  **set_range**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_range**()

The range of the light, beyond which the light has no effect. glTF lights with no range defined behave like physical lights (which have infinite range). When creating a Godot light, the range is clamped to `4096.0`.

---

## Method Descriptions

GLTFLight **from_dictionary**(dictionary: [Dictionary](class_dictionary.md#class-dictionary))

Creates a new GLTFLight instance by parsing the given [Dictionary](class_dictionary.md#class-dictionary).

---

GLTFLight **from_node**(light_node: [Light3D](class_light3d.md#class-light3d))

Create a new GLTFLight instance from the given Godot [Light3D](class_light3d.md#class-light3d) node.

---

[Variant](class_variant.md#class-variant) **get_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **set_additional_data**(extension_name: [StringName](class_stringname.md#class-stringname), additional_data: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **to_dictionary**()

Serializes this GLTFLight instance into a [Dictionary](class_dictionary.md#class-dictionary).

---

[Light3D](class_light3d.md#class-light3d) **to_node**()

Converts this GLTFLight instance into a Godot [Light3D](class_light3d.md#class-light3d) node.
