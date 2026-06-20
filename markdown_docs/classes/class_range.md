# Range

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorSpinSlider](class_editorspinslider.md#class-editorspinslider), [ProgressBar](class_progressbar.md#class-progressbar), [ScrollBar](class_scrollbar.md#class-scrollbar), [Slider](class_slider.md#class-slider), [SpinBox](class_spinbox.md#class-spinbox), [TextureProgressBar](class_textureprogressbar.md#class-textureprogressbar)

Abstract base class for controls that represent a number within a range.

## Description

Range is an abstract base class for controls that represent a number within a range, using a configured step and page size. See e.g. [ScrollBar](class_scrollbar.md#class-scrollbar) and [Slider](class_slider.md#class-slider) for examples of higher-level nodes using Range.

## Properties

| [bool](class_bool.md#class-bool)                       | allow_greater   | `false`                                                                                |
|--------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                       | allow_lesser     | `false`                                                                                |
| [bool](class_bool.md#class-bool)                       | exp_edit             | `false`                                                                                |
| [float](class_float.md#class-float)                    | max_value           | `100.0`                                                                                |
| [float](class_float.md#class-float)                    | min_value           | `0.0`                                                                                  |
| [float](class_float.md#class-float)                    | page                     | `0.0`                                                                                  |
| [float](class_float.md#class-float)                    | ratio                   |                                                                                        |
| [bool](class_bool.md#class-bool)                       | rounded               | `false`                                                                                |
| [[SizeFlags](class_control.md#enum-control-sizeflags)] | size_flags_vertical                                    | `0` (overrides [Control](class_control.md#class-control-property-size-flags-vertical)) |
| [float](class_float.md#class-float)                    | step                     | `0.01`                                                                                 |
| [float](class_float.md#class-float)                    | value                   | `0.0`                                                                                  |

## Methods

|    | \_value_changed(new_value: [float](class_float.md#class-float))    |
|----|-----------------------------------------------------------------------------------------------------------------|
|    | set_value_no_signal(value: [float](class_float.md#class-float))      |
|    | share(with: [Node](class_node.md#class-node))                                      |
|    | unshare()                                                                        |

---

## Signals

**changed**()

Emitted when min_value, max_value, page, or step change.

---

**value_changed**(value: [float](class_float.md#class-float))

Emitted when value changes. When used on a [Slider](class_slider.md#class-slider), this is called continuously while dragging (potentially every frame). If you are performing an expensive operation in a function connected to value_changed, consider using a *debouncing* [Timer](class_timer.md#class-timer) to call the function less often.

**Note:** Unlike signals such as [LineEdit.text_changed](class_lineedit.md#class-lineedit-signal-text-changed), value_changed is also emitted when `value` is set directly via code.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **allow_greater** = `false`

-  **set_allow_greater**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_greater_allowed**()

If `true`, value may be greater than max_value.

---

[bool](class_bool.md#class-bool) **allow_lesser** = `false`

-  **set_allow_lesser**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_lesser_allowed**()

If `true`, value may be less than min_value.

---

[bool](class_bool.md#class-bool) **exp_edit** = `false`

-  **set_exp_ratio**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_ratio_exp**()

If `true`, and min_value is greater or equal to `0`, value will be represented exponentially rather than linearly.

---

[float](class_float.md#class-float) **max_value** = `100.0`

-  **set_max**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_max**()

Maximum value. Range is clamped if value is greater than max_value.

---

[float](class_float.md#class-float) **min_value** = `0.0`

-  **set_min**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_min**()

Minimum value. Range is clamped if value is less than min_value.

---

[float](class_float.md#class-float) **page** = `0.0`

-  **set_page**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_page**()

Page size. Used mainly for [ScrollBar](class_scrollbar.md#class-scrollbar). A [ScrollBar](class_scrollbar.md#class-scrollbar)'s grabber length is the [ScrollBar](class_scrollbar.md#class-scrollbar)'s size multiplied by page over the difference between min_value and max_value.

---

[float](class_float.md#class-float) **ratio**

-  **set_as_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_as_ratio**()

The value mapped between 0 and 1.

---

[bool](class_bool.md#class-bool) **rounded** = `false`

-  **set_use_rounded_values**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_rounded_values**()

If `true`, value will always be rounded to the nearest integer.

---

[float](class_float.md#class-float) **step** = `0.01`

-  **set_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_step**()

If greater than `0.0`, value will always be rounded to a multiple of this property's value above min_value. For example, if min_value is `0.1` and step is `0.2`, then value is limited to `0.1`, `0.3`, `0.5`, and so on. If rounded is also `true`, value will first be rounded to a multiple of this property's value, then rounded to the nearest integer.

---

[float](class_float.md#class-float) **value** = `0.0`

-  **set_value**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_value**()

Range's current value. Changing this property (even via code) will trigger value_changed signal. Use set_value_no_signal() if you want to avoid it.

---

## Method Descriptions

 **\_value_changed**(new_value: [float](class_float.md#class-float))

Called when the **Range**'s value is changed (following the same conditions as value_changed).

---

 **set_value_no_signal**(value: [float](class_float.md#class-float))

Sets the **Range**'s current value to the specified `value`, without emitting the value_changed signal.

---

 **share**(with: [Node](class_node.md#class-node))

Binds two **Range**s together along with any ranges previously grouped with either of them. When any of range's member variables change, it will share the new value with all other ranges in its group.

---

 **unshare**()

Stops the **Range** from sharing its member variables with any other.
