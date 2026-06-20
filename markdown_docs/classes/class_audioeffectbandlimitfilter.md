# AudioEffectBandLimitFilter

**Inherits:** [AudioEffectFilter](class_audioeffectfilter.md#class-audioeffectfilter) **<** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a band-limit filter to an audio bus.

## Description

A "band-limit" filter attenuates the frequencies at [AudioEffectFilter.cutoff_hz](class_audioeffectfilter.md#class-audioeffectfilter-property-cutoff-hz), and allows frequencies outside the frequency threshold to pass unchanged. It is a wider and weaker version of [AudioEffectNotchFilter](class_audioeffectnotchfilter.md#class-audioeffectnotchfilter), and is the opposite of [AudioEffectBandPassFilter](class_audioeffectbandpassfilter.md#class-audioeffectbandpassfilter).

This filter can be used to give more room for other sounds to play at that frequency.

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)
