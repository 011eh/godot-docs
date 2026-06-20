# GraphEdit

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

An editor for graph-like structures, using [GraphNode](class_graphnode.md#class-graphnode)s.

## Description

**GraphEdit** provides tools for creation, manipulation, and display of various graphs. Its main purpose in the engine is to power the visual programming systems, such as visual shaders, but it is also available for use in user projects.

**GraphEdit** by itself is only an empty container, representing an infinite grid where [GraphNode](class_graphnode.md#class-graphnode)s can be placed. Each [GraphNode](class_graphnode.md#class-graphnode) represents a node in the graph, a single unit of data in the connected scheme. **GraphEdit**, in turn, helps to control various interactions with nodes and between nodes. When the user attempts to connect, disconnect, or delete a [GraphNode](class_graphnode.md#class-graphnode), a signal is emitted in the **GraphEdit**, but no action is taken by default. It is the responsibility of the programmer utilizing this control to implement the necessary logic to determine how each request should be handled.

**Performance:** It is greatly advised to enable low-processor usage mode (see [OS.low_processor_usage_mode](class_os.md#class-os-property-low-processor-usage-mode)) when using GraphEdits.

**Note:** Keep in mind that [Node.get_children()](class_node.md#class-node-method-get-children) will also return the connection layer node named `_connection_layer` due to technical limitations. This behavior may change in future releases.

## Properties

| [bool](class_bool.md#class-bool)                                                        | clip_contents                                                                          | `true` (overrides [Control](class_control.md#class-control-property-clip-contents))   |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                        | connection_lines_antialiased | `true`                                                                                |
| [float](class_float.md#class-float)                                                     | connection_lines_curvature     | `0.5`                                                                                 |
| [float](class_float.md#class-float)                                                     | connection_lines_thickness     | `4.0`                                                                                 |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | connections                                   | `[]`                                                                                  |
| [FocusMode](class_control.md#enum-control-focusmode)                                    | focus_mode                                                                             | `2` (overrides [Control](class_control.md#class-control-property-focus-mode))         |
| GridPattern                                              | grid_pattern                                 | `0`                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | minimap_enabled                           | `true`                                                                                |
| [float](class_float.md#class-float)                                                     | minimap_opacity                           | `0.65`                                                                                |
| [Vector2](class_vector2.md#class-vector2)                                               | minimap_size                                 | `Vector2(240, 160)`                                                                   |
| PanningScheme                                          | panning_scheme                             | `0`                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | right_disconnects                       | `false`                                                                               |
| [Vector2](class_vector2.md#class-vector2)                                               | scroll_offset                               | `Vector2(0, 0)`                                                                       |
| [bool](class_bool.md#class-bool)                                                        | show_arrange_button                   | `true`                                                                                |
| [bool](class_bool.md#class-bool)                                                        | show_grid                                       | `true`                                                                                |
| [bool](class_bool.md#class-bool)                                                        | show_grid_buttons                       | `true`                                                                                |
| [bool](class_bool.md#class-bool)                                                        | show_menu                                       | `true`                                                                                |
| [bool](class_bool.md#class-bool)                                                        | show_minimap_button                   | `true`                                                                                |
| [bool](class_bool.md#class-bool)                                                        | show_zoom_buttons                       | `true`                                                                                |
| [bool](class_bool.md#class-bool)                                                        | show_zoom_label                           | `false`                                                                               |
| [int](class_int.md#class-int)                                                           | snapping_distance                       | `20`                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | snapping_enabled                         | `true`                                                                                |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | type_names                                     | `{}`                                                                                  |
| [float](class_float.md#class-float)                                                     | zoom                                                 | `1.0`                                                                                 |
| [float](class_float.md#class-float)                                                     | zoom_max                                         | `2.0736003`                                                                           |
| [float](class_float.md#class-float)                                                     | zoom_min                                         | `0.23256795`                                                                          |
| [float](class_float.md#class-float)                                                     | zoom_step                                       | `1.2`                                                                                 |

## Methods

| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)              | \_get_connection_line(from_position: [Vector2](class_vector2.md#class-vector2), to_position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                        |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                        | \_is_in_input_hotzone(in_node: [Object](class_object.md#class-object), in_port: [int](class_int.md#class-int), mouse_position: [Vector2](class_vector2.md#class-vector2))                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | \_is_in_output_hotzone(in_node: [Object](class_object.md#class-object), in_port: [int](class_int.md#class-int), mouse_position: [Vector2](class_vector2.md#class-vector2))                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | \_is_node_hover_valid(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int))                                            |
|                                                                                         | add_valid_connection_type(from_type: [int](class_int.md#class-int), to_type: [int](class_int.md#class-int))                                                                                                                                                                      |
|                                                                                         | add_valid_left_disconnect_type(type: [int](class_int.md#class-int))                                                                                                                                                                                                         |
|                                                                                         | add_valid_right_disconnect_type(type: [int](class_int.md#class-int))                                                                                                                                                                                                       |
|                                                                                         | arrange_nodes()                                                                                                                                                                                                                                                                              |
|                                                                                         | attach_graph_element_to_frame(element: [StringName](class_stringname.md#class-stringname), frame: [StringName](class_stringname.md#class-stringname))                                                                                                                        |
|                                                                                         | clear_connections()                                                                                                                                                                                                                                                                      |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | connect_node(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int), keep_alive: [bool](class_bool.md#class-bool) = false)              |
|                                                                                         | detach_graph_element_from_frame(element: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                               |
|                                                                                         | disconnect_node(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int))                                                              |
|                                                                                         | force_connection_drag_end()                                                                                                                                                                                                                                                      |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_attached_nodes_of_frame(frame: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                         |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | get_closest_connection_at_point(point: [Vector2](class_vector2.md#class-vector2), max_distance: [float](class_float.md#class-float) = 4.0)                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | get_connection_count(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int))                                                                                                                                                         |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)              | get_connection_line(from_node: [Vector2](class_vector2.md#class-vector2), to_node: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                          |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | get_connection_list_from_node(node: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                      |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | get_connections_intersecting_with_rect(rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                   |
| [GraphFrame](class_graphframe.md#class-graphframe)                                      | get_element_frame(element: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                           |
| [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer)                             | get_menu_hbox()                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | is_node_connected(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int))                                                          |
| [bool](class_bool.md#class-bool)                                                        | is_valid_connection_type(from_type: [int](class_int.md#class-int), to_type: [int](class_int.md#class-int))                                                                                                                                                                        |
|                                                                                         | remove_valid_connection_type(from_type: [int](class_int.md#class-int), to_type: [int](class_int.md#class-int))                                                                                                                                                                |
|                                                                                         | remove_valid_left_disconnect_type(type: [int](class_int.md#class-int))                                                                                                                                                                                                   |
|                                                                                         | remove_valid_right_disconnect_type(type: [int](class_int.md#class-int))                                                                                                                                                                                                 |
|                                                                                         | set_connection_activity(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int), amount: [float](class_float.md#class-float)) |
|                                                                                         | set_selected(node: [Node](class_node.md#class-node))                                                                                                                                                                                                                                          |

## Theme Properties

| [Color](class_color.md#class-color)             | activity                                                     | `Color(1, 1, 1, 1)`         |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------|
| [Color](class_color.md#class-color)             | connection_hover_tint_color               | `Color(0, 0, 0, 0.3)`       |
| [Color](class_color.md#class-color)             | connection_rim_color                             | `Color(0.1, 0.1, 0.1, 0.6)` |
| [Color](class_color.md#class-color)             | connection_valid_target_tint_color | `Color(1, 1, 1, 0.4)`       |
| [Color](class_color.md#class-color)             | grid_major                                                 | `Color(1, 1, 1, 0.2)`       |
| [Color](class_color.md#class-color)             | grid_minor                                                 | `Color(1, 1, 1, 0.05)`      |
| [Color](class_color.md#class-color)             | selection_fill                                         | `Color(1, 1, 1, 0.3)`       |
| [Color](class_color.md#class-color)             | selection_stroke                                     | `Color(1, 1, 1, 0.8)`       |
| [int](class_int.md#class-int)                   | connection_hover_thickness              | `0`                         |
| [int](class_int.md#class-int)                   | port_hotzone_inner_extent                | `22`                        |
| [int](class_int.md#class-int)                   | port_hotzone_outer_extent                | `26`                        |
| [Texture2D](class_texture2d.md#class-texture2d) | grid_toggle                                                |                             |
| [Texture2D](class_texture2d.md#class-texture2d) | layout                                                          |                             |
| [Texture2D](class_texture2d.md#class-texture2d) | minimap_toggle                                          |                             |
| [Texture2D](class_texture2d.md#class-texture2d) | snapping_toggle                                        |                             |
| [Texture2D](class_texture2d.md#class-texture2d) | zoom_in                                                        |                             |
| [Texture2D](class_texture2d.md#class-texture2d) | zoom_out                                                      |                             |
| [Texture2D](class_texture2d.md#class-texture2d) | zoom_reset                                                  |                             |
| [StyleBox](class_stylebox.md#class-stylebox)    | menu_panel                                                 |                             |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel                                                           |                             |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel_focus                                               |                             |

---

## Signals

**begin_node_move**()

Emitted at the beginning of a [GraphElement](class_graphelement.md#class-graphelement)'s movement.

---

**connection_drag_ended**()

Emitted at the end of a connection drag.

---

**connection_drag_started**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), is_output: [bool](class_bool.md#class-bool))

Emitted at the beginning of a connection drag.

---

**connection_from_empty**(to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int), release_position: [Vector2](class_vector2.md#class-vector2))

Emitted when user drags a connection from an input port into the empty space of the graph.

---

**connection_request**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int))

Emitted to the GraphEdit when the connection between the `from_port` of the `from_node` [GraphNode](class_graphnode.md#class-graphnode) and the `to_port` of the `to_node` [GraphNode](class_graphnode.md#class-graphnode) is attempted to be created.

---

**connection_to_empty**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), release_position: [Vector2](class_vector2.md#class-vector2))

Emitted when user drags a connection from an output port into the empty space of the graph.

---

**copy_nodes_request**()

Emitted when this **GraphEdit** captures a `ui_copy` action (`Ctrl + C` by default). In general, this signal indicates that the selected [GraphElement](class_graphelement.md#class-graphelement)s should be copied.

---

**cut_nodes_request**()

Emitted when this **GraphEdit** captures a `ui_cut` action (`Ctrl + X` by default). In general, this signal indicates that the selected [GraphElement](class_graphelement.md#class-graphelement)s should be cut.

---

**delete_nodes_request**(nodes: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)])

Emitted when this **GraphEdit** captures a `ui_graph_delete` action (`Delete` by default).

`nodes` is an array of node names that should be removed. These usually include all selected nodes.

---

**disconnection_request**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int))

Emitted to the GraphEdit when the connection between `from_port` of `from_node` [GraphNode](class_graphnode.md#class-graphnode) and `to_port` of `to_node` [GraphNode](class_graphnode.md#class-graphnode) is attempted to be removed.

---

**duplicate_nodes_request**()

Emitted when this **GraphEdit** captures a `ui_graph_duplicate` action (`Ctrl + D` by default). In general, this signal indicates that the selected [GraphElement](class_graphelement.md#class-graphelement)s should be duplicated.

---

**end_node_move**()

Emitted at the end of a [GraphElement](class_graphelement.md#class-graphelement)'s movement.

---

**frame_rect_changed**(frame: [GraphFrame](class_graphframe.md#class-graphframe), new_rect: [Rect2](class_rect2.md#class-rect2))

Emitted when the [GraphFrame](class_graphframe.md#class-graphframe) `frame` is resized to `new_rect`.

---

**graph_elements_linked_to_frame_request**(elements: [Array](class_array.md#class-array), frame: [StringName](class_stringname.md#class-stringname))

Emitted when one or more [GraphElement](class_graphelement.md#class-graphelement)s are dropped onto the [GraphFrame](class_graphframe.md#class-graphframe) named `frame`, when they were not previously attached to any other one.

`elements` is an array of [GraphElement](class_graphelement.md#class-graphelement)s to be attached.

---

**node_deselected**(node: [Node](class_node.md#class-node))

Emitted when the given [GraphElement](class_graphelement.md#class-graphelement) node is deselected.

---

**node_selected**(node: [Node](class_node.md#class-node))

Emitted when the given [GraphElement](class_graphelement.md#class-graphelement) node is selected.

---

**paste_nodes_request**()

Emitted when this **GraphEdit** captures a `ui_paste` action (`Ctrl + V` by default). In general, this signal indicates that previously copied [GraphElement](class_graphelement.md#class-graphelement)s should be pasted.

---

**popup_request**(at_position: [Vector2](class_vector2.md#class-vector2))

Emitted when a popup is requested. Happens on right-clicking in the GraphEdit. `at_position` is the position of the mouse pointer when the signal is sent.

---

**scroll_offset_changed**(offset: [Vector2](class_vector2.md#class-vector2))

Emitted when the scroll offset is changed by the user. It will not be emitted when changed in code.

---

## Enumerations

enum **PanningScheme**:

PanningScheme **SCROLL_ZOOMS** = `0`

`Mouse Wheel` will zoom, `Ctrl + Mouse Wheel` will move the view.

PanningScheme **SCROLL_PANS** = `1`

`Mouse Wheel` will move the view, `Ctrl + Mouse Wheel` will zoom.

---

enum **GridPattern**:

GridPattern **GRID_PATTERN_LINES** = `0`

Draw the grid using solid lines.

GridPattern **GRID_PATTERN_DOTS** = `1`

Draw the grid using dots.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **connection_lines_antialiased** = `true`

-  **set_connection_lines_antialiased**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_connection_lines_antialiased**()

If `true`, the lines between nodes will use antialiasing.

---

[float](class_float.md#class-float) **connection_lines_curvature** = `0.5`

-  **set_connection_lines_curvature**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_connection_lines_curvature**()

The curvature of the lines between the nodes. 0 results in straight lines.

---

[float](class_float.md#class-float) **connection_lines_thickness** = `4.0`

-  **set_connection_lines_thickness**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_connection_lines_thickness**()

The thickness of the lines between the nodes.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **connections** = `[]`

-  **set_connections**(value: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)])
- [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_connection_list**()

The connections between [GraphNode](class_graphnode.md#class-graphnode)s.

A connection is represented as a [Dictionary](class_dictionary.md#class-dictionary) in the form of:

```gdscript
{
    from_node: StringName,
    from_port: int,
    to_node: StringName,
    to_port: int,
    keep_alive: bool
}
```

Connections with `keep_alive` set to `false` may be deleted automatically if invalid during a redraw.

---

GridPattern **grid_pattern** = `0`

-  **set_grid_pattern**(value: GridPattern)
- GridPattern **get_grid_pattern**()

The pattern used for drawing the grid.

---

[bool](class_bool.md#class-bool) **minimap_enabled** = `true`

-  **set_minimap_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_minimap_enabled**()

If `true`, the minimap is visible.

---

[float](class_float.md#class-float) **minimap_opacity** = `0.65`

-  **set_minimap_opacity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_minimap_opacity**()

The opacity of the minimap rectangle.

---

[Vector2](class_vector2.md#class-vector2) **minimap_size** = `Vector2(240, 160)`

-  **set_minimap_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_minimap_size**()

The size of the minimap rectangle. The map itself is based on the size of the grid area and is scaled to fit this rectangle.

---

PanningScheme **panning_scheme** = `0`

-  **set_panning_scheme**(value: PanningScheme)
- PanningScheme **get_panning_scheme**()

Defines the control scheme for panning with mouse wheel.

---

[bool](class_bool.md#class-bool) **right_disconnects** = `false`

-  **set_right_disconnects**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_right_disconnects_enabled**()

If `true`, enables disconnection of existing connections in the GraphEdit by dragging the right end.

---

[Vector2](class_vector2.md#class-vector2) **scroll_offset** = `Vector2(0, 0)`

-  **set_scroll_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_scroll_offset**()

The scroll offset.

---

[bool](class_bool.md#class-bool) **show_arrange_button** = `true`

-  **set_show_arrange_button**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_arrange_button**()

If `true`, the button to automatically arrange graph nodes is visible.

---

[bool](class_bool.md#class-bool) **show_grid** = `true`

-  **set_show_grid**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_grid**()

If `true`, the grid is visible.

---

[bool](class_bool.md#class-bool) **show_grid_buttons** = `true`

-  **set_show_grid_buttons**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_grid_buttons**()

If `true`, buttons that allow to configure grid and snapping options are visible.

---

[bool](class_bool.md#class-bool) **show_menu** = `true`

-  **set_show_menu**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_menu**()

If `true`, the menu toolbar is visible.

---

[bool](class_bool.md#class-bool) **show_minimap_button** = `true`

-  **set_show_minimap_button**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_minimap_button**()

If `true`, the button to toggle the minimap is visible.

---

[bool](class_bool.md#class-bool) **show_zoom_buttons** = `true`

-  **set_show_zoom_buttons**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_zoom_buttons**()

If `true`, buttons that allow to change and reset the zoom level are visible.

---

[bool](class_bool.md#class-bool) **show_zoom_label** = `false`

-  **set_show_zoom_label**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_zoom_label**()

If `true`, the label with the current zoom level is visible. The zoom level is displayed in percents.

---

[int](class_int.md#class-int) **snapping_distance** = `20`

-  **set_snapping_distance**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_snapping_distance**()

The snapping distance in pixels, also determines the grid line distance.

---

[bool](class_bool.md#class-bool) **snapping_enabled** = `true`

-  **set_snapping_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_snapping_enabled**()

If `true`, enables snapping.

---

[Dictionary](class_dictionary.md#class-dictionary) **type_names** = `{}`

-  **set_type_names**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_type_names**()

[Dictionary](class_dictionary.md#class-dictionary) of human-readable port type names.

---

[float](class_float.md#class-float) **zoom** = `1.0`

-  **set_zoom**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_zoom**()

The current zoom value.

---

[float](class_float.md#class-float) **zoom_max** = `2.0736003`

-  **set_zoom_max**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_zoom_max**()

The upper zoom limit.

---

[float](class_float.md#class-float) **zoom_min** = `0.23256795`

-  **set_zoom_min**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_zoom_min**()

The lower zoom limit.

---

[float](class_float.md#class-float) **zoom_step** = `1.2`

-  **set_zoom_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_zoom_step**()

The step of each zoom level.

---

## Method Descriptions

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **\_get_connection_line**(from_position: [Vector2](class_vector2.md#class-vector2), to_position: [Vector2](class_vector2.md#class-vector2))

Virtual method which can be overridden to customize how connections are drawn.

---

[bool](class_bool.md#class-bool) **\_is_in_input_hotzone**(in_node: [Object](class_object.md#class-object), in_port: [int](class_int.md#class-int), mouse_position: [Vector2](class_vector2.md#class-vector2))

Returns whether the `mouse_position` is in the input hot zone.

By default, a hot zone is a [Rect2](class_rect2.md#class-rect2) positioned such that its center is at `in_node`.[GraphNode.get_input_port_position()](class_graphnode.md#class-graphnode-method-get-input-port-position)(`in_port`) (For output's case, call [GraphNode.get_output_port_position()](class_graphnode.md#class-graphnode-method-get-output-port-position) instead). The hot zone's width is twice the Theme Property `port_grab_distance_horizontal`, and its height is twice the `port_grab_distance_vertical`.

Below is a sample code to help get started:

```gdscript
func _is_in_input_hotzone(in_node, in_port, mouse_position):
    var port_size = Vector2(get_theme_constant("port_grab_distance_horizontal"), get_theme_constant("port_grab_distance_vertical"))
    var port_pos = in_node.get_position() + in_node.get_input_port_position(in_port) - port_size / 2
    var rect = Rect2(port_pos, port_size)

    return rect.has_point(mouse_position)
```

---

[bool](class_bool.md#class-bool) **\_is_in_output_hotzone**(in_node: [Object](class_object.md#class-object), in_port: [int](class_int.md#class-int), mouse_position: [Vector2](class_vector2.md#class-vector2))

Returns whether the `mouse_position` is in the output hot zone. For more information on hot zones, see \_is_in_input_hotzone().

Below is a sample code to help get started:

```gdscript
func _is_in_output_hotzone(in_node, in_port, mouse_position):
    var port_size = Vector2(get_theme_constant("port_grab_distance_horizontal"), get_theme_constant("port_grab_distance_vertical"))
    var port_pos = in_node.get_position() + in_node.get_output_port_position(in_port) - port_size / 2
    var rect = Rect2(port_pos, port_size)

    return rect.has_point(mouse_position)
```

---

[bool](class_bool.md#class-bool) **\_is_node_hover_valid**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int))

This virtual method can be used to insert additional error detection while the user is dragging a connection over a valid port.

Return `true` if the connection is indeed valid or return `false` if the connection is impossible. If the connection is impossible, no snapping to the port and thus no connection request to that port will happen.

In this example a connection to same node is suppressed:

GDScript

```gdscript
func _is_node_hover_valid(from, from_port, to, to_port):
    return from != to
```

C#

```csharp
public override bool _IsNodeHoverValid(StringName fromNode, int fromPort, StringName toNode, int toPort)
{
    return fromNode != toNode;
}
```

---

 **add_valid_connection_type**(from_type: [int](class_int.md#class-int), to_type: [int](class_int.md#class-int))

Allows the connection between two different port types. The port type is defined individually for the left and the right port of each slot with the [GraphNode.set_slot()](class_graphnode.md#class-graphnode-method-set-slot) method.

See also is_valid_connection_type() and remove_valid_connection_type().

---

 **add_valid_left_disconnect_type**(type: [int](class_int.md#class-int))

Allows to disconnect nodes when dragging from the left port of the [GraphNode](class_graphnode.md#class-graphnode)'s slot if it has the specified type. See also remove_valid_left_disconnect_type().

---

 **add_valid_right_disconnect_type**(type: [int](class_int.md#class-int))

Allows to disconnect nodes when dragging from the right port of the [GraphNode](class_graphnode.md#class-graphnode)'s slot if it has the specified type. See also remove_valid_right_disconnect_type().

---

 **arrange_nodes**()

Rearranges selected nodes in a layout with minimum crossings between connections and uniform horizontal and vertical gap between nodes.

---

 **attach_graph_element_to_frame**(element: [StringName](class_stringname.md#class-stringname), frame: [StringName](class_stringname.md#class-stringname))

Attaches the `element` [GraphElement](class_graphelement.md#class-graphelement) to the `frame` [GraphFrame](class_graphframe.md#class-graphframe).

---

 **clear_connections**()

Removes all connections between nodes.

---

[Error](class_@globalscope.md#enum-globalscope-error) **connect_node**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int), keep_alive: [bool](class_bool.md#class-bool) = false)

Create a connection between the `from_port` of the `from_node` [GraphNode](class_graphnode.md#class-graphnode) and the `to_port` of the `to_node` [GraphNode](class_graphnode.md#class-graphnode). If the connection already exists, no connection is created.

Connections with `keep_alive` set to `false` may be deleted automatically if invalid during a redraw.

---

 **detach_graph_element_from_frame**(element: [StringName](class_stringname.md#class-stringname))

Detaches the `element` [GraphElement](class_graphelement.md#class-graphelement) from the [GraphFrame](class_graphframe.md#class-graphframe) it is currently attached to.

---

 **disconnect_node**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int))

Removes the connection between the `from_port` of the `from_node` [GraphNode](class_graphnode.md#class-graphnode) and the `to_port` of the `to_node` [GraphNode](class_graphnode.md#class-graphnode). If the connection does not exist, no connection is removed.

---

 **force_connection_drag_end**()

Ends the creation of the current connection. In other words, if you are dragging a connection you can use this method to abort the process and remove the line that followed your cursor.

This is best used together with connection_drag_started and connection_drag_ended to add custom behavior like node addition through shortcuts.

**Note:** This method suppresses any other connection request signals apart from connection_drag_ended.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_attached_nodes_of_frame**(frame: [StringName](class_stringname.md#class-stringname))

Returns an array of node names that are attached to the [GraphFrame](class_graphframe.md#class-graphframe) with the given name.

---

[Dictionary](class_dictionary.md#class-dictionary) **get_closest_connection_at_point**(point: [Vector2](class_vector2.md#class-vector2), max_distance: [float](class_float.md#class-float) = 4.0)

Returns the closest connection to the given point in screen space. If no connection is found within `max_distance` pixels, an empty [Dictionary](class_dictionary.md#class-dictionary) is returned.

A connection is represented as a [Dictionary](class_dictionary.md#class-dictionary) in the form of:

```gdscript
{
    from_node: StringName,
    from_port: int,
    to_node: StringName,
    to_port: int,
    keep_alive: bool
}
```

For example, getting a connection at a given mouse position can be achieved like this:

GDScript

```gdscript
var connection = get_closest_connection_at_point(mouse_event.get_position())
```

---

[int](class_int.md#class-int) **get_connection_count**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int))

Returns the number of connections from `from_port` of `from_node`.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_connection_line**(from_node: [Vector2](class_vector2.md#class-vector2), to_node: [Vector2](class_vector2.md#class-vector2))

Returns the points which would make up a connection between `from_node` and `to_node`.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_connection_list_from_node**(node: [StringName](class_stringname.md#class-stringname))

Returns an [Array](class_array.md#class-array) containing a list of all connections for `node`.

A connection is represented as a [Dictionary](class_dictionary.md#class-dictionary) in the form of:

```gdscript
{
    from_node: StringName,
    from_port: int,
    to_node: StringName,
    to_port: int,
    keep_alive: bool
}
```

**Example:** Get all connections on a specific port:

```gdscript
func get_connection_list_from_port(node, port):
    var connections = get_connection_list_from_node(node)
    var result = []
    for connection in connections:
        var dict = {}
        if connection["from_node"] == node and connection["from_port"] == port:
            dict["node"] = connection["to_node"]
            dict["port"] = connection["to_port"]
            dict["type"] = "left"
            result.push_back(dict)
        elif connection["to_node"] == node and connection["to_port"] == port:
            dict["node"] = connection["from_node"]
            dict["port"] = connection["from_port"]
            dict["type"] = "right"
            result.push_back(dict)
    return result
```

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_connections_intersecting_with_rect**(rect: [Rect2](class_rect2.md#class-rect2))

Returns an [Array](class_array.md#class-array) containing the list of connections that intersect with the given [Rect2](class_rect2.md#class-rect2).

A connection is represented as a [Dictionary](class_dictionary.md#class-dictionary) in the form of:

```gdscript
{
    from_node: StringName,
    from_port: int,
    to_node: StringName,
    to_port: int,
    keep_alive: bool
}
```

---

[GraphFrame](class_graphframe.md#class-graphframe) **get_element_frame**(element: [StringName](class_stringname.md#class-stringname))

Returns the [GraphFrame](class_graphframe.md#class-graphframe) that contains the [GraphElement](class_graphelement.md#class-graphelement) with the given name.

---

[HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **get_menu_hbox**()

Gets the [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) that contains the zooming and grid snap controls in the top left of the graph. You can use this method to reposition the toolbar or to add your own custom controls to it.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

[bool](class_bool.md#class-bool) **is_node_connected**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int))

Returns `true` if the `from_port` of the `from_node` [GraphNode](class_graphnode.md#class-graphnode) is connected to the `to_port` of the `to_node` [GraphNode](class_graphnode.md#class-graphnode).

---

[bool](class_bool.md#class-bool) **is_valid_connection_type**(from_type: [int](class_int.md#class-int), to_type: [int](class_int.md#class-int))

Returns whether it's possible to make a connection between two different port types. The port type is defined individually for the left and the right port of each slot with the [GraphNode.set_slot()](class_graphnode.md#class-graphnode-method-set-slot) method.

See also add_valid_connection_type() and remove_valid_connection_type().

---

 **remove_valid_connection_type**(from_type: [int](class_int.md#class-int), to_type: [int](class_int.md#class-int))

Disallows the connection between two different port types previously allowed by add_valid_connection_type(). The port type is defined individually for the left and the right port of each slot with the [GraphNode.set_slot()](class_graphnode.md#class-graphnode-method-set-slot) method.

See also is_valid_connection_type().

---

 **remove_valid_left_disconnect_type**(type: [int](class_int.md#class-int))

Disallows to disconnect nodes when dragging from the left port of the [GraphNode](class_graphnode.md#class-graphnode)'s slot if it has the specified type. Use this to disable a disconnection previously allowed with add_valid_left_disconnect_type().

---

 **remove_valid_right_disconnect_type**(type: [int](class_int.md#class-int))

Disallows to disconnect nodes when dragging from the right port of the [GraphNode](class_graphnode.md#class-graphnode)'s slot if it has the specified type. Use this to disable a disconnection previously allowed with add_valid_right_disconnect_type().

---

 **set_connection_activity**(from_node: [StringName](class_stringname.md#class-stringname), from_port: [int](class_int.md#class-int), to_node: [StringName](class_stringname.md#class-stringname), to_port: [int](class_int.md#class-int), amount: [float](class_float.md#class-float))

Sets the coloration of the connection between `from_node`'s `from_port` and `to_node`'s `to_port` with the color provided in the activity theme property. The color is linearly interpolated between the connection color and the activity color using `amount` as weight.

---

 **set_selected**(node: [Node](class_node.md#class-node))

Sets the specified `node` as the one selected.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **activity** = `Color(1, 1, 1, 1)`

Color the connection line is interpolated to based on the activity value of a connection (see set_connection_activity()).

---

[Color](class_color.md#class-color) **connection_hover_tint_color** = `Color(0, 0, 0, 0.3)`

Color which is blended with the connection line when the mouse is hovering over it.

---

[Color](class_color.md#class-color) **connection_rim_color** = `Color(0.1, 0.1, 0.1, 0.6)`

Color of the rim around each connection line used for making intersecting lines more distinguishable.

---

[Color](class_color.md#class-color) **connection_valid_target_tint_color** = `Color(1, 1, 1, 0.4)`

Color which is blended with the connection line when the currently dragged connection is hovering over a valid target port.

---

[Color](class_color.md#class-color) **grid_major** = `Color(1, 1, 1, 0.2)`

Color of major grid lines/dots.

---

[Color](class_color.md#class-color) **grid_minor** = `Color(1, 1, 1, 0.05)`

Color of minor grid lines/dots.

---

[Color](class_color.md#class-color) **selection_fill** = `Color(1, 1, 1, 0.3)`

The fill color of the selection rectangle.

---

[Color](class_color.md#class-color) **selection_stroke** = `Color(1, 1, 1, 0.8)`

The outline color of the selection rectangle.

---

[int](class_int.md#class-int) **connection_hover_thickness** = `0`

Widens the line of a connection when the mouse is hovering over it by a percentage factor. A value of `0` disables the highlight. A value of `100` doubles the line width.

---

[int](class_int.md#class-int) **port_hotzone_inner_extent** = `22`

The horizontal range within which a port can be grabbed (inner side).

---

[int](class_int.md#class-int) **port_hotzone_outer_extent** = `26`

The horizontal range within which a port can be grabbed (outer side).

---

[Texture2D](class_texture2d.md#class-texture2d) **grid_toggle**

The icon for the grid toggle button.

---

[Texture2D](class_texture2d.md#class-texture2d) **layout**

The icon for the layout button for auto-arranging the graph.

---

[Texture2D](class_texture2d.md#class-texture2d) **minimap_toggle**

The icon for the minimap toggle button.

---

[Texture2D](class_texture2d.md#class-texture2d) **snapping_toggle**

The icon for the snapping toggle button.

---

[Texture2D](class_texture2d.md#class-texture2d) **zoom_in**

The icon for the zoom in button.

---

[Texture2D](class_texture2d.md#class-texture2d) **zoom_out**

The icon for the zoom out button.

---

[Texture2D](class_texture2d.md#class-texture2d) **zoom_reset**

The icon for the zoom reset button.

---

[StyleBox](class_stylebox.md#class-stylebox) **menu_panel**

There is currently no description for this theme property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

The background drawn under the grid.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel_focus**

[StyleBox](class_stylebox.md#class-stylebox) used when the **GraphEdit** is focused (when used with assistive apps).
