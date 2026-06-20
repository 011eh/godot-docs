# MultiplayerSynchronizer

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Synchronizes properties from the multiplayer authority to the remote peers.

## Description

By default, **MultiplayerSynchronizer** synchronizes configured properties to all peers.

Visibility can be handled directly with set_visibility_for() or as-needed with add_visibility_filter() and update_visibility().

[MultiplayerSpawner](class_multiplayerspawner.md#class-multiplayerspawner)s will handle nodes according to visibility of synchronizers as long as the node at root_path was spawned by one.

Internally, **MultiplayerSynchronizer** uses [MultiplayerAPI.object_configuration_add()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-add) to notify synchronization start passing the [Node](class_node.md#class-node) at root_path as the `object` and itself as the `configuration`, and uses [MultiplayerAPI.object_configuration_remove()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-remove) to notify synchronization end in a similar way.

**Note:** Synchronization is not supported for [Object](class_object.md#class-object) type properties, like [Resource](class_resource.md#class-resource). Properties that are unique to each peer, like the instance IDs of [Object](class_object.md#class-object)s (see [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id)) or [RID](class_rid.md#class-rid)s, will also not work in synchronization.

## Properties

| [float](class_float.md#class-float)                                                    | delta_interval                 | `0.0`            |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------|
| [bool](class_bool.md#class-bool)                                                       | public_visibility           | `true`           |
| [SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig) | replication_config         |                  |
| [float](class_float.md#class-float)                                                    | replication_interval     | `0.0`            |
| [NodePath](class_nodepath.md#class-nodepath)                                           | root_path                           | `NodePath("..")` |
| VisibilityUpdateMode             | visibility_update_mode | `0`              |

## Methods

|                                  | add_visibility_filter(filter: [Callable](class_callable.md#class-callable))                     |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool) | get_visibility_for(peer: [int](class_int.md#class-int))                                            |
|                                  | remove_visibility_filter(filter: [Callable](class_callable.md#class-callable))               |
|                                  | set_visibility_for(peer: [int](class_int.md#class-int), visible: [bool](class_bool.md#class-bool)) |
|                                  | update_visibility(for_peer: [int](class_int.md#class-int) = 0)                                      |

---

## Signals

**delta_synchronized**()

Emitted when a new delta synchronization state is received by this synchronizer after the properties have been updated.

---

**synchronized**()

Emitted when a new synchronization state is received by this synchronizer after the properties have been updated.

---

**visibility_changed**(for_peer: [int](class_int.md#class-int))

Emitted when visibility of `for_peer` is updated. See update_visibility().

---

## Enumerations

enum **VisibilityUpdateMode**:

VisibilityUpdateMode **VISIBILITY_PROCESS_IDLE** = `0`

Visibility filters are updated during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class-node-constant-notification-internal-process)).

VisibilityUpdateMode **VISIBILITY_PROCESS_PHYSICS** = `1`

Visibility filters are updated during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class-node-constant-notification-internal-physics-process)).

VisibilityUpdateMode **VISIBILITY_PROCESS_NONE** = `2`

Visibility filters are not updated automatically, and must be updated manually by calling update_visibility().

---

## Property Descriptions

[float](class_float.md#class-float) **delta_interval** = `0.0`

-  **set_delta_interval**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_delta_interval**()

Time interval between delta synchronizations. Used when the replication is set to [SceneReplicationConfig.REPLICATION_MODE_ON_CHANGE](class_scenereplicationconfig.md#class-scenereplicationconfig-constant-replication-mode-on-change). If set to `0.0` (the default), delta synchronizations happen every network process frame.

---

[bool](class_bool.md#class-bool) **public_visibility** = `true`

-  **set_visibility_public**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visibility_public**()

Whether synchronization should be visible to all peers by default. See set_visibility_for() and add_visibility_filter() for ways of configuring fine-grained visibility options.

---

[SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig) **replication_config**

-  **set_replication_config**(value: [SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig))
- [SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig) **get_replication_config**()

Resource containing which properties to synchronize.

---

[float](class_float.md#class-float) **replication_interval** = `0.0`

-  **set_replication_interval**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_replication_interval**()

Time interval between synchronizations. Used when the replication is set to [SceneReplicationConfig.REPLICATION_MODE_ALWAYS](class_scenereplicationconfig.md#class-scenereplicationconfig-constant-replication-mode-always). If set to `0.0` (the default), synchronizations happen every network process frame.

---

[NodePath](class_nodepath.md#class-nodepath) **root_path** = `NodePath("..")`

-  **set_root_path**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_root_path**()

Node path that replicated properties are relative to.

If root_path was spawned by a [MultiplayerSpawner](class_multiplayerspawner.md#class-multiplayerspawner), the node will be also be spawned and despawned based on this synchronizer visibility options.

---

VisibilityUpdateMode **visibility_update_mode** = `0`

-  **set_visibility_update_mode**(value: VisibilityUpdateMode)
- VisibilityUpdateMode **get_visibility_update_mode**()

Specifies when visibility filters are updated.

---

## Method Descriptions

 **add_visibility_filter**(filter: [Callable](class_callable.md#class-callable))

Adds a peer visibility filter for this synchronizer.

`filter` should take a peer ID [int](class_int.md#class-int) and return a [bool](class_bool.md#class-bool).

---

[bool](class_bool.md#class-bool) **get_visibility_for**(peer: [int](class_int.md#class-int))

Queries the current visibility for peer `peer`.

---

 **remove_visibility_filter**(filter: [Callable](class_callable.md#class-callable))

Removes a peer visibility filter from this synchronizer.

---

 **set_visibility_for**(peer: [int](class_int.md#class-int), visible: [bool](class_bool.md#class-bool))

Sets the visibility of `peer` to `visible`. If `peer` is `0`, the value of public_visibility will be updated instead.

---

 **update_visibility**(for_peer: [int](class_int.md#class-int) = 0)

Updates the visibility of `for_peer` according to visibility filters. If `for_peer` is `0` (the default), all peers' visibilties are updated.
