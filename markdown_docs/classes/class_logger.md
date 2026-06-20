# Logger

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Custom logger to receive messages from the internal error/warning stream.

## Description

Custom logger to receive messages from the internal error/warning stream. Loggers are registered via [OS.add_logger()](class_os.md#class-os-method-add-logger).

## Tutorials

- [Logging](../tutorials/scripting/logging.md)

## Methods

|    | \_log_error(function: [String](class_string.md#class-string), file: [String](class_string.md#class-string), line: [int](class_int.md#class-int), code: [String](class_string.md#class-string), rationale: [String](class_string.md#class-string), editor_notify: [bool](class_bool.md#class-bool), error_type: [int](class_int.md#class-int), script_backtraces: [Array](class_array.md#class-array)[[ScriptBacktrace](class_scriptbacktrace.md#class-scriptbacktrace)])    |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | \_log_message(message: [String](class_string.md#class-string), error: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                   |

---

## Enumerations

enum **ErrorType**:

ErrorType **ERROR_TYPE_ERROR** = `0`

The message received is an error.

ErrorType **ERROR_TYPE_WARNING** = `1`

The message received is a warning.

ErrorType **ERROR_TYPE_SCRIPT** = `2`

The message received is a script error.

ErrorType **ERROR_TYPE_SHADER** = `3`

The message received is a shader error.

---

## Method Descriptions

 **\_log_error**(function: [String](class_string.md#class-string), file: [String](class_string.md#class-string), line: [int](class_int.md#class-int), code: [String](class_string.md#class-string), rationale: [String](class_string.md#class-string), editor_notify: [bool](class_bool.md#class-bool), error_type: [int](class_int.md#class-int), script_backtraces: [Array](class_array.md#class-array)[[ScriptBacktrace](class_scriptbacktrace.md#class-scriptbacktrace)])

Called when an error is logged. The error provides the `function`, `file`, and `line` that it originated from, as well as either the `code` that generated the error or a `rationale`.

The type of error provided by `error_type` is described in the ErrorType enumeration.

Additionally, `script_backtraces` provides backtraces for each of the script languages. These will only contain stack frames in editor builds and debug builds by default. To enable them for release builds as well, you need to enable [ProjectSettings.debug/settings/gdscript/always_track_call_stacks](class_projectsettings.md#class-projectsettings-property-debug-settings-gdscript-always-track-call-stacks).

**Warning:** This method will be called from threads other than the main thread, possibly at the same time, so you will need to have some kind of thread-safety in your implementation of it, like a [Mutex](class_mutex.md#class-mutex).

**Note:** `script_backtraces` will not contain any captured variables, due to its prohibitively high cost. To get those, you will need to capture the backtraces yourself, from within the **Logger** virtual methods, using [Engine.capture_script_backtraces()](class_engine.md#class-engine-method-capture-script-backtraces).

**Note:** Logging errors from this method using functions like [@GlobalScope.push_error()](class_@globalscope.md#class-globalscope-method-push-error) or [@GlobalScope.push_warning()](class_@globalscope.md#class-globalscope-method-push-warning) is not supported, as it could cause infinite recursion. These errors will only show up in the console output.

---

 **\_log_message**(message: [String](class_string.md#class-string), error: [bool](class_bool.md#class-bool))

Called when a message is logged. If `error` is `true`, then this message was meant to be sent to `stderr`.

**Warning:** This method will be called from threads other than the main thread, possibly at the same time, so you will need to have some kind of thread-safety in your implementation of it, like a [Mutex](class_mutex.md#class-mutex).

**Note:** Logging another message from this method using functions like [@GlobalScope.print()](class_@globalscope.md#class-globalscope-method-print) is not supported, as it could cause infinite recursion. These messages will only show up in the console output.
