# VisualShaderNodeColorConstant

**Inherits:** [VisualShaderNodeConstant](class_visualshadernodeconstant.md#class-visualshadernodeconstant) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Color](class_color.md#class-color) constant to be used within the visual shader graph.

## Description

Has two output ports representing RGB and alpha channels of [Color](class_color.md#class-color).

Translated to `vec3 rgb` and `float alpha` in the shader language.

## Properties

| [Color](class_color.md#class-color)   | constant   | `Color(1, 1, 1, 1)`   |
|---------------------------------------|----------------------------------------------------------------------|-----------------------|

---

## Property Descriptions

[Color](class_color.md#class-color) **constant** = `Color(1, 1, 1, 1)`

-  **set_constant**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_constant**()

A [Color](class_color.md#class-color) constant which represents a state of this node.
