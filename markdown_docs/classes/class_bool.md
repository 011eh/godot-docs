# bool

A built-in boolean type.

## Description

The **bool** is a built-in [Variant](class_variant.md#class-variant) type that may only store one of two values: `true` or `false`. You can imagine it as a switch that can be either turned on or off, or as a binary digit that can either be 1 or 0.

Booleans can be directly used in `if`, and other conditional statements:

GDScript

```gdscript
var can_shoot = true
if can_shoot:
    launch_bullet()
```

C#

```csharp
bool canShoot = true;
if (canShoot)
{
    LaunchBullet();
}
```

All comparison operators return booleans (`==`, `>`, `<=`, etc.). As such, it is not necessary to compare booleans themselves. You do not need to add `== true` or `== false`.

Booleans can be combined with the logical operators `and`, `or`, `not` to create complex conditions:

GDScript

```gdscript
if bullets > 0 and not is_reloading():
    launch_bullet()

if bullets == 0 or is_reloading():
    play_clack_sound()
```

C#

```csharp
if (bullets > 0 && !IsReloading())
{
    LaunchBullet();
}

if (bullets == 0 || IsReloading())
{
    PlayClackSound();
}
```

**Note:** In modern programming languages, logical operators are evaluated in order. All remaining conditions are skipped if their result would have no effect on the final value. This concept is known as [short-circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation) and can be useful to avoid evaluating expensive conditions in some performance-critical cases.

**Note:** By convention, built-in methods and properties that return booleans are usually defined as yes-no questions, single adjectives, or similar ([String.is_empty()](class_string.md#class-string-method-is-empty), [Node.can_process()](class_node.md#class-node-method-can-process), [Camera2D.enabled](class_camera2d.md#class-camera2d-property-enabled), etc.).

## Constructors

| bool   | bool()                                          |
|-----------------------|---------------------------------------------------------------------------------|
| bool   | bool(from: bool)                 |
| bool   | bool(from: [float](class_float.md#class-float)) |
| bool   | bool(from: [int](class_int.md#class-int))       |

## Operators

| bool   | operator !=(right: bool)   |
|-----------------------|----------------------------------------------------------------------------|
| bool   | operator <(right: bool)     |
| bool   | operator ==(right: bool)    |
| bool   | operator >(right: bool)     |

---

## Constructor Descriptions

bool **bool**()

Constructs a **bool** set to `false`.

---

bool **bool**(from: bool)

Constructs a **bool** as a copy of the given **bool**.

---

bool **bool**(from: [float](class_float.md#class-float))

Casts a [float](class_float.md#class-float) value to a **bool**. Returns `false` if `from` is equal to `0.0` (including `-0.0`), and `true` for all other values (including [@GDScript.INF](class_@gdscript.md#class-gdscript-constant-inf) and [@GDScript.NAN](class_@gdscript.md#class-gdscript-constant-nan)).

---

bool **bool**(from: [int](class_int.md#class-int))

Casts an [int](class_int.md#class-int) value to a **bool**. Returns `false` if `from` is equal to `0`, and `true` for all other values.

---

## Operator Descriptions

bool **operator !=**(right: bool)

Returns `true` if one **bool** is `true` and the other **bool** is `false`. Equivalent to logical XOR (NEQ).

---

bool **operator <**(right: bool)

Returns `true` if the left **bool** is `false` and `right` is `true`.

---

bool **operator ==**(right: bool)

Returns `true` if both **bool**s are `true`, or if both **bool**s are `false`. Equivalent to logical XNOR (EQ).

---

bool **operator >**(right: bool)

Returns `true` if the left **bool** is `true` and `right` is `false`.
