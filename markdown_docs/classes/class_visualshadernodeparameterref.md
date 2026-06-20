# VisualShaderNodeParameterRef

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A reference to an existing [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter).

## Description

Creating a reference to a [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) allows you to reuse this parameter in different shaders or shader stages easily.

## Properties

| [String](class_string.md#class-string)   | parameter_name   | `"[None]"`   |
|------------------------------------------|---------------------------------------------------------------------------------|--------------|

---

## Property Descriptions

[String](class_string.md#class-string) **parameter_name** = `"[None]"`

-  **set_parameter_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_parameter_name**()

The name of the parameter which this reference points to.
