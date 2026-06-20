# RDShaderSource

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Shader source code (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

Shader source code in text form.

See also [RDShaderFile](class_rdshaderfile.md#class-rdshaderfile). **RDShaderSource** is only meant to be used with the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) API. It should not be confused with Godot's own [Shader](class_shader.md#class-shader) resource, which is what Godot's various nodes use for high-level shader programming.

## Properties

| [ShaderLanguage](class_renderingdevice.md#enum-renderingdevice-shaderlanguage)   | language                                           | `0`   |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------|
| [String](class_string.md#class-string)                                           | source_any_hit                               | `""`  |
| [String](class_string.md#class-string)                                           | source_closest_hit                       | `""`  |
| [String](class_string.md#class-string)                                           | source_compute                               | `""`  |
| [String](class_string.md#class-string)                                           | source_fragment                             | `""`  |
| [String](class_string.md#class-string)                                           | source_intersection                     | `""`  |
| [String](class_string.md#class-string)                                           | source_miss                                     | `""`  |
| [String](class_string.md#class-string)                                           | source_raygen                                 | `""`  |
| [String](class_string.md#class-string)                                           | source_tesselation_control       | `""`  |
| [String](class_string.md#class-string)                                           | source_tesselation_evaluation | `""`  |
| [String](class_string.md#class-string)                                           | source_vertex                                 | `""`  |

## Methods

| [String](class_string.md#class-string)   | get_stage_source(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage))                                                 |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                          | set_stage_source(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string)) |

---

## Property Descriptions

[ShaderLanguage](class_renderingdevice.md#enum-renderingdevice-shaderlanguage) **language** = `0`

-  **set_language**(value: [ShaderLanguage](class_renderingdevice.md#enum-renderingdevice-shaderlanguage))
- [ShaderLanguage](class_renderingdevice.md#enum-renderingdevice-shaderlanguage) **get_language**()

The language the shader is written in.

---

[String](class_string.md#class-string) **source_any_hit** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's any hit stage.

---

[String](class_string.md#class-string) **source_closest_hit** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's closest hit stage.

---

[String](class_string.md#class-string) **source_compute** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's compute stage.

---

[String](class_string.md#class-string) **source_fragment** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's fragment stage.

---

[String](class_string.md#class-string) **source_intersection** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's intersection stage.

---

[String](class_string.md#class-string) **source_miss** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's miss stage.

---

[String](class_string.md#class-string) **source_raygen** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's ray generation stage.

---

[String](class_string.md#class-string) **source_tesselation_control** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's tessellation control stage.

---

[String](class_string.md#class-string) **source_tesselation_evaluation** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's tessellation evaluation stage.

---

[String](class_string.md#class-string) **source_vertex** = `""`

-  **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

Source code for the shader's vertex stage.

---

## Method Descriptions

[String](class_string.md#class-string) **get_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage))

Returns source code for the specified shader `stage`. Equivalent to getting one of source_compute, source_fragment, source_tesselation_control, source_tesselation_evaluation or source_vertex.

---

 **set_stage_source**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), source: [String](class_string.md#class-string))

Sets `source` code for the specified shader `stage`. Equivalent to setting one of source_compute, source_fragment, source_tesselation_control, source_tesselation_evaluation or source_vertex.

**Note:** If you set the compute shader source code using this method directly, remember to remove the Godot-specific hint `#[compute]`.
