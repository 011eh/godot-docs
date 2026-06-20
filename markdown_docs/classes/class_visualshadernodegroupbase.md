# VisualShaderNodeGroupBase

**Inherits:** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class-visualshadernoderesizablebase) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeExpression](class_visualshadernodeexpression.md#class-visualshadernodeexpression)

Base class for a family of nodes with variable number of input and output ports within the visual shader graph.

## Description

Currently, has no direct usage, use the derived classes instead.

## Methods

|                                        | add_input_port(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int), name: [String](class_string.md#class-string))   |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                        | add_output_port(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int), name: [String](class_string.md#class-string)) |
|                                        | clear_input_ports()                                                                                                                 |
|                                        | clear_output_ports()                                                                                                               |
| [int](class_int.md#class-int)          | get_free_input_port_id()                                                                                                       |
| [int](class_int.md#class-int)          | get_free_output_port_id()                                                                                                     |
| [int](class_int.md#class-int)          | get_input_port_count()                                                                                                           |
| [String](class_string.md#class-string) | get_inputs()                                                                                                                               |
| [int](class_int.md#class-int)          | get_output_port_count()                                                                                                         |
| [String](class_string.md#class-string) | get_outputs()                                                                                                                             |
| [bool](class_bool.md#class-bool)       | has_input_port(id: [int](class_int.md#class-int))                                                                                      |
| [bool](class_bool.md#class-bool)       | has_output_port(id: [int](class_int.md#class-int))                                                                                    |
| [bool](class_bool.md#class-bool)       | is_valid_port_name(name: [String](class_string.md#class-string))                                                                   |
|                                        | remove_input_port(id: [int](class_int.md#class-int))                                                                                |
|                                        | remove_output_port(id: [int](class_int.md#class-int))                                                                              |
|                                        | set_input_port_name(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                              |
|                                        | set_input_port_type(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int))                                       |
|                                        | set_inputs(inputs: [String](class_string.md#class-string))                                                                                 |
|                                        | set_output_port_name(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                            |
|                                        | set_output_port_type(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int))                                     |
|                                        | set_outputs(outputs: [String](class_string.md#class-string))                                                                              |

---

## Method Descriptions

 **add_input_port**(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Adds an input port with the specified `type` (see [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)) and `name`.

---

 **add_output_port**(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Adds an output port with the specified `type` (see [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)) and `name`.

---

 **clear_input_ports**()

Removes all previously specified input ports.

---

 **clear_output_ports**()

Removes all previously specified output ports.

---

[int](class_int.md#class-int) **get_free_input_port_id**()

Returns a free input port ID which can be used in add_input_port().

---

[int](class_int.md#class-int) **get_free_output_port_id**()

Returns a free output port ID which can be used in add_output_port().

---

[int](class_int.md#class-int) **get_input_port_count**()

Returns the number of input ports in use. Alternative for get_free_input_port_id().

---

[String](class_string.md#class-string) **get_inputs**()

Returns a [String](class_string.md#class-string) description of the input ports as a colon-separated list using the format `id,type,name;` (see add_input_port()).

---

[int](class_int.md#class-int) **get_output_port_count**()

Returns the number of output ports in use. Alternative for get_free_output_port_id().

---

[String](class_string.md#class-string) **get_outputs**()

Returns a [String](class_string.md#class-string) description of the output ports as a colon-separated list using the format `id,type,name;` (see add_output_port()).

---

[bool](class_bool.md#class-bool) **has_input_port**(id: [int](class_int.md#class-int))

Returns `true` if the specified input port exists.

---

[bool](class_bool.md#class-bool) **has_output_port**(id: [int](class_int.md#class-int))

Returns `true` if the specified output port exists.

---

[bool](class_bool.md#class-bool) **is_valid_port_name**(name: [String](class_string.md#class-string))

Returns `true` if the specified port name does not override an existed port name and is valid within the shader.

---

 **remove_input_port**(id: [int](class_int.md#class-int))

Removes the specified input port.

---

 **remove_output_port**(id: [int](class_int.md#class-int))

Removes the specified output port.

---

 **set_input_port_name**(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Renames the specified input port.

---

 **set_input_port_type**(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int))

Sets the specified input port's type (see [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)).

---

 **set_inputs**(inputs: [String](class_string.md#class-string))

Defines all input ports using a [String](class_string.md#class-string) formatted as a colon-separated list: `id,type,name;` (see add_input_port()).

---

 **set_output_port_name**(id: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Renames the specified output port.

---

 **set_output_port_type**(id: [int](class_int.md#class-int), type: [int](class_int.md#class-int))

Sets the specified output port's type (see [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)).

---

 **set_outputs**(outputs: [String](class_string.md#class-string))

Defines all output ports using a [String](class_string.md#class-string) formatted as a colon-separated list: `id,type,name;` (see add_output_port()).
