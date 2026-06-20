# ScriptCreateDialog

**Inherits:** [ConfirmationDialog](class_confirmationdialog.md#class-confirmationdialog) **<** [AcceptDialog](class_acceptdialog.md#class-acceptdialog) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's popup dialog for creating new [Script](class_script.md#class-script) files.

## Description

The **ScriptCreateDialog** creates script files according to a given template for a given scripting language. The standard use is to configure its fields prior to calling one of the [Window.popup()](class_window.md#class-window-method-popup) methods.

GDScript

```gdscript
func _ready():
    var dialog = ScriptCreateDialog.new();
    dialog.config("Node", "res://new_node.gd") # For in-engine types.
    dialog.config("\"res://base_node.gd\"", "res://derived_node.gd") # For script types.
    dialog.popup_centered()
```

C#

```csharp
public override void _Ready()
{
    var dialog = new ScriptCreateDialog();
    dialog.Config("Node", "res://NewNode.cs"); // For in-engine types.
    dialog.Config("\"res://BaseNode.cs\"", "res://DerivedNode.cs"); // For script types.
    dialog.PopupCentered();
}
```

## Properties

| [bool](class_bool.md#class-bool)       | dialog_hide_on_ok   | `false` (overrides [AcceptDialog](class_acceptdialog.md#class-acceptdialog-property-dialog-hide-on-ok))   |
|----------------------------------------|---------------------|-----------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string) | ok_button_text      | `"Create"` (overrides [AcceptDialog](class_acceptdialog.md#class-acceptdialog-property-ok-button-text))   |
| [String](class_string.md#class-string) | title               | `"Attach Node Script"` (overrides [Window](class_window.md#class-window-property-title))                  |

## Methods

|    | config(inherits: [String](class_string.md#class-string), path: [String](class_string.md#class-string), built_in_enabled: [bool](class_bool.md#class-bool) = true, load_enabled: [bool](class_bool.md#class-bool) = true)   |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

## Signals

**script_created**(script: [Script](class_script.md#class-script))

Emitted when the user clicks the OK button.

---

## Method Descriptions

 **config**(inherits: [String](class_string.md#class-string), path: [String](class_string.md#class-string), built_in_enabled: [bool](class_bool.md#class-bool) = true, load_enabled: [bool](class_bool.md#class-bool) = true)

Prefills required fields to configure the ScriptCreateDialog for use.
