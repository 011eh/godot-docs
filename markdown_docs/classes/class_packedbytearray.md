# PackedByteArray

A packed array of bytes.

## Description

An array specifically designed to hold bytes. Packs data tightly, so it saves memory for large array sizes.

**PackedByteArray** also provides methods to encode/decode various types to/from bytes. The way values are encoded is an implementation detail and shouldn't be relied upon when interacting with external apps.

**Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use duplicate(). This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

**Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Constructors

| PackedByteArray   | PackedByteArray()                                                |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| PackedByteArray   | PackedByteArray(from: PackedByteArray) |
| PackedByteArray   | PackedByteArray(from: [Array](class_array.md#class-array))       |

## Methods

| [bool](class_bool.md#class-bool)                                           | append(value: [int](class_int.md#class-int))                                                                                                                          |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                            | append_array(array: PackedByteArray)                                                                                                  |
| [int](class_int.md#class-int)                                              | bsearch(value: [int](class_int.md#class-int), before: [bool](class_bool.md#class-bool) = true)                                                                       |
|                                                                            | bswap16(offset: [int](class_int.md#class-int) = 0, count: [int](class_int.md#class-int) = -1)                                                                        |
|                                                                            | bswap32(offset: [int](class_int.md#class-int) = 0, count: [int](class_int.md#class-int) = -1)                                                                        |
|                                                                            | bswap64(offset: [int](class_int.md#class-int) = 0, count: [int](class_int.md#class-int) = -1)                                                                        |
|                                                                            | clear()                                                                                                                                                                |
| PackedByteArray                                  | compress(compression_mode: [int](class_int.md#class-int) = 0)                                                                                                       |
| [int](class_int.md#class-int)                                              | count(value: [int](class_int.md#class-int))                                                                                                                            |
| [float](class_float.md#class-float)                                        | decode_double(byte_offset: [int](class_int.md#class-int))                                                                                                      |
| [float](class_float.md#class-float)                                        | decode_float(byte_offset: [int](class_int.md#class-int))                                                                                                        |
| [float](class_float.md#class-float)                                        | decode_half(byte_offset: [int](class_int.md#class-int))                                                                                                          |
| [int](class_int.md#class-int)                                              | decode_s8(byte_offset: [int](class_int.md#class-int))                                                                                                              |
| [int](class_int.md#class-int)                                              | decode_s16(byte_offset: [int](class_int.md#class-int))                                                                                                            |
| [int](class_int.md#class-int)                                              | decode_s32(byte_offset: [int](class_int.md#class-int))                                                                                                            |
| [int](class_int.md#class-int)                                              | decode_s64(byte_offset: [int](class_int.md#class-int))                                                                                                            |
| [int](class_int.md#class-int)                                              | decode_u8(byte_offset: [int](class_int.md#class-int))                                                                                                              |
| [int](class_int.md#class-int)                                              | decode_u16(byte_offset: [int](class_int.md#class-int))                                                                                                            |
| [int](class_int.md#class-int)                                              | decode_u32(byte_offset: [int](class_int.md#class-int))                                                                                                            |
| [int](class_int.md#class-int)                                              | decode_u64(byte_offset: [int](class_int.md#class-int))                                                                                                            |
| [Variant](class_variant.md#class-variant)                                  | decode_var(byte_offset: [int](class_int.md#class-int), allow_objects: [bool](class_bool.md#class-bool) = false)                                                   |
| [int](class_int.md#class-int)                                              | decode_var_size(byte_offset: [int](class_int.md#class-int), allow_objects: [bool](class_bool.md#class-bool) = false)                                         |
| PackedByteArray                                  | decompress(buffer_size: [int](class_int.md#class-int), compression_mode: [int](class_int.md#class-int) = 0)                                                       |
| PackedByteArray                                  | decompress_dynamic(max_output_size: [int](class_int.md#class-int), compression_mode: [int](class_int.md#class-int) = 0)                                   |
| PackedByteArray                                  | duplicate()                                                                                                                                                        |
|                                                                            | encode_double(byte_offset: [int](class_int.md#class-int), value: [float](class_float.md#class-float))                                                          |
|                                                                            | encode_float(byte_offset: [int](class_int.md#class-int), value: [float](class_float.md#class-float))                                                            |
|                                                                            | encode_half(byte_offset: [int](class_int.md#class-int), value: [float](class_float.md#class-float))                                                              |
|                                                                            | encode_s8(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                        |
|                                                                            | encode_s16(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                      |
|                                                                            | encode_s32(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                      |
|                                                                            | encode_s64(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                      |
|                                                                            | encode_u8(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                        |
|                                                                            | encode_u16(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                      |
|                                                                            | encode_u32(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                      |
|                                                                            | encode_u64(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                      |
| [int](class_int.md#class-int)                                              | encode_var(byte_offset: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant), allow_objects: [bool](class_bool.md#class-bool) = false) |
| [bool](class_bool.md#class-bool)                                           | erase(value: [int](class_int.md#class-int))                                                                                                                            |
|                                                                            | fill(value: [int](class_int.md#class-int))                                                                                                                              |
| [int](class_int.md#class-int)                                              | find(value: [int](class_int.md#class-int), from: [int](class_int.md#class-int) = 0)                                                                                     |
| [int](class_int.md#class-int)                                              | get(index: [int](class_int.md#class-int))                                                                                                                                |
| [String](class_string.md#class-string)                                     | get_string_from_ascii()                                                                                                                                |
| [String](class_string.md#class-string)                                     | get_string_from_multibyte_char(encoding: [String](class_string.md#class-string) = "")                                                         |
| [String](class_string.md#class-string)                                     | get_string_from_utf8()                                                                                                                                  |
| [String](class_string.md#class-string)                                     | get_string_from_utf16()                                                                                                                                |
| [String](class_string.md#class-string)                                     | get_string_from_utf32()                                                                                                                                |
| [String](class_string.md#class-string)                                     | get_string_from_wchar()                                                                                                                                |
| [bool](class_bool.md#class-bool)                                           | has(value: [int](class_int.md#class-int))                                                                                                                                |
| [bool](class_bool.md#class-bool)                                           | has_encoded_var(byte_offset: [int](class_int.md#class-int), allow_objects: [bool](class_bool.md#class-bool) = false)                                         |
| [String](class_string.md#class-string)                                     | hex_encode()                                                                                                                                                      |
| [int](class_int.md#class-int)                                              | insert(at_index: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                                 |
| [bool](class_bool.md#class-bool)                                           | is_empty()                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                           | push_back(value: [int](class_int.md#class-int))                                                                                                                    |
|                                                                            | remove_at(index: [int](class_int.md#class-int))                                                                                                                    |
| [int](class_int.md#class-int)                                              | resize(new_size: [int](class_int.md#class-int))                                                                                                                       |
|                                                                            | reverse()                                                                                                                                                            |
| [int](class_int.md#class-int)                                              | rfind(value: [int](class_int.md#class-int), from: [int](class_int.md#class-int) = -1)                                                                                  |
|                                                                            | set(index: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                                                                                          |
| [int](class_int.md#class-int)                                              | size()                                                                                                                                                                  |
| PackedByteArray                                  | slice(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647)                                                                           |
|                                                                            | sort()                                                                                                                                                                  |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)       | to_color_array()                                                                                                                                              |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | to_float32_array()                                                                                                                                          |
| [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) | to_float64_array()                                                                                                                                          |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)       | to_int32_array()                                                                                                                                              |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array)       | to_int64_array()                                                                                                                                              |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | to_vector2_array()                                                                                                                                          |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | to_vector3_array()                                                                                                                                          |
| [PackedVector4Array](class_packedvector4array.md#class-packedvector4array) | to_vector4_array()                                                                                                                                          |

## Operators

| [bool](class_bool.md#class-bool)          | operator !=(right: PackedByteArray)   |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| PackedByteArray | operator +(right: PackedByteArray)    |
| [bool](class_bool.md#class-bool)          | operator ==(right: PackedByteArray)    |
| [int](class_int.md#class-int)             | operator [](index: [int](class_int.md#class-int))                           |

---

## Constructor Descriptions

PackedByteArray **PackedByteArray**()

Constructs an empty **PackedByteArray**.

---

PackedByteArray **PackedByteArray**(from: PackedByteArray)

Constructs a **PackedByteArray** as a copy of the given **PackedByteArray**.

---

PackedByteArray **PackedByteArray**(from: [Array](class_array.md#class-array))

Constructs a new **PackedByteArray**. Optionally, you can pass in a generic [Array](class_array.md#class-array) that will be converted.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **append**(value: [int](class_int.md#class-int))

Appends an element at the end of the array (alias of push_back()).

---

 **append_array**(array: PackedByteArray)

Appends a **PackedByteArray** at the end of this array.

---

[int](class_int.md#class-int) **bsearch**(value: [int](class_int.md#class-int), before: [bool](class_bool.md#class-bool) = true)

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

**Note:** Calling bsearch() on an unsorted array results in unexpected behavior.

---

 **bswap16**(offset: [int](class_int.md#class-int) = 0, count: [int](class_int.md#class-int) = -1)

Swaps the byte order of `count` 16-bit segments of the array starting at `offset`. Swap is done in-place. If `count` is less than zero, all segments to the end of array are processed, if processed data size is not a multiple of 2, the byte after the last processed 16-bit segment is not modified.

---

 **bswap32**(offset: [int](class_int.md#class-int) = 0, count: [int](class_int.md#class-int) = -1)

Swaps the byte order of `count` 32-bit segments of the array starting at `offset`. Swap is done in-place. If `count` is less than zero, all segments to the end of array are processed, if processed data size is not a multiple of 4, bytes after the last processed 32-bit segment are not modified.

---

 **bswap64**(offset: [int](class_int.md#class-int) = 0, count: [int](class_int.md#class-int) = -1)

Swaps the byte order of `count` 64-bit segments of the array starting at `offset`. Swap is done in-place. If `count` is less than zero, all segments to the end of array are processed, if processed data size is not a multiple of 8, bytes after the last processed 64-bit segment are not modified.

---

 **clear**()

Clears the array. This is equivalent to using resize() with a size of `0`.

---

PackedByteArray **compress**(compression_mode: [int](class_int.md#class-int) = 0)

Returns a new **PackedByteArray** with the data compressed. Set the compression mode using one of [CompressionMode](class_fileaccess.md#enum-fileaccess-compressionmode)'s constants.

---

[int](class_int.md#class-int) **count**(value: [int](class_int.md#class-int))

Returns the number of times an element is in the array.

---

[float](class_float.md#class-float) **decode_double**(byte_offset: [int](class_int.md#class-int))

Decodes a 64-bit floating-point number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if a valid number can't be decoded.

---

[float](class_float.md#class-float) **decode_float**(byte_offset: [int](class_int.md#class-int))

Decodes a 32-bit floating-point number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if a valid number can't be decoded.

---

[float](class_float.md#class-float) **decode_half**(byte_offset: [int](class_int.md#class-int))

Decodes a 16-bit floating-point number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0.0` if a valid number can't be decoded.

---

[int](class_int.md#class-int) **decode_s8**(byte_offset: [int](class_int.md#class-int))

Decodes a 8-bit signed integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

[int](class_int.md#class-int) **decode_s16**(byte_offset: [int](class_int.md#class-int))

Decodes a 16-bit signed integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

[int](class_int.md#class-int) **decode_s32**(byte_offset: [int](class_int.md#class-int))

Decodes a 32-bit signed integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

[int](class_int.md#class-int) **decode_s64**(byte_offset: [int](class_int.md#class-int))

Decodes a 64-bit signed integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

[int](class_int.md#class-int) **decode_u8**(byte_offset: [int](class_int.md#class-int))

Decodes a 8-bit unsigned integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

[int](class_int.md#class-int) **decode_u16**(byte_offset: [int](class_int.md#class-int))

Decodes a 16-bit unsigned integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

[int](class_int.md#class-int) **decode_u32**(byte_offset: [int](class_int.md#class-int))

Decodes a 32-bit unsigned integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

[int](class_int.md#class-int) **decode_u64**(byte_offset: [int](class_int.md#class-int))

Decodes a 64-bit unsigned integer number from the bytes starting at `byte_offset`. Fails if the byte count is insufficient. Returns `0` if a valid number can't be decoded.

---

[Variant](class_variant.md#class-variant) **decode_var**(byte_offset: [int](class_int.md#class-int), allow_objects: [bool](class_bool.md#class-bool) = false)

Decodes a [Variant](class_variant.md#class-variant) from the bytes starting at `byte_offset`. Returns `null` if a valid variant can't be decoded or the value is [Object](class_object.md#class-object)-derived and `allow_objects` is `false`.

---

[int](class_int.md#class-int) **decode_var_size**(byte_offset: [int](class_int.md#class-int), allow_objects: [bool](class_bool.md#class-bool) = false)

Decodes a size of a [Variant](class_variant.md#class-variant) from the bytes starting at `byte_offset`. Requires at least 4 bytes of data starting at the offset, otherwise fails.

---

PackedByteArray **decompress**(buffer_size: [int](class_int.md#class-int), compression_mode: [int](class_int.md#class-int) = 0)

Returns a new **PackedByteArray** with the data decompressed. Set `buffer_size` to the size of the uncompressed data. Set the compression mode using one of [CompressionMode](class_fileaccess.md#enum-fileaccess-compressionmode)'s constants.

**Note:** Decompression is not guaranteed to work with data not compressed by Godot, for example if data compressed with the deflate compression mode lacks a checksum or header.

---

PackedByteArray **decompress_dynamic**(max_output_size: [int](class_int.md#class-int), compression_mode: [int](class_int.md#class-int) = 0)

Returns a new **PackedByteArray** with the data decompressed. Set the compression mode using one of [CompressionMode](class_fileaccess.md#enum-fileaccess-compressionmode)'s constants. **This method only accepts brotli, gzip, and deflate compression modes.**

This method is potentially slower than decompress(), as it may have to re-allocate its output buffer multiple times while decompressing, whereas decompress() knows it's output buffer size from the beginning.

GZIP has a maximal compression ratio of 1032:1, meaning it's very possible for a small compressed payload to decompress to a potentially very large output. To guard against this, you may provide a maximum size this function is allowed to allocate in bytes via `max_output_size`. Passing -1 will allow for unbounded output. If any positive value is passed, and the decompression exceeds that amount in bytes, then an error will be returned.

**Note:** Decompression is not guaranteed to work with data not compressed by Godot, for example if data compressed with the deflate compression mode lacks a checksum or header.

---

PackedByteArray **duplicate**()

Creates a copy of the array, and returns it.

---

 **encode_double**(byte_offset: [int](class_int.md#class-int), value: [float](class_float.md#class-float))

Encodes a 64-bit floating-point number as bytes at the index of `byte_offset` bytes. The array must have at least 8 bytes of allocated space, starting at the offset.

---

 **encode_float**(byte_offset: [int](class_int.md#class-int), value: [float](class_float.md#class-float))

Encodes a 32-bit floating-point number as bytes at the index of `byte_offset` bytes. The array must have at least 4 bytes of space, starting at the offset.

---

 **encode_half**(byte_offset: [int](class_int.md#class-int), value: [float](class_float.md#class-float))

Encodes a 16-bit floating-point number as bytes at the index of `byte_offset` bytes. The array must have at least 2 bytes of space, starting at the offset.

---

 **encode_s8**(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Encodes a 8-bit signed integer number (signed byte) at the index of `byte_offset` bytes. The array must have at least 1 byte of space, starting at the offset.

---

 **encode_s16**(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Encodes a 16-bit signed integer number as bytes at the index of `byte_offset` bytes. The array must have at least 2 bytes of space, starting at the offset.

---

 **encode_s32**(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Encodes a 32-bit signed integer number as bytes at the index of `byte_offset` bytes. The array must have at least 4 bytes of space, starting at the offset.

---

 **encode_s64**(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Encodes a 64-bit signed integer number as bytes at the index of `byte_offset` bytes. The array must have at least 8 bytes of space, starting at the offset.

---

 **encode_u8**(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Encodes a 8-bit unsigned integer number (byte) at the index of `byte_offset` bytes. The array must have at least 1 byte of space, starting at the offset.

---

 **encode_u16**(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Encodes a 16-bit unsigned integer number as bytes at the index of `byte_offset` bytes. The array must have at least 2 bytes of space, starting at the offset.

---

 **encode_u32**(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Encodes a 32-bit unsigned integer number as bytes at the index of `byte_offset` bytes. The array must have at least 4 bytes of space, starting at the offset.

---

 **encode_u64**(byte_offset: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Encodes a 64-bit unsigned integer number as bytes at the index of `byte_offset` bytes. The array must have at least 8 bytes of space, starting at the offset.

---

[int](class_int.md#class-int) **encode_var**(byte_offset: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant), allow_objects: [bool](class_bool.md#class-bool) = false)

Encodes a [Variant](class_variant.md#class-variant) at the index of `byte_offset` bytes. A sufficient space must be allocated, depending on the encoded variant's size. If `allow_objects` is `false`, [Object](class_object.md#class-object)-derived values are not permitted and will instead be serialized as ID-only.

---

[bool](class_bool.md#class-bool) **erase**(value: [int](class_int.md#class-int))

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use remove_at() instead.

---

 **fill**(value: [int](class_int.md#class-int))

Assigns the given value to all elements in the array. This can typically be used together with resize() to create an array with a given size and initialized elements.

---

[int](class_int.md#class-int) **find**(value: [int](class_int.md#class-int), from: [int](class_int.md#class-int) = 0)

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

---

[int](class_int.md#class-int) **get**(index: [int](class_int.md#class-int))

Returns the byte at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `0`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

---

[String](class_string.md#class-string) **get_string_from_ascii**()

Converts ASCII/Latin-1 encoded array to [String](class_string.md#class-string). Fast alternative to get_string_from_utf8() if the content is ASCII/Latin-1 only. Unlike the UTF-8 function this function maps every byte to a character in the array. Multibyte sequences will not be interpreted correctly. For parsing user input always use get_string_from_utf8(). This is the inverse of [String.to_ascii_buffer()](class_string.md#class-string-method-to-ascii-buffer).

---

[String](class_string.md#class-string) **get_string_from_multibyte_char**(encoding: [String](class_string.md#class-string) = "")

Converts system multibyte code page encoded array to [String](class_string.md#class-string). If conversion fails, empty string is returned. This is the inverse of [String.to_multibyte_char_buffer()](class_string.md#class-string-method-to-multibyte-char-buffer).

The values permitted for `encoding` are system dependent. If `encoding` is empty string, system default encoding is used.

- For Windows, see [Code Page Identifiers](https://learn.microsoft.com/en-us/windows/win32/Intl/code-page-identifiers) .NET names.
- For macOS and Linux/BSD, see `libiconv` library documentation and `iconv --list` for a list of supported encodings.

---

[String](class_string.md#class-string) **get_string_from_utf8**()

Converts UTF-8 encoded array to [String](class_string.md#class-string). Slower than get_string_from_ascii() but supports UTF-8 encoded data. Use this function if you are unsure about the source of the data. For user input this function should always be preferred. Returns empty string if source array is not valid UTF-8 string. This is the inverse of [String.to_utf8_buffer()](class_string.md#class-string-method-to-utf8-buffer).

---

[String](class_string.md#class-string) **get_string_from_utf16**()

Converts UTF-16 encoded array to [String](class_string.md#class-string). If the BOM is missing, little-endianness is assumed. Returns empty string if source array is not valid UTF-16 string. This is the inverse of [String.to_utf16_buffer()](class_string.md#class-string-method-to-utf16-buffer).

---

[String](class_string.md#class-string) **get_string_from_utf32**()

Converts UTF-32 encoded array to [String](class_string.md#class-string). Returns empty string if source array is not valid UTF-32 string. This is the inverse of [String.to_utf32_buffer()](class_string.md#class-string-method-to-utf32-buffer).

---

[String](class_string.md#class-string) **get_string_from_wchar**()

Converts wide character (`wchar_t`, UTF-16 on Windows, UTF-32 on other platforms) encoded array to [String](class_string.md#class-string). Returns empty string if source array is not valid wide string. This is the inverse of [String.to_wchar_buffer()](class_string.md#class-string-method-to-wchar-buffer).

---

[bool](class_bool.md#class-bool) **has**(value: [int](class_int.md#class-int))

Returns `true` if the array contains `value`.

---

[bool](class_bool.md#class-bool) **has_encoded_var**(byte_offset: [int](class_int.md#class-int), allow_objects: [bool](class_bool.md#class-bool) = false)

Returns `true` if a valid [Variant](class_variant.md#class-variant) value can be decoded at the `byte_offset`. Returns `false` otherwise or when the value is [Object](class_object.md#class-object)-derived and `allow_objects` is `false`.

---

[String](class_string.md#class-string) **hex_encode**()

Returns a hexadecimal representation of this array as a [String](class_string.md#class-string).

GDScript

```gdscript
var array = PackedByteArray([11, 46, 255])
print(array.hex_encode()) # Prints "0b2eff"
```

C#

```csharp
byte[] array = [11, 46, 255];
GD.Print(array.HexEncode()); // Prints "0b2eff"
```

---

[int](class_int.md#class-int) **insert**(at_index: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).

---

[bool](class_bool.md#class-bool) **is_empty**()

Returns `true` if the array is empty.

---

[bool](class_bool.md#class-bool) **push_back**(value: [int](class_int.md#class-int))

Appends an element at the end of the array.

---

 **remove_at**(index: [int](class_int.md#class-int))

Removes an element from the array by index.

---

[int](class_int.md#class-int) **resize**(new_size: [int](class_int.md#class-int))

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling resize() once and assigning the new values is faster than adding new elements one by one.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, or one of the following [Error](class_@globalscope.md#enum-globalscope-error) constants if this method fails: [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) if the size is negative, or [@GlobalScope.ERR_OUT_OF_MEMORY](class_@globalscope.md#class-globalscope-constant-err-out-of-memory) if allocations fail. Use size() to find the actual size of the array after resize.

---

 **reverse**()

Reverses the order of the elements in the array.

---

[int](class_int.md#class-int) **rfind**(value: [int](class_int.md#class-int), from: [int](class_int.md#class-int) = -1)

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

---

 **set**(index: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Changes the byte at the given index.

---

[int](class_int.md#class-int) **size**()

Returns the number of elements in the array.

---

PackedByteArray **slice**(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647)

Returns the slice of the **PackedByteArray**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedByteArray**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

---

 **sort**()

Sorts the elements of the array in ascending order.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **to_color_array**()

Returns a copy of the data converted to a [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), where each block of 16 bytes has been converted to a [Color](class_color.md#class-color) variant.

**Note:** The size of the input array must be a multiple of 16 (size of four 32-bit float variables). The size of the new array will be `byte_array.size() / 16`. If the original data can't be converted to [Color](class_color.md#class-color) variants, the resulting data is undefined.

---

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **to_float32_array**()

Returns a copy of the data converted to a [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), where each block of 4 bytes has been converted to a 32-bit float (C++ `float`).

The size of the input array must be a multiple of 4 (size of 32-bit float). The size of the new array will be `byte_array.size() / 4`.

If the original data can't be converted to 32-bit floats, the resulting data is undefined.

---

[PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) **to_float64_array**()

Returns a copy of the data converted to a [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array), where each block of 8 bytes has been converted to a 64-bit float (C++ `double`, Godot [float](class_float.md#class-float)).

The size of the input array must be a multiple of 8 (size of 64-bit double). The size of the new array will be `byte_array.size() / 8`.

If the original data can't be converted to 64-bit floats, the resulting data is undefined.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **to_int32_array**()

Returns a copy of the data converted to a [PackedInt32Array](class_packedint32array.md#class-packedint32array), where each block of 4 bytes has been converted to a signed 32-bit integer (C++ `int32_t`).

The size of the input array must be a multiple of 4 (size of 32-bit integer). The size of the new array will be `byte_array.size() / 4`.

If the original data can't be converted to signed 32-bit integers, the resulting data is undefined.

---

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **to_int64_array**()

Returns a copy of the data converted to a [PackedInt64Array](class_packedint64array.md#class-packedint64array), where each block of 8 bytes has been converted to a signed 64-bit integer (C++ `int64_t`, Godot [int](class_int.md#class-int)).

The size of the input array must be a multiple of 8 (size of 64-bit integer). The size of the new array will be `byte_array.size() / 8`.

If the original data can't be converted to signed 64-bit integers, the resulting data is undefined.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **to_vector2_array**()

Returns a copy of the data converted to a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), where each block of 8 bytes or 16 bytes (32-bit or 64-bit) has been converted to a [Vector2](class_vector2.md#class-vector2) variant.

**Note:** The size of the input array must be a multiple of 8 or 16 (depending on the build settings, see [Vector2](class_vector2.md#class-vector2) for more details). The size of the new array will be `byte_array.size() / (8 or 16)`. If the original data can't be converted to [Vector2](class_vector2.md#class-vector2) variants, the resulting data is undefined.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **to_vector3_array**()

Returns a copy of the data converted to a [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), where each block of 12 or 24 bytes (32-bit or 64-bit) has been converted to a [Vector3](class_vector3.md#class-vector3) variant.

**Note:** The size of the input array must be a multiple of 12 or 24 (depending on the build settings, see [Vector3](class_vector3.md#class-vector3) for more details). The size of the new array will be `byte_array.size() / (12 or 24)`. If the original data can't be converted to [Vector3](class_vector3.md#class-vector3) variants, the resulting data is undefined.

---

[PackedVector4Array](class_packedvector4array.md#class-packedvector4array) **to_vector4_array**()

Returns a copy of the data converted to a [PackedVector4Array](class_packedvector4array.md#class-packedvector4array), where each block of 16 or 32 bytes (32-bit or 64-bit) has been converted to a [Vector4](class_vector4.md#class-vector4) variant.

**Note:** The size of the input array must be a multiple of 16 or 32 (depending on the build settings, see [Vector4](class_vector4.md#class-vector4) for more details). The size of the new array will be `byte_array.size() / (16 or 32)`. If the original data can't be converted to [Vector4](class_vector4.md#class-vector4) variants, the resulting data is undefined.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: PackedByteArray)

Returns `true` if contents of the arrays differ.

---

PackedByteArray **operator +**(right: PackedByteArray)

Returns a new **PackedByteArray** with contents of `right` added at the end of this array. For better performance, consider using append_array() instead.

---

[bool](class_bool.md#class-bool) **operator ==**(right: PackedByteArray)

Returns `true` if contents of both arrays are the same, i.e. they have all equal bytes at the corresponding indices.

---

[int](class_int.md#class-int) **operator []**(index: [int](class_int.md#class-int))

Returns the byte at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

Note that the byte is returned as a 64-bit [int](class_int.md#class-int).
