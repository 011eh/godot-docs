# AudioStreamPlaylist

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

[AudioStream](class_audiostream.md#class-audiostream) that includes sub-streams and plays them back like a playlist.

## Description

An audio stream that can play back sub-streams in sequence. Streams can be added to the Playlist with set_list_stream(), and shuffled with shuffle.

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

## Properties

| [float](class_float.md#class-float)   | fade_time       | `0.3`   |
|---------------------------------------|------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)      | loop                 | `true`  |
| [bool](class_bool.md#class-bool)      | shuffle           | `false` |
| [int](class_int.md#class-int)         | stream_count | `0`     |

## Methods

| [float](class_float.md#class-float)                   | get_bpm()                                                                                                                                 |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AudioStream](class_audiostream.md#class-audiostream) | get_list_stream(stream_index: [int](class_int.md#class-int))                                                                      |
|                                                       | set_list_stream(stream_index: [int](class_int.md#class-int), audio_stream: [AudioStream](class_audiostream.md#class-audiostream)) |

---

## Constants

**MAX_STREAMS** = `64`

Maximum amount of streams supported in the playlist.

---

## Property Descriptions

[float](class_float.md#class-float) **fade_time** = `0.3`

-  **set_fade_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fade_time**()

Fade time used when a stream ends, when going to the next one. Streams are expected to have an extra bit of audio after the end to help with fading.

---

[bool](class_bool.md#class-bool) **loop** = `true`

-  **set_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_loop**()

If `true`, the playlist will loop, otherwise the playlist will end when the last stream is finished.

---

[bool](class_bool.md#class-bool) **shuffle** = `false`

-  **set_shuffle**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_shuffle**()

If `true`, the playlist will shuffle each time playback starts and each time it loops.

---

[int](class_int.md#class-int) **stream_count** = `0`

-  **set_stream_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_stream_count**()

Amount of streams in the playlist.

---

## Method Descriptions

[float](class_float.md#class-float) **get_bpm**()

Returns the BPM of the playlist, which can vary depending on the clip being played.

---

[AudioStream](class_audiostream.md#class-audiostream) **get_list_stream**(stream_index: [int](class_int.md#class-int))

Returns the stream at playback position index.

---

 **set_list_stream**(stream_index: [int](class_int.md#class-int), audio_stream: [AudioStream](class_audiostream.md#class-audiostream))

Sets the stream at playback position index.
