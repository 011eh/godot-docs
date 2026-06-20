# AnimationLibrary

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Container for [Animation](class_animation.md#class-animation) resources.

## Description

An animation library stores a set of animations accessible through [StringName](class_stringname.md#class-stringname) keys, for use with [AnimationPlayer](class_animationplayer.md#class-animationplayer) nodes.

## Tutorials

- [Animation tutorial index](../tutorials/animation/index.md)

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)                                   | add_animation(name: [StringName](class_stringname.md#class-stringname), animation: [Animation](class_animation.md#class-animation))        |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Animation](class_animation.md#class-animation)                                         | get_animation(name: [StringName](class_stringname.md#class-stringname))                                                                    |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_animation_list()                                                                                                                  |
| [int](class_int.md#class-int)                                                           | get_animation_list_size()                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | has_animation(name: [StringName](class_stringname.md#class-stringname))                                                                    |
|                                                                                         | remove_animation(name: [StringName](class_stringname.md#class-stringname))                                                              |
|                                                                                         | rename_animation(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname)) |

---

## Signals

**animation_added**(anim_name: [StringName](class_stringname.md#class-stringname))

Emitted when an [Animation](class_animation.md#class-animation) is added, under the key `anim_name`.

---

**animation_changed**(anim_name: [StringName](class_stringname.md#class-stringname))

Emitted when there's a change in one of the animations, e.g. tracks are added, moved or have changed paths. `anim_name` is the key of the animation that was changed.

See also [Resource.changed](class_resource.md#class-resource-signal-changed), which this acts as a relay for.

---

**animation_removed**(anim_name: [StringName](class_stringname.md#class-stringname))

Emitted when an [Animation](class_animation.md#class-animation) stored with the key `anim_name` is removed.

---

**animation_renamed**(old_name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname))

Emitted when the key for an [Animation](class_animation.md#class-animation) is changed, from `old_name` to `new_name`.

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **add_animation**(name: [StringName](class_stringname.md#class-stringname), animation: [Animation](class_animation.md#class-animation))

Adds the `animation` to the library, accessible by the key `name`.

---

[Animation](class_animation.md#class-animation) **get_animation**(name: [StringName](class_stringname.md#class-stringname))

Returns the [Animation](class_animation.md#class-animation) with the key `name`. If the animation does not exist, `null` is returned and an error is logged.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_animation_list**()

Returns the keys for the [Animation](class_animation.md#class-animation)s stored in the library.

---

[int](class_int.md#class-int) **get_animation_list_size**()

Returns the key count for the [Animation](class_animation.md#class-animation)s stored in the library.

---

[bool](class_bool.md#class-bool) **has_animation**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if the library stores an [Animation](class_animation.md#class-animation) with `name` as the key.

---

 **remove_animation**(name: [StringName](class_stringname.md#class-stringname))

Removes the [Animation](class_animation.md#class-animation) with the key `name`.

---

 **rename_animation**(name: [StringName](class_stringname.md#class-stringname), newname: [StringName](class_stringname.md#class-stringname))

Changes the key of the [Animation](class_animation.md#class-animation) associated with the key `name` to `newname`.
