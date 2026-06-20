# AudioEffectStereoEnhance

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a stereo manipulation audio effect to an audio bus.

Controls gain of the side channels, and widens the stereo image.

## Description

Adjusts gain of the left and right channels, and makes mono sounds stereo through phase shifting.

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

## Properties

| [float](class_float.md#class-float)   | pan_pullout         | `1.0`   |
|---------------------------------------|-----------------------------------------------------------------------------|---------|
| [float](class_float.md#class-float)   | surround               | `0.0`   |
| [float](class_float.md#class-float)   | time_pullout_ms | `0.0`   |

---

## Property Descriptions

[float](class_float.md#class-float) **pan_pullout** = `1.0`

-  **set_pan_pullout**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pan_pullout**()

Gain of the side channels, if they exist. A value of 0 will downmix stereo to mono. Value can range from 0 to 4.

---

[float](class_float.md#class-float) **surround** = `0.0`

-  **set_surround**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_surround**()

Widens the stereo image through phase shifting in conjunction with time_pullout_ms. Just pans sound to the left channel if time_pullout_ms is 0. Value can range from 0 to 1.

---

[float](class_float.md#class-float) **time_pullout_ms** = `0.0`

-  **set_time_pullout**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_time_pullout**()

Widens the stereo image through phase shifting in conjunction with surround. Just delays the right channel if surround is 0. Value is in milliseconds, and can range from 0 to 50.
