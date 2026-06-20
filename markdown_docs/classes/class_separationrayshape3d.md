# SeparationRayShape3D

**Inherits:** [Shape3D](class_shape3d.md#class-shape3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 3D ray shape used for physics collision that tries to separate itself from any collider.

## Description

A 3D ray shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d). When a **SeparationRayShape3D** collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a **SeparationRayShape3D** next to a character can allow it to instantly move up when touching stairs.

## Properties

| [float](class_float.md#class-float)   | length                 | `1.0`   |
|---------------------------------------|-----------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)      | slide_on_slope | `false` |

---

## Property Descriptions

[float](class_float.md#class-float) **length** = `1.0`

-  **set_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_length**()

The ray's length.

---

[bool](class_bool.md#class-bool) **slide_on_slope** = `false`

-  **set_slide_on_slope**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_slide_on_slope**()

If `false` (default), the shape always separates and returns a normal along its own direction.

If `true`, the shape can return the correct normal and separate in any direction, allowing sliding motion on slopes.
