# VisualShaderNodeParameter

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisualShaderNodeBooleanParameter](class_visualshadernodebooleanparameter.md#class-visualshadernodebooleanparameter), [VisualShaderNodeColorParameter](class_visualshadernodecolorparameter.md#class-visualshadernodecolorparameter), [VisualShaderNodeFloatParameter](class_visualshadernodefloatparameter.md#class-visualshadernodefloatparameter), [VisualShaderNodeIntParameter](class_visualshadernodeintparameter.md#class-visualshadernodeintparameter), [VisualShaderNodeTextureParameter](class_visualshadernodetextureparameter.md#class-visualshadernodetextureparameter), [VisualShaderNodeTransformParameter](class_visualshadernodetransformparameter.md#class-visualshadernodetransformparameter), [VisualShaderNodeUIntParameter](class_visualshadernodeuintparameter.md#class-visualshadernodeuintparameter), [VisualShaderNodeVec2Parameter](class_visualshadernodevec2parameter.md#class-visualshadernodevec2parameter), [VisualShaderNodeVec3Parameter](class_visualshadernodevec3parameter.md#class-visualshadernodevec3parameter), [VisualShaderNodeVec4Parameter](class_visualshadernodevec4parameter.md#class-visualshadernodevec4parameter)

A base type for the parameters within the visual shader graph.

## Description

A parameter represents a variable in the shader which is set externally, i.e. from the [ShaderMaterial](class_shadermaterial.md#class-shadermaterial). Parameters are exposed as properties in the [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) and can be assigned from the Inspector or from a script.

## Properties

| [int](class_int.md#class-int)                          | instance_index   | `0`   |
|--------------------------------------------------------|------------------------------------------------------------------------------|-------|
| [String](class_string.md#class-string)                 | parameter_name   | `""`  |
| Qualifier | qualifier             | `0`   |

---

## Enumerations

enum **Qualifier**:

Qualifier **QUAL_NONE** = `0`

The parameter will be tied to the [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) using this shader.

Qualifier **QUAL_GLOBAL** = `1`

The parameter will use a global value, defined in Project Settings.

Qualifier **QUAL_INSTANCE** = `2`

The parameter will be tied to the node with attached [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) using this shader.

Qualifier **QUAL_INSTANCE_INDEX** = `3`

The parameter will be tied to the node with attached [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) using this shader. Enables setting a instance_index property.

Qualifier **QUAL_MAX** = `4`

Represents the size of the Qualifier enum.

---

## Property Descriptions

[int](class_int.md#class-int) **instance_index** = `0`

-  **set_instance_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_instance_index**()

The index within 0-15 range, which is used to avoid clashes when shader used on multiple materials.

---

[String](class_string.md#class-string) **parameter_name** = `""`

-  **set_parameter_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_parameter_name**()

Name of the parameter, by which it can be accessed through the [ShaderMaterial](class_shadermaterial.md#class-shadermaterial) properties.

---

Qualifier **qualifier** = `0`

-  **set_qualifier**(value: Qualifier)
- Qualifier **get_qualifier**()

Defines the scope of the parameter.
