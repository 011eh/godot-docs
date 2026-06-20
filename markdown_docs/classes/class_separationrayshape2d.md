# SeparationRayShape2D

**Inherits:** [Shape2D](class_shape2d.md#class-shape2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D ray shape used for physics collision that tries to separate itself from any collider.

## Description

A 2D ray shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d). When a **SeparationRayShape2D** collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a **SeparationRayShape2D** next to a character can allow it to instantly move up when touching stairs.

## Properties

| [float](class_float.md#class-float)   | length                 | `20.0`   |
|---------------------------------------|-----------------------------------------------------------------------|----------|
| [bool](class_bool.md#class-bool)      | slide_on_slope | `false`  |

---

## Property Descriptions

[float](class_float.md#class-float) **length** = `20.0`

-  **set_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_length**()

The ray's length.

---

[bool](class_bool.md#class-bool) **slide_on_slope** = `false`

-  **set_slide_on_slope**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_slide_on_slope**()

If `false` (default), the shape always separates and returns a normal along its own direction.

If `true`, the shape can return the correct normal and separate in any direction, allowing sliding motion on slopes.
