# RDPipelineColorBlendState

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline color blend state (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [Array](class_array.md#class-array)[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class-rdpipelinecolorblendstateattachment)]   | attachments         | `[]`                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|---------------------|
| [Color](class_color.md#class-color)                                                                                                                                  | blend_constant   | `Color(0, 0, 0, 1)` |
| [bool](class_bool.md#class-bool)                                                                                                                                     | enable_logic_op | `false`             |
| [LogicOperation](class_renderingdevice.md#enum-renderingdevice-logicoperation)                                                                                       | logic_op               | `0`                 |

---

## Property Descriptions

[Array](class_array.md#class-array)[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class-rdpipelinecolorblendstateattachment)] **attachments** = `[]`

-  **set_attachments**(value: [Array](class_array.md#class-array)[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class-rdpipelinecolorblendstateattachment)])
- [Array](class_array.md#class-array)[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class-rdpipelinecolorblendstateattachment)] **get_attachments**()

The attachments that are blended together.

---

[Color](class_color.md#class-color) **blend_constant** = `Color(0, 0, 0, 1)`

-  **set_blend_constant**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_blend_constant**()

The constant color to blend with. See also [RenderingDevice.draw_list_set_blend_constants()](class_renderingdevice.md#class-renderingdevice-method-draw-list-set-blend-constants).

---

[bool](class_bool.md#class-bool) **enable_logic_op** = `false`

-  **set_enable_logic_op**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_logic_op**()

If `true`, performs the logic operation defined in logic_op.

---

[LogicOperation](class_renderingdevice.md#enum-renderingdevice-logicoperation) **logic_op** = `0`

-  **set_logic_op**(value: [LogicOperation](class_renderingdevice.md#enum-renderingdevice-logicoperation))
- [LogicOperation](class_renderingdevice.md#enum-renderingdevice-logicoperation) **get_logic_op**()

The logic operation to perform for blending. Only effective if enable_logic_op is `true`.
