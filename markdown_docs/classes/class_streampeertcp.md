# StreamPeerTCP

**Inherits:** [StreamPeerSocket](class_streampeersocket.md#class-streampeersocket) **<** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A stream peer that handles TCP connections.

## Description

A stream peer that handles TCP connections. This object can be used to connect to TCP servers, or also is returned by a TCP server.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

## Methods

| [Error](class_@globalscope.md#enum-globalscope-error)   | bind(port: [int](class_int.md#class-int), host: [String](class_string.md#class-string) = "\*")                |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)   | connect_to_host(host: [String](class_string.md#class-string), port: [int](class_int.md#class-int)) |
| [String](class_string.md#class-string)                  | get_connected_host()                                                                            |
| [int](class_int.md#class-int)                           | get_connected_port()                                                                            |
| [int](class_int.md#class-int)                           | get_local_port()                                                                                    |
|                                                         | set_no_delay(enabled: [bool](class_bool.md#class-bool))                                               |

---

## Method Descriptions

[Error](class_@globalscope.md#enum-globalscope-error) **bind**(port: [int](class_int.md#class-int), host: [String](class_string.md#class-string) = "\*")

Opens the TCP socket, and binds it to the specified local address.

This method is generally not needed, and only used to force the subsequent call to connect_to_host() to use the specified `host` and `port` as source address. This can be desired in some NAT punchthrough techniques, or when forcing the source network interface.

---

[Error](class_@globalscope.md#enum-globalscope-error) **connect_to_host**(host: [String](class_string.md#class-string), port: [int](class_int.md#class-int))

Connects to the specified `host:port` pair. A hostname will be resolved if valid. Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success.

---

[String](class_string.md#class-string) **get_connected_host**()

Returns the IP of this peer.

---

[int](class_int.md#class-int) **get_connected_port**()

Returns the port of this peer.

---

[int](class_int.md#class-int) **get_local_port**()

Returns the local port to which this peer is bound.

---

 **set_no_delay**(enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, packets will be sent immediately. If `enabled` is `false` (the default), packet transfers will be delayed and combined using [Nagle's algorithm](https://en.wikipedia.org/wiki/Nagle%27s_algorithm).

**Note:** It's recommended to leave this disabled for applications that send large packets or need to transfer a lot of data, as enabling this can decrease the total available bandwidth.
