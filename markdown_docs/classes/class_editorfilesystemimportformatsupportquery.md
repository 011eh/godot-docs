# EditorFileSystemImportFormatSupportQuery

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Used to query and configure import format support.

## Description

This class is used to query and configure a certain import format. It is used in conjunction with asset format import plugins.

## Methods

| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)   | \_get_file_extensions()      |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                          | \_is_active()                          |
| [bool](class_bool.md#class-bool)                                          | \_query()                                  |

---

## Method Descriptions

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_file_extensions**()

Return the file extensions supported.

---

[bool](class_bool.md#class-bool) **\_is_active**()

Return whether this importer is active.

---

[bool](class_bool.md#class-bool) **\_query**()

Query support. Return `false` if import must not continue.
