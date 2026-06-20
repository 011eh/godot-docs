# PhysicsMaterial

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Holds physics-related properties of a surface, namely its roughness and bounciness.

## Description

Holds physics-related properties of a surface, namely its roughness and bounciness. This class is used to apply these properties to a physics body.

## Properties

| [bool](class_bool.md#class-bool)    | absorbent   | `false`   |
|-------------------------------------|----------------------------------------------------------|-----------|
| [float](class_float.md#class-float) | bounce         | `0.0`     |
| [float](class_float.md#class-float) | friction     | `1.0`     |
| [bool](class_bool.md#class-bool)    | rough           | `false`   |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **absorbent** = `false`

-  **set_absorbent**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_absorbent**()

If `true`, subtracts the bounciness from the colliding object's bounciness instead of adding it.

---

[float](class_float.md#class-float) **bounce** = `0.0`

-  **set_bounce**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bounce**()

The body's bounciness. Values range from `0` (no bounce) to `1` (full bounciness).

**Note:** Even with bounce set to `1.0`, some energy will be lost over time due to linear and angular damping. To have a physics body that preserves all its energy over time, set bounce to `1.0`, the body's linear damp mode to **Replace** (if applicable), its linear damp to `0.0`, its angular damp mode to **Replace** (if applicable), and its angular damp to `0.0`.

---

[float](class_float.md#class-float) **friction** = `1.0`

-  **set_friction**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_friction**()

The body's friction. Values range from `0` (frictionless) to `1` (maximum friction).

---

[bool](class_bool.md#class-bool) **rough** = `false`

-  **set_rough**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_rough**()

If `true`, the physics engine will use the friction of the object marked as "rough" when two objects collide. If `false`, the physics engine will use the lowest friction of all colliding objects instead. If `true` for both colliding objects, the physics engine will use the highest friction.
