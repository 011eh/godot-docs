# OpenXRBindingModifier

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class-openxractionbindingmodifier), [OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class-openxripbindingmodifier)

Binding modifier base class.

## Description

Binding modifier base class. Subclasses implement various modifiers that alter how an OpenXR runtime processes inputs.

## Methods

| [String](class_string.md#class-string)                            | \_get_description()         |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | \_get_ip_modification() |

---

## Method Descriptions

[String](class_string.md#class-string) **\_get_description**()

Return the description of this class that is used for the title bar of the binding modifier editor.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **\_get_ip_modification**()

Returns the data that is sent to OpenXR when submitting the suggested interacting bindings this modifier is a part of.

**Note:** This must be data compatible with an `XrBindingModificationBaseHeaderKHR` structure.
