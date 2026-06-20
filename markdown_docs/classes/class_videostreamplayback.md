# VideoStreamPlayback

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Internal class used by [VideoStream](class_videostream.md#class-videostream) to manage playback state when played from a [VideoStreamPlayer](class_videostreamplayer.md#class-videostreamplayer).

## Description

This class is intended to be overridden by video decoder extensions with custom implementations of [VideoStream](class_videostream.md#class-videostream).

## Methods

| [int](class_int.md#class-int)                   | \_get_channels()                                                                                                                                                                                |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float)             | \_get_length()                                                                                                                                                                                    |
| [int](class_int.md#class-int)                   | \_get_mix_rate()                                                                                                                                                                                |
| [float](class_float.md#class-float)             | \_get_playback_position()                                                                                                                                                              |
| [Texture2D](class_texture2d.md#class-texture2d) | \_get_texture()                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                | \_is_paused()                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                | \_is_playing()                                                                                                                                                                                    |
|                                                 | \_play()                                                                                                                                                                                                |
|                                                 | \_seek(time: [float](class_float.md#class-float))                                                                                                                                                       |
|                                                 | \_set_audio_track(idx: [int](class_int.md#class-int))                                                                                                                                        |
|                                                 | \_set_paused(paused: [bool](class_bool.md#class-bool))                                                                                                                                            |
|                                                 | \_stop()                                                                                                                                                                                                |
|                                                 | \_update(delta: [float](class_float.md#class-float))                                                                                                                                                  |
| [int](class_int.md#class-int)                   | mix_audio(num_frames: [int](class_int.md#class-int), buffer: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) = PackedFloat32Array(), offset: [int](class_int.md#class-int) = 0) |

---

## Method Descriptions

[int](class_int.md#class-int) **\_get_channels**()

Returns the number of audio channels.

---

[float](class_float.md#class-float) **\_get_length**()

Returns the video duration in seconds, if known, or 0 if unknown.

---

[int](class_int.md#class-int) **\_get_mix_rate**()

Returns the audio sample rate used for mixing.

---

[float](class_float.md#class-float) **\_get_playback_position**()

Return the current playback timestamp. Called in response to the [VideoStreamPlayer.stream_position](class_videostreamplayer.md#class-videostreamplayer-property-stream-position) getter.

---

[Texture2D](class_texture2d.md#class-texture2d) **\_get_texture**()

Allocates a [Texture2D](class_texture2d.md#class-texture2d) in which decoded video frames will be drawn.

---

[bool](class_bool.md#class-bool) **\_is_paused**()

Returns the paused status, as set by \_set_paused().

---

[bool](class_bool.md#class-bool) **\_is_playing**()

Returns the playback state, as determined by calls to \_play() and \_stop().

---

 **\_play**()

Called in response to [VideoStreamPlayer.autoplay](class_videostreamplayer.md#class-videostreamplayer-property-autoplay) or [VideoStreamPlayer.play()](class_videostreamplayer.md#class-videostreamplayer-method-play). Note that manual playback may also invoke \_stop() multiple times before this method is called. \_is_playing() should return `true` once playing.

---

 **\_seek**(time: [float](class_float.md#class-float))

Seeks to `time` seconds. Called in response to the [VideoStreamPlayer.stream_position](class_videostreamplayer.md#class-videostreamplayer-property-stream-position) setter.

---

 **\_set_audio_track**(idx: [int](class_int.md#class-int))

Select the audio track `idx`. Called when playback starts, and in response to the [VideoStreamPlayer.audio_track](class_videostreamplayer.md#class-videostreamplayer-property-audio-track) setter.

---

 **\_set_paused**(paused: [bool](class_bool.md#class-bool))

Set the paused status of video playback. \_is_paused() must return `paused`. Called in response to the [VideoStreamPlayer.paused](class_videostreamplayer.md#class-videostreamplayer-property-paused) setter.

---

 **\_stop**()

Stops playback. May be called multiple times before \_play(), or in response to [VideoStreamPlayer.stop()](class_videostreamplayer.md#class-videostreamplayer-method-stop). \_is_playing() should return `false` once stopped.

---

 **\_update**(delta: [float](class_float.md#class-float))

Ticks video playback for `delta` seconds. Called every frame as long as both \_is_paused() and \_is_playing() return `true`.

---

[int](class_int.md#class-int) **mix_audio**(num_frames: [int](class_int.md#class-int), buffer: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) = PackedFloat32Array(), offset: [int](class_int.md#class-int) = 0)

Render `num_frames` audio frames (of \_get_channels() floats each) from `buffer`, starting from index `offset` in the array. Returns the number of audio frames rendered, or -1 on error.
