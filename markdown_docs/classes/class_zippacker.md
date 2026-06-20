# ZIPPacker

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Allows the creation of ZIP files.

## Description

This class implements a writer that allows storing the multiple blobs in a ZIP archive. See also [ZIPReader](class_zipreader.md#class-zipreader) and [PCKPacker](class_pckpacker.md#class-pckpacker).

```gdscript
# Create a ZIP archive with a single file at its root.
func write_zip_file():
    var writer = ZIPPacker.new()
    var err = writer.open("user://archive.zip")
    if err != OK:
        return err
    writer.start_file("hello.txt")
    writer.write_file("Hello World".to_utf8_buffer())
    writer.close_file()

    writer.close()
    return OK
```

## Properties

| [int](class_int.md#class-int)   | compression_level   | `-1`   |
|---------------------------------|--------------------------------------------------------------------|--------|

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | add_directory(path: [String](class_string.md#class-string), permissions: [[UnixPermissionFlags](class_fileaccess.md#enum-fileaccess-unixpermissionflags)] = 493, modified_time: [int](class_int.md#class-int) = 0)   |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)   | close()                                                                                                                                                                                                                      |
| [Error](class_@globalscope.md#enum-globalscope-error)   | close_file()                                                                                                                                                                                                            |
| [Error](class_@globalscope.md#enum-globalscope-error)   | open(path: [String](class_string.md#class-string), append: ZipAppend = 0)                                                                                                                        |
| [Error](class_@globalscope.md#enum-globalscope-error)   | start_file(path: [String](class_string.md#class-string), permissions: [[UnixPermissionFlags](class_fileaccess.md#enum-fileaccess-unixpermissionflags)] = 420, modified_time: [int](class_int.md#class-int) = 0)         |
| [Error](class_@globalscope.md#enum-globalscope-error)   | write_file(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                     |

---

## Enumerations

enum **ZipAppend**:

ZipAppend **APPEND_CREATE** = `0`

Create a new zip archive at the given path.

ZipAppend **APPEND_CREATEAFTER** = `1`

Append a new zip archive to the end of the already existing file at the given path.

ZipAppend **APPEND_ADDINZIP** = `2`

Add new files to the existing zip archive at the given path.

---

enum **CompressionLevel**:

CompressionLevel **COMPRESSION_DEFAULT** = `-1`

Start a file with the default Deflate compression level (`6`). This is a good compromise between speed and file size.

CompressionLevel **COMPRESSION_NONE** = `0`

Start a file with no compression. This is also known as the "Store" compression mode and is the fastest method of packing files inside a ZIP archive. Consider using this mode for files that are already compressed (such as JPEG, PNG, MP3, or Ogg Vorbis files).

CompressionLevel **COMPRESSION_FAST** = `1`

Start a file with the fastest Deflate compression level (`1`). This is fast to compress, but results in larger file sizes than COMPRESSION_DEFAULT. Decompression speed is generally unaffected by the chosen compression level.

CompressionLevel **COMPRESSION_BEST** = `9`

Start a file with the best Deflate compression level (`9`). This is slow to compress, but results in smaller file sizes than COMPRESSION_DEFAULT. Decompression speed is generally unaffected by the chosen compression level.

---

## Property Descriptions

[int](class_int.md#class-int) **compression_level** = `-1`

-  **set_compression_level**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_compression_level**()

The compression level used when start_file() is called. Use CompressionLevel as a reference.

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **add_directory**(path: [String](class_string.md#class-string), permissions: [[UnixPermissionFlags](class_fileaccess.md#enum-fileaccess-unixpermissionflags)] = 493, modified_time: [int](class_int.md#class-int) = 0)

Adds directory to the archive. If `modified_time` is set to `0`, current system time is used.

**Note:** Directories are automatically created when start_file() is called, use this function before adding files to create directories with custom permissions and modification time.

---

[Error](class_@globalscope.md#enum-globalscope-error) **close**()

Closes the underlying resources used by this instance.

---

[Error](class_@globalscope.md#enum-globalscope-error) **close_file**()

Stops writing to a file within the archive.

It will fail if there is no open file.

---

[Error](class_@globalscope.md#enum-globalscope-error) **open**(path: [String](class_string.md#class-string), append: ZipAppend = 0)

Opens a zip file for writing at the given path using the specified write mode.

This must be called before everything else.

---

[Error](class_@globalscope.md#enum-globalscope-error) **start_file**(path: [String](class_string.md#class-string), permissions: [[UnixPermissionFlags](class_fileaccess.md#enum-fileaccess-unixpermissionflags)] = 420, modified_time: [int](class_int.md#class-int) = 0)

Starts writing to a file within the archive. Only one file can be written at the same time. If `modified_time` is set to `0`, current system time is used.

Must be called after open().

---

[Error](class_@globalscope.md#enum-globalscope-error) **write_file**(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Write the given `data` to the file.

Needs to be called after start_file().
