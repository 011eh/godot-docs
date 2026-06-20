# VisualShaderNodeVec3Parameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Vector3](class_vector3.md#class-vector3) parameter to be used within the visual shader graph.

## Description

Translated to `uniform vec3` in the shader language.

## Properties

| [Vector3](class_vector3.md#class-vector3)   | default_value                 | `Vector3(0, 0, 0)`   |
|---------------------------------------------|----------------------------------------------------------------------------------------------|----------------------|
| [bool](class_bool.md#class-bool)            | default_value_enabled | `false`              |

---

## Property Descriptions

[Vector3](class_vector3.md#class-vector3) **default_value** = `Vector3(0, 0, 0)`

-  **set_default_value**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_default_value**()

A default value to be assigned within the shader.

---

[bool](class_bool.md#class-bool) **default_value_enabled** = `false`

-  **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the default_value.
