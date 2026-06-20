# GDExtensionManager

**Inherits:** [Object](class_object.md#class-object)

Provides access to GDExtension functionality.

## Description

The GDExtensionManager loads, initializes, and keeps track of all available [GDExtension](class_gdextension.md#class-gdextension) libraries in the project.

**Note:** Do not worry about GDExtension unless you know what you are doing.

## Tutorials

- [GDExtension overview](../engine_details/engine_api/gdextension/what_is_gdextension.md)
- [GDExtension example in C++](../tutorials/scripting/cpp/gdextension_cpp_example.md)

## Methods

| [GDExtension](class_gdextension.md#class-gdextension)                   | get_extension(path: [String](class_string.md#class-string))                                                                                      |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_loaded_extensions()                                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | is_extension_loaded(path: [String](class_string.md#class-string))                                                                          |
| LoadStatus                       | load_extension(path: [String](class_string.md#class-string))                                                                                    |
| LoadStatus                       | load_extension_from_function(path: [String](class_string.md#class-string), init_func: `const GDExtensionInitializationFunction*`) |
| LoadStatus                       | reload_extension(path: [String](class_string.md#class-string))                                                                                |
| LoadStatus                       | unload_extension(path: [String](class_string.md#class-string))                                                                                |

---

## Signals

**extension_loaded**(extension: [GDExtension](class_gdextension.md#class-gdextension))

Emitted after the editor has finished loading a new extension.

**Note:** This signal is only emitted in editor builds.

---

**extension_unloading**(extension: [GDExtension](class_gdextension.md#class-gdextension))

Emitted before the editor starts unloading an extension.

**Note:** This signal is only emitted in editor builds.

---

**extensions_reloaded**()

Emitted after the editor has finished reloading one or more extensions.

---

## Enumerations

enum **LoadStatus**:

LoadStatus **LOAD_STATUS_OK** = `0`

The extension has loaded successfully.

LoadStatus **LOAD_STATUS_FAILED** = `1`

The extension has failed to load, possibly because it does not exist or has missing dependencies.

LoadStatus **LOAD_STATUS_ALREADY_LOADED** = `2`

The extension has already been loaded.

LoadStatus **LOAD_STATUS_NOT_LOADED** = `3`

The extension has not been loaded.

LoadStatus **LOAD_STATUS_NEEDS_RESTART** = `4`

The extension requires the application to restart to fully load.

---

## Method Descriptions

[GDExtension](class_gdextension.md#class-gdextension) **get_extension**(path: [String](class_string.md#class-string))

Returns the [GDExtension](class_gdextension.md#class-gdextension) at the given file `path`, or `null` if it has not been loaded or does not exist.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_loaded_extensions**()

Returns the file paths of all currently loaded extensions.

---

[bool](class_bool.md#class-bool) **is_extension_loaded**(path: [String](class_string.md#class-string))

Returns `true` if the extension at the given file `path` has already been loaded successfully. See also get_loaded_extensions().

---

LoadStatus **load_extension**(path: [String](class_string.md#class-string))

Loads an extension by absolute file path. The `path` needs to point to a valid [GDExtension](class_gdextension.md#class-gdextension). Returns LOAD_STATUS_OK if successful.

---

LoadStatus **load_extension_from_function**(path: [String](class_string.md#class-string), init_func: `const GDExtensionInitializationFunction*`)

Loads the extension already in address space via the given path and initialization function. The `path` needs to be unique and start with `"libgodot://"`. Returns LOAD_STATUS_OK if successful.

---

LoadStatus **reload_extension**(path: [String](class_string.md#class-string))

Reloads the extension at the given file path. The `path` needs to point to a valid [GDExtension](class_gdextension.md#class-gdextension), otherwise this method may return either LOAD_STATUS_NOT_LOADED or LOAD_STATUS_FAILED.

**Note:** You can only reload extensions in the editor. In release builds, this method always fails and returns LOAD_STATUS_FAILED.

---

LoadStatus **unload_extension**(path: [String](class_string.md#class-string))

Unloads an extension by file path. The `path` needs to point to an already loaded [GDExtension](class_gdextension.md#class-gdextension), otherwise this method returns LOAD_STATUS_NOT_LOADED.
