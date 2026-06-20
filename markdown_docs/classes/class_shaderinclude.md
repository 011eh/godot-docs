# ShaderInclude

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A snippet of shader code to be included in a [Shader](class_shader.md#class-shader) with `#include`.

## Description

A shader include file, saved with the `.gdshaderinc` extension. This class allows you to define a custom shader snippet that can be included in a [Shader](class_shader.md#class-shader) by using the preprocessor directive `#include`, followed by the file path (e.g. `#include "res://shader_lib.gdshaderinc"`). The snippet doesn't have to be a valid shader on its own.

## Tutorials

- [Shader preprocessor](../tutorials/shaders/shader_reference/shader_preprocessor.md)

## Properties

| [String](class_string.md#class-string)   | code   | `""`   |
|------------------------------------------|----------------------------------------------|--------|

---

## Property Descriptions

[String](class_string.md#class-string) **code** = `""`

-  **set_code**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_code**()

Returns the code of the shader include file. The returned text is what the user has written, not the full generated code used internally.
