# WebRTCDataChannel

**Inherits:** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [WebRTCDataChannelExtension](class_webrtcdatachannelextension.md#class-webrtcdatachannelextension)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

## Properties

| WriteMode   | write_mode   | `1`   |
|--------------------------------------------------|--------------------------------------------------------------|-------|

## Methods

|                                                       | close()                                       |
|-------------------------------------------------------|----------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                         | get_buffered_amount()           |
| [int](class_int.md#class-int)                         | get_id()                                     |
| [String](class_string.md#class-string)                | get_label()                               |
| [int](class_int.md#class-int)                         | get_max_packet_life_time() |
| [int](class_int.md#class-int)                         | get_max_retransmits()           |
| [String](class_string.md#class-string)                | get_protocol()                         |
| ChannelState  | get_ready_state()                   |
| [bool](class_bool.md#class-bool)                      | is_negotiated()                       |
| [bool](class_bool.md#class-bool)                      | is_ordered()                             |
| [Error](class_@globalscope.md#enum-globalscope-error) | poll()                                         |
| [bool](class_bool.md#class-bool)                      | was_string_packet()               |

---

## Enumerations

enum **WriteMode**:

WriteMode **WRITE_MODE_TEXT** = `0`

Tells the channel to send data over this channel as text. An external peer (non-Godot) would receive this as a string.

WriteMode **WRITE_MODE_BINARY** = `1`

Tells the channel to send data over this channel as binary. An external peer (non-Godot) would receive this as array buffer or blob.

---

enum **ChannelState**:

ChannelState **STATE_CONNECTING** = `0`

The channel was created, but it's still trying to connect.

ChannelState **STATE_OPEN** = `1`

The channel is currently open, and data can flow over it.

ChannelState **STATE_CLOSING** = `2`

The channel is being closed, no new messages will be accepted, but those already in queue will be flushed.

ChannelState **STATE_CLOSED** = `3`

The channel was closed, or connection failed.

---

## Property Descriptions

WriteMode **write_mode** = `1`

-  **set_write_mode**(value: WriteMode)
- WriteMode **get_write_mode**()

The transfer mode to use when sending outgoing packet. Either text or binary.

---

## Method Descriptions

 **close**()

Closes this data channel, notifying the other peer.

---

[int](class_int.md#class-int) **get_buffered_amount**()

Returns the number of bytes currently queued to be sent over this channel.

---

[int](class_int.md#class-int) **get_id**()

Returns the ID assigned to this channel during creation (or auto-assigned during negotiation).

If the channel is not negotiated out-of-band the ID will only be available after the connection is established (will return `65535` until then).

---

[String](class_string.md#class-string) **get_label**()

Returns the label assigned to this channel during creation.

---

[int](class_int.md#class-int) **get_max_packet_life_time**()

Returns the `maxPacketLifeTime` value assigned to this channel during creation.

Will be `65535` if not specified.

---

[int](class_int.md#class-int) **get_max_retransmits**()

Returns the `maxRetransmits` value assigned to this channel during creation.

Will be `65535` if not specified.

---

[String](class_string.md#class-string) **get_protocol**()

Returns the sub-protocol assigned to this channel during creation. An empty string if not specified.

---

ChannelState **get_ready_state**()

Returns the current state of this channel.

---

[bool](class_bool.md#class-bool) **is_negotiated**()

Returns `true` if this channel was created with out-of-band configuration.

---

[bool](class_bool.md#class-bool) **is_ordered**()

Returns `true` if this channel was created with ordering enabled (default).

---

[Error](class_@globalscope.md#enum-globalscope-error) **poll**()

Reserved, but not used for now.

---

[bool](class_bool.md#class-bool) **was_string_packet**()

Returns `true` if the last received packet was transferred as text. See write_mode.
