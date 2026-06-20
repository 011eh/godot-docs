# AudioStreamPlaybackInteractive

**Inherits:** [AudioStreamPlayback](class_audiostreamplayback.md#class-audiostreamplayback) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Playback component of [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive).

## Description

Playback component of [AudioStreamInteractive](class_audiostreaminteractive.md#class-audiostreaminteractive). Contains functions to change the currently played clip.

## Methods

| [int](class_int.md#class-int)   | get_current_clip_index()                                                              |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                 | switch_to_clip(clip_index: [int](class_int.md#class-int))                                     |
|                                 | switch_to_clip_by_name(clip_name: [StringName](class_stringname.md#class-stringname)) |

---

## Method Descriptions

[int](class_int.md#class-int) **get_current_clip_index**()

Return the index of the currently playing clip. You can use this to get the name of the currently playing clip with [AudioStreamInteractive.get_clip_name()](class_audiostreaminteractive.md#class-audiostreaminteractive-method-get-clip-name).

**Example:** Get the currently playing clip name from inside an [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer) node.

GDScript

```gdscript
var playing_clip_name = stream.get_clip_name(get_stream_playback().get_current_clip_index())
```

---

 **switch_to_clip**(clip_index: [int](class_int.md#class-int))

Switch to a clip (by index).

---

 **switch_to_clip_by_name**(clip_name: [StringName](class_stringname.md#class-stringname))

Switch to a clip (by name).
