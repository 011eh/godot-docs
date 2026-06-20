# VisualShaderNodeTransformParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class-visualshadernodeparameter) **<** [VisualShaderNode](class_visualshadernode.md#class-visualshadernode) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A [Transform3D](class_transform3d.md#class-transform3d) parameter for use within the visual shader graph.

## Description

Translated to `uniform mat4` in the shader language.

## Properties

| [Transform3D](class_transform3d.md#class-transform3d)   | default_value                 | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`   |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [bool](class_bool.md#class-bool)                        | default_value_enabled | `false`                                             |

---

## Property Descriptions

[Transform3D](class_transform3d.md#class-transform3d) **default_value** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

-  **set_default_value**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_default_value**()

A default value to be assigned within the shader.

---

[bool](class_bool.md#class-bool) **default_value_enabled** = `false`

-  **set_default_value_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_value_enabled**()

Enables usage of the default_value.
