# WebSocketPeer

**Inherits:** [PacketPeer](class_packetpeer.md#class-packetpeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A WebSocket connection.

## Description

This class represents WebSocket connection, and can be used as a WebSocket client ([RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455)-compliant) or as a remote peer of a WebSocket server.

You can send WebSocket binary frames using [PacketPeer.put_packet()](class_packetpeer.md#class-packetpeer-method-put-packet), and WebSocket text frames using send() (prefer text frames when interacting with text-based API). You can check the frame type of the last packet via was_string_packet().

To start a WebSocket client, first call connect_to_url(), then regularly call poll() (e.g. during [Node](class_node.md#class-node) process). You can query the socket state via get_ready_state(), get the number of pending packets using [PacketPeer.get_available_packet_count()](class_packetpeer.md#class-packetpeer-method-get-available-packet-count), and retrieve them via [PacketPeer.get_packet()](class_packetpeer.md#class-packetpeer-method-get-packet).

GDScript

```gdscript
extends Node

var socket = WebSocketPeer.new()

func _ready():
    socket.connect_to_url("wss://example.com")

func _process(delta):
    socket.poll()
    var state = socket.get_ready_state()
    if state == WebSocketPeer.STATE_OPEN:
        while socket.get_available_packet_count():
            print("Packet: ", socket.get_packet())
    elif state == WebSocketPeer.STATE_CLOSING:
        # Keep polling to achieve proper close.
        pass
    elif state == WebSocketPeer.STATE_CLOSED:
        var code = socket.get_close_code()
        var reason = socket.get_close_reason()
        print("WebSocket closed with code: %d, reason %s. Clean: %s" % [code, reason, code != -1])
        set_process(false) # Stop processing.
```

To use the peer as part of a WebSocket server refer to accept_stream() and the online tutorial.

## Properties

| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)   | handshake_headers       | `PackedStringArray()`   |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------------|
| [float](class_float.md#class-float)                                       | heartbeat_interval     | `0.0`                   |
| [int](class_int.md#class-int)                                             | inbound_buffer_size   | `65535`                 |
| [int](class_int.md#class-int)                                             | max_queued_packets     | `4096`                  |
| [int](class_int.md#class-int)                                             | outbound_buffer_size | `65535`                 |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)   | supported_protocols   | `PackedStringArray()`   |

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | accept_stream(stream: [StreamPeer](class_streampeer.md#class-streampeer))                                                                   |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                         | close(code: [int](class_int.md#class-int) = 1000, reason: [String](class_string.md#class-string) = "")                                              |
| [Error](class_@globalscope.md#enum-globalscope-error)   | connect_to_url(url: [String](class_string.md#class-string), tls_client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) |
| [int](class_int.md#class-int)                           | get_close_code()                                                                                                                           |
| [String](class_string.md#class-string)                  | get_close_reason()                                                                                                                       |
| [String](class_string.md#class-string)                  | get_connected_host()                                                                                                                   |
| [int](class_int.md#class-int)                           | get_connected_port()                                                                                                                   |
| [int](class_int.md#class-int)                           | get_current_outbound_buffered_amount()                                                                               |
| State                      | get_ready_state()                                                                                                                         |
| [String](class_string.md#class-string)                  | get_requested_url()                                                                                                                     |
| [String](class_string.md#class-string)                  | get_selected_protocol()                                                                                                             |
|                                                         | poll()                                                                                                                                               |
| [Error](class_@globalscope.md#enum-globalscope-error)   | send(message: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), write_mode: WriteMode = 1)         |
| [Error](class_@globalscope.md#enum-globalscope-error)   | send_text(message: [String](class_string.md#class-string))                                                                                      |
|                                                         | set_no_delay(enabled: [bool](class_bool.md#class-bool))                                                                                      |
| [bool](class_bool.md#class-bool)                        | was_string_packet()                                                                                                                     |

---

## Enumerations

enum **WriteMode**:

WriteMode **WRITE_MODE_TEXT** = `0`

Specifies that WebSockets messages should be transferred as text payload (only valid UTF-8 is allowed).

WriteMode **WRITE_MODE_BINARY** = `1`

Specifies that WebSockets messages should be transferred as binary payload (any byte combination is allowed).

---

enum **State**:

State **STATE_CONNECTING** = `0`

Socket has been created. The connection is not yet open.

State **STATE_OPEN** = `1`

The connection is open and ready to communicate.

State **STATE_CLOSING** = `2`

The connection is in the process of closing. This means a close request has been sent to the remote peer but confirmation has not been received.

State **STATE_CLOSED** = `3`

The connection is closed or couldn't be opened.

---

## Property Descriptions

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **handshake_headers** = `PackedStringArray()`

-  **set_handshake_headers**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_handshake_headers**()

The extra HTTP headers to be sent during the WebSocket handshake.

**Note:** Not supported in Web exports due to browsers' restrictions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

[float](class_float.md#class-float) **heartbeat_interval** = `0.0`

-  **set_heartbeat_interval**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_heartbeat_interval**()

The interval (in seconds) at which the peer will automatically send WebSocket "ping" control frames. When set to `0`, no "ping" control frames will be sent.

**Note:** Has no effect in Web exports due to browser restrictions.

---

[int](class_int.md#class-int) **inbound_buffer_size** = `65535`

-  **set_inbound_buffer_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_inbound_buffer_size**()

The size of the input buffer in bytes (roughly the maximum amount of memory that will be allocated for the inbound packets).

---

[int](class_int.md#class-int) **max_queued_packets** = `4096`

-  **set_max_queued_packets**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_max_queued_packets**()

The maximum amount of packets that will be allowed in the queues (both inbound and outbound).

---

[int](class_int.md#class-int) **outbound_buffer_size** = `65535`

-  **set_outbound_buffer_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_outbound_buffer_size**()

The size of the input buffer in bytes (roughly the maximum amount of memory that will be allocated for the outbound packets).

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **supported_protocols** = `PackedStringArray()`

-  **set_supported_protocols**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_supported_protocols**()

The WebSocket sub-protocols allowed during the WebSocket handshake.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **accept_stream**(stream: [StreamPeer](class_streampeer.md#class-streampeer))

Accepts a peer connection performing the HTTP handshake as a WebSocket server. The `stream` must be a valid TCP stream retrieved via [TCPServer.take_connection()](class_tcpserver.md#class-tcpserver-method-take-connection), or a TLS stream accepted via [StreamPeerTLS.accept_stream()](class_streampeertls.md#class-streampeertls-method-accept-stream).

**Note:** Not supported in Web exports due to browsers' restrictions.

---

 **close**(code: [int](class_int.md#class-int) = 1000, reason: [String](class_string.md#class-string) = "")

Closes this WebSocket connection.

`code` is the status code for the closure (see [RFC 6455 section 7.4](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1) for a list of valid status codes). If `code` is negative, the connection will be closed immediately without notifying the remote peer.

`reason` is the human-readable reason for closing the connection. It can be any UTF-8 string that's smaller than 123 bytes.

**Note:** To achieve a clean closure, you will need to keep polling until STATE_CLOSED is reached.

**Note:** The Web export might not support all status codes. Please refer to browser-specific documentation for more details.

---

[Error](class_@globalscope.md#enum-globalscope-error) **connect_to_url**(url: [String](class_string.md#class-string), tls_client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null)

Connects to the given URL. TLS certificates will be verified against the hostname when connecting using the `wss://` protocol. You can pass the optional `tls_client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class-tlsoptions-method-client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class-tlsoptions-method-client-unsafe).

**Note:** This method is non-blocking, and will return [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) before the connection is established as long as the provided parameters are valid and the peer is not in an invalid state (e.g. already connected). Regularly call poll() (e.g. during [Node](class_node.md#class-node) process) and check the result of get_ready_state() to know whether the connection succeeds or fails.

**Note:** To avoid mixed content warnings or errors in Web, you may have to use a `url` that starts with `wss://` (secure) instead of `ws://`. When doing so, make sure to use the fully qualified domain name that matches the one defined in the server's TLS certificate. Do not connect directly via the IP address for `wss://` connections, as it won't match with the TLS certificate.

---

[int](class_int.md#class-int) **get_close_code**()

Returns the received WebSocket close frame status code, or `-1` when the connection was not cleanly closed. Only call this method when get_ready_state() returns STATE_CLOSED.

---

[String](class_string.md#class-string) **get_close_reason**()

Returns the received WebSocket close frame status reason string. Only call this method when get_ready_state() returns STATE_CLOSED.

---

[String](class_string.md#class-string) **get_connected_host**()

Returns the IP address of the connected peer.

**Note:** Not available in the Web export.

---

[int](class_int.md#class-int) **get_connected_port**()

Returns the remote port of the connected peer.

**Note:** Not available in the Web export.

---

[int](class_int.md#class-int) **get_current_outbound_buffered_amount**()

Returns the current amount of data in the outbound websocket buffer. **Note:** Web exports use WebSocket.bufferedAmount, while other platforms use an internal buffer.

---

State **get_ready_state**()

Returns the ready state of the connection.

---

[String](class_string.md#class-string) **get_requested_url**()

Returns the URL requested by this peer. The URL is derived from the `url` passed to connect_to_url() or from the HTTP headers when acting as server (i.e. when using accept_stream()).

---

[String](class_string.md#class-string) **get_selected_protocol**()

Returns the selected WebSocket sub-protocol for this connection or an empty string if the sub-protocol has not been selected yet.

---

 **poll**()

Updates the connection state and receive incoming packets. Call this function regularly to keep it in a clean state.

---

[Error](class_@globalscope.md#enum-globalscope-error) **send**(message: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), write_mode: WriteMode = 1)

Sends the given `message` using the desired `write_mode`. When sending a [String](class_string.md#class-string), prefer using send_text().

---

[Error](class_@globalscope.md#enum-globalscope-error) **send_text**(message: [String](class_string.md#class-string))

Sends the given `message` using WebSocket text mode. Prefer this method over [PacketPeer.put_packet()](class_packetpeer.md#class-packetpeer-method-put-packet) when interacting with third-party text-based API (e.g. when using [JSON](class_json.md#class-json) formatted messages).

---

 **set_no_delay**(enabled: [bool](class_bool.md#class-bool))

Disable Nagle's algorithm on the underlying TCP socket (default). See [StreamPeerTCP.set_no_delay()](class_streampeertcp.md#class-streampeertcp-method-set-no-delay) for more information.

**Note:** Not available in the Web export.

---

[bool](class_bool.md#class-bool) **was_string_packet**()

Returns `true` if the last received packet was sent as a text payload. See WriteMode.
