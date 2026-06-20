# Rect2i

A 2D axis-aligned bounding box using integer coordinates.

## Description

The **Rect2i** built-in [Variant](class_variant.md#class-variant) type represents an axis-aligned rectangle in a 2D space, using integer coordinates. It is defined by its position and size, which are [Vector2i](class_vector2i.md#class-vector2i). Because it does not rotate, it is frequently used for fast overlap tests (see intersects()).

For floating-point coordinates, see [Rect2](class_rect2.md#class-rect2).

**Note:** Negative values for size are not supported. With negative size, most **Rect2i** methods do not work correctly. Use abs() to get an equivalent **Rect2i** with a non-negative size.

**Note:** In a boolean context, a **Rect2i** evaluates to `false` if both position and size are zero (equal to [Vector2i.ZERO](class_vector2i.md#class-vector2i-constant-zero)). Otherwise, it always evaluates to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Tutorials

- [Math documentation index](../tutorials/math/index.md)
- [Vector math](../tutorials/math/vector_math.md)

## Properties

| [Vector2i](class_vector2i.md#class-vector2i)   | end           | `Vector2i(0, 0)`   |
|------------------------------------------------|---------------------------------------------|--------------------|
| [Vector2i](class_vector2i.md#class-vector2i)   | position | `Vector2i(0, 0)`   |
| [Vector2i](class_vector2i.md#class-vector2i)   | size         | `Vector2i(0, 0)`   |

## Constructors

| Rect2i   | Rect2i()                                                                                                                                                |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rect2i   | Rect2i(from: Rect2i)                                                                                                                   |
| Rect2i   | Rect2i(from: [Rect2](class_rect2.md#class-rect2))                                                                                                       |
| Rect2i   | Rect2i(position: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i))                                      |
| Rect2i   | Rect2i(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int)) |

## Methods

| Rect2i                      | abs()                                                                                                                                                                             |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)             | encloses(b: Rect2i)                                                                                                                                         |
| Rect2i                      | expand(to: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                       |
| [int](class_int.md#class-int)                | get_area()                                                                                                                                                                   |
| [Vector2i](class_vector2i.md#class-vector2i) | get_center()                                                                                                                                                               |
| Rect2i                      | grow(amount: [int](class_int.md#class-int))                                                                                                                                      |
| Rect2i                      | grow_individual(left: [int](class_int.md#class-int), top: [int](class_int.md#class-int), right: [int](class_int.md#class-int), bottom: [int](class_int.md#class-int)) |
| Rect2i                      | grow_side(side: [int](class_int.md#class-int), amount: [int](class_int.md#class-int))                                                                                       |
| [bool](class_bool.md#class-bool)             | has_area()                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)             | has_point(point: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                              |
| Rect2i                      | intersection(b: Rect2i)                                                                                                                                 |
| [bool](class_bool.md#class-bool)             | intersects(b: Rect2i)                                                                                                                                     |
| Rect2i                      | merge(b: Rect2i)                                                                                                                                               |

## Operators

| [bool](class_bool.md#class-bool)   | operator !=(right: Rect2i)   |
|------------------------------------|------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)   | operator ==(right: Rect2i)    |

---

## Property Descriptions

[Vector2i](class_vector2i.md#class-vector2i) **end** = `Vector2i(0, 0)`

The ending point. This is usually the bottom-right corner of the rectangle, and is equivalent to `position + size`. Setting this point affects the size.

---

[Vector2i](class_vector2i.md#class-vector2i) **position** = `Vector2i(0, 0)`

The origin point. This is usually the top-left corner of the rectangle.

---

[Vector2i](class_vector2i.md#class-vector2i) **size** = `Vector2i(0, 0)`

The rectangle's width and height, starting from position. Setting this value also affects the end point.

**Note:** It's recommended setting the width and height to non-negative values, as most methods in Godot assume that the position is the top-left corner, and the end is the bottom-right corner. To get an equivalent rectangle with non-negative size, use abs().

---

## Constructor Descriptions

Rect2i **Rect2i**()

Constructs a **Rect2i** with its position and size set to [Vector2i.ZERO](class_vector2i.md#class-vector2i-constant-zero).

---

Rect2i **Rect2i**(from: Rect2i)

Constructs a **Rect2i** as a copy of the given **Rect2i**.

---

Rect2i **Rect2i**(from: [Rect2](class_rect2.md#class-rect2))

Constructs a **Rect2i** from a [Rect2](class_rect2.md#class-rect2). The floating-point coordinates are truncated.

---

Rect2i **Rect2i**(position: [Vector2i](class_vector2i.md#class-vector2i), size: [Vector2i](class_vector2i.md#class-vector2i))

Constructs a **Rect2i** by `position` and `size`.

---

Rect2i **Rect2i**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int))

Constructs a **Rect2i** by setting its position to (`x`, `y`), and its size to (`width`, `height`).

---

## Method Descriptions

Rect2i **abs**()

Returns a **Rect2i** equivalent to this rectangle, with its width and height modified to be non-negative values, and with its position being the top-left corner of the rectangle.

GDScript

```gdscript
var rect = Rect2i(25, 25, -100, -50)
var absolute = rect.abs() # absolute is Rect2i(-75, -25, 100, 50)
```

C#

```csharp
var rect = new Rect2I(25, 25, -100, -50);
var absolute = rect.Abs(); // absolute is Rect2I(-75, -25, 100, 50)
```

**Note:** It's recommended to use this method when size is negative, as most other methods in Godot assume that the position is the top-left corner, and the end is the bottom-right corner.

---

[bool](class_bool.md#class-bool) **encloses**(b: Rect2i)

Returns `true` if this **Rect2i** completely encloses another one.

---

Rect2i **expand**(to: [Vector2i](class_vector2i.md#class-vector2i))

Returns a copy of this rectangle expanded to align the edges with the given `to` point, if necessary.

GDScript

```gdscript
var rect = Rect2i(0, 0, 5, 2)

rect = rect.expand(Vector2i(10, 0)) # rect is Rect2i(0, 0, 10, 2)
rect = rect.expand(Vector2i(-5, 5)) # rect is Rect2i(-5, 0, 15, 5)
```

C#

```csharp
var rect = new Rect2I(0, 0, 5, 2);

rect = rect.Expand(new Vector2I(10, 0)); // rect is Rect2I(0, 0, 10, 2)
rect = rect.Expand(new Vector2I(-5, 5)); // rect is Rect2I(-5, 0, 15, 5)
```

---

[int](class_int.md#class-int) **get_area**()

Returns the rectangle's area. This is equivalent to `size.x * size.y`. See also has_area().

---

[Vector2i](class_vector2i.md#class-vector2i) **get_center**()

Returns the center point of the rectangle. This is the same as `position + (size / 2)`.

**Note:** If the size is odd, the result will be rounded towards position.

---

Rect2i **grow**(amount: [int](class_int.md#class-int))

Returns a copy of this rectangle extended on all sides by the given `amount`. A negative `amount` shrinks the rectangle instead. See also grow_individual() and grow_side().

GDScript

```gdscript
var a = Rect2i(4, 4, 8, 8).grow(4) # a is Rect2i(0, 0, 16, 16)
var b = Rect2i(0, 0, 8, 4).grow(2) # b is Rect2i(-2, -2, 12, 8)
```

C#

```csharp
var a = new Rect2I(4, 4, 8, 8).Grow(4); // a is Rect2I(0, 0, 16, 16)
var b = new Rect2I(0, 0, 8, 4).Grow(2); // b is Rect2I(-2, -2, 12, 8)
```

---

Rect2i **grow_individual**(left: [int](class_int.md#class-int), top: [int](class_int.md#class-int), right: [int](class_int.md#class-int), bottom: [int](class_int.md#class-int))

Returns a copy of this rectangle with its `left`, `top`, `right`, and `bottom` sides extended by the given amounts. Negative values shrink the sides, instead. See also grow() and grow_side().

---

Rect2i **grow_side**(side: [int](class_int.md#class-int), amount: [int](class_int.md#class-int))

Returns a copy of this rectangle with its `side` extended by the given `amount` (see [Side](class_@globalscope.md#enum-globalscope-side) constants). A negative `amount` shrinks the rectangle, instead. See also grow() and grow_individual().

---

[bool](class_bool.md#class-bool) **has_area**()

Returns `true` if this rectangle has positive width and height. See also get_area().

---

[bool](class_bool.md#class-bool) **has_point**(point: [Vector2i](class_vector2i.md#class-vector2i))

Returns `true` if the rectangle contains the given `point`. By convention, points on the right and bottom edges are **not** included.

**Note:** This method is not reliable for **Rect2i** with a *negative* size. Use abs() first to get a valid rectangle.

---

Rect2i **intersection**(b: Rect2i)

Returns the intersection between this rectangle and `b`. If the rectangles do not intersect, returns an empty **Rect2i**.

GDScript

```gdscript
var a = Rect2i(0, 0, 5, 10)
var b = Rect2i(2, 0, 8, 4)

var c = a.intersection(b) # c is Rect2i(2, 0, 3, 4)
```

C#

```csharp
var a = new Rect2I(0, 0, 5, 10);
var b = new Rect2I(2, 0, 8, 4);

var c = rect1.Intersection(rect2); // c is Rect2I(2, 0, 3, 4)
```

**Note:** If you only need to know whether two rectangles are overlapping, use intersects(), instead.

---

[bool](class_bool.md#class-bool) **intersects**(b: Rect2i)

Returns `true` if this rectangle overlaps with the `b` rectangle. The edges of both rectangles are excluded.

---

Rect2i **merge**(b: Rect2i)

Returns a **Rect2i** that encloses both this rectangle and `b` around the edges. See also encloses().

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: Rect2i)

Returns `true` if the position or size of both rectangles are not equal.

---

[bool](class_bool.md#class-bool) **operator ==**(right: Rect2i)

Returns `true` if both position and size of the rectangles are equal, respectively.
