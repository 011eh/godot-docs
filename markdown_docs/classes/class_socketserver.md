# SocketServer

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [TCPServer](class_tcpserver.md#class-tcpserver), [UDSServer](class_udsserver.md#class-udsserver)

An abstract class for servers based on sockets.

## Description

A socket server.

## Methods

| [bool](class_bool.md#class-bool)                                     | is_connection_available()    |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                     | is_listening()                          |
|                                                                      | stop()                                          |
| [StreamPeerSocket](class_streampeersocket.md#class-streampeersocket) | take_socket_connection()      |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **is_connection_available**()

Returns `true` if a connection is available for taking.

---

[bool](class_bool.md#class-bool) **is_listening**()

Returns `true` if the server is currently listening for connections.

---

 **stop**()

Stops listening.

---

[StreamPeerSocket](class_streampeersocket.md#class-streampeersocket) **take_socket_connection**()

If a connection is available, returns a StreamPeerSocket with the connection.
