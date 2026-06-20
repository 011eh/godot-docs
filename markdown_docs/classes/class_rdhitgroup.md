# RDHitGroup

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Hit group (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

Defines a hit group for use with [RenderingDevice.raytracing_pipeline_create()](class_renderingdevice.md#class-renderingdevice-method-raytracing-pipeline-create).

A hit group combines shaders that are executed when a ray intersects geometry. It may include a closest-hit shader, any-hit shader, and intersection shader.

Hit groups are referenced by index when populating hit shader binding tables using [RenderingDevice.hit_sbt_range_update()](class_renderingdevice.md#class-renderingdevice-method-hit-sbt-range-update).

## Properties

| [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader)   | any_hit_shader           |
|------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader)   | closest_hit_shader   |
| [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader)   | intersection_shader |

---

## Property Descriptions

[RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **any_hit_shader**

-  **set_any_hit_shader**(value: [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader))
- [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **get_any_hit_shader**()

Any-hit shader for this hit group. Executed for each potential intersection. Can be `null`.

---

[RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **closest_hit_shader**

-  **set_closest_hit_shader**(value: [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader))
- [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **get_closest_hit_shader**()

Closest-hit shader for this hit group. Executed for the closest intersection. Can be `null`.

---

[RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **intersection_shader**

-  **set_intersection_shader**(value: [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader))
- [RDPipelineShader](class_rdpipelineshader.md#class-rdpipelineshader) **get_intersection_shader**()

Intersection shader for this hit group. Required for non-triangle geometry. Must be `null` when using for triangle geometry.
