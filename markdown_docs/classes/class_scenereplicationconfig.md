# SceneReplicationConfig

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Configuration for properties to synchronize with a [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer).

## Methods

|                                                                                   | add_property(path: [NodePath](class_nodepath.md#class-nodepath), index: [int](class_int.md#class-int) = -1)                                                               |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)[[NodePath](class_nodepath.md#class-nodepath)] | get_properties()                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                  | has_property(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                          |
| [int](class_int.md#class-int)                                                     | property_get_index(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                              |
| ReplicationMode                   | property_get_replication_mode(path: [NodePath](class_nodepath.md#class-nodepath))                                                                        |
| [bool](class_bool.md#class-bool)                                                  | property_get_spawn(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                              |
| [bool](class_bool.md#class-bool)                                                  | property_get_sync(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                |
| [bool](class_bool.md#class-bool)                                                  | property_get_watch(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                              |
|                                                                                   | property_set_replication_mode(path: [NodePath](class_nodepath.md#class-nodepath), mode: ReplicationMode) |
|                                                                                   | property_set_spawn(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool))                                                   |
|                                                                                   | property_set_sync(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool))                                                     |
|                                                                                   | property_set_watch(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool))                                                   |
|                                                                                   | remove_property(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                    |

---

## Enumerations

enum **ReplicationMode**:

ReplicationMode **REPLICATION_MODE_NEVER** = `0`

Do not keep the given property synchronized.

ReplicationMode **REPLICATION_MODE_ALWAYS** = `1`

Replicate the given property on process by constantly sending updates using unreliable transfer mode.

ReplicationMode **REPLICATION_MODE_ON_CHANGE** = `2`

Replicate the given property on process by sending updates using reliable transfer mode when its value changes.

---

## Method Descriptions

 **add_property**(path: [NodePath](class_nodepath.md#class-nodepath), index: [int](class_int.md#class-int) = -1)

Adds the property identified by the given `path` to the list of the properties being synchronized, optionally passing an `index`.

**Note:** For details on restrictions and limitations on property synchronization, see [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer).

---

[Array](class_array.md#class-array)[[NodePath](class_nodepath.md#class-nodepath)] **get_properties**()

Returns a list of synchronized property [NodePath](class_nodepath.md#class-nodepath)s.

---

[bool](class_bool.md#class-bool) **has_property**(path: [NodePath](class_nodepath.md#class-nodepath))

Returns `true` if the given `path` is configured for synchronization.

---

[int](class_int.md#class-int) **property_get_index**(path: [NodePath](class_nodepath.md#class-nodepath))

Finds the index of the given `path`.

---

ReplicationMode **property_get_replication_mode**(path: [NodePath](class_nodepath.md#class-nodepath))

Returns the replication mode for the property identified by the given `path`.

---

[bool](class_bool.md#class-bool) **property_get_spawn**(path: [NodePath](class_nodepath.md#class-nodepath))

Returns `true` if the property identified by the given `path` is configured to be synchronized on spawn.

---

[bool](class_bool.md#class-bool) **property_get_sync**(path: [NodePath](class_nodepath.md#class-nodepath))

**Deprecated:** Use property_get_replication_mode() instead.

Returns `true` if the property identified by the given `path` is configured to be synchronized on process.

---

[bool](class_bool.md#class-bool) **property_get_watch**(path: [NodePath](class_nodepath.md#class-nodepath))

**Deprecated:** Use property_get_replication_mode() instead.

Returns `true` if the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.

---

 **property_set_replication_mode**(path: [NodePath](class_nodepath.md#class-nodepath), mode: ReplicationMode)

Sets the synchronization mode for the property identified by the given `path`.

---

 **property_set_spawn**(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool))

Sets whether the property identified by the given `path` is configured to be synchronized on spawn.

---

 **property_set_sync**(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool))

**Deprecated:** Use property_set_replication_mode() with REPLICATION_MODE_ALWAYS instead.

Sets whether the property identified by the given `path` is configured to be synchronized on process.

---

 **property_set_watch**(path: [NodePath](class_nodepath.md#class-nodepath), enabled: [bool](class_bool.md#class-bool))

**Deprecated:** Use property_set_replication_mode() with REPLICATION_MODE_ON_CHANGE instead.

Sets whether the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.

---

 **remove_property**(path: [NodePath](class_nodepath.md#class-nodepath))

Removes the property identified by the given `path` from the configuration.
