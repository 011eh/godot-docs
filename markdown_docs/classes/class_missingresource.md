# MissingResource

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An internal editor class intended for keeping the data of unrecognized resources.

## Description

This is an internal editor class intended for keeping data of resources of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

**Warning:** Ignore missing resources unless you know what you are doing. Existing properties on a missing resource can be freely modified in code, regardless of the type they are intended to be.

## Properties

| [String](class_string.md#class-string)   | original_class             |
|------------------------------------------|------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)         | recording_properties |

---

## Property Descriptions

[String](class_string.md#class-string) **original_class**

-  **set_original_class**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_original_class**()

The name of the class this resource was supposed to be (see [Object.get_class()](class_object.md#class-object-method-get-class)).

---

[bool](class_bool.md#class-bool) **recording_properties**

-  **set_recording_properties**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_recording_properties**()

If set to `true`, allows new properties to be added on top of the existing ones with [Object.set()](class_object.md#class-object-method-set).
