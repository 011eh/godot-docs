# AudioStreamPlayer3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Plays positional sound in 3D space.

## Description

Plays audio with positional sound effects, based on the relative position of the audio listener. Positional effects include distance attenuation, directionality, and the Doppler effect. For greater realism, a low-pass filter is applied to distant sounds. This can be disabled by setting attenuation_filter_cutoff_hz to `20500`.

By default, audio is heard from the camera position. This can be changed by adding an [AudioListener3D](class_audiolistener3d.md#class-audiolistener3d) node to the scene and enabling it by calling [AudioListener3D.make_current()](class_audiolistener3d.md#class-audiolistener3d-method-make-current) on it.

See also [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) to play a sound non-positionally.

**Note:** Hiding an **AudioStreamPlayer3D** node does not disable its audio output. To temporarily disable an **AudioStreamPlayer3D**'s audio output, set volume_db to a very low value like `-100` (which isn't audible to human hearing).

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

## Properties

| [int](class_int.md#class-int)                                      | area_mask                                                       | `0`         |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------|
| [float](class_float.md#class-float)                                | attenuation_filter_cutoff_hz                 | `5000.0`    |
| [float](class_float.md#class-float)                                | attenuation_filter_db                               | `-24.0`     |
| AttenuationModel     | attenuation_model                                       | `0`         |
| [bool](class_bool.md#class-bool)                                   | autoplay                                                         | `false`     |
| [StringName](class_stringname.md#class-stringname)                 | bus                                                                   | `&"Master"` |
| DopplerTracking       | doppler_tracking                                         | `0`         |
| [float](class_float.md#class-float)                                | emission_angle_degrees                             | `45.0`      |
| [bool](class_bool.md#class-bool)                                   | emission_angle_enabled                             | `false`     |
| [float](class_float.md#class-float)                                | emission_angle_filter_attenuation_db | `-12.0`     |
| [float](class_float.md#class-float)                                | max_db                                                             | `3.0`       |
| [float](class_float.md#class-float)                                | max_distance                                                 | `0.0`       |
| [int](class_int.md#class-int)                                      | max_polyphony                                               | `1`         |
| [float](class_float.md#class-float)                                | panning_strength                                         | `1.0`       |
| [float](class_float.md#class-float)                                | pitch_scale                                                   | `1.0`       |
| [PlaybackType](class_audioserver.md#enum-audioserver-playbacktype) | playback_type                                               | `0`         |
| [bool](class_bool.md#class-bool)                                   | playing                                                           | `false`     |
| [AudioStream](class_audiostream.md#class-audiostream)              | stream                                                             |             |
| [bool](class_bool.md#class-bool)                                   | stream_paused                                               | `false`     |
| [float](class_float.md#class-float)                                | unit_size                                                       | `10.0`      |
| [float](class_float.md#class-float)                                | volume_db                                                       | `0.0`       |
| [float](class_float.md#class-float)                                | volume_linear                                               |             |

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

## Enumerations

enum **AttenuationModel**:

AttenuationModel **ATTENUATION_INVERSE_DISTANCE** = `0`

Attenuation of loudness according to linear distance.

AttenuationModel **ATTENUATION_INVERSE_SQUARE_DISTANCE** = `1`

Attenuation of loudness according to squared distance.

AttenuationModel **ATTENUATION_LOGARITHMIC** = `2`

Attenuation of loudness according to logarithmic distance.

AttenuationModel **ATTENUATION_DISABLED** = `3`

No attenuation of loudness according to distance. The sound will still be heard positionally, unlike an [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer). ATTENUATION_DISABLED can be combined with a max_distance value greater than `0.0` to achieve linear attenuation clamped to a sphere of a defined size.

---

enum **DopplerTracking**:

DopplerTracking **DOPPLER_TRACKING_DISABLED** = `0`

Disables doppler tracking.

DopplerTracking **DOPPLER_TRACKING_IDLE_STEP** = `1`

Executes doppler tracking during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class-node-constant-notification-internal-process)).

DopplerTracking **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Executes doppler tracking during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class-node-constant-notification-internal-physics-process)).

---

## Property Descriptions

[int](class_int.md#class-int) **area_mask** = `0`

-  **set_area_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_area_mask**()

Determines which [Area3D](class_area3d.md#class-area3d) layers affect the sound for reverb and audio bus effects. Areas can be used to redirect [AudioStream](class_audiostream.md#class-audiostream)s so that they play in a certain audio bus. An example of how you might use this is making a "water" area so that sounds played in the water are redirected through an audio bus to make them sound like they are being played underwater.

---

[float](class_float.md#class-float) **attenuation_filter_cutoff_hz** = `5000.0`

-  **set_attenuation_filter_cutoff_hz**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_attenuation_filter_cutoff_hz**()

The cutoff frequency of the attenuation low-pass filter, in Hz. A sound above this frequency is attenuated more than a sound below this frequency. To disable this effect, set this to `20500` as this frequency is above the human hearing limit.

---

[float](class_float.md#class-float) **attenuation_filter_db** = `-24.0`

-  **set_attenuation_filter_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_attenuation_filter_db**()

Amount how much the filter affects the loudness, in decibels.

---

AttenuationModel **attenuation_model** = `0`

-  **set_attenuation_model**(value: AttenuationModel)
- AttenuationModel **get_attenuation_model**()

Decides if audio should get quieter with distance linearly, quadratically, logarithmically, or not be affected by distance, effectively disabling attenuation.

---

[bool](class_bool.md#class-bool) **autoplay** = `false`

-  **set_autoplay**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_autoplay_enabled**()

If `true`, audio plays when the AudioStreamPlayer3D node is added to scene tree.

---

[StringName](class_stringname.md#class-stringname) **bus** = `&"Master"`

-  **set_bus**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_bus**()

The bus on which this audio is playing.

**Note:** When setting this property, keep in mind that no validation is performed to see if the given name matches an existing bus. This is because audio bus layouts might be loaded after this property is set. If this given name can't be resolved at runtime, it will fall back to `"Master"`.

---

DopplerTracking **doppler_tracking** = `0`

-  **set_doppler_tracking**(value: DopplerTracking)
- DopplerTracking **get_doppler_tracking**()

Decides in which step the Doppler effect should be calculated.

**Note:** If doppler_tracking is not DOPPLER_TRACKING_DISABLED but the current [Camera3D](class_camera3d.md#class-camera3d)/[AudioListener3D](class_audiolistener3d.md#class-audiolistener3d) has doppler tracking disabled, the Doppler effect will be heard but will not take the movement of the current listener into account. If accurate Doppler effect is desired, doppler tracking should be enabled on both the **AudioStreamPlayer3D** and the current [Camera3D](class_camera3d.md#class-camera3d)/[AudioListener3D](class_audiolistener3d.md#class-audiolistener3d).

---

[float](class_float.md#class-float) **emission_angle_degrees** = `45.0`

-  **set_emission_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_angle**()

The angle in which the audio reaches a listener unattenuated.

---

[bool](class_bool.md#class-bool) **emission_angle_enabled** = `false`

-  **set_emission_angle_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_emission_angle_enabled**()

If `true`, the audio should be attenuated according to the direction of the sound.

---

[float](class_float.md#class-float) **emission_angle_filter_attenuation_db** = `-12.0`

-  **set_emission_angle_filter_attenuation_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_emission_angle_filter_attenuation_db**()

Attenuation factor used if listener is outside of emission_angle_degrees and emission_angle_enabled is set, in decibels.

---

[float](class_float.md#class-float) **max_db** = `3.0`

-  **set_max_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_db**()

Sets the absolute maximum of the sound level, in decibels.

---

[float](class_float.md#class-float) **max_distance** = `0.0`

-  **set_max_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_distance**()

The distance past which the sound can no longer be heard at all. Only has an effect if set to a value greater than `0.0`. max_distance works in tandem with unit_size. However, unlike unit_size whose behavior depends on the attenuation_model, max_distance always works in a linear fashion. This can be used to prevent the **AudioStreamPlayer3D** from requiring audio mixing when the listener is far away, which saves CPU resources.

---

[int](class_int.md#class-int) **max_polyphony** = `1`

-  **set_max_polyphony**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_polyphony**()

The maximum number of sounds this node can play at the same time. Playing additional sounds after this value is reached will cut off the oldest sounds.

---

[float](class_float.md#class-float) **panning_strength** = `1.0`

-  **set_panning_strength**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_panning_strength**()

Scales the panning strength for this node by multiplying the base [ProjectSettings.audio/general/3d_panning_strength](class_projectsettings.md#class-projectsettings-property-audio-general-3d-panning-strength) by this factor. If the product is `0.0` then stereo panning is disabled and the volume is the same for all channels. If the product is `1.0` then one of the channels will be muted when the sound is located exactly to the left (or right) of the listener.

Two speaker stereo arrangements implement the [WebAudio standard for StereoPannerNode Panning](https://webaudio.github.io/web-audio-api/#stereopanner-algorithm) where the volume is cosine of half the azimuth angle to the ear.

For other speaker arrangements such as the 5.1 and 7.1 the SPCAP (Speaker-Placement Correction Amplitude) algorithm is implemented.

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

The [AudioStream](class_audiostream.md#class-audiostream) resource to be played.

---

[bool](class_bool.md#class-bool) **stream_paused** = `false`

-  **set_stream_paused**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_stream_paused**()

If `true`, the playback is paused. You can resume it by setting stream_paused to `false`.

---

[float](class_float.md#class-float) **unit_size** = `10.0`

-  **set_unit_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_unit_size**()

The factor for the attenuation effect. Higher values make the sound audible over a larger distance.

---

[float](class_float.md#class-float) **volume_db** = `0.0`

-  **set_volume_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_db**()

The base sound level before attenuation, in decibels.

---

[float](class_float.md#class-float) **volume_linear**

-  **set_volume_linear**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_linear**()

The base sound level before attenuation, as a linear value.

**Note:** This member modifies volume_db for convenience. The returned value is equivalent to the result of [@GlobalScope.db_to_linear()](class_@globalscope.md#class-globalscope-method-db-to-linear) on volume_db. Setting this member is equivalent to setting volume_db to the result of [@GlobalScope.linear_to_db()](class_@globalscope.md#class-globalscope-method-linear-to-db) on a value.

---

## Method Descriptions

[float](class_float.md#class-float) **get_playback_position**()

Returns the position in the [AudioStream](class_audiostream.md#class-audiostream).

---

[AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **get_stream_playback**()

Returns the [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) object associated with this **AudioStreamPlayer3D**.

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
