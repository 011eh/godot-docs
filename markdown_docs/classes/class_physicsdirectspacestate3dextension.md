# PhysicsDirectSpaceState3DExtension

**Inherits:** [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) implementations.

## Description

This class extends [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d).

## Methods

| [bool](class_bool.md#class-bool)          | \_cast_motion(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_closest_safe: `float*`, r_closest_unsafe: `float*`, r_info: `PhysicsServer3DExtensionShapeRestInfo*`)     |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)          | \_collide_shape(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `void*`, max_results: [int](class_int.md#class-int), r_result_count: `int32_t*`)             |
| [Vector3](class_vector3.md#class-vector3) | \_get_closest_point_to_object_volume(object: [RID](class_rid.md#class-rid), point: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)             | \_intersect_point(position: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class-int))                                                                                                                                                             |
| [bool](class_bool.md#class-bool)          | \_intersect_ray(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), hit_from_inside: [bool](class_bool.md#class-bool), hit_back_faces: [bool](class_bool.md#class-bool), pick_ray: [bool](class_bool.md#class-bool), r_result: `PhysicsServer3DExtensionRayResult*`)                    |
| [int](class_int.md#class-int)             | \_intersect_shape(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_result_count: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool)          | \_rest_info(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_rest_info: `PhysicsServer3DExtensionShapeRestInfo*`)                                                          |
| [bool](class_bool.md#class-bool)          | is_body_excluded_from_query(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                          |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **\_cast_motion**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_closest_safe: `float*`, r_closest_unsafe: `float*`, r_info: `PhysicsServer3DExtensionShapeRestInfo*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_collide_shape**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `void*`, max_results: [int](class_int.md#class-int), r_result_count: `int32_t*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_get_closest_point_to_object_volume**(object: [RID](class_rid.md#class-rid), point: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_intersect_point**(position: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_intersect_ray**(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), hit_from_inside: [bool](class_bool.md#class-bool), hit_back_faces: [bool](class_bool.md#class-bool), pick_ray: [bool](class_bool.md#class-bool), r_result: `PhysicsServer3DExtensionRayResult*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_intersect_shape**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_result_count: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_rest_info**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_rest_info: `PhysicsServer3DExtensionShapeRestInfo*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **is_body_excluded_from_query**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
