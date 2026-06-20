# StreamPeerUDS

**Inherits:** [StreamPeerSocket](class_streampeersocket.md#class-streampeersocket) **<** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A stream peer that handles UNIX Domain Socket (UDS) connections.

## Description

A stream peer that handles UNIX Domain Socket (UDS) connections. This object can be used to connect to UDS servers, or also is returned by a UDS server. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Note:** UNIX Domain Sockets are only available on UNIX-like systems (Linux, macOS, etc.) and are not supported on Windows.

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | bind(path: [String](class_string.md#class-string))                       |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)   | connect_to_host(path: [String](class_string.md#class-string)) |
| [String](class_string.md#class-string)                  | get_connected_path()                                       |

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **bind**(path: [String](class_string.md#class-string))

Opens the UDS socket, and binds it to the specified socket path.

This method is generally not needed, and only used to force the subsequent call to connect_to_host() to use the specified `path` as the source address.

---

[Error](class_@globalscope.md#enum-globalscope-error) **connect_to_host**(path: [String](class_string.md#class-string))

Connects to the specified UNIX Domain Socket path. Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success.

---

[String](class_string.md#class-string) **get_connected_path**()

Returns the socket path of this peer.
