# AnimationMixer

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [AnimationPlayer](class_animationplayer.md#class-animationplayer), [AnimationTree](class_animationtree.md#class-animationtree)

Base class for [AnimationPlayer](class_animationplayer.md#class-animationplayer) and [AnimationTree](class_animationtree.md#class-animationtree).

## Description

Base class for [AnimationPlayer](class_animationplayer.md#class-animationplayer) and [AnimationTree](class_animationtree.md#class-animationtree) to manage animation lists. It also has general properties and methods for playback and blending.

After instantiating the playback information data within the extended class, the blending is processed by the **AnimationMixer**.

## Tutorials

- [Migrating Animations from Godot 4.0 to 4.3](https://godotengine.org/article/migrating-animations-from-godot-4-0-to-4-3/)

## Properties

| [bool](class_bool.md#class-bool)                                                    | active                                 | `true`           |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------------|
| [int](class_int.md#class-int)                                                       | audio_max_polyphony       | `32`             |
| AnimationCallbackModeDiscrete | callback_mode_discrete | `1`              |
| AnimationCallbackModeMethod     | callback_mode_method     | `0`              |
| AnimationCallbackModeProcess   | callback_mode_process   | `1`              |
| [bool](class_bool.md#class-bool)                                                    | deterministic                   | `false`          |
| [bool](class_bool.md#class-bool)                                                    | reset_on_save                   | `true`           |
| [bool](class_bool.md#class-bool)                                                    | root_motion_local           | `false`          |
| [NodePath](class_nodepath.md#class-nodepath)                                        | root_motion_track           | `NodePath("")`   |
| [NodePath](class_nodepath.md#class-nodepath)                                        | root_node                           | `NodePath("..")` |

## Methods

| [Variant](class_variant.md#class-variant)                                               | \_post_process_key_value(animation: [Animation](class_animation.md#class-animation), track: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant), object_id: [int](class_int.md#class-int), object_sub_idx: [int](class_int.md#class-int))     |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | add_animation_library(name: [StringName](class_stringname.md#class-stringname), library: [AnimationLibrary](class_animationlibrary.md#class-animationlibrary))                                                                                                                     |
|                                                                                         | advance(delta: [float](class_float.md#class-float))                                                                                                                                                                                                                                              |
|                                                                                         | capture(name: [StringName](class_stringname.md#class-stringname), duration: [float](class_float.md#class-float), trans_type: [TransitionType](class_tween.md#enum-tween-transitiontype) = 0, ease_type: [EaseType](class_tween.md#enum-tween-easetype) = 0)                                      |
|                                                                                         | clear_caches()                                                                                                                                                                                                                                                                              |
| [StringName](class_stringname.md#class-stringname)                                      | find_animation(animation: [Animation](class_animation.md#class-animation))                                                                                                                                                                                                                |
| [StringName](class_stringname.md#class-stringname)                                      | find_animation_library(animation: [Animation](class_animation.md#class-animation))                                                                                                                                                                                                |
| [Animation](class_animation.md#class-animation)                                         | get_animation(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                    |
| [AnimationLibrary](class_animationlibrary.md#class-animationlibrary)                    | get_animation_library(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                    |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_animation_library_list()                                                                                                                                                                                                                                                  |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | get_animation_list()                                                                                                                                                                                                                                                                  |
| [Vector3](class_vector3.md#class-vector3)                                               | get_root_motion_position()                                                                                                                                                                                                                                                      |
| [Vector3](class_vector3.md#class-vector3)                                               | get_root_motion_position_accumulator()                                                                                                                                                                                                                              |
| [Quaternion](class_quaternion.md#class-quaternion)                                      | get_root_motion_rotation()                                                                                                                                                                                                                                                      |
| [Quaternion](class_quaternion.md#class-quaternion)                                      | get_root_motion_rotation_accumulator()                                                                                                                                                                                                                              |
| [Vector3](class_vector3.md#class-vector3)                                               | get_root_motion_scale()                                                                                                                                                                                                                                                            |
| [Vector3](class_vector3.md#class-vector3)                                               | get_root_motion_scale_accumulator()                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | has_animation(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | has_animation_library(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                    |
|                                                                                         | remove_animation_library(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                              |
|                                                                                         | rename_animation_library(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname))                                                                                                                                 |

---

## Signals

**animation_finished**(anim_name: [StringName](class_stringname.md#class-stringname))

Notifies when an animation finished playing.

**Note:** This signal is not emitted if an animation is looping.

---

**animation_libraries_updated**()

Notifies when the animation libraries have changed.

---

**animation_list_changed**()

Notifies when an animation list is changed.

---

**animation_started**(anim_name: [StringName](class_stringname.md#class-stringname))

Notifies when an animation starts playing.

**Note:** This signal is not emitted if an animation is looping.

---

**caches_cleared**()

Notifies when the caches have been cleared, either automatically, or manually via clear_caches().

---

**mixer_applied**()

Notifies when the blending result related have been applied to the target objects.

---

**mixer_updated**()

Notifies when the property related process have been updated.

---

## Enumerations

enum **AnimationCallbackModeProcess**:

AnimationCallbackModeProcess **ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS** = `0`

Process animation during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class-node-constant-notification-internal-physics-process)). This is especially useful when animating physics bodies.

AnimationCallbackModeProcess **ANIMATION_CALLBACK_MODE_PROCESS_IDLE** = `1`

Process animation during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class-node-constant-notification-internal-process)).

AnimationCallbackModeProcess **ANIMATION_CALLBACK_MODE_PROCESS_MANUAL** = `2`

Do not process animation. Use advance() to process the animation manually.

---

enum **AnimationCallbackModeMethod**:

AnimationCallbackModeMethod **ANIMATION_CALLBACK_MODE_METHOD_DEFERRED** = `0`

Batch method calls during the animation process, then do the calls after events are processed. This avoids bugs involving deleting nodes or modifying the AnimationPlayer while playing.

AnimationCallbackModeMethod **ANIMATION_CALLBACK_MODE_METHOD_IMMEDIATE** = `1`

Make method calls immediately when reached in the animation.

---

enum **AnimationCallbackModeDiscrete**:

AnimationCallbackModeDiscrete **ANIMATION_CALLBACK_MODE_DISCRETE_DOMINANT** = `0`

An [Animation.UPDATE_DISCRETE](class_animation.md#class-animation-constant-update-discrete) track value takes precedence when blending [Animation.UPDATE_CONTINUOUS](class_animation.md#class-animation-constant-update-continuous) or [Animation.UPDATE_CAPTURE](class_animation.md#class-animation-constant-update-capture) track values and [Animation.UPDATE_DISCRETE](class_animation.md#class-animation-constant-update-discrete) track values.

AnimationCallbackModeDiscrete **ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE** = `1`

An [Animation.UPDATE_CONTINUOUS](class_animation.md#class-animation-constant-update-continuous) or [Animation.UPDATE_CAPTURE](class_animation.md#class-animation-constant-update-capture) track value takes precedence when blending the [Animation.UPDATE_CONTINUOUS](class_animation.md#class-animation-constant-update-continuous) or [Animation.UPDATE_CAPTURE](class_animation.md#class-animation-constant-update-capture) track values and the [Animation.UPDATE_DISCRETE](class_animation.md#class-animation-constant-update-discrete) track values. This is the default behavior for [AnimationPlayer](class_animationplayer.md#class-animationplayer).

AnimationCallbackModeDiscrete **ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS** = `2`

Always treat the [Animation.UPDATE_DISCRETE](class_animation.md#class-animation-constant-update-discrete) track value as [Animation.UPDATE_CONTINUOUS](class_animation.md#class-animation-constant-update-continuous) with [Animation.INTERPOLATION_NEAREST](class_animation.md#class-animation-constant-interpolation-nearest). This is the default behavior for [AnimationTree](class_animationtree.md#class-animationtree).

If a value track has un-interpolatable type key values, it is internally converted to use ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE with [Animation.UPDATE_DISCRETE](class_animation.md#class-animation-constant-update-discrete).

Un-interpolatable type list:

- [@GlobalScope.TYPE_NIL](class_@globalscope.md#class-globalscope-constant-type-nil)
- [@GlobalScope.TYPE_NODE_PATH](class_@globalscope.md#class-globalscope-constant-type-node-path)
- [@GlobalScope.TYPE_RID](class_@globalscope.md#class-globalscope-constant-type-rid)
- [@GlobalScope.TYPE_OBJECT](class_@globalscope.md#class-globalscope-constant-type-object)
- [@GlobalScope.TYPE_CALLABLE](class_@globalscope.md#class-globalscope-constant-type-callable)
- [@GlobalScope.TYPE_SIGNAL](class_@globalscope.md#class-globalscope-constant-type-signal)
- [@GlobalScope.TYPE_DICTIONARY](class_@globalscope.md#class-globalscope-constant-type-dictionary)
- [@GlobalScope.TYPE_PACKED_BYTE_ARRAY](class_@globalscope.md#class-globalscope-constant-type-packed-byte-array)

[@GlobalScope.TYPE_BOOL](class_@globalscope.md#class-globalscope-constant-type-bool) and [@GlobalScope.TYPE_INT](class_@globalscope.md#class-globalscope-constant-type-int) are treated as [@GlobalScope.TYPE_FLOAT](class_@globalscope.md#class-globalscope-constant-type-float) during blending and rounded when the result is retrieved.

It is same for arrays and vectors with them such as [@GlobalScope.TYPE_PACKED_INT32_ARRAY](class_@globalscope.md#class-globalscope-constant-type-packed-int32-array) or [@GlobalScope.TYPE_VECTOR2I](class_@globalscope.md#class-globalscope-constant-type-vector2i), they are treated as [@GlobalScope.TYPE_PACKED_FLOAT32_ARRAY](class_@globalscope.md#class-globalscope-constant-type-packed-float32-array) or [@GlobalScope.TYPE_VECTOR2](class_@globalscope.md#class-globalscope-constant-type-vector2). Also note that for arrays, the size is also interpolated.

[@GlobalScope.TYPE_STRING](class_@globalscope.md#class-globalscope-constant-type-string) and [@GlobalScope.TYPE_STRING_NAME](class_@globalscope.md#class-globalscope-constant-type-string-name) are interpolated between character codes and lengths, but note that there is a difference in algorithm between interpolation between keys and interpolation by blending.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **active** = `true`

-  **set_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_active**()

If `true`, the **AnimationMixer** will be processing.

---

[int](class_int.md#class-int) **audio_max_polyphony** = `32`

-  **set_audio_max_polyphony**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_audio_max_polyphony**()

The number of possible simultaneous sounds for each of the assigned AudioStreamPlayers.

For example, if this value is `32` and the animation has two audio tracks, the two [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer)s assigned can play simultaneously up to `32` voices each.

---

AnimationCallbackModeDiscrete **callback_mode_discrete** = `1`

-  **set_callback_mode_discrete**(value: AnimationCallbackModeDiscrete)
- AnimationCallbackModeDiscrete **get_callback_mode_discrete**()

Ordinarily, tracks can be set to [Animation.UPDATE_DISCRETE](class_animation.md#class-animation-constant-update-discrete) to update infrequently, usually when using nearest interpolation.

However, when blending with [Animation.UPDATE_CONTINUOUS](class_animation.md#class-animation-constant-update-continuous) several results are considered. The callback_mode_discrete specify it explicitly. See also AnimationCallbackModeDiscrete.

To make the blended results look good, it is recommended to set this to ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS to update every frame during blending. Other values exist for compatibility and they are fine if there is no blending, but not so, may produce artifacts.

---

AnimationCallbackModeMethod **callback_mode_method** = `0`

-  **set_callback_mode_method**(value: AnimationCallbackModeMethod)
- AnimationCallbackModeMethod **get_callback_mode_method**()

The call mode used for "Call Method" tracks.

---

AnimationCallbackModeProcess **callback_mode_process** = `1`

-  **set_callback_mode_process**(value: AnimationCallbackModeProcess)
- AnimationCallbackModeProcess **get_callback_mode_process**()

The process notification in which to update animations.

---

[bool](class_bool.md#class-bool) **deterministic** = `false`

-  **set_deterministic**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deterministic**()

If `true`, the blending uses the deterministic algorithm. The total weight is not normalized and the result is accumulated with an initial value (`0` or a `"RESET"` animation if present).

This means that if the total amount of blending is `0.0`, the result is equal to the `"RESET"` animation.

If the number of tracks between the blended animations is different, the animation with the missing track is treated as if it had the initial value.

If `false`, The blend does not use the deterministic algorithm. The total weight is normalized and always `1.0`. If the number of tracks between the blended animations is different, nothing is done about the animation that is missing a track.

**Note:** In [AnimationTree](class_animationtree.md#class-animationtree), the blending with [AnimationNodeAdd2](class_animationnodeadd2.md#class-animationnodeadd2), [AnimationNodeAdd3](class_animationnodeadd3.md#class-animationnodeadd3), [AnimationNodeSub2](class_animationnodesub2.md#class-animationnodesub2) or the weight greater than `1.0` may produce unexpected results.

For example, if [AnimationNodeAdd2](class_animationnodeadd2.md#class-animationnodeadd2) blends two nodes with the amount `1.0`, then total weight is `2.0` but it will be normalized to make the total amount `1.0` and the result will be equal to [AnimationNodeBlend2](class_animationnodeblend2.md#class-animationnodeblend2) with the amount `0.5`.

---

[bool](class_bool.md#class-bool) **reset_on_save** = `true`

-  **set_reset_on_save_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_reset_on_save_enabled**()

This is used by the editor. If set to `true`, the scene will be saved with the effects of the reset animation (the animation with the key `"RESET"`) applied as if it had been seeked to time 0, with the editor keeping the values that the scene had before saving.

This makes it more convenient to preview and edit animations in the editor, as changes to the scene will not be saved as long as they are set in the reset animation.

---

[bool](class_bool.md#class-bool) **root_motion_local** = `false`

-  **set_root_motion_local**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_root_motion_local**()

If `true`, get_root_motion_position() value is extracted as a local translation value before blending. In other words, it is treated like the translation is done after the rotation.

---

[NodePath](class_nodepath.md#class-nodepath) **root_motion_track** = `NodePath("")`

-  **set_root_motion_track**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_root_motion_track**()

The path to the Animation track used for root motion. Paths must be valid scene-tree paths to a node, and must be specified starting from the parent node of the node that will reproduce the animation. The root_motion_track uses the same format as [Animation.track_set_path()](class_animation.md#class-animation-method-track-set-path), but note that a bone must be specified.

If the track has type [Animation.TYPE_POSITION_3D](class_animation.md#class-animation-constant-type-position-3d), [Animation.TYPE_ROTATION_3D](class_animation.md#class-animation-constant-type-rotation-3d), or [Animation.TYPE_SCALE_3D](class_animation.md#class-animation-constant-type-scale-3d) the transformation will be canceled visually, and the animation will appear to stay in place. See also get_root_motion_position(), get_root_motion_rotation(), get_root_motion_scale(), and [RootMotionView](class_rootmotionview.md#class-rootmotionview).

---

[NodePath](class_nodepath.md#class-nodepath) **root_node** = `NodePath("..")`

-  **set_root_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_root_node**()

The node which node path references will travel from.

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **\_post_process_key_value**(animation: [Animation](class_animation.md#class-animation), track: [int](class_int.md#class-int), value: [Variant](class_variant.md#class-variant), object_id: [int](class_int.md#class-int), object_sub_idx: [int](class_int.md#class-int))

A virtual function for processing after getting a key during playback.

---

[Error](class_@globalscope.md#enum-globalscope-error) **add_animation_library**(name: [StringName](class_stringname.md#class-stringname), library: [AnimationLibrary](class_animationlibrary.md#class-animationlibrary))

Adds `library` to the animation player, under the key `name`.

AnimationMixer has a global library by default with an empty string as key. For adding an animation to the global library:

GDScript

```gdscript
var global_library = mixer.get_animation_library("")
global_library.add_animation("animation_name", animation_resource)
```

---

 **advance**(delta: [float](class_float.md#class-float))

Manually advance the animations by the specified time (in seconds).

---

 **capture**(name: [StringName](class_stringname.md#class-stringname), duration: [float](class_float.md#class-float), trans_type: [TransitionType](class_tween.md#enum-tween-transitiontype) = 0, ease_type: [EaseType](class_tween.md#enum-tween-easetype) = 0)

If the animation track specified by `name` has an option [Animation.UPDATE_CAPTURE](class_animation.md#class-animation-constant-update-capture), stores current values of the objects indicated by the track path as a cache. If there is already a captured cache, the old cache is discarded.

After this it will interpolate with current animation blending result during the playback process for the time specified by `duration`, working like a crossfade.

You can specify `trans_type` as the curve for the interpolation. For better results, it may be appropriate to specify [Tween.TRANS_LINEAR](class_tween.md#class-tween-constant-trans-linear) for cases where the first key of the track begins with a non-zero value or where the key value does not change, and [Tween.TRANS_QUAD](class_tween.md#class-tween-constant-trans-quad) for cases where the key value changes linearly.

---

 **clear_caches**()

**AnimationMixer** caches animated nodes. It may not notice if a node disappears; clear_caches() forces it to update the cache again.

---

[StringName](class_stringname.md#class-stringname) **find_animation**(animation: [Animation](class_animation.md#class-animation))

Returns the key of `animation` or an empty [StringName](class_stringname.md#class-stringname) if not found.

---

[StringName](class_stringname.md#class-stringname) **find_animation_library**(animation: [Animation](class_animation.md#class-animation))

Returns the key for the [AnimationLibrary](class_animationlibrary.md#class-animationlibrary) that contains `animation` or an empty [StringName](class_stringname.md#class-stringname) if not found.

---

[Animation](class_animation.md#class-animation) **get_animation**(name: [StringName](class_stringname.md#class-stringname))

Returns the [Animation](class_animation.md#class-animation) with the key `name`. If the animation does not exist, `null` is returned and an error is logged.

---

[AnimationLibrary](class_animationlibrary.md#class-animationlibrary) **get_animation_library**(name: [StringName](class_stringname.md#class-stringname))

Returns the first [AnimationLibrary](class_animationlibrary.md#class-animationlibrary) with key `name` or `null` if not found.

To get the **AnimationMixer**'s global animation library, use `get_animation_library("")`.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_animation_library_list**()

Returns the list of stored library keys.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_animation_list**()

Returns the list of stored animation keys.

---

[Vector3](class_vector3.md#class-vector3) **get_root_motion_position**()

Retrieve the motion delta of position with the root_motion_track as a [Vector3](class_vector3.md#class-vector3) that can be used elsewhere.

If root_motion_track is not a path to a track of type [Animation.TYPE_POSITION_3D](class_animation.md#class-animation-constant-type-position-3d), returns `Vector3(0, 0, 0)`.

See also root_motion_track and [RootMotionView](class_rootmotionview.md#class-rootmotionview).

The most basic example is applying position to [CharacterBody3D](class_characterbody3d.md#class-characterbody3d):

GDScript

```gdscript
var current_rotation

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        current_rotation = get_quaternion()
        state_machine.travel("Animate")
    var velocity = current_rotation * animation_tree.get_root_motion_position() / delta
    set_velocity(velocity)
    move_and_slide()
```

By using this in combination with get_root_motion_rotation_accumulator(), you can apply the root motion position more correctly to account for the rotation of the node.

GDScript

```gdscript
func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())
    var velocity = (animation_tree.get_root_motion_rotation_accumulator().inverse() * get_quaternion()) * animation_tree.get_root_motion_position() / delta
    set_velocity(velocity)
    move_and_slide()
```

If root_motion_local is `true`, returns the pre-multiplied translation value with the inverted rotation.

In this case, the code can be written as follows:

GDScript

```gdscript
func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())
    var velocity = get_quaternion() * animation_tree.get_root_motion_position() / delta
    set_velocity(velocity)
    move_and_slide()
```

---

[Vector3](class_vector3.md#class-vector3) **get_root_motion_position_accumulator**()

Retrieve the blended value of the position tracks with the root_motion_track as a [Vector3](class_vector3.md#class-vector3) that can be used elsewhere.

This is useful in cases where you want to respect the initial key values of the animation.

For example, if an animation with only one key `Vector3(0, 0, 0)` is played in the previous frame and then an animation with only one key `Vector3(1, 0, 1)` is played in the next frame, the difference can be calculated as follows:

GDScript

```gdscript
var prev_root_motion_position_accumulator

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    var current_root_motion_position_accumulator = animation_tree.get_root_motion_position_accumulator()
    var difference = current_root_motion_position_accumulator - prev_root_motion_position_accumulator
    prev_root_motion_position_accumulator = current_root_motion_position_accumulator
    transform.origin += difference
```

However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.

---

[Quaternion](class_quaternion.md#class-quaternion) **get_root_motion_rotation**()

Retrieve the motion delta of rotation with the root_motion_track as a [Quaternion](class_quaternion.md#class-quaternion) that can be used elsewhere.

If root_motion_track is not a path to a track of type [Animation.TYPE_ROTATION_3D](class_animation.md#class-animation-constant-type-rotation-3d), returns `Quaternion(0, 0, 0, 1)`.

See also root_motion_track and [RootMotionView](class_rootmotionview.md#class-rootmotionview).

The most basic example is applying rotation to [CharacterBody3D](class_characterbody3d.md#class-characterbody3d):

GDScript

```gdscript
func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())
```

---

[Quaternion](class_quaternion.md#class-quaternion) **get_root_motion_rotation_accumulator**()

Retrieve the blended value of the rotation tracks with the root_motion_track as a [Quaternion](class_quaternion.md#class-quaternion) that can be used elsewhere.

This is necessary to apply the root motion position correctly, taking rotation into account. See also get_root_motion_position().

Also, this is useful in cases where you want to respect the initial key values of the animation.

For example, if an animation with only one key `Quaternion(0, 0, 0, 1)` is played in the previous frame and then an animation with only one key `Quaternion(0, 0.707, 0, 0.707)` is played in the next frame, the difference can be calculated as follows:

GDScript

```gdscript
var prev_root_motion_rotation_accumulator

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    var current_root_motion_rotation_accumulator = animation_tree.get_root_motion_rotation_accumulator()
    var difference = prev_root_motion_rotation_accumulator.inverse() * current_root_motion_rotation_accumulator
    prev_root_motion_rotation_accumulator = current_root_motion_rotation_accumulator
    transform.basis *=  Basis(difference)
```

However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.

---

[Vector3](class_vector3.md#class-vector3) **get_root_motion_scale**()

Retrieve the motion delta of scale with the root_motion_track as a [Vector3](class_vector3.md#class-vector3) that can be used elsewhere.

If root_motion_track is not a path to a track of type [Animation.TYPE_SCALE_3D](class_animation.md#class-animation-constant-type-scale-3d), returns `Vector3(0, 0, 0)`.

See also root_motion_track and [RootMotionView](class_rootmotionview.md#class-rootmotionview).

The most basic example is applying scale to [CharacterBody3D](class_characterbody3d.md#class-characterbody3d):

GDScript

```gdscript
var current_scale = Vector3(1, 1, 1)
var scale_accum = Vector3(1, 1, 1)

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        current_scale = get_scale()
        scale_accum = Vector3(1, 1, 1)
        state_machine.travel("Animate")
    scale_accum += animation_tree.get_root_motion_scale()
    set_scale(current_scale * scale_accum)
```

---

[Vector3](class_vector3.md#class-vector3) **get_root_motion_scale_accumulator**()

Retrieve the blended value of the scale tracks with the root_motion_track as a [Vector3](class_vector3.md#class-vector3) that can be used elsewhere.

For example, if an animation with only one key `Vector3(1, 1, 1)` is played in the previous frame and then an animation with only one key `Vector3(2, 2, 2)` is played in the next frame, the difference can be calculated as follows:

GDScript

```gdscript
var prev_root_motion_scale_accumulator

func _process(delta):
    if Input.is_action_just_pressed("animate"):
        state_machine.travel("Animate")
    var current_root_motion_scale_accumulator = animation_tree.get_root_motion_scale_accumulator()
    var difference = current_root_motion_scale_accumulator - prev_root_motion_scale_accumulator
    prev_root_motion_scale_accumulator = current_root_motion_scale_accumulator
    transform.basis = transform.basis.scaled(difference)
```

However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.

---

[bool](class_bool.md#class-bool) **has_animation**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if the **AnimationMixer** stores an [Animation](class_animation.md#class-animation) with key `name`.

---

[bool](class_bool.md#class-bool) **has_animation_library**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if the **AnimationMixer** stores an [AnimationLibrary](class_animationlibrary.md#class-animationlibrary) with key `name`.

---

 **remove_animation_library**(name: [StringName](class_stringname.md#class-stringname))

Removes the [AnimationLibrary](class_animationlibrary.md#class-animationlibrary) associated with the key `name`.

---

 **rename_animation_library**(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname))

Moves the [AnimationLibrary](class_animationlibrary.md#class-animationlibrary) associated with the key `name` to the key `newname`.
