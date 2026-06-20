# OpenXRIPBinding

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Defines a binding between an [OpenXRAction](class_openxraction.md#class-openxraction) and an XR input or output.

## Description

This binding resource binds an [OpenXRAction](class_openxraction.md#class-openxraction) to an input or output. As most controllers have left hand and right versions that are handled by the same interaction profile we can specify multiple bindings. For instance an action "Fire" could be bound to both "/user/hand/left/input/trigger" and "/user/hand/right/input/trigger". This would require two binding entries.

## Properties

| [OpenXRAction](class_openxraction.md#class-openxraction)                | action                       |      |
|-------------------------------------------------------------------------|------------------------------------------------------------------------|------|
| [Array](class_array.md#class-array)                                     | binding_modifiers | `[]` |
| [String](class_string.md#class-string)                                  | binding_path           | `""` |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | paths                         |      |

## Methods

|                                                                                                       | add_path(path: [String](class_string.md#class-string))                 |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class-openxractionbindingmodifier) | get_binding_modifier(index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int)                                                                         | get_binding_modifier_count()                         |
| [int](class_int.md#class-int)                                                                         | get_path_count()                                                 |
| [bool](class_bool.md#class-bool)                                                                      | has_path(path: [String](class_string.md#class-string))                 |
|                                                                                                       | remove_path(path: [String](class_string.md#class-string))           |

---

## Property Descriptions

[OpenXRAction](class_openxraction.md#class-openxraction) **action**

-  **set_action**(value: [OpenXRAction](class_openxraction.md#class-openxraction))
- [OpenXRAction](class_openxraction.md#class-openxraction) **get_action**()

[OpenXRAction](class_openxraction.md#class-openxraction) that is bound to binding_path.

---

[Array](class_array.md#class-array) **binding_modifiers** = `[]`

-  **set_binding_modifiers**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_binding_modifiers**()

Binding modifiers for this binding.

---

[String](class_string.md#class-string) **binding_path** = `""`

-  **set_binding_path**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_binding_path**()

Binding path that defines the input or output bound to action.

**Note:** Binding paths are suggestions, an XR runtime may choose to bind the action to a different input or output emulating this input or output.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **paths**

-  **set_paths**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_paths**()

**Deprecated:** Use binding_path instead.

Paths that define the inputs or outputs bound on the device.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

## Method Descriptions

 **add_path**(path: [String](class_string.md#class-string))

**Deprecated:** Binding is for a single path.

Add an input/output path to this binding.

---

[OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class-openxractionbindingmodifier) **get_binding_modifier**(index: [int](class_int.md#class-int))

Get the [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) at this index.

---

[int](class_int.md#class-int) **get_binding_modifier_count**()

Get the number of binding modifiers for this binding.

---

[int](class_int.md#class-int) **get_path_count**()

**Deprecated:** Binding is for a single path.

Get the number of input/output paths in this binding.

---

[bool](class_bool.md#class-bool) **has_path**(path: [String](class_string.md#class-string))

**Deprecated:** Binding is for a single path.

Returns `true` if this input/output path is part of this binding.

---

 **remove_path**(path: [String](class_string.md#class-string))

**Deprecated:** Binding is for a single path.

Removes this input/output path from this binding.
