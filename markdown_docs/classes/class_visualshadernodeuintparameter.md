# VisualShaderNodeUIntParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node for shader parameter (uniform) of type unsigned [int](class_int.md#class-int).

## Description

A [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) of type unsigned [int](class_int.md#class-int). Offers additional customization for range of accepted values.

## Properties

| [int](class_int.md#class-int)    | default_value                 | `0`     |
|----------------------------------|----------------------------------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool) | default_value_enabled | `false` |

---

## Property Descriptions

[int](class_int.md#class-int) **default_value** = `0`

-  **set_default_value**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_default_value**()

Default value of this parameter, which will be used if not set externally. default_value_enabled must be enabled; defaults to `0` otherwise.

---

[bool](class_bool.md#class-bool) **default_value_enabled** = `false`

-  **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

If `true`, the node will have a custom default value.
