# VoxelGIData

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Contains baked voxel global illumination data for use in a [VoxelGI](class_voxelgi.md#class-voxelgi) node.

## Description

**VoxelGIData** contains baked voxel global illumination for use in a [VoxelGI](class_voxelgi.md#class-voxelgi) node. **VoxelGIData** also offers several properties to adjust the final appearance of the global illumination. These properties can be adjusted at run-time without having to bake the [VoxelGI](class_voxelgi.md#class-voxelgi) node again.

**Note:** To prevent text-based scene files (`.tscn`) from growing too much and becoming slow to load and save, always save **VoxelGIData** to an external binary resource file (`.res`) instead of embedding it within the scene. This can be done by clicking the dropdown arrow next to the **VoxelGIData** resource, choosing **Edit**, clicking the floppy disk icon at the top of the Inspector then choosing **Save As...**.

## Tutorials

- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [float](class_float.md#class-float)   | bias                       | `1.5`   |
|---------------------------------------|----------------------------------------------------------------|---------|
| [float](class_float.md#class-float)   | dynamic_range     | `2.0`   |
| [float](class_float.md#class-float)   | energy                   | `1.0`   |
| [bool](class_bool.md#class-bool)      | interior               | `false` |
| [float](class_float.md#class-float)   | normal_bias         | `0.0`   |
| [float](class_float.md#class-float)   | propagation         | `0.5`   |
| [bool](class_bool.md#class-bool)      | use_two_bounces | `true`  |

## Methods

|                                                                      | allocate(to_cell_xform: [Transform3D](class_transform3d.md#class-transform3d), aabb: [AABB](class_aabb.md#class-aabb), octree_size: [Vector3](class_vector3.md#class-vector3), octree_cells: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), data_cells: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), distance_field: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), level_counts: [PackedInt32Array](class_packedint32array.md#class-packedint32array))   |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AABB](class_aabb.md#class-aabb)                                     | get_bounds()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)    | get_data_cells()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array) | get_level_counts()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)    | get_octree_cells()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Vector3](class_vector3.md#class-vector3)                            | get_octree_size()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Transform3D](class_transform3d.md#class-transform3d)                | get_to_cell_xform()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

## Property Descriptions

[float](class_float.md#class-float) **bias** = `1.5`

-  **set_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bias**()

The normal bias to use for indirect lighting and reflections. Higher values reduce self-reflections visible in non-rough materials, at the cost of more visible light leaking and flatter-looking indirect lighting. To prioritize hiding self-reflections over lighting quality, set bias to `0.0` and normal_bias to a value between `1.0` and `2.0`.

---

[float](class_float.md#class-float) **dynamic_range** = `2.0`

-  **set_dynamic_range**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_dynamic_range**()

The dynamic range to use (`1.0` represents a low dynamic range scene brightness). Higher values can be used to provide brighter indirect lighting, at the cost of more visible color banding in dark areas (both in indirect lighting and reflections). To avoid color banding, it's recommended to use the lowest value that does not result in visible light clipping.

---

[float](class_float.md#class-float) **energy** = `1.0`

-  **set_energy**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_energy**()

The energy of the indirect lighting and reflections produced by the [VoxelGI](class_voxelgi.md#class-voxelgi) node. Higher values result in brighter indirect lighting. If indirect lighting looks too flat, try decreasing propagation while increasing energy at the same time. See also use_two_bounces which influences the indirect lighting's effective brightness.

---

[bool](class_bool.md#class-bool) **interior** = `false`

-  **set_interior**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_interior**()

If `true`, [Environment](class_environment.md#class-environment) lighting is ignored by the [VoxelGI](class_voxelgi.md#class-voxelgi) node. If `false`, [Environment](class_environment.md#class-environment) lighting is taken into account by the [VoxelGI](class_voxelgi.md#class-voxelgi) node. [Environment](class_environment.md#class-environment) lighting updates in real-time, which means it can be changed without having to bake the [VoxelGI](class_voxelgi.md#class-voxelgi) node again.

---

[float](class_float.md#class-float) **normal_bias** = `0.0`

-  **set_normal_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_normal_bias**()

The normal bias to use for indirect lighting and reflections. Higher values reduce self-reflections visible in non-rough materials, at the cost of more visible light leaking and flatter-looking indirect lighting. See also bias. To prioritize hiding self-reflections over lighting quality, set bias to `0.0` and normal_bias to a value between `1.0` and `2.0`.

---

[float](class_float.md#class-float) **propagation** = `0.5`

-  **set_propagation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_propagation**()

The multiplier to use when light bounces off a surface. Higher values result in brighter indirect lighting. If indirect lighting looks too flat, try decreasing propagation while increasing energy at the same time. See also use_two_bounces which influences the indirect lighting's effective brightness.

---

[bool](class_bool.md#class-bool) **use_two_bounces** = `true`

-  **set_use_two_bounces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_two_bounces**()

If `true`, performs two bounces of indirect lighting instead of one. This makes indirect lighting look more natural and brighter at a small performance cost. The second bounce is also visible in reflections. If the scene appears too bright after enabling use_two_bounces, adjust propagation and energy.

---

## Method Descriptions

 **allocate**(to_cell_xform: [Transform3D](class_transform3d.md#class-transform3d), aabb: [AABB](class_aabb.md#class-aabb), octree_size: [Vector3](class_vector3.md#class-vector3), octree_cells: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), data_cells: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), distance_field: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), level_counts: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Initializes this **VoxelGIData** with the specified data. `octree_cells` must be a multiple of 32. `octree_cells` must be double the size of `data_cells`. The allocated data can be retrieved later using the various getter methods.

---

[AABB](class_aabb.md#class-aabb) **get_bounds**()

Returns the bounds of the baked voxel data as an [AABB](class_aabb.md#class-aabb), which should match [VoxelGI.size](class_voxelgi.md#class-voxelgi-property-size) after being baked (which only contains the size as a [Vector3](class_vector3.md#class-vector3)).

**Note:** If the size was modified without baking the VoxelGI data, then the value of get_bounds() and [VoxelGI.size](class_voxelgi.md#class-voxelgi-property-size) will not match.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_data_cells**()

Returns the baked cell data for this **VoxelGIData**.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_level_counts**()

Returns the baked level counts for this **VoxelGIData**.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **get_octree_cells**()

Returns the baked octree cell data for this **VoxelGIData**.

---

[Vector3](class_vector3.md#class-vector3) **get_octree_size**()

Returns the baked octree size for this **VoxelGIData**, which corresponds to the number of subdivisions per axis. This can be viewed in the editor by hovering the **Bake VoxelGI** button at the top of the 3D editor viewport when a [VoxelGI](class_voxelgi.md#class-voxelgi) node is selected and looking at the **Subdivisions** field in the tooltip.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_to_cell_xform**()

Returns the baked cell transform for this **VoxelGIData**.
