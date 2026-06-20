# AnimatedSprite3D

**Inherits:** [SpriteBase3D](class_spritebase3d.md#class-spritebase3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

2D sprite node in 3D world, that can use multiple 2D textures for animation.

## Description

**AnimatedSprite3D** is similar to the [Sprite3D](class_sprite3d.md#class-sprite3d) node, except it carries multiple textures as animation sprite_frames. Animations are created using a [SpriteFrames](class_spriteframes.md#class-spriteframes) resource, which allows you to import image files (or a folder containing said files) to provide the animation frames for the sprite. The [SpriteFrames](class_spriteframes.md#class-spriteframes) resource can be configured in the editor via the SpriteFrames bottom panel.

## Tutorials

- [2D Sprite animation (also applies to 3D)](../tutorials/2d/2d_sprite_animation.md)

## Properties

| [StringName](class_stringname.md#class-stringname)       | animation           | `&"default"`   |
|----------------------------------------------------------|-------------------------------------------------------------------|----------------|
| [String](class_string.md#class-string)                   | autoplay             | `""`           |
| [int](class_int.md#class-int)                            | frame                   | `0`            |
| [float](class_float.md#class-float)                      | frame_progress | `0.0`          |
| [float](class_float.md#class-float)                      | speed_scale       | `1.0`          |
| [SpriteFrames](class_spriteframes.md#class-spriteframes) | sprite_frames   |                |

## Methods

| [float](class_float.md#class-float)   | get_playing_speed()                                                                                                                                                  |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)      | is_playing()                                                                                                                                                                |
|                                       | pause()                                                                                                                                                                          |
|                                       | play(name: [StringName](class_stringname.md#class-stringname) = &"", custom_speed: [float](class_float.md#class-float) = 1.0, from_end: [bool](class_bool.md#class-bool) = false) |
|                                       | play_backwards(name: [StringName](class_stringname.md#class-stringname) = &"")                                                                                          |
|                                       | set_frame_and_progress(frame: [int](class_int.md#class-int), progress: [float](class_float.md#class-float))                                                     |
|                                       | stop()                                                                                                                                                                            |

---

## Signals

**animation_changed**()

Emitted when animation changes.

---

**animation_finished**()

Emitted when the animation reaches the end, or the start if it is played in reverse. When the animation finishes, it pauses the playback.

**Note:** This signal is not emitted if an animation is looping.

---

**animation_looped**()

Emitted when the animation loops.

---

**frame_changed**()

Emitted when frame changes.

---

**sprite_frames_changed**()

Emitted when sprite_frames changes.

---

## Property Descriptions

[StringName](class_stringname.md#class-stringname) **animation** = `&"default"`

-  **set_animation**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_animation**()

The current animation from the sprite_frames resource. If this value is changed, the frame counter and the frame_progress are reset.

---

[String](class_string.md#class-string) **autoplay** = `""`

-  **set_autoplay**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_autoplay**()

The key of the animation to play when the scene loads.

---

[int](class_int.md#class-int) **frame** = `0`

-  **set_frame**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_frame**()

The displayed animation frame's index. Setting this property also resets frame_progress. If this is not desired, use set_frame_and_progress().

---

[float](class_float.md#class-float) **frame_progress** = `0.0`

-  **set_frame_progress**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_frame_progress**()

The progress value between `0.0` and `1.0` until the current frame transitions to the next frame. If the animation is playing backwards, the value transitions from `1.0` to `0.0`.

---

[float](class_float.md#class-float) **speed_scale** = `1.0`

-  **set_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_speed_scale**()

The speed scaling ratio. For example, if this value is `1`, then the animation plays at normal speed. If it's `0.5`, then it plays at half speed. If it's `2`, then it plays at double speed.

If set to a negative value, the animation is played in reverse. If set to `0`, the animation will not advance.

---

[SpriteFrames](class_spriteframes.md#class-spriteframes) **sprite_frames**

-  **set_sprite_frames**(value: [SpriteFrames](class_spriteframes.md#class-spriteframes))
- [SpriteFrames](class_spriteframes.md#class-spriteframes) **get_sprite_frames**()

The [SpriteFrames](class_spriteframes.md#class-spriteframes) resource containing the animation(s). Allows you the option to load, edit, clear, make unique and save the states of the [SpriteFrames](class_spriteframes.md#class-spriteframes) resource.

---

## Method Descriptions

[float](class_float.md#class-float) **get_playing_speed**()

Returns the actual playing speed of current animation or `0` if not playing. This speed is the speed_scale property multiplied by `custom_speed` argument specified when calling the play() method.

Returns a negative value if the current animation is playing backwards.

---

[bool](class_bool.md#class-bool) **is_playing**()

Returns `true` if an animation is currently playing (even if speed_scale and/or `custom_speed` are `0`).

---

 **pause**()

Pauses the currently playing animation. The frame and frame_progress will be kept and calling play() or play_backwards() without arguments will resume the animation from the current playback position.

See also stop().

---

 **play**(name: [StringName](class_stringname.md#class-stringname) = &"", custom_speed: [float](class_float.md#class-float) = 1.0, from_end: [bool](class_bool.md#class-bool) = false)

Plays the animation with key `name`. If `custom_speed` is negative and `from_end` is `true`, the animation will play backwards (which is equivalent to calling play_backwards()).

If this method is called with that same animation `name`, or with no `name` parameter, the assigned animation will resume playing if it was paused.

---

 **play_backwards**(name: [StringName](class_stringname.md#class-stringname) = &"")

Plays the animation with key `name` in reverse.

This method is a shorthand for play() with `custom_speed = -1.0` and `from_end = true`, so see its description for more information.

---

 **set_frame_and_progress**(frame: [int](class_int.md#class-int), progress: [float](class_float.md#class-float))

Sets frame and frame_progress to the given values. Unlike setting frame, this method does not reset the frame_progress to `0.0` implicitly.

**Example:** Change the animation while keeping the same frame and frame_progress:

GDScript

```gdscript
var current_frame = animated_sprite.get_frame()
var current_progress = animated_sprite.get_frame_progress()
animated_sprite.play("walk_another_skin")
animated_sprite.set_frame_and_progress(current_frame, current_progress)
```

---

 **stop**()

Stops the currently playing animation. The animation position is reset to `0` and the `custom_speed` is reset to `1.0`. See also pause().
