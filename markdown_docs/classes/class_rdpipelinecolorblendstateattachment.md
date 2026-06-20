# RDPipelineColorBlendStateAttachment

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Pipeline color blend state attachment (used by [RenderingDevice](class_renderingdevice.md#class-renderingdevice)).

## Description

Controls how blending between source and destination fragments is performed when using [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

For reference, this is how common user-facing blend modes are implemented in Godot's 2D renderer:

**Mix:**

```gdscript
var attachment = RDPipelineColorBlendStateAttachment.new()
attachment.enable_blend = true
attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
```

**Add:**

```gdscript
var attachment = RDPipelineColorBlendStateAttachment.new()
attachment.enable_blend = true
attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
```

**Subtract:**

```gdscript
var attachment = RDPipelineColorBlendStateAttachment.new()
attachment.enable_blend = true
attachment.alpha_blend_op = RenderingDevice.BLEND_OP_REVERSE_SUBTRACT
attachment.color_blend_op = RenderingDevice.BLEND_OP_REVERSE_SUBTRACT
attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
```

**Multiply:**

```gdscript
var attachment = RDPipelineColorBlendStateAttachment.new()
attachment.enable_blend = true
attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_DST_COLOR
attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ZERO
attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_DST_ALPHA
attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ZERO
```

**Pre-multiplied alpha:**

```gdscript
var attachment = RDPipelineColorBlendStateAttachment.new()
attachment.enable_blend = true
attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
```

## Properties

| [BlendOperation](class_renderingdevice.md#enum-renderingdevice-blendoperation)   | alpha_blend_op                 | `0`     |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------|
| [BlendOperation](class_renderingdevice.md#enum-renderingdevice-blendoperation)   | color_blend_op                 | `0`     |
| [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor)         | dst_alpha_blend_factor | `0`     |
| [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor)         | dst_color_blend_factor | `0`     |
| [bool](class_bool.md#class-bool)                                                 | enable_blend                     | `false` |
| [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor)         | src_alpha_blend_factor | `0`     |
| [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor)         | src_color_blend_factor | `0`     |
| [bool](class_bool.md#class-bool)                                                 | write_a                               | `true`  |
| [bool](class_bool.md#class-bool)                                                 | write_b                               | `true`  |
| [bool](class_bool.md#class-bool)                                                 | write_g                               | `true`  |
| [bool](class_bool.md#class-bool)                                                 | write_r                               | `true`  |

## Methods

|    | set_as_mix()   |
|----|--------------------------------------------------------------------------------|

---

## Property Descriptions

[BlendOperation](class_renderingdevice.md#enum-renderingdevice-blendoperation) **alpha_blend_op** = `0`

-  **set_alpha_blend_op**(value: [BlendOperation](class_renderingdevice.md#enum-renderingdevice-blendoperation))
- [BlendOperation](class_renderingdevice.md#enum-renderingdevice-blendoperation) **get_alpha_blend_op**()

The blend mode to use for the alpha channel.

---

[BlendOperation](class_renderingdevice.md#enum-renderingdevice-blendoperation) **color_blend_op** = `0`

-  **set_color_blend_op**(value: [BlendOperation](class_renderingdevice.md#enum-renderingdevice-blendoperation))
- [BlendOperation](class_renderingdevice.md#enum-renderingdevice-blendoperation) **get_color_blend_op**()

The blend mode to use for the red/green/blue color channels.

---

[BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor) **dst_alpha_blend_factor** = `0`

-  **set_dst_alpha_blend_factor**(value: [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor))
- [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor) **get_dst_alpha_blend_factor**()

Controls how the blend factor for the alpha channel is determined based on the destination's fragments.

---

[BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor) **dst_color_blend_factor** = `0`

-  **set_dst_color_blend_factor**(value: [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor))
- [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor) **get_dst_color_blend_factor**()

Controls how the blend factor for the color channels is determined based on the destination's fragments.

---

[bool](class_bool.md#class-bool) **enable_blend** = `false`

-  **set_enable_blend**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_enable_blend**()

If `true`, performs blending between the source and destination according to the factors defined in src_color_blend_factor, dst_color_blend_factor, src_alpha_blend_factor and dst_alpha_blend_factor. The blend modes color_blend_op and alpha_blend_op are also taken into account, with write_r, write_g, write_b and write_a controlling the output.

---

[BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor) **src_alpha_blend_factor** = `0`

-  **set_src_alpha_blend_factor**(value: [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor))
- [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor) **get_src_alpha_blend_factor**()

Controls how the blend factor for the alpha channel is determined based on the source's fragments.

---

[BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor) **src_color_blend_factor** = `0`

-  **set_src_color_blend_factor**(value: [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor))
- [BlendFactor](class_renderingdevice.md#enum-renderingdevice-blendfactor) **get_src_color_blend_factor**()

Controls how the blend factor for the color channels is determined based on the source's fragments.

---

[bool](class_bool.md#class-bool) **write_a** = `true`

-  **set_write_a**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_write_a**()

If `true`, writes the new alpha channel to the final result.

---

[bool](class_bool.md#class-bool) **write_b** = `true`

-  **set_write_b**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_write_b**()

If `true`, writes the new blue color channel to the final result.

---

[bool](class_bool.md#class-bool) **write_g** = `true`

-  **set_write_g**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_write_g**()

If `true`, writes the new green color channel to the final result.

---

[bool](class_bool.md#class-bool) **write_r** = `true`

-  **set_write_r**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_write_r**()

If `true`, writes the new red color channel to the final result.

---

## Method Descriptions

 **set_as_mix**()

Convenience method to perform standard mix blending with straight (non-premultiplied) alpha. This sets enable_blend to `true`, src_color_blend_factor to [RenderingDevice.BLEND_FACTOR_SRC_ALPHA](class_renderingdevice.md#class-renderingdevice-constant-blend-factor-src-alpha), dst_color_blend_factor to [RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA](class_renderingdevice.md#class-renderingdevice-constant-blend-factor-one-minus-src-alpha), src_alpha_blend_factor to [RenderingDevice.BLEND_FACTOR_SRC_ALPHA](class_renderingdevice.md#class-renderingdevice-constant-blend-factor-src-alpha) and dst_alpha_blend_factor to [RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA](class_renderingdevice.md#class-renderingdevice-constant-blend-factor-one-minus-src-alpha).
