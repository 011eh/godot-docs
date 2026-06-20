# AudioStream

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator), [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive), [AudioStreamMicrophone](class_audiostreammicrophone.md#class-audiostreammicrophone), [AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3), [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis), [AudioStreamPlaylist](class_audiostreamplaylist.md#class-audiostreamplaylist), [AudioStreamPolyphonic](class_audiostreampolyphonic.md#class-audiostreampolyphonic), [AudioStreamRandomizer](class_audiostreamrandomizer.md#class-audiostreamrandomizer), [AudioStreamSynchronized](class_audiostreamsynchronized.md#class-audiostreamsynchronized), [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav)

Base class for audio streams.

## Description

Base class for audio streams. Audio streams are used for sound effects and music playback, and support WAV (via [AudioStreamWAV](class_audiostreamwav.md#class-audiostreamwav)), Ogg (via [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class-audiostreamoggvorbis)), and MP3 (via [AudioStreamMP3](class_audiostreammp3.md#class-audiostreammp3)) file formats.

## Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)
- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

## Methods

| [int](class_int.md#class-int)                                                           | \_get_bar_beats()               |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                                           | \_get_beat_count()             |
| [float](class_float.md#class-float)                                                     | \_get_bpm()                           |
| [float](class_float.md#class-float)                                                     | \_get_length()                     |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_parameter_list()     |
| [String](class_string.md#class-string)                                                  | \_get_stream_name()           |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_get_tags()                         |
| [bool](class_bool.md#class-bool)                                                        | \_has_loop()                         |
| [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback)           | \_instantiate_playback() |
| [bool](class_bool.md#class-bool)                                                        | \_is_monophonic()               |
| [bool](class_bool.md#class-bool)                                                        | can_be_sampled()                       |
| [AudioSample](class_audiosample.md#class-audiosample)                                   | generate_sample()                     |
| [float](class_float.md#class-float)                                                     | get_length()                               |
| [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback)           | instantiate_playback()           |
| [bool](class_bool.md#class-bool)                                                        | is_meta_stream()                       |
| [bool](class_bool.md#class-bool)                                                        | is_monophonic()                         |

---

## Signals

**parameter_list_changed**()

Signal to be emitted to notify when the parameter list changed.

---

## Method Descriptions

[int](class_int.md#class-int) **\_get_bar_beats**()

Override this method to return the bar beats of this stream.

---

[int](class_int.md#class-int) **\_get_beat_count**()

Overridable method. Should return the total number of beats of this audio stream. Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate ([AudioStreamWAV.mix_rate](class_audiostreamwav.md#class-audiostreamwav-property-mix-rate), for example).

---

[float](class_float.md#class-float) **\_get_bpm**()

Overridable method. Should return the tempo of this audio stream, in beats per minute (BPM). Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate ([AudioStreamWAV.mix_rate](class_audiostreamwav.md#class-audiostreamwav-property-mix-rate), for example).

---

[float](class_float.md#class-float) **\_get_length**()

Override this method to customize the returned value of get_length(). Should return the length of this audio stream, in seconds.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_parameter_list**()

Return the controllable parameters of this stream. This array contains dictionaries with a property info description format (see [Object.get_property_list()](class_object.md#class-object-method-get-property-list)). Additionally, the default value for this parameter must be added tho each dictionary in "default_value" field.

---

[String](class_string.md#class-string) **\_get_stream_name**()

Override this method to customize the name assigned to this audio stream. Unused by the engine.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_tags**()

Override this method to customize the tags for this audio stream. Should return a [Dictionary](class_dictionary.md#class-dictionary) of strings with the tag as the key and its content as the value.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date`.

---

[bool](class_bool.md#class-bool) **\_has_loop**()

Override this method to return `true` if this stream has a loop.

---

[AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **\_instantiate_playback**()

Override this method to customize the returned value of instantiate_playback(). Should return a new [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) created when the stream is played (such as by an [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer)).

---

[bool](class_bool.md#class-bool) **\_is_monophonic**()

Override this method to customize the returned value of is_monophonic(). Should return `true` if this audio stream only supports one channel.

---

[bool](class_bool.md#class-bool) **can_be_sampled**()

**Experimental:** This method may be changed or removed in future versions.

Returns if the current **AudioStream** can be used as a sample. Only static streams can be sampled.

---

[AudioSample](class_audiosample.md#class-audiosample) **generate_sample**()

**Experimental:** This method may be changed or removed in future versions.

Generates an [AudioSample](class_audiosample.md#class-audiosample) based on the current stream.

---

[float](class_float.md#class-float) **get_length**()

Returns the length of the audio stream in seconds. If this stream is an [AudioStreamRandomizer](class_audiostreamrandomizer.md#class-audiostreamrandomizer), returns the length of the last played stream. If this stream has an indefinite length (such as for [AudioStreamGenerator](class_audiostreamgenerator.md#class-audiostreamgenerator) and [AudioStreamMicrophone](class_audiostreammicrophone.md#class-audiostreammicrophone)), returns `0.0`.

---

[AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **instantiate_playback**()

Returns a newly created [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) intended to play this audio stream. Useful for when you want to extend \_instantiate_playback() but call instantiate_playback() from an internally held AudioStream subresource. An example of this can be found in the source code for `AudioStreamRandomPitch::instantiate_playback`.

---

[bool](class_bool.md#class-bool) **is_meta_stream**()

Returns `true` if the stream is a collection of other streams, `false` otherwise.

---

[bool](class_bool.md#class-bool) **is_monophonic**()

Returns `true` if this audio stream only supports one channel (*monophony*), or `false` if the audio stream supports two or more channels (*polyphony*).
