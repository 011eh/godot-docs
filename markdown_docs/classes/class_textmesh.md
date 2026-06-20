# TextMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) **<** [Mesh](class_mesh.md#class-mesh) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Generate a [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) from the text.

## Description

Generate a [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh) from the text.

TextMesh can be generated only when using dynamic fonts with vector glyph contours. Bitmap fonts (including bitmap data in the TrueType/OpenType containers, like color emoji fonts) are not supported.

The UV layout is arranged in 4 horizontal strips, top to bottom: 40% of the height for the front face, 40% for the back face, 10% for the outer edges and 10% for the inner edges.

## Tutorials

- [3D text](../tutorials/3d/3d_text.md)

## Properties

| [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode)                  | autowrap_mode                                                 | `0`             |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------|
| [float](class_float.md#class-float)                                               | curve_step                                                       | `0.5`           |
| [float](class_float.md#class-float)                                               | depth                                                                 | `0.05`          |
| [Font](class_font.md#class-font)                                                  | font                                                                   |                 |
| [int](class_int.md#class-int)                                                     | font_size                                                         | `16`            |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | horizontal_alignment                                   | `1`             |
| [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)]      | justification_flags                                     | `163`           |
| [String](class_string.md#class-string)                                            | language                                                           | `""`            |
| [float](class_float.md#class-float)                                               | line_spacing                                                   | `0.0`           |
| [Vector2](class_vector2.md#class-vector2)                                         | offset                                                               | `Vector2(0, 0)` |
| [float](class_float.md#class-float)                                               | pixel_size                                                       | `0.01`          |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser)  | structured_text_bidi_override                 | `0`             |
| [Array](class_array.md#class-array)                                               | structured_text_bidi_override_options | `[]`            |
| [String](class_string.md#class-string)                                            | text                                                                   | `""`            |
| [Direction](class_textserver.md#enum-textserver-direction)                        | text_direction                                               | `0`             |
| [bool](class_bool.md#class-bool)                                                  | uppercase                                                         | `false`         |
| [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment)     | vertical_alignment                                       | `1`             |
| [float](class_float.md#class-float)                                               | width                                                                 | `500.0`         |

---

## Property Descriptions

[AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **autowrap_mode** = `0`

-  **set_autowrap_mode**(value: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode))
- [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **get_autowrap_mode**()

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off), the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

---

[float](class_float.md#class-float) **curve_step** = `0.5`

-  **set_curve_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_curve_step**()

Step (in pixels) used to approximate Bézier curves. Lower values result in smoother curves, but is slower to generate and render. Consider adjusting this according to the font size and the typical viewing distance.

**Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts.

---

[float](class_float.md#class-float) **depth** = `0.05`

-  **set_depth**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_depth**()

Depths of the mesh, if set to `0.0` only front surface, is generated, and UV layout is changed to use full texture for the front face only.

---

[Font](class_font.md#class-font) **font**

-  **set_font**(value: [Font](class_font.md#class-font))
- [Font](class_font.md#class-font) **get_font**()

Font configuration used to display text.

---

[int](class_int.md#class-int) **font_size** = `16`

-  **set_font_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_font_size**()

Font size of the **TextMesh**'s text. This property works in tandem with pixel_size. Higher values will result in a more detailed font, regardless of curve_step and pixel_size. Consider keeping this value below 63 (inclusive) for good performance, and adjust pixel_size as needed to enlarge text.

**Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts. To change the text's size in real-time efficiently, change the node's [Node3D.scale](class_node3d.md#class-node3d-property-scale) instead.

---

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **horizontal_alignment** = `1`

-  **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---

[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **justification_flags** = `163`

-  **set_justification_flags**(value: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_justification_flags**()

Line fill alignment rules.

---

[String](class_string.md#class-string) **language** = `""`

-  **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

[float](class_float.md#class-float) **line_spacing** = `0.0`

-  **set_line_spacing**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)`

-  **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The text drawing offset (in pixels).

**Note:** Changing this property will regenerate the mesh, which is a slow operation. To change the text's position in real-time efficiently, change the node's [Node3D.position](class_node3d.md#class-node3d-property-position) instead.

---

[float](class_float.md#class-float) **pixel_size** = `0.01`

-  **set_pixel_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pixel_size**()

The size of one pixel's width on the text to scale it in 3D. This property works in tandem with font_size.

**Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts. To change the text's size in real-time efficiently, change the node's [Node3D.scale](class_node3d.md#class-node3d-property-scale) instead.

---

[StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **structured_text_bidi_override** = `0`

-  **set_structured_text_bidi_override**(value: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser))
- [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

---

[Array](class_array.md#class-array) **structured_text_bidi_override_options** = `[]`

-  **set_structured_text_bidi_override_options**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

---

[String](class_string.md#class-string) **text** = `""`

-  **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

The text to generate mesh from.

**Note:** Due to being a [Resource](class_resource.md#class-resource), it doesn't follow the rules of [Node.auto_translate_mode](class_node.md#class-node-property-auto-translate-mode). If disabling translation is desired, it should be done manually with [Object.set_message_translation()](class_object.md#class-object-method-set-message-translation).

---

[Direction](class_textserver.md#enum-textserver-direction) **text_direction** = `0`

-  **set_text_direction**(value: [Direction](class_textserver.md#enum-textserver-direction))
- [Direction](class_textserver.md#enum-textserver-direction) **get_text_direction**()

Base text writing direction.

---

[bool](class_bool.md#class-bool) **uppercase** = `false`

-  **set_uppercase**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_uppercase**()

If `true`, all the text displays as UPPERCASE.

---

[VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **vertical_alignment** = `1`

-  **set_vertical_alignment**(value: [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment))
- [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **get_vertical_alignment**()

Controls the text's vertical alignment. Supports top, center, and bottom.

---

[float](class_float.md#class-float) **width** = `500.0`

-  **set_width**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_width**()

Text width (in pixels), used for fill alignment.
