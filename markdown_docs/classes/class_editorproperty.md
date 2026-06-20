# EditorProperty

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Custom control for editing properties that can be added to the [EditorInspector](class_editorinspector.md#class-editorinspector).

## Description

A custom control for editing properties that can be added to the [EditorInspector](class_editorinspector.md#class-editorinspector). It is added via [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin).

## Properties

| [bool](class_bool.md#class-bool)                     | checkable               | `false`                                                                       |
|------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                     | checked                   | `false`                                                                       |
| [bool](class_bool.md#class-bool)                     | deletable               | `false`                                                                       |
| [bool](class_bool.md#class-bool)                     | draw_background   | `true`                                                                        |
| [bool](class_bool.md#class-bool)                     | draw_label             | `true`                                                                        |
| [bool](class_bool.md#class-bool)                     | draw_warning         | `false`                                                                       |
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode                                                          | `3` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [bool](class_bool.md#class-bool)                     | keying                     | `false`                                                                       |
| [String](class_string.md#class-string)               | label                       | `""`                                                                          |
| [float](class_float.md#class-float)                  | name_split_ratio | `0.5`                                                                         |
| [bool](class_bool.md#class-bool)                     | read_only               | `false`                                                                       |
| [bool](class_bool.md#class-bool)                     | selectable             | `true`                                                                        |
| [bool](class_bool.md#class-bool)                     | use_folding           | `false`                                                                       |

## Methods

|                                                    | \_set_read_only(read_only: [bool](class_bool.md#class-bool))                                                                                                                                                                             |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                    | \_update_property()                                                                                                                                                                                                                    |
|                                                    | add_focusable(control: [Control](class_control.md#class-control))                                                                                                                                                                                |
|                                                    | deselect()                                                                                                                                                                                                                                            |
|                                                    | emit_changed(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant), field: [StringName](class_stringname.md#class-stringname) = &"", changing: [bool](class_bool.md#class-bool) = false) |
| [Object](class_object.md#class-object)             | get_edited_object()                                                                                                                                                                                                                          |
| [StringName](class_stringname.md#class-stringname) | get_edited_property()                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                   | is_selected()                                                                                                                                                                                                                                      |
|                                                    | select(focusable: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                   |
|                                                    | set_bottom_editor(editor: [Control](class_control.md#class-control))                                                                                                                                                                         |
|                                                    | set_label_reference(control: [Control](class_control.md#class-control))                                                                                                                                                                    |
|                                                    | set_object_and_property(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname))                                                                                                  |
|                                                    | update_property()                                                                                                                                                                                                                              |

---

## Signals

**multiple_properties_changed**(properties: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), value: [Array](class_array.md#class-array))

Emit it if you want multiple properties modified at the same time. Do not use if added via [EditorInspectorPlugin._parse_property()](class_editorinspectorplugin.md#class-editorinspectorplugin-private-method-parse-property).

---

**object_id_selected**(property: [StringName](class_stringname.md#class-stringname), id: [int](class_int.md#class-int))

Used by sub-inspectors. Emit it if what was selected was an Object ID.

---

**property_can_revert_changed**(property: [StringName](class_stringname.md#class-stringname), can_revert: [bool](class_bool.md#class-bool))

Emitted when the revertability (i.e., whether it has a non-default value and thus is displayed with a revert icon) of a property has changed.

---

**property_changed**(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant), field: [StringName](class_stringname.md#class-stringname), changing: [bool](class_bool.md#class-bool))

Do not emit this manually, use the emit_changed() method instead.

---

**property_checked**(property: [StringName](class_stringname.md#class-stringname), checked: [bool](class_bool.md#class-bool))

Emitted when a property was checked. Used internally.

---

**property_deleted**(property: [StringName](class_stringname.md#class-stringname))

Emitted when a property was deleted. Used internally.

---

**property_favorited**(property: [StringName](class_stringname.md#class-stringname), favorited: [bool](class_bool.md#class-bool))

Emit it if you want to mark a property as favorited, making it appear at the top of the inspector.

---

**property_keyed**(property: [StringName](class_stringname.md#class-stringname))

Emit it if you want to add this value as an animation key (check for keying being enabled first).

---

**property_keyed_with_value**(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Emit it if you want to key a property with a single value.

---

**property_overridden**()

Emitted when a setting override for the current project is requested.

---

**property_pinned**(property: [StringName](class_stringname.md#class-stringname), pinned: [bool](class_bool.md#class-bool))

Emit it if you want to mark (or unmark) the value of a property for being saved regardless of being equal to the default value.

The default value is the one the property will get when the node is just instantiated and can come from an ancestor scene in the inheritance/instantiation chain, a script or a builtin class.

---

**resource_selected**(path: [String](class_string.md#class-string), resource: [Resource](class_resource.md#class-resource))

If you want a sub-resource to be edited, emit this signal with the resource.

---

**selected**(path: [String](class_string.md#class-string), focusable_idx: [int](class_int.md#class-int))

Emitted when selected. Used internally.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **checkable** = `false`

-  **set_checkable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_checkable**()

Used by the inspector, set to `true` when the property is checkable.

---

[bool](class_bool.md#class-bool) **checked** = `false`

-  **set_checked**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_checked**()

Used by the inspector, set to `true` when the property is checked.

---

[bool](class_bool.md#class-bool) **deletable** = `false`

-  **set_deletable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deletable**()

Used by the inspector, set to `true` when the property can be deleted by the user.

---

[bool](class_bool.md#class-bool) **draw_background** = `true`

-  **set_draw_background**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_background**()

Used by the inspector, set to `true` when the property background is drawn.

---

[bool](class_bool.md#class-bool) **draw_label** = `true`

-  **set_draw_label**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_label**()

Used by the inspector, set to `true` when the property label is drawn.

---

[bool](class_bool.md#class-bool) **draw_warning** = `false`

-  **set_draw_warning**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_warning**()

Used by the inspector, set to `true` when the property is drawn with the editor theme's warning color. This is used for editable children's properties.

---

[bool](class_bool.md#class-bool) **keying** = `false`

-  **set_keying**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_keying**()

Used by the inspector, set to `true` when the property can add keys for animation.

---

[String](class_string.md#class-string) **label** = `""`

-  **set_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_label**()

Set this property to change the label (if you want to show one).

---

[float](class_float.md#class-float) **name_split_ratio** = `0.5`

-  **set_name_split_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_name_split_ratio**()

Space distribution ratio between the label and the editing field.

---

[bool](class_bool.md#class-bool) **read_only** = `false`

-  **set_read_only**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_read_only**()

Used by the inspector, set to `true` when the property is read-only.

---

[bool](class_bool.md#class-bool) **selectable** = `true`

-  **set_selectable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_selectable**()

Used by the inspector, set to `true` when the property is selectable.

---

[bool](class_bool.md#class-bool) **use_folding** = `false`

-  **set_use_folding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_folding**()

Used by the inspector, set to `true` when the property is using folding.

---

## Method Descriptions

 **\_set_read_only**(read_only: [bool](class_bool.md#class-bool))

Called when the read-only status of the property is changed. It may be used to change custom controls into a read-only or modifiable state.

---

 **\_update_property**()

When this virtual function is called, you must update your editor.

---

 **add_focusable**(control: [Control](class_control.md#class-control))

If any of the controls added can gain keyboard focus, add it here. This ensures that focus will be restored if the inspector is refreshed.

---

 **deselect**()

Draw property as not selected. Used by the inspector.

---

 **emit_changed**(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant), field: [StringName](class_stringname.md#class-stringname) = &"", changing: [bool](class_bool.md#class-bool) = false)

If one or several properties have changed, this must be called. `field` is used in case your editor can modify fields separately (as an example, Vector3.x). The `changing` argument avoids the editor requesting this property to be refreshed (leave as `false` if unsure).

---

[Object](class_object.md#class-object) **get_edited_object**()

Returns the edited object.

**Note:** This method could return `null` if the editor has not yet been associated with a property. However, in \_update_property() and \_set_read_only(), this value is *guaranteed* to be non-`null`.

---

[StringName](class_stringname.md#class-stringname) **get_edited_property**()

Returns the edited property. If your editor is for a single property (added via [EditorInspectorPlugin._parse_property()](class_editorinspectorplugin.md#class-editorinspectorplugin-private-method-parse-property)), then this will return the property.

**Note:** This method could return `null` if the editor has not yet been associated with a property. However, in \_update_property() and \_set_read_only(), this value is *guaranteed* to be non-`null`.

---

[bool](class_bool.md#class-bool) **is_selected**()

Returns `true` if property is drawn as selected. Used by the inspector.

---

 **select**(focusable: [int](class_int.md#class-int) = -1)

Draw property as selected. Used by the inspector.

---

 **set_bottom_editor**(editor: [Control](class_control.md#class-control))

Puts the `editor` control below the property label. The control must be previously added using [Node.add_child()](class_node.md#class-node-method-add-child).

---

 **set_label_reference**(control: [Control](class_control.md#class-control))

Used by the inspector, set to a control that will be used as a reference to calculate the size of the label.

---

 **set_object_and_property**(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname))

Assigns object and property to edit.

---

 **update_property**()

Forces a refresh of the property display.
