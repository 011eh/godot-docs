# ScriptEditorBase

**Inherits:** [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Base editor for editing scripts in the [ScriptEditor](class_scripteditor.md#class-scripteditor).

## Description

Base editor for editing scripts in the [ScriptEditor](class_scripteditor.md#class-scripteditor). This does not include documentation items.

## Methods

|                                           | add_syntax_highlighter(highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter))   |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Control](class_control.md#class-control) | get_base_editor()                                                                                                                       |

---

## Signals

**edited_script_changed**()

Emitted after script validation.

---

**go_to_help**(what: [String](class_string.md#class-string))

Emitted when the user requests a specific documentation page.

---

**go_to_method**(script: [Object](class_object.md#class-object), method: [String](class_string.md#class-string))

Emitted when the user requests to view a specific method of a script, similar to request_open_script_at_line.

---

**name_changed**()

Emitted after script validation or when the edited resource has changed.

---

**replace_in_files_requested**(text: [String](class_string.md#class-string))

Emitted when the user request to find and replace text in the file system.

---

**request_help**(topic: [String](class_string.md#class-string))

Emitted when the user requests contextual help.

---

**request_open_script_at_line**(script: [Object](class_object.md#class-object), line: [int](class_int.md#class-int))

Emitted when the user requests to view a specific line of a script, similar to go_to_method.

---

**request_save_history**()

Emitted when the user contextual goto and the item is in the same script.

---

**request_save_previous_state**(state: [Dictionary](class_dictionary.md#class-dictionary))

Emitted when the user changes current script or moves caret by 10 or more columns within the same script.

---

**search_in_files_requested**(text: [String](class_string.md#class-string))

Emitted when the user request to search text in the file system.

---

## Method Descriptions

 **add_syntax_highlighter**(highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter))

Adds an [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) to the open script.

---

[Control](class_control.md#class-control) **get_base_editor**()

Returns the underlying [Control](class_control.md#class-control) used for editing scripts. For text scripts, this is a [CodeEdit](class_codeedit.md#class-codeedit).
