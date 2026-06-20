# ShaderIncludeDB

**Inherits:** [Object](class_object.md#class-object)

Internal database of built in shader include files.

## Description

This object contains shader fragments from Godot's internal shaders. These can be used when access to internal uniform buffers and/or internal functions is required for instance when composing compositor effects or compute shaders. Only fragments for the current rendering device are loaded.

## Methods

| [String](class_string.md#class-string)                                  | get_built_in_include_file(filename: [String](class_string.md#class-string))    |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                        | has_built_in_include_file(filename: [String](class_string.md#class-string))    |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | list_built_in_include_files()                                                |

---

## Method Descriptions

[String](class_string.md#class-string) **get_built_in_include_file**(filename: [String](class_string.md#class-string))

Returns the code for the built-in shader fragment. You can also access this in your shader code through `#include "filename"`.

---

[bool](class_bool.md#class-bool) **has_built_in_include_file**(filename: [String](class_string.md#class-string))

Returns `true` if an include file with this name exists.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **list_built_in_include_files**()

Returns a list of built-in include files that are currently registered.
