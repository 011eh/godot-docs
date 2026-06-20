# OpenXRDpadBindingModifier

**Inherits:** [OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class-openxripbindingmodifier) **<** [OpenXRBindingModifier](class_openxrbindingmodifier.md#class-openxrbindingmodifier) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

The DPad binding modifier converts an axis input to a dpad output.

## Description

The DPad binding modifier converts an axis input to a dpad output, emulating a DPad. New input paths for each dpad direction will be added to the interaction profile. When bound to actions the DPad emulation will be activated. You should **not** combine dpad inputs with normal inputs in the same action set for the same control, this will result in an error being returned when suggested bindings are submitted to OpenXR.

See [XR_EXT_dpad_binding](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_dpad_binding) for in-depth details.

**Note:** If the DPad binding modifier extension is enabled, all dpad binding paths will be available in the action map. Adding the modifier to an interaction profile allows you to further customize the behavior.

## Properties

| [OpenXRActionSet](class_openxractionset.md#class-openxractionset)    | action_set                 |             |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------|-------------|
| [float](class_float.md#class-float)                                  | center_region           | `0.1`       |
| [String](class_string.md#class-string)                               | input_path                 | `""`        |
| [bool](class_bool.md#class-bool)                                     | is_sticky                   | `false`     |
| [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) | off_haptic                 |             |
| [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) | on_haptic                   |             |
| [float](class_float.md#class-float)                                  | threshold                   | `0.6`       |
| [float](class_float.md#class-float)                                  | threshold_released | `0.4`       |
| [float](class_float.md#class-float)                                  | wedge_angle               | `1.5707964` |

---

## Property Descriptions

[OpenXRActionSet](class_openxractionset.md#class-openxractionset) **action_set**

-  **set_action_set**(value: [OpenXRActionSet](class_openxractionset.md#class-openxractionset))
- [OpenXRActionSet](class_openxractionset.md#class-openxractionset) **get_action_set**()

Action set for which this dpad binding modifier is active.

---

[float](class_float.md#class-float) **center_region** = `0.1`

-  **set_center_region**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_center_region**()

Center region in which our center position of our dpad return `true`.

---

[String](class_string.md#class-string) **input_path** = `""`

-  **set_input_path**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_input_path**()

Input path for this dpad binding modifier.

---

[bool](class_bool.md#class-bool) **is_sticky** = `false`

-  **set_is_sticky**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_is_sticky**()

If `false`, when the joystick enters a new dpad zone this becomes `true`.

If `true`, when the joystick remains in active dpad zone, this remains `true` even if we overlap with another zone.

---

[OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **off_haptic**

-  **set_off_haptic**(value: [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase))
- [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **get_off_haptic**()

Haptic pulse to emit when the user releases the input.

---

[OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **on_haptic**

-  **set_on_haptic**(value: [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase))
- [OpenXRHapticBase](class_openxrhapticbase.md#class-openxrhapticbase) **get_on_haptic**()

Haptic pulse to emit when the user presses the input.

---

[float](class_float.md#class-float) **threshold** = `0.6`

-  **set_threshold**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_threshold**()

When our input value is equal or larger than this value, our dpad in that direction becomes `true`. It stays `true` until it falls under the threshold_released value.

---

[float](class_float.md#class-float) **threshold_released** = `0.4`

-  **set_threshold_released**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_threshold_released**()

When our input value falls below this, our output becomes `false`.

---

[float](class_float.md#class-float) **wedge_angle** = `1.5707964`

-  **set_wedge_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_wedge_angle**()

The angle of each wedge that identifies the 4 directions of the emulated dpad.
