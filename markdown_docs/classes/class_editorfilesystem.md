# EditorFileSystem

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Resource filesystem, as the editor sees it.

## Description

This object holds information of all resources in the filesystem, their types, etc.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_resource_filesystem()](class_editorinterface.md#class-editorinterface-method-get-resource-filesystem).

## Methods

| [String](class_string.md#class-string)                                                          | get_file_type(path: [String](class_string.md#class-string))                                     |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) | get_filesystem()                                                                               |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) | get_filesystem_path(path: [String](class_string.md#class-string))                         |
| [float](class_float.md#class-float)                                                             | get_scanning_progress()                                                                 |
| [bool](class_bool.md#class-bool)                                                                | is_importing()                                                                                   |
| [bool](class_bool.md#class-bool)                                                                | is_scanning()                                                                                     |
|                                                                                                 | reimport_files(files: [PackedStringArray](class_packedstringarray.md#class-packedstringarray)) |
|                                                                                                 | scan()                                                                                                   |
|                                                                                                 | scan_sources()                                                                                   |
|                                                                                                 | update_file(path: [String](class_string.md#class-string))                                         |

---

## Signals

**filesystem_changed**()

Emitted if the filesystem changed.

---

**resources_reimported**(resources: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Emitted if a resource is reimported.

---

**resources_reimporting**(resources: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Emitted before a resource is reimported.

---

**resources_reload**(resources: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Emitted if at least one resource is reloaded when the filesystem is scanned.

---

**script_classes_updated**()

Emitted when the list of global script classes gets updated.

---

**sources_changed**(exist: [bool](class_bool.md#class-bool))

Emitted if the source of any imported file changed.

---

## Method Descriptions

[String](class_string.md#class-string) **get_file_type**(path: [String](class_string.md#class-string))

Returns the resource type of the file, given the full path. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.

---

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) **get_filesystem**()

Gets the root directory object.

---

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class-editorfilesystemdirectory) **get_filesystem_path**(path: [String](class_string.md#class-string))

Returns a view into the filesystem at `path`.

---

[float](class_float.md#class-float) **get_scanning_progress**()

Returns the scan progress for 0 to 1 if the FS is being scanned.

---

[bool](class_bool.md#class-bool) **is_importing**()

Returns `true` if resources are currently being imported.

---

[bool](class_bool.md#class-bool) **is_scanning**()

Returns `true` if the filesystem is being scanned.

---

 **reimport_files**(files: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Reimports a set of files. Call this if these files or their `.import` files were directly edited by script or an external program.

If the file type changed or the file was newly created, use update_file() or scan().

**Note:** This function blocks until the import is finished. However, the main loop iteration, including timers and [Node._process()](class_node.md#class-node-private-method-process), will occur during the import process due to progress bar updates. Avoid calls to reimport_files() or scan() while an import is in progress.

---

 **scan**()

Scan the filesystem for changes.

---

 **scan_sources**()

Check if the source of any imported resource changed.

---

 **update_file**(path: [String](class_string.md#class-string))

Add a file in an existing directory, or schedule file information to be updated on editor restart. Can be used to update text files saved by an external program.

This will not import the file. To reimport, call reimport_files() or scan() methods.
