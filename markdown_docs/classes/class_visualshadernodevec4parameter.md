# VisualShaderNodeVec4Parameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 4D vector parameter to be used within the visual shader graph.

## Description

Translated to `uniform vec4` in the shader language.

## Properties

| [Vector4](class_vector4.md#class-vector4)   | default_value                 | `Vector4(0, 0, 0, 0)`   |
|---------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------|
| [bool](class_bool.md#class-bool)            | default_value_enabled | `false`                 |

---

## Property Descriptions

[Vector4](class_vector4.md#class-vector4) **default_value** = `Vector4(0, 0, 0, 0)`

-  **set_default_value**(value: [Vector4](class_vector4.md#class-vector4))
- [Vector4](class_vector4.md#class-vector4) **get_default_value**()

A default value to be assigned within the shader.

---

[bool](class_bool.md#class-bool) **default_value_enabled** = `false`

-  **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the default_value.
