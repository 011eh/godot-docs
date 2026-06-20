# EditorScenePostImportPlugin

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plugin to control and modifying the process of importing a scene.

## Description

This plugin type exists to modify the process of importing scenes, allowing to change the content as well as add importer options at every stage of the process.

## Methods

|                                           | \_get_import_options(path: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                           | \_get_internal_import_options(category: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                        |
| [Variant](class_variant.md#class-variant) | \_get_internal_option_update_view_required(category: [int](class_int.md#class-int), option: [String](class_string.md#class-string))                                                                                                                                                                                                                                              |
| [Variant](class_variant.md#class-variant) | \_get_internal_option_visibility(category: [int](class_int.md#class-int), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string))                                                                                                                                                                                                                 |
| [Variant](class_variant.md#class-variant) | \_get_option_visibility(path: [String](class_string.md#class-string), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string))                                                                                                                                                                                                                              |
|                                           | \_internal_process(category: [int](class_int.md#class-int), base_node: [Node](class_node.md#class-node), node: [Node](class_node.md#class-node), resource: [Resource](class_resource.md#class-resource))                                                                                                                                                                                                 |
|                                           | \_post_process(scene: [Node](class_node.md#class-node))                                                                                                                                                                                                                                                                                                                                                      |
|                                           | \_pre_process(scene: [Node](class_node.md#class-node))                                                                                                                                                                                                                                                                                                                                                        |
|                                           | add_import_option(name: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                               |
|                                           | add_import_option_advanced(type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), name: [String](class_string.md#class-string), default_value: [Variant](class_variant.md#class-variant), hint: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint) = 0, hint_string: [String](class_string.md#class-string) = "", usage_flags: [int](class_int.md#class-int) = 6) |
| [Variant](class_variant.md#class-variant) | get_option_value(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                       |

---

## Enumerations

enum **InternalImportCategory**:

InternalImportCategory **INTERNAL_IMPORT_CATEGORY_NODE** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

InternalImportCategory **INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

InternalImportCategory **INTERNAL_IMPORT_CATEGORY_MESH** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

InternalImportCategory **INTERNAL_IMPORT_CATEGORY_MATERIAL** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

InternalImportCategory **INTERNAL_IMPORT_CATEGORY_ANIMATION** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

InternalImportCategory **INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

InternalImportCategory **INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

InternalImportCategory **INTERNAL_IMPORT_CATEGORY_MAX** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

## Method Descriptions

 **\_get_import_options**(path: [String](class_string.md#class-string))

Override to add general import options. These will appear in the main import dock on the editor. Add options via add_import_option() and add_import_option_advanced().

---

 **\_get_internal_import_options**(category: [int](class_int.md#class-int))

Override to add internal import options. These will appear in the 3D scene import dialog. Add options via add_import_option() and add_import_option_advanced().

---

[Variant](class_variant.md#class-variant) **\_get_internal_option_update_view_required**(category: [int](class_int.md#class-int), option: [String](class_string.md#class-string))

Should return `true` if the 3D view of the import dialog needs to update when changing the given option.

---

[Variant](class_variant.md#class-variant) **\_get_internal_option_visibility**(category: [int](class_int.md#class-int), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string))

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

---

[Variant](class_variant.md#class-variant) **\_get_option_visibility**(path: [String](class_string.md#class-string), for_animation: [bool](class_bool.md#class-bool), option: [String](class_string.md#class-string))

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

---

 **\_internal_process**(category: [int](class_int.md#class-int), base_node: [Node](class_node.md#class-node), node: [Node](class_node.md#class-node), resource: [Resource](class_resource.md#class-resource))

Process a specific node or resource for a given category.

---

 **\_post_process**(scene: [Node](class_node.md#class-node))

Post-process the scene. This function is called after the final scene has been configured.

---

 **\_pre_process**(scene: [Node](class_node.md#class-node))

Pre-process the scene. This function is called right after the scene format loader loaded the scene and no changes have been made.

Pre-process may be used to adjust internal import options in the `"nodes"`, `"meshes"`, `"animations"` or `"materials"` keys inside `get_option_value("_subresources")`.

---

 **add_import_option**(name: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))

Add a specific import option (name and default value only). This function can only be called from \_get_import_options() and \_get_internal_import_options().

---

 **add_import_option_advanced**(type: [Variant.Type](class_@globalscope.md#enum-globalscope-variant-type), name: [String](class_string.md#class-string), default_value: [Variant](class_variant.md#class-variant), hint: [PropertyHint](class_@globalscope.md#enum-globalscope-propertyhint) = 0, hint_string: [String](class_string.md#class-string) = "", usage_flags: [int](class_int.md#class-int) = 6)

Add a specific import option. This function can only be called from \_get_import_options() and \_get_internal_import_options().

---

[Variant](class_variant.md#class-variant) **get_option_value**(name: [StringName](class_stringname.md#class-stringname))

Query the value of an option. This function can only be called from those querying visibility, or processing.
