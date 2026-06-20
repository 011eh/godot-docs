# SpringBoneCollision3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [SpringBoneCollisionCapsule3D](class_springbonecollisioncapsule3d.md#class-springbonecollisioncapsule3d), [SpringBoneCollisionPlane3D](class_springbonecollisionplane3d.md#class-springbonecollisionplane3d), [SpringBoneCollisionSphere3D](class_springbonecollisionsphere3d.md#class-springbonecollisionsphere3d)

A base class of the collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d).

## Description

A collision can be a child of [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d). If it is not a child of [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d), it has no effect.

The colliding and sliding are done in the [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d)'s modification process in order of its collision list which is set by [SpringBoneSimulator3D.set_collision_path()](class_springbonesimulator3d.md#class-springbonesimulator3d-method-set-collision-path). If [SpringBoneSimulator3D.are_all_child_collisions_enabled()](class_springbonesimulator3d.md#class-springbonesimulator3d-method-are-all-child-collisions-enabled) is `true`, the order matches [SceneTree](class_scenetree.md#class-scenetree).

If bone is set, it synchronizes with the bone pose of the ancestor [Skeleton3D](class_skeleton3d.md#class-skeleton3d), which is done in before the [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d)'s modification process as the pre-process.

**Warning:** A scaled **SpringBoneCollision3D** will likely not behave as expected. Make sure that the parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) and its bones are not scaled.

## Properties

| [int](class_int.md#class-int)                      | bone                       | `-1`   |
|----------------------------------------------------|--------------------------------------------------------------------------|--------|
| [String](class_string.md#class-string)             | bone_name             | `""`   |
| [Vector3](class_vector3.md#class-vector3)          | position_offset |        |
| [Quaternion](class_quaternion.md#class-quaternion) | rotation_offset |        |

## Methods

| [Skeleton3D](class_skeleton3d.md#class-skeleton3d)   | get_skeleton()    |
|------------------------------------------------------|-----------------------------------------------------------------------|

---

## Property Descriptions

[int](class_int.md#class-int) **bone** = `-1`

-  **set_bone**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone**()

The index of the attached bone.

---

[String](class_string.md#class-string) **bone_name** = `""`

-  **set_bone_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_bone_name**()

The name of the attached bone.

---

[Vector3](class_vector3.md#class-vector3) **position_offset**

-  **set_position_offset**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_position_offset**()

The offset of the position from [Skeleton3D](class_skeleton3d.md#class-skeleton3d)'s bone pose position.

---

[Quaternion](class_quaternion.md#class-quaternion) **rotation_offset**

-  **set_rotation_offset**(value: [Quaternion](class_quaternion.md#class-quaternion))
- [Quaternion](class_quaternion.md#class-quaternion) **get_rotation_offset**()

The offset of the rotation from [Skeleton3D](class_skeleton3d.md#class-skeleton3d)'s bone pose rotation.

---

## Method Descriptions

[Skeleton3D](class_skeleton3d.md#class-skeleton3d) **get_skeleton**()

Get parent [Skeleton3D](class_skeleton3d.md#class-skeleton3d) node of the parent [SpringBoneSimulator3D](class_springbonesimulator3d.md#class-springbonesimulator3d) if found.
