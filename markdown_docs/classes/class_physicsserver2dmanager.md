# PhysicsServer2DManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementations.

## Description

**PhysicsServer2DManager** is the API for registering [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementations and for setting the default implementation.

**Note:** It is not possible to switch physics servers at runtime. This class is only used on startup at the server initialization level, by Godot itself and possibly by GDExtensions.

## Methods

|    | register_server(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable))   |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | set_default_server(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int))                   |

---

## Method Descriptions

 **register_server**(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable))

Register a [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementation by passing a `name` and a [Callable](class_callable.md#class-callable) that returns a [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) object.

---

 **set_default_server**(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int))

Set the default [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
