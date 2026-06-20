# EditorCommandPalette

**Inherits:** [ConfirmationDialog](class_confirmationdialog.md#class-confirmationdialog) **<** [AcceptDialog](class_acceptdialog.md#class-acceptdialog) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's command palette.

## Description

Object that holds all the available Commands and their shortcuts text. These Commands can be accessed through **Editor > Command Palette** menu.

Command key names use slash delimiters to distinguish sections, for example: `"example/command1"` then `example` will be the section name.

GDScript

```gdscript
var command_palette = EditorInterface.get_command_palette()
# external_command is a function that will be called with the command is executed.
var command_callable = Callable(self, "external_command").bind(arguments)
command_palette.add_command("command", "test/command",command_callable)
```

C#

```csharp
EditorCommandPalette commandPalette = EditorInterface.Singleton.GetCommandPalette();
// ExternalCommand is a function that will be called with the command is executed.
Callable commandCallable = new Callable(this, MethodName.ExternalCommand);
commandPalette.AddCommand("command", "test/command", commandCallable)
```

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_command_palette()](class_editorinterface.md#class-editorinterface-method-get-command-palette).

## Methods

|    | add_command(command_name: [String](class_string.md#class-string), key_name: [String](class_string.md#class-string), binded_callable: [Callable](class_callable.md#class-callable), shortcut_text: [String](class_string.md#class-string) = "None")   |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | remove_command(key_name: [String](class_string.md#class-string))                                                                                                                                                                                  |

---

## Method Descriptions

 **add_command**(command_name: [String](class_string.md#class-string), key_name: [String](class_string.md#class-string), binded_callable: [Callable](class_callable.md#class-callable), shortcut_text: [String](class_string.md#class-string) = "None")

Adds a custom command to EditorCommandPalette.

- `command_name`: [String](class_string.md#class-string) (Name of the **Command**. This is displayed to the user.)
- `key_name`: [String](class_string.md#class-string) (Name of the key for a particular **Command**. This is used to uniquely identify the **Command**.)
- `binded_callable`: [Callable](class_callable.md#class-callable) (Callable of the **Command**. This will be executed when the **Command** is selected.)
- `shortcut_text`: [String](class_string.md#class-string) (Shortcut text of the **Command** if available.)

---

 **remove_command**(key_name: [String](class_string.md#class-string))

Removes the custom command from EditorCommandPalette.

- `key_name`: [String](class_string.md#class-string) (Name of the key for a particular **Command**.)
