# TextEdit

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [CodeEdit](class_codeedit.md#class-codeedit)

A multiline text editor.

## Description

A multiline text editor. It also has limited facilities for editing code, such as syntax highlighting support. For more advanced facilities for editing code, see [CodeEdit](class_codeedit.md#class-codeedit).

While entering text, it is possible to insert special characters using Unicode, OEM or Windows alt codes:

- To enter Unicode codepoints, hold `Alt` and type the codepoint on the numpad. For example, to enter the character `á` (U+00E1), hold `Alt` and type `+E1` on the numpad (the leading zeroes can be omitted).
- To enter OEM codepoints, hold `Alt` and type the code on the numpad. For example, to enter the character `á` (OEM 160), hold `Alt` and type `160` on the numpad.
- To enter Windows codepoints, hold `Alt` and type the code on the numpad. For example, to enter the character `á` (Windows 0225), hold `Alt` and type `0`, `2`, `2`, `5` on the numpad. The leading zero here must **not** be omitted, as this is how Windows codepoints are distinguished from OEM codepoints.

**Note:** Most viewport, caret, and edit methods contain a `caret_index` argument for caret_multiple support. The argument should be one of the following: `-1` for all carets, `0` for the main caret, or greater than `0` for secondary carets in the order they were created.

**Note:** When holding down `Alt`, the vertical scroll wheel will scroll 5 times as fast as it would normally do. This also works in the Godot script editor.

## Properties

| [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode)                 | autowrap_mode                                                                 | `3`                                                                                           |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                 | backspace_deletes_composite_character_enabled | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | caret_blink                                                                     | `false`                                                                                       |
| [float](class_float.md#class-float)                                              | caret_blink_interval                                                   | `0.65`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | caret_draw_when_editable_disabled                         | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | caret_mid_grapheme                                                       | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | caret_move_on_right_click                                         | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | caret_multiple                                                               | `true`                                                                                        |
| CaretType                                            | caret_type                                                                       | `0`                                                                                           |
| [bool](class_bool.md#class-bool)                                                 | context_menu_enabled                                                   | `true`                                                                                        |
| [String](class_string.md#class-string)                                           | custom_word_separators                                               | `""`                                                                                          |
| [bool](class_bool.md#class-bool)                                                 | deselect_on_focus_loss_enabled                               | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | drag_and_drop_selection_enabled                             | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | draw_control_chars                                                       | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | draw_spaces                                                                     | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | draw_tabs                                                                         | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | editable                                                                           | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | emoji_menu_enabled                                                       | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | empty_selection_clipboard_enabled                         | `true`                                                                                        |
| [FocusMode](class_control.md#enum-control-focusmode)                             | focus_mode                                                                                                              | `2` (overrides [Control](class_control.md#class-control-property-focus-mode))                 |
| [bool](class_bool.md#class-bool)                                                 | highlight_all_occurrences                                         | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | highlight_current_line                                               | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | indent_wrapped_lines                                                   | `false`                                                                                       |
| [String](class_string.md#class-string)                                           | language                                                                           | `""`                                                                                          |
| [bool](class_bool.md#class-bool)                                                 | middle_mouse_paste_enabled                                       | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | minimap_draw                                                                   | `false`                                                                                       |
| [int](class_int.md#class-int)                                                    | minimap_width                                                                 | `80`                                                                                          |
| [CursorShape](class_control.md#enum-control-cursorshape)                         | mouse_default_cursor_shape                                                                                              | `1` (overrides [Control](class_control.md#class-control-property-mouse-default-cursor-shape)) |
| [String](class_string.md#class-string)                                           | placeholder_text                                                           | `""`                                                                                          |
| [bool](class_bool.md#class-bool)                                                 | scroll_fit_content_height                                         | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | scroll_fit_content_width                                           | `false`                                                                                       |
| [int](class_int.md#class-int)                                                    | scroll_horizontal                                                         | `0`                                                                                           |
| [bool](class_bool.md#class-bool)                                                 | scroll_past_end_of_file                                             | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | scroll_smooth                                                                 | `false`                                                                                       |
| [float](class_float.md#class-float)                                              | scroll_v_scroll_speed                                                 | `80.0`                                                                                        |
| [float](class_float.md#class-float)                                              | scroll_vertical                                                             | `0.0`                                                                                         |
| [bool](class_bool.md#class-bool)                                                 | selecting_enabled                                                         | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | shortcut_keys_enabled                                                 | `true`                                                                                        |
| [StructuredTextParser](class_textserver.md#enum-textserver-structuredtextparser) | structured_text_bidi_override                                 | `0`                                                                                           |
| [Array](class_array.md#class-array)                                              | structured_text_bidi_override_options                 | `[]`                                                                                          |
| [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter)          | syntax_highlighter                                                       |                                                                                               |
| [bool](class_bool.md#class-bool)                                                 | tab_input_mode                                                               | `true`                                                                                        |
| [String](class_string.md#class-string)                                           | text                                                                                   | `""`                                                                                          |
| [TextDirection](class_control.md#enum-control-textdirection)                     | text_direction                                                               | `0`                                                                                           |
| [bool](class_bool.md#class-bool)                                                 | use_custom_word_separators                                       | `false`                                                                                       |
| [bool](class_bool.md#class-bool)                                                 | use_default_word_separators                                     | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | virtual_keyboard_enabled                                           | `true`                                                                                        |
| [bool](class_bool.md#class-bool)                                                 | virtual_keyboard_show_on_focus                               | `true`                                                                                        |
| LineWrappingMode                              | wrap_mode                                                                         | `0`                                                                                           |

## Methods

|                                                                                   | \_backspace(caret_index: [int](class_int.md#class-int))                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                   | \_copy(caret_index: [int](class_int.md#class-int))                                                                                                                                                                                                                     |
|                                                                                   | \_cut(caret_index: [int](class_int.md#class-int))                                                                                                                                                                                                                       |
|                                                                                   | \_handle_unicode_input(unicode_char: [int](class_int.md#class-int), caret_index: [int](class_int.md#class-int))                                                                                                                                        |
|                                                                                   | \_paste(caret_index: [int](class_int.md#class-int))                                                                                                                                                                                                                   |
|                                                                                   | \_paste_primary_clipboard(caret_index: [int](class_int.md#class-int))                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                     | add_caret(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                                                                     |
|                                                                                   | add_caret_at_carets(below: [bool](class_bool.md#class-bool))                                                                                                                                                                                                    |
|                                                                                   | add_gutter(at: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                       |
|                                                                                   | add_selection_for_next_occurrence()                                                                                                                                                                                                               |
|                                                                                   | adjust_carets_after_edit(caret: [int](class_int.md#class-int), from_line: [int](class_int.md#class-int), from_col: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int), to_col: [int](class_int.md#class-int))                           |
|                                                                                   | adjust_viewport_to_caret(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                   |
|                                                                                   | apply_ime()                                                                                                                                                                                                                                                               |
|                                                                                   | backspace(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                |
|                                                                                   | begin_complex_operation()                                                                                                                                                                                                                                   |
|                                                                                   | begin_multicaret_edit()                                                                                                                                                                                                                                       |
|                                                                                   | cancel_ime()                                                                                                                                                                                                                                                             |
|                                                                                   | center_viewport_to_caret(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                   |
|                                                                                   | clear()                                                                                                                                                                                                                                                                       |
|                                                                                   | clear_undo_history()                                                                                                                                                                                                                                             |
|                                                                                   | collapse_carets(from_line: [int](class_int.md#class-int), from_column: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int), to_column: [int](class_int.md#class-int), inclusive: [bool](class_bool.md#class-bool) = false)                        |
|                                                                                   | copy(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                          |
|                                                                                   | cut(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                            |
|                                                                                   | delete_selection(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                  |
|                                                                                   | deselect(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                  |
|                                                                                   | end_action()                                                                                                                                                                                                                                                             |
|                                                                                   | end_complex_operation()                                                                                                                                                                                                                                       |
|                                                                                   | end_multicaret_edit()                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                     | get_caret_column(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                     | get_caret_count()                                                                                                                                                                                                                                                   |
| [Vector2](class_vector2.md#class-vector2)                                         | get_caret_draw_pos(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                               |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)              | get_caret_index_edit_order()                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                     | get_caret_line(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                     | get_caret_wrap_index(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                     | get_first_non_whitespace_column(line: [int](class_int.md#class-int))                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                     | get_first_visible_line()                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                     | get_gutter_count()                                                                                                                                                                                                                                                 |
| [String](class_string.md#class-string)                                            | get_gutter_name(gutter: [int](class_int.md#class-int))                                                                                                                                                                                                              |
| GutterType                                           | get_gutter_type(gutter: [int](class_int.md#class-int))                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                     | get_gutter_width(gutter: [int](class_int.md#class-int))                                                                                                                                                                                                            |
| [HScrollBar](class_hscrollbar.md#class-hscrollbar)                                | get_h_scroll_bar()                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_indent_level(line: [int](class_int.md#class-int))                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                     | get_last_full_visible_line()                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                     | get_last_full_visible_line_wrap_index()                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                     | get_last_unhidden_line()                                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)                                            | get_line(line: [int](class_int.md#class-int))                                                                                                                                                                                                                              |
| [Color](class_color.md#class-color)                                               | get_line_background_color(line: [int](class_int.md#class-int))                                                                                                                                                                                            |
| [Vector2i](class_vector2i.md#class-vector2i)                                      | get_line_column_at_pos(position: [Vector2i](class_vector2i.md#class-vector2i), clamp_line: [bool](class_bool.md#class-bool) = true, clamp_column: [bool](class_bool.md#class-bool) = true)                                                                   |
| [int](class_int.md#class-int)                                                     | get_line_count()                                                                                                                                                                                                                                                     |
| [Texture2D](class_texture2d.md#class-texture2d)                                   | get_line_gutter_icon(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))                                                                                                                                                               |
| [Color](class_color.md#class-color)                                               | get_line_gutter_item_color(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))                                                                                                                                                   |
| [Variant](class_variant.md#class-variant)                                         | get_line_gutter_metadata(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))                                                                                                                                                       |
| [String](class_string.md#class-string)                                            | get_line_gutter_text(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))                                                                                                                                                               |
| [int](class_int.md#class-int)                                                     | get_line_height()                                                                                                                                                                                                                                                   |
| [Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] | get_line_ranges_from_carets(only_selections: [bool](class_bool.md#class-bool) = false, merge_adjacent: [bool](class_bool.md#class-bool) = true)                                                                                                         |
| [int](class_int.md#class-int)                                                     | get_line_width(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                  |
| [String](class_string.md#class-string)                                            | get_line_with_ime(line: [int](class_int.md#class-int))                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                                     | get_line_wrap_count(line: [int](class_int.md#class-int))                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                     | get_line_wrap_index_at_column(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                             |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)           | get_line_wrapped_text(line: [int](class_int.md#class-int))                                                                                                                                                                                                    |
| [Vector2](class_vector2.md#class-vector2)                                         | get_local_mouse_pos()                                                                                                                                                                                                                                           |
| [PopupMenu](class_popupmenu.md#class-popupmenu)                                   | get_menu()                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_minimap_line_at_pos(position: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                     | get_minimap_visible_lines()                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                     | get_next_composite_character_column(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                 |
| [Vector2i](class_vector2i.md#class-vector2i)                                      | get_next_visible_line_index_offset_from(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int), visible_amount: [int](class_int.md#class-int))                                                                      |
| [int](class_int.md#class-int)                                                     | get_next_visible_line_offset_from(line: [int](class_int.md#class-int), visible_amount: [int](class_int.md#class-int))                                                                                                                             |
| [Vector2i](class_vector2i.md#class-vector2i)                                      | get_pos_at_line_column(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                                           |
| [int](class_int.md#class-int)                                                     | get_previous_composite_character_column(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                         |
| [Rect2i](class_rect2i.md#class-rect2i)                                            | get_rect_at_line_column(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                                         |
| [int](class_int.md#class-int)                                                     | get_saved_version()                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                               | get_scroll_pos_for_line(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = 0)                                                                                                                                                 |
| [String](class_string.md#class-string)                                            | get_selected_text(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                     | get_selection_at_line_column(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int), include_edges: [bool](class_bool.md#class-bool) = true, only_selections: [bool](class_bool.md#class-bool) = true)                             |
| [int](class_int.md#class-int)                                                     | get_selection_column(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                     | get_selection_from_column(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_selection_from_line(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                     | get_selection_line(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                               |
| SelectionMode                                     | get_selection_mode()                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                     | get_selection_origin_column(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                     | get_selection_origin_line(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_selection_to_column(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                     | get_selection_to_line(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                         |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)              | get_sorted_carets(include_ignored_carets: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                     | get_tab_size()                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                     | get_total_gutter_width()                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                     | get_total_visible_line_count()                                                                                                                                                                                                                         |
| [VScrollBar](class_vscrollbar.md#class-vscrollbar)                                | get_v_scroll_bar()                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                     | get_version()                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                     | get_visible_line_count()                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                     | get_visible_line_count_in_range(from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))                                                                                                                                   |
| [String](class_string.md#class-string)                                            | get_word_at_pos(position: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                |
| [String](class_string.md#class-string)                                            | get_word_under_caret(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                  | has_ime_text()                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                  | has_redo()                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                  | has_selection(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                  | has_undo()                                                                                                                                                                                                                                                                 |
|                                                                                   | insert_line_at(line: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                                                                                                                    |
|                                                                                   | insert_text(text: [String](class_string.md#class-string), line: [int](class_int.md#class-int), column: [int](class_int.md#class-int), before_selection_begin: [bool](class_bool.md#class-bool) = true, before_selection_end: [bool](class_bool.md#class-bool) = false)  |
|                                                                                   | insert_text_at_caret(text: [String](class_string.md#class-string), caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                  | is_caret_after_selection_origin(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                  | is_caret_visible(caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                  | is_dragging_cursor()                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                  | is_gutter_clickable(gutter: [int](class_int.md#class-int))                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                  | is_gutter_drawn(gutter: [int](class_int.md#class-int))                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                  | is_gutter_overwritable(gutter: [int](class_int.md#class-int))                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                  | is_in_mulitcaret_edit()                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                  | is_line_gutter_clickable(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                  | is_line_in_viewport(line: [int](class_int.md#class-int))                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                  | is_line_wrapped(line: [int](class_int.md#class-int))                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                  | is_menu_visible()                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                  | is_mouse_over_selection(edges: [bool](class_bool.md#class-bool), caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                  | is_overtype_mode_enabled()                                                                                                                                                                                                                                 |
|                                                                                   | menu_option(option: [int](class_int.md#class-int))                                                                                                                                                                                                                      |
|                                                                                   | merge_gutters(from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))                                                                                                                                                                       |
|                                                                                   | merge_overlapping_carets()                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                  | multicaret_edit_ignore_caret(caret_index: [int](class_int.md#class-int))                                                                                                                                                                               |
|                                                                                   | paste(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                        |
|                                                                                   | paste_primary_clipboard(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                    |
|                                                                                   | redo()                                                                                                                                                                                                                                                                         |
|                                                                                   | remove_caret(caret: [int](class_int.md#class-int))                                                                                                                                                                                                                     |
|                                                                                   | remove_gutter(gutter: [int](class_int.md#class-int))                                                                                                                                                                                                                  |
|                                                                                   | remove_line_at(line: [int](class_int.md#class-int), move_carets_down: [bool](class_bool.md#class-bool) = true)                                                                                                                                                       |
|                                                                                   | remove_secondary_carets()                                                                                                                                                                                                                                   |
|                                                                                   | remove_text(from_line: [int](class_int.md#class-int), from_column: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int), to_column: [int](class_int.md#class-int))                                                                                     |
| [Vector2i](class_vector2i.md#class-vector2i)                                      | search(text: [String](class_string.md#class-string), flags: [int](class_int.md#class-int), from_line: [int](class_int.md#class-int), from_column: [int](class_int.md#class-int))                                                                                             |
|                                                                                   | select(origin_line: [int](class_int.md#class-int), origin_column: [int](class_int.md#class-int), caret_line: [int](class_int.md#class-int), caret_column: [int](class_int.md#class-int), caret_index: [int](class_int.md#class-int) = 0)                                     |
|                                                                                   | select_all()                                                                                                                                                                                                                                                             |
|                                                                                   | select_word_under_caret(caret_index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                    |
|                                                                                   | set_caret_column(column: [int](class_int.md#class-int), adjust_viewport: [bool](class_bool.md#class-bool) = true, caret_index: [int](class_int.md#class-int) = 0)                                                                                                  |
|                                                                                   | set_caret_line(line: [int](class_int.md#class-int), adjust_viewport: [bool](class_bool.md#class-bool) = true, can_be_hidden: [bool](class_bool.md#class-bool) = true, wrap_index: [int](class_int.md#class-int) = 0, caret_index: [int](class_int.md#class-int) = 0) |
|                                                                                   | set_gutter_clickable(gutter: [int](class_int.md#class-int), clickable: [bool](class_bool.md#class-bool))                                                                                                                                                       |
|                                                                                   | set_gutter_custom_draw(column: [int](class_int.md#class-int), draw_callback: [Callable](class_callable.md#class-callable))                                                                                                                                   |
|                                                                                   | set_gutter_draw(gutter: [int](class_int.md#class-int), draw: [bool](class_bool.md#class-bool))                                                                                                                                                                      |
|                                                                                   | set_gutter_name(gutter: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                                                                                                                |
|                                                                                   | set_gutter_overwritable(gutter: [int](class_int.md#class-int), overwritable: [bool](class_bool.md#class-bool))                                                                                                                                              |
|                                                                                   | set_gutter_type(gutter: [int](class_int.md#class-int), type: GutterType)                                                                                                                                                               |
|                                                                                   | set_gutter_width(gutter: [int](class_int.md#class-int), width: [int](class_int.md#class-int))                                                                                                                                                                      |
|                                                                                   | set_line(line: [int](class_int.md#class-int), new_text: [String](class_string.md#class-string))                                                                                                                                                                            |
|                                                                                   | set_line_as_center_visible(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = 0)                                                                                                                                           |
|                                                                                   | set_line_as_first_visible(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = 0)                                                                                                                                             |
|                                                                                   | set_line_as_last_visible(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = 0)                                                                                                                                               |
|                                                                                   | set_line_background_color(line: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                |
|                                                                                   | set_line_gutter_clickable(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), clickable: [bool](class_bool.md#class-bool))                                                                                                        |
|                                                                                   | set_line_gutter_icon(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                        |
|                                                                                   | set_line_gutter_item_color(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                       |
|                                                                                   | set_line_gutter_metadata(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))                                                                                                  |
|                                                                                   | set_line_gutter_text(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                                                                 |
|                                                                                   | set_overtype_mode_enabled(enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                      |
|                                                                                   | set_search_flags(flags: [int](class_int.md#class-int))                                                                                                                                                                                                             |
|                                                                                   | set_search_text(search_text: [String](class_string.md#class-string))                                                                                                                                                                                                |
|                                                                                   | set_selection_mode(mode: SelectionMode)                                                                                                                                                                                          |
|                                                                                   | set_selection_origin_column(column: [int](class_int.md#class-int), caret_index: [int](class_int.md#class-int) = 0)                                                                                                                                      |
|                                                                                   | set_selection_origin_line(line: [int](class_int.md#class-int), can_be_hidden: [bool](class_bool.md#class-bool) = true, wrap_index: [int](class_int.md#class-int) = -1, caret_index: [int](class_int.md#class-int) = 0)                                    |
|                                                                                   | set_tab_size(size: [int](class_int.md#class-int))                                                                                                                                                                                                                      |
|                                                                                   | set_tooltip_request_func(callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                           |
|                                                                                   | skip_selection_for_next_occurrence()                                                                                                                                                                                                             |
|                                                                                   | start_action(action: EditAction)                                                                                                                                                                                                          |
|                                                                                   | swap_lines(from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))                                                                                                                                                                             |
|                                                                                   | tag_saved_version()                                                                                                                                                                                                                                               |
|                                                                                   | undo()                                                                                                                                                                                                                                                                         |

## Theme Properties

| [Color](class_color.md#class-color)             | background_color                     | `Color(0, 0, 0, 0)`               |
|-------------------------------------------------|--------------------------------------------------------------------------------------|-----------------------------------|
| [Color](class_color.md#class-color)             | caret_background_color         | `Color(0, 0, 0, 1)`               |
| [Color](class_color.md#class-color)             | caret_color                               | `Color(0.875, 0.875, 0.875, 1)`   |
| [Color](class_color.md#class-color)             | current_line_color                 | `Color(0.25, 0.25, 0.26, 0.8)`    |
| [Color](class_color.md#class-color)             | font_color                                 | `Color(0.875, 0.875, 0.875, 1)`   |
| [Color](class_color.md#class-color)             | font_outline_color                 | `Color(0, 0, 0, 1)`               |
| [Color](class_color.md#class-color)             | font_placeholder_color         | `Color(0.875, 0.875, 0.875, 0.6)` |
| [Color](class_color.md#class-color)             | font_readonly_color               | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class-color)             | font_selected_color               | `Color(0, 0, 0, 0)`               |
| [Color](class_color.md#class-color)             | search_result_border_color | `Color(0.3, 0.3, 0.3, 0.4)`       |
| [Color](class_color.md#class-color)             | search_result_color               | `Color(0.3, 0.3, 0.3, 1)`         |
| [Color](class_color.md#class-color)             | selection_color                       | `Color(0.5, 0.5, 0.5, 1)`         |
| [Color](class_color.md#class-color)             | word_highlighted_color         | `Color(0.5, 0.5, 0.5, 0.25)`      |
| [int](class_int.md#class-int)                   | caret_width                            | `1`                               |
| [int](class_int.md#class-int)                   | line_spacing                          | `4`                               |
| [int](class_int.md#class-int)                   | outline_size                          | `0`                               |
| [int](class_int.md#class-int)                   | wrap_offset                            | `10`                              |
| [Font](class_font.md#class-font)                | font                                              |                                   |
| [int](class_int.md#class-int)                   | font_size                               |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | space                                            |                                   |
| [Texture2D](class_texture2d.md#class-texture2d) | tab                                                |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | focus                                           |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | normal                                         |                                   |
| [StyleBox](class_stylebox.md#class-stylebox)    | read_only                                   |                                   |

---

## Signals

**caret_changed**()

Emitted when any caret changes position.

---

**gutter_added**()

Emitted when a gutter is added.

---

**gutter_clicked**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))

Emitted when a gutter is clicked.

---

**gutter_removed**()

Emitted when a gutter is removed.

---

**lines_edited_from**(from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))

Emitted immediately when the text changes.

When text is added `from_line` will be less than `to_line`. On a remove `to_line` will be less than `from_line`.

---

**text_changed**()

Emitted when the text changes.

---

**text_set**()

Emitted when clear() is called or text is set.

---

## Enumerations

enum **MenuItems**:

MenuItems **MENU_CUT** = `0`

Cuts (copies and clears) the selected text.

MenuItems **MENU_COPY** = `1`

Copies the selected text.

MenuItems **MENU_PASTE** = `2`

Pastes the clipboard text over the selected text (or at the cursor's position).

MenuItems **MENU_CLEAR** = `3`

Erases the whole **TextEdit** text.

MenuItems **MENU_SELECT_ALL** = `4`

Selects the whole **TextEdit** text.

MenuItems **MENU_UNDO** = `5`

Undoes the previous action.

MenuItems **MENU_REDO** = `6`

Redoes the previous action.

MenuItems **MENU_SUBMENU_TEXT_DIR** = `7`

ID of "Text Writing Direction" submenu.

MenuItems **MENU_DIR_INHERITED** = `8`

Sets text direction to inherited.

MenuItems **MENU_DIR_AUTO** = `9`

Sets text direction to automatic.

MenuItems **MENU_DIR_LTR** = `10`

Sets text direction to left-to-right.

MenuItems **MENU_DIR_RTL** = `11`

Sets text direction to right-to-left.

MenuItems **MENU_DISPLAY_UCC** = `12`

Toggles control character display.

MenuItems **MENU_SUBMENU_INSERT_UCC** = `13`

ID of "Insert Control Character" submenu.

MenuItems **MENU_INSERT_LRM** = `14`

Inserts left-to-right mark (LRM) character.

MenuItems **MENU_INSERT_RLM** = `15`

Inserts right-to-left mark (RLM) character.

MenuItems **MENU_INSERT_LRE** = `16`

Inserts start of left-to-right embedding (LRE) character.

MenuItems **MENU_INSERT_RLE** = `17`

Inserts start of right-to-left embedding (RLE) character.

MenuItems **MENU_INSERT_LRO** = `18`

Inserts start of left-to-right override (LRO) character.

MenuItems **MENU_INSERT_RLO** = `19`

Inserts start of right-to-left override (RLO) character.

MenuItems **MENU_INSERT_PDF** = `20`

Inserts pop direction formatting (PDF) character.

MenuItems **MENU_INSERT_ALM** = `21`

Inserts Arabic letter mark (ALM) character.

MenuItems **MENU_INSERT_LRI** = `22`

Inserts left-to-right isolate (LRI) character.

MenuItems **MENU_INSERT_RLI** = `23`

Inserts right-to-left isolate (RLI) character.

MenuItems **MENU_INSERT_FSI** = `24`

Inserts first strong isolate (FSI) character.

MenuItems **MENU_INSERT_PDI** = `25`

Inserts pop direction isolate (PDI) character.

MenuItems **MENU_INSERT_ZWJ** = `26`

Inserts zero width joiner (ZWJ) character.

MenuItems **MENU_INSERT_ZWNJ** = `27`

Inserts zero width non-joiner (ZWNJ) character.

MenuItems **MENU_INSERT_WJ** = `28`

Inserts word joiner (WJ) character.

MenuItems **MENU_INSERT_SHY** = `29`

Inserts soft hyphen (SHY) character.

MenuItems **MENU_EMOJI_AND_SYMBOL** = `30`

Opens system emoji and symbol picker.

MenuItems **MENU_MAX** = `31`

Represents the size of the MenuItems enum.

---

enum **EditAction**:

EditAction **ACTION_NONE** = `0`

No current action.

EditAction **ACTION_TYPING** = `1`

A typing action.

EditAction **ACTION_BACKSPACE** = `2`

A backwards delete action.

EditAction **ACTION_DELETE** = `3`

A forward delete action.

---

enum **SearchFlags**:

SearchFlags **SEARCH_MATCH_CASE** = `1`

Match case when searching.

SearchFlags **SEARCH_WHOLE_WORDS** = `2`

Match whole words when searching.

SearchFlags **SEARCH_BACKWARDS** = `4`

Search from end to beginning.

---

enum **CaretType**:

CaretType **CARET_TYPE_LINE** = `0`

Vertical line caret.

CaretType **CARET_TYPE_BLOCK** = `1`

Block caret.

---

enum **SelectionMode**:

SelectionMode **SELECTION_MODE_NONE** = `0`

Not selecting.

SelectionMode **SELECTION_MODE_SHIFT** = `1`

Select as if `shift` is pressed.

SelectionMode **SELECTION_MODE_POINTER** = `2`

Select single characters as if the user single clicked.

SelectionMode **SELECTION_MODE_WORD** = `3`

Select whole words as if the user double clicked.

SelectionMode **SELECTION_MODE_LINE** = `4`

Select whole lines as if the user triple clicked.

---

enum **LineWrappingMode**:

LineWrappingMode **LINE_WRAPPING_NONE** = `0`

Line wrapping is disabled.

LineWrappingMode **LINE_WRAPPING_BOUNDARY** = `1`

Line wrapping occurs at the control boundary, beyond what would normally be visible.

---

enum **GutterType**:

GutterType **GUTTER_TYPE_STRING** = `0`

When a gutter is set to string using set_gutter_type(), it is used to contain text set via the set_line_gutter_text() method.

GutterType **GUTTER_TYPE_ICON** = `1`

When a gutter is set to icon using set_gutter_type(), it is used to contain an icon set via the set_line_gutter_icon() method.

GutterType **GUTTER_TYPE_CUSTOM** = `2`

When a gutter is set to custom using set_gutter_type(), it is used to contain custom visuals controlled by a callback method set via the set_gutter_custom_draw() method.

---

## Property Descriptions

[AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **autowrap_mode** = `3`

-  **set_autowrap_mode**(value: [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode))
- [AutowrapMode](class_textserver.md#enum-textserver-autowrapmode) **get_autowrap_mode**()

If wrap_mode is set to LINE_WRAPPING_BOUNDARY, sets text wrapping mode.

---

[bool](class_bool.md#class-bool) **backspace_deletes_composite_character_enabled** = `false`

-  **set_backspace_deletes_composite_character_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_backspace_deletes_composite_character_enabled**()

If `true` and caret_mid_grapheme is `false`, backspace deletes an entire composite character such as ❤️‍🩹, instead of deleting part of the composite character.

---

[bool](class_bool.md#class-bool) **caret_blink** = `false`

-  **set_caret_blink_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_caret_blink_enabled**()

If `true`, makes the caret blink.

---

[float](class_float.md#class-float) **caret_blink_interval** = `0.65`

-  **set_caret_blink_interval**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_caret_blink_interval**()

The interval at which the caret blinks (in seconds).

---

[bool](class_bool.md#class-bool) **caret_draw_when_editable_disabled** = `false`

-  **set_draw_caret_when_editable_disabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drawing_caret_when_editable_disabled**()

If `true`, caret will be visible when editable is disabled.

---

[bool](class_bool.md#class-bool) **caret_mid_grapheme** = `false`

-  **set_caret_mid_grapheme_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_caret_mid_grapheme_enabled**()

Allow moving caret, selecting and removing the individual composite character components.

**Note:** `Backspace` is always removing individual composite character components.

---

[bool](class_bool.md#class-bool) **caret_move_on_right_click** = `true`

-  **set_move_caret_on_right_click_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_move_caret_on_right_click_enabled**()

If `true`, a right-click moves the caret at the mouse position before displaying the context menu.

If `false`, the context menu ignores mouse location.

---

[bool](class_bool.md#class-bool) **caret_multiple** = `true`

-  **set_multiple_carets_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_multiple_carets_enabled**()

If `true`, multiple carets are allowed. Left-clicking with `Alt` adds a new caret. See add_caret() and get_caret_count().

---

CaretType **caret_type** = `0`

-  **set_caret_type**(value: CaretType)
- CaretType **get_caret_type**()

Set the type of caret to draw.

---

[bool](class_bool.md#class-bool) **context_menu_enabled** = `true`

-  **set_context_menu_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_context_menu_enabled**()

If `true`, a right-click displays the context menu.

---

[String](class_string.md#class-string) **custom_word_separators** = `""`

-  **set_custom_word_separators**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_custom_word_separators**()

The characters to consider as word delimiters if use_custom_word_separators is `true`. The characters should be defined without separation, for example `#_!`.

---

[bool](class_bool.md#class-bool) **deselect_on_focus_loss_enabled** = `true`

-  **set_deselect_on_focus_loss_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_deselect_on_focus_loss_enabled**()

If `true`, the selected text will be deselected when focus is lost.

---

[bool](class_bool.md#class-bool) **drag_and_drop_selection_enabled** = `true`

-  **set_drag_and_drop_selection_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drag_and_drop_selection_enabled**()

If `true`, allow drag and drop of selected text. Text can still be dropped from other sources.

---

[bool](class_bool.md#class-bool) **draw_control_chars** = `false`

-  **set_draw_control_chars**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_draw_control_chars**()

If `true`, control characters are displayed.

---

[bool](class_bool.md#class-bool) **draw_spaces** = `false`

-  **set_draw_spaces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drawing_spaces**()

If `true`, the "space" character will have a visible representation.

---

[bool](class_bool.md#class-bool) **draw_tabs** = `false`

-  **set_draw_tabs**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drawing_tabs**()

If `true`, the "tab" character will have a visible representation.

---

[bool](class_bool.md#class-bool) **editable** = `true`

-  **set_editable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editable**()

If `false`, existing text cannot be modified and new text cannot be added.

---

[bool](class_bool.md#class-bool) **emoji_menu_enabled** = `true`

-  **set_emoji_menu_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_emoji_menu_enabled**()

If `true`, "Emoji and Symbols" menu is enabled.

---

[bool](class_bool.md#class-bool) **empty_selection_clipboard_enabled** = `true`

-  **set_empty_selection_clipboard_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_empty_selection_clipboard_enabled**()

If `true`, copying or cutting without a selection is performed on all lines with a caret. Otherwise, copy and cut require a selection.

---

[bool](class_bool.md#class-bool) **highlight_all_occurrences** = `false`

-  **set_highlight_all_occurrences**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_highlight_all_occurrences_enabled**()

If `true`, all occurrences of the selected text will be highlighted.

---

[bool](class_bool.md#class-bool) **highlight_current_line** = `false`

-  **set_highlight_current_line**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_highlight_current_line_enabled**()

If `true`, the line containing the cursor is highlighted.

---

[bool](class_bool.md#class-bool) **indent_wrapped_lines** = `false`

-  **set_indent_wrapped_lines**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_indent_wrapped_lines**()

If `true`, all wrapped lines are indented to the same amount as the unwrapped line.

---

[String](class_string.md#class-string) **language** = `""`

-  **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

[bool](class_bool.md#class-bool) **middle_mouse_paste_enabled** = `true`

-  **set_middle_mouse_paste_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_middle_mouse_paste_enabled**()

If `false`, using middle mouse button to paste clipboard will be disabled.

**Note:** This method is only implemented on Linux.

---

[bool](class_bool.md#class-bool) **minimap_draw** = `false`

-  **set_draw_minimap**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drawing_minimap**()

If `true`, a minimap is shown, providing an outline of your source code. The minimap uses a fixed-width text size.

---

[int](class_int.md#class-int) **minimap_width** = `80`

-  **set_minimap_width**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_minimap_width**()

The width, in pixels, of the minimap.

---

[String](class_string.md#class-string) **placeholder_text** = `""`

-  **set_placeholder**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_placeholder**()

Text shown when the **TextEdit** is empty. It is **not** the **TextEdit**'s default value (see text).

---

[bool](class_bool.md#class-bool) **scroll_fit_content_height** = `false`

-  **set_fit_content_height_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_fit_content_height_enabled**()

If `true`, **TextEdit** fits its minimum height to the number of visible lines instead of scrolling vertically. If a maximum height is set (for example via [Control.custom_maximum_size](class_control.md#class-control-property-custom-maximum-size)) and content exceeds it, a vertical scrollbar is shown.

---

[bool](class_bool.md#class-bool) **scroll_fit_content_width** = `false`

-  **set_fit_content_width_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_fit_content_width_enabled**()

If `true`, **TextEdit** fits its minimum width to the widest line instead of scrolling horizontally. If a maximum width is set (for example via [Control.custom_maximum_size](class_control.md#class-control-property-custom-maximum-size)) and content exceeds it, a horizontal scrollbar is shown.

---

[int](class_int.md#class-int) **scroll_horizontal** = `0`

-  **set_h_scroll**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_h_scroll**()

If there is a horizontal scrollbar, this determines the current horizontal scroll value in pixels.

---

[bool](class_bool.md#class-bool) **scroll_past_end_of_file** = `false`

-  **set_scroll_past_end_of_file_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scroll_past_end_of_file_enabled**()

Allow scrolling past the last line into "virtual" space.

---

[bool](class_bool.md#class-bool) **scroll_smooth** = `false`

-  **set_smooth_scroll_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_smooth_scroll_enabled**()

Scroll smoothly over the text rather than jumping to the next location.

---

[float](class_float.md#class-float) **scroll_v_scroll_speed** = `80.0`

-  **set_v_scroll_speed**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_v_scroll_speed**()

Sets the scroll speed with the minimap or when scroll_smooth is enabled.

---

[float](class_float.md#class-float) **scroll_vertical** = `0.0`

-  **set_v_scroll**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_v_scroll**()

If there is a vertical scrollbar, this determines the current vertical scroll value in line numbers, starting at 0 for the top line.

---

[bool](class_bool.md#class-bool) **selecting_enabled** = `true`

-  **set_selecting_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_selecting_enabled**()

If `true`, text can be selected.

If `false`, text can not be selected by the user or by the select() or select_all() methods.

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

[SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter) **syntax_highlighter**

-  **set_syntax_highlighter**(value: [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter))
- [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter) **get_syntax_highlighter**()

The syntax highlighter to use.

**Note:** A [SyntaxHighlighter](class_syntaxhighlighter.md#class-syntaxhighlighter) instance should not be used across multiple **TextEdit** nodes.

---

[bool](class_bool.md#class-bool) **tab_input_mode** = `true`

-  **set_tab_input_mode**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_tab_input_mode**()

If `true`, [ProjectSettings.input/ui_text_indent](class_projectsettings.md#class-projectsettings-property-input-ui-text-indent) input `Tab` character, otherwise it moves keyboard focus to the next [Control](class_control.md#class-control) in the scene.

---

[String](class_string.md#class-string) **text** = `""`

-  **set_text**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_text**()

String value of the **TextEdit**.

---

[TextDirection](class_control.md#enum-control-textdirection) **text_direction** = `0`

-  **set_text_direction**(value: [TextDirection](class_control.md#enum-control-textdirection))
- [TextDirection](class_control.md#enum-control-textdirection) **get_text_direction**()

Base text writing direction.

---

[bool](class_bool.md#class-bool) **use_custom_word_separators** = `false`

-  **set_use_custom_word_separators**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_custom_word_separators_enabled**()

If `false`, using `Ctrl + Left` or `Ctrl + Right` (`Cmd + Left` or `Cmd + Right` on macOS) bindings will use the behavior of use_default_word_separators. If `true`, it will also stop the caret if a character within custom_word_separators is detected. Useful for subword moving. This behavior also will be applied to the behavior of text selection.

---

[bool](class_bool.md#class-bool) **use_default_word_separators** = `true`

-  **set_use_default_word_separators**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_default_word_separators_enabled**()

If `false`, using `Ctrl + Left` or `Ctrl + Right` (`Cmd + Left` or `Cmd + Right` on macOS) bindings will stop moving caret only if a space or punctuation is detected. If `true`, it will also stop the caret if a character is part of `!"#$%&'()*+,-./:;<=>?@[\]^`{|}~`, the Unicode General Punctuation table, or the Unicode CJK Punctuation table. Useful for subword moving. This behavior also will be applied to the behavior of text selection.

---

[bool](class_bool.md#class-bool) **virtual_keyboard_enabled** = `true`

-  **set_virtual_keyboard_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_virtual_keyboard_enabled**()

If `true`, the native virtual keyboard is enabled on platforms that support it.

---

[bool](class_bool.md#class-bool) **virtual_keyboard_show_on_focus** = `true`

-  **set_virtual_keyboard_show_on_focus**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_virtual_keyboard_show_on_focus**()

If `true`, the native virtual keyboard is shown on focus events on platforms that support it.

---

LineWrappingMode **wrap_mode** = `0`

-  **set_line_wrapping_mode**(value: LineWrappingMode)
- LineWrappingMode **get_line_wrapping_mode**()

Sets the line wrapping mode to use.

---

## Method Descriptions

 **\_backspace**(caret_index: [int](class_int.md#class-int))

Override this method to define what happens when the user presses the backspace key.

---

 **\_copy**(caret_index: [int](class_int.md#class-int))

Override this method to define what happens when the user performs a copy operation.

---

 **\_cut**(caret_index: [int](class_int.md#class-int))

Override this method to define what happens when the user performs a cut operation.

---

 **\_handle_unicode_input**(unicode_char: [int](class_int.md#class-int), caret_index: [int](class_int.md#class-int))

Override this method to define what happens when the user types in the provided key `unicode_char`.

---

 **\_paste**(caret_index: [int](class_int.md#class-int))

Override this method to define what happens when the user performs a paste operation.

---

 **\_paste_primary_clipboard**(caret_index: [int](class_int.md#class-int))

Override this method to define what happens when the user performs a paste operation with middle mouse button.

**Note:** This method is only implemented on Linux.

---

[int](class_int.md#class-int) **add_caret**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Adds a new caret at the given location. Returns the index of the new caret, or `-1` if the location is invalid.

---

 **add_caret_at_carets**(below: [bool](class_bool.md#class-bool))

Adds an additional caret above or below every caret. If `below` is `true` the new caret will be added below and above otherwise.

---

 **add_gutter**(at: [int](class_int.md#class-int) = -1)

Register a new gutter to this **TextEdit**. Use `at` to have a specific gutter order. A value of `-1` appends the gutter to the right.

---

 **add_selection_for_next_occurrence**()

Adds a selection and a caret for the next occurrence of the current selection. If there is no active selection, selects word under caret.

---

 **adjust_carets_after_edit**(caret: [int](class_int.md#class-int), from_line: [int](class_int.md#class-int), from_col: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int), to_col: [int](class_int.md#class-int))

**Deprecated:** No longer necessary since methods now adjust carets themselves.

This method does nothing.

---

 **adjust_viewport_to_caret**(caret_index: [int](class_int.md#class-int) = 0)

Adjust the viewport so the caret is visible.

---

 **apply_ime**()

Applies text from the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME) to each caret and closes the IME if it is open.

---

 **backspace**(caret_index: [int](class_int.md#class-int) = -1)

Called when the user presses the backspace key. Can be overridden with \_backspace().

---

 **begin_complex_operation**()

Starts a multipart edit. All edits will be treated as one action until end_complex_operation() is called.

---

 **begin_multicaret_edit**()

Starts an edit for multiple carets. The edit must be ended with end_multicaret_edit(). Multicaret edits can be used to edit text at multiple carets and delay merging the carets until the end, so the caret indexes aren't affected immediately. begin_multicaret_edit() and end_multicaret_edit() can be nested, and the merge will happen at the last end_multicaret_edit().

```gdscript
begin_complex_operation()
begin_multicaret_edit()
for i in range(get_caret_count()):
    if multicaret_edit_ignore_caret(i):
        continue
    # Logic here.
end_multicaret_edit()
end_complex_operation()
```

---

 **cancel_ime**()

Closes the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME) if it is open. Any text in the IME will be lost.

---

 **center_viewport_to_caret**(caret_index: [int](class_int.md#class-int) = 0)

Centers the viewport on the line the editing caret is at. This also resets the scroll_horizontal value to `0`.

---

 **clear**()

Performs a full reset of **TextEdit**, including undo history.

---

 **clear_undo_history**()

Clears the undo history.

---

 **collapse_carets**(from_line: [int](class_int.md#class-int), from_column: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int), to_column: [int](class_int.md#class-int), inclusive: [bool](class_bool.md#class-bool) = false)

Collapse all carets in the given range to the `from_line` and `from_column` position.

`inclusive` applies to both ends.

If is_in_mulitcaret_edit() is `true`, carets that are collapsed will be `true` for multicaret_edit_ignore_caret().

merge_overlapping_carets() will be called if any carets were collapsed.

---

 **copy**(caret_index: [int](class_int.md#class-int) = -1)

Copies the current text selection. Can be overridden with \_copy().

---

 **cut**(caret_index: [int](class_int.md#class-int) = -1)

Cut's the current selection. Can be overridden with \_cut().

---

 **delete_selection**(caret_index: [int](class_int.md#class-int) = -1)

Deletes the selected text.

---

 **deselect**(caret_index: [int](class_int.md#class-int) = -1)

Deselects the current selection.

---

 **end_action**()

Marks the end of steps in the current action started with start_action().

---

 **end_complex_operation**()

Ends a multipart edit, started with begin_complex_operation(). If called outside a complex operation, the current operation is pushed onto the undo/redo stack.

---

 **end_multicaret_edit**()

Ends an edit for multiple carets, that was started with begin_multicaret_edit(). If this was the last end_multicaret_edit() and merge_overlapping_carets() was called, carets will be merged.

---

[int](class_int.md#class-int) **get_caret_column**(caret_index: [int](class_int.md#class-int) = 0)

Returns the column the editing caret is at.

---

[int](class_int.md#class-int) **get_caret_count**()

Returns the number of carets in this **TextEdit**.

---

[Vector2](class_vector2.md#class-vector2) **get_caret_draw_pos**(caret_index: [int](class_int.md#class-int) = 0)

Returns the caret pixel draw position.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_caret_index_edit_order**()

**Deprecated:** Carets no longer need to be edited in any specific order. If the carets need to be sorted, use get_sorted_carets() instead.

Returns a list of caret indexes in their edit order, this done from bottom to top. Edit order refers to the way actions such as insert_text_at_caret() are applied.

---

[int](class_int.md#class-int) **get_caret_line**(caret_index: [int](class_int.md#class-int) = 0)

Returns the line the editing caret is on.

---

[int](class_int.md#class-int) **get_caret_wrap_index**(caret_index: [int](class_int.md#class-int) = 0)

Returns the wrap index the editing caret is on.

---

[int](class_int.md#class-int) **get_first_non_whitespace_column**(line: [int](class_int.md#class-int))

Returns the first column containing a non-whitespace character on the given line. If there is only whitespace, returns the number of characters.

---

[int](class_int.md#class-int) **get_first_visible_line**()

Returns the first visible line.

---

[int](class_int.md#class-int) **get_gutter_count**()

Returns the number of gutters registered.

---

[String](class_string.md#class-string) **get_gutter_name**(gutter: [int](class_int.md#class-int))

Returns the name of the gutter at the given index.

---

GutterType **get_gutter_type**(gutter: [int](class_int.md#class-int))

Returns the type of the gutter at the given index. Gutters can contain icons, text, or custom visuals.

---

[int](class_int.md#class-int) **get_gutter_width**(gutter: [int](class_int.md#class-int))

Returns the width of the gutter at the given index.

---

[HScrollBar](class_hscrollbar.md#class-hscrollbar) **get_h_scroll_bar**()

Returns the [HScrollBar](class_hscrollbar.md#class-hscrollbar) used by **TextEdit**.

---

[int](class_int.md#class-int) **get_indent_level**(line: [int](class_int.md#class-int))

Returns the indent level of the given line. This is the number of spaces and tabs at the beginning of the line, with the tabs taking the tab size into account (see get_tab_size()).

---

[int](class_int.md#class-int) **get_last_full_visible_line**()

Returns the last visible line. Use get_last_full_visible_line_wrap_index() for the wrap index.

---

[int](class_int.md#class-int) **get_last_full_visible_line_wrap_index**()

Returns the last visible wrap index of the last visible line.

---

[int](class_int.md#class-int) **get_last_unhidden_line**()

Returns the last unhidden line in the entire **TextEdit**.

---

[String](class_string.md#class-string) **get_line**(line: [int](class_int.md#class-int))

Returns the text of a specific line.

---

[Color](class_color.md#class-color) **get_line_background_color**(line: [int](class_int.md#class-int))

Returns the custom background color of the given line. If no color is set, returns `Color(0, 0, 0, 0)`.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_line_column_at_pos**(position: [Vector2i](class_vector2i.md#class-vector2i), clamp_line: [bool](class_bool.md#class-bool) = true, clamp_column: [bool](class_bool.md#class-bool) = true)

Returns the line and column at the given position. In the returned vector, `x` is the column and `y` is the line.

If `clamp_line` is `false` and `position` is below the last line, `Vector2i(-1, -1)` is returned.

If `clamp_column` is `false` and `position` is outside the column range of the line, `Vector2i(-1, -1)` is returned.

---

[int](class_int.md#class-int) **get_line_count**()

Returns the number of lines in the text.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_line_gutter_icon**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))

Returns the icon currently in `gutter` at `line`. This only works when the gutter type is GUTTER_TYPE_ICON (see set_gutter_type()).

---

[Color](class_color.md#class-color) **get_line_gutter_item_color**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))

Returns the color currently in `gutter` at `line`.

---

[Variant](class_variant.md#class-variant) **get_line_gutter_metadata**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))

Returns the metadata currently in `gutter` at `line`.

---

[String](class_string.md#class-string) **get_line_gutter_text**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))

Returns the text currently in `gutter` at `line`. This only works when the gutter type is GUTTER_TYPE_STRING (see set_gutter_type()).

---

[int](class_int.md#class-int) **get_line_height**()

Returns the maximum value of the line height among all lines.

**Note:** The return value is influenced by line_spacing and font_size. And it will not be less than `1`.

---

[Array](class_array.md#class-array)[[Vector2i](class_vector2i.md#class-vector2i)] **get_line_ranges_from_carets**(only_selections: [bool](class_bool.md#class-bool) = false, merge_adjacent: [bool](class_bool.md#class-bool) = true)

Returns an [Array](class_array.md#class-array) of line ranges where `x` is the first line and `y` is the last line. All lines within these ranges will have a caret on them or be part of a selection. Each line will only be part of one line range, even if it has multiple carets on it.

If a selection's end column (get_selection_to_column()) is at column `0`, that line will not be included. If a selection begins on the line after another selection ends and `merge_adjacent` is `true`, or they begin and end on the same line, one line range will include both selections.

---

[int](class_int.md#class-int) **get_line_width**(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = -1)

Returns the width in pixels of the `wrap_index` on `line`.

---

[String](class_string.md#class-string) **get_line_with_ime**(line: [int](class_int.md#class-int))

Returns line text as it is currently displayed, including IME composition string.

---

[int](class_int.md#class-int) **get_line_wrap_count**(line: [int](class_int.md#class-int))

Returns the number of times the given line is wrapped.

---

[int](class_int.md#class-int) **get_line_wrap_index_at_column**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Returns the wrap index of the given column on the given line. This ranges from `0` to get_line_wrap_count().

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_line_wrapped_text**(line: [int](class_int.md#class-int))

Returns an array of [String](class_string.md#class-string)s representing each wrapped index.

---

[Vector2](class_vector2.md#class-vector2) **get_local_mouse_pos**()

Returns the local mouse position adjusted for the text direction.

---

[PopupMenu](class_popupmenu.md#class-popupmenu) **get_menu**()

Returns the [PopupMenu](class_popupmenu.md#class-popupmenu) of this **TextEdit**. By default, this menu is displayed when right-clicking on the **TextEdit**.

You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (see MenuItems). For example:

GDScript

```gdscript
func _ready():
    var menu = get_menu()
    # Remove all items after "Redo".
    menu.item_count = menu.get_item_index(MENU_REDO) + 1
    # Add custom items.
    menu.add_separator()
    menu.add_item("Insert Date", MENU_MAX + 1)
    # Connect callback.
    menu.id_pressed.connect(_on_item_pressed)

func _on_item_pressed(id):
    if id == MENU_MAX + 1:
        insert_text_at_caret(Time.get_date_string_from_system())
```

C#

```csharp
public override void _Ready()
{
    var menu = GetMenu();
    // Remove all items after "Redo".
    menu.ItemCount = menu.GetItemIndex(TextEdit.MenuItems.Redo) + 1;
    // Add custom items.
    menu.AddSeparator();
    menu.AddItem("Insert Date", TextEdit.MenuItems.Max + 1);
    // Add event handler.
    menu.IdPressed += OnItemPressed;
}

public void OnItemPressed(int id)
{
    if (id == TextEdit.MenuItems.Max + 1)
    {
        InsertTextAtCaret(Time.GetDateStringFromSystem());
    }
}
```

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class-window-property-visible) property.

---

[int](class_int.md#class-int) **get_minimap_line_at_pos**(position: [Vector2i](class_vector2i.md#class-vector2i))

Returns the equivalent minimap line at `position`.

---

[int](class_int.md#class-int) **get_minimap_visible_lines**()

Returns the number of lines that may be drawn on the minimap.

---

[int](class_int.md#class-int) **get_next_composite_character_column**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Returns the correct column at the end of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the start of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

**Note:** To check at caret location use `get_next_composite_character_column(get_caret_line(), get_caret_column())`

---

[Vector2i](class_vector2i.md#class-vector2i) **get_next_visible_line_index_offset_from**(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int), visible_amount: [int](class_int.md#class-int))

Similar to get_next_visible_line_offset_from(), but takes into account the line wrap indexes. In the returned vector, `x` is the line, `y` is the wrap index.

---

[int](class_int.md#class-int) **get_next_visible_line_offset_from**(line: [int](class_int.md#class-int), visible_amount: [int](class_int.md#class-int))

Returns the count to the next visible line from `line` to `line + visible_amount`. Can also count backwards. For example if a **TextEdit** has 5 lines with lines 2 and 3 hidden, calling this with `line = 1, visible_amount = 1` would return 3.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_pos_at_line_column**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Returns the local position for the given `line` and `column`. If `x` or `y` of the returned vector equal `-1`, the position is outside of the viewable area of the control.

**Note:** The Y position corresponds to the bottom side of the line. Use get_rect_at_line_column() to get the top side position.

---

[int](class_int.md#class-int) **get_previous_composite_character_column**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Returns the correct column at the start of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the end of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

**Note:** To check at caret location use `get_previous_composite_character_column(get_caret_line(), get_caret_column())`

---

[Rect2i](class_rect2i.md#class-rect2i) **get_rect_at_line_column**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Returns the local position and size for the grapheme at the given `line` and `column`. If `x` or `y` position of the returned rect equal `-1`, the position is outside of the viewable area of the control.

**Note:** The Y position of the returned rect corresponds to the top side of the line, unlike get_pos_at_line_column() which returns the bottom side.

---

[int](class_int.md#class-int) **get_saved_version**()

Returns the last tagged saved version from tag_saved_version().

---

[float](class_float.md#class-float) **get_scroll_pos_for_line**(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = 0)

Returns the scroll position for `wrap_index` of `line`.

---

[String](class_string.md#class-string) **get_selected_text**(caret_index: [int](class_int.md#class-int) = -1)

Returns the text inside the selection of a caret, or all the carets if `caret_index` is its default value `-1`.

---

[int](class_int.md#class-int) **get_selection_at_line_column**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int), include_edges: [bool](class_bool.md#class-bool) = true, only_selections: [bool](class_bool.md#class-bool) = true)

Returns the caret index of the selection at the given `line` and `column`, or `-1` if there is none.

If `include_edges` is `false`, the position must be inside the selection and not at either end. If `only_selections` is `false`, carets without a selection will also be considered.

---

[int](class_int.md#class-int) **get_selection_column**(caret_index: [int](class_int.md#class-int) = 0)

**Deprecated:** Use get_selection_origin_column() instead.

Returns the original start column of the selection.

---

[int](class_int.md#class-int) **get_selection_from_column**(caret_index: [int](class_int.md#class-int) = 0)

Returns the selection begin column. Returns the caret column if there is no selection.

---

[int](class_int.md#class-int) **get_selection_from_line**(caret_index: [int](class_int.md#class-int) = 0)

Returns the selection begin line. Returns the caret line if there is no selection.

---

[int](class_int.md#class-int) **get_selection_line**(caret_index: [int](class_int.md#class-int) = 0)

**Deprecated:** Use get_selection_origin_line() instead.

Returns the original start line of the selection.

---

SelectionMode **get_selection_mode**()

Returns the current selection mode.

---

[int](class_int.md#class-int) **get_selection_origin_column**(caret_index: [int](class_int.md#class-int) = 0)

Returns the origin column of the selection. This is the opposite end from the caret.

---

[int](class_int.md#class-int) **get_selection_origin_line**(caret_index: [int](class_int.md#class-int) = 0)

Returns the origin line of the selection. This is the opposite end from the caret.

---

[int](class_int.md#class-int) **get_selection_to_column**(caret_index: [int](class_int.md#class-int) = 0)

Returns the selection end column. Returns the caret column if there is no selection.

---

[int](class_int.md#class-int) **get_selection_to_line**(caret_index: [int](class_int.md#class-int) = 0)

Returns the selection end line. Returns the caret line if there is no selection.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_sorted_carets**(include_ignored_carets: [bool](class_bool.md#class-bool) = false)

Returns the carets sorted by selection beginning from lowest line and column to highest (from top to bottom of text).

If `include_ignored_carets` is `false`, carets from multicaret_edit_ignore_caret() will be ignored.

---

[int](class_int.md#class-int) **get_tab_size**()

Returns the **TextEdit**'s' tab size.

---

[int](class_int.md#class-int) **get_total_gutter_width**()

Returns the total width of all gutters and internal padding.

---

[int](class_int.md#class-int) **get_total_visible_line_count**()

Returns the total number of lines in the text. This includes wrapped lines and excludes folded lines. If wrap_mode is set to LINE_WRAPPING_NONE and no lines are folded (see [CodeEdit.is_line_folded()](class_codeedit.md#class-codeedit-method-is-line-folded)) then this is equivalent to get_line_count(). See get_visible_line_count_in_range() for a limited range of lines.

---

[VScrollBar](class_vscrollbar.md#class-vscrollbar) **get_v_scroll_bar**()

Returns the [VScrollBar](class_vscrollbar.md#class-vscrollbar) of the **TextEdit**.

---

[int](class_int.md#class-int) **get_version**()

Returns the current version of the **TextEdit**. The version is a count of recorded operations by the undo/redo history.

---

[int](class_int.md#class-int) **get_visible_line_count**()

Returns the number of lines that can visually fit, rounded down, based on this control's height.

---

[int](class_int.md#class-int) **get_visible_line_count_in_range**(from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))

Returns the total number of lines between `from_line` and `to_line` (inclusive) in the text. This includes wrapped lines and excludes folded lines. If the range covers all lines it is equivalent to get_total_visible_line_count().

---

[String](class_string.md#class-string) **get_word_at_pos**(position: [Vector2](class_vector2.md#class-vector2))

Returns the word at `position`.

---

[String](class_string.md#class-string) **get_word_under_caret**(caret_index: [int](class_int.md#class-int) = -1)

Returns a [String](class_string.md#class-string) text with the word under the caret's location.

---

[bool](class_bool.md#class-bool) **has_ime_text**()

Returns `true` if the user has text in the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME).

---

[bool](class_bool.md#class-bool) **has_redo**()

Returns `true` if a "redo" action is available.

---

[bool](class_bool.md#class-bool) **has_selection**(caret_index: [int](class_int.md#class-int) = -1)

Returns `true` if the user has selected text.

---

[bool](class_bool.md#class-bool) **has_undo**()

Returns `true` if an "undo" action is available.

---

 **insert_line_at**(line: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

Inserts a new line with `text` at `line`.

---

 **insert_text**(text: [String](class_string.md#class-string), line: [int](class_int.md#class-int), column: [int](class_int.md#class-int), before_selection_begin: [bool](class_bool.md#class-bool) = true, before_selection_end: [bool](class_bool.md#class-bool) = false)

Inserts the `text` at `line` and `column`.

If `before_selection_begin` is `true`, carets and selections that begin at `line` and `column` will moved to the end of the inserted text, along with all carets after it.

If `before_selection_end` is `true`, selections that end at `line` and `column` will be extended to the end of the inserted text. These parameters can be used to insert text inside of or outside of selections.

---

 **insert_text_at_caret**(text: [String](class_string.md#class-string), caret_index: [int](class_int.md#class-int) = -1)

Insert the specified text at the caret position.

---

[bool](class_bool.md#class-bool) **is_caret_after_selection_origin**(caret_index: [int](class_int.md#class-int) = 0)

Returns `true` if the caret of the selection is after the selection origin. This can be used to determine the direction of the selection.

---

[bool](class_bool.md#class-bool) **is_caret_visible**(caret_index: [int](class_int.md#class-int) = 0)

Returns `true` if the caret is visible, `false` otherwise. A caret will be considered hidden if it is outside the scrollable area when scrolling is enabled.

**Note:** is_caret_visible() does not account for a caret being off-screen if it is still within the scrollable area. It will return `true` even if the caret is off-screen as long as it meets **TextEdit**'s own conditions for being visible. This includes uses of scroll_fit_content_width and scroll_fit_content_height that cause the **TextEdit** to expand beyond the viewport's bounds.

**Note:** This method does *not* guarantee an accurate visibility check immediately after setting the caret position. The correct value may only be available in the next frame after the **TextEdit** has finished drawing. This also applies to any operation that causes the **TextEdit** to change in size.

---

[bool](class_bool.md#class-bool) **is_dragging_cursor**()

Returns `true` if the user is dragging their mouse for scrolling, selecting, or text dragging.

---

[bool](class_bool.md#class-bool) **is_gutter_clickable**(gutter: [int](class_int.md#class-int))

Returns `true` if the gutter at the given index is clickable. See set_gutter_clickable().

---

[bool](class_bool.md#class-bool) **is_gutter_drawn**(gutter: [int](class_int.md#class-int))

Returns `true` if the gutter at the given index is currently drawn. See set_gutter_draw().

---

[bool](class_bool.md#class-bool) **is_gutter_overwritable**(gutter: [int](class_int.md#class-int))

Returns `true` if the gutter at the given index is overwritable. See set_gutter_overwritable().

---

[bool](class_bool.md#class-bool) **is_in_mulitcaret_edit**()

Returns `true` if a begin_multicaret_edit() has been called and end_multicaret_edit() has not yet been called.

---

[bool](class_bool.md#class-bool) **is_line_gutter_clickable**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int))

Returns `true` if the gutter at the given index on the given line is clickable. See set_line_gutter_clickable().

---

[bool](class_bool.md#class-bool) **is_line_in_viewport**(line: [int](class_int.md#class-int))

Returns `true` if the given line is within the scope of the scrollable area of the viewport.

---

[bool](class_bool.md#class-bool) **is_line_wrapped**(line: [int](class_int.md#class-int))

Returns if the given line is wrapped.

---

[bool](class_bool.md#class-bool) **is_menu_visible**()

Returns `true` if the menu is visible. Use this instead of `get_menu().visible` to improve performance (so the creation of the menu is avoided). See get_menu().

---

[bool](class_bool.md#class-bool) **is_mouse_over_selection**(edges: [bool](class_bool.md#class-bool), caret_index: [int](class_int.md#class-int) = -1)

Returns `true` if the mouse is over a selection. If `edges` is `true`, the edges are considered part of the selection.

---

[bool](class_bool.md#class-bool) **is_overtype_mode_enabled**()

Returns `true` if overtype mode is enabled. See set_overtype_mode_enabled().

---

 **menu_option**(option: [int](class_int.md#class-int))

Executes a given action as defined in the MenuItems enum.

---

 **merge_gutters**(from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))

Merge the gutters from `from_line` into `to_line`. Only overwritable gutters will be copied. See set_gutter_overwritable().

---

 **merge_overlapping_carets**()

Merges any overlapping carets. Will favor the newest caret, or the caret with a selection.

If is_in_mulitcaret_edit() is `true`, the merge will be queued to happen at the end of the multicaret edit. See begin_multicaret_edit() and end_multicaret_edit().

**Note:** This is not called when a caret changes position but after certain actions, so it is possible to get into a state where carets overlap.

---

[bool](class_bool.md#class-bool) **multicaret_edit_ignore_caret**(caret_index: [int](class_int.md#class-int))

Returns `true` if the given `caret_index` should be ignored as part of a multicaret edit. See begin_multicaret_edit() and end_multicaret_edit(). Carets that should be ignored are ones that were part of removed text and will likely be merged at the end of the edit, or carets that were added during the edit.

It is recommended to `continue` within a loop iterating on multiple carets if a caret should be ignored.

---

 **paste**(caret_index: [int](class_int.md#class-int) = -1)

Paste at the current location. Can be overridden with \_paste().

---

 **paste_primary_clipboard**(caret_index: [int](class_int.md#class-int) = -1)

Pastes the primary clipboard.

---

 **redo**()

Perform redo operation.

---

 **remove_caret**(caret: [int](class_int.md#class-int))

Removes the given caret index.

**Note:** This can result in adjustment of all other caret indices.

---

 **remove_gutter**(gutter: [int](class_int.md#class-int))

Removes the gutter at the given index.

---

 **remove_line_at**(line: [int](class_int.md#class-int), move_carets_down: [bool](class_bool.md#class-bool) = true)

Removes the line of text at `line`. Carets on this line will attempt to match their previous visual x position.

If `move_carets_down` is `true` carets will move to the next line down, otherwise carets will move up.

---

 **remove_secondary_carets**()

Removes all additional carets.

---

 **remove_text**(from_line: [int](class_int.md#class-int), from_column: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int), to_column: [int](class_int.md#class-int))

Removes text between the given positions.

---

[Vector2i](class_vector2i.md#class-vector2i) **search**(text: [String](class_string.md#class-string), flags: [int](class_int.md#class-int), from_line: [int](class_int.md#class-int), from_column: [int](class_int.md#class-int))

Perform a search inside the text. Search flags can be specified in the SearchFlags enum.

In the returned vector, `x` is the column, `y` is the line. If no results are found, both are equal to `-1`.

GDScript

```gdscript
var result = search("print", SEARCH_WHOLE_WORDS, 0, 0)
if result.x != -1:
    # Result found.
    var line_number = result.y
    var column_number = result.x
```

C#

```csharp
Vector2I result = Search("print", (uint)TextEdit.SearchFlags.WholeWords, 0, 0);
if (result.X != -1)
{
    // Result found.
    int lineNumber = result.Y;
    int columnNumber = result.X;
}
```

---

 **select**(origin_line: [int](class_int.md#class-int), origin_column: [int](class_int.md#class-int), caret_line: [int](class_int.md#class-int), caret_column: [int](class_int.md#class-int), caret_index: [int](class_int.md#class-int) = 0)

Selects text from `origin_line` and `origin_column` to `caret_line` and `caret_column` for the given `caret_index`. This moves the selection origin and the caret. If the positions are the same, the selection will be deselected.

If selecting_enabled is `false`, no selection will occur.

**Note:** If supporting multiple carets this will not check for any overlap. See merge_overlapping_carets().

---

 **select_all**()

Select all the text.

If selecting_enabled is `false`, no selection will occur.

---

 **select_word_under_caret**(caret_index: [int](class_int.md#class-int) = -1)

Selects the word under the caret.

---

 **set_caret_column**(column: [int](class_int.md#class-int), adjust_viewport: [bool](class_bool.md#class-bool) = true, caret_index: [int](class_int.md#class-int) = 0)

Moves the caret to the specified `column` index.

If `adjust_viewport` is `true`, the viewport will center at the caret position after the move occurs.

**Note:** If supporting multiple carets this will not check for any overlap. See merge_overlapping_carets().

---

 **set_caret_line**(line: [int](class_int.md#class-int), adjust_viewport: [bool](class_bool.md#class-bool) = true, can_be_hidden: [bool](class_bool.md#class-bool) = true, wrap_index: [int](class_int.md#class-int) = 0, caret_index: [int](class_int.md#class-int) = 0)

Moves the caret to the specified `line` index. The caret column will be moved to the same visual position it was at the last time set_caret_column() was called, or clamped to the end of the line.

If `adjust_viewport` is `true`, the viewport will center at the caret position after the move occurs.

If `can_be_hidden` is `true`, the specified `line` can be hidden.

If `wrap_index` is `-1`, the caret column will be clamped to the `line`'s length. If `wrap_index` is greater than `-1`, the column will be moved to attempt to match the visual x position on the line's `wrap_index` to the position from the last time set_caret_column() was called.

**Note:** If supporting multiple carets this will not check for any overlap. See merge_overlapping_carets().

---

 **set_gutter_clickable**(gutter: [int](class_int.md#class-int), clickable: [bool](class_bool.md#class-bool))

If `true`, the mouse cursor will change to a pointing hand ([Control.CURSOR_POINTING_HAND](class_control.md#class-control-constant-cursor-pointing-hand)) when hovering over the gutter at the given index. See is_gutter_clickable() and set_line_gutter_clickable().

---

 **set_gutter_custom_draw**(column: [int](class_int.md#class-int), draw_callback: [Callable](class_callable.md#class-callable))

Set a custom draw callback for the gutter at the given index. `draw_callback` must take the following arguments: A line index [int](class_int.md#class-int), a gutter index [int](class_int.md#class-int), and an area [Rect2](class_rect2.md#class-rect2). This callback only works when the gutter type is GUTTER_TYPE_CUSTOM (see set_gutter_type()).

---

 **set_gutter_draw**(gutter: [int](class_int.md#class-int), draw: [bool](class_bool.md#class-bool))

If `true`, the gutter at the given index is drawn. The gutter type (set_gutter_type()) determines how it is drawn. See is_gutter_drawn().

---

 **set_gutter_name**(gutter: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets the name of the gutter at the given index.

---

 **set_gutter_overwritable**(gutter: [int](class_int.md#class-int), overwritable: [bool](class_bool.md#class-bool))

If `true`, the line data of the gutter at the given index can be overridden when using merge_gutters(). See is_gutter_overwritable().

---

 **set_gutter_type**(gutter: [int](class_int.md#class-int), type: GutterType)

Sets the type of gutter at the given index. Gutters can contain icons, text, or custom visuals.

---

 **set_gutter_width**(gutter: [int](class_int.md#class-int), width: [int](class_int.md#class-int))

Set the width of the gutter at the given index.

---

 **set_line**(line: [int](class_int.md#class-int), new_text: [String](class_string.md#class-string))

Sets the text for a specific `line`.

Carets on the line will attempt to keep their visual x position.

---

 **set_line_as_center_visible**(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = 0)

Positions the `wrap_index` of `line` at the center of the viewport.

---

 **set_line_as_first_visible**(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = 0)

Positions the `wrap_index` of `line` at the top of the viewport.

---

 **set_line_as_last_visible**(line: [int](class_int.md#class-int), wrap_index: [int](class_int.md#class-int) = 0)

Positions the `wrap_index` of `line` at the bottom of the viewport.

---

 **set_line_background_color**(line: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the custom background color of the given line. If transparent, this color is applied on top of the default background color (See background_color). If set to `Color(0, 0, 0, 0)`, no additional color is applied.

---

 **set_line_gutter_clickable**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), clickable: [bool](class_bool.md#class-bool))

If `clickable` is `true`, makes the `gutter` on the given `line` clickable. This is like set_gutter_clickable(), but for a single line. If is_gutter_clickable() is `true`, this will not have any effect. See is_line_gutter_clickable() and gutter_clicked.

---

 **set_line_gutter_icon**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets the icon for `gutter` on `line` to `icon`. This only works when the gutter type is GUTTER_TYPE_ICON (see set_gutter_type()).

---

 **set_line_gutter_item_color**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the color for `gutter` on `line` to `color`.

---

 **set_line_gutter_metadata**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), metadata: [Variant](class_variant.md#class-variant))

Sets the metadata for `gutter` on `line` to `metadata`.

---

 **set_line_gutter_text**(line: [int](class_int.md#class-int), gutter: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

Sets the text for `gutter` on `line` to `text`. This only works when the gutter type is GUTTER_TYPE_STRING (see set_gutter_type()).

---

 **set_overtype_mode_enabled**(enabled: [bool](class_bool.md#class-bool))

If `true`, enables overtype mode. In this mode, typing overrides existing text instead of inserting text. The [ProjectSettings.input/ui_text_toggle_insert_mode](class_projectsettings.md#class-projectsettings-property-input-ui-text-toggle-insert-mode) action toggles overtype mode. See is_overtype_mode_enabled().

---

 **set_search_flags**(flags: [int](class_int.md#class-int))

Sets the search `flags`. This is used with set_search_text() to highlight occurrences of the searched text. Search flags can be specified from the SearchFlags enum.

---

 **set_search_text**(search_text: [String](class_string.md#class-string))

Sets the search text. See set_search_flags().

---

 **set_selection_mode**(mode: SelectionMode)

Sets the current selection mode.

---

 **set_selection_origin_column**(column: [int](class_int.md#class-int), caret_index: [int](class_int.md#class-int) = 0)

Sets the selection origin column to the `column` for the given `caret_index`. If the selection origin is moved to the caret position, the selection will deselect.

---

 **set_selection_origin_line**(line: [int](class_int.md#class-int), can_be_hidden: [bool](class_bool.md#class-bool) = true, wrap_index: [int](class_int.md#class-int) = -1, caret_index: [int](class_int.md#class-int) = 0)

Sets the selection origin line to the `line` for the given `caret_index`. If the selection origin is moved to the caret position, the selection will deselect.

If `can_be_hidden` is `false`, The line will be set to the nearest unhidden line below or above.

If `wrap_index` is `-1`, the selection origin column will be clamped to the `line`'s length. If `wrap_index` is greater than `-1`, the column will be moved to attempt to match the visual x position on the line's `wrap_index` to the position from the last time set_selection_origin_column() or select() was called.

---

 **set_tab_size**(size: [int](class_int.md#class-int))

Sets the tab size for the **TextEdit** to use.

---

 **set_tooltip_request_func**(callback: [Callable](class_callable.md#class-callable))

Provide custom tooltip text. The callback method must take the following args: `hovered_word: String`.

---

 **skip_selection_for_next_occurrence**()

Moves a selection and a caret for the next occurrence of the current selection. If there is no active selection, moves to the next occurrence of the word under caret.

---

 **start_action**(action: EditAction)

Starts an action, will end the current action if `action` is different.

An action will also end after a call to end_action(), after [ProjectSettings.gui/timers/text_edit_idle_detect_sec](class_projectsettings.md#class-projectsettings-property-gui-timers-text-edit-idle-detect-sec) is triggered or a new undoable step outside the start_action() and end_action() calls.

---

 **swap_lines**(from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))

Swaps the two lines. Carets will be swapped with the lines.

---

 **tag_saved_version**()

Tag the current version as saved.

---

 **undo**()

Perform undo operation.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **background_color** = `Color(0, 0, 0, 0)`

Sets the background [Color](class_color.md#class-color) of this **TextEdit**.

---

[Color](class_color.md#class-color) **caret_background_color** = `Color(0, 0, 0, 1)`

[Color](class_color.md#class-color) of the text behind the caret when using a block caret.

---

[Color](class_color.md#class-color) **caret_color** = `Color(0.875, 0.875, 0.875, 1)`

[Color](class_color.md#class-color) of the caret. This can be set to a fully transparent color to hide the caret entirely.

---

[Color](class_color.md#class-color) **current_line_color** = `Color(0.25, 0.25, 0.26, 0.8)`

Background [Color](class_color.md#class-color) of the line containing the caret.

---

[Color](class_color.md#class-color) **font_color** = `Color(0.875, 0.875, 0.875, 1)`

Sets the font [Color](class_color.md#class-color).

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(0, 0, 0, 1)`

The tint of text outline of the **TextEdit**.

---

[Color](class_color.md#class-color) **font_placeholder_color** = `Color(0.875, 0.875, 0.875, 0.6)`

Font color for placeholder_text.

---

[Color](class_color.md#class-color) **font_readonly_color** = `Color(0.875, 0.875, 0.875, 0.5)`

Sets the font [Color](class_color.md#class-color) when editable is disabled.

---

[Color](class_color.md#class-color) **font_selected_color** = `Color(0, 0, 0, 0)`

Sets the [Color](class_color.md#class-color) of the selected text. If equal to `Color(0, 0, 0, 0)`, it will be ignored.

---

[Color](class_color.md#class-color) **search_result_border_color** = `Color(0.3, 0.3, 0.3, 0.4)`

[Color](class_color.md#class-color) of the border around text that matches the search query.

---

[Color](class_color.md#class-color) **search_result_color** = `Color(0.3, 0.3, 0.3, 1)`

[Color](class_color.md#class-color) behind the text that matches the search query.

---

[Color](class_color.md#class-color) **selection_color** = `Color(0.5, 0.5, 0.5, 1)`

Sets the highlight [Color](class_color.md#class-color) of text selections.

---

[Color](class_color.md#class-color) **word_highlighted_color** = `Color(0.5, 0.5, 0.5, 0.25)`

Sets the highlight [Color](class_color.md#class-color) of multiple occurrences. highlight_all_occurrences has to be enabled.

---

[int](class_int.md#class-int) **caret_width** = `1`

The caret's width in pixels. Greater values can be used to improve accessibility by ensuring the caret is easily visible, or to ensure consistency with a large font size. If set to `0` or lower, the caret width is automatically set to 1 pixel and multiplied by the display scaling factor.

---

[int](class_int.md#class-int) **line_spacing** = `4`

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

[int](class_int.md#class-int) **outline_size** = `0`

The size of the text outline.

**Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class-fontfile-property-multichannel-signed-distance-field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class-fontfile-property-msdf-pixel-range) must be set to at least *twice* the value of outline_size for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

[int](class_int.md#class-int) **wrap_offset** = `10`

Sets an additional margin for line wrapping width.

---

[Font](class_font.md#class-font) **font**

Sets the default [Font](class_font.md#class-font).

---

[int](class_int.md#class-int) **font_size**

Sets default font size.

---

[Texture2D](class_texture2d.md#class-texture2d) **space**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) for space text characters.

---

[Texture2D](class_texture2d.md#class-texture2d) **tab**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) for tab text characters.

---

[StyleBox](class_stylebox.md#class-stylebox) **focus**

Sets the [StyleBox](class_stylebox.md#class-stylebox) when in focus. The focus [StyleBox](class_stylebox.md#class-stylebox) is displayed *over* the base [StyleBox](class_stylebox.md#class-stylebox), so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the base [StyleBox](class_stylebox.md#class-stylebox) remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

[StyleBox](class_stylebox.md#class-stylebox) **normal**

Sets the [StyleBox](class_stylebox.md#class-stylebox) of this **TextEdit**.

---

[StyleBox](class_stylebox.md#class-stylebox) **read_only**

Sets the [StyleBox](class_stylebox.md#class-stylebox) of this **TextEdit** when editable is disabled.
