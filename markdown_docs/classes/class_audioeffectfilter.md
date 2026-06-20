# AudioEffectFilter

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioEffectBandLimitFilter](class_audioeffectbandlimitfilter.md#class-audioeffectbandlimitfilter), [AudioEffectBandPassFilter](class_audioeffectbandpassfilter.md#class-audioeffectbandpassfilter), [AudioEffectHighPassFilter](class_audioeffecthighpassfilter.md#class-audioeffecthighpassfilter), [AudioEffectHighShelfFilter](class_audioeffecthighshelffilter.md#class-audioeffecthighshelffilter), [AudioEffectLowPassFilter](class_audioeffectlowpassfilter.md#class-audioeffectlowpassfilter), [AudioEffectLowShelfFilter](class_audioeffectlowshelffilter.md#class-audioeffectlowshelffilter), [AudioEffectNotchFilter](class_audioeffectnotchfilter.md#class-audioeffectnotchfilter)

Base class for filters. Use effects that inherit this class instead of using it directly.

## Description

A "filter" controls the gain of frequencies, using cutoff_hz as a frequency threshold. Filters can help to give room for each sound, and create interesting effects.

There are different types of filter that inherit this class:

Shelf filters: [AudioEffectLowShelfFilter](class_audioeffectlowshelffilter.md#class-audioeffectlowshelffilter) and [AudioEffectHighShelfFilter](class_audioeffecthighshelffilter.md#class-audioeffecthighshelffilter)

Band-pass and notch filters: [AudioEffectBandPassFilter](class_audioeffectbandpassfilter.md#class-audioeffectbandpassfilter), [AudioEffectBandLimitFilter](class_audioeffectbandlimitfilter.md#class-audioeffectbandlimitfilter), and [AudioEffectNotchFilter](class_audioeffectnotchfilter.md#class-audioeffectnotchfilter)

Low/high-pass filters: [AudioEffectLowPassFilter](class_audioeffectlowpassfilter.md#class-audioeffectlowpassfilter) and [AudioEffectHighPassFilter](class_audioeffecthighpassfilter.md#class-audioeffecthighpassfilter)

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

## Properties

| [float](class_float.md#class-float)          | cutoff_hz   | `2000.0`   |
|----------------------------------------------|------------------------------------------------------------|------------|
| FilterDB | db                 | `0`        |
| [float](class_float.md#class-float)          | gain             | `1.0`      |
| [float](class_float.md#class-float)          | resonance   | `0.5`      |

---

## Enumerations

enum **FilterDB**:

FilterDB **FILTER_6DB** = `0`

Cutting off at 6 dB per octave. One octave is twice the frequency above cutoff_hz, or half the frequency below cutoff_hz.

FilterDB **FILTER_12DB** = `1`

Cutting off at 12 dB per octave. One octave is twice the frequency above cutoff_hz, or half the frequency below cutoff_hz.

FilterDB **FILTER_18DB** = `2`

Cutting off at 18 dB per octave. One octave is twice the frequency above cutoff_hz, or half the frequency below cutoff_hz.

FilterDB **FILTER_24DB** = `3`

Cutting off at 24 dB per octave. One octave is twice the frequency above cutoff_hz, or half the frequency below cutoff_hz.

---

## Property Descriptions

[float](class_float.md#class-float) **cutoff_hz** = `2000.0`

-  **set_cutoff**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_cutoff**()

Frequency threshold for the filter, in Hz. Value can range from 1 to 20500.

---

FilterDB **db** = `0`

-  **set_db**(value: FilterDB)
- FilterDB **get_db**()

Steepness of the cutoff curve in dB per octave (twice the frequency above cutoff_hz, or half the frequency below cutoff_hz), also known as the "order" of the filter. Higher orders have a more aggressive cutoff.

---

[float](class_float.md#class-float) **gain** = `1.0`

-  **set_gain**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_gain**()

Gain of the frequencies affected by the filter. This property is only available for [AudioEffectLowShelfFilter](class_audioeffectlowshelffilter.md#class-audioeffectlowshelffilter) and [AudioEffectHighShelfFilter](class_audioeffecthighshelffilter.md#class-audioeffecthighshelffilter). Value can range from 0 to 4.

---

[float](class_float.md#class-float) **resonance** = `0.5`

-  **set_resonance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_resonance**()

Gain at or directly next to the cutoff_hz frequency threshold. Value can range from 0 to 1.

Its exact behavior depends on the selected filter type:

- For shelf filters, it accentuates or masks the order by increasing frequencies right next to the cutoff_hz frequency and decreasing frequencies on the opposite side.
- For the band-pass and notch filters, it widens or narrows the filter at the cutoff_hz frequency threshold.
- For low/high-pass filters, it increases or decreases frequencies at the cutoff_hz frequency threshold.
