# ShaderMaterial

**Inherits:** [Material](class_material.md#class-material) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A material defined by a custom [Shader](class_shader.md#class-shader) program and the values of its shader parameters.

## Description

A material that uses a custom [Shader](class_shader.md#class-shader) program to render visual items (canvas items, meshes, skies, fog), or to process particles. Compared to other materials, **ShaderMaterial** gives deeper control over the generated shader code. For more information, see the shaders documentation index below.

Multiple **ShaderMaterial**s can use the same shader and configure different values for the shader uniforms.

**Note:** For performance reasons, the [Resource.changed](class_resource.md#class-resource-signal-changed) signal is only emitted when the [Resource.resource_name](class_resource.md#class-resource-property-resource-name) changes. Only in editor, it is also emitted for shader changes.

## Tutorials

- [Shaders documentation index](../tutorials/shaders/index.md)

## Properties

| [Shader](class_shader.md#class-shader)   | shader   |
|------------------------------------------|---------------------------------------------------|

## Methods

| [Variant](class_variant.md#class-variant)   | get_shader_parameter(param: [StringName](class_stringname.md#class-stringname))                                                   |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                             | set_shader_parameter(param: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant)) |

---

## Property Descriptions

[Shader](class_shader.md#class-shader) **shader**

-  **set_shader**(value: [Shader](class_shader.md#class-shader))
- [Shader](class_shader.md#class-shader) **get_shader**()

The [Shader](class_shader.md#class-shader) program used to render this material.

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **get_shader_parameter**(param: [StringName](class_stringname.md#class-stringname))

Returns the current value set for this material of a uniform in the shader.

---

 **set_shader_parameter**(param: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Changes the value set for this material of a uniform in the shader.

**Note:** `param` is case-sensitive and must match the name of the uniform in the code exactly (not the capitalized name in the inspector).

**Note:** Changes to the shader uniform will be effective on all instances using this **ShaderMaterial**. To prevent this, use per-instance uniforms with [CanvasItem.set_instance_shader_parameter()](class_canvasitem.md#class-canvasitem-method-set-instance-shader-parameter), [GeometryInstance3D.set_instance_shader_parameter()](class_geometryinstance3d.md#class-geometryinstance3d-method-set-instance-shader-parameter) or duplicate the **ShaderMaterial** resource using [Resource.duplicate()](class_resource.md#class-resource-method-duplicate). Per-instance uniforms allow for better shader reuse and are therefore faster, so they should be preferred over duplicating the **ShaderMaterial** when possible.
