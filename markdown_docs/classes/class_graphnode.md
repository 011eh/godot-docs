# GraphNode

**Inherits:** [GraphElement](class_graphelement.md#class-graphelement) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A container with connection ports, representing a node in a [GraphEdit](class_graphedit.md#class-graphedit).

## Description

**GraphNode** allows to create nodes for a [GraphEdit](class_graphedit.md#class-graphedit) graph with customizable content based on its child controls. **GraphNode** is derived from [Container](class_container.md#class-container) and it is responsible for placing its children on screen. This works similar to [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer). Children, in turn, provide **GraphNode** with so-called slots, each of which can have a connection port on either side.

Each **GraphNode** slot is defined by its index and can provide the node with up to two ports: one on the left, and one on the right. By convention the left port is also referred to as the **input port** and the right port is referred to as the **output port**. Each port can be enabled and configured individually, using different type and color. The type is an arbitrary value that you can define using your own considerations. The parent [GraphEdit](class_graphedit.md#class-graphedit) will receive this information on each connect and disconnect request.

Slots can be configured in the Inspector dock once you add at least one child [Control](class_control.md#class-control). The properties are grouped by each slot's index in the "Slot" section.

**Note:** While GraphNode is set up using slots and slot indices, connections are made between the ports which are enabled. Because of that [GraphEdit](class_graphedit.md#class-graphedit) uses the port's index and not the slot's index. You can use get_input_port_slot() and get_output_port_slot() to get the slot index from the port index.

## Properties

| [FocusMode](class_control.md#enum-control-focusmode)     | focus_mode                                                                                 | `3` (overrides [Control](class_control.md#class-control-property-focus-mode))   |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                         | ignore_invalid_connection_type | `false`                                                                         |
| [MouseFilter](class_control.md#enum-control-mousefilter) | mouse_filter                                                                               | `0` (overrides [Control](class_control.md#class-control-property-mouse-filter)) |
| [FocusMode](class_control.md#enum-control-focusmode)     | slots_focus_mode                             | `3`                                                                             |
| [String](class_string.md#class-string)                   | title                                                   | `""`                                                                            |

## Methods

|                                                             | \_draw_port(slot_index: [int](class_int.md#class-int), position: [Vector2i](class_vector2i.md#class-vector2i), left: [bool](class_bool.md#class-bool), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                             | clear_all_slots()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                             | clear_slot(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Color](class_color.md#class-color)                         | get_input_port_color(port_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                               | get_input_port_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Vector2](class_vector2.md#class-vector2)                   | get_input_port_position(port_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                               | get_input_port_slot(port_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                               | get_input_port_type(port_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Color](class_color.md#class-color)                         | get_output_port_color(port_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                               | get_output_port_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Vector2](class_vector2.md#class-vector2)                   | get_output_port_position(port_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                               | get_output_port_slot(port_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                               | get_output_port_type(port_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Color](class_color.md#class-color)                         | get_slot_color_left(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Color](class_color.md#class-color)                         | get_slot_color_right(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Texture2D](class_texture2d.md#class-texture2d)             | get_slot_custom_icon_left(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Texture2D](class_texture2d.md#class-texture2d)             | get_slot_custom_icon_right(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Variant](class_variant.md#class-variant)                   | get_slot_metadata_left(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Variant](class_variant.md#class-variant)                   | get_slot_metadata_right(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                               | get_slot_type_left(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                               | get_slot_type_right(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) | get_titlebar_hbox()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                            | is_slot_draw_stylebox(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                            | is_slot_enabled_left(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                            | is_slot_enabled_right(slot_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                             | set_slot(slot_index: [int](class_int.md#class-int), enable_left_port: [bool](class_bool.md#class-bool), type_left: [int](class_int.md#class-int), color_left: [Color](class_color.md#class-color), enable_right_port: [bool](class_bool.md#class-bool), type_right: [int](class_int.md#class-int), color_right: [Color](class_color.md#class-color), custom_icon_left: [Texture2D](class_texture2d.md#class-texture2d) = null, custom_icon_right: [Texture2D](class_texture2d.md#class-texture2d) = null, draw_stylebox: [bool](class_bool.md#class-bool) = true) |
|                                                             | set_slot_color_left(slot_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                             | set_slot_color_right(slot_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                             | set_slot_custom_icon_left(slot_index: [int](class_int.md#class-int), custom_icon: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                             | set_slot_custom_icon_right(slot_index: [int](class_int.md#class-int), custom_icon: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                             | set_slot_draw_stylebox(slot_index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                             | set_slot_enabled_left(slot_index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                             | set_slot_enabled_right(slot_index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                             | set_slot_metadata_left(slot_index: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                             | set_slot_metadata_right(slot_index: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                             | set_slot_type_left(slot_index: [int](class_int.md#class-int), type: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                             | set_slot_type_right(slot_index: [int](class_int.md#class-int), type: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Theme Properties

| [Color](class_color.md#class-color)             | resizer_color         | `Color(0.875, 0.875, 0.875, 1)`   |
|-------------------------------------------------|---------------------------------------------------------------------|-----------------------------------|
| [int](class_int.md#class-int)                   | port_h_offset      | `0`                               |
| [int](class_int.md#class-int)                   | separation            | `2`                               |
| [Texture2D](class_texture2d.md#class-texture2d) | port                            |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel                         |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel_focus             |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel_selected       |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | slot                           |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | slot_selected         |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | titlebar                   |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | titlebar_selected |                                   |

---

## Signals

**slot_sizes_changed**()

Emitted when any slot's size might have changed.

---

**slot_updated**(slot_index: [int](class_int.md#class-int))

Emitted when any GraphNode's slot is updated.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **ignore_invalid_connection_type** = `false`

-  **set_ignore_invalid_connection_type**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ignoring_valid_connection_type**()

If `true`, you can connect ports with different types, even if the connection was not explicitly allowed in the parent [GraphEdit](class_graphedit.md#class-graphedit).

---

[FocusMode](class_control.md#enum-control-focusmode) **slots_focus_mode** = `3`

-  **set_slots_focus_mode**(value: [FocusMode](class_control.md#enum-control-focusmode))
- [FocusMode](class_control.md#enum-control-focusmode) **get_slots_focus_mode**()

Determines how connection slots can be focused.

- If set to [Control.FOCUS_CLICK](class_control.md#class-control-constant-focus-click), connections can only be made with the mouse.
- If set to [Control.FOCUS_ALL](class_control.md#class-control-constant-focus-all), slots can also be focused using the [ProjectSettings.input/ui_up](class_projectsettings.md#class-projectsettings-property-input-ui-up) and [ProjectSettings.input/ui_down](class_projectsettings.md#class-projectsettings-property-input-ui-down) and connected using [ProjectSettings.input/ui_left](class_projectsettings.md#class-projectsettings-property-input-ui-left) and [ProjectSettings.input/ui_right](class_projectsettings.md#class-projectsettings-property-input-ui-right) input actions.
- If set to [Control.FOCUS_ACCESSIBILITY](class_control.md#class-control-constant-focus-accessibility), slot input actions are only enabled when the screen reader is active.

---

[String](class_string.md#class-string) **title** = `""`

-  **set_title**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_title**()

The text displayed in the GraphNode's title bar.

---

## Method Descriptions

 **\_draw_port**(slot_index: [int](class_int.md#class-int), position: [Vector2i](class_vector2i.md#class-vector2i), left: [bool](class_bool.md#class-bool), color: [Color](class_color.md#class-color))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **clear_all_slots**()

Disables all slots of the GraphNode. This will remove all input/output ports from the GraphNode.

---

 **clear_slot**(slot_index: [int](class_int.md#class-int))

Disables the slot with the given `slot_index`. This will remove the corresponding input and output port from the GraphNode.

---

[Color](class_color.md#class-color) **get_input_port_color**(port_idx: [int](class_int.md#class-int))

Returns the [Color](class_color.md#class-color) of the input port with the given `port_idx`.

---

[int](class_int.md#class-int) **get_input_port_count**()

Returns the number of slots with an enabled input port.

---

[Vector2](class_vector2.md#class-vector2) **get_input_port_position**(port_idx: [int](class_int.md#class-int))

Returns the position of the input port with the given `port_idx`.

---

[int](class_int.md#class-int) **get_input_port_slot**(port_idx: [int](class_int.md#class-int))

Returns the corresponding slot index of the input port with the given `port_idx`.

---

[int](class_int.md#class-int) **get_input_port_type**(port_idx: [int](class_int.md#class-int))

Returns the type of the input port with the given `port_idx`.

---

[Color](class_color.md#class-color) **get_output_port_color**(port_idx: [int](class_int.md#class-int))

Returns the [Color](class_color.md#class-color) of the output port with the given `port_idx`.

---

[int](class_int.md#class-int) **get_output_port_count**()

Returns the number of slots with an enabled output port.

---

[Vector2](class_vector2.md#class-vector2) **get_output_port_position**(port_idx: [int](class_int.md#class-int))

Returns the position of the output port with the given `port_idx`.

---

[int](class_int.md#class-int) **get_output_port_slot**(port_idx: [int](class_int.md#class-int))

Returns the corresponding slot index of the output port with the given `port_idx`.

---

[int](class_int.md#class-int) **get_output_port_type**(port_idx: [int](class_int.md#class-int))

Returns the type of the output port with the given `port_idx`.

---

[Color](class_color.md#class-color) **get_slot_color_left**(slot_index: [int](class_int.md#class-int))

Returns the left (input) [Color](class_color.md#class-color) of the slot with the given `slot_index`.

---

[Color](class_color.md#class-color) **get_slot_color_right**(slot_index: [int](class_int.md#class-int))

Returns the right (output) [Color](class_color.md#class-color) of the slot with the given `slot_index`.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_slot_custom_icon_left**(slot_index: [int](class_int.md#class-int))

Returns the left (input) custom [Texture2D](class_texture2d.md#class-texture2d) of the slot with the given `slot_index`.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_slot_custom_icon_right**(slot_index: [int](class_int.md#class-int))

Returns the right (output) custom [Texture2D](class_texture2d.md#class-texture2d) of the slot with the given `slot_index`.

---

[Variant](class_variant.md#class-variant) **get_slot_metadata_left**(slot_index: [int](class_int.md#class-int))

Returns the left (input) metadata of the slot with the given `slot_index`.

---

[Variant](class_variant.md#class-variant) **get_slot_metadata_right**(slot_index: [int](class_int.md#class-int))

Returns the right (output) metadata of the slot with the given `slot_index`.

---

[int](class_int.md#class-int) **get_slot_type_left**(slot_index: [int](class_int.md#class-int))

Returns the left (input) type of the slot with the given `slot_index`.

---

[int](class_int.md#class-int) **get_slot_type_right**(slot_index: [int](class_int.md#class-int))

Returns the right (output) type of the slot with the given `slot_index`.

---

[HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **get_titlebar_hbox**()

Returns the [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) used for the title bar, only containing a [Label](class_label.md#class-label) for displaying the title by default. This can be used to add custom controls to the title bar such as option or close buttons.

---

[bool](class_bool.md#class-bool) **is_slot_draw_stylebox**(slot_index: [int](class_int.md#class-int))

Returns `true` if the background [StyleBox](class_stylebox.md#class-stylebox) of the slot with the given `slot_index` is drawn.

---

[bool](class_bool.md#class-bool) **is_slot_enabled_left**(slot_index: [int](class_int.md#class-int))

Returns `true` if left (input) side of the slot with the given `slot_index` is enabled.

---

[bool](class_bool.md#class-bool) **is_slot_enabled_right**(slot_index: [int](class_int.md#class-int))

Returns `true` if right (output) side of the slot with the given `slot_index` is enabled.

---

 **set_slot**(slot_index: [int](class_int.md#class-int), enable_left_port: [bool](class_bool.md#class-bool), type_left: [int](class_int.md#class-int), color_left: [Color](class_color.md#class-color), enable_right_port: [bool](class_bool.md#class-bool), type_right: [int](class_int.md#class-int), color_right: [Color](class_color.md#class-color), custom_icon_left: [Texture2D](class_texture2d.md#class-texture2d) = null, custom_icon_right: [Texture2D](class_texture2d.md#class-texture2d) = null, draw_stylebox: [bool](class_bool.md#class-bool) = true)

Sets properties of the slot with the given `slot_index`.

If `enable_left_port`/`enable_right_port` is `true`, a port will appear and the slot will be able to be connected from this side.

With `type_left`/`type_right` an arbitrary type can be assigned to each port. Two ports can be connected if they share the same type, or if the connection between their types is allowed in the parent [GraphEdit](class_graphedit.md#class-graphedit) (see [GraphEdit.add_valid_connection_type()](class_graphedit.md#class-graphedit-method-add-valid-connection-type)). Keep in mind that the [GraphEdit](class_graphedit.md#class-graphedit) has the final say in accepting the connection. Type compatibility simply allows the [GraphEdit.connection_request](class_graphedit.md#class-graphedit-signal-connection-request) signal to be emitted.

Ports can be further customized using `color_left`/`color_right` and `custom_icon_left`/`custom_icon_right`. The color parameter adds a tint to the icon. The custom icon can be used to override the default port dot.

Additionally, `draw_stylebox` can be used to enable or disable drawing of the background stylebox for each slot. See slot.

Individual properties can also be set using one of the `set_slot_*` methods.

**Note:** This method only sets properties of the slot. To create the slot itself, add a [Control](class_control.md#class-control)-derived child to the GraphNode.

---

 **set_slot_color_left**(slot_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the [Color](class_color.md#class-color) of the left (input) side of the slot with the given `slot_index` to `color`.

---

 **set_slot_color_right**(slot_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the [Color](class_color.md#class-color) of the right (output) side of the slot with the given `slot_index` to `color`.

---

 **set_slot_custom_icon_left**(slot_index: [int](class_int.md#class-int), custom_icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets the custom [Texture2D](class_texture2d.md#class-texture2d) of the left (input) side of the slot with the given `slot_index` to `custom_icon`.

---

 **set_slot_custom_icon_right**(slot_index: [int](class_int.md#class-int), custom_icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets the custom [Texture2D](class_texture2d.md#class-texture2d) of the right (output) side of the slot with the given `slot_index` to `custom_icon`.

---

 **set_slot_draw_stylebox**(slot_index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

Toggles the background [StyleBox](class_stylebox.md#class-stylebox) of the slot with the given `slot_index`.

---

 **set_slot_enabled_left**(slot_index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

Toggles the left (input) side of the slot with the given `slot_index`. If `enable` is `true`, a port will appear on the left side and the slot will be able to be connected from this side.

---

 **set_slot_enabled_right**(slot_index: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

Toggles the right (output) side of the slot with the given `slot_index`. If `enable` is `true`, a port will appear on the right side and the slot will be able to be connected from this side.

---

 **set_slot_metadata_left**(slot_index: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant))

Sets the custom metadata for the left (input) side of the slot with the given `slot_index` to `value`.

---

 **set_slot_metadata_right**(slot_index: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant))

Sets the custom metadata for the right (output) side of the slot with the given `slot_index` to `value`.

---

 **set_slot_type_left**(slot_index: [int](class_int.md#class-int), type: [int](class_int.md#class-int))

Sets the left (input) type of the slot with the given `slot_index` to `type`. If the value is negative, all connections will be disallowed to be created via user inputs.

---

 **set_slot_type_right**(slot_index: [int](class_int.md#class-int), type: [int](class_int.md#class-int))

Sets the right (output) type of the slot with the given `slot_index` to `type`. If the value is negative, all connections will be disallowed to be created via user inputs.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **resizer_color** = `Color(0.875, 0.875, 0.875, 1)`

The color modulation applied to the resizer icon.

---

[int](class_int.md#class-int) **port_h_offset** = `0`

Horizontal offset for the ports.

---

[int](class_int.md#class-int) **separation** = `2`

The vertical distance between ports.

---

[Texture2D](class_texture2d.md#class-texture2d) **port**

The icon used for representing ports.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

The default background for the slot area of the **GraphNode**.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel_focus**

[StyleBox](class_stylebox.md#class-stylebox) used when the **GraphNode** is focused (when used with assistive apps).

---

[StyleBox](class_stylebox.md#class-stylebox) **panel_selected**

The [StyleBox](class_stylebox.md#class-stylebox) used for the slot area when selected.

---

[StyleBox](class_stylebox.md#class-stylebox) **slot**

The [StyleBox](class_stylebox.md#class-stylebox) used for each slot of the **GraphNode**.

---

[StyleBox](class_stylebox.md#class-stylebox) **slot_selected**

[StyleBox](class_stylebox.md#class-stylebox) used when the slot is focused (when used with assistive apps).

---

[StyleBox](class_stylebox.md#class-stylebox) **titlebar**

The [StyleBox](class_stylebox.md#class-stylebox) used for the title bar of the **GraphNode**.

---

[StyleBox](class_stylebox.md#class-stylebox) **titlebar_selected**

The [StyleBox](class_stylebox.md#class-stylebox) used for the title bar of the **GraphNode** when it is selected.
