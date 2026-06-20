# ReflectionProbe

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Captures its surroundings to create fast, accurate reflections from a given point.

## Description

Captures its surroundings as a cubemap, and stores versions of it with increasing levels of blur to simulate different material roughnesses.

The **ReflectionProbe** is used to create high-quality reflections at a low performance cost (when update_mode is UPDATE_ONCE). **ReflectionProbe**s can be blended together and with the rest of the scene smoothly. **ReflectionProbe**s can also be combined with [VoxelGI](class_voxelgi.md#class-voxelgi), SDFGI ([Environment.sdfgi_enabled](class_environment.md#class-environment-property-sdfgi-enabled)) and screen-space reflections ([Environment.ssr_enabled](class_environment.md#class-environment-property-ssr-enabled)) to get more accurate reflections in specific areas. **ReflectionProbe**s render all objects within their cull_mask, so updating them can be quite expensive. It is best to update them once with the important static objects and then leave them as-is.

**Note:** Unlike [VoxelGI](class_voxelgi.md#class-voxelgi) and SDFGI, **ReflectionProbe**s only source their environment from a [WorldEnvironment](class_worldenvironment.md#class-worldenvironment) node. If you specify an [Environment](class_environment.md#class-environment) resource within a [Camera3D](class_camera3d.md#class-camera3d) node, it will be ignored by the **ReflectionProbe**. This can lead to incorrect lighting within the **ReflectionProbe**.

**Note:** When using the Mobile rendering method, only `8` reflection probes can be displayed on each mesh resource, while the Compatibility rendering method only supports up to `2` reflection probes on each mesh. Attempting to display more than `8` reflection probes on a single mesh resource using the Mobile renderer will result in reflection probes flickering in and out as the camera moves, while the Compatibility renderer will not render any additional probes if more than `2` reflection probes are being used.

**Note:** When using the Mobile rendering method, reflection probes will only correctly affect meshes whose visibility AABB intersects with the reflection probe's AABB. If using a shader to deform the mesh in a way that makes it go outside its AABB, [GeometryInstance3D.extra_cull_margin](class_geometryinstance3d.md#class-geometryinstance3d-property-extra-cull-margin) must be increased on the mesh. Otherwise, the reflection probe may not be visible on the mesh.

## Tutorials

- [Reflection probes](../tutorials/3d/global_illumination/reflection_probes.md)

## Properties

| [Color](class_color.md#class-color)              | ambient_color               | `Color(0, 0, 0, 1)`   |
|--------------------------------------------------|------------------------------------------------------------------------------|-----------------------|
| [float](class_float.md#class-float)              | ambient_color_energy | `1.0`                 |
| AmbientMode | ambient_mode                 | `1`                   |
| [float](class_float.md#class-float)              | blend_distance             | `1.0`                 |
| [bool](class_bool.md#class-bool)                 | box_projection             | `false`               |
| [int](class_int.md#class-int)                    | cull_mask                       | `1048575`             |
| [bool](class_bool.md#class-bool)                 | enable_shadows             | `false`               |
| [float](class_float.md#class-float)              | intensity                       | `1.0`                 |
| [bool](class_bool.md#class-bool)                 | interior                         | `false`               |
| [float](class_float.md#class-float)              | max_distance                 | `0.0`                 |
| [float](class_float.md#class-float)              | mesh_lod_threshold     | `1.0`                 |
| [Vector3](class_vector3.md#class-vector3)        | origin_offset               | `Vector3(0, 0, 0)`    |
| [int](class_int.md#class-int)                    | reflection_mask           | `1048575`             |
| [Vector3](class_vector3.md#class-vector3)        | size                                 | `Vector3(20, 20, 20)` |
| UpdateMode   | update_mode                   | `0`                   |

---

## Enumerations

enum **UpdateMode**:

UpdateMode **UPDATE_ONCE** = `0`

Update the probe once on the next frame (recommended for most objects). The corresponding radiance map will be generated over the following six frames. This takes more time to update than UPDATE_ALWAYS, but it has a lower performance cost and can result in higher-quality reflections. The ReflectionProbe is updated when its transform changes, but not when nearby geometry changes. You can force a **ReflectionProbe** update by moving the **ReflectionProbe** slightly in any direction.

UpdateMode **UPDATE_ALWAYS** = `1`

Update the probe every frame. This provides better results for fast-moving dynamic objects (such as cars). However, it has a significant performance cost. Due to the cost, it's recommended to only use one ReflectionProbe with UPDATE_ALWAYS at most per scene. For all other use cases, use UPDATE_ONCE.

---

enum **AmbientMode**:

AmbientMode **AMBIENT_DISABLED** = `0`

Do not apply any ambient lighting inside the **ReflectionProbe**'s box defined by its size.

AmbientMode **AMBIENT_ENVIRONMENT** = `1`

Apply automatically-sourced environment lighting inside the **ReflectionProbe**'s box defined by its size.

AmbientMode **AMBIENT_COLOR** = `2`

Apply custom ambient lighting inside the **ReflectionProbe**'s box defined by its size. See ambient_color and ambient_color_energy.

---

## Property Descriptions

[Color](class_color.md#class-color) **ambient_color** = `Color(0, 0, 0, 1)`

-  **set_ambient_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_ambient_color**()

The custom ambient color to use within the **ReflectionProbe**'s box defined by its size. Only effective if ambient_mode is AMBIENT_COLOR.

---

[float](class_float.md#class-float) **ambient_color_energy** = `1.0`

-  **set_ambient_color_energy**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_ambient_color_energy**()

The custom ambient color energy to use within the **ReflectionProbe**'s box defined by its size. Only effective if ambient_mode is AMBIENT_COLOR.

---

AmbientMode **ambient_mode** = `1`

-  **set_ambient_mode**(value: AmbientMode)
- AmbientMode **get_ambient_mode**()

The ambient color to use within the **ReflectionProbe**'s box defined by its size. The ambient color will smoothly blend with other **ReflectionProbe**s and the rest of the scene (outside the **ReflectionProbe**'s box defined by its size).

---

[float](class_float.md#class-float) **blend_distance** = `1.0`

-  **set_blend_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_blend_distance**()

Defines the distance in meters over which a probe blends into the scene.

---

[bool](class_bool.md#class-bool) **box_projection** = `false`

-  **set_enable_box_projection**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_box_projection_enabled**()

If `true`, enables box projection. This makes reflections look more correct in rectangle-shaped rooms by offsetting the reflection center depending on the camera's location.

**Note:** To better fit rectangle-shaped rooms that are not aligned to the grid, you can rotate the **ReflectionProbe** node.

---

[int](class_int.md#class-int) **cull_mask** = `1048575`

-  **set_cull_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_cull_mask**()

Sets the cull mask which determines what objects are drawn by this probe. Every [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) with a layer included in this cull mask will be rendered by the probe. It is best to only include large objects which are likely to take up a lot of space in the reflection in order to save on rendering cost.

This can also be used to prevent an object from reflecting upon itself (for instance, a **ReflectionProbe** centered on a vehicle).

---

[bool](class_bool.md#class-bool) **enable_shadows** = `false`

-  **set_enable_shadows**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **are_shadows_enabled**()

If `true`, computes shadows in the reflection probe. This makes the reflection probe slower to render; you may want to disable this if using the UPDATE_ALWAYS update_mode.

---

[float](class_float.md#class-float) **intensity** = `1.0`

-  **set_intensity**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_intensity**()

Defines the reflection intensity. Intensity modulates the strength of the reflection.

---

[bool](class_bool.md#class-bool) **interior** = `false`

-  **set_as_interior**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_set_as_interior**()

If `true`, reflections will ignore sky contribution.

---

[float](class_float.md#class-float) **max_distance** = `0.0`

-  **set_max_distance**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max_distance**()

The maximum distance away from the **ReflectionProbe** an object can be before it is culled. Decrease this to improve performance, especially when using the UPDATE_ALWAYS update_mode.

**Note:** The maximum reflection distance is always at least equal to the probe's extents. This means that decreasing max_distance will not always cull objects from reflections, especially if the reflection probe's box defined by its size is already large.

---

[float](class_float.md#class-float) **mesh_lod_threshold** = `1.0`

-  **set_mesh_lod_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mesh_lod_threshold**()

The automatic LOD bias to use for meshes rendered within the **ReflectionProbe** (this is analog to [Viewport.mesh_lod_threshold](class_viewport.md#class-viewport-property-mesh-lod-threshold)). Higher values will use less detailed versions of meshes that have LOD variations generated. If set to `0.0`, automatic LOD is disabled. Increase mesh_lod_threshold to improve performance at the cost of geometry detail, especially when using the UPDATE_ALWAYS update_mode.

**Note:** mesh_lod_threshold does not affect [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) visibility ranges (also known as "manual" LOD or hierarchical LOD).

---

[Vector3](class_vector3.md#class-vector3) **origin_offset** = `Vector3(0, 0, 0)`

-  **set_origin_offset**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_origin_offset**()

Sets the origin offset to be used when this **ReflectionProbe** is in box_projection mode. This can be set to a non-zero value to ensure a reflection fits a rectangle-shaped room, while reducing the number of objects that "get in the way" of the reflection.

---

[int](class_int.md#class-int) **reflection_mask** = `1048575`

-  **set_reflection_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_reflection_mask**()

Sets the reflection mask which determines what objects have reflections applied from this probe. Every [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) with a layer included in this reflection mask will have reflections applied from this probe. See also cull_mask, which can be used to exclude objects from appearing in the reflection while still making them affected by the **ReflectionProbe**.

---

[Vector3](class_vector3.md#class-vector3) **size** = `Vector3(20, 20, 20)`

-  **set_size**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_size**()

The size of the reflection probe. The larger the size, the more space covered by the probe, which will lower the perceived resolution. It is best to keep the size only as large as you need it.

**Note:** To better fit areas that are not aligned to the grid, you can rotate the **ReflectionProbe** node.

---

UpdateMode **update_mode** = `0`

-  **set_update_mode**(value: UpdateMode)
- UpdateMode **get_update_mode**()

Sets how frequently the **ReflectionProbe** is updated. Can be UPDATE_ONCE or UPDATE_ALWAYS.
