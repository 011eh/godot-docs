# SpringBoneCollisionCapsule3D

**Inherits:** [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A capsule shape collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d).

## Description

A capsule shape collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d).

## Properties

| [float](class_float.md#class-float)   | height         | `0.5`   |
|---------------------------------------|-----------------------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)      | inside         | `false` |
| [float](class_float.md#class-float)   | mid_height |         |
| [float](class_float.md#class-float)   | radius         | `0.1`   |

---

## Property Descriptions

[float](class_float.md#class-float) **height** = `0.5`

-  **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The capsule's full height, including the hemispheres.

**Note:** The height of a capsule must be at least twice its radius. Otherwise, the capsule becomes a sphere. If the height is less than twice the radius, the properties adjust to a valid value.

---

[bool](class_bool.md#class-bool) **inside** = `false`

-  **set_inside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_inside**()

If `true`, the collision acts to trap the joint within the collision.

---

[float](class_float.md#class-float) **mid_height**

-  **set_mid_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_mid_height**()

The capsule's height, excluding the hemispheres. This is the height of the central cylindrical part in the middle of the capsule, and is the distance between the centers of the two hemispheres. This is a wrapper for height.

---

[float](class_float.md#class-float) **radius** = `0.1`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The capsule's radius.

**Note:** The radius of a capsule cannot be greater than half of its height. Otherwise, the capsule becomes a sphere. If the radius is greater than half of the height, the properties adjust to a valid value.
