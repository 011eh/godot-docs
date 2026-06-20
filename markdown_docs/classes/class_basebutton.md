# BaseButton

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [Button](class_button.md#class-button), [LinkButton](class_linkbutton.md#class-linkbutton), [TextureButton](class_texturebutton.md#class-texturebutton)

Abstract base class for GUI buttons.

## Description

**BaseButton** is an abstract base class for GUI buttons. It doesn't display anything by itself.

## Properties

| ActionMode                                   | action_mode                   | `1`                                                                           |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [ButtonGroup](class_buttongroup.md#class-buttongroup)                       | button_group                 |                                                                               |
| [[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] | button_mask                   | `1`                                                                           |
| [bool](class_bool.md#class-bool)                                            | button_pressed             | `false`                                                                       |
| [bool](class_bool.md#class-bool)                                            | disabled                         | `false`                                                                       |
| [FocusMode](class_control.md#enum-control-focusmode)                        | focus_mode                                                              | `2` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [bool](class_bool.md#class-bool)                                            | keep_pressed_outside | `false`                                                                       |
| [Shortcut](class_shortcut.md#class-shortcut)                                | shortcut                         |                                                                               |
| [bool](class_bool.md#class-bool)                                            | shortcut_feedback       | `true`                                                                        |
| [bool](class_bool.md#class-bool)                                            | shortcut_in_tooltip   | `true`                                                                        |
| [bool](class_bool.md#class-bool)                                            | toggle_mode                   | `false`                                                                       |

## Methods

|                                       | \_pressed()                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|
|                                       | \_toggled(toggled_on: [bool](class_bool.md#class-bool))                |
| DrawMode | get_draw_mode()                                                          |
| [bool](class_bool.md#class-bool)      | is_hovered()                                                                |
|                                       | set_pressed_no_signal(pressed: [bool](class_bool.md#class-bool)) |

---

## Signals

**button_down**()

Emitted when the button starts being held down.

---

**button_up**()

Emitted when the button stops being held down.

---

**pressed**()

Emitted when the button is toggled or pressed. This is on button_down if action_mode is ACTION_MODE_BUTTON_PRESS and on button_up otherwise.

If you need to know the button's pressed state (and toggle_mode is active), use toggled instead.

---

**toggled**(toggled_on: [bool](class_bool.md#class-bool))

Emitted when the button was just toggled between pressed and normal states (only if toggle_mode is active). The new state is contained in the `toggled_on` argument.

---

## Enumerations

enum **DrawMode**:

DrawMode **DRAW_NORMAL** = `0`

The normal state (i.e. not pressed, not hovered, not toggled and enabled) of buttons.

DrawMode **DRAW_PRESSED** = `1`

The state of buttons are pressed.

DrawMode **DRAW_HOVER** = `2`

The state of buttons are hovered.

DrawMode **DRAW_DISABLED** = `3`

The state of buttons are disabled.

DrawMode **DRAW_HOVER_PRESSED** = `4`

The state of buttons are both hovered and pressed.

---

enum **ActionMode**:

ActionMode **ACTION_MODE_BUTTON_PRESS** = `0`

Require just a press to consider the button clicked.

ActionMode **ACTION_MODE_BUTTON_RELEASE** = `1`

Require a press and a subsequent release before considering the button clicked.

---

## Property Descriptions

ActionMode **action_mode** = `1`

-  **set_action_mode**(value: ActionMode)
- ActionMode **get_action_mode**()

Determines when the button is considered clicked.

---

[ButtonGroup](class_buttongroup.md#class-buttongroup) **button_group**

-  **set_button_group**(value: [ButtonGroup](class_buttongroup.md#class-buttongroup))
- [ButtonGroup](class_buttongroup.md#class-buttongroup) **get_button_group**()

The [ButtonGroup](class_buttongroup.md#class-buttongroup) associated with the button. Not to be confused with node groups.

**Note:** The button will be configured as a radio button if a [ButtonGroup](class_buttongroup.md#class-buttongroup) is assigned to it.

---

[[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] **button_mask** = `1`

-  **set_button_mask**(value: [[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)])
- [[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] **get_button_mask**()

Binary mask to choose which mouse buttons this button will respond to.

To allow both left-click and right-click, use `MOUSE_BUTTON_MASK_LEFT | MOUSE_BUTTON_MASK_RIGHT`.

---

[bool](class_bool.md#class-bool) **button_pressed** = `false`

-  **set_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pressed**()

If `true`, the button's state is pressed. Means the button is pressed down or toggled (if toggle_mode is active). Only works if toggle_mode is `true`.

**Note:** Changing the value of button_pressed will result in toggled to be emitted. If you want to change the pressed state without emitting that signal, use set_pressed_no_signal().

---

[bool](class_bool.md#class-bool) **disabled** = `false`

-  **set_disabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_disabled**()

If `true`, the button is in disabled state and can't be clicked or toggled.

**Note:** If the button is disabled while held down, button_up will be emitted.

---

[bool](class_bool.md#class-bool) **keep_pressed_outside** = `false`

-  **set_keep_pressed_outside**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_keep_pressed_outside**()

If `true`, the button stays pressed when moving the cursor outside the button while pressing it.

**Note:** This property only affects the button's visual appearance. Signals will be emitted at the same moment regardless of this property's value.

---

[Shortcut](class_shortcut.md#class-shortcut) **shortcut**

-  **set_shortcut**(value: [Shortcut](class_shortcut.md#class-shortcut))
- [Shortcut](class_shortcut.md#class-shortcut) **get_shortcut**()

[Shortcut](class_shortcut.md#class-shortcut) associated to the button.

---

[bool](class_bool.md#class-bool) **shortcut_feedback** = `true`

-  **set_shortcut_feedback**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shortcut_feedback**()

If `true`, the button will highlight for a short amount of time when its shortcut is activated. If `false` and toggle_mode is `false`, the shortcut will activate without any visual feedback.

---

[bool](class_bool.md#class-bool) **shortcut_in_tooltip** = `true`

-  **set_shortcut_in_tooltip**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shortcut_in_tooltip_enabled**()

If `true`, the button will add information about its shortcut in the tooltip. This includes the shortcut's events and its [Resource.resource_name](class_resource.md#class-resource-property-resource-name). If both events and name are empty, the shortcut will not be included.

**Note:** This property does nothing when the tooltip control is customized using [Control._make_custom_tooltip()](class_control.md#class-control-private-method-make-custom-tooltip).

---

[bool](class_bool.md#class-bool) **toggle_mode** = `false`

-  **set_toggle_mode**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_toggle_mode**()

If `true`, the button is in toggle mode. Makes the button flip state between pressed and unpressed each time its area is clicked.

---

## Method Descriptions

 **\_pressed**()

Called when the button is pressed. If you need to know the button's pressed state (and toggle_mode is active), use \_toggled() instead.

---

 **\_toggled**(toggled_on: [bool](class_bool.md#class-bool))

Called when the button is toggled (only if toggle_mode is active).

---

DrawMode **get_draw_mode**()

Returns the visual state used to draw the button. This is useful mainly when implementing your own draw code by either overriding \_draw() or connecting to "draw" signal. The visual state of the button is defined by the DrawMode enum.

---

[bool](class_bool.md#class-bool) **is_hovered**()

Returns `true` if the mouse has entered the button and has not left it yet.

---

 **set_pressed_no_signal**(pressed: [bool](class_bool.md#class-bool))

Changes the button_pressed state of the button, without emitting toggled. Use when you just want to change the state of the button without sending the pressed event (e.g. when initializing scene). Only works if toggle_mode is `true`.

**Note:** This method doesn't unpress other buttons in button_group.
