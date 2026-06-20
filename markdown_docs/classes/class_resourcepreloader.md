# ResourcePreloader

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node used to preload sub-resources inside a scene.

## Description

This node is used to preload sub-resources inside a scene, so when the scene is loaded, all the resources are ready to use and can be retrieved from the preloader. You can add the resources using the ResourcePreloader tab when the node is selected.

GDScript has a simplified [@GDScript.preload()](class_@gdscript.md#class-gdscript-method-preload) built-in method which can be used in most situations, leaving the use of **ResourcePreloader** for more advanced scenarios.

## Methods

|                                                                         | add_resource(name: [StringName](class_stringname.md#class-stringname), resource: [Resource](class_resource.md#class-resource))            |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Resource](class_resource.md#class-resource)                            | get_resource(name: [StringName](class_stringname.md#class-stringname))                                                                    |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_resource_list()                                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | has_resource(name: [StringName](class_stringname.md#class-stringname))                                                                    |
|                                                                         | remove_resource(name: [StringName](class_stringname.md#class-stringname))                                                              |
|                                                                         | rename_resource(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname)) |

---

## Method Descriptions

 **add_resource**(name: [StringName](class_stringname.md#class-stringname), resource: [Resource](class_resource.md#class-resource))

Adds a resource to the preloader with the given `name`. If a resource with the given `name` already exists, the new resource will be renamed to "`name` N" where N is an incrementing number starting from 2.

---

[Resource](class_resource.md#class-resource) **get_resource**(name: [StringName](class_stringname.md#class-stringname))

Returns the resource associated to `name`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_resource_list**()

Returns the list of resources inside the preloader.

---

[bool](class_bool.md#class-bool) **has_resource**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if the preloader contains a resource associated to `name`.

---

 **remove_resource**(name: [StringName](class_stringname.md#class-stringname))

Removes the resource associated to `name` from the preloader.

---

 **rename_resource**(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname))

Renames a resource inside the preloader from `name` to `newname`.
