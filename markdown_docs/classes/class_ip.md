# IP

**Inherits:** [Object](class_object.md#class-object)

Internet protocol (IP) support functions such as DNS resolution.

## Description

IP contains support functions for the Internet Protocol (IP). TCP/IP support is in different classes (see [StreamPeerTCP](class_streampeertcp.md#class-streampeertcp) and [TCPServer](class_tcpserver.md#class-tcpserver)). IP provides DNS hostname resolution support, both blocking and threaded.

## Methods

|                                                                                         | clear_cache(hostname: [String](class_string.md#class-string) = "")                                                            |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                         | erase_resolve_item(id: [int](class_int.md#class-int))                                                                  |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | get_local_addresses()                                                                                                 |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | get_local_interfaces()                                                                                               |
| [String](class_string.md#class-string)                                                  | get_resolve_item_address(id: [int](class_int.md#class-int))                                                      |
| [Array](class_array.md#class-array)                                                     | get_resolve_item_addresses(id: [int](class_int.md#class-int))                                                  |
| ResolverStatus                                               | get_resolve_item_status(id: [int](class_int.md#class-int))                                                        |
| [String](class_string.md#class-string)                                                  | resolve_hostname(host: [String](class_string.md#class-string), ip_type: Type = 3)                       |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | resolve_hostname_addresses(host: [String](class_string.md#class-string), ip_type: Type = 3)   |
| [int](class_int.md#class-int)                                                           | resolve_hostname_queue_item(host: [String](class_string.md#class-string), ip_type: Type = 3) |

---

## Enumerations

enum **ResolverStatus**:

ResolverStatus **RESOLVER_STATUS_NONE** = `0`

DNS hostname resolver status: No status.

ResolverStatus **RESOLVER_STATUS_WAITING** = `1`

DNS hostname resolver status: Waiting.

ResolverStatus **RESOLVER_STATUS_DONE** = `2`

DNS hostname resolver status: Done.

ResolverStatus **RESOLVER_STATUS_ERROR** = `3`

DNS hostname resolver status: Error.

---

enum **Type**:

Type **TYPE_NONE** = `0`

Address type: None.

Type **TYPE_IPV4** = `1`

Address type: Internet protocol version 4 (IPv4).

Type **TYPE_IPV6** = `2`

Address type: Internet protocol version 6 (IPv6).

Type **TYPE_ANY** = `3`

Address type: Any.

---

## Constants

**RESOLVER_MAX_QUERIES** = `256`

Maximum number of concurrent DNS resolver queries allowed, RESOLVER_INVALID_ID is returned if exceeded.

**RESOLVER_INVALID_ID** = `-1`

Invalid ID constant. Returned if RESOLVER_MAX_QUERIES is exceeded.

---

## Method Descriptions

 **clear_cache**(hostname: [String](class_string.md#class-string) = "")

Removes all of a `hostname`'s cached references. If no `hostname` is given, all cached IP addresses are removed.

---

 **erase_resolve_item**(id: [int](class_int.md#class-int))

Removes a given item `id` from the queue. This should be used to free a queue after it has completed to enable more queries to happen.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_local_addresses**()

Returns all the user's current IPv4 and IPv6 addresses as an array.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_local_interfaces**()

Returns all network adapters as an array.

Each adapter is a dictionary of the form:

```gdscript
{
    "index": "1", # Interface index.
    "name": "eth0", # Interface name.
    "friendly": "Ethernet One", # A friendly name (might be empty).
    "addresses": ["192.168.1.101"], # An array of IP addresses associated to this interface.
}
```

---

[String](class_string.md#class-string) **get_resolve_item_address**(id: [int](class_int.md#class-int))

Returns a queued hostname's IP address, given its queue `id`. Returns an empty string on error or if resolution hasn't happened yet (see get_resolve_item_status()).

---

[Array](class_array.md#class-array) **get_resolve_item_addresses**(id: [int](class_int.md#class-int))

Returns resolved addresses, or an empty array if an error happened or resolution didn't happen yet (see get_resolve_item_status()).

---

ResolverStatus **get_resolve_item_status**(id: [int](class_int.md#class-int))

Returns a queued hostname's status as a ResolverStatus constant, given its queue `id`.

---

[String](class_string.md#class-string) **resolve_hostname**(host: [String](class_string.md#class-string), ip_type: Type = 3)

Returns a given hostname's IPv4 or IPv6 address when resolved (blocking-type method). The address type returned depends on the Type constant given as `ip_type`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **resolve_hostname_addresses**(host: [String](class_string.md#class-string), ip_type: Type = 3)

Resolves a given hostname in a blocking way. Addresses are returned as an [Array](class_array.md#class-array) of IPv4 or IPv6 addresses depending on `ip_type`.

---

[int](class_int.md#class-int) **resolve_hostname_queue_item**(host: [String](class_string.md#class-string), ip_type: Type = 3)

Creates a queue item to resolve a hostname to an IPv4 or IPv6 address depending on the Type constant given as `ip_type`. Returns the queue ID if successful, or RESOLVER_INVALID_ID on error.
