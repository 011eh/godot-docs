# ThemeDB

**Inherits:** [Object](class_object.md#class-object)

A singleton that provides access to static information about [Theme](class_theme.md#class-theme) resources used by the engine and by your project.

## Description

This singleton provides access to static information about [Theme](class_theme.md#class-theme) resources used by the engine and by your projects. You can fetch the default engine theme, as well as your project configured theme.

**ThemeDB** also contains fallback values for theme properties.

## Properties

| [float](class_float.md#class-float)             | fallback_base_scale   | `1.0`   |
|-------------------------------------------------|----------------------------------------------------------------------|---------|
| [Font](class_font.md#class-font)                | fallback_font               |         |
| [int](class_int.md#class-int)                   | fallback_font_size     | `16`    |
| [Texture2D](class_texture2d.md#class-texture2d) | fallback_icon               |         |
| [StyleBox](class_stylebox.md#class-stylebox)    | fallback_stylebox       |         |

## Methods

| [Theme](class_theme.md#class-theme)   | get_default_theme()   |
|---------------------------------------|------------------------------------------------------------------|
| [Theme](class_theme.md#class-theme)   | get_project_theme()   |

---

## Signals

**fallback_changed**()

Emitted when one of the fallback values had been changed. Use it to refresh the look of controls that may rely on the fallback theme items.

---

## Property Descriptions

[float](class_float.md#class-float) **fallback_base_scale** = `1.0`

-  **set_fallback_base_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fallback_base_scale**()

The fallback base scale factor of every [Control](class_control.md#class-control) node and [Theme](class_theme.md#class-theme) resource. Used when no other value is available to the control.

See also [Theme.default_base_scale](class_theme.md#class-theme-property-default-base-scale).

---

[Font](class_font.md#class-font) **fallback_font**

-  **set_fallback_font**(value: [Font](class_font.md#class-font))
- [Font](class_font.md#class-font) **get_fallback_font**()

The fallback font of every [Control](class_control.md#class-control) node and [Theme](class_theme.md#class-theme) resource. Used when no other value is available to the control.

See also [Theme.default_font](class_theme.md#class-theme-property-default-font).

---

[int](class_int.md#class-int) **fallback_font_size** = `16`

-  **set_fallback_font_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fallback_font_size**()

The fallback font size of every [Control](class_control.md#class-control) node and [Theme](class_theme.md#class-theme) resource. Used when no other value is available to the control.

See also [Theme.default_font_size](class_theme.md#class-theme-property-default-font-size).

---

[Texture2D](class_texture2d.md#class-texture2d) **fallback_icon**

-  **set_fallback_icon**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_fallback_icon**()

The fallback icon of every [Control](class_control.md#class-control) node and [Theme](class_theme.md#class-theme) resource. Used when no other value is available to the control.

---

[StyleBox](class_stylebox.md#class-stylebox) **fallback_stylebox**

-  **set_fallback_stylebox**(value: [StyleBox](class_stylebox.md#class-stylebox))
- [StyleBox](class_stylebox.md#class-stylebox) **get_fallback_stylebox**()

The fallback stylebox of every [Control](class_control.md#class-control) node and [Theme](class_theme.md#class-theme) resource. Used when no other value is available to the control.

---

## Method Descriptions

[Theme](class_theme.md#class-theme) **get_default_theme**()

Returns a reference to the default engine [Theme](class_theme.md#class-theme). This theme resource is responsible for the out-of-the-box look of [Control](class_control.md#class-control) nodes and cannot be overridden.

---

[Theme](class_theme.md#class-theme) **get_project_theme**()

Returns a reference to the custom project [Theme](class_theme.md#class-theme). This theme resources allows to override the default engine theme for every control node in the project.

To set the project theme, see [ProjectSettings.gui/theme/custom](class_projectsettings.md#class-projectsettings-property-gui-theme-custom).
