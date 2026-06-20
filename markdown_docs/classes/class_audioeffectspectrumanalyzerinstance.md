# AudioEffectSpectrumAnalyzerInstance

**Inherits:** [AudioEffectInstance](class_audioeffectinstance.md#class-audioeffectinstance) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Queryable instance of an [AudioEffectSpectrumAnalyzer](class_audioeffectspectrumanalyzer.md#class-audioeffectspectrumanalyzer).

## Description

The runtime part of an [AudioEffectSpectrumAnalyzer](class_audioeffectspectrumanalyzer.md#class-audioeffectspectrumanalyzer), which can be used to query the magnitude of a frequency range on its host bus.

An instance of this class can be obtained with [AudioServer.get_bus_effect_instance()](class_audioserver.md#class-audioserver-method-get-bus-effect-instance).

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

## Methods

| [Vector2](class_vector2.md#class-vector2)   | get_magnitude_for_frequency_range(from_hz: [float](class_float.md#class-float), to_hz: [float](class_float.md#class-float), mode: MagnitudeMode = 1)    |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

## Enumerations

enum **MagnitudeMode**:

MagnitudeMode **MAGNITUDE_AVERAGE** = `0`

Use the average value across the frequency range as magnitude.

MagnitudeMode **MAGNITUDE_MAX** = `1`

Use the maximum value of the frequency range as magnitude.

---

## Method Descriptions

[Vector2](class_vector2.md#class-vector2) **get_magnitude_for_frequency_range**(from_hz: [float](class_float.md#class-float), to_hz: [float](class_float.md#class-float), mode: MagnitudeMode = 1)

Returns the magnitude of the frequencies from `from_hz` to `to_hz` in linear energy as a Vector2. The `x` component of the return value represents the left stereo channel, and `y` represents the right channel.

`mode` determines how the frequency range will be processed.
