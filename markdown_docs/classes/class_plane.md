# Plane

A plane in Hessian normal form.

## Description

Represents a normalized plane equation. normal is the normal of the plane (a, b, c normalized), and d is the distance from the origin to the plane (in the direction of "normal"). "Over" or "Above" the plane is considered the side of the plane towards where the normal is pointing.

**Note:** In a boolean context, a plane will evaluate to `false` if all its components equal `0`. Otherwise, a plane will always evaluate to `true`.

## Tutorials

- [Math documentation index](../tutorials/math/index.md)

## Properties

| [float](class_float.md#class-float)       | d           | `0.0`              |
|-------------------------------------------|----------------------------------------|--------------------|
| [Vector3](class_vector3.md#class-vector3) | normal | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float)       | x           | `0.0`              |
| [float](class_float.md#class-float)       | y           | `0.0`              |
| [float](class_float.md#class-float)       | z           | `0.0`              |

## Constructors

| Plane   | Plane()                                                                                                                                                               |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plane   | Plane(from: Plane)                                                                                                                                    |
| Plane   | Plane(a: [float](class_float.md#class-float), b: [float](class_float.md#class-float), c: [float](class_float.md#class-float), d: [float](class_float.md#class-float)) |
| Plane   | Plane(normal: [Vector3](class_vector3.md#class-vector3))                                                                                                              |
| Plane   | Plane(normal: [Vector3](class_vector3.md#class-vector3), d: [float](class_float.md#class-float))                                                                      |
| Plane   | Plane(normal: [Vector3](class_vector3.md#class-vector3), point: [Vector3](class_vector3.md#class-vector3))                                                            |
| Plane   | Plane(point1: [Vector3](class_vector3.md#class-vector3), point2: [Vector3](class_vector3.md#class-vector3), point3: [Vector3](class_vector3.md#class-vector3))        |

## Methods

| [float](class_float.md#class-float)       | distance_to(point: [Vector3](class_vector3.md#class-vector3))                                                             |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Vector3](class_vector3.md#class-vector3) | get_center()                                                                                                               |
| [bool](class_bool.md#class-bool)          | has_point(point: [Vector3](class_vector3.md#class-vector3), tolerance: [float](class_float.md#class-float) = 1e-05)         |
| [Variant](class_variant.md#class-variant) | intersect_3(b: Plane, c: Plane)                                                           |
| [Variant](class_variant.md#class-variant) | intersects_ray(from: [Vector3](class_vector3.md#class-vector3), dir: [Vector3](class_vector3.md#class-vector3))        |
| [Variant](class_variant.md#class-variant) | intersects_segment(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3)) |
| [bool](class_bool.md#class-bool)          | is_equal_approx(to_plane: Plane)                                                                      |
| [bool](class_bool.md#class-bool)          | is_finite()                                                                                                                 |
| [bool](class_bool.md#class-bool)          | is_point_over(point: [Vector3](class_vector3.md#class-vector3))                                                         |
| Plane                     | normalized()                                                                                                               |
| [Vector3](class_vector3.md#class-vector3) | project(point: [Vector3](class_vector3.md#class-vector3))                                                                     |

## Operators

| [bool](class_bool.md#class-bool)   | operator !=(right: Plane)                                       |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Plane              | operator \*(right: [Transform3D](class_transform3d.md#class-transform3d)) |
| [bool](class_bool.md#class-bool)   | operator ==(right: Plane)                                        |
| Plane              | operator unary+()                                                                  |
| Plane              | operator unary-()                                                                 |

---

## Constants

**PLANE_YZ** = `Plane(1, 0, 0, 0)`

A plane that extends in the Y and Z axes (normal vector points +X).

**PLANE_XZ** = `Plane(0, 1, 0, 0)`

A plane that extends in the X and Z axes (normal vector points +Y).

**PLANE_XY** = `Plane(0, 0, 1, 0)`

A plane that extends in the X and Y axes (normal vector points +Z).

---

## Property Descriptions

[float](class_float.md#class-float) **d** = `0.0`

The distance from the origin to the plane, expressed in terms of normal (according to its direction and magnitude). Actual absolute distance from the origin to the plane can be calculated as `abs(d) / normal.length()` (if normal has zero length then this **Plane** does not represent a valid plane).

In the scalar equation of the plane `ax + by + cz = d`, this is `d`, while the `(a, b, c)` coordinates are represented by the normal property.

---

[Vector3](class_vector3.md#class-vector3) **normal** = `Vector3(0, 0, 0)`

The normal of the plane, typically a unit vector. Shouldn't be a zero vector as **Plane** with such normal does not represent a valid plane.

In the scalar equation of the plane `ax + by + cz = d`, this is the vector `(a, b, c)`, where `d` is the d property.

---

[float](class_float.md#class-float) **x** = `0.0`

The X component of the plane's normal vector.

---

[float](class_float.md#class-float) **y** = `0.0`

The Y component of the plane's normal vector.

---

[float](class_float.md#class-float) **z** = `0.0`

The Z component of the plane's normal vector.

---

## Constructor Descriptions

Plane **Plane**()

Constructs a default-initialized **Plane** with all components set to `0`.

---

Plane **Plane**(from: Plane)

Constructs a **Plane** as a copy of the given **Plane**.

---

Plane **Plane**(a: [float](class_float.md#class-float), b: [float](class_float.md#class-float), c: [float](class_float.md#class-float), d: [float](class_float.md#class-float))

Creates a plane from the four parameters. The three components of the resulting plane's normal are `a`, `b` and `c`, and the plane has a distance of `d` from the origin.

---

Plane **Plane**(normal: [Vector3](class_vector3.md#class-vector3))

Creates a plane from the normal vector. The plane will intersect the origin.

The `normal` of the plane must be a unit vector.

---

Plane **Plane**(normal: [Vector3](class_vector3.md#class-vector3), d: [float](class_float.md#class-float))

Creates a plane from the normal vector and the plane's distance from the origin.

The `normal` of the plane must be a unit vector.

---

Plane **Plane**(normal: [Vector3](class_vector3.md#class-vector3), point: [Vector3](class_vector3.md#class-vector3))

Creates a plane from the normal vector and a point on the plane.

The `normal` of the plane must be a unit vector.

---

Plane **Plane**(point1: [Vector3](class_vector3.md#class-vector3), point2: [Vector3](class_vector3.md#class-vector3), point3: [Vector3](class_vector3.md#class-vector3))

Creates a plane from the three points, given in clockwise order.

---

## Method Descriptions

[float](class_float.md#class-float) **distance_to**(point: [Vector3](class_vector3.md#class-vector3))

Returns the shortest distance from the plane to the position `point`. If the point is above the plane, the distance will be positive. If below, the distance will be negative.

---

[Vector3](class_vector3.md#class-vector3) **get_center**()

Returns the center of the plane.

---

[bool](class_bool.md#class-bool) **has_point**(point: [Vector3](class_vector3.md#class-vector3), tolerance: [float](class_float.md#class-float) = 1e-05)

Returns `true` if `point` is inside the plane. Comparison uses a custom minimum `tolerance` threshold.

---

[Variant](class_variant.md#class-variant) **intersect_3**(b: Plane, c: Plane)

Returns the intersection point of the three planes `b`, `c` and this plane. If no intersection is found, `null` is returned.

---

[Variant](class_variant.md#class-variant) **intersects_ray**(from: [Vector3](class_vector3.md#class-vector3), dir: [Vector3](class_vector3.md#class-vector3))

Returns the intersection point of a ray consisting of the position `from` and the direction normal `dir` with this plane. If no intersection is found, `null` is returned.

---

[Variant](class_variant.md#class-variant) **intersects_segment**(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3))

Returns the intersection point of a segment from position `from` to position `to` with this plane. If no intersection is found, `null` is returned.

---

[bool](class_bool.md#class-bool) **is_equal_approx**(to_plane: Plane)

Returns `true` if this plane and `to_plane` are approximately equal, by running [@GlobalScope.is_equal_approx()](class_@globalscope.md#class-globalscope-method-is-equal-approx) on each component.

---

[bool](class_bool.md#class-bool) **is_finite**()

Returns `true` if this plane is finite, by calling [@GlobalScope.is_finite()](class_@globalscope.md#class-globalscope-method-is-finite) on each component.

---

[bool](class_bool.md#class-bool) **is_point_over**(point: [Vector3](class_vector3.md#class-vector3))

Returns `true` if `point` is located above the plane.

---

Plane **normalized**()

Returns a copy of the plane, with normalized normal (so it's a unit vector). Returns `Plane(0, 0, 0, 0)` if normal can't be normalized (it has zero length).

---

[Vector3](class_vector3.md#class-vector3) **project**(point: [Vector3](class_vector3.md#class-vector3))

Returns the orthogonal projection of `point` into a point in the plane.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: Plane)

Returns `true` if the planes are not equal.

**Note:** Due to floating-point precision errors, consider using is_equal_approx() instead, which is more reliable.

---

Plane **operator \***(right: [Transform3D](class_transform3d.md#class-transform3d))

Inversely transforms (multiplies) the **Plane** by the given [Transform3D](class_transform3d.md#class-transform3d) transformation matrix.

`plane * transform` is equivalent to `transform.affine_inverse() * plane`. See [Transform3D.affine_inverse()](class_transform3d.md#class-transform3d-method-affine-inverse).

---

[bool](class_bool.md#class-bool) **operator ==**(right: Plane)

Returns `true` if the planes are exactly equal.

**Note:** Due to floating-point precision errors, consider using is_equal_approx() instead, which is more reliable.

---

Plane **operator unary+**()

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

Plane **operator unary-**()

Returns the negative value of the **Plane**. This is the same as writing `Plane(-p.normal, -p.d)`. This operation flips the direction of the normal vector and also flips the distance value, resulting in a Plane that is in the same place, but facing the opposite direction.
