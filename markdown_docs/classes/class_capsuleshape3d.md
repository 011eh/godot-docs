# CapsuleShape3D

**Inherits:** [Shape3D](class_shape3d.md#class-shape3d) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A 3D capsule shape used for physics collision.

## Description

A 3D capsule shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d).

**Performance:** **CapsuleShape3D** is fast to check collisions against. It is faster than [CylinderShape3D](class_cylindershape3d.md#class-cylindershape3d), but slower than [SphereShape3D](class_sphereshape3d.md#class-sphereshape3d) and [BoxShape3D](class_boxshape3d.md#class-boxshape3d).

## Tutorials

- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)

## Properties

| [float](class_float.md#class-float)   | height         | `2.0`   |
|---------------------------------------|---------------------------------------------------------|---------|
| [float](class_float.md#class-float)   | mid_height |         |
| [float](class_float.md#class-float)   | radius         | `0.5`   |

---

## Property Descriptions

[float](class_float.md#class-float) **height** = `2.0`

-  **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The capsule's full height, including the hemispheres.

**Note:** The height of a capsule must be at least twice its radius. Otherwise, the capsule becomes a sphere. If the height is less than twice the radius, the properties adjust to a valid value.

---

[float](class_float.md#class-float) **mid_height**

-  **set_mid_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mid_height**()

The capsule's height, excluding the hemispheres. This is the height of the central cylindrical part in the middle of the capsule, and is the distance between the centers of the two hemispheres. This is a wrapper for height.

---

[float](class_float.md#class-float) **radius** = `0.5`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The capsule's radius.

**Note:** The radius of a capsule cannot be greater than half of its height. Otherwise, the capsule becomes a sphere. If the radius is greater than half of the height, the properties adjust to a valid value.
