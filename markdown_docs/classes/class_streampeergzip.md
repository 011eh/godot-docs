# StreamPeerGZIP

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A stream peer that handles GZIP and deflate compression/decompression.

## Description

This class allows to compress or decompress data using GZIP/deflate in a streaming fashion. This is particularly useful when compressing or decompressing files that have to be sent through the network without needing to allocate them all in memory.

After starting the stream via start_compression() (or start_decompression()), calling [StreamPeer.put_partial_data()](class_streampeer.md#class-streampeer-method-put-partial-data) on this stream will compress (or decompress) the data, writing it to the internal buffer. Calling [StreamPeer.get_available_bytes()](class_streampeer.md#class-streampeer-method-get-available-bytes) will return the pending bytes in the internal buffer, and [StreamPeer.get_partial_data()](class_streampeer.md#class-streampeer-method-get-partial-data) will retrieve the compressed (or decompressed) bytes from it. When the stream is over, you must call finish() to ensure the internal buffer is properly flushed (make sure to call [StreamPeer.get_available_bytes()](class_streampeer.md#class-streampeer-method-get-available-bytes) on last time to check if more data needs to be read after that).

## Methods

|                                                       | clear()                                                                                                                                      |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error) | finish()                                                                                                                                    |
| [Error](class_@globalscope.md#enum-globalscope-error) | start_compression(use_deflate: [bool](class_bool.md#class-bool) = false, buffer_size: [int](class_int.md#class-int) = 65535)     |
| [Error](class_@globalscope.md#enum-globalscope-error) | start_decompression(use_deflate: [bool](class_bool.md#class-bool) = false, buffer_size: [int](class_int.md#class-int) = 65535) |

---

## Method Descriptions

 **clear**()

Clears this stream, resetting the internal state.

---

[Error](class_@globalscope.md#enum-globalscope-error) **finish**()

Finalizes the stream, compressing any buffered chunk left.

You must call it only when you are compressing.

---

[Error](class_@globalscope.md#enum-globalscope-error) **start_compression**(use_deflate: [bool](class_bool.md#class-bool) = false, buffer_size: [int](class_int.md#class-int) = 65535)

Start the stream in compression mode with the given `buffer_size`, if `use_deflate` is `true` uses deflate instead of GZIP.

---

[Error](class_@globalscope.md#enum-globalscope-error) **start_decompression**(use_deflate: [bool](class_bool.md#class-bool) = false, buffer_size: [int](class_int.md#class-int) = 65535)

Start the stream in decompression mode with the given `buffer_size`, if `use_deflate` is `true` uses deflate instead of GZIP.
