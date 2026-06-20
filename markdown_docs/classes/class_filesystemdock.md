# FileSystemDock

**Inherits:** [EditorDock](class_editordock.md#class-editordock) **<** [MarginContainer](class_margincontainer.md#class-margincontainer) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's dock for managing files in the project.

## Description

This class is available only in [EditorPlugin](class_editorplugin.md#class-editorplugin)s and can't be instantiated. You can access it using [EditorInterface.get_file_system_dock()](class_editorinterface.md#class-editorinterface-method-get-file-system-dock).

While **FileSystemDock** doesn't expose any methods for file manipulation, it can listen for various file-related signals.

## Methods

|    | add_resource_tooltip_plugin(plugin: [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class-editorresourcetooltipplugin))       |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | navigate_to_path(path: [String](class_string.md#class-string))                                                                                              |
|    | remove_resource_tooltip_plugin(plugin: [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class-editorresourcetooltipplugin)) |

---

## Signals

**display_mode_changed**()

Emitted when the user switches file display mode or split mode.

---

**file_removed**(file: [String](class_string.md#class-string))

Emitted when the given `file` was removed.

---

**files_moved**(old_file: [String](class_string.md#class-string), new_file: [String](class_string.md#class-string))

Emitted when a file is moved from `old_file` path to `new_file` path.

---

**folder_color_changed**()

Emitted when folders change color.

---

**folder_moved**(old_folder: [String](class_string.md#class-string), new_folder: [String](class_string.md#class-string))

Emitted when a folder is moved from `old_folder` path to `new_folder` path.

---

**folder_removed**(folder: [String](class_string.md#class-string))

Emitted when the given `folder` was removed.

---

**inherit**(file: [String](class_string.md#class-string))

Emitted when a new scene is created that inherits the scene at `file` path.

---

**instantiate**(files: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Emitted when the given scenes are being instantiated in the editor.

---

**resource_removed**(resource: [Resource](class_resource.md#class-resource))

Emitted when an external `resource` had its file removed.

---

**selection_changed**()

Emitted when the selection changes. Use [EditorInterface.get_selected_paths()](class_editorinterface.md#class-editorinterface-method-get-selected-paths) in the connected method to get the selected paths.

---

## Method Descriptions

 **add_resource_tooltip_plugin**(plugin: [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class-editorresourcetooltipplugin))

Registers a new [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class-editorresourcetooltipplugin).

---

 **navigate_to_path**(path: [String](class_string.md#class-string))

Sets the given `path` as currently selected, ensuring that the selected file/directory is visible.

---

 **remove_resource_tooltip_plugin**(plugin: [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class-editorresourcetooltipplugin))

Removes an [EditorResourceTooltipPlugin](class_editorresourcetooltipplugin.md#class-editorresourcetooltipplugin). Fails if the plugin wasn't previously added.
