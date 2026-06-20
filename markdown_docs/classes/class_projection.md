# Projection

A 4×4 matrix for 3D projective transformations.

## Description

A 4×4 matrix used for 3D projective transformations. It can represent transformations such as translation, rotation, scaling, shearing, and perspective division. It consists of four [Vector4](class_vector4.md#class-vector4) columns.

For purely linear transformations (translation, rotation, and scale), it is recommended to use [Transform3D](class_transform3d.md#class-transform3d), as it is more performant and requires less memory.

Used internally as [Camera3D](class_camera3d.md#class-camera3d)'s projection matrix.

**Note:** In a boolean context, a projection will evaluate to `false` if it's equal to IDENTITY. Otherwise, a projection will always evaluate to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Properties

| [Vector4](class_vector4.md#class-vector4)   | w   | `Vector4(0, 0, 0, 1)`   |
|---------------------------------------------|-------------------------------------|-------------------------|
| [Vector4](class_vector4.md#class-vector4)   | x   | `Vector4(1, 0, 0, 0)`   |
| [Vector4](class_vector4.md#class-vector4)   | y   | `Vector4(0, 1, 0, 0)`   |
| [Vector4](class_vector4.md#class-vector4)   | z   | `Vector4(0, 0, 1, 0)`   |

## Constructors

| Projection   | Projection()                                                                                                                                                                                                           |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Projection   | Projection(from: Projection)                                                                                                                                                                      |
| Projection   | Projection(from: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                |
| Projection   | Projection(x_axis: [Vector4](class_vector4.md#class-vector4), y_axis: [Vector4](class_vector4.md#class-vector4), z_axis: [Vector4](class_vector4.md#class-vector4), w_axis: [Vector4](class_vector4.md#class-vector4)) |

## Methods

| Projection           | create_depth_correction(flip_y: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Projection           | create_fit_aabb(aabb: [AABB](class_aabb.md#class-aabb))                                                                                                                                                                                                                                                                                                                                                      |
| Projection           | create_for_hmd(eye: [int](class_int.md#class-int), aspect: [float](class_float.md#class-float), intraocular_dist: [float](class_float.md#class-float), display_width: [float](class_float.md#class-float), display_to_lens: [float](class_float.md#class-float), oversample: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))    |
| Projection           | create_frustum(left: [float](class_float.md#class-float), right: [float](class_float.md#class-float), bottom: [float](class_float.md#class-float), top: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))                                                                                                                         |
| Projection           | create_frustum_aspect(size: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float), offset: [Vector2](class_vector2.md#class-vector2), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float), flip_fov: [bool](class_bool.md#class-bool) = false)                                                                                          |
| Projection           | create_light_atlas_rect(rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                                                                                                                                   |
| Projection           | create_orthogonal(left: [float](class_float.md#class-float), right: [float](class_float.md#class-float), bottom: [float](class_float.md#class-float), top: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))                                                                                                                   |
| Projection           | create_orthogonal_aspect(size: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float), flip_fov: [bool](class_bool.md#class-bool) = false)                                                                                                                                       |
| Projection           | create_perspective(fovy: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float), flip_fov: [bool](class_bool.md#class-bool) = false)                                                                                                                                                   |
| Projection           | create_perspective_hmd(fovy: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float), flip_fov: [bool](class_bool.md#class-bool), eye: [int](class_int.md#class-int), intraocular_dist: [float](class_float.md#class-float), convergence_dist: [float](class_float.md#class-float)) |
| [float](class_float.md#class-float)       | determinant()                                                                                                                                                                                                                                                                                                                                                                                                    |
| Projection           | flipped_y()                                                                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)       | get_aspect()                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Vector2](class_vector2.md#class-vector2) | get_far_plane_half_extents()                                                                                                                                                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)       | get_fov()                                                                                                                                                                                                                                                                                                                                                                                                            |
| [float](class_float.md#class-float)       | get_fovy(fovx: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                    |
| [float](class_float.md#class-float)       | get_lod_multiplier()                                                                                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)             | get_pixels_per_meter(for_pixel_width: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                    |
| [Plane](class_plane.md#class-plane)       | get_projection_plane(plane: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                              |
| [Vector2](class_vector2.md#class-vector2) | get_viewport_half_extents()                                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)       | get_z_far()                                                                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)       | get_z_near()                                                                                                                                                                                                                                                                                                                                                                                                      |
| Projection           | inverse()                                                                                                                                                                                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)          | is_orthogonal()                                                                                                                                                                                                                                                                                                                                                                                                |
| Projection           | jitter_offseted(offset: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                                                           |
| Projection           | perspective_znear_adjusted(new_znear: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                        |

## Operators

| [bool](class_bool.md#class-bool)          | operator !=(right: Projection)        |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Projection           | operator \*(right: Projection)        |
| [Vector4](class_vector4.md#class-vector4) | operator \*(right: [Vector4](class_vector4.md#class-vector4)) |
| [bool](class_bool.md#class-bool)          | operator ==(right: Projection)         |
| [Vector4](class_vector4.md#class-vector4) | operator [](index: [int](class_int.md#class-int))                 |

---

## Enumerations

enum **Planes**:

Planes **PLANE_NEAR** = `0`

The index value of the projection's near clipping plane.

Planes **PLANE_FAR** = `1`

The index value of the projection's far clipping plane.

Planes **PLANE_LEFT** = `2`

The index value of the projection's left clipping plane.

Planes **PLANE_TOP** = `3`

The index value of the projection's top clipping plane.

Planes **PLANE_RIGHT** = `4`

The index value of the projection's right clipping plane.

Planes **PLANE_BOTTOM** = `5`

The index value of the projection bottom clipping plane.

---

## Constants

**IDENTITY** = `Projection(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)`

A **Projection** with no transformation defined. When applied to other data structures, no transformation is performed.

**ZERO** = `Projection(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)`

A **Projection** with all values initialized to 0. When applied to other data structures, they will be zeroed.

---

## Property Descriptions

[Vector4](class_vector4.md#class-vector4) **w** = `Vector4(0, 0, 0, 1)`

The projection matrix's W vector (column 3). Equivalent to array index `3`.

---

[Vector4](class_vector4.md#class-vector4) **x** = `Vector4(1, 0, 0, 0)`

The projection matrix's X vector (column 0). Equivalent to array index `0`.

---

[Vector4](class_vector4.md#class-vector4) **y** = `Vector4(0, 1, 0, 0)`

The projection matrix's Y vector (column 1). Equivalent to array index `1`.

---

[Vector4](class_vector4.md#class-vector4) **z** = `Vector4(0, 0, 1, 0)`

The projection matrix's Z vector (column 2). Equivalent to array index `2`.

---

## Constructor Descriptions

Projection **Projection**()

Constructs a default-initialized **Projection** identical to IDENTITY.

**Note:** In C#, this constructs a **Projection** identical to ZERO.

---

Projection **Projection**(from: Projection)

Constructs a **Projection** as a copy of the given **Projection**.

---

Projection **Projection**(from: [Transform3D](class_transform3d.md#class-transform3d))

Constructs a Projection as a copy of the given [Transform3D](class_transform3d.md#class-transform3d).

---

Projection **Projection**(x_axis: [Vector4](class_vector4.md#class-vector4), y_axis: [Vector4](class_vector4.md#class-vector4), z_axis: [Vector4](class_vector4.md#class-vector4), w_axis: [Vector4](class_vector4.md#class-vector4))

Constructs a Projection from four [Vector4](class_vector4.md#class-vector4) values (matrix columns).

---

## Method Descriptions

Projection **create_depth_correction**(flip_y: [bool](class_bool.md#class-bool))

Creates a new **Projection** that projects positions from a depth range of `-1` to `1` to one that ranges from `0` to `1`, and flips the projected positions vertically, according to `flip_y`.

---

Projection **create_fit_aabb**(aabb: [AABB](class_aabb.md#class-aabb))

Creates a new **Projection** that scales a given projection to fit around a given [AABB](class_aabb.md#class-aabb) in projection space.

---

Projection **create_for_hmd**(eye: [int](class_int.md#class-int), aspect: [float](class_float.md#class-float), intraocular_dist: [float](class_float.md#class-float), display_width: [float](class_float.md#class-float), display_to_lens: [float](class_float.md#class-float), oversample: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Creates a new **Projection** for projecting positions onto a head-mounted display with the given X:Y aspect ratio, distance between eyes, display width, distance to lens, oversampling factor, and depth clipping planes.

`eye` creates the projection for the left eye when set to 1, or the right eye when set to 2.

---

Projection **create_frustum**(left: [float](class_float.md#class-float), right: [float](class_float.md#class-float), bottom: [float](class_float.md#class-float), top: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Creates a new **Projection** that projects positions in a frustum with the given clipping planes.

---

Projection **create_frustum_aspect**(size: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float), offset: [Vector2](class_vector2.md#class-vector2), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float), flip_fov: [bool](class_bool.md#class-bool) = false)

Creates a new **Projection** that projects positions in a frustum with the given size, X:Y aspect ratio, offset, and clipping planes.

`flip_fov` determines whether the projection's field of view is flipped over its diagonal.

---

Projection **create_light_atlas_rect**(rect: [Rect2](class_rect2.md#class-rect2))

Creates a new **Projection** that projects positions into the given [Rect2](class_rect2.md#class-rect2).

---

Projection **create_orthogonal**(left: [float](class_float.md#class-float), right: [float](class_float.md#class-float), bottom: [float](class_float.md#class-float), top: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Creates a new **Projection** that projects positions using an orthogonal projection with the given clipping planes.

---

Projection **create_orthogonal_aspect**(size: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float), flip_fov: [bool](class_bool.md#class-bool) = false)

Creates a new **Projection** that projects positions using an orthogonal projection with the given size, X:Y aspect ratio, and clipping planes.

`flip_fov` determines whether the projection's field of view is flipped over its diagonal.

---

Projection **create_perspective**(fovy: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float), flip_fov: [bool](class_bool.md#class-bool) = false)

Creates a new **Projection** that projects positions using a perspective projection with the given Y-axis field of view (in degrees), X:Y aspect ratio, and clipping planes.

`flip_fov` determines whether the projection's field of view is flipped over its diagonal.

---

Projection **create_perspective_hmd**(fovy: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float), flip_fov: [bool](class_bool.md#class-bool), eye: [int](class_int.md#class-int), intraocular_dist: [float](class_float.md#class-float), convergence_dist: [float](class_float.md#class-float))

Creates a new **Projection** that projects positions using a perspective projection with the given Y-axis field of view (in degrees), X:Y aspect ratio, and clipping distances. The projection is adjusted for a head-mounted display with the given distance between eyes and distance to a point that can be focused on.

`eye` creates the projection for the left eye when set to 1, or the right eye when set to 2.

`flip_fov` determines whether the projection's field of view is flipped over its diagonal.

---

[float](class_float.md#class-float) **determinant**()

Returns a scalar value that is the signed factor by which areas are scaled by this matrix. If the sign is negative, the matrix flips the orientation of the area.

The determinant can be used to calculate the invertibility of a matrix or solve linear systems of equations involving the matrix, among other applications.

---

Projection **flipped_y**()

Returns a copy of this **Projection** with the signs of the values of the Y column flipped.

---

[float](class_float.md#class-float) **get_aspect**()

Returns the X:Y aspect ratio of this **Projection**'s viewport.

---

[Vector2](class_vector2.md#class-vector2) **get_far_plane_half_extents**()

Returns the dimensions of the far clipping plane of the projection, divided by two.

---

[float](class_float.md#class-float) **get_fov**()

Returns the horizontal field of view of the projection (in degrees).

---

[float](class_float.md#class-float) **get_fovy**(fovx: [float](class_float.md#class-float), aspect: [float](class_float.md#class-float))

Returns the vertical field of view of the projection (in degrees) associated with the given horizontal field of view (in degrees) and aspect ratio.

**Note:** Unlike most methods of **Projection**, `aspect` is expected to be 1 divided by the X:Y aspect ratio.

---

[float](class_float.md#class-float) **get_lod_multiplier**()

Returns the factor by which the visible level of detail is scaled by this **Projection**.

---

[int](class_int.md#class-int) **get_pixels_per_meter**(for_pixel_width: [int](class_int.md#class-int))

Returns `for_pixel_width` divided by the viewport's width measured in meters on the near plane, after this **Projection** is applied.

---

[Plane](class_plane.md#class-plane) **get_projection_plane**(plane: [int](class_int.md#class-int))

Returns the clipping plane of this **Projection** whose index is given by `plane`.

`plane` should be equal to one of PLANE_NEAR, PLANE_FAR, PLANE_LEFT, PLANE_TOP, PLANE_RIGHT, or PLANE_BOTTOM.

---

[Vector2](class_vector2.md#class-vector2) **get_viewport_half_extents**()

Returns the dimensions of the viewport plane that this **Projection** projects positions onto, divided by two.

---

[float](class_float.md#class-float) **get_z_far**()

Returns the distance for this **Projection** beyond which positions are clipped.

---

[float](class_float.md#class-float) **get_z_near**()

Returns the distance for this **Projection** before which positions are clipped.

---

Projection **inverse**()

Returns a **Projection** that performs the inverse of this **Projection**'s projective transformation.

---

[bool](class_bool.md#class-bool) **is_orthogonal**()

Returns `true` if this **Projection** performs an orthogonal projection.

---

Projection **jitter_offseted**(offset: [Vector2](class_vector2.md#class-vector2))

Returns a **Projection** with the X and Y values from the given [Vector2](class_vector2.md#class-vector2) added to the first and second values of the final column respectively.

---

Projection **perspective_znear_adjusted**(new_znear: [float](class_float.md#class-float))

Returns a **Projection** with the near clipping distance adjusted to be `new_znear`.

**Note:** The original **Projection** must be a perspective projection.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: Projection)

Returns `true` if the projections are not equal.

**Note:** Due to floating-point precision errors, this may return `true`, even if the projections are virtually equal. An `is_equal_approx` method may be added in a future version of Godot.

---

Projection **operator \***(right: Projection)

Returns a **Projection** that applies the combined transformations of this **Projection** and `right`.

---

[Vector4](class_vector4.md#class-vector4) **operator \***(right: [Vector4](class_vector4.md#class-vector4))

Projects (multiplies) the given [Vector4](class_vector4.md#class-vector4) by this **Projection** matrix.

---

[bool](class_bool.md#class-bool) **operator ==**(right: Projection)

Returns `true` if the projections are equal.

**Note:** Due to floating-point precision errors, this may return `false`, even if the projections are virtually equal. An `is_equal_approx` method may be added in a future version of Godot.

---

[Vector4](class_vector4.md#class-vector4) **operator []**(index: [int](class_int.md#class-int))

Returns the column of the **Projection** with the given index.

Indices are in the following order: x, y, z, w.
