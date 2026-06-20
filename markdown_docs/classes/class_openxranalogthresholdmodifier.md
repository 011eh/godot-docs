# OpenXRAnalogThresholdModifier

**Inherits:** [OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class-openxractionbindingmodifier) **<** [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

## Description

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

See [XR_VALVE_analog_threshold](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_VALVE_analog_threshold) for in-depth details.

## Properties

| [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase)   | off_haptic       |       |
|------------------------------------------------------------------------|------------------------------------------------------------------------------|-------|
| [float](class_float.md#class-float)                                    | off_threshold | `0.4` |
| [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase)   | on_haptic         |       |
| [float](class_float.md#class-float)                                    | on_threshold   | `0.6` |

---

## Property Descriptions

[OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **off_haptic**

-  **set_off_haptic**(value: [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase))
- [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **get_off_haptic**()

Haptic pulse to emit when the user releases the input.

---

[float](class_float.md#class-float) **off_threshold** = `0.4`

-  **set_off_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_off_threshold**()

When our input value falls below this, our output becomes `false`.

---

[OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **on_haptic**

-  **set_on_haptic**(value: [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase))
- [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **get_on_haptic**()

Haptic pulse to emit when the user presses the input.

---

[float](class_float.md#class-float) **on_threshold** = `0.6`

-  **set_on_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_on_threshold**()

When our input value is equal or larger than this value, our output becomes `true`. It stays `true` until it falls under the off_threshold value.
