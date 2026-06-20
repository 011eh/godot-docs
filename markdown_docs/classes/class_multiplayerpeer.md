# MultiplayerPeer

**Inherits:** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [ENetMultiplayerPeer](class_enetmultiplayerpeer.md#class-enetmultiplayerpeer), [MultiplayerPeerExtension](class_multiplayerpeerextension.md#class-multiplayerpeerextension), [OfflineMultiplayerPeer](class_offlinemultiplayerpeer.md#class-offlinemultiplayerpeer), [WebRTCMultiplayerPeer](class_webrtcmultiplayerpeer.md#class-webrtcmultiplayerpeer), [WebSocketMultiplayerPeer](class_websocketmultiplayerpeer.md#class-websocketmultiplayerpeer)

Abstract class for specialized [PacketPeer](class_packetpeer.md#class-packetpeer)s used by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

## Description

Manages the connection with one or more remote peers acting as server or client and assigning unique IDs to each of them. See also [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

**Note:** The [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) protocol is an implementation detail and isn't meant to be used by non-Godot servers. It may change without notice.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Tutorials

- [High-level multiplayer](../tutorials/networking/high_level_multiplayer.md)

## Properties

| [bool](class_bool.md#class-bool)                   | refuse_new_connections   | `false`   |
|----------------------------------------------------|------------------------------------------------------------------------------------|-----------|
| [int](class_int.md#class-int)                      | transfer_channel               | `0`       |
| TransferMode | transfer_mode                     | `2`       |

## Methods

|                                                            | close()                                                                                                         |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                            | disconnect_peer(peer: [int](class_int.md#class-int), force: [bool](class_bool.md#class-bool) = false) |
| [int](class_int.md#class-int)                              | generate_unique_id()                                                                               |
| ConnectionStatus | get_connection_status()                                                                         |
| [int](class_int.md#class-int)                              | get_packet_channel()                                                                               |
| TransferMode         | get_packet_mode()                                                                                     |
| [int](class_int.md#class-int)                              | get_packet_peer()                                                                                     |
| [int](class_int.md#class-int)                              | get_unique_id()                                                                                         |
| [bool](class_bool.md#class-bool)                           | is_server_relay_supported()                                                                 |
|                                                            | poll()                                                                                                           |
|                                                            | set_target_peer(id: [int](class_int.md#class-int))                                                    |

---

## Signals

**peer_connected**(id: [int](class_int.md#class-int))

Emitted when a remote peer connects.

---

**peer_disconnected**(id: [int](class_int.md#class-int))

Emitted when a remote peer has disconnected.

---

## Enumerations

enum **ConnectionStatus**:

ConnectionStatus **CONNECTION_DISCONNECTED** = `0`

The MultiplayerPeer is disconnected.

ConnectionStatus **CONNECTION_CONNECTING** = `1`

The MultiplayerPeer is currently connecting to a server.

ConnectionStatus **CONNECTION_CONNECTED** = `2`

This MultiplayerPeer is connected.

---

enum **TransferMode**:

TransferMode **TRANSFER_MODE_UNRELIABLE** = `0`

Packets are not acknowledged, no resend attempts are made for lost packets. Packets may arrive in any order. Potentially faster than TRANSFER_MODE_UNRELIABLE_ORDERED. Use for non-critical data, and always consider whether the order matters.

TransferMode **TRANSFER_MODE_UNRELIABLE_ORDERED** = `1`

Packets are not acknowledged, no resend attempts are made for lost packets. Packets are received in the order they were sent in. Potentially faster than TRANSFER_MODE_RELIABLE. Use for non-critical data or data that would be outdated if received late due to resend attempt(s) anyway, for example movement and positional data.

TransferMode **TRANSFER_MODE_RELIABLE** = `2`

Packets must be received and resend attempts should be made until the packets are acknowledged. Packets must be received in the order they were sent in. Most reliable transfer mode, but potentially the slowest due to the overhead. Use for critical data that must be transmitted and arrive in order, for example an ability being triggered or a chat message. Consider carefully if the information really is critical, and use sparingly.

---

## Constants

**TARGET_PEER_BROADCAST** = `0`

Packets are sent to all connected peers.

**TARGET_PEER_SERVER** = `1`

Packets are sent to the remote peer acting as server.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **refuse_new_connections** = `false`

-  **set_refuse_new_connections**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_refusing_new_connections**()

If `true`, this **MultiplayerPeer** refuses new connections.

---

[int](class_int.md#class-int) **transfer_channel** = `0`

-  **set_transfer_channel**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_transfer_channel**()

The channel to use to send packets. Many network APIs such as ENet and WebRTC allow the creation of multiple independent channels which behaves, in a way, like separate connections. This means that reliable data will only block delivery of other packets on that channel, and ordering will only be in respect to the channel the packet is being sent on. Using different channels to send **different and independent** state updates is a common way to optimize network usage and decrease latency in fast-paced games.

**Note:** The default channel (`0`) actually works as 3 separate channels (one for each TransferMode) so that TRANSFER_MODE_RELIABLE and TRANSFER_MODE_UNRELIABLE_ORDERED does not interact with each other by default. Refer to the specific network API documentation (e.g. ENet or WebRTC) to learn how to set up channels correctly.

---

TransferMode **transfer_mode** = `2`

-  **set_transfer_mode**(value: TransferMode)
- TransferMode **get_transfer_mode**()

The manner in which to send packets to the target peer. See the set_target_peer() method.

---

## Method Descriptions

 **close**()

Immediately close the multiplayer peer returning to the state CONNECTION_DISCONNECTED. Connected peers will be dropped without emitting peer_disconnected.

---

 **disconnect_peer**(peer: [int](class_int.md#class-int), force: [bool](class_bool.md#class-bool) = false)

Disconnects the given `peer` from this host. If `force` is `true` the peer_disconnected signal will not be emitted for this peer.

---

[int](class_int.md#class-int) **generate_unique_id**()

Returns a randomly generated integer that can be used as a network unique ID.

---

ConnectionStatus **get_connection_status**()

Returns the current state of the connection.

---

[int](class_int.md#class-int) **get_packet_channel**()

Returns the channel over which the next available packet was received. See [PacketPeer.get_available_packet_count()](class_packetpeer.md#class-packetpeer-method-get-available-packet-count).

---

TransferMode **get_packet_mode**()

Returns the transfer mode the remote peer used to send the next available packet. See [PacketPeer.get_available_packet_count()](class_packetpeer.md#class-packetpeer-method-get-available-packet-count).

---

[int](class_int.md#class-int) **get_packet_peer**()

Returns the ID of the **MultiplayerPeer** who sent the next available packet. See [PacketPeer.get_available_packet_count()](class_packetpeer.md#class-packetpeer-method-get-available-packet-count).

---

[int](class_int.md#class-int) **get_unique_id**()

Returns the ID of this **MultiplayerPeer**.

---

[bool](class_bool.md#class-bool) **is_server_relay_supported**()

Returns `true` if the server can act as a relay in the current configuration. That is, if the higher level [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) should notify connected clients of other peers, and implement a relay protocol to allow communication between them.

---

 **poll**()

Waits up to 1 second to receive a new network event.

---

 **set_target_peer**(id: [int](class_int.md#class-int))

Sets the peer to which packets will be sent.

The `id` can be one of: TARGET_PEER_BROADCAST to send to all connected peers, TARGET_PEER_SERVER to send to the peer acting as server, a valid peer ID to send to that specific peer, a negative peer ID to send to all peers except that one. By default, the target peer is TARGET_PEER_BROADCAST.
