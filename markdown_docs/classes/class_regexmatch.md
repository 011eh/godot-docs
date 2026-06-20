# RegExMatch

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Contains the results of a [RegEx](class_regex.md#class-regex) search.

## Description

Contains the results of a single [RegEx](class_regex.md#class-regex) match returned by [RegEx.search()](class_regex.md#class-regex-method-search) and [RegEx.search_all()](class_regex.md#class-regex-method-search-all). It can be used to find the position and range of the match and its capturing groups, and it can extract its substring for you.

## Properties

| [Dictionary](class_dictionary.md#class-dictionary)                      | names     | `{}`                  |
|-------------------------------------------------------------------------|-----------------------------------------------|-----------------------|
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | strings | `PackedStringArray()` |
| [String](class_string.md#class-string)                                  | subject | `""`                  |

## Methods

| [int](class_int.md#class-int)          | get_end(name: [Variant](class_variant.md#class-variant) = 0)       |
|----------------------------------------|--------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)          | get_group_count()                                          |
| [int](class_int.md#class-int)          | get_start(name: [Variant](class_variant.md#class-variant) = 0)   |
| [String](class_string.md#class-string) | get_string(name: [Variant](class_variant.md#class-variant) = 0) |

---

## Property Descriptions

[Dictionary](class_dictionary.md#class-dictionary) **names** = `{}`

- [Dictionary](class_dictionary.md#class-dictionary) **get_names**()

A dictionary of named groups and its corresponding group number. Only groups that were matched are included. If multiple groups have the same name, that name would refer to the first matching one.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **strings** = `PackedStringArray()`

- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_strings**()

An [Array](class_array.md#class-array) of the match and its capturing groups.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

[String](class_string.md#class-string) **subject** = `""`

- [String](class_string.md#class-string) **get_subject**()

The source string used with the search pattern to find this matching result.

---

## Method Descriptions

[int](class_int.md#class-int) **get_end**(name: [Variant](class_variant.md#class-variant) = 0)

Returns the end position of the match within the source string. The end position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.

---

[int](class_int.md#class-int) **get_group_count**()

Returns the number of capturing groups.

---

[int](class_int.md#class-int) **get_start**(name: [Variant](class_variant.md#class-variant) = 0)

Returns the starting position of the match within the source string. The starting position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.

---

[String](class_string.md#class-string) **get_string**(name: [Variant](class_variant.md#class-variant) = 0)

Returns the substring of the match from the source string. Capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns an empty string if the group did not match or doesn't exist.
