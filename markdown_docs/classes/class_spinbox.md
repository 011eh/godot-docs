# SpinBox

**Inherits:** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

An input field for numbers.

## Description

**SpinBox** is a numerical input text field. It allows entering integers and floating-point numbers. The **SpinBox** also has up and down buttons that can be clicked to increase or decrease the value. The value can also be changed by dragging the mouse up or down over the **SpinBox**'s arrows.

Additionally, mathematical expressions can be entered. These are evaluated when the user presses `Enter` while editing the **SpinBox**'s text field. This uses the [Expression](class_expression.md#class-expression) class to parse and evaluate the expression. The result of the expression is then set as the value of the **SpinBox**. Some examples of valid expressions are `5 + 2 * 3`, `pow(2, 4)`, and `PI + sin(0.5)`. Expressions are case-sensitive.

**Example:** Create a **SpinBox**, disable its context menu and set its text alignment to right.

GDScript

```gdscript
var spin_box = SpinBox.new()
add_child(spin_box)
var line_edit = spin_box.get_line_edit()
line_edit.context_menu_enabled = false
spin_box.horizontal_alignment = LineEdit.HORIZONTAL_ALIGNMENT_RIGHT
```

C#

```csharp
var spinBox = new SpinBox();
AddChild(spinBox);
var lineEdit = spinBox.GetLineEdit();
lineEdit.ContextMenuEnabled = false;
spinBox.AlignHorizontal = LineEdit.HorizontalAlignEnum.Right;
```

