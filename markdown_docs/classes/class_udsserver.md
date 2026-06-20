# UDSServer

**Inherits:** [SocketServer](class_socketserver.md#class-socketserver) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A Unix Domain Socket (UDS) server.

## Description

A Unix Domain Socket (UDS) server. Listens to connections on a socket path and returns a [StreamPeerUDS](class_streampeeruds.md#class-streampeeruds) when it gets an incoming connection. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Note:** Unix Domain Sockets are only available on Unix-like systems (Linux, macOS, etc.) and are not supported on Windows.

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)       | listen(path: [String](class_string.md#class-string))   |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [StreamPeerUDS](class_streampeeruds.md#class-streampeeruds) | take_connection()                             |

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **listen**(path: [String](class_string.md#class-string))

Listens on the socket at `path`. The socket file will be created at the specified path.

**Note:** The socket file must not already exist at the specified path. You may need to remove any existing socket file before calling this method.

---

[StreamPeerUDS](class_streampeeruds.md#class-streampeeruds) **take_connection**()

If a connection is available, returns a StreamPeerUDS with the connection.
