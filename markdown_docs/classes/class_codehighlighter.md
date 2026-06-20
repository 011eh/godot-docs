# CodeHighlighter

**Inherits:** [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A syntax highlighter intended for code.

## Description

By adjusting various properties of this resource, you can change the colors of strings, comments, numbers, and other text patterns inside a [TextEdit](class_textedit.md#class-textedit) control.

## Properties

| [Dictionary](class_dictionary.md#class-dictionary)   | color_regions                 | `{}`                |
|------------------------------------------------------|--------------------------------------------------------------------------------|---------------------|
| [Color](class_color.md#class-color)                  | function_color               | `Color(0, 0, 0, 1)` |
| [Dictionary](class_dictionary.md#class-dictionary)   | keyword_colors               | `{}`                |
| [Dictionary](class_dictionary.md#class-dictionary)   | member_keyword_colors | `{}`                |
| [Color](class_color.md#class-color)                  | member_variable_color | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class-color)                  | number_color                   | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class-color)                  | symbol_color                   | `Color(0, 0, 0, 1)` |

## Methods

|                                     | add_color_region(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string), color: [Color](class_color.md#class-color), line_only: [bool](class_bool.md#class-bool) = false)   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                     | add_keyword_color(keyword: [String](class_string.md#class-string), color: [Color](class_color.md#class-color))                                                                                                         |
|                                     | add_member_keyword_color(member_keyword: [String](class_string.md#class-string), color: [Color](class_color.md#class-color))                                                                                    |
|                                     | clear_color_regions()                                                                                                                                                                                                |
|                                     | clear_keyword_colors()                                                                                                                                                                                              |
|                                     | clear_member_keyword_colors()                                                                                                                                                                                |
| [Color](class_color.md#class-color) | get_keyword_color(keyword: [String](class_string.md#class-string))                                                                                                                                                     |
| [Color](class_color.md#class-color) | get_member_keyword_color(member_keyword: [String](class_string.md#class-string))                                                                                                                                |
| [bool](class_bool.md#class-bool)    | has_color_region(start_key: [String](class_string.md#class-string))                                                                                                                                                     |
| [bool](class_bool.md#class-bool)    | has_keyword_color(keyword: [String](class_string.md#class-string))                                                                                                                                                     |
| [bool](class_bool.md#class-bool)    | has_member_keyword_color(member_keyword: [String](class_string.md#class-string))                                                                                                                                |
|                                     | remove_color_region(start_key: [String](class_string.md#class-string))                                                                                                                                               |
|                                     | remove_keyword_color(keyword: [String](class_string.md#class-string))                                                                                                                                               |
|                                     | remove_member_keyword_color(member_keyword: [String](class_string.md#class-string))                                                                                                                          |

---

## Property Descriptions

[Dictionary](class_dictionary.md#class-dictionary) **color_regions** = `{}`

-  **set_color_regions**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_color_regions**()

Sets the color regions. All existing regions will be removed. The [Dictionary](class_dictionary.md#class-dictionary) key is the region start and end key, separated by a space. The value is the region color.

---

[Color](class_color.md#class-color) **function_color** = `Color(0, 0, 0, 1)`

-  **set_function_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_function_color**()

Sets color for functions. A function is a non-keyword string followed by a '('.

---

[Dictionary](class_dictionary.md#class-dictionary) **keyword_colors** = `{}`

-  **set_keyword_colors**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_keyword_colors**()

Sets the keyword colors. All existing keywords will be removed. The [Dictionary](class_dictionary.md#class-dictionary) key is the keyword. The value is the keyword color.

---

[Dictionary](class_dictionary.md#class-dictionary) **member_keyword_colors** = `{}`

-  **set_member_keyword_colors**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_member_keyword_colors**()

Sets the member keyword colors. All existing member keyword will be removed. The [Dictionary](class_dictionary.md#class-dictionary) key is the member keyword. The value is the member keyword color.

---

[Color](class_color.md#class-color) **member_variable_color** = `Color(0, 0, 0, 1)`

-  **set_member_variable_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_member_variable_color**()

Sets color for member variables. A member variable is non-keyword, non-function string proceeded with a '.'.

---

[Color](class_color.md#class-color) **number_color** = `Color(0, 0, 0, 1)`

-  **set_number_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_number_color**()

Sets the color for numbers.

---

[Color](class_color.md#class-color) **symbol_color** = `Color(0, 0, 0, 1)`

-  **set_symbol_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_symbol_color**()

Sets the color for symbols.

---

## Method Descriptions

 **add_color_region**(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string), color: [Color](class_color.md#class-color), line_only: [bool](class_bool.md#class-bool) = false)

Adds a color region (such as for comments or strings) from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty [String](class_string.md#class-string), the region does not carry over to the next line.

---

 **add_keyword_color**(keyword: [String](class_string.md#class-string), color: [Color](class_color.md#class-color))

Sets the color for a keyword.

The keyword cannot contain any symbols except '_'.

---

 **add_member_keyword_color**(member_keyword: [String](class_string.md#class-string), color: [Color](class_color.md#class-color))

Sets the color for a member keyword.

The member keyword cannot contain any symbols except '_'.

It will not be highlighted if preceded by a '.'.

---

 **clear_color_regions**()

Removes all color regions.

---

 **clear_keyword_colors**()

Removes all keywords.

---

 **clear_member_keyword_colors**()

Removes all member keywords.

---

[Color](class_color.md#class-color) **get_keyword_color**(keyword: [String](class_string.md#class-string))

Returns the color for a keyword.

---

[Color](class_color.md#class-color) **get_member_keyword_color**(member_keyword: [String](class_string.md#class-string))

Returns the color for a member keyword.

---

[bool](class_bool.md#class-bool) **has_color_region**(start_key: [String](class_string.md#class-string))

Returns `true` if the start key exists, else `false`.

---

[bool](class_bool.md#class-bool) **has_keyword_color**(keyword: [String](class_string.md#class-string))

Returns `true` if the keyword exists, else `false`.

---

[bool](class_bool.md#class-bool) **has_member_keyword_color**(member_keyword: [String](class_string.md#class-string))

Returns `true` if the member keyword exists, else `false`.

---

 **remove_color_region**(start_key: [String](class_string.md#class-string))

Removes the color region that uses that start key.

---

 **remove_keyword_color**(keyword: [String](class_string.md#class-string))

Removes the keyword.

---

 **remove_member_keyword_color**(member_keyword: [String](class_string.md#class-string))

Removes the member keyword.
