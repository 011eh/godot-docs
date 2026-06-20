# EditorDebuggerSession

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A class to interact with the editor debugger.

## Description

This class cannot be directly instantiated and must be retrieved via an [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin).

You can add tabs to the session UI via add_session_tab(), send messages via send_message(), and toggle [EngineProfiler](class_engineprofiler.md#class-engineprofiler)s via toggle_profiler().

## Methods

|                                  | add_session_tab(control: [Control](class_control.md#class-control))                                                                                         |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool) | is_active()                                                                                                                                                       |
| [bool](class_bool.md#class-bool) | is_breaked()                                                                                                                                                     |
| [bool](class_bool.md#class-bool) | is_debuggable()                                                                                                                                               |
|                                  | remove_session_tab(control: [Control](class_control.md#class-control))                                                                                   |
|                                  | send_message(message: [String](class_string.md#class-string), data: [Array](class_array.md#class-array) = [])                                                  |
|                                  | set_breakpoint(path: [String](class_string.md#class-string), line: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                 |
|                                  | toggle_profiler(profiler: [String](class_string.md#class-string), enable: [bool](class_bool.md#class-bool), data: [Array](class_array.md#class-array) = []) |

---

## Signals

**breaked**(can_debug: [bool](class_bool.md#class-bool))

Emitted when the attached remote instance enters a break state. If `can_debug` is `true`, the remote instance will enter the debug loop.

---

**continued**()

Emitted when the attached remote instance exits a break state.

---

**started**()

Emitted when a remote instance is attached to this session (i.e. the session becomes active).

---

**stopped**()

Emitted when a remote instance is detached from this session (i.e. the session becomes inactive).

---

## Method Descriptions

 **add_session_tab**(control: [Control](class_control.md#class-control))

Adds the given `control` to the debug session UI in the debugger bottom panel. The `control`'s node name will be used as the tab title.

---

[bool](class_bool.md#class-bool) **is_active**()

Returns `true` if the debug session is currently attached to a remote instance.

---

[bool](class_bool.md#class-bool) **is_breaked**()

Returns `true` if the attached remote instance is currently in the debug loop.

---

[bool](class_bool.md#class-bool) **is_debuggable**()

Returns `true` if the attached remote instance can be debugged.

---

 **remove_session_tab**(control: [Control](class_control.md#class-control))

Removes the given `control` from the debug session UI in the debugger bottom panel.

---

 **send_message**(message: [String](class_string.md#class-string), data: [Array](class_array.md#class-array) = [])

Sends the given `message` to the attached remote instance, optionally passing additionally `data`. See [EngineDebugger](class_enginedebugger.md#class-enginedebugger) for how to retrieve those messages.

---

 **set_breakpoint**(path: [String](class_string.md#class-string), line: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

Enables or disables a specific breakpoint based on `enabled`, updating the Editor Breakpoint Panel accordingly.

---

 **toggle_profiler**(profiler: [String](class_string.md#class-string), enable: [bool](class_bool.md#class-bool), data: [Array](class_array.md#class-array) = [])

Toggle the given `profiler` on the attached remote instance, optionally passing additionally `data`. See [EngineProfiler](class_engineprofiler.md#class-engineprofiler) for more details.
