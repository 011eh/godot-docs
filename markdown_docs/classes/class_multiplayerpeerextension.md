# MultiplayerPeerExtension

**Inherits:** [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) **<** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Class that can be inherited to implement custom multiplayer API networking layers via GDExtension.

## Description

This class is designed to be inherited from a GDExtension plugin to implement custom networking layers for the multiplayer API (such as WebRTC). All the methods below **must** be implemented to have a working custom multiplayer implementation. See also [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

## Methods

|                                                                                    | \_close()                                                                                                         |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                    | \_disconnect_peer(peer: [int](class_int.md#class-int), force: [bool](class_bool.md#class-bool))         |
| [int](class_int.md#class-int)                                                      | \_get_available_packet_count()                                                               |
| [ConnectionStatus](class_multiplayerpeer.md#enum-multiplayerpeer-connectionstatus) | \_get_connection_status()                                                                         |
| [int](class_int.md#class-int)                                                      | \_get_max_packet_size()                                                                             |
| [Error](class_@globalscope.md#enum-globalscope-error)                              | \_get_packet(r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*`)                                        |
| [int](class_int.md#class-int)                                                      | \_get_packet_channel()                                                                               |
| [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode)         | \_get_packet_mode()                                                                                     |
| [int](class_int.md#class-int)                                                      | \_get_packet_peer()                                                                                     |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)                  | \_get_packet_script()                                                                                 |
| [int](class_int.md#class-int)                                                      | \_get_transfer_channel()                                                                           |
| [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode)         | \_get_transfer_mode()                                                                                 |
| [int](class_int.md#class-int)                                                      | \_get_unique_id()                                                                                         |
| [bool](class_bool.md#class-bool)                                                   | \_is_refusing_new_connections()                                                             |
| [bool](class_bool.md#class-bool)                                                   | \_is_server()                                                                                                 |
| [bool](class_bool.md#class-bool)                                                   | \_is_server_relay_supported()                                                                 |
|                                                                                    | \_poll()                                                                                                           |
| [Error](class_@globalscope.md#enum-globalscope-error)                              | \_put_packet(buffer: `const uint8_t*`, buffer_size: [int](class_int.md#class-int))                           |
| [Error](class_@globalscope.md#enum-globalscope-error)                              | \_put_packet_script(buffer: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))        |
|                                                                                    | \_set_refuse_new_connections(enable: [bool](class_bool.md#class-bool))                       |
|                                                                                    | \_set_target_peer(peer: [int](class_int.md#class-int))                                                  |
|                                                                                    | \_set_transfer_channel(channel: [int](class_int.md#class-int))                                     |
|                                                                                    | \_set_transfer_mode(mode: [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode)) |

---

## Method Descriptions

 **\_close**()

Called when the multiplayer peer should be immediately closed (see [MultiplayerPeer.close()](class_multiplayerpeer.md#class-multiplayerpeer-method-close)).

---

 **\_disconnect_peer**(peer: [int](class_int.md#class-int), force: [bool](class_bool.md#class-bool))

Called when the connected `peer` should be forcibly disconnected (see [MultiplayerPeer.disconnect_peer()](class_multiplayerpeer.md#class-multiplayerpeer-method-disconnect-peer)).

---

[int](class_int.md#class-int) **\_get_available_packet_count**()

Called when the available packet count is internally requested by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

---

[ConnectionStatus](class_multiplayerpeer.md#enum-multiplayerpeer-connectionstatus) **\_get_connection_status**()

Called when the connection status is requested on the [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) (see [MultiplayerPeer.get_connection_status()](class_multiplayerpeer.md#class-multiplayerpeer-method-get-connection-status)).

---

[int](class_int.md#class-int) **\_get_max_packet_size**()

Called when the maximum allowed packet size (in bytes) is requested by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_get_packet**(r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*`)

Called when a packet needs to be received by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi), with `r_buffer_size` being the size of the binary `r_buffer` in bytes.

---

[int](class_int.md#class-int) **\_get_packet_channel**()

Called to get the channel over which the next available packet was received. See [MultiplayerPeer.get_packet_channel()](class_multiplayerpeer.md#class-multiplayerpeer-method-get-packet-channel).

---

[TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode) **\_get_packet_mode**()

Called to get the transfer mode the remote peer used to send the next available packet. See [MultiplayerPeer.get_packet_mode()](class_multiplayerpeer.md#class-multiplayerpeer-method-get-packet-mode).

---

[int](class_int.md#class-int) **\_get_packet_peer**()

Called when the ID of the [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) who sent the most recent packet is requested (see [MultiplayerPeer.get_packet_peer()](class_multiplayerpeer.md#class-multiplayerpeer-method-get-packet-peer)).

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **\_get_packet_script**()

Called when a packet needs to be received by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi), if \_get_packet() isn't implemented. Use this when extending this class via GDScript.

---

[int](class_int.md#class-int) **\_get_transfer_channel**()

Called when the transfer channel to use is read on this [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) (see [MultiplayerPeer.transfer_channel](class_multiplayerpeer.md#class-multiplayerpeer-property-transfer-channel)).

---

[TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode) **\_get_transfer_mode**()

Called when the transfer mode to use is read on this [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) (see [MultiplayerPeer.transfer_mode](class_multiplayerpeer.md#class-multiplayerpeer-property-transfer-mode)).

---

[int](class_int.md#class-int) **\_get_unique_id**()

Called when the unique ID of this [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) is requested (see [MultiplayerPeer.get_unique_id()](class_multiplayerpeer.md#class-multiplayerpeer-method-get-unique-id)). The value must be between `1` and `2147483647`.

---

[bool](class_bool.md#class-bool) **\_is_refusing_new_connections**()

Called when the "refuse new connections" status is requested on this [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) (see [MultiplayerPeer.refuse_new_connections](class_multiplayerpeer.md#class-multiplayerpeer-property-refuse-new-connections)).

---

[bool](class_bool.md#class-bool) **\_is_server**()

Called when the "is server" status is requested on the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi). See [MultiplayerAPI.is_server()](class_multiplayerapi.md#class-multiplayerapi-method-is-server).

---

[bool](class_bool.md#class-bool) **\_is_server_relay_supported**()

Called to check if the server can act as a relay in the current configuration. See [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class-multiplayerpeer-method-is-server-relay-supported).

---

 **\_poll**()

Called when the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) is polled. See [MultiplayerAPI.poll()](class_multiplayerapi.md#class-multiplayerapi-method-poll).

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_put_packet**(buffer: `const uint8_t*`, buffer_size: [int](class_int.md#class-int))

Called when a packet needs to be sent by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi), with `buffer_size` being the size of the binary `buffer` in bytes.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_put_packet_script**(buffer: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Called when a packet needs to be sent by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi), if \_put_packet() isn't implemented. Use this when extending this class via GDScript.

---

 **\_set_refuse_new_connections**(enable: [bool](class_bool.md#class-bool))

Called when the "refuse new connections" status is set on this [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) (see [MultiplayerPeer.refuse_new_connections](class_multiplayerpeer.md#class-multiplayerpeer-property-refuse-new-connections)).

---

 **\_set_target_peer**(peer: [int](class_int.md#class-int))

Called when the target peer to use is set for this [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) (see [MultiplayerPeer.set_target_peer()](class_multiplayerpeer.md#class-multiplayerpeer-method-set-target-peer)).

---

 **\_set_transfer_channel**(channel: [int](class_int.md#class-int))

Called when the channel to use is set for this [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) (see [MultiplayerPeer.transfer_channel](class_multiplayerpeer.md#class-multiplayerpeer-property-transfer-channel)).

---

 **\_set_transfer_mode**(mode: [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode))

Called when the transfer mode is set on this [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) (see [MultiplayerPeer.transfer_mode](class_multiplayerpeer.md#class-multiplayerpeer-property-transfer-mode)).
