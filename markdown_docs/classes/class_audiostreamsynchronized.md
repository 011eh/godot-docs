# AudioStreamSynchronized

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Stream that can be fitted with sub-streams, which will be played in-sync.

## Description

This is a stream that can be fitted with sub-streams, which will be played in-sync. The streams begin at exactly the same time when play is pressed, and will end when the last of them ends. If one of the sub-streams loops, then playback will continue.

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

## Properties

| [int](class_int.md#class-int)   | stream_count   | `0`   |
|---------------------------------|------------------------------------------------------------------------|-------|

## Methods

| [AudioStream](class_audiostream.md#class-audiostream)   | get_sync_stream(stream_index: [int](class_int.md#class-int))                                                                      |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float)                     | get_sync_stream_volume(stream_index: [int](class_int.md#class-int))                                                        |
|                                                         | set_sync_stream(stream_index: [int](class_int.md#class-int), audio_stream: [AudioStream](class_audiostream.md#class-audiostream)) |
|                                                         | set_sync_stream_volume(stream_index: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float))        |

---

## Constants

**MAX_STREAMS** = `32`

Maximum amount of streams that can be synchronized.

---

## Property Descriptions

[int](class_int.md#class-int) **stream_count** = `0`

-  **set_stream_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stream_count**()

Set the total amount of streams that will be played back synchronized.

---

## Method Descriptions

[AudioStream](class_audiostream.md#class-audiostream) **get_sync_stream**(stream_index: [int](class_int.md#class-int))

Get one of the synchronized streams, by index.

---

[float](class_float.md#class-float) **get_sync_stream_volume**(stream_index: [int](class_int.md#class-int))

Get the volume of one of the synchronized streams, by index.

---

 **set_sync_stream**(stream_index: [int](class_int.md#class-int), audio_stream: [AudioStream](class_audiostream.md#class-audiostream))

Set one of the synchronized streams, by index.

---

 **set_sync_stream_volume**(stream_index: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float))

Set the volume of one of the synchronized streams, by index.
