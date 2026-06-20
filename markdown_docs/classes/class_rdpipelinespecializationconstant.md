# RDPipelineSpecializationConstant

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline specialization constant (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

A *specialization constant* is a way to create additional variants of shaders without actually increasing the number of shader versions that are compiled. This allows improving performance by reducing the number of shader versions and reducing `if` branching, while still allowing shaders to be flexible for different use cases.

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [int](class_int.md#class-int)             | constant_id   | `0`   |
|-------------------------------------------|-------------------------------------------------------------------------------|-------|
| [Variant](class_variant.md#class-variant) | value               |       |

---

## Property Descriptions

[int](class_int.md#class-int) **constant_id** = `0`

-  **set_constant_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_constant_id**()

The identifier of the specialization constant. This is a value starting from `0` and that increments for every different specialization constant for a given shader.

---

[Variant](class_variant.md#class-variant) **value**

-  **set_value**(value: [Variant](class_variant.md#class-variant))
- [Variant](class_variant.md#class-variant) **get_value**()

The specialization constant's value. Only [bool](class_bool.md#class-bool), [int](class_int.md#class-int) and [float](class_float.md#class-float) types are valid for specialization constants.
