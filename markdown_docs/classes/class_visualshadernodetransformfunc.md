# VisualShaderNodeTransformFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Computes a [Transform3D](class_transform3d.md#class-transform3d) function within the visual shader graph.

## Description

Computes an inverse or transpose function on the provided [Transform3D](class_transform3d.md#class-transform3d).

## Properties

| Function   | function   | `0`   |
|------------------------------------------------------------|----------------------------------------------------------------------|-------|

---

## Enumerations

enum **Function**:

Function **FUNC_INVERSE** = `0`

Perform the inverse operation on the [Transform3D](class_transform3d.md#class-transform3d) matrix.

Function **FUNC_TRANSPOSE** = `1`

Perform the transpose operation on the [Transform3D](class_transform3d.md#class-transform3d) matrix.

Function **FUNC_MAX** = `2`

Represents the size of the Function enum.

---

## Property Descriptions

Function **function** = `0`

-  **set_function**(value: Function)
- Function **get_function**()

The function to be computed.
