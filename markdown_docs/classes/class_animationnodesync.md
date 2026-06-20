# AnimationNodeSync

**Inherits:** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AnimationNodeAdd2](class_animationnodeadd2.md#class-animationnodeadd2), [AnimationNodeAdd3](class_animationnodeadd3.md#class-animationnodeadd3), [AnimationNodeBlend2](class_animationnodeblend2.md#class-animationnodeblend2), [AnimationNodeBlend3](class_animationnodeblend3.md#class-animationnodeblend3), [AnimationNodeOneShot](class_animationnodeoneshot.md#class-animationnodeoneshot), [AnimationNodeSub2](class_animationnodesub2.md#class-animationnodesub2), [AnimationNodeTransition](class_animationnodetransition.md#class-animationnodetransition)

Base class for [AnimationNode](class_animationnode.md#class-animationnode)s with multiple input ports that must be synchronized.

## Description

An animation node used to combine, mix, or blend two or more animations together while keeping them synchronized within an [AnimationTree](class_animationtree.md#class-animationtree).

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

## Properties

| [bool](class_bool.md#class-bool)   | sync   | `false`   |
|------------------------------------|--------------------------------------------------|-----------|

---

## Property Descriptions

[bool](class_bool.md#class-bool) **sync** = `false`

-  **set_use_sync**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_sync**()

If `false`, the blended animations' frame are stopped when the blend value is `0`.

If `true`, forcing the blended animations to advance frame.
