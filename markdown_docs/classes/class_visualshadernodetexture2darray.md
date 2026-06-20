# VisualShaderNodeTexture2DArray

**Inherits:** [VisualShaderNodeSample3D](class_visualshadernodesample3d.md#class-visualshadernodesample3d) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D texture uniform array to be used within the visual shader graph.

## Description

Translated to `uniform sampler2DArray` in the shader language.

## Properties

| [TextureLayered](class_texturelayered.md#class-texturelayered)   | texture_array   |
|------------------------------------------------------------------|---------------------------------------------------------------------------------|

---

## Property Descriptions

[TextureLayered](class_texturelayered.md#class-texturelayered) **texture_array**

-  **set_texture_array**(value: [TextureLayered](class_texturelayered.md#class-texturelayered))
- [TextureLayered](class_texturelayered.md#class-texturelayered) **get_texture_array**()

A source texture array. Used if [VisualShaderNodeSample3D.source](class_visualshadernodesample3d.md#class-visualshadernodesample3d-property-source) is set to [VisualShaderNodeSample3D.SOURCE_TEXTURE](class_visualshadernodesample3d.md#class-visualshadernodesample3d-constant-source-texture).
