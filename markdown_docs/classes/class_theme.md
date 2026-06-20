# Theme

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A resource used for styling/skinning [Control](class_control.md#class-control)s and [Window](class_window.md#class-window)s.

## Description

A resource used for styling/skinning [Control](class_control.md#class-control) and [Window](class_window.md#class-window) nodes. While individual controls can be styled using their local theme overrides (see [Control.add_theme_color_override()](class_control.md#class-control-method-add-theme-color-override)), theme resources allow you to store and apply the same settings across all controls sharing the same type (e.g. style all [Button](class_button.md#class-button)s the same). One theme resource can be used for the entire project, but you can also set a separate theme resource to a branch of control nodes. A theme resource assigned to a control applies to the control itself, as well as all of its direct and indirect children (as long as a chain of controls is uninterrupted).

Use [ProjectSettings.gui/theme/custom](class_projectsettings.md#class-projectsettings-property-gui-theme-custom) to set up a project-scope theme that will be available to every control in your project.

Use [Control.theme](class_control.md#class-control-property-theme) of any control node to set up a theme that will be available to that control and all of its direct and indirect children.

## Tutorials

- [GUI skinning](../tutorials/ui/gui_skinning.md)
- [Using the theme editor](../tutorials/ui/gui_using_theme_editor.md)

## Properties

| [float](class_float.md#class-float)   | default_base_scale   | `0.0`   |
|---------------------------------------|------------------------------------------------------------------|---------|
| [Font](class_font.md#class-font)      | default_font               |         |
| [int](class_int.md#class-int)         | default_font_size     | `-1`    |

## Methods

|                                                                         | add_type(theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                        |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                         | clear()                                                                                                                                                                                                                                                            |
|                                                                         | clear_color(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                        |
|                                                                         | clear_constant(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                  |
|                                                                         | clear_font(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                          |
|                                                                         | clear_font_size(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                |
|                                                                         | clear_icon(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                          |
|                                                                         | clear_stylebox(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                  |
|                                                                         | clear_theme_item(data_type: DataType, name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                 |
|                                                                         | clear_type_variation(theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                |
| [Color](class_color.md#class-color)                                     | get_color(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                            |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_color_list(theme_type: [String](class_string.md#class-string))                                                                                                                                                                                        |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_color_type_list()                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                           | get_constant(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                      |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_constant_list(theme_type: [String](class_string.md#class-string))                                                                                                                                                                                  |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_constant_type_list()                                                                                                                                                                                                                          |
| [Font](class_font.md#class-font)                                        | get_font(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                              |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_font_list(theme_type: [String](class_string.md#class-string))                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                           | get_font_size(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                    |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_font_size_list(theme_type: [String](class_string.md#class-string))                                                                                                                                                                                |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_font_size_type_list()                                                                                                                                                                                                                        |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_font_type_list()                                                                                                                                                                                                                                  |
| [Texture2D](class_texture2d.md#class-texture2d)                         | get_icon(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                              |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_icon_list(theme_type: [String](class_string.md#class-string))                                                                                                                                                                                          |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_icon_type_list()                                                                                                                                                                                                                                  |
| [StyleBox](class_stylebox.md#class-stylebox)                            | get_stylebox(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                      |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_stylebox_list(theme_type: [String](class_string.md#class-string))                                                                                                                                                                                  |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_stylebox_type_list()                                                                                                                                                                                                                          |
| [Variant](class_variant.md#class-variant)                               | get_theme_item(data_type: DataType, name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                     |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_theme_item_list(data_type: DataType, theme_type: [String](class_string.md#class-string))                                                                                                                                 |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_theme_item_type_list(data_type: DataType)                                                                                                                                                                           |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_type_list()                                                                                                                                                                                                                                            |
| [StringName](class_stringname.md#class-stringname)                      | get_type_variation_base(theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                                                          |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_type_variation_list(base_type: [StringName](class_stringname.md#class-stringname))                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                        | has_color(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                            |
| [bool](class_bool.md#class-bool)                                        | has_constant(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                      |
| [bool](class_bool.md#class-bool)                                        | has_default_base_scale()                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                        | has_default_font()                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                        | has_default_font_size()                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                        | has_font(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                              |
| [bool](class_bool.md#class-bool)                                        | has_font_size(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                    |
| [bool](class_bool.md#class-bool)                                        | has_icon(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                              |
| [bool](class_bool.md#class-bool)                                        | has_stylebox(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                      |
| [bool](class_bool.md#class-bool)                                        | has_theme_item(data_type: DataType, name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                     |
| [bool](class_bool.md#class-bool)                                        | is_type_variation(theme_type: [StringName](class_stringname.md#class-stringname), base_type: [StringName](class_stringname.md#class-stringname))                                                                                                       |
|                                                                         | merge_with(other: Theme)                                                                                                                                                                                                                      |
|                                                                         | remove_type(theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                  |
|                                                                         | rename_color(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                        |
|                                                                         | rename_constant(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                  |
|                                                                         | rename_font(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                          |
|                                                                         | rename_font_size(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                |
|                                                                         | rename_icon(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                          |
|                                                                         | rename_stylebox(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                  |
|                                                                         | rename_theme_item(data_type: DataType, old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname)) |
|                                                                         | rename_type(old_theme_type: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))                                                                                                              |
|                                                                         | set_color(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), color: [Color](class_color.md#class-color))                                                                                |
|                                                                         | set_constant(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), constant: [int](class_int.md#class-int))                                                                             |
|                                                                         | set_font(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), font: [Font](class_font.md#class-font))                                                                                      |
|                                                                         | set_font_size(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), font_size: [int](class_int.md#class-int))                                                                          |
|                                                                         | set_icon(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), texture: [Texture2D](class_texture2d.md#class-texture2d))                                                                    |
|                                                                         | set_stylebox(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), texture: [StyleBox](class_stylebox.md#class-stylebox))                                                               |
|                                                                         | set_theme_item(data_type: DataType, name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                   |
|                                                                         | set_type_variation(theme_type: [StringName](class_stringname.md#class-stringname), base_type: [StringName](class_stringname.md#class-stringname))                                                                                                     |

---

## Enumerations

enum **DataType**:

DataType **DATA_TYPE_COLOR** = `0`

Theme's [Color](class_color.md#class-color) item type.

DataType **DATA_TYPE_CONSTANT** = `1`

Theme's constant item type.

DataType **DATA_TYPE_FONT** = `2`

Theme's [Font](class_font.md#class-font) item type.

DataType **DATA_TYPE_FONT_SIZE** = `3`

Theme's font size item type.

DataType **DATA_TYPE_ICON** = `4`

Theme's icon [Texture2D](class_texture2d.md#class-texture2d) item type.

DataType **DATA_TYPE_STYLEBOX** = `5`

Theme's [StyleBox](class_stylebox.md#class-stylebox) item type.

DataType **DATA_TYPE_MAX** = `6`

Maximum value for the DataType enum.

---

## Property Descriptions

[float](class_float.md#class-float) **default_base_scale** = `0.0`

-  **set_default_base_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_default_base_scale**()

The default base scale factor of this theme resource. Used by some controls to scale their visual properties based on the global scale factor. If this value is set to `0.0`, the global scale factor is used (see [ThemeDB.fallback_base_scale](class_themedb.md#class-themedb-property-fallback-base-scale)).

Use has_default_base_scale() to check if this value is valid.

---

[Font](class_font.md#class-font) **default_font**

-  **set_default_font**(value: [Font](class_font.md#class-font))
- [Font](class_font.md#class-font) **get_default_font**()

The default font of this theme resource. Used as the default value when trying to fetch a font resource that doesn't exist in this theme or is in invalid state. If the default font is also missing or invalid, the engine fallback value is used (see [ThemeDB.fallback_font](class_themedb.md#class-themedb-property-fallback-font)).

Use has_default_font() to check if this value is valid.

---

[int](class_int.md#class-int) **default_font_size** = `-1`

-  **set_default_font_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_default_font_size**()

The default font size of this theme resource. Used as the default value when trying to fetch a font size value that doesn't exist in this theme or is in invalid state. If the default font size is also missing or invalid, the engine fallback value is used (see [ThemeDB.fallback_font_size](class_themedb.md#class-themedb-property-fallback-font-size)).

Values below `1` are invalid and can be used to unset the property. Use has_default_font_size() to check if this value is valid.

---

## Method Descriptions

 **add_type**(theme_type: [StringName](class_stringname.md#class-stringname))

Adds an empty theme type for every valid data type.

**Note:** Empty types are not saved with the theme. This method only exists to perform in-memory changes to the resource. Use available `set_*` methods to add theme items.

---

 **clear**()

Removes all the theme properties defined on the theme resource.

---

 **clear_color**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Removes the [Color](class_color.md#class-color) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use has_color() to check for existence.

---

 **clear_constant**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Removes the constant property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use has_constant() to check for existence.

---

 **clear_font**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Removes the [Font](class_font.md#class-font) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use has_font() to check for existence.

---

 **clear_font_size**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Removes the font size property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use has_font_size() to check for existence.

---

 **clear_icon**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Removes the icon property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use has_icon() to check for existence.

---

 **clear_stylebox**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Removes the [StyleBox](class_stylebox.md#class-stylebox) property defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use has_stylebox() to check for existence.

---

 **clear_theme_item**(data_type: DataType, name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Removes the theme property of `data_type` defined by `name` and `theme_type`, if it exists.

Fails if it doesn't exist. Use has_theme_item() to check for existence.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

 **clear_type_variation**(theme_type: [StringName](class_stringname.md#class-stringname))

Unmarks `theme_type` as being a variation of another theme type. See set_type_variation().

---

[Color](class_color.md#class-color) **get_color**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns the [Color](class_color.md#class-color) property defined by `name` and `theme_type`, if it exists.

Returns the default color value if the property doesn't exist. Use has_color() to check for existence.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_color_list**(theme_type: [String](class_string.md#class-string))

Returns a list of names for [Color](class_color.md#class-color) properties defined with `theme_type`. Use get_color_type_list() to get a list of possible theme type names.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_color_type_list**()

Returns a list of all unique theme type names for [Color](class_color.md#class-color) properties. Use get_type_list() to get a list of all unique theme types.

---

[int](class_int.md#class-int) **get_constant**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns the constant property defined by `name` and `theme_type`, if it exists.

Returns `0` if the property doesn't exist. Use has_constant() to check for existence.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_constant_list**(theme_type: [String](class_string.md#class-string))

Returns a list of names for constant properties defined with `theme_type`. Use get_constant_type_list() to get a list of possible theme type names.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_constant_type_list**()

Returns a list of all unique theme type names for constant properties. Use get_type_list() to get a list of all unique theme types.

---

[Font](class_font.md#class-font) **get_font**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns the [Font](class_font.md#class-font) property defined by `name` and `theme_type`, if it exists.

Returns the default theme font if the property doesn't exist and the default theme font is set up (see default_font). Use has_font() to check for existence of the property and has_default_font() to check for existence of the default theme font.

Returns the engine fallback font value, if neither exist (see [ThemeDB.fallback_font](class_themedb.md#class-themedb-property-fallback-font)).

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_list**(theme_type: [String](class_string.md#class-string))

Returns a list of names for [Font](class_font.md#class-font) properties defined with `theme_type`. Use get_font_type_list() to get a list of possible theme type names.

---

[int](class_int.md#class-int) **get_font_size**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns the font size property defined by `name` and `theme_type`, if it exists.

Returns the default theme font size if the property doesn't exist and the default theme font size is set up (see default_font_size). Use has_font_size() to check for existence of the property and has_default_font_size() to check for existence of the default theme font.

Returns the engine fallback font size value, if neither exist (see [ThemeDB.fallback_font_size](class_themedb.md#class-themedb-property-fallback-font-size)).

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_size_list**(theme_type: [String](class_string.md#class-string))

Returns a list of names for font size properties defined with `theme_type`. Use get_font_size_type_list() to get a list of possible theme type names.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_size_type_list**()

Returns a list of all unique theme type names for font size properties. Use get_type_list() to get a list of all unique theme types.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_font_type_list**()

Returns a list of all unique theme type names for [Font](class_font.md#class-font) properties. Use get_type_list() to get a list of all unique theme types.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_icon**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns the icon property defined by `name` and `theme_type`, if it exists.

Returns the engine fallback icon value if the property doesn't exist (see [ThemeDB.fallback_icon](class_themedb.md#class-themedb-property-fallback-icon)). Use has_icon() to check for existence.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_icon_list**(theme_type: [String](class_string.md#class-string))

Returns a list of names for icon properties defined with `theme_type`. Use get_icon_type_list() to get a list of possible theme type names.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_icon_type_list**()

Returns a list of all unique theme type names for icon properties. Use get_type_list() to get a list of all unique theme types.

---

[StyleBox](class_stylebox.md#class-stylebox) **get_stylebox**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns the [StyleBox](class_stylebox.md#class-stylebox) property defined by `name` and `theme_type`, if it exists.

Returns the engine fallback stylebox value if the property doesn't exist (see [ThemeDB.fallback_stylebox](class_themedb.md#class-themedb-property-fallback-stylebox)). Use has_stylebox() to check for existence.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_stylebox_list**(theme_type: [String](class_string.md#class-string))

Returns a list of names for [StyleBox](class_stylebox.md#class-stylebox) properties defined with `theme_type`. Use get_stylebox_type_list() to get a list of possible theme type names.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_stylebox_type_list**()

Returns a list of all unique theme type names for [StyleBox](class_stylebox.md#class-stylebox) properties. Use get_type_list() to get a list of all unique theme types.

---

[Variant](class_variant.md#class-variant) **get_theme_item**(data_type: DataType, name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns the theme property of `data_type` defined by `name` and `theme_type`, if it exists.

Returns the engine fallback value if the property doesn't exist (see [ThemeDB](class_themedb.md#class-themedb)). Use has_theme_item() to check for existence.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_theme_item_list**(data_type: DataType, theme_type: [String](class_string.md#class-string))

Returns a list of names for properties of `data_type` defined with `theme_type`. Use get_theme_item_type_list() to get a list of possible theme type names.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_theme_item_type_list**(data_type: DataType)

Returns a list of all unique theme type names for `data_type` properties. Use get_type_list() to get a list of all unique theme types.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_type_list**()

Returns a list of all unique theme type names. Use the appropriate `get_*_type_list` method to get a list of unique theme types for a single data type.

---

[StringName](class_stringname.md#class-stringname) **get_type_variation_base**(theme_type: [StringName](class_stringname.md#class-stringname))

Returns the name of the base theme type if `theme_type` is a valid variation type. Returns an empty string otherwise.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_type_variation_list**(base_type: [StringName](class_stringname.md#class-stringname))

Returns a list of all type variations for the given `base_type`.

---

[bool](class_bool.md#class-bool) **has_color**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns `true` if the [Color](class_color.md#class-color) property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use set_color() to define it.

---

[bool](class_bool.md#class-bool) **has_constant**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns `true` if the constant property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use set_constant() to define it.

---

[bool](class_bool.md#class-bool) **has_default_base_scale**()

Returns `true` if default_base_scale has a valid value.

Returns `false` if it doesn't. The value must be greater than `0.0` to be considered valid.

---

[bool](class_bool.md#class-bool) **has_default_font**()

Returns `true` if default_font has a valid value.

Returns `false` if it doesn't.

---

[bool](class_bool.md#class-bool) **has_default_font_size**()

Returns `true` if default_font_size has a valid value.

Returns `false` if it doesn't. The value must be greater than `0` to be considered valid.

---

[bool](class_bool.md#class-bool) **has_font**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns `true` if the [Font](class_font.md#class-font) property defined by `name` and `theme_type` exists, or if the default theme font is set up (see has_default_font()).

Returns `false` if neither exist. Use set_font() to define the property.

---

[bool](class_bool.md#class-bool) **has_font_size**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns `true` if the font size property defined by `name` and `theme_type` exists, or if the default theme font size is set up (see has_default_font_size()).

Returns `false` if neither exist. Use set_font_size() to define the property.

---

[bool](class_bool.md#class-bool) **has_icon**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns `true` if the icon property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use set_icon() to define it.

---

[bool](class_bool.md#class-bool) **has_stylebox**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns `true` if the [StyleBox](class_stylebox.md#class-stylebox) property defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use set_stylebox() to define it.

---

[bool](class_bool.md#class-bool) **has_theme_item**(data_type: DataType, name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Returns `true` if the theme property of `data_type` defined by `name` and `theme_type` exists.

Returns `false` if it doesn't exist. Use set_theme_item() to define it.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

[bool](class_bool.md#class-bool) **is_type_variation**(theme_type: [StringName](class_stringname.md#class-stringname), base_type: [StringName](class_stringname.md#class-stringname))

Returns `true` if `theme_type` is marked as a variation of `base_type`.

---

 **merge_with**(other: Theme)

Adds missing and overrides existing definitions with values from the `other` theme resource.

**Note:** This modifies the current theme. If you want to merge two themes together without modifying either one, create a new empty theme and merge the other two into it one after another.

---

 **remove_type**(theme_type: [StringName](class_stringname.md#class-stringname))

Removes the theme type, gracefully discarding defined theme items. If the type is a variation, this information is also erased. If the type is a base for type variations, those variations lose their base.

---

 **rename_color**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Renames the [Color](class_color.md#class-color) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use has_color() to check for existence, and clear_color() to remove the existing property.

---

 **rename_constant**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Renames the constant property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use has_constant() to check for existence, and clear_constant() to remove the existing property.

---

 **rename_font**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Renames the [Font](class_font.md#class-font) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use has_font() to check for existence, and clear_font() to remove the existing property.

---

 **rename_font_size**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Renames the font size property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use has_font_size() to check for existence, and clear_font_size() to remove the existing property.

---

 **rename_icon**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Renames the icon property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use has_icon() to check for existence, and clear_icon() to remove the existing property.

---

 **rename_stylebox**(old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Renames the [StyleBox](class_stylebox.md#class-stylebox) property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use has_stylebox() to check for existence, and clear_stylebox() to remove the existing property.

---

 **rename_theme_item**(data_type: DataType, old_name: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Renames the theme property of `data_type` defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn't exist, or if a similar property with the new name already exists. Use has_theme_item() to check for existence, and clear_theme_item() to remove the existing property.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

 **rename_type**(old_theme_type: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname))

Renames the theme type `old_theme_type` to `theme_type`, if the old type exists and the new one doesn't exist.

**Note:** Renaming a theme type to an empty name or a variation to a type associated with a built-in class removes type variation connections in a way that cannot be undone by reversing the rename alone.

---

 **set_color**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), color: [Color](class_color.md#class-color))

Creates or changes the value of the [Color](class_color.md#class-color) property defined by `name` and `theme_type`. Use clear_color() to remove the property.

---

 **set_constant**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), constant: [int](class_int.md#class-int))

Creates or changes the value of the constant property defined by `name` and `theme_type`. Use clear_constant() to remove the property.

---

 **set_font**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), font: [Font](class_font.md#class-font))

Creates or changes the value of the [Font](class_font.md#class-font) property defined by `name` and `theme_type`. Use clear_font() to remove the property.

---

 **set_font_size**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), font_size: [int](class_int.md#class-int))

Creates or changes the value of the font size property defined by `name` and `theme_type`. Use clear_font_size() to remove the property.

---

 **set_icon**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), texture: [Texture2D](class_texture2d.md#class-texture2d))

Creates or changes the value of the icon property defined by `name` and `theme_type`. Use clear_icon() to remove the property.

---

 **set_stylebox**(name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), texture: [StyleBox](class_stylebox.md#class-stylebox))

Creates or changes the value of the [StyleBox](class_stylebox.md#class-stylebox) property defined by `name` and `theme_type`. Use clear_stylebox() to remove the property.

---

 **set_theme_item**(data_type: DataType, name: [StringName](class_stringname.md#class-stringname), theme_type: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Creates or changes the value of the theme property of `data_type` defined by `name` and `theme_type`. Use clear_theme_item() to remove the property.

Fails if the `value` type is not accepted by `data_type`.

**Note:** This method is analogous to calling the corresponding data type specific method, but can be used for more generalized logic.

---

 **set_type_variation**(theme_type: [StringName](class_stringname.md#class-stringname), base_type: [StringName](class_stringname.md#class-stringname))

Marks `theme_type` as a variation of `base_type`.

This adds `theme_type` as a suggested option for [Control.theme_type_variation](class_control.md#class-control-property-theme-type-variation) on a [Control](class_control.md#class-control) that is of the `base_type` class.

Variations can also be nested, i.e. `base_type` can be another variation. If a chain of variations ends with a `base_type` matching the class of the [Control](class_control.md#class-control), the whole chain is going to be suggested as options.

**Note:** Suggestions only show up if this theme resource is set as the project default theme. See [ProjectSettings.gui/theme/custom](class_projectsettings.md#class-projectsettings-property-gui-theme-custom).
