# VisualShaderNodeBooleanParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A boolean parameter to be used within the visual shader graph.

## Description

Translated to `uniform bool` in the shader language.

## Properties

| [bool](class_bool.md#class-bool)   | default_value                 | `false`   |
|------------------------------------|-------------------------------------------------------------------------------------------------|-----------|
| [bool](class_bool.md#class-bool)   | default_value_enabled | `false`   |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **default_value** = `false`

-  **set_default_value**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_default_value**()

A default value to be assigned within the shader.

---

[bool](class_bool.md#class-bool) **default_value_enabled** = `false`

-  **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the default_value.
