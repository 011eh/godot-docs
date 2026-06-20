# AudioStreamPlaybackResampled

**Inherits:** [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioStreamGeneratorPlayback](class_audiostreamgeneratorplayback.md#class-audiostreamgeneratorplayback), [AudioStreamPlaybackOggVorbis](class_audiostreamplaybackoggvorbis.md#class-audiostreamplaybackoggvorbis)

Playback class used for resampled [AudioStream](class_audiostream.md#class-audiostream)s.

## Description

Playback class used to mix an [AudioStream](class_audiostream.md#class-audiostream)'s audio samples to [AudioServer.get_mix_rate()](class_audioserver.md#class-audioserver-method-get-mix-rate) using cubic interpolation.

## Methods

| [float](class_float.md#class-float)   | \_get_stream_sampling_rate()                                                |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)         | \_mix_resampled(dst_buffer: `AudioFrame*`, frame_count: [int](class_int.md#class-int)) |
|                                       | begin_resample()                                                                              |

---

## Method Descriptions

[float](class_float.md#class-float) **\_get_stream_sampling_rate**()

Returns an [AudioStream](class_audiostream.md#class-audiostream)'s sample rate, in Hz. Used to perform resampling.

---

[int](class_int.md#class-int) **\_mix_resampled**(dst_buffer: `AudioFrame*`, frame_count: [int](class_int.md#class-int))

Called by begin_resample() to mix an [AudioStream](class_audiostream.md#class-audiostream) to [AudioServer.get_mix_rate()](class_audioserver.md#class-audioserver-method-get-mix-rate). Uses \_get_stream_sampling_rate() as the source sample rate. Returns the number of mixed frames.

---

 **begin_resample**()

Called when an [AudioStream](class_audiostream.md#class-audiostream) is played. Clears the cubic interpolation history and starts mixing by calling \_mix_resampled().
