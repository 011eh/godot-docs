# CodeEdit

**Inherits:** [TextEdit](class_textedit.md#class-textedit) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A multiline text editor designed for editing code.

## Description

CodeEdit is a specialized [TextEdit](class_textedit.md#class-textedit) designed for editing plain text code files. It has many features commonly found in code editors such as line numbers, line folding, code completion, indent management, and string/comment management.

**Note:** Regardless of locale, **CodeEdit** will by default always use left-to-right text direction to correctly display source code.

## Properties

| [bool](class_bool.md#class-bool)                                            | auto_brace_completion_enabled                       | `false`                                                                              |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                            | auto_brace_completion_highlight_matching | `false`                                                                              |
| [Dictionary](class_dictionary.md#class-dictionary)                          | auto_brace_completion_pairs                           | `{ "\"": "\"", "'": "'", "(": ")", "[": "]", "{": "}" }`                             |
| [bool](class_bool.md#class-bool)                                            | code_completion_enabled                                   | `false`                                                                              |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)] | code_completion_prefixes                                 | `[]`                                                                                 |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)] | delimiter_comments                                             | `[]`                                                                                 |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)] | delimiter_strings                                               | `["' '", "\" \""]`                                                                   |
| [bool](class_bool.md#class-bool)                                            | gutters_draw_bookmarks                                     | `false`                                                                              |
| [bool](class_bool.md#class-bool)                                            | gutters_draw_breakpoints_gutter                   | `false`                                                                              |
| [bool](class_bool.md#class-bool)                                            | gutters_draw_executing_lines                         | `false`                                                                              |
| [bool](class_bool.md#class-bool)                                            | gutters_draw_fold_gutter                                 | `false`                                                                              |
| [bool](class_bool.md#class-bool)                                            | gutters_draw_line_numbers                               | `false`                                                                              |
| [int](class_int.md#class-int)                                               | gutters_line_numbers_min_digits                   | `3`                                                                                  |
| [bool](class_bool.md#class-bool)                                            | gutters_zero_pad_line_numbers                       | `false`                                                                              |
| [bool](class_bool.md#class-bool)                                            | indent_automatic                                                 | `false`                                                                              |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)] | indent_automatic_prefixes                               | `[":", "{", "[", "("]`                                                               |
| [int](class_int.md#class-int)                                               | indent_size                                                           | `4`                                                                                  |
| [bool](class_bool.md#class-bool)                                            | indent_use_spaces                                               | `false`                                                                              |
| [LayoutDirection](class_control.md#enum-control-layoutdirection)            | layout_direction                                                                                              | `2` (overrides [Control](class_control.md#class-control-property-layout-direction))  |
| [bool](class_bool.md#class-bool)                                            | line_folding                                                         | `false`                                                                              |
| [Array](class_array.md#class-array)[[int](class_int.md#class-int)]          | line_length_guidelines                                     | `[]`                                                                                 |
| [bool](class_bool.md#class-bool)                                            | symbol_lookup_on_click                                     | `false`                                                                              |
| [bool](class_bool.md#class-bool)                                            | symbol_tooltip_on_hover                                   | `false`                                                                              |
| [TextDirection](class_control.md#enum-control-textdirection)                | text_direction                                                                                                | `1` (overrides [TextEdit](class_textedit.md#class-textedit-property-text-direction)) |

## Methods

|                                                                                         | \_confirm_code_completion(replace: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_filter_code_completion_candidates(candidates: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)])                                                                                                                                                                                                                                                                                       |
|                                                                                         | \_request_code_completion(force: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | add_auto_brace_completion_pair(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                        |
|                                                                                         | add_code_completion_option(type: CodeCompletionKind, display_text: [String](class_string.md#class-string), insert_text: [String](class_string.md#class-string), text_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), icon: [Resource](class_resource.md#class-resource) = null, value: [Variant](class_variant.md#class-variant) = null, location: [int](class_int.md#class-int) = 1024) |
|                                                                                         | add_comment_delimiter(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string), line_only: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                     |
|                                                                                         | add_string_delimiter(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string), line_only: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | can_fold_line(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | cancel_code_completion()                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | clear_bookmarked_lines()                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | clear_breakpointed_lines()                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | clear_comment_delimiters()                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | clear_executing_lines()                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | clear_string_delimiters()                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | confirm_code_completion(replace: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | convert_indent(from_line: [int](class_int.md#class-int) = -1, to_line: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | create_code_region()                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | delete_lines()                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | do_indent()                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | duplicate_lines()                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | duplicate_selection()                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | fold_all_lines()                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | fold_line(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [String](class_string.md#class-string)                                                  | get_auto_brace_completion_close_key(open_key: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | get_bookmarked_lines()                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | get_breakpointed_lines()                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | get_code_completion_option(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                              |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | get_code_completion_options()                                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                           | get_code_completion_selected_index()                                                                                                                                                                                                                                                                                                                                                                                                  |
| [String](class_string.md#class-string)                                                  | get_code_region_end_tag()                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | get_code_region_start_tag()                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [String](class_string.md#class-string)                                                  | get_delimiter_end_key(delimiter_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                              |
| [Vector2](class_vector2.md#class-vector2)                                               | get_delimiter_end_position(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | get_delimiter_start_key(delimiter_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                          |
| [Vector2](class_vector2.md#class-vector2)                                               | get_delimiter_start_position(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                    |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | get_executing_lines()                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Array](class_array.md#class-array)[[int](class_int.md#class-int)]                      | get_folded_lines()                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [String](class_string.md#class-string)                                                  | get_text_for_code_completion()                                                                                                                                                                                                                                                                                                                                                                                                              |
| [String](class_string.md#class-string)                                                  | get_text_for_symbol_lookup()                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [String](class_string.md#class-string)                                                  | get_text_with_cursor_char(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | has_auto_brace_completion_close_key(close_key: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | has_auto_brace_completion_open_key(open_key: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | has_comment_delimiter(start_key: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                        | has_string_delimiter(start_key: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | indent_lines()                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | is_in_comment(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | is_in_string(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | is_line_bookmarked(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | is_line_breakpointed(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                        | is_line_code_region_end(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | is_line_code_region_start(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | is_line_executing(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | is_line_folded(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | join_lines(line_ending: [String](class_string.md#class-string) = " ")                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | move_lines_down()                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | move_lines_up()                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | remove_comment_delimiter(start_key: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | remove_string_delimiter(start_key: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | request_code_completion(force: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | set_code_completion_selected_index(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | set_code_hint(code_hint: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | set_code_hint_draw_below(draw_below: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | set_code_region_tags(start: [String](class_string.md#class-string) = "region", end: [String](class_string.md#class-string) = "endregion")                                                                                                                                                                                                                                                                                                           |
|                                                                                         | set_line_as_bookmarked(line: [int](class_int.md#class-int), bookmarked: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | set_line_as_breakpoint(line: [int](class_int.md#class-int), breakpointed: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | set_line_as_executing(line: [int](class_int.md#class-int), executing: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | set_symbol_lookup_word_as_valid(valid: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | toggle_foldable_line(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | toggle_foldable_lines_at_carets()                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | unfold_all_lines()                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | unfold_line(line: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | unindent_lines()                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | update_code_completion_options(force: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                   |

## Theme Properties

| [Color](class_color.md#class-color)             | bookmark_color                                   | `Color(0.5, 0.64, 1, 0.8)`      |
|-------------------------------------------------|------------------------------------------------------------------------------------------------|---------------------------------|
| [Color](class_color.md#class-color)             | brace_mismatch_color                       | `Color(1, 0.2, 0.2, 1)`         |
| [Color](class_color.md#class-color)             | breakpoint_color                               | `Color(0.9, 0.29, 0.3, 1)`      |
| [Color](class_color.md#class-color)             | code_folding_color                           | `Color(0.8, 0.8, 0.8, 0.8)`     |
| [Color](class_color.md#class-color)             | completion_background_color         | `Color(0.17, 0.16, 0.2, 1)`     |
| [Color](class_color.md#class-color)             | completion_existing_color             | `Color(0.87, 0.87, 0.87, 0.13)` |
| [Color](class_color.md#class-color)             | completion_scroll_color                 | `Color(1, 1, 1, 0.29)`          |
| [Color](class_color.md#class-color)             | completion_scroll_hovered_color | `Color(1, 1, 1, 0.4)`           |
| [Color](class_color.md#class-color)             | completion_selected_color             | `Color(0.26, 0.26, 0.27, 1)`    |
| [Color](class_color.md#class-color)             | executing_line_color                       | `Color(0.98, 0.89, 0.27, 1)`    |
| [Color](class_color.md#class-color)             | folded_code_region_color               | `Color(0.68, 0.46, 0.77, 0.2)`  |
| [Color](class_color.md#class-color)             | line_length_guideline_color         | `Color(0.3, 0.5, 0.8, 0.1)`     |
| [Color](class_color.md#class-color)             | line_number_color                             | `Color(0.67, 0.67, 0.67, 0.4)`  |
| [int](class_int.md#class-int)                   | completion_lines                            | `7`                             |
| [int](class_int.md#class-int)                   | completion_max_width                    | `50`                            |
| [int](class_int.md#class-int)                   | completion_scroll_width              | `6`                             |
| [Texture2D](class_texture2d.md#class-texture2d) | bookmark                                                |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | breakpoint                                            |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | can_fold                                                |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | can_fold_code_region                        |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | completion_color_bg                          |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | executing_line                                    |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | folded                                                    |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | folded_code_region                            |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | folded_eol_icon                                  |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | completion                                           |                                 |

---

## Signals

**breakpoint_toggled**(line: [int](class_int.md#class-int))

Emitted when a breakpoint is added or removed from a line. If the line is removed via backspace, a signal is emitted at the old line.

---

**code_completion_requested**()

Emitted when the user requests code completion. This signal will not be sent if \_request_code_completion() is overridden or code_completion_enabled is `false`.

---

**symbol_hovered**(symbol: [String](class_string.md#class-string), line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Emitted when the user hovers over a symbol. Unlike [Control.mouse_entered](class_control.md#class-control-signal-mouse-entered), this signal is not emitted immediately, but when the cursor is over the symbol for [ProjectSettings.gui/timers/tooltip_delay_sec](class_projectsettings.md#class-projectsettings-property-gui-timers-tooltip-delay-sec) seconds.

**Note:** symbol_tooltip_on_hover must be `true` for this signal to be emitted.

---

**symbol_lookup**(symbol: [String](class_string.md#class-string), line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Emitted when the user has clicked on a valid symbol.

---

**symbol_validate**(symbol: [String](class_string.md#class-string))

Emitted when the user hovers over a symbol. The symbol should be validated and responded to, by calling set_symbol_lookup_word_as_valid().

**Note:** symbol_lookup_on_click must be `true` for this signal to be emitted.

---

## Enumerations

enum **CodeCompletionKind**:

CodeCompletionKind **KIND_CLASS** = `0`

Marks the option as a class.

CodeCompletionKind **KIND_FUNCTION** = `1`

Marks the option as a function.

CodeCompletionKind **KIND_SIGNAL** = `2`

Marks the option as a Godot signal.

CodeCompletionKind **KIND_VARIABLE** = `3`

Marks the option as a variable.

CodeCompletionKind **KIND_MEMBER** = `4`

Marks the option as a member.

CodeCompletionKind **KIND_ENUM** = `5`

Marks the option as an enum entry.

CodeCompletionKind **KIND_CONSTANT** = `6`

Marks the option as a constant.

CodeCompletionKind **KIND_NODE_PATH** = `7`

Marks the option as a Godot node path.

CodeCompletionKind **KIND_FILE_PATH** = `8`

Marks the option as a file path.

CodeCompletionKind **KIND_PLAIN_TEXT** = `9`

Marks the option as unclassified or plain text.

CodeCompletionKind **KIND_KEYWORD** = `10`

Marks the option as a keyword.

---

enum **CodeCompletionLocation**:

CodeCompletionLocation **LOCATION_LOCAL** = `0`

The option is local to the location of the code completion query - e.g. a local variable. Subsequent value of location represent options from the outer class, the exact value represent how far they are (in terms of inner classes).

CodeCompletionLocation **LOCATION_PARENT_MASK** = `256`

The option is from the containing class or a parent class, relative to the location of the code completion query. Perform a bitwise OR with the class depth (e.g. `0` for the local class, `1` for the parent, `2` for the grandparent, etc.) to store the depth of an option in the class or a parent class.

CodeCompletionLocation **LOCATION_OTHER_USER_CODE** = `512`

The option is from user code which is not local and not in a derived class (e.g. Autoload Singletons).

CodeCompletionLocation **LOCATION_OTHER** = `1024`

The option is from other engine code, not covered by the other enum constants - e.g. built-in classes.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **auto_brace_completion_enabled** = `false`

-  **set_auto_brace_completion_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_auto_brace_completion_enabled**()

If `true`, uses auto_brace_completion_pairs to automatically insert the closing brace when the opening brace is inserted by typing or autocompletion. Also automatically removes the closing brace when using backspace on the opening brace.

---

[bool](class_bool.md#class-bool) **auto_brace_completion_highlight_matching** = `false`

-  **set_highlight_matching_braces_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_highlight_matching_braces_enabled**()

If `true`, highlights brace pairs when the caret is on either one, using auto_brace_completion_pairs. If matching, the pairs will be underlined. If a brace is unmatched, it is colored with brace_mismatch_color.

---

[Dictionary](class_dictionary.md#class-dictionary) **auto_brace_completion_pairs** = `{ "\"": "\"", "'": "'", "(": ")", "[": "]", "{": "}" }`

-  **set_auto_brace_completion_pairs**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_auto_brace_completion_pairs**()

Sets the brace pairs to be autocompleted. For each entry in the dictionary, the key is the opening brace and the value is the closing brace that matches it. A brace is a [String](class_string.md#class-string) made of symbols. See auto_brace_completion_enabled and auto_brace_completion_highlight_matching.

---

[bool](class_bool.md#class-bool) **code_completion_enabled** = `false`

-  **set_code_completion_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_code_completion_enabled**()

If `true`, the [ProjectSettings.input/ui_text_completion_query](class_projectsettings.md#class-projectsettings-property-input-ui-text-completion-query) action requests code completion. To handle it, see \_request_code_completion() or code_completion_requested.

---

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **code_completion_prefixes** = `[]`

-  **set_code_completion_prefixes**(value: [Array](class_array.md#class-array)[[String](class_string.md#class-string)])
- [Array](class_array.md#class-array)[[String](class_string.md#class-string)] **get_code_completion_prefixes**()

Sets prefixes that will trigger code completion.

---

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **delimiter_comments** = `[]`

-  **set_comment_delimiters**(value: [Array](class_array.md#class-array)[[String](class_string.md#class-string)])
- [Array](class_array.md#class-array)[[String](class_string.md#class-string)] **get_comment_delimiters**()

Sets the comment delimiters. All existing comment delimiters will be removed.

---

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **delimiter_strings** = `["' '", "\" \""]`

-  **set_string_delimiters**(value: [Array](class_array.md#class-array)[[String](class_string.md#class-string)])
- [Array](class_array.md#class-array)[[String](class_string.md#class-string)] **get_string_delimiters**()

Sets the string delimiters. All existing string delimiters will be removed.

---

[bool](class_bool.md#class-bool) **gutters_draw_bookmarks** = `false`

-  **set_draw_bookmarks_gutter**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drawing_bookmarks_gutter**()

If `true`, bookmarks are drawn in the gutter. This gutter is shared with breakpoints and executing lines. See set_line_as_bookmarked().

---

[bool](class_bool.md#class-bool) **gutters_draw_breakpoints_gutter** = `false`

-  **set_draw_breakpoints_gutter**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drawing_breakpoints_gutter**()

If `true`, breakpoints are drawn in the gutter. This gutter is shared with bookmarks and executing lines. Clicking the gutter will toggle the breakpoint for the line, see set_line_as_breakpoint().

---

[bool](class_bool.md#class-bool) **gutters_draw_executing_lines** = `false`

-  **set_draw_executing_lines_gutter**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drawing_executing_lines_gutter**()

If `true`, executing lines are marked in the gutter. This gutter is shared with breakpoints and bookmarks. See set_line_as_executing().

---

[bool](class_bool.md#class-bool) **gutters_draw_fold_gutter** = `false`

-  **set_draw_fold_gutter**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_drawing_fold_gutter**()

If `true`, the fold gutter is drawn. In this gutter, the can_fold_code_region icon is drawn for each foldable line (see can_fold_line()) and the folded_code_region icon is drawn for each folded line (see is_line_folded()). These icons can be clicked to toggle the fold state, see toggle_foldable_line(). line_folding must be `true` to show icons.

---

[bool](class_bool.md#class-bool) **gutters_draw_line_numbers** = `false`

-  **set_draw_line_numbers**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_line_numbers_enabled**()

If `true`, the line number gutter is drawn. Line numbers start at `1` and are incremented for each line of text. Clicking and dragging in the line number gutter will select entire lines of text.

---

[int](class_int.md#class-int) **gutters_line_numbers_min_digits** = `3`

-  **set_line_numbers_min_digits**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_line_numbers_min_digits**()

The minimum width in digits reserved for the line number gutter.

---

[bool](class_bool.md#class-bool) **gutters_zero_pad_line_numbers** = `false`

-  **set_line_numbers_zero_padded**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_line_numbers_zero_padded**()

If `true`, line numbers drawn in the gutter are zero padded based on the total line count. Requires gutters_draw_line_numbers to be set to `true`.

---

[bool](class_bool.md#class-bool) **indent_automatic** = `false`

-  **set_auto_indent_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_auto_indent_enabled**()

If `true`, an extra indent is automatically inserted when a new line is added and a prefix in indent_automatic_prefixes is found. If a brace pair opening key is found, the matching closing brace will be moved to another new line (see auto_brace_completion_pairs).

---

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **indent_automatic_prefixes** = `[":", "{", "[", "("]`

-  **set_auto_indent_prefixes**(value: [Array](class_array.md#class-array)[[String](class_string.md#class-string)])
- [Array](class_array.md#class-array)[[String](class_string.md#class-string)] **get_auto_indent_prefixes**()

Prefixes to trigger an automatic indent. Used when indent_automatic is set to `true`.

---

[int](class_int.md#class-int) **indent_size** = `4`

-  **set_indent_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_indent_size**()

Size of the tabulation indent (one `Tab` press) in characters. If indent_use_spaces is enabled the number of spaces to use.

---

[bool](class_bool.md#class-bool) **indent_use_spaces** = `false`

-  **set_indent_using_spaces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_indent_using_spaces**()

Use spaces instead of tabs for indentation.

---

[bool](class_bool.md#class-bool) **line_folding** = `false`

-  **set_line_folding_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_line_folding_enabled**()

If `true`, lines can be folded. Otherwise, line folding methods like fold_line() will not work and can_fold_line() will always return `false`. See gutters_draw_fold_gutter.

---

[Array](class_array.md#class-array)[[int](class_int.md#class-int)] **line_length_guidelines** = `[]`

-  **set_line_length_guidelines**(value: [Array](class_array.md#class-array)[[int](class_int.md#class-int)])
- [Array](class_array.md#class-array)[[int](class_int.md#class-int)] **get_line_length_guidelines**()

Draws vertical lines at the provided columns. The first entry is considered a main hard guideline and is drawn more prominently.

---

[bool](class_bool.md#class-bool) **symbol_lookup_on_click** = `false`

-  **set_symbol_lookup_on_click_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_symbol_lookup_on_click_enabled**()

Set when a validated word from symbol_validate is clicked, the symbol_lookup should be emitted.

---

[bool](class_bool.md#class-bool) **symbol_tooltip_on_hover** = `false`

-  **set_symbol_tooltip_on_hover_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_symbol_tooltip_on_hover_enabled**()

If `true`, the symbol_hovered signal is emitted when hovering over a word.

---

## Method Descriptions

 **\_confirm_code_completion**(replace: [bool](class_bool.md#class-bool))

Override this method to define how the selected entry should be inserted. If `replace` is `true`, any existing text should be replaced.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_filter_code_completion_candidates**(candidates: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)])

Override this method to define what items in `candidates` should be displayed.

Both `candidates` and the return is an [Array](class_array.md#class-array) of [Dictionary](class_dictionary.md#class-dictionary), see get_code_completion_option() for [Dictionary](class_dictionary.md#class-dictionary) content.

---

 **\_request_code_completion**(force: [bool](class_bool.md#class-bool))

Override this method to define what happens when the user requests code completion. If `force` is `true`, any checks should be bypassed.

---

 **add_auto_brace_completion_pair**(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string))

Adds a brace pair.

Both the start and end keys must be symbols. Only the start key has to be unique.

---

 **add_code_completion_option**(type: CodeCompletionKind, display_text: [String](class_string.md#class-string), insert_text: [String](class_string.md#class-string), text_color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), icon: [Resource](class_resource.md#class-resource) = null, value: [Variant](class_variant.md#class-variant) = null, location: [int](class_int.md#class-int) = 1024)

Submits an item to the queue of potential candidates for the autocomplete menu. Call update_code_completion_options() to update the list.

`location` indicates location of the option relative to the location of the code completion query. See CodeCompletionLocation for how to set this value.

**Note:** This list will replace all current candidates.

---

 **add_comment_delimiter**(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string), line_only: [bool](class_bool.md#class-bool) = false)

Adds a comment delimiter from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty [String](class_string.md#class-string), the region does not carry over to the next line.

---

 **add_string_delimiter**(start_key: [String](class_string.md#class-string), end_key: [String](class_string.md#class-string), line_only: [bool](class_bool.md#class-bool) = false)

Defines a string delimiter from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty [String](class_string.md#class-string), the region does not carry over to the next line.

---

[bool](class_bool.md#class-bool) **can_fold_line**(line: [int](class_int.md#class-int))

Returns `true` if the given line is foldable. A line is foldable if it is the start of a valid code region (see get_code_region_start_tag()), if it is the start of a comment or string block, or if the next non-empty line is more indented (see [TextEdit.get_indent_level()](class_textedit.md#class-textedit-method-get-indent-level)).

---

 **cancel_code_completion**()

Cancels the autocomplete menu.

---

 **clear_bookmarked_lines**()

Clears all bookmarked lines.

---

 **clear_breakpointed_lines**()

Clears all breakpointed lines.

---

 **clear_comment_delimiters**()

Removes all comment delimiters.

---

 **clear_executing_lines**()

Clears all executed lines.

---

 **clear_string_delimiters**()

Removes all string delimiters.

---

 **confirm_code_completion**(replace: [bool](class_bool.md#class-bool) = false)

Inserts the selected entry into the text. If `replace` is `true`, any existing text is replaced rather than merged.

---

 **convert_indent**(from_line: [int](class_int.md#class-int) = -1, to_line: [int](class_int.md#class-int) = -1)

Converts the indents of lines between `from_line` and `to_line` to tabs or spaces as set by indent_use_spaces.

Values of `-1` convert the entire text.

---

 **create_code_region**()

Creates a new code region with the selection. At least one single line comment delimiter have to be defined (see add_comment_delimiter()).

A code region is a part of code that is highlighted when folded and can help organize your script.

Code region start and end tags can be customized (see set_code_region_tags()).

Code regions are delimited using start and end tags (respectively `region` and `endregion` by default) preceded by one line comment delimiter. (eg. `#region` and `#endregion`)

---

 **delete_lines**()

Deletes all lines that are selected or have a caret on them.

---

 **do_indent**()

If there is no selection, indentation is inserted at the caret. Otherwise, the selected lines are indented like indent_lines(). Equivalent to the [ProjectSettings.input/ui_text_indent](class_projectsettings.md#class-projectsettings-property-input-ui-text-indent) action. The indentation characters used depend on indent_use_spaces and indent_size.

---

 **duplicate_lines**()

Duplicates all lines currently selected with any caret. Duplicates the entire line beneath the current one no matter where the caret is within the line.

---

 **duplicate_selection**()

Duplicates all selected text and duplicates all lines with a caret on them.

---

 **fold_all_lines**()

Folds all lines that are possible to be folded (see can_fold_line()).

---

 **fold_line**(line: [int](class_int.md#class-int))

Folds the given line, if possible (see can_fold_line()).

---

[String](class_string.md#class-string) **get_auto_brace_completion_close_key**(open_key: [String](class_string.md#class-string))

Gets the matching auto brace close key for `open_key`.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_bookmarked_lines**()

Gets all bookmarked lines.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_breakpointed_lines**()

Gets all breakpointed lines.

---

[Dictionary](class_dictionary.md#class-dictionary) **get_code_completion_option**(index: [int](class_int.md#class-int))

Gets the completion option at `index`. The return [Dictionary](class_dictionary.md#class-dictionary) has the following key-values:

`kind`: CodeCompletionKind

`display_text`: Text that is shown on the autocomplete menu.

`insert_text`: Text that is to be inserted when this item is selected.

`font_color`: Color of the text on the autocomplete menu.

`icon`: Icon to draw on the autocomplete menu.

`default_value`: Value of the symbol.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_code_completion_options**()

Gets all completion options, see get_code_completion_option() for return content.

---

[int](class_int.md#class-int) **get_code_completion_selected_index**()

Gets the index of the current selected completion option.

---

[String](class_string.md#class-string) **get_code_region_end_tag**()

Returns the code region end tag (without comment delimiter).

---

[String](class_string.md#class-string) **get_code_region_start_tag**()

Returns the code region start tag (without comment delimiter).

---

[String](class_string.md#class-string) **get_delimiter_end_key**(delimiter_index: [int](class_int.md#class-int))

Gets the end key for a string or comment region index.

---

[Vector2](class_vector2.md#class-vector2) **get_delimiter_end_position**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

If `line` `column` is in a string or comment, returns the end position of the region. If not or no end could be found, both [Vector2](class_vector2.md#class-vector2) values will be `-1`.

---

[String](class_string.md#class-string) **get_delimiter_start_key**(delimiter_index: [int](class_int.md#class-int))

Gets the start key for a string or comment region index.

---

[Vector2](class_vector2.md#class-vector2) **get_delimiter_start_position**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

If `line` `column` is in a string or comment, returns the start position of the region. If not or no start could be found, both [Vector2](class_vector2.md#class-vector2) values will be `-1`.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_executing_lines**()

Gets all executing lines.

---

[Array](class_array.md#class-array)[[int](class_int.md#class-int)] **get_folded_lines**()

Returns all lines that are currently folded.

---

[String](class_string.md#class-string) **get_text_for_code_completion**()

Returns the full text with char `0xFFFF` at the caret location.

---

[String](class_string.md#class-string) **get_text_for_symbol_lookup**()

Returns the full text with char `0xFFFF` at the cursor location.

---

[String](class_string.md#class-string) **get_text_with_cursor_char**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

Returns the full text with char `0xFFFF` at the specified location.

---

[bool](class_bool.md#class-bool) **has_auto_brace_completion_close_key**(close_key: [String](class_string.md#class-string))

Returns `true` if close key `close_key` exists.

---

[bool](class_bool.md#class-bool) **has_auto_brace_completion_open_key**(open_key: [String](class_string.md#class-string))

Returns `true` if open key `open_key` exists.

---

[bool](class_bool.md#class-bool) **has_comment_delimiter**(start_key: [String](class_string.md#class-string))

Returns `true` if comment `start_key` exists.

---

[bool](class_bool.md#class-bool) **has_string_delimiter**(start_key: [String](class_string.md#class-string))

Returns `true` if string `start_key` exists.

---

 **indent_lines**()

Indents all lines that are selected or have a caret on them. Uses spaces or a tab depending on indent_use_spaces. See unindent_lines().

---

[int](class_int.md#class-int) **is_in_comment**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int) = -1)

Returns delimiter index if `line` `column` is in a comment. If `column` is not provided, will return delimiter index if the entire `line` is a comment. Otherwise `-1`.

---

[int](class_int.md#class-int) **is_in_string**(line: [int](class_int.md#class-int), column: [int](class_int.md#class-int) = -1)

Returns the delimiter index if `line` `column` is in a string. If `column` is not provided, will return the delimiter index if the entire `line` is a string. Otherwise `-1`.

---

[bool](class_bool.md#class-bool) **is_line_bookmarked**(line: [int](class_int.md#class-int))

Returns `true` if the given line is bookmarked. See set_line_as_bookmarked().

---

[bool](class_bool.md#class-bool) **is_line_breakpointed**(line: [int](class_int.md#class-int))

Returns `true` if the given line is breakpointed. See set_line_as_breakpoint().

---

[bool](class_bool.md#class-bool) **is_line_code_region_end**(line: [int](class_int.md#class-int))

Returns `true` if the given line is a code region end. See set_code_region_tags().

---

[bool](class_bool.md#class-bool) **is_line_code_region_start**(line: [int](class_int.md#class-int))

Returns `true` if the given line is a code region start. See set_code_region_tags().

---

[bool](class_bool.md#class-bool) **is_line_executing**(line: [int](class_int.md#class-int))

Returns `true` if the given line is marked as executing. See set_line_as_executing().

---

[bool](class_bool.md#class-bool) **is_line_folded**(line: [int](class_int.md#class-int))

Returns `true` if the given line is folded. See fold_line().

---

 **join_lines**(line_ending: [String](class_string.md#class-string) = " ")

Joins all selected lines or lines containing a caret with their next line. Whitespace in between will be removed. If the next line has content, the `line_ending` will be inserted in between.

---

 **move_lines_down**()

Moves all lines down that are selected or have a caret on them.

---

 **move_lines_up**()

Moves all lines up that are selected or have a caret on them.

---

 **remove_comment_delimiter**(start_key: [String](class_string.md#class-string))

Removes the comment delimiter with `start_key`.

---

 **remove_string_delimiter**(start_key: [String](class_string.md#class-string))

Removes the string delimiter with `start_key`.

---

 **request_code_completion**(force: [bool](class_bool.md#class-bool) = false)

Emits code_completion_requested, if `force` is `true` will bypass all checks. Otherwise will check that the caret is in a word or in front of a prefix. Will ignore the request if all current options are of type file path, node path, or signal.

---

 **set_code_completion_selected_index**(index: [int](class_int.md#class-int))

Sets the current selected completion option.

---

 **set_code_hint**(code_hint: [String](class_string.md#class-string))

Sets the code hint text. Pass an empty string to clear.

---

 **set_code_hint_draw_below**(draw_below: [bool](class_bool.md#class-bool))

If `true`, the code hint will draw below the main caret. If `false`, the code hint will draw above the main caret. See set_code_hint().

---

 **set_code_region_tags**(start: [String](class_string.md#class-string) = "region", end: [String](class_string.md#class-string) = "endregion")

Sets the code region start and end tags (without comment delimiter).

---

 **set_line_as_bookmarked**(line: [int](class_int.md#class-int), bookmarked: [bool](class_bool.md#class-bool))

Sets the given line as bookmarked. If `true` and gutters_draw_bookmarks is `true`, draws the bookmark icon in the gutter for this line. See get_bookmarked_lines() and is_line_bookmarked().

---

 **set_line_as_breakpoint**(line: [int](class_int.md#class-int), breakpointed: [bool](class_bool.md#class-bool))

Sets the given line as a breakpoint. If `true` and gutters_draw_breakpoints_gutter is `true`, draws the breakpoint icon in the gutter for this line. See get_breakpointed_lines() and is_line_breakpointed().

---

 **set_line_as_executing**(line: [int](class_int.md#class-int), executing: [bool](class_bool.md#class-bool))

Sets the given line as executing. If `true` and gutters_draw_executing_lines is `true`, draws the executing_line icon in the gutter for this line. See get_executing_lines() and is_line_executing().

---

 **set_symbol_lookup_word_as_valid**(valid: [bool](class_bool.md#class-bool))

Sets the symbol emitted by symbol_validate as a valid lookup.

---

 **toggle_foldable_line**(line: [int](class_int.md#class-int))

Toggle the folding of the code block at the given line.

---

 **toggle_foldable_lines_at_carets**()

Toggle the folding of the code block on all lines with a caret on them.

---

 **unfold_all_lines**()

Unfolds all lines that are folded.

---

 **unfold_line**(line: [int](class_int.md#class-int))

Unfolds the given line if it is folded or if it is hidden under a folded line.

---

 **unindent_lines**()

Unindents all lines that are selected or have a caret on them. Uses spaces or a tab depending on indent_use_spaces. Equivalent to the [ProjectSettings.input/ui_text_dedent](class_projectsettings.md#class-projectsettings-property-input-ui-text-dedent) action. See indent_lines().

---

 **update_code_completion_options**(force: [bool](class_bool.md#class-bool))

Submits all completion options added with add_code_completion_option(). Will try to force the autocomplete menu to popup, if `force` is `true`.

**Note:** This will replace all current candidates.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **bookmark_color** = `Color(0.5, 0.64, 1, 0.8)`

[Color](class_color.md#class-color) of the bookmark icon for bookmarked lines.

---

[Color](class_color.md#class-color) **brace_mismatch_color** = `Color(1, 0.2, 0.2, 1)`

[Color](class_color.md#class-color) of the text to highlight mismatched braces.

---

[Color](class_color.md#class-color) **breakpoint_color** = `Color(0.9, 0.29, 0.3, 1)`

[Color](class_color.md#class-color) of the breakpoint icon for bookmarked lines.

---

[Color](class_color.md#class-color) **code_folding_color** = `Color(0.8, 0.8, 0.8, 0.8)`

[Color](class_color.md#class-color) for all icons related to line folding.

---

[Color](class_color.md#class-color) **completion_background_color** = `Color(0.17, 0.16, 0.2, 1)`

Sets the background [Color](class_color.md#class-color) for the code completion popup.

---

[Color](class_color.md#class-color) **completion_existing_color** = `Color(0.87, 0.87, 0.87, 0.13)`

Background highlight [Color](class_color.md#class-color) for matching text in code completion options.

---

[Color](class_color.md#class-color) **completion_scroll_color** = `Color(1, 1, 1, 0.29)`

[Color](class_color.md#class-color) of the scrollbar in the code completion popup.

---

[Color](class_color.md#class-color) **completion_scroll_hovered_color** = `Color(1, 1, 1, 0.4)`

[Color](class_color.md#class-color) of the scrollbar in the code completion popup when hovered.

---

[Color](class_color.md#class-color) **completion_selected_color** = `Color(0.26, 0.26, 0.27, 1)`

Background highlight [Color](class_color.md#class-color) for the current selected option item in the code completion popup.

---

[Color](class_color.md#class-color) **executing_line_color** = `Color(0.98, 0.89, 0.27, 1)`

[Color](class_color.md#class-color) of the executing icon for executing lines.

---

[Color](class_color.md#class-color) **folded_code_region_color** = `Color(0.68, 0.46, 0.77, 0.2)`

[Color](class_color.md#class-color) of background line highlight for folded code region.

---

[Color](class_color.md#class-color) **line_length_guideline_color** = `Color(0.3, 0.5, 0.8, 0.1)`

[Color](class_color.md#class-color) of the main line length guideline, secondary guidelines will have 50% alpha applied.

---

[Color](class_color.md#class-color) **line_number_color** = `Color(0.67, 0.67, 0.67, 0.4)`

Sets the [Color](class_color.md#class-color) of line numbers.

---

[int](class_int.md#class-int) **completion_lines** = `7`

Max number of options to display in the code completion popup at any one time.

---

[int](class_int.md#class-int) **completion_max_width** = `50`

Max width of options in the code completion popup. Options longer than this will be cut off.

---

[int](class_int.md#class-int) **completion_scroll_width** = `6`

Width of the scrollbar in the code completion popup.

---

[Texture2D](class_texture2d.md#class-texture2d) **bookmark**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) to draw in the bookmark gutter for bookmarked lines.

---

[Texture2D](class_texture2d.md#class-texture2d) **breakpoint**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) to draw in the breakpoint gutter for breakpointed lines.

---

[Texture2D](class_texture2d.md#class-texture2d) **can_fold**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) to draw in the line folding gutter when a line can be folded.

---

[Texture2D](class_texture2d.md#class-texture2d) **can_fold_code_region**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) to draw in the line folding gutter when a code region can be folded.

---

[Texture2D](class_texture2d.md#class-texture2d) **completion_color_bg**

Background panel for the color preview box in autocompletion (visible when the color is translucent).

---

[Texture2D](class_texture2d.md#class-texture2d) **executing_line**

Icon to draw in the executing gutter for executing lines.

---

[Texture2D](class_texture2d.md#class-texture2d) **folded**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) to draw in the line folding gutter when a line is folded and can be unfolded.

---

[Texture2D](class_texture2d.md#class-texture2d) **folded_code_region**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) to draw in the line folding gutter when a code region is folded and can be unfolded.

---

[Texture2D](class_texture2d.md#class-texture2d) **folded_eol_icon**

Sets a custom [Texture2D](class_texture2d.md#class-texture2d) to draw at the end of a folded line.

---

[StyleBox](class_stylebox.md#class-stylebox) **completion**

[StyleBox](class_stylebox.md#class-stylebox) for the code completion popup.
