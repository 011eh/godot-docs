# OpenXRStructureBase

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRSpatialContextPersistenceConfig](class_openxrspatialcontextpersistenceconfig.md#class-openxrspatialcontextpersistenceconfig)

Object for storing OpenXR structure data.

## Description

Object for storing OpenXR structure data that is passed when calling into OpenXR APIs.

## Properties

| OpenXRStructureBase   | next   |
|-----------------------------------------------------|----------------------------------------------------|

## Methods

| [int](class_int.md#class-int)   | \_get_header(next: [int](class_int.md#class-int))    |
|---------------------------------|--------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)   | get_structure_type()                                 |

---

## Property Descriptions

OpenXRStructureBase **next**

-  **set_next**(value: OpenXRStructureBase)
- OpenXRStructureBase **get_next**()

Setting another structure object here chains these structures together to extend the API functionality. Consult the OpenXR documentation for which structures can be used with a given API call.

---

## Method Descriptions

[int](class_int.md#class-int) **\_get_header**(next: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **get_structure_type**()

Returns the structure type (OpenXR `XrStructureType`) used for this structure.
