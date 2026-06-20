# StatusIndicator

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Application status indicator (aka notification area icon).

**Note:** Status indicator is implemented on macOS and Windows.

## Properties

| [Texture2D](class_texture2d.md#class-texture2d)   | icon       |                |
|---------------------------------------------------|----------------------------------------------------|----------------|
| [NodePath](class_nodepath.md#class-nodepath)      | menu       | `NodePath("")` |
| [String](class_string.md#class-string)            | tooltip | `""`           |
| [bool](class_bool.md#class-bool)                  | visible | `true`         |

## Methods

| [Rect2](class_rect2.md#class-rect2)   | get_rect()    |
|---------------------------------------|---------------------------------------------------------|

---

## Signals

**pressed**(mouse_button: [int](class_int.md#class-int), mouse_position: [Vector2i](class_vector2i.md#class-vector2i))

Emitted when the status indicator is pressed.

---

## Property Descriptions

[Texture2D](class_texture2d.md#class-texture2d) **icon**

-  **set_icon**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_icon**()

Status indicator icon.

---

[NodePath](class_nodepath.md#class-nodepath) **menu** = `NodePath("")`

-  **set_menu**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_menu**()

Status indicator native popup menu. If this is set, the pressed signal is not emitted.

**Note:** Native popup is only supported if [NativeMenu](class_nativemenu.md#class-nativemenu) supports [NativeMenu.FEATURE_POPUP_MENU](class_nativemenu.md#class-nativemenu-constant-feature-popup-menu) feature.

---

[String](class_string.md#class-string) **tooltip** = `""`

-  **set_tooltip**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_tooltip**()

Status indicator tooltip.

---

[bool](class_bool.md#class-bool) **visible** = `true`

-  **set_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visible**()

If `true`, the status indicator is visible.

---

## Method Descriptions

[Rect2](class_rect2.md#class-rect2) **get_rect**()

Returns the status indicator rectangle in screen coordinates. If this status indicator is not visible, returns an empty [Rect2](class_rect2.md#class-rect2).
