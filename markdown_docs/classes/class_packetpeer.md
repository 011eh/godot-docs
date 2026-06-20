# PacketPeer

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [ENetPacketPeer](class_enetpacketpeer.md#class-enetpacketpeer), [MultiplayerPeer](class_multiplayerpeer.md#class-multiplayerpeer), [PacketPeerDTLS](class_packetpeerdtls.md#class-packetpeerdtls), [PacketPeerExtension](class_packetpeerextension.md#class-packetpeerextension), [PacketPeerStream](class_packetpeerstream.md#class-packetpeerstream), [PacketPeerUDP](class_packetpeerudp.md#class-packetpeerudp), [WebRTCDataChannel](class_webrtcdatachannel.md#class-webrtcdatachannel), [WebSocketPeer](class_websocketpeer.md#class-websocketpeer)

Abstraction and base class for packet-based protocols.

## Description

PacketPeer is an abstraction and base class for packet-based protocols (such as UDP). It provides an API for sending and receiving packets both as raw data or variables. This makes it easy to transfer data over a protocol, without having to encode data as low-level bytes or having to worry about network ordering.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Properties

| [int](class_int.md#class-int)   | encode_buffer_max_size   | `8388608`   |
|---------------------------------|-------------------------------------------------------------------------------|-------------|

## Methods

| [int](class_int.md#class-int)                                     | get_available_packet_count()                                                                 |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | get_packet()                                                                                                 |
| [Error](class_@globalscope.md#enum-globalscope-error)             | get_packet_error()                                                                                     |
| [Variant](class_variant.md#class-variant)                         | get_var(allow_objects: [bool](class_bool.md#class-bool) = false)                                                |
| [Error](class_@globalscope.md#enum-globalscope-error)             | put_packet(buffer: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                        |
| [Error](class_@globalscope.md#enum-globalscope-error)             | put_var(var: [Variant](class_variant.md#class-variant), full_objects: [bool](class_bool.md#class-bool) = false) |

---

## Property Descriptions

[int](class_int.md#class-int) **encode_buffer_max_size** = `8388608`

-  **set_encode_buffer_max_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_encode_buffer_max_size**()

Maximum buffer size allowed when encoding [Variant](class_variant.md#class-variant)s. Raise this value to support heavier memory allocations.

The put_var() method allocates memory on the stack, and the buffer used will grow automatically to the closest power of two to match the size of the [Variant](class_variant.md#class-variant). If the [Variant](class_variant.md#class-variant) is bigger than encode_buffer_max_size, the method will error out with [@GlobalScope.ERR_OUT_OF_MEMORY](class_@globalscope.md#class-globalscope-constant-err-out-of-memory).

---

## Method Descriptions

[int](class_int.md#class-int) **get_available_packet_count**()

Returns the number of packets currently available in the ring-buffer.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_packet**()

Gets a raw packet.

---

[Error](class_@globalscope.md#enum-globalscope-error) **get_packet_error**()

Returns the error state of the last packet received (via get_packet() and get_var()).

---

[Variant](class_variant.md#class-variant) **get_var**(allow_objects: [bool](class_bool.md#class-bool) = false)

Gets a Variant. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the [@GlobalScope.bytes_to_var()](class_@globalscope.md#class-globalscope-method-bytes-to-var) method.

**Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.

---

[Error](class_@globalscope.md#enum-globalscope-error) **put_packet**(buffer: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Sends a raw packet.

---

[Error](class_@globalscope.md#enum-globalscope-error) **put_var**(var: [Variant](class_variant.md#class-variant), full_objects: [bool](class_bool.md#class-bool) = false)

Sends a [Variant](class_variant.md#class-variant) as a packet. If `full_objects` is `true`, encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the [@GlobalScope.var_to_bytes()](class_@globalscope.md#class-globalscope-method-var-to-bytes) method.
