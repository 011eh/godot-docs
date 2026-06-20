# AcceptDialog

**Inherits:** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [ConfirmationDialog](class_confirmationdialog.md#class-confirmationdialog)

A base dialog used for user notification.

## Description

The default use of **AcceptDialog** is to allow it to only be accepted or closed, with the same result. However, the confirmed and canceled signals allow to make the two actions different, and the add_button() method allows to add custom buttons and actions.

**Note:** **AcceptDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class-window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class-window-method-popup-centered-clamped).

## Properties

| [bool](class_bool.md#class-bool)       | dialog_autowrap               | `false`                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)       | dialog_close_on_escape | `true`                                                                                |
| [bool](class_bool.md#class-bool)       | dialog_hide_on_ok           | `true`                                                                                |
| [String](class_string.md#class-string) | dialog_text                       | `""`                                                                                  |
| [bool](class_bool.md#class-bool)       | exclusive                                                                     | `true` (overrides [Window](class_window.md#class-window-property-exclusive))          |
| [bool](class_bool.md#class-bool)       | keep_title_visible                                                            | `true` (overrides [Window](class_window.md#class-window-property-keep-title-visible)) |
| [bool](class_bool.md#class-bool)       | maximize_disabled                                                             | `true` (overrides [Window](class_window.md#class-window-property-maximize-disabled))  |
| [bool](class_bool.md#class-bool)       | minimize_disabled                                                             | `true` (overrides [Window](class_window.md#class-window-property-minimize-disabled))  |
| [String](class_string.md#class-string) | ok_button_text                 | `""`                                                                                  |
| [String](class_string.md#class-string) | title                                                                         | `"Alert!"` (overrides [Window](class_window.md#class-window-property-title))          |
| [bool](class_bool.md#class-bool)       | transient                                                                     | `true` (overrides [Window](class_window.md#class-window-property-transient))          |
| [bool](class_bool.md#class-bool)       | visible                                                                       | `false` (overrides [Window](class_window.md#class-window-property-visible))           |
| [bool](class_bool.md#class-bool)       | wrap_controls                                                                 | `true` (overrides [Window](class_window.md#class-window-property-wrap-controls))      |

## Methods

| [Button](class_button.md#class-button)   | add_button(text: [String](class_string.md#class-string), right: [bool](class_bool.md#class-bool) = false, action: [String](class_string.md#class-string) = "")   |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Button](class_button.md#class-button)   | add_cancel_button(name: [String](class_string.md#class-string))                                                                                           |
| [Label](class_label.md#class-label)      | get_label()                                                                                                                                                       |
| [Button](class_button.md#class-button)   | get_ok_button()                                                                                                                                               |
|                                          | register_text_enter(line_edit: [LineEdit](class_lineedit.md#class-lineedit))                                                                            |
|                                          | remove_button(button: [Button](class_button.md#class-button))                                                                                                 |

## Theme Properties

| [int](class_int.md#class-int)                | buttons_min_height   | `0`   |
|----------------------------------------------|-------------------------------------------------------------------------------|-------|
| [int](class_int.md#class-int)                | buttons_min_width     | `0`   |
| [int](class_int.md#class-int)                | buttons_separation   | `10`  |
| [StyleBox](class_stylebox.md#class-stylebox) | panel                                |       |

---

## Signals

**canceled**()

Emitted when the dialog is closed or the button created with add_cancel_button() is pressed.

---

**confirmed**()

Emitted when the dialog is accepted, i.e. the OK button is pressed.

---

**custom_action**(action: [StringName](class_stringname.md#class-stringname))

Emitted when a custom button with an action is pressed. See add_button().

---

## Property Descriptions

[bool](class_bool.md#class-bool) **dialog_autowrap** = `false`

-  **set_autowrap**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_autowrap**()

Sets autowrapping for the text in the dialog.

---

[bool](class_bool.md#class-bool) **dialog_close_on_escape** = `true`

-  **set_close_on_escape**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_close_on_escape**()

If `true`, the dialog will be hidden when the `ui_close_dialog` action is pressed (by default, this action is bound to `Escape`, or `Cmd + W` on macOS).

---

[bool](class_bool.md#class-bool) **dialog_hide_on_ok** = `true`

-  **set_hide_on_ok**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_hide_on_ok**()

If `true`, the dialog is hidden when the OK button is pressed. You can set it to `false` if you want to do e.g. input validation when receiving the confirmed signal, and handle hiding the dialog in your own logic.

**Note:** Some nodes derived from this class can have a different default value, and potentially their own built-in logic overriding this setting. For example [FileDialog](class_filedialog.md#class-filedialog) defaults to `false`, and has its own input validation code that is called when you press OK, which eventually hides the dialog if the input is valid. As such, this property can't be used in [FileDialog](class_filedialog.md#class-filedialog) to disable hiding the dialog when pressing OK.

---

[String](class_string.md#class-string) **dialog_text** = `""`

-  **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

The text displayed by the dialog.

---

[String](class_string.md#class-string) **ok_button_text** = `""`

-  **set_ok_button_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_ok_button_text**()

The text displayed by the OK button (see get_ok_button()). If empty, a default text will be used.

---

## Method Descriptions

[Button](class_button.md#class-button) **add_button**(text: [String](class_string.md#class-string), right: [bool](class_bool.md#class-bool) = false, action: [String](class_string.md#class-string) = "")

Adds a button with label `text` and a custom `action` to the dialog and returns the created button.

If `action` is not empty, pressing the button will emit the custom_action signal with the specified action string.

If `true`, `right` will place the button to the right of any sibling buttons.

You can use remove_button() method to remove a button created with this method from the dialog.

---

[Button](class_button.md#class-button) **add_cancel_button**(name: [String](class_string.md#class-string))

Adds a button with label `name` and a cancel action to the dialog and returns the created button.

You can use remove_button() method to remove a button created with this method from the dialog.

---

[Label](class_label.md#class-label) **get_label**()

Returns the label used for built-in text.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

[Button](class_button.md#class-button) **get_ok_button**()

Returns the OK [Button](class_button.md#class-button) instance.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

 **register_text_enter**(line_edit: [LineEdit](class_lineedit.md#class-lineedit))

Registers a [LineEdit](class_lineedit.md#class-lineedit) in the dialog. When the enter key is pressed, the dialog will be accepted.

---

 **remove_button**(button: [Button](class_button.md#class-button))

Removes the `button` from the dialog. Does NOT free the `button`. The `button` must be a [Button](class_button.md#class-button) added with add_button() or add_cancel_button() method. After removal, pressing the `button` will no longer emit this dialog's custom_action or canceled signals.

---

## Theme Property Descriptions

[int](class_int.md#class-int) **buttons_min_height** = `0`

The minimum height of each button in the bottom row (such as OK/Cancel) in pixels. This can be increased to make buttons with short texts easier to click/tap.

---

[int](class_int.md#class-int) **buttons_min_width** = `0`

The minimum width of each button in the bottom row (such as OK/Cancel) in pixels. This can be increased to make buttons with short texts easier to click/tap.

---

[int](class_int.md#class-int) **buttons_separation** = `10`

The size of the vertical space between the dialog's content and the button row.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

The panel that fills the background of the window.
