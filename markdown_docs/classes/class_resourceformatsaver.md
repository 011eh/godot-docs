# ResourceFormatSaver

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Saves a specific resource type to a file.

## Description

The engine can save resources when you do it from the editor, or when you use the [ResourceSaver](class_resourcesaver.md#class-resourcesaver) singleton. This is accomplished thanks to multiple **ResourceFormatSaver**s, each handling its own format and called automatically by the engine.

By default, Godot saves resources as `.tres` (text-based), `.res` (binary) or another built-in format, but you can choose to create your own format by extending this class. Be sure to respect the documented return types and values. You should give it a global class name with `class_name` for it to be registered. Like built-in ResourceFormatSavers, it will be called automatically when saving resources of its recognized type(s). You may also implement a [ResourceFormatLoader](class_resourceformatloader.md#class-resourceformatloader).

## Methods

| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)   | \_get_recognized_extensions(resource: [Resource](class_resource.md#class-resource))                                           |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                          | \_recognize(resource: [Resource](class_resource.md#class-resource))                                                                           |
| [bool](class_bool.md#class-bool)                                          | \_recognize_path(resource: [Resource](class_resource.md#class-resource), path: [String](class_string.md#class-string))                   |
| [Error](class_@globalscope.md#enum-globalscope-error)                     | \_save(resource: [Resource](class_resource.md#class-resource), path: [String](class_string.md#class-string), flags: [int](class_int.md#class-int)) |
| [Error](class_@globalscope.md#enum-globalscope-error)                     | \_set_uid(path: [String](class_string.md#class-string), uid: [int](class_int.md#class-int))                                                     |

---

## Method Descriptions

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_recognized_extensions**(resource: [Resource](class_resource.md#class-resource))

Returns the list of extensions available for saving the resource object, provided it is recognized (see \_recognize()).

---

[bool](class_bool.md#class-bool) **\_recognize**(resource: [Resource](class_resource.md#class-resource))

Returns whether the given resource object can be saved by this saver.

---

[bool](class_bool.md#class-bool) **\_recognize_path**(resource: [Resource](class_resource.md#class-resource), path: [String](class_string.md#class-string))

Returns `true` if this saver handles a given save path and `false` otherwise.

If this method is not implemented, the default behavior returns whether the path's extension is within the ones provided by \_get_recognized_extensions().

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_save**(resource: [Resource](class_resource.md#class-resource), path: [String](class_string.md#class-string), flags: [int](class_int.md#class-int))

Saves the given resource object to a file at the target `path`. `flags` is a bitmask composed with [SaverFlags](class_resourcesaver.md#enum-resourcesaver-saverflags) constants.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, or an [Error](class_@globalscope.md#enum-globalscope-error) constant in case of failure.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_set_uid**(path: [String](class_string.md#class-string), uid: [int](class_int.md#class-int))

Sets a new UID for the resource at the given `path`. Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, or an [Error](class_@globalscope.md#enum-globalscope-error) constant in case of failure.
