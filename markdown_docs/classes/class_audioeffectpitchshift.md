# AudioEffectPitchShift

**Inherits:** [AudioEffect](class_audioeffect.md#class-audioeffect) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Adds a pitch-shifting audio effect to an audio bus.

Raises or lowers the pitch of the input audio.

## Description

Allows modulation of pitch without modifying speed. All frequencies can be raised or lowered with minimal effect on transients.

## Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)
- [Audio effects](../tutorials/audio/audio_effects.md)

## Properties

| FFTSize   | fft_size         | `3`   |
|--------------------------------------------------|--------------------------------------------------------------------|-------|
| [int](class_int.md#class-int)                    | oversampling | `4`   |
| [float](class_float.md#class-float)              | pitch_scale   | `1.0` |

---

## Enumerations

enum **FFTSize**:

FFTSize **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest latency, but least stable over time.

FFTSize **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency, but less stable over time.

FFTSize **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a compromise between latency and stability over time.

FFTSize **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High latency, but stable over time.

FFTSize **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest latency, but most stable over time.

FFTSize **FFT_SIZE_MAX** = `5`

Represents the size of the FFTSize enum.

---

## Property Descriptions

FFTSize **fft_size** = `3`

-  **set_fft_size**(value: FFTSize)
- FFTSize **get_fft_size**()

The size of the [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) buffer. Higher values smooth out the effect over time, but have greater latency. The effects of this higher latency are especially noticeable on audio signals that have sudden amplitude changes.

---

[int](class_int.md#class-int) **oversampling** = `4`

-  **set_oversampling**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_oversampling**()

The oversampling factor to use. Higher values result in better quality, but are more demanding on the CPU and may cause audio cracking if the CPU can't keep up.

---

[float](class_float.md#class-float) **pitch_scale** = `1.0`

-  **set_pitch_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pitch_scale**()

The pitch scale to use. `1.0` is the default pitch and plays sounds unaffected. pitch_scale can range from 0 (infinitely low pitch, inaudible) to 16 (16 times higher than the initial pitch).
