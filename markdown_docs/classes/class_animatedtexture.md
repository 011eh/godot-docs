# AnimatedTexture

**Deprecated:** This class does not work properly in current versions and may be removed in the future. There is currently no equivalent workaround.

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Proxy texture for simple frame-based animations.

## Description

**AnimatedTexture** is a resource format for frame-based animations, where multiple textures can be chained automatically with a predefined delay for each frame. Unlike [AnimationPlayer](class_animationplayer.md#class-animationplayer) or [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d), it isn't a [Node](class_node.md#class-node), but has the advantage of being usable anywhere a [Texture2D](class_texture2d.md#class-texture2d) resource can be used, e.g. in a [TileSet](class_tileset.md#class-tileset).

The playback of the animation is controlled by the speed_scale property, as well as each frame's duration (see set_frame_duration()). The animation loops, i.e. it will restart at frame 0 automatically after playing the last frame.

**AnimatedTexture** currently requires all frame textures to have the same size, otherwise the bigger ones will be cropped to match the smallest one.

**Note:** AnimatedTexture doesn't support using [AtlasTexture](class_atlastexture.md#class-atlastexture)s. Each frame needs to be a separate [Texture2D](class_texture2d.md#class-texture2d).

**Warning:** The current implementation is not efficient for the modern renderers.

## Properties

| [int](class_int.md#class-int)       | current_frame   |                                                                                                   |
|-------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)       | frames                 | `1`                                                                                               |
| [bool](class_bool.md#class-bool)    | one_shot             | `false`                                                                                           |
| [bool](class_bool.md#class-bool)    | pause                   | `false`                                                                                           |
| [bool](class_bool.md#class-bool)    | resource_local_to_scene                                          | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [float](class_float.md#class-float) | speed_scale       | `1.0`                                                                                             |

## Methods

| [float](class_float.md#class-float)             | get_frame_duration(frame: [int](class_int.md#class-int))                                                         |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Texture2D](class_texture2d.md#class-texture2d) | get_frame_texture(frame: [int](class_int.md#class-int))                                                           |
|                                                 | set_frame_duration(frame: [int](class_int.md#class-int), duration: [float](class_float.md#class-float))          |
|                                                 | set_frame_texture(frame: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d)) |

---

## Constants

**MAX_FRAMES** = `256`

The maximum number of frames supported by **AnimatedTexture**. If you need more frames in your animation, use [AnimationPlayer](class_animationplayer.md#class-animationplayer) or [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d).

---

## Property Descriptions

[int](class_int.md#class-int) **current_frame**

-  **set_current_frame**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_current_frame**()

Sets the currently visible frame of the texture. Setting this frame while playing resets the current frame time, so the newly selected frame plays for its whole configured frame duration.

---

[int](class_int.md#class-int) **frames** = `1`

-  **set_frames**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_frames**()

Number of frames to use in the animation. While you can create the frames independently with set_frame_texture(), you need to set this value for the animation to take new frames into account. The maximum number of frames is MAX_FRAMES.

---

[bool](class_bool.md#class-bool) **one_shot** = `false`

-  **set_one_shot**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_one_shot**()

If `true`, the animation will only play once and will not loop back to the first frame after reaching the end. Note that reaching the end will not set pause to `true`.

---

[bool](class_bool.md#class-bool) **pause** = `false`

-  **set_pause**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_pause**()

If `true`, the animation will pause where it currently is (i.e. at current_frame). The animation will continue from where it was paused when changing this property to `false`.

---

[float](class_float.md#class-float) **speed_scale** = `1.0`

-  **set_speed_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_speed_scale**()

The animation speed is multiplied by this value. If set to a negative value, the animation is played in reverse.

---

## Method Descriptions

[float](class_float.md#class-float) **get_frame_duration**(frame: [int](class_int.md#class-int))

Returns the given `frame`'s duration, in seconds.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_frame_texture**(frame: [int](class_int.md#class-int))

Returns the given frame's [Texture2D](class_texture2d.md#class-texture2d).

---

 **set_frame_duration**(frame: [int](class_int.md#class-int), duration: [float](class_float.md#class-float))

Sets the duration of any given `frame`. The final duration is affected by the speed_scale. If set to `0`, the frame is skipped during playback.

---

 **set_frame_texture**(frame: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))

Assigns a [Texture2D](class_texture2d.md#class-texture2d) to the given frame. Frame IDs start at 0, so the first frame has ID 0, and the last frame of the animation has ID frames - 1.

You can define any number of textures up to MAX_FRAMES, but keep in mind that only frames from 0 to frames - 1 will be part of the animation.
