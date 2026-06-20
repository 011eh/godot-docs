# EditorSyntaxHighlighter

**Inherits:** [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [GDScriptSyntaxHighlighter](class_gdscriptsyntaxhighlighter.md#class-gdscriptsyntaxhighlighter)

Base class for [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter) used by the [ScriptEditor](class_scripteditor.md#class-scripteditor).

## Description

Base class that all [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter)s used by the [ScriptEditor](class_scripteditor.md#class-scripteditor) extend from.

Add a syntax highlighter to an individual script by calling [ScriptEditorBase.add_syntax_highlighter()](class_scripteditorbase.md#class-scripteditorbase-method-add-syntax-highlighter). To apply to all scripts on open, call [ScriptEditor.register_syntax_highlighter()](class_scripteditor.md#class-scripteditor-method-register-syntax-highlighter).

## Methods

| EditorSyntaxHighlighter               | \_create()                                   |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                                  | \_get_name()                               |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | \_get_supported_languages() |

---

## Method Descriptions

EditorSyntaxHighlighter **\_create**()

Virtual method which creates a new instance of the syntax highlighter.

---

[String](class_string.md#class-string) **\_get_name**()

Virtual method which can be overridden to return the syntax highlighter name.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_supported_languages**()

Virtual method which can be overridden to return the supported language names.
