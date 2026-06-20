# PhysicsServer3DExtension

**Inherits:** [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) **<** [Object](class_object.md#class-object)

Provides virtual methods that can be overridden to create custom [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementations.

## Description

This class extends [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d).

## Methods

|                                                                                                 | \_area_add_shape(area: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                 | \_area_attach_object_instance_id(area: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_area_clear_shapes(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                                   | \_area_create()                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                                   | \_area_get_collision_layer(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                                   | \_area_get_collision_mask(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                                   | \_area_get_object_instance_id(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                             |
| [Variant](class_variant.md#class-variant)                                                       | \_area_get_param(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver3d.md#enum-physicsserver3d-areaparameter))                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                                   | \_area_get_shape(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                                   | \_area_get_shape_count(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                           |
| [Transform3D](class_transform3d.md#class-transform3d)                                           | \_area_get_shape_transform(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                                                   | \_area_get_space(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                       |
| [Transform3D](class_transform3d.md#class-transform3d)                                           | \_area_get_transform(area: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_area_remove_shape(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_area_set_area_monitor_callback(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_area_set_collision_layer(area: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_area_set_collision_mask(area: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_area_set_monitor_callback(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                         |
|                                                                                                 | \_area_set_monitorable(area: [RID](class_rid.md#class-rid), monitorable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_area_set_param(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver3d.md#enum-physicsserver3d-areaparameter), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                |
|                                                                                                 | \_area_set_ray_pickable(area: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_area_set_shape(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_area_set_shape_disabled(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_area_set_shape_transform(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                       |
|                                                                                                 | \_area_set_space(area: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                 | \_area_set_transform(area: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_body_add_collision_exception(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_body_add_constant_central_force(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                   |
|                                                                                                 | \_body_add_constant_force(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                              |
|                                                                                                 | \_body_add_constant_torque(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_body_add_shape(body: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                   |
|                                                                                                 | \_body_apply_central_force(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                 |
|                                                                                                 | \_body_apply_central_impulse(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                           |
|                                                                                                 | \_body_apply_force(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_body_apply_impulse(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                      |
|                                                                                                 | \_body_apply_torque(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                              |
|                                                                                                 | \_body_apply_torque_impulse(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_body_attach_object_instance_id(body: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_body_clear_shapes(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                                   | \_body_create()                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]                              | \_body_get_collision_exceptions(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                                   | \_body_get_collision_layer(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                                   | \_body_get_collision_mask(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                     |
| [float](class_float.md#class-float)                                                             | \_body_get_collision_priority(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                             |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_body_get_constant_force(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                     |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_body_get_constant_torque(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                   |
| [float](class_float.md#class-float)                                                             | \_body_get_contacts_reported_depth_threshold(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                               |
| [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d)    | \_body_get_direct_state(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                                   | \_body_get_max_contacts_reported(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                       |
| [BodyMode](class_physicsserver3d.md#enum-physicsserver3d-bodymode)                              | \_body_get_mode(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                                   | \_body_get_object_instance_id(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                             |
| [Variant](class_variant.md#class-variant)                                                       | \_body_get_param(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver3d.md#enum-physicsserver3d-bodyparameter))                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                                   | \_body_get_shape(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                                   | \_body_get_shape_count(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                           |
| [Transform3D](class_transform3d.md#class-transform3d)                                           | \_body_get_shape_transform(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                                                   | \_body_get_space(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                       |
| [Variant](class_variant.md#class-variant)                                                       | \_body_get_state(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate))                                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                                                   | \_body_get_user_flags(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                                | \_body_is_axis_locked(body: [RID](class_rid.md#class-rid), axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis))                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                                | \_body_is_continuous_collision_detection_enabled(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                                | \_body_is_omitting_force_integration(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_remove_collision_exception(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_remove_shape(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_reset_mass_properties(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_set_axis_lock(body: [RID](class_rid.md#class-rid), axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                             |
|                                                                                                 | \_body_set_axis_velocity(body: [RID](class_rid.md#class-rid), axis_velocity: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_body_set_collision_layer(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_body_set_collision_mask(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_body_set_collision_priority(body: [RID](class_rid.md#class-rid), priority: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                              |
|                                                                                                 | \_body_set_constant_force(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                   |
|                                                                                                 | \_body_set_constant_torque(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_body_set_contacts_reported_depth_threshold(body: [RID](class_rid.md#class-rid), threshold: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_set_enable_continuous_collision_detection(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                             |
|                                                                                                 | \_body_set_force_integration_callback(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable), userdata: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                |
|                                                                                                 | \_body_set_max_contacts_reported(body: [RID](class_rid.md#class-rid), amount: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_body_set_mode(body: [RID](class_rid.md#class-rid), mode: [BodyMode](class_physicsserver3d.md#enum-physicsserver3d-bodymode))                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_set_omit_force_integration(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                           |
|                                                                                                 | \_body_set_param(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver3d.md#enum-physicsserver3d-bodyparameter), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                |
|                                                                                                 | \_body_set_ray_pickable(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_set_shape(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_set_shape_disabled(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_body_set_shape_transform(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                       |
|                                                                                                 | \_body_set_space(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                 | \_body_set_state(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                        |
|                                                                                                 | \_body_set_state_sync_callback(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                   |
|                                                                                                 | \_body_set_user_flags(body: [RID](class_rid.md#class-rid), flags: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                                | \_body_test_motion(body: [RID](class_rid.md#class-rid), from: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), max_collisions: [int](class_int.md#class-int), collide_separation_ray: [bool](class_bool.md#class-bool), recovery_as_collision: [bool](class_bool.md#class-bool), r_result: `PhysicsServer3DExtensionMotionResult*`) |
| [RID](class_rid.md#class-rid)                                                                   | \_box_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                                   | \_capsule_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                              |
| [RID](class_rid.md#class-rid)                                                                   | \_concave_polygon_shape_create()                                                                                                                                                                                                                                                                                                                                                                                              |
| [float](class_float.md#class-float)                                                             | \_cone_twist_joint_get_param(joint: [RID](class_rid.md#class-rid), param: [ConeTwistJointParam](class_physicsserver3d.md#enum-physicsserver3d-conetwistjointparam))                                                                                                                                                                                                                                                             |
|                                                                                                 | \_cone_twist_joint_set_param(joint: [RID](class_rid.md#class-rid), param: [ConeTwistJointParam](class_physicsserver3d.md#enum-physicsserver3d-conetwistjointparam), value: [float](class_float.md#class-float))                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                                   | \_convex_polygon_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)                                                                   | \_custom_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)                                                                   | \_cylinder_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_end_sync()                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                 | \_finish()                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                 | \_flush_queries()                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_free_rid(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                                | \_generic_6dof_joint_get_flag(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisflag))                                                                                                                                                                                                            |
| [float](class_float.md#class-float)                                                             | \_generic_6dof_joint_get_param(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisparam))                                                                                                                                                                                                       |
|                                                                                                 | \_generic_6dof_joint_set_flag(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisflag), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                  |
|                                                                                                 | \_generic_6dof_joint_set_param(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisparam), value: [float](class_float.md#class-float))                                                                                                                                                           |
| [int](class_int.md#class-int)                                                                   | \_get_process_info(process_info: [ProcessInfo](class_physicsserver3d.md#enum-physicsserver3d-processinfo))                                                                                                                                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)                                                                   | \_heightmap_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                                | \_hinge_joint_get_flag(joint: [RID](class_rid.md#class-rid), flag: [HingeJointFlag](class_physicsserver3d.md#enum-physicsserver3d-hingejointflag))                                                                                                                                                                                                                                                                                    |
| [float](class_float.md#class-float)                                                             | \_hinge_joint_get_param(joint: [RID](class_rid.md#class-rid), param: [HingeJointParam](class_physicsserver3d.md#enum-physicsserver3d-hingejointparam))                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_hinge_joint_set_flag(joint: [RID](class_rid.md#class-rid), flag: [HingeJointFlag](class_physicsserver3d.md#enum-physicsserver3d-hingejointflag), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                         |
|                                                                                                 | \_hinge_joint_set_param(joint: [RID](class_rid.md#class-rid), param: [HingeJointParam](class_physicsserver3d.md#enum-physicsserver3d-hingejointparam), value: [float](class_float.md#class-float))                                                                                                                                                                                                                                   |
|                                                                                                 | \_init()                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                                | \_is_flushing_queries()                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_joint_clear(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                            |
| [RID](class_rid.md#class-rid)                                                                   | \_joint_create()                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                 | \_joint_disable_collisions_between_bodies(joint: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                                   | \_joint_get_solver_priority(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                |
| [JointType](class_physicsserver3d.md#enum-physicsserver3d-jointtype)                            | \_joint_get_type(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                                | \_joint_is_disabled_collisions_between_bodies(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                            |
|                                                                                                 | \_joint_make_cone_twist(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                  |
|                                                                                                 | \_joint_make_generic_6dof(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                              |
|                                                                                                 | \_joint_make_hinge(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), hinge_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), hinge_B: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                    |
|                                                                                                 | \_joint_make_hinge_simple(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), pivot_A: [Vector3](class_vector3.md#class-vector3), axis_A: [Vector3](class_vector3.md#class-vector3), body_B: [RID](class_rid.md#class-rid), pivot_B: [Vector3](class_vector3.md#class-vector3), axis_B: [Vector3](class_vector3.md#class-vector3))                                                                        |
|                                                                                                 | \_joint_make_pin(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_A: [Vector3](class_vector3.md#class-vector3), body_B: [RID](class_rid.md#class-rid), local_B: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                |
|                                                                                                 | \_joint_make_slider(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                          |
|                                                                                                 | \_joint_set_solver_priority(joint: [RID](class_rid.md#class-rid), priority: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                       |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_pin_joint_get_local_a(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                        |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_pin_joint_get_local_b(joint: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                                             | \_pin_joint_get_param(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver3d.md#enum-physicsserver3d-pinjointparam))                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_pin_joint_set_local_a(joint: [RID](class_rid.md#class-rid), local_A: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_pin_joint_set_local_b(joint: [RID](class_rid.md#class-rid), local_B: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_pin_joint_set_param(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver3d.md#enum-physicsserver3d-pinjointparam), value: [float](class_float.md#class-float))                                                                                                                                                                                                                                           |
| [RID](class_rid.md#class-rid)                                                                   | \_separation_ray_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_set_active(active: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                          |
| [float](class_float.md#class-float)                                                             | \_shape_get_custom_solver_bias(shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                          |
| [Variant](class_variant.md#class-variant)                                                       | \_shape_get_data(shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)                                                             | \_shape_get_margin(shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                  |
| [ShapeType](class_physicsserver3d.md#enum-physicsserver3d-shapetype)                            | \_shape_get_type(shape: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                 | \_shape_set_custom_solver_bias(shape: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_shape_set_data(shape: [RID](class_rid.md#class-rid), data: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_shape_set_margin(shape: [RID](class_rid.md#class-rid), margin: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                     |
| [float](class_float.md#class-float)                                                             | \_slider_joint_get_param(joint: [RID](class_rid.md#class-rid), param: [SliderJointParam](class_physicsserver3d.md#enum-physicsserver3d-sliderjointparam))                                                                                                                                                                                                                                                                           |
|                                                                                                 | \_slider_joint_set_param(joint: [RID](class_rid.md#class-rid), param: [SliderJointParam](class_physicsserver3d.md#enum-physicsserver3d-sliderjointparam), value: [float](class_float.md#class-float))                                                                                                                                                                                                                               |
|                                                                                                 | \_soft_body_add_collision_exception(body: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                          |
|                                                                                                 | \_soft_body_apply_central_force(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_soft_body_apply_central_impulse(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                 |
|                                                                                                 | \_soft_body_apply_point_force(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), force: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                               |
|                                                                                                 | \_soft_body_apply_point_impulse(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), impulse: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                                                   | \_soft_body_create()                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [AABB](class_aabb.md#class-aabb)                                                                | \_soft_body_get_bounds(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                           |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]                              | \_soft_body_get_collision_exceptions(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                                   | \_soft_body_get_collision_layer(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                                   | \_soft_body_get_collision_mask(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                           |
| [float](class_float.md#class-float)                                                             | \_soft_body_get_damping_coefficient(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                             | \_soft_body_get_drag_coefficient(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                       |
| [float](class_float.md#class-float)                                                             | \_soft_body_get_linear_stiffness(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                       |
| [Vector3](class_vector3.md#class-vector3)                                                       | \_soft_body_get_point_global_position(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                             | \_soft_body_get_pressure_coefficient(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                             | \_soft_body_get_shrinking_factor(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                                   | \_soft_body_get_simulation_precision(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                                   | \_soft_body_get_space(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                             |
| [Variant](class_variant.md#class-variant)                                                       | \_soft_body_get_state(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate))                                                                                                                                                                                                                                                                                                |
| [float](class_float.md#class-float)                                                             | \_soft_body_get_total_mass(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                                | \_soft_body_is_point_pinned(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_soft_body_move_point(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), global_position: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                   |
|                                                                                                 | \_soft_body_pin_point(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), pin: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                          |
|                                                                                                 | \_soft_body_remove_all_pinned_points(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                 | \_soft_body_remove_collision_exception(body: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_soft_body_set_collision_layer(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                   |
|                                                                                                 | \_soft_body_set_collision_mask(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                      |
|                                                                                                 | \_soft_body_set_damping_coefficient(body: [RID](class_rid.md#class-rid), damping_coefficient: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_soft_body_set_drag_coefficient(body: [RID](class_rid.md#class-rid), drag_coefficient: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_soft_body_set_linear_stiffness(body: [RID](class_rid.md#class-rid), linear_stiffness: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_soft_body_set_mesh(body: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                 | \_soft_body_set_pressure_coefficient(body: [RID](class_rid.md#class-rid), pressure_coefficient: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_soft_body_set_ray_pickable(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_soft_body_set_shrinking_factor(body: [RID](class_rid.md#class-rid), shrinking_factor: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_soft_body_set_simulation_precision(body: [RID](class_rid.md#class-rid), simulation_precision: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                          |
|                                                                                                 | \_soft_body_set_space(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                 | \_soft_body_set_state(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate), variant: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                            |
|                                                                                                 | \_soft_body_set_total_mass(body: [RID](class_rid.md#class-rid), total_mass: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                  |
|                                                                                                 | \_soft_body_set_transform(body: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                                                                   |
|                                                                                                 | \_soft_body_update_rendering_server(body: [RID](class_rid.md#class-rid), rendering_server_handler: [PhysicsServer3DRenderingServerHandler](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler))                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                                   | \_space_create()                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                                   | \_space_get_contact_count(space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                    |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)                      | \_space_get_contacts(space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                              |
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) | \_space_get_direct_state(space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)                                                             | \_space_get_param(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver3d.md#enum-physicsserver3d-spaceparameter))                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                                | \_space_is_active(space: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                 | \_space_set_active(space: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                 | \_space_set_debug_contacts(space: [RID](class_rid.md#class-rid), max_contacts: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_space_set_param(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver3d.md#enum-physicsserver3d-spaceparameter), value: [float](class_float.md#class-float))                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                                   | \_sphere_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                 | \_step(step: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                 | \_sync()                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [RID](class_rid.md#class-rid)                                                                   | \_world_boundary_shape_create()                                                                                                                                                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                                | body_test_motion_is_excluding_body(body: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                                | body_test_motion_is_excluding_object(object: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                   |

---

## Method Descriptions

 **\_area_add_shape**(area: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), disabled: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_attach_object_instance_id**(area: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_clear_shapes**(area: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_area_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_area_get_collision_layer**(area: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_area_get_collision_mask**(area: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_area_get_object_instance_id**(area: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Variant](class_variant.md#class-variant) **\_area_get_param**(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver3d.md#enum-physicsserver3d-areaparameter))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_area_get_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_area_get_shape_count**(area: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Transform3D](class_transform3d.md#class-transform3d) **\_area_get_shape_transform**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_area_get_space**(area: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Transform3D](class_transform3d.md#class-transform3d) **\_area_get_transform**(area: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_remove_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_area_monitor_callback**(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_collision_layer**(area: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_collision_mask**(area: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_monitor_callback**(area: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_monitorable**(area: [RID](class_rid.md#class-rid), monitorable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_param**(area: [RID](class_rid.md#class-rid), param: [AreaParameter](class_physicsserver3d.md#enum-physicsserver3d-areaparameter), value: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_ray_pickable**(area: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_shape**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_shape_disabled**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_shape_transform**(area: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_space**(area: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_area_set_transform**(area: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_add_collision_exception**(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_add_constant_central_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_add_constant_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_add_constant_torque**(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_add_shape**(body: [RID](class_rid.md#class-rid), shape: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), disabled: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_apply_central_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_apply_central_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_apply_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_apply_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3), position: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_apply_torque**(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_apply_torque_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_attach_object_instance_id**(body: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_clear_shapes**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_body_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **\_body_get_collision_exceptions**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_body_get_collision_layer**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_body_get_collision_mask**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_body_get_collision_priority**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_body_get_constant_force**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_body_get_constant_torque**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_body_get_contacts_reported_depth_threshold**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class-physicsdirectbodystate3d) **\_body_get_direct_state**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_body_get_max_contacts_reported**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[BodyMode](class_physicsserver3d.md#enum-physicsserver3d-bodymode) **\_body_get_mode**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_body_get_object_instance_id**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Variant](class_variant.md#class-variant) **\_body_get_param**(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver3d.md#enum-physicsserver3d-bodyparameter))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_body_get_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_body_get_shape_count**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Transform3D](class_transform3d.md#class-transform3d) **\_body_get_shape_transform**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_body_get_space**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Variant](class_variant.md#class-variant) **\_body_get_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_body_get_user_flags**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_body_is_axis_locked**(body: [RID](class_rid.md#class-rid), axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_body_is_continuous_collision_detection_enabled**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_body_is_omitting_force_integration**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_remove_collision_exception**(body: [RID](class_rid.md#class-rid), excepted_body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_remove_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_reset_mass_properties**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_axis_lock**(body: [RID](class_rid.md#class-rid), axis: [BodyAxis](class_physicsserver3d.md#enum-physicsserver3d-bodyaxis), lock: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_axis_velocity**(body: [RID](class_rid.md#class-rid), axis_velocity: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_collision_layer**(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_collision_mask**(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_collision_priority**(body: [RID](class_rid.md#class-rid), priority: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_constant_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_constant_torque**(body: [RID](class_rid.md#class-rid), torque: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_contacts_reported_depth_threshold**(body: [RID](class_rid.md#class-rid), threshold: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_enable_continuous_collision_detection**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_force_integration_callback**(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable), userdata: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_max_contacts_reported**(body: [RID](class_rid.md#class-rid), amount: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_mode**(body: [RID](class_rid.md#class-rid), mode: [BodyMode](class_physicsserver3d.md#enum-physicsserver3d-bodymode))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_omit_force_integration**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_param**(body: [RID](class_rid.md#class-rid), param: [BodyParameter](class_physicsserver3d.md#enum-physicsserver3d-bodyparameter), value: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_ray_pickable**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_shape**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), shape: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_shape_disabled**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_shape_transform**(body: [RID](class_rid.md#class-rid), shape_idx: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_space**(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate), value: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_state_sync_callback**(body: [RID](class_rid.md#class-rid), callable: [Callable](class_callable.md#class-callable))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_body_set_user_flags**(body: [RID](class_rid.md#class-rid), flags: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_body_test_motion**(body: [RID](class_rid.md#class-rid), from: [Transform3D](class_transform3d.md#class-transform3d), motion: [Vector3](class_vector3.md#class-vector3), margin: [float](class_float.md#class-float), max_collisions: [int](class_int.md#class-int), collide_separation_ray: [bool](class_bool.md#class-bool), recovery_as_collision: [bool](class_bool.md#class-bool), r_result: `PhysicsServer3DExtensionMotionResult*`)

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_box_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_capsule_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_concave_polygon_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_cone_twist_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [ConeTwistJointParam](class_physicsserver3d.md#enum-physicsserver3d-conetwistjointparam))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_cone_twist_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [ConeTwistJointParam](class_physicsserver3d.md#enum-physicsserver3d-conetwistjointparam), value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_convex_polygon_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_custom_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_cylinder_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_end_sync**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_finish**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_flush_queries**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_free_rid**(rid: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_generic_6dof_joint_get_flag**(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisflag))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_generic_6dof_joint_get_param**(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisparam))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_generic_6dof_joint_set_flag**(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisflag), enable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_generic_6dof_joint_set_param**(joint: [RID](class_rid.md#class-rid), axis: [Axis](class_vector3.md#enum-vector3-axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum-physicsserver3d-g6dofjointaxisparam), value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_get_process_info**(process_info: [ProcessInfo](class_physicsserver3d.md#enum-physicsserver3d-processinfo))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_heightmap_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_hinge_joint_get_flag**(joint: [RID](class_rid.md#class-rid), flag: [HingeJointFlag](class_physicsserver3d.md#enum-physicsserver3d-hingejointflag))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_hinge_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [HingeJointParam](class_physicsserver3d.md#enum-physicsserver3d-hingejointparam))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_hinge_joint_set_flag**(joint: [RID](class_rid.md#class-rid), flag: [HingeJointFlag](class_physicsserver3d.md#enum-physicsserver3d-hingejointflag), enabled: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_hinge_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [HingeJointParam](class_physicsserver3d.md#enum-physicsserver3d-hingejointparam), value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_init**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_is_flushing_queries**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_clear**(joint: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_joint_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_disable_collisions_between_bodies**(joint: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_joint_get_solver_priority**(joint: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[JointType](class_physicsserver3d.md#enum-physicsserver3d-jointtype) **\_joint_get_type**(joint: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_joint_is_disabled_collisions_between_bodies**(joint: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_make_cone_twist**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_make_generic_6dof**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_make_hinge**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), hinge_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), hinge_B: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_make_hinge_simple**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), pivot_A: [Vector3](class_vector3.md#class-vector3), axis_A: [Vector3](class_vector3.md#class-vector3), body_B: [RID](class_rid.md#class-rid), pivot_B: [Vector3](class_vector3.md#class-vector3), axis_B: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_make_pin**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_A: [Vector3](class_vector3.md#class-vector3), body_B: [RID](class_rid.md#class-rid), local_B: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_make_slider**(joint: [RID](class_rid.md#class-rid), body_A: [RID](class_rid.md#class-rid), local_ref_A: [Transform3D](class_transform3d.md#class-transform3d), body_B: [RID](class_rid.md#class-rid), local_ref_B: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_joint_set_solver_priority**(joint: [RID](class_rid.md#class-rid), priority: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_pin_joint_get_local_a**(joint: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_pin_joint_get_local_b**(joint: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_pin_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver3d.md#enum-physicsserver3d-pinjointparam))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_pin_joint_set_local_a**(joint: [RID](class_rid.md#class-rid), local_A: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_pin_joint_set_local_b**(joint: [RID](class_rid.md#class-rid), local_B: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_pin_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [PinJointParam](class_physicsserver3d.md#enum-physicsserver3d-pinjointparam), value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_separation_ray_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_set_active**(active: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_shape_get_custom_solver_bias**(shape: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Variant](class_variant.md#class-variant) **\_shape_get_data**(shape: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_shape_get_margin**(shape: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[ShapeType](class_physicsserver3d.md#enum-physicsserver3d-shapetype) **\_shape_get_type**(shape: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_shape_set_custom_solver_bias**(shape: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_shape_set_data**(shape: [RID](class_rid.md#class-rid), data: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_shape_set_margin**(shape: [RID](class_rid.md#class-rid), margin: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_slider_joint_get_param**(joint: [RID](class_rid.md#class-rid), param: [SliderJointParam](class_physicsserver3d.md#enum-physicsserver3d-sliderjointparam))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_slider_joint_set_param**(joint: [RID](class_rid.md#class-rid), param: [SliderJointParam](class_physicsserver3d.md#enum-physicsserver3d-sliderjointparam), value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_add_collision_exception**(body: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_apply_central_force**(body: [RID](class_rid.md#class-rid), force: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_apply_central_impulse**(body: [RID](class_rid.md#class-rid), impulse: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_apply_point_force**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), force: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_apply_point_impulse**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), impulse: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_soft_body_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[AABB](class_aabb.md#class-aabb) **\_soft_body_get_bounds**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **\_soft_body_get_collision_exceptions**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_soft_body_get_collision_layer**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_soft_body_get_collision_mask**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_soft_body_get_damping_coefficient**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_soft_body_get_drag_coefficient**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_soft_body_get_linear_stiffness**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector3](class_vector3.md#class-vector3) **\_soft_body_get_point_global_position**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_soft_body_get_pressure_coefficient**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_soft_body_get_shrinking_factor**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_soft_body_get_simulation_precision**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_soft_body_get_space**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Variant](class_variant.md#class-variant) **\_soft_body_get_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_soft_body_get_total_mass**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_soft_body_is_point_pinned**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_move_point**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), global_position: [Vector3](class_vector3.md#class-vector3))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_pin_point**(body: [RID](class_rid.md#class-rid), point_index: [int](class_int.md#class-int), pin: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_remove_all_pinned_points**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_remove_collision_exception**(body: [RID](class_rid.md#class-rid), body_b: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_collision_layer**(body: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_collision_mask**(body: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_damping_coefficient**(body: [RID](class_rid.md#class-rid), damping_coefficient: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_drag_coefficient**(body: [RID](class_rid.md#class-rid), drag_coefficient: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_linear_stiffness**(body: [RID](class_rid.md#class-rid), linear_stiffness: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_mesh**(body: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_pressure_coefficient**(body: [RID](class_rid.md#class-rid), pressure_coefficient: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_ray_pickable**(body: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_shrinking_factor**(body: [RID](class_rid.md#class-rid), shrinking_factor: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_simulation_precision**(body: [RID](class_rid.md#class-rid), simulation_precision: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_space**(body: [RID](class_rid.md#class-rid), space: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_state**(body: [RID](class_rid.md#class-rid), state: [BodyState](class_physicsserver3d.md#enum-physicsserver3d-bodystate), variant: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_total_mass**(body: [RID](class_rid.md#class-rid), total_mass: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_set_transform**(body: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_soft_body_update_rendering_server**(body: [RID](class_rid.md#class-rid), rendering_server_handler: [PhysicsServer3DRenderingServerHandler](class_physicsserver3drenderingserverhandler.md#class-physicsserver3drenderingserverhandler))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_space_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_space_get_contact_count**(space: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **\_space_get_contacts**(space: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **\_space_get_direct_state**(space: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **\_space_get_param**(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver3d.md#enum-physicsserver3d-spaceparameter))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_space_is_active**(space: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_space_set_active**(space: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_space_set_debug_contacts**(space: [RID](class_rid.md#class-rid), max_contacts: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_space_set_param**(space: [RID](class_rid.md#class-rid), param: [SpaceParameter](class_physicsserver3d.md#enum-physicsserver3d-spaceparameter), value: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_sphere_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_step**(step: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_sync**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **\_world_boundary_shape_create**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **body_test_motion_is_excluding_body**(body: [RID](class_rid.md#class-rid))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **body_test_motion_is_excluding_object**(object: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
