# Vector2i

A 2D vector using integer coordinates.

## Description

A 2-element structure that can be used to represent 2D grid coordinates or any other pair of integers.

It uses integer coordinates and is therefore preferable to [Vector2](class_vector2.md#class-vector2) when exact precision is required. Note that the values are limited to 32 bits, and unlike [Vector2](class_vector2.md#class-vector2) this cannot be configured with an engine build option. Use [int](class_int.md#class-int) or [PackedInt64Array](class_packedint64array.md#class-packedint64array) if 64-bit values are needed.

**Note:** In a boolean context, a Vector2i will evaluate to `false` if it's equal to `Vector2i(0, 0)`. Otherwise, a Vector2i will always evaluate to `true`.

## Tutorials

- [Math documentation index](../tutorials/math/index.md)
- [Vector math](../tutorials/math/vector_math.md)
- [3Blue1Brown Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

## Properties

| [int](class_int.md#class-int)   | x   | `0`   |
|---------------------------------|-----------------------------------|-------|
| [int](class_int.md#class-int)   | y   | `0`   |

## Constructors

| Vector2i   | Vector2i()                                                                   |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Vector2i   | Vector2i(from: Vector2i)                                  |
| Vector2i   | Vector2i(from: [Vector2](class_vector2.md#class-vector2))                    |
| Vector2i   | Vector2i(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int)) |

## Methods

| Vector2i         | abs()                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float) | aspect()                                                                       |
| Vector2i         | clamp(min: Vector2i, max: Vector2i)       |
| Vector2i         | clampi(min: [int](class_int.md#class-int), max: [int](class_int.md#class-int)) |
| [int](class_int.md#class-int)       | distance_squared_to(to: Vector2i)              |
| [float](class_float.md#class-float) | distance_to(to: Vector2i)                              |
| [float](class_float.md#class-float) | length()                                                                       |
| [int](class_int.md#class-int)       | length_squared()                                                       |
| Vector2i         | max(with: Vector2i)                                            |
| [int](class_int.md#class-int)       | max_axis_index()                                                       |
| Vector2i         | maxi(with: [int](class_int.md#class-int))                                        |
| Vector2i         | min(with: Vector2i)                                            |
| [int](class_int.md#class-int)       | min_axis_index()                                                       |
| Vector2i         | mini(with: [int](class_int.md#class-int))                                        |
| Vector2i         | sign()                                                                           |
| Vector2i         | snapped(step: Vector2i)                                    |
| Vector2i         | snappedi(step: [int](class_int.md#class-int))                                |

## Operators

| [bool](class_bool.md#class-bool)          | operator !=(right: Vector2i)      |
|-------------------------------------------|-----------------------------------------------------------------------------------------------|
| Vector2i               | operator %(right: Vector2i)       |
| Vector2i               | operator %(right: [int](class_int.md#class-int))          |
| Vector2i               | operator \*(right: Vector2i)      |
| [Vector2](class_vector2.md#class-vector2) | operator \*(right: [float](class_float.md#class-float)) |
| Vector2i               | operator \*(right: [int](class_int.md#class-int))         |
| Vector2i               | operator +(right: Vector2i)       |
| Vector2i               | operator -(right: Vector2i)       |
| Vector2i               | operator /(right: Vector2i)       |
| [Vector2](class_vector2.md#class-vector2) | operator /(right: [float](class_float.md#class-float))  |
| Vector2i               | operator /(right: [int](class_int.md#class-int))          |
| [bool](class_bool.md#class-bool)          | operator <(right: Vector2i)        |
| [bool](class_bool.md#class-bool)          | operator <=(right: Vector2i)      |
| [bool](class_bool.md#class-bool)          | operator ==(right: Vector2i)       |
| [bool](class_bool.md#class-bool)          | operator >(right: Vector2i)        |
| [bool](class_bool.md#class-bool)          | operator >=(right: Vector2i)      |
| [int](class_int.md#class-int)             | operator [](index: [int](class_int.md#class-int))         |
| Vector2i               | operator unary+()                                          |
| Vector2i               | operator unary-()                                         |

---

## Enumerations

enum **Axis**:

Axis **AXIS_X** = `0`

Enumerated value for the X axis. Returned by max_axis_index() and min_axis_index().

Axis **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by max_axis_index() and min_axis_index().

---

## Constants

**ZERO** = `Vector2i(0, 0)`

Zero vector, a vector with all components set to `0`.

**ONE** = `Vector2i(1, 1)`

One vector, a vector with all components set to `1`.

**MIN** = `Vector2i(-2147483648, -2147483648)`

Min vector, a vector with all components equal to `INT32_MIN`. Can be used as a negative integer equivalent of [Vector2.INF](class_vector2.md#class-vector2-constant-inf).

**MAX** = `Vector2i(2147483647, 2147483647)`

Max vector, a vector with all components equal to `INT32_MAX`. Can be used as an integer equivalent of [Vector2.INF](class_vector2.md#class-vector2-constant-inf).

**LEFT** = `Vector2i(-1, 0)`

Left unit vector. Represents the direction of left.

**RIGHT** = `Vector2i(1, 0)`

Right unit vector. Represents the direction of right.

**UP** = `Vector2i(0, -1)`

Up unit vector. Y is down in 2D, so this vector points -Y.

**DOWN** = `Vector2i(0, 1)`

Down unit vector. Y is down in 2D, so this vector points +Y.

---

## Property Descriptions

[int](class_int.md#class-int) **x** = `0`

The vector's X component. Also accessible by using the index position `[0]`.

---

[int](class_int.md#class-int) **y** = `0`

The vector's Y component. Also accessible by using the index position `[1]`.

---

## Constructor Descriptions

Vector2i **Vector2i**()

Constructs a default-initialized **Vector2i** with all components set to `0`.

---

Vector2i **Vector2i**(from: Vector2i)

Constructs a **Vector2i** as a copy of the given **Vector2i**.

---

Vector2i **Vector2i**(from: [Vector2](class_vector2.md#class-vector2))

Constructs a new **Vector2i** from the given [Vector2](class_vector2.md#class-vector2) by truncating components' fractional parts (rounding towards zero). For a different behavior consider passing the result of [Vector2.ceil()](class_vector2.md#class-vector2-method-ceil), [Vector2.floor()](class_vector2.md#class-vector2-method-floor) or [Vector2.round()](class_vector2.md#class-vector2-method-round) to this constructor instead.

---

Vector2i **Vector2i**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int))

Constructs a new **Vector2i** from the given `x` and `y`.

---

## Method Descriptions

Vector2i **abs**()

Returns a new vector with all components in absolute values (i.e. positive).

---

[float](class_float.md#class-float) **aspect**()

Returns the aspect ratio of this vector, the ratio of x to y.

---

Vector2i **clamp**(min: Vector2i, max: Vector2i)

Returns a new vector with all components clamped between the components of `min` and `max`, by running [@GlobalScope.clamp()](class_@globalscope.md#class-globalscope-method-clamp) on each component.

---

Vector2i **clampi**(min: [int](class_int.md#class-int), max: [int](class_int.md#class-int))

Returns a new vector with all components clamped between `min` and `max`, by running [@GlobalScope.clamp()](class_@globalscope.md#class-globalscope-method-clamp) on each component.

---

[int](class_int.md#class-int) **distance_squared_to**(to: Vector2i)

Returns the squared [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between this vector and `to`.

This method runs faster than distance_to(), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

[float](class_float.md#class-float) **distance_to**(to: Vector2i)

Returns the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between this vector and `to`.

---

[float](class_float.md#class-float) **length**()

Returns the length (magnitude) of this vector.

---

[int](class_int.md#class-int) **length_squared**()

Returns the squared length (squared magnitude) of this vector.

This method runs faster than length(), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

Vector2i **max**(with: Vector2i)

Returns the component-wise maximum of this and `with`, equivalent to `Vector2i(maxi(x, with.x), maxi(y, with.y))`.

---

[int](class_int.md#class-int) **max_axis_index**()

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns AXIS_X.

---

Vector2i **maxi**(with: [int](class_int.md#class-int))

Returns the component-wise maximum of this and `with`, equivalent to `Vector2i(maxi(x, with), maxi(y, with))`.

---

Vector2i **min**(with: Vector2i)

Returns the component-wise minimum of this and `with`, equivalent to `Vector2i(mini(x, with.x), mini(y, with.y))`.

---

[int](class_int.md#class-int) **min_axis_index**()

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns AXIS_Y.

---

Vector2i **mini**(with: [int](class_int.md#class-int))

Returns the component-wise minimum of this and `with`, equivalent to `Vector2i(mini(x, with), mini(y, with))`.

---

Vector2i **sign**()

Returns a new vector with each component set to `1` if it's positive, `-1` if it's negative, and `0` if it's zero. The result is identical to calling [@GlobalScope.sign()](class_@globalscope.md#class-globalscope-method-sign) on each component.

---

Vector2i **snapped**(step: Vector2i)

Returns a new vector with each component snapped to the closest multiple of the corresponding component in `step`.

---

Vector2i **snappedi**(step: [int](class_int.md#class-int))

Returns a new vector with each component snapped to the closest multiple of `step`.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: Vector2i)

Returns `true` if the vectors are not equal.

---

Vector2i **operator %**(right: Vector2i)

Gets the remainder of each component of the **Vector2i** with the components of the given **Vector2i**. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using [@GlobalScope.posmod()](class_@globalscope.md#class-globalscope-method-posmod) instead if you want to handle negative numbers.

```gdscript
print(Vector2i(10, -20) % Vector2i(7, 8)) # Prints (3, -4)
```

---

Vector2i **operator %**(right: [int](class_int.md#class-int))

Gets the remainder of each component of the **Vector2i** with the given [int](class_int.md#class-int). This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using [@GlobalScope.posmod()](class_@globalscope.md#class-globalscope-method-posmod) instead if you want to handle negative numbers.

```gdscript
print(Vector2i(10, -20) % 7) # Prints (3, -6)
```

---

Vector2i **operator \***(right: Vector2i)

Multiplies each component of the **Vector2i** by the components of the given **Vector2i**.

```gdscript
print(Vector2i(10, 20) * Vector2i(3, 4)) # Prints (30, 80)
```

---

[Vector2](class_vector2.md#class-vector2) **operator \***(right: [float](class_float.md#class-float))

Multiplies each component of the **Vector2i** by the given [float](class_float.md#class-float). Returns a [Vector2](class_vector2.md#class-vector2).

```gdscript
print(Vector2i(10, 15) * 0.9) # Prints (9.0, 13.5)
```

---

Vector2i **operator \***(right: [int](class_int.md#class-int))

Multiplies each component of the **Vector2i** by the given [int](class_int.md#class-int).

---

Vector2i **operator +**(right: Vector2i)

Adds each component of the **Vector2i** by the components of the given **Vector2i**.

```gdscript
print(Vector2i(10, 20) + Vector2i(3, 4)) # Prints (13, 24)
```

---

Vector2i **operator -**(right: Vector2i)

Subtracts each component of the **Vector2i** by the components of the given **Vector2i**.

```gdscript
print(Vector2i(10, 20) - Vector2i(3, 4)) # Prints (7, 16)
```

---

Vector2i **operator /**(right: Vector2i)

Divides each component of the **Vector2i** by the components of the given **Vector2i**.

```gdscript
print(Vector2i(10, 20) / Vector2i(2, 5)) # Prints (5, 4)
```

---

[Vector2](class_vector2.md#class-vector2) **operator /**(right: [float](class_float.md#class-float))

Divides each component of the **Vector2i** by the given [float](class_float.md#class-float). Returns a [Vector2](class_vector2.md#class-vector2).

```gdscript
print(Vector2i(1, 2) / 2.5) # Prints (0.4, 0.8)
```

---

Vector2i **operator /**(right: [int](class_int.md#class-int))

Divides each component of the **Vector2i** by the given [int](class_int.md#class-int).

---

[bool](class_bool.md#class-bool) **operator <**(right: Vector2i)

Compares two **Vector2i** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

---

[bool](class_bool.md#class-bool) **operator <=**(right: Vector2i)

Compares two **Vector2i** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

---

[bool](class_bool.md#class-bool) **operator ==**(right: Vector2i)

Returns `true` if the vectors are equal.

---

[bool](class_bool.md#class-bool) **operator >**(right: Vector2i)

Compares two **Vector2i** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

---

[bool](class_bool.md#class-bool) **operator >=**(right: Vector2i)

Compares two **Vector2i** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

---

[int](class_int.md#class-int) **operator []**(index: [int](class_int.md#class-int))

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, and `v[1]` is equivalent to `v.y`.

---

Vector2i **operator unary+**()

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

Vector2i **operator unary-**()

Returns the negative value of the **Vector2i**. This is the same as writing `Vector2i(-v.x, -v.y)`. This operation flips the direction of the vector while keeping the same magnitude.
