# VisualShaderNodeExpression

**Inherits:** [VisualShaderNodeGroupBase](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase) **<** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class-visualshadernoderesizablebase) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeGlobalExpression](class_visualshadernodeglobalexpression.md#class-visualshadernodeglobalexpression)

A custom visual shader graph expression written in Godot Shading Language.

## Description

Custom Godot Shading Language expression, with a custom number of input and output ports.

The provided code is directly injected into the graph's matching shader function (`vertex`, `fragment`, or `light`), so it cannot be used to declare functions, varyings, uniforms, or global constants. See [VisualShaderNodeGlobalExpression](class_visualshadernodeglobalexpression.md#class-visualshadernodeglobalexpression) for such global definitions.

## Properties

| [String](class_string.md#class-string)   | expression   | `""`   |
|------------------------------------------|-----------------------------------------------------------------------|--------|

---

## Property Descriptions

[String](class_string.md#class-string) **expression** = `""`

-  **set_expression**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_expression**()

An expression in Godot Shading Language, which will be injected at the start of the graph's matching shader function (`vertex`, `fragment`, or `light`), and thus cannot be used to declare functions, varyings, uniforms, or global constants.
