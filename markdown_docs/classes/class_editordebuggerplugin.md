# EditorDebuggerPlugin

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A base class to implement debugger plugins.

## Description

**EditorDebuggerPlugin** provides functions related to the editor side of the debugger.

To interact with the debugger, an instance of this class must be added to the editor via [EditorPlugin.add_debugger_plugin()](class_editorplugin.md#class-editorplugin-method-add-debugger-plugin).

Once added, the \_setup_session() callback will be called for every [EditorDebuggerSession](class_editordebuggersession.md#class-editordebuggersession) available to the plugin, and when new ones are created (the sessions may be inactive during this stage).

You can retrieve the available [EditorDebuggerSession](class_editordebuggersession.md#class-editordebuggersession)s via get_sessions() or get a specific one via get_session().

GDScript

```gdscript
@tool
extends EditorPlugin

class ExampleEditorDebugger extends EditorDebuggerPlugin:

    func _has_capture(capture):
        # Return true if you wish to handle messages with the prefix "my_plugin:".
        return capture == "my_plugin"

    func _capture(message, data, session_id):
        if message == "my_plugin:ping":
            get_session(session_id).send_message("my_plugin:echo", data)
            return true
        return false

    func _setup_session(session_id):
        # Add a new tab in the debugger session UI containing a label.
        var label = Label.new()
        label.name = "Example plugin" # Will be used as the tab title.
        label.text = "Example plugin"
        var session = get_session(session_id)
        # Listens to the session started and stopped signals.
        session.started.connect(func (): print("Session started"))
        session.stopped.connect(func (): print("Session stopped"))
        session.add_session_tab(label)

var debugger = ExampleEditorDebugger.new()

func _enter_tree():
    add_debugger_plugin(debugger)

func _exit_tree():
    remove_debugger_plugin(debugger)
```

To connect on the running game side, use the [EngineDebugger](class_enginedebugger.md#class-enginedebugger) singleton:

GDScript

```gdscript
extends Node

func _ready():
    EngineDebugger.register_message_capture("my_plugin", _capture)
    EngineDebugger.send_message("my_plugin:ping", ["test"])

func _capture(message, data):
    # Note that the "my_plugin:" prefix is not used here.
    if message == "echo":
        prints("Echo received:", data)
        return true
    return false
```

**Note:** While the game is running, [@GlobalScope.print()](class_@globalscope.md#class-globalscope-method-print) and similar functions *called in the editor* do not print anything, the Output Log prints only game messages.

## Methods

|                                                                                     | \_breakpoint_set_in_tree(script: [Script](class_script.md#class-script), line: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))    |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                     | \_breakpoints_cleared_in_tree()                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                    | \_capture(message: [String](class_string.md#class-string), data: [Array](class_array.md#class-array), session_id: [int](class_int.md#class-int))                           |
|                                                                                     | \_goto_script_line(script: [Script](class_script.md#class-script), line: [int](class_int.md#class-int))                                                           |
| [bool](class_bool.md#class-bool)                                                    | \_has_capture(capture: [String](class_string.md#class-string))                                                                                                         |
|                                                                                     | \_setup_session(session_id: [int](class_int.md#class-int))                                                                                                           |
| [EditorDebuggerSession](class_editordebuggersession.md#class-editordebuggersession) | get_session(id: [int](class_int.md#class-int))                                                                                                                                 |
| [Array](class_array.md#class-array)                                                 | get_sessions()                                                                                                                                                                |

---

## Method Descriptions

 **\_breakpoint_set_in_tree**(script: [Script](class_script.md#class-script), line: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

Override this method to be notified when a breakpoint is set in the editor.

---

 **\_breakpoints_cleared_in_tree**()

Override this method to be notified when all breakpoints are cleared in the editor.

---

[bool](class_bool.md#class-bool) **\_capture**(message: [String](class_string.md#class-string), data: [Array](class_array.md#class-array), session_id: [int](class_int.md#class-int))

Override this method to process incoming messages. The `session_id` is the ID of the [EditorDebuggerSession](class_editordebuggersession.md#class-editordebuggersession) that received the `message`. Use get_session() to retrieve the session. This method should return `true` if the message is recognized.

---

 **\_goto_script_line**(script: [Script](class_script.md#class-script), line: [int](class_int.md#class-int))

Override this method to be notified when a breakpoint line has been clicked in the debugger breakpoint panel.

---

[bool](class_bool.md#class-bool) **\_has_capture**(capture: [String](class_string.md#class-string))

Override this method to enable receiving messages from the debugger. If `capture` is "my_message" then messages starting with "my_message:" will be passed to the \_capture() method.

---

 **\_setup_session**(session_id: [int](class_int.md#class-int))

Override this method to be notified whenever a new [EditorDebuggerSession](class_editordebuggersession.md#class-editordebuggersession) is created. Note that the session may be inactive during this stage.

---

[EditorDebuggerSession](class_editordebuggersession.md#class-editordebuggersession) **get_session**(id: [int](class_int.md#class-int))

Returns the [EditorDebuggerSession](class_editordebuggersession.md#class-editordebuggersession) with the given `id`.

---

[Array](class_array.md#class-array) **get_sessions**()

Returns an array of [EditorDebuggerSession](class_editordebuggersession.md#class-editordebuggersession) currently available to this debugger plugin.

**Note:** Sessions in the array may be inactive, check their state via [EditorDebuggerSession.is_active()](class_editordebuggersession.md#class-editordebuggersession-method-is-active).
