# AudioEffectReverb

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a reverberation audio effect to an audio bus.

Emulates an echo by playing a blurred version of the input audio.

## Description

A "reverb" effect plays the input audio back continuously, decaying over a period of time. It simulates sounds in different kinds of spaces, ranging from small rooms, to big caverns.

See also [AudioEffectDelay](class_audioeffectdelay.md#class-audioeffectdelay) for a non-blurry type of echo.

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [float](class_float.md#class-float)   | damping                     | `0.5`   |
|---------------------------------------|--------------------------------------------------------------------------|---------|
| [float](class_float.md#class-float)   | dry                             | `1.0`   |
| [float](class_float.md#class-float)   | hipass                       | `0.0`   |
| [float](class_float.md#class-float)   | predelay_feedback | `0.4`   |
| [float](class_float.md#class-float)   | predelay_msec         | `150.0` |
| [float](class_float.md#class-float)   | room_size                 | `0.8`   |
| [float](class_float.md#class-float)   | spread                       | `1.0`   |
| [float](class_float.md#class-float)   | wet                             | `0.5`   |

---

## Property Descriptions

[float](class_float.md#class-float) **damping** = `0.5`

-  **set_damping**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_damping**()

Defines how reflective the imaginary room's walls are. The more reflective, the more high frequency content the reverb has. Value can range from 0 to 1.

---

[float](class_float.md#class-float) **dry** = `1.0`

-  **set_dry**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_dry**()

The volume ratio of the original audio. At 0, only the modified audio is outputted. Value can range from 0 to 1.

---

[float](class_float.md#class-float) **hipass** = `0.0`

-  **set_hpf**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_hpf**()

High-pass filter allows frequencies higher than a certain cutoff threshold and attenuates frequencies lower than the cutoff threshold. Value can range from 0 to 1.

---

[float](class_float.md#class-float) **predelay_feedback** = `0.4`

-  **set_predelay_feedback**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_predelay_feedback**()

Gain of early reflection copies. At higher values, early reflection copies are louder and ring out for longer. Value can range from 0 to 1.

---

[float](class_float.md#class-float) **predelay_msec** = `150.0`

-  **set_predelay_msec**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_predelay_msec**()

Time between the original audio and the early reflections of the reverb signal, in milliseconds. Value can range from 20 to 500.

---

[float](class_float.md#class-float) **room_size** = `0.8`

-  **set_room_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_room_size**()

Dimensions of simulated room. Bigger means more echoes. Value can range from 0 to 1.

---

[float](class_float.md#class-float) **spread** = `1.0`

-  **set_spread**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_spread**()

Widens or narrows the stereo image of the reverb tail. At 1, it fully widens. Value can range from 0 to 1.

---

[float](class_float.md#class-float) **wet** = `0.5`

-  **set_wet**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_wet**()

The volume ratio of the modified audio. At 0, only the original audio is outputted. Value can range from 0 to 1.
