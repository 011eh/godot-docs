# SyntaxHighlighter

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [CodeHighlighter](class_codehighlighter.md#class-codehighlighter), [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter)

Base class for syntax highlighters. Provides syntax highlighting data to a [TextEdit](class_textedit.md#class-textedit).

## Description

Base class for syntax highlighters. Provides syntax highlighting data to a [TextEdit](class_textedit.md#class-textedit). The associated [TextEdit](class_textedit.md#class-textedit) will call into the **SyntaxHighlighter** on an as-needed basis.

**Note:** A **SyntaxHighlighter** instance should not be used across multiple [TextEdit](class_textedit.md#class-textedit) nodes.

## Methods

|                                                    | \_clear_highlighting_cache()                                            |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [Dictionary](class_dictionary.md#class-dictionary) | \_get_line_syntax_highlighting(line: [int](class_int.md#class-int)) |
|                                                    | \_update_cache()                                                                    |
|                                                    | clear_highlighting_cache()                                                      |
| [Dictionary](class_dictionary.md#class-dictionary) | get_line_syntax_highlighting(line: [int](class_int.md#class-int))           |
| [TextEdit](class_textedit.md#class-textedit)       | get_text_edit()                                                                            |
|                                                    | update_cache()                                                                              |

---

## Method Descriptions

 **\_clear_highlighting_cache**()

Virtual method which can be overridden to clear any local caches.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_line_syntax_highlighting**(line: [int](class_int.md#class-int))

Virtual method which can be overridden to return syntax highlighting data.

See get_line_syntax_highlighting() for more details.

---

 **\_update_cache**()

Virtual method which can be overridden to update any local caches.

---

 **clear_highlighting_cache**()

Clears all cached syntax highlighting data.

Then calls overridable method \_clear_highlighting_cache().

---

[Dictionary](class_dictionary.md#class-dictionary) **get_line_syntax_highlighting**(line: [int](class_int.md#class-int))

Returns the syntax highlighting data for the line at index `line`. If the line is not cached, calls \_get_line_syntax_highlighting() first to calculate the data.

Each entry is a column number containing a nested [Dictionary](class_dictionary.md#class-dictionary). The column number denotes the start of a region, the region will end if another region is found, or at the end of the line. The nested [Dictionary](class_dictionary.md#class-dictionary) contains the data for that region. Currently only the key `"color"` is supported.

**Example:** Possible return value. This means columns `0` to `4` should be red, and columns `5` to the end of the line should be green:

```gdscript
{
    0: {
        "color": Color(1, 0, 0)
    },
    5: {
        "color": Color(0, 1, 0)
    }
}
```

---

[TextEdit](class_textedit.md#class-textedit) **get_text_edit**()

Returns the associated [TextEdit](class_textedit.md#class-textedit) node.

---

 **update_cache**()

Clears then updates the **SyntaxHighlighter** caches. Override \_update_cache() for a callback.

**Note:** This is called automatically when the associated [TextEdit](class_textedit.md#class-textedit) node, updates its own cache.
