# AudioEffectRecord

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Audio effect used for recording the sound from an audio bus.

## Description

Allows the user to record the sound from an audio bus into an [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav). When used on the Master audio bus, this includes all audio output by Godot.

Unlike [AudioEffectCapture](class_audioeffectcapture.md#class-audioeffectcapture), this effect encodes the recording with the given format (8-bit, 16-bit, or compressed) instead of giving access to the raw audio samples.

Can be used (with an [AudioStreamMicrophone](class_audiostreammicrophone.md#class-audiostreammicrophone)) to record from a microphone.

**Note:** [ProjectSettings.audio/driver/enable_input](class_projectsettings.md#class-projectsettings-property-audio-driver-enable-input) must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

## Tutorials

- [Recording with microphone](../tutorials/audio/recording_with_microphone.md)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)

## Properties

| [Format](class_audiostreamwav.md#enum-audiostreamwav-format)   | format   | `1`   |
|----------------------------------------------------------------|------------------------------------------------------|-------|

## Methods

| [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav)   | get_recording()                                                       |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                 | is_recording_active()                                           |
|                                                                  | set_recording_active(record: [bool](class_bool.md#class-bool)) |

---

## Property Descriptions

[Format](class_audiostreamwav.md#enum-audiostreamwav-format) **format** = `1`

-  **set_format**(value: [Format](class_audiostreamwav.md#enum-audiostreamwav-format))
- [Format](class_audiostreamwav.md#enum-audiostreamwav-format) **get_format**()

Specifies the format in which the sample will be recorded.

---

## Method Descriptions

[AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav) **get_recording**()

Returns the recorded sample.

---

[bool](class_bool.md#class-bool) **is_recording_active**()

Returns whether the recording is active or not.

---

 **set_recording_active**(record: [bool](class_bool.md#class-bool))

If `true`, the sound will be recorded. Note that restarting the recording will remove the previously recorded sample.
