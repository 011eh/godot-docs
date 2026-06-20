# RDFramebufferPass

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Framebuffer pass attachment description (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

This class contains the list of attachment descriptions for a framebuffer pass. Each points with an index to a previously supplied list of texture attachments.

Multipass framebuffers can optimize some configurations in mobile. On desktop, they provide little to no advantage.

This object is used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

## Properties

| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | color_attachments       | `PackedInt32Array()`   |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------|
| [int](class_int.md#class-int)                                          | depth_attachment         | `-1`                   |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | input_attachments       | `PackedInt32Array()`   |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | preserve_attachments | `PackedInt32Array()`   |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | resolve_attachments   | `PackedInt32Array()`   |

---

## Constants

**ATTACHMENT_UNUSED** = `-1`

Attachment is unused.

---

## Property Descriptions

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **color_attachments** = `PackedInt32Array()`

-  **set_color_attachments**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_color_attachments**()

Color attachments in order starting from 0. If this attachment is not used by the shader, pass ATTACHMENT_UNUSED to skip.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[int](class_int.md#class-int) **depth_attachment** = `-1`

-  **set_depth_attachment**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_depth_attachment**()

Depth attachment. ATTACHMENT_UNUSED should be used if no depth buffer is required for this pass.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **input_attachments** = `PackedInt32Array()`

-  **set_input_attachments**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_input_attachments**()

Used for multipass framebuffers (more than one render pass). Converts an attachment to an input. Make sure to also supply it properly in the [RDUniform](class_rduniform.md#class-rduniform) for the uniform set.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **preserve_attachments** = `PackedInt32Array()`

-  **set_preserve_attachments**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_preserve_attachments**()

Attachments to preserve in this pass (otherwise they are erased).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **resolve_attachments** = `PackedInt32Array()`

-  **set_resolve_attachments**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_resolve_attachments**()

If the color attachments are multisampled, non-multisampled resolve attachments can be provided.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.
