# TriangleMesh

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Triangle geometry for efficient, physicsless intersection queries.

## Description

Creates a bounding volume hierarchy (BVH) tree structure around triangle geometry.

The triangle BVH tree can be used for efficient intersection queries without involving a physics engine.

For example, this can be used in editor tools to select objects with complex shapes based on the mouse cursor position.

**Performance:** Creating the BVH tree for complex geometry is a slow process and best done in a background thread.

## Methods

| [bool](class_bool.md#class-bool)                                           | create_from_faces(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))                |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | get_faces()                                                                                                                 |
| [Dictionary](class_dictionary.md#class-dictionary)                         | intersect_ray(begin: [Vector3](class_vector3.md#class-vector3), dir: [Vector3](class_vector3.md#class-vector3))         |
| [Dictionary](class_dictionary.md#class-dictionary)                         | intersect_segment(begin: [Vector3](class_vector3.md#class-vector3), end: [Vector3](class_vector3.md#class-vector3)) |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **create_from_faces**(faces: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))

Creates the BVH tree from an array of faces. Each 3 vertices of the input `faces` array represent one triangle (face).

Returns `true` if the tree is successfully built, `false` otherwise.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **get_faces**()

Returns a copy of the geometry faces. Each 3 vertices of the array represent one triangle (face).

---

[Dictionary](class_dictionary.md#class-dictionary) **intersect_ray**(begin: [Vector3](class_vector3.md#class-vector3), dir: [Vector3](class_vector3.md#class-vector3))

Tests for intersection with a ray starting at `begin` and facing `dir` and extending toward infinity.

If an intersection with a triangle happens, returns a [Dictionary](class_dictionary.md#class-dictionary) with the following fields:

`position`: The position on the intersected triangle.

`normal`: The normal of the intersected triangle.

`face_index`: The index of the intersected triangle.

Returns an empty [Dictionary](class_dictionary.md#class-dictionary) if no intersection happens.

See also intersect_segment(), which is similar but uses a finite-length segment.

---

[Dictionary](class_dictionary.md#class-dictionary) **intersect_segment**(begin: [Vector3](class_vector3.md#class-vector3), end: [Vector3](class_vector3.md#class-vector3))

Tests for intersection with a segment going from `begin` to `end`.

If an intersection with a triangle happens returns a [Dictionary](class_dictionary.md#class-dictionary) with the following fields:

`position`: The position on the intersected triangle.

`normal`: The normal of the intersected triangle.

`face_index`: The index of the intersected triangle.

Returns an empty [Dictionary](class_dictionary.md#class-dictionary) if no intersection happens.

See also intersect_ray(), which is similar but uses an infinite-length ray.
