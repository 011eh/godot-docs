# VisualShaderNodeParticleOutput

**Inherits:** [VisualShaderNodeOutput](class_visualshadernodeoutput.md#class-visualshadernodeoutput) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Visual shader node that defines output values for particle emitting.

## Description

This node defines how particles are emitted. It allows to customize e.g. position and velocity. Available ports are different depending on which function this node is inside (start, process, collision) and whether custom data is enabled.
