# CapsuleShape2D

**Inherits:** [Shape2D](class_shape2d.md#class-shape2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D capsule shape used for physics collision.

## Description

A 2D capsule shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d).

**Performance:** **CapsuleShape2D** is fast to check collisions against, but it is slower than [RectangleShape2D](class_rectangleshape2d.md#class-rectangleshape2d) and [CircleShape2D](class_circleshape2d.md#class-circleshape2d).

## Properties

| [float](class_float.md#class-float)   | height         | `30.0`   |
|---------------------------------------|---------------------------------------------------------|----------|
| [float](class_float.md#class-float)   | mid_height |          |
| [float](class_float.md#class-float)   | radius         | `10.0`   |

---

## Property Descriptions

[float](class_float.md#class-float) **height** = `30.0`

-  **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The capsule's full height, including the semicircles.

**Note:** The height of a capsule must be at least twice its radius. Otherwise, the capsule becomes a circle. If the height is less than twice the radius, the properties adjust to a valid value.

---

[float](class_float.md#class-float) **mid_height**

-  **set_mid_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mid_height**()

The capsule's height, excluding the semicircles. This is the height of the central rectangular part in the middle of the capsule, and is the distance between the centers of the two semicircles. This is a wrapper for height.

---

[float](class_float.md#class-float) **radius** = `10.0`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The capsule's radius.

**Note:** The radius of a capsule cannot be greater than half of its height. Otherwise, the capsule becomes a circle. If the radius is greater than half of the height, the properties adjust to a valid value.
