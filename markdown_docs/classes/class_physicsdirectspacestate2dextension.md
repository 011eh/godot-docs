# PhysicsDirectSpaceState2DExtension

**Inherits:** [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) implementations.

## Description

This class extends [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d).

## Methods

| [bool](class_bool.md#class-bool)   | \_cast_motion(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_closest_safe: `float*`, r_closest_unsafe: `float*`)                                                 |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)   | \_collide_shape(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `void*`, max_results: [int](class_int.md#class-int), r_result_count: `int32_t*`)       |
| [int](class_int.md#class-int)      | \_intersect_point(position: [Vector2](class_vector2.md#class-vector2), canvas_instance_id: [int](class_int.md#class-int), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class-int))                                                                                                    |
| [bool](class_bool.md#class-bool)   | \_intersect_ray(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), hit_from_inside: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionRayResult*`)                                                                                                            |
| [int](class_int.md#class-int)      | \_intersect_shape(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool)   | \_rest_info(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_rest_info: `PhysicsServer2DExtensionShapeRestInfo*`)                                                    |
| [bool](class_bool.md#class-bool)   | is_body_excluded_from_query(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **\_cast_motion**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_closest_safe: `float*`, r_closest_unsafe: `float*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_collide_shape**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `void*`, max_results: [int](class_int.md#class-int), r_result_count: `int32_t*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_intersect_point**(position: [Vector2](class_vector2.md#class-vector2), canvas_instance_id: [int](class_int.md#class-int), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_results: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_intersect_ray**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), hit_from_inside: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionRayResult*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_intersect_shape**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_rest_info**(shape_rid: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collision_mask: [int](class_int.md#class-int), collide_with_bodies: [bool](class_bool.md#class-bool), collide_with_areas: [bool](class_bool.md#class-bool), r_rest_info: `PhysicsServer2DExtensionShapeRestInfo*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **is_body_excluded_from_query**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
