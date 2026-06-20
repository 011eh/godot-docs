# JavaObject

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents an object from the Java Native Interface.

## Description

Represents an object from the Java Native Interface. It can be returned from Java methods called on [JavaClass](class_javaclass.md#class-javaclass) or other **JavaObject**s. See [JavaClassWrapper](class_javaclasswrapper.md#class-javaclasswrapper) for an example.

**Note:** This class only works on Android. On any other platform, this class does nothing.

**Note:** This class is not to be confused with [JavaScriptObject](class_javascriptobject.md#class-javascriptobject).

## Methods

| [JavaClass](class_javaclass.md#class-javaclass)   | get_java_class()                                                             |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                  | has_java_method(method: [StringName](class_stringname.md#class-stringname)) |

---

## Method Descriptions

[JavaClass](class_javaclass.md#class-javaclass) **get_java_class**()

Returns the [JavaClass](class_javaclass.md#class-javaclass) that this object is an instance of.

---

[bool](class_bool.md#class-bool) **has_java_method**(method: [StringName](class_stringname.md#class-stringname))

Returns `true` if the given `method` name exists in the object's Java methods.
