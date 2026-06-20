# AudioStreamRandomizer

**Inherits:** [AudioStream](class_audiostream.md#class-audiostream) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Wraps a pool of audio streams with pitch and volume shifting.

## Description

Picks a random AudioStream from the pool, depending on the playback mode, and applies random pitch shifting and volume shifting during playback.

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

## Properties

| PlaybackMode   | playback_mode                     | `0`   |
|------------------------------------------------------------|------------------------------------------------------------------------------------------|-------|
| [float](class_float.md#class-float)                        | random_pitch                       | `1.0` |
| [float](class_float.md#class-float)                        | random_pitch_semitones   | `0.0` |
| [float](class_float.md#class-float)                        | random_volume_offset_db | `0.0` |
| [AudioStream](class_audiostream.md#class-audiostream)      | stream_{index}/stream       |       |
| [float](class_float.md#class-float)                        | stream_{index}/weight       | `1.0` |
| [int](class_int.md#class-int)                              | streams_count                     | `0`   |

## Methods

|                                                       | add_stream(index: [int](class_int.md#class-int), stream: [AudioStream](class_audiostream.md#class-audiostream), weight: [float](class_float.md#class-float) = 1.0)   |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AudioStream](class_audiostream.md#class-audiostream) | get_stream(index: [int](class_int.md#class-int))                                                                                                                     |
| [float](class_float.md#class-float)                   | get_stream_probability_weight(index: [int](class_int.md#class-int))                                                                               |
|                                                       | move_stream(index_from: [int](class_int.md#class-int), index_to: [int](class_int.md#class-int))                                                                     |
|                                                       | remove_stream(index: [int](class_int.md#class-int))                                                                                                               |
|                                                       | set_stream(index: [int](class_int.md#class-int), stream: [AudioStream](class_audiostream.md#class-audiostream))                                                      |
|                                                       | set_stream_probability_weight(index: [int](class_int.md#class-int), weight: [float](class_float.md#class-float))                                  |

---

## Enumerations

enum **PlaybackMode**:

PlaybackMode **PLAYBACK_RANDOM_NO_REPEATS** = `0`

Pick a stream at random according to the probability weights chosen for each stream, but avoid playing the same stream twice in a row whenever possible. If only 1 sound is present in the pool, the same sound will always play, effectively allowing repeats to occur.

PlaybackMode **PLAYBACK_RANDOM** = `1`

Pick a stream at random according to the probability weights chosen for each stream. If only 1 sound is present in the pool, the same sound will always play.

PlaybackMode **PLAYBACK_SEQUENTIAL** = `2`

Play streams in the order they appear in the stream pool. If only 1 sound is present in the pool, the same sound will always play.

---

## Property Descriptions

PlaybackMode **playback_mode** = `0`

-  **set_playback_mode**(value: PlaybackMode)
- PlaybackMode **get_playback_mode**()

Controls how this AudioStreamRandomizer picks which AudioStream to play next.

---

[float](class_float.md#class-float) **random_pitch** = `1.0`

-  **set_random_pitch**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_random_pitch**()

The largest possible frequency multiplier of the random pitch variation. Pitch will be randomly chosen within a range of `1.0 / random_pitch` and `random_pitch`. A value of `1.0` means no variation. A value of `2.0` means pitch will be randomized between double and half.

**Note:** Setting this property also sets random_pitch_semitones.

---

[float](class_float.md#class-float) **random_pitch_semitones** = `0.0`

-  **set_random_pitch_semitones**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_random_pitch_semitones**()

The largest possible distance, in semitones, of the random pitch variation. A value of `0.0` means no variation.

**Note:** Setting this property also sets random_pitch.

---

[float](class_float.md#class-float) **random_volume_offset_db** = `0.0`

-  **set_random_volume_offset_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_random_volume_offset_db**()

The intensity of random volume variation. Volume will be increased or decreased by a random value up to `random_volume_offset_db`. A value of `0.0` means no variation. A value of `3.0` means volume will be randomized between `-3.0 dB` and `+3.0 dB`.

---

[AudioStream](class_audiostream.md#class-audiostream) **stream_{index}/stream**

The [AudioStream](class_audiostream.md#class-audiostream) at `index`.

**Note:** `index` is a value in the `0 .. streams_count - 1` range.

---

[float](class_float.md#class-float) **stream_{index}/weight** = `1.0`

The probability weight of the [AudioStream](class_audiostream.md#class-audiostream) at `index`.

**Note:** `index` is a value in the `0 .. streams_count - 1` range.

---

[int](class_int.md#class-int) **streams_count** = `0`

-  **set_streams_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_streams_count**()

The number of streams in the stream pool.

---

## Method Descriptions

 **add_stream**(index: [int](class_int.md#class-int), stream: [AudioStream](class_audiostream.md#class-audiostream), weight: [float](class_float.md#class-float) = 1.0)

Insert a stream at the specified index. If the index is less than zero, the insertion occurs at the end of the underlying pool.

---

[AudioStream](class_audiostream.md#class-audiostream) **get_stream**(index: [int](class_int.md#class-int))

Returns the stream at the specified index.

---

[float](class_float.md#class-float) **get_stream_probability_weight**(index: [int](class_int.md#class-int))

Returns the probability weight associated with the stream at the given index.

---

 **move_stream**(index_from: [int](class_int.md#class-int), index_to: [int](class_int.md#class-int))

Move a stream from one index to another.

---

 **remove_stream**(index: [int](class_int.md#class-int))

Remove the stream at the specified index.

---

 **set_stream**(index: [int](class_int.md#class-int), stream: [AudioStream](class_audiostream.md#class-audiostream))

Set the AudioStream at the specified index.

---

 **set_stream_probability_weight**(index: [int](class_int.md#class-int), weight: [float](class_float.md#class-float))

Set the probability weight of the stream at the specified index. The higher this value, the more likely that the randomizer will choose this stream during random playback modes.
