# RichTextLabel

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control for displaying text that can contain different font styles, images, and basic formatting.

## Description

A control for displaying text that can contain custom fonts, images, and basic formatting. **RichTextLabel** manages these as an internal tag stack. It also adapts itself to given width/heights.

**Note:** newline(), push_paragraph(), `"\n"`, `"\r\n"`, `p` tag, and alignment tags start a new paragraph. Each paragraph is processed independently, in its own BiDi context. If you want to force line wrapping within paragraph, any other line breaking character can be used, for example, Form Feed (U+000C), Next Line (U+0085), Line Separator (U+2028).

**Note:** Assignments to text clear the tag stack and reconstruct it from the property's contents. Any edits made to text will erase previous edits made from other manual sources such as append_text() and the `push_*` / pop() methods.

**Note:** RichTextLabel doesn't support entangled BBCode tags. For example, instead of using `[b]bold[i]bold italic[/b]italic[/i]`, use `[b]bold[i]bold italic[/i][/b][i]italic[/i]`.

**Note:** `push_*/pop_*` functions won't affect BBCode.

**Note:** While bbcode_enabled is enabled, alignment tags such as `[center]` will take priority over the horizontal_alignment setting which determines the default text alignment.

## Tutorials

- [BBCode in RichTextLabel](../tutorials/ui/bbcode_in_richtextlabel.md)
- [Rich Text Label with BBCode Demo](https://godotengine.org/asset-library/asset/2774)
- [Operating System Testing Demo](https://godotengine.org/asset-library/asset/2789)

## Properties

| [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode)                           | autowrap_mode                                                 | `3`                                                                                 |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)]                       | autowrap_trim_flags                                     | `192`                                                                               |
| [bool](class_bool.md#class-bool)                                                           | bbcode_enabled                                               | `false`                                                                             |
| [bool](class_bool.md#class-bool)                                                           | clip_contents                                                                                                | `true` (overrides [Control](class_control.md#class-control-property-clip-contents)) |
| [bool](class_bool.md#class-bool)                                                           | context_menu_enabled                                   | `false`                                                                             |
| [Array](class_array.md#class-array)                                                        | custom_effects                                               | `[]`                                                                                |
| [bool](class_bool.md#class-bool)                                                           | deselect_on_focus_loss_enabled               | `true`                                                                              |
| [bool](class_bool.md#class-bool)                                                           | drag_and_drop_selection_enabled             | `true`                                                                              |
| [bool](class_bool.md#class-bool)                                                           | fit_content                                                     | `false`                                                                             |
| [FocusMode](class_control.md#enum-control-focusmode)                                       | focus_mode                                                                                                   | `3` (overrides [Control](class_control.md#class-control-property-focus-mode))       |
| [bool](class_bool.md#class-bool)                                                           | hint_underlined                                             | `true`                                                                              |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment)          | horizontal_alignment                                   | `0`                                                                                 |
| [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)]               | justification_flags                                     | `163`                                                                               |
| [String](class_string.md#class-string)                                                     | language                                                           | `""`                                                                                |
| [bool](class_bool.md#class-bool)                                                           | meta_underlined                                             | `true`                                                                              |
| [int](class_int.md#class-int)                                                              | progress_bar_delay                                       | `1000`                                                                              |
| [bool](class_bool.md#class-bool)                                                           | scroll_active                                                 | `true`                                                                              |
| [bool](class_bool.md#class-bool)                                                           | scroll_following                                           | `false`                                                                             |
| [bool](class_bool.md#class-bool)                                                           | scroll_following_visible_characters     | `false`                                                                             |
| [bool](class_bool.md#class-bool)                                                           | selection_enabled                                         | `false`                                                                             |
| [bool](class_bool.md#class-bool)                                                           | shortcut_keys_enabled                                 | `true`                                                                              |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser)           | structured_text_bidi_override                 | `0`                                                                                 |
| [Array](class_array.md#class-array)                                                        | structured_text_bidi_override_options | `[]`                                                                                |
| [int](class_int.md#class-int)                                                              | tab_size                                                           | `4`                                                                                 |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)                 | tab_stops                                                         | `PackedFloat32Array()`                                                              |
| [String](class_string.md#class-string)                                                     | text                                                                   | `""`                                                                                |
| [TextDirection](class_control.md#enum-control-textdirection)                               | text_direction                                               | `0`                                                                                 |
| [bool](class_bool.md#class-bool)                                                           | threaded                                                           | `false`                                                                             |
| [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment)              | vertical_alignment                                       | `0`                                                                                 |
| [int](class_int.md#class-int)                                                              | visible_characters                                       | `-1`                                                                                |
| [VisibleCharactersBehavior](class_textserver.md#enum-textserver-visiblecharactersbehavior) | visible_characters_behavior                     | `0`                                                                                 |
| [float](class_float.md#class-float)                                                        | visible_ratio                                                 | `1.0`                                                                               |

## Methods

|                                                    | add_hr(width: [int](class_int.md#class-int) = 90, height: [int](class_int.md#class-int) = 2, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 1, width_in_percent: [bool](class_bool.md#class-bool) = true, height_in_percent: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                    | add_image(image: [Texture2D](class_texture2d.md#class-texture2d), width: [float](class_float.md#class-float) = 0, height: [float](class_float.md#class-float) = 0, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, region: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), key: [Variant](class_variant.md#class-variant) = null, pad: [bool](class_bool.md#class-bool) = false, tooltip: [String](class_string.md#class-string) = "", width_unit: ImageUnit = 0, height_unit: ImageUnit = 0, alt_text: [String](class_string.md#class-string) = "")         |
|                                                    | add_text(text: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                    | append_text(bbcode: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                    | clear()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                    | deselect()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                      | get_character_line(character: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                      | get_character_paragraph(character: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                      | get_content_height()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                      | get_content_width()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                      | get_line_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                      | get_line_height(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [float](class_float.md#class-float)                | get_line_offset(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Vector2i](class_vector2i.md#class-vector2i)       | get_line_range(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                      | get_line_width(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [PopupMenu](class_popupmenu.md#class-popupmenu)    | get_menu()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                      | get_paragraph_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [float](class_float.md#class-float)                | get_paragraph_offset(paragraph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)             | get_parsed_text()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [String](class_string.md#class-string)             | get_selected_text()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                      | get_selection_from()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                | get_selection_line_offset()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                      | get_selection_to()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                      | get_total_character_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [VScrollBar](class_vscrollbar.md#class-vscrollbar) | get_v_scroll_bar()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Rect2i](class_rect2i.md#class-rect2i)             | get_visible_content_rect()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                      | get_visible_line_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                      | get_visible_paragraph_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                    | install_effect(effect: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                   | invalidate_paragraph(paragraph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                   | is_finished()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                   | is_menu_visible()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                   | is_ready()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                    | menu_option(option: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    | newline()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                    | parse_bbcode(bbcode: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dictionary](class_dictionary.md#class-dictionary) | parse_expressions_for_values(expressions: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                    | pop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                    | pop_all()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                    | pop_context()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                    | push_bgcolor(bgcolor: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                    | push_bold()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                    | push_bold_italics()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                    | push_cell()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                    | push_color(color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                    | push_context()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                    | push_customfx(effect: [RichTextEffect](class_richtexteffect.md#class-richtexteffect), env: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                    | push_dropcap(string: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), size: [int](class_int.md#class-int), dropcap_margins: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), outline_size: [int](class_int.md#class-int) = 0, outline_color: [Color](class_color.md#class-color) = Color(0, 0, 0, 0))                                                                                                                                                                                                                                                                                                                                      |
|                                                    | push_fgcolor(fgcolor: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                    | push_font(font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                    | push_font_size(font_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                    | push_hint(description: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                    | push_indent(level: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                    | push_italics()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                    | push_language(language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                    | push_list(level: [int](class_int.md#class-int), type: ListType, capitalize: [bool](class_bool.md#class-bool), bullet: [String](class_string.md#class-string) = "•")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                    | push_meta(data: [Variant](class_variant.md#class-variant), underline_mode: MetaUnderline = 1, tooltip: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                    | push_mono()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                    | push_normal()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                    | push_outline_color(color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                    | push_outline_size(outline_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                    | push_paragraph(alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment), base_direction: [TextDirection](class_control.md#enum-control-textdirection) = 0, language: [String](class_string.md#class-string) = "", st_parser: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) = 0, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 163, tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) = PackedFloat32Array())                                                                                                                                                                   |
|                                                    | push_strikethrough(color: [Color](class_color.md#class-color) = Color(0, 0, 0, 0))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                    | push_table(columns: [int](class_int.md#class-int), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 0, align_to_row: [int](class_int.md#class-int) = -1, name: [String](class_string.md#class-string) = "")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                    | push_underline(color: [Color](class_color.md#class-color) = Color(0, 0, 0, 0))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                    | reload_effects()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                   | remove_paragraph(paragraph: [int](class_int.md#class-int), no_invalidate: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                    | scroll_to_line(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                    | scroll_to_paragraph(paragraph: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                    | scroll_to_selection()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                    | select_all()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                    | set_cell_border_color(color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                    | set_cell_padding(padding: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                    | set_cell_row_background_color(odd_row_bg: [Color](class_color.md#class-color), even_row_bg: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                    | set_cell_size_override(min_size: [Vector2](class_vector2.md#class-vector2), max_size: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                    | set_table_column_expand(column: [int](class_int.md#class-int), expand: [bool](class_bool.md#class-bool), ratio: [int](class_int.md#class-int) = 1, shrink: [bool](class_bool.md#class-bool) = true)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                    | set_table_column_name(column: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                    | update_image(key: [Variant](class_variant.md#class-variant), mask: [ImageUpdateMask], image: [Texture2D](class_texture2d.md#class-texture2d), width: [float](class_float.md#class-float) = 0, height: [float](class_float.md#class-float) = 0, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, region: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), pad: [bool](class_bool.md#class-bool) = false, tooltip: [String](class_string.md#class-string) = "", width_unit: ImageUnit = 0, height_unit: ImageUnit = 0) |

## Theme Properties

| [Color](class_color.md#class-color)             | default_color                          | `Color(1, 1, 1, 1)`       |
|-------------------------------------------------|------------------------------------------------------------------------------------------|---------------------------|
| [Color](class_color.md#class-color)             | font_outline_color                | `Color(0, 0, 0, 1)`       |
| [Color](class_color.md#class-color)             | font_selected_color              | `Color(0, 0, 0, 0)`       |
| [Color](class_color.md#class-color)             | font_shadow_color                  | `Color(0, 0, 0, 0)`       |
| [Color](class_color.md#class-color)             | selection_color                      | `Color(0.1, 0.1, 1, 0.8)` |
| [Color](class_color.md#class-color)             | table_border                            | `Color(0, 0, 0, 0)`       |
| [Color](class_color.md#class-color)             | table_even_row_bg                  | `Color(0, 0, 0, 0)`       |
| [Color](class_color.md#class-color)             | table_odd_row_bg                    | `Color(0, 0, 0, 0)`       |
| [int](class_int.md#class-int)                   | line_separation                   | `0`                       |
| [int](class_int.md#class-int)                   | outline_size                         | `0`                       |
| [int](class_int.md#class-int)                   | paragraph_separation         | `0`                       |
| [int](class_int.md#class-int)                   | shadow_offset_x                   | `1`                       |
| [int](class_int.md#class-int)                   | shadow_offset_y                   | `1`                       |
| [int](class_int.md#class-int)                   | shadow_outline_size           | `1`                       |
| [int](class_int.md#class-int)                   | strikethrough_alpha           | `50`                      |
| [int](class_int.md#class-int)                   | table_h_separation             | `3`                       |
| [int](class_int.md#class-int)                   | table_v_separation             | `3`                       |
| [int](class_int.md#class-int)                   | text_highlight_h_padding | `3`                       |
| [int](class_int.md#class-int)                   | text_highlight_v_padding | `3`                       |
| [int](class_int.md#class-int)                   | underline_alpha                   | `50`                      |
| [Font](class_font.md#class-font)                | bold_font                                   |                           |
| [Font](class_font.md#class-font)                | bold_italics_font                   |                           |
| [Font](class_font.md#class-font)                | italics_font                             |                           |
| [Font](class_font.md#class-font)                | mono_font                                   |                           |
| [Font](class_font.md#class-font)                | normal_font                               |                           |
| [int](class_int.md#class-int)                   | bold_font_size                    |                           |
| [int](class_int.md#class-int)                   | bold_italics_font_size    |                           |
| [int](class_int.md#class-int)                   | italics_font_size              |                           |
| [int](class_int.md#class-int)                   | mono_font_size                    |                           |
| [int](class_int.md#class-int)                   | normal_font_size                |                           |
| [Texture2D](class_texture2d.md#class-texture2d) | horizontal_rule                       |                           |
| [StyleBox](class_stylebox.md#class-stylebox)    | focus                                          |                           |
| [StyleBox](class_stylebox.md#class-stylebox)    | normal                                        |                           |

---

## Signals

**finished**()

Triggered when the document is fully loaded.

**Note:** This can happen before the text is processed for drawing. Scrolling values may not be valid until the document is drawn for the first time after this signal.

---

**meta_clicked**(meta: [Variant](class_variant.md#class-variant))

Triggered when the user clicks on content between meta (URL) tags. If the meta is defined in BBCode, e.g. `[url={"key": "value"}]Text[/url]`, then the parameter for this signal will always be a [String](class_string.md#class-string) type. If a particular type or an object is desired, the push_meta() method must be used to manually insert the data into the tag stack. Alternatively, you can convert the [String](class_string.md#class-string) input to the desired type based on its contents (such as calling [JSON.parse()](class_json.md#class-json-method-parse) on it).

For example, the following method can be connected to meta_clicked to open clicked URLs using the user's default web browser:

GDScript

```gdscript
# This assumes RichTextLabel's `meta_clicked` signal was connected to
# the function below using the signal connection dialog.
func _richtextlabel_on_meta_clicked(meta):
    # `meta` is of Variant type, so convert it to a String to avoid script errors at run-time.
    OS.shell_open(str(meta))
```

---

**meta_hover_ended**(meta: [Variant](class_variant.md#class-variant))

Triggers when the mouse exits a meta tag.

---

**meta_hover_started**(meta: [Variant](class_variant.md#class-variant))

Triggers when the mouse enters a meta tag.

---

## Enumerations

enum **ListType**:

ListType **LIST_NUMBERS** = `0`

Each list item has a number marker.

ListType **LIST_LETTERS** = `1`

Each list item has a letter marker.

ListType **LIST_ROMAN** = `2`

Each list item has a roman number marker.

ListType **LIST_DOTS** = `3`

Each list item has a filled circle marker.

---

enum **MenuItems**:

MenuItems **MENU_COPY** = `0`

Copies the selected text.

MenuItems **MENU_SELECT_ALL** = `1`

Selects the whole **RichTextLabel** text.

MenuItems **MENU_MAX** = `2`

Represents the size of the MenuItems enum.

---

enum **MetaUnderline**:

MetaUnderline **META_UNDERLINE_NEVER** = `0`

Meta tag does not display an underline, even if meta_underlined is `true`.

MetaUnderline **META_UNDERLINE_ALWAYS** = `1`

If meta_underlined is `true`, meta tag always display an underline.

MetaUnderline **META_UNDERLINE_ON_HOVER** = `2`

If meta_underlined is `true`, meta tag display an underline when the mouse cursor is over it.

---

flags **ImageUpdateMask**:

ImageUpdateMask **UPDATE_TEXTURE** = `1`

If this bit is set, update_image() changes image texture.

ImageUpdateMask **UPDATE_SIZE** = `2`

If this bit is set, update_image() changes image size.

ImageUpdateMask **UPDATE_COLOR** = `4`

If this bit is set, update_image() changes image color.

ImageUpdateMask **UPDATE_ALIGNMENT** = `8`

If this bit is set, update_image() changes image inline alignment.

ImageUpdateMask **UPDATE_REGION** = `16`

If this bit is set, update_image() changes image texture region.

ImageUpdateMask **UPDATE_PAD** = `32`

If this bit is set, update_image() changes image padding.

ImageUpdateMask **UPDATE_TOOLTIP** = `64`

If this bit is set, update_image() changes image tooltip.

ImageUpdateMask **UPDATE_WIDTH_UNIT** = `128`

If this bit is set, update_image() changes the units used to calculate image size.

---

enum **ImageUnit**:

ImageUnit **IMAGE_UNIT_PIXEL** = `0`

Images drawn with this unit will be in pixels.

ImageUnit **IMAGE_UNIT_PERCENT** = `1`

Images drawn with this unit will be in percentages of the control width.

ImageUnit **IMAGE_UNIT_EM** = `2`

Images drawn with this unit will be in percentages of the surrounding font size.

---

## Property Descriptions

[AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **autowrap_mode** = `3`

-  **set_autowrap_mode**(value: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode))
- [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **get_autowrap_mode**()

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class-textserver-constant-autowrap-off), the text gets wrapped inside the node's bounding rectangle.

**Note:** RichTextLabels with autowrapping and fit_content enabled must have a custom maximum width configured to work correctly, either through the RichTextLabel's own [Control.custom_maximum_size](class_control.md#class-control-property-custom-maximum-size) or as a result of a propagated maximum size from a parent Control with [Control.propagate_maximum_size](class_control.md#class-control-property-propagate-maximum-size) enabled.

---

[[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **autowrap_trim_flags** = `192`

-  **set_autowrap_trim_flags**(value: [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)])
- [[LineBreakFlag](class_textserver.md#enum-textserver-linebreakflag)] **get_autowrap_trim_flags**()

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-start-edge-spaces) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class-textserver-constant-break-trim-end-edge-spaces) for more info.

---

[bool](class_bool.md#class-bool) **bbcode_enabled** = `false`

-  **set_use_bbcode**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_using_bbcode**()

If `true`, the label uses BBCode formatting.

**Note:** This only affects the contents of text, not the tag stack.

---

[bool](class_bool.md#class-bool) **context_menu_enabled** = `false`

-  **set_context_menu_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_context_menu_enabled**()

If `true`, a right-click displays the context menu.

---

[Array](class_array.md#class-array) **custom_effects** = `[]`

-  **set_effects**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_effects**()

The currently installed custom effects. This is an array of [RichTextEffect](class_richtexteffect.md#class-richtexteffect)s.

To add a custom effect, it's more convenient to use install_effect().

---

[bool](class_bool.md#class-bool) **deselect_on_focus_loss_enabled** = `true`

-  **set_deselect_on_focus_loss_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deselect_on_focus_loss_enabled**()

If `true`, the selected text will be deselected when focus is lost.

---

[bool](class_bool.md#class-bool) **drag_and_drop_selection_enabled** = `true`

-  **set_drag_and_drop_selection_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drag_and_drop_selection_enabled**()

If `true`, allow drag and drop of selected text.

---

[bool](class_bool.md#class-bool) **fit_content** = `false`

-  **set_fit_content**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_fit_content_enabled**()

If `true`, the label's minimum size will be automatically updated to fit its content, matching the behavior of [Label](class_label.md#class-label).

**Note:** RichTextLabels with autowrapping and fit_content enabled must have a custom maximum width configured to work correctly, either through the RichTextLabel's own [Control.custom_maximum_size](class_control.md#class-control-property-custom-maximum-size) or as a result of a propagated maximum size from a parent Control with [Control.propagate_maximum_size](class_control.md#class-control-property-propagate-maximum-size) enabled.

---

[bool](class_bool.md#class-bool) **hint_underlined** = `true`

-  **set_hint_underline**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_hint_underlined**()

If `true`, the label underlines hint tags such as `[hint=description]{text}[/hint]`.

---

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **horizontal_alignment** = `0`

-  **set_horizontal_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_horizontal_alignment**()

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---

[[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **justification_flags** = `163`

-  **set_justification_flags**(value: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)])
- [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] **get_justification_flags**()

Line fill alignment rules.

---

[String](class_string.md#class-string) **language** = `""`

-  **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

[bool](class_bool.md#class-bool) **meta_underlined** = `true`

-  **set_meta_underline**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_meta_underlined**()

If `true`, the label underlines meta tags such as `[url]{text}[/url]`. These tags can call a function when clicked if meta_clicked is connected to a function.

---

[int](class_int.md#class-int) **progress_bar_delay** = `1000`

-  **set_progress_bar_delay**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_progress_bar_delay**()

The delay after which the loading progress bar is displayed, in milliseconds. Set to `-1` to disable progress bar entirely.

**Note:** Progress bar is displayed only if threaded is enabled.

---

[bool](class_bool.md#class-bool) **scroll_active** = `true`

-  **set_scroll_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_active**()

If `true`, the scrollbar is visible. Setting this to `false` does not block scrolling completely. See scroll_to_line().

---

[bool](class_bool.md#class-bool) **scroll_following** = `false`

-  **set_scroll_follow**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_following**()

If `true`, the window scrolls down to display new content automatically.

---

[bool](class_bool.md#class-bool) **scroll_following_visible_characters** = `false`

-  **set_scroll_follow_visible_characters**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_following_visible_characters**()

If `true`, the window scrolls to display the last visible line when visible_characters or visible_ratio is changed.

---

[bool](class_bool.md#class-bool) **selection_enabled** = `false`

-  **set_selection_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_selection_enabled**()

If `true`, the label allows text selection.

---

[bool](class_bool.md#class-bool) **shortcut_keys_enabled** = `true`

-  **set_shortcut_keys_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_shortcut_keys_enabled**()

If `true`, shortcut keys for context menu items are enabled, even if the context menu is disabled.

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

[int](class_int.md#class-int) **tab_size** = `4`

-  **set_tab_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_tab_size**()

The number of spaces associated with a single tab length. Does not affect `\t` in text tags, only indent tags.

---

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **tab_stops** = `PackedFloat32Array()`

-  **set_tab_stops**(value: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))
- [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_tab_stops**()

Aligns text to the given tab-stops.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) for more details.

---

[String](class_string.md#class-string) **text** = `""`

-  **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

The label's text in BBCode format. Is not representative of manual modifications to the internal tag stack. Erases changes made by other methods when edited.

**Note:** If bbcode_enabled is `true`, it is unadvised to use the `+=` operator with text (e.g. `text += "some string"`) as it replaces the whole text and can cause slowdowns. It will also erase all BBCode that was added to stack using `push_*` methods. Use append_text() for adding text instead, unless you absolutely need to close a tag that was opened in an earlier method call.

---

[TextDirection](class_control.md#enum-control-textdirection) **text_direction** = `0`

-  **set_text_direction**(value: [TextDirection](class_control.md#enum-control-textdirection))
- [TextDirection](class_control.md#enum-control-textdirection) **get_text_direction**()

Base text writing direction.

---

[bool](class_bool.md#class-bool) **threaded** = `false`

-  **set_threaded**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_threaded**()

If `true`, text processing is done in a background thread.

---

[VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **vertical_alignment** = `0`

-  **set_vertical_alignment**(value: [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment))
- [VerticalAlignment](class_@globalscope.md#enum-globalscope-verticalalignment) **get_vertical_alignment**()

Controls the text's vertical alignment. Supports top, center, bottom, and fill.

---

[int](class_int.md#class-int) **visible_characters** = `-1`

-  **set_visible_characters**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_visible_characters**()

The number of characters to display. If set to `-1`, all characters are displayed. This can be useful when animating the text appearing in a dialog box.

**Note:** Setting this property updates visible_ratio accordingly.

**Note:** Characters are counted as Unicode codepoints. A single visible grapheme may contain multiple codepoints (e.g. certain emoji use three codepoints). A single codepoint may contain two UTF-16 characters, which are used in C# strings.

---

[VisibleCharactersBehavior](class_textserver.md#enum-textserver-visiblecharactersbehavior) **visible_characters_behavior** = `0`

-  **set_visible_characters_behavior**(value: [VisibleCharactersBehavior](class_textserver.md#enum-textserver-visiblecharactersbehavior))
- [VisibleCharactersBehavior](class_textserver.md#enum-textserver-visiblecharactersbehavior) **get_visible_characters_behavior**()

The clipping behavior when visible_characters or visible_ratio is set.

---

[float](class_float.md#class-float) **visible_ratio** = `1.0`

-  **set_visible_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_visible_ratio**()

The fraction of characters to display, relative to the total number of characters (see get_total_character_count()). If set to `1.0`, all characters are displayed. If set to `0.5`, only half of the characters will be displayed. This can be useful when animating the text appearing in a dialog box.

**Note:** Setting this property updates visible_characters accordingly.

---

## Method Descriptions

 **add_hr**(width: [int](class_int.md#class-int) = 90, height: [int](class_int.md#class-int) = 2, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) = 1, width_in_percent: [bool](class_bool.md#class-bool) = true, height_in_percent: [bool](class_bool.md#class-bool) = false)

Adds a horizontal rule that can be used to separate content.

If `width_in_percent` is set, `width` values are percentages of the control width instead of pixels.

If `height_in_percent` is set, `height` values are percentages of the control width instead of pixels.

---

 **add_image**(image: [Texture2D](class_texture2d.md#class-texture2d), width: [float](class_float.md#class-float) = 0, height: [float](class_float.md#class-float) = 0, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, region: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), key: [Variant](class_variant.md#class-variant) = null, pad: [bool](class_bool.md#class-bool) = false, tooltip: [String](class_string.md#class-string) = "", width_unit: ImageUnit = 0, height_unit: ImageUnit = 0, alt_text: [String](class_string.md#class-string) = "")

Adds an image's opening and closing tags to the tag stack, optionally providing a `width` and `height` to resize the image, a `color` to tint the image and a `region` to only use parts of the image.

If `width` or `height` is set to 0, the image size will be adjusted in order to keep the original aspect ratio.

If `width` and `height` are not set, but `region` is, the region's rect will be used.

`key` is an optional identifier, that can be used to modify the image via update_image().

If `pad` is set, and the image is smaller than the size specified by `width` and `height`, the image padding is added to match the size instead of upscaling.

Parameters `width_unit` and `height_unit` determine the units used to calculate the image width and height, respectively.

`alt_text` is used as the image description for assistive apps.

---

 **add_text**(text: [String](class_string.md#class-string))

Adds raw non-BBCode-parsed text to the tag stack.

---

 **append_text**(bbcode: [String](class_string.md#class-string))

Parses `bbcode` and adds tags to the tag stack as needed.

**Note:** Using this method, you can't close a tag that was opened in a previous append_text() call. This is done to improve performance, especially when updating large RichTextLabels since rebuilding the whole BBCode every time would be slower. If you absolutely need to close a tag in a future method call, append the text instead of using append_text().

---

 **clear**()

Clears the tag stack, causing the label to display nothing.

**Note:** This method does not affect text, and its contents will show again if the label is redrawn. However, setting text to an empty [String](class_string.md#class-string) also clears the stack.

---

 **deselect**()

Clears the current selection.

---

[int](class_int.md#class-int) **get_character_line**(character: [int](class_int.md#class-int))

Returns the line number of the character position provided. Line and character numbers are both zero-indexed.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[int](class_int.md#class-int) **get_character_paragraph**(character: [int](class_int.md#class-int))

Returns the paragraph number of the character position provided. Paragraph and character numbers are both zero-indexed.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[int](class_int.md#class-int) **get_content_height**()

Returns the height of the content.

**Note:** This method always returns the full content size, and is not affected by visible_ratio and visible_characters. To get the visible content size, use get_visible_content_rect().

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[int](class_int.md#class-int) **get_content_width**()

Returns the width of the content.

**Note:** This method always returns the full content size, and is not affected by visible_ratio and visible_characters. To get the visible content size, use get_visible_content_rect().

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[int](class_int.md#class-int) **get_line_count**()

Returns the total number of lines in the text. Wrapped text is counted as multiple lines.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[int](class_int.md#class-int) **get_line_height**(line: [int](class_int.md#class-int))

Returns the height of the line found at the provided index.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether the document is fully loaded.

---

[float](class_float.md#class-float) **get_line_offset**(line: [int](class_int.md#class-int))

Returns the vertical offset of the line found at the provided index.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_line_range**(line: [int](class_int.md#class-int))

Returns the indexes of the first and last visible characters for the given `line`, as a [Vector2i](class_vector2i.md#class-vector2i).

**Note:** If visible_characters_behavior is set to [TextServer.VC_CHARS_BEFORE_SHAPING](class_textserver.md#class-textserver-constant-vc-chars-before-shaping) only visible wrapped lines are counted.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[int](class_int.md#class-int) **get_line_width**(line: [int](class_int.md#class-int))

Returns the width of the line found at the provided index.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether the document is fully loaded.

---

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_menu**()

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) of this **RichTextLabel**. By default, this menu is displayed when right-clicking on the **RichTextLabel**.

You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (see MenuItems). For example:

GDScript

```gdscript
func _ready():
    var menu = get_menu()
    # Remove "Select All" item.
    menu.remove_item(MENU_SELECT_ALL)
    # Add custom items.
    menu.add_separator()
    menu.add_item("Duplicate Text", MENU_MAX + 1)
    # Connect callback.
    menu.id_pressed.connect(_on_item_pressed)

func _on_item_pressed(id):
    if id == MENU_MAX + 1:
        add_text("\n" + get_parsed_text())
```

C#

```csharp
public override void _Ready()
{
    var menu = GetMenu();
    // Remove "Select All" item.
    menu.RemoveItem(RichTextLabel.MenuItems.SelectAll);
    // Add custom items.
    menu.AddSeparator();
    menu.AddItem("Duplicate Text", RichTextLabel.MenuItems.Max + 1);
    // Add event handler.
    menu.IdPressed += OnItemPressed;
}

public void OnItemPressed(int id)
{
    if (id == TextEdit.MenuItems.Max + 1)
    {
        AddText("\n" + GetParsedText());
    }
}
```

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---

[int](class_int.md#class-int) **get_paragraph_count**()

Returns the total number of paragraphs (newlines or `p` tags in the tag stack's text tags). Considers wrapped text as one paragraph.

---

[float](class_float.md#class-float) **get_paragraph_offset**(paragraph: [int](class_int.md#class-int))

Returns the vertical offset of the paragraph found at the provided index.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[String](class_string.md#class-string) **get_parsed_text**()

Returns the text without BBCode mark-up.

---

[String](class_string.md#class-string) **get_selected_text**()

Returns the current selection text. Does not include BBCodes.

---

[int](class_int.md#class-int) **get_selection_from**()

Returns the current selection first character index if a selection is active, `-1` otherwise. Does not include BBCodes.

---

[float](class_float.md#class-float) **get_selection_line_offset**()

Returns the current selection vertical line offset if a selection is active, `-1.0` otherwise.

---

[int](class_int.md#class-int) **get_selection_to**()

Returns the current selection last character index if a selection is active, `-1` otherwise. Does not include BBCodes.

---

[int](class_int.md#class-int) **get_total_character_count**()

Returns the total number of characters from text tags. Does not include BBCodes.

---

[VScrollBar](class_vscrollbar.md#class-vscrollbar) **get_v_scroll_bar**()

Returns the vertical scrollbar.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

[Rect2i](class_rect2i.md#class-rect2i) **get_visible_content_rect**()

Returns the bounding rectangle of the visible content.

**Note:** This method returns a correct value only after the label has been drawn.

GDScript

```gdscript
extends RichTextLabel

@export var background_panel: Panel

func _ready():
    await draw
    background_panel.position = get_visible_content_rect().position
    background_panel.size = get_visible_content_rect().size
```

C#

```csharp
public partial class TestLabel : RichTextLabel
{
    [Export]
    public Panel BackgroundPanel { get; set; }

    public override async void _Ready()
    {
        await ToSignal(this, Control.SignalName.Draw);
        BackgroundGPanel.Position = GetVisibleContentRect().Position;
        BackgroundPanel.Size = GetVisibleContentRect().Size;
    }
}
```

---

[int](class_int.md#class-int) **get_visible_line_count**()

Returns the number of visible lines.

**Note:** This method returns a correct value only after the label has been drawn.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

[int](class_int.md#class-int) **get_visible_paragraph_count**()

Returns the number of visible paragraphs. A paragraph is considered visible if at least one of its lines is visible.

**Note:** This method returns a correct value only after the label has been drawn.

**Note:** If threaded is enabled, this method returns a value for the loaded part of the document. Use is_finished() or finished to determine whether document is fully loaded.

---

 **install_effect**(effect: [Variant](class_variant.md#class-variant))

Installs a custom effect. This can also be done in the Inspector through the custom_effects property. `effect` should be a valid [RichTextEffect](class_richtexteffect.md#class-richtexteffect).

**Example:** With the following script extending from [RichTextEffect](class_richtexteffect.md#class-richtexteffect):

```gdscript
# effect.gd
class_name MyCustomEffect
extends RichTextEffect

var bbcode = "my_custom_effect"

# ...
```

The above effect can be installed in **RichTextLabel** from a script:

```gdscript
# rich_text_label.gd
extends RichTextLabel

func _ready():
    install_effect(MyCustomEffect.new())

    # Alternatively, if not using `class_name` in the script that extends RichTextEffect:
    install_effect(preload("res://effect.gd").new())
```

---

[bool](class_bool.md#class-bool) **invalidate_paragraph**(paragraph: [int](class_int.md#class-int))

Invalidates `paragraph` and all subsequent paragraphs cache.

---

[bool](class_bool.md#class-bool) **is_finished**()

If threaded is enabled, returns `true` if the background thread has finished text processing, otherwise always return `true`.

---

[bool](class_bool.md#class-bool) **is_menu_visible**()

Returns whether the menu is visible. Use this instead of `get_menu().visible` to improve performance (so the creation of the menu is avoided).

---

[bool](class_bool.md#class-bool) **is_ready**()

**Deprecated:** Use is_finished() instead.

If threaded is enabled, returns `true` if the background thread has finished text processing, otherwise always return `true`.

---

 **menu_option**(option: [int](class_int.md#class-int))

Executes a given action as defined in the MenuItems enum.

---

 **newline**()

Adds a newline tag to the tag stack.

---

 **parse_bbcode**(bbcode: [String](class_string.md#class-string))

The assignment version of append_text(). Clears the tag stack and inserts the new content.

---

[Dictionary](class_dictionary.md#class-dictionary) **parse_expressions_for_values**(expressions: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Parses BBCode parameter `expressions` into a dictionary.

---

 **pop**()

Terminates the current tag. Use after `push_*` methods to close BBCodes manually. Does not need to follow `add_*` methods.

---

 **pop_all**()

Terminates all tags opened by `push_*` methods.

---

 **pop_context**()

Terminates tags opened after the last push_context() call (including context marker), or all tags if there's no context marker on the stack.

---

 **push_bgcolor**(bgcolor: [Color](class_color.md#class-color))

Adds a `[bgcolor]` tag to the tag stack.

**Note:** The background color has padding applied by default, which is controlled using text_highlight_h_padding and text_highlight_v_padding. This can lead to overlapping highlights if background colors are placed on neighboring lines/columns, so consider setting those theme items to `0` if you want to avoid this.

---

 **push_bold**()

Adds a `[font]` tag with a bold font to the tag stack. This is the same as adding a `[b]` tag if not currently in a `[i]` tag.

---

 **push_bold_italics**()

Adds a `[font]` tag with a bold italics font to the tag stack.

---

 **push_cell**()

Adds a `[cell]` tag to the tag stack. Must be inside a `[table]` tag. See push_table() for details. Use set_table_column_expand() to set column expansion ratio, set_cell_border_color() to set cell border, set_cell_row_background_color() to set cell background, set_cell_size_override() to override cell size, and set_cell_padding() to set padding.

---

 **push_color**(color: [Color](class_color.md#class-color))

Adds a `[color]` tag to the tag stack.

---

 **push_context**()

Adds a context marker to the tag stack. See pop_context().

---

 **push_customfx**(effect: [RichTextEffect](class_richtexteffect.md#class-richtexteffect), env: [Dictionary](class_dictionary.md#class-dictionary))

Adds a custom effect tag to the tag stack. The effect does not need to be in custom_effects. The environment is directly passed to the effect.

---

 **push_dropcap**(string: [String](class_string.md#class-string), font: [Font](class_font.md#class-font), size: [int](class_int.md#class-int), dropcap_margins: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), outline_size: [int](class_int.md#class-int) = 0, outline_color: [Color](class_color.md#class-color) = Color(0, 0, 0, 0))

Adds a `[dropcap]` tag to the tag stack. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.

---

 **push_fgcolor**(fgcolor: [Color](class_color.md#class-color))

Adds a `[fgcolor]` tag to the tag stack.

**Note:** The foreground color has padding applied by default, which is controlled using text_highlight_h_padding and text_highlight_v_padding. This can lead to overlapping highlights if foreground colors are placed on neighboring lines/columns, so consider setting those theme items to `0` if you want to avoid this.

---

 **push_font**(font: [Font](class_font.md#class-font), font_size: [int](class_int.md#class-int) = 0)

Adds a `[font]` tag to the tag stack. Overrides default fonts for its duration.

Passing `0` to `font_size` will use the existing default font size.

---

 **push_font_size**(font_size: [int](class_int.md#class-int))

Adds a `[font_size]` tag to the tag stack. Overrides default font size for its duration.

---

 **push_hint**(description: [String](class_string.md#class-string))

Adds a `[hint]` tag to the tag stack. Same as BBCode `[hint=something]{text}[/hint]`.

---

 **push_indent**(level: [int](class_int.md#class-int))

Adds an `[indent]` tag to the tag stack. Multiplies `level` by current tab_size to determine new margin length.

---

 **push_italics**()

Adds a `[font]` tag with an italics font to the tag stack. This is the same as adding an `[i]` tag if not currently in a `[b]` tag.

---

 **push_language**(language: [String](class_string.md#class-string))

Adds language code used for text shaping algorithm and Open-Type font features.

---

 **push_list**(level: [int](class_int.md#class-int), type: ListType, capitalize: [bool](class_bool.md#class-bool), bullet: [String](class_string.md#class-string) = "•")

Adds `[ol]` or `[ul]` tag to the tag stack. Multiplies `level` by current tab_size to determine new margin length.

---

 **push_meta**(data: [Variant](class_variant.md#class-variant), underline_mode: MetaUnderline = 1, tooltip: [String](class_string.md#class-string) = "")

Adds a meta tag to the tag stack. Similar to the BBCode `[url=something]{text}[/url]`, but supports non-[String](class_string.md#class-string) metadata types.

If meta_underlined is `true`, meta tags display an underline. This behavior can be customized with `underline_mode`.

**Note:** Meta tags do nothing by default when clicked. To assign behavior when clicked, connect meta_clicked to a function that is called when the meta tag is clicked.

---

 **push_mono**()

Adds a `[font]` tag with a monospace font to the tag stack.

---

 **push_normal**()

Adds a `[font]` tag with a normal font to the tag stack.

---

 **push_outline_color**(color: [Color](class_color.md#class-color))

Adds a `[outline_color]` tag to the tag stack. Adds text outline for its duration.

---

 **push_outline_size**(outline_size: [int](class_int.md#class-int))

Adds a `[outline_size]` tag to the tag stack. Overrides default text outline size for its duration.

---

 **push_paragraph**(alignment: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment), base_direction: [TextDirection](class_control.md#enum-control-textdirection) = 0, language: [String](class_string.md#class-string) = "", st_parser: [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) = 0, justification_flags: [[JustificationFlag](class_textserver.md#enum-textserver-justificationflag)] = 163, tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) = PackedFloat32Array())

Adds a `[p]` tag to the tag stack.

---

 **push_strikethrough**(color: [Color](class_color.md#class-color) = Color(0, 0, 0, 0))

Adds a `[s]` tag to the tag stack. If `color`'s alpha value is `0.0`, the current font's color with its alpha multiplied by strikethrough_alpha is used.

---

 **push_table**(columns: [int](class_int.md#class-int), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 0, align_to_row: [int](class_int.md#class-int) = -1, name: [String](class_string.md#class-string) = "")

Adds a `[table=columns,inline_align]` tag to the tag stack. Use set_table_column_expand() to set column expansion ratio. Use push_cell() to add cells. `name` is used as the table name for assistive apps.

---

 **push_underline**(color: [Color](class_color.md#class-color) = Color(0, 0, 0, 0))

Adds a `[u]` tag to the tag stack. If `color`'s alpha value is `0.0`, the current font's color with its alpha multiplied by underline_alpha is used.

---

 **reload_effects**()

Reloads custom effects. Useful when custom_effects is modified manually.

---

[bool](class_bool.md#class-bool) **remove_paragraph**(paragraph: [int](class_int.md#class-int), no_invalidate: [bool](class_bool.md#class-bool) = false)

Removes a paragraph of content from the label. Returns `true` if the paragraph exists.

The `paragraph` argument is the index of the paragraph to remove, it can take values in the interval `[0, get_paragraph_count() - 1]`.

If `no_invalidate` is set to `true`, cache for the subsequent paragraphs is not invalidated. Use it for faster updates if deleted paragraph is fully self-contained (have no unclosed tags), or this call is part of the complex edit operation and invalidate_paragraph() will be called at the end of operation.

---

 **scroll_to_line**(line: [int](class_int.md#class-int))

Scrolls the window's top line to match `line`.

---

 **scroll_to_paragraph**(paragraph: [int](class_int.md#class-int))

Scrolls the window's top line to match first line of the `paragraph`.

---

 **scroll_to_selection**()

Scrolls to the beginning of the current selection.

---

 **select_all**()

Select all the text.

If selection_enabled is `false`, no selection will occur.

---

 **set_cell_border_color**(color: [Color](class_color.md#class-color))

Sets color of a table cell border.

---

 **set_cell_padding**(padding: [Rect2](class_rect2.md#class-rect2))

Sets inner padding of a table cell.

---

 **set_cell_row_background_color**(odd_row_bg: [Color](class_color.md#class-color), even_row_bg: [Color](class_color.md#class-color))

Sets color of a table cell. Separate colors for alternating rows can be specified.

---

 **set_cell_size_override**(min_size: [Vector2](class_vector2.md#class-vector2), max_size: [Vector2](class_vector2.md#class-vector2))

Sets minimum and maximum size overrides for a table cell.

---

 **set_table_column_expand**(column: [int](class_int.md#class-int), expand: [bool](class_bool.md#class-bool), ratio: [int](class_int.md#class-int) = 1, shrink: [bool](class_bool.md#class-bool) = true)

Edits the selected column's expansion options. If `expand` is `true`, the column expands in proportion to its expansion ratio versus the other columns' ratios.

For example, 2 columns with ratios 3 and 4 plus 70 pixels in available width would expand 30 and 40 pixels, respectively.

If `expand` is `false`, the column will not contribute to the total ratio.

---

 **set_table_column_name**(column: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets table column name for assistive apps.

---

 **update_image**(key: [Variant](class_variant.md#class-variant), mask: [ImageUpdateMask], image: [Texture2D](class_texture2d.md#class-texture2d), width: [float](class_float.md#class-float) = 0, height: [float](class_float.md#class-float) = 0, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), inline_align: [InlineAlignment](class_@globalscope.md#enum-globalscope-inlinealignment) = 5, region: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), pad: [bool](class_bool.md#class-bool) = false, tooltip: [String](class_string.md#class-string) = "", width_unit: ImageUnit = 0, height_unit: ImageUnit = 0)

Updates the existing images with the key `key`. Only properties specified by `mask` bits are updated. See add_image().

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **default_color** = `Color(1, 1, 1, 1)`

The default text color.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The default tint of text outline.

---

[Color](class_color.md#class-color) **font_selected_color** = `Color(0, 0, 0, 0)`

The color of selected text, used when selection_enabled is `true`. If equal to `Color(0, 0, 0, 0)`, it will be ignored.

---

[Color](class_color.md#class-color) **font_shadow_color** = `Color(0, 0, 0, 0)`

The color of the font's shadow.

---

[Color](class_color.md#class-color) **selection_color** = `Color(0.1, 0.1, 1, 0.8)`

The color of the selection box.

---

[Color](class_color.md#class-color) **table_border** = `Color(0, 0, 0, 0)`

The default cell border color.

---

[Color](class_color.md#class-color) **table_even_row_bg** = `Color(0, 0, 0, 0)`

The default background color for even rows.

---

[Color](class_color.md#class-color) **table_odd_row_bg** = `Color(0, 0, 0, 0)`

The default background color for odd rows.

---

[int](class_int.md#class-int) **line_separation** = `0`

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[int](class_int.md#class-int) **paragraph_separation** = `0`

Additional vertical spacing between paragraphs (in pixels). Spacing is added after the last line. This value can be negative.

---

[int](class_int.md#class-int) **shadow_offset_x** = `1`

The horizontal offset of the font's shadow.

---

[int](class_int.md#class-int) **shadow_offset_y** = `1`

The vertical offset of the font's shadow.

---

[int](class_int.md#class-int) **shadow_outline_size** = `1`

The size of the shadow outline.

---

[int](class_int.md#class-int) **strikethrough_alpha** = `50`

The default strikethrough color transparency (percent). For strikethroughs with a custom color, this theme item is only used if the custom color's alpha is `0.0` (fully transparent).

---

[int](class_int.md#class-int) **table_h_separation** = `3`

The horizontal separation of elements in a table.

---

[int](class_int.md#class-int) **table_v_separation** = `3`

The vertical separation of elements in a table.

---

[int](class_int.md#class-int) **text_highlight_h_padding** = `3`

The horizontal padding around boxes drawn by the `[fgcolor]` and `[bgcolor]` tags. This does not affect the appearance of text selection. To avoid any risk of neighboring highlights overlapping each other, set this to `0` to disable padding.

---

[int](class_int.md#class-int) **text_highlight_v_padding** = `3`

The vertical padding around boxes drawn by the `[fgcolor]` and `[bgcolor]` tags. This does not affect the appearance of text selection. To avoid any risk of neighboring highlights overlapping each other, set this to `0` to disable padding.

---

[int](class_int.md#class-int) **underline_alpha** = `50`

The default underline color transparency (percent). For underlines with a custom color, this theme item is only used if the custom color's alpha is `0.0` (fully transparent).

---

[Font](class_font.md#class-font) **bold_font**

The font used for bold text.

---

[Font](class_font.md#class-font) **bold_italics_font**

The font used for bold italics text.

---

[Font](class_font.md#class-font) **italics_font**

The font used for italics text.

---

[Font](class_font.md#class-font) **mono_font**

The font used for monospace text.

---

[Font](class_font.md#class-font) **normal_font**

The default text font.

---

[int](class_int.md#class-int) **bold_font_size**

The font size used for bold text.

---

[int](class_int.md#class-int) **bold_italics_font_size**

The font size used for bold italics text.

---

[int](class_int.md#class-int) **italics_font_size**

The font size used for italics text.

---

[int](class_int.md#class-int) **mono_font_size**

The font size used for monospace text.

---

[int](class_int.md#class-int) **normal_font_size**

The default text font size.

---

[Texture2D](class_texture2d.md#class-texture2d) **horizontal_rule**

The horizontal rule texture.

---

[StyleBox](class_stylebox.md#class-stylebox) **focus**

The background used when the **RichTextLabel** is focused. The focus [StyleBox](class_stylebox.md#class-stylebox) is displayed *over* the base [StyleBox](class_stylebox.md#class-stylebox), so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the base [StyleBox](class_stylebox.md#class-stylebox) remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

[StyleBox](class_stylebox.md#class-stylebox) **normal**

The normal background for the **RichTextLabel**.