See [Range](class_range.md#class-range) class for more options over the **SpinBox**.

**Note:** With the **SpinBox**'s context menu disabled, you can right-click the bottom half of the spinbox to set the value to its minimum, while right-clicking the top half sets the value to its maximum.

**Note:** **SpinBox** relies on an underlying [LineEdit](class_lineedit.md#class-lineedit) node. To theme a **SpinBox**'s background, add theme items for [LineEdit](class_lineedit.md#class-lineedit) and customize them. The [LineEdit](class_lineedit.md#class-lineedit) has the `SpinBoxInnerLineEdit` theme variation, so that you can give it a distinct appearance from regular [LineEdit](class_lineedit.md#class-lineedit)s.

**Note:** If you want to implement drag and drop for the underlying [LineEdit](class_lineedit.md#class-lineedit), you can use [Control.set_drag_forwarding()](class_control.md#class-control-method-set-drag-forwarding) on the node returned by get_line_edit().

## Properties

| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)   | alignment                           | `0`                                                                                    |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                    | custom_arrow_round         | `false`                                                                                |
| [float](class_float.md#class-float)                                                 | custom_arrow_step           | `0.0`                                                                                  |
| [bool](class_bool.md#class-bool)                                                    | editable                             | `true`                                                                                 |
| [String](class_string.md#class-string)                                              | prefix                                 | `""`                                                                                   |
| [bool](class_bool.md#class-bool)                                                    | select_all_on_focus       | `false`                                                                                |
| [[SizeFlags](class_control.md#enum-control-sizeflags)]                              | size_flags_vertical                                                      | `1` (overrides [Control](class_control.md#class-control-property-size-flags-vertical)) |
| [float](class_float.md#class-float)                                                 | step                                                                     | `1.0` (overrides [Range](class_range.md#class-range-property-step))                    |
| [String](class_string.md#class-string)                                              | suffix                                 | `""`                                                                                   |
| [bool](class_bool.md#class-bool)                                                    | update_on_text_changed | `false`                                                                                |

## Methods

|                                              | apply()                 |
|----------------------------------------------|--------------------------------------------------------|
| [LineEdit](class_lineedit.md#class-lineedit) | get_line_edit() |

## Theme Properties

| [Color](class_color.md#class-color)             | down_disabled_icon_modulate              | `Color(0.875, 0.875, 0.875, 0.5)`   |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------|
| [Color](class_color.md#class-color)             | down_hover_icon_modulate                    | `Color(0.95, 0.95, 0.95, 1)`        |
| [Color](class_color.md#class-color)             | down_icon_modulate                                | `Color(0.875, 0.875, 0.875, 1)`     |
| [Color](class_color.md#class-color)             | down_pressed_icon_modulate                | `Color(0.95, 0.95, 0.95, 1)`        |
| [Color](class_color.md#class-color)             | up_disabled_icon_modulate                  | `Color(0.875, 0.875, 0.875, 0.5)`   |
| [Color](class_color.md#class-color)             | up_hover_icon_modulate                        | `Color(0.95, 0.95, 0.95, 1)`        |
| [Color](class_color.md#class-color)             | up_icon_modulate                                    | `Color(0.875, 0.875, 0.875, 1)`     |
| [Color](class_color.md#class-color)             | up_pressed_icon_modulate                    | `Color(0.95, 0.95, 0.95, 1)`        |
| [int](class_int.md#class-int)                   | buttons_vertical_separation           | `0`                                 |
| [int](class_int.md#class-int)                   | buttons_width                                       | `16`                                |
| [int](class_int.md#class-int)                   | field_and_buttons_separation         | `2`                                 |
| [int](class_int.md#class-int)                   | set_min_buttons_width_from_icons | `1`                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | down                                                             |                                     |
| [Texture2D](class_texture2d.md#class-texture2d) | down_disabled                                           |                                     |
| [Texture2D](class_texture2d.md#class-texture2d) | down_hover                                                 |                                     |
| [Texture2D](class_texture2d.md#class-texture2d) | down_pressed                                             |                                     |
| [Texture2D](class_texture2d.md#class-texture2d) | up                                                                 |                                     |
| [Texture2D](class_texture2d.md#class-texture2d) | up_disabled                                               |                                     |
| [Texture2D](class_texture2d.md#class-texture2d) | up_hover                                                     |                                     |
| [Texture2D](class_texture2d.md#class-texture2d) | up_pressed                                                 |                                     |
| [Texture2D](class_texture2d.md#class-texture2d) | updown                                                         |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | down_background                                      |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | down_background_disabled                    |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | down_background_hovered                      |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | down_background_pressed                      |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | field_and_buttons_separator              |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | up_background                                          |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | up_background_disabled                        |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | up_background_hovered                          |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | up_background_pressed                          |                                     |
| [StyleBox](class_stylebox.md#class-stylebox)    | up_down_buttons_separator                  |                                     |

---

## Property Descriptions

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **alignment** = `0`

-  **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

Changes the alignment of the underlying [LineEdit](class_lineedit.md#class-lineedit).

---

[bool](class_bool.md#class-bool) **custom_arrow_round** = `false`

-  **set_custom_arrow_round**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_custom_arrow_rounding**()

If `true`, the value will be rounded to a multiple of custom_arrow_step when interacting with the arrow buttons. Otherwise, increments the value by custom_arrow_step and then rounds it according to [Range.step](class_range.md#class-range-property-step).

---

[float](class_float.md#class-float) **custom_arrow_step** = `0.0`

-  **set_custom_arrow_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_custom_arrow_step**()

If not `0`, sets the step when interacting with the arrow buttons of the **SpinBox**.

**Note:** [Range.value](class_range.md#class-range-property-value) will still be rounded to a multiple of [Range.step](class_range.md#class-range-property-step).

---

[bool](class_bool.md#class-bool) **editable** = `true`

-  **set_editable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editable**()

If `true`, the **SpinBox** will be editable. Otherwise, it will be read only.

---

[String](class_string.md#class-string) **prefix** = `""`

-  **set_prefix**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_prefix**()

Adds the specified prefix string before the numerical value of the **SpinBox**.

---

[bool](class_bool.md#class-bool) **select_all_on_focus** = `false`

-  **set_select_all_on_focus**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_select_all_on_focus**()

If `true`, the **SpinBox** will select the whole text when the [LineEdit](class_lineedit.md#class-lineedit) gains focus. Clicking the up and down arrows won't trigger this behavior.

---

[String](class_string.md#class-string) **suffix** = `""`

-  **set_suffix**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_suffix**()

Adds the specified suffix string after the numerical value of the **SpinBox**.

---

[bool](class_bool.md#class-bool) **update_on_text_changed** = `false`

-  **set_update_on_text_changed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_update_on_text_changed**()

Sets the value of the [Range](class_range.md#class-range) for this **SpinBox** when the [LineEdit](class_lineedit.md#class-lineedit) text is *changed* instead of *submitted*. See [LineEdit.text_changed](class_lineedit.md#class-lineedit-signal-text-changed) and [LineEdit.text_submitted](class_lineedit.md#class-lineedit-signal-text-submitted).

**Note:** If set to `true`, this will interfere with entering mathematical expressions in the **SpinBox**. The **SpinBox** will try to evaluate the expression as you type, which means symbols like a trailing `+` are removed immediately by the expression being evaluated.

---

## Method Descriptions

 **apply**()

Applies the current value of this **SpinBox**. This is equivalent to pressing `Enter` while editing the [LineEdit](class_lineedit.md#class-lineedit) used by the **SpinBox**. This will cause [LineEdit.text_submitted](class_lineedit.md#class-lineedit-signal-text-submitted) to be emitted and its currently contained expression to be evaluated.

---

[LineEdit](class_lineedit.md#class-lineedit) **get_line_edit**()

Returns the [LineEdit](class_lineedit.md#class-lineedit) instance from this **SpinBox**. You can use it to access properties and methods of [LineEdit](class_lineedit.md#class-lineedit).

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **down_disabled_icon_modulate** = `Color(0.875, 0.875, 0.875, 0.5)`

Down button icon modulation color, when the button is disabled.

---

[Color](class_color.md#class-color) **down_hover_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)`

Down button icon modulation color, when the button is hovered.

---

[Color](class_color.md#class-color) **down_icon_modulate** = `Color(0.875, 0.875, 0.875, 1)`

Down button icon modulation color.

---

[Color](class_color.md#class-color) **down_pressed_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)`

Down button icon modulation color, when the button is being pressed.

---

[Color](class_color.md#class-color) **up_disabled_icon_modulate** = `Color(0.875, 0.875, 0.875, 0.5)`

Up button icon modulation color, when the button is disabled.

---

[Color](class_color.md#class-color) **up_hover_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)`

Up button icon modulation color, when the button is hovered.

---

[Color](class_color.md#class-color) **up_icon_modulate** = `Color(0.875, 0.875, 0.875, 1)`

Up button icon modulation color.

---

[Color](class_color.md#class-color) **up_pressed_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)`

Up button icon modulation color, when the button is being pressed.

---

[int](class_int.md#class-int) **buttons_vertical_separation** = `0`

Vertical separation between the up and down buttons.

---

[int](class_int.md#class-int) **buttons_width** = `16`

Width of the up and down buttons. If smaller than any icon set on the buttons, the respective icon may overlap neighboring elements. If smaller than `0`, the width is automatically adjusted from the icon size.

---

[int](class_int.md#class-int) **field_and_buttons_separation** = `2`

Width of the horizontal separation between the text input field ([LineEdit](class_lineedit.md#class-lineedit)) and the buttons.

---

[int](class_int.md#class-int) **set_min_buttons_width_from_icons** = `1`

If not `0`, the minimum button width corresponds to the widest of all icons set on those buttons, even if buttons_width is smaller.

---

[Texture2D](class_texture2d.md#class-texture2d) **down**

Down button icon, displayed in the middle of the down (value-decreasing) button.

---

[Texture2D](class_texture2d.md#class-texture2d) **down_disabled**

Down button icon when the button is disabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **down_hover**

Down button icon when the button is hovered.

---

[Texture2D](class_texture2d.md#class-texture2d) **down_pressed**

Down button icon when the button is being pressed.

---

[Texture2D](class_texture2d.md#class-texture2d) **up**

Up button icon, displayed in the middle of the up (value-increasing) button.

---

[Texture2D](class_texture2d.md#class-texture2d) **up_disabled**

Up button icon when the button is disabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **up_hover**

Up button icon when the button is hovered.

---

[Texture2D](class_texture2d.md#class-texture2d) **up_pressed**

Up button icon when the button is being pressed.

---

[Texture2D](class_texture2d.md#class-texture2d) **updown**

Single texture representing both the up and down buttons icons. It is displayed in the middle of the buttons and does not change upon interaction. If a valid icon is assigned, it will replace up and down.

---

[StyleBox](class_stylebox.md#class-stylebox) **down_background**

Background style of the down button.

---

[StyleBox](class_stylebox.md#class-stylebox) **down_background_disabled**

Background style of the down button when disabled.

---

[StyleBox](class_stylebox.md#class-stylebox) **down_background_hovered**

Background style of the down button when hovered.

---

[StyleBox](class_stylebox.md#class-stylebox) **down_background_pressed**

Background style of the down button when being pressed.

---

[StyleBox](class_stylebox.md#class-stylebox) **field_and_buttons_separator**

[StyleBox](class_stylebox.md#class-stylebox) drawn in the space occupied by the separation between the input field and the buttons.

---

[StyleBox](class_stylebox.md#class-stylebox) **up_background**

Background style of the up button.

---

[StyleBox](class_stylebox.md#class-stylebox) **up_background_disabled**

Background style of the up button when disabled.

---

[StyleBox](class_stylebox.md#class-stylebox) **up_background_hovered**

Background style of the up button when hovered.

---

[StyleBox](class_stylebox.md#class-stylebox) **up_background_pressed**

Background style of the up button when being pressed.

---

[StyleBox](class_stylebox.md#class-stylebox) **up_down_buttons_separator**

[StyleBox](class_stylebox.md#class-stylebox) drawn in the space occupied by the separation between the up and down buttons.
