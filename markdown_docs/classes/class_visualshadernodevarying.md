# VisualShaderNodeVarying

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeVaryingGetter](class_visualshadernodevaryinggetter.md#class-visualshadernodevaryinggetter), [VisualShaderNodeVaryingSetter](class_visualshadernodevaryingsetter.md#class-visualshadernodevaryingsetter)

A visual shader node that represents a "varying" shader value.

## Description

Varying values are shader variables that can be passed between shader functions, e.g. from Vertex shader to Fragment shader.

## Properties

| [String](class_string.md#class-string)                             | varying_name   | `"[None]"`   |
|--------------------------------------------------------------------|------------------------------------------------------------------------|--------------|
| [VaryingType](class_visualshader.md#enum-visualshader-varyingtype) | varying_type   | `0`          |

---

## Property Descriptions

[String](class_string.md#class-string) **varying_name** = `"[None]"`

-  **set_varying_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_varying_name**()

Name of the variable. Must be unique.

---

[VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **varying_type** = `0`

-  **set_varying_type**(value: [VaryingType](class_visualshader.md#enum-visualshader-varyingtype))
- [VaryingType](class_visualshader.md#enum-visualshader-varyingtype) **get_varying_type**()

Type of the variable. Determines where the variable can be accessed.
