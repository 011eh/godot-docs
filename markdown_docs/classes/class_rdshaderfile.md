# RDShaderFile

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Compiled shader file in SPIR-V form (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)). Not to be confused with Godot's own [Shader](class_shader.md#class-shader).

## Description

Compiled shader file in SPIR-V form.

See also [RDShaderSource](class_rdshadersource.md#class-rdshadersource). **RDShaderFile** is only meant to be used with the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) API. It should not be confused with Godot's own [Shader](class_shader.md#class-shader) resource, which is what Godot's various nodes use for high-level shader programming.

## Properties

| [String](class_string.md#class-string)   | base_error   | `""`   |
|------------------------------------------|---------------------------------------------------------|--------|

## Methods

| [RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv)                             | get_spirv(version: [StringName](class_stringname.md#class-stringname) = &"")                                                                              |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_version_list()                                                                                                                                 |
|                                                                                         | set_bytecode(bytecode: [RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv), version: [StringName](class_stringname.md#class-stringname) = &"") |

---

## Property Descriptions

[String](class_string.md#class-string) **base_error** = `""`

-  **set_base_error**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_base_error**()

The base compilation error message, which indicates errors not related to a specific shader stage if non-empty. If empty, shader compilation is not necessarily successful (check [RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv)'s error message members).

---

## Method Descriptions

[RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv) **get_spirv**(version: [StringName](class_stringname.md#class-stringname) = &"")

Returns the SPIR-V intermediate representation for the specified shader `version`.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_version_list**()

Returns the list of compiled versions for this shader.

---

 **set_bytecode**(bytecode: [RDShaderSPIRV](class_rdshaderspirv.md#class-rdshaderspirv), version: [StringName](class_stringname.md#class-stringname) = &"")

Sets the SPIR-V `bytecode` that will be compiled for the specified `version`.
