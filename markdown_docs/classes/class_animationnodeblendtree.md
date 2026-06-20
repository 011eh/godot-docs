# AnimationNodeBlendTree

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) **<** [AnimationNode](class_animationnode.md#class-animationnode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A sub-tree of many type [AnimationNode](class_animationnode.md#class-animationnode)s used for complex animations. Used by [AnimationTree](class_animationtree.md#class-animationtree).

## Description

This animation node may contain a sub-tree of any other type animation nodes, such as [AnimationNodeTransition](class_animationnodetransition.md#class-animationnodetransition), [AnimationNodeBlend2](class_animationnodeblend2.md#class-animationnodeblend2), [AnimationNodeBlend3](class_animationnodeblend3.md#class-animationnodeblend3), [AnimationNodeOneShot](class_animationnodeoneshot.md#class-animationnodeoneshot), etc. This is one of the most commonly used animation node roots.

An [AnimationNodeOutput](class_animationnodeoutput.md#class-animationnodeoutput) node named `output` is created by default.

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

## Properties

| [Vector2](class_vector2.md#class-vector2)   | graph_offset   | `Vector2(0, 0)`   |
|---------------------------------------------|-----------------------------------------------------------------------|-------------------|

## Methods

|                                                                                         | add_node(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))   |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                         | connect_node(input_node: [StringName](class_stringname.md#class-stringname), input_index: [int](class_int.md#class-int), output_node: [StringName](class_stringname.md#class-stringname))                |
|                                                                                         | disconnect_node(input_node: [StringName](class_stringname.md#class-stringname), input_index: [int](class_int.md#class-int))                                                                           |
| [AnimationNode](class_animationnode.md#class-animationnode)                             | get_node(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                           |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_node_list()                                                                                                                                                                                         |
| [Vector2](class_vector2.md#class-vector2)                                               | get_node_position(name: [StringName](class_stringname.md#class-stringname))                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | has_node(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                           |
|                                                                                         | remove_node(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                     |
|                                                                                         | rename_node(name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname))                                                                       |
|                                                                                         | set_node_position(name: [StringName](class_stringname.md#class-stringname), position: [Vector2](class_vector2.md#class-vector2))                                                                    |

---

## Signals

**node_changed**(node_name: [StringName](class_stringname.md#class-stringname))

Emitted when the input port information is changed.

---

## Constants

**CONNECTION_OK** = `0`

The connection was successful.

**CONNECTION_ERROR_NO_INPUT** = `1`

The input node is `null`.

**CONNECTION_ERROR_NO_INPUT_INDEX** = `2`

The specified input port is out of range.

**CONNECTION_ERROR_NO_OUTPUT** = `3`

The output node is `null`.

**CONNECTION_ERROR_SAME_NODE** = `4`

Input and output nodes are the same.

**CONNECTION_ERROR_CONNECTION_EXISTS** = `5`

The specified connection already exists.

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **graph_offset** = `Vector2(0, 0)`

-  **set_graph_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_graph_offset**()

The global offset of all sub animation nodes.

---

## Method Descriptions

 **add_node**(name: [StringName](class_stringname.md#class-stringname), node: [AnimationNode](class_animationnode.md#class-animationnode), position: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Adds an [AnimationNode](class_animationnode.md#class-animationnode) at the given `position`. The `name` is used to identify the created sub animation node later.

---

 **connect_node**(input_node: [StringName](class_stringname.md#class-stringname), input_index: [int](class_int.md#class-int), output_node: [StringName](class_stringname.md#class-stringname))

Connects the output of an [AnimationNode](class_animationnode.md#class-animationnode) as input for another [AnimationNode](class_animationnode.md#class-animationnode), at the input port specified by `input_index`.

---

 **disconnect_node**(input_node: [StringName](class_stringname.md#class-stringname), input_index: [int](class_int.md#class-int))

Disconnects the animation node connected to the specified input.

---

[AnimationNode](class_animationnode.md#class-animationnode) **get_node**(name: [StringName](class_stringname.md#class-stringname))

Returns the sub animation node with the specified `name`.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_node_list**()

Returns a list containing the names of all sub animation nodes in this blend tree.

---

[Vector2](class_vector2.md#class-vector2) **get_node_position**(name: [StringName](class_stringname.md#class-stringname))

Returns the position of the sub animation node with the specified `name`.

---

[bool](class_bool.md#class-bool) **has_node**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if a sub animation node with specified `name` exists.

---

 **remove_node**(name: [StringName](class_stringname.md#class-stringname))

Removes a sub animation node.

---

 **rename_node**(name: [StringName](class_stringname.md#class-stringname), new_name: [StringName](class_stringname.md#class-stringname))

Changes the name of a sub animation node.

---

 **set_node_position**(name: [StringName](class_stringname.md#class-stringname), position: [Vector2](class_vector2.md#class-vector2))

Modifies the position of a sub animation node.
