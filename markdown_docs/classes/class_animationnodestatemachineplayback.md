# AnimationNodeStateMachinePlayback

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides playback control for an [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine).

## Description

Allows control of [AnimationTree](class_animationtree.md#class-animationtree) state machines created with [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine). Retrieve with `$AnimationTree.get("parameters/playback")`.

GDScript

```gdscript
var state_machine = $AnimationTree.get("parameters/playback")
state_machine.travel("some_state")
```

C#

```csharp
var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback").As<AnimationNodeStateMachinePlayback>();
stateMachine.Travel("some_state");
```

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

## Properties

| [bool](class_bool.md#class-bool)   | resource_local_to_scene   | `true` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene))   |
|------------------------------------|---------------------------|----------------------------------------------------------------------------------------------------|

## Methods

| [float](class_float.md#class-float)                                                     | get_current_length()                                                                                                |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StringName](class_stringname.md#class-stringname)                                      | get_current_node()                                                                                                    |
| [float](class_float.md#class-float)                                                     | get_current_play_position()                                                                                  |
| [float](class_float.md#class-float)                                                     | get_fading_from_length()                                                                                        |
| [StringName](class_stringname.md#class-stringname)                                      | get_fading_from_node()                                                                                            |
| [float](class_float.md#class-float)                                                     | get_fading_from_play_position()                                                                          |
| [float](class_float.md#class-float)                                                     | get_fading_length()                                                                                                  |
| [float](class_float.md#class-float)                                                     | get_fading_position()                                                                                              |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_travel_path()                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | is_playing()                                                                                                                |
|                                                                                         | next()                                                                                                                            |
|                                                                                         | start(node: [StringName](class_stringname.md#class-stringname), reset: [bool](class_bool.md#class-bool) = true)                  |
|                                                                                         | stop()                                                                                                                            |
|                                                                                         | travel(to_node: [StringName](class_stringname.md#class-stringname), reset_on_teleport: [bool](class_bool.md#class-bool) = true) |

---

## Signals

**state_finished**(state: [StringName](class_stringname.md#class-stringname))

Emitted when the `state` finishes playback. If `state` is a state machine set to grouped mode, its signals are passed through with its name prefixed.

If there is a crossfade, this will be fired when the influence of the get_fading_from_node() animation is no longer present.

---

**state_started**(state: [StringName](class_stringname.md#class-stringname))

Emitted when the `state` starts playback. If `state` is a state machine set to grouped mode, its signals are passed through with its name prefixed.

---

## Method Descriptions

[float](class_float.md#class-float) **get_current_length**()

Returns the current state length.

**Note:** It is possible that any [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) can be nodes as well as animations. This means that there can be multiple animations within a single state. Which animation length has priority depends on the nodes connected inside it. Also, if a transition does not reset, the remaining length at that point will be returned.

---

[StringName](class_stringname.md#class-stringname) **get_current_node**()

Returns the currently playing animation state.

**Note:** When using a cross-fade, the current state changes to the next state immediately after the cross-fade begins.

---

[float](class_float.md#class-float) **get_current_play_position**()

Returns the playback position within the current animation state.

---

[float](class_float.md#class-float) **get_fading_from_length**()

Returns the playback state length of the node from get_fading_from_node(). Returns `0` if no animation fade is occurring.

---

[StringName](class_stringname.md#class-stringname) **get_fading_from_node**()

Returns the starting state of currently fading animation.

---

[float](class_float.md#class-float) **get_fading_from_play_position**()

Returns the playback position of the node from get_fading_from_node(). Returns `0` if no animation fade is occurring.

---

[float](class_float.md#class-float) **get_fading_length**()

Returns the length of the current fade animation. Returns `0` if no animation fade is occurring.

---

[float](class_float.md#class-float) **get_fading_position**()

Returns the playback position of the current fade animation. Returns `0` if no animation fade is occurring.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_travel_path**()

Returns the current travel path as computed internally by the A\* algorithm.

---

[bool](class_bool.md#class-bool) **is_playing**()

Returns `true` if an animation is playing.

---

 **next**()

If there is a next path by travel or auto advance, immediately transitions from the current state to the next state.

---

 **start**(node: [StringName](class_stringname.md#class-stringname), reset: [bool](class_bool.md#class-bool) = true)

Starts playing the given animation.

If `reset` is `true`, the animation is played from the beginning.

---

 **stop**()

Stops the currently playing animation.

---

 **travel**(to_node: [StringName](class_stringname.md#class-stringname), reset_on_teleport: [bool](class_bool.md#class-bool) = true)

Transitions from the current state to another one, following the shortest path.

If the path does not connect from the current state, the animation will play after the state teleports.

If `reset_on_teleport` is `true`, the animation is played from the beginning when the travel cause a teleportation.
