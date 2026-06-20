# EditorFileSystemDirectory

**Inherits:** [Object](class_object.md#class-object)

A directory for the resource filesystem.

## Description

A more generalized, low-level variation of the directory concept.

## Methods

| [int](class_int.md#class-int)                                 | find_dir_index(name: [String](class_string.md#class-string))                     |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                 | find_file_index(name: [String](class_string.md#class-string))                   |
| [String](class_string.md#class-string)                        | get_file(idx: [int](class_int.md#class-int))                                           |
| [int](class_int.md#class-int)                                 | get_file_count()                                                                 |
| [bool](class_bool.md#class-bool)                              | get_file_import_is_valid(idx: [int](class_int.md#class-int))           |
| [String](class_string.md#class-string)                        | get_file_path(idx: [int](class_int.md#class-int))                                 |
| [String](class_string.md#class-string)                        | get_file_script_class_extends(idx: [int](class_int.md#class-int)) |
| [String](class_string.md#class-string)                        | get_file_script_class_name(idx: [int](class_int.md#class-int))       |
| [StringName](class_stringname.md#class-stringname)            | get_file_type(idx: [int](class_int.md#class-int))                                 |
| [String](class_string.md#class-string)                        | get_name()                                                                             |
| EditorFileSystemDirectory | get_parent()                                                                         |
| [String](class_string.md#class-string)                        | get_path()                                                                             |
| EditorFileSystemDirectory | get_subdir(idx: [int](class_int.md#class-int))                                       |
| [int](class_int.md#class-int)                                 | get_subdir_count()                                                             |

---

## Method Descriptions

[int](class_int.md#class-int) **find_dir_index**(name: [String](class_string.md#class-string))

Returns the index of the directory with name `name` or `-1` if not found.

---

[int](class_int.md#class-int) **find_file_index**(name: [String](class_string.md#class-string))

Returns the index of the file with name `name` or `-1` if not found.

---

[String](class_string.md#class-string) **get_file**(idx: [int](class_int.md#class-int))

Returns the name of the file at index `idx`.

---

[int](class_int.md#class-int) **get_file_count**()

Returns the number of files in this directory.

---

[bool](class_bool.md#class-bool) **get_file_import_is_valid**(idx: [int](class_int.md#class-int))

Returns `true` if the file at index `idx` imported properly.

---

[String](class_string.md#class-string) **get_file_path**(idx: [int](class_int.md#class-int))

Returns the path to the file at index `idx`.

---

[String](class_string.md#class-string) **get_file_script_class_extends**(idx: [int](class_int.md#class-int))

Returns the base class of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.

---

[String](class_string.md#class-string) **get_file_script_class_name**(idx: [int](class_int.md#class-int))

Returns the name of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.

---

[StringName](class_stringname.md#class-stringname) **get_file_type**(idx: [int](class_int.md#class-int))

Returns the resource type of the file at index `idx`. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.

---

[String](class_string.md#class-string) **get_name**()

Returns the name of this directory.

---

EditorFileSystemDirectory **get_parent**()

Returns the parent directory for this directory or `null` if called on a directory at `res://` or `user://`.

---

[String](class_string.md#class-string) **get_path**()

Returns the path to this directory.

---

EditorFileSystemDirectory **get_subdir**(idx: [int](class_int.md#class-int))

Returns the subdirectory at index `idx`.

---

[int](class_int.md#class-int) **get_subdir_count**()

Returns the number of subdirectories in this directory.
