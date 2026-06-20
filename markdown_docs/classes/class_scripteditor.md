# ScriptEditor

**Inherits:** [PanelContainer](class_panelcontainer.md#class-panelcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's script editor.

## Description

Godot editor's script editor.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_script_editor()](class_editorinterface.md#class-editorinterface-method-get-script-editor).

## Methods

|                                                                                                           | clear_docs_from_script(script: [Script](class_script.md#class-script))                                                                              |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)                                                     | close_file(path: [String](class_string.md#class-string))                                                                                                        |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                                   | get_breakpoints()                                                                                                                                          |
| [ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase)                                      | get_current_editor()                                                                                                                                    |
| [Script](class_script.md#class-script)                                                                    | get_current_script()                                                                                                                                    |
| [Array](class_array.md#class-array)[[ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase)] | get_open_script_editors()                                                                                                                          |
| [Array](class_array.md#class-array)[[Script](class_script.md#class-script)]                               | get_open_scripts()                                                                                                                                        |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                                   | get_unsaved_files()                                                                                                                                      |
|                                                                                                           | goto_help(topic: [String](class_string.md#class-string))                                                                                                         |
|                                                                                                           | goto_line(line_number: [int](class_int.md#class-int))                                                                                                            |
|                                                                                                           | open_script_create_dialog(base_name: [String](class_string.md#class-string), base_path: [String](class_string.md#class-string))                  |
|                                                                                                           | register_syntax_highlighter(syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter))     |
|                                                                                                           | reload_open_files()                                                                                                                                      |
|                                                                                                           | save_all_scripts()                                                                                                                                        |
|                                                                                                           | unregister_syntax_highlighter(syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter)) |
|                                                                                                           | update_docs_from_script(script: [Script](class_script.md#class-script))                                                                            |

---

## Signals

**editor_script_changed**(script: [Script](class_script.md#class-script))

Emitted when user changed active script. Argument is a freshly activated [Script](class_script.md#class-script).

---

**script_close**(script: [Script](class_script.md#class-script))

Emitted when editor is about to close the active script. Argument is a [Script](class_script.md#class-script) that is going to be closed.

---

## Method Descriptions

 **clear_docs_from_script**(script: [Script](class_script.md#class-script))

Removes the documentation for the given `script`.

**Note:** This should be called whenever the script is changed to keep the open documentation state up to date.

---

[Error](class_@globalscope.md#enum-globalscope-error) **close_file**(path: [String](class_string.md#class-string))

Closes the file at the given `path`, discarding any unsaved changes.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success or [@GlobalScope.ERR_FILE_NOT_FOUND](class_@globalscope.md#class-globalscope-constant-err-file-not-found) if the file is not found.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_breakpoints**()

Returns array of breakpoints.

---

[ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase) **get_current_editor**()

Returns the [ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase) object that the user is currently editing.

---

[Script](class_script.md#class-script) **get_current_script**()

Returns a [Script](class_script.md#class-script) that is currently active in editor.

---

[Array](class_array.md#class-array)[[ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase)] **get_open_script_editors**()

Returns an array with all [ScriptEditorBase](class_scripteditorbase.md#class-scripteditorbase) objects which are currently open in editor.

---

[Array](class_array.md#class-array)[[Script](class_script.md#class-script)] **get_open_scripts**()

Returns an array with all [Script](class_script.md#class-script) objects which are currently open in editor.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_unsaved_files**()

Returns an array of file paths of scripts with unsaved changes open in the editor.

---

 **goto_help**(topic: [String](class_string.md#class-string))

Opens help for the given topic. The `topic` is an encoded string that controls which class, method, constant, signal, annotation, property, or theme item should be focused.

The supported `topic` formats include `class_name:class`, `class_method:class:method`, `class_constant:class:constant`, `class_signal:class:signal`, `class_annotation:class:@annotation`, `class_property:class:property`, and `class_theme_item:class:item`, where `class` is the class name, `method` is the method name, `constant` is the constant name, `signal` is the signal name, `annotation` is the annotation name, `property` is the property name, and `item` is the theme item.

```gdscript
# Shows help for the Node class.
class_name:Node
# Shows help for the global min function.
# Global objects are accessible in the `@GlobalScope` namespace, shown here.
class_method:@GlobalScope:min
# Shows help for get_viewport in the Node class.
class_method:Node:get_viewport
# Shows help for the Input constant MOUSE_BUTTON_MIDDLE.
class_constant:Input:MOUSE_BUTTON_MIDDLE
# Shows help for the BaseButton signal pressed.
class_signal:BaseButton:pressed
# Shows help for the CanvasItem property visible.
class_property:CanvasItem:visible
# Shows help for the GDScript annotation export.
# Annotations should be prefixed with the `@` symbol in the descriptor, as shown here.
class_annotation:@GDScript:@export
# Shows help for the GraphNode theme item named panel_selected.
class_theme_item:GraphNode:panel_selected
```

---

 **goto_line**(line_number: [int](class_int.md#class-int))

Goes to the specified line in the current script.

---

 **open_script_create_dialog**(base_name: [String](class_string.md#class-string), base_path: [String](class_string.md#class-string))

Opens the script create dialog. The script will extend `base_name`. The file extension can be omitted from `base_path`. It will be added based on the selected scripting language.

---

 **register_syntax_highlighter**(syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter))

Registers the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) to the editor, the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) will be available on all open scripts.

**Note:** Does not apply to scripts that are already opened.

---

 **reload_open_files**()

Reloads all currently opened files. This should be used when opened files are changed outside of the script editor. The user may be prompted to resolve file conflicts, see [EditorSettings.text_editor/behavior/files/auto_reload_scripts_on_external_change](class_editorsettings.md#class-editorsettings-property-text-editor-behavior-files-auto-reload-scripts-on-external-change).

---

 **save_all_scripts**()

Saves all open scripts.

---

 **unregister_syntax_highlighter**(syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter))

Unregisters the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) from the editor.

**Note:** The [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class-editorsyntaxhighlighter) will still be applied to scripts that are already opened.

---

 **update_docs_from_script**(script: [Script](class_script.md#class-script))

Updates the documentation for the given `script`.

**Note:** This should be called whenever the script is changed to keep the open documentation state up to date.
