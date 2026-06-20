# EditorScript

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base script that can be used to add extension functions to the editor.

## Description

Scripts extending this class and implementing its \_run() method can be executed from the Script Editor's **File > Run** menu option (or by pressing `Ctrl + Shift + X`) while the editor is running. This is useful for adding custom in-editor functionality to Godot. For more complex additions, consider using [EditorPlugin](class_editorplugin.md#class-editorplugin)s instead.

If a script extending this class also has a global class name, it will be included in the editor's command palette.

**Note:** Extending scripts need to have `tool` mode enabled.

**Example:** Running the following script prints "Hello from the Godot Editor!":

GDScript

```gdscript
@tool
extends EditorScript

func _run():
    print("Hello from the Godot Editor!")
```

C#

```csharp
using Godot;

[Tool]
public partial class HelloEditor : EditorScript
{
    public override void _Run()
    {
        GD.Print("Hello from the Godot Editor!");
    }
}
```

**Note:** EditorScript is [RefCounted](class_refcounted.md#class-refcounted), meaning it is destroyed when nothing references it. This can cause errors during asynchronous operations if there are no references to the script.

## Methods

|                                                                   | \_run()                                                 |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|                                                                   | add_root_node(node: [Node](class_node.md#class-node)) |
| [EditorInterface](class_editorinterface.md#class-editorinterface) | get_editor_interface()                         |
| [Node](class_node.md#class-node)                                  | get_scene()                                               |

---

## Method Descriptions

 **\_run**()

This method is executed by the Editor when **File > Run** is used.

---

 **add_root_node**(node: [Node](class_node.md#class-node))

**Deprecated:** Use [EditorInterface.add_root_node()](class_editorinterface.md#class-editorinterface-method-add-root-node) instead.

Makes `node` root of the currently opened scene. Only works if the scene is empty. If the `node` is a scene instance, an inheriting scene will be created.

---

[EditorInterface](class_editorinterface.md#class-editorinterface) **get_editor_interface**()

**Deprecated:** [EditorInterface](class_editorinterface.md#class-editorinterface) is a global singleton and can be accessed directly by its name.

Returns the [EditorInterface](class_editorinterface.md#class-editorinterface) singleton instance.

---

[Node](class_node.md#class-node) **get_scene**()

**Deprecated:** Use [EditorInterface.get_edited_scene_root()](class_editorinterface.md#class-editorinterface-method-get-edited-scene-root) instead.

Returns the edited (current) scene's root [Node](class_node.md#class-node). Equivalent of [EditorInterface.get_edited_scene_root()](class_editorinterface.md#class-editorinterface-method-get-edited-scene-root).
