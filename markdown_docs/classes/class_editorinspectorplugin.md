# EditorInspectorPlugin

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plugin for adding custom property editors on the inspector.

## Description

**EditorInspectorPlugin** allows adding custom property editors to [EditorInspector](class_editorinspector.md#class-editorinspector).

When an object is edited, the \_can_handle() function is called and must return `true` if the object type is supported.

If supported, the function \_parse_begin() will be called, allowing to place custom controls at the beginning of the class.

Subsequently, the \_parse_category() and \_parse_property() are called for every category and property. They offer the ability to add custom controls to the inspector too.

Finally, \_parse_end() will be called.

On each of these calls, the "add" functions can be called.

To use **EditorInspectorPlugin**, register it using the [EditorPlugin.add_inspector_plugin()](class_editorplugin.md#class-editorplugin-method-add-inspector-plugin) method first.

## Tutorials

- [Inspector plugins](../tutorials/plugins/editor/inspector_plugins.md)

## Methods

| [bool](class_bool.md#class-bool)   | \_can_handle(object: [Object](class_object.md#class-object))                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                    | \_parse_begin(object: [Object](class_object.md#class-object))                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                    | \_parse_category(object: [Object](class_object.md#class-object), category: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                     |
|                                    | \_parse_end(object: [Object](class_object.md#class-object))                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                    | \_parse_group(object: [Object](class_object.md#class-object), group: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)   | \_parse_property(object: [Object](class_object.md#class-object), type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), name: [String](class_string.md#class-string), hint_type: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint), hint_string: [String](class_string.md#class-string), usage_flags: [[PropertyUsageFlags](class_@globalscope.md#enum-globalscope-propertyusageflags)], wide: [bool](class_bool.md#class-bool)) |
|                                    | add_custom_control(control: [Control](class_control.md#class-control))                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                    | add_property_editor(property: [String](class_string.md#class-string), editor: [Control](class_control.md#class-control), add_to_end: [bool](class_bool.md#class-bool) = false, label: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                        |
|                                    | add_property_editor_for_multiple_properties(label: [String](class_string.md#class-string), properties: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), editor: [Control](class_control.md#class-control))                                                                                                                                                                                                                |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **\_can_handle**(object: [Object](class_object.md#class-object))

Returns `true` if this object can be handled by this plugin.

---

 **\_parse_begin**(object: [Object](class_object.md#class-object))

Called to allow adding controls at the beginning of the property list for `object`.

---

 **\_parse_category**(object: [Object](class_object.md#class-object), category: [String](class_string.md#class-string))

Called to allow adding controls at the beginning of a category in the property list for `object`.

---

 **\_parse_end**(object: [Object](class_object.md#class-object))

Called to allow adding controls at the end of the property list for `object`.

---

 **\_parse_group**(object: [Object](class_object.md#class-object), group: [String](class_string.md#class-string))

Called to allow adding controls at the beginning of a group or a sub-group in the property list for `object`.

---

[bool](class_bool.md#class-bool) **\_parse_property**(object: [Object](class_object.md#class-object), type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), name: [String](class_string.md#class-string), hint_type: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint), hint_string: [String](class_string.md#class-string), usage_flags: [[PropertyUsageFlags](class_@globalscope.md#enum-globalscope-propertyusageflags)], wide: [bool](class_bool.md#class-bool))

Called to allow adding property-specific editors to the property list for `object`. The added editor control must extend [EditorProperty](class_editorproperty.md#class-editorproperty). Returning `true` removes the built-in editor for this property, otherwise allows to insert a custom editor before the built-in one.

---

 **add_custom_control**(control: [Control](class_control.md#class-control))

Adds a custom control, which is not necessarily a property editor.

---

 **add_property_editor**(property: [String](class_string.md#class-string), editor: [Control](class_control.md#class-control), add_to_end: [bool](class_bool.md#class-bool) = false, label: [String](class_string.md#class-string) = "")

Adds a property editor for an individual property. The `editor` control must extend [EditorProperty](class_editorproperty.md#class-editorproperty).

There can be multiple property editors for a property. If `add_to_end` is `true`, this newly added editor will be displayed after all the other editors of the property whose `add_to_end` is `false`. For example, the editor uses this parameter to add an "Edit Region" button for [Sprite2D.region_rect](class_sprite2d.md#class-sprite2d-property-region-rect) below the regular [Rect2](class_rect2.md#class-rect2) editor.

`label` can be used to choose a custom label for the property editor in the inspector. If left empty, the label is computed from the name of the property instead.

---

 **add_property_editor_for_multiple_properties**(label: [String](class_string.md#class-string), properties: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), editor: [Control](class_control.md#class-control))

Adds an editor that allows modifying multiple properties. The `editor` control must extend [EditorProperty](class_editorproperty.md#class-editorproperty).
