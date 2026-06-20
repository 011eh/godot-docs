# Basis

A 3×3 matrix for representing 3D rotation and scale.

## Description

The **Basis** built-in [Variant](class_variant.md#class-variant) type is a 3×3 [matrix](https://en.wikipedia.org/wiki/Matrix_(mathematics)) used to represent 3D rotation, scale, and shear. It is frequently used within a [Transform3D](class_transform3d.md#class-transform3d).

A **Basis** is composed by 3 axis vectors, each representing a column of the matrix: x, y, and z. The length of each axis ([Vector3.length()](class_vector3.md#class-vector3-method-length)) influences the basis's scale, while the direction of all axes influence the rotation. Usually, these axes are perpendicular to one another. However, when you rotate any axis individually, the basis becomes sheared. Applying a sheared basis to a 3D model will make the model appear distorted.

A **Basis** is:

- **Orthogonal** if its axes are perpendicular to each other.
- **Normalized** if the length of every axis is `1.0`.
- **Uniform** if all axes share the same length (see get_scale()).
- **Orthonormal** if it is both orthogonal and normalized, which allows it to only represent rotations (see orthonormalized()).
- **Conformal** if it is both orthogonal and uniform, which ensures it is not distorted.

For a general introduction, see the [Matrices and transforms](../tutorials/math/matrices_and_transforms.md) tutorial.

**Note:** Godot uses a [right-handed coordinate system](https://en.wikipedia.org/wiki/Right-hand_rule), which is a common standard. For directions, the convention for built-in types like [Camera3D](class_camera3d.md#class-camera3d) is for -Z to point forward (+X is right, +Y is up, and +Z is back). Other objects may use different direction conventions. For more information, see the [3D asset direction conventions](../tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html#d-asset-direction-conventions) tutorial.

**Note:** The basis matrices are exposed as [column-major](https://www.mindcontrol.org/~hplus/graphics/matrix-layout.html) order, which is the same as OpenGL. However, they are stored internally in row-major order, which is the same as DirectX.

**Note:** In a boolean context, a basis will evaluate to `false` if it's equal to IDENTITY. Otherwise, a basis will always evaluate to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Tutorials

- [Math documentation index](../tutorials/math/index.md)
- [Matrices and transforms](../tutorials/math/matrices_and_transforms.md)
- [Using 3D transforms](../tutorials/3d/using_transforms.md)
- [Matrix Transform Demo](https://godotengine.org/asset-library/asset/2787)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)
- [2.5D Game Demo](https://godotengine.org/asset-library/asset/2783)

## Properties

| [Vector3](class_vector3.md#class-vector3)   | x   | `Vector3(1, 0, 0)`   |
|---------------------------------------------|--------------------------------|----------------------|
| [Vector3](class_vector3.md#class-vector3)   | y   | `Vector3(0, 1, 0)`   |
| [Vector3](class_vector3.md#class-vector3)   | z   | `Vector3(0, 0, 1)`   |

## Constructors

| Basis   | Basis()                                                                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basis   | Basis(from: Basis)                                                                                                                             |
| Basis   | Basis(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))                                                             |
| Basis   | Basis(from: [Quaternion](class_quaternion.md#class-quaternion))                                                                                                |
| Basis   | Basis(x_axis: [Vector3](class_vector3.md#class-vector3), y_axis: [Vector3](class_vector3.md#class-vector3), z_axis: [Vector3](class_vector3.md#class-vector3)) |

## Methods

| [float](class_float.md#class-float)                | determinant()                                                                                                                                                                             |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basis                              | from_euler(euler: [Vector3](class_vector3.md#class-vector3), order: [int](class_int.md#class-int) = 2)                                                                                     |
| Basis                              | from_scale(scale: [Vector3](class_vector3.md#class-vector3))                                                                                                                               |
| [Vector3](class_vector3.md#class-vector3)          | get_euler(order: [int](class_int.md#class-int) = 2)                                                                                                                                         |
| [Quaternion](class_quaternion.md#class-quaternion) | get_rotation_quaternion()                                                                                                                                                     |
| [Vector3](class_vector3.md#class-vector3)          | get_scale()                                                                                                                                                                                 |
| Basis                              | inverse()                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                   | is_conformal()                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                   | is_equal_approx(b: Basis)                                                                                                                                             |
| [bool](class_bool.md#class-bool)                   | is_finite()                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                   | is_orthonormal()                                                                                                                                                                       |
| Basis                              | looking_at(target: [Vector3](class_vector3.md#class-vector3), up: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class-bool) = false) |
| Basis                              | orthonormalized()                                                                                                                                                                     |
| Basis                              | rotated(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))                                                                                          |
| Basis                              | scaled(scale: [Vector3](class_vector3.md#class-vector3))                                                                                                                                       |
| Basis                              | scaled_local(scale: [Vector3](class_vector3.md#class-vector3))                                                                                                                           |
| Basis                              | slerp(to: Basis, weight: [float](class_float.md#class-float))                                                                                                                   |
| [float](class_float.md#class-float)                | tdotx(with: [Vector3](class_vector3.md#class-vector3))                                                                                                                                          |
| [float](class_float.md#class-float)                | tdoty(with: [Vector3](class_vector3.md#class-vector3))                                                                                                                                          |
| [float](class_float.md#class-float)                | tdotz(with: [Vector3](class_vector3.md#class-vector3))                                                                                                                                          |
| Basis                              | transposed()                                                                                                                                                                               |

## Operators

| [bool](class_bool.md#class-bool)          | operator !=(right: Basis)                       |
|-------------------------------------------|----------------------------------------------------------------------------------------------------|
| Basis                     | operator \*(right: Basis)                       |
| [Vector3](class_vector3.md#class-vector3) | operator \*(right: [Vector3](class_vector3.md#class-vector3)) |
| Basis                     | operator \*(right: [float](class_float.md#class-float))         |
| Basis                     | operator \*(right: [int](class_int.md#class-int))                 |
| Basis                     | operator /(right: [float](class_float.md#class-float))          |
| Basis                     | operator /(right: [int](class_int.md#class-int))                  |
| [bool](class_bool.md#class-bool)          | operator ==(right: Basis)                        |
| [Vector3](class_vector3.md#class-vector3) | operator [](index: [int](class_int.md#class-int))                 |

---

## Constants

**IDENTITY** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)`

The identity **Basis**. This is an orthonormal basis with no rotation, no shear, and a scale of [Vector3.ONE](class_vector3.md#class-vector3-constant-one). This also means that:

- The x points right ([Vector3.RIGHT](class_vector3.md#class-vector3-constant-right));
- The y points up ([Vector3.UP](class_vector3.md#class-vector3-constant-up));
- The z points back ([Vector3.BACK](class_vector3.md#class-vector3-constant-back)).

```gdscript
var basis = Basis.IDENTITY
print("| X | Y | Z")
print("| %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x])
print("| %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y])
print("| %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z])
# Prints:
# | X | Y | Z
# | 1 | 0 | 0
# | 0 | 1 | 0
# | 0 | 0 | 1
```

If a [Vector3](class_vector3.md#class-vector3) or another **Basis** is transformed (multiplied) by this constant, no transformation occurs.

**Note:** In GDScript, this constant is equivalent to creating a Basis without any arguments. It can be used to make your code clearer, and for consistency with C#.

**FLIP_X** = `Basis(-1, 0, 0, 0, 1, 0, 0, 0, 1)`

When any basis is multiplied by FLIP_X, it negates all components of the x axis (the X column).

When FLIP_X is multiplied by any basis, it negates the [Vector3.x](class_vector3.md#class-vector3-property-x) component of all axes (the X row).

**FLIP_Y** = `Basis(1, 0, 0, 0, -1, 0, 0, 0, 1)`

When any basis is multiplied by FLIP_Y, it negates all components of the y axis (the Y column).

When FLIP_Y is multiplied by any basis, it negates the [Vector3.y](class_vector3.md#class-vector3-property-y) component of all axes (the Y row).

**FLIP_Z** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, -1)`

When any basis is multiplied by FLIP_Z, it negates all components of the z axis (the Z column).

When FLIP_Z is multiplied by any basis, it negates the [Vector3.z](class_vector3.md#class-vector3-property-z) component of all axes (the Z row).

---

## Property Descriptions

[Vector3](class_vector3.md#class-vector3) **x** = `Vector3(1, 0, 0)`

The basis's X axis, and the column `0` of the matrix.

On the identity basis, this vector points right ([Vector3.RIGHT](class_vector3.md#class-vector3-constant-right)).

---

[Vector3](class_vector3.md#class-vector3) **y** = `Vector3(0, 1, 0)`

The basis's Y axis, and the column `1` of the matrix.

On the identity basis, this vector points up ([Vector3.UP](class_vector3.md#class-vector3-constant-up)).

---

[Vector3](class_vector3.md#class-vector3) **z** = `Vector3(0, 0, 1)`

The basis's Z axis, and the column `2` of the matrix.

On the identity basis, this vector points back ([Vector3.BACK](class_vector3.md#class-vector3-constant-back)).

---

## Constructor Descriptions

Basis **Basis**()

Constructs a **Basis** identical to IDENTITY.

**Note:** In C#, this constructs a **Basis** with all of its components set to [Vector3.ZERO](class_vector3.md#class-vector3-constant-zero).

---

Basis **Basis**(from: Basis)

Constructs a **Basis** as a copy of the given **Basis**.

---

Basis **Basis**(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))

Constructs a **Basis** that only represents rotation, rotated around the `axis` by the given `angle`, in radians. The axis must be a normalized vector.

**Note:** This is the same as using rotated() on the IDENTITY basis. With more than one angle consider using from_euler(), instead.

---

Basis **Basis**(from: [Quaternion](class_quaternion.md#class-quaternion))

Constructs a **Basis** that only represents rotation from the given [Quaternion](class_quaternion.md#class-quaternion).

**Note:** Quaternions *only* store rotation, not scale. Because of this, conversions from **Basis** to [Quaternion](class_quaternion.md#class-quaternion) cannot always be reversed.

---

Basis **Basis**(x_axis: [Vector3](class_vector3.md#class-vector3), y_axis: [Vector3](class_vector3.md#class-vector3), z_axis: [Vector3](class_vector3.md#class-vector3))

Constructs a **Basis** from 3 axis vectors. These are the columns of the basis matrix.

---

## Method Descriptions

[float](class_float.md#class-float) **determinant**()

Returns the [determinant](https://en.wikipedia.org/wiki/Determinant) of this basis's matrix. For advanced math, this number can be used to determine a few attributes:

- If the determinant is exactly `0.0`, the basis is not invertible (see inverse()).
- If the determinant is a negative number, the basis represents a negative scale.

**Note:** If the basis's scale is the same for every axis, its determinant is always that scale by the power of 3.

---

Basis **from_euler**(euler: [Vector3](class_vector3.md#class-vector3), order: [int](class_int.md#class-int) = 2)

Constructs a new **Basis** that only represents rotation from the given [Vector3](class_vector3.md#class-vector3) of [Euler angles](https://en.wikipedia.org/wiki/Euler_angles), in radians.

- The [Vector3.x](class_vector3.md#class-vector3-property-x) should contain the angle around the x axis (pitch);
- The [Vector3.y](class_vector3.md#class-vector3-property-y) should contain the angle around the y axis (yaw);
- The [Vector3.z](class_vector3.md#class-vector3-property-z) should contain the angle around the z axis (roll).

GDScript

```gdscript
# Creates a Basis whose z axis points down.
var my_basis = Basis.from_euler(Vector3(TAU / 4, 0, 0))

print(my_basis.z) # Prints (0.0, -1.0, 0.0)
```

C#

```csharp
// Creates a Basis whose z axis points down.
var myBasis = Basis.FromEuler(new Vector3(Mathf.Tau / 4.0f, 0.0f, 0.0f));

GD.Print(myBasis.Z); // Prints (0, -1, 0)
```

The order of each consecutive rotation can be changed with `order` (see [EulerOrder](class_@globalscope.md#enum-globalscope-eulerorder) constants). In Godot, Euler angles always use intrinsic order. By default, the intrinsic YXZ convention is used ([@GlobalScope.EULER_ORDER_YXZ](class_@globalscope.md#class-globalscope-constant-euler-order-yxz)): the basis rotates first around the local Y axis (yaw), then local X (pitch), and lastly local Z (roll). When using the opposite method get_euler() to decompose a rotation, this order is reversed.

---

Basis **from_scale**(scale: [Vector3](class_vector3.md#class-vector3))

Constructs a new **Basis** that only represents scale, with no rotation or shear, from the given `scale` vector.

GDScript

```gdscript
var my_basis = Basis.from_scale(Vector3(2, 4, 8))

print(my_basis.x) # Prints (2.0, 0.0, 0.0)
print(my_basis.y) # Prints (0.0, 4.0, 0.0)
print(my_basis.z) # Prints (0.0, 0.0, 8.0)
```

C#

```csharp
var myBasis = Basis.FromScale(new Vector3(2.0f, 4.0f, 8.0f));

GD.Print(myBasis.X); // Prints (2, 0, 0)
GD.Print(myBasis.Y); // Prints (0, 4, 0)
GD.Print(myBasis.Z); // Prints (0, 0, 8)
```

**Note:** In linear algebra, the matrix of this basis is also known as a [diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix).

---

[Vector3](class_vector3.md#class-vector3) **get_euler**(order: [int](class_int.md#class-int) = 2)

Returns this basis's rotation as a [Vector3](class_vector3.md#class-vector3) of [Euler angles](https://en.wikipedia.org/wiki/Euler_angles), in radians. For the returned value:

- The [Vector3.x](class_vector3.md#class-vector3-property-x) contains the angle around the x axis (pitch);
- The [Vector3.y](class_vector3.md#class-vector3-property-y) contains the angle around the y axis (yaw);
- The [Vector3.z](class_vector3.md#class-vector3-property-z) contains the angle around the z axis (roll).

The order of each consecutive rotation can be changed with `order` (see [EulerOrder](class_@globalscope.md#enum-globalscope-eulerorder) constants). In Godot, Euler angles always use intrinsic order. By default, the intrinsic YXZ convention is used ([@GlobalScope.EULER_ORDER_YXZ](class_@globalscope.md#class-globalscope-constant-euler-order-yxz)): since we are decomposing, local Z (roll) is calculated first, then local X (pitch), and lastly local Y (yaw). When using the opposite method from_euler() to compose a rotation, this order is reversed.

**Note:** For this method to return correctly, the basis needs to be *orthonormal* (see orthonormalized()).

**Note:** Euler angles are much more intuitive but are not suitable for 3D math. Because of this, consider using the get_rotation_quaternion() method instead, which returns a [Quaternion](class_quaternion.md#class-quaternion).

**Note:** In the Inspector dock, a basis's rotation is often displayed in Euler angles (in degrees), as is the case with the [Node3D.rotation](class_node3d.md#class-node3d-property-rotation) property.

---

[Quaternion](class_quaternion.md#class-quaternion) **get_rotation_quaternion**()

Returns this basis's rotation as a [Quaternion](class_quaternion.md#class-quaternion).

**Note:** Quaternions are much more suitable for 3D math but are less intuitive. For user interfaces, consider using the get_euler() method, which returns Euler angles.

---

[Vector3](class_vector3.md#class-vector3) **get_scale**()

Returns the length of each axis of this basis, as a [Vector3](class_vector3.md#class-vector3). If the basis is not sheared, this value is the scaling factor. It is not affected by rotation.

GDScript

```gdscript
var my_basis = Basis(
    Vector3(2, 0, 0),
    Vector3(0, 4, 0),
    Vector3(0, 0, 8)
)
# Rotating the Basis in any way preserves its scale.
my_basis = my_basis.rotated(Vector3.UP, TAU / 2)
my_basis = my_basis.rotated(Vector3.RIGHT, TAU / 4)

print(my_basis.get_scale()) # Prints (2.0, 4.0, 8.0)
```

C#

```csharp
var myBasis = new Basis(
    Vector3(2.0f, 0.0f, 0.0f),
    Vector3(0.0f, 4.0f, 0.0f),
    Vector3(0.0f, 0.0f, 8.0f)
);
// Rotating the Basis in any way preserves its scale.
myBasis = myBasis.Rotated(Vector3.Up, Mathf.Tau / 2.0f);
myBasis = myBasis.Rotated(Vector3.Right, Mathf.Tau / 4.0f);

GD.Print(myBasis.Scale); // Prints (2, 4, 8)
```

**Note:** If the value returned by determinant() is negative, the scale is also negative.

---

Basis **inverse**()

Returns the [inverse of this basis's matrix](https://en.wikipedia.org/wiki/Invertible_matrix).

---

[bool](class_bool.md#class-bool) **is_conformal**()

Returns `true` if this basis is conformal. A conformal basis is both *orthogonal* (the axes are perpendicular to each other) and *uniform* (the axes share the same length). This method can be especially useful during physics calculations.

---

[bool](class_bool.md#class-bool) **is_equal_approx**(b: Basis)

Returns `true` if this basis and `b` are approximately equal, by calling [@GlobalScope.is_equal_approx()](class_@globalscope.md#class-globalscope-method-is-equal-approx) on all vector components.

---

[bool](class_bool.md#class-bool) **is_finite**()

Returns `true` if this basis is finite, by calling [@GlobalScope.is_finite()](class_@globalscope.md#class-globalscope-method-is-finite) on all vector components.

---

[bool](class_bool.md#class-bool) **is_orthonormal**()

Returns `true` if this basis is orthonormal. An orthonormal basis is both *orthogonal* (the axes are perpendicular to each other) and *normalized* (the length of every axis is `1.0`). This method can be especially useful during physics calculations.

---

Basis **looking_at**(target: [Vector3](class_vector3.md#class-vector3), up: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class-bool) = false)

Creates a new **Basis** with a rotation such that the forward axis (-Z) points towards the `target` position.

By default, the -Z axis (camera forward) is treated as forward (implies +X is right). If `use_model_front` is `true`, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward the `target` position.

The up axis (+Y) points as close to the `up` vector as possible while staying perpendicular to the forward axis. The returned basis is orthonormalized (see orthonormalized()).

The `target` and the `up` cannot be [Vector3.ZERO](class_vector3.md#class-vector3-constant-zero), and shouldn't be colinear to avoid unintended rotation around local Z axis.

---

Basis **orthonormalized**()

Returns the orthonormalized version of this basis. An orthonormal basis is both *orthogonal* (the axes are perpendicular to each other) and *normalized* (the axes have a length of `1.0`), which also means it can only represent a rotation.

It is often useful to call this method to avoid rounding errors on a rotating basis:

GDScript

```gdscript
# Rotate this Node3D every frame.
func _process(delta):
    basis = basis.rotated(Vector3.UP, TAU * delta)
    basis = basis.rotated(Vector3.RIGHT, TAU * delta)
    basis = basis.orthonormalized()
```

C#

```csharp
// Rotate this Node3D every frame.
public override void _Process(double delta)
{
    Basis = Basis.Rotated(Vector3.Up, Mathf.Tau * (float)delta)
            .Rotated(Vector3.Right, Mathf.Tau * (float)delta)
            .Orthonormalized();
}
```

---

Basis **rotated**(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))

Returns a copy of this basis rotated around the given `axis` by the given `angle` (in radians).

The `axis` must be a normalized vector (see [Vector3.normalized()](class_vector3.md#class-vector3-method-normalized)). If `angle` is positive, the basis is rotated counter-clockwise around the axis.

GDScript

```gdscript
var my_basis = Basis.IDENTITY
var angle = TAU / 2

my_basis = my_basis.rotated(Vector3.UP, angle)    # Rotate around the up axis (yaw).
my_basis = my_basis.rotated(Vector3.RIGHT, angle) # Rotate around the right axis (pitch).
my_basis = my_basis.rotated(Vector3.BACK, angle)  # Rotate around the back axis (roll).
```

C#

```csharp
var myBasis = Basis.Identity;
var angle = Mathf.Tau / 2.0f;

myBasis = myBasis.Rotated(Vector3.Up, angle);    // Rotate around the up axis (yaw).
myBasis = myBasis.Rotated(Vector3.Right, angle); // Rotate around the right axis (pitch).
myBasis = myBasis.Rotated(Vector3.Back, angle);  // Rotate around the back axis (roll).
```

---

Basis **scaled**(scale: [Vector3](class_vector3.md#class-vector3))

Returns this basis with each axis's components scaled by the given `scale`'s components.

The basis matrix's rows are multiplied by `scale`'s components. This operation is a global scale (relative to the parent).

GDScript

```gdscript
var my_basis = Basis(
    Vector3(1, 1, 1),
    Vector3(2, 2, 2),
    Vector3(3, 3, 3)
)
my_basis = my_basis.scaled(Vector3(0, 2, -2))

print(my_basis.x) # Prints (0.0, 2.0, -2.0)
print(my_basis.y) # Prints (0.0, 4.0, -4.0)
print(my_basis.z) # Prints (0.0, 6.0, -6.0)
```

C#

```csharp
var myBasis = new Basis(
    new Vector3(1.0f, 1.0f, 1.0f),
    new Vector3(2.0f, 2.0f, 2.0f),
    new Vector3(3.0f, 3.0f, 3.0f)
);
myBasis = myBasis.Scaled(new Vector3(0.0f, 2.0f, -2.0f));

GD.Print(myBasis.X); // Prints (0, 2, -2)
GD.Print(myBasis.Y); // Prints (0, 4, -4)
GD.Print(myBasis.Z); // Prints (0, 6, -6)
```

---

Basis **scaled_local**(scale: [Vector3](class_vector3.md#class-vector3))

Returns this basis with each axis scaled by the corresponding component in the given `scale`.

The basis matrix's columns are multiplied by `scale`'s components. This operation is a local scale (relative to self).

GDScript

```gdscript
var my_basis = Basis(
    Vector3(1, 1, 1),
    Vector3(2, 2, 2),
    Vector3(3, 3, 3)
)
my_basis = my_basis.scaled_local(Vector3(0, 2, -2))

print(my_basis.x) # Prints (0.0, 0.0, 0.0)
print(my_basis.y) # Prints (4.0, 4.0, 4.0)
print(my_basis.z) # Prints (-6.0, -6.0, -6.0)
```

C#

```csharp
var myBasis = new Basis(
    new Vector3(1.0f, 1.0f, 1.0f),
    new Vector3(2.0f, 2.0f, 2.0f),
    new Vector3(3.0f, 3.0f, 3.0f)
);
myBasis = myBasis.ScaledLocal(new Vector3(0.0f, 2.0f, -2.0f));

GD.Print(myBasis.X); // Prints (0, 0, 0)
GD.Print(myBasis.Y); // Prints (4, 4, 4)
GD.Print(myBasis.Z); // Prints (-6, -6, -6)
```

---

Basis **slerp**(to: Basis, weight: [float](class_float.md#class-float))

Performs a spherical-linear interpolation with the `to` basis, given a `weight`. Both this basis and `to` should represent a rotation.

**Example:** Smoothly rotate a [Node3D](class_node3d.md#class-node3d) to the target basis over time, with a [Tween](class_tween.md#class-tween):

```gdscript
var start_basis = Basis.IDENTITY
var target_basis = Basis.IDENTITY.rotated(Vector3.UP, TAU / 2)

func _ready():
    create_tween().tween_method(interpolate, 0.0, 1.0, 5.0).set_trans(Tween.TRANS_EXPO)

func interpolate(weight):
    basis = start_basis.slerp(target_basis, weight)
```

---

[float](class_float.md#class-float) **tdotx**(with: [Vector3](class_vector3.md#class-vector3))

Returns the transposed dot product between `with` and the x axis (see transposed()).

This is equivalent to `basis.x.dot(vector)`.

---

[float](class_float.md#class-float) **tdoty**(with: [Vector3](class_vector3.md#class-vector3))

Returns the transposed dot product between `with` and the y axis (see transposed()).

This is equivalent to `basis.y.dot(vector)`.

---

[float](class_float.md#class-float) **tdotz**(with: [Vector3](class_vector3.md#class-vector3))

Returns the transposed dot product between `with` and the z axis (see transposed()).

This is equivalent to `basis.z.dot(vector)`.

---

Basis **transposed**()

Returns the transposed version of this basis. This turns the basis matrix's columns into rows, and its rows into columns.

GDScript

```gdscript
var my_basis = Basis(
    Vector3(1, 2, 3),
    Vector3(4, 5, 6),
    Vector3(7, 8, 9)
)
my_basis = my_basis.transposed()

print(my_basis.x) # Prints (1.0, 4.0, 7.0)
print(my_basis.y) # Prints (2.0, 5.0, 8.0)
print(my_basis.z) # Prints (3.0, 6.0, 9.0)
```

C#

```csharp
var myBasis = new Basis(
    new Vector3(1.0f, 2.0f, 3.0f),
    new Vector3(4.0f, 5.0f, 6.0f),
    new Vector3(7.0f, 8.0f, 9.0f)
);
myBasis = myBasis.Transposed();

GD.Print(myBasis.X); // Prints (1, 4, 7)
GD.Print(myBasis.Y); // Prints (2, 5, 8)
GD.Print(myBasis.Z); // Prints (3, 6, 9)
```

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: Basis)

Returns `true` if the components of both **Basis** matrices are not equal.

**Note:** Due to floating-point precision errors, consider using is_equal_approx() instead, which is more reliable.

---

Basis **operator \***(right: Basis)

Transforms (multiplies) the `right` basis by this basis.

This is the operation performed between parent and child [Node3D](class_node3d.md#class-node3d)s.

---

[Vector3](class_vector3.md#class-vector3) **operator \***(right: [Vector3](class_vector3.md#class-vector3))

Transforms (multiplies) the `right` vector by this basis, returning a [Vector3](class_vector3.md#class-vector3).

GDScript

```gdscript
# Basis that swaps the X/Z axes and doubles the scale.
var my_basis = Basis(Vector3(0, 2, 0), Vector3(2, 0, 0), Vector3(0, 0, 2))
print(my_basis * Vector3(1, 2, 3)) # Prints (4.0, 2.0, 6.0)
```

C#

```csharp
// Basis that swaps the X/Z axes and doubles the scale.
var myBasis = new Basis(new Vector3(0, 2, 0), new Vector3(2, 0, 0), new Vector3(0, 0, 2));
GD.Print(myBasis * new Vector3(1, 2, 3)); // Prints (4, 2, 6)
```

---

Basis **operator \***(right: [float](class_float.md#class-float))

Multiplies all components of the **Basis** by the given [float](class_float.md#class-float). This affects the basis's scale uniformly, resizing all 3 axes by the `right` value.

---

Basis **operator \***(right: [int](class_int.md#class-int))

Multiplies all components of the **Basis** by the given [int](class_int.md#class-int). This affects the basis's scale uniformly, resizing all 3 axes by the `right` value.

---

Basis **operator /**(right: [float](class_float.md#class-float))

Divides all components of the **Basis** by the given [float](class_float.md#class-float). This affects the basis's scale uniformly, resizing all 3 axes by the `right` value.

---

Basis **operator /**(right: [int](class_int.md#class-int))

Divides all components of the **Basis** by the given [int](class_int.md#class-int). This affects the basis's scale uniformly, resizing all 3 axes by the `right` value.

---

[bool](class_bool.md#class-bool) **operator ==**(right: Basis)

Returns `true` if the components of both **Basis** matrices are exactly equal.

**Note:** Due to floating-point precision errors, consider using is_equal_approx() instead, which is more reliable.

---

[Vector3](class_vector3.md#class-vector3) **operator []**(index: [int](class_int.md#class-int))

Accesses each axis (column) of this basis by their index. Index `0` is the same as x, index `1` is the same as y, and index `2` is the same as z.

**Note:** In C++, this operator accesses the rows of the basis matrix, *not* the columns. For the same behavior as scripting languages, use the `set_column` and `get_column` methods.
