# AudioEffectDelay

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a delay audio effect to an audio bus.

Emulates an echo by playing the input audio back after a period of time.

## Description

A "delay" effect plays the input audio signal back after a period of time. Each repetition is called a "delay tap" or simply "tap". Delay taps may be played back multiple times to create the sound of a repeating, decaying echo. Delay effects range from a subtle echo to a pronounced blending of previous sounds with new sounds.

See also [AudioEffectReverb](class_audioeffectreverb.md#class-audioeffectreverb) for a blurry, continuous echo.

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

## Properties

| [float](class_float.md#class-float)   | dry                             | `1.0`     |
|---------------------------------------|-------------------------------------------------------------------------|-----------|
| [bool](class_bool.md#class-bool)      | feedback_active     | `false`   |
| [float](class_float.md#class-float)   | feedback_delay_ms | `340.0`   |
| [float](class_float.md#class-float)   | feedback_level_db | `-6.0`    |
| [float](class_float.md#class-float)   | feedback_lowpass   | `16000.0` |
| [bool](class_bool.md#class-bool)      | tap1_active             | `true`    |
| [float](class_float.md#class-float)   | tap1_delay_ms         | `250.0`   |
| [float](class_float.md#class-float)   | tap1_level_db         | `-6.0`    |
| [float](class_float.md#class-float)   | tap1_pan                   | `0.2`     |
| [bool](class_bool.md#class-bool)      | tap2_active             | `true`    |
| [float](class_float.md#class-float)   | tap2_delay_ms         | `500.0`   |
| [float](class_float.md#class-float)   | tap2_level_db         | `-12.0`   |
| [float](class_float.md#class-float)   | tap2_pan                   | `-0.4`    |

---

## Property Descriptions

[float](class_float.md#class-float) **dry** = `1.0`

-  **set_dry**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_dry**()

The volume ratio of the original audio. Value can range from 0 to 1.

---

[bool](class_bool.md#class-bool) **feedback_active** = `false`

-  **set_feedback_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_feedback_active**()

If `true`, feedback is enabled, repeating taps after they are played.

---

[float](class_float.md#class-float) **feedback_delay_ms** = `340.0`

-  **set_feedback_delay_ms**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_feedback_delay_ms**()

Feedback delay time in milliseconds. Value can range from 0 to 1500.

---

[float](class_float.md#class-float) **feedback_level_db** = `-6.0`

-  **set_feedback_level_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_feedback_level_db**()

Gain for feedback, in dB. Value can range from -60 to 0.

---

[float](class_float.md#class-float) **feedback_lowpass** = `16000.0`

-  **set_feedback_lowpass**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_feedback_lowpass**()

Low-pass filter for feedback, in Hz. Frequencies above this value are filtered out. Value can range from 1 to 16000.

---

[bool](class_bool.md#class-bool) **tap1_active** = `true`

-  **set_tap1_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_tap1_active**()

If `true`, the first tap will be enabled.

---

[float](class_float.md#class-float) **tap1_delay_ms** = `250.0`

-  **set_tap1_delay_ms**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_tap1_delay_ms**()

First tap delay time in milliseconds, compared to the original audio. Value can range from 0 to 1500.

---

[float](class_float.md#class-float) **tap1_level_db** = `-6.0`

-  **set_tap1_level_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_tap1_level_db**()

Gain for the first tap, in dB. Value can range from -60 to 0.

---

[float](class_float.md#class-float) **tap1_pan** = `0.2`

-  **set_tap1_pan**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_tap1_pan**()

Pan position for the first tap. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.

---

[bool](class_bool.md#class-bool) **tap2_active** = `true`

-  **set_tap2_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_tap2_active**()

If `true`, the second tap will be enabled.

---

[float](class_float.md#class-float) **tap2_delay_ms** = `500.0`

-  **set_tap2_delay_ms**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_tap2_delay_ms**()

Second tap delay time in milliseconds, compared to the original audio. Value can range from 0 to 1500.

---

[float](class_float.md#class-float) **tap2_level_db** = `-12.0`

-  **set_tap2_level_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_tap2_level_db**()

Gain for the second tap, in dB. Value can range from -60 to 0.

---

[float](class_float.md#class-float) **tap2_pan** = `-0.4`

-  **set_tap2_pan**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_tap2_pan**()

Pan position for the second tap. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.
