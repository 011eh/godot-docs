# VisualShaderNodeIntParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A visual shader node for shader parameter (uniform) of type [int](class_int.md#class-int).

## Description

A [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) of type [int](class_int.md#class-int). Offers additional customization for range of accepted values.

## Properties

| [int](class_int.md#class-int)                                           | default_value                 | `0`                   |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------|
| [bool](class_bool.md#class-bool)                                        | default_value_enabled | `false`               |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | enum_names                       | `PackedStringArray()` |
| Hint                         | hint                                   | `0`                   |
| [int](class_int.md#class-int)                                           | max                                     | `100`                 |
| [int](class_int.md#class-int)                                           | min                                     | `0`                   |
| [int](class_int.md#class-int)                                           | step                                   | `1`                   |

---

## Enumerations

enum **Hint**:

Hint **HINT_NONE** = `0`

The parameter will not constrain its value.

Hint **HINT_RANGE** = `1`

The parameter's value must be within the specified min/max range.

Hint **HINT_RANGE_STEP** = `2`

The parameter's value must be within the specified range, with the given step between values.

Hint **HINT_ENUM** = `3`

The parameter uses an enum to associate preset values to names in the editor.

Hint **HINT_MAX** = `4`

Represents the size of the Hint enum.

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

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **enum_names** = `PackedStringArray()`

-  **set_enum_names**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_enum_names**()

The names used for the enum select in the editor. hint must be HINT_ENUM for this to take effect.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

Hint **hint** = `0`

-  **set_hint**(value: Hint)
- Hint **get_hint**()

Range hint of this node. Use it to customize valid parameter range.

---

[int](class_int.md#class-int) **max** = `100`

-  **set_max**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max**()

The maximum value this parameter can take. hint must be either HINT_RANGE or HINT_RANGE_STEP for this to take effect.

---

[int](class_int.md#class-int) **min** = `0`

-  **set_min**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_min**()

The minimum value this parameter can take. hint must be either HINT_RANGE or HINT_RANGE_STEP for this to take effect.

---

[int](class_int.md#class-int) **step** = `1`

-  **set_step**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_step**()

The step between parameter's values. Forces the parameter to be a multiple of the given value. hint must be HINT_RANGE_STEP for this to take effect.
