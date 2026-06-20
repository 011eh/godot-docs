# WebRTCMultiplayerPeer

**Inherits:** [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer) **<** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A simple interface to create a peer-to-peer mesh network composed of [WebRTCPeerConnection](class_webrtcpeerconnection.md#class-webrtcpeerconnection) that is compatible with the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

## Description

This class constructs a full mesh of [WebRTCPeerConnection](class_webrtcpeerconnection.md#class-webrtcpeerconnection) (one connection for each peer) that can be used as a [MultiplayerAPI.multiplayer_peer](class_multiplayerapi.md#class-multiplayerapi-property-multiplayer-peer).

You can add each [WebRTCPeerConnection](class_webrtcpeerconnection.md#class-webrtcpeerconnection) via add_peer() or remove them via remove_peer(). Peers must be added in [WebRTCPeerConnection.STATE_NEW](class_webrtcpeerconnection.md#class-webrtcpeerconnection-constant-state-new) state to allow it to create the appropriate channels. This class will not create offers nor set descriptions, it will only poll them, and notify connections and disconnections.

When creating the peer via create_client() or create_server() the [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class-multiplayerpeer-method-is-server-relay-supported) method will return `true` enabling peer exchange and packet relaying when supported by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) implementation.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | add_peer(peer: [WebRTCPeerConnection](class_webrtcpeerconnection.md#class-webrtcpeerconnection), peer_id: [int](class_int.md#class-int), unreliable_lifetime: [int](class_int.md#class-int) = 1)   |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)   | create_client(peer_id: [int](class_int.md#class-int), channels_config: [Array](class_array.md#class-array) = [])                                                                              |
| [Error](class_@globalscope.md#enum-globalscope-error)   | create_mesh(peer_id: [int](class_int.md#class-int), channels_config: [Array](class_array.md#class-array) = [])                                                                                  |
| [Error](class_@globalscope.md#enum-globalscope-error)   | create_server(channels_config: [Array](class_array.md#class-array) = [])                                                                                                                      |
| [Dictionary](class_dictionary.md#class-dictionary)      | get_peer(peer_id: [int](class_int.md#class-int))                                                                                                                                                   |
| [Dictionary](class_dictionary.md#class-dictionary)      | get_peers()                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                        | has_peer(peer_id: [int](class_int.md#class-int))                                                                                                                                                   |
|                                                         | remove_peer(peer_id: [int](class_int.md#class-int))                                                                                                                                             |

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **add_peer**(peer: [WebRTCPeerConnection](class_webrtcpeerconnection.md#class-webrtcpeerconnection), peer_id: [int](class_int.md#class-int), unreliable_lifetime: [int](class_int.md#class-int) = 1)

Add a new peer to the mesh with the given `peer_id`. The [WebRTCPeerConnection](class_webrtcpeerconnection.md#class-webrtcpeerconnection) must be in state [WebRTCPeerConnection.STATE_NEW](class_webrtcpeerconnection.md#class-webrtcpeerconnection-constant-state-new).

Three channels will be created for reliable, unreliable, and ordered transport. The value of `unreliable_lifetime` will be passed to the `"maxPacketLifetime"` option when creating unreliable and ordered channels (see [WebRTCPeerConnection.create_data_channel()](class_webrtcpeerconnection.md#class-webrtcpeerconnection-method-create-data-channel)).

---

[Error](class_@globalscope.md#enum-globalscope-error) **create_client**(peer_id: [int](class_int.md#class-int), channels_config: [Array](class_array.md#class-array) = [])

Initialize the multiplayer peer as a client with the given `peer_id` (must be between 2 and 2147483647). In this mode, you should only call add_peer() once and with `peer_id` of `1`. This mode enables [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class-multiplayerpeer-method-is-server-relay-supported), allowing the upper [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) layer to perform peer exchange and packet relaying.

You can optionally specify a `channels_config` array of [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode) which will be used to create extra channels (WebRTC only supports one transfer mode per channel).

---

[Error](class_@globalscope.md#enum-globalscope-error) **create_mesh**(peer_id: [int](class_int.md#class-int), channels_config: [Array](class_array.md#class-array) = [])

Initialize the multiplayer peer as a mesh (i.e. all peers connect to each other) with the given `peer_id` (must be between 1 and 2147483647).

---

[Error](class_@globalscope.md#enum-globalscope-error) **create_server**(channels_config: [Array](class_array.md#class-array) = [])

Initialize the multiplayer peer as a server (with unique ID of `1`). This mode enables [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class-multiplayerpeer-method-is-server-relay-supported), allowing the upper [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) layer to perform peer exchange and packet relaying.

You can optionally specify a `channels_config` array of [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode) which will be used to create extra channels (WebRTC only supports one transfer mode per channel).

---

[Dictionary](class_dictionary.md#class-dictionary) **get_peer**(peer_id: [int](class_int.md#class-int))

Returns a dictionary representation of the peer with given `peer_id` with three keys. `"connection"` containing the [WebRTCPeerConnection](class_webrtcpeerconnection.md#class-webrtcpeerconnection) to this peer, `"channels"` an array of three [WebRTCDataChannel](class_webrtcdatachannel.md#class-webrtcdatachannel), and `"connected"` a boolean representing if the peer connection is currently connected (all three channels are open).

---

[Dictionary](class_dictionary.md#class-dictionary) **get_peers**()

Returns a dictionary which keys are the peer ids and values the peer representation as in get_peer().

---

[bool](class_bool.md#class-bool) **has_peer**(peer_id: [int](class_int.md#class-int))

Returns `true` if the given `peer_id` is in the peers map (it might not be connected though).

---

 **remove_peer**(peer_id: [int](class_int.md#class-int))

Remove the peer with given `peer_id` from the mesh. If the peer was connected, and [MultiplayerPeer.peer_connected](class_multiplayerpeer.md#class-multiplayerpeer-signal-peer-connected) was emitted for it, then [MultiplayerPeer.peer_disconnected](class_multiplayerpeer.md#class-multiplayerpeer-signal-peer-disconnected) will be emitted.
