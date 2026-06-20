# RectangleShape2D

**Inherits:** [Shape2D](class_shape2d.md#class-shape2d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 2D rectangle shape used for physics collision.

## Description

A 2D rectangle shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d).

**Performance:** **RectangleShape2D** is fast to check collisions against. It is faster than [CapsuleShape2D](class_capsuleshape2d.md#class-capsuleshape2d), but slower than [CircleShape2D](class_circleshape2d.md#class-circleshape2d).

## Tutorials

- [2D Pong Demo](https://godotengine.org/asset-library/asset/2728)
- [2D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2719)

## Properties

| [Vector2](class_vector2.md#class-vector2)   | size   | `Vector2(20, 20)`   |
|---------------------------------------------|-------------------------------------------------|---------------------|

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **size** = `Vector2(20, 20)`

-  **set_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_size**()

The rectangle's width and height.
