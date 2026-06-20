# VisualShaderNodeCustom

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Virtual class to define custom [VisualShaderNode](class_visualshadernode.md#class-visualshadernode)s for use in the Visual Shader Editor.

## Description

By inheriting this class you can create a custom [VisualShader](class_visualshader.md#class-visualshader) script addon which will be automatically added to the Visual Shader Editor. The [VisualShaderNode](class_visualshadernode.md#class-visualshadernode)'s behavior is defined by overriding the provided virtual methods.

In order for the node to be registered as an editor addon, you must use the `@tool` annotation and provide a `class_name` for your custom script. For example:

```gdscript
@tool
extends VisualShaderNodeCustom
class_name VisualShaderNodeNoise
```

## Tutorials

- [Visual Shader plugins](../tutorials/plugins/editor/visual_shader_plugins.md)

## Methods

| [String](class_string.md#class-string)                                  | \_get_category()                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                                  | \_get_code(input_vars: [Array](class_array.md#class-array)[[String](class_string.md#class-string)], output_vars: [Array](class_array.md#class-array)[[String](class_string.md#class-string)], mode: [Mode](class_shader.md#enum-shader-mode), type: [Type](class_visualshader.md#enum-visualshader-type)) |
| [int](class_int.md#class-int)                                           | \_get_default_input_port(type: [PortType](class_visualshadernode.md#enum-visualshadernode-porttype))                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                  | \_get_description()                                                                                                                                                                                                                                                                                |
| [String](class_string.md#class-string)                                  | \_get_func_code(mode: [Mode](class_shader.md#enum-shader-mode), type: [Type](class_visualshader.md#enum-visualshader-type))                                                                                                                                                                          |
| [String](class_string.md#class-string)                                  | \_get_global_code(mode: [Mode](class_shader.md#enum-shader-mode))                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                           | \_get_input_port_count()                                                                                                                                                                                                                                                                      |
| [Variant](class_variant.md#class-variant)                               | \_get_input_port_default_value(port: [int](class_int.md#class-int))                                                                                                                                                                                                                   |
| [String](class_string.md#class-string)                                  | \_get_input_port_name(port: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)    | \_get_input_port_type(port: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)                                  | \_get_name()                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                           | \_get_output_port_count()                                                                                                                                                                                                                                                                    |
| [String](class_string.md#class-string)                                  | \_get_output_port_name(port: [int](class_int.md#class-int))                                                                                                                                                                                                                                   |
| [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)    | \_get_output_port_type(port: [int](class_int.md#class-int))                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                           | \_get_property_count()                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                           | \_get_property_default_index(index: [int](class_int.md#class-int))                                                                                                                                                                                                                      |
| [String](class_string.md#class-string)                                  | \_get_property_name(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                        |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | \_get_property_options(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                  |
| [PortType](class_visualshadernode.md#enum-visualshadernode-porttype)    | \_get_return_icon_type()                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                        | \_is_available(mode: [Mode](class_shader.md#enum-shader-mode), type: [Type](class_visualshader.md#enum-visualshader-type))                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                        | \_is_highend()                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                           | get_option_index(option: [int](class_int.md#class-int))                                                                                                                                                                                                                                                   |

---

## Method Descriptions

[String](class_string.md#class-string) **\_get_category**()

Override this method to define the path to the associated custom node in the Visual Shader Editor's members dialog. The path may look like `"MyGame/MyFunctions/Noise"`.

Defining this method is **optional**. If not overridden, the node will be filed under the "Addons" category.

---

[String](class_string.md#class-string) **\_get_code**(input_vars: [Array](class_array.md#class-array)[[String](class_string.md#class-string)], output_vars: [Array](class_array.md#class-array)[[String](class_string.md#class-string)], mode: [Mode](class_shader.md#enum-shader-mode), type: [Type](class_visualshader.md#enum-visualshader-type))

Override this method to define the actual shader code of the associated custom node. The shader code should be returned as a string, which can have multiple lines (the `"""` multiline string construct can be used for convenience).

The `input_vars` and `output_vars` arrays contain the string names of the various input and output variables, as defined by `_get_input_*` and `_get_output_*` virtual methods in this class.

The output ports can be assigned values in the shader code. For example, `return output_vars[0] + " = " + input_vars[0] + ";"`.

You can customize the generated code based on the shader `mode` and/or `type`.

Defining this method is **required**.

---

[int](class_int.md#class-int) **\_get_default_input_port**(type: [PortType](class_visualshadernode.md#enum-visualshadernode-porttype))

Override this method to define the input port which should be connected by default when this node is created as a result of dragging a connection from an existing node to the empty space on the graph.

Defining this method is **optional**. If not overridden, the connection will be created to the first valid port.

---

[String](class_string.md#class-string) **\_get_description**()

Override this method to define the description of the associated custom node in the Visual Shader Editor's members dialog.

Defining this method is **optional**.

---

[String](class_string.md#class-string) **\_get_func_code**(mode: [Mode](class_shader.md#enum-shader-mode), type: [Type](class_visualshader.md#enum-visualshader-type))

Override this method to add a shader code to the beginning of each shader function (once). The shader code should be returned as a string, which can have multiple lines (the `"""` multiline string construct can be used for convenience).

If there are multiple custom nodes of different types which use this feature the order of each insertion is undefined.

You can customize the generated code based on the shader `mode` and/or `type`.

Defining this method is **optional**.

---

[String](class_string.md#class-string) **\_get_global_code**(mode: [Mode](class_shader.md#enum-shader-mode))

Override this method to add shader code on top of the global shader, to define your own standard library of reusable methods, varyings, constants, uniforms, etc. The shader code should be returned as a string, which can have multiple lines (the `"""` multiline string construct can be used for convenience).

Be careful with this functionality as it can cause name conflicts with other custom nodes, so be sure to give the defined entities unique names.

You can customize the generated code based on the shader `mode`.

Defining this method is **optional**.

---

[int](class_int.md#class-int) **\_get_input_port_count**()

Override this method to define the number of input ports of the associated custom node.

Defining this method is **required**. If not overridden, the node has no input ports.

---

[Variant](class_variant.md#class-variant) **\_get_input_port_default_value**(port: [int](class_int.md#class-int))

Override this method to define the default value for the specified input port. Prefer use this over [VisualShaderNode.set_input_port_default_value()](class_visualshadernode.md#class-visualshadernode-method-set-input-port-default-value).

Defining this method is **required**. If not overridden, the node has no default values for their input ports.

---

[String](class_string.md#class-string) **\_get_input_port_name**(port: [int](class_int.md#class-int))

Override this method to define the names of input ports of the associated custom node. The names are used both for the input slots in the editor and as identifiers in the shader code, and are passed in the `input_vars` array in \_get_code().

Defining this method is **optional**, but recommended. If not overridden, input ports are named as `"in" + str(port)`.

---

[PortType](class_visualshadernode.md#enum-visualshadernode-porttype) **\_get_input_port_type**(port: [int](class_int.md#class-int))

Override this method to define the returned type of each input port of the associated custom node.

Defining this method is **optional**, but recommended. If not overridden, input ports will return the [VisualShaderNode.PORT_TYPE_SCALAR](class_visualshadernode.md#class-visualshadernode-constant-port-type-scalar) type.

---

[String](class_string.md#class-string) **\_get_name**()

Override this method to define the name of the associated custom node in the Visual Shader Editor's members dialog and graph.

Defining this method is **optional**, but recommended. If not overridden, the node will be named as "Unnamed".

---

[int](class_int.md#class-int) **\_get_output_port_count**()

Override this method to define the number of output ports of the associated custom node.

Defining this method is **required**. If not overridden, the node has no output ports.

---

[String](class_string.md#class-string) **\_get_output_port_name**(port: [int](class_int.md#class-int))

Override this method to define the names of output ports of the associated custom node. The names are used both for the output slots in the editor and as identifiers in the shader code, and are passed in the `output_vars` array in \_get_code().

Defining this method is **optional**, but recommended. If not overridden, output ports are named as `"out" + str(port)`.

---

[PortType](class_visualshadernode.md#enum-visualshadernode-porttype) **\_get_output_port_type**(port: [int](class_int.md#class-int))

Override this method to define the returned type of each output port of the associated custom node.

Defining this method is **optional**, but recommended. If not overridden, output ports will return the [VisualShaderNode.PORT_TYPE_SCALAR](class_visualshadernode.md#class-visualshadernode-constant-port-type-scalar) type.

---

[int](class_int.md#class-int) **\_get_property_count**()

Override this method to define the number of the properties.

Defining this method is **optional**.

---

[int](class_int.md#class-int) **\_get_property_default_index**(index: [int](class_int.md#class-int))

Override this method to define the default index of the property of the associated custom node.

Defining this method is **optional**.

---

[String](class_string.md#class-string) **\_get_property_name**(index: [int](class_int.md#class-int))

Override this method to define the names of the property of the associated custom node.

Defining this method is **optional**.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_property_options**(index: [int](class_int.md#class-int))

Override this method to define the options inside the drop-down list property of the associated custom node.

Defining this method is **optional**.

---

[PortType](class_visualshadernode.md#enum-visualshadernode-porttype) **\_get_return_icon_type**()

Override this method to define the return icon of the associated custom node in the Visual Shader Editor's members dialog.

Defining this method is **optional**. If not overridden, no return icon is shown.

---

[bool](class_bool.md#class-bool) **\_is_available**(mode: [Mode](class_shader.md#enum-shader-mode), type: [Type](class_visualshader.md#enum-visualshader-type))

Override this method to prevent the node to be visible in the member dialog for the certain `mode` and/or `type`.

Defining this method is **optional**. If not overridden, it's `true`.

---

[bool](class_bool.md#class-bool) **\_is_highend**()

Override this method to enable the high-end mark in the Visual Shader Editor's members dialog. This should return `true` for nodes that only work when using the Forward+ and Mobile renderers.

Defining this method is **optional**. If not overridden, it's `false`, which indicates this node works with all renderers (including Compatibility).

---

[int](class_int.md#class-int) **get_option_index**(option: [int](class_int.md#class-int))

Returns the selected index of the drop-down list option within a graph. You may use this function to define the specific behavior in the \_get_code() or \_get_global_code().
