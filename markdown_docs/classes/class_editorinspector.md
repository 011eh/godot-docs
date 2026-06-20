# EditorInspector

**Inherits:** [ScrollContainer](class_scrollcontainer.md#class-scrollcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control used to edit properties of an object.

## Description

This is the control that implements property editing in the editor's Settings dialogs, the Inspector dock, etc. To get the **EditorInspector** used in the editor's Inspector dock, use [EditorInterface.get_inspector()](class_editorinterface.md#class-editorinterface-method-get-inspector).

**EditorInspector** will show properties in the same order as the array returned by [Object.get_property_list()](class_object.md#class-object-method-get-property-list).

If a property's name is path-like (i.e. if it contains forward slashes), **EditorInspector** will create nested sections for "directories" along the path. For example, if a property is named `highlighting/gdscript/node_path_color`, it will be shown as "Node Path Color" inside the "GDScript" section nested inside the "Highlighting" section.

If a property has [@GlobalScope.PROPERTY_USAGE_GROUP](class_@globalscope.md#class-globalscope-constant-property-usage-group) usage, it will group subsequent properties whose name starts with the property's hint string. The group ends when a property does not start with that hint string or when a new group starts. An empty group name effectively ends the current group. **EditorInspector** will create a top-level section for each group. For example, if a property with group usage is named `Collide With` and its hint string is `collide_with_`, a subsequent `collide_with_area` property will be shown as "Area" inside the "Collide With" section. There is also a special case: when the hint string contains the name of a property, that property is grouped too. This is mainly to help grouping properties like `font`, `font_color` and `font_size` (using the hint string `font_`).

If a property has [@GlobalScope.PROPERTY_USAGE_SUBGROUP](class_@globalscope.md#class-globalscope-constant-property-usage-subgroup) usage, a subgroup will be created in the same way as a group, and a second-level section will be created for each subgroup.

**Note:** Unlike sections created from path-like property names, **EditorInspector** won't capitalize the name for sections created from groups. So properties with group usage usually use capitalized names instead of snake_cased names.

## Properties

| [bool](class_bool.md#class-bool)                                       | draw_focus_border      | `true` (overrides [ScrollContainer](class_scrollcontainer.md#class-scrollcontainer-property-draw-focus-border))   |
|------------------------------------------------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------|
| [FocusMode](class_control.md#enum-control-focusmode)                   | focus_mode             | `2` (overrides [Control](class_control.md#class-control-property-focus-mode))                                     |
| [bool](class_bool.md#class-bool)                                       | follow_focus           | `true` (overrides [ScrollContainer](class_scrollcontainer.md#class-scrollcontainer-property-follow-focus))        |
| [ScrollMode](class_scrollcontainer.md#enum-scrollcontainer-scrollmode) | horizontal_scroll_mode | `0` (overrides [ScrollContainer](class_scrollcontainer.md#class-scrollcontainer-property-horizontal-scroll-mode)) |

## Methods

|                                                                | collapse_all_folding()                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EditorInspector                      | create_default_inspector(filter_line_edit: [LineEdit](class_lineedit.md#class-lineedit) = null)                                                                                                                                                                                                                                                                                                                             |
|                                                                | edit(object: [Object](class_object.md#class-object))                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                | expand_all_folding()                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                | expand_revertable()                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Object](class_object.md#class-object)                         | get_edited_object()                                                                                                                                                                                                                                                                                                                                                                                                                |
| [String](class_string.md#class-string)                         | get_selected_path()                                                                                                                                                                                                                                                                                                                                                                                                                |
| [EditorProperty](class_editorproperty.md#class-editorproperty) | instantiate_property_editor(object: [Object](class_object.md#class-object), type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), path: [String](class_string.md#class-string), hint: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint), hint_text: [String](class_string.md#class-string), usage: [int](class_int.md#class-int), wide: [bool](class_bool.md#class-bool) = false) |

---

## Signals

**edited_object_changed**()

Emitted when the object being edited by the inspector has changed.

---

**object_id_selected**(id: [int](class_int.md#class-int))

Emitted when the Edit button of an [Object](class_object.md#class-object) has been pressed in the inspector. This is mainly used in the remote scene tree Inspector.

---

**property_deleted**(property: [String](class_string.md#class-string))

Emitted when a property is removed from the inspector.

---

**property_edited**(property: [String](class_string.md#class-string))

Emitted when a property is edited in the inspector.

---

**property_keyed**(property: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant), advance: [bool](class_bool.md#class-bool))

Emitted when a property is keyed in the inspector. Properties can be keyed by clicking the "key" icon next to a property when the Animation panel is toggled.

---

**property_selected**(property: [String](class_string.md#class-string))

Emitted when a property is selected in the inspector.

---

**property_toggled**(property: [String](class_string.md#class-string), checked: [bool](class_bool.md#class-bool))

Emitted when a boolean property is toggled in the inspector.

**Note:** This signal is never emitted if the internal `autoclear` property enabled. Since this property is always enabled in the editor inspector, this signal is never emitted by the editor itself.

---

**resource_selected**(resource: [Resource](class_resource.md#class-resource), path: [String](class_string.md#class-string))

Emitted when a resource is selected in the inspector.

---

**restart_requested**()

Emitted when a property that requires a restart to be applied is edited in the inspector. This is only used in the Project Settings and Editor Settings.

---

## Method Descriptions

 **collapse_all_folding**()

Collapses all foldable sections.

---

EditorInspector **create_default_inspector**(filter_line_edit: [LineEdit](class_lineedit.md#class-lineedit) = null)

Creates an inspector with the same configuration as the one used in the editor's Inspector dock. When passing a [LineEdit](class_lineedit.md#class-lineedit) into `filter_line_edit`, the inspector will filter its properties based on [LineEdit.text](class_lineedit.md#class-lineedit-property-text) whenever [LineEdit.text_changed](class_lineedit.md#class-lineedit-signal-text-changed) is emitted.

---

 **edit**(object: [Object](class_object.md#class-object))

Shows the properties of the given `object` in this inspector for editing. To clear the inspector, call this method with `null`.

**Note:** If you want to edit an object in the editor's main inspector, use the `edit_*` methods in [EditorInterface](class_editorinterface.md#class-editorinterface) instead.

---

 **expand_all_folding**()

Expands all foldable sections.

---

 **expand_revertable**()

Expands only the foldable sections that contain a revertable (i.e. non-default) property.

---

[Object](class_object.md#class-object) **get_edited_object**()

Returns the object currently selected in this inspector.

---

[String](class_string.md#class-string) **get_selected_path**()

Gets the path of the currently selected property.

---

[EditorProperty](class_editorproperty.md#class-editorproperty) **instantiate_property_editor**(object: [Object](class_object.md#class-object), type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), path: [String](class_string.md#class-string), hint: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint), hint_text: [String](class_string.md#class-string), usage: [int](class_int.md#class-int), wide: [bool](class_bool.md#class-bool) = false)

Creates a property editor that can be used by plugin UI to edit the specified property of an `object`.
