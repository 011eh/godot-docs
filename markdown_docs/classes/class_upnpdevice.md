# UPNPDevice

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Universal Plug and Play (UPnP) device.

## Description

Universal Plug and Play (UPnP) device. See [UPNP](class_upnp.md#class-upnp) for UPnP discovery and utility functions. Provides low-level access to UPNP control commands. Allows to manage port mappings (port forwarding) and to query network information of the device (like local and external IP address and status). Note that methods on this class are synchronous and block the calling thread.

## Properties

| [String](class_string.md#class-string)   | description_url   | `""`   |
|------------------------------------------|-----------------------------------------------------------------|--------|
| [String](class_string.md#class-string)   | igd_control_url   | `""`   |
| [String](class_string.md#class-string)   | igd_our_addr         | `""`   |
| [String](class_string.md#class-string)   | igd_service_type | `""`   |
| IGDStatus  | igd_status             | `9`    |
| [String](class_string.md#class-string)   | service_type         | `""`   |

## Methods

| [int](class_int.md#class-int)          | add_port_mapping(port: [int](class_int.md#class-int), port_internal: [int](class_int.md#class-int) = 0, desc: [String](class_string.md#class-string) = "", proto: [String](class_string.md#class-string) = "UDP", duration: [int](class_int.md#class-int) = 0)    |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)          | delete_port_mapping(port: [int](class_int.md#class-int), proto: [String](class_string.md#class-string) = "UDP")                                                                                                                                                |
| [bool](class_bool.md#class-bool)       | is_valid_gateway()                                                                                                                                                                                                                                                |
| [String](class_string.md#class-string) | query_external_address()                                                                                                                                                                                                                                    |

---

## Enumerations

enum **IGDStatus**:

IGDStatus **IGD_STATUS_OK** = `0`

OK.

IGDStatus **IGD_STATUS_HTTP_ERROR** = `1`

HTTP error.

IGDStatus **IGD_STATUS_HTTP_EMPTY** = `2`

Empty HTTP response.

IGDStatus **IGD_STATUS_NO_URLS** = `3`

**Deprecated:** This value is no longer used.

Returned response contained no URLs.

IGDStatus **IGD_STATUS_NO_IGD** = `4`

Not a valid IGD.

IGDStatus **IGD_STATUS_DISCONNECTED** = `5`

Disconnected.

IGDStatus **IGD_STATUS_UNKNOWN_DEVICE** = `6`

Unknown device.

IGDStatus **IGD_STATUS_INVALID_CONTROL** = `7`

Invalid control.

IGDStatus **IGD_STATUS_MALLOC_ERROR** = `8`

**Deprecated:** This value is no longer used.

Memory allocation error.

IGDStatus **IGD_STATUS_UNKNOWN_ERROR** = `9`

Unknown error.

---

## Property Descriptions

[String](class_string.md#class-string) **description_url** = `""`

-  **set_description_url**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_description_url**()

URL to the device description.

---

[String](class_string.md#class-string) **igd_control_url** = `""`

-  **set_igd_control_url**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_igd_control_url**()

IDG control URL.

---

[String](class_string.md#class-string) **igd_our_addr** = `""`

-  **set_igd_our_addr**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_igd_our_addr**()

Address of the local machine in the network connecting it to this **UPNPDevice**.

---

[String](class_string.md#class-string) **igd_service_type** = `""`

-  **set_igd_service_type**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_igd_service_type**()

IGD service type.

---

IGDStatus **igd_status** = `9`

-  **set_igd_status**(value: IGDStatus)
- IGDStatus **get_igd_status**()

IGD status.

---

[String](class_string.md#class-string) **service_type** = `""`

-  **set_service_type**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_service_type**()

Service type.

---

## Method Descriptions

[int](class_int.md#class-int) **add_port_mapping**(port: [int](class_int.md#class-int), port_internal: [int](class_int.md#class-int) = 0, desc: [String](class_string.md#class-string) = "", proto: [String](class_string.md#class-string) = "UDP", duration: [int](class_int.md#class-int) = 0)

Adds a port mapping to forward the given external port on this **UPNPDevice** for the given protocol to the local machine. See [UPNP.add_port_mapping()](class_upnp.md#class-upnp-method-add-port-mapping).

---

[int](class_int.md#class-int) **delete_port_mapping**(port: [int](class_int.md#class-int), proto: [String](class_string.md#class-string) = "UDP")

Deletes the port mapping identified by the given port and protocol combination on this device. See [UPNP.delete_port_mapping()](class_upnp.md#class-upnp-method-delete-port-mapping).

---

[bool](class_bool.md#class-bool) **is_valid_gateway**()

Returns `true` if this is a valid IGD (InternetGatewayDevice) which potentially supports port forwarding.

---

[String](class_string.md#class-string) **query_external_address**()

Returns the external IP address of this **UPNPDevice** or an empty string.
