# SceneState

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides access to a scene file's information.

## Description

Maintains a list of resources, nodes, exported and overridden properties, and built-in scripts associated with a scene. They cannot be modified from a **SceneState**, only accessed. Useful for peeking into what a [PackedScene](class_packedscene.md#class-packedscene) contains without instantiating it.

This class cannot be instantiated directly, it is retrieved for a given scene as the result of [PackedScene.get_state()](class_packedscene.md#class-packedscene-method-get-state).

## Methods

| SceneState                                         | get_base_scene_state()                                                                                  |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)                                     | get_connection_binds(idx: [int](class_int.md#class-int))                                                |
| [int](class_int.md#class-int)                                           | get_connection_count()                                                                                  |
| [int](class_int.md#class-int)                                           | get_connection_flags(idx: [int](class_int.md#class-int))                                                |
| [StringName](class_stringname.md#class-stringname)                      | get_connection_method(idx: [int](class_int.md#class-int))                                              |
| [StringName](class_stringname.md#class-stringname)                      | get_connection_signal(idx: [int](class_int.md#class-int))                                              |
| [NodePath](class_nodepath.md#class-nodepath)                            | get_connection_source(idx: [int](class_int.md#class-int))                                              |
| [NodePath](class_nodepath.md#class-nodepath)                            | get_connection_target(idx: [int](class_int.md#class-int))                                              |
| [int](class_int.md#class-int)                                           | get_connection_unbinds(idx: [int](class_int.md#class-int))                                            |
| [int](class_int.md#class-int)                                           | get_node_count()                                                                                              |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_node_groups(idx: [int](class_int.md#class-int))                                                          |
| [int](class_int.md#class-int)                                           | get_node_index(idx: [int](class_int.md#class-int))                                                            |
| [PackedScene](class_packedscene.md#class-packedscene)                   | get_node_instance(idx: [int](class_int.md#class-int))                                                      |
| [String](class_string.md#class-string)                                  | get_node_instance_placeholder(idx: [int](class_int.md#class-int))                              |
| [StringName](class_stringname.md#class-stringname)                      | get_node_name(idx: [int](class_int.md#class-int))                                                              |
| [NodePath](class_nodepath.md#class-nodepath)                            | get_node_owner_path(idx: [int](class_int.md#class-int))                                                  |
| [NodePath](class_nodepath.md#class-nodepath)                            | get_node_path(idx: [int](class_int.md#class-int), for_parent: [bool](class_bool.md#class-bool) = false)        |
| [int](class_int.md#class-int)                                           | get_node_property_count(idx: [int](class_int.md#class-int))                                          |
| [StringName](class_stringname.md#class-stringname)                      | get_node_property_name(idx: [int](class_int.md#class-int), prop_idx: [int](class_int.md#class-int))   |
| [Variant](class_variant.md#class-variant)                               | get_node_property_value(idx: [int](class_int.md#class-int), prop_idx: [int](class_int.md#class-int)) |
| [StringName](class_stringname.md#class-stringname)                      | get_node_type(idx: [int](class_int.md#class-int))                                                              |
| [String](class_string.md#class-string)                                  | get_path()                                                                                                          |
| [bool](class_bool.md#class-bool)                                        | is_node_instance_placeholder(idx: [int](class_int.md#class-int))                                |

---

## Enumerations

enum **GenEditState**:

GenEditState **GEN_EDIT_STATE_DISABLED** = `0`

If passed to [PackedScene.instantiate()](class_packedscene.md#class-packedscene-method-instantiate), blocks edits to the scene state.

GenEditState **GEN_EDIT_STATE_INSTANCE** = `1`

If passed to [PackedScene.instantiate()](class_packedscene.md#class-packedscene-method-instantiate), provides inherited scene resources to the local scene.

**Note:** Only available in editor builds.

GenEditState **GEN_EDIT_STATE_MAIN** = `2`

If passed to [PackedScene.instantiate()](class_packedscene.md#class-packedscene-method-instantiate), provides local scene resources to the local scene. Only the main scene should receive the main edit state.

**Note:** Only available in editor builds.

GenEditState **GEN_EDIT_STATE_MAIN_INHERITED** = `3`

If passed to [PackedScene.instantiate()](class_packedscene.md#class-packedscene-method-instantiate), it's similar to GEN_EDIT_STATE_MAIN, but for the case where the scene is being instantiated to be the base of another one.

**Note:** Only available in editor builds.

---

## Method Descriptions

SceneState **get_base_scene_state**()

Returns the **SceneState** of the scene that this scene inherits from, or `null` if it doesn't inherit from any scene.

---

[Array](class_array.md#class-array) **get_connection_binds**(idx: [int](class_int.md#class-int))

Returns the list of bound parameters for the signal at `idx`.

---

[int](class_int.md#class-int) **get_connection_count**()

Returns the number of signal connections in the scene.

The `idx` argument used to query connection metadata in other `get_connection_*` methods in the interval `[0, get_connection_count() - 1]`.

---

[int](class_int.md#class-int) **get_connection_flags**(idx: [int](class_int.md#class-int))

Returns the connection flags for the signal at `idx`. See [ConnectFlags](class_object.md#enum-object-connectflags) constants.

---

[StringName](class_stringname.md#class-stringname) **get_connection_method**(idx: [int](class_int.md#class-int))

Returns the method connected to the signal at `idx`.

---

[StringName](class_stringname.md#class-stringname) **get_connection_signal**(idx: [int](class_int.md#class-int))

Returns the name of the signal at `idx`.

---

[NodePath](class_nodepath.md#class-nodepath) **get_connection_source**(idx: [int](class_int.md#class-int))

Returns the path to the node that owns the signal at `idx`, relative to the root node.

---

[NodePath](class_nodepath.md#class-nodepath) **get_connection_target**(idx: [int](class_int.md#class-int))

Returns the path to the node that owns the method connected to the signal at `idx`, relative to the root node.

---

[int](class_int.md#class-int) **get_connection_unbinds**(idx: [int](class_int.md#class-int))

Returns the number of unbound parameters for the signal at `idx`.

---

[int](class_int.md#class-int) **get_node_count**()

Returns the number of nodes in the scene.

The `idx` argument used to query node data in other `get_node_*` methods in the interval `[0, get_node_count() - 1]`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_node_groups**(idx: [int](class_int.md#class-int))

Returns the list of group names associated with the node at `idx`.

---

[int](class_int.md#class-int) **get_node_index**(idx: [int](class_int.md#class-int))

Returns the node's index, which is its position relative to its siblings. This is only relevant and saved in scenes for cases where new nodes are added to an instantiated or inherited scene among siblings from the base scene. Despite the name, this index is not related to the `idx` argument used here and in other methods.

---

[PackedScene](class_packedscene.md#class-packedscene) **get_node_instance**(idx: [int](class_int.md#class-int))

Returns a [PackedScene](class_packedscene.md#class-packedscene) for the node at `idx` (i.e. the whole branch starting at this node, with its child nodes and resources), or `null` if the node is not an instance.

---

[String](class_string.md#class-string) **get_node_instance_placeholder**(idx: [int](class_int.md#class-int))

Returns the path to the represented scene file if the node at `idx` is an [InstancePlaceholder](class_instanceplaceholder.md#class-instanceplaceholder).

---

[StringName](class_stringname.md#class-stringname) **get_node_name**(idx: [int](class_int.md#class-int))

Returns the name of the node at `idx`.

---

[NodePath](class_nodepath.md#class-nodepath) **get_node_owner_path**(idx: [int](class_int.md#class-int))

Returns the path to the owner of the node at `idx`, relative to the root node.

---

[NodePath](class_nodepath.md#class-nodepath) **get_node_path**(idx: [int](class_int.md#class-int), for_parent: [bool](class_bool.md#class-bool) = false)

Returns the path to the node at `idx`.

If `for_parent` is `true`, returns the path of the `idx` node's parent instead.

---

[int](class_int.md#class-int) **get_node_property_count**(idx: [int](class_int.md#class-int))

Returns the number of exported or overridden properties for the node at `idx`.

The `prop_idx` argument used to query node property data in other `get_node_property_*` methods in the interval `[0, get_node_property_count() - 1]`.

---

[StringName](class_stringname.md#class-stringname) **get_node_property_name**(idx: [int](class_int.md#class-int), prop_idx: [int](class_int.md#class-int))

Returns the name of the property at `prop_idx` for the node at `idx`.

---

[Variant](class_variant.md#class-variant) **get_node_property_value**(idx: [int](class_int.md#class-int), prop_idx: [int](class_int.md#class-int))

Returns the value of the property at `prop_idx` for the node at `idx`.

---

[StringName](class_stringname.md#class-stringname) **get_node_type**(idx: [int](class_int.md#class-int))

Returns the type of the node at `idx`.

---

[String](class_string.md#class-string) **get_path**()

Returns the resource path to the represented [PackedScene](class_packedscene.md#class-packedscene).

---

[bool](class_bool.md#class-bool) **is_node_instance_placeholder**(idx: [int](class_int.md#class-int))

Returns `true` if the node at `idx` is an [InstancePlaceholder](class_instanceplaceholder.md#class-instanceplaceholder).
