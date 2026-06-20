# VisualShaderNodeResizableBase

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeCurveTexture](class_visualshadernodecurvetexture.md#class-visualshadernodecurvetexture), [VisualShaderNodeCurveXYZTexture](class_visualshadernodecurvexyztexture.md#class-visualshadernodecurvexyztexture), [VisualShaderNodeFrame](class_visualshadernodeframe.md#class-visualshadernodeframe), [VisualShaderNodeGroupBase](class_visualshadernodegroupbase.md#class-visualshadernodegroupbase)

Base class for resizable nodes in a visual shader graph.

## Description

Resizable nodes have a handle that allows the user to adjust their size as needed.

## Properties

| [Vector2](class_vector2.md#class-vector2)   | size   | `Vector2(0, 0)`   |
|---------------------------------------------|--------------------------------------------------------------|-------------------|

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **size** = `Vector2(0, 0)`

-  **set_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_size**()

The size of the node in the visual shader graph.
