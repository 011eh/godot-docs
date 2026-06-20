# VideoStreamPlayer

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control used for video playback.

## Description

A control used for playback of [VideoStream](class_videostream.md#class-videostream) resources.

Supported video formats are [Ogg Theora](https://www.theora.org/) (`.ogv`, [VideoStreamTheora](class_videostreamtheora.md#class-videostreamtheora)) and any format exposed via a GDExtension plugin.

**Warning:** On Web, video playback *will* perform poorly due to missing architecture-specific assembly optimizations.

## Tutorials

- [Playing videos](../tutorials/animation/playing_videos.md)

## Properties

| [int](class_int.md#class-int)                         | audio_track         | `0`         |
|-------------------------------------------------------|----------------------------------------------------------------------|-------------|
| [bool](class_bool.md#class-bool)                      | autoplay               | `false`     |
| [int](class_int.md#class-int)                         | buffering_msec   | `500`       |
| [StringName](class_stringname.md#class-stringname)    | bus                         | `&"Master"` |
| [bool](class_bool.md#class-bool)                      | expand                   | `false`     |
| [bool](class_bool.md#class-bool)                      | loop                       | `false`     |
| [bool](class_bool.md#class-bool)                      | paused                   | `false`     |
| [float](class_float.md#class-float)                   | speed_scale         | `1.0`       |
| [VideoStream](class_videostream.md#class-videostream) | stream                   |             |
| [float](class_float.md#class-float)                   | stream_position |             |
| [float](class_float.md#class-float)                   | volume                   |             |
| [float](class_float.md#class-float)                   | volume_db             | `0.0`       |

## Methods

| [float](class_float.md#class-float)             | get_stream_length()    |
|-------------------------------------------------|-----------------------------------------------------------------------------|
| [String](class_string.md#class-string)          | get_stream_name()        |
| [Texture2D](class_texture2d.md#class-texture2d) | get_video_texture()    |
| [bool](class_bool.md#class-bool)                | is_playing()                  |
|                                                 | play()                              |
|                                                 | stop()                              |

---

## Signals

**finished**()

Emitted when playback is finished.

---

## Property Descriptions

[int](class_int.md#class-int) **audio_track** = `0`

-  **set_audio_track**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_audio_track**()

The embedded audio track to play.

---

[bool](class_bool.md#class-bool) **autoplay** = `false`

-  **set_autoplay**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_autoplay**()

If `true`, playback starts when the scene loads.

---

[int](class_int.md#class-int) **buffering_msec** = `500`

-  **set_buffering_msec**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_buffering_msec**()

Amount of time in milliseconds to store in buffer while playing.

---

[StringName](class_stringname.md#class-stringname) **bus** = `&"Master"`

-  **set_bus**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_bus**()

Audio bus to use for sound playback.

---

[bool](class_bool.md#class-bool) **expand** = `false`

-  **set_expand**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_expand**()

If `true`, the video scales to the control size. Otherwise, the control minimum size will be automatically adjusted to match the video stream's dimensions.

---

[bool](class_bool.md#class-bool) **loop** = `false`

-  **set_loop**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_loop**()

If `true`, the video restarts when it reaches its end.

---

[bool](class_bool.md#class-bool) **paused** = `false`

-  **set_paused**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_paused**()

If `true`, the video is paused.

---

[float](class_float.md#class-float) **speed_scale** = `1.0`

-  **set_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_speed_scale**()

The stream's current speed scale. `1.0` is the normal speed, while `2.0` is double speed and `0.5` is half speed. A speed scale of `0.0` pauses the video, similar to setting paused to `true`.

---

[VideoStream](class_videostream.md#class-videostream) **stream**

-  **set_stream**(value: [VideoStream](class_videostream.md#class-videostream))
- [VideoStream](class_videostream.md#class-videostream) **get_stream**()

The assigned video stream. See description for supported formats.

---

[float](class_float.md#class-float) **stream_position**

-  **set_stream_position**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_stream_position**()

The current position of the stream, in seconds.

---

[float](class_float.md#class-float) **volume**

-  **set_volume**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume**()

Audio volume as a linear value.

---

[float](class_float.md#class-float) **volume_db** = `0.0`

-  **set_volume_db**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_volume_db**()

Audio volume in dB.

---

## Method Descriptions

[float](class_float.md#class-float) **get_stream_length**()

The length of the current stream, in seconds.

---

[String](class_string.md#class-string) **get_stream_name**()

Returns the video stream's name, or `"<No Stream>"` if no video stream is assigned.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_video_texture**()

Returns the current frame as a [Texture2D](class_texture2d.md#class-texture2d).

---

[bool](class_bool.md#class-bool) **is_playing**()

Returns `true` if the video is playing.

**Note:** The video is still considered playing if paused during playback.

---

 **play**()

Starts the video playback from the beginning. If the video is paused, this will not unpause the video.

---

 **stop**()

Stops the video playback and sets the stream position to 0.

**Note:** Although the stream position will be set to 0, the first frame of the video stream won't become the current frame.
