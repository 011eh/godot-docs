# EngineProfiler

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for creating custom profilers.

## Description

This class can be used to implement custom profilers that are able to interact with the engine and editor debugger.

See [EngineDebugger](class_enginedebugger.md#class-enginedebugger) and [EditorDebuggerPlugin](class_editordebuggerplugin.md#class-editordebuggerplugin) for more information.

## Methods

|    | \_add_frame(data: [Array](class_array.md#class-array))                                                                                                                                                            |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | \_tick(frame_time: [float](class_float.md#class-float), process_time: [float](class_float.md#class-float), physics_time: [float](class_float.md#class-float), physics_frame_time: [float](class_float.md#class-float)) |
|    | \_toggle(enable: [bool](class_bool.md#class-bool), options: [Array](class_array.md#class-array))                                                                                                                     |

---

## Method Descriptions

 **\_add_frame**(data: [Array](class_array.md#class-array))

Called when data is added to profiler using [EngineDebugger.profiler_add_frame_data()](class_enginedebugger.md#class-enginedebugger-method-profiler-add-frame-data).

---

 **\_tick**(frame_time: [float](class_float.md#class-float), process_time: [float](class_float.md#class-float), physics_time: [float](class_float.md#class-float), physics_frame_time: [float](class_float.md#class-float))

Called once every engine iteration when the profiler is active with information about the current frame. All time values are in seconds. Lower values represent faster processing times and are therefore considered better.

---

 **\_toggle**(enable: [bool](class_bool.md#class-bool), options: [Array](class_array.md#class-array))

Called when the profiler is enabled/disabled, along with a set of `options`.
