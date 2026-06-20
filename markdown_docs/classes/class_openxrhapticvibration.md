# OpenXRHapticVibration

**Inherits:** [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Vibration haptic feedback.

## Description

This haptic feedback resource makes it possible to define a vibration based haptic feedback pulse that can be triggered through actions in the OpenXR action map.

## Properties

| [float](class_float.md#class-float)   | amplitude   | `1.0`   |
|---------------------------------------|----------------------------------------------------------------|---------|
| [int](class_int.md#class-int)         | duration     | `-1`    |
| [float](class_float.md#class-float)   | frequency   | `0.0`   |

---

## Property Descriptions

[float](class_float.md#class-float) **amplitude** = `1.0`

-  **set_amplitude**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_amplitude**()

The amplitude of the pulse between `0.0` and `1.0`.

---

[int](class_int.md#class-int) **duration** = `-1`

-  **set_duration**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_duration**()

The duration of the pulse in nanoseconds. Use `-1` for a minimum duration pulse for the current XR runtime.

---

[float](class_float.md#class-float) **frequency** = `0.0`

-  **set_frequency**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_frequency**()

The frequency of the pulse in Hz. `0.0` will let the XR runtime chose an optimal frequency for the device used.
