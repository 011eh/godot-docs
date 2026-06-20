# VisualShader

**Inherits:** [Shader](class_shader.md#class-shader) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A custom shader program with a visual editor.

## Description

This class provides a graph-like visual editor for creating a [Shader](class_shader.md#class-shader). Although **VisualShader**s do not require coding, they share the same logic with script shaders. They use [VisualShaderNode](class_visualshadernode.md#class-visualshadernode)s that can be connected to each other to control the flow of the shader. The visual shader graph is converted to a script shader behind the scenes.

## Tutorials

- [Using VisualShaders](../tutorials/shaders/visual_shaders.md)

## Properties

| [Vector2](class_vector2.md#class-vector2)   | graph_offset   |
|---------------------------------------------|-------------------------------------------------------------|

## Methods

|                                                                                         | add_node(type: Type, node: [VisualShaderNode](class_visualshadernode.md#class-visualshadernode), position: [Vector2](class_vector2.md#class-vector2), id: [int](class_int.md#class-int))                         |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                         | add_varying(name: [String](class_string.md#class-string), mode: VaryingMode, type: VaryingType)                                                                      |
|                                                                                         | attach_node_to_frame(type: Type, id: [int](class_int.md#class-int), frame: [int](class_int.md#class-int))                                                                                            |
| [bool](class_bool.md#class-bool)                                                        | can_connect_nodes(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))       |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | connect_nodes(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))               |
|                                                                                         | connect_nodes_forced(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int)) |
|                                                                                         | detach_node_from_frame(type: Type, id: [int](class_int.md#class-int))                                                                                                                              |
|                                                                                         | disconnect_nodes(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))         |
| [VisualShaderNode](class_visualshadernode.md#class-visualshadernode)                    | get_node(type: Type, id: [int](class_int.md#class-int))                                                                                                                                                          |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | get_node_connections(type: Type)                                                                                                                                                                     |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | get_node_list(type: Type)                                                                                                                                                                                   |
| [Vector2](class_vector2.md#class-vector2)                                               | get_node_position(type: Type, id: [int](class_int.md#class-int))                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | get_valid_node_id(type: Type)                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                        | has_varying(name: [String](class_string.md#class-string))                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                        | is_node_connection(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))     |
|                                                                                         | remove_node(type: Type, id: [int](class_int.md#class-int))                                                                                                                                                    |
|                                                                                         | remove_varying(name: [String](class_string.md#class-string))                                                                                                                                                                          |
|                                                                                         | replace_node(type: Type, id: [int](class_int.md#class-int), new_class: [StringName](class_stringname.md#class-stringname))                                                                                   |
|                                                                                         | set_mode(mode: [Mode](class_shader.md#enum-shader-mode))                                                                                                                                                                                    |
|                                                                                         | set_node_position(type: Type, id: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2))                                                                                   |

---

## Enumerations

enum **Type**:

Type **TYPE_VERTEX** = `0`

A vertex shader, operating on vertices.

Type **TYPE_FRAGMENT** = `1`

A fragment shader, operating on fragments (pixels).

Type **TYPE_LIGHT** = `2`

A shader for light calculations.

Type **TYPE_START** = `3`

A function for the "start" stage of particle shader.

Type **TYPE_PROCESS** = `4`

A function for the "process" stage of particle shader.

Type **TYPE_COLLIDE** = `5`

A function for the "collide" stage (particle collision handler) of particle shader.

Type **TYPE_START_CUSTOM** = `6`

A function for the "start" stage of particle shader, with customized output.

Type **TYPE_PROCESS_CUSTOM** = `7`

A function for the "process" stage of particle shader, with customized output.

Type **TYPE_SKY** = `8`

A shader for 3D environment's sky.

Type **TYPE_FOG** = `9`

A compute shader that runs for each froxel of the volumetric fog map.

Type **TYPE_TEXTURE_BLIT** = `10`

A shader used to process blit calls to a DrawableTexture.

Type **TYPE_MAX** = `11`

Represents the size of the Type enum.

---

enum **VaryingMode**:

VaryingMode **VARYING_MODE_VERTEX_TO_FRAG_LIGHT** = `0`

Varying is passed from `Vertex` function to `Fragment` and `Light` functions.

VaryingMode **VARYING_MODE_FRAG_TO_LIGHT** = `1`

Varying is passed from `Fragment` function to `Light` function.

VaryingMode **VARYING_MODE_MAX** = `2`

Represents the size of the VaryingMode enum.

---

enum **VaryingType**:

VaryingType **VARYING_TYPE_FLOAT** = `0`

Varying is of type [float](class_float.md#class-float).

VaryingType **VARYING_TYPE_INT** = `1`

Varying is of type [int](class_int.md#class-int).

VaryingType **VARYING_TYPE_UINT** = `2`

Varying is of type unsigned [int](class_int.md#class-int).

VaryingType **VARYING_TYPE_VECTOR_2D** = `3`

Varying is of type [Vector2](class_vector2.md#class-vector2).

VaryingType **VARYING_TYPE_VECTOR_3D** = `4`

Varying is of type [Vector3](class_vector3.md#class-vector3).

VaryingType **VARYING_TYPE_VECTOR_4D** = `5`

Varying is of type [Vector4](class_vector4.md#class-vector4).

VaryingType **VARYING_TYPE_BOOLEAN** = `6`

Varying is of type [bool](class_bool.md#class-bool).

VaryingType **VARYING_TYPE_TRANSFORM** = `7`

Varying is of type [Transform3D](class_transform3d.md#class-transform3d).

VaryingType **VARYING_TYPE_MAX** = `8`

Represents the size of the VaryingType enum.

---

## Constants

**NODE_ID_INVALID** = `-1`

Indicates an invalid **VisualShader** node.

**NODE_ID_OUTPUT** = `0`

Indicates an output node of **VisualShader**.

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **graph_offset**

-  **set_graph_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_graph_offset**()

**Deprecated:** This property does nothing and always equals to zero.

Deprecated.

---

## Method Descriptions

 **add_node**(type: Type, node: [VisualShaderNode](class_visualshadernode.md#class-visualshadernode), position: [Vector2](class_vector2.md#class-vector2), id: [int](class_int.md#class-int))

Adds the specified `node` to the shader.

---

 **add_varying**(name: [String](class_string.md#class-string), mode: VaryingMode, type: VaryingType)

Adds a new varying value node to the shader.

---

 **attach_node_to_frame**(type: Type, id: [int](class_int.md#class-int), frame: [int](class_int.md#class-int))

Attaches the given node to the given frame.

---

[bool](class_bool.md#class-bool) **can_connect_nodes**(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))

Returns `true` if the specified nodes and ports can be connected together.

---

[Error](class_@globalscope.md#enum-globalscope-error) **connect_nodes**(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))

Connects the specified nodes and ports.

---

 **connect_nodes_forced**(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))

Connects the specified nodes and ports, even if they can't be connected. Such connection is invalid and will not function properly.

---

 **detach_node_from_frame**(type: Type, id: [int](class_int.md#class-int))

Detaches the given node from the frame it is attached to.

---

 **disconnect_nodes**(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))

Connects the specified nodes and ports.

---

[VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **get_node**(type: Type, id: [int](class_int.md#class-int))

Returns the shader node instance with specified `type` and `id`.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_node_connections**(type: Type)

Returns the list of connected nodes with the specified type.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_node_list**(type: Type)

Returns the list of all nodes in the shader with the specified type.

---

[Vector2](class_vector2.md#class-vector2) **get_node_position**(type: Type, id: [int](class_int.md#class-int))

Returns the position of the specified node within the shader graph.

---

[int](class_int.md#class-int) **get_valid_node_id**(type: Type)

Returns next valid node ID that can be added to the shader graph.

---

[bool](class_bool.md#class-bool) **has_varying**(name: [String](class_string.md#class-string))

Returns `true` if the shader has a varying with the given `name`.

---

[bool](class_bool.md#class-bool) **is_node_connection**(type: Type, from_node: [int](class_int.md#class-int), from_port: [int](class_int.md#class-int), to_node: [int](class_int.md#class-int), to_port: [int](class_int.md#class-int))

Returns `true` if the specified node and port connection exist.

---

 **remove_node**(type: Type, id: [int](class_int.md#class-int))

Removes the specified node from the shader.

---

 **remove_varying**(name: [String](class_string.md#class-string))

Removes a varying value node with the given `name`. Prints an error if a node with this name is not found.

---

 **replace_node**(type: Type, id: [int](class_int.md#class-int), new_class: [StringName](class_stringname.md#class-stringname))

Replaces the specified node with a node of new class type.

---

 **set_mode**(mode: [Mode](class_shader.md#enum-shader-mode))

Sets the mode of this shader.

---

 **set_node_position**(type: Type, id: [int](class_int.md#class-int), position: [Vector2](class_vector2.md#class-vector2))

Sets the position of the specified node.
