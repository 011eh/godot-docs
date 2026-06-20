# Transform3D

A 3×4 matrix representing a 3D transformation.

## Description

The **Transform3D** built-in [Variant](class_variant.md#class-variant) type is a 3×4 matrix representing a transformation in 3D space. It contains a [Basis](class_basis.md#class-basis), which on its own can represent rotation, scale, and shear. Additionally, combined with its own origin, the transform can also represent a translation.

For a general introduction, see the [Matrices and transforms](../tutorials/math/matrices_and_transforms.md) tutorial.

**Note:** Godot uses a [right-handed coordinate system](https://en.wikipedia.org/wiki/Right-hand_rule), which is a common standard. For directions, the convention for built-in types like [Camera3D](class_camera3d.md#class-camera3d) is for -Z to point forward (+X is right, +Y is up, and +Z is back). Other objects may use different direction conventions. For more information, see the [3D asset direction conventions](../tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html#d-asset-direction-conventions) tutorial.

**Note:** In a boolean context, a Transform3D will evaluate to `false` if it's equal to IDENTITY. Otherwise, a Transform3D will always evaluate to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Tutorials

- [Math documentation index](../tutorials/math/index.md)
- [Matrices and transforms](../tutorials/math/matrices_and_transforms.md)
- [Using 3D transforms](../tutorials/3d/using_transforms.md)
- [Matrix Transform Demo](https://godotengine.org/asset-library/asset/2787)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [2.5D Game Demo](https://godotengine.org/asset-library/asset/2783)

## Properties

| [Basis](class_basis.md#class-basis)       | basis   | `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)`   |
|-------------------------------------------|----------------------------------------------|--------------------------------------|
| [Vector3](class_vector3.md#class-vector3) | origin | `Vector3(0, 0, 0)`                   |

## Constructors

| Transform3D   | Transform3D()                                                                                                                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transform3D   | Transform3D(from: Transform3D)                                                                                                                                                                    |
| Transform3D   | Transform3D(basis: [Basis](class_basis.md#class-basis), origin: [Vector3](class_vector3.md#class-vector3))                                                                                                              |
| Transform3D   | Transform3D(from: [Projection](class_projection.md#class-projection))                                                                                                                                                   |
| Transform3D   | Transform3D(x_axis: [Vector3](class_vector3.md#class-vector3), y_axis: [Vector3](class_vector3.md#class-vector3), z_axis: [Vector3](class_vector3.md#class-vector3), origin: [Vector3](class_vector3.md#class-vector3)) |

## Methods

| Transform3D   | affine_inverse()                                                                                                                                                                       |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transform3D   | interpolate_with(xform: Transform3D, weight: [float](class_float.md#class-float))                                                                              |
| Transform3D   | inverse()                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)    | is_equal_approx(xform: Transform3D)                                                                                                                             |
| [bool](class_bool.md#class-bool)    | is_finite()                                                                                                                                                                                 |
| Transform3D   | looking_at(target: [Vector3](class_vector3.md#class-vector3), up: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class-bool) = false) |
| Transform3D   | orthonormalized()                                                                                                                                                                     |
| Transform3D   | rotated(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))                                                                                          |
| Transform3D   | rotated_local(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))                                                                              |
| Transform3D   | scaled(scale: [Vector3](class_vector3.md#class-vector3))                                                                                                                                       |
| Transform3D   | scaled_local(scale: [Vector3](class_vector3.md#class-vector3))                                                                                                                           |
| Transform3D   | translated(offset: [Vector3](class_vector3.md#class-vector3))                                                                                                                              |
| Transform3D   | translated_local(offset: [Vector3](class_vector3.md#class-vector3))                                                                                                                  |

## Operators

| [bool](class_bool.md#class-bool)                                           | operator !=(right: Transform3D)                                                 |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AABB](class_aabb.md#class-aabb)                                           | operator \*(right: [AABB](class_aabb.md#class-aabb))                                                         |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | operator \*(right: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)) |
| [Plane](class_plane.md#class-plane)                                        | operator \*(right: [Plane](class_plane.md#class-plane))                                                     |
| Transform3D                                          | operator \*(right: Transform3D)                                                 |
| [Vector3](class_vector3.md#class-vector3)                                  | operator \*(right: [Vector3](class_vector3.md#class-vector3))                                             |
| Transform3D                                          | operator \*(right: [float](class_float.md#class-float))                                                     |
| Transform3D                                          | operator \*(right: [int](class_int.md#class-int))                                                             |
| Transform3D                                          | operator /(right: [float](class_float.md#class-float))                                                      |
| Transform3D                                          | operator /(right: [int](class_int.md#class-int))                                                              |
| [bool](class_bool.md#class-bool)                                           | operator ==(right: Transform3D)                                                  |

---

## Constants

**IDENTITY** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

The identity **Transform3D**. This is a transform with no translation, no rotation, and a scale of [Vector3.ONE](class_vector3.md#class-vector3-constant-one). Its basis is equal to [Basis.IDENTITY](class_basis.md#class-basis-constant-identity). This also means that:

- Its [Basis.x](class_basis.md#class-basis-property-x) points right ([Vector3.RIGHT](class_vector3.md#class-vector3-constant-right));
- Its [Basis.y](class_basis.md#class-basis-property-y) points up ([Vector3.UP](class_vector3.md#class-vector3-constant-up));
- Its [Basis.z](class_basis.md#class-basis-property-z) points back ([Vector3.BACK](class_vector3.md#class-vector3-constant-back)).

```gdscript
var transform = Transform3D.IDENTITY
var basis = transform.basis
print("| X | Y | Z | Origin")
print("| %.f | %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x, transform.origin.x])
print("| %.f | %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y, transform.origin.y])
print("| %.f | %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z, transform.origin.z])
# Prints:
# | X | Y | Z | Origin
# | 1 | 0 | 0 | 0
# | 0 | 1 | 0 | 0
# | 0 | 0 | 1 | 0
```

If a [Vector3](class_vector3.md#class-vector3), an [AABB](class_aabb.md#class-aabb), a [Plane](class_plane.md#class-plane), a [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), or another **Transform3D** is transformed (multiplied) by this constant, no transformation occurs.

**Note:** In GDScript, this constant is equivalent to creating a Transform3D without any arguments. It can be used to make your code clearer, and for consistency with C#.

**FLIP_X** = `Transform3D(-1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

**Transform3D** with mirroring applied perpendicular to the YZ plane. Its basis is equal to [Basis.FLIP_X](class_basis.md#class-basis-constant-flip-x).

**FLIP_Y** = `Transform3D(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0)`

**Transform3D** with mirroring applied perpendicular to the XZ plane. Its basis is equal to [Basis.FLIP_Y](class_basis.md#class-basis-constant-flip-y).

**FLIP_Z** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0)`

**Transform3D** with mirroring applied perpendicular to the XY plane. Its basis is equal to [Basis.FLIP_Z](class_basis.md#class-basis-constant-flip-z).

---

## Property Descriptions

[Basis](class_basis.md#class-basis) **basis** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)`

The [Basis](class_basis.md#class-basis) of this transform. It is composed by 3 axes ([Basis.x](class_basis.md#class-basis-property-x), [Basis.y](class_basis.md#class-basis-property-y), and [Basis.z](class_basis.md#class-basis-property-z)). Together, these represent the transform's rotation, scale, and shear.

---

[Vector3](class_vector3.md#class-vector3) **origin** = `Vector3(0, 0, 0)`

The translation offset of this transform. In 3D space, this can be seen as the position.

---

## Constructor Descriptions

Transform3D **Transform3D**()

Constructs a **Transform3D** identical to IDENTITY.

**Note:** In C#, this constructs a **Transform3D** with its origin and the components of its basis set to [Vector3.ZERO](class_vector3.md#class-vector3-constant-zero).

---

Transform3D **Transform3D**(from: Transform3D)

Constructs a **Transform3D** as a copy of the given **Transform3D**.

---

Transform3D **Transform3D**(basis: [Basis](class_basis.md#class-basis), origin: [Vector3](class_vector3.md#class-vector3))

Constructs a **Transform3D** from a [Basis](class_basis.md#class-basis) and [Vector3](class_vector3.md#class-vector3).

---

Transform3D **Transform3D**(from: [Projection](class_projection.md#class-projection))

Constructs a **Transform3D** from a [Projection](class_projection.md#class-projection). Because **Transform3D** is a 3×4 matrix and [Projection](class_projection.md#class-projection) is a 4×4 matrix, this operation trims the last row of the projection matrix (`from.x.w`, `from.y.w`, `from.z.w`, and `from.w.w` are not included in the new transform).

---

Transform3D **Transform3D**(x_axis: [Vector3](class_vector3.md#class-vector3), y_axis: [Vector3](class_vector3.md#class-vector3), z_axis: [Vector3](class_vector3.md#class-vector3), origin: [Vector3](class_vector3.md#class-vector3))

Constructs a **Transform3D** from four [Vector3](class_vector3.md#class-vector3) values (also called matrix columns).

The first three arguments are the basis's axes ([Basis.x](class_basis.md#class-basis-property-x), [Basis.y](class_basis.md#class-basis-property-y), and [Basis.z](class_basis.md#class-basis-property-z)).

---

## Method Descriptions

Transform3D **affine_inverse**()

Returns the inverted version of this transform. Unlike inverse(), this method works with almost any basis, including non-uniform ones, but is slower. See also [Basis.inverse()](class_basis.md#class-basis-method-inverse).

**Note:** For this method to return correctly, the transform's basis needs to have a determinant that is not exactly `0.0` (see [Basis.determinant()](class_basis.md#class-basis-method-determinant)).

---

Transform3D **interpolate_with**(xform: Transform3D, weight: [float](class_float.md#class-float))

Returns the result of the linear interpolation between this transform and `xform` by the given `weight`.

The `weight` should be between `0.0` and `1.0` (inclusive). Values outside this range are allowed and can be used to perform *extrapolation* instead.

---

Transform3D **inverse**()

Returns the [inverted version of this transform](https://en.wikipedia.org/wiki/Invertible_matrix). See also [Basis.inverse()](class_basis.md#class-basis-method-inverse).

**Note:** For this method to return correctly, the transform's basis needs to be *orthonormal* (see orthonormalized()). That means the basis should only represent a rotation. If it does not, use affine_inverse() instead.

---

[bool](class_bool.md#class-bool) **is_equal_approx**(xform: Transform3D)

Returns `true` if this transform and `xform` are approximately equal, by running [@GlobalScope.is_equal_approx()](class_@globalscope.md#class-globalscope-method-is-equal-approx) on each component.

---

[bool](class_bool.md#class-bool) **is_finite**()

Returns `true` if this transform is finite, by calling [@GlobalScope.is_finite()](class_@globalscope.md#class-globalscope-method-is-finite) on each component.

---

Transform3D **looking_at**(target: [Vector3](class_vector3.md#class-vector3), up: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class-bool) = false)

Returns a copy of this transform rotated so that the forward axis (-Z) points towards the `target` position.

The up axis (+Y) points as close to the `up` vector as possible while staying perpendicular to the forward axis. The resulting transform is orthonormalized. The existing rotation, scale, and skew information from the original transform is discarded. The `target` and `up` vectors cannot be zero, cannot be parallel to each other, and are defined in global/parent space.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward the `target` position. By default, the -Z axis (camera forward) is treated as forward (implies +X is right).

---

Transform3D **orthonormalized**()

Returns a copy of this transform with its basis orthonormalized. An orthonormal basis is both *orthogonal* (the axes are perpendicular to each other) and *normalized* (the axes have a length of `1.0`), which also means it can only represent a rotation. See also [Basis.orthonormalized()](class_basis.md#class-basis-method-orthonormalized).

---

Transform3D **rotated**(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))

Returns a copy of this transform rotated around the given `axis` by the given `angle` (in radians).

The `axis` must be a normalized vector (see [Vector3.normalized()](class_vector3.md#class-vector3-method-normalized)). If `angle` is positive, the basis is rotated counter-clockwise around the axis.

This method is an optimized version of multiplying the given transform `X` with a corresponding rotation transform `R` from the left, i.e., `R * X`.

This can be seen as transforming with respect to the global/parent frame.

---

Transform3D **rotated_local**(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))

Returns a copy of this transform rotated around the given `axis` by the given `angle` (in radians).

The `axis` must be a normalized vector in the transform's local coordinate system. For example, to rotate around the local X-axis, use [Vector3.RIGHT](class_vector3.md#class-vector3-constant-right).

This method is an optimized version of multiplying the given transform `X` with a corresponding rotation transform `R` from the right, i.e., `X * R`.

This can be seen as transforming with respect to the local frame.

---

Transform3D **scaled**(scale: [Vector3](class_vector3.md#class-vector3))

Returns a copy of this transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform `X` with a corresponding scaling transform `S` from the left, i.e., `S * X`.

This can be seen as transforming with respect to the global/parent frame.

---

Transform3D **scaled_local**(scale: [Vector3](class_vector3.md#class-vector3))

Returns a copy of this transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform `X` with a corresponding scaling transform `S` from the right, i.e., `X * S`.

This can be seen as transforming with respect to the local frame.

---

Transform3D **translated**(offset: [Vector3](class_vector3.md#class-vector3))

Returns a copy of this transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform `X` with a corresponding translation transform `T` from the left, i.e., `T * X`.

This can be seen as transforming with respect to the global/parent frame.

---

Transform3D **translated_local**(offset: [Vector3](class_vector3.md#class-vector3))

Returns a copy of this transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform `X` with a corresponding translation transform `T` from the right, i.e., `X * T`.

This can be seen as transforming with respect to the local frame.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: Transform3D)

Returns `true` if the components of both transforms are not equal.

**Note:** Due to floating-point precision errors, consider using is_equal_approx() instead, which is more reliable.

---

[AABB](class_aabb.md#class-aabb) **operator \***(right: [AABB](class_aabb.md#class-aabb))

Transforms (multiplies) the [AABB](class_aabb.md#class-aabb) by this transformation matrix.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **operator \***(right: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))

Transforms (multiplies) every [Vector3](class_vector3.md#class-vector3) element of the given [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) by this transformation matrix.

On larger arrays, this operation is much faster than transforming each [Vector3](class_vector3.md#class-vector3) individually.

---

[Plane](class_plane.md#class-plane) **operator \***(right: [Plane](class_plane.md#class-plane))

Transforms (multiplies) the [Plane](class_plane.md#class-plane) by this transformation matrix.

---

Transform3D **operator \***(right: Transform3D)

Transforms (multiplies) this transform by the `right` transform.

This is the operation performed between parent and child [Node3D](class_node3d.md#class-node3d)s.

**Note:** If you need to only modify one attribute of this transform, consider using one of the following methods, instead:

- For translation, see translated() or translated_local().
- For rotation, see rotated() or rotated_local().
- For scale, see scaled() or scaled_local().

---

[Vector3](class_vector3.md#class-vector3) **operator \***(right: [Vector3](class_vector3.md#class-vector3))

Transforms (multiplies) the [Vector3](class_vector3.md#class-vector3) by this transformation matrix.

---

Transform3D **operator \***(right: [float](class_float.md#class-float))

Multiplies all components of the **Transform3D** by the given [float](class_float.md#class-float), including the origin. This affects the transform's scale uniformly, scaling the basis.

---

Transform3D **operator \***(right: [int](class_int.md#class-int))

Multiplies all components of the **Transform3D** by the given [int](class_int.md#class-int), including the origin. This affects the transform's scale uniformly, scaling the basis.

---

Transform3D **operator /**(right: [float](class_float.md#class-float))

Divides all components of the **Transform3D** by the given [float](class_float.md#class-float), including the origin. This affects the transform's scale uniformly, scaling the basis.

---

Transform3D **operator /**(right: [int](class_int.md#class-int))

Divides all components of the **Transform3D** by the given [int](class_int.md#class-int), including the origin. This affects the transform's scale uniformly, scaling the basis.

---

[bool](class_bool.md#class-bool) **operator ==**(right: Transform3D)

Returns `true` if the components of both transforms are exactly equal.

**Note:** Due to floating-point precision errors, consider using is_equal_approx() instead, which is more reliable.
