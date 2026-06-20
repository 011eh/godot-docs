# StreamPeerTLS

**Inherits:** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A stream peer that handles TLS connections.

## Description

A stream peer that handles TLS connections. This object can be used to connect to a TLS server or accept a single TLS client connection.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Tutorials

- [TLS certificates](../tutorials/networking/ssl_certificates.md)

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | accept_stream(stream: [StreamPeer](class_streampeer.md#class-streampeer), server_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions))                                                                     |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)   | connect_to_stream(stream: [StreamPeer](class_streampeer.md#class-streampeer), common_name: [String](class_string.md#class-string), client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null) |
|                                                         | disconnect_from_stream()                                                                                                                                                                                 |
| Status                    | get_status()                                                                                                                                                                                                         |
| [StreamPeer](class_streampeer.md#class-streampeer)      | get_stream()                                                                                                                                                                                                         |
|                                                         | poll()                                                                                                                                                                                                                     |

---

## Enumerations

enum **Status**:

Status **STATUS_DISCONNECTED** = `0`

A status representing a **StreamPeerTLS** that is disconnected.

Status **STATUS_HANDSHAKING** = `1`

A status representing a **StreamPeerTLS** during handshaking.

Status **STATUS_CONNECTED** = `2`

A status representing a **StreamPeerTLS** that is connected to a host.

Status **STATUS_ERROR** = `3`

A status representing a **StreamPeerTLS** in error state.

Status **STATUS_ERROR_HOSTNAME_MISMATCH** = `4`

An error status that shows a mismatch in the TLS certificate domain presented by the host and the domain requested for validation.

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **accept_stream**(stream: [StreamPeer](class_streampeer.md#class-streampeer), server_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions))

Accepts a peer connection as a server using the given `server_options`. See [TLSOptions.server()](class_tlsoptions.md#class-tlsoptions-method-server).

---

[Error](class_@globalscope.md#enum-globalscope-error) **connect_to_stream**(stream: [StreamPeer](class_streampeer.md#class-streampeer), common_name: [String](class_string.md#class-string), client_options: [TLSOptions](class_tlsoptions.md#class-tlsoptions) = null)

Connects to a peer using an underlying [StreamPeer](class_streampeer.md#class-streampeer) `stream` and verifying the remote certificate is correctly signed for the given `common_name`. You can pass the optional `client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class-tlsoptions-method-client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class-tlsoptions-method-client-unsafe).

---

 **disconnect_from_stream**()

Disconnects from host.

---

Status **get_status**()

Returns the status of the connection.

---

[StreamPeer](class_streampeer.md#class-streampeer) **get_stream**()

Returns the underlying [StreamPeer](class_streampeer.md#class-streampeer) connection, used in accept_stream() or connect_to_stream().

---

 **poll**()

Poll the connection to check for incoming bytes. Call this right before [StreamPeer.get_available_bytes()](class_streampeer.md#class-streampeer-method-get-available-bytes) for it to work properly.
