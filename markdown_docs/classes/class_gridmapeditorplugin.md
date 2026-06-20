# GridMapEditorPlugin

**Inherits:** [EditorPlugin](class_editorplugin.md#class-editorplugin) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Editor for [GridMap](class_gridmap.md#class-gridmap) nodes.

## Description

GridMapEditorPlugin provides access to the [GridMap](class_gridmap.md#class-gridmap) editor functionality.

## Methods

|                                           | clear_selection()                                                                                                   |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GridMap](class_gridmap.md#class-gridmap) | get_current_grid_map()                                                                                         |
| [Array](class_array.md#class-array)       | get_selected_cells()                                                                                             |
| [int](class_int.md#class-int)             | get_selected_palette_item()                                                                               |
| [AABB](class_aabb.md#class-aabb)          | get_selection()                                                                                                       |
| [bool](class_bool.md#class-bool)          | has_selection()                                                                                                       |
|                                           | set_selected_palette_item(item: [int](class_int.md#class-int))                                            |
|                                           | set_selection(begin: [Vector3i](class_vector3i.md#class-vector3i), end: [Vector3i](class_vector3i.md#class-vector3i)) |

---

## Method Descriptions

 **clear_selection**()

Deselects any currently selected cells.

---

[GridMap](class_gridmap.md#class-gridmap) **get_current_grid_map**()

Returns the [GridMap](class_gridmap.md#class-gridmap) node currently edited by the grid map editor.

---

[Array](class_array.md#class-array) **get_selected_cells**()

Returns an array of [Vector3i](class_vector3i.md#class-vector3i)s with the selected cells' coordinates.

---

[int](class_int.md#class-int) **get_selected_palette_item**()

Returns the index of the selected [MeshLibrary](class_meshlibrary.md#class-meshlibrary) item in the grid map editor's palette or `-1` if no item is selected.

**Note:** The indices might not be in the same order as they appear in the editor's interface.

---

[AABB](class_aabb.md#class-aabb) **get_selection**()

Returns the cell coordinate bounds of the current selection. Use has_selection() to check if there is an active selection.

---

[bool](class_bool.md#class-bool) **has_selection**()

Returns `true` if there are selected cells.

---

 **set_selected_palette_item**(item: [int](class_int.md#class-int))

Selects the [MeshLibrary](class_meshlibrary.md#class-meshlibrary) item with the given index in the grid map editor's palette. If a negative index is given, no item will be selected. If a value greater than the last index is given, the last item will be selected.

**Note:** The indices might not be in the same order as they appear in the editor's interface.

---

 **set_selection**(begin: [Vector3i](class_vector3i.md#class-vector3i), end: [Vector3i](class_vector3i.md#class-vector3i))

Selects the cells inside the given bounds from `begin` to `end`.
