# AudioStreamPlayer

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node for audio playback.

## Description

The **AudioStreamPlayer** node plays an audio stream non-positionally. It is ideal for user interfaces, menus, or background music.

To use this node, stream needs to be set to a valid [AudioStream](class_audiostream.md#class-audiostream) resource. Playing more than one sound at the same time is also supported, see max_polyphony.

If you need to play audio at a specific position, use [AudioStreamPlayer2D](class_audiostreamplayer2d.md#class-audiostreamplayer2d) or [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d) instead.

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)
- [Audio Device Changer Demo](https://godotengine.org/asset-library/asset/2758)
- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

## Properties

| [bool](class_bool.md#class-bool)                                   | autoplay           | `false`     |
|--------------------------------------------------------------------|------------------------------------------------------------------|-------------|
| [StringName](class_stringname.md#class-stringname)                 | bus                     | `&"Master"` |
| [int](class_int.md#class-int)                                      | max_polyphony | `1`         |
| MixTarget                     | mix_target       | `0`         |
| [float](class_float.md#class-float)                                | pitch_scale     | `1.0`       |
| [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) | playback_type | `0`         |
| [bool](class_bool.md#class-bool)                                   | playing             | `false`     |
| [AudioStream](class_audiostream.md#class-audiostream)              | stream               |             |
| [bool](class_bool.md#class-bool)                                   | stream_paused | `false`     |
| [float](class_float.md#class-float)                                | volume_db         | `0.0`       |
| [float](class_float.md#class-float)                                | volume_linear |             |

## Methods

| [float](class_float.md#class-float)                                           | get_playback_position()                       |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) | get_stream_playback()                           |
| [bool](class_bool.md#class-bool)                                              | has_stream_playback()                           |
|                                                                               | play(from_position: [float](class_float.md#class-float) = 0.0) |
|                                                                               | seek(to_position: [float](class_float.md#class-float))         |
|                                                                               | stop()                                                         |

---

## Signals

**finished**()

Emitted when a sound finishes playing without interruptions. This signal is *not* emitted when calling stop(), or when exiting the tree while sounds are playing.

---

## Enumerations

enum **MixTarget**:

MixTarget **MIX_TARGET_STEREO** = `0`

The audio will be played only on the first channel. This is the default.

MixTarget **MIX_TARGET_SURROUND** = `1`

The audio will be played on all surround channels.

MixTarget **MIX_TARGET_CENTER** = `2`

The audio will be played on the second channel, which is usually the center.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **autoplay** = `false`

-  **set_autoplay**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_autoplay_enabled**()

If `true`, this node calls play() when entering the tree.

---

[StringName](class_stringname.md#class-stringname) **bus** = `&"Master"`

-  **set_bus**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_bus**()

The target bus name. All sounds from this node will be playing on this bus.

**Note:** At runtime, if no bus with the given name exists, all sounds will fall back on `"Master"`. See also [AudioServer.get_bus_name()](class_audioserver.md#class-audioserver-method-get-bus-name).

---

[int](class_int.md#class-int) **max_polyphony** = `1`

-  **set_max_polyphony**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_polyphony**()

The maximum number of sounds this node can play at the same time. Calling play() after this value is reached will cut off the oldest sounds.

---

MixTarget **mix_target** = `0`

-  **set_mix_target**(value: MixTarget)
- MixTarget **get_mix_target**()

The mix target channels. Has no effect when two speakers or less are detected (see [SpeakerMode](class_audioserver.md#enum-audioserver-speakermode)).

---

[float](class_float.md#class-float) **pitch_scale** = `1.0`

-  **set_pitch_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pitch_scale**()

The audio's pitch and tempo, as a multiplier of the stream's sample rate. A value of `2.0` doubles the audio's pitch, while a value of `0.5` halves the pitch.

---

[PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) **playback_type** = `0`

-  **set_playback_type**(value: [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype))
- [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) **get_playback_type**()

**Experimental:** This property may be changed or removed in future versions.

The playback type of the stream player. If set other than to the default value, it will force that playback type.

---

[bool](class_bool.md#class-bool) **playing** = `false`

-  **set_playing**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_playing**()

If `true`, this node is playing sounds. Setting this property has the same effect as play() and stop().

---

[AudioStream](class_audiostream.md#class-audiostream) **stream**

-  **set_stream**(value: [AudioStream](class_audiostream.md#class-audiostream))
- [AudioStream](class_audiostream.md#class-audiostream) **get_stream**()

The [AudioStream](class_audiostream.md#class-audiostream) resource to be played. Setting this property stops all currently playing sounds. If left empty, the **AudioStreamPlayer** does not work.

---

[bool](class_bool.md#class-bool) **stream_paused** = `false`

-  **set_stream_paused**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_stream_paused**()

If `true`, the sounds are paused. Setting stream_paused to `false` resumes all sounds.

**Note:** This property is automatically changed when exiting or entering the tree, or this node is paused (see [Node.process_mode](class_node.md#class-node-property-process-mode)).

---

[float](class_float.md#class-float) **volume_db** = `0.0`

-  **set_volume_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_db**()

Volume of sound, in decibels. This is an offset of the stream's volume.

**Note:** To convert between decibel and linear energy (like most volume sliders do), use volume_linear, or [@GlobalScope.db_to_linear()](class_@globalscope.md#class-globalscope-method-db-to-linear) and [@GlobalScope.linear_to_db()](class_@globalscope.md#class-globalscope-method-linear-to-db).

---

[float](class_float.md#class-float) **volume_linear**

-  **set_volume_linear**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_linear**()

Volume of sound, as a linear value.

**Note:** This member modifies volume_db for convenience. The returned value is equivalent to the result of [@GlobalScope.db_to_linear()](class_@globalscope.md#class-globalscope-method-db-to-linear) on volume_db. Setting this member is equivalent to setting volume_db to the result of [@GlobalScope.linear_to_db()](class_@globalscope.md#class-globalscope-method-linear-to-db) on a value.

---

## Method Descriptions

[float](class_float.md#class-float) **get_playback_position**()

Returns the position in the [AudioStream](class_audiostream.md#class-audiostream) of the latest sound, in seconds. Returns `0.0` if no sounds are playing.

**Note:** The position is not always accurate, as the [AudioServer](class_audioserver.md#class-audioserver) does not mix audio every processed frame. To get more accurate results, add [AudioServer.get_time_since_last_mix()](class_audioserver.md#class-audioserver-method-get-time-since-last-mix) to the returned position.

**Note:** This method always returns `0.0` if the stream is an [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive), since it can have multiple clips playing at once.

---

[AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **get_stream_playback**()

Returns the latest [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) of this node, usually the most recently created by play(). If no sounds are playing, this method fails and returns an empty playback.

---

[bool](class_bool.md#class-bool) **has_stream_playback**()

Returns `true` if any sound is active, even if stream_paused is set to `true`. See also playing and get_stream_playback().

---

 **play**(from_position: [float](class_float.md#class-float) = 0.0)

Plays a sound from the beginning, or the given `from_position` in seconds.

---

 **seek**(to_position: [float](class_float.md#class-float))

Restarts all sounds to be played from the given `to_position`, in seconds. Does nothing if no sounds are playing.

---

 **stop**()

Stops all sounds from this node.
