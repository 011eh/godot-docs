# AnimationNodeStateMachineTransition

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A transition within an [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine) connecting two [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s.

## Description

The path generated when using [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel) is limited to the nodes connected by **AnimationNodeStateMachineTransition**.

You can set the timing and conditions of the transition in detail.

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

## Properties

| [StringName](class_stringname.md#class-stringname)                   | advance_condition   | `&""`   |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------|
| [String](class_string.md#class-string)                               | advance_expression | `""`    |
| AdvanceMode | advance_mode             | `1`     |
| [bool](class_bool.md#class-bool)                                     | break_loop_at_end   | `false` |
| [int](class_int.md#class-int)                                        | priority                     | `1`     |
| [bool](class_bool.md#class-bool)                                     | reset                           | `true`  |
| SwitchMode   | switch_mode               | `0`     |
| [Curve](class_curve.md#class-curve)                                  | xfade_curve               |         |
| [float](class_float.md#class-float)                                  | xfade_time                 | `0.0`   |

---

## Signals

**advance_condition_changed**()

Emitted when advance_condition is changed.

---

## Enumerations

enum **SwitchMode**:

SwitchMode **SWITCH_MODE_IMMEDIATE** = `0`

Switch to the next state immediately. The current state will end and blend into the beginning of the new one.

SwitchMode **SWITCH_MODE_SYNC** = `1`

Switch to the next state immediately, but will seek the new state to the playback position of the old state.

SwitchMode **SWITCH_MODE_AT_END** = `2`

Wait for the current state playback to end, then switch to the beginning of the next state animation.

---

enum **AdvanceMode**:

AdvanceMode **ADVANCE_MODE_DISABLED** = `0`

Don't use this transition.

AdvanceMode **ADVANCE_MODE_ENABLED** = `1`

Only use this transition during [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel).

AdvanceMode **ADVANCE_MODE_AUTO** = `2`

Automatically use this transition if the advance_condition and advance_expression checks are `true` (if assigned).

---

## Property Descriptions

[StringName](class_stringname.md#class-stringname) **advance_condition** = `&""`

-  **set_advance_condition**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_advance_condition**()

Turn on auto advance when this condition is set. The provided name will become a boolean parameter on the [AnimationTree](class_animationtree.md#class-animationtree) that can be controlled from code (see [Using AnimationTree](../tutorials/animation/animation_tree.html#controlling-from-code)). For example, if [AnimationTree.tree_root](class_animationtree.md#class-animationtree-property-tree-root) is an [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine) and advance_condition is set to `"idle"`:

GDScript

```gdscript
$animation_tree.set("parameters/conditions/idle", is_on_floor and (linear_velocity.x == 0))
```

C#

```csharp
GetNode<AnimationTree>("animation_tree").Set("parameters/conditions/idle", IsOnFloor && (LinearVelocity.X == 0));
```

---

[String](class_string.md#class-string) **advance_expression** = `""`

-  **set_advance_expression**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_advance_expression**()

Use an expression as a condition for state machine transitions. It is possible to create complex animation advance conditions for switching between states and gives much greater flexibility for creating complex state machines by directly interfacing with the script code.

---

AdvanceMode **advance_mode** = `1`

-  **set_advance_mode**(value: AdvanceMode)
- AdvanceMode **get_advance_mode**()

Determines whether the transition should be disabled, enabled when using [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel), or traversed automatically if the advance_condition and advance_expression checks are `true` (if assigned).

---

[bool](class_bool.md#class-bool) **break_loop_at_end** = `false`

-  **set_break_loop_at_end**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_loop_broken_at_end**()

If `true`, breaks the loop at the end of the loop cycle for transition, even if the animation is looping.

---

[int](class_int.md#class-int) **priority** = `1`

-  **set_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_priority**()

Lower priority transitions are preferred when travelling through the tree via [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel) or advance_mode is set to ADVANCE_MODE_AUTO.

---

[bool](class_bool.md#class-bool) **reset** = `true`

-  **set_reset**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_reset**()

If `true`, the destination animation is played back from the beginning when switched.

---

SwitchMode **switch_mode** = `0`

-  **set_switch_mode**(value: SwitchMode)
- SwitchMode **get_switch_mode**()

The transition type.

---

[Curve](class_curve.md#class-curve) **xfade_curve**

-  **set_xfade_curve**(value: [Curve](class_curve.md#class-curve))
- [Curve](class_curve.md#class-curve) **get_xfade_curve**()

Ease curve for better control over cross-fade between this state and the next. Should be a unit [Curve](class_curve.md#class-curve).

---

[float](class_float.md#class-float) **xfade_time** = `0.0`

-  **set_xfade_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_xfade_time**()

The time to cross-fade between this state and the next.

**Note:** [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine) transitions the current state immediately after the start of the fading. The precise remaining time can only be inferred from the main animation. When [AnimationNodeOutput](class_animationnodeoutput.md#class-animationnodeoutput) is considered as the most upstream, so the xfade_time is not scaled depending on the downstream delta. See also [AnimationNodeOneShot.fadeout_time](class_animationnodeoneshot.md#class-animationnodeoneshot-property-fadeout-time).
