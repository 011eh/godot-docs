# EditorSpinSlider

**Inherits:** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Godot editor's control for editing numeric values.

## Description

This [Control](class_control.md#class-control) node is used in the editor's Inspector dock to allow editing of numeric values. Can be used with [EditorInspectorPlugin](class_editorinspectorplugin.md#class-editorinspectorplugin) to recreate the same behavior.

If the [Range.step](class_range.md#class-range-property-step) value is `1`, the **EditorSpinSlider** will display up/down arrows, similar to [SpinBox](class_spinbox.md#class-spinbox). If the [Range.step](class_range.md#class-range-property-step) value is not `1`, a slider will be displayed instead.

## Properties

| ControlState    | control_state           | `0`                                                                                    |
|--------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                       | deferred_drag_mode | `false`                                                                                |
| [bool](class_bool.md#class-bool)                       | editing_integer       | `false`                                                                                |
| [bool](class_bool.md#class-bool)                       | flat                             | `false`                                                                                |
| [FocusMode](class_control.md#enum-control-focusmode)   | focus_mode                                                                | `2` (overrides [Control](class_control.md#class-control-property-focus-mode))          |
| [bool](class_bool.md#class-bool)                       | hide_slider               | `false`                                                                                |
| [String](class_string.md#class-string)                 | label                           | `""`                                                                                   |
| [bool](class_bool.md#class-bool)                       | read_only                   | `false`                                                                                |
| [[SizeFlags](class_control.md#enum-control-sizeflags)] | size_flags_vertical                                                       | `1` (overrides [Control](class_control.md#class-control-property-size-flags-vertical)) |
| [float](class_float.md#class-float)                    | step                                                                      | `1.0` (overrides [Range](class_range.md#class-range-property-step))                    |
| [String](class_string.md#class-string)                 | suffix                         | `""`                                                                                   |

## Theme Properties

| [Texture2D](class_texture2d.md#class-texture2d)   | updown                   |
|---------------------------------------------------|-----------------------------------------------------------------------|
| [Texture2D](class_texture2d.md#class-texture2d)   | updown_disabled |

---

## Signals

**grabbed**()

Emitted when the spinner/slider is grabbed.

---

**ungrabbed**()

Emitted when the spinner/slider is ungrabbed.

---

**updown_pressed**()

Emitted when the updown button is pressed.

---

**value_focus_entered**()

Emitted when the value form gains focus.

---

**value_focus_exited**()

Emitted when the value form loses focus.

---

## Enumerations

enum **ControlState**:

ControlState **CONTROL_STATE_DEFAULT** = `0`

The type of control used will depend on the value of editing_integer. Up-down arrows if `true`, a slider if `false`.

ControlState **CONTROL_STATE_PREFER_SLIDER** = `1`

A slider will always be used, even if editing_integer is enabled.

ControlState **CONTROL_STATE_HIDE** = `2`

Neither the up-down arrows nor the slider will be shown.

---

## Property Descriptions

ControlState **control_state** = `0`

-  **set_control_state**(value: ControlState)
- ControlState **get_control_state**()

The state in which the control used to manipulate the value will be.

---

[bool](class_bool.md#class-bool) **deferred_drag_mode** = `false`

-  **set_deferred_drag_mode_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deferred_drag_mode_enabled**()

If `true`, changing via dragging is applied only at the end of the input (for example, when the user releases a mouse button).

---

[bool](class_bool.md#class-bool) **editing_integer** = `false`

-  **set_editing_integer**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editing_integer**()

If `true`, the **EditorSpinSlider** is considered to be editing an integer value. If `false`, the **EditorSpinSlider** is considered to be editing a floating-point value. This is used to determine whether a slider should be drawn by default. The slider is only drawn for floats; integers use up-down arrows similar to [SpinBox](class_spinbox.md#class-spinbox) instead, unless control_state is set to CONTROL_STATE_PREFER_SLIDER. It will also use [EditorSettings.interface/inspector/integer_drag_speed](class_editorsettings.md#class-editorsettings-property-interface-inspector-integer-drag-speed) instead of [EditorSettings.interface/inspector/float_drag_speed](class_editorsettings.md#class-editorsettings-property-interface-inspector-float-drag-speed) if the slider is available.

---

[bool](class_bool.md#class-bool) **flat** = `false`

-  **set_flat**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flat**()

If `true`, the slider will not draw background.

---

[bool](class_bool.md#class-bool) **hide_slider** = `false`

-  **set_hide_slider**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hiding_slider**()

**Deprecated:** Use control_state instead.

If `true`, the slider and up/down arrows are hidden.

---

[String](class_string.md#class-string) **label** = `""`

-  **set_label**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_label**()

The text that displays to the left of the value.

---

[bool](class_bool.md#class-bool) **read_only** = `false`

-  **set_read_only**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_read_only**()

If `true`, the slider can't be interacted with.

---

[String](class_string.md#class-string) **suffix** = `""`

-  **set_suffix**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_suffix**()

The suffix to display after the value (in a faded color). This should generally be a plural word. You may have to use an abbreviation if the suffix is too long to be displayed.

---

## Theme Property Descriptions

[Texture2D](class_texture2d.md#class-texture2d) **updown**

Single texture representing both the up and down buttons.

---

[Texture2D](class_texture2d.md#class-texture2d) **updown_disabled**

Single texture representing both the up and down buttons, when the control is readonly or disabled.
