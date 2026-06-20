# EditorPlugin

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [GridMapEditorPlugin](class_gridmapeditorplugin.md#class-gridmapeditorplugin)

Used by the editor to extend its functionality.

## Description

Plugins are used by the editor to extend functionality. The most common types of plugins are those which edit a given node or resource type, import plugins and export plugins. See also [EditorScript](class_editorscript.md#class-editorscript) to add functions to the editor.

**Note:** Some names in this class contain "left" or "right" (e.g. DOCK_SLOT_LEFT_UL). These APIs assume left-to-right layout, and would be backwards when using right-to-left layout. These names are kept for compatibility reasons.

## Tutorials

- [Editor plugins documentation index](../tutorials/plugins/editor/index.md)

## Methods

|                                                                                     | \_apply_changes()                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                    | \_build()                                                                                                                                                                                                                                    |
|                                                                                     | \_clear()                                                                                                                                                                                                                                    |
|                                                                                     | \_disable_plugin()                                                                                                                                                                                                                  |
|                                                                                     | \_edit(object: [Object](class_object.md#class-object))                                                                                                                                                                                        |
|                                                                                     | \_enable_plugin()                                                                                                                                                                                                                    |
|                                                                                     | \_forward_3d_draw_over_viewport(viewport_control: [Control](class_control.md#class-control))                                                                                                                         |
|                                                                                     | \_forward_3d_force_draw_over_viewport(viewport_control: [Control](class_control.md#class-control))                                                                                                             |
| [int](class_int.md#class-int)                                                       | \_forward_3d_gui_input(viewport_camera: [Camera3D](class_camera3d.md#class-camera3d), event: [InputEvent](class_inputevent.md#class-inputevent))                                                                              |
|                                                                                     | \_forward_canvas_draw_over_viewport(viewport_control: [Control](class_control.md#class-control))                                                                                                                 |
|                                                                                     | \_forward_canvas_force_draw_over_viewport(viewport_control: [Control](class_control.md#class-control))                                                                                                     |
| [bool](class_bool.md#class-bool)                                                    | \_forward_canvas_gui_input(event: [InputEvent](class_inputevent.md#class-inputevent))                                                                                                                                     |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)             | \_get_breakpoints()                                                                                                                                                                                                                |
| [Texture2D](class_texture2d.md#class-texture2d)                                     | \_get_plugin_icon()                                                                                                                                                                                                                |
| [String](class_string.md#class-string)                                              | \_get_plugin_name()                                                                                                                                                                                                                |
| [Dictionary](class_dictionary.md#class-dictionary)                                  | \_get_state()                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)                                              | \_get_unsaved_status(for_scene: [String](class_string.md#class-string))                                                                                                                                                         |
|                                                                                     | \_get_window_layout(configuration: [ConfigFile](class_configfile.md#class-configfile))                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                    | \_handles(object: [Object](class_object.md#class-object))                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                    | \_has_main_screen()                                                                                                                                                                                                                |
|                                                                                     | \_make_visible(visible: [bool](class_bool.md#class-bool))                                                                                                                                                                             |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)             | \_run_scene(scene: [String](class_string.md#class-string), args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                                                                                |
|                                                                                     | \_save_external_data()                                                                                                                                                                                                          |
|                                                                                     | \_set_state(state: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                                                                   |
|                                                                                     | \_set_window_layout(configuration: [ConfigFile](class_configfile.md#class-configfile))                                                                                                                                           |
|                                                                                     | add_autoload_singleton(name: [String](class_string.md#class-string), path: [String](class_string.md#class-string))                                                                                                                  |
|                                                                                     | add_context_menu_plugin(slot: [ContextMenuSlot](class_editorcontextmenuplugin.md#enum-editorcontextmenuplugin-contextmenuslot), plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class-editorcontextmenuplugin)) |
| [Button](class_button.md#class-button)                                              | add_control_to_bottom_panel(control: [Control](class_control.md#class-control), title: [String](class_string.md#class-string), shortcut: [Shortcut](class_shortcut.md#class-shortcut) = null)                                  |
|                                                                                     | add_control_to_container(container: CustomControlContainer, control: [Control](class_control.md#class-control))                                                                      |
|                                                                                     | add_control_to_dock(slot: DockSlot, control: [Control](class_control.md#class-control), shortcut: [Shortcut](class_shortcut.md#class-shortcut) = null)                                                  |
|                                                                                     | add_custom_type(type: [String](class_string.md#class-string), base: [String](class_string.md#class-string), script: [Script](class_script.md#class-script), icon: [Texture2D](class_texture2d.md#class-texture2d))                         |
|                                                                                     | add_debugger_plugin(script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin))                                                                                                                          |
|                                                                                     | add_dock(dock: [EditorDock](class_editordock.md#class-editordock))                                                                                                                                                                                |
|                                                                                     | add_export_platform(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform))                                                                                                                        |
|                                                                                     | add_export_plugin(plugin: [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin))                                                                                                                                    |
|                                                                                     | add_import_plugin(importer: [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin), first_priority: [bool](class_bool.md#class-bool) = false)                                                                        |
|                                                                                     | add_inspector_plugin(plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin))                                                                                                                     |
|                                                                                     | add_node_3d_gizmo_plugin(plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin))                                                                                                       |
|                                                                                     | add_resource_conversion_plugin(plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin))                                                                      |
|                                                                                     | add_scene_format_importer_plugin(scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter), first_priority: [bool](class_bool.md#class-bool) = false)        |
|                                                                                     | add_scene_post_import_plugin(scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin), first_priority: [bool](class_bool.md#class-bool) = false)            |
|                                                                                     | add_tool_menu_item(name: [String](class_string.md#class-string), callable: [Callable](class_callable.md#class-callable))                                                                                                                |
|                                                                                     | add_tool_submenu_item(name: [String](class_string.md#class-string), submenu: [PopupMenu](class_popupmenu.md#class-popupmenu))                                                                                                        |
|                                                                                     | add_translation_parser_plugin(parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class-editortranslationparserplugin))                                                                           |
|                                                                                     | add_undo_redo_inspector_hook_callback(callable: [Callable](class_callable.md#class-callable))                                                                                                                        |
| [EditorInterface](class_editorinterface.md#class-editorinterface)                   | get_editor_interface()                                                                                                                                                                                                                |
| [PopupMenu](class_popupmenu.md#class-popupmenu)                                     | get_export_as_menu()                                                                                                                                                                                                                    |
| [String](class_string.md#class-string)                                              | get_plugin_version()                                                                                                                                                                                                                    |
| [ScriptCreateDialog](class_scriptcreatedialog.md#class-scriptcreatedialog)          | get_script_create_dialog()                                                                                                                                                                                                        |
| [EditorUndoRedoManager](class_editorundoredomanager.md#class-editorundoredomanager) | get_undo_redo()                                                                                                                                                                                                                              |
|                                                                                     | hide_bottom_panel()                                                                                                                                                                                                                      |
|                                                                                     | make_bottom_panel_item_visible(item: [Control](class_control.md#class-control))                                                                                                                                             |
|                                                                                     | queue_save_layout()                                                                                                                                                                                                                      |
|                                                                                     | remove_autoload_singleton(name: [String](class_string.md#class-string))                                                                                                                                                          |
|                                                                                     | remove_context_menu_plugin(plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class-editorcontextmenuplugin))                                                                                                   |
|                                                                                     | remove_control_from_bottom_panel(control: [Control](class_control.md#class-control))                                                                                                                                      |
|                                                                                     | remove_control_from_container(container: CustomControlContainer, control: [Control](class_control.md#class-control))                                                            |
|                                                                                     | remove_control_from_docks(control: [Control](class_control.md#class-control))                                                                                                                                                    |
|                                                                                     | remove_custom_type(type: [String](class_string.md#class-string))                                                                                                                                                                        |
|                                                                                     | remove_debugger_plugin(script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin))                                                                                                                    |
|                                                                                     | remove_dock(dock: [EditorDock](class_editordock.md#class-editordock))                                                                                                                                                                          |
|                                                                                     | remove_export_platform(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform))                                                                                                                  |
|                                                                                     | remove_export_plugin(plugin: [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin))                                                                                                                              |
|                                                                                     | remove_import_plugin(importer: [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin))                                                                                                                            |
|                                                                                     | remove_inspector_plugin(plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin))                                                                                                               |
|                                                                                     | remove_node_3d_gizmo_plugin(plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin))                                                                                                 |
|                                                                                     | remove_resource_conversion_plugin(plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin))                                                                |
|                                                                                     | remove_scene_format_importer_plugin(scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter))                                                            |
|                                                                                     | remove_scene_post_import_plugin(scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin))                                                                |
|                                                                                     | remove_tool_menu_item(name: [String](class_string.md#class-string))                                                                                                                                                                  |
|                                                                                     | remove_translation_parser_plugin(parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class-editortranslationparserplugin))                                                                     |
|                                                                                     | remove_undo_redo_inspector_hook_callback(callable: [Callable](class_callable.md#class-callable))                                                                                                                  |
|                                                                                     | set_dock_tab_icon(control: [Control](class_control.md#class-control), icon: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                             |
|                                                                                     | set_force_draw_over_forwarding_enabled()                                                                                                                                                                            |
|                                                                                     | set_input_event_forwarding_always_enabled()                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                       | update_overlays()                                                                                                                                                                                                                          |

---

## Signals

**main_screen_changed**(screen_name: [String](class_string.md#class-string))

Emitted when user changes the workspace (**2D**, **3D**, **Script**, **Game**, **Asset Store**). Also works with custom screens defined by plugins.

---

**project_settings_changed**()

**Deprecated:** Use [ProjectSettings.settings_changed](class_projectsettings.md#class-projectsettings-signal-settings-changed) instead.

Emitted when any project setting has changed.

---

**resource_saved**(resource: [Resource](class_resource.md#class-resource))

Emitted when the given `resource` was saved on disc. See also scene_saved.

---

**scene_changed**(scene_root: [Node](class_node.md#class-node))

Emitted when the scene is changed in the editor. The argument will return the root node of the scene that has just become active. If this scene is new and empty, the argument will be `null`.

---

**scene_closed**(filepath: [String](class_string.md#class-string))

Emitted when user closes a scene. The argument is a file path to the closed scene.

---

**scene_saved**(filepath: [String](class_string.md#class-string))

Emitted when a scene was saved on disc. The argument is a file path to the saved scene. See also resource_saved.

---

## Enumerations

enum **CustomControlContainer**:

CustomControlContainer **CONTAINER_TOOLBAR** = `0`

Main editor toolbar, next to play buttons.

CustomControlContainer **CONTAINER_SPATIAL_EDITOR_MENU** = `1`

The toolbar that appears when 3D editor is active.

CustomControlContainer **CONTAINER_SPATIAL_EDITOR_SIDE_LEFT** = `2`

Left sidebar of the 3D editor.

CustomControlContainer **CONTAINER_SPATIAL_EDITOR_SIDE_RIGHT** = `3`

Right sidebar of the 3D editor.

CustomControlContainer **CONTAINER_SPATIAL_EDITOR_BOTTOM** = `4`

Bottom panel of the 3D editor.

CustomControlContainer **CONTAINER_CANVAS_EDITOR_MENU** = `5`

The toolbar that appears when 2D editor is active.

CustomControlContainer **CONTAINER_CANVAS_EDITOR_SIDE_LEFT** = `6`

Left sidebar of the 2D editor.

CustomControlContainer **CONTAINER_CANVAS_EDITOR_SIDE_RIGHT** = `7`

Right sidebar of the 2D editor.

CustomControlContainer **CONTAINER_CANVAS_EDITOR_BOTTOM** = `8`

Bottom panel of the 2D editor.

CustomControlContainer **CONTAINER_INSPECTOR_BOTTOM** = `9`

Bottom section of the inspector.

CustomControlContainer **CONTAINER_PROJECT_SETTING_TAB_LEFT** = `10`

Tab of Project Settings dialog, to the left of other tabs.

CustomControlContainer **CONTAINER_PROJECT_SETTING_TAB_RIGHT** = `11`

Tab of Project Settings dialog, to the right of other tabs.

---

enum **DockSlot**:

DockSlot **DOCK_SLOT_NONE** = `-1`

The dock is closed.

DockSlot **DOCK_SLOT_LEFT_UL** = `0`

Dock slot, left side, upper-left (empty in default layout).

DockSlot **DOCK_SLOT_LEFT_BL** = `1`

Dock slot, left side, bottom-left (empty in default layout).

DockSlot **DOCK_SLOT_LEFT_UR** = `2`

Dock slot, left side, upper-right (in default layout includes Scene and Import docks).

DockSlot **DOCK_SLOT_LEFT_BR** = `3`

Dock slot, left side, bottom-right (in default layout includes FileSystem dock).

DockSlot **DOCK_SLOT_RIGHT_UL** = `4`

Dock slot, right side, upper-left (in default layout includes Inspector, Node, and History docks).

DockSlot **DOCK_SLOT_RIGHT_BL** = `5`

Dock slot, right side, bottom-left (empty in default layout).

DockSlot **DOCK_SLOT_RIGHT_UR** = `6`

Dock slot, right side, upper-right (empty in default layout).

DockSlot **DOCK_SLOT_RIGHT_BR** = `7`

Dock slot, right side, bottom-right (empty in default layout).

DockSlot **DOCK_SLOT_BOTTOM** = `8`

Bottom panel.

DockSlot **DOCK_SLOT_MAX** = `9`

Represents the size of the DockSlot enum.

---

enum **AfterGUIInput**:

AfterGUIInput **AFTER_GUI_INPUT_PASS** = `0`

Forwards the [InputEvent](class_inputevent.md#class-inputevent) to other EditorPlugins.

AfterGUIInput **AFTER_GUI_INPUT_STOP** = `1`

Prevents the [InputEvent](class_inputevent.md#class-inputevent) from reaching other Editor classes.

AfterGUIInput **AFTER_GUI_INPUT_CUSTOM** = `2`

Pass the [InputEvent](class_inputevent.md#class-inputevent) to other editor plugins except the main [Node3D](class_node3d.md#class-node3d) one. This can be used to prevent node selection changes and work with sub-gizmos instead.

---

## Method Descriptions

 **\_apply_changes**()

This method is called when the editor is about to save the project, switch to another tab, etc. It asks the plugin to apply any pending state changes to ensure consistency.

This is used, for example, in shader editors to let the plugin know that it must apply the shader code being written by the user to the object.

---

[bool](class_bool.md#class-bool) **\_build**()

This method is called when the editor is about to run the project. The plugin can then perform required operations before the project runs.

This method must return a boolean. If this method returns `false`, the project will not run. The run is aborted immediately, so this also prevents all other plugins' \_build() methods from running.

---

 **\_clear**()

Clear all the state and reset the object being edited to zero. This ensures your plugin does not keep editing a currently existing node, or a node from the wrong scene.

---

 **\_disable_plugin**()

Called by the engine when the user disables the **EditorPlugin** in the Plugin tab of the project settings window.

---

 **\_edit**(object: [Object](class_object.md#class-object))

This function is used for plugins that edit specific object types (nodes or resources). It requests the editor to edit the given object.

`object` can be `null` if the plugin was editing an object, but there is no longer any selected object handled by this plugin. It can be used to cleanup editing state.

---

 **\_enable_plugin**()

Called by the engine when the user enables the **EditorPlugin** in the Plugin tab of the project settings window.

---

 **\_forward_3d_draw_over_viewport**(viewport_control: [Control](class_control.md#class-control))

Called by the engine when the 3D editor's viewport is updated. `viewport_control` is an overlay on top of the viewport and it can be used for drawing. You can update the viewport manually by calling update_overlays().

GDScript

```gdscript
func _forward_3d_draw_over_viewport(overlay):
    # Draw a circle at the cursor's position.
    overlay.draw_circle(overlay.get_local_mouse_position(), 64, Color.WHITE)

func _forward_3d_gui_input(camera, event):
    if event is InputEventMouseMotion:
        # Redraw the viewport when the cursor is moved.
        update_overlays()
        return EditorPlugin.AFTER_GUI_INPUT_STOP
    return EditorPlugin.AFTER_GUI_INPUT_PASS
```

C#

```csharp
public override void _Forward3DDrawOverViewport(Control viewportControl)
{
    // Draw a circle at the cursor's position.
    viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64, Colors.White);
}

public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D viewportCamera, InputEvent @event)
{
    if (@event is InputEventMouseMotion)
    {
        // Redraw the viewport when the cursor is moved.
        UpdateOverlays();
        return EditorPlugin.AfterGuiInput.Stop;
    }
    return EditorPlugin.AfterGuiInput.Pass;
}
```

---

 **\_forward_3d_force_draw_over_viewport**(viewport_control: [Control](class_control.md#class-control))

This method is the same as \_forward_3d_draw_over_viewport(), except it draws on top of everything. Useful when you need an extra layer that shows over anything else.

You need to enable calling of this method by using set_force_draw_over_forwarding_enabled().

---

[int](class_int.md#class-int) **\_forward_3d_gui_input**(viewport_camera: [Camera3D](class_camera3d.md#class-camera3d), event: [InputEvent](class_inputevent.md#class-inputevent))

Called when there is a root node in the current edited scene, \_handles() is implemented, and an [InputEvent](class_inputevent.md#class-inputevent) happens in the 3D viewport. The return value decides whether the [InputEvent](class_inputevent.md#class-inputevent) is consumed or forwarded to other **EditorPlugin**s. See AfterGUIInput for options.

GDScript

```gdscript
# Prevents the InputEvent from reaching other Editor classes.
func _forward_3d_gui_input(camera, event):
    return EditorPlugin.AFTER_GUI_INPUT_STOP
```

C#

```csharp
// Prevents the InputEvent from reaching other Editor classes.
public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D camera, InputEvent @event)
{
    return EditorPlugin.AfterGuiInput.Stop;
}
```

This method must return AFTER_GUI_INPUT_PASS in order to forward the [InputEvent](class_inputevent.md#class-inputevent) to other Editor classes.

GDScript

```gdscript
# Consumes InputEventMouseMotion and forwards other InputEvent types.
func _forward_3d_gui_input(camera, event):
    return EditorPlugin.AFTER_GUI_INPUT_STOP if event is InputEventMouseMotion else EditorPlugin.AFTER_GUI_INPUT_PASS
```

C#

```csharp
// Consumes InputEventMouseMotion and forwards other InputEvent types.
public override EditorPlugin.AfterGuiInput _Forward3DGuiInput(Camera3D camera, InputEvent @event)
{
    return @event is InputEventMouseMotion ? EditorPlugin.AfterGuiInput.Stop : EditorPlugin.AfterGuiInput.Pass;
}
```

---

 **\_forward_canvas_draw_over_viewport**(viewport_control: [Control](class_control.md#class-control))

Called by the engine when the 2D editor's viewport is updated. `viewport_control` is an overlay on top of the viewport and it can be used for drawing. You can update the viewport manually by calling update_overlays().

GDScript

```gdscript
func _forward_canvas_draw_over_viewport(overlay):
    # Draw a circle at the cursor's position.
    overlay.draw_circle(overlay.get_local_mouse_position(), 64, Color.WHITE)

func _forward_canvas_gui_input(event):
    if event is InputEventMouseMotion:
        # Redraw the viewport when the cursor is moved.
        update_overlays()
        return true
    return false
```

C#

```csharp
public override void _ForwardCanvasDrawOverViewport(Control viewportControl)
{
    // Draw a circle at the cursor's position.
    viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64, Colors.White);
}

public override bool _ForwardCanvasGuiInput(InputEvent @event)
{
    if (@event is InputEventMouseMotion)
    {
        // Redraw the viewport when the cursor is moved.
        UpdateOverlays();
        return true;
    }
    return false;
}
```

---

 **\_forward_canvas_force_draw_over_viewport**(viewport_control: [Control](class_control.md#class-control))

This method is the same as \_forward_canvas_draw_over_viewport(), except it draws on top of everything. Useful when you need an extra layer that shows over anything else.

You need to enable calling of this method by using set_force_draw_over_forwarding_enabled().

---

[bool](class_bool.md#class-bool) **\_forward_canvas_gui_input**(event: [InputEvent](class_inputevent.md#class-inputevent))

Called when there is a root node in the current edited scene, \_handles() is implemented, and an [InputEvent](class_inputevent.md#class-inputevent) happens in the 2D viewport. If this method returns `true`, `event` is intercepted by this **EditorPlugin**, otherwise `event` is forwarded to other Editor classes.

GDScript

```gdscript
# Prevents the InputEvent from reaching other Editor classes.
func _forward_canvas_gui_input(event):
    return true
```

C#

```csharp
// Prevents the InputEvent from reaching other Editor classes.
public override bool ForwardCanvasGuiInput(InputEvent @event)
{
    return true;
}
```

This method must return `false` in order to forward the [InputEvent](class_inputevent.md#class-inputevent) to other Editor classes.

GDScript

```gdscript
# Consumes InputEventMouseMotion and forwards other InputEvent types.
func _forward_canvas_gui_input(event):
    if (event is InputEventMouseMotion):
        return true
    return false
```

C#

```csharp
// Consumes InputEventMouseMotion and forwards other InputEvent types.
public override bool _ForwardCanvasGuiInput(InputEvent @event)
{
    if (@event is InputEventMouseMotion)
    {
        return true;
    }
    return false;
}
```

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_breakpoints**()

This is for editors that edit script-based objects. You can return a list of breakpoints in the format (`script:line`), for example: `res://path_to_script.gd:25`.

---

[Texture2D](class_texture2d.md#class-texture2d) **\_get_plugin_icon**()

Override this method in your plugin to return a [Texture2D](class_texture2d.md#class-texture2d) in order to give it an icon.

For main screen plugins, this appears at the top of the screen, to the right of the "2D", "3D", "Script", "Game", and "Asset Store" buttons.

Ideally, the plugin icon should be white with a transparent background and 16×16 pixels in size.

GDScript

```gdscript
func _get_plugin_icon():
    # You can use a custom icon:
    return preload("res://addons/my_plugin/my_plugin_icon.svg")
    # Or use a built-in icon:
    return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")
```

C#

```csharp
public override Texture2D _GetPluginIcon()
{
    // You can use a custom icon:
    return ResourceLoader.Load<Texture2D>("res://addons/my_plugin/my_plugin_icon.svg");
    // Or use a built-in icon:
    return EditorInterface.Singleton.GetEditorTheme().GetIcon("Node", "EditorIcons");
}
```

---

[String](class_string.md#class-string) **\_get_plugin_name**()

Override this method in your plugin to provide the name of the plugin when displayed in the Godot editor.

For main screen plugins, this appears at the top of the screen, to the right of the "2D", "3D", "Script", "Game", and "Asset Store" buttons.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_state**()

Override this method to provide a state data you want to be saved, like view position, grid settings, folding, etc. This is used when saving the scene (so state is kept when opening it again) and for switching tabs (so state can be restored when the tab returns). This data is automatically saved for each scene in an `editstate` file in the editor metadata folder. If you want to store global (scene-independent) editor data for your plugin, you can use \_get_window_layout() instead.

Use \_set_state() to restore your saved state.

**Note:** This method should not be used to save important settings that should persist with the project.

**Note:** You must implement \_get_plugin_name() for the state to be stored and restored correctly.

```gdscript
func _get_state():
    var state = { "zoom": zoom, "preferred_color": my_color }
    return state
```

---

[String](class_string.md#class-string) **\_get_unsaved_status**(for_scene: [String](class_string.md#class-string))

Override this method to provide a custom message that lists unsaved changes. The editor will call this method when exiting or when closing a scene, and display the returned string in a confirmation dialog. Return empty string if the plugin has no unsaved changes.

When closing a scene, `for_scene` is the path to the scene being closed. You can use it to handle built-in resources in that scene.

If the user confirms saving, \_save_external_data() will be called, before closing the editor.

```gdscript
func _get_unsaved_status(for_scene):
    if not unsaved:
        return ""

    if for_scene.is_empty():
        return "Save changes in MyCustomPlugin before closing?"
    else:
        return "Scene %s has changes from MyCustomPlugin. Save before closing?" % for_scene.get_file()

func _save_external_data():
    unsaved = false
```

If the plugin has no scene-specific changes, you can ignore the calls when closing scenes:

```gdscript
func _get_unsaved_status(for_scene):
    if not for_scene.is_empty():
        return ""
```

---

 **\_get_window_layout**(configuration: [ConfigFile](class_configfile.md#class-configfile))

Override this method to provide the GUI layout of the plugin or any other data you want to be stored. This is used to save the project's editor layout when queue_save_layout() is called or the editor layout was changed (for example changing the position of a dock). The data is stored in the `editor_layout.cfg` file in the editor metadata directory.

Use \_set_window_layout() to restore your saved layout.

```gdscript
func _get_window_layout(configuration):
    configuration.set_value("MyPlugin", "window_position", $Window.position)
    configuration.set_value("MyPlugin", "icon_color", $Icon.modulate)
```

---

[bool](class_bool.md#class-bool) **\_handles**(object: [Object](class_object.md#class-object))

Implement this function if your plugin edits a specific type of object (Resource or Node). If you return `true`, then you will get the functions \_edit() and \_make_visible() called when the editor requests them. If you have declared the methods \_forward_canvas_gui_input() and \_forward_3d_gui_input() these will be called too.

**Note:** Each plugin should handle only one type of objects at a time. If a plugin handles more types of objects and they are edited at the same time, it will result in errors.

---

[bool](class_bool.md#class-bool) **\_has_main_screen**()

Returns `true` if this is a main screen editor plugin (it goes in the workspace selector together with **2D**, **3D**, **Script**, **Game**, and **Asset Store**).

When the plugin's workspace is selected, other main screen plugins will be hidden, but your plugin will not appear automatically. It needs to be added as a child of [EditorInterface.get_editor_main_screen()](class_editorinterface.md#class-editorinterface-method-get-editor-main-screen) and made visible inside \_make_visible().

Use \_get_plugin_name() and \_get_plugin_icon() to customize the plugin button's appearance.

```gdscript
var plugin_control

func _enter_tree():
    plugin_control = preload("my_plugin_control.tscn").instantiate()
    EditorInterface.get_editor_main_screen().add_child(plugin_control)
    plugin_control.hide()

func _has_main_screen():
    return true

func _make_visible(visible):
    plugin_control.visible = visible

func _get_plugin_name():
    return "My Super Cool Plugin 3000"

func _get_plugin_icon():
    return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")
```

---

 **\_make_visible**(visible: [bool](class_bool.md#class-bool))

This function will be called when the editor is requested to become visible. It is used for plugins that edit a specific object type.

Remember that you have to manage the visibility of all your editor controls manually.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_run_scene**(scene: [String](class_string.md#class-string), args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

This function is called when an individual scene is about to be played in the editor. `args` is a list of command line arguments that will be passed to the new Godot instance, which will be replaced by the list returned by this function.

```gdscript
func _run_scene(scene, args):
    args.append("--an-extra-argument")
    return args
```

**Note:** Text that is printed in this method will not be visible in the editor's Output panel unless [EditorSettings.run/output/always_clear_output_on_play](class_editorsettings.md#class-editorsettings-property-run-output-always-clear-output-on-play) is `false`.

---

 **\_save_external_data**()

This method is called after the editor saves the project or when it's closed. It asks the plugin to save edited external scenes/resources.

---

 **\_set_state**(state: [Dictionary](class_dictionary.md#class-dictionary))

Restore the state saved by \_get_state(). This method is called when the current scene tab is changed in the editor.

**Note:** Your plugin must implement \_get_plugin_name(), otherwise it will not be recognized and this method will not be called.

```gdscript
func _set_state(data):
    zoom = data.get("zoom", 1.0)
    preferred_color = data.get("my_color", Color.WHITE)
```

---

 **\_set_window_layout**(configuration: [ConfigFile](class_configfile.md#class-configfile))

Restore the plugin GUI layout and data saved by \_get_window_layout(). This method is called for every plugin on editor startup. Use the provided `configuration` file to read your saved data.

```gdscript
func _set_window_layout(configuration):
    $Window.position = configuration.get_value("MyPlugin", "window_position", Vector2())
    $Icon.modulate = configuration.get_value("MyPlugin", "icon_color", Color.WHITE)
```

---

 **add_autoload_singleton**(name: [String](class_string.md#class-string), path: [String](class_string.md#class-string))

Adds a script at `path` to the Autoload list as `name`.

---

 **add_context_menu_plugin**(slot: [ContextMenuSlot](class_editorcontextmenuplugin.md#enum-editorcontextmenuplugin-contextmenuslot), plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class-editorcontextmenuplugin))

Adds a plugin to the context menu. `slot` is the context menu where the plugin will be added.

**Note:** A plugin instance can belong only to a single context menu slot.

---

[Button](class_button.md#class-button) **add_control_to_bottom_panel**(control: [Control](class_control.md#class-control), title: [String](class_string.md#class-string), shortcut: [Shortcut](class_shortcut.md#class-shortcut) = null)

**Deprecated:** Use add_dock() instead, with [EditorDock.default_slot](class_editordock.md#class-editordock-property-default-slot) set to DOCK_SLOT_BOTTOM.

Adds a control to the bottom panel (together with Output, Debug, Animation, etc.). Returns a reference to a button that is outside the scene tree. It's up to you to hide/show the button when needed. When your plugin is deactivated, make sure to remove your custom control with remove_control_from_bottom_panel() and free it with [Node.queue_free()](class_node.md#class-node-method-queue-free).

`shortcut` is a shortcut that, when activated, will toggle the bottom panel's visibility. The shortcut object is only set when this control is added to the bottom panel.

**Note** See the default editor bottom panel shortcuts in the Editor Settings for inspiration. By convention, they all use `Alt` modifier.

---

 **add_control_to_container**(container: CustomControlContainer, control: [Control](class_control.md#class-control))

Adds a custom control to a container in the editor UI.

Please remember that you have to manage the visibility of your custom controls yourself (and likely hide it after adding it).

When your plugin is deactivated, make sure to remove your custom control with remove_control_from_container() and free it with [Node.queue_free()](class_node.md#class-node-method-queue-free).

---

 **add_control_to_dock**(slot: DockSlot, control: [Control](class_control.md#class-control), shortcut: [Shortcut](class_shortcut.md#class-shortcut) = null)

**Deprecated:** Use add_dock() instead.

Adds the control to a specific dock slot.

If the dock is repositioned and as long as the plugin is active, the editor will save the dock position on further sessions.

When your plugin is deactivated, make sure to remove your custom control with remove_control_from_docks() and free it with [Node.queue_free()](class_node.md#class-node-method-queue-free).

Optionally, you can specify a shortcut parameter. When pressed, this shortcut will open and focus the dock.

---

 **add_custom_type**(type: [String](class_string.md#class-string), base: [String](class_string.md#class-string), script: [Script](class_script.md#class-script), icon: [Texture2D](class_texture2d.md#class-texture2d))

Adds a custom type, which will appear in the list of nodes or resources.

When a given node or resource is selected, the base type will be instantiated (e.g. "Node3D", "Control", "Resource"), then the script will be loaded and set to this object.

**Note:** The base type is the base engine class which this type's class hierarchy inherits, not any custom type parent classes.

You can use the virtual method \_handles() to check if your custom object is being edited by checking the script or using the `is` keyword.

During run-time, this will be a simple object with a script so this function does not need to be called then.

**Note:** Custom types added this way are not true classes. They are just a helper to create a node with specific script.

---

 **add_debugger_plugin**(script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin))

Adds a [Script](class_script.md#class-script) as debugger plugin to the Debugger. The script must extend [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin).

---

 **add_dock**(dock: [EditorDock](class_editordock.md#class-editordock))

Adds a new dock.

When your plugin is deactivated, make sure to remove your custom dock with remove_dock() and free it with [Node.queue_free()](class_node.md#class-node-method-queue-free).

---

 **add_export_platform**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform))

Registers a new [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform). Export platforms provides functionality of exporting to the specific platform.

---

 **add_export_plugin**(plugin: [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin))

Registers a new [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin). Export plugins are used to perform tasks when the project is being exported.

See add_inspector_plugin() for an example of how to register a plugin.

---

 **add_import_plugin**(importer: [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin), first_priority: [bool](class_bool.md#class-bool) = false)

Registers a new [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin). Import plugins are used to import custom and unsupported assets as a custom [Resource](class_resource.md#class-resource) type.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

**Note:** If you want to import custom 3D asset formats use add_scene_format_importer_plugin() instead.

See add_inspector_plugin() for an example of how to register a plugin.

---

 **add_inspector_plugin**(plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin))

Registers a new [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin). Inspector plugins are used to extend [EditorInspector](class_editorinspector.md#class-editorinspector) and provide custom configuration tools for your object's properties.

**Note:** Always use remove_inspector_plugin() to remove the registered [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin) when your **EditorPlugin** is disabled to prevent leaks and an unexpected behavior.

GDScript

```gdscript
const MyInspectorPlugin = preload("res://addons/your_addon/path/to/your/script.gd")
var inspector_plugin = MyInspectorPlugin.new()

func _enter_tree():
    add_inspector_plugin(inspector_plugin)

func _exit_tree():
    remove_inspector_plugin(inspector_plugin)
```

---

 **add_node_3d_gizmo_plugin**(plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin))

Registers a new [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin). Gizmo plugins are used to add custom gizmos to the 3D preview viewport for a [Node3D](class_node3d.md#class-node3d).

See add_inspector_plugin() for an example of how to register a plugin.

---

 **add_resource_conversion_plugin**(plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin))

Registers a new [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin). Resource conversion plugins are used to add custom resource converters to the editor inspector.

See [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin) for an example of how to create a resource conversion plugin.

---

 **add_scene_format_importer_plugin**(scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter), first_priority: [bool](class_bool.md#class-bool) = false)

Registers a new [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter). Scene importers are used to import custom 3D asset formats as scenes.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

---

 **add_scene_post_import_plugin**(scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin), first_priority: [bool](class_bool.md#class-bool) = false)

Add an [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin). These plugins allow customizing the import process of 3D assets by adding new options to the import dialogs.

If `first_priority` is `true`, the new import plugin is inserted first in the list and takes precedence over pre-existing plugins.

---

 **add_tool_menu_item**(name: [String](class_string.md#class-string), callable: [Callable](class_callable.md#class-callable))

Adds a custom menu item to **Project > Tools** named `name`. When clicked, the provided `callable` will be called.

---

 **add_tool_submenu_item**(name: [String](class_string.md#class-string), submenu: [PopupMenu](class_popupmenu.md#class-popupmenu))

Adds a custom [PopupMenu](class_popupmenu.md#class-popupmenu) submenu under **Project > Tools >** `name`. Use remove_tool_menu_item() on plugin clean up to remove the menu.

---

 **add_translation_parser_plugin**(parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class-editortranslationparserplugin))

Registers a custom translation parser plugin for extracting translatable strings from custom files.

---

 **add_undo_redo_inspector_hook_callback**(callable: [Callable](class_callable.md#class-callable))

Hooks a callback into the undo/redo action creation when a property is modified in the inspector. This allows, for example, to save other properties that may be lost when a given property is modified.

The callback should have 4 arguments: [Object](class_object.md#class-object) `undo_redo`, [Object](class_object.md#class-object) `modified_object`, [String](class_string.md#class-string) `property` and [Variant](class_variant.md#class-variant) `new_value`. They are, respectively, the [UndoRedo](class_undoredo.md#class-undoredo) object used by the inspector, the currently modified object, the name of the modified property and the new value the property is about to take.

---

[EditorInterface](class_editorinterface.md#class-editorinterface) **get_editor_interface**()

**Deprecated:** [EditorInterface](class_editorinterface.md#class-editorinterface) is a global singleton and can be accessed directly by its name.

Returns the [EditorInterface](class_editorinterface.md#class-editorinterface) singleton instance.

---

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_export_as_menu**()

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) under **Scene > Export As...**.

---

[String](class_string.md#class-string) **get_plugin_version**()

Provide the version of the plugin declared in the `plugin.cfg` config file.

---

[ScriptCreateDialog](class_scriptcreatedialog.md#class-scriptcreatedialog) **get_script_create_dialog**()

Gets the Editor's dialog used for making scripts.

**Note:** Users can configure it before use.

**Warning:** Removing and freeing this node will render a part of the editor useless and may cause a crash.

---

[EditorUndoRedoManager](class_editorundoredomanager.md#class-editorundoredomanager) **get_undo_redo**()

Gets the undo/redo object. Most actions in the editor can be undoable, so use this object to make sure this happens when it's worth it.

---

 **hide_bottom_panel**()

Minimizes the bottom panel.

---

 **make_bottom_panel_item_visible**(item: [Control](class_control.md#class-control))

Makes a specific item in the bottom panel visible.

---

 **queue_save_layout**()

Queue save the project's editor layout.

---

 **remove_autoload_singleton**(name: [String](class_string.md#class-string))

Removes an Autoload `name` from the list.

---

 **remove_context_menu_plugin**(plugin: [EditorContextMenuPlugin](class_editorcontextmenuplugin.md#class-editorcontextmenuplugin))

Removes the specified context menu plugin.

---

 **remove_control_from_bottom_panel**(control: [Control](class_control.md#class-control))

**Deprecated:** Use remove_dock() instead.

Removes the control from the bottom panel. You have to manually [Node.queue_free()](class_node.md#class-node-method-queue-free) the control.

---

 **remove_control_from_container**(container: CustomControlContainer, control: [Control](class_control.md#class-control))

Removes the control from the specified container. You have to manually [Node.queue_free()](class_node.md#class-node-method-queue-free) the control.

---

 **remove_control_from_docks**(control: [Control](class_control.md#class-control))

**Deprecated:** Use remove_dock() instead.

Removes the control from the dock. You have to manually [Node.queue_free()](class_node.md#class-node-method-queue-free) the control.

---

 **remove_custom_type**(type: [String](class_string.md#class-string))

Removes a custom type added by add_custom_type().

---

 **remove_debugger_plugin**(script: [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin))

Removes the debugger plugin with given script from the Debugger.

---

 **remove_dock**(dock: [EditorDock](class_editordock.md#class-editordock))

Removes `dock` from the available docks. You should manually call [Node.queue_free()](class_node.md#class-node-method-queue-free) to free it.

---

 **remove_export_platform**(platform: [EditorExportPlatform](class_editorexportplatform.md#class-editorexportplatform))

Removes an export platform registered by add_export_platform().

---

 **remove_export_plugin**(plugin: [EditorExportPlugin](class_editorexportplugin.md#class-editorexportplugin))

Removes an export plugin registered by add_export_plugin().

---

 **remove_import_plugin**(importer: [EditorImportPlugin](class_editorimportplugin.md#class-editorimportplugin))

Removes an import plugin registered by add_import_plugin().

---

 **remove_inspector_plugin**(plugin: [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin))

Removes an inspector plugin registered by add_inspector_plugin().

---

 **remove_node_3d_gizmo_plugin**(plugin: [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin))

Removes a gizmo plugin registered by add_node_3d_gizmo_plugin().

---

 **remove_resource_conversion_plugin**(plugin: [EditorResourceConversionPlugin](class_editorresourceconversionplugin.md#class-editorresourceconversionplugin))

Removes a resource conversion plugin registered by add_resource_conversion_plugin().

---

 **remove_scene_format_importer_plugin**(scene_format_importer: [EditorSceneFormatImporter](class_editorsceneformatimporter.md#class-editorsceneformatimporter))

Removes a scene format importer registered by add_scene_format_importer_plugin().

---

 **remove_scene_post_import_plugin**(scene_import_plugin: [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin))

Remove the [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class-editorscenepostimportplugin), added with add_scene_post_import_plugin().

---

 **remove_tool_menu_item**(name: [String](class_string.md#class-string))

Removes a menu `name` from **Project > Tools**.

---

 **remove_translation_parser_plugin**(parser: [EditorTranslationParserPlugin](class_editortranslationparserplugin.md#class-editortranslationparserplugin))

Removes a custom translation parser plugin registered by add_translation_parser_plugin().

---

 **remove_undo_redo_inspector_hook_callback**(callable: [Callable](class_callable.md#class-callable))

Removes a callback previously added by add_undo_redo_inspector_hook_callback().

---

 **set_dock_tab_icon**(control: [Control](class_control.md#class-control), icon: [Texture2D](class_texture2d.md#class-texture2d))

**Deprecated:** Use [EditorDock.dock_icon](class_editordock.md#class-editordock-property-dock-icon) instead.

Sets the tab icon for the given control in a dock slot. Setting to `null` removes the icon.

---

 **set_force_draw_over_forwarding_enabled**()

Enables calling of \_forward_canvas_force_draw_over_viewport() for the 2D editor and \_forward_3d_force_draw_over_viewport() for the 3D editor when their viewports are updated. You need to call this method only once and it will work permanently for this plugin.

---

 **set_input_event_forwarding_always_enabled**()

Use this method if you always want to receive inputs from 3D view screen inside \_forward_3d_gui_input(). It might be especially usable if your plugin will want to use raycast in the scene.

---

[int](class_int.md#class-int) **update_overlays**()

Updates the overlays of the 2D and 3D editor viewport. Causes methods \_forward_canvas_draw_over_viewport(), \_forward_canvas_force_draw_over_viewport(), \_forward_3d_draw_over_viewport() and \_forward_3d_force_draw_over_viewport() to be called.
