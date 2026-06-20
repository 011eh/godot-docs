# StreamPeerSocket

**Inherits:** [StreamPeer](class_streampeer.md#class-streampeer) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [StreamPeerTCP](class_streampeertcp.md#class-streampeertcp), [StreamPeerUDS](class_streampeeruds.md#class-streampeeruds)

Abstract base class for interacting with socket streams.

## Description

StreamPeerSocket is an abstract base class that defines common behavior for socket-based streams.

## Methods

|                                                       | disconnect_from_host()   |
|-------------------------------------------------------|---------------------------------------------------------------------------------|
| Status               | get_status()                       |
| [Error](class_@globalscope.md#enum-globalscope-error) | poll()                                   |

---

## Enumerations

enum **Status**:

Status **STATUS_NONE** = `0`

The initial status of the **StreamPeerSocket**. This is also the status after disconnecting.

Status **STATUS_CONNECTING** = `1`

A status representing a **StreamPeerSocket** that is connecting to a host.

Status **STATUS_CONNECTED** = `2`

A status representing a **StreamPeerSocket** that is connected to a host.

Status **STATUS_ERROR** = `3`

A status representing a **StreamPeerSocket** in error state.

---

## Method Descriptions

 **disconnect_from_host**()

Disconnects from host.

---

Status **get_status**()

Returns the status of the connection.

---

[Error](class_@globalscope.md#enum-globalscope-error) **poll**()

Polls the socket, updating its state. See get_status().
