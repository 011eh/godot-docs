# PhysicsServer3DRenderingServerHandler

**Inherits:** [Object](class_object.md#class-object)

A class used to provide [PhysicsServer3DExtension._soft_body_update_rendering_server()](class_physicsserver3dextension.md#class-physicsserver3dextension-private-method-soft-body-update-rendering-server) with a rendering handler for soft bodies.

## Methods

|    | \_set_aabb(aabb: [AABB](class_aabb.md#class-aabb))                                                          |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | \_set_normal(vertex_id: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3)) |
|    | \_set_vertex(vertex_id: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3)) |
|    | set_aabb(aabb: [AABB](class_aabb.md#class-aabb))                                                                    |
|    | set_normal(vertex_id: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3))           |
|    | set_vertex(vertex_id: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3))           |

---

## Method Descriptions

 **\_set_aabb**(aabb: [AABB](class_aabb.md#class-aabb))

Called by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) to set the bounding box for the [SoftBody3D](class_softbody3d.md#class-softbody3d).

---

 **\_set_normal**(vertex_id: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3))

Called by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) to set the normal for the [SoftBody3D](class_softbody3d.md#class-softbody3d) vertex at the index specified by `vertex_id`.

**Note:** The `normal` parameter used to be of type `const void*` prior to Godot 4.2.

---

 **\_set_vertex**(vertex_id: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3))

Called by the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) to set the position for the [SoftBody3D](class_softbody3d.md#class-softbody3d) vertex at the index specified by `vertex_id`.

**Note:** The `vertex` parameter used to be of type `const void*` prior to Godot 4.2.

---

 **set_aabb**(aabb: [AABB](class_aabb.md#class-aabb))

Sets the bounding box for the [SoftBody3D](class_softbody3d.md#class-softbody3d).

---

 **set_normal**(vertex_id: [int](class_int.md#class-int), normal: [Vector3](class_vector3.md#class-vector3))

Sets the normal for the [SoftBody3D](class_softbody3d.md#class-softbody3d) vertex at the index specified by `vertex_id`.

---

 **set_vertex**(vertex_id: [int](class_int.md#class-int), vertex: [Vector3](class_vector3.md#class-vector3))

Sets the position for the [SoftBody3D](class_softbody3d.md#class-softbody3d) vertex at the index specified by `vertex_id`.
