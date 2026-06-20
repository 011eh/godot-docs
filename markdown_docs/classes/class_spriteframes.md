# SpriteFrames

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Sprite frame library for AnimatedSprite2D and AnimatedSprite3D.

## Description

Sprite frame library for an [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d) or [AnimatedSprite3D](class_animatedsprite3d.md#class-animatedsprite3d) node. Contains frames and animation data for playback.

## Methods

|                                                                         | add_animation(anim: [StringName](class_stringname.md#class-stringname))                                                                                                                                                         |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                         | add_frame(anim: [StringName](class_stringname.md#class-stringname), texture: [Texture2D](class_texture2d.md#class-texture2d), duration: [float](class_float.md#class-float) = 1.0, at_position: [int](class_int.md#class-int) = -1) |
|                                                                         | clear(anim: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                         |
|                                                                         | clear_all()                                                                                                                                                                                                                         |
|                                                                         | duplicate_animation(anim_from: [StringName](class_stringname.md#class-stringname), anim_to: [StringName](class_stringname.md#class-stringname))                                                                           |
| [bool](class_bool.md#class-bool)                                        | get_animation_loop(anim: [StringName](class_stringname.md#class-stringname))                                                                                                                                               |
| LoopMode                                 | get_animation_loop_mode(anim: [StringName](class_stringname.md#class-stringname))                                                                                                                                     |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_animation_names()                                                                                                                                                                                                     |
| [float](class_float.md#class-float)                                     | get_animation_speed(anim: [StringName](class_stringname.md#class-stringname))                                                                                                                                             |
| [int](class_int.md#class-int)                                           | get_frame_count(anim: [StringName](class_stringname.md#class-stringname))                                                                                                                                                     |
| [float](class_float.md#class-float)                                     | get_frame_duration(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int))                                                                                                           |
| [Texture2D](class_texture2d.md#class-texture2d)                         | get_frame_texture(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int))                                                                                                             |
| [bool](class_bool.md#class-bool)                                        | has_animation(anim: [StringName](class_stringname.md#class-stringname))                                                                                                                                                         |
|                                                                         | remove_animation(anim: [StringName](class_stringname.md#class-stringname))                                                                                                                                                   |
|                                                                         | remove_frame(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int))                                                                                                                       |
|                                                                         | rename_animation(anim: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname))                                                                                      |
|                                                                         | set_animation_loop(anim: [StringName](class_stringname.md#class-stringname), loop: [bool](class_bool.md#class-bool))                                                                                                       |
|                                                                         | set_animation_loop_mode(anim: [StringName](class_stringname.md#class-stringname), loop_mode: LoopMode)                                                                                 |
|                                                                         | set_animation_speed(anim: [StringName](class_stringname.md#class-stringname), fps: [float](class_float.md#class-float))                                                                                                   |
|                                                                         | set_frame(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d), duration: [float](class_float.md#class-float) = 1.0)              |

---

## Enumerations

enum **LoopMode**:

LoopMode **LOOP_NONE** = `0`

The animation plays once and stops when it reaches the end, or the start if played in reverse.

LoopMode **LOOP_LINEAR** = `1`

The animation restarts from the beginning when it reaches the end, or from the end if played in reverse, repeating continuously.

LoopMode **LOOP_PINGPONG** = `2`

The animation alternates direction each time it reaches the end or start, playing forward and then in reverse repeatedly.

**Note:** Both [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d) and [AnimatedSprite3D](class_animatedsprite3d.md#class-animatedsprite3d) play the first/last frame for its duration only once at each end of the animation loop (instead of twice, once per forward/backward animation direction).

---

## Method Descriptions

 **add_animation**(anim: [StringName](class_stringname.md#class-stringname))

Adds a new `anim` animation to the library.

---

 **add_frame**(anim: [StringName](class_stringname.md#class-stringname), texture: [Texture2D](class_texture2d.md#class-texture2d), duration: [float](class_float.md#class-float) = 1.0, at_position: [int](class_int.md#class-int) = -1)

Adds a frame to the `anim` animation. If `at_position` is `-1`, the frame will be added to the end of the animation. `duration` specifies the relative duration, see get_frame_duration() for details.

---

 **clear**(anim: [StringName](class_stringname.md#class-stringname))

Removes all frames from the `anim` animation.

---

 **clear_all**()

Removes all animations. An empty `default` animation will be created.

---

 **duplicate_animation**(anim_from: [StringName](class_stringname.md#class-stringname), anim_to: [StringName](class_stringname.md#class-stringname))

Duplicates the animation `anim_from` to a new animation named `anim_to`. Fails if `anim_to` already exists, or if `anim_from` does not exist.

---

[bool](class_bool.md#class-bool) **get_animation_loop**(anim: [StringName](class_stringname.md#class-stringname))

**Deprecated:** Use get_animation_loop_mode() instead.

Returns `true` if `get_animation_loop_mode(anim) == LOOP_LINEAR`. Otherwise, returns `false`.

---

LoopMode **get_animation_loop_mode**(anim: [StringName](class_stringname.md#class-stringname))

Returns the loop mode for the `anim` animation.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_animation_names**()

Returns an array containing the names associated to each animation. Values are placed in alphabetical order.

---

[float](class_float.md#class-float) **get_animation_speed**(anim: [StringName](class_stringname.md#class-stringname))

Returns the speed in frames per second for the `anim` animation.

---

[int](class_int.md#class-int) **get_frame_count**(anim: [StringName](class_stringname.md#class-stringname))

Returns the number of frames for the `anim` animation.

---

[float](class_float.md#class-float) **get_frame_duration**(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int))

Returns a relative duration of the frame `idx` in the `anim` animation (defaults to `1.0`). For example, a frame with a duration of `2.0` is displayed twice as long as a frame with a duration of `1.0`. You can calculate the absolute duration (in seconds) of a frame using the following formula:

```gdscript
absolute_duration = relative_duration / (animation_fps * abs(playing_speed))
```

In this example, `playing_speed` refers to either [AnimatedSprite2D.get_playing_speed()](class_animatedsprite2d.md#class-animatedsprite2d-method-get-playing-speed) or [AnimatedSprite3D.get_playing_speed()](class_animatedsprite3d.md#class-animatedsprite3d-method-get-playing-speed).

---

[Texture2D](class_texture2d.md#class-texture2d) **get_frame_texture**(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int))

Returns the texture of the frame `idx` in the `anim` animation.

---

[bool](class_bool.md#class-bool) **has_animation**(anim: [StringName](class_stringname.md#class-stringname))

Returns `true` if the `anim` animation exists.

---

 **remove_animation**(anim: [StringName](class_stringname.md#class-stringname))

Removes the `anim` animation.

---

 **remove_frame**(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int))

Removes the `anim` animation's frame `idx`.

---

 **rename_animation**(anim: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname))

Changes the `anim` animation's name to `newname`.

---

 **set_animation_loop**(anim: [StringName](class_stringname.md#class-stringname), loop: [bool](class_bool.md#class-bool))

**Deprecated:** Use set_animation_loop_mode() instead.

If `loop` is `false` equivalent to `set_animation_loop_mode(LOOP_NONE)`.

If `loop` is `true` equivalent to `set_animation_loop_mode(LOOP_LINEAR)`.

---

 **set_animation_loop_mode**(anim: [StringName](class_stringname.md#class-stringname), loop_mode: LoopMode)

Sets the `loop_mode` for the `anim` animation.

---

 **set_animation_speed**(anim: [StringName](class_stringname.md#class-stringname), fps: [float](class_float.md#class-float))

Sets the speed for the `anim` animation in frames per second.

---

 **set_frame**(anim: [StringName](class_stringname.md#class-stringname), idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d), duration: [float](class_float.md#class-float) = 1.0)

Sets the `texture` and the `duration` of the frame `idx` in the `anim` animation. `duration` specifies the relative duration, see get_frame_duration() for details.
