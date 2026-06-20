# int

A built-in type for integers.

## Description

Signed 64-bit integer type. This means that it can take values from `-2^63` to `2^63 - 1`, i.e. from `-9223372036854775808` to `9223372036854775807`. When it exceeds these bounds, it will wrap around.

**int**s can be automatically converted to [float](class_float.md#class-float)s when necessary, for example when passing them as arguments in functions. The [float](class_float.md#class-float) will be as close to the original integer as possible.

Likewise, [float](class_float.md#class-float)s can be automatically converted into **int**s. This will truncate the [float](class_float.md#class-float), discarding anything after the floating-point.

**Note:** In a boolean context, an **int** will evaluate to `false` if it equals `0`, and to `true` otherwise.

GDScript

```gdscript
var x: int = 1 # x is 1
x = 4.2 # x is 4, because 4.2 gets truncated
var max_int = 9223372036854775807 # Biggest value an int can store
max_int += 1 # max_int is -9223372036854775808, because it wrapped around
```

C#

```csharp
int x = 1; // x is 1
x = (int)4.2; // x is 4, because 4.2 gets truncated
// We use long below, because GDScript's int is 64-bit while C#'s int is 32-bit.
long maxLong = 9223372036854775807; // Biggest value a long can store
maxLong++; // maxLong is now -9223372036854775808, because it wrapped around.

// Alternatively with C#'s 32-bit int type, which has a smaller maximum value.
int maxInt = 2147483647; // Biggest value an int can store
maxInt++; // maxInt is now -2147483648, because it wrapped around
```

You can use the `0b` literal for binary representation, the `0x` literal for hexadecimal representation, and the `_` symbol to separate long numbers and improve readability.

GDScript

```gdscript
var x = 0b1001 # x is 9
var y = 0xF5 # y is 245
var z = 10_000_000 # z is 10000000
```

C#

```csharp
int x = 0b1001; // x is 9
int y = 0xF5; // y is 245
int z = 10_000_000; // z is 10000000
```

## Constructors

| int   | int()                                             |
|---------------------|---------------------------------------------------------------------------------|
| int   | int(from: int)                      |
| int   | int(from: [String](class_string.md#class-string)) |
| int   | int(from: [bool](class_bool.md#class-bool))       |
| int   | int(from: [float](class_float.md#class-float))    |

## Operators

| [bool](class_bool.md#class-bool)                   | operator !=(right: [float](class_float.md#class-float))                     |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                   | operator !=(right: int)                                         |
| int                                  | operator %(right: int)                                          |
| int                                  | operator &(right: int)                                        |
| [Color](class_color.md#class-color)                | operator \*(right: [Color](class_color.md#class-color))                     |
| [Quaternion](class_quaternion.md#class-quaternion) | operator \*(right: [Quaternion](class_quaternion.md#class-quaternion)) |
| [Vector2](class_vector2.md#class-vector2)          | operator \*(right: [Vector2](class_vector2.md#class-vector2))             |
| [Vector2i](class_vector2i.md#class-vector2i)       | operator \*(right: [Vector2i](class_vector2i.md#class-vector2i))         |
| [Vector3](class_vector3.md#class-vector3)          | operator \*(right: [Vector3](class_vector3.md#class-vector3))             |
| [Vector3i](class_vector3i.md#class-vector3i)       | operator \*(right: [Vector3i](class_vector3i.md#class-vector3i))         |
| [Vector4](class_vector4.md#class-vector4)          | operator \*(right: [Vector4](class_vector4.md#class-vector4))             |
| [Vector4i](class_vector4i.md#class-vector4i)       | operator \*(right: [Vector4i](class_vector4i.md#class-vector4i))         |
| [float](class_float.md#class-float)                | operator \*(right: [float](class_float.md#class-float))                     |
| int                                  | operator \*(right: int)                                         |
| [float](class_float.md#class-float)                | operator \*\*(right: [float](class_float.md#class-float))                   |
| int                                  | operator \*\*(right: int)                                       |
| [float](class_float.md#class-float)                | operator +(right: [float](class_float.md#class-float))                      |
| int                                  | operator +(right: int)                                          |
| [float](class_float.md#class-float)                | operator -(right: [float](class_float.md#class-float))                      |
| int                                  | operator -(right: int)                                          |
| [float](class_float.md#class-float)                | operator /(right: [float](class_float.md#class-float))                      |
| int                                  | operator /(right: int)                                          |
| [bool](class_bool.md#class-bool)                   | operator <(right: [float](class_float.md#class-float))                       |
| [bool](class_bool.md#class-bool)                   | operator <(right: int)                                           |
| int                                  | operator <<(right: int)                                        |
| [bool](class_bool.md#class-bool)                   | operator <=(right: [float](class_float.md#class-float))                     |
| [bool](class_bool.md#class-bool)                   | operator <=(right: int)                                         |
| [bool](class_bool.md#class-bool)                   | operator ==(right: [float](class_float.md#class-float))                      |
| [bool](class_bool.md#class-bool)                   | operator ==(right: int)                                          |
| [bool](class_bool.md#class-bool)                   | operator >(right: [float](class_float.md#class-float))                       |
| [bool](class_bool.md#class-bool)                   | operator >(right: int)                                           |
| [bool](class_bool.md#class-bool)                   | operator >=(right: [float](class_float.md#class-float))                     |
| [bool](class_bool.md#class-bool)                   | operator >=(right: int)                                         |
| int                                  | operator >>(right: int)                                        |
| int                                  | operator ^(right: int)                                        |
| int                                  | operator unary+()                                                              |
| int                                  | operator unary-()                                                             |
| int                                  | operator |(right: int)                                         |
| int                                  | operator ~()                                                                    |

---

## Constructor Descriptions

int **int**()

Constructs an **int** set to `0`.

---

int **int**(from: int)

Constructs an **int** as a copy of the given **int**.

---

int **int**(from: [String](class_string.md#class-string))

Constructs a new **int** from a [String](class_string.md#class-string), following the same rules as [String.to_int()](class_string.md#class-string-method-to-int).

---

int **int**(from: [bool](class_bool.md#class-bool))

Constructs a new **int** from a [bool](class_bool.md#class-bool). `true` is converted to `1` and `false` is converted to `0`.

---

int **int**(from: [float](class_float.md#class-float))

Constructs a new **int** from a [float](class_float.md#class-float). This will truncate the [float](class_float.md#class-float), discarding anything after the floating point.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: [float](class_float.md#class-float))

Returns `true` if the **int** is not equivalent to the [float](class_float.md#class-float).

---

[bool](class_bool.md#class-bool) **operator !=**(right: int)

Returns `true` if the **int**s are not equal.

---

int **operator %**(right: int)

Returns the remainder after dividing two **int**s. Uses truncated division, which returns a negative number if the dividend is negative. If this is not desired, consider using [@GlobalScope.posmod()](class_@globalscope.md#class-globalscope-method-posmod).

```gdscript
print(6 % 2) # Prints 0
print(11 % 4) # Prints 3
print(-5 % 3) # Prints -2
```

---

int **operator &**(right: int)

Performs the bitwise `AND` operation.

```gdscript
print(0b1100 & 0b1010) # Prints 8 (binary 1000)
```

This is useful for retrieving binary flags from a variable.

```gdscript
var flags = 0b101
# Check if the first or second bit are enabled.
if flags & 0b011:
    do_stuff() # This line will run.
```

---

[Color](class_color.md#class-color) **operator \***(right: [Color](class_color.md#class-color))

Multiplies each component of the [Color](class_color.md#class-color) by the **int**.

---

[Quaternion](class_quaternion.md#class-quaternion) **operator \***(right: [Quaternion](class_quaternion.md#class-quaternion))

Multiplies each component of the [Quaternion](class_quaternion.md#class-quaternion) by the **int**. This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---

[Vector2](class_vector2.md#class-vector2) **operator \***(right: [Vector2](class_vector2.md#class-vector2))

Multiplies each component of the [Vector2](class_vector2.md#class-vector2) by the **int**.

```gdscript
print(2 * Vector2(1, 4)) # Prints (2, 8)
```

---

[Vector2i](class_vector2i.md#class-vector2i) **operator \***(right: [Vector2i](class_vector2i.md#class-vector2i))

Multiplies each component of the [Vector2i](class_vector2i.md#class-vector2i) by the **int**.

---

[Vector3](class_vector3.md#class-vector3) **operator \***(right: [Vector3](class_vector3.md#class-vector3))

Multiplies each component of the [Vector3](class_vector3.md#class-vector3) by the **int**.

---

[Vector3i](class_vector3i.md#class-vector3i) **operator \***(right: [Vector3i](class_vector3i.md#class-vector3i))

Multiplies each component of the [Vector3i](class_vector3i.md#class-vector3i) by the **int**.

---

[Vector4](class_vector4.md#class-vector4) **operator \***(right: [Vector4](class_vector4.md#class-vector4))

Multiplies each component of the [Vector4](class_vector4.md#class-vector4) by the **int**.

---

[Vector4i](class_vector4i.md#class-vector4i) **operator \***(right: [Vector4i](class_vector4i.md#class-vector4i))

Multiplies each component of the [Vector4i](class_vector4i.md#class-vector4i) by the **int**.

---

[float](class_float.md#class-float) **operator \***(right: [float](class_float.md#class-float))

Multiplies the [float](class_float.md#class-float) by the **int**. The result is a [float](class_float.md#class-float).

---

int **operator \***(right: int)

Multiplies the two **int**s.

---

[float](class_float.md#class-float) **operator \*\***(right: [float](class_float.md#class-float))

Raises an **int** to a power of a [float](class_float.md#class-float). The result is a [float](class_float.md#class-float).

```gdscript
print(2 ** 0.5) # Prints 1.4142135623731
```

---

int **operator \*\***(right: int)

Raises the left **int** to a power of the right **int**.

```gdscript
print(3 ** 4) # Prints 81
```

---

[float](class_float.md#class-float) **operator +**(right: [float](class_float.md#class-float))

Adds the **int** and the [float](class_float.md#class-float). The result is a [float](class_float.md#class-float).

---

int **operator +**(right: int)

Adds the two **int**s.

---

[float](class_float.md#class-float) **operator -**(right: [float](class_float.md#class-float))

Subtracts the [float](class_float.md#class-float) from the **int**. The result is a [float](class_float.md#class-float).

---

int **operator -**(right: int)

Subtracts the two **int**s.

---

[float](class_float.md#class-float) **operator /**(right: [float](class_float.md#class-float))

Divides the **int** by the [float](class_float.md#class-float). The result is a [float](class_float.md#class-float).

```gdscript
print(10 / 3.0) # Prints 3.33333333333333
```

---

int **operator /**(right: int)

Divides the two **int**s. The result is an **int**. This will truncate the [float](class_float.md#class-float), discarding anything after the floating point.

```gdscript
print(6 / 2) # Prints 3
print(5 / 3) # Prints 1
```

---

[bool](class_bool.md#class-bool) **operator <**(right: [float](class_float.md#class-float))

Returns `true` if the **int** is less than the [float](class_float.md#class-float).

---

[bool](class_bool.md#class-bool) **operator <**(right: int)

Returns `true` if the left **int** is less than the right **int**.

---

int **operator <<**(right: int)

Performs the bitwise shift left operation. Effectively the same as multiplying by a power of 2.

```gdscript
print(0b1010 << 1) # Prints 20 (binary 10100)
print(0b1010 << 3) # Prints 80 (binary 1010000)
```

---

[bool](class_bool.md#class-bool) **operator <=**(right: [float](class_float.md#class-float))

Returns `true` if the **int** is less than or equal to the [float](class_float.md#class-float).

---

[bool](class_bool.md#class-bool) **operator <=**(right: int)

Returns `true` if the left **int** is less than or equal to the right **int**.

---

[bool](class_bool.md#class-bool) **operator ==**(right: [float](class_float.md#class-float))

Returns `true` if the **int** is equal to the [float](class_float.md#class-float).

---

[bool](class_bool.md#class-bool) **operator ==**(right: int)

Returns `true` if the two **int**s are equal.

---

[bool](class_bool.md#class-bool) **operator >**(right: [float](class_float.md#class-float))

Returns `true` if the **int** is greater than the [float](class_float.md#class-float).

---

[bool](class_bool.md#class-bool) **operator >**(right: int)

Returns `true` if the left **int** is greater than the right **int**.

---

[bool](class_bool.md#class-bool) **operator >=**(right: [float](class_float.md#class-float))

Returns `true` if the **int** is greater than or equal to the [float](class_float.md#class-float).

---

[bool](class_bool.md#class-bool) **operator >=**(right: int)

Returns `true` if the left **int** is greater than or equal to the right **int**.

---

int **operator >>**(right: int)

Performs the bitwise shift right operation. Effectively the same as dividing by a power of 2.

```gdscript
print(0b1010 >> 1) # Prints 5 (binary 101)
print(0b1010 >> 2) # Prints 2 (binary 10)
```

---

int **operator ^**(right: int)

Performs the bitwise `XOR` operation.

```gdscript
print(0b1100 ^ 0b1010) # Prints 6 (binary 110)
```

---

int **operator unary+**()

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

int **operator unary-**()

Returns the negated value of the **int**. If positive, turns the number negative. If negative, turns the number positive. If zero, does nothing.

---

int **operator |**(right: int)

Performs the bitwise `OR` operation.

```gdscript
print(0b1100 | 0b1010) # Prints 14 (binary 1110)
```

This is useful for storing binary flags in a variable.

```gdscript
var flags = 0
flags |= 0b101 # Turn the first and third bits on.
```

---

int **operator ~**()

Performs the bitwise `NOT` operation on the **int**. Due to [2's complement](https://en.wikipedia.org/wiki/Two%27s_complement), it's effectively equal to `-(int + 1)`.

```gdscript
print(~4) # Prints -5
print(~(-7)) # Prints 6
```
