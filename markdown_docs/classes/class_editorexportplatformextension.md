# EditorExportPlatformExtension

**Inherits:** [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for custom [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) implementations (plugins).

## Description

External [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform) implementations should inherit from this class.

To use [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform), register it using the [EditorPlugin.add_export_platform()](class_editorplugin.md#class-editorplugin-method-add-export-platform) method first.

## Methods

| [bool](class_bool.md#class-bool)                                                        | \_can_export(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                         | \_cleanup()                                                                                                                                                                                                                                                                                                                                                                           |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | \_export_pack(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])                                                                                               |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | \_export_pack_patch(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)]) |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | \_export_project(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])                                                                                         |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | \_export_zip(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])                                                                                                 |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | \_export_zip_patch(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_binary_extensions(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset))                                                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                                                  | \_get_debug_protocol()                                                                                                                                                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)                                                  | \_get_device_architecture(device: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | \_get_export_option_visibility(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), option: [String](class_string.md#class-string))                                                                                                                                                                                               |
| [String](class_string.md#class-string)                                                  | \_get_export_option_warning(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), option: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                         |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_export_options()                                                                                                                                                                                                                                                                                                                                                     |
| [Texture2D](class_texture2d.md#class-texture2d)                                         | \_get_logo()                                                                                                                                                                                                                                                                                                                                                                         |
| [String](class_string.md#class-string)                                                  | \_get_name()                                                                                                                                                                                                                                                                                                                                                                         |
| [Texture2D](class_texture2d.md#class-texture2d)                                         | \_get_option_icon(device: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                      |
| [String](class_string.md#class-string)                                                  | \_get_option_label(device: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                    |
| [String](class_string.md#class-string)                                                  | \_get_option_tooltip(device: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                           | \_get_options_count()                                                                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | \_get_options_tooltip()                                                                                                                                                                                                                                                                                                                                                   |
| [String](class_string.md#class-string)                                                  | \_get_os_name()                                                                                                                                                                                                                                                                                                                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_platform_features()                                                                                                                                                                                                                                                                                                                                               |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_preset_features(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset))                                                                                                                                                                                                                                                                 |
| [Texture2D](class_texture2d.md#class-texture2d)                                         | \_get_run_icon()                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | \_has_valid_export_configuration(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool))                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | \_has_valid_project_configuration(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset))                                                                                                                                                                                                                                         |
|                                                                                         | \_initialize()                                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | \_is_executable(path: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | \_poll_export()                                                                                                                                                                                                                                                                                                                                                                   |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | \_run(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), device: [int](class_int.md#class-int), debug_flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | \_should_update_export_options()                                                                                                                                                                                                                                                                                                                                 |
| [String](class_string.md#class-string)                                                  | get_config_error()                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | get_config_missing_templates()                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | set_config_error(error_text: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | set_config_missing_templates(missing_templates: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                        |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **\_can_export**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool))

Returns `true` if the specified `preset` is valid and can be exported. Use set_config_error() and set_config_missing_templates() to set error details.

Usual implementations call \_has_valid_export_configuration() and \_has_valid_project_configuration() to determine if exporting is possible.

---

 **\_cleanup**()

Called by the editor before platform is unregistered.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_export_pack**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])

Creates a PCK archive at `path` for the specified `preset`.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" disabled, and PCK is selected as a file type.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_export_pack_patch**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])

Creates a patch PCK archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" enabled, and PCK is selected as a file type.

**Note:** The patches provided in `patches` have already been loaded when this method is called and are merely provided as context. When empty the patches defined in the export preset have been loaded instead.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_export_project**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])

Creates a full project at `path` for the specified `preset`.

This method is called when "Export" button is pressed in the export dialog.

This method implementation can call [EditorExportPlatform.save_pack()](class_editorexportplatform.md#class-editorexportplatform-method-save-pack) or [EditorExportPlatform.save_zip()](class_editorexportplatform.md#class-editorexportplatform-method-save-zip) to use default PCK/ZIP export process, or calls [EditorExportPlatform.export_project_files()](class_editorexportplatform.md#class-editorexportplatform-method-export-project-files) and implement custom callback for processing each exported file.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_export_zip**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])

Create a ZIP archive at `path` for the specified `preset`.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" disabled, and ZIP is selected as a file type.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_export_zip_patch**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool), path: [String](class_string.md#class-string), patches: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])

Create a ZIP archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" enabled, and ZIP is selected as a file type.

**Note:** The patches provided in `patches` have already been loaded when this method is called and are merely provided as context. When empty the patches defined in the export preset have been loaded instead.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_binary_extensions**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset))

Returns array of supported binary extensions for the full project export.

---

[String](class_string.md#class-string) **\_get_debug_protocol**()

Returns protocol used for remote debugging. Default implementation return `tcp://`.

---

[String](class_string.md#class-string) **\_get_device_architecture**(device: [int](class_int.md#class-int))

Returns device architecture for one-click deploy.

---

[bool](class_bool.md#class-bool) **\_get_export_option_visibility**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), option: [String](class_string.md#class-string))

Validates `option` and returns visibility for the specified `preset`. Default implementation return `true` for all options.

---

[String](class_string.md#class-string) **\_get_export_option_warning**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), option: [StringName](class_stringname.md#class-stringname))

Validates `option` and returns warning message for the specified `preset`. Default implementation return empty string for all options.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_export_options**()

Returns a property list, as an [Array](class_array.md#class-array) of dictionaries. Each [Dictionary](class_dictionary.md#class-dictionary) must at least contain the `name: StringName` and `type: Variant.Type` entries.

Additionally, the following keys are supported:

- `hint: PropertyHint`
- `hint_string: String`
- `usage: PropertyUsageFlags`
- `class_name: StringName`
- `default_value: Variant`, default value of the property.
- `update_visibility: bool`, if set to `true`, \_get_export_option_visibility() is called for each property when this property is changed.
- `required: bool`, if set to `true`, this property warnings are critical, and should be resolved to make export possible. This value is a hint for the \_has_valid_export_configuration() implementation, and not used by the engine directly.

See also [Object._get_property_list()](class_object.md#class-object-private-method-get-property-list).

---

[Texture2D](class_texture2d.md#class-texture2d) **\_get_logo**()

Returns the platform logo displayed in the export dialog. The logo should be 32×32 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class-editorinterface-method-get-editor-scale)).

---

[String](class_string.md#class-string) **\_get_name**()

Returns export platform name.

---

[Texture2D](class_texture2d.md#class-texture2d) **\_get_option_icon**(device: [int](class_int.md#class-int))

Returns the item icon for the specified `device` in the one-click deploy menu. The icon should be 16×16 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class-editorinterface-method-get-editor-scale)).

---

[String](class_string.md#class-string) **\_get_option_label**(device: [int](class_int.md#class-int))

Returns one-click deploy menu item label for the specified `device`.

---

[String](class_string.md#class-string) **\_get_option_tooltip**(device: [int](class_int.md#class-int))

Returns one-click deploy menu item tooltip for the specified `device`.

---

[int](class_int.md#class-int) **\_get_options_count**()

Returns the number of devices (or other options) available in the one-click deploy menu.

---

[String](class_string.md#class-string) **\_get_options_tooltip**()

Returns tooltip of the one-click deploy menu button.

---

[String](class_string.md#class-string) **\_get_os_name**()

Returns target OS name.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_platform_features**()

Returns array of platform specific features.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_preset_features**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset))

Returns array of platform specific features for the specified `preset`.

---

[Texture2D](class_texture2d.md#class-texture2d) **\_get_run_icon**()

Returns the icon of the one-click deploy menu button. The icon should be 16×16 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class-editorinterface-method-get-editor-scale)).

---

[bool](class_bool.md#class-bool) **\_has_valid_export_configuration**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), debug: [bool](class_bool.md#class-bool))

Returns `true` if export configuration is valid.

---

[bool](class_bool.md#class-bool) **\_has_valid_project_configuration**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset))

Returns `true` if project configuration is valid.

---

 **\_initialize**()

Initializes the plugin. Called by the editor when platform is registered.

---

[bool](class_bool.md#class-bool) **\_is_executable**(path: [String](class_string.md#class-string))

Returns `true` if specified file is a valid executable (native executable or script) for the target platform.

---

[bool](class_bool.md#class-bool) **\_poll_export**()

Returns `true` if one-click deploy options are changed and editor interface should be updated.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_run**(preset: [EditorExportPreset](class_editorexportpreset.md#class-editorexportpreset), device: [int](class_int.md#class-int), debug_flags: [[DebugFlags](class_editorexportplatform.md#enum-editorexportplatform-debugflags)])

This method is called when `device` one-click deploy menu option is selected.

Implementation should export project to a temporary location, upload and run it on the specific `device`, or perform another action associated with the menu item.

---

[bool](class_bool.md#class-bool) **\_should_update_export_options**()

Returns `true` if export options list is changed and presets should be updated.

---

[String](class_string.md#class-string) **get_config_error**()

Returns current configuration error message text. This method should be called only from the \_can_export(), \_has_valid_export_configuration(), or \_has_valid_project_configuration() implementations.

---

[bool](class_bool.md#class-bool) **get_config_missing_templates**()

Returns `true` is export templates are missing from the current configuration. This method should be called only from the \_can_export(), \_has_valid_export_configuration(), or \_has_valid_project_configuration() implementations.

---

 **set_config_error**(error_text: [String](class_string.md#class-string))

Sets current configuration error message text. This method should be called only from the \_can_export(), \_has_valid_export_configuration(), or \_has_valid_project_configuration() implementations.

---

 **set_config_missing_templates**(missing_templates: [bool](class_bool.md#class-bool))

Set to `true` is export templates are missing from the current configuration. This method should be called only from the \_can_export(), \_has_valid_export_configuration(), or \_has_valid_project_configuration() implementations.
