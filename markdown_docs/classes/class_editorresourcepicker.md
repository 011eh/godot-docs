# EditorResourcePicker

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorScriptPicker](class_editorscriptpicker.md#class-editorscriptpicker)

Godot editor's control for selecting [Resource](class_resource.md#class-resource) type properties.

## Description

This [Control](class_control.md#class-control) node is used in the editor's Inspector dock to allow editing of [Resource](class_resource.md#class-resource) type properties. It provides options for creating, loading, saving and converting resources. Can be used with [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin) to recreate the same behavior.

**Note:** This [Control](class_control.md#class-control) does not include any editor for the resource, as editing is controlled by the Inspector dock itself or sub-Inspectors.

## Properties

| [String](class_string.md#class-string)       | base_type             | `""`    |
|----------------------------------------------|-------------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)             | editable               | `true`  |
| [Resource](class_resource.md#class-resource) | edited_resource |         |
| [bool](class_bool.md#class-bool)             | toggle_mode         | `false` |

## Methods

| [bool](class_bool.md#class-bool)                                        | \_handle_menu_selected(id: [int](class_int.md#class-int))             |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                         | \_set_create_options(menu_node: [Object](class_object.md#class-object)) |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_allowed_types()                                                              |
|                                                                         | set_toggle_pressed(pressed: [bool](class_bool.md#class-bool))                   |

---

## Signals

**resource_changed**(resource: [Resource](class_resource.md#class-resource))

Emitted when the value of the edited resource was changed.

---

**resource_selected**(resource: [Resource](class_resource.md#class-resource), inspect: [bool](class_bool.md#class-bool))

Emitted when the resource value was set and user clicked to edit it. When `inspect` is `true`, the signal was caused by the context menu "Edit" or "Inspect" option.

---

## Property Descriptions

[String](class_string.md#class-string) **base_type** = `""`

-  **set_base_type**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_base_type**()

The base type of allowed resource types. Can be a comma-separated list of several options.

---

[bool](class_bool.md#class-bool) **editable** = `true`

-  **set_editable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editable**()

If `true`, the value can be selected and edited.

---

[Resource](class_resource.md#class-resource) **edited_resource**

-  **set_edited_resource**(value: [Resource](class_resource.md#class-resource))
- [Resource](class_resource.md#class-resource) **get_edited_resource**()

The edited resource value.

---

[bool](class_bool.md#class-bool) **toggle_mode** = `false`

-  **set_toggle_mode**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_toggle_mode**()

If `true`, the main button with the resource preview works in the toggle mode. Use set_toggle_pressed() to manually set the state.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **\_handle_menu_selected**(id: [int](class_int.md#class-int))

This virtual method can be implemented to handle context menu items not handled by default. See \_set_create_options().

---

 **\_set_create_options**(menu_node: [Object](class_object.md#class-object))

This virtual method is called when updating the context menu of an editable **EditorResourcePicker**. Implement this method to override the "New" items section with your own options. `menu_node` is a reference to the [PopupMenu](class_popupmenu.md#class-popupmenu) node.

**Note:** Implement \_handle_menu_selected() to handle these custom items.

**Note:** Relevant built-in options ("Load", "Copy", "Paste", etc.) are automatically added to the `menu_node` afterwards, using their hard-coded IDs starting from `0`. Custom options need to use non-colliding IDs to be handled properly. Using `id = 100 + custom_option_index` is safe (this is what the default items in the "New" section use).

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_allowed_types**()

Returns a list of all allowed types and subtypes corresponding to the base_type. If the base_type is empty, an empty list is returned.

---

 **set_toggle_pressed**(pressed: [bool](class_bool.md#class-bool))

Sets the toggle mode state for the main button. Works only if toggle_mode is set to `true`.
