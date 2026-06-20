# EditorToaster

**Inherits:** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **<** [BoxContainer](class_boxcontainer.md#class-boxcontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Manages toast notifications within the editor.

## Description

This object manages the functionality and display of toast notifications within the editor, ensuring immediate and informative alerts are presented to the user.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_editor_toaster()](class_editorinterface.md#class-editorinterface-method-get-editor-toaster).

## Methods

|    | push_toast(message: [String](class_string.md#class-string), severity: Severity = 0, tooltip: [String](class_string.md#class-string) = "")   |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

## Enumerations

enum **Severity**:

Severity **SEVERITY_INFO** = `0`

Toast will display with an INFO severity.

Severity **SEVERITY_WARNING** = `1`

Toast will display with a WARNING severity and have a corresponding color.

Severity **SEVERITY_ERROR** = `2`

Toast will display with an ERROR severity and have a corresponding color.

---

## Method Descriptions

 **push_toast**(message: [String](class_string.md#class-string), severity: Severity = 0, tooltip: [String](class_string.md#class-string) = "")

Pushes a toast notification to the editor for display.
