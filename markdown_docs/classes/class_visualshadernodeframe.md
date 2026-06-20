# VisualShaderNodeFrame

**Inherits:** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class-visualshadernoderesizablebase) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeComment](class_visualshadernodecomment.md#class-visualshadernodecomment)

A frame other visual shader nodes can be attached to for better organization.

## Description

A rectangular frame that can be used to group visual shader nodes together to improve organization.

Nodes attached to the frame will move with it when it is dragged and it can automatically resize to enclose all attached nodes.

Its title, description and color can be customized.

## Properties

| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | attached_nodes         | `PackedInt32Array()`         |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------|
| [bool](class_bool.md#class-bool)                                       | autoshrink                 | `true`                       |
| [Color](class_color.md#class-color)                                    | tint_color                 | `Color(0.3, 0.3, 0.3, 0.75)` |
| [bool](class_bool.md#class-bool)                                       | tint_color_enabled | `false`                      |
| [String](class_string.md#class-string)                                 | title                           | `"Title"`                    |

## Methods

|    | add_attached_node(node: [int](class_int.md#class-int))       |
|----|-----------------------------------------------------------------------------------------------------------------------|
|    | remove_attached_node(node: [int](class_int.md#class-int)) |

---

## Property Descriptions

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **attached_nodes** = `PackedInt32Array()`

-  **set_attached_nodes**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_attached_nodes**()

The list of nodes attached to the frame.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

[bool](class_bool.md#class-bool) **autoshrink** = `true`

-  **set_autoshrink_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_autoshrink_enabled**()

If `true`, the frame will automatically resize to enclose all attached nodes.

---

[Color](class_color.md#class-color) **tint_color** = `Color(0.3, 0.3, 0.3, 0.75)`

-  **set_tint_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_tint_color**()

The color of the frame when tint_color_enabled is `true`.

---

[bool](class_bool.md#class-bool) **tint_color_enabled** = `false`

-  **set_tint_color_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_tint_color_enabled**()

If `true`, the frame will be tinted with the color specified in tint_color.

---

[String](class_string.md#class-string) **title** = `"Title"`

-  **set_title**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_title**()

The title of the node.

---

## Method Descriptions

 **add_attached_node**(node: [int](class_int.md#class-int))

Adds a node to the list of nodes attached to the frame. Should not be called directly, use the [VisualShader.attach_node_to_frame()](class_visualshader.md#class-visualshader-method-attach-node-to-frame) method instead.

---

 **remove_attached_node**(node: [int](class_int.md#class-int))

Removes a node from the list of nodes attached to the frame. Should not be called directly, use the [VisualShader.detach_node_from_frame()](class_visualshader.md#class-visualshader-method-detach-node-from-frame) method instead.
