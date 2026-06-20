# UniformSetCacheRD

**Inherits:** [Object](class_object.md#class-object)

Uniform set cache manager for Rendering Device based renderers.

## Description

Uniform set cache manager for [RenderingDevice](class_renderingdevice.md#class-renderingdevice)-based renderers. Provides a way to create a uniform set and reuse it in subsequent calls for as long as the uniform set exists. Uniform set will automatically be cleaned up when dependent objects are freed.

## Methods

| [RID](class_rid.md#class-rid)   | get_cache(shader: [RID](class_rid.md#class-rid), set: [int](class_int.md#class-int), uniforms: [Array](class_array.md#class-array)[[RDUniform](class_rduniform.md#class-rduniform)])    |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

## Method Descriptions

[RID](class_rid.md#class-rid) **get_cache**(shader: [RID](class_rid.md#class-rid), set: [int](class_int.md#class-int), uniforms: [Array](class_array.md#class-array)[[RDUniform](class_rduniform.md#class-rduniform)])

Creates/returns a cached uniform set based on the provided uniforms for a given shader.
