# AnimationNodeAnimation

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An input animation for an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

## Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree). Only has one output port using the animation property. Used as an input for [AnimationNode](class_animationnode.md#class-animationnode)s that blend animations together.

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [bool](class_bool.md#class-bool)                       | advance_on_start       | `false`   |
|--------------------------------------------------------|-----------------------------------------------------------------------------------|-----------|
| [StringName](class_stringname.md#class-stringname)     | animation                     | `&""`     |
| [LoopMode](class_animation.md#enum-animation-loopmode) | loop_mode                     |           |
| PlayMode      | play_mode                     | `0`       |
| [float](class_float.md#class-float)                    | start_offset               |           |
| [bool](class_bool.md#class-bool)                       | stretch_time_scale   |           |
| [float](class_float.md#class-float)                    | timeline_length         |           |
| [bool](class_bool.md#class-bool)                       | use_custom_timeline | `false`   |

---

## Enumerations

enum **PlayMode**:

PlayMode **PLAY_MODE_FORWARD** = `0`

Plays animation in forward direction.

PlayMode **PLAY_MODE_BACKWARD** = `1`

Plays animation in backward direction.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **advance_on_start** = `false`

-  **set_advance_on_start**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_advance_on_start**()

If `true`, on receiving a request to play an animation from the start, the first frame is not drawn, but only processed, and playback starts from the next frame.

See also the notes of [AnimationPlayer.play()](class_animationplayer.md#class-animationplayer-method-play).

---

[StringName](class_stringname.md#class-stringname) **animation** = `&""`

-  **set_animation**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_animation**()

Animation to use as an output. It is one of the animations provided by [AnimationTree.anim_player](class_animationtree.md#class-animationtree-property-anim-player).

---

[LoopMode](class_animation.md#enum-animation-loopmode) **loop_mode**

-  **set_loop_mode**(value: [LoopMode](class_animation.md#enum-animation-loopmode))
- [LoopMode](class_animation.md#enum-animation-loopmode) **get_loop_mode**()

If use_custom_timeline is `true`, override the loop settings of the original [Animation](class_animation.md#class-animation) resource with the value.

**Note:** If the [Animation.loop_mode](class_animation.md#class-animation-property-loop-mode) isn't set to looping, the [Animation.track_set_interpolation_loop_wrap()](class_animation.md#class-animation-method-track-set-interpolation-loop-wrap) option will not be respected. If you cannot get the expected behavior, consider duplicating the [Animation](class_animation.md#class-animation) resource and changing the loop settings.

---

PlayMode **play_mode** = `0`

-  **set_play_mode**(value: PlayMode)
- PlayMode **get_play_mode**()

Determines the playback direction of the animation.

---

[float](class_float.md#class-float) **start_offset**

-  **set_start_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_start_offset**()

If use_custom_timeline is `true`, offset the start position of the animation.

This is useful for adjusting which foot steps first in 3D walking animations.

---

[bool](class_bool.md#class-bool) **stretch_time_scale**

-  **set_stretch_time_scale**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_stretching_time_scale**()

If `true`, scales the time so that the length specified in timeline_length is one cycle.

This is useful for matching the periods of walking and running animations.

If `false`, the original animation length is respected. If you set the loop to loop_mode, the animation will loop in timeline_length.

---

[float](class_float.md#class-float) **timeline_length**

-  **set_timeline_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_timeline_length**()

The length of the custom timeline.

If stretch_time_scale is `true`, scales the animation to this length.

---

[bool](class_bool.md#class-bool) **use_custom_timeline** = `false`

-  **set_use_custom_timeline**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_custom_timeline**()

If `true`, [AnimationNode](class_animationnode.md#class-animationnode) provides an animation based on the [Animation](class_animation.md#class-animation) resource with some parameters adjusted.
