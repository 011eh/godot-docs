# EngineDebugger

**Inherits:** [Object](class_object.md#class-object)

Exposes the internal debugger.

## Description

**EngineDebugger** handles the communication between the editor and the running game. It is active in the running game. Messages can be sent/received through it. It also manages the profilers.

## Methods

|                                  | clear_breakpoints()                                                                                                                                                                                     |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  | debug(can_continue: [bool](class_bool.md#class-bool) = true, is_error_breakpoint: [bool](class_bool.md#class-bool) = false)                                                                                         |
| [int](class_int.md#class-int)    | get_depth()                                                                                                                                                                                                     |
| [int](class_int.md#class-int)    | get_lines_left()                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool) | has_capture(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                         |
| [bool](class_bool.md#class-bool) | has_profiler(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                       |
|                                  | insert_breakpoint(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname))                                                                                      |
| [bool](class_bool.md#class-bool) | is_active()                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool) | is_breakpoint(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname))                                                                                              |
| [bool](class_bool.md#class-bool) | is_profiling(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                       |
| [bool](class_bool.md#class-bool) | is_skipping_breakpoints()                                                                                                                                                                         |
|                                  | line_poll()                                                                                                                                                                                                     |
|                                  | profiler_add_frame_data(name: [StringName](class_stringname.md#class-stringname), data: [Array](class_array.md#class-array))                                                                      |
|                                  | profiler_enable(name: [StringName](class_stringname.md#class-stringname), enable: [bool](class_bool.md#class-bool), arguments: [Array](class_array.md#class-array) = [])                                  |
|                                  | register_message_capture(name: [StringName](class_stringname.md#class-stringname), callable: [Callable](class_callable.md#class-callable))                                                       |
|                                  | register_profiler(name: [StringName](class_stringname.md#class-stringname), profiler: [EngineProfiler](class_engineprofiler.md#class-engineprofiler))                                                   |
|                                  | remove_breakpoint(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname))                                                                                      |
|                                  | script_debug(language: [ScriptLanguage](class_scriptlanguage.md#class-scriptlanguage), can_continue: [bool](class_bool.md#class-bool) = true, is_error_breakpoint: [bool](class_bool.md#class-bool) = false) |
|                                  | send_message(message: [String](class_string.md#class-string), data: [Array](class_array.md#class-array))                                                                                                     |
|                                  | set_depth(depth: [int](class_int.md#class-int))                                                                                                                                                                 |
|                                  | set_lines_left(lines: [int](class_int.md#class-int))                                                                                                                                                       |
|                                  | unregister_message_capture(name: [StringName](class_stringname.md#class-stringname))                                                                                                           |
|                                  | unregister_profiler(name: [StringName](class_stringname.md#class-stringname))                                                                                                                         |

---

## Method Descriptions

 **clear_breakpoints**()

Clears all breakpoints.

---

 **debug**(can_continue: [bool](class_bool.md#class-bool) = true, is_error_breakpoint: [bool](class_bool.md#class-bool) = false)

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.

---

[int](class_int.md#class-int) **get_depth**()

**Experimental:** This method may be changed or removed in future versions.

Returns the current debug depth.

---

[int](class_int.md#class-int) **get_lines_left**()

**Experimental:** This method may be changed or removed in future versions.

Returns the number of lines that remain.

---

[bool](class_bool.md#class-bool) **has_capture**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if a capture with the given name is present otherwise `false`.

---

[bool](class_bool.md#class-bool) **has_profiler**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if a profiler with the given name is present otherwise `false`.

---

 **insert_breakpoint**(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname))

Inserts a new breakpoint with the given `source` and `line`.

---

[bool](class_bool.md#class-bool) **is_active**()

Returns `true` if the debugger is active otherwise `false`.

---

[bool](class_bool.md#class-bool) **is_breakpoint**(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname))

Returns `true` if the given `source` and `line` represent an existing breakpoint.

---

[bool](class_bool.md#class-bool) **is_profiling**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if a profiler with the given name is present and active otherwise `false`.

---

[bool](class_bool.md#class-bool) **is_skipping_breakpoints**()

Returns `true` if the debugger is skipping breakpoints otherwise `false`.

---

 **line_poll**()

Forces a processing loop of debugger events. The purpose of this method is just processing events every now and then when the script might get too busy, so that bugs like infinite loops can be caught.

---

 **profiler_add_frame_data**(name: [StringName](class_stringname.md#class-stringname), data: [Array](class_array.md#class-array))

Calls the `add` callable of the profiler with given `name` and `data`.

---

 **profiler_enable**(name: [StringName](class_stringname.md#class-stringname), enable: [bool](class_bool.md#class-bool), arguments: [Array](class_array.md#class-array) = [])

Calls the `toggle` callable of the profiler with given `name` and `arguments`. Enables/Disables the same profiler depending on `enable` argument.

---

 **register_message_capture**(name: [StringName](class_stringname.md#class-stringname), callable: [Callable](class_callable.md#class-callable))

Registers a message capture with given `name`. If `name` is "my_message" then messages starting with "my_message:" will be called with the given callable.

The callable must accept a message string and a data array as argument. The callable should return `true` if the message is recognized.

**Note:** The callable will receive the message with the prefix stripped, unlike [EditorDebuggerPlugin._capture()](class_editordebuggerplugin.md#class-editordebuggerplugin-private-method-capture). See the [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin) description for an example.

---

 **register_profiler**(name: [StringName](class_stringname.md#class-stringname), profiler: [EngineProfiler](class_engineprofiler.md#class-engineprofiler))

Registers a profiler with the given `name`. See [EngineProfiler](class_engineprofiler.md#class-engineprofiler) for more information.

---

 **remove_breakpoint**(line: [int](class_int.md#class-int), source: [StringName](class_stringname.md#class-stringname))

Removes a breakpoint with the given `source` and `line`.

---

 **script_debug**(language: [ScriptLanguage](class_scriptlanguage.md#class-scriptlanguage), can_continue: [bool](class_bool.md#class-bool) = true, is_error_breakpoint: [bool](class_bool.md#class-bool) = false)

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.

---

 **send_message**(message: [String](class_string.md#class-string), data: [Array](class_array.md#class-array))

Sends a message with given `message` and `data` array.

---

 **set_depth**(depth: [int](class_int.md#class-int))

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging depth.

---

 **set_lines_left**(lines: [int](class_int.md#class-int))

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging lines that remain.

---

 **unregister_message_capture**(name: [StringName](class_stringname.md#class-stringname))

Unregisters the message capture with given `name`.

---

 **unregister_profiler**(name: [StringName](class_stringname.md#class-stringname))

Unregisters a profiler with given `name`.
