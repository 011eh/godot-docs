# VisualShaderNodeSample3D

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeTexture2DArray](class_visualshadernodetexture2darray.md#class-visualshadernodetexture2darray), [VisualShaderNodeTexture3D](class_visualshadernodetexture3d.md#class-visualshadernodetexture3d)

A base node for nodes which samples 3D textures in the visual shader graph.

## Description

A virtual class, use the descendants instead.

## Properties

| Source   | source   | `0`   |
|---------------------------------------------------|-------------------------------------------------------------|-------|

---

## Enumerations

enum **Source**:

Source **SOURCE_TEXTURE** = `0`

Creates internal uniform and provides a way to assign it within node.

Source **SOURCE_PORT** = `1`

Use the uniform texture from sampler port.

Source **SOURCE_MAX** = `2`

Represents the size of the Source enum.

---

## Property Descriptions

Source **source** = `0`

-  **set_source**(value: Source)
- Source **get_source**()

An input source type.
