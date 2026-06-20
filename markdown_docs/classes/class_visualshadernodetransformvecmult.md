# VisualShaderNodeTransformVecMult

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Multiplies a [Transform3D](class_transform3d.md#class-transform3d) and a [Vector3](class_vector3.md#class-vector3) within the visual shader graph.

## Description

A multiplication operation on a transform (4×4 matrix) and a vector, with support for different multiplication operators.

## Properties

| Operator   | operator   | `0`   |
|---------------------------------------------------------------|-------------------------------------------------------------------------|-------|

---

## Enumerations

enum **Operator**:

Operator **OP_AxB** = `0`

Multiplies transform `a` by the vector `b`.

Operator **OP_BxA** = `1`

Multiplies vector `b` by the transform `a`.

Operator **OP_3x3_AxB** = `2`

Multiplies transform `a` by the vector `b`, skipping the last row and column of the transform.

Operator **OP_3x3_BxA** = `3`

Multiplies vector `b` by the transform `a`, skipping the last row and column of the transform.

Operator **OP_MAX** = `4`

Represents the size of the Operator enum.

---

## Property Descriptions

Operator **operator** = `0`

-  **set_operator**(value: Operator)
- Operator **get_operator**()

The multiplication type to be performed.
