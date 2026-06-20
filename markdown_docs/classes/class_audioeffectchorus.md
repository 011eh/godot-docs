# AudioEffectChorus

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a chorus audio effect to an audio bus.

Gives the impression of multiple audio sources.

## Description

A "chorus" effect creates multiple copies of the original audio (called "voices") with variations in pitch, and layers on top of the original, giving the impression that the sound comes from multiple sources. This creates spectral and spatial movement.

Each voice is played a short period of time after the original audio, controlled by `delay`. An internal low-frequency oscillator (LFO) controls their pitch, and `depth` controls the LFO's maximum amount.

In the real world, this kind of effect is found in pianos, choirs, and instrument ensembles.

This effect can also be used to widen mono audio and make digital sounds have a more natural or analog quality.

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

## Properties

| [float](class_float.md#class-float)   | dry                             | `1.0`    |
|---------------------------------------|--------------------------------------------------------------------------|----------|
| [float](class_float.md#class-float)   | voice/1/cutoff_hz | `8000.0` |
| [float](class_float.md#class-float)   | voice/1/delay_ms   | `15.0`   |
| [float](class_float.md#class-float)   | voice/1/depth_ms   | `2.0`    |
| [float](class_float.md#class-float)   | voice/1/level_db   | `0.0`    |
| [float](class_float.md#class-float)   | voice/1/pan             | `-0.5`   |
| [float](class_float.md#class-float)   | voice/1/rate_hz     | `0.8`    |
| [float](class_float.md#class-float)   | voice/2/cutoff_hz | `8000.0` |
| [float](class_float.md#class-float)   | voice/2/delay_ms   | `20.0`   |
| [float](class_float.md#class-float)   | voice/2/depth_ms   | `3.0`    |
| [float](class_float.md#class-float)   | voice/2/level_db   | `0.0`    |
| [float](class_float.md#class-float)   | voice/2/pan             | `0.5`    |
| [float](class_float.md#class-float)   | voice/2/rate_hz     | `1.2`    |
| [float](class_float.md#class-float)   | voice/3/cutoff_hz |          |
| [float](class_float.md#class-float)   | voice/3/delay_ms   |          |
| [float](class_float.md#class-float)   | voice/3/depth_ms   |          |
| [float](class_float.md#class-float)   | voice/3/level_db   |          |
| [float](class_float.md#class-float)   | voice/3/pan             |          |
| [float](class_float.md#class-float)   | voice/3/rate_hz     |          |
| [float](class_float.md#class-float)   | voice/4/cutoff_hz |          |
| [float](class_float.md#class-float)   | voice/4/delay_ms   |          |
| [float](class_float.md#class-float)   | voice/4/depth_ms   |          |
| [float](class_float.md#class-float)   | voice/4/level_db   |          |
| [float](class_float.md#class-float)   | voice/4/pan             |          |
| [float](class_float.md#class-float)   | voice/4/rate_hz     |          |
| [int](class_int.md#class-int)         | voice_count             | `2`      |
| [float](class_float.md#class-float)   | wet                             | `0.5`    |

## Methods

| [float](class_float.md#class-float)   | get_voice_cutoff_hz(voice_idx: [int](class_int.md#class-int))                                                 |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float)   | get_voice_delay_ms(voice_idx: [int](class_int.md#class-int))                                                   |
| [float](class_float.md#class-float)   | get_voice_depth_ms(voice_idx: [int](class_int.md#class-int))                                                   |
| [float](class_float.md#class-float)   | get_voice_level_db(voice_idx: [int](class_int.md#class-int))                                                   |
| [float](class_float.md#class-float)   | get_voice_pan(voice_idx: [int](class_int.md#class-int))                                                             |
| [float](class_float.md#class-float)   | get_voice_rate_hz(voice_idx: [int](class_int.md#class-int))                                                     |
|                                       | set_voice_cutoff_hz(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float)) |
|                                       | set_voice_delay_ms(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))    |
|                                       | set_voice_depth_ms(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))    |
|                                       | set_voice_level_db(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))    |
|                                       | set_voice_pan(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))                   |
|                                       | set_voice_rate_hz(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))       |

---

## Property Descriptions

[float](class_float.md#class-float) **dry** = `1.0`

-  **set_dry**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_dry**()

The volume ratio of the original audio. Value can range from 0 to 1.

---

[float](class_float.md#class-float) **voice/1/cutoff_hz** = `8000.0`

-  **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) 

The frequency threshold of the voice's low-pass filter in Hz.

---

[float](class_float.md#class-float) **voice/1/delay_ms** = `15.0`

-  **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) 

The delay of the voice in milliseconds, compared to the original audio.

---

[float](class_float.md#class-float) **voice/1/depth_ms** = `2.0`

-  **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) 

The depth of the voice's low-frequency oscillator in milliseconds.

---

[float](class_float.md#class-float) **voice/1/level_db** = `0.0`

-  **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) 

The gain of the voice in dB.

---

[float](class_float.md#class-float) **voice/1/pan** = `-0.5`

-  **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) 

The pan position of the voice.

---

[float](class_float.md#class-float) **voice/1/rate_hz** = `0.8`

-  **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) 

The rate of the voice's low-frequency oscillator in Hz.

---

[float](class_float.md#class-float) **voice/2/cutoff_hz** = `8000.0`

-  **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) 

The frequency threshold of the voice's low-pass filter in Hz.

---

[float](class_float.md#class-float) **voice/2/delay_ms** = `20.0`

-  **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) 

The delay of the voice in milliseconds, compared to the original audio.

---

[float](class_float.md#class-float) **voice/2/depth_ms** = `3.0`

-  **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) 

The depth of the voice's low-frequency oscillator in milliseconds.

---

[float](class_float.md#class-float) **voice/2/level_db** = `0.0`

-  **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) 

The gain of the voice in dB.

---

[float](class_float.md#class-float) **voice/2/pan** = `0.5`

-  **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) 

The pan position of the voice.

---

[float](class_float.md#class-float) **voice/2/rate_hz** = `1.2`

-  **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) 

The rate of the voice's low-frequency oscillator in Hz.

---

[float](class_float.md#class-float) **voice/3/cutoff_hz**

-  **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) 

The frequency threshold of the voice's low-pass filter in Hz.

---

[float](class_float.md#class-float) **voice/3/delay_ms**

-  **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) 

The delay of the voice in milliseconds, compared to the original audio.

---

[float](class_float.md#class-float) **voice/3/depth_ms**

-  **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) 

The depth of the voice's low-frequency oscillator in milliseconds.

---

[float](class_float.md#class-float) **voice/3/level_db**

-  **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) 

The gain of the voice in dB.

---

[float](class_float.md#class-float) **voice/3/pan**

-  **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) 

The pan position of the voice.

---

[float](class_float.md#class-float) **voice/3/rate_hz**

-  **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) 

The rate of the voice's low-frequency oscillator in Hz.

---

[float](class_float.md#class-float) **voice/4/cutoff_hz**

-  **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int)) 

The frequency threshold of the voice's low-pass filter in Hz.

---

[float](class_float.md#class-float) **voice/4/delay_ms**

-  **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int)) 

The delay of the voice in milliseconds, compared to the original audio.

---

[float](class_float.md#class-float) **voice/4/depth_ms**

-  **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int)) 

The depth of the voice's low-frequency oscillator in milliseconds.

---

[float](class_float.md#class-float) **voice/4/level_db**

-  **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int)) 

The gain of the voice in dB.

---

[float](class_float.md#class-float) **voice/4/pan**

-  **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int)) 

The pan position of the voice.

---

[float](class_float.md#class-float) **voice/4/rate_hz**

-  **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int)) 

The rate of the voice's low-frequency oscillator in Hz.

---

[int](class_int.md#class-int) **voice_count** = `2`

-  **set_voice_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_voice_count**()

The number of voices in the effect. Value can range from 1 to 4.

---

[float](class_float.md#class-float) **wet** = `0.5`

-  **set_wet**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_wet**()

The volume ratio of all voices. Value can range from 0 to 1.

---

## Method Descriptions

[float](class_float.md#class-float) **get_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int))

Returns the frequency threshold of a given `voice_idx`'s low-pass filter in Hz. Frequencies above this value are removed from the voice.

---

[float](class_float.md#class-float) **get_voice_delay_ms**(voice_idx: [int](class_int.md#class-int))

Returns the delay of a given `voice_idx` in milliseconds, compared to the original audio.

---

[float](class_float.md#class-float) **get_voice_depth_ms**(voice_idx: [int](class_int.md#class-int))

Returns the depth of a given `voice_idx`'s low-frequency oscillator in milliseconds.

---

[float](class_float.md#class-float) **get_voice_level_db**(voice_idx: [int](class_int.md#class-int))

Returns the gain of a given `voice_idx` in dB.

---

[float](class_float.md#class-float) **get_voice_pan**(voice_idx: [int](class_int.md#class-int))

Returns the pan position of a given `voice_idx`. Negative values mean the left channel, positive mean the right.

---

[float](class_float.md#class-float) **get_voice_rate_hz**(voice_idx: [int](class_int.md#class-int))

Returns the rate of a given `voice_idx`'s low-frequency oscillator in Hz.

---

 **set_voice_cutoff_hz**(voice_idx: [int](class_int.md#class-int), cutoff_hz: [float](class_float.md#class-float))

Sets the frequency threshold of a given `voice_idx`'s low-pass filter in Hz. Frequencies above `cutoff_hz` are removed from `voice_idx`. Value can range from 1 to 20500.

---

 **set_voice_delay_ms**(voice_idx: [int](class_int.md#class-int), delay_ms: [float](class_float.md#class-float))

Sets the delay of a given `voice_idx` in milliseconds, compared to the original audio. Value can range from 0 to 50.

---

 **set_voice_depth_ms**(voice_idx: [int](class_int.md#class-int), depth_ms: [float](class_float.md#class-float))

Sets the depth of a given `voice_idx`'s low-frequency oscillator in milliseconds. Value can range from 0 to 20.

---

 **set_voice_level_db**(voice_idx: [int](class_int.md#class-int), level_db: [float](class_float.md#class-float))

Sets the gain of a given `voice_idx` in dB. Value can range from -60 to 24.

---

 **set_voice_pan**(voice_idx: [int](class_int.md#class-int), pan: [float](class_float.md#class-float))

Sets the pan position of a given `voice_idx`. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.

---

 **set_voice_rate_hz**(voice_idx: [int](class_int.md#class-int), rate_hz: [float](class_float.md#class-float))

Sets the rate of a given `voice_idx`'s low-frequency oscillator in Hz. Value can range from 0.1 to 20.
