# Material

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d), [BlitMaterial](class_blitmaterial.md#class-blitmaterial), [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial), [FogMaterial](class_fogmaterial.md#class-fogmaterial), [PanoramaSkyMaterial](class_panoramaskymaterial.md#class-panoramaskymaterial), [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial), [PhysicalSkyMaterial](class_physicalskymaterial.md#class-physicalskymaterial), [PlaceholderMaterial](class_placeholdermaterial.md#class-placeholdermaterial), [ProceduralSkyMaterial](class_proceduralskymaterial.md#class-proceduralskymaterial), [ShaderMaterial](class_shadermaterial.md#class-shadermaterial)

Virtual base class for applying visual properties to an object, such as color and roughness.

## Description

**Material** is a base resource used for coloring and shading geometry. All materials inherit from it and almost all [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) derived nodes carry a **Material**. A few flags and parameters are shared between all material types and are configured here.

Importantly, you can inherit from **Material** to create your own custom material type in script or in GDExtension.

## Tutorials

- [3D Material Testers Demo](https://godotengine.org/asset-library/asset/2742)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| Material   | next_pass             |
|-------------------------------|-------------------------------------------------------------|
| [int](class_int.md#class-int) | render_priority |

## Methods

| [bool](class_bool.md#class-bool)             | \_can_do_next_pass()               |
|----------------------------------------------|---------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)             | \_can_use_render_priority() |
| [Mode](class_shader.md#enum-shader-mode)     | \_get_shader_mode()                 |
| [RID](class_rid.md#class-rid)                | \_get_shader_rid()                   |
| [Resource](class_resource.md#class-resource) | create_placeholder()                     |
|                                              | inspect_native_shader_code()     |

---

## Constants

**RENDER_PRIORITY_MAX** = `127`

Maximum value for the render_priority parameter.

**RENDER_PRIORITY_MIN** = `-128`

Minimum value for the render_priority parameter.

---

## Property Descriptions

Material **next_pass**

-  **set_next_pass**(value: Material)
- Material **get_next_pass**()

Sets the **Material** to be used for the next pass. This renders the object again using a different material.

**Note:** next_pass materials are not necessarily drawn immediately after the source **Material**. Draw order is determined by material properties, render_priority, and distance to camera.

**Note:** This only applies to [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d)s and [ShaderMaterial](class_shadermaterial.md#class-shadermaterial)s with type "Spatial".

---

[int](class_int.md#class-int) **render_priority**

-  **set_render_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_render_priority**()

Sets the render priority for objects in 3D scenes. Higher priority objects will be sorted in front of lower priority objects. In other words, all objects with render_priority `1` will render on top of all objects with render_priority `0`.

**Note:** This only applies to [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d)s and [ShaderMaterial](class_shadermaterial.md#class-shadermaterial)s with type "Spatial".

**Note:** This will not impact how transparent objects are sorted relative to opaque objects or how dynamic meshes will be sorted relative to other opaque meshes. This is because all transparent objects are drawn after all opaque objects and all dynamic opaque meshes are drawn before other opaque meshes.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **\_can_do_next_pass**()

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally to determine if next_pass should be shown in the editor or not.

---

[bool](class_bool.md#class-bool) **\_can_use_render_priority**()

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally to determine if render_priority should be shown in the editor or not.

---

[Mode](class_shader.md#enum-shader-mode) **\_get_shader_mode**()

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally by various editor tools.

---

[RID](class_rid.md#class-rid) **\_get_shader_rid**()

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally by various editor tools. Used to access the RID of the **Material**'s [Shader](class_shader.md#class-shader).

---

[Resource](class_resource.md#class-resource) **create_placeholder**()

Creates a placeholder version of this resource ([PlaceholderMaterial](class_placeholdermaterial.md#class-placeholdermaterial)).

---

 **inspect_native_shader_code**()

Only available when running in the editor. Opens a popup that visualizes the generated shader code, including all variants and internal shader code. See also [Shader.inspect_native_shader_code()](class_shader.md#class-shader-method-inspect-native-shader-code).
