# MenuBar

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A horizontal menu bar that creates a menu for each [PopupMenu](class_popupmenu.md#class-popupmenu) child.

## Description

A horizontal menu bar that creates a menu for each [PopupMenu](class_popupmenu.md#class-popupmenu) child. New items are created by adding [PopupMenu](class_popupmenu.md#class-popupmenu)s to this node. Item title is determined by [Window.title](class_window.md#class-window-property-title), or node name if [Window.title](class_window.md#class-window-property-title) is empty. Item title can be overridden using set_menu_title().

## Properties

| [bool](class_bool.md#class-bool)                             | flat                             | `false`                                                                       |
|--------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [FocusMode](class_control.md#enum-control-focusmode)         | focus_mode                                                       | `3` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [String](class_string.md#class-string)                       | language                     | `""`                                                                          |
| [bool](class_bool.md#class-bool)                             | prefer_global_menu | `true`                                                                        |
| [int](class_int.md#class-int)                                | start_index               | `-1`                                                                          |
| [bool](class_bool.md#class-bool)                             | switch_on_hover       | `true`                                                                        |
| [TextDirection](class_control.md#enum-control-textdirection) | text_direction         | `0`                                                                           |

## Methods

| [int](class_int.md#class-int)                   | get_menu_count()                                                                                         |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [PopupMenu](class_popupmenu.md#class-popupmenu) | get_menu_popup(menu: [int](class_int.md#class-int))                                                      |
| [String](class_string.md#class-string)          | get_menu_title(menu: [int](class_int.md#class-int))                                                      |
| [String](class_string.md#class-string)          | get_menu_tooltip(menu: [int](class_int.md#class-int))                                                  |
| [bool](class_bool.md#class-bool)                | is_menu_disabled(menu: [int](class_int.md#class-int))                                                  |
| [bool](class_bool.md#class-bool)                | is_menu_hidden(menu: [int](class_int.md#class-int))                                                      |
| [bool](class_bool.md#class-bool)                | is_native_menu()                                                                                         |
|                                                 | set_disable_shortcuts(disabled: [bool](class_bool.md#class-bool))                                 |
|                                                 | set_menu_disabled(menu: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))    |
|                                                 | set_menu_hidden(menu: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))          |
|                                                 | set_menu_title(menu: [int](class_int.md#class-int), title: [String](class_string.md#class-string))       |
|                                                 | set_menu_tooltip(menu: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string)) |

## Theme Properties

| [Color](class_color.md#class-color)          | font_color                             | `Color(0.875, 0.875, 0.875, 1)`   |
|----------------------------------------------|---------------------------------------------------------------------------------|-----------------------------------|
| [Color](class_color.md#class-color)          | font_disabled_color           | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class-color)          | font_focus_color                 | `Color(0.95, 0.95, 0.95, 1)`      |
| [Color](class_color.md#class-color)          | font_hover_color                 | `Color(0.95, 0.95, 0.95, 1)`      |
| [Color](class_color.md#class-color)          | font_hover_pressed_color | `Color(1, 1, 1, 1)`               |
| [Color](class_color.md#class-color)          | font_outline_color             | `Color(0, 0, 0, 1)`               |
| [Color](class_color.md#class-color)          | font_pressed_color             | `Color(1, 1, 1, 1)`               |
| [int](class_int.md#class-int)                | h_separation                      | `4`                               |
| [int](class_int.md#class-int)                | outline_size                      | `0`                               |
| [Font](class_font.md#class-font)             | font                                          |                                   |
| [int](class_int.md#class-int)                | font_size                           |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | disabled                                 |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | disabled_mirrored               |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | hover                                       |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | hover_mirrored                     |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | hover_pressed                       |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | hover_pressed_mirrored     |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | normal                                     |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | normal_mirrored                   |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | pressed                                   |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | pressed_mirrored                 |                                   |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **flat** = `false`

-  **set_flat**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flat**()

Flat **MenuBar** don't display item decoration.

---

[String](class_string.md#class-string) **language** = `""`

-  **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

[bool](class_bool.md#class-bool) **prefer_global_menu** = `true`

-  **set_prefer_global_menu**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_prefer_global_menu**()

If `true`, **MenuBar** will use system global menu when supported.

**Note:** If `true` and global menu is supported, this node is not displayed, has zero size, and all its child nodes except [PopupMenu](class_popupmenu.md#class-popupmenu)s are inaccessible.

**Note:** This property overrides the value of the [PopupMenu.prefer_native_menu](class_popupmenu.md#class-popupmenu-property-prefer-native-menu) property of the child nodes.

---

[int](class_int.md#class-int) **start_index** = `-1`

-  **set_start_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_start_index**()

Position order in the global menu to insert **MenuBar** items at. All menu items in the **MenuBar** are always inserted as a continuous range. Menus with lower start_index are inserted first. Menus with start_index equal to `-1` are inserted last.

---

[bool](class_bool.md#class-bool) **switch_on_hover** = `true`

-  **set_switch_on_hover**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_switch_on_hover**()

If `true`, when the cursor hovers above menu item, it will close the current [PopupMenu](class_popupmenu.md#class-popupmenu) and open the other one.

---

[TextDirection](class_control.md#enum-control-textdirection) **text_direction** = `0`

-  **set_text_direction**(value: [TextDirection](class_control.md#enum-control-textdirection))
- [TextDirection](class_control.md#enum-control-textdirection) **get_text_direction**()

Base text writing direction.

---

## Method Descriptions

[int](class_int.md#class-int) **get_menu_count**()

Returns number of menu items.

---

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_menu_popup**(menu: [int](class_int.md#class-int))

Returns [PopupMenu](class_popupmenu.md#class-popupmenu) associated with menu item.

---

[String](class_string.md#class-string) **get_menu_title**(menu: [int](class_int.md#class-int))

Returns menu item title.

---

[String](class_string.md#class-string) **get_menu_tooltip**(menu: [int](class_int.md#class-int))

Returns menu item tooltip.

---

[bool](class_bool.md#class-bool) **is_menu_disabled**(menu: [int](class_int.md#class-int))

Returns `true` if the menu item is disabled.

---

[bool](class_bool.md#class-bool) **is_menu_hidden**(menu: [int](class_int.md#class-int))

Returns `true` if the menu item is hidden.

---

[bool](class_bool.md#class-bool) **is_native_menu**()

Returns `true` if the current system's global menu is supported and used by this **MenuBar**.

---

 **set_disable_shortcuts**(disabled: [bool](class_bool.md#class-bool))

If `true`, shortcuts are disabled and cannot be used to trigger the button.

---

 **set_menu_disabled**(menu: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

If `true`, menu item is disabled.

---

 **set_menu_hidden**(menu: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))

If `true`, menu item is hidden.

---

 **set_menu_title**(menu: [int](class_int.md#class-int), title: [String](class_string.md#class-string))

Sets menu item title.

---

 **set_menu_tooltip**(menu: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets menu item tooltip.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **font_color** = `Color(0.875, 0.875, 0.875, 1)`

Default text [Color](class_color.md#class-color) of the menu item.

---

[Color](class_color.md#class-color) **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)`

Text [Color](class_color.md#class-color) used when the menu item is disabled.

---

[Color](class_color.md#class-color) **font_focus_color** = `Color(0.95, 0.95, 0.95, 1)`

Text [Color](class_color.md#class-color) used when the menu item is focused. Only replaces the normal text color of the menu item. Disabled, hovered, and pressed states take precedence over this color.

---

[Color](class_color.md#class-color) **font_hover_color** = `Color(0.95, 0.95, 0.95, 1)`

Text [Color](class_color.md#class-color) used when the menu item is being hovered.

---

[Color](class_color.md#class-color) **font_hover_pressed_color** = `Color(1, 1, 1, 1)`

Text [Color](class_color.md#class-color) used when the menu item is being hovered and pressed.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The tint of text outline of the menu item.

---

[Color](class_color.md#class-color) **font_pressed_color** = `Color(1, 1, 1, 1)`

Text [Color](class_color.md#class-color) used when the menu item is being pressed.

---

[int](class_int.md#class-int) **h_separation** = `4`

The horizontal space between menu items.

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[Font](class_font.md#class-font) **font**

[Font](class_font.md#class-font) of the menu item's text.

---

[int](class_int.md#class-int) **font_size**

Font size of the menu item's text.

---

[StyleBox](class_stylebox.md#class-stylebox) **disabled**

[StyleBox](class_stylebox.md#class-stylebox) used when the menu item is disabled.

---

[StyleBox](class_stylebox.md#class-stylebox) **disabled_mirrored**

[StyleBox](class_stylebox.md#class-stylebox) used when the menu item is disabled (for right-to-left layouts).

---

[StyleBox](class_stylebox.md#class-stylebox) **hover**

[StyleBox](class_stylebox.md#class-stylebox) used when the menu item is being hovered.

---

[StyleBox](class_stylebox.md#class-stylebox) **hover_mirrored**

[StyleBox](class_stylebox.md#class-stylebox) used when the menu item is being hovered (for right-to-left layouts).

---

[StyleBox](class_stylebox.md#class-stylebox) **hover_pressed**

[StyleBox](class_stylebox.md#class-stylebox) used when the menu item is being pressed and hovered at the same time.

---

[StyleBox](class_stylebox.md#class-stylebox) **hover_pressed_mirrored**

[StyleBox](class_stylebox.md#class-stylebox) used when the menu item is being pressed and hovered at the same time (for right-to-left layouts).

---

[StyleBox](class_stylebox.md#class-stylebox) **normal**

Default [StyleBox](class_stylebox.md#class-stylebox) for the menu item.

---

[StyleBox](class_stylebox.md#class-stylebox) **normal_mirrored**

Default [StyleBox](class_stylebox.md#class-stylebox) for the menu item (for right-to-left layouts).

---

[StyleBox](class_stylebox.md#class-stylebox) **pressed**

[StyleBox](class_stylebox.md#class-stylebox) used when the menu item is being pressed.

---

[StyleBox](class_stylebox.md#class-stylebox) **pressed_mirrored**

[StyleBox](class_stylebox.md#class-stylebox) used when the menu item is being pressed (for right-to-left layouts).
