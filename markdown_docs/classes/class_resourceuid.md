# ResourceUID

**Inherits:** [Object](class_object.md#class-object)

A singleton that manages the unique identifiers of all resources within a project.

## Description

Resource UIDs (Unique IDentifiers) allow the engine to keep references between resources intact, even if files are renamed or moved. They can be accessed with `uid://`.

**ResourceUID** keeps track of all registered resource UIDs in a project, generates new UIDs, and converts between their string and integer representations.

## Methods

|                                        | add_id(id: [int](class_int.md#class-int), path: [String](class_string.md#class-string))   |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)          | create_id()                                                                            |
| [int](class_int.md#class-int)          | create_id_for_path(path: [String](class_string.md#class-string))              |
| [String](class_string.md#class-string) | ensure_path(path_or_uid: [String](class_string.md#class-string))                     |
| [String](class_string.md#class-string) | get_id_path(id: [int](class_int.md#class-int))                                       |
| [bool](class_bool.md#class-bool)       | has_id(id: [int](class_int.md#class-int))                                                 |
| [String](class_string.md#class-string) | id_to_text(id: [int](class_int.md#class-int))                                         |
| [String](class_string.md#class-string) | path_to_uid(path: [String](class_string.md#class-string))                            |
|                                        | remove_id(id: [int](class_int.md#class-int))                                           |
|                                        | set_id(id: [int](class_int.md#class-int), path: [String](class_string.md#class-string))   |
| [int](class_int.md#class-int)          | text_to_id(text_id: [String](class_string.md#class-string))                           |
| [String](class_string.md#class-string) | uid_to_path(uid: [String](class_string.md#class-string))                             |

---

## Constants

**INVALID_ID** = `-1`

The value to use for an invalid UID, for example if the resource could not be loaded.

Its text representation is `uid://<invalid>`.

---

## Method Descriptions

 **add_id**(id: [int](class_int.md#class-int), path: [String](class_string.md#class-string))

Adds a new UID value which is mapped to the given resource path.

Fails with an error if the UID already exists, so be sure to check has_id() beforehand, or use set_id() instead.

---

[int](class_int.md#class-int) **create_id**()

Generates a random resource UID which is guaranteed to be unique within the list of currently loaded UIDs.

In order for this UID to be registered, you must call add_id() or set_id().

---

[int](class_int.md#class-int) **create_id_for_path**(path: [String](class_string.md#class-string))

Like create_id(), but the UID is seeded with the provided `path` and project name. UIDs generated for that path will be always the same within the current project.

---

[String](class_string.md#class-string) **ensure_path**(path_or_uid: [String](class_string.md#class-string))

Returns a path, converting `path_or_uid` if necessary. Fails and returns an empty string if an invalid UID is provided.

---

[String](class_string.md#class-string) **get_id_path**(id: [int](class_int.md#class-int))

Returns the path that the given UID value refers to.

Fails with an error if the UID does not exist, so be sure to check has_id() beforehand.

---

[bool](class_bool.md#class-bool) **has_id**(id: [int](class_int.md#class-int))

Returns whether the given UID value is known to the cache.

---

[String](class_string.md#class-string) **id_to_text**(id: [int](class_int.md#class-int))

Converts the given UID to a `uid://` string value.

---

[String](class_string.md#class-string) **path_to_uid**(path: [String](class_string.md#class-string))

Converts the provided resource `path` to a UID. Returns the unchanged path if it has no associated UID.

---

 **remove_id**(id: [int](class_int.md#class-int))

Removes a loaded UID value from the cache.

Fails with an error if the UID does not exist, so be sure to check has_id() beforehand.

---

 **set_id**(id: [int](class_int.md#class-int), path: [String](class_string.md#class-string))

Updates the resource path of an existing UID.

Fails with an error if the UID does not exist, so be sure to check has_id() beforehand, or use add_id() instead.

---

[int](class_int.md#class-int) **text_to_id**(text_id: [String](class_string.md#class-string))

Extracts the UID value from the given `uid://` string.

---

[String](class_string.md#class-string) **uid_to_path**(uid: [String](class_string.md#class-string))

Converts the provided `uid` to a path. Prints an error if the UID is invalid.
