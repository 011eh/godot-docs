# VisualShaderNodeScreenUVToSDF

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A function to convert screen UV to an SDF (signed-distance field), to be used within the visual shader graph.

## Description

Translates to `screen_uv_to_sdf(uv)` in the shader language. If the UV port isn't connected, `SCREEN_UV` is used instead.
