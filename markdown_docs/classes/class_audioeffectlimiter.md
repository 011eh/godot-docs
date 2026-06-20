# AudioEffectLimiter

**Deprecated:** Use [AudioEffectHardLimiter](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter) instead.

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a soft-clip limiter audio effect to an audio bus.

## Description

A "limiter" is an audio effect designed to stop audio signals from exceeding a specified volume threshold level, and usually works by decreasing the volume or soft-clipping the audio. Adding one in the Master bus is always recommended to prevent clipping when the volume goes above 0 dB.

Soft clipping starts to decrease the peaks a little below the volume threshold level and progressively increases its effect as the input volume increases such that the threshold level is never exceeded.

If hard clipping is desired, consider [AudioEffectDistortion.MODE_CLIP](class_audioeffectdistortion.md#class-audioeffectdistortion-constant-mode-clip).

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

## Properties

| [float](class_float.md#class-float)   | ceiling_db           | `-0.1`   |
|---------------------------------------|-----------------------------------------------------------------------|----------|
| [float](class_float.md#class-float)   | soft_clip_db       | `2.0`    |
| [float](class_float.md#class-float)   | soft_clip_ratio | `10.0`   |
| [float](class_float.md#class-float)   | threshold_db       | `0.0`    |

---

## Property Descriptions

[float](class_float.md#class-float) **ceiling_db** = `-0.1`

-  **set_ceiling_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_ceiling_db**()

The waveform's maximum allowed value, in dB. Value can range from -20 to -0.1.

---

[float](class_float.md#class-float) **soft_clip_db** = `2.0`

-  **set_soft_clip_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_soft_clip_db**()

Modifies the volume of the limited waves, in dB. Value can range from 0 to 6.

---

[float](class_float.md#class-float) **soft_clip_ratio** = `10.0`

-  **set_soft_clip_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_soft_clip_ratio**()

This property has no effect on the audio. Use [AudioEffectHardLimiter](class_audioeffecthardlimiter.md#class-audioeffecthardlimiter) instead, as this Limiter effect is deprecated.

---

[float](class_float.md#class-float) **threshold_db** = `0.0`

-  **set_threshold_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_threshold_db**()

The volume threshold level from which the limiter begins to be active, in dB. Value can range from -30 to 0.
