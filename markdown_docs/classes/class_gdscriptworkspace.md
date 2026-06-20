# GDScriptWorkspace

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Workspace related language server functionality.

## Description

Provides language server functionality related to the workspace.

## Methods

|                                                       | apply_new_signal(obj: [Object](class_object.md#class-object), function: [String](class_string.md#class-string), args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))   |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                       | didDeleteFiles(params: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                         |
| [Dictionary](class_dictionary.md#class-dictionary)    | generate_script_api(path: [String](class_string.md#class-string))                                                                                                                             |
| [String](class_string.md#class-string)                | get_file_path(uri: [String](class_string.md#class-string))                                                                                                                                          |
| [String](class_string.md#class-string)                | get_file_uri(path: [String](class_string.md#class-string))                                                                                                                                           |
| [Error](class_@globalscope.md#enum-globalscope-error) | parse_local_script(path: [String](class_string.md#class-string))                                                                                                                               |
| [Error](class_@globalscope.md#enum-globalscope-error) | parse_script(path: [String](class_string.md#class-string), content: [String](class_string.md#class-string))                                                                                          |
|                                                       | publish_diagnostics(path: [String](class_string.md#class-string))                                                                                                                             |

---

## Method Descriptions

 **apply_new_signal**(obj: [Object](class_object.md#class-object), function: [String](class_string.md#class-string), args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

**Deprecated:** Might result in unwanted side effects for connected clients.

---

 **didDeleteFiles**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Dictionary](class_dictionary.md#class-dictionary) **generate_script_api**(path: [String](class_string.md#class-string))

Returns the interface of the script in a machine-readable format.

---

[String](class_string.md#class-string) **get_file_path**(uri: [String](class_string.md#class-string))

Converts a URI to a file path.

---

[String](class_string.md#class-string) **get_file_uri**(path: [String](class_string.md#class-string))

Converts a file path to a URI.

---

[Error](class_@globalscope.md#enum-globalscope-error) **parse_local_script**(path: [String](class_string.md#class-string))

**Deprecated:** Might result in unwanted side effects for connected clients.

---

[Error](class_@globalscope.md#enum-globalscope-error) **parse_script**(path: [String](class_string.md#class-string), content: [String](class_string.md#class-string))

**Deprecated:** Might result in unwanted side effects for connected clients.

---

 **publish_diagnostics**(path: [String](class_string.md#class-string))

**Deprecated:** Might result in unwanted side effects for connected clients.
