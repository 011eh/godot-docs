# AudioStreamGeneratorPlayback

**Inherits:** [AudioStreamPlaybackResampled](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled) **<** [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plays back audio generated using [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator).

## Description

This class is meant to be used with [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator) to play back the generated audio in real-time.

## Tutorials

- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)
- [Godot 3.2 will get new audio features](https://godotengine.org/article/godot-32-will-get-new-audio-features)

## Methods

| [bool](class_bool.md#class-bool)   | can_push_buffer(amount: [int](class_int.md#class-int))                                      |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                    | clear_buffer()                                                                                 |
| [int](class_int.md#class-int)      | get_frames_available()                                                                 |
| [int](class_int.md#class-int)      | get_skips()                                                                                       |
| [bool](class_bool.md#class-bool)   | push_buffer(frames: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)) |
| [bool](class_bool.md#class-bool)   | push_frame(frame: [Vector2](class_vector2.md#class-vector2))                                     |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **can_push_buffer**(amount: [int](class_int.md#class-int))

Returns `true` if a buffer of the size `amount` can be pushed to the audio sample data buffer without overflowing it, `false` otherwise.

---

 **clear_buffer**()

Clears the audio sample data buffer.

---

[int](class_int.md#class-int) **get_frames_available**()

Returns the number of frames that can be pushed to the audio sample data buffer without overflowing it. If the result is `0`, the buffer is full.

---

[int](class_int.md#class-int) **get_skips**()

Returns the number of times the playback skipped due to a buffer underrun in the audio sample data. This value is reset at the start of the playback.

---

[bool](class_bool.md#class-bool) **push_buffer**(frames: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))

Pushes several audio data frames to the buffer. This is usually more efficient than push_frame() in C# and compiled languages via GDExtension, but push_buffer() may be *less* efficient in GDScript.

---

[bool](class_bool.md#class-bool) **push_frame**(frame: [Vector2](class_vector2.md#class-vector2))

Pushes a single audio data frame to the buffer. This is usually less efficient than push_buffer() in C# and compiled languages via GDExtension, but push_frame() may be *more* efficient in GDScript.
