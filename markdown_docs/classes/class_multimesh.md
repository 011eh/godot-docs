# MultiMesh

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Provides high-performance drawing of a mesh multiple times using GPU instancing.

## Description

MultiMesh provides low-level mesh instancing. Drawing thousands of [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) nodes can be slow, since each object is submitted to the GPU then drawn individually.

MultiMesh is much faster as it can draw thousands of instances with a single draw call, resulting in less API overhead.

As a drawback, if the instances are too far away from each other, performance may be reduced as every single instance will always render (they are spatially indexed as one, for the whole object).

Since instances may have any behavior, the AABB used for visibility must be provided by the user.

**Note:** A MultiMesh is a single object, therefore the same maximum lights per object restriction applies. This means, that once the maximum lights are consumed by one or more instances, the rest of the MultiMesh instances will **not** receive any lighting.

**Note:** Blend Shapes will be ignored if used in a MultiMesh.

## Tutorials

- [Using MultiMeshInstance](../tutorials/3d/using_multi_mesh_instance.md)
- [Optimization using MultiMeshes](../tutorials/performance/using_multimesh.md)
- [Animating thousands of fish with MultiMeshInstance](../tutorials/performance/vertex_animation/animating_thousands_of_fish.md)

## Properties

| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)   | buffer                                               | `PackedFloat32Array()`   |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------|
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)         | color_array                                     |                          |
| [AABB](class_aabb.md#class-aabb)                                             | custom_aabb                                     | `AABB(0, 0, 0, 0, 0, 0)` |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)         | custom_data_array                         |                          |
| [int](class_int.md#class-int)                                                | instance_count                               | `0`                      |
| [Mesh](class_mesh.md#class-mesh)                                             | mesh                                                   |                          |
| PhysicsInterpolationQuality   | physics_interpolation_quality | `0`                      |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)   | transform_2d_array                       |                          |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)   | transform_array                             |                          |
| TransformFormat                           | transform_format                           | `0`                      |
| [bool](class_bool.md#class-bool)                                             | use_colors                                       | `false`                  |
| [bool](class_bool.md#class-bool)                                             | use_custom_data                             | `false`                  |
| [int](class_int.md#class-int)                                                | visible_instance_count               | `-1`                     |

## Methods

| [AABB](class_aabb.md#class-aabb)                      | get_aabb()                                                                                                                                                                                                               |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Color](class_color.md#class-color)                   | get_instance_color(instance: [int](class_int.md#class-int))                                                                                                                                                    |
| [Color](class_color.md#class-color)                   | get_instance_custom_data(instance: [int](class_int.md#class-int))                                                                                                                                        |
| [Transform3D](class_transform3d.md#class-transform3d) | get_instance_transform(instance: [int](class_int.md#class-int))                                                                                                                                            |
| [Transform2D](class_transform2d.md#class-transform2d) | get_instance_transform_2d(instance: [int](class_int.md#class-int))                                                                                                                                      |
|                                                       | reset_instance_physics_interpolation(instance: [int](class_int.md#class-int))                                                                                                                |
|                                                       | reset_instances_physics_interpolation()                                                                                                                                                     |
|                                                       | set_buffer_interpolated(buffer_curr: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), buffer_prev: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |
|                                                       | set_instance_color(instance: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                        |
|                                                       | set_instance_custom_data(instance: [int](class_int.md#class-int), custom_data: [Color](class_color.md#class-color))                                                                                      |
|                                                       | set_instance_transform(instance: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                          |
|                                                       | set_instance_transform_2d(instance: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                    |

---

## Enumerations

enum **TransformFormat**:

TransformFormat **TRANSFORM_2D** = `0`

Use this when using 2D transforms.

TransformFormat **TRANSFORM_3D** = `1`

Use this when using 3D transforms.

---

enum **PhysicsInterpolationQuality**:

PhysicsInterpolationQuality **INTERP_QUALITY_FAST** = `0`

Always interpolate using Basis lerping, which can produce warping artifacts in some situations.

PhysicsInterpolationQuality **INTERP_QUALITY_HIGH** = `1`

Attempt to interpolate using Basis slerping (spherical linear interpolation) where possible, otherwise fall back to lerping.

---

## Property Descriptions

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **buffer** = `PackedFloat32Array()`

-  **set_buffer**(value: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))
- [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_buffer**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) for more details.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **color_array**

**Deprecated:** Accessing this property is very slow. Use set_instance_color() and get_instance_color() instead.

Array containing each [Color](class_color.md#class-color) used by all instances of this mesh.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---

[AABB](class_aabb.md#class-aabb) **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)`

-  **set_custom_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_custom_aabb**()

Custom AABB for this MultiMesh resource. Setting this manually prevents costly runtime AABB recalculations.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **custom_data_array**

**Deprecated:** Accessing this property is very slow. Use set_instance_custom_data() and get_instance_custom_data() instead.

Array containing each custom data value used by all instances of this mesh, as a [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---

[int](class_int.md#class-int) **instance_count** = `0`

-  **set_instance_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_instance_count**()

Number of instances that will get drawn. This clears and (re)sizes the buffers. Setting data format or flags afterwards will have no effect.

By default, all instances are drawn but you can limit this with visible_instance_count.

---

[Mesh](class_mesh.md#class-mesh) **mesh**

-  **set_mesh**(value: [Mesh](class_mesh.md#class-mesh))
- [Mesh](class_mesh.md#class-mesh) **get_mesh**()

[Mesh](class_mesh.md#class-mesh) resource to be instanced.

The looks of the individual instances can be modified using set_instance_color() and set_instance_custom_data().

---

PhysicsInterpolationQuality **physics_interpolation_quality** = `0`

-  **set_physics_interpolation_quality**(value: PhysicsInterpolationQuality)
- PhysicsInterpolationQuality **get_physics_interpolation_quality**()

Choose whether to use an interpolation method that favors speed or quality.

When using low physics tick rates (typically below 20) or high rates of object rotation, you may get better results from the high quality setting.

**Note:** Fast quality does not equate to low quality. Except in the special cases mentioned above, the quality should be comparable to high quality.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **transform_2d_array**

**Deprecated:** Accessing this property is very slow. Use set_instance_transform_2d() and get_instance_transform_2d() instead.

Array containing each [Transform2D](class_transform2d.md#class-transform2d) value used by all instances of this mesh, as a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array). Each transform is divided into 3 [Vector2](class_vector2.md#class-vector2) values corresponding to the transforms' `x`, `y`, and `origin`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **transform_array**

**Deprecated:** Accessing this property is very slow. Use set_instance_transform() and get_instance_transform() instead.

Array containing each [Transform3D](class_transform3d.md#class-transform3d) value used by all instances of this mesh, as a [PackedVector3Array](class_packedvector3array.md#class-packedvector3array). Each transform is divided into 4 [Vector3](class_vector3.md#class-vector3) values corresponding to the transforms' `x`, `y`, `z`, and `origin`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) for more details.

---

TransformFormat **transform_format** = `0`

-  **set_transform_format**(value: TransformFormat)
- TransformFormat **get_transform_format**()

Format of transform used to transform mesh, either 2D or 3D.

---

[bool](class_bool.md#class-bool) **use_colors** = `false`

-  **set_use_colors**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_colors**()

If `true`, the **MultiMesh** will use color data (see set_instance_color()). Can only be set when instance_count is `0` or less. This means that you need to call this method before setting the instance count, or temporarily reset it to `0`.

---

[bool](class_bool.md#class-bool) **use_custom_data** = `false`

-  **set_use_custom_data**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_custom_data**()

If `true`, the **MultiMesh** will use custom data (see set_instance_custom_data()). Can only be set when instance_count is `0` or less. This means that you need to call this method before setting the instance count, or temporarily reset it to `0`.

---

[int](class_int.md#class-int) **visible_instance_count** = `-1`

-  **set_visible_instance_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_visible_instance_count**()

Limits the number of instances drawn, -1 draws all instances. Changing this does not change the sizes of the buffers.

---

## Method Descriptions

[AABB](class_aabb.md#class-aabb) **get_aabb**()

Returns the visibility axis-aligned bounding box in local space.

---

[Color](class_color.md#class-color) **get_instance_color**(instance: [int](class_int.md#class-int))

Gets a specific instance's color multiplier.

---

[Color](class_color.md#class-color) **get_instance_custom_data**(instance: [int](class_int.md#class-int))

Returns the custom data that has been set for a specific instance.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_instance_transform**(instance: [int](class_int.md#class-int))

Returns the [Transform3D](class_transform3d.md#class-transform3d) of a specific instance.

---

[Transform2D](class_transform2d.md#class-transform2d) **get_instance_transform_2d**(instance: [int](class_int.md#class-int))

Returns the [Transform2D](class_transform2d.md#class-transform2d) of a specific instance.

---

 **reset_instance_physics_interpolation**(instance: [int](class_int.md#class-int))

When using *physics interpolation*, this function allows you to prevent interpolation on an instance in the current physics tick.

This allows you to move instances instantaneously, and should usually be used when initially placing an instance such as a bullet to prevent graphical glitches.

---

 **reset_instances_physics_interpolation**()

When using *physics interpolation*, this function allows you to prevent interpolation for all instances in the current physics tick.

This allows you to move all instances instantaneously, and should usually be used when initially placing instances to prevent graphical glitches.

---

 **set_buffer_interpolated**(buffer_curr: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), buffer_prev: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

An alternative to setting the buffer property, which can be used with *physics interpolation*. This method takes two arrays, and can set the data for the current and previous tick in one go. The renderer will automatically interpolate the data at each frame.

This is useful for situations where the order of instances may change from physics tick to tick, such as particle systems.

When the order of instances is coherent, the simpler alternative of setting buffer can still be used with interpolation.

---

 **set_instance_color**(instance: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the color of a specific instance by *multiplying* the mesh's existing vertex colors. This allows for different color tinting per instance.

**Note:** Each component is stored in 32 bits in the Forward+ and Mobile rendering methods, but is packed into 16 bits in the Compatibility rendering method.

For the color to take effect, ensure that use_colors is `true` on the **MultiMesh** and [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class-basematerial3d-property-vertex-color-use-as-albedo) is `true` on the material. If you intend to set an absolute color instead of tinting, make sure the material's albedo color is set to pure white (`Color(1, 1, 1)`).

---

 **set_instance_custom_data**(instance: [int](class_int.md#class-int), custom_data: [Color](class_color.md#class-color))

Sets custom data for a specific instance. `custom_data` is a [Color](class_color.md#class-color) type only to contain 4 floating-point numbers.

**Note:** Each number is stored in 32 bits in the Forward+ and Mobile rendering methods, but is packed into 16 bits in the Compatibility rendering method.

For the custom data to be used, ensure that use_custom_data is `true`.

This custom instance data has to be manually accessed in your custom shader using `INSTANCE_CUSTOM`.

---

 **set_instance_transform**(instance: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))

Sets the [Transform3D](class_transform3d.md#class-transform3d) for a specific instance.

---

 **set_instance_transform_2d**(instance: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the [Transform2D](class_transform2d.md#class-transform2d) for a specific instance.
