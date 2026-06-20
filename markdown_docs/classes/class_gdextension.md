# GDExtension

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A native library for GDExtension.

## Description

The **GDExtension** resource type represents a [shared library](https://en.wikipedia.org/wiki/Shared_library) which can expand the functionality of the engine. The [GDExtensionManager](class_gdextensionmanager.md#class-gdextensionmanager) singleton is responsible for loading, reloading, and unloading **GDExtension** resources.

**Note:** GDExtension itself is not a scripting language and has no relation to [GDScript](class_gdscript.md#class-gdscript) resources.

## Tutorials

- [GDExtension overview](../engine_details/engine_api/gdextension/what_is_gdextension.md)
- [GDExtension example in C++](../tutorials/scripting/cpp/gdextension_cpp_example.md)

## Methods

| InitializationLevel   | get_minimum_library_initialization_level()    |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                               | is_library_open()                                                      |

---

## Enumerations

enum **InitializationLevel**:

InitializationLevel **INITIALIZATION_LEVEL_CORE** = `0`

The library is initialized at the same time as the core features of the engine.

InitializationLevel **INITIALIZATION_LEVEL_SERVERS** = `1`

The library is initialized at the same time as the engine's servers (such as [RenderingServer](class_renderingserver.md#class-renderingserver) or [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d)).

InitializationLevel **INITIALIZATION_LEVEL_SCENE** = `2`

The library is initialized at the same time as the engine's scene-related classes.

InitializationLevel **INITIALIZATION_LEVEL_EDITOR** = `3`

The library is initialized at the same time as the engine's editor classes. Only happens when loading the GDExtension in the editor.

---

## Method Descriptions

InitializationLevel **get_minimum_library_initialization_level**()

Returns the lowest level required for this extension to be properly initialized (see the InitializationLevel enum).

---

[bool](class_bool.md#class-bool) **is_library_open**()

Returns `true` if this extension's library has been opened.
