# TCPServer

**Inherits:** [SocketServer](class_socketserver.md#class-socketserver) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A TCP server.

## Description

A TCP server. Listens to connections on a port and returns a [StreamPeerTCP](class_streampeertcp.md#class-streampeertcp) when it gets an incoming connection.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Methods

| [int](class_int.md#class-int)                               | get_local_port()                                                                                 |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)       | listen(port: [int](class_int.md#class-int), bind_address: [String](class_string.md#class-string) = "\*") |
| [StreamPeerTCP](class_streampeertcp.md#class-streampeertcp) | take_connection()                                                                               |

---

## Method Descriptions

[int](class_int.md#class-int) **get_local_port**()

Returns the local port this server is listening to.

---

[Error](class_@globalscope.md#enum-globalscope-error) **listen**(port: [int](class_int.md#class-int), bind_address: [String](class_string.md#class-string) = "\*")

Listen on the `port` binding to `bind_address`.

If `bind_address` is set as `"*"` (default), the server will listen on all available addresses (both IPv4 and IPv6).

If `bind_address` is set as `"0.0.0.0"` (for IPv4) or `"::"` (for IPv6), the server will listen on all available addresses matching that IP type.

If `bind_address` is set to any valid address (e.g. `"192.168.1.101"`, `"::1"`, etc.), the server will only listen on the interface with that address (or fail if no interface with the given address exists).

---

[StreamPeerTCP](class_streampeertcp.md#class-streampeertcp) **take_connection**()

If a connection is available, returns a StreamPeerTCP with the connection.
