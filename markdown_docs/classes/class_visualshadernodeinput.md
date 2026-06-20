# VisualShaderNodeInput

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents the input shader parameter within the visual shader graph.

## Description

Gives access to input variables (built-ins) available for the shader. See the shading reference for the list of available built-ins for each shader type (check `Tutorials` section for link).

## Tutorials

- [Shading reference index](../tutorials/shaders/shader_reference/index.md)

## Properties

| [String](class_string.md#class-string)   | input_name   | `"[None]"`   |
|------------------------------------------|------------------------------------------------------------------|--------------|

## Methods

| [String](class_string.md#class-string)   | get_input_real_name()    |
|------------------------------------------|-------------------------------------------------------------------------------------|

---

## Signals

**input_type_changed**()

Emitted when input is changed via input_name.

---

## Property Descriptions

[String](class_string.md#class-string) **input_name** = `"[None]"`

-  **set_input_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_input_name**()

One of the several input constants in lower-case style like: "vertex" (`VERTEX`) or "point_size" (`POINT_SIZE`).

---

## Method Descriptions

[String](class_string.md#class-string) **get_input_real_name**()

Returns a translated name of the current constant in the Godot Shader Language. E.g. `"ALBEDO"` if the input_name equal to `"albedo"`.
