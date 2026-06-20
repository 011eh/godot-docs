# JavaClass

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a class from the Java Native Interface.

## Description

Represents a class from the Java Native Interface. It is returned from [JavaClassWrapper.wrap()](class_javaclasswrapper.md#class-javaclasswrapper-method-wrap).

**Note:** This class only works on Android. On any other platform, this class does nothing.

**Note:** This class is not to be confused with [JavaScriptObject](class_javascriptobject.md#class-javascriptobject).

## Methods

| [String](class_string.md#class-string)                                                  | get_java_class_name()                                                   |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | get_java_method_list()                                                 |
| JavaClass                                                           | get_java_parent_class()                                               |
| [bool](class_bool.md#class-bool)                                                        | has_java_method(method: [StringName](class_stringname.md#class-stringname)) |

---

## Method Descriptions

[String](class_string.md#class-string) **get_java_class_name**()

Returns the Java class name.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_java_method_list**()

Returns the object's Java methods and their signatures as an [Array](class_array.md#class-array) of dictionaries, in the same format as [Object.get_method_list()](class_object.md#class-object-method-get-method-list).

---

JavaClass **get_java_parent_class**()

Returns a **JavaClass** representing the Java parent class of this class.

---

[bool](class_bool.md#class-bool) **has_java_method**(method: [StringName](class_stringname.md#class-stringname))

Returns `true` if the given `method` name exists in the object's Java methods.
