# RDPipelineDepthStencilState

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline depth/stencil state (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

**RDPipelineDepthStencilState** controls the way depth and stencil comparisons are performed when sampling those values using [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator)   | back_op_compare               | `7`     |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------|
| [int](class_int.md#class-int)                                                      | back_op_compare_mask     | `0`     |
| [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) | back_op_depth_fail         | `1`     |
| [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) | back_op_fail                     | `1`     |
| [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) | back_op_pass                     | `1`     |
| [int](class_int.md#class-int)                                                      | back_op_reference           | `0`     |
| [int](class_int.md#class-int)                                                      | back_op_write_mask         | `0`     |
| [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator)   | depth_compare_operator | `7`     |
| [float](class_float.md#class-float)                                                | depth_range_max               | `0.0`   |
| [float](class_float.md#class-float)                                                | depth_range_min               | `0.0`   |
| [bool](class_bool.md#class-bool)                                                   | enable_depth_range         | `false` |
| [bool](class_bool.md#class-bool)                                                   | enable_depth_test           | `false` |
| [bool](class_bool.md#class-bool)                                                   | enable_depth_write         | `false` |
| [bool](class_bool.md#class-bool)                                                   | enable_stencil                 | `false` |
| [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator)   | front_op_compare             | `7`     |
| [int](class_int.md#class-int)                                                      | front_op_compare_mask   | `0`     |
| [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) | front_op_depth_fail       | `1`     |
| [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) | front_op_fail                   | `1`     |
| [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) | front_op_pass                   | `1`     |
| [int](class_int.md#class-int)                                                      | front_op_reference         | `0`     |
| [int](class_int.md#class-int)                                                      | front_op_write_mask       | `0`     |

---

## Property Descriptions

[CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator) **back_op_compare** = `7`

-  **set_back_op_compare**(value: [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator))
- [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator) **get_back_op_compare**()

The method used for comparing the previous back stencil value and back_op_reference.

---

[int](class_int.md#class-int) **back_op_compare_mask** = `0`

-  **set_back_op_compare_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_back_op_compare_mask**()

Selects which bits from the back stencil value will be compared.

---

[StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **back_op_depth_fail** = `1`

-  **set_back_op_depth_fail**(value: [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation))
- [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **get_back_op_depth_fail**()

The operation to perform on the stencil buffer for back pixels that pass the stencil test but fail the depth test.

---

[StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **back_op_fail** = `1`

-  **set_back_op_fail**(value: [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation))
- [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **get_back_op_fail**()

The operation to perform on the stencil buffer for back pixels that fail the stencil test.

---

[StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **back_op_pass** = `1`

-  **set_back_op_pass**(value: [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation))
- [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **get_back_op_pass**()

The operation to perform on the stencil buffer for back pixels that pass the stencil test.

---

[int](class_int.md#class-int) **back_op_reference** = `0`

-  **set_back_op_reference**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_back_op_reference**()

The value the previous back stencil value will be compared to.

---

[int](class_int.md#class-int) **back_op_write_mask** = `0`

-  **set_back_op_write_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_back_op_write_mask**()

Selects which bits from the back stencil value will be changed.

---

[CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator) **depth_compare_operator** = `7`

-  **set_depth_compare_operator**(value: [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator))
- [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator) **get_depth_compare_operator**()

The method used for comparing the previous and current depth values.

---

[float](class_float.md#class-float) **depth_range_max** = `0.0`

-  **set_depth_range_max**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_range_max**()

The maximum depth that returns `true` for enable_depth_range.

---

[float](class_float.md#class-float) **depth_range_min** = `0.0`

-  **set_depth_range_min**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth_range_min**()

The minimum depth that returns `true` for enable_depth_range.

---

[bool](class_bool.md#class-bool) **enable_depth_range** = `false`

-  **set_enable_depth_range**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_depth_range**()

If `true`, each depth value will be tested to see if it is between depth_range_min and depth_range_max. If it is outside of these values, it is discarded.

---

[bool](class_bool.md#class-bool) **enable_depth_test** = `false`

-  **set_enable_depth_test**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_depth_test**()

If `true`, enables depth testing which allows objects to be automatically occluded by other objects based on their depth. This also allows objects to be partially occluded by other objects. If `false`, objects will appear in the order they were drawn (like in Godot's 2D renderer).

---

[bool](class_bool.md#class-bool) **enable_depth_write** = `false`

-  **set_enable_depth_write**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_depth_write**()

If `true`, writes to the depth buffer whenever the depth test returns `true`. Only works when enable_depth_test is also `true`.

---

[bool](class_bool.md#class-bool) **enable_stencil** = `false`

-  **set_enable_stencil**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_stencil**()

If `true`, enables stencil testing. There are separate stencil buffers for front-facing triangles and back-facing triangles. See properties that begin with "front_op" and properties with "back_op" for each.

---

[CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator) **front_op_compare** = `7`

-  **set_front_op_compare**(value: [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator))
- [CompareOperator](class_renderingdevice.md#enum-renderingdevice-compareoperator) **get_front_op_compare**()

The method used for comparing the previous front stencil value and front_op_reference.

---

[int](class_int.md#class-int) **front_op_compare_mask** = `0`

-  **set_front_op_compare_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_front_op_compare_mask**()

Selects which bits from the front stencil value will be compared.

---

[StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **front_op_depth_fail** = `1`

-  **set_front_op_depth_fail**(value: [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation))
- [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **get_front_op_depth_fail**()

The operation to perform on the stencil buffer for front pixels that pass the stencil test but fail the depth test.

---

[StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **front_op_fail** = `1`

-  **set_front_op_fail**(value: [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation))
- [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **get_front_op_fail**()

The operation to perform on the stencil buffer for front pixels that fail the stencil test.

---

[StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **front_op_pass** = `1`

-  **set_front_op_pass**(value: [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation))
- [StencilOperation](class_renderingdevice.md#enum-renderingdevice-stenciloperation) **get_front_op_pass**()

The operation to perform on the stencil buffer for front pixels that pass the stencil test.

---

[int](class_int.md#class-int) **front_op_reference** = `0`

-  **set_front_op_reference**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_front_op_reference**()

The value the previous front stencil value will be compared to.

---

[int](class_int.md#class-int) **front_op_write_mask** = `0`

-  **set_front_op_write_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_front_op_write_mask**()

Selects which bits from the front stencil value will be changed.
