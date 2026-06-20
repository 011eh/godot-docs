# AnimationTree

**Inherits:** [AnimationMixer](class_animationmixer.md#class-animationmixer) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node used for advanced animation transitions in an [AnimationPlayer](class_animationplayer.md#class-animationplayer).

## Description

A node used for advanced animation transitions in an [AnimationPlayer](class_animationplayer.md#class-animationplayer).

**Note:** When linked with an [AnimationPlayer](class_animationplayer.md#class-animationplayer), several properties and methods of the corresponding [AnimationPlayer](class_animationplayer.md#class-animationplayer) will not function as expected. Playback and transitions should be handled using only the **AnimationTree** and its constituent [AnimationNode](class_animationnode.md#class-animationnode)(s). The [AnimationPlayer](class_animationplayer.md#class-animationplayer) node should be used solely for adding, deleting, and editing animations.

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [NodePath](class_nodepath.md#class-nodepath)                                                               | advance_expression_base_node   | `NodePath(".")`                                                                                                |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [NodePath](class_nodepath.md#class-nodepath)                                                               | anim_player                                     | `NodePath("")`                                                                                                 |
| [AnimationCallbackModeDiscrete](class_animationmixer.md#enum-animationmixer-animationcallbackmodediscrete) | callback_mode_discrete                                                                       | `2` (overrides [AnimationMixer](class_animationmixer.md#class-animationmixer-property-callback-mode-discrete)) |
| [bool](class_bool.md#class-bool)                                                                           | deterministic                                                                                | `true` (overrides [AnimationMixer](class_animationmixer.md#class-animationmixer-property-deterministic))       |
| [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)                                    | tree_root                                         |                                                                                                                |

## Methods

| AnimationProcessCallback   | get_process_callback()                                                                               |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                            | set_process_callback(mode: AnimationProcessCallback) |

---

## Signals

**animation_player_changed**()

Emitted when the anim_player is changed.

---

## Enumerations

enum **AnimationProcessCallback**:

AnimationProcessCallback **ANIMATION_PROCESS_PHYSICS** = `0`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS](class_animationmixer.md#class-animationmixer-constant-animation-callback-mode-process-physics).

AnimationProcessCallback **ANIMATION_PROCESS_IDLE** = `1`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_IDLE](class_animationmixer.md#class-animationmixer-constant-animation-callback-mode-process-idle).

AnimationProcessCallback **ANIMATION_PROCESS_MANUAL** = `2`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_MANUAL](class_animationmixer.md#class-animationmixer-constant-animation-callback-mode-process-manual).

---

## Property Descriptions

[NodePath](class_nodepath.md#class-nodepath) **advance_expression_base_node** = `NodePath(".")`

-  **set_advance_expression_base_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_advance_expression_base_node**()

The path to the [Node](class_node.md#class-node) used to evaluate the [AnimationNode](class_animationnode.md#class-animationnode) [Expression](class_expression.md#class-expression) if one is not explicitly specified internally.

---

[NodePath](class_nodepath.md#class-nodepath) **anim_player** = `NodePath("")`

-  **set_animation_player**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_animation_player**()

The path to the [AnimationPlayer](class_animationplayer.md#class-animationplayer) used for animating.

---

[AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **tree_root**

-  **set_tree_root**(value: [AnimationRootNode](class_animationrootnode.md#class-animationrootnode))
- [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **get_tree_root**()

The root animation node of this **AnimationTree**. See [AnimationRootNode](class_animationrootnode.md#class-animationrootnode).

---

## Method Descriptions

AnimationProcessCallback **get_process_callback**()

**Deprecated:** Use [AnimationMixer.callback_mode_process](class_animationmixer.md#class-animationmixer-property-callback-mode-process) instead.

Returns the process notification in which to update animations.

---

 **set_process_callback**(mode: AnimationProcessCallback)

**Deprecated:** Use [AnimationMixer.callback_mode_process](class_animationmixer.md#class-animationmixer-property-callback-mode-process) instead.

Sets the process notification in which to update animations.
