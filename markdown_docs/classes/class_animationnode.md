# AnimationNode

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AnimationNodeExtension](class_animationnodeextension.md#class-animationnodeextension), [AnimationNodeOutput](class_animationnodeoutput.md#class-animationnodeoutput), [AnimationNodeSync](class_animationnodesync.md#class-animationnodesync), [AnimationNodeTimeScale](class_animationnodetimescale.md#class-animationnodetimescale), [AnimationNodeTimeSeek](class_animationnodetimeseek.md#class-animationnodetimeseek), [AnimationRootNode](class_animationrootnode.md#class-animationrootnode)

Base class for [AnimationTree](class_animationtree.md#class-animationtree) nodes. Not related to scene nodes.

## Description

Base resource for [AnimationTree](class_animationtree.md#class-animationtree) nodes. In general, it's not used directly, but you can create custom ones with custom blending formulas.

Inherit this when creating animation nodes mainly for use in [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree), otherwise [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) should be used instead.

You can access the time information as read-only parameter which is processed and stored in the previous frame for all nodes except [AnimationNodeOutput](class_animationnodeoutput.md#class-animationnodeoutput).

**Note:** If multiple inputs exist in the **AnimationNode**, which time information takes precedence depends on the type of **AnimationNode**.

```gdscript
var current_length = $AnimationTree["parameters/AnimationNodeName/current_length"]
var current_position = $AnimationTree["parameters/AnimationNodeName/current_position"]
var current_delta = $AnimationTree["parameters/AnimationNodeName/current_delta"]
```

## Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

## Properties

| [bool](class_bool.md#class-bool)   | filter_enabled   |
|------------------------------------|------------------------------------------------------------------|

## Methods

| [String](class_string.md#class-string)             | \_get_caption()                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AnimationNode              | \_get_child_by_name(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                              |
| [Dictionary](class_dictionary.md#class-dictionary) | \_get_child_nodes()                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Variant](class_variant.md#class-variant)          | \_get_parameter_default_value(parameter: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                     |
| [Array](class_array.md#class-array)                | \_get_parameter_list()                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                   | \_has_filter()                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                   | \_is_parameter_read_only(parameter: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                | \_process(time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), test_only: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                   | add_input(name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                    | blend_animation(animation: [StringName](class_stringname.md#class-stringname), time: [float](class_float.md#class-float), delta: [float](class_float.md#class-float), seeked: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), looped_flag: [LoopedFlag](class_animation.md#enum-animation-loopedflag) = 0)                                                                      |
| [float](class_float.md#class-float)                | blend_input(input_index: [int](class_int.md#class-int), time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), filter: FilterAction = 0, sync: [bool](class_bool.md#class-bool) = true, test_only: [bool](class_bool.md#class-bool) = false)                                                          |
| [float](class_float.md#class-float)                | blend_node(name: [StringName](class_stringname.md#class-stringname), node: AnimationNode, time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), filter: FilterAction = 0, sync: [bool](class_bool.md#class-bool) = true, test_only: [bool](class_bool.md#class-bool) = false) |
| [int](class_int.md#class-int)                      | find_input(name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                      | get_input_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [String](class_string.md#class-string)             | get_input_name(input: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Variant](class_variant.md#class-variant)          | get_parameter(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                      | get_processing_animation_tree_instance_id()                                                                                                                                                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                   | is_path_filtered(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                                                                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                   | is_process_testing()                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                    | remove_input(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                    | set_filter_path(path: [NodePath](class_nodepath.md#class-nodepath), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                   | set_input_name(input: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                    |
|                                                    | set_parameter(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                              |

---

## Signals

**animation_node_removed**(object_id: [int](class_int.md#class-int), node_name: [String](class_string.md#class-string))

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes removes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine), and [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

---

**animation_node_renamed**(object_id: [int](class_int.md#class-int), old_name: [String](class_string.md#class-string), new_name: [String](class_string.md#class-string))

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation node names changes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine), and [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

---

**node_updated**(object_id: [int](class_int.md#class-int))

**Experimental:** This signal may be changed or removed in future versions.

Emitted by [AnimationNodeAnimation](class_animationnodeanimation.md#class-animationnodeanimation) when its [AnimationNodeAnimation.animation](class_animationnodeanimation.md#class-animationnodeanimation-property-animation) resource is changed, or by [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree) when its connections change.

---

**tree_changed**()

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes changes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class-animationnodeblendspace1d), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class-animationnodeblendspace2d), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class-animationnodestatemachine), [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree) and [AnimationNodeTransition](class_animationnodetransition.md#class-animationnodetransition).

---

## Enumerations

enum **FilterAction**:

FilterAction **FILTER_IGNORE** = `0`

Do not use filtering.

FilterAction **FILTER_PASS** = `1`

Paths matching the filter will be allowed to pass.

FilterAction **FILTER_STOP** = `2`

Paths matching the filter will be discarded.

FilterAction **FILTER_BLEND** = `3`

Paths matching the filter will be blended (by the blend value).

---

## Property Descriptions

[bool](class_bool.md#class-bool) **filter_enabled**

-  **set_filter_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_filter_enabled**()

If `true`, filtering is enabled.

---

## Method Descriptions

[String](class_string.md#class-string) **\_get_caption**()

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to override the text caption for this animation node.

---

AnimationNode **\_get_child_by_name**(name: [StringName](class_stringname.md#class-stringname))

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return a child animation node by its `name`.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_child_nodes**()

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return all child animation nodes in order as a `name: node` dictionary.

---

[Variant](class_variant.md#class-variant) **\_get_parameter_default_value**(parameter: [StringName](class_stringname.md#class-stringname))

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return the default value of a `parameter`. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---

[Array](class_array.md#class-array) **\_get_parameter_list**()

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return a list of the properties on this animation node. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees. Format is similar to [Object.get_property_list()](class_object.md#class-object-method-get-property-list).

---

[bool](class_bool.md#class-bool) **\_has_filter**()

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return whether the blend tree editor should display filter editing on this animation node.

---

[bool](class_bool.md#class-bool) **\_is_parameter_read_only**(parameter: [StringName](class_stringname.md#class-stringname))

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to return whether the `parameter` is read-only. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---

[float](class_float.md#class-float) **\_process**(time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), test_only: [bool](class_bool.md#class-bool))

**Deprecated:** Currently this is mostly useless as there is a lack of many APIs to extend AnimationNode by GDScript. It is planned that a more flexible API using structures will be provided in the future.

When inheriting from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode), implement this virtual method to run some code when this animation node is processed. The `time` parameter is a relative delta, unless `seek` is `true`, in which case it is absolute.

Here, call the blend_input(), blend_node() or blend_animation() functions. You can also use get_parameter() and set_parameter() to modify local memory.

This function should return the delta.

---

[bool](class_bool.md#class-bool) **add_input**(name: [String](class_string.md#class-string))

Adds an input to the animation node. This is only useful for animation nodes created for use in an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree). If the addition fails, returns `false`.

---

 **blend_animation**(animation: [StringName](class_stringname.md#class-stringname), time: [float](class_float.md#class-float), delta: [float](class_float.md#class-float), seeked: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), looped_flag: [LoopedFlag](class_animation.md#enum-animation-loopedflag) = 0)

Blends an animation by `blend` amount (name must be valid in the linked [AnimationPlayer](class_animationplayer.md#class-animationplayer)). A `time` and `delta` may be passed, as well as whether `seeked` happened.

A `looped_flag` is used by internal processing immediately after the loop.

---

[float](class_float.md#class-float) **blend_input**(input_index: [int](class_int.md#class-int), time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), filter: FilterAction = 0, sync: [bool](class_bool.md#class-bool) = true, test_only: [bool](class_bool.md#class-bool) = false)

Blends an input. This is only useful for animation nodes created for an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree). The `time` parameter is a relative delta, unless `seek` is `true`, in which case it is absolute. A filter mode may be optionally passed.

---

[float](class_float.md#class-float) **blend_node**(name: [StringName](class_stringname.md#class-stringname), node: AnimationNode, time: [float](class_float.md#class-float), seek: [bool](class_bool.md#class-bool), is_external_seeking: [bool](class_bool.md#class-bool), blend: [float](class_float.md#class-float), filter: FilterAction = 0, sync: [bool](class_bool.md#class-bool) = true, test_only: [bool](class_bool.md#class-bool) = false)

Blend another animation node (in case this animation node contains child animation nodes). This function is only useful if you inherit from [AnimationRootNode](class_animationrootnode.md#class-animationrootnode) instead, otherwise editors will not display your animation node for addition.

---

[int](class_int.md#class-int) **find_input**(name: [String](class_string.md#class-string))

Returns the input index which corresponds to `name`. If not found, returns `-1`.

---

[int](class_int.md#class-int) **get_input_count**()

Amount of inputs in this animation node, only useful for animation nodes that go into [AnimationNodeBlendTree](class_animationnodeblendtree.md#class-animationnodeblendtree).

---

[String](class_string.md#class-string) **get_input_name**(input: [int](class_int.md#class-int))

Gets the name of an input by index.

---

[Variant](class_variant.md#class-variant) **get_parameter**(name: [StringName](class_stringname.md#class-stringname))

Gets the value of a parameter. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.

---

[int](class_int.md#class-int) **get_processing_animation_tree_instance_id**()

Returns the object id of the [AnimationTree](class_animationtree.md#class-animationtree) that owns this node.

**Note:** This method should only be called from within the [AnimationNodeExtension._process_animation_node()](class_animationnodeextension.md#class-animationnodeextension-private-method-process-animation-node) method, and will return an invalid id otherwise.

---

[bool](class_bool.md#class-bool) **is_path_filtered**(path: [NodePath](class_nodepath.md#class-nodepath))

Returns `true` if the given path is filtered.

---

[bool](class_bool.md#class-bool) **is_process_testing**()

Returns `true` if this animation node is being processed in test-only mode.

---

 **remove_input**(index: [int](class_int.md#class-int))

Removes an input, call this only when inactive.

---

 **set_filter_path**(path: [NodePath](class_nodepath.md#class-nodepath), enable: [bool](class_bool.md#class-bool))

Adds or removes a path for the filter.

---

[bool](class_bool.md#class-bool) **set_input_name**(input: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets the name of the input at the given `input` index. If the setting fails, returns `false`.

---

 **set_parameter**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Sets a custom parameter. These are used as local memory, because resources can be reused across the tree or scenes.
