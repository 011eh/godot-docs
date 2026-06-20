# RDShaderSPIRV

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

SPIR-V intermediate representation as part of an [RDShaderFile](class_rdshaderfile.md#class-rdshaderfile) (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

**RDShaderSPIRV** represents an [RDShaderFile](class_rdshaderfile.md#class-rdshaderfile)'s [SPIR-V](https://www.khronos.org/spir/) code for various shader stages, as well as possible compilation error messages. SPIR-V is a low-level intermediate shader representation. This intermediate representation is not used directly by GPUs for rendering, but it can be compiled into binary shaders that GPUs can understand. Unlike compiled shaders, SPIR-V is portable across GPU models and driver versions.

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_any_hit                                         | `PackedByteArray()`   |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------|
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_closest_hit                                 | `PackedByteArray()`   |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_compute                                         | `PackedByteArray()`   |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_fragment                                       | `PackedByteArray()`   |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_intersection                               | `PackedByteArray()`   |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_miss                                               | `PackedByteArray()`   |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_raygen                                           | `PackedByteArray()`   |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_tesselation_control                 | `PackedByteArray()`   |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_tesselation_evaluation           | `PackedByteArray()`   |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | bytecode_vertex                                           | `PackedByteArray()`   |
| [String](class_string.md#class-string)                              | compile_error_any_hit                               | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_closest_hit                       | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_compute                               | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_fragment                             | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_intersection                     | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_miss                                     | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_raygen                                 | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_tesselation_control       | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_tesselation_evaluation | `""`                  |
| [String](class_string.md#class-string)                              | compile_error_vertex                                 | `""`                  |

## Methods

| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | get_stage_bytecode(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage))                                                                              |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                              | get_stage_compile_error(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage))                                                                    |
|                                                                     | set_stage_bytecode(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray)) |
|                                                                     | set_stage_compile_error(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))             |

---

## Property Descriptions

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_any_hit** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the any hit shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_closest_hit** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the closest hit shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_compute** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the compute shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_fragment** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the fragment shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_intersection** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the intersection shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_miss** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the miss shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_raygen** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the ray generation shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_tesselation_control** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the tessellation control shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_tesselation_evaluation** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the tessellation evaluation shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **bytecode_vertex** = `PackedByteArray()`

-  **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The SPIR-V bytecode for the vertex shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

[String](class_string.md#class-string) **compile_error_any_hit** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the any hit shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_closest_hit** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the closest hit shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_compute** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the compute shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_fragment** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the fragment shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_intersection** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the intersection shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_miss** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the miss shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_raygen** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the ray generation shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_tesselation_control** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the tessellation control shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_tesselation_evaluation** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the tessellation evaluation shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

[String](class_string.md#class-string) **compile_error_vertex** = `""`

-  **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage)) 

The compilation error message for the vertex shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

## Method Descriptions

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage))

Equivalent to getting one of bytecode_compute, bytecode_fragment, bytecode_tesselation_control, bytecode_tesselation_evaluation, bytecode_vertex.

---

[String](class_string.md#class-string) **get_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage))

Returns the compilation error message for the given shader `stage`. Equivalent to getting one of compile_error_compute, compile_error_fragment, compile_error_tesselation_control, compile_error_tesselation_evaluation, compile_error_vertex.

---

 **set_stage_bytecode**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), bytecode: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Sets the SPIR-V `bytecode` for the given shader `stage`. Equivalent to setting one of bytecode_compute, bytecode_fragment, bytecode_tesselation_control, bytecode_tesselation_evaluation, bytecode_vertex.

---

 **set_stage_compile_error**(stage: [ShaderStage](class_renderingdevice.md#enum-renderingdevice-shaderstage), compile_error: [String](class_string.md#class-string))

Sets the compilation error message for the given shader `stage` to `compile_error`. Equivalent to setting one of compile_error_compute, compile_error_fragment, compile_error_tesselation_control, compile_error_tesselation_evaluation, compile_error_vertex.
