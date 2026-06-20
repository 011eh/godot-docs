# PhysicsServer2DExtension

**Inherits:** [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementations.

## Description

This class extends [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d).

## Methods

|                                                                                                 | \_area_add_shape(area: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                 | \_area_attach_canvas_instance_id(area: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_area_attach_object_instance_id(area: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_area_clear_shapes(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                                                   | \_area_create()                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                                   | \_area_get_canvas_instance_id(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                                   | \_area_get_collision_layer(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                                   | \_area_get_collision_mask(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                                   | \_area_get_object_instance_id(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                     |
| [Variant](class_variant.md#class-variant)                                                       | \_area_get_param(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver2d.md#enum-physicsserver2d-areaparameter))                                                                                                                                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                                                   | \_area_get_shape(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                                   | \_area_get_shape_count(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                   |
| [Transform2D](class_transform2d.md#class-transform2d)                                           | \_area_get_shape_transform(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                                   | \_area_get_space(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                               |
| [Transform2D](class_transform2d.md#class-transform2d)                                           | \_area_get_transform(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_area_remove_shape(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_area_set_area_monitor_callback(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_area_set_collision_layer(area: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_area_set_collision_mask(area: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                        |
|                                                                                                 | \_area_set_monitor_callback(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                 |
|                                                                                                 | \_area_set_monitorable(area: [RID](class_rid.md#class-rid), monitorable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_area_set_param(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver2d.md#enum-physicsserver2d-areaparameter), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                        |
|                                                                                                 | \_area_set_pickable(area: [RID](class_rid.md#class-rid), pickable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_area_set_shape(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_area_set_shape_disabled(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_area_set_shape_transform(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                               |
|                                                                                                 | \_area_set_space(area: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                 | \_area_set_transform(area: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_body_add_collision_exception(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_body_add_constant_central_force(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                           |
|                                                                                                 | \_body_add_constant_force(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                      |
|                                                                                                 | \_body_add_constant_torque(body: [RID](class_rid.md#class-rid), torque: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                              |
|                                                                                                 | \_body_add_shape(body: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                           |
|                                                                                                 | \_body_apply_central_force(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                         |
|                                                                                                 | \_body_apply_central_impulse(body: [RID](class_rid.md#class-rid), impulse: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                   |
|                                                                                                 | \_body_apply_force(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_body_apply_impulse(body: [RID](class_rid.md#class-rid), impulse: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                              |
|                                                                                                 | \_body_apply_torque(body: [RID](class_rid.md#class-rid), torque: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_body_apply_torque_impulse(body: [RID](class_rid.md#class-rid), impulse: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                           |
|                                                                                                 | \_body_attach_canvas_instance_id(body: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_body_attach_object_instance_id(body: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_body_clear_shapes(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                                | \_body_collide_shape(body: [RID](class_rid.md#class-rid), body_shape: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid), shape_xform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), r_results: `void*`, result_max: [int](class_int.md#class-int), r_result_count: `int32_t*`)                                                                    |
| [RID](class_rid.md#class-rid)                                                                   | \_body_create()                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                                   | \_body_get_canvas_instance_id(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                     |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]                              | \_body_get_collision_exceptions(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                                   | \_body_get_collision_layer(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                                   | \_body_get_collision_mask(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                             |
| [float](class_float.md#class-float)                                                             | \_body_get_collision_priority(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                     |
| [Vector2](class_vector2.md#class-vector2)                                                       | \_body_get_constant_force(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                             |
| [float](class_float.md#class-float)                                                             | \_body_get_constant_torque(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                           |
| [float](class_float.md#class-float)                                                             | \_body_get_contacts_reported_depth_threshold(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [CCDMode](class_physicsserver2d.md#enum-physicsserver2d-ccdmode)                                | \_body_get_continuous_collision_detection_mode(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                   |
| [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d)    | \_body_get_direct_state(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                                   | \_body_get_max_contacts_reported(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
| [BodyMode](class_physicsserver2d.md#enum-physicsserver2d-bodymode)                              | \_body_get_mode(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                                   | \_body_get_object_instance_id(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                     |
| [Variant](class_variant.md#class-variant)                                                       | \_body_get_param(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver2d.md#enum-physicsserver2d-bodyparameter))                                                                                                                                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                                                   | \_body_get_shape(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                                   | \_body_get_shape_count(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                   |
| [Transform2D](class_transform2d.md#class-transform2d)                                           | \_body_get_shape_transform(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                                   | \_body_get_space(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                               |
| [Variant](class_variant.md#class-variant)                                                       | \_body_get_state(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver2d.md#enum-physicsserver2d-bodystate))                                                                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                                | \_body_is_omitting_force_integration(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_remove_collision_exception(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_remove_shape(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_reset_mass_properties(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_set_axis_velocity(body: [RID](class_rid.md#class-rid), axis_velocity: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_body_set_collision_layer(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_body_set_collision_mask(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                        |
|                                                                                                 | \_body_set_collision_priority(body: [RID](class_rid.md#class-rid), priority: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                      |
|                                                                                                 | \_body_set_constant_force(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                           |
|                                                                                                 | \_body_set_constant_torque(body: [RID](class_rid.md#class-rid), torque: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                              |
|                                                                                                 | \_body_set_contacts_reported_depth_threshold(body: [RID](class_rid.md#class-rid), threshold: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_set_continuous_collision_detection_mode(body: [RID](class_rid.md#class-rid), mode: [CCDMode](class_physicsserver2d.md#enum-physicsserver2d-ccdmode))                                                                                                                                                                                                                                           |
|                                                                                                 | \_body_set_force_integration_callback(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable), userdata: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                        |
|                                                                                                 | \_body_set_max_contacts_reported(body: [RID](class_rid.md#class-rid), amount: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                        |
|                                                                                                 | \_body_set_mode(body: [RID](class_rid.md#class-rid), mode: [BodyMode](class_physicsserver2d.md#enum-physicsserver2d-bodymode))                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_set_omit_force_integration(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                   |
|                                                                                                 | \_body_set_param(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver2d.md#enum-physicsserver2d-bodyparameter), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                        |
|                                                                                                 | \_body_set_pickable(body: [RID](class_rid.md#class-rid), pickable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_body_set_shape(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_set_shape_as_one_way_collision(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool), margin: [float](class_float.md#class-float), direction: [Vector2](class_vector2.md#class-vector2))                                                                                                                                              |
|                                                                                                 | \_body_set_shape_disabled(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_set_shape_transform(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_set_space(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                 | \_body_set_state(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver2d.md#enum-physicsserver2d-bodystate), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                |
|                                                                                                 | \_body_set_state_sync_callback(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                                | \_body_test_motion(body: [RID](class_rid.md#class-rid), from: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collide_separation_ray: [bool](class_bool.md#class-bool), recovery_as_collision: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionMotionResult*`)                                        |
| [RID](class_rid.md#class-rid)                                                                   | \_capsule_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                                   | \_circle_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                        |
| [RID](class_rid.md#class-rid)                                                                   | \_concave_polygon_shape_create()                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                                   | \_convex_polygon_shape_create()                                                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                                             | \_damped_spring_joint_get_param(joint: [RID](class_rid.md#class-rid), param: [DampedSpringParam](class_physicsserver2d.md#enum-physicsserver2d-dampedspringparam))                                                                                                                                                                                                                                                   |
|                                                                                                 | \_damped_spring_joint_set_param(joint: [RID](class_rid.md#class-rid), param: [DampedSpringParam](class_physicsserver2d.md#enum-physicsserver2d-dampedspringparam), value: [float](class_float.md#class-float))                                                                                                                                                                                                       |
|                                                                                                 | \_end_sync()                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                 | \_finish()                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                 | \_flush_queries()                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_free_rid(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                                                   | \_get_process_info(process_info: [ProcessInfo](class_physicsserver2d.md#enum-physicsserver2d-processinfo))                                                                                                                                                                                                                                                                                                                        |
|                                                                                                 | \_init()                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                                | \_is_flushing_queries()                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                 | \_joint_clear(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                    |
| [RID](class_rid.md#class-rid)                                                                   | \_joint_create()                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                 | \_joint_disable_collisions_between_bodies(joint: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                             | \_joint_get_param(joint: [RID](class_rid.md#class-rid), param: [JointParam](class_physicsserver2d.md#enum-physicsserver2d-jointparam))                                                                                                                                                                                                                                                                                             |
| [JointType](class_physicsserver2d.md#enum-physicsserver2d-jointtype)                            | \_joint_get_type(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                                | \_joint_is_disabled_collisions_between_bodies(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_joint_make_damped_spring(joint: [RID](class_rid.md#class-rid), anchor_a: [Vector2](class_vector2.md#class-vector2), anchor_b: [Vector2](class_vector2.md#class-vector2), body_a: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))                                                                                                                                                                  |
|                                                                                                 | \_joint_make_groove(joint: [RID](class_rid.md#class-rid), a_groove1: [Vector2](class_vector2.md#class-vector2), a_groove2: [Vector2](class_vector2.md#class-vector2), b_anchor: [Vector2](class_vector2.md#class-vector2), body_a: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))                                                                                                                         |
|                                                                                                 | \_joint_make_pin(joint: [RID](class_rid.md#class-rid), anchor: [Vector2](class_vector2.md#class-vector2), body_a: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                             |
|                                                                                                 | \_joint_set_param(joint: [RID](class_rid.md#class-rid), param: [JointParam](class_physicsserver2d.md#enum-physicsserver2d-jointparam), value: [float](class_float.md#class-float))                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                                | \_pin_joint_get_flag(joint: [RID](class_rid.md#class-rid), flag: [PinJointFlag](class_physicsserver2d.md#enum-physicsserver2d-pinjointflag))                                                                                                                                                                                                                                                                                    |
| [float](class_float.md#class-float)                                                             | \_pin_joint_get_param(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver2d.md#enum-physicsserver2d-pinjointparam))                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_pin_joint_set_flag(joint: [RID](class_rid.md#class-rid), flag: [PinJointFlag](class_physicsserver2d.md#enum-physicsserver2d-pinjointflag), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                         |
|                                                                                                 | \_pin_joint_set_param(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver2d.md#enum-physicsserver2d-pinjointparam), value: [float](class_float.md#class-float))                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                                                   | \_rectangle_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                                   | \_segment_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                                   | \_separation_ray_shape_create()                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                 | \_set_active(active: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                                | \_shape_collide(shape_A: [RID](class_rid.md#class-rid), xform_A: [Transform2D](class_transform2d.md#class-transform2d), motion_A: [Vector2](class_vector2.md#class-vector2), shape_B: [RID](class_rid.md#class-rid), xform_B: [Transform2D](class_transform2d.md#class-transform2d), motion_B: [Vector2](class_vector2.md#class-vector2), r_results: `void*`, result_max: [int](class_int.md#class-int), r_result_count: `int32_t*`) |
| [float](class_float.md#class-float)                                                             | \_shape_get_custom_solver_bias(shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                  |
| [Variant](class_variant.md#class-variant)                                                       | \_shape_get_data(shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| [ShapeType](class_physicsserver2d.md#enum-physicsserver2d-shapetype)                            | \_shape_get_type(shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                 | \_shape_set_custom_solver_bias(shape: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_shape_set_data(shape: [RID](class_rid.md#class-rid), data: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                                   | \_space_create()                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                                   | \_space_get_contact_count(space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                            |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)                      | \_space_get_contacts(space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                      |
| [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) | \_space_get_direct_state(space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                              |
| [float](class_float.md#class-float)                                                             | \_space_get_param(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver2d.md#enum-physicsserver2d-spaceparameter))                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                                | \_space_is_active(space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_space_set_active(space: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_space_set_debug_contacts(space: [RID](class_rid.md#class-rid), max_contacts: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_space_set_param(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver2d.md#enum-physicsserver2d-spaceparameter), value: [float](class_float.md#class-float))                                                                                                                                                                                                                                         |
|                                                                                                 | \_step(step: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_sync()                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                                   | \_world_boundary_shape_create()                                                                                                                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                                | body_test_motion_is_excluding_body(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                                | body_test_motion_is_excluding_object(object: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                           |

---

## Method Descriptions

 **\_area_add_shape**(area: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), disabled: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.area_add_shape()](class_physicsserver2d.md#class-physicsserver2d-method-area-add-shape).

---

 **\_area_attach_canvas_instance_id**(area: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.area_attach_canvas_instance_id()](class_physicsserver2d.md#class-physicsserver2d-method-area-attach-canvas-instance-id).

---

 **\_area_attach_object_instance_id**(area: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.area_attach_object_instance_id()](class_physicsserver2d.md#class-physicsserver2d-method-area-attach-object-instance-id).

---

 **\_area_clear_shapes**(area: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_clear_shapes()](class_physicsserver2d.md#class-physicsserver2d-method-area-clear-shapes).

---

[RID](class_rid.md#class-rid) **\_area_create**()

Overridable version of [PhysicsServer2D.area_create()](class_physicsserver2d.md#class-physicsserver2d-method-area-create).

---

[int](class_int.md#class-int) **\_area_get_canvas_instance_id**(area: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_get_canvas_instance_id()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-canvas-instance-id).

---

[int](class_int.md#class-int) **\_area_get_collision_layer**(area: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_get_collision_layer()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-collision-layer).

---

[int](class_int.md#class-int) **\_area_get_collision_mask**(area: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_get_collision_mask()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-collision-mask).

---

[int](class_int.md#class-int) **\_area_get_object_instance_id**(area: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_get_object_instance_id()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-object-instance-id).

---

[Variant](class_variant.md#class-variant) **\_area_get_param**(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver2d.md#enum-physicsserver2d-areaparameter))

Overridable version of [PhysicsServer2D.area_get_param()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-param).

---

[RID](class_rid.md#class-rid) **\_area_get_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.area_get_shape()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-shape).

---

[int](class_int.md#class-int) **\_area_get_shape_count**(area: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_get_shape_count()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-shape-count).

---

[Transform2D](class_transform2d.md#class-transform2d) **\_area_get_shape_transform**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.area_get_shape_transform()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-shape-transform).

---

[RID](class_rid.md#class-rid) **\_area_get_space**(area: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_get_space()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-space).

---

[Transform2D](class_transform2d.md#class-transform2d) **\_area_get_transform**(area: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_get_transform()](class_physicsserver2d.md#class-physicsserver2d-method-area-get-transform).

---

 **\_area_remove_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.area_remove_shape()](class_physicsserver2d.md#class-physicsserver2d-method-area-remove-shape).

---

 **\_area_set_area_monitor_callback**(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))

Overridable version of [PhysicsServer2D.area_set_area_monitor_callback()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-area-monitor-callback).

---

 **\_area_set_collision_layer**(area: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.area_set_collision_layer()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-collision-layer).

---

 **\_area_set_collision_mask**(area: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.area_set_collision_mask()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-collision-mask).

---

 **\_area_set_monitor_callback**(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))

Overridable version of [PhysicsServer2D.area_set_monitor_callback()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-monitor-callback).

---

 **\_area_set_monitorable**(area: [RID](class_rid.md#class-rid), monitorable: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.area_set_monitorable()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-monitorable).

---

 **\_area_set_param**(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver2d.md#enum-physicsserver2d-areaparameter), value: [Variant](class_variant.md#class-variant))

Overridable version of [PhysicsServer2D.area_set_param()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-param).

---

 **\_area_set_pickable**(area: [RID](class_rid.md#class-rid), pickable: [bool](class_bool.md#class-bool))

If set to `true`, allows the area with the given [RID](class_rid.md#class-rid) to detect mouse inputs when the mouse cursor is hovering on it.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `area_set_pickable` method. Corresponds to [CollisionObject2D.input_pickable](class_collisionobject2d.md#class-collisionobject2d-property-input-pickable).

---

 **\_area_set_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_set_shape()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-shape).

---

 **\_area_set_shape_disabled**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.area_set_shape_disabled()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-shape-disabled).

---

 **\_area_set_shape_transform**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))

Overridable version of [PhysicsServer2D.area_set_shape_transform()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-shape-transform).

---

 **\_area_set_space**(area: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.area_set_space()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-space).

---

 **\_area_set_transform**(area: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Overridable version of [PhysicsServer2D.area_set_transform()](class_physicsserver2d.md#class-physicsserver2d-method-area-set-transform).

---

 **\_body_add_collision_exception**(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_add_collision_exception()](class_physicsserver2d.md#class-physicsserver2d-method-body-add-collision-exception).

---

 **\_body_add_constant_central_force**(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_add_constant_central_force()](class_physicsserver2d.md#class-physicsserver2d-method-body-add-constant-central-force).

---

 **\_body_add_constant_force**(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_add_constant_force()](class_physicsserver2d.md#class-physicsserver2d-method-body-add-constant-force).

---

 **\_body_add_constant_torque**(body: [RID](class_rid.md#class-rid), torque: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.body_add_constant_torque()](class_physicsserver2d.md#class-physicsserver2d-method-body-add-constant-torque).

---

 **\_body_add_shape**(body: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d), disabled: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.body_add_shape()](class_physicsserver2d.md#class-physicsserver2d-method-body-add-shape).

---

 **\_body_apply_central_force**(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_apply_central_force()](class_physicsserver2d.md#class-physicsserver2d-method-body-apply-central-force).

---

 **\_body_apply_central_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_apply_central_impulse()](class_physicsserver2d.md#class-physicsserver2d-method-body-apply-central-impulse).

---

 **\_body_apply_force**(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_apply_force()](class_physicsserver2d.md#class-physicsserver2d-method-body-apply-force).

---

 **\_body_apply_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector2](class_vector2.md#class-vector2), position: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_apply_impulse()](class_physicsserver2d.md#class-physicsserver2d-method-body-apply-impulse).

---

 **\_body_apply_torque**(body: [RID](class_rid.md#class-rid), torque: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.body_apply_torque()](class_physicsserver2d.md#class-physicsserver2d-method-body-apply-torque).

---

 **\_body_apply_torque_impulse**(body: [RID](class_rid.md#class-rid), impulse: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.body_apply_torque_impulse()](class_physicsserver2d.md#class-physicsserver2d-method-body-apply-torque-impulse).

---

 **\_body_attach_canvas_instance_id**(body: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.body_attach_canvas_instance_id()](class_physicsserver2d.md#class-physicsserver2d-method-body-attach-canvas-instance-id).

---

 **\_body_attach_object_instance_id**(body: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.body_attach_object_instance_id()](class_physicsserver2d.md#class-physicsserver2d-method-body-attach-object-instance-id).

---

 **\_body_clear_shapes**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_clear_shapes()](class_physicsserver2d.md#class-physicsserver2d-method-body-clear-shapes).

---

[bool](class_bool.md#class-bool) **\_body_collide_shape**(body: [RID](class_rid.md#class-rid), body_shape: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid), shape_xform: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), r_results: `void*`, result_max: [int](class_int.md#class-int), r_result_count: `int32_t*`)

Given a `body`, a `shape`, and their respective parameters, this method should return `true` if a collision between the two would occur, with additional details passed in `r_results`.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `shape_collide` method. Corresponds to [PhysicsDirectSpaceState2D.collide_shape()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-collide-shape).

---

[RID](class_rid.md#class-rid) **\_body_create**()

Overridable version of [PhysicsServer2D.body_create()](class_physicsserver2d.md#class-physicsserver2d-method-body-create).

---

[int](class_int.md#class-int) **\_body_get_canvas_instance_id**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_canvas_instance_id()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-canvas-instance-id).

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **\_body_get_collision_exceptions**(body: [RID](class_rid.md#class-rid))

Returns the [RID](class_rid.md#class-rid)s of all bodies added as collision exceptions for the given `body`. See also \_body_add_collision_exception() and \_body_remove_collision_exception().

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `body_get_collision_exceptions` method. Corresponds to [PhysicsBody2D.get_collision_exceptions()](class_physicsbody2d.md#class-physicsbody2d-method-get-collision-exceptions).

---

[int](class_int.md#class-int) **\_body_get_collision_layer**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_collision_layer()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-collision-layer).

---

[int](class_int.md#class-int) **\_body_get_collision_mask**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_collision_mask()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-collision-mask).

---

[float](class_float.md#class-float) **\_body_get_collision_priority**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_collision_priority()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-collision-priority).

---

[Vector2](class_vector2.md#class-vector2) **\_body_get_constant_force**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_constant_force()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-constant-force).

---

[float](class_float.md#class-float) **\_body_get_constant_torque**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_constant_torque()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-constant-torque).

---

[float](class_float.md#class-float) **\_body_get_contacts_reported_depth_threshold**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `body_get_contacts_reported_depth_threshold` method.

**Note:** This method is currently unused by Godot's default physics implementation.

---

[CCDMode](class_physicsserver2d.md#enum-physicsserver2d-ccdmode) **\_body_get_continuous_collision_detection_mode**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_continuous_collision_detection_mode()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-continuous-collision-detection-mode).

---

[PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class-physicsdirectbodystate2d) **\_body_get_direct_state**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_direct_state()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-direct-state).

---

[int](class_int.md#class-int) **\_body_get_max_contacts_reported**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_max_contacts_reported()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-max-contacts-reported).

---

[BodyMode](class_physicsserver2d.md#enum-physicsserver2d-bodymode) **\_body_get_mode**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_mode()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-mode).

---

[int](class_int.md#class-int) **\_body_get_object_instance_id**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_object_instance_id()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-object-instance-id).

---

[Variant](class_variant.md#class-variant) **\_body_get_param**(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver2d.md#enum-physicsserver2d-bodyparameter))

Overridable version of [PhysicsServer2D.body_get_param()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-param).

---

[RID](class_rid.md#class-rid) **\_body_get_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.body_get_shape()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-shape).

---

[int](class_int.md#class-int) **\_body_get_shape_count**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_shape_count()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-shape-count).

---

[Transform2D](class_transform2d.md#class-transform2d) **\_body_get_shape_transform**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.body_get_shape_transform()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-shape-transform).

---

[RID](class_rid.md#class-rid) **\_body_get_space**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_get_space()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-space).

---

[Variant](class_variant.md#class-variant) **\_body_get_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver2d.md#enum-physicsserver2d-bodystate))

Overridable version of [PhysicsServer2D.body_get_state()](class_physicsserver2d.md#class-physicsserver2d-method-body-get-state).

---

[bool](class_bool.md#class-bool) **\_body_is_omitting_force_integration**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_is_omitting_force_integration()](class_physicsserver2d.md#class-physicsserver2d-method-body-is-omitting-force-integration).

---

 **\_body_remove_collision_exception**(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_remove_collision_exception()](class_physicsserver2d.md#class-physicsserver2d-method-body-remove-collision-exception).

---

 **\_body_remove_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.body_remove_shape()](class_physicsserver2d.md#class-physicsserver2d-method-body-remove-shape).

---

 **\_body_reset_mass_properties**(body: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_reset_mass_properties()](class_physicsserver2d.md#class-physicsserver2d-method-body-reset-mass-properties).

---

 **\_body_set_axis_velocity**(body: [RID](class_rid.md#class-rid), axis_velocity: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_set_axis_velocity()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-axis-velocity).

---

 **\_body_set_collision_layer**(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.body_set_collision_layer()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-collision-layer).

---

 **\_body_set_collision_mask**(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.body_set_collision_mask()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-collision-mask).

---

 **\_body_set_collision_priority**(body: [RID](class_rid.md#class-rid), priority: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.body_set_collision_priority()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-collision-priority).

---

 **\_body_set_constant_force**(body: [RID](class_rid.md#class-rid), force: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_set_constant_force()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-constant-force).

---

 **\_body_set_constant_torque**(body: [RID](class_rid.md#class-rid), torque: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.body_set_constant_torque()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-constant-torque).

---

 **\_body_set_contacts_reported_depth_threshold**(body: [RID](class_rid.md#class-rid), threshold: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `body_set_contacts_reported_depth_threshold` method.

**Note:** This method is currently unused by Godot's default physics implementation.

---

 **\_body_set_continuous_collision_detection_mode**(body: [RID](class_rid.md#class-rid), mode: [CCDMode](class_physicsserver2d.md#enum-physicsserver2d-ccdmode))

Overridable version of [PhysicsServer2D.body_set_continuous_collision_detection_mode()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-continuous-collision-detection-mode).

---

 **\_body_set_force_integration_callback**(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable), userdata: [Variant](class_variant.md#class-variant))

Overridable version of [PhysicsServer2D.body_set_force_integration_callback()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-force-integration-callback).

---

 **\_body_set_max_contacts_reported**(body: [RID](class_rid.md#class-rid), amount: [int](class_int.md#class-int))

Overridable version of [PhysicsServer2D.body_set_max_contacts_reported()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-max-contacts-reported).

---

 **\_body_set_mode**(body: [RID](class_rid.md#class-rid), mode: [BodyMode](class_physicsserver2d.md#enum-physicsserver2d-bodymode))

Overridable version of [PhysicsServer2D.body_set_mode()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-mode).

---

 **\_body_set_omit_force_integration**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.body_set_omit_force_integration()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-omit-force-integration).

---

 **\_body_set_param**(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver2d.md#enum-physicsserver2d-bodyparameter), value: [Variant](class_variant.md#class-variant))

Overridable version of [PhysicsServer2D.body_set_param()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-param).

---

 **\_body_set_pickable**(body: [RID](class_rid.md#class-rid), pickable: [bool](class_bool.md#class-bool))

If set to `true`, allows the body with the given [RID](class_rid.md#class-rid) to detect mouse inputs when the mouse cursor is hovering on it.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `body_set_pickable` method. Corresponds to [CollisionObject2D.input_pickable](class_collisionobject2d.md#class-collisionobject2d-property-input-pickable).

---

 **\_body_set_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_set_shape()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-shape).

---

 **\_body_set_shape_as_one_way_collision**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool), margin: [float](class_float.md#class-float), direction: [Vector2](class_vector2.md#class-vector2))

Overridable version of [PhysicsServer2D.body_set_shape_as_one_way_collision()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-shape-as-one-way-collision).

---

 **\_body_set_shape_disabled**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.body_set_shape_disabled()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-shape-disabled).

---

 **\_body_set_shape_transform**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))

Overridable version of [PhysicsServer2D.body_set_shape_transform()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-shape-transform).

---

 **\_body_set_space**(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.body_set_space()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-space).

---

 **\_body_set_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver2d.md#enum-physicsserver2d-bodystate), value: [Variant](class_variant.md#class-variant))

Overridable version of [PhysicsServer2D.body_set_state()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-state).

---

 **\_body_set_state_sync_callback**(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable))

Assigns the `body` to call the given `callable` during the synchronization phase of the loop, before \_step() is called. See also \_sync().

Overridable version of [PhysicsServer2D.body_set_state_sync_callback()](class_physicsserver2d.md#class-physicsserver2d-method-body-set-state-sync-callback).

---

[bool](class_bool.md#class-bool) **\_body_test_motion**(body: [RID](class_rid.md#class-rid), from: [Transform2D](class_transform2d.md#class-transform2d), motion: [Vector2](class_vector2.md#class-vector2), margin: [float](class_float.md#class-float), collide_separation_ray: [bool](class_bool.md#class-bool), recovery_as_collision: [bool](class_bool.md#class-bool), r_result: `PhysicsServer2DExtensionMotionResult*`)

Overridable version of [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class-physicsserver2d-method-body-test-motion). Unlike the exposed implementation, this method does not receive all of the arguments inside a [PhysicsTestMotionParameters2D](class_physicstestmotionparameters2d.md#class-physicstestmotionparameters2d).

---

[RID](class_rid.md#class-rid) **\_capsule_shape_create**()

Overridable version of [PhysicsServer2D.capsule_shape_create()](class_physicsserver2d.md#class-physicsserver2d-method-capsule-shape-create).

---

[RID](class_rid.md#class-rid) **\_circle_shape_create**()

Overridable version of [PhysicsServer2D.circle_shape_create()](class_physicsserver2d.md#class-physicsserver2d-method-circle-shape-create).

---

[RID](class_rid.md#class-rid) **\_concave_polygon_shape_create**()

Overridable version of [PhysicsServer2D.concave_polygon_shape_create()](class_physicsserver2d.md#class-physicsserver2d-method-concave-polygon-shape-create).

---

[RID](class_rid.md#class-rid) **\_convex_polygon_shape_create**()

Overridable version of [PhysicsServer2D.convex_polygon_shape_create()](class_physicsserver2d.md#class-physicsserver2d-method-convex-polygon-shape-create).

---

[float](class_float.md#class-float) **\_damped_spring_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [DampedSpringParam](class_physicsserver2d.md#enum-physicsserver2d-dampedspringparam))

Overridable version of [PhysicsServer2D.damped_spring_joint_get_param()](class_physicsserver2d.md#class-physicsserver2d-method-damped-spring-joint-get-param).

---

 **\_damped_spring_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [DampedSpringParam](class_physicsserver2d.md#enum-physicsserver2d-dampedspringparam), value: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.damped_spring_joint_set_param()](class_physicsserver2d.md#class-physicsserver2d-method-damped-spring-joint-set-param).

---

 **\_end_sync**()

Called to indicate that the physics server has stopped synchronizing. It is in the loop's iteration/physics phase, and can access physics objects even if running on a separate thread. See also \_sync().

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `end_sync` method.

---

 **\_finish**()

Called when the main loop finalizes to shut down the physics server. See also [MainLoop._finalize()](class_mainloop.md#class-mainloop-private-method-finalize) and \_init().

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `finish` method.

---

 **\_flush_queries**()

Called every physics step before \_step() to process all remaining queries.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `flush_queries` method.

---

 **\_free_rid**(rid: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.free_rid()](class_physicsserver2d.md#class-physicsserver2d-method-free-rid).

---

[int](class_int.md#class-int) **\_get_process_info**(process_info: [ProcessInfo](class_physicsserver2d.md#enum-physicsserver2d-processinfo))

Overridable version of [PhysicsServer2D.get_process_info()](class_physicsserver2d.md#class-physicsserver2d-method-get-process-info).

---

 **\_init**()

Called when the main loop is initialized and creates a new instance of this physics server. See also [MainLoop._initialize()](class_mainloop.md#class-mainloop-private-method-initialize) and \_finish().

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `init` method.

---

[bool](class_bool.md#class-bool) **\_is_flushing_queries**()

Overridable method that should return `true` when the physics server is processing queries. See also \_flush_queries().

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `is_flushing_queries` method.

---

 **\_joint_clear**(joint: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.joint_clear()](class_physicsserver2d.md#class-physicsserver2d-method-joint-clear).

---

[RID](class_rid.md#class-rid) **\_joint_create**()

Overridable version of [PhysicsServer2D.joint_create()](class_physicsserver2d.md#class-physicsserver2d-method-joint-create).

---

 **\_joint_disable_collisions_between_bodies**(joint: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.joint_disable_collisions_between_bodies()](class_physicsserver2d.md#class-physicsserver2d-method-joint-disable-collisions-between-bodies).

---

[float](class_float.md#class-float) **\_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [JointParam](class_physicsserver2d.md#enum-physicsserver2d-jointparam))

Overridable version of [PhysicsServer2D.joint_get_param()](class_physicsserver2d.md#class-physicsserver2d-method-joint-get-param).

---

[JointType](class_physicsserver2d.md#enum-physicsserver2d-jointtype) **\_joint_get_type**(joint: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.joint_get_type()](class_physicsserver2d.md#class-physicsserver2d-method-joint-get-type).

---

[bool](class_bool.md#class-bool) **\_joint_is_disabled_collisions_between_bodies**(joint: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.joint_is_disabled_collisions_between_bodies()](class_physicsserver2d.md#class-physicsserver2d-method-joint-is-disabled-collisions-between-bodies).

---

 **\_joint_make_damped_spring**(joint: [RID](class_rid.md#class-rid), anchor_a: [Vector2](class_vector2.md#class-vector2), anchor_b: [Vector2](class_vector2.md#class-vector2), body_a: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.joint_make_damped_spring()](class_physicsserver2d.md#class-physicsserver2d-method-joint-make-damped-spring).

---

 **\_joint_make_groove**(joint: [RID](class_rid.md#class-rid), a_groove1: [Vector2](class_vector2.md#class-vector2), a_groove2: [Vector2](class_vector2.md#class-vector2), b_anchor: [Vector2](class_vector2.md#class-vector2), body_a: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.joint_make_groove()](class_physicsserver2d.md#class-physicsserver2d-method-joint-make-groove).

---

 **\_joint_make_pin**(joint: [RID](class_rid.md#class-rid), anchor: [Vector2](class_vector2.md#class-vector2), body_a: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.joint_make_pin()](class_physicsserver2d.md#class-physicsserver2d-method-joint-make-pin).

---

 **\_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [JointParam](class_physicsserver2d.md#enum-physicsserver2d-jointparam), value: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.joint_set_param()](class_physicsserver2d.md#class-physicsserver2d-method-joint-set-param).

---

[bool](class_bool.md#class-bool) **\_pin_joint_get_flag**(joint: [RID](class_rid.md#class-rid), flag: [PinJointFlag](class_physicsserver2d.md#enum-physicsserver2d-pinjointflag))

Overridable version of [PhysicsServer2D.pin_joint_get_flag()](class_physicsserver2d.md#class-physicsserver2d-method-pin-joint-get-flag).

---

[float](class_float.md#class-float) **\_pin_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver2d.md#enum-physicsserver2d-pinjointparam))

Overridable version of [PhysicsServer2D.pin_joint_get_param()](class_physicsserver2d.md#class-physicsserver2d-method-pin-joint-get-param).

---

 **\_pin_joint_set_flag**(joint: [RID](class_rid.md#class-rid), flag: [PinJointFlag](class_physicsserver2d.md#enum-physicsserver2d-pinjointflag), enabled: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.pin_joint_set_flag()](class_physicsserver2d.md#class-physicsserver2d-method-pin-joint-set-flag).

---

 **\_pin_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver2d.md#enum-physicsserver2d-pinjointparam), value: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.pin_joint_set_param()](class_physicsserver2d.md#class-physicsserver2d-method-pin-joint-set-param).

---

[RID](class_rid.md#class-rid) **\_rectangle_shape_create**()

Overridable version of [PhysicsServer2D.rectangle_shape_create()](class_physicsserver2d.md#class-physicsserver2d-method-rectangle-shape-create).

---

[RID](class_rid.md#class-rid) **\_segment_shape_create**()

Overridable version of [PhysicsServer2D.segment_shape_create()](class_physicsserver2d.md#class-physicsserver2d-method-segment-shape-create).

---

[RID](class_rid.md#class-rid) **\_separation_ray_shape_create**()

Overridable version of [PhysicsServer2D.separation_ray_shape_create()](class_physicsserver2d.md#class-physicsserver2d-method-separation-ray-shape-create).

---

 **\_set_active**(active: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.set_active()](class_physicsserver2d.md#class-physicsserver2d-method-set-active).

---

[bool](class_bool.md#class-bool) **\_shape_collide**(shape_A: [RID](class_rid.md#class-rid), xform_A: [Transform2D](class_transform2d.md#class-transform2d), motion_A: [Vector2](class_vector2.md#class-vector2), shape_B: [RID](class_rid.md#class-rid), xform_B: [Transform2D](class_transform2d.md#class-transform2d), motion_B: [Vector2](class_vector2.md#class-vector2), r_results: `void*`, result_max: [int](class_int.md#class-int), r_result_count: `int32_t*`)

Given two shapes and their parameters, should return `true` if a collision between the two would occur, with additional details passed in `r_results`.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `shape_collide` method. Corresponds to [PhysicsDirectSpaceState2D.collide_shape()](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d-method-collide-shape).

---

[float](class_float.md#class-float) **\_shape_get_custom_solver_bias**(shape: [RID](class_rid.md#class-rid))

Should return the custom solver bias of the given `shape`, which defines how much bodies are forced to separate on contact when this shape is involved.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `shape_get_custom_solver_bias` method. Corresponds to [Shape2D.custom_solver_bias](class_shape2d.md#class-shape2d-property-custom-solver-bias).

---

[Variant](class_variant.md#class-variant) **\_shape_get_data**(shape: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.shape_get_data()](class_physicsserver2d.md#class-physicsserver2d-method-shape-get-data).

---

[ShapeType](class_physicsserver2d.md#enum-physicsserver2d-shapetype) **\_shape_get_type**(shape: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.shape_get_type()](class_physicsserver2d.md#class-physicsserver2d-method-shape-get-type).

---

 **\_shape_set_custom_solver_bias**(shape: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float))

Should set the custom solver bias for the given `shape`. It defines how much bodies are forced to separate on contact.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `shape_get_custom_solver_bias` method. Corresponds to [Shape2D.custom_solver_bias](class_shape2d.md#class-shape2d-property-custom-solver-bias).

---

 **\_shape_set_data**(shape: [RID](class_rid.md#class-rid), data: [Variant](class_variant.md#class-variant))

Overridable version of [PhysicsServer2D.shape_set_data()](class_physicsserver2d.md#class-physicsserver2d-method-shape-set-data).

---

[RID](class_rid.md#class-rid) **\_space_create**()

Overridable version of [PhysicsServer2D.space_create()](class_physicsserver2d.md#class-physicsserver2d-method-space-create).

---

[int](class_int.md#class-int) **\_space_get_contact_count**(space: [RID](class_rid.md#class-rid))

Should return how many contacts have occurred during the last physics step in the given `space`. See also \_space_get_contacts() and \_space_set_debug_contacts().

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `space_get_contact_count` method.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **\_space_get_contacts**(space: [RID](class_rid.md#class-rid))

Should return the positions of all contacts that have occurred during the last physics step in the given `space`. See also \_space_get_contact_count() and \_space_set_debug_contacts().

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `space_get_contacts` method.

---

[PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class-physicsdirectspacestate2d) **\_space_get_direct_state**(space: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.space_get_direct_state()](class_physicsserver2d.md#class-physicsserver2d-method-space-get-direct-state).

---

[float](class_float.md#class-float) **\_space_get_param**(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver2d.md#enum-physicsserver2d-spaceparameter))

Overridable version of [PhysicsServer2D.space_get_param()](class_physicsserver2d.md#class-physicsserver2d-method-space-get-param).

---

[bool](class_bool.md#class-bool) **\_space_is_active**(space: [RID](class_rid.md#class-rid))

Overridable version of [PhysicsServer2D.space_is_active()](class_physicsserver2d.md#class-physicsserver2d-method-space-is-active).

---

 **\_space_set_active**(space: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool))

Overridable version of [PhysicsServer2D.space_set_active()](class_physicsserver2d.md#class-physicsserver2d-method-space-set-active).

---

 **\_space_set_debug_contacts**(space: [RID](class_rid.md#class-rid), max_contacts: [int](class_int.md#class-int))

Used internally to allow the given `space` to store contact points, up to `max_contacts`. This is automatically set for the main [World2D](class_world2d.md#class-world2d)'s space when [SceneTree.debug_collisions_hint](class_scenetree.md#class-scenetree-property-debug-collisions-hint) is `true`, or by checking "Visible Collision Shapes" in the editor. Only works in debug builds.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `space_set_debug_contacts` method.

---

 **\_space_set_param**(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver2d.md#enum-physicsserver2d-spaceparameter), value: [float](class_float.md#class-float))

Overridable version of [PhysicsServer2D.space_set_param()](class_physicsserver2d.md#class-physicsserver2d-method-space-set-param).

---

 **\_step**(step: [float](class_float.md#class-float))

Called every physics step to process the physics simulation. `step` is the time elapsed since the last physics step, in seconds. It is usually the same as the value returned by [Node.get_physics_process_delta_time()](class_node.md#class-node-method-get-physics-process-delta-time).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `step` method.

---

 **\_sync**()

Called to indicate that the physics server is synchronizing and cannot access physics states if running on a separate thread. See also \_end_sync().

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d)'s internal `sync` method.

---

[RID](class_rid.md#class-rid) **\_world_boundary_shape_create**()

Overridable version of [PhysicsServer2D.world_boundary_shape_create()](class_physicsserver2d.md#class-physicsserver2d-method-world-boundary-shape-create).

---

[bool](class_bool.md#class-bool) **body_test_motion_is_excluding_body**(body: [RID](class_rid.md#class-rid))

Returns `true` if the body with the given [RID](class_rid.md#class-rid) is being excluded from \_body_test_motion(). See also [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).

---

[bool](class_bool.md#class-bool) **body_test_motion_is_excluding_object**(object: [int](class_int.md#class-int))

Returns `true` if the object with the given instance ID is being excluded from \_body_test_motion(). See also [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id).
