# VisualShaderNodeColorParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Color](class_color.md#class-color) parameter to be used within the visual shader graph.

## Description

Translated to `uniform vec4` in the shader language.

## Properties

| [Color](class_color.md#class-color)   | default_value                 | `Color(1, 1, 1, 1)`   |
|---------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------|
| [bool](class_bool.md#class-bool)      | default_value_enabled | `false`               |

---

## Property Descriptions

[Color](class_color.md#class-color) **default_value** = `Color(1, 1, 1, 1)`

-  **set_default_value**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_default_value**()

A default value to be assigned within the shader.

---

[bool](class_bool.md#class-bool) **default_value_enabled** = `false`

-  **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the default_value.
