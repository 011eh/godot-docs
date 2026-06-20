# RDPipelineShader

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline shader (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

Wraps a shader resource and allows specialization constants to be applied at pipeline creation time.

Used by [RenderingDevice.raytracing_pipeline_create()](class_renderingdevice.md#class-renderingdevice-method-raytracing-pipeline-create) for ray generation, miss, and hit shaders. The pipeline selects the required shader stage automatically.

## Properties

| [RID](class_rid.md#class-rid)                                                                                                                             | shader                                     | `RID()`   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-----------|
| [Array](class_array.md#class-array)[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class-rdpipelinespecializationconstant)] | specialization_constants | `[]`      |

---

## Property Descriptions

[RID](class_rid.md#class-rid) **shader** = `RID()`

-  **set_shader**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_shader**()

Shader resource. The required stage is selected by the pipeline.

---

[Array](class_array.md#class-array)[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class-rdpipelinespecializationconstant)] **specialization_constants** = `[]`

-  **set_specialization_constants**(value: [Array](class_array.md#class-array)[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class-rdpipelinespecializationconstant)])
- [Array](class_array.md#class-array)[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class-rdpipelinespecializationconstant)] **get_specialization_constants**()

Specialization constants applied to the selected shader stage at pipeline creation time.
