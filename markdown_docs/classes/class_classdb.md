# ClassDB

**Inherits:** [Object](class_object.md#class-object)

A class information repository.

## Description

Provides access to metadata stored for every available engine class.

**Note:** Script-defined classes with `class_name` are not part of **ClassDB**, so they will not return reflection data such as a method or property list. However, [GDExtension](class_gdextension.md#class-gdextension)-defined classes *are* part of **ClassDB**, so they will return reflection data.

## Methods

| [bool](class_bool.md#class-bool)                                                        | can_instantiate(class: [StringName](class_stringname.md#class-stringname))                                                                                                                                                       |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Variant](class_variant.md#class-variant)                                               | class_call_static(class: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), ...)                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | class_exists(class: [StringName](class_stringname.md#class-stringname))                                                                                                                                                             |
| APIType                                                        | class_get_api_type(class: [StringName](class_stringname.md#class-stringname))                                                                                                                                                 |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | class_get_enum_constants(class: [StringName](class_stringname.md#class-stringname), enum: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                 |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | class_get_enum_list(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                                                                                     |
| [int](class_int.md#class-int)                                                           | class_get_integer_constant(class: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))                                                                       |
| [StringName](class_stringname.md#class-stringname)                                      | class_get_integer_constant_enum(class: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | class_get_integer_constant_list(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                                                             |
| [int](class_int.md#class-int)                                                           | class_get_method_argument_count(class: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false) |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | class_get_method_list(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                                                                                 |
| [Variant](class_variant.md#class-variant)                                               | class_get_property(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname))                                                                                              |
| [Variant](class_variant.md#class-variant)                                               | class_get_property_default_value(class: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname))                                                       |
| [StringName](class_stringname.md#class-stringname)                                      | class_get_property_getter(class: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname))                                                                     |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | class_get_property_list(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                                                                             |
| [StringName](class_stringname.md#class-stringname)                                      | class_get_property_setter(class: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname))                                                                     |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | class_get_signal(class: [StringName](class_stringname.md#class-stringname), signal: [StringName](class_stringname.md#class-stringname))                                                                                         |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | class_get_signal_list(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | class_has_enum(class: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                                     |
| [bool](class_bool.md#class-bool)                                                        | class_has_integer_constant(class: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))                                                                       |
| [bool](class_bool.md#class-bool)                                                        | class_has_method(class: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                               |
| [bool](class_bool.md#class-bool)                                                        | class_has_signal(class: [StringName](class_stringname.md#class-stringname), signal: [StringName](class_stringname.md#class-stringname))                                                                                         |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | class_set_property(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                            |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | get_class_list()                                                                                                                                                                                                                  |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | get_inheriters_from_class(class: [StringName](class_stringname.md#class-stringname))                                                                                                                                   |
| [StringName](class_stringname.md#class-stringname)                                      | get_parent_class(class: [StringName](class_stringname.md#class-stringname))                                                                                                                                                     |
| [Variant](class_variant.md#class-variant)                                               | instantiate(class: [StringName](class_stringname.md#class-stringname))                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | is_class_enabled(class: [StringName](class_stringname.md#class-stringname))                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | is_class_enum_bitfield(class: [StringName](class_stringname.md#class-stringname), enum: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)                     |
| [bool](class_bool.md#class-bool)                                                        | is_parent_class(class: [StringName](class_stringname.md#class-stringname), inherits: [StringName](class_stringname.md#class-stringname))                                                                                         |

---

## Enumerations

enum **APIType**:

APIType **API_CORE** = `0`

Native Core class type.

APIType **API_EDITOR** = `1`

Native Editor class type.

APIType **API_EXTENSION** = `2`

GDExtension class type.

APIType **API_EDITOR_EXTENSION** = `3`

GDExtension Editor class type.

APIType **API_NONE** = `4`

Unknown class type.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **can_instantiate**(class: [StringName](class_stringname.md#class-stringname))

Returns `true` if objects can be instantiated from the specified `class`, otherwise returns `false`.

---

[Variant](class_variant.md#class-variant) **class_call_static**(class: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), ...)

Calls a static method on a class.

---

[bool](class_bool.md#class-bool) **class_exists**(class: [StringName](class_stringname.md#class-stringname))

Returns whether the specified `class` is available or not.

---

APIType **class_get_api_type**(class: [StringName](class_stringname.md#class-stringname))

Returns the API type of the specified `class`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **class_get_enum_constants**(class: [StringName](class_stringname.md#class-stringname), enum: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns an array with all the keys in `enum` of `class` or its ancestry.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **class_get_enum_list**(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns an array with all the enums of `class` or its ancestry.

---

[int](class_int.md#class-int) **class_get_integer_constant**(class: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))

Returns the value of the integer constant `name` of `class` or its ancestry. Always returns 0 when the constant could not be found.

---

[StringName](class_stringname.md#class-stringname) **class_get_integer_constant_enum**(class: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns which enum the integer constant `name` of `class` or its ancestry belongs to.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **class_get_integer_constant_list**(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns an array with the names all the integer constants of `class` or its ancestry.

---

[int](class_int.md#class-int) **class_get_method_argument_count**(class: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns the number of arguments of the method `method` of `class` or its ancestry if `no_inheritance` is `false`.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **class_get_method_list**(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns an array with all the methods of `class` or its ancestry if `no_inheritance` is `false`. Every element of the array is a [Dictionary](class_dictionary.md#class-dictionary) with the following keys: `args`, `default_args`, `flags`, `id`, `name`, `return: (class_name, hint, hint_string, name, type, usage)`.

**Note:** In exported release builds the debug info is not available, so the returned dictionaries will contain only method names.

---

[Variant](class_variant.md#class-variant) **class_get_property**(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname))

Returns the value of `property` of `object` or its ancestry.

---

[Variant](class_variant.md#class-variant) **class_get_property_default_value**(class: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname))

Returns the default value of `property` of `class` or its ancestor classes.

---

[StringName](class_stringname.md#class-stringname) **class_get_property_getter**(class: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname))

Returns the getter method name of `property` of `class`.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **class_get_property_list**(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns an array with all the properties of `class` or its ancestry if `no_inheritance` is `false`.

---

[StringName](class_stringname.md#class-stringname) **class_get_property_setter**(class: [StringName](class_stringname.md#class-stringname), property: [StringName](class_stringname.md#class-stringname))

Returns the setter method name of `property` of `class`.

---

[Dictionary](class_dictionary.md#class-dictionary) **class_get_signal**(class: [StringName](class_stringname.md#class-stringname), signal: [StringName](class_stringname.md#class-stringname))

Returns the `signal` data of `class` or its ancestry. The returned value is a [Dictionary](class_dictionary.md#class-dictionary) with the following keys: `args`, `default_args`, `flags`, `id`, `name`, `return: (class_name, hint, hint_string, name, type, usage)`.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **class_get_signal_list**(class: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns an array with all the signals of `class` or its ancestry if `no_inheritance` is `false`. Every element of the array is a [Dictionary](class_dictionary.md#class-dictionary) as described in class_get_signal().

---

[bool](class_bool.md#class-bool) **class_has_enum**(class: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns whether `class` or its ancestry has an enum called `name` or not.

---

[bool](class_bool.md#class-bool) **class_has_integer_constant**(class: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))

Returns whether `class` or its ancestry has an integer constant called `name` or not.

---

[bool](class_bool.md#class-bool) **class_has_method**(class: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns whether `class` (or its ancestry if `no_inheritance` is `false`) has a method called `method` or not.

---

[bool](class_bool.md#class-bool) **class_has_signal**(class: [StringName](class_stringname.md#class-stringname), signal: [StringName](class_stringname.md#class-stringname))

Returns whether `class` or its ancestry has a signal called `signal` or not.

---

[Error](class_@globalscope.md#enum-globalscope-error) **class_set_property**(object: [Object](class_object.md#class-object), property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Sets `property` value of `object` to `value`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_class_list**()

Returns the names of all engine classes available.

**Note:** Script-defined classes with `class_name` are not included in this list. Use [ProjectSettings.get_global_class_list()](class_projectsettings.md#class-projectsettings-method-get-global-class-list) to get a list of script-defined classes instead.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_inheriters_from_class**(class: [StringName](class_stringname.md#class-stringname))

Returns the names of all engine classes that directly or indirectly inherit from `class`.

---

[StringName](class_stringname.md#class-stringname) **get_parent_class**(class: [StringName](class_stringname.md#class-stringname))

Returns the parent class of `class`.

---

[Variant](class_variant.md#class-variant) **instantiate**(class: [StringName](class_stringname.md#class-stringname))

Creates an instance of `class`.

---

[bool](class_bool.md#class-bool) **is_class_enabled**(class: [StringName](class_stringname.md#class-stringname))

Returns whether this `class` is enabled or not.

---

[bool](class_bool.md#class-bool) **is_class_enum_bitfield**(class: [StringName](class_stringname.md#class-stringname), enum: [StringName](class_stringname.md#class-stringname), no_inheritance: [bool](class_bool.md#class-bool) = false)

Returns whether `class` (or its ancestor classes if `no_inheritance` is `false`) has an enum called `enum` that is a bitfield.

---

[bool](class_bool.md#class-bool) **is_parent_class**(class: [StringName](class_stringname.md#class-stringname), inherits: [StringName](class_stringname.md#class-stringname))

Returns whether `inherits` is an ancestor of `class` or not.
