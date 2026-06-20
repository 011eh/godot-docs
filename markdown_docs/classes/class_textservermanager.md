# TextServerManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [TextServer](class_textserver.md#class-textserver) implementations.

## Description

**TextServerManager** is the API backend for loading, enumerating, and switching [TextServer](class_textserver.md#class-textserver)s.

**Note:** Switching text server at runtime is possible, but will invalidate all fonts and text buffers. Make sure to unload all controls, fonts, and themes before doing so.

## Methods

|                                                                                         | add_interface(interface: [TextServer](class_textserver.md#class-textserver))             |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [TextServer](class_textserver.md#class-textserver)                                      | find_interface(name: [String](class_string.md#class-string))                            |
| [TextServer](class_textserver.md#class-textserver)                                      | get_interface(idx: [int](class_int.md#class-int))                                        |
| [int](class_int.md#class-int)                                                           | get_interface_count()                                                              |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | get_interfaces()                                                                        |
| [TextServer](class_textserver.md#class-textserver)                                      | get_primary_interface()                                                          |
|                                                                                         | remove_interface(interface: [TextServer](class_textserver.md#class-textserver))       |
|                                                                                         | set_primary_interface(index: [TextServer](class_textserver.md#class-textserver)) |

---

## Signals

**interface_added**(interface_name: [StringName](class_stringname.md#class-stringname))

Emitted when a new interface has been added.

---

**interface_removed**(interface_name: [StringName](class_stringname.md#class-stringname))

Emitted when an interface is removed.

---

## Method Descriptions

 **add_interface**(interface: [TextServer](class_textserver.md#class-textserver))

Registers a [TextServer](class_textserver.md#class-textserver) interface.

---

[TextServer](class_textserver.md#class-textserver) **find_interface**(name: [String](class_string.md#class-string))

Finds an interface by its `name`.

---

[TextServer](class_textserver.md#class-textserver) **get_interface**(idx: [int](class_int.md#class-int))

Returns the interface registered at a given index.

---

[int](class_int.md#class-int) **get_interface_count**()

Returns the number of interfaces currently registered.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_interfaces**()

Returns a list of available interfaces, with the index and name of each interface.

---

[TextServer](class_textserver.md#class-textserver) **get_primary_interface**()

Returns the primary [TextServer](class_textserver.md#class-textserver) interface currently in use.

---

 **remove_interface**(interface: [TextServer](class_textserver.md#class-textserver))

Removes an interface. All fonts and shaped text caches should be freed before removing an interface.

---

 **set_primary_interface**(index: [TextServer](class_textserver.md#class-textserver))

Sets the primary [TextServer](class_textserver.md#class-textserver) interface.
