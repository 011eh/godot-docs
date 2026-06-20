# AnimationNodeStateMachine

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A state machine with multiple [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s, used by [AnimationTree](class_animationtree.md#class-animationtree).

## Description

Contains multiple [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)s representing animation states, connected in a graph. State transitions can be configured to happen automatically or via code, using a shortest-path algorithm. Retrieve the [AnimationNodeStateMachinePlayback](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback) object from the [AnimationTree](class_animationtree.md#class-animationtree) node to control it programmatically.

GDScript

```gdscript
var state_machine = $AnimationTree.get("parameters/playback")
state_machine.travel("some_state")
```

C#

```csharp
var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback") as AnimationNodeStateMachinePlayback;
stateMachine.Travel("some_state");
```

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

## Properties

| [bool](class_bool.md#class-bool)                                     | allow_transition_to_self   | `false`   |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-----------|
| [bool](class_bool.md#class-bool)                                     | reset_ends                               | `false`   |
| StateMachineType | state_machine_type               | `0`       |

## Methods

|                                                                                                                               | add_node(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                               | add_transition(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname), transition: [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition)) |
| [Vector2](class_vector2.md#class-vector2)                                                                                     | get_graph_offset()                                                                                                                                                                                                                                                        |
| [AnimationNode](class_animationnode.md#class-animationnode)                                                                   | get_node(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)]                                       | get_node_list()                                                                                                                                                                                                                                                              |
| [StringName](class_stringname.md#class-stringname)                                                                            | get_node_name(node: [AnimationNode](class_animationnode.md#class-animationnode))                                                                                                                                                                                             |
| [Vector2](class_vector2.md#class-vector2)                                                                                     | get_node_position(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                              |
| [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition) | get_transition(idx: [int](class_int.md#class-int))                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                                                                                 | get_transition_count()                                                                                                                                                                                                                                                |
| [StringName](class_stringname.md#class-stringname)                                                                            | get_transition_from(idx: [int](class_int.md#class-int))                                                                                                                                                                                                                |
| [StringName](class_stringname.md#class-stringname)                                                                            | get_transition_to(idx: [int](class_int.md#class-int))                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                                                              | has_node(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                                                              | has_transition(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname))                                                                                                                                            |
|                                                                                                                               | remove_node(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                          |
|                                                                                                                               | remove_transition(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname))                                                                                                                                      |
|                                                                                                                               | remove_transition_by_index(idx: [int](class_int.md#class-int))                                                                                                                                                                                                  |
|                                                                                                                               | rename_node(name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname))                                                                                                                                            |
|                                                                                                                               | replace_node(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode))                                                                                                                                     |
|                                                                                                                               | set_graph_offset(offset: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                       |
|                                                                                                                               | set_node_position(name: [StringName](class_stringname.md#class-stringname), position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                         |

---

## Enumerations

enum **StateMachineType**:

StateMachineType **STATE_MACHINE_TYPE_ROOT** = `0`

Seeking to the beginning is treated as playing from the start state. Transition to the end state is treated as exiting the state machine.

StateMachineType **STATE_MACHINE_TYPE_NESTED** = `1`

Seeking to the beginning is treated as seeking to the beginning of the animation in the current state. Transition to the end state, or the absence of transitions in each state, is treated as exiting the state machine.

StateMachineType **STATE_MACHINE_TYPE_GROUPED** = `2`

This is a grouped state machine that can be controlled from a parent state machine. It does not work independently. There must be a state machine with state_machine_type of STATE_MACHINE_TYPE_ROOT or STATE_MACHINE_TYPE_NESTED in the parent or ancestor.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_transition_to_self** = `false`

-  **set_allow_transition_to_self**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_allow_transition_to_self**()

If `true`, allows teleport to the self state with [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel). When the reset option is enabled in [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class-animationnodestatemachineplayback-method-travel), the animation is restarted. If `false`, nothing happens on the teleportation to the self state.

---

[bool](class_bool.md#class-bool) **reset_ends** = `false`

-  **set_reset_ends**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_ends_reset**()

If `true`, treat the cross-fade to the start and end nodes as a blend with the RESET animation.

In most cases, when additional cross-fades are performed in the parent [AnimationNode](class_animationnode.md#class-animationnode) of the state machine, setting this property to `false` and matching the cross-fade time of the parent [AnimationNode](class_animationnode.md#class-animationnode) and the state machine's start node and end node gives good results.

---

StateMachineType **state_machine_type** = `0`

-  **set_state_machine_type**(value: StateMachineType)
- StateMachineType **get_state_machine_type**()

This property can define the process of transitions for different use cases. See also StateMachineType.

---

## Method Descriptions

 **add_node**(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Adds a new animation node to the graph. The `position` is used for display in the editor.

---

 **add_transition**(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname), transition: [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition))

Adds a transition between the given animation nodes.

---

[Vector2](class_vector2.md#class-vector2) **get_graph_offset**()

Returns the draw offset of the graph. Used for display in the editor.

---

[AnimationNode](class_animationnode.md#class-animationnode) **get_node**(name: [StringName](class_stringname.md#class-stringname))

Returns the animation node with the given name.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_node_list**()

Returns a list containing the names of all animation nodes in this state machine.

---

[StringName](class_stringname.md#class-stringname) **get_node_name**(node: [AnimationNode](class_animationnode.md#class-animationnode))

Returns the given animation node's name.

---

[Vector2](class_vector2.md#class-vector2) **get_node_position**(name: [StringName](class_stringname.md#class-stringname))

Returns the given animation node's coordinates. Used for display in the editor.

---

[AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class-animationnodestatemachinetransition) **get_transition**(idx: [int](class_int.md#class-int))

Returns the given transition.

---

[int](class_int.md#class-int) **get_transition_count**()

Returns the number of connections in the graph.

---

[StringName](class_stringname.md#class-stringname) **get_transition_from**(idx: [int](class_int.md#class-int))

Returns the given transition's start node.

---

[StringName](class_stringname.md#class-stringname) **get_transition_to**(idx: [int](class_int.md#class-int))

Returns the given transition's end node.

---

[bool](class_bool.md#class-bool) **has_node**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if the graph contains the given animation node.

---

[bool](class_bool.md#class-bool) **has_transition**(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname))

Returns `true` if there is a transition between the given animation nodes.

---

 **remove_node**(name: [StringName](class_stringname.md#class-stringname))

Deletes the given animation node from the graph.

---

 **remove_transition**(from: [StringName](class_stringname.md#class-stringname), to: [StringName](class_stringname.md#class-stringname))

Deletes the transition between the two specified animation nodes.

---

 **remove_transition_by_index**(idx: [int](class_int.md#class-int))

Deletes the given transition by index.

---

 **rename_node**(name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname))

Renames the given animation node.

---

 **replace_node**(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode))

Replaces the given animation node with a new animation node.

---

 **set_graph_offset**(offset: [Vector2](class_vector2.md#class-vector2))

Sets the draw offset of the graph. Used for display in the editor.

---

 **set_node_position**(name: [StringName](class_stringname.md#class-stringname), position: [Vector2](class_vector2.md#class-vector2))

Sets the animation node's coordinates. Used for display in the editor.
