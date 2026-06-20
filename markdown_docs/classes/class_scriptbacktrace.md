# ScriptBacktrace

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A captured backtrace of a specific script language.

## Description

**ScriptBacktrace** holds an already captured backtrace of a specific script language, such as GDScript or C#, which are captured using [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

See [ProjectSettings.debug/settings/gdscript/always_track_call_stacks](class_projectsettings.md#class-projectsettings-property-debug-settings-gdscript-always-track-call-stacks) and [ProjectSettings.debug/settings/gdscript/always_track_local_variables](class_projectsettings.md#class-projectsettings-property-debug-settings-gdscript-always-track-local-variables) for ways of controlling the contents of this class.

## Methods

| [String](class_string.md#class-string)    | format(indent_all: [int](class_int.md#class-int) = 0, indent_frames: [int](class_int.md#class-int) = 4)                                 |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)             | get_frame_count()                                                                                                              |
| [String](class_string.md#class-string)    | get_frame_file(index: [int](class_int.md#class-int))                                                                            |
| [String](class_string.md#class-string)    | get_frame_function(index: [int](class_int.md#class-int))                                                                    |
| [int](class_int.md#class-int)             | get_frame_line(index: [int](class_int.md#class-int))                                                                            |
| [int](class_int.md#class-int)             | get_global_variable_count()                                                                                          |
| [String](class_string.md#class-string)    | get_global_variable_name(variable_index: [int](class_int.md#class-int))                                               |
| [Variant](class_variant.md#class-variant) | get_global_variable_value(variable_index: [int](class_int.md#class-int))                                             |
| [String](class_string.md#class-string)    | get_language_name()                                                                                                          |
| [int](class_int.md#class-int)             | get_local_variable_count(frame_index: [int](class_int.md#class-int))                                                  |
| [String](class_string.md#class-string)    | get_local_variable_name(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int))     |
| [Variant](class_variant.md#class-variant) | get_local_variable_value(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int))   |
| [int](class_int.md#class-int)             | get_member_variable_count(frame_index: [int](class_int.md#class-int))                                                |
| [String](class_string.md#class-string)    | get_member_variable_name(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int))   |
| [Variant](class_variant.md#class-variant) | get_member_variable_value(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int)) |
| [bool](class_bool.md#class-bool)          | is_empty()                                                                                                                            |

---

## Method Descriptions

[String](class_string.md#class-string) **format**(indent_all: [int](class_int.md#class-int) = 0, indent_frames: [int](class_int.md#class-int) = 4)

Converts the backtrace to a [String](class_string.md#class-string), where the entire string will be indented by `indent_all` number of spaces, and the individual stack frames will be additionally indented by `indent_frames` number of spaces.

**Note:** Calling [Object.to_string()](class_object.md#class-object-method-to-string) on a **ScriptBacktrace** will produce the same output as calling format() with all parameters left at their default values.

---

[int](class_int.md#class-int) **get_frame_count**()

Returns the number of stack frames in the backtrace.

---

[String](class_string.md#class-string) **get_frame_file**(index: [int](class_int.md#class-int))

Returns the file name of the call site represented by the stack frame at the specified index.

---

[String](class_string.md#class-string) **get_frame_function**(index: [int](class_int.md#class-int))

Returns the name of the function called at the stack frame at the specified index.

---

[int](class_int.md#class-int) **get_frame_line**(index: [int](class_int.md#class-int))

Returns the line number of the call site represented by the stack frame at the specified index.

---

[int](class_int.md#class-int) **get_global_variable_count**()

Returns the number of global variables (e.g. autoload singletons) in the backtrace.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

---

[String](class_string.md#class-string) **get_global_variable_name**(variable_index: [int](class_int.md#class-int))

Returns the name of the global variable at the specified index.

---

[Variant](class_variant.md#class-variant) **get_global_variable_value**(variable_index: [int](class_int.md#class-int))

Returns the value of the global variable at the specified index.

**Warning:** With GDScript backtraces, the returned [Variant](class_variant.md#class-variant) will be the variable's actual value, including any object references. This means that storing the returned [Variant](class_variant.md#class-variant) will prevent any such object from being deallocated, so it's generally recommended not to do so.

---

[String](class_string.md#class-string) **get_language_name**()

Returns the name of the script language that this backtrace was captured from.

---

[int](class_int.md#class-int) **get_local_variable_count**(frame_index: [int](class_int.md#class-int))

Returns the number of local variables in the stack frame at the specified index.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

---

[String](class_string.md#class-string) **get_local_variable_name**(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int))

Returns the name of the local variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

---

[Variant](class_variant.md#class-variant) **get_local_variable_value**(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int))

Returns the value of the local variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

**Warning:** With GDScript backtraces, the returned [Variant](class_variant.md#class-variant) will be the variable's actual value, including any object references. This means that storing the returned [Variant](class_variant.md#class-variant) will prevent any such object from being deallocated, so it's generally recommended not to do so.

---

[int](class_int.md#class-int) **get_member_variable_count**(frame_index: [int](class_int.md#class-int))

Returns the number of member variables in the stack frame at the specified index.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

---

[String](class_string.md#class-string) **get_member_variable_name**(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int))

Returns the name of the member variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

---

[Variant](class_variant.md#class-variant) **get_member_variable_value**(frame_index: [int](class_int.md#class-int), variable_index: [int](class_int.md#class-int))

Returns the value of the member variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

**Warning:** With GDScript backtraces, the returned [Variant](class_variant.md#class-variant) will be the variable's actual value, including any object references. This means that storing the returned [Variant](class_variant.md#class-variant) will prevent any such object from being deallocated, so it's generally recommended not to do so.

---

[bool](class_bool.md#class-bool) **is_empty**()

Returns `true` if the backtrace has no stack frames.
