# World3D

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A resource that holds all components of a 3D world, such as a visual scenario and a physics space.

## Description

Class that has everything pertaining to a world: A physics space, a visual scenario, and a sound space. 3D nodes register their resources into the current 3D world.

## Tutorials

- [Ray-casting](../tutorials/physics/ray-casting.md)

## Properties

| [CameraAttributes](class_cameraattributes.md#class-cameraattributes)                            | camera_attributes       |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) | direct_space_state     |
| [Environment](class_environment.md#class-environment)                                           | environment                   |
| [Environment](class_environment.md#class-environment)                                           | fallback_environment |
| [RID](class_rid.md#class-rid)                                                                   | navigation_map             |
| [RID](class_rid.md#class-rid)                                                                   | scenario                         |
| [RID](class_rid.md#class-rid)                                                                   | space                               |

---

## Property Descriptions

[CameraAttributes](class_cameraattributes.md#class-cameraattributes) **camera_attributes**

-  **set_camera_attributes**(value: [CameraAttributes](class_cameraattributes.md#class-cameraattributes))
- [CameraAttributes](class_cameraattributes.md#class-cameraattributes) **get_camera_attributes**()

The default [CameraAttributes](class_cameraattributes.md#class-cameraattributes) resource to use if none set on the [Camera3D](class_camera3d.md#class-camera3d).

---

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **direct_space_state**

- [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class-physicsdirectspacestate3d) **get_direct_space_state**()

Direct access to the world's physics 3D space state. Used for querying current and potential collisions. When using multi-threaded physics, access is limited to [Node._physics_process()](class_node.md#class-node-private-method-physics-process) in the main thread.

---

[Environment](class_environment.md#class-environment) **environment**

-  **set_environment**(value: [Environment](class_environment.md#class-environment))
- [Environment](class_environment.md#class-environment) **get_environment**()

The World3D's [Environment](class_environment.md#class-environment).

---

[Environment](class_environment.md#class-environment) **fallback_environment**

-  **set_fallback_environment**(value: [Environment](class_environment.md#class-environment))
- [Environment](class_environment.md#class-environment) **get_fallback_environment**()

The World3D's fallback environment will be used if environment fails or is missing.

---

[RID](class_rid.md#class-rid) **navigation_map**

- [RID](class_rid.md#class-rid) **get_navigation_map**()

The [RID](class_rid.md#class-rid) of this world's navigation map. Used by the [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d).

---

[RID](class_rid.md#class-rid) **scenario**

- [RID](class_rid.md#class-rid) **get_scenario**()

The World3D's visual scenario.

---

[RID](class_rid.md#class-rid) **space**

- [RID](class_rid.md#class-rid) **get_space**()

The World3D's physics space.
