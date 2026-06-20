# OpenXRInteractionProfile

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Suggested bindings object for OpenXR.

## Description

This object stores suggested bindings for an interaction profile. Interaction profiles define the metadata for a tracked XR device such as an XR controller.

For more information see the [interaction profiles info in the OpenXR specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-interaction-profiles).

## Properties

| [Array](class_array.md#class-array)    | binding_modifiers               | `[]`   |
|----------------------------------------|-----------------------------------------------------------------------------------------------|--------|
| [Array](class_array.md#class-array)    | bindings                                 | `[]`   |
| [String](class_string.md#class-string) | interaction_profile_path | `""`   |

## Methods

| [OpenXRIPBinding](class_openxripbinding.md#class-openxripbinding)                         | get_binding(index: [int](class_int.md#class-int))                   |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                                             | get_binding_count()                                           |
| [OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class-openxripbindingmodifier) | get_binding_modifier(index: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int)                                                             | get_binding_modifier_count()                         |

---

## Property Descriptions

[Array](class_array.md#class-array) **binding_modifiers** = `[]`

-  **set_binding_modifiers**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_binding_modifiers**()

Binding modifiers for this interaction profile.

---

[Array](class_array.md#class-array) **bindings** = `[]`

-  **set_bindings**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_bindings**()

Action bindings for this interaction profile.

---

[String](class_string.md#class-string) **interaction_profile_path** = `""`

-  **set_interaction_profile_path**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_interaction_profile_path**()

The interaction profile path identifying the XR device.

---

## Method Descriptions

[OpenXRIPBinding](class_openxripbinding.md#class-openxripbinding) **get_binding**(index: [int](class_int.md#class-int))

Retrieve the binding at this index.

---

[int](class_int.md#class-int) **get_binding_count**()

Get the number of bindings in this interaction profile.

---

[OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class-openxripbindingmodifier) **get_binding_modifier**(index: [int](class_int.md#class-int))

Get the [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) at this index.

---

[int](class_int.md#class-int) **get_binding_modifier_count**()

Get the number of binding modifiers in this interaction profile.
