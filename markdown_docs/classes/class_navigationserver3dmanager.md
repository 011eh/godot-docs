# NavigationServer3DManager

**Inherits:** [Object](class_object.md#class-object)

A singleton for managing [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) implementations.

## Description

**NavigationServer3DManager** is the API for registering [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) implementations and setting the default implementation.

**Note:** It is not possible to switch servers at runtime. This class is only used on startup at the server initialization level.

## Methods

|    | register_server(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable))   |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | set_default_server(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int))                   |

---

## Method Descriptions

 **register_server**(name: [String](class_string.md#class-string), create_callback: [Callable](class_callable.md#class-callable))

Registers a [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) implementation by passing a `name` and a [Callable](class_callable.md#class-callable) that returns a [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) object.

---

 **set_default_server**(name: [String](class_string.md#class-string), priority: [int](class_int.md#class-int))

Sets the default [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d) implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.
