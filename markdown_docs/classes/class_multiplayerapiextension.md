# MultiplayerAPIExtension

**Inherits:** [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class used for extending the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

## Description

This class can be used to extend or replace the default [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) implementation via script or extensions.

The following example extend the default implementation ([SceneMultiplayer](class_scenemultiplayer.md#class-scenemultiplayer)) by logging every RPC being made, and every object being configured for replication.

GDScript

```gdscript
extends MultiplayerAPIExtension
class_name LogMultiplayer

# We want to extend the default SceneMultiplayer.
var base_multiplayer = SceneMultiplayer.new()

func _init():
    # Just passthrough base signals (copied to var to avoid cyclic reference)
    var cts = connected_to_server
    var cf = connection_failed
    var sd = server_disconnected
    var pc = peer_connected
    var pd = peer_disconnected
    base_multiplayer.connected_to_server.connect(func(): cts.emit())
    base_multiplayer.connection_failed.connect(func(): cf.emit())
    base_multiplayer.server_disconnected.connect(func(): sd.emit())
    base_multiplayer.peer_connected.connect(func(id): pc.emit(id))
    base_multiplayer.peer_disconnected.connect(func(id): pd.emit(id))

func _poll():
    return base_multiplayer.poll()

# Log RPC being made and forward it to the default multiplayer.
func _rpc(peer: int, object: Object, method: StringName, args: Array) -> Error:
    print("Got RPC for %d: %s::%s(%s)" % [peer, object, method, args])
    return base_multiplayer.rpc(peer, object, method, args)

# Log configuration add. E.g. root path (nullptr, NodePath), replication (Node, Spawner|Synchronizer), custom.
func _object_configuration_add(object, config: Variant) -> Error:
    if config is MultiplayerSynchronizer:
        print("Adding synchronization configuration for %s. Synchronizer: %s" % [object, config])
    elif config is MultiplayerSpawner:
        print("Adding node %s to the spawn list. Spawner: %s" % [object, config])
    return base_multiplayer.object_configuration_add(object, config)

# Log configuration remove. E.g. root path (nullptr, NodePath), replication (Node, Spawner|Synchronizer), custom.
func _object_configuration_remove(object, config: Variant) -> Error:
    if config is MultiplayerSynchronizer:
        print("Removing synchronization configuration for %s. Synchronizer: %s" % [object, config])
    elif config is MultiplayerSpawner:
        print("Removing node %s from the spawn list. Spawner: %s" % [object, config])
    return base_multiplayer.object_configuration_remove(object, config)

# These can be optional, but in our case we want to extend SceneMultiplayer, so forward everything.
func _set_multiplayer_peer(p_peer: MultiplayerPeer):
    base_multiplayer.multiplayer_peer = p_peer

func _get_multiplayer_peer() -> MultiplayerPeer:
    return base_multiplayer.multiplayer_peer

func _get_unique_id() -> int:
    return base_multiplayer.get_unique_id()

func _get_remote_sender_id() -> int:
    return base_multiplayer.get_remote_sender_id()

func _get_peer_ids() -> PackedInt32Array:
    return base_multiplayer.get_peers()
```

Then in your main scene or in an autoload call [SceneTree.set_multiplayer()](class_scenetree.md#class-scenetree-method-set-multiplayer) to start using your custom [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi):

GDScript

```gdscript
# autoload.gd
func _enter_tree():
    # Sets our custom multiplayer as the main one in SceneTree.
    get_tree().set_multiplayer(LogMultiplayer.new())
```

Native extensions can alternatively use the [MultiplayerAPI.set_default_interface()](class_multiplayerapi.md#class-multiplayerapi-method-set-default-interface) method during initialization to configure themselves as the default implementation.

## Methods

| [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer)    | \_get_multiplayer_peer()                                                                                                                                                         |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | \_get_peer_ids()                                                                                                                                                                         |
| [int](class_int.md#class-int)                                        | \_get_remote_sender_id()                                                                                                                                                         |
| [int](class_int.md#class-int)                                        | \_get_unique_id()                                                                                                                                                                       |
| [Error](class_@globalscope.md#enum-globalscope-error)                | \_object_configuration_add(object: [Object](class_object.md#class-object), configuration: [Variant](class_variant.md#class-variant))                                         |
| [Error](class_@globalscope.md#enum-globalscope-error)                | \_object_configuration_remove(object: [Object](class_object.md#class-object), configuration: [Variant](class_variant.md#class-variant))                                   |
| [Error](class_@globalscope.md#enum-globalscope-error)                | \_poll()                                                                                                                                                                                         |
| [Error](class_@globalscope.md#enum-globalscope-error)                | \_rpc(peer: [int](class_int.md#class-int), object: [Object](class_object.md#class-object), method: [StringName](class_stringname.md#class-stringname), args: [Array](class_array.md#class-array)) |
|                                                                      | \_set_multiplayer_peer(multiplayer_peer: [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer))                                                                      |

---

## Method Descriptions

[MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) **\_get_multiplayer_peer**()

Called when the [MultiplayerAPI.multiplayer_peer](class_multiplayerapi.md#class-multiplayerapi-property-multiplayer-peer) is retrieved.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_get_peer_ids**()

Callback for [MultiplayerAPI.get_peers()](class_multiplayerapi.md#class-multiplayerapi-method-get-peers).

---

[int](class_int.md#class-int) **\_get_remote_sender_id**()

Callback for [MultiplayerAPI.get_remote_sender_id()](class_multiplayerapi.md#class-multiplayerapi-method-get-remote-sender-id).

---

[int](class_int.md#class-int) **\_get_unique_id**()

Callback for [MultiplayerAPI.get_unique_id()](class_multiplayerapi.md#class-multiplayerapi-method-get-unique-id).

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_object_configuration_add**(object: [Object](class_object.md#class-object), configuration: [Variant](class_variant.md#class-variant))

Callback for [MultiplayerAPI.object_configuration_add()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-add).

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_object_configuration_remove**(object: [Object](class_object.md#class-object), configuration: [Variant](class_variant.md#class-variant))

Callback for [MultiplayerAPI.object_configuration_remove()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-remove).

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_poll**()

Callback for [MultiplayerAPI.poll()](class_multiplayerapi.md#class-multiplayerapi-method-poll).

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_rpc**(peer: [int](class_int.md#class-int), object: [Object](class_object.md#class-object), method: [StringName](class_stringname.md#class-stringname), args: [Array](class_array.md#class-array))

Callback for [MultiplayerAPI.rpc()](class_multiplayerapi.md#class-multiplayerapi-method-rpc).

---

 **\_set_multiplayer_peer**(multiplayer_peer: [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer))

Called when the [MultiplayerAPI.multiplayer_peer](class_multiplayerapi.md#class-multiplayerapi-property-multiplayer-peer) is set.
