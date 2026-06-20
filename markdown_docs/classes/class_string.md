# String

A built-in type for strings.

## Description

This is the built-in string Variant type (and the one used by GDScript). Strings may contain any number of Unicode characters, and expose methods useful for manipulating and generating strings. Strings are reference-counted and use a copy-on-write approach (every modification to a string returns a new **String**), so passing them around is cheap in resources.

Some string methods have corresponding variations. Variations suffixed with `n` (countn(), findn(), replacen(), etc.) are **case-insensitive** (they make no distinction between uppercase and lowercase letters). Method variations prefixed with `r` (rfind(), rsplit(), etc.) are reversed, and start from the end of the string, instead of the beginning.

To convert any [Variant](class_variant.md#class-variant) to or from a string, see [@GlobalScope.str()](class_@globalscope.md#class-globalscope-method-str), [@GlobalScope.str_to_var()](class_@globalscope.md#class-globalscope-method-str-to-var), and [@GlobalScope.var_to_str()](class_@globalscope.md#class-globalscope-method-var-to-str).

**Note:** In a boolean context, a string will evaluate to `false` if it is empty (`""`). Otherwise, a string will always evaluate to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Tutorials

- [GDScript format strings](../tutorials/scripting/gdscript/gdscript_format_string.md)

## Constructors

| String   | String()                                                         |
|---------------------------|------------------------------------------------------------------------------------------------------|
| String   | String(from: String)                            |
| String   | String(from: [NodePath](class_nodepath.md#class-nodepath))       |
| String   | String(from: [StringName](class_stringname.md#class-stringname)) |

## Methods

| [bool](class_bool.md#class-bool)                                           | begins_with(text: String)                                                                                                           |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)    | bigrams()                                                                                                                                                |
| [int](class_int.md#class-int)                                              | bin_to_int()                                                                                                                                          |
| String                                                    | c_escape()                                                                                                                                              |
| String                                                    | c_unescape()                                                                                                                                          |
| String                                                    | capitalize()                                                                                                                                          |
| [int](class_int.md#class-int)                                              | casecmp_to(to: String)                                                                                                               |
| String                                                    | chr(code: [int](class_int.md#class-int))                                                                                                                     |
| [bool](class_bool.md#class-bool)                                           | contains(what: String)                                                                                                                 |
| [bool](class_bool.md#class-bool)                                           | containsn(what: String)                                                                                                               |
| [int](class_int.md#class-int)                                              | count(what: String, from: [int](class_int.md#class-int) = 0, to: [int](class_int.md#class-int) = 0)                                       |
| [int](class_int.md#class-int)                                              | countn(what: String, from: [int](class_int.md#class-int) = 0, to: [int](class_int.md#class-int) = 0)                                     |
| String                                                    | dedent()                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                           | ends_with(text: String)                                                                                                               |
| String                                                    | erase(position: [int](class_int.md#class-int), chars: [int](class_int.md#class-int) = 1)                                                                   |
| [int](class_int.md#class-int)                                              | filecasecmp_to(to: String)                                                                                                       |
| [int](class_int.md#class-int)                                              | filenocasecmp_to(to: String)                                                                                                   |
| [int](class_int.md#class-int)                                              | find(what: String, from: [int](class_int.md#class-int) = 0)                                                                                |
| [int](class_int.md#class-int)                                              | findn(what: String, from: [int](class_int.md#class-int) = 0)                                                                              |
| String                                                    | format(values: [Variant](class_variant.md#class-variant), placeholder: String = "{_}")                                                   |
| String                                                    | get_base_dir()                                                                                                                                      |
| String                                                    | get_basename()                                                                                                                                      |
| String                                                    | get_extension()                                                                                                                                    |
| String                                                    | get_file()                                                                                                                                              |
| String                                                    | get_slice(delimiter: String, slice: [int](class_int.md#class-int))                                                                    |
| [int](class_int.md#class-int)                                              | get_slice_count(delimiter: String)                                                                                              |
| String                                                    | get_slicec(delimiter: [int](class_int.md#class-int), slice: [int](class_int.md#class-int))                                                            |
| [int](class_int.md#class-int)                                              | hash()                                                                                                                                                      |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | hex_decode()                                                                                                                                          |
| [int](class_int.md#class-int)                                              | hex_to_int()                                                                                                                                          |
| String                                                    | humanize_size(size: [int](class_int.md#class-int))                                                                                                 |
| String                                                    | indent(prefix: String)                                                                                                                   |
| String                                                    | insert(position: [int](class_int.md#class-int), what: String)                                                                            |
| [bool](class_bool.md#class-bool)                                           | is_absolute_path()                                                                                                                              |
| [bool](class_bool.md#class-bool)                                           | is_empty()                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                           | is_relative_path()                                                                                                                              |
| [bool](class_bool.md#class-bool)                                           | is_subsequence_of(text: String)                                                                                               |
| [bool](class_bool.md#class-bool)                                           | is_subsequence_ofn(text: String)                                                                                             |
| [bool](class_bool.md#class-bool)                                           | is_valid_ascii_identifier()                                                                                                            |
| [bool](class_bool.md#class-bool)                                           | is_valid_filename()                                                                                                                            |
| [bool](class_bool.md#class-bool)                                           | is_valid_float()                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                           | is_valid_hex_number(with_prefix: [bool](class_bool.md#class-bool) = false)                                                                   |
| [bool](class_bool.md#class-bool)                                           | is_valid_html_color()                                                                                                                        |
| [bool](class_bool.md#class-bool)                                           | is_valid_identifier()                                                                                                                        |
| [bool](class_bool.md#class-bool)                                           | is_valid_int()                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                           | is_valid_ip_address()                                                                                                                        |
| [bool](class_bool.md#class-bool)                                           | is_valid_unicode_identifier()                                                                                                        |
| String                                                    | join(parts: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                                                        |
| String                                                    | json_escape()                                                                                                                                        |
| String                                                    | left(length: [int](class_int.md#class-int))                                                                                                                 |
| [int](class_int.md#class-int)                                              | length()                                                                                                                                                  |
| String                                                    | lpad(min_length: [int](class_int.md#class-int), character: String = " ")                                                                   |
| String                                                    | lstrip(chars: String)                                                                                                                    |
| [bool](class_bool.md#class-bool)                                           | match(expr: String)                                                                                                                       |
| [bool](class_bool.md#class-bool)                                           | matchn(expr: String)                                                                                                                     |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | md5_buffer()                                                                                                                                          |
| String                                                    | md5_text()                                                                                                                                              |
| [int](class_int.md#class-int)                                              | naturalcasecmp_to(to: String)                                                                                                 |
| [int](class_int.md#class-int)                                              | naturalnocasecmp_to(to: String)                                                                                             |
| [int](class_int.md#class-int)                                              | nocasecmp_to(to: String)                                                                                                           |
| String                                                    | num(number: [float](class_float.md#class-float), decimals: [int](class_int.md#class-int) = -1)                                                               |
| String                                                    | num_int64(number: [int](class_int.md#class-int), base: [int](class_int.md#class-int) = 10, capitalize_hex: [bool](class_bool.md#class-bool) = false)   |
| String                                                    | num_scientific(number: [float](class_float.md#class-float))                                                                                       |
| String                                                    | num_uint64(number: [int](class_int.md#class-int), base: [int](class_int.md#class-int) = 10, capitalize_hex: [bool](class_bool.md#class-bool) = false) |
| String                                                    | pad_decimals(digits: [int](class_int.md#class-int))                                                                                                 |
| String                                                    | pad_zeros(digits: [int](class_int.md#class-int))                                                                                                       |
| String                                                    | path_join(path: String)                                                                                                               |
| String                                                    | remove_char(what: [int](class_int.md#class-int))                                                                                                     |
| String                                                    | remove_chars(chars: String)                                                                                                        |
| String                                                    | repeat(count: [int](class_int.md#class-int))                                                                                                              |
| String                                                    | replace(what: String, forwhat: String)                                                                                 |
| String                                                    | replace_char(key: [int](class_int.md#class-int), with: [int](class_int.md#class-int))                                                               |
| String                                                    | replace_chars(keys: String, with: [int](class_int.md#class-int))                                                                  |
| String                                                    | replacen(what: String, forwhat: String)                                                                               |
| String                                                    | reverse()                                                                                                                                                |
| [int](class_int.md#class-int)                                              | rfind(what: String, from: [int](class_int.md#class-int) = -1)                                                                             |
| [int](class_int.md#class-int)                                              | rfindn(what: String, from: [int](class_int.md#class-int) = -1)                                                                           |
| String                                                    | right(length: [int](class_int.md#class-int))                                                                                                               |
| String                                                    | rpad(min_length: [int](class_int.md#class-int), character: String = " ")                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)    | rsplit(delimiter: String = "", allow_empty: [bool](class_bool.md#class-bool) = true, maxsplit: [int](class_int.md#class-int) = 0)        |
| String                                                    | rstrip(chars: String)                                                                                                                    |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | sha1_buffer()                                                                                                                                        |
| String                                                    | sha1_text()                                                                                                                                            |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | sha256_buffer()                                                                                                                                    |
| String                                                    | sha256_text()                                                                                                                                        |
| [float](class_float.md#class-float)                                        | similarity(text: String)                                                                                                             |
| String                                                    | simplify_path()                                                                                                                                    |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)    | split(delimiter: String = "", allow_empty: [bool](class_bool.md#class-bool) = true, maxsplit: [int](class_int.md#class-int) = 0)          |
| [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) | split_floats(delimiter: String, allow_empty: [bool](class_bool.md#class-bool) = true)                                              |
| String                                                    | strip_edges(left: [bool](class_bool.md#class-bool) = true, right: [bool](class_bool.md#class-bool) = true)                                           |
| String                                                    | strip_escapes()                                                                                                                                    |
| String                                                    | substr(from: [int](class_int.md#class-int), len: [int](class_int.md#class-int) = -1)                                                                      |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | to_ascii_buffer()                                                                                                                                |
| String                                                    | to_camel_case()                                                                                                                                    |
| [float](class_float.md#class-float)                                        | to_float()                                                                                                                                              |
| [int](class_int.md#class-int)                                              | to_int()                                                                                                                                                  |
| String                                                    | to_kebab_case()                                                                                                                                    |
| String                                                    | to_lower()                                                                                                                                              |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | to_multibyte_char_buffer(encoding: String = "")                                                                        |
| String                                                    | to_pascal_case()                                                                                                                                  |
| String                                                    | to_snake_case()                                                                                                                                    |
| String                                                    | to_upper()                                                                                                                                              |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | to_utf8_buffer()                                                                                                                                  |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | to_utf16_buffer()                                                                                                                                |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | to_utf32_buffer()                                                                                                                                |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)          | to_wchar_buffer()                                                                                                                                |
| String                                                    | trim_prefix(prefix: String)                                                                                                         |
| String                                                    | trim_suffix(suffix: String)                                                                                                         |
| [int](class_int.md#class-int)                                              | unicode_at(at: [int](class_int.md#class-int))                                                                                                         |
| String                                                    | uri_decode()                                                                                                                                          |
| String                                                    | uri_encode()                                                                                                                                          |
| String                                                    | uri_file_decode()                                                                                                                                |
| String                                                    | validate_filename()                                                                                                                            |
| String                                                    | validate_node_name()                                                                                                                          |
| String                                                    | xml_escape(escape_quotes: [bool](class_bool.md#class-bool) = false)                                                                                   |
| String                                                    | xml_unescape()                                                                                                                                      |

## Operators

| [bool](class_bool.md#class-bool)   | operator !=(right: String)                                |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)   | operator !=(right: [StringName](class_stringname.md#class-stringname)) |
| String            | operator %(right: [Variant](class_variant.md#class-variant))              |
| String            | operator +(right: String)                                 |
| String            | operator +(right: [StringName](class_stringname.md#class-stringname))  |
| [bool](class_bool.md#class-bool)   | operator <(right: String)                                  |
| [bool](class_bool.md#class-bool)   | operator <=(right: String)                                |
| [bool](class_bool.md#class-bool)   | operator ==(right: String)                                 |
| [bool](class_bool.md#class-bool)   | operator ==(right: [StringName](class_stringname.md#class-stringname))  |
| [bool](class_bool.md#class-bool)   | operator >(right: String)                                  |
| [bool](class_bool.md#class-bool)   | operator >=(right: String)                                |
| String            | operator [](index: [int](class_int.md#class-int))                             |

---

## Constructor Descriptions

String **String**()

Constructs an empty **String** (`""`).

---

String **String**(from: String)

Constructs a **String** as a copy of the given **String**.

---

String **String**(from: [NodePath](class_nodepath.md#class-nodepath))

Constructs a new **String** from the given [NodePath](class_nodepath.md#class-nodepath).

---

String **String**(from: [StringName](class_stringname.md#class-stringname))

Constructs a new **String** from the given [StringName](class_stringname.md#class-stringname).

---

## Method Descriptions

[bool](class_bool.md#class-bool) **begins_with**(text: String)

Returns `true` if the string begins with the given `text`. See also ends_with().

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **bigrams**()

Returns an array containing the bigrams (pairs of consecutive characters) of this string.

```gdscript
print("Get up!".bigrams()) # Prints ["Ge", "et", "t ", " u", "up", "p!"]
```

---

[int](class_int.md#class-int) **bin_to_int**()

Converts the string representing a binary number into an [int](class_int.md#class-int). The string may optionally be prefixed with `"0b"`, and an additional `-` prefix for negative numbers.

GDScript

```gdscript
print("101".bin_to_int())   # Prints 5
print("0b101".bin_to_int()) # Prints 5
print("-0b10".bin_to_int()) # Prints -2
```

C#

```csharp
GD.Print("101".BinToInt());   // Prints 5
GD.Print("0b101".BinToInt()); // Prints 5
GD.Print("-0b10".BinToInt()); // Prints -2
```

---

String **c_escape**()

Returns a copy of the string with special characters escaped using the C language standard.

---

String **c_unescape**()

Returns a copy of the string with escaped characters replaced by their meanings. Supported escape sequences are `\'`, `\"`, `\\`, `\a`, `\b`, `\f`, `\n`, `\r`, `\t`, `\v`.

**Note:** Unlike the GDScript parser, this method doesn't support the `\uXXXX` escape sequence.

---

String **capitalize**()

Returns a copy of the string with changed appearance. Replaces underscores (`_`) and hyphens (`-`) with spaces, adds spaces before uppercase letters in the middle of a word, converts all letters to lowercase, then converts the first one and each one following a space to uppercase.

GDScript

```gdscript
"move_local_x".capitalize()   # Returns "Move Local X"
"sceneFile_path".capitalize() # Returns "Scene File Path"
"2D, FPS, PNG".capitalize()   # Returns "2d, Fps, Png"
"example-name".capitalize()   # Returns "Example Name"
```

C#

```csharp
"move_local_x".Capitalize();   // Returns "Move Local X"
"sceneFile_path".Capitalize(); // Returns "Scene File Path"
"2D, FPS, PNG".Capitalize();   // Returns "2d, Fps, Png"
"example-name".Capitalize();   // Returns "Example Name"
```

---

[int](class_int.md#class-int) **casecmp_to**(to: String)

Performs a case-sensitive comparison to another string. Returns `-1` if less than, `1` if greater than, or `0` if equal. "Less than" and "greater than" are determined by the [Unicode code points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) of each string, which roughly matches the alphabetical order.

If the character comparison reaches the end of one string, but the other string contains more characters, then it will use length as the deciding factor: `1` will be returned if this string is longer than the `to` string, or `-1` if shorter. Note that the length of empty strings is always `0`.

To get a [bool](class_bool.md#class-bool) result from a string comparison, use the `==` operator instead. See also nocasecmp_to(), filecasecmp_to(), and naturalcasecmp_to().

---

String **chr**(code: [int](class_int.md#class-int))

Returns a single Unicode character from the integer `code`. You may use [unicodelookup.com](https://unicodelookup.com/) or [unicode.org](https://www.unicode.org/charts/) as points of reference.

```gdscript
print(String.chr(65))     # Prints "A"
print(String.chr(129302)) # Prints "🤖" (robot face emoji)
```

See also unicode_at(), [@GDScript.char()](class_@gdscript.md#class-gdscript-method-char), and [@GDScript.ord()](class_@gdscript.md#class-gdscript-method-ord).

---

[bool](class_bool.md#class-bool) **contains**(what: String)

Returns `true` if the string contains `what`. In GDScript, this corresponds to the `in` operator.

GDScript

```gdscript
print("Node".contains("de")) # Prints true
print("team".contains("I"))  # Prints false
print("I" in "team")         # Prints false
```

C#

```csharp
GD.Print("Node".Contains("de")); // Prints True
GD.Print("team".Contains("I"));  // Prints False
```

If you need to know where `what` is within the string, use find(). See also containsn().

---

[bool](class_bool.md#class-bool) **containsn**(what: String)

Returns `true` if the string contains `what`, **ignoring case**.

If you need to know where `what` is within the string, use findn(). See also contains().

---

[int](class_int.md#class-int) **count**(what: String, from: [int](class_int.md#class-int) = 0, to: [int](class_int.md#class-int) = 0)

Returns the number of occurrences of the substring `what` between `from` and `to` positions. If `to` is 0, the search continues until the end of the string.

---

[int](class_int.md#class-int) **countn**(what: String, from: [int](class_int.md#class-int) = 0, to: [int](class_int.md#class-int) = 0)

Returns the number of occurrences of the substring `what` between `from` and `to` positions, **ignoring case**. If `to` is 0, the search continues until the end of the string.

---

String **dedent**()

Returns a copy of the string with indentation (leading tabs and spaces) removed. See also indent() to add indentation.

---

[bool](class_bool.md#class-bool) **ends_with**(text: String)

Returns `true` if the string ends with the given `text`. See also begins_with().

---

String **erase**(position: [int](class_int.md#class-int), chars: [int](class_int.md#class-int) = 1)

Returns a string with `chars` characters erased starting from `position`. If `chars` goes beyond the string's length given the specified `position`, fewer characters will be erased from the returned string. Returns an empty string if either `position` or `chars` is negative. Returns the original string unmodified if `chars` is `0`.

---

[int](class_int.md#class-int) **filecasecmp_to**(to: String)

Like naturalcasecmp_to() but prioritizes strings that begin with periods (`.`) and underscores (`_`) before any other character. Useful when sorting folders or file names.

To get a [bool](class_bool.md#class-bool) result from a string comparison, use the `==` operator instead. See also filenocasecmp_to(), naturalcasecmp_to(), and casecmp_to().

---

[int](class_int.md#class-int) **filenocasecmp_to**(to: String)

Like naturalnocasecmp_to() but prioritizes strings that begin with periods (`.`) and underscores (`_`) before any other character. Useful when sorting folders or file names.

To get a [bool](class_bool.md#class-bool) result from a string comparison, use the `==` operator instead. See also filecasecmp_to(), naturalnocasecmp_to(), and nocasecmp_to().

---

[int](class_int.md#class-int) **find**(what: String, from: [int](class_int.md#class-int) = 0)

Returns the index of the **first** occurrence of `what` in this string, or `-1` if there are none. The search's start can be specified with `from`, continuing to the end of the string.

GDScript

```gdscript
print("Team".find("I")) # Prints -1

print("Potato".find("t"))    # Prints 2
print("Potato".find("t", 3)) # Prints 4
print("Potato".find("t", 5)) # Prints -1
```

C#

```csharp
GD.Print("Team".Find("I")); // Prints -1

GD.Print("Potato".Find("t"));    // Prints 2
GD.Print("Potato".Find("t", 3)); // Prints 4
GD.Print("Potato".Find("t", 5)); // Prints -1
```

**Note:** If you just want to know whether the string contains `what`, use contains(). In GDScript, you may also use the `in` operator.

**Note:** A negative value of `from` is converted to a starting index by counting back from the last possible index with enough space to find `what`.

---

[int](class_int.md#class-int) **findn**(what: String, from: [int](class_int.md#class-int) = 0)

Returns the index of the **first** **case-insensitive** occurrence of `what` in this string, or `-1` if there are none. The starting search index can be specified with `from`, continuing to the end of the string.

---

String **format**(values: [Variant](class_variant.md#class-variant), placeholder: String = "{_}")

Formats the string by replacing all occurrences of `placeholder` with the elements of `values`.

`values` can be a [Dictionary](class_dictionary.md#class-dictionary), an [Array](class_array.md#class-array), or an [Object](class_object.md#class-object). Any underscores in `placeholder` will be replaced with the corresponding keys in advance. Array elements use their index as keys.

```gdscript
# Prints "Waiting for Godot is a play by Samuel Beckett, and Godot Engine is named after it."
var use_array_values = "Waiting for {0} is a play by {1}, and {0} Engine is named after it."
print(use_array_values.format(["Godot", "Samuel Beckett"]))

# Prints "User 42 is Godot."
print("User {id} is {name}.".format({"id": 42, "name": "Godot"}))
```

Some additional handling is performed when `values` is an [Array](class_array.md#class-array). If `placeholder` does not contain an underscore, the elements of the `values` array will be used to replace one occurrence of the placeholder in order; If an element of `values` is another 2-element array, it'll be interpreted as a key-value pair.

```gdscript
# Prints "User 42 is Godot."
print("User {} is {}.".format([42, "Godot"], "{}"))
print("User {id} is {name}.".format([["id", 42], ["name", "Godot"]]))
```

When passing an [Object](class_object.md#class-object), the property names from [Object.get_property_list()](class_object.md#class-object-method-get-property-list) are used as keys.

```gdscript
# Prints "Visible true, position (0, 0)"
var node = Node2D.new()
print("Visible {visible}, position {position}".format(node))
```

See also the [GDScript format string](../tutorials/scripting/gdscript/gdscript_format_string.md) tutorial.

**Note:** Each replacement is done sequentially for each element of `values`, **not** all at once. This means that if any element is inserted and it contains another placeholder, it may be changed by the next replacement. While this can be very useful, it often causes unexpected results. If not necessary, make sure `values`'s elements do not contain placeholders.

```gdscript
print("{0} {1}".format(["{1}", "x"]))           # Prints "x x"
print("{0} {1}".format(["x", "{0}"]))           # Prints "x {0}"
print("{a} {b}".format({"a": "{b}", "b": "c"})) # Prints "c c"
print("{a} {b}".format({"b": "c", "a": "{b}"})) # Prints "{b} c"
```

**Note:** In C#, it's recommended to [interpolate strings with "$"](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated), instead.

---

String **get_base_dir**()

If the string is a valid file path, returns the base directory name.

```gdscript
var dir_path = "/path/to/file.txt".get_base_dir() # dir_path is "/path/to"
```

---

String **get_basename**()

If the string is a valid file path, returns the full file path, without the extension.

```gdscript
var base = "/path/to/file.txt".get_basename() # base is "/path/to/file"
```

---

String **get_extension**()

If the string is a valid file name or path, returns the file extension without the leading period (`.`). Otherwise, returns an empty string.

```gdscript
var a = "/path/to/file.txt".get_extension() # a is "txt"
var b = "cool.txt".get_extension()          # b is "txt"
var c = "cool.font.tres".get_extension()    # c is "tres"
var d = ".pack1".get_extension()            # d is "pack1"

var e = "file.txt.".get_extension()  # e is ""
var f = "file.txt..".get_extension() # f is ""
var g = "txt".get_extension()        # g is ""
var h = "".get_extension()           # h is ""
```

---

String **get_file**()

If the string is a valid file path, returns the file name, including the extension.

```gdscript
var file = "/path/to/icon.png".get_file() # file is "icon.png"
```

---

String **get_slice**(delimiter: String, slice: [int](class_int.md#class-int))

Splits the string using a `delimiter` and returns the substring at index `slice`. Returns the original string if `delimiter` does not occur in the string. Returns an empty string if the `slice` does not exist.

This is faster than split(), if you only need one or two substrings.

```gdscript
print("i/am/example/hi".get_slice("/", 2)) # Prints "example"
```

---

[int](class_int.md#class-int) **get_slice_count**(delimiter: String)

Returns the total number of slices when the string is split with the given `delimiter` (see split()).

Use get_slice() to extract a specific slice.

```gdscript
print("i/am/example/string".get_slice_count("/")) # Prints '4'.
print("i am example string".get_slice_count("/")) # Prints '1'.
```

---

String **get_slicec**(delimiter: [int](class_int.md#class-int), slice: [int](class_int.md#class-int))

Splits the string using a Unicode character with code `delimiter` and returns the substring at index `slice`. Returns an empty string if the `slice` does not exist.

This is faster than split(), if you only need one or two substrings.

This is a Unicode version of get_slice().

---

[int](class_int.md#class-int) **hash**()

Returns the 32-bit hash value representing the string's contents.

**Note:** Strings with equal hash values are *not* guaranteed to be the same, as a result of hash collisions. On the contrary, strings with different hash values are guaranteed to be different.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **hex_decode**()

Decodes a hexadecimal string as a [PackedByteArray](class_packedbytearray.md#class-packedbytearray).

GDScript

```gdscript
var text = "hello world"
var encoded = text.to_utf8_buffer().hex_encode() # outputs "68656c6c6f20776f726c64"
print(encoded.hex_decode().get_string_from_utf8())
```

C#

```csharp
var text = "hello world";
var encoded = text.ToUtf8Buffer().HexEncode(); // outputs "68656c6c6f20776f726c64"
GD.Print(encoded.HexDecode().GetStringFromUtf8());
```

---

[int](class_int.md#class-int) **hex_to_int**()

Converts the string representing a hexadecimal number into an [int](class_int.md#class-int). The string may be optionally prefixed with `"0x"`, and an additional `-` prefix for negative numbers.

GDScript

```gdscript
print("0xff".hex_to_int()) # Prints 255
print("ab".hex_to_int())   # Prints 171
```

C#

```csharp
GD.Print("0xff".HexToInt()); // Prints 255
GD.Print("ab".HexToInt());   // Prints 171
```

---

String **humanize_size**(size: [int](class_int.md#class-int))

Converts `size` which represents a number of bytes into a human-readable form.

The result is in [IEC prefix format](https://en.wikipedia.org/wiki/Binary_prefix#IEC_prefixes), which may end in either `"B"`, `"KiB"`, `"MiB"`, `"GiB"`, `"TiB"`, `"PiB"`, or `"EiB"`.

---

String **indent**(prefix: String)

Indents every line of the string with the given `prefix`. Empty lines are not indented. See also dedent() to remove indentation.

For example, the string can be indented with two tabulations using `"\t\t"`, or four spaces using `"    "`.

---

String **insert**(position: [int](class_int.md#class-int), what: String)

Inserts `what` at the given `position` in the string.

---

[bool](class_bool.md#class-bool) **is_absolute_path**()

Returns `true` if the string is a path to a file or directory, and its starting point is explicitly defined. This method is the opposite of is_relative_path().

This includes all paths starting with `"res://"`, `"user://"`, `"C:\"`, `"/"`, etc.

---

[bool](class_bool.md#class-bool) **is_empty**()

Returns `true` if the string's length is `0` (`""`). See also length().

---

[bool](class_bool.md#class-bool) **is_relative_path**()

Returns `true` if the string is a path, and its starting point is dependent on context. The path could begin from the current directory, or the current [Node](class_node.md#class-node) (if the string is derived from a [NodePath](class_nodepath.md#class-nodepath)), and may sometimes be prefixed with `"./"`. This method is the opposite of is_absolute_path().

---

[bool](class_bool.md#class-bool) **is_subsequence_of**(text: String)

Returns `true` if all characters of this string can be found in `text` in their original order. This is not the same as contains().

```gdscript
var text = "Wow, incredible!"

print("inedible".is_subsequence_of(text)) # Prints true
print("Word!".is_subsequence_of(text))    # Prints true
print("Window".is_subsequence_of(text))   # Prints false
print("".is_subsequence_of(text))         # Prints true
```

---

[bool](class_bool.md#class-bool) **is_subsequence_ofn**(text: String)

Returns `true` if all characters of this string can be found in `text` in their original order, **ignoring case**. This is not the same as containsn().

---

[bool](class_bool.md#class-bool) **is_valid_ascii_identifier**()

Returns `true` if this string is a valid ASCII identifier. A valid ASCII identifier may contain only letters, digits, and underscores (`_`), and the first character may not be a digit.

```gdscript
print("node_2d".is_valid_ascii_identifier())    # Prints true
print("TYPE_FLOAT".is_valid_ascii_identifier()) # Prints true
print("1st_method".is_valid_ascii_identifier()) # Prints false
print("MyMethod#2".is_valid_ascii_identifier()) # Prints false
```

See also is_valid_unicode_identifier().

---

[bool](class_bool.md#class-bool) **is_valid_filename**()

Returns `true` if this string is a valid file name. A valid file name cannot be empty, begin or end with space characters, or contain characters that are not allowed (`:` `/` `\` `?` `*` `"` `|` `%` `<` `>`).

---

[bool](class_bool.md#class-bool) **is_valid_float**()

Returns `true` if this string represents a valid floating-point number. A valid float may contain only digits, one decimal point (`.`), and the exponent letter (`e`). It may also be prefixed with a positive (`+`) or negative (`-`) sign. Any valid integer is also a valid float (see is_valid_int()). See also to_float().

```gdscript
print("1.7".is_valid_float())   # Prints true
print("24".is_valid_float())    # Prints true
print("7e3".is_valid_float())   # Prints true
print("Hello".is_valid_float()) # Prints false
```

---

[bool](class_bool.md#class-bool) **is_valid_hex_number**(with_prefix: [bool](class_bool.md#class-bool) = false)

Returns `true` if this string is a valid hexadecimal number. A valid hexadecimal number only contains digits or letters `A` to `F` (either uppercase or lowercase), and may be prefixed with a positive (`+`) or negative (`-`) sign.

If `with_prefix` is `true`, the hexadecimal number needs to prefixed by `"0x"` to be considered valid.

```gdscript
print("A08E".is_valid_hex_number())    # Prints true
print("-AbCdEf".is_valid_hex_number()) # Prints true
print("2.5".is_valid_hex_number())     # Prints false

print("0xDEADC0DE".is_valid_hex_number(true)) # Prints true
```

---

[bool](class_bool.md#class-bool) **is_valid_html_color**()

Returns `true` if this string is a valid color in hexadecimal HTML notation. The string must be a hexadecimal value (see is_valid_hex_number()) of either 3, 4, 6 or 8 digits, and may be prefixed by a hash sign (`#`). Other HTML notations for colors, such as names or `hsl()`, are not considered valid. See also [Color.html()](class_color.md#class-color-method-html).

---

[bool](class_bool.md#class-bool) **is_valid_identifier**()

**Deprecated:** Use is_valid_ascii_identifier() instead.

Returns `true` if this string is a valid identifier. A valid identifier may contain only letters, digits and underscores (`_`), and the first character may not be a digit.

```gdscript
print("node_2d".is_valid_identifier())    # Prints true
print("TYPE_FLOAT".is_valid_identifier()) # Prints true
print("1st_method".is_valid_identifier()) # Prints false
print("MyMethod#2".is_valid_identifier()) # Prints false
```

---

[bool](class_bool.md#class-bool) **is_valid_int**()

Returns `true` if this string represents a valid integer. A valid integer only contains digits, and may be prefixed with a positive (`+`) or negative (`-`) sign. See also to_int().

```gdscript
print("7".is_valid_int())    # Prints true
print("1.65".is_valid_int()) # Prints false
print("Hi".is_valid_int())   # Prints false
print("+3".is_valid_int())   # Prints true
print("-12".is_valid_int())  # Prints true
```

---

[bool](class_bool.md#class-bool) **is_valid_ip_address**()

Returns `true` if this string represents a well-formatted IPv4 or IPv6 address. This method considers [reserved IP addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses) such as `"0.0.0.0"` and `"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"` as valid.

---

[bool](class_bool.md#class-bool) **is_valid_unicode_identifier**()

Returns `true` if this string is a valid Unicode identifier.

A valid Unicode identifier must begin with a Unicode character of class `XID_Start` or `"_"`, and may contain Unicode characters of class `XID_Continue` in the other positions.

```gdscript
print("node_2d".is_valid_unicode_identifier())      # Prints true
print("1st_method".is_valid_unicode_identifier())   # Prints false
print("MyMethod#2".is_valid_unicode_identifier())   # Prints false
print("állóképesség".is_valid_unicode_identifier()) # Prints true
print("выносливость".is_valid_unicode_identifier()) # Prints true
print("体力".is_valid_unicode_identifier())         # Prints true
```

See also is_valid_ascii_identifier().

**Note:** This method checks identifiers the same way as GDScript. See [TextServer.is_valid_identifier()](class_textserver.md#class-textserver-method-is-valid-identifier) for more advanced checks.

---

String **join**(parts: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Returns the concatenation of `parts`' elements, with each element separated by the string calling this method. This method is the opposite of split().

GDScript

```gdscript
var fruits = ["Apple", "Orange", "Pear", "Kiwi"]

print(", ".join(fruits))  # Prints "Apple, Orange, Pear, Kiwi"
print("---".join(fruits)) # Prints "Apple---Orange---Pear---Kiwi"
```

C#

```csharp
string[] fruits = ["Apple", "Orange", "Pear", "Kiwi"];

// In C#, this method is static.
GD.Print(string.Join(", ", fruits));  // Prints "Apple, Orange, Pear, Kiwi"
GD.Print(string.Join("---", fruits)); // Prints "Apple---Orange---Pear---Kiwi"
```

---

String **json_escape**()

Returns a copy of the string with special characters escaped using the JSON standard. Because it closely matches the C standard, it is possible to use c_unescape() to unescape the string, if necessary.

---

String **left**(length: [int](class_int.md#class-int))

Returns the first `length` characters from the beginning of the string. If `length` is negative, strips the last `length` characters from the string's end.

```gdscript
print("Hello World!".left(3))  # Prints "Hel"
print("Hello World!".left(-4)) # Prints "Hello Wo"
```

---

[int](class_int.md#class-int) **length**()

Returns the number of characters in the string. Empty strings (`""`) always return `0`. See also is_empty().

---

String **lpad**(min_length: [int](class_int.md#class-int), character: String = " ")

Formats the string to be at least `min_length` long by adding `character`s to the left of the string, if necessary. See also rpad().

---

String **lstrip**(chars: String)

Removes a set of characters defined in `chars` from the string's beginning. See also rstrip().

**Note:** `chars` is not a prefix. Use trim_prefix() to remove a single prefix, rather than a set of characters.

---

[bool](class_bool.md#class-bool) **match**(expr: String)

Does a simple expression match (also called "glob" or "globbing"), where `*` matches zero or more arbitrary characters and `?` matches any single character except a period (`.`). An empty string or empty expression always evaluates to `false`.

---

[bool](class_bool.md#class-bool) **matchn**(expr: String)

Does a simple **case-insensitive** expression match, where `*` matches zero or more arbitrary characters and `?` matches any single character except a period (`.`). An empty string or empty expression always evaluates to `false`.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **md5_buffer**()

Returns the [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the string as a [PackedByteArray](class_packedbytearray.md#class-packedbytearray).

---

String **md5_text**()

Returns the [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the string as another **String**.

---

[int](class_int.md#class-int) **naturalcasecmp_to**(to: String)

Performs a **case-sensitive**, *natural order* comparison to another string. Returns `-1` if less than, `1` if greater than, or `0` if equal. "Less than" or "greater than" are determined by the [Unicode code points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) of each string, which roughly matches the alphabetical order.

When used for sorting, natural order comparison orders sequences of numbers by the combined value of each digit as is often expected, instead of the single digit's value. A sorted sequence of numbered strings will be `["1", "2", "3", ...]`, not `["1", "10", "2", "3", ...]`.

If the character comparison reaches the end of one string, but the other string contains more characters, then it will use length as the deciding factor: `1` will be returned if this string is longer than the `to` string, or `-1` if shorter. Note that the length of empty strings is always `0`.

To get a [bool](class_bool.md#class-bool) result from a string comparison, use the `==` operator instead. See also naturalnocasecmp_to(), filecasecmp_to(), and nocasecmp_to().

---

[int](class_int.md#class-int) **naturalnocasecmp_to**(to: String)

Performs a **case-insensitive**, *natural order* comparison to another string. Returns `-1` if less than, `1` if greater than, or `0` if equal. "Less than" or "greater than" are determined by the [Unicode code points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) of each string, which roughly matches the alphabetical order. Internally, lowercase characters are converted to uppercase for the comparison.

When used for sorting, natural order comparison orders sequences of numbers by the combined value of each digit as is often expected, instead of the single digit's value. A sorted sequence of numbered strings will be `["1", "2", "3", ...]`, not `["1", "10", "2", "3", ...]`.

If the character comparison reaches the end of one string, but the other string contains more characters, then it will use length as the deciding factor: `1` will be returned if this string is longer than the `to` string, or `-1` if shorter. Note that the length of empty strings is always `0`.

To get a [bool](class_bool.md#class-bool) result from a string comparison, use the `==` operator instead. See also naturalcasecmp_to(), filenocasecmp_to(), and casecmp_to().

---

[int](class_int.md#class-int) **nocasecmp_to**(to: String)

Performs a **case-insensitive** comparison to another string. Returns `-1` if less than, `1` if greater than, or `0` if equal. "Less than" or "greater than" are determined by the [Unicode code points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) of each string, which roughly matches the alphabetical order. Internally, lowercase characters are converted to uppercase for the comparison.

If the character comparison reaches the end of one string, but the other string contains more characters, then it will use length as the deciding factor: `1` will be returned if this string is longer than the `to` string, or `-1` if shorter. Note that the length of empty strings is always `0`.

To get a [bool](class_bool.md#class-bool) result from a string comparison, use the `==` operator instead. See also casecmp_to(), filenocasecmp_to(), and naturalnocasecmp_to().

---

String **num**(number: [float](class_float.md#class-float), decimals: [int](class_int.md#class-int) = -1)

Converts a [float](class_float.md#class-float) to a string representation of a decimal number, with the number of decimal places specified in `decimals`.

If `decimals` is `-1` as by default, the string representation may only have up to 14 significant digits, with digits before the decimal point having priority over digits after.

Trailing zeros are not included in the string. The last digit is rounded, not truncated.

```gdscript
String.num(3.141593)     # Returns "3.141593"
String.num(3.141593, 3)  # Returns "3.142"
String.num(3.14159300)   # Returns "3.141593"

# Here, the last digit will be rounded up,
# which reduces the total digit count, since trailing zeros are removed:
String.num(42.129999, 5) # Returns "42.13"

# If `decimals` is not specified, the maximum number of significant digits is 14:
String.num(-0.0000012345432123454321)     # Returns "-0.00000123454321"
String.num(-10000.0000012345432123454321) # Returns "-10000.0000012345"
```

---

String **num_int64**(number: [int](class_int.md#class-int), base: [int](class_int.md#class-int) = 10, capitalize_hex: [bool](class_bool.md#class-bool) = false)

Converts the given `number` to a string representation, with the given `base`.

By default, `base` is set to decimal (`10`). Other common bases in programming include binary (`2`), [octal](https://en.wikipedia.org/wiki/Octal) (`8`), hexadecimal (`16`).

If `capitalize_hex` is `true`, digits higher than 9 are represented in uppercase.

---

String **num_scientific**(number: [float](class_float.md#class-float))

Converts the given `number` to a string representation, in scientific notation.

GDScript

```gdscript
var n = -5.2e8
print(n)                        # Prints -520000000
print(String.num_scientific(n)) # Prints -5.2e+08
```

C#

```csharp
// This method is not implemented in C#.
// Use `string.ToString()` with "e" to achieve similar results.
var n = -5.2e8f;
GD.Print(n);                // Prints -520000000
GD.Print(n.ToString("e1")); // Prints -5.2e+008
```

**Note:** In C#, this method is not implemented. To achieve similar results, see C#'s [Standard numeric format strings](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings).

---

String **num_uint64**(number: [int](class_int.md#class-int), base: [int](class_int.md#class-int) = 10, capitalize_hex: [bool](class_bool.md#class-bool) = false)

Converts the given unsigned [int](class_int.md#class-int) to a string representation, with the given `base`.

By default, `base` is set to decimal (`10`). Other common bases in programming include binary (`2`), [octal](https://en.wikipedia.org/wiki/Octal) (`8`), hexadecimal (`16`).

If `capitalize_hex` is `true`, digits higher than 9 are represented in uppercase.

---

String **pad_decimals**(digits: [int](class_int.md#class-int))

Formats the string representing a number to have an exact number of `digits` *after* the decimal point.

---

String **pad_zeros**(digits: [int](class_int.md#class-int))

Formats the string representing a number to have an exact number of `digits` *before* the decimal point.

---

String **path_join**(path: String)

Concatenates `path` at the end of the string as a subpath, adding `/` if necessary.

**Example:** `"this/is".path_join("path") == "this/is/path"`.

---

String **remove_char**(what: [int](class_int.md#class-int))

Removes all occurrences of the Unicode character with code `what`. Faster version of replace() when the key is only one character long and the replacement is `""`.

---

String **remove_chars**(chars: String)

Removes all occurrences of the characters in `chars`. See also remove_char().

---

String **repeat**(count: [int](class_int.md#class-int))

Repeats this string a number of times. `count` needs to be greater than `0`. Otherwise, returns an empty string.

---

String **replace**(what: String, forwhat: String)

Replaces all occurrences of `what` inside the string with the given `forwhat`.

---

String **replace_char**(key: [int](class_int.md#class-int), with: [int](class_int.md#class-int))

Replaces all occurrences of the Unicode character with code `key` with the Unicode character with code `with`. Faster version of replace() when the key is only one character long. To get a single character use `"X".unicode_at(0)` (note that some strings, like compound letters and emoji, can be composed of multiple unicode codepoints, and will not work with this method, use length() to make sure).

---

String **replace_chars**(keys: String, with: [int](class_int.md#class-int))

Replaces any occurrence of the characters in `keys` with the Unicode character with code `with`. See also replace_char().

---

String **replacen**(what: String, forwhat: String)

Replaces all **case-insensitive** occurrences of `what` inside the string with the given `forwhat`.

---

String **reverse**()

Returns the copy of this string in reverse order. This operation works on unicode codepoints, rather than sequences of codepoints, and may break things like compound letters or emojis.

---

[int](class_int.md#class-int) **rfind**(what: String, from: [int](class_int.md#class-int) = -1)

Returns the index of the **last** occurrence of `what` in this string, or `-1` if there are none. The search's start can be specified with `from`, continuing to the beginning of the string. This method is the reverse of find().

**Note:** A negative value of `from` is converted to a starting index by counting back from the last possible index with enough space to find `what`.

**Note:** A value of `from` that is greater than the last possible index with enough space to find `what` is considered out-of-bounds, and returns `-1`.

---

[int](class_int.md#class-int) **rfindn**(what: String, from: [int](class_int.md#class-int) = -1)

Returns the index of the **last** **case-insensitive** occurrence of `what` in this string, or `-1` if there are none. The starting search index can be specified with `from`, continuing to the beginning of the string. This method is the reverse of findn().

---

String **right**(length: [int](class_int.md#class-int))

Returns the last `length` characters from the end of the string. If `length` is negative, strips the first `length` characters from the string's beginning.

```gdscript
print("Hello World!".right(3))  # Prints "ld!"
print("Hello World!".right(-4)) # Prints "o World!"
```

---

String **rpad**(min_length: [int](class_int.md#class-int), character: String = " ")

Formats the string to be at least `min_length` long, by adding `character`s to the right of the string, if necessary. See also lpad().

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **rsplit**(delimiter: String = "", allow_empty: [bool](class_bool.md#class-bool) = true, maxsplit: [int](class_int.md#class-int) = 0)

Splits the string using a `delimiter` and returns an array of the substrings, starting from the end of the string. The splits in the returned array appear in the same order as the original string. If `delimiter` is an empty string, each substring will be a single character.

If `allow_empty` is `false`, empty strings between adjacent delimiters are excluded from the array.

If `maxsplit` is greater than `0`, the number of splits may not exceed `maxsplit`. By default, the entire string is split, which is mostly identical to split().

GDScript

```gdscript
var some_string = "One,Two,Three,Four"
var some_array = some_string.rsplit(",", true, 1)

print(some_array.size()) # Prints 2
print(some_array[0])     # Prints "One,Two,Three"
print(some_array[1])     # Prints "Four"
```

C#

```csharp
// In C#, there is no String.RSplit() method.
```

---

String **rstrip**(chars: String)

Removes a set of characters defined in `chars` from the string's end. See also lstrip().

**Note:** `chars` is not a suffix. Use trim_suffix() to remove a single suffix, rather than a set of characters.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **sha1_buffer**()

Returns the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash of the string as a [PackedByteArray](class_packedbytearray.md#class-packedbytearray).

---

String **sha1_text**()

Returns the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash of the string as another **String**.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **sha256_buffer**()

Returns the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash of the string as a [PackedByteArray](class_packedbytearray.md#class-packedbytearray).

---

String **sha256_text**()

Returns the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash of the string as another **String**.

---

[float](class_float.md#class-float) **similarity**(text: String)

Returns the similarity index ([Sørensen-Dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)) of this string compared to another. A result of `1.0` means totally similar, while `0.0` means totally dissimilar.

```gdscript
print("ABC123".similarity("ABC123")) # Prints 1.0
print("ABC123".similarity("XYZ456")) # Prints 0.0
print("ABC123".similarity("123ABC")) # Prints 0.8
print("ABC123".similarity("abc123")) # Prints 0.4
```

---

String **simplify_path**()

If the string is a valid file path, converts the string into a canonical path. This is the shortest possible path, without `"./"`, and all the unnecessary `".."` and `"/"`.

```gdscript
var simple_path = "./path/to///../file".simplify_path()
print(simple_path) # Prints "path/file"
```

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **split**(delimiter: String = "", allow_empty: [bool](class_bool.md#class-bool) = true, maxsplit: [int](class_int.md#class-int) = 0)

Splits the string using a `delimiter` and returns an array of the substrings. If `delimiter` is an empty string, each substring will be a single character. This method is the opposite of join().

If `allow_empty` is `false`, empty strings between adjacent delimiters are excluded from the array.

If `maxsplit` is greater than `0`, the number of splits may not exceed `maxsplit`. By default, the entire string is split.

GDScript

```gdscript
var some_array = "One,Two,Three,Four".split(",", true, 2)

print(some_array.size()) # Prints 3
print(some_array[0])     # Prints "One"
print(some_array[1])     # Prints "Two"
print(some_array[2])     # Prints "Three,Four"
```

C#

```csharp
// C#'s `Split()` does not support the `maxsplit` parameter.
var someArray = "One,Two,Three".Split(",");

GD.Print(someArray[0]); // Prints "One"
GD.Print(someArray[1]); // Prints "Two"
GD.Print(someArray[2]); // Prints "Three"
```

**Note:** If you only need one substring from the array, consider using get_slice() which is faster. If you need to split strings with more complex rules, use the [RegEx](class_regex.md#class-regex) class instead.

---

[PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) **split_floats**(delimiter: String, allow_empty: [bool](class_bool.md#class-bool) = true)

Splits the string into floats by using a `delimiter` and returns a [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array).

If `allow_empty` is `false`, empty or invalid [float](class_float.md#class-float) conversions between adjacent delimiters are excluded.

```gdscript
var a = "1,2,4.5".split_floats(",")         # a is [1.0, 2.0, 4.5]
var c = "1| ||4.5".split_floats("|")        # c is [1.0, 0.0, 0.0, 4.5]
var b = "1| ||4.5".split_floats("|", false) # b is [1.0, 4.5]
```

---

String **strip_edges**(left: [bool](class_bool.md#class-bool) = true, right: [bool](class_bool.md#class-bool) = true)

Strips all non-printable characters from the beginning and the end of the string. These include spaces, tabulations (`\t`), and newlines (`\n` `\r`).

If `left` is `false`, ignores the string's beginning. Likewise, if `right` is `false`, ignores the string's end.

---

String **strip_escapes**()

Strips all escape characters from the string. These include all non-printable control characters of the first page of the ASCII table (values from 0 to 31), such as tabulation (`\t`) and newline (`\n`, `\r`) characters, but *not* spaces.

---

String **substr**(from: [int](class_int.md#class-int), len: [int](class_int.md#class-int) = -1)

Returns part of the string from the position `from` with length `len`. If `len` is `-1` (as by default), returns the rest of the string starting from the given position.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_ascii_buffer**()

Converts the string to an [ASCII](https://en.wikipedia.org/wiki/ASCII)/Latin-1 encoded [PackedByteArray](class_packedbytearray.md#class-packedbytearray). This method is slightly faster than to_utf8_buffer(), but replaces all unsupported characters with spaces. This is the inverse of [PackedByteArray.get_string_from_ascii()](class_packedbytearray.md#class-packedbytearray-method-get-string-from-ascii).

---

String **to_camel_case**()

Returns the string converted to `camelCase`.

---

[float](class_float.md#class-float) **to_float**()

Converts the string representing a decimal number into a [float](class_float.md#class-float). This method stops on the first non-number character, except the first decimal point (`.`) and the exponent letter (`e`). See also is_valid_float().

```gdscript
var a = "12.35".to_float()  # a is 12.35
var b = "1.2.3".to_float()  # b is 1.2
var c = "12xy3".to_float()  # c is 12.0
var d = "1e3".to_float()    # d is 1000.0
var e = "Hello!".to_float() # e is 0.0
```

---

[int](class_int.md#class-int) **to_int**()

Converts the string representing an integer number into an [int](class_int.md#class-int). This method removes any non-number character and stops at the first decimal point (`.`). See also is_valid_int().

```gdscript
var a = "123".to_int()    # a is 123
var b = "x1y2z3".to_int() # b is 123
var c = "-1.2.3".to_int() # c is -1
var d = "Hello!".to_int() # d is 0
```

---

String **to_kebab_case**()

Returns the string converted to `kebab-case`.

**Note:** Numbers followed by a *single* letter are not separated in the conversion to keep some words (such as "2D") together.

GDScript

```gdscript
"Node2D".to_kebab_case()               # Returns "node-2d"
"2nd place".to_kebab_case()            # Returns "2-nd-place"
"Texture3DAssetFolder".to_kebab_case() # Returns "texture-3d-asset-folder"
```

C#

```csharp
"Node2D".ToKebabCase();               // Returns "node-2d"
"2nd place".ToKebabCase();            // Returns "2-nd-place"
"Texture3DAssetFolder".ToKebabCase(); // Returns "texture-3d-asset-folder"
```

---

String **to_lower**()

Returns the string converted to `lowercase`.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_multibyte_char_buffer**(encoding: String = "")

Converts the string to system multibyte code page encoded [PackedByteArray](class_packedbytearray.md#class-packedbytearray). If conversion fails, empty array is returned.

The values permitted for `encoding` are system dependent. If `encoding` is empty string, system default encoding is used.

- For Windows, see [Code Page Identifiers](https://learn.microsoft.com/en-us/windows/win32/Intl/code-page-identifiers) .NET names.
- For macOS and Linux/BSD, see `libiconv` library documentation and `iconv --list` for a list of supported encodings.

---

String **to_pascal_case**()

Returns the string converted to `PascalCase`.

---

String **to_snake_case**()

Returns the string converted to `snake_case`.

**Note:** Numbers followed by a *single* letter are not separated in the conversion to keep some words (such as "2D") together.

GDScript

```gdscript
"Node2D".to_snake_case()               # Returns "node_2d"
"2nd place".to_snake_case()            # Returns "2_nd_place"
"Texture3DAssetFolder".to_snake_case() # Returns "texture_3d_asset_folder"
```

C#

```csharp
"Node2D".ToSnakeCase();               // Returns "node_2d"
"2nd place".ToSnakeCase();            // Returns "2_nd_place"
"Texture3DAssetFolder".ToSnakeCase(); // Returns "texture_3d_asset_folder"
```

---

String **to_upper**()

Returns the string converted to `UPPERCASE`.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_utf8_buffer**()

Converts the string to a [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoded [PackedByteArray](class_packedbytearray.md#class-packedbytearray). This method is slightly slower than to_ascii_buffer(), but supports all UTF-8 characters. For most cases, prefer using this method. This is the inverse of [PackedByteArray.get_string_from_utf8()](class_packedbytearray.md#class-packedbytearray-method-get-string-from-utf8).

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_utf16_buffer**()

Converts the string to a [UTF-16](https://en.wikipedia.org/wiki/UTF-16) encoded [PackedByteArray](class_packedbytearray.md#class-packedbytearray). This is the inverse of [PackedByteArray.get_string_from_utf16()](class_packedbytearray.md#class-packedbytearray-method-get-string-from-utf16).

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_utf32_buffer**()

Converts the string to a [UTF-32](https://en.wikipedia.org/wiki/UTF-32) encoded [PackedByteArray](class_packedbytearray.md#class-packedbytearray). This is the inverse of [PackedByteArray.get_string_from_utf32()](class_packedbytearray.md#class-packedbytearray-method-get-string-from-utf32).

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_wchar_buffer**()

Converts the string to a [wide character](https://en.wikipedia.org/wiki/Wide_character) (`wchar_t`, UTF-16 on Windows, UTF-32 on other platforms) encoded [PackedByteArray](class_packedbytearray.md#class-packedbytearray). This is the inverse of [PackedByteArray.get_string_from_wchar()](class_packedbytearray.md#class-packedbytearray-method-get-string-from-wchar).

---

String **trim_prefix**(prefix: String)

Removes the given `prefix` from the start of the string, or returns the string unchanged.

---

String **trim_suffix**(suffix: String)

Removes the given `suffix` from the end of the string, or returns the string unchanged.

---

[int](class_int.md#class-int) **unicode_at**(at: [int](class_int.md#class-int))

Returns the character code at position `at`.

See also chr(), [@GDScript.char()](class_@gdscript.md#class-gdscript-method-char), and [@GDScript.ord()](class_@gdscript.md#class-gdscript-method-ord).

---

String **uri_decode**()

Decodes the string from its URL-encoded format. This method is meant to properly decode the parameters in a URL when receiving an HTTP request. See also uri_encode().

GDScript

```gdscript
var url = "$DOCS_URL/?highlight=Godot%20Engine%3%docs"
print(url.uri_decode()) # Prints "$DOCS_URL/?highlight=Godot Engine:docs"
```

C#

```csharp
var url = "$DOCS_URL/?highlight=Godot%20Engine%3%docs"
GD.Print(url.URIDecode()) // Prints "$DOCS_URL/?highlight=Godot Engine:docs"
```

**Note:** This method decodes `+` as space.

---

String **uri_encode**()

Encodes the string to URL-friendly format. This method is meant to properly encode the parameters in a URL when sending an HTTP request. See also uri_decode().

GDScript

```gdscript
var prefix = "$DOCS_URL/?highlight="
var url = prefix + "Godot Engine:docs".uri_encode()

print(url) # Prints "$DOCS_URL/?highlight=Godot%20Engine%3%docs"
```

C#

```csharp
var prefix = "$DOCS_URL/?highlight=";
var url = prefix + "Godot Engine:docs".URIEncode();

GD.Print(url); // Prints "$DOCS_URL/?highlight=Godot%20Engine%3%docs"
```

---

String **uri_file_decode**()

Decodes the file path from its URL-encoded format. Unlike uri_decode() this method leaves `+` as is.

---

String **validate_filename**()

Returns a copy of the string with all characters that are not allowed in is_valid_filename() replaced with underscores.

---

String **validate_node_name**()

Returns a copy of the string with all characters that are not allowed in [Node.name](class_node.md#class-node-property-name) (`.` `:` `@` `/` `"` `%`) replaced with underscores.

---

String **xml_escape**(escape_quotes: [bool](class_bool.md#class-bool) = false)

Returns a copy of the string with special characters escaped using the XML standard. If `escape_quotes` is `true`, the single quote (`'`) and double quote (`"`) characters are also escaped.

---

String **xml_unescape**()

Returns a copy of the string with escaped characters replaced by their meanings according to the XML standard.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: String)

Returns `true` if both strings do not contain the same sequence of characters.

---

[bool](class_bool.md#class-bool) **operator !=**(right: [StringName](class_stringname.md#class-stringname))

Returns `true` if this **String** is not equivalent to the given [StringName](class_stringname.md#class-stringname).

---

String **operator %**(right: [Variant](class_variant.md#class-variant))

Formats the **String**, replacing the placeholders with one or more parameters. To pass multiple parameters, `right` needs to be an [Array](class_array.md#class-array).

```gdscript
print("I caught %d fishes!" % 2) # Prints "I caught 2 fishes!"

var my_message = "Travelling to %s, at %2.2f km/h."
var location = "Deep Valley"
var speed = 40.3485
print(my_message % [location, speed]) # Prints "Travelling to Deep Valley, at 40.35 km/h."
```

For more information, see the [GDScript format strings](../tutorials/scripting/gdscript/gdscript_format_string.md) tutorial.

**Note:** In C#, this operator is not available. Instead, see [how to interpolate strings with "$"](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated).

---

String **operator +**(right: String)

Appends `right` at the end of this **String**, also known as a string concatenation.

---

String **operator +**(right: [StringName](class_stringname.md#class-stringname))

Appends `right` at the end of this **String**, returning a **String**. This is also known as a string concatenation.

---

[bool](class_bool.md#class-bool) **operator <**(right: String)

Returns `true` if the left **String** comes before `right` in [Unicode order](https://en.wikipedia.org/wiki/List_of_Unicode_characters), which roughly matches the alphabetical order. Useful for sorting.

---

[bool](class_bool.md#class-bool) **operator <=**(right: String)

Returns `true` if the left **String** comes before `right` in [Unicode order](https://en.wikipedia.org/wiki/List_of_Unicode_characters), which roughly matches the alphabetical order, or if both are equal.

---

[bool](class_bool.md#class-bool) **operator ==**(right: String)

Returns `true` if both strings contain the same sequence of characters.

---

[bool](class_bool.md#class-bool) **operator ==**(right: [StringName](class_stringname.md#class-stringname))

Returns `true` if this **String** is equivalent to the given [StringName](class_stringname.md#class-stringname).

---

[bool](class_bool.md#class-bool) **operator >**(right: String)

Returns `true` if the left **String** comes after `right` in [Unicode order](https://en.wikipedia.org/wiki/List_of_Unicode_characters), which roughly matches the alphabetical order. Useful for sorting.

---

[bool](class_bool.md#class-bool) **operator >=**(right: String)

Returns `true` if the left **String** comes after `right` in [Unicode order](https://en.wikipedia.org/wiki/List_of_Unicode_characters), which roughly matches the alphabetical order, or if both are equal.

---

String **operator []**(index: [int](class_int.md#class-int))

Returns a new **String** that only contains the character at `index`. Indices start from `0`. If `index` is greater or equal to `0`, the character is fetched starting from the beginning of the string. If `index` is a negative value, it is fetched starting from the end. Accessing a string out-of-bounds will cause a run-time error, pausing the project execution if run from the editor.
