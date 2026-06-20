# SceneMultiplayer

**Inherits:** [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

High-level multiplayer API implementation.

## Description

This class is the default implementation of [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi), used to provide multiplayer functionalities in Godot Engine.

This implementation supports RPCs via [Node.rpc()](class_node.md#class-node-method-rpc) and [Node.rpc_id()](class_node.md#class-node-method-rpc-id) and requires [MultiplayerAPI.rpc()](class_multiplayerapi.md#class-multiplayerapi-method-rpc) to be passed a [Node](class_node.md#class-node) (it will fail for other object types).

This implementation additionally provide [SceneTree](class_scenetree.md#class-scenetree) replication via the [MultiplayerSpawner](class_multiplayerspawner.md#class-multiplayerspawner) and [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer) nodes, and the [SceneReplicationConfig](class_scenereplicationconfig.md#class-scenereplicationconfig) resource.

**Note:** The high-level multiplayer API protocol is an implementation detail and isn't meant to be used by non-Godot servers. It may change without notice.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Properties

| [bool](class_bool.md#class-bool)             | allow_object_decoding   | `false`        |
|----------------------------------------------|-----------------------------------------------------------------------------------|----------------|
| [Callable](class_callable.md#class-callable) | auth_callback                   | `Callable()`   |
| [float](class_float.md#class-float)          | auth_timeout                     | `3.0`          |
| [int](class_int.md#class-int)                | max_delta_packet_size   | `65535`        |
| [int](class_int.md#class-int)                | max_sync_packet_size     | `1350`         |
| [bool](class_bool.md#class-bool)             | refuse_new_connections | `false`        |
| [NodePath](class_nodepath.md#class-nodepath) | root_path                           | `NodePath("")` |
| [bool](class_bool.md#class-bool)             | server_relay                     | `true`         |

## Methods

|                                                                      | clear()                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)                | complete_auth(id: [int](class_int.md#class-int))                                                                                                                                                                                                           |
|                                                                      | disconnect_peer(id: [int](class_int.md#class-int))                                                                                                                                                                                                       |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | get_authenticating_peers()                                                                                                                                                                                                                      |
| [Error](class_@globalscope.md#enum-globalscope-error)                | send_auth(id: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                          |
| [Error](class_@globalscope.md#enum-globalscope-error)                | send_bytes(bytes: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), id: [int](class_int.md#class-int) = 0, mode: [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode) = 2, channel: [int](class_int.md#class-int) = 0) |

---

## Signals

**peer_authenticating**(id: [int](class_int.md#class-int))

Emitted when this MultiplayerAPI's [MultiplayerAPI.multiplayer_peer](class_multiplayerapi.md#class-multiplayerapi-property-multiplayer-peer) connects to a new peer and a valid auth_callback is set. In this case, the [MultiplayerAPI.peer_connected](class_multiplayerapi.md#class-multiplayerapi-signal-peer-connected) will not be emitted until complete_auth() is called with given peer `id`. While in this state, the peer will not be included in the list returned by [MultiplayerAPI.get_peers()](class_multiplayerapi.md#class-multiplayerapi-method-get-peers) (but in the one returned by get_authenticating_peers()), and only authentication data will be sent or received. See send_auth() for sending authentication data.

---

**peer_authentication_failed**(id: [int](class_int.md#class-int))

Emitted when this MultiplayerAPI's [MultiplayerAPI.multiplayer_peer](class_multiplayerapi.md#class-multiplayerapi-property-multiplayer-peer) disconnects from a peer for which authentication had not yet completed. See peer_authenticating.

---

**peer_packet**(id: [int](class_int.md#class-int), packet: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Emitted when this MultiplayerAPI's [MultiplayerAPI.multiplayer_peer](class_multiplayerapi.md#class-multiplayerapi-property-multiplayer-peer) receives a `packet` with custom data (see send_bytes()). ID is the peer ID of the peer that sent the packet.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_object_decoding** = `false`

-  **set_allow_object_decoding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_object_decoding_allowed**()

If `true`, the MultiplayerAPI will allow encoding and decoding of object during RPCs.

**Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threat such as remote code execution.

---

[Callable](class_callable.md#class-callable) **auth_callback** = `Callable()`

-  **set_auth_callback**(value: [Callable](class_callable.md#class-callable))
- [Callable](class_callable.md#class-callable) **get_auth_callback**()

The callback to execute when receiving authentication data sent via send_auth(). If the [Callable](class_callable.md#class-callable) is empty (default), peers will be automatically accepted as soon as they connect.

---

[float](class_float.md#class-float) **auth_timeout** = `3.0`

-  **set_auth_timeout**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_auth_timeout**()

If set to a value greater than `0.0`, the maximum duration in seconds peers can stay in the authenticating state, after which the authentication will automatically fail. See the peer_authenticating and peer_authentication_failed signals.

---

[int](class_int.md#class-int) **max_delta_packet_size** = `65535`

-  **set_max_delta_packet_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_delta_packet_size**()

Maximum size of each delta packet. Higher values increase the chance of receiving full updates in a single frame, but also the chance of causing networking congestion (higher latency, disconnections). See [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer).

---

[int](class_int.md#class-int) **max_sync_packet_size** = `1350`

-  **set_max_sync_packet_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_sync_packet_size**()

Maximum size of each synchronization packet. Higher values increase the chance of receiving full updates in a single frame, but also the chance of packet loss. See [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer).

---

[bool](class_bool.md#class-bool) **refuse_new_connections** = `false`

-  **set_refuse_new_connections**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_refusing_new_connections**()

If `true`, the MultiplayerAPI's [MultiplayerAPI.multiplayer_peer](class_multiplayerapi.md#class-multiplayerapi-property-multiplayer-peer) refuses new incoming connections.

---

[NodePath](class_nodepath.md#class-nodepath) **root_path** = `NodePath("")`

-  **set_root_path**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_root_path**()

The root path to use for RPCs and replication. Instead of an absolute path, a relative path will be used to find the node upon which the RPC should be executed.

This effectively allows to have different branches of the scene tree to be managed by different MultiplayerAPI, allowing for example to run both client and server in the same scene.

---

[bool](class_bool.md#class-bool) **server_relay** = `true`

-  **set_server_relay_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_server_relay_enabled**()

Enable or disable the server feature that notifies clients of other peers' connection/disconnection, and relays messages between them. When this option is `false`, clients won't be automatically notified of other peers and won't be able to send them packets through the server.

**Note:** Changing this option while other peers are connected may lead to unexpected behaviors.

**Note:** Support for this feature may depend on the current [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) configuration. See [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class-multiplayerpeer-method-is-server-relay-supported).

---

## Method Descriptions

 **clear**()

Clears the current SceneMultiplayer network state (you shouldn't call this unless you know what you are doing).

---

[Error](class_@globalscope.md#enum-globalscope-error) **complete_auth**(id: [int](class_int.md#class-int))

Mark the authentication step as completed for the remote peer identified by `id`. The [MultiplayerAPI.peer_connected](class_multiplayerapi.md#class-multiplayerapi-signal-peer-connected) signal will be emitted for this peer once the remote side also completes the authentication. No further authentication messages are expected to be received from this peer.

If a peer disconnects before completing authentication, either due to a network issue, the auth_timeout expiring, or manually calling disconnect_peer(), the peer_authentication_failed signal will be emitted instead of [MultiplayerAPI.peer_disconnected](class_multiplayerapi.md#class-multiplayerapi-signal-peer-disconnected).

---

 **disconnect_peer**(id: [int](class_int.md#class-int))

Disconnects the peer identified by `id`, removing it from the list of connected peers, and closing the underlying connection with it.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_authenticating_peers**()

Returns the IDs of the peers currently trying to authenticate with this [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

---

[Error](class_@globalscope.md#enum-globalscope-error) **send_auth**(id: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Sends the specified `data` to the remote peer identified by `id` as part of an authentication message. This can be used to authenticate peers, and control when [MultiplayerAPI.peer_connected](class_multiplayerapi.md#class-multiplayerapi-signal-peer-connected) is emitted (and the remote peer accepted as one of the connected peers).

---

[Error](class_@globalscope.md#enum-globalscope-error) **send_bytes**(bytes: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), id: [int](class_int.md#class-int) = 0, mode: [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode) = 2, channel: [int](class_int.md#class-int) = 0)

Sends the given raw `bytes` to a specific peer identified by `id` (see [MultiplayerPeer.set_target_peer()](class_multiplayerpeer.md#class-multiplayerpeer-method-set-target-peer)). Default ID is `0`, i.e. broadcast to all peers.
