# AudioServer

**Inherits:** [Object](class_object.md#class-object)

Server interface for low-level audio access.

## Description

**AudioServer** is a low-level server interface for audio access. It is in charge of creating sample data (playable audio) as well as its playback via a voice interface.

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio Device Changer Demo](https://godotengine.org/asset-library/asset/2758)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

## Properties

| [int](class_int.md#class-int)          | bus_count                       | `1`         |
|----------------------------------------|--------------------------------------------------------------------------|-------------|
| [String](class_string.md#class-string) | input_device                 | `"Default"` |
| [String](class_string.md#class-string) | output_device               | `"Default"` |
| [float](class_float.md#class-float)    | playback_speed_scale | `1.0`       |

## Methods

|                                                                               | add_bus(at_position: [int](class_int.md#class-int) = -1)                                                                                                                      |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                               | add_bus_effect(bus_idx: [int](class_int.md#class-int), effect: [AudioEffect](class_audioeffect.md#class-audioeffect), at_position: [int](class_int.md#class-int) = -1) |
| [AudioBusLayout](class_audiobuslayout.md#class-audiobuslayout)                | generate_bus_layout()                                                                                                                                             |
| [int](class_int.md#class-int)                                                 | get_bus_channels(bus_idx: [int](class_int.md#class-int))                                                                                                             |
| [AudioEffect](class_audioeffect.md#class-audioeffect)                         | get_bus_effect(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int))                                                                      |
| [int](class_int.md#class-int)                                                 | get_bus_effect_count(bus_idx: [int](class_int.md#class-int))                                                                                                     |
| [AudioEffectInstance](class_audioeffectinstance.md#class-audioeffectinstance) | get_bus_effect_instance(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int), channel: [int](class_int.md#class-int) = 0)        |
| [int](class_int.md#class-int)                                                 | get_bus_index(bus_name: [StringName](class_stringname.md#class-stringname))                                                                                             |
| [String](class_string.md#class-string)                                        | get_bus_name(bus_idx: [int](class_int.md#class-int))                                                                                                                     |
| [float](class_float.md#class-float)                                           | get_bus_peak_volume_left_db(bus_idx: [int](class_int.md#class-int), channel: [int](class_int.md#class-int))                                               |
| [float](class_float.md#class-float)                                           | get_bus_peak_volume_right_db(bus_idx: [int](class_int.md#class-int), channel: [int](class_int.md#class-int))                                             |
| [StringName](class_stringname.md#class-stringname)                            | get_bus_send(bus_idx: [int](class_int.md#class-int))                                                                                                                     |
| [float](class_float.md#class-float)                                           | get_bus_volume_db(bus_idx: [int](class_int.md#class-int))                                                                                                           |
| [float](class_float.md#class-float)                                           | get_bus_volume_linear(bus_idx: [int](class_int.md#class-int))                                                                                                   |
| [String](class_string.md#class-string)                                        | get_driver_name()                                                                                                                                                     |
| [int](class_int.md#class-int)                                                 | get_input_buffer_length_frames()                                                                                                                       |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)       | get_input_device_list()                                                                                                                                         |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)    | get_input_frames(frames: [int](class_int.md#class-int))                                                                                                              |
| [int](class_int.md#class-int)                                                 | get_input_frames_available()                                                                                                                               |
| [float](class_float.md#class-float)                                           | get_input_mix_rate()                                                                                                                                               |
| [float](class_float.md#class-float)                                           | get_mix_rate()                                                                                                                                                           |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)       | get_output_device_list()                                                                                                                                       |
| [float](class_float.md#class-float)                                           | get_output_latency()                                                                                                                                               |
| SpeakerMode                                  | get_speaker_mode()                                                                                                                                                   |
| [float](class_float.md#class-float)                                           | get_time_since_last_mix()                                                                                                                                     |
| [float](class_float.md#class-float)                                           | get_time_to_next_mix()                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                              | is_bus_bypassing_effects(bus_idx: [int](class_int.md#class-int))                                                                                             |
| [bool](class_bool.md#class-bool)                                              | is_bus_effect_enabled(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int))                                                        |
| [bool](class_bool.md#class-bool)                                              | is_bus_mute(bus_idx: [int](class_int.md#class-int))                                                                                                                       |
| [bool](class_bool.md#class-bool)                                              | is_bus_solo(bus_idx: [int](class_int.md#class-int))                                                                                                                       |
| [bool](class_bool.md#class-bool)                                              | is_stream_registered_as_sample(stream: [AudioStream](class_audiostream.md#class-audiostream))                                                          |
|                                                                               | lock()                                                                                                                                                                           |
|                                                                               | move_bus(index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int))                                                                                      |
|                                                                               | register_stream_as_sample(stream: [AudioStream](class_audiostream.md#class-audiostream))                                                                    |
|                                                                               | remove_bus(index: [int](class_int.md#class-int))                                                                                                                           |
|                                                                               | remove_bus_effect(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int))                                                                |
|                                                                               | set_bus_bypass_effects(bus_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                       |
|                                                                               | set_bus_effect_enabled(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))           |
|                                                                               | set_bus_layout(bus_layout: [AudioBusLayout](class_audiobuslayout.md#class-audiobuslayout))                                                                             |
|                                                                               | set_bus_mute(bus_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                           |
|                                                                               | set_bus_name(bus_idx: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                       |
|                                                                               | set_bus_send(bus_idx: [int](class_int.md#class-int), send: [StringName](class_stringname.md#class-stringname))                                                           |
|                                                                               | set_bus_solo(bus_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                           |
|                                                                               | set_bus_volume_db(bus_idx: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float))                                                           |
|                                                                               | set_bus_volume_linear(bus_idx: [int](class_int.md#class-int), volume_linear: [float](class_float.md#class-float))                                               |
|                                                                               | set_enable_tagging_used_audio_streams(enable: [bool](class_bool.md#class-bool))                                                                 |
| [Error](class_@globalscope.md#enum-globalscope-error)                         | set_input_device_active(active: [bool](class_bool.md#class-bool))                                                                                             |
|                                                                               | swap_bus_effects(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int), by_effect_idx: [int](class_int.md#class-int))                    |
|                                                                               | unlock()                                                                                                                                                                       |

---

## Signals

**bus_layout_changed**()

Emitted when an audio bus is added, deleted, or moved.

---

**bus_renamed**(bus_index: [int](class_int.md#class-int), old_name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname))

Emitted when the audio bus at `bus_index` is renamed from `old_name` to `new_name`.

---

## Enumerations

enum **SpeakerMode**:

SpeakerMode **SPEAKER_MODE_STEREO** = `0`

Two or fewer speakers were detected.

SpeakerMode **SPEAKER_SURROUND_31** = `1`

A 3.1 channel surround setup was detected.

SpeakerMode **SPEAKER_SURROUND_51** = `2`

A 5.1 channel surround setup was detected.

SpeakerMode **SPEAKER_SURROUND_71** = `3`

A 7.1 channel surround setup was detected.

---

enum **PlaybackType**:

PlaybackType **PLAYBACK_TYPE_DEFAULT** = `0`

**Experimental:** This constant may be changed or removed in future versions.

The playback will be considered of the type declared at [ProjectSettings.audio/general/default_playback_type](class_projectsettings.md#class-projectsettings-property-audio-general-default-playback-type).

PlaybackType **PLAYBACK_TYPE_STREAM** = `1`

**Experimental:** This constant may be changed or removed in future versions.

Force the playback to be considered as a stream.

PlaybackType **PLAYBACK_TYPE_SAMPLE** = `2`

**Experimental:** This constant may be changed or removed in future versions.

Force the playback to be considered as a sample. This can provide lower latency and more stable playback (with less risk of audio crackling), at the cost of having less flexibility.

**Note:** Only currently supported on the web platform.

**Note:** [AudioEffect](class_audioeffect.md#class-audioeffect)s are not supported when playback is considered as a sample.

PlaybackType **PLAYBACK_TYPE_MAX** = `3`

**Experimental:** This constant may be changed or removed in future versions.

Represents the size of the PlaybackType enum.

---

## Property Descriptions

[int](class_int.md#class-int) **bus_count** = `1`

-  **set_bus_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bus_count**()

Number of available audio buses.

---

[String](class_string.md#class-string) **input_device** = `"Default"`

-  **set_input_device**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_input_device**()

Name of the current device for audio input (see get_input_device_list()). On systems with multiple audio inputs (such as analog, USB and HDMI audio), this can be used to select the audio input device. The value `"Default"` will record audio on the system-wide default audio input. If an invalid device name is set, the value will be reverted back to `"Default"`.

**Note:** [ProjectSettings.audio/driver/enable_input](class_projectsettings.md#class-projectsettings-property-audio-driver-enable-input) must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

---

[String](class_string.md#class-string) **output_device** = `"Default"`

-  **set_output_device**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_output_device**()

Name of the current device for audio output (see get_output_device_list()). On systems with multiple audio outputs (such as analog, USB and HDMI audio), this can be used to select the audio output device. The value `"Default"` will play audio on the system-wide default audio output. If an invalid device name is set, the value will be reverted back to `"Default"`.

---

[float](class_float.md#class-float) **playback_speed_scale** = `1.0`

-  **set_playback_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_playback_speed_scale**()

Scales the rate at which audio is played (i.e. setting it to `0.5` will make the audio be played at half its speed). See also [Engine.time_scale](class_engine.md#class-engine-property-time-scale) to affect the general simulation speed, which is independent from playback_speed_scale.

---

## Method Descriptions

 **add_bus**(at_position: [int](class_int.md#class-int) = -1)

Adds a bus at `at_position`.

---

 **add_bus_effect**(bus_idx: [int](class_int.md#class-int), effect: [AudioEffect](class_audioeffect.md#class-audioeffect), at_position: [int](class_int.md#class-int) = -1)

Adds an [AudioEffect](class_audioeffect.md#class-audioeffect) effect to the bus `bus_idx` at `at_position`.

---

[AudioBusLayout](class_audiobuslayout.md#class-audiobuslayout) **generate_bus_layout**()

Generates an [AudioBusLayout](class_audiobuslayout.md#class-audiobuslayout) using the available buses and effects.

---

[int](class_int.md#class-int) **get_bus_channels**(bus_idx: [int](class_int.md#class-int))

Returns the number of channels of the bus at index `bus_idx`.

---

[AudioEffect](class_audioeffect.md#class-audioeffect) **get_bus_effect**(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int))

Returns the [AudioEffect](class_audioeffect.md#class-audioeffect) at position `effect_idx` in bus `bus_idx`.

---

[int](class_int.md#class-int) **get_bus_effect_count**(bus_idx: [int](class_int.md#class-int))

Returns the number of effects on the bus at `bus_idx`.

---

[AudioEffectInstance](class_audioeffectinstance.md#class-audioeffectinstance) **get_bus_effect_instance**(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int), channel: [int](class_int.md#class-int) = 0)

Returns the [AudioEffectInstance](class_audioeffectinstance.md#class-audioeffectinstance) assigned to the given bus and effect indices (and optionally channel).

---

[int](class_int.md#class-int) **get_bus_index**(bus_name: [StringName](class_stringname.md#class-stringname))

Returns the index of the bus with the name `bus_name`. Returns `-1` if no bus with the specified name exist.

---

[String](class_string.md#class-string) **get_bus_name**(bus_idx: [int](class_int.md#class-int))

Returns the name of the bus with the index `bus_idx`.

---

[float](class_float.md#class-float) **get_bus_peak_volume_left_db**(bus_idx: [int](class_int.md#class-int), channel: [int](class_int.md#class-int))

Returns the peak volume of the left speaker at bus index `bus_idx` and channel index `channel`.

---

[float](class_float.md#class-float) **get_bus_peak_volume_right_db**(bus_idx: [int](class_int.md#class-int), channel: [int](class_int.md#class-int))

Returns the peak volume of the right speaker at bus index `bus_idx` and channel index `channel`.

---

[StringName](class_stringname.md#class-stringname) **get_bus_send**(bus_idx: [int](class_int.md#class-int))

Returns the name of the bus that the bus at index `bus_idx` sends to.

---

[float](class_float.md#class-float) **get_bus_volume_db**(bus_idx: [int](class_int.md#class-int))

Returns the volume of the bus at index `bus_idx` in dB.

---

[float](class_float.md#class-float) **get_bus_volume_linear**(bus_idx: [int](class_int.md#class-int))

Returns the volume of the bus at index `bus_idx` as a linear value.

**Note:** The returned value is equivalent to the result of [@GlobalScope.db_to_linear()](class_@globalscope.md#class-globalscope-method-db-to-linear) on the result of get_bus_volume_db().

---

[String](class_string.md#class-string) **get_driver_name**()

Returns the name of the current audio driver. The default usually depends on the operating system, but may be overridden via the `--audio-driver` [command line argument](../tutorials/editor/command_line_tutorial.md). `--headless` also automatically sets the audio driver to `Dummy`. See also [ProjectSettings.audio/driver/driver](class_projectsettings.md#class-projectsettings-property-audio-driver-driver).

---

[int](class_int.md#class-int) **get_input_buffer_length_frames**()

**Experimental:** This method may be changed or removed in future versions.

Returns the absolute size of the microphone input buffer. This is set to a multiple of the audio latency and can be used to estimate the minimum rate at which the frames need to be fetched.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_input_device_list**()

Returns the names of all audio input devices detected on the system.

**Note:** [ProjectSettings.audio/driver/enable_input](class_projectsettings.md#class-projectsettings-property-audio-driver-enable-input) must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_input_frames**(frames: [int](class_int.md#class-int))

**Experimental:** This method may be changed or removed in future versions.

Returns a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) containing exactly `frames` audio samples from the internal microphone buffer if available, otherwise returns an empty [PackedVector2Array](class_packedvector2array.md#class-packedvector2array).

The buffer is filled at the rate of get_input_mix_rate() frames per second when set_input_device_active() has successfully been set to `true`.

The samples are signed floating-point PCM values between `-1` and `1`.

---

[int](class_int.md#class-int) **get_input_frames_available**()

**Experimental:** This method may be changed or removed in future versions.

Returns the number of frames available to read using get_input_frames().

---

[float](class_float.md#class-float) **get_input_mix_rate**()

Returns the sample rate at the input of the **AudioServer**.

---

[float](class_float.md#class-float) **get_mix_rate**()

Returns the sample rate at the output of the **AudioServer**.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_output_device_list**()

Returns the names of all audio output devices detected on the system.

---

[float](class_float.md#class-float) **get_output_latency**()

Returns the audio driver's effective output latency. This is based on [ProjectSettings.audio/driver/output_latency](class_projectsettings.md#class-projectsettings-property-audio-driver-output-latency), but the exact returned value will differ depending on the operating system and audio driver.

**Note:** This can be expensive; it is not recommended to call get_output_latency() every frame.

---

SpeakerMode **get_speaker_mode**()

Returns the speaker configuration.

---

[float](class_float.md#class-float) **get_time_since_last_mix**()

Returns the relative time since the last mix occurred, in seconds.

---

[float](class_float.md#class-float) **get_time_to_next_mix**()

Returns the relative time until the next mix occurs, in seconds.

---

[bool](class_bool.md#class-bool) **is_bus_bypassing_effects**(bus_idx: [int](class_int.md#class-int))

If `true`, the bus at index `bus_idx` is bypassing effects.

---

[bool](class_bool.md#class-bool) **is_bus_effect_enabled**(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int))

If `true`, the effect at index `effect_idx` on the bus at index `bus_idx` is enabled.

---

[bool](class_bool.md#class-bool) **is_bus_mute**(bus_idx: [int](class_int.md#class-int))

If `true`, the bus at index `bus_idx` is muted.

---

[bool](class_bool.md#class-bool) **is_bus_solo**(bus_idx: [int](class_int.md#class-int))

If `true`, the bus at index `bus_idx` is in solo mode.

---

[bool](class_bool.md#class-bool) **is_stream_registered_as_sample**(stream: [AudioStream](class_audiostream.md#class-audiostream))

**Experimental:** This method may be changed or removed in future versions.

If `true`, the stream is registered as a sample. The engine will not have to register it before playing the sample.

If `false`, the stream will have to be registered before playing it. To prevent lag spikes, register the stream as sample with register_stream_as_sample().

---

 **lock**()

Locks the audio driver's main loop.

**Note:** Remember to unlock it afterwards.

---

 **move_bus**(index: [int](class_int.md#class-int), to_index: [int](class_int.md#class-int))

Moves the bus from index `index` to index `to_index`.

---

 **register_stream_as_sample**(stream: [AudioStream](class_audiostream.md#class-audiostream))

**Experimental:** This method may be changed or removed in future versions.

Forces the registration of a stream as a sample.

**Note:** Lag spikes may occur when calling this method, especially on single-threaded builds. It is suggested to call this method while loading assets, where the lag spike could be masked, instead of registering the sample right before it needs to be played.

---

 **remove_bus**(index: [int](class_int.md#class-int))

Removes the bus at index `index`.

---

 **remove_bus_effect**(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int))

Removes the effect at index `effect_idx` from the bus at index `bus_idx`.

---

 **set_bus_bypass_effects**(bus_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

If `true`, the bus at index `bus_idx` is bypassing effects.

---

 **set_bus_effect_enabled**(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `true`, the effect at index `effect_idx` on the bus at index `bus_idx` is enabled.

---

 **set_bus_layout**(bus_layout: [AudioBusLayout](class_audiobuslayout.md#class-audiobuslayout))

Overwrites the currently used [AudioBusLayout](class_audiobuslayout.md#class-audiobuslayout).

---

 **set_bus_mute**(bus_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

If `true`, the bus at index `bus_idx` is muted.

---

 **set_bus_name**(bus_idx: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets the name of the bus at index `bus_idx` to `name`.

---

 **set_bus_send**(bus_idx: [int](class_int.md#class-int), send: [StringName](class_stringname.md#class-stringname))

Connects the output of the bus at `bus_idx` to the bus named `send`.

---

 **set_bus_solo**(bus_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

If `true`, the bus at index `bus_idx` is in solo mode.

---

 **set_bus_volume_db**(bus_idx: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float))

Sets the volume in decibels of the bus at index `bus_idx` to `volume_db`.

---

 **set_bus_volume_linear**(bus_idx: [int](class_int.md#class-int), volume_linear: [float](class_float.md#class-float))

Sets the volume as a linear value of the bus at index `bus_idx` to `volume_linear`.

**Note:** Using this method is equivalent to calling set_bus_volume_db() with the result of [@GlobalScope.linear_to_db()](class_@globalscope.md#class-globalscope-method-linear-to-db) on a value.

---

 **set_enable_tagging_used_audio_streams**(enable: [bool](class_bool.md#class-bool))

If set to `true`, all instances of [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) will call [AudioStreamPlayback._tag_used_streams()](class_audiostreamplayback.md#class-audiostreamplayback-private-method-tag-used-streams) every mix step.

**Note:** This is enabled by default in the editor, as it is used by editor plugins for the audio stream previews.

---

[Error](class_@globalscope.md#enum-globalscope-error) **set_input_device_active**(active: [bool](class_bool.md#class-bool))

**Experimental:** This method may be changed or removed in future versions.

If `active` is `true`, starts the microphone input stream specified by input_device or returns an error if it failed.

If `active` is `false`, stops the input stream if it is running.

---

 **swap_bus_effects**(bus_idx: [int](class_int.md#class-int), effect_idx: [int](class_int.md#class-int), by_effect_idx: [int](class_int.md#class-int))

Swaps the position of two effects in bus `bus_idx`.

---

 **unlock**()

Unlocks the audio driver's main loop. (After locking it, you should always unlock it.)
