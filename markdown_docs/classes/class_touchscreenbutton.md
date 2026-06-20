# TouchScreenButton

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Button for touch screen devices for gameplay use.

## Description

TouchScreenButton allows you to create on-screen buttons for touch devices. It's intended for gameplay use, such as a unit you have to touch to move. Unlike [Button](class_button.md#class-button), TouchScreenButton supports multitouch out of the box. Several TouchScreenButtons can be pressed at the same time with touch input.

This node inherits from [Node2D](class_node2d.md#class-node2d). Unlike with [Control](class_control.md#class-control) nodes, you cannot set anchors on it. If you want to create menus or user interfaces, you may want to use [Button](class_button.md#class-button) nodes instead. To make button nodes react to touch events, you can enable [ProjectSettings.input_devices/pointing/emulate_mouse_from_touch](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-emulate-mouse-from-touch) in the Project Settings.

You can configure TouchScreenButton to be visible only on touch devices, helping you develop your game both for desktop and mobile devices.

## Properties

| [String](class_string.md#class-string)                   | action                   | `""`    |
|----------------------------------------------------------|----------------------------------------------------------------------|---------|
| [BitMap](class_bitmap.md#class-bitmap)                   | bitmask                 |         |
| [bool](class_bool.md#class-bool)                         | passby_press       | `false` |
| [Shape2D](class_shape2d.md#class-shape2d)                | shape                     |         |
| [bool](class_bool.md#class-bool)                         | shape_centered   | `true`  |
| [bool](class_bool.md#class-bool)                         | shape_visible     | `true`  |
| [Texture2D](class_texture2d.md#class-texture2d)          | texture_normal   |         |
| [Texture2D](class_texture2d.md#class-texture2d)          | texture_pressed |         |
| VisibilityMode | visibility_mode | `0`     |

## Methods

| [bool](class_bool.md#class-bool)   | is_pressed()    |
|------------------------------------|---------------------------------------------------------------|

---

## Signals

**pressed**()

Emitted when the button is pressed (down).

---

**released**()

Emitted when the button is released (up).

---

## Enumerations

enum **VisibilityMode**:

VisibilityMode **VISIBILITY_ALWAYS** = `0`

Always visible.

VisibilityMode **VISIBILITY_TOUCHSCREEN_ONLY** = `1`

Visible on touch screens only.

---

## Property Descriptions

[String](class_string.md#class-string) **action** = `""`

-  **set_action**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_action**()

The button's action. Actions can be handled with [InputEventAction](class_inputeventaction.md#class-inputeventaction).

---

[BitMap](class_bitmap.md#class-bitmap) **bitmask**

-  **set_bitmask**(value: [BitMap](class_bitmap.md#class-bitmap))
- [BitMap](class_bitmap.md#class-bitmap) **get_bitmask**()

The button's bitmask.

---

[bool](class_bool.md#class-bool) **passby_press** = `false`

-  **set_passby_press**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_passby_press_enabled**()

If `true`, the pressed and released signals are emitted whenever a pressed finger goes in and out of the button, even if the pressure started outside the active area of the button.

**Note:** This is a "pass-by" (not "bypass") press mode.

---

[Shape2D](class_shape2d.md#class-shape2d) **shape**

-  **set_shape**(value: [Shape2D](class_shape2d.md#class-shape2d))
- [Shape2D](class_shape2d.md#class-shape2d) **get_shape**()

The button's shape.

---

[bool](class_bool.md#class-bool) **shape_centered** = `true`

-  **set_shape_centered**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shape_centered**()

If `true`, the button's shape is centered in the provided texture. If no texture is used, this property has no effect.

---

[bool](class_bool.md#class-bool) **shape_visible** = `true`

-  **set_shape_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shape_visible**()

If `true`, the button's shape is visible in the editor.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture_normal**

-  **set_texture_normal**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_normal**()

The button's texture for the normal state.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture_pressed**

-  **set_texture_pressed**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture_pressed**()

The button's texture for the pressed state.

---

VisibilityMode **visibility_mode** = `0`

-  **set_visibility_mode**(value: VisibilityMode)
- VisibilityMode **get_visibility_mode**()

The button's visibility mode.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **is_pressed**()

Returns `true` if this button is currently pressed.
