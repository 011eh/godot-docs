# PhysicsServer3DManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementations.

## Description

**PhysicsServer3DManager** is the API for registering [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementations and for setting the default implementation.

**Note:** It is not possible to switch physics servers at runtime. This class is only used on startup at the server initialization level, by Godot itself and possibly by GDExtensions.

## Methods

|    | register_server(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable))   |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | set_default_server(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int))                   |

---

## Method Descriptions

 **register_server**(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable))

Register a [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementation by passing a `name` and a [Callable](class_callable.md#class-callable) that returns a [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) object.

---

 **set_default_server**(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int))

Set the default [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
