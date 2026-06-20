# AudioStreamPlayback

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioStreamPlaybackInteractive](class_audiostreamplaybackinteractive.md#class-audiostreamplaybackinteractive), [AudioStreamPlaybackPlaylist](class_audiostreamplaybackplaylist.md#class-audiostreamplaybackplaylist), [AudioStreamPlaybackPolyphonic](class_audiostreamplaybackpolyphonic.md#class-audiostreamplaybackpolyphonic), [AudioStreamPlaybackResampled](class_audiostreamplaybackresampled.md#class-audiostreamplaybackresampled), [AudioStreamPlaybackSynchronized](class_audiostreamplaybacksynchronized.md#class-audiostreamplaybacksynchronized)

Meta class for playing back audio.

## Description

Can play, loop, pause a scroll through audio. See [AudioStream](class_audiostream.md#class-audiostream) and [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis) for usage.

## Tutorials

- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)

## Methods

| [int](class_int.md#class-int)                                                 | \_get_loop_count()                                                                                                         |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Variant](class_variant.md#class-variant)                                     | \_get_parameter(name: [StringName](class_stringname.md#class-stringname))                                                   |
| [float](class_float.md#class-float)                                           | \_get_playback_position()                                                                                           |
| [bool](class_bool.md#class-bool)                                              | \_is_playing()                                                                                                                 |
| [int](class_int.md#class-int)                                                 | \_mix(buffer: `AudioFrame*`, rate_scale: [float](class_float.md#class-float), frames: [int](class_int.md#class-int))                  |
|                                                                               | \_seek(position: [float](class_float.md#class-float))                                                                                |
|                                                                               | \_set_parameter(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) |
|                                                                               | \_start(from_pos: [float](class_float.md#class-float))                                                                              |
|                                                                               | \_stop()                                                                                                                             |
|                                                                               | \_tag_used_streams()                                                                                                     |
| [int](class_int.md#class-int)                                                 | get_loop_count()                                                                                                                   |
| [float](class_float.md#class-float)                                           | get_playback_position()                                                                                                     |
| [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback) | get_sample_playback()                                                                                                         |
| [bool](class_bool.md#class-bool)                                              | is_playing()                                                                                                                           |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)    | mix_audio(rate_scale: [float](class_float.md#class-float), frames: [int](class_int.md#class-int))                                       |
|                                                                               | seek(time: [float](class_float.md#class-float) = 0.0)                                                                                        |
|                                                                               | set_sample_playback(playback_sample: [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback))           |
|                                                                               | start(from_pos: [float](class_float.md#class-float) = 0.0)                                                                                  |
|                                                                               | stop()                                                                                                                                       |

---

## Method Descriptions

[int](class_int.md#class-int) **\_get_loop_count**()

Overridable method. Should return how many times this audio stream has looped. Most built-in playbacks always return `0`.

---

[Variant](class_variant.md#class-variant) **\_get_parameter**(name: [StringName](class_stringname.md#class-stringname))

Return the current value of a playback parameter by name (see [AudioStream._get_parameter_list()](class_audiostream.md#class-audiostream-private-method-get-parameter-list)).

---

[float](class_float.md#class-float) **\_get_playback_position**()

Overridable method. Should return the current progress along the audio stream, in seconds.

---

[bool](class_bool.md#class-bool) **\_is_playing**()

Overridable method. Should return `true` if this playback is active and playing its audio stream.

---

[int](class_int.md#class-int) **\_mix**(buffer: `AudioFrame*`, rate_scale: [float](class_float.md#class-float), frames: [int](class_int.md#class-int))

Override this method to customize how the audio stream is mixed. This method is called even if the playback is not active.

**Note:** It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.

---

 **\_seek**(position: [float](class_float.md#class-float))

Override this method to customize what happens when seeking this audio stream at the given `position`, such as by calling [AudioStreamPlayer.seek()](class_audiostreamplayer.md#class-audiostreamplayer-method-seek).

---

 **\_set_parameter**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Set the current value of a playback parameter by name (see [AudioStream._get_parameter_list()](class_audiostream.md#class-audiostream-private-method-get-parameter-list)).

---

 **\_start**(from_pos: [float](class_float.md#class-float))

Override this method to customize what happens when the playback starts at the given position, such as by calling [AudioStreamPlayer.play()](class_audiostreamplayer.md#class-audiostreamplayer-method-play).

---

 **\_stop**()

Override this method to customize what happens when the playback is stopped, such as by calling [AudioStreamPlayer.stop()](class_audiostreamplayer.md#class-audiostreamplayer-method-stop).

---

 **\_tag_used_streams**()

Overridable method. Called whenever the audio stream is mixed if the playback is active and [AudioServer.set_enable_tagging_used_audio_streams()](class_audioserver.md#class-audioserver-method-set-enable-tagging-used-audio-streams) has been set to `true`. Editor plugins may use this method to "tag" the current position along the audio stream and display it in a preview.

---

[int](class_int.md#class-int) **get_loop_count**()

Returns the number of times the stream has looped.

---

[float](class_float.md#class-float) **get_playback_position**()

Returns the current position in the stream, in seconds.

---

[AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback) **get_sample_playback**()

**Experimental:** This method may be changed or removed in future versions.

Returns the [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback) associated with this **AudioStreamPlayback** for playing back the audio sample of this stream.

---

[bool](class_bool.md#class-bool) **is_playing**()

Returns `true` if the stream is playing.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **mix_audio**(rate_scale: [float](class_float.md#class-float), frames: [int](class_int.md#class-int))

Mixes up to `frames` of audio from the stream from the current position, at a rate of `rate_scale`, advancing the stream.

Returns a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) where each element holds the left and right channel volume levels of each frame.

**Note:** Can return fewer frames than requested, make sure to use the size of the return value.

---

 **seek**(time: [float](class_float.md#class-float) = 0.0)

Seeks the stream at the given `time`, in seconds.

---

 **set_sample_playback**(playback_sample: [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback))

**Experimental:** This method may be changed or removed in future versions.

Associates [AudioSamplePlayback](class_audiosampleplayback.md#class-audiosampleplayback) to this **AudioStreamPlayback** for playing back the audio sample of this stream.

---

 **start**(from_pos: [float](class_float.md#class-float) = 0.0)

Starts the stream from the given `from_pos`, in seconds.

---

 **stop**()

Stops the stream.
