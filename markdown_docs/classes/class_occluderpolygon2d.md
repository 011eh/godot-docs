# OccluderPolygon2D

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Defines a 2D polygon for LightOccluder2D.

## Description

Editor facility that helps you draw a 2D polygon used as resource for [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d).

## Properties

| [bool](class_bool.md#class-bool)                                           | closed       | `true`                 |
|----------------------------------------------------------------------------|----------------------------------------------------------|------------------------|
| CullMode                               | cull_mode | `0`                    |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | polygon     | `PackedVector2Array()` |

---

## Enumerations

enum **CullMode**:

CullMode **CULL_DISABLED** = `0`

Culling is disabled. See cull_mode.

CullMode **CULL_CLOCKWISE** = `1`

Culling is performed in the clockwise direction. See cull_mode.

CullMode **CULL_COUNTER_CLOCKWISE** = `2`

Culling is performed in the counterclockwise direction. See cull_mode.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **closed** = `true`

-  **set_closed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_closed**()

If `true`, closes the polygon. A closed OccluderPolygon2D occludes the light coming from any direction. An opened OccluderPolygon2D occludes the light only at its outline's direction.

---

CullMode **cull_mode** = `0`

-  **set_cull_mode**(value: CullMode)
- CullMode **get_cull_mode**()

The culling mode to use.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **polygon** = `PackedVector2Array()`

-  **set_polygon**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_polygon**()

A [Vector2](class_vector2.md#class-vector2) array with the index for polygon's vertices positions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.
