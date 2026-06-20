# AudioStreamPlayer2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Plays positional sound in 2D space.

## Description

Plays audio that is attenuated with distance to the listener.

By default, audio is heard from the screen center. This can be changed by adding an [AudioListener2D](class_audiolistener2d.md#class-audiolistener2d) node to the scene and enabling it by calling [AudioListener2D.make_current()](class_audiolistener2d.md#class-audiolistener2d-method-make-current) on it.

See also [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) to play a sound non-positionally.

**Note:** Hiding an **AudioStreamPlayer2D** node does not disable its audio output. To temporarily disable an **AudioStreamPlayer2D**'s audio output, set volume_db to a very low value like `-100` (which isn't audible to human hearing).

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

## Properties

| [int](class_int.md#class-int)                                      | area_mask               | `0`         |
|--------------------------------------------------------------------|--------------------------------------------------------------------------|-------------|
| [float](class_float.md#class-float)                                | attenuation           | `1.0`       |
| [bool](class_bool.md#class-bool)                                   | autoplay                 | `false`     |
| [StringName](class_stringname.md#class-stringname)                 | bus                           | `&"Master"` |
| [float](class_float.md#class-float)                                | max_distance         | `2000.0`    |
| [int](class_int.md#class-int)                                      | max_polyphony       | `1`         |
| [float](class_float.md#class-float)                                | panning_strength | `1.0`       |
| [float](class_float.md#class-float)                                | pitch_scale           | `1.0`       |
| [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) | playback_type       | `0`         |
| [bool](class_bool.md#class-bool)                                   | playing                   | `false`     |
| [AudioStream](class_audiostream.md#class-audiostream)              | stream                     |             |
| [bool](class_bool.md#class-bool)                                   | stream_paused       | `false`     |
| [float](class_float.md#class-float)                                | volume_db               | `0.0`       |
| [float](class_float.md#class-float)                                | volume_linear       |             |

## Methods

| [float](class_float.md#class-float)                                           | get_playback_position()                       |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) | get_stream_playback()                           |
| [bool](class_bool.md#class-bool)                                              | has_stream_playback()                           |
|                                                                               | play(from_position: [float](class_float.md#class-float) = 0.0) |
|                                                                               | seek(to_position: [float](class_float.md#class-float))         |
|                                                                               | stop()                                                         |

---

## Signals

**finished**()

Emitted when the audio stops playing.

---

## Property Descriptions

[int](class_int.md#class-int) **area_mask** = `0`

-  **set_area_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_area_mask**()

Determines which [Area2D](class_area2d.md#class-area2d) layers affect the sound for reverb and audio bus effects. Areas can be used to redirect [AudioStream](class_audiostream.md#class-audiostream)s so that they play in a certain audio bus. An example of how you might use this is making a "water" area so that sounds played in the water are redirected through an audio bus to make them sound like they are being played underwater.

---

[float](class_float.md#class-float) **attenuation** = `1.0`

-  **set_attenuation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_attenuation**()

The volume is attenuated over distance with this as an exponent.

---

[bool](class_bool.md#class-bool) **autoplay** = `false`

-  **set_autoplay**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_autoplay_enabled**()

If `true`, audio plays when added to scene tree.

---

[StringName](class_stringname.md#class-stringname) **bus** = `&"Master"`

-  **set_bus**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_bus**()

Bus on which this audio is playing.

**Note:** When setting this property, keep in mind that no validation is performed to see if the given name matches an existing bus. This is because audio bus layouts might be loaded after this property is set. If this given name can't be resolved at runtime, it will fall back to `"Master"`.

---

[float](class_float.md#class-float) **max_distance** = `2000.0`

-  **set_max_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_distance**()

Maximum distance from which audio is still hearable.

---

[int](class_int.md#class-int) **max_polyphony** = `1`

-  **set_max_polyphony**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_polyphony**()

The maximum number of sounds this node can play at the same time. Playing additional sounds after this value is reached will cut off the oldest sounds.

---

[float](class_float.md#class-float) **panning_strength** = `1.0`

-  **set_panning_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_panning_strength**()

Scales the panning strength for this node by multiplying the base [ProjectSettings.audio/general/2d_panning_strength](class_projectsettings.md#class-projectsettings-property-audio-general-2d-panning-strength) with this factor. Higher values will pan audio from left to right more dramatically than lower values.

---

[float](class_float.md#class-float) **pitch_scale** = `1.0`

-  **set_pitch_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pitch_scale**()

The pitch and the tempo of the audio, as a multiplier of the audio sample's sample rate.

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

If `true`, audio is playing or is queued to be played (see play()).

---

[AudioStream](class_audiostream.md#class-audiostream) **stream**

-  **set_stream**(value: [AudioStream](class_audiostream.md#class-audiostream))
- [AudioStream](class_audiostream.md#class-audiostream) **get_stream**()

The [AudioStream](class_audiostream.md#class-audiostream) object to be played.

---

[bool](class_bool.md#class-bool) **stream_paused** = `false`

-  **set_stream_paused**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_stream_paused**()

If `true`, the playback is paused. You can resume it by setting stream_paused to `false`.

---

[float](class_float.md#class-float) **volume_db** = `0.0`

-  **set_volume_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_db**()

Base volume before attenuation, in decibels.

---

[float](class_float.md#class-float) **volume_linear**

-  **set_volume_linear**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_linear**()

Base volume before attenuation, as a linear value.

**Note:** This member modifies volume_db for convenience. The returned value is equivalent to the result of [@GlobalScope.db_to_linear()](class_@globalscope.md#class-globalscope-method-db-to-linear) on volume_db. Setting this member is equivalent to setting volume_db to the result of [@GlobalScope.linear_to_db()](class_@globalscope.md#class-globalscope-method-linear-to-db) on a value.

---

## Method Descriptions

[float](class_float.md#class-float) **get_playback_position**()

Returns the position in the [AudioStream](class_audiostream.md#class-audiostream).

---

[AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **get_stream_playback**()

Returns the [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) object associated with this **AudioStreamPlayer2D**.

---

[bool](class_bool.md#class-bool) **has_stream_playback**()

Returns whether the [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) can return the [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) object or not.

---

 **play**(from_position: [float](class_float.md#class-float) = 0.0)

Queues the audio to play on the next physics frame, from the given position `from_position`, in seconds.

---

 **seek**(to_position: [float](class_float.md#class-float))

Sets the position from which audio will be played, in seconds.

---

 **stop**()

Stops the audio.
