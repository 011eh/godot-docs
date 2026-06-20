# EditorSelection

**Inherits:** [Object](class_object.md#class-object)

Manages the SceneTree selection in the editor.

## Description

This object manages the SceneTree selection in the editor.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_selection()](class_editorinterface.md#class-editorinterface-method-get-selection).

## Methods

|                                                                       | add_node(node: [Node](class_node.md#class-node))           |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
|                                                                       | clear()                                                       |
| [Array](class_array.md#class-array)[[Node](class_node.md#class-node)] | get_selected_nodes()                             |
| [Array](class_array.md#class-array)[[Node](class_node.md#class-node)] | get_top_selected_nodes()                     |
| [Array](class_array.md#class-array)[[Node](class_node.md#class-node)] | get_transformable_selected_nodes() |
|                                                                       | remove_node(node: [Node](class_node.md#class-node))     |

---

## Signals

**selection_changed**()

Emitted when the selection changes.

---

## Method Descriptions

 **add_node**(node: [Node](class_node.md#class-node))

Adds a node to the selection.

**Note:** The newly selected node will not be automatically edited in the inspector. If you want to edit a node, use [EditorInterface.edit_node()](class_editorinterface.md#class-editorinterface-method-edit-node).

---

 **clear**()

Clear the selection.

---

[Array](class_array.md#class-array)[[Node](class_node.md#class-node)] **get_selected_nodes**()

Returns the list of selected nodes.

---

[Array](class_array.md#class-array)[[Node](class_node.md#class-node)] **get_top_selected_nodes**()

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.).

For example, if there is a node A with a child B and a sibling C, then selecting all three will cause this method to return only A and C. Changing the global transform of A will affect the global transform of B, so there is no need to change B separately.

---

[Array](class_array.md#class-array)[[Node](class_node.md#class-node)] **get_transformable_selected_nodes**()

**Deprecated:** Use get_top_selected_nodes() instead.

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.). See get_top_selected_nodes().

---

 **remove_node**(node: [Node](class_node.md#class-node))

Removes a node from the selection.
