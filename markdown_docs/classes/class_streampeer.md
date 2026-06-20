# StreamPeer

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [StreamPeerBuffer](class_streampeerbuffer.md#class-streampeerbuffer), [StreamPeerExtension](class_streampeerextension.md#class-streampeerextension), [StreamPeerGZIP](class_streampeergzip.md#class-streampeergzip), [StreamPeerSocket](class_streampeersocket.md#class-streampeersocket), [StreamPeerTLS](class_streampeertls.md#class-streampeertls)

Abstract base class for interacting with streams.

## Description

StreamPeer is an abstract base class mostly used for stream-based protocols (such as TCP). It provides an API for sending and receiving data through streams as raw data or strings.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Properties

| [bool](class_bool.md#class-bool)   | big_endian   | `false`   |
|------------------------------------|-------------------------------------------------------|-----------|

## Methods

| [int](class_int.md#class-int)                         | get_8()                                                                                                             |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                         | get_16()                                                                                                           |
| [int](class_int.md#class-int)                         | get_32()                                                                                                           |
| [int](class_int.md#class-int)                         | get_64()                                                                                                           |
| [int](class_int.md#class-int)                         | get_available_bytes()                                                                                 |
| [Array](class_array.md#class-array)                   | get_data(bytes: [int](class_int.md#class-int))                                                                   |
| [float](class_float.md#class-float)                   | get_double()                                                                                                   |
| [float](class_float.md#class-float)                   | get_float()                                                                                                     |
| [float](class_float.md#class-float)                   | get_half()                                                                                                       |
| [Array](class_array.md#class-array)                   | get_partial_data(bytes: [int](class_int.md#class-int))                                                   |
| [String](class_string.md#class-string)                | get_string(bytes: [int](class_int.md#class-int) = -1)                                                          |
| [int](class_int.md#class-int)                         | get_u8()                                                                                                           |
| [int](class_int.md#class-int)                         | get_u16()                                                                                                         |
| [int](class_int.md#class-int)                         | get_u32()                                                                                                         |
| [int](class_int.md#class-int)                         | get_u64()                                                                                                         |
| [String](class_string.md#class-string)                | get_utf8_string(bytes: [int](class_int.md#class-int) = -1)                                                |
| [Variant](class_variant.md#class-variant)             | get_var(allow_objects: [bool](class_bool.md#class-bool) = false)                                                  |
|                                                       | put_8(value: [int](class_int.md#class-int))                                                                         |
|                                                       | put_16(value: [int](class_int.md#class-int))                                                                       |
|                                                       | put_32(value: [int](class_int.md#class-int))                                                                       |
|                                                       | put_64(value: [int](class_int.md#class-int))                                                                       |
| [Error](class_@globalscope.md#enum-globalscope-error) | put_data(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                |
|                                                       | put_double(value: [float](class_float.md#class-float))                                                         |
|                                                       | put_float(value: [float](class_float.md#class-float))                                                           |
|                                                       | put_half(value: [float](class_float.md#class-float))                                                             |
| [Array](class_array.md#class-array)                   | put_partial_data(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                |
|                                                       | put_string(value: [String](class_string.md#class-string))                                                      |
|                                                       | put_u8(value: [int](class_int.md#class-int))                                                                       |
|                                                       | put_u16(value: [int](class_int.md#class-int))                                                                     |
|                                                       | put_u32(value: [int](class_int.md#class-int))                                                                     |
|                                                       | put_u64(value: [int](class_int.md#class-int))                                                                     |
|                                                       | put_utf8_string(value: [String](class_string.md#class-string))                                            |
|                                                       | put_var(value: [Variant](class_variant.md#class-variant), full_objects: [bool](class_bool.md#class-bool) = false) |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **big_endian** = `false`

-  **set_big_endian**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_big_endian_enabled**()

If `true`, this **StreamPeer** will using big-endian format for encoding and decoding.

---

## Method Descriptions

[int](class_int.md#class-int) **get_8**()

Gets a signed byte from the stream.

---

[int](class_int.md#class-int) **get_16**()

Gets a signed 16-bit value from the stream.

---

[int](class_int.md#class-int) **get_32**()

Gets a signed 32-bit value from the stream.

---

[int](class_int.md#class-int) **get_64**()

Gets a signed 64-bit value from the stream.

---

[int](class_int.md#class-int) **get_available_bytes**()

Returns the number of bytes this **StreamPeer** has available.

---

[Array](class_array.md#class-array) **get_data**(bytes: [int](class_int.md#class-int))

Returns a chunk data with the received bytes, as an [Array](class_array.md#class-array) containing two elements: an [Error](class_@globalscope.md#enum-globalscope-error) constant and a [PackedByteArray](class_packedbytearray.md#class-packedbytearray). `bytes` is the number of bytes to be received. If not enough bytes are available, the function will block until the desired amount is received.

---

[float](class_float.md#class-float) **get_double**()

Gets a double-precision float from the stream.

---

[float](class_float.md#class-float) **get_float**()

Gets a single-precision float from the stream.

---

[float](class_float.md#class-float) **get_half**()

Gets a half-precision float from the stream.

---

[Array](class_array.md#class-array) **get_partial_data**(bytes: [int](class_int.md#class-int))

Returns a chunk data with the received bytes, as an [Array](class_array.md#class-array) containing two elements: an [Error](class_@globalscope.md#enum-globalscope-error) constant and a [PackedByteArray](class_packedbytearray.md#class-packedbytearray). `bytes` is the number of bytes to be received. If not enough bytes are available, the function will return how many were actually received.

---

[String](class_string.md#class-string) **get_string**(bytes: [int](class_int.md#class-int) = -1)

Gets an ASCII string with byte-length `bytes` from the stream. If `bytes` is negative (default) the length will be read from the stream using the reverse process of put_string().

---

[int](class_int.md#class-int) **get_u8**()

Gets an unsigned byte from the stream.

---

[int](class_int.md#class-int) **get_u16**()

Gets an unsigned 16-bit value from the stream.

---

[int](class_int.md#class-int) **get_u32**()

Gets an unsigned 32-bit value from the stream.

---

[int](class_int.md#class-int) **get_u64**()

Gets an unsigned 64-bit value from the stream.

---

[String](class_string.md#class-string) **get_utf8_string**(bytes: [int](class_int.md#class-int) = -1)

Gets a UTF-8 string with byte-length `bytes` from the stream (this decodes the string sent as UTF-8). If `bytes` is negative (default) the length will be read from the stream using the reverse process of put_utf8_string().

---

[Variant](class_variant.md#class-variant) **get_var**(allow_objects: [bool](class_bool.md#class-bool) = false)

Gets a Variant from the stream. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the [@GlobalScope.bytes_to_var()](class_@globalscope.md#class-globalscope-method-bytes-to-var) method.

**Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.

---

 **put_8**(value: [int](class_int.md#class-int))

Puts a signed byte into the stream.

---

 **put_16**(value: [int](class_int.md#class-int))

Puts a signed 16-bit value into the stream.

---

 **put_32**(value: [int](class_int.md#class-int))

Puts a signed 32-bit value into the stream.

---

 **put_64**(value: [int](class_int.md#class-int))

Puts a signed 64-bit value into the stream.

---

[Error](class_@globalscope.md#enum-globalscope-error) **put_data**(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Sends a chunk of data through the connection, blocking if necessary until the data is done sending. This function returns an [Error](class_@globalscope.md#enum-globalscope-error) code.

---

 **put_double**(value: [float](class_float.md#class-float))

Puts a double-precision float into the stream.

---

 **put_float**(value: [float](class_float.md#class-float))

Puts a single-precision float into the stream.

---

 **put_half**(value: [float](class_float.md#class-float))

Puts a half-precision float into the stream.

---

[Array](class_array.md#class-array) **put_partial_data**(data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Sends a chunk of data through the connection. If all the data could not be sent at once, only part of it will. This function returns two values, an [Error](class_@globalscope.md#enum-globalscope-error) code and an integer, describing how much data was actually sent.

---

 **put_string**(value: [String](class_string.md#class-string))

Puts a zero-terminated ASCII string into the stream prepended by a 32-bit unsigned integer representing its size.

**Note:** To put an ASCII string without prepending its size, you can use put_data():

GDScript

```gdscript
put_data("Hello world".to_ascii_buffer())
```

C#

```csharp
PutData("Hello World".ToAsciiBuffer());
```

---

 **put_u8**(value: [int](class_int.md#class-int))

Puts an unsigned byte into the stream.

---

 **put_u16**(value: [int](class_int.md#class-int))

Puts an unsigned 16-bit value into the stream.

---

 **put_u32**(value: [int](class_int.md#class-int))

Puts an unsigned 32-bit value into the stream.

---

 **put_u64**(value: [int](class_int.md#class-int))

Puts an unsigned 64-bit value into the stream.

---

 **put_utf8_string**(value: [String](class_string.md#class-string))

Puts a zero-terminated UTF-8 string into the stream prepended by a 32 bits unsigned integer representing its size.

**Note:** To put a UTF-8 string without prepending its size, you can use put_data():

GDScript

```gdscript
put_data("Hello world".to_utf8_buffer())
```

C#

```csharp
PutData("Hello World".ToUtf8Buffer());
```

---

 **put_var**(value: [Variant](class_variant.md#class-variant), full_objects: [bool](class_bool.md#class-bool) = false)

Puts a Variant into the stream. If `full_objects` is `true` encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the [@GlobalScope.var_to_bytes()](class_@globalscope.md#class-globalscope-method-var-to-bytes) method.
