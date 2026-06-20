# EditorExportPreset

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Export preset configuration.

## Description

Represents the configuration of an export preset, as created by the editor's export dialog. An **EditorExportPreset** instance is intended to be used a read-only configuration passed to the [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) methods when exporting the project.

## Methods

| [bool](class_bool.md#class-bool)                                        | are_advanced_options_enabled()                                                                                                     |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                                  | get_custom_features()                                                                                                                       |
| [Dictionary](class_dictionary.md#class-dictionary)                      | get_customized_files()                                                                                                                     |
| [int](class_int.md#class-int)                                           | get_customized_files_count()                                                                                                         |
| [bool](class_bool.md#class-bool)                                        | get_encrypt_directory()                                                                                                                   |
| [bool](class_bool.md#class-bool)                                        | get_encrypt_pck()                                                                                                                               |
| [String](class_string.md#class-string)                                  | get_encryption_ex_filter()                                                                                                             |
| [String](class_string.md#class-string)                                  | get_encryption_in_filter()                                                                                                             |
| [String](class_string.md#class-string)                                  | get_encryption_key()                                                                                                                         |
| [String](class_string.md#class-string)                                  | get_exclude_filter()                                                                                                                         |
| ExportFilter                   | get_export_filter()                                                                                                                           |
| [String](class_string.md#class-string)                                  | get_export_path()                                                                                                                               |
| FileExportMode               | get_file_export_mode(path: [String](class_string.md#class-string), default: FileExportMode = 0) |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_files_to_export()                                                                                                                       |
| [String](class_string.md#class-string)                                  | get_include_filter()                                                                                                                         |
| [Variant](class_variant.md#class-variant)                               | get_or_env(name: [StringName](class_stringname.md#class-stringname), env_var: [String](class_string.md#class-string))                                |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_patches()                                                                                                                                       |
| [String](class_string.md#class-string)                                  | get_preset_name()                                                                                                                               |
| [Variant](class_variant.md#class-variant)                               | get_project_setting(name: [StringName](class_stringname.md#class-stringname))                                                               |
| ScriptExportMode           | get_script_export_mode()                                                                                                                 |
| [String](class_string.md#class-string)                                  | get_version(name: [StringName](class_stringname.md#class-stringname), windows_version: [bool](class_bool.md#class-bool))                            |
| [bool](class_bool.md#class-bool)                                        | has(property: [StringName](class_stringname.md#class-stringname))                                                                                           |
| [bool](class_bool.md#class-bool)                                        | has_export_file(path: [String](class_string.md#class-string))                                                                                   |
| [bool](class_bool.md#class-bool)                                        | is_dedicated_server()                                                                                                                       |
| [bool](class_bool.md#class-bool)                                        | is_runnable()                                                                                                                                       |

---

## Enumerations

enum **ExportFilter**:

ExportFilter **EXPORT_ALL_RESOURCES** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

ExportFilter **EXPORT_SELECTED_SCENES** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

ExportFilter **EXPORT_SELECTED_RESOURCES** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

ExportFilter **EXCLUDE_SELECTED_RESOURCES** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

ExportFilter **EXPORT_CUSTOMIZED** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

enum **FileExportMode**:

FileExportMode **MODE_FILE_NOT_CUSTOMIZED** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

FileExportMode **MODE_FILE_STRIP** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

FileExportMode **MODE_FILE_KEEP** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

FileExportMode **MODE_FILE_REMOVE** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

enum **ScriptExportMode**:

ScriptExportMode **MODE_SCRIPT_TEXT** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

ScriptExportMode **MODE_SCRIPT_BINARY_TOKENS** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

ScriptExportMode **MODE_SCRIPT_BINARY_TOKENS_COMPRESSED** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

## Method Descriptions

[bool](class_bool.md#class-bool) **are_advanced_options_enabled**()

Returns `true` if the "Advanced" toggle is enabled in the export dialog.

---

[String](class_string.md#class-string) **get_custom_features**()

Returns a comma-separated list of custom features added to this preset, as a string. See [Feature tags](../tutorials/export/feature_tags.md) in the documentation for more information.

---

[Dictionary](class_dictionary.md#class-dictionary) **get_customized_files**()

Returns a dictionary of files selected in the "Resources" tab of the export dialog. The dictionary's keys are file paths, and its values are the corresponding export modes: `"strip"`, `"keep"`, or `"remove"`. See also get_file_export_mode().

---

[int](class_int.md#class-int) **get_customized_files_count**()

Returns the number of files selected in the "Resources" tab of the export dialog.

---

[bool](class_bool.md#class-bool) **get_encrypt_directory**()

Returns `true` if PCK directory encryption is enabled in the export dialog.

---

[bool](class_bool.md#class-bool) **get_encrypt_pck**()

Returns `true` if PCK encryption is enabled in the export dialog.

---

[String](class_string.md#class-string) **get_encryption_ex_filter**()

Returns file filters to exclude during PCK encryption.

---

[String](class_string.md#class-string) **get_encryption_in_filter**()

Returns file filters to include during PCK encryption.

---

[String](class_string.md#class-string) **get_encryption_key**()

Returns PCK encryption key.

---

[String](class_string.md#class-string) **get_exclude_filter**()

Returns file filters to exclude during export.

---

ExportFilter **get_export_filter**()

Returns export file filter mode selected in the "Resources" tab of the export dialog.

---

[String](class_string.md#class-string) **get_export_path**()

Returns export target path.

---

FileExportMode **get_file_export_mode**(path: [String](class_string.md#class-string), default: FileExportMode = 0)

Returns file export mode for the specified file.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_files_to_export**()

Returns array of files to export.

---

[String](class_string.md#class-string) **get_include_filter**()

Returns file filters to include during export.

---

[Variant](class_variant.md#class-variant) **get_or_env**(name: [StringName](class_stringname.md#class-stringname), env_var: [String](class_string.md#class-string))

Returns export option value or value of environment variable if it is set.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_patches**()

Returns the list of packs on which to base a patch export on.

---

[String](class_string.md#class-string) **get_preset_name**()

Returns this export preset's name.

---

[Variant](class_variant.md#class-variant) **get_project_setting**(name: [StringName](class_stringname.md#class-stringname))

Returns the value of the setting identified by `name` using export preset feature tag overrides instead of current OS features.

---

ScriptExportMode **get_script_export_mode**()

Returns the export mode used by GDScript files. `0` for "Text", `1` for "Binary tokens", and `2` for "Compressed binary tokens (smaller files)".

---

[String](class_string.md#class-string) **get_version**(name: [StringName](class_stringname.md#class-stringname), windows_version: [bool](class_bool.md#class-bool))

Returns the preset's version number, or fall back to the [ProjectSettings.application/config/version](class_projectsettings.md#class-projectsettings-property-application-config-version) project setting if set to an empty string.

If `windows_version` is `true`, formats the returned version number to be compatible with Windows executable metadata.

---

[bool](class_bool.md#class-bool) **has**(property: [StringName](class_stringname.md#class-stringname))

Returns `true` if the preset has the property named `property`.

---

[bool](class_bool.md#class-bool) **has_export_file**(path: [String](class_string.md#class-string))

Returns `true` if the file at the specified `path` will be exported.

---

[bool](class_bool.md#class-bool) **is_dedicated_server**()

Returns `true` if the dedicated server export mode is selected in the export dialog.

---

[bool](class_bool.md#class-bool) **is_runnable**()

Returns `true` if the "Runnable" toggle is enabled in the export dialog.
