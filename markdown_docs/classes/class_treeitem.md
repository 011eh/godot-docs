# TreeItem

**Inherits:** [Object](class_object.md#class-object)

An internal control for a single item inside [Tree](class_tree.md#class-tree).

## Description

A single item of a [Tree](class_tree.md#class-tree) control. It can contain other **TreeItem**s as children, which allows it to create a hierarchy. It can also contain text and buttons. **TreeItem** is not a [Node](class_node.md#class-node), it is internal to the [Tree](class_tree.md#class-tree).

To create a **TreeItem**, use [Tree.create_item()](class_tree.md#class-tree-method-create-item) or create_child(). To remove a **TreeItem**, use [Object.free()](class_object.md#class-object-method-free).

**Note:** The ID values used for buttons are 32-bit, unlike [int](class_int.md#class-int) which is always 64-bit. They go from `-2147483648` to `2147483647`.

## Properties

| [bool](class_bool.md#class-bool)   | collapsed                         |
|------------------------------------|-------------------------------------------------------------------------|
| [int](class_int.md#class-int)      | custom_minimum_height |
| [bool](class_bool.md#class-bool)   | disable_folding             |
| [bool](class_bool.md#class-bool)   | visible                             |

## Methods

|                                                                                   | add_button(column: [int](class_int.md#class-int), button: [Texture2D](class_texture2d.md#class-texture2d), id: [int](class_int.md#class-int) = -1, disabled: [bool](class_bool.md#class-bool) = false, tooltip_text: [String](class_string.md#class-string) = "", description: [String](class_string.md#class-string) = "")   |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                   | add_child(child: TreeItem)                                                                                                                                                                                                                                                                                  |
|                                                                                   | call_recursive(method: [StringName](class_stringname.md#class-stringname), ...)                                                                                                                                                                                                                                           |
|                                                                                   | clear_buttons()                                                                                                                                                                                                                                                                                                            |
|                                                                                   | clear_custom_bg_color(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                       |
|                                                                                   | clear_custom_color(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                             |
| TreeItem                                                       | create_child(index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                     |
|                                                                                   | deselect(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                 |
|                                                                                   | erase_button(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))                                                                                                                                                                                                                            |
| [AutoTranslateMode](class_node.md#enum-node-autotranslatemode)                    | get_auto_translate_mode(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                   |
| [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode)                  | get_autowrap_mode(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                               |
| [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]              | get_autowrap_trim_flags(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                   |
| [Texture2D](class_texture2d.md#class-texture2d)                                   | get_button(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                     | get_button_by_id(column: [int](class_int.md#class-int), id: [int](class_int.md#class-int))                                                                                                                                                                                                                              |
| [Color](class_color.md#class-color)                                               | get_button_color(column: [int](class_int.md#class-int), id: [int](class_int.md#class-int))                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                     | get_button_count(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_button_id(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))                                                                                                                                                                                                                          |
| [String](class_string.md#class-string)                                            | get_button_tooltip_text(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))                                                                                                                                                                                                      |
| TreeCellMode                                       | get_cell_mode(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                       |
| TreeItem                                                       | get_child(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                     | get_child_count()                                                                                                                                                                                                                                                                                                        |
| [Array](class_array.md#class-array)[TreeItem]                  | get_children()                                                                                                                                                                                                                                                                                                              |
| [Color](class_color.md#class-color)                                               | get_custom_bg_color(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                           |
| [Color](class_color.md#class-color)                                               | get_custom_color(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                 |
| [Callable](class_callable.md#class-callable)                                      | get_custom_draw_callback(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                 |
| [Font](class_font.md#class-font)                                                  | get_custom_font(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                     | get_custom_font_size(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                         |
| [StyleBox](class_stylebox.md#class-stylebox)                                      | get_custom_stylebox(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                           |
| [String](class_string.md#class-string)                                            | get_description(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                  | get_expand_right(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                 |
| TreeItem                                                       | get_first_child()                                                                                                                                                                                                                                                                                                        |
| [Texture2D](class_texture2d.md#class-texture2d)                                   | get_icon(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_icon_max_width(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                             |
| [Color](class_color.md#class-color)                                               | get_icon_modulate(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                               |
| [Texture2D](class_texture2d.md#class-texture2d)                                   | get_icon_overlay(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                 |
| [Rect2](class_rect2.md#class-rect2)                                               | get_icon_region(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                     | get_index()                                                                                                                                                                                                                                                                                                                    |
| [String](class_string.md#class-string)                                            | get_language(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                         |
| [Variant](class_variant.md#class-variant)                                         | get_metadata(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                         |
| TreeItem                                                       | get_next()                                                                                                                                                                                                                                                                                                                      |
| TreeItem                                                       | get_next_in_tree(wrap: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                        |
| TreeItem                                                       | get_next_visible(wrap: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                        |
| TreeItem                                                       | get_parent()                                                                                                                                                                                                                                                                                                                  |
| TreeItem                                                       | get_prev()                                                                                                                                                                                                                                                                                                                      |
| TreeItem                                                       | get_prev_in_tree(wrap: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                        |
| TreeItem                                                       | get_prev_visible(wrap: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                               | get_range(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                               |
| [Dictionary](class_dictionary.md#class-dictionary)                                | get_range_config(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                 |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser)  | get_structured_text_bidi_override(column: [int](class_int.md#class-int))                                                                                                                                                                                                                               |
| [Array](class_array.md#class-array)                                               | get_structured_text_bidi_override_options(column: [int](class_int.md#class-int))                                                                                                                                                                                                               |
| [String](class_string.md#class-string)                                            | get_suffix(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                                            | get_text(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                 |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | get_text_alignment(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                             |
| [TextDirection](class_control.md#enum-control-textdirection)                      | get_text_direction(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                             |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior)            | get_text_overrun_behavior(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                               |
| [String](class_string.md#class-string)                                            | get_tooltip_text(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                 |
| [Tree](class_tree.md#class-tree)                                                  | get_tree()                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                  | is_accepting_children()                                                                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                  | is_any_collapsed(only_visible: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                  | is_button_disabled(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                  | is_checked(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                  | is_custom_set_as_button(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                  | is_edit_multiline(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                  | is_editable(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                  | is_indeterminate(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                  | is_selectable(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                  | is_selected(column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                  | is_visible_in_tree()                                                                                                                                                                                                                                                                                                  |
|                                                                                   | move_after(item: TreeItem)                                                                                                                                                                                                                                                                                 |
|                                                                                   | move_before(item: TreeItem)                                                                                                                                                                                                                                                                               |
|                                                                                   | propagate_check(column: [int](class_int.md#class-int), emit_signal: [bool](class_bool.md#class-bool) = true)                                                                                                                                                                                                             |
|                                                                                   | remove_child(child: TreeItem)                                                                                                                                                                                                                                                                            |
|                                                                                   | select(column: [int](class_int.md#class-int), set_as_cursor: [bool](class_bool.md#class-bool) = true)                                                                                                                                                                                                                             |
|                                                                                   | set_accept_children(allowed: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                       |
|                                                                                   | set_auto_translate_mode(column: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode))                                                                                                                                                                             |
|                                                                                   | set_autowrap_mode(column: [int](class_int.md#class-int), autowrap_mode: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode))                                                                                                                                                                              |
|                                                                                   | set_autowrap_trim_flags(column: [int](class_int.md#class-int), flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])                                                                                                                                                                      |
|                                                                                   | set_button(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), button: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                       |
|                                                                                   | set_button_color(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                                        |
|                                                                                   | set_button_description(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), description: [String](class_string.md#class-string))                                                                                                                                                   |
|                                                                                   | set_button_disabled(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                  |
|                                                                                   | set_button_tooltip_text(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                                                                                                                                     |
|                                                                                   | set_cell_mode(column: [int](class_int.md#class-int), mode: TreeCellMode)                                                                                                                                                                                                                    |
|                                                                                   | set_checked(column: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                |
|                                                                                   | set_collapsed_recursive(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                |
|                                                                                   | set_custom_as_button(column: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                               |
|                                                                                   | set_custom_bg_color(column: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), just_outline: [bool](class_bool.md#class-bool) = false)                                                                                                                                                       |
|                                                                                   | set_custom_color(column: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                     |
|                                                                                   | set_custom_draw(column: [int](class_int.md#class-int), object: [Object](class_object.md#class-object), callback: [StringName](class_stringname.md#class-stringname))                                                                                                                                                     |
|                                                                                   | set_custom_draw_callback(column: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                         |
|                                                                                   | set_custom_font(column: [int](class_int.md#class-int), font: [Font](class_font.md#class-font))                                                                                                                                                                                                                           |
|                                                                                   | set_custom_font_size(column: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int))                                                                                                                                                                                                               |
|                                                                                   | set_custom_stylebox(column: [int](class_int.md#class-int), stylebox: [StyleBox](class_stylebox.md#class-stylebox))                                                                                                                                                                                                   |
|                                                                                   | set_description(column: [int](class_int.md#class-int), description: [String](class_string.md#class-string))                                                                                                                                                                                                              |
|                                                                                   | set_edit_multiline(column: [int](class_int.md#class-int), multiline: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                |
|                                                                                   | set_editable(column: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                              |
|                                                                                   | set_expand_right(column: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                       |
|                                                                                   | set_icon(column: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                                                                       |
|                                                                                   | set_icon_max_width(column: [int](class_int.md#class-int), width: [int](class_int.md#class-int))                                                                                                                                                                                                                       |
|                                                                                   | set_icon_modulate(column: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color))                                                                                                                                                                                                                |
|                                                                                   | set_icon_overlay(column: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                                                       |
|                                                                                   | set_icon_region(column: [int](class_int.md#class-int), region: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                      |
|                                                                                   | set_indeterminate(column: [int](class_int.md#class-int), indeterminate: [bool](class_bool.md#class-bool))                                                                                                                                                                                                              |
|                                                                                   | set_language(column: [int](class_int.md#class-int), language: [String](class_string.md#class-string))                                                                                                                                                                                                                       |
|                                                                                   | set_metadata(column: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                        |
|                                                                                   | set_range(column: [int](class_int.md#class-int), value: [float](class_float.md#class-float))                                                                                                                                                                                                                                   |
|                                                                                   | set_range_config(column: [int](class_int.md#class-int), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float), step: [float](class_float.md#class-float), expr: [bool](class_bool.md#class-bool) = false)                                                                                  |
|                                                                                   | set_selectable(column: [int](class_int.md#class-int), selectable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                       |
|                                                                                   | set_structured_text_bidi_override(column: [int](class_int.md#class-int), parser: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser))                                                                                                                                     |
|                                                                                   | set_structured_text_bidi_override_options(column: [int](class_int.md#class-int), args: [Array](class_array.md#class-array))                                                                                                                                                                    |
|                                                                                   | set_suffix(column: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                                                                                                                                                                               |
|                                                                                   | set_text(column: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                                                                                                                                                                                   |
|                                                                                   | set_text_alignment(column: [int](class_int.md#class-int), text_alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))                                                                                                                                                          |
|                                                                                   | set_text_direction(column: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection))                                                                                                                                                                                    |
|                                                                                   | set_text_overrun_behavior(column: [int](class_int.md#class-int), overrun_behavior: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))                                                                                                                                                     |
|                                                                                   | set_tooltip_text(column: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                                                                                                                                                                                                |
|                                                                                   | uncollapse_tree()                                                                                                                                                                                                                                                                                                        |

---

## Enumerations

enum **TreeCellMode**:

TreeCellMode **CELL_MODE_STRING** = `0`

Cell shows a string label, optionally with an icon. When editable, the text can be edited using a [LineEdit](class_lineedit.md#class-lineedit), or a [TextEdit](class_textedit.md#class-textedit) popup if set_edit_multiline() is used.

TreeCellMode **CELL_MODE_CHECK** = `1`

Cell shows a checkbox, optionally with text and an icon. The checkbox can be pressed, released, or indeterminate (via set_indeterminate()). The checkbox can't be clicked unless the cell is editable.

TreeCellMode **CELL_MODE_RANGE** = `2`

Cell shows a numeric range. When editable, it can be edited using a range slider. Use set_range() to set the value and set_range_config() to configure the range.

This cell can also be used in a text dropdown mode when you assign a text with set_text(). Separate options with a comma, e.g. `"Option1,Option2,Option3"`.

TreeCellMode **CELL_MODE_ICON** = `3`

Cell shows an icon. It can't be edited nor display text. The icon is always centered within the cell.

TreeCellMode **CELL_MODE_CUSTOM** = `4`

Cell shows as a clickable button. It will display an arrow similar to [OptionButton](class_optionbutton.md#class-optionbutton), but doesn't feature a dropdown (for that you can use CELL_MODE_RANGE). Clicking the button emits the [Tree.item_edited](class_tree.md#class-tree-signal-item-edited) signal. The button is flat by default, you can use set_custom_as_button() to display it with a [StyleBox](class_stylebox.md#class-stylebox).

This mode also supports custom drawing using set_custom_draw_callback().

---

## Property Descriptions

[bool](class_bool.md#class-bool) **collapsed**

-  **set_collapsed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_collapsed**()

If `true`, the TreeItem is collapsed.

---

[int](class_int.md#class-int) **custom_minimum_height**

-  **set_custom_minimum_height**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_custom_minimum_height**()

The custom minimum height.

---

[bool](class_bool.md#class-bool) **disable_folding**

-  **set_disable_folding**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_folding_disabled**()

If `true`, folding is disabled for this TreeItem.

---

[bool](class_bool.md#class-bool) **visible**

-  **set_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visible**()

If `true`, the **TreeItem** is visible (default).

Note that if a **TreeItem** is set to not be visible, none of its children will be visible either.

---

## Method Descriptions

 **add_button**(column: [int](class_int.md#class-int), button: [Texture2D](class_texture2d.md#class-texture2d), id: [int](class_int.md#class-int) = -1, disabled: [bool](class_bool.md#class-bool) = false, tooltip_text: [String](class_string.md#class-string) = "", description: [String](class_string.md#class-string) = "")

Adds a button with [Texture2D](class_texture2d.md#class-texture2d) `button` to the end of the cell at column `column`. The `id` is used to identify the button in the according [Tree.button_clicked](class_tree.md#class-tree-signal-button-clicked) signal and can be different from the buttons index. If not specified, the next available index is used, which may be retrieved by calling get_button_count() immediately before this method. Optionally, the button can be `disabled` and have a `tooltip_text`. `description` is used as the button description for assistive apps.

---

 **add_child**(child: TreeItem)

Adds a previously unparented **TreeItem** as a direct child of this one. The `child` item must not be a part of any [Tree](class_tree.md#class-tree) or parented to any **TreeItem**. See also remove_child().

---

 **call_recursive**(method: [StringName](class_stringname.md#class-stringname), ...)

Calls the `method` on the actual TreeItem and its children recursively. Pass parameters as a comma separated list.

---

 **clear_buttons**()

Removes all buttons from all columns of this item.

---

 **clear_custom_bg_color**(column: [int](class_int.md#class-int))

Resets the background color for the given column to default.

---

 **clear_custom_color**(column: [int](class_int.md#class-int))

Resets the color for the given column to default.

---

TreeItem **create_child**(index: [int](class_int.md#class-int) = -1)

Creates an item and adds it as a child.

The new item will be inserted as position `index` (the default value `-1` means the last position), or it will be the last child if `index` is higher than the child count.

---

 **deselect**(column: [int](class_int.md#class-int))

Deselects the given column.

---

 **erase_button**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))

Removes the button at index `button_index` in column `column`.

---

[AutoTranslateMode](class_node.md#enum-node-autotranslatemode) **get_auto_translate_mode**(column: [int](class_int.md#class-int))

Returns the column's auto translate mode.

---

[AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **get_autowrap_mode**(column: [int](class_int.md#class-int))

Returns the text autowrap mode in the given `column`. By default it is [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off).

---

[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **get_autowrap_trim_flags**(column: [int](class_int.md#class-int))

Returns the autowrap trim flags for the given `column`. By default, both [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-start-edge-spaces) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-end-edge-spaces) are enabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_button**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))

Returns the [Texture2D](class_texture2d.md#class-texture2d) of the button at index `button_index` in column `column`.

---

[int](class_int.md#class-int) **get_button_by_id**(column: [int](class_int.md#class-int), id: [int](class_int.md#class-int))

Returns the button index if there is a button with ID `id` in column `column`, otherwise returns -1.

---

[Color](class_color.md#class-color) **get_button_color**(column: [int](class_int.md#class-int), id: [int](class_int.md#class-int))

Returns the color of the button with ID `id` in column `column`. If the specified button does not exist, returns [Color.BLACK](class_color.md#class-color-constant-black).

---

[int](class_int.md#class-int) **get_button_count**(column: [int](class_int.md#class-int))

Returns the number of buttons in column `column`.

---

[int](class_int.md#class-int) **get_button_id**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))

Returns the ID for the button at index `button_index` in column `column`.

---

[String](class_string.md#class-string) **get_button_tooltip_text**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))

Returns the tooltip text for the button at index `button_index` in column `column`.

---

TreeCellMode **get_cell_mode**(column: [int](class_int.md#class-int))

Returns the column's cell mode.

---

TreeItem **get_child**(index: [int](class_int.md#class-int))

Returns a child item by its `index` (see get_child_count()). This method is often used for iterating all children of an item.

Negative indices access the children from the last one.

---

[int](class_int.md#class-int) **get_child_count**()

Returns the number of child items.

---

[Array](class_array.md#class-array)[TreeItem] **get_children**()

Returns an array of references to the item's children.

---

[Color](class_color.md#class-color) **get_custom_bg_color**(column: [int](class_int.md#class-int))

Returns the custom background color of column `column`.

---

[Color](class_color.md#class-color) **get_custom_color**(column: [int](class_int.md#class-int))

Returns the custom color of column `column`.

---

[Callable](class_callable.md#class-callable) **get_custom_draw_callback**(column: [int](class_int.md#class-int))

Returns the custom callback of column `column`.

---

[Font](class_font.md#class-font) **get_custom_font**(column: [int](class_int.md#class-int))

Returns custom font used to draw text in the column `column`.

---

[int](class_int.md#class-int) **get_custom_font_size**(column: [int](class_int.md#class-int))

Returns custom font size used to draw text in the column `column`.

---

[StyleBox](class_stylebox.md#class-stylebox) **get_custom_stylebox**(column: [int](class_int.md#class-int))

Returns the given column's custom [StyleBox](class_stylebox.md#class-stylebox) used to draw the background.

---

[String](class_string.md#class-string) **get_description**(column: [int](class_int.md#class-int))

Returns the given column's description for assistive apps.

---

[bool](class_bool.md#class-bool) **get_expand_right**(column: [int](class_int.md#class-int))

Returns `true` if `expand_right` is set.

---

TreeItem **get_first_child**()

Returns the TreeItem's first child.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_icon**(column: [int](class_int.md#class-int))

Returns the given column's icon [Texture2D](class_texture2d.md#class-texture2d). Error if no icon is set.

---

[int](class_int.md#class-int) **get_icon_max_width**(column: [int](class_int.md#class-int))

Returns the maximum allowed width of the icon in the given `column`.

---

[Color](class_color.md#class-color) **get_icon_modulate**(column: [int](class_int.md#class-int))

Returns the [Color](class_color.md#class-color) modulating the column's icon.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_icon_overlay**(column: [int](class_int.md#class-int))

Returns the given column's icon overlay [Texture2D](class_texture2d.md#class-texture2d).

---

[Rect2](class_rect2.md#class-rect2) **get_icon_region**(column: [int](class_int.md#class-int))

Returns the icon [Texture2D](class_texture2d.md#class-texture2d) region as [Rect2](class_rect2.md#class-rect2).

---

[int](class_int.md#class-int) **get_index**()

Returns the node's order in the tree. For example, if called on the first child item the position is `0`.

---

[String](class_string.md#class-string) **get_language**(column: [int](class_int.md#class-int))

Returns item's text language code.

---

[Variant](class_variant.md#class-variant) **get_metadata**(column: [int](class_int.md#class-int))

Returns the metadata value that was set for the given column using set_metadata().

---

TreeItem **get_next**()

Returns the next sibling TreeItem in the tree or a `null` object if there is none.

---

TreeItem **get_next_in_tree**(wrap: [bool](class_bool.md#class-bool) = false)

Returns the next TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the first element in the tree when called on the last element, otherwise it returns `null`.

---

TreeItem **get_next_visible**(wrap: [bool](class_bool.md#class-bool) = false)

Returns the next visible TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the first visible element in the tree when called on the last visible element, otherwise it returns `null`.

---

TreeItem **get_parent**()

Returns the parent TreeItem or a `null` object if there is none.

---

TreeItem **get_prev**()

Returns the previous sibling TreeItem in the tree or a `null` object if there is none.

---

TreeItem **get_prev_in_tree**(wrap: [bool](class_bool.md#class-bool) = false)

Returns the previous TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the last element in the tree when called on the first visible element, otherwise it returns `null`.

---

TreeItem **get_prev_visible**(wrap: [bool](class_bool.md#class-bool) = false)

Returns the previous visible sibling TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the last visible element in the tree when called on the first visible element, otherwise it returns `null`.

---

[float](class_float.md#class-float) **get_range**(column: [int](class_int.md#class-int))

Returns the value of a CELL_MODE_RANGE column.

---

[Dictionary](class_dictionary.md#class-dictionary) **get_range_config**(column: [int](class_int.md#class-int))

Returns a dictionary containing the range parameters for a given column. The keys are "min", "max", "step", and "expr".

---

[StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) **get_structured_text_bidi_override**(column: [int](class_int.md#class-int))

Returns the BiDi algorithm override set for this cell.

---

[Array](class_array.md#class-array) **get_structured_text_bidi_override_options**(column: [int](class_int.md#class-int))

Returns the additional BiDi options set for this cell.

---

[String](class_string.md#class-string) **get_suffix**(column: [int](class_int.md#class-int))

Gets the suffix string shown after the column value.

---

[String](class_string.md#class-string) **get_text**(column: [int](class_int.md#class-int))

Returns the given column's text.

---

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_text_alignment**(column: [int](class_int.md#class-int))

Returns the given column's text alignment.

---

[TextDirection](class_control.md#enum-control-textdirection) **get_text_direction**(column: [int](class_int.md#class-int))

Returns item's text base writing direction.

---

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_text_overrun_behavior**(column: [int](class_int.md#class-int))

Returns the clipping behavior when the text exceeds the item's bounding rectangle in the given `column`. By default it is [TextServer.OVERRUN_TRIM_ELLIPSIS](class_textserver.md#class-textserver-constant-overrun-trim-ellipsis).

---

[String](class_string.md#class-string) **get_tooltip_text**(column: [int](class_int.md#class-int))

Returns the given column's tooltip text.

---

[Tree](class_tree.md#class-tree) **get_tree**()

Returns the [Tree](class_tree.md#class-tree) that owns this TreeItem.

---

[bool](class_bool.md#class-bool) **is_accepting_children**()

Returns `true` if this **TreeItem** is allowed to accept children.

---

[bool](class_bool.md#class-bool) **is_any_collapsed**(only_visible: [bool](class_bool.md#class-bool) = false)

Returns `true` if this **TreeItem**, or any of its descendants, is collapsed.

If `only_visible` is `true` it ignores non-visible **TreeItem**s.

---

[bool](class_bool.md#class-bool) **is_button_disabled**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int))

Returns `true` if the button at index `button_index` for the given `column` is disabled.

---

[bool](class_bool.md#class-bool) **is_checked**(column: [int](class_int.md#class-int))

Returns `true` if the given `column` is checked.

---

[bool](class_bool.md#class-bool) **is_custom_set_as_button**(column: [int](class_int.md#class-int))

Returns `true` if the cell was made into a button with set_custom_as_button().

---

[bool](class_bool.md#class-bool) **is_edit_multiline**(column: [int](class_int.md#class-int))

Returns `true` if the given `column` is multiline editable.

---

[bool](class_bool.md#class-bool) **is_editable**(column: [int](class_int.md#class-int))

Returns `true` if the given `column` is editable.

---

[bool](class_bool.md#class-bool) **is_indeterminate**(column: [int](class_int.md#class-int))

Returns `true` if the given `column` is indeterminate.

---

[bool](class_bool.md#class-bool) **is_selectable**(column: [int](class_int.md#class-int))

Returns `true` if the given `column` is selectable.

---

[bool](class_bool.md#class-bool) **is_selected**(column: [int](class_int.md#class-int))

Returns `true` if the given `column` is selected.

---

[bool](class_bool.md#class-bool) **is_visible_in_tree**()

Returns `true` if visible is `true` and all its ancestors are also visible.

---

 **move_after**(item: TreeItem)

Moves this TreeItem right after the given `item`.

**Note:** You can't move to the root or move the root.

---

 **move_before**(item: TreeItem)

Moves this TreeItem right before the given `item`.

**Note:** You can't move to the root or move the root.

---

 **propagate_check**(column: [int](class_int.md#class-int), emit_signal: [bool](class_bool.md#class-bool) = true)

Propagates this item's checked status to its children and parents for the given `column`. It is possible to process the items affected by this method call by connecting to [Tree.check_propagated_to_item](class_tree.md#class-tree-signal-check-propagated-to-item). The order that the items affected will be processed is as follows: the item invoking this method, children of that item, and finally parents of that item. If `emit_signal` is `false`, then [Tree.check_propagated_to_item](class_tree.md#class-tree-signal-check-propagated-to-item) will not be emitted.

---

 **remove_child**(child: TreeItem)

Removes the given child **TreeItem** and all its children from the [Tree](class_tree.md#class-tree). Note that it doesn't free the item from memory, so it can be reused later (see add_child()). To completely remove a **TreeItem** use [Object.free()](class_object.md#class-object-method-free).

**Note:** If you want to move a child from one [Tree](class_tree.md#class-tree) to another, then instead of removing and adding it manually you can use move_before() or move_after().

---

 **select**(column: [int](class_int.md#class-int), set_as_cursor: [bool](class_bool.md#class-bool) = true)

Selects the given `column`. If `set_as_cursor` is `true`, the [Tree](class_tree.md#class-tree)'s cursor will be moved to this item (only matters if [Tree.select_mode](class_tree.md#class-tree-property-select-mode) is set to [Tree.SELECT_MULTI](class_tree.md#class-tree-constant-select-multi)).

---

 **set_accept_children**(allowed: [bool](class_bool.md#class-bool))

Sets **TreeItem**'s ability to accept children.

---

 **set_auto_translate_mode**(column: [int](class_int.md#class-int), mode: [AutoTranslateMode](class_node.md#enum-node-autotranslatemode))

Sets the given column's auto translate mode to `mode`.

All columns use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class-node-constant-auto-translate-mode-inherit) by default, which uses the same auto translate mode as the [Tree](class_tree.md#class-tree) itself.

---

 **set_autowrap_mode**(column: [int](class_int.md#class-int), autowrap_mode: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode))

Sets the autowrap mode in the given `column`. If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off), the text gets wrapped inside the cell's bounding rectangle.

---

 **set_autowrap_trim_flags**(column: [int](class_int.md#class-int), flags: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])

Sets the autowrap trim flags for the given `column`. These flags control whether leading and trailing spaces are trimmed on wrapped lines. Set to `0` to disable all trimming.

---

 **set_button**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), button: [Texture2D](class_texture2d.md#class-texture2d))

Sets the given column's button [Texture2D](class_texture2d.md#class-texture2d) at index `button_index` to `button`.

---

 **set_button_color**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the given column's button color at index `button_index` to `color`.

---

 **set_button_description**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), description: [String](class_string.md#class-string))

Sets the given column's button description at index `button_index` for assistive apps.

---

 **set_button_disabled**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

If `true`, disables the button at index `button_index` in the given `column`.

---

 **set_button_tooltip_text**(column: [int](class_int.md#class-int), button_index: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets the tooltip text for the button at index `button_index` in the given `column`.

---

 **set_cell_mode**(column: [int](class_int.md#class-int), mode: TreeCellMode)

Sets the given column's cell mode to `mode`. This determines how the cell is displayed and edited.

---

 **set_checked**(column: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool))

If `checked` is `true`, the given `column` is checked. Clears column's indeterminate status.

---

 **set_collapsed_recursive**(enable: [bool](class_bool.md#class-bool))

Collapses or uncollapses this **TreeItem** and all the descendants of this item.

---

 **set_custom_as_button**(column: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

Makes a cell with CELL_MODE_CUSTOM display as a non-flat button with a [StyleBox](class_stylebox.md#class-stylebox).

---

 **set_custom_bg_color**(column: [int](class_int.md#class-int), color: [Color](class_color.md#class-color), just_outline: [bool](class_bool.md#class-bool) = false)

Sets the given column's custom background color and whether to just use it as an outline.

**Note:** If a custom [StyleBox](class_stylebox.md#class-stylebox) is set, the background color will be drawn behind it.

---

 **set_custom_color**(column: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the given column's custom color.

---

 **set_custom_draw**(column: [int](class_int.md#class-int), object: [Object](class_object.md#class-object), callback: [StringName](class_stringname.md#class-stringname))

**Deprecated:** Use set_custom_draw_callback() instead.

Sets the given column's custom draw callback to the `callback` method on `object`.

The method named `callback` should accept two arguments: the **TreeItem** that is drawn and its position and size as a [Rect2](class_rect2.md#class-rect2).

---

 **set_custom_draw_callback**(column: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))

Sets the given column's custom draw callback. Use an empty [Callable](class_callable.md#class-callable) (`Callable()`) to clear the custom callback. The cell has to be in CELL_MODE_CUSTOM to use this feature.

The `callback` should accept two arguments: the **TreeItem** that is drawn and its position and size as a [Rect2](class_rect2.md#class-rect2).

To draw custom content over the native style, please use [Tree.get_custom_drawing_canvas_item()](class_tree.md#class-tree-method-get-custom-drawing-canvas-item).

---

 **set_custom_font**(column: [int](class_int.md#class-int), font: [Font](class_font.md#class-font))

Sets custom font used to draw text in the given `column`.

---

 **set_custom_font_size**(column: [int](class_int.md#class-int), font_size: [int](class_int.md#class-int))

Sets custom font size used to draw text in the given `column`.

---

 **set_custom_stylebox**(column: [int](class_int.md#class-int), stylebox: [StyleBox](class_stylebox.md#class-stylebox))

Sets the given column's custom [StyleBox](class_stylebox.md#class-stylebox) used to draw the background.

**Note:** If a custom background color is set, the [StyleBox](class_stylebox.md#class-stylebox) will be drawn in front of it.

---

 **set_description**(column: [int](class_int.md#class-int), description: [String](class_string.md#class-string))

Sets the given column's description for assistive apps.

---

 **set_edit_multiline**(column: [int](class_int.md#class-int), multiline: [bool](class_bool.md#class-bool))

If `multiline` is `true`, the given `column` is multiline editable.

**Note:** This option only affects the type of control ([LineEdit](class_lineedit.md#class-lineedit) or [TextEdit](class_textedit.md#class-textedit)) that appears when editing the column. You can set multiline values with set_text() even if the column is not multiline editable.

---

 **set_editable**(column: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, the given `column` is editable.

---

 **set_expand_right**(column: [int](class_int.md#class-int), enable: [bool](class_bool.md#class-bool))

If `enable` is `true`, the given `column` is expanded to the right.

---

 **set_icon**(column: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))

Sets the given cell's icon [Texture2D](class_texture2d.md#class-texture2d). If the cell is in CELL_MODE_ICON mode, the icon is displayed in the center of the cell. Otherwise, the icon is displayed before the cell's text. CELL_MODE_RANGE does not display an icon.

---

 **set_icon_max_width**(column: [int](class_int.md#class-int), width: [int](class_int.md#class-int))

Sets the maximum allowed width of the icon in the given `column`. This limit is applied on top of the default size of the icon and on top of [Tree.icon_max_width](class_tree.md#class-tree-theme-constant-icon-max-width). The height is adjusted according to the icon's ratio.

---

 **set_icon_modulate**(column: [int](class_int.md#class-int), modulate: [Color](class_color.md#class-color))

Modulates the given column's icon with `modulate`.

---

 **set_icon_overlay**(column: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))

Sets the given cell's icon overlay [Texture2D](class_texture2d.md#class-texture2d). The cell has to be in CELL_MODE_ICON mode, and icon has to be set. Overlay is drawn on top of icon, in the bottom left corner.

---

 **set_icon_region**(column: [int](class_int.md#class-int), region: [Rect2](class_rect2.md#class-rect2))

Sets the given column's icon's texture region.

---

 **set_indeterminate**(column: [int](class_int.md#class-int), indeterminate: [bool](class_bool.md#class-bool))

If `indeterminate` is `true`, the given `column` is marked indeterminate.

**Note:** If set `true` from `false`, then column is cleared of checked status.

---

 **set_language**(column: [int](class_int.md#class-int), language: [String](class_string.md#class-string))

Sets the language code of the given `column`'s text to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---

 **set_metadata**(column: [int](class_int.md#class-int), meta: [Variant](class_variant.md#class-variant))

Sets the metadata value for the given column, which can be retrieved later using get_metadata(). This can be used, for example, to store a reference to the original data.

---

 **set_range**(column: [int](class_int.md#class-int), value: [float](class_float.md#class-float))

Sets the value of a CELL_MODE_RANGE column.

---

 **set_range_config**(column: [int](class_int.md#class-int), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float), step: [float](class_float.md#class-float), expr: [bool](class_bool.md#class-bool) = false)

Sets the range of accepted values for a column. The column must be in the CELL_MODE_RANGE mode.

If `expr` is `true`, the edit mode slider will use an exponential scale as with [Range.exp_edit](class_range.md#class-range-property-exp-edit).

---

 **set_selectable**(column: [int](class_int.md#class-int), selectable: [bool](class_bool.md#class-bool))

If `selectable` is `true`, the given `column` is selectable.

---

 **set_structured_text_bidi_override**(column: [int](class_int.md#class-int), parser: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser))

Set BiDi algorithm override for the structured text. Has effect for cells that display text.

---

 **set_structured_text_bidi_override_options**(column: [int](class_int.md#class-int), args: [Array](class_array.md#class-array))

Set additional options for BiDi override. Has effect for cells that display text.

---

 **set_suffix**(column: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

Sets a string to be shown after a column's value (for example, a unit abbreviation).

---

 **set_text**(column: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

Sets the given column's text value.

---

 **set_text_alignment**(column: [int](class_int.md#class-int), text_alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))

Sets the given column's text alignment to `text_alignment`.

---

 **set_text_direction**(column: [int](class_int.md#class-int), direction: [TextDirection](class_control.md#enum-control-textdirection))

Sets item's text base writing direction.

---

 **set_text_overrun_behavior**(column: [int](class_int.md#class-int), overrun_behavior: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))

Sets the clipping behavior when the text exceeds the item's bounding rectangle in the given `column`.

---

 **set_tooltip_text**(column: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets the given column's tooltip text.

---

 **uncollapse_tree**()

Uncollapses all **TreeItem**s necessary to reveal this **TreeItem**, i.e. all ancestor **TreeItem**s.
