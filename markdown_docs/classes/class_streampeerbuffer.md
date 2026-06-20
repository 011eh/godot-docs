# StreamPeerBuffer

**Inherits:** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A stream peer used to handle binary data streams.

## Description

A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files, [FileAccess](class_fileaccess.md#class-fileaccess) can be used directly.

A **StreamPeerBuffer** object keeps an internal cursor which is the offset in bytes to the start of the buffer. Get and put operations are performed at the cursor position and will move the cursor accordingly.

## Properties

| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)   | data_array   | `PackedByteArray()`   |
|---------------------------------------------------------------------|-------------------------------------------------------------|-----------------------|

## Methods

|                                             | clear()                                      |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| StreamPeerBuffer | duplicate()                              |
| [int](class_int.md#class-int)               | get_position()                        |
| [int](class_int.md#class-int)               | get_size()                                |
|                                             | resize(size: [int](class_int.md#class-int)) |
|                                             | seek(position: [int](class_int.md#class-int)) |

---

## Property Descriptions

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **data_array** = `PackedByteArray()`

-  **set_data_array**(value: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))
- [PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_data_array**()

The underlying data buffer. Setting this value resets the cursor.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class-packedbytearray) for more details.

---

## Method Descriptions

 **clear**()

Clears the data_array and resets the cursor.

---

StreamPeerBuffer **duplicate**()

Returns a new **StreamPeerBuffer** with the same data_array content.

---

[int](class_int.md#class-int) **get_position**()

Returns the current cursor position.

---

[int](class_int.md#class-int) **get_size**()

Returns the size of data_array.

---

 **resize**(size: [int](class_int.md#class-int))

Resizes the data_array. This *doesn't* update the cursor.

---

 **seek**(position: [int](class_int.md#class-int))

Moves the cursor to the specified position. `position` must be a valid index of data_array.
