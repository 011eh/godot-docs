# GraphElement

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [GraphFrame](class_graphframe.md#class-graphframe), [GraphNode](class_graphnode.md#class-graphnode)

A container that represents a basic element that can be placed inside a [GraphEdit](class_graphedit.md#class-graphedit) control.

## Description

**GraphElement** allows to create custom elements for a [GraphEdit](class_graphedit.md#class-graphedit) graph. By default such elements can be selected, resized, and repositioned, but they cannot be connected. For a graph element that allows for connections see [GraphNode](class_graphnode.md#class-graphnode).

## Properties

| [bool](class_bool.md#class-bool)          | draggable             | `true`          |
|-------------------------------------------|-----------------------------------------------------------------|-----------------|
| [Vector2](class_vector2.md#class-vector2) | position_offset | `Vector2(0, 0)` |
| [bool](class_bool.md#class-bool)          | resizable             | `false`         |
| [bool](class_bool.md#class-bool)          | scaling_menus     | `false`         |
| [bool](class_bool.md#class-bool)          | selectable           | `true`          |
| [bool](class_bool.md#class-bool)          | selected               | `false`         |

## Theme Properties

| [Texture2D](class_texture2d.md#class-texture2d)   | resizer   |
|---------------------------------------------------|-----------------------------------------------------|

---

## Signals

**delete_request**()

Emitted when removing the GraphElement is requested.

---

**dragged**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2))

Emitted when the GraphElement is dragged.

---

**node_deselected**()

Emitted when the GraphElement is deselected.

---

**node_selected**()

Emitted when the GraphElement is selected.

---

**position_offset_changed**()

Emitted when the GraphElement is moved.

---

**raise_request**()

Emitted when displaying the GraphElement over other ones is requested. Happens on focusing (clicking into) the GraphElement.

---

**resize_end**(new_size: [Vector2](class_vector2.md#class-vector2))

Emitted when releasing the mouse button after dragging the resizer handle (see resizable).

---

**resize_request**(new_size: [Vector2](class_vector2.md#class-vector2))

Emitted when resizing the GraphElement is requested. Happens on dragging the resizer handle (see resizable).

---

## Property Descriptions

[bool](class_bool.md#class-bool) **draggable** = `true`

-  **set_draggable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draggable**()

If `true`, the user can drag the GraphElement.

---

[Vector2](class_vector2.md#class-vector2) **position_offset** = `Vector2(0, 0)`

-  **set_position_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position_offset**()

The offset of the GraphElement, relative to the scroll offset of the [GraphEdit](class_graphedit.md#class-graphedit).

---

[bool](class_bool.md#class-bool) **resizable** = `false`

-  **set_resizable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_resizable**()

If `true`, the user can resize the GraphElement.

**Note:** Dragging the handle will only emit the resize_request and resize_end signals, the GraphElement needs to be resized manually.

---

[bool](class_bool.md#class-bool) **scaling_menus** = `false`

-  **set_scaling_menus**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scaling_menus**()

If `true`, [PopupMenu](class_popupmenu.md#class-popupmenu)s that are descendants of the GraphElement are scaled with the [GraphEdit](class_graphedit.md#class-graphedit) zoom.

---

[bool](class_bool.md#class-bool) **selectable** = `true`

-  **set_selectable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_selectable**()

If `true`, the user can select the GraphElement.

---

[bool](class_bool.md#class-bool) **selected** = `false`

-  **set_selected**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_selected**()

If `true`, the GraphElement is selected.

---

## Theme Property Descriptions

[Texture2D](class_texture2d.md#class-texture2d) **resizer**

The icon used for the resizer, visible when resizable is enabled.
