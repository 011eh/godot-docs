# LinkButton

**Inherits:** [BaseButton](class_basebutton.md#class-basebutton) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A button that represents a link.

## Description

A button that represents a link. This type of button is primarily used for interactions that cause a context change (like linking to a web page).

See also [BaseButton](class_basebutton.md#class-basebutton) which contains common properties and methods associated with this node.

## Properties

| [String](class_string.md#class-string)                                           | ellipsis_char                                                 | `"…"`                                                                                         |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [FocusMode](class_control.md#enum-control-focusmode)                             | focus_mode                                                                                                | `3` (overrides [Control](class_control.md#class-control-property-focus-mode))                 |
| [String](class_string.md#class-string)                                           | language                                                           | `""`                                                                                          |
| [CursorShape](class_control.md#enum-control-cursorshape)                         | mouse_default_cursor_shape                                                                                | `2` (overrides [Control](class_control.md#class-control-property-mouse-default-cursor-shape)) |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) | structured_text_bidi_override                 | `0`                                                                                           |
| [Array](class_array.md#class-array)                                              | structured_text_bidi_override_options | `[]`                                                                                          |
| [String](class_string.md#class-string)                                           | text                                                                   | `""`                                                                                          |
| [TextDirection](class_control.md#enum-control-textdirection)                     | text_direction                                               | `0`                                                                                           |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior)           | text_overrun_behavior                                 | `0`                                                                                           |
| UnderlineMode                                  | underline                                                         | `0`                                                                                           |
| [String](class_string.md#class-string)                                           | uri                                                                     | `""`                                                                                          |

## Theme Properties

| [Color](class_color.md#class-color)          | font_color                             | `Color(0.875, 0.875, 0.875, 1)`   |
|----------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------|
| [Color](class_color.md#class-color)          | font_disabled_color           | `Color(0, 0, 0, 1)`               |
| [Color](class_color.md#class-color)          | font_focus_color                 | `Color(0.95, 0.95, 0.95, 1)`      |
| [Color](class_color.md#class-color)          | font_hover_color                 | `Color(0.95, 0.95, 0.95, 1)`      |
| [Color](class_color.md#class-color)          | font_hover_pressed_color | `Color(0, 0, 0, 1)`               |
| [Color](class_color.md#class-color)          | font_outline_color             | `Color(0, 0, 0, 1)`               |
| [Color](class_color.md#class-color)          | font_pressed_color             | `Color(1, 1, 1, 1)`               |
| [int](class_int.md#class-int)                | outline_size                      | `0`                               |
| [int](class_int.md#class-int)                | underline_spacing            | `2`                               |
| [Font](class_font.md#class-font)             | font                                          |                                   |
| [int](class_int.md#class-int)                | font_size                           |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | focus                                       |                                   |

---

## Enumerations

enum **UnderlineMode**:

UnderlineMode **UNDERLINE_MODE_ALWAYS** = `0`

The LinkButton will always show an underline at the bottom of its text.

UnderlineMode **UNDERLINE_MODE_ON_HOVER** = `1`

The LinkButton will show an underline at the bottom of its text when the mouse cursor is over it.

UnderlineMode **UNDERLINE_MODE_NEVER** = `2`

The LinkButton will never show an underline at the bottom of its text.

---

## Property Descriptions

[String](class_string.md#class-string) **ellipsis_char** = `"…"`

-  **set_ellipsis_char**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_ellipsis_char**()

Ellipsis character used for text clipping.

---

[String](class_string.md#class-string) **language** = `""`

-  **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

[StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **structured_text_bidi_override** = `0`

-  **set_structured_text_bidi_override**(value: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser))
- [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

---

[Array](class_array.md#class-array) **structured_text_bidi_override_options** = `[]`

-  **set_structured_text_bidi_override_options**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

---

[String](class_string.md#class-string) **text** = `""`

-  **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

The button's text that will be displayed inside the button's area.

---

[TextDirection](class_control.md#enum-control-textdirection) **text_direction** = `0`

-  **set_text_direction**(value: [TextDirection](class_control.md#enum-control-textdirection))
- [TextDirection](class_control.md#enum-control-textdirection) **get_text_direction**()

Base text writing direction.

---

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **text_overrun_behavior** = `0`

-  **set_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**()

Sets the clipping behavior when the text exceeds the node's bounding rectangle.

---

UnderlineMode **underline** = `0`

-  **set_underline_mode**(value: UnderlineMode)
- UnderlineMode **get_underline_mode**()

The underline mode to use for the text.

---

[String](class_string.md#class-string) **uri** = `""`

-  **set_uri**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_uri**()

The [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) for this **LinkButton**. If set to a valid URI, pressing the button opens the URI using the operating system's default program for the protocol (via [OS.shell_open()](class_os.md#class-os-method-shell-open)). HTTP and HTTPS URLs open the default web browser.

GDScript

```gdscript
uri = "https://godotengine.org"  # Opens the URL in the default web browser.
uri = "C:\SomeFolder"  # Opens the file explorer at the given path.
uri = "C:\SomeImage.png"  # Opens the given image in the default viewing app.
```

C#

```csharp
Uri = "https://godotengine.org"; // Opens the URL in the default web browser.
Uri = "C:\SomeFolder"; // Opens the file explorer at the given path.
Uri = "C:\SomeImage.png"; // Opens the given image in the default viewing app.
```

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **font_color** = `Color(0.875, 0.875, 0.875, 1)`

Default text [Color](class_color.md#class-color) of the **LinkButton**.

---

[Color](class_color.md#class-color) **font_disabled_color** = `Color(0, 0, 0, 1)`

Text [Color](class_color.md#class-color) used when the **LinkButton** is disabled.

---

[Color](class_color.md#class-color) **font_focus_color** = `Color(0.95, 0.95, 0.95, 1)`

Text [Color](class_color.md#class-color) used when the **LinkButton** is focused. Only replaces the normal text color of the button. Disabled, hovered, and pressed states take precedence over this color.

---

[Color](class_color.md#class-color) **font_hover_color** = `Color(0.95, 0.95, 0.95, 1)`

Text [Color](class_color.md#class-color) used when the **LinkButton** is being hovered.

---

[Color](class_color.md#class-color) **font_hover_pressed_color** = `Color(0, 0, 0, 1)`

Text [Color](class_color.md#class-color) used when the **LinkButton** is being hovered and pressed.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The tint of text outline of the **LinkButton**.

---

[Color](class_color.md#class-color) **font_pressed_color** = `Color(1, 1, 1, 1)`

Text [Color](class_color.md#class-color) used when the **LinkButton** is being pressed.

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[int](class_int.md#class-int) **underline_spacing** = `2`

The vertical space between the baseline of text and the underline.

---

[Font](class_font.md#class-font) **font**

[Font](class_font.md#class-font) of the **LinkButton**'s text.

---

[int](class_int.md#class-int) **font_size**

Font size of the **LinkButton**'s text.

---

[StyleBox](class_stylebox.md#class-stylebox) **focus**

[StyleBox](class_stylebox.md#class-stylebox) used when the **LinkButton** is focused. The focus [StyleBox](class_stylebox.md#class-stylebox) is displayed *over* the base [StyleBox](class_stylebox.md#class-stylebox), so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the base [StyleBox](class_stylebox.md#class-stylebox) remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.
