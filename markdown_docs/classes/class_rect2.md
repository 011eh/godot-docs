# Rect2

A 2D axis-aligned bounding box using floating-point coordinates.

## Description

The **Rect2** built-in [Variant](class_variant.md#class-variant) type represents an axis-aligned rectangle in a 2D space. It is defined by its position and size, which are [Vector2](class_vector2.md#class-vector2). It is frequently used for fast overlap tests (see intersects()). Although **Rect2** itself is axis-aligned, it can be combined with [Transform2D](class_transform2d.md#class-transform2d) to represent a rotated or skewed rectangle.

For integer coordinates, use [Rect2i](class_rect2i.md#class-rect2i). The 3D equivalent to **Rect2** is [AABB](class_aabb.md#class-aabb).

**Note:** Negative values for size are not supported. With negative size, most **Rect2** methods do not work correctly. Use abs() to get an equivalent **Rect2** with a non-negative size.

**Note:** In a boolean context, a **Rect2** evaluates to `false` if both position and size are zero (equal to [Vector2.ZERO](class_vector2.md#class-vector2-constant-zero)). Otherwise, it always evaluates to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Tutorials

- [Math documentation index](../tutorials/math/index.md)
- [Vector math](../tutorials/math/vector_math.md)
- [Advanced vector math](../tutorials/math/vectors_advanced.md)

## Properties

| [Vector2](class_vector2.md#class-vector2)   | end           | `Vector2(0, 0)`   |
|---------------------------------------------|--------------------------------------------|-------------------|
| [Vector2](class_vector2.md#class-vector2)   | position | `Vector2(0, 0)`   |
| [Vector2](class_vector2.md#class-vector2)   | size         | `Vector2(0, 0)`   |

## Constructors

| Rect2   | Rect2()                                                                                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rect2   | Rect2(from: Rect2)                                                                                                                                             |
| Rect2   | Rect2(from: [Rect2i](class_rect2i.md#class-rect2i))                                                                                                                            |
| Rect2   | Rect2(position: [Vector2](class_vector2.md#class-vector2), size: [Vector2](class_vector2.md#class-vector2))                                                                    |
| Rect2   | Rect2(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float), width: [float](class_float.md#class-float), height: [float](class_float.md#class-float)) |

## Methods

| Rect2                     | abs()                                                                                                                                                                                                     |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)          | encloses(b: Rect2)                                                                                                                                                                   |
| Rect2                     | expand(to: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                  |
| [float](class_float.md#class-float)       | get_area()                                                                                                                                                                                           |
| [Vector2](class_vector2.md#class-vector2) | get_center()                                                                                                                                                                                       |
| [Vector2](class_vector2.md#class-vector2) | get_support(direction: [Vector2](class_vector2.md#class-vector2))                                                                                                                                 |
| Rect2                     | grow(amount: [float](class_float.md#class-float))                                                                                                                                                        |
| Rect2                     | grow_individual(left: [float](class_float.md#class-float), top: [float](class_float.md#class-float), right: [float](class_float.md#class-float), bottom: [float](class_float.md#class-float)) |
| Rect2                     | grow_side(side: [int](class_int.md#class-int), amount: [float](class_float.md#class-float))                                                                                                         |
| [bool](class_bool.md#class-bool)          | has_area()                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)          | has_point(point: [Vector2](class_vector2.md#class-vector2))                                                                                                                                         |
| Rect2                     | intersection(b: Rect2)                                                                                                                                                           |
| [bool](class_bool.md#class-bool)          | intersects(b: Rect2, include_borders: [bool](class_bool.md#class-bool) = false)                                                                                                    |
| [bool](class_bool.md#class-bool)          | is_equal_approx(rect: Rect2)                                                                                                                                                  |
| [bool](class_bool.md#class-bool)          | is_finite()                                                                                                                                                                                         |
| Rect2                     | merge(b: Rect2)                                                                                                                                                                         |

## Operators

| [bool](class_bool.md#class-bool)   | operator !=(right: Rect2)                                       |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Rect2              | operator \*(right: [Transform2D](class_transform2d.md#class-transform2d)) |
| [bool](class_bool.md#class-bool)   | operator ==(right: Rect2)                                        |

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **end** = `Vector2(0, 0)`

The ending point. This is usually the bottom-right corner of the rectangle, and is equivalent to `position + size`. Setting this point affects the size.

---

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)`

The origin point. This is usually the top-left corner of the rectangle.

---

[Vector2](class_vector2.md#class-vector2) **size** = `Vector2(0, 0)`

The rectangle's width and height, starting from position. Setting this value also affects the end point.

**Note:** It's recommended setting the width and height to non-negative values, as most methods in Godot assume that the position is the top-left corner, and the end is the bottom-right corner. To get an equivalent rectangle with non-negative size, use abs().

---

## Constructor Descriptions

Rect2 **Rect2**()

Constructs a **Rect2** with its position and size set to [Vector2.ZERO](class_vector2.md#class-vector2-constant-zero).

---

Rect2 **Rect2**(from: Rect2)

Constructs a **Rect2** as a copy of the given **Rect2**.

---

Rect2 **Rect2**(from: [Rect2i](class_rect2i.md#class-rect2i))

Constructs a **Rect2** from a [Rect2i](class_rect2i.md#class-rect2i).

---

Rect2 **Rect2**(position: [Vector2](class_vector2.md#class-vector2), size: [Vector2](class_vector2.md#class-vector2))

Constructs a **Rect2** by `position` and `size`.

---

Rect2 **Rect2**(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float), width: [float](class_float.md#class-float), height: [float](class_float.md#class-float))

Constructs a **Rect2** by setting its position to (`x`, `y`), and its size to (`width`, `height`).

---

## Method Descriptions

Rect2 **abs**()

Returns a **Rect2** equivalent to this rectangle, with its width and height modified to be non-negative values, and with its position being the top-left corner of the rectangle.

GDScript

```gdscript
var rect = Rect2(25, 25, -100, -50)
var absolute = rect.abs() # absolute is Rect2(-75, -25, 100, 50)
```

C#

```csharp
var rect = new Rect2(25, 25, -100, -50);
var absolute = rect.Abs(); // absolute is Rect2(-75, -25, 100, 50)
```

**Note:** It's recommended to use this method when size is negative, as most other methods in Godot assume that the position is the top-left corner, and the end is the bottom-right corner.

---

[bool](class_bool.md#class-bool) **encloses**(b: Rect2)

Returns `true` if this rectangle *completely* encloses the `b` rectangle.

---

Rect2 **expand**(to: [Vector2](class_vector2.md#class-vector2))

Returns a copy of this rectangle expanded to align the edges with the given `to` point, if necessary.

GDScript

```gdscript
var rect = Rect2(0, 0, 5, 2)

rect = rect.expand(Vector2(10, 0)) # rect is Rect2(0, 0, 10, 2)
rect = rect.expand(Vector2(-5, 5)) # rect is Rect2(-5, 0, 15, 5)
```

C#

```csharp
var rect = new Rect2(0, 0, 5, 2);

rect = rect.Expand(new Vector2(10, 0)); // rect is Rect2(0, 0, 10, 2)
rect = rect.Expand(new Vector2(-5, 5)); // rect is Rect2(-5, 0, 15, 5)
```

---

[float](class_float.md#class-float) **get_area**()

Returns the rectangle's area. This is equivalent to `size.x * size.y`. See also has_area().

---

[Vector2](class_vector2.md#class-vector2) **get_center**()

Returns the center point of the rectangle. This is the same as `position + (size / 2.0)`.

---

[Vector2](class_vector2.md#class-vector2) **get_support**(direction: [Vector2](class_vector2.md#class-vector2))

Returns the vertex's position of this rect that's the farthest in the given direction. This point is commonly known as the support point in collision detection algorithms.

---

Rect2 **grow**(amount: [float](class_float.md#class-float))

Returns a copy of this rectangle extended on all sides by the given `amount`. A negative `amount` shrinks the rectangle instead. See also grow_individual() and grow_side().

GDScript

```gdscript
var a = Rect2(4, 4, 8, 8).grow(4) # a is Rect2(0, 0, 16, 16)
var b = Rect2(0, 0, 8, 4).grow(2) # b is Rect2(-2, -2, 12, 8)
```

C#

```csharp
var a = new Rect2(4, 4, 8, 8).Grow(4); // a is Rect2(0, 0, 16, 16)
var b = new Rect2(0, 0, 8, 4).Grow(2); // b is Rect2(-2, -2, 12, 8)
```

---

Rect2 **grow_individual**(left: [float](class_float.md#class-float), top: [float](class_float.md#class-float), right: [float](class_float.md#class-float), bottom: [float](class_float.md#class-float))

Returns a copy of this rectangle with its `left`, `top`, `right`, and `bottom` sides extended by the given amounts. Negative values shrink the sides, instead. See also grow() and grow_side().

---

Rect2 **grow_side**(side: [int](class_int.md#class-int), amount: [float](class_float.md#class-float))

Returns a copy of this rectangle with its `side` extended by the given `amount` (see [Side](class_@globalscope.md#enum-globalscope-side) constants). A negative `amount` shrinks the rectangle, instead. See also grow() and grow_individual().

---

[bool](class_bool.md#class-bool) **has_area**()

Returns `true` if this rectangle has positive width and height. See also get_area().

---

[bool](class_bool.md#class-bool) **has_point**(point: [Vector2](class_vector2.md#class-vector2))

Returns `true` if the rectangle contains the given `point`. By convention, points on the right and bottom edges are **not** included.

**Note:** This method is not reliable for **Rect2** with a *negative* size. Use abs() first to get a valid rectangle.

---

Rect2 **intersection**(b: Rect2)

Returns the intersection between this rectangle and `b`. If the rectangles do not intersect, returns an empty **Rect2**.

GDScript

```gdscript
var rect1 = Rect2(0, 0, 5, 10)
var rect2 = Rect2(2, 0, 8, 4)

var a = rect1.intersection(rect2) # a is Rect2(2, 0, 3, 4)
```

C#

```csharp
var rect1 = new Rect2(0, 0, 5, 10);
var rect2 = new Rect2(2, 0, 8, 4);

var a = rect1.Intersection(rect2); // a is Rect2(2, 0, 3, 4)
```

**Note:** If you only need to know whether two rectangles are overlapping, use intersects(), instead.

---

[bool](class_bool.md#class-bool) **intersects**(b: Rect2, include_borders: [bool](class_bool.md#class-bool) = false)

Returns `true` if this rectangle overlaps with the `b` rectangle. The edges of both rectangles are excluded, unless `include_borders` is `true`.

---

[bool](class_bool.md#class-bool) **is_equal_approx**(rect: Rect2)

Returns `true` if this rectangle and `rect` are approximately equal, by calling [Vector2.is_equal_approx()](class_vector2.md#class-vector2-method-is-equal-approx) on the position and the size.

---

[bool](class_bool.md#class-bool) **is_finite**()

Returns `true` if this rectangle's values are finite, by calling [Vector2.is_finite()](class_vector2.md#class-vector2-method-is-finite) on the position and the size.

---

Rect2 **merge**(b: Rect2)

Returns a **Rect2** that encloses both this rectangle and `b` around the edges. See also encloses().

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: Rect2)

Returns `true` if the position or size of both rectangles are not equal.

**Note:** Due to floating-point precision errors, consider using is_equal_approx() instead, which is more reliable.

---

Rect2 **operator \***(right: [Transform2D](class_transform2d.md#class-transform2d))

Inversely transforms (multiplies) the **Rect2** by the given [Transform2D](class_transform2d.md#class-transform2d) transformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).

`rect * transform` is equivalent to `transform.inverse() * rect`. See [Transform2D.inverse()](class_transform2d.md#class-transform2d-method-inverse).

For transforming by inverse of an affine transformation (e.g. with scaling) `transform.affine_inverse() * rect` can be used instead. See [Transform2D.affine_inverse()](class_transform2d.md#class-transform2d-method-affine-inverse).

---

[bool](class_bool.md#class-bool) **operator ==**(right: Rect2)

Returns `true` if both position and size of the rectangles are exactly equal, respectively.

**Note:** Due to floating-point precision errors, consider using is_equal_approx() instead, which is more reliable.
