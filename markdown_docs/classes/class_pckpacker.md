# PCKPacker

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Creates packages that can be loaded into a running project.

## Description

The **PCKPacker** is used to create packages that can be loaded into a running project using [ProjectSettings.load_resource_pack()](class_projectsettings.md#class-projectsettings-method-load-resource-pack).

GDScript

```gdscript
var packer = PCKPacker.new()
packer.pck_start("test.pck")
packer.add_file("res://text.txt", "text.txt")
packer.flush()
```

C#

```csharp
var packer = new PckPacker();
packer.PckStart("test.pck");
packer.AddFile("res://text.txt", "text.txt");
packer.Flush();
```

The above **PCKPacker** creates package `test.pck`, then adds a file named `text.txt` at the root of the package.

**Note:** PCK is Godot's own pack file format. To create ZIP archives that can be read by any program, use [ZIPPacker](class_zippacker.md#class-zippacker) instead.

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | add_file(target_path: [String](class_string.md#class-string), source_path: [String](class_string.md#class-string), encrypt: [bool](class_bool.md#class-bool) = false)                                                                                                                      |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)   | add_file_from_buffer(target_path: [String](class_string.md#class-string), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), encrypt: [bool](class_bool.md#class-bool) = false)                                                                          |
| [Error](class_@globalscope.md#enum-globalscope-error)   | add_file_removal(target_path: [String](class_string.md#class-string))                                                                                                                                                                                                              |
| [Error](class_@globalscope.md#enum-globalscope-error)   | flush(verbose: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                      |
| [Error](class_@globalscope.md#enum-globalscope-error)   | pck_start(pck_path: [String](class_string.md#class-string), alignment: [int](class_int.md#class-int) = 32, key: [String](class_string.md#class-string) = "0000000000000000000000000000000000000000000000000000000000000000", encrypt_directory: [bool](class_bool.md#class-bool) = false) |

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **add_file**(target_path: [String](class_string.md#class-string), source_path: [String](class_string.md#class-string), encrypt: [bool](class_bool.md#class-bool) = false)

Adds the `source_path` file to the current PCK package at the `target_path` internal path. The `res://` prefix for `target_path` is optional and stripped internally. File content is immediately written to the PCK.

---

[Error](class_@globalscope.md#enum-globalscope-error) **add_file_from_buffer**(target_path: [String](class_string.md#class-string), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), encrypt: [bool](class_bool.md#class-bool) = false)

Adds the `data` to the current PCK package at the `target_path` internal path. The `res://` prefix for `target_path` is optional and stripped internally. File content is immediately written to the PCK.

---

[Error](class_@globalscope.md#enum-globalscope-error) **add_file_removal**(target_path: [String](class_string.md#class-string))

Registers a file removal of the `target_path` internal path to the PCK. This is mainly used for patches. If the file at this path has been loaded from a previous PCK, it will be removed. The `res://` prefix for `target_path` is optional and stripped internally.

---

[Error](class_@globalscope.md#enum-globalscope-error) **flush**(verbose: [bool](class_bool.md#class-bool) = false)

Writes the file directory and closes the PCK. If `verbose` is `true`, a list of files added will be printed to the console for easier debugging.

**Note:** **PCKPacker** will automatically flush when it's freed, which happens when it goes out of scope or when it gets assigned with `null`. In C# the reference must be disposed after use, either with the `using` statement or by calling the `Dispose` method directly.

---

[Error](class_@globalscope.md#enum-globalscope-error) **pck_start**(pck_path: [String](class_string.md#class-string), alignment: [int](class_int.md#class-int) = 32, key: [String](class_string.md#class-string) = "0000000000000000000000000000000000000000000000000000000000000000", encrypt_directory: [bool](class_bool.md#class-bool) = false)

Creates a new PCK file at the file path `pck_path`. The `.pck` file extension isn't added automatically, so it should be part of `pck_path` (even though it's not required).
