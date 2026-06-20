# AudioEffectEQ

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioEffectEQ10](class_audioeffecteq10.md#class-audioeffecteq10), [AudioEffectEQ21](class_audioeffecteq21.md#class-audioeffecteq21), [AudioEffectEQ6](class_audioeffecteq6.md#class-audioeffecteq6)

Base class for audio equalizers (EQ). Gives you control over frequencies.

Use it to create a custom equalizer if [AudioEffectEQ6](class_audioeffecteq6.md#class-audioeffecteq6), [AudioEffectEQ10](class_audioeffecteq10.md#class-audioeffecteq10), or [AudioEffectEQ21](class_audioeffecteq21.md#class-audioeffecteq21) don't fit your needs.

## Description

An "equalizer" gives you control over the gain of frequencies in the entire spectrum, by allowing their adjustment through bands. A band is a point in the frequency spectrum, and each band means a division of the spectrum that can be adjusted.

Use equalizers to compensate for existing deficiencies in the audio, make room for other elements, or remove undesirable frequencies. AudioEffectEQs are useful on the Master bus to balance the entire mix or give it more character. They are also useful when a game is run on a mobile device, to adjust the mix to that kind of speakers (it can be disabled when headphones are plugged in).

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

## Methods

| [int](class_int.md#class-int)       | get_band_count()                                                                                            |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float) | get_band_gain_db(band_idx: [int](class_int.md#class-int))                                                 |
|                                     | set_band_gain_db(band_idx: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float)) |

---

## Method Descriptions

[int](class_int.md#class-int) **get_band_count**()

Returns the number of bands of the equalizer.

---

[float](class_float.md#class-float) **get_band_gain_db**(band_idx: [int](class_int.md#class-int))

Returns the band's gain at the specified index, in dB.

---

 **set_band_gain_db**(band_idx: [int](class_int.md#class-int), volume_db: [float](class_float.md#class-float))

Sets band's gain at the specified index, in dB.
