# DisplayServer

**Inherits:** [Object](class_object.md#class-object)

A server interface for low-level window management.

## Description

**DisplayServer** handles everything related to window management. It is separated from [OS](class_os.md#class-os) as a single operating system may support multiple display servers.

**Headless mode:** Starting the engine with the `--headless` [command line argument](../tutorials/editor/command_line_tutorial.md) disables all rendering and window management functions. Most functions from **DisplayServer** will return dummy values in this case.

## Methods

| [RID](class_rid.md#class-rid)                                                           | accessibility_create_element(window_id: [int](class_int.md#class-int), role: AccessibilityRole)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)                                                           | accessibility_create_sub_element(parent_rid: [RID](class_rid.md#class-rid), role: AccessibilityRole, insert_pos: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [RID](class_rid.md#class-rid)                                                           | accessibility_create_sub_text_edit_elements(parent_rid: [RID](class_rid.md#class-rid), shaped_text: [RID](class_rid.md#class-rid), min_height: [float](class_float.md#class-float), insert_pos: [int](class_int.md#class-int) = -1, is_last_line: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                           |
| [Variant](class_variant.md#class-variant)                                               | accessibility_element_get_meta(id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | accessibility_element_set_meta(id: [RID](class_rid.md#class-rid), meta: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | accessibility_free_element(id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                                           | accessibility_get_window_root(window_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                        | accessibility_has_element(id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                                           | accessibility_screen_reader_active()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | accessibility_set_window_focused(window_id: [int](class_int.md#class-int), focused: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | accessibility_set_window_rect(window_id: [int](class_int.md#class-int), rect_out: [Rect2](class_rect2.md#class-rect2), rect_in: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                           | accessibility_should_increase_contrast()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | accessibility_should_reduce_animation()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | accessibility_should_reduce_transparency()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | accessibility_update_add_action(id: [RID](class_rid.md#class-rid), action: AccessibilityAction, callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | accessibility_update_add_child(id: [RID](class_rid.md#class-rid), child_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | accessibility_update_add_custom_action(id: [RID](class_rid.md#class-rid), action_id: [int](class_int.md#class-int), action_description: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | accessibility_update_add_related_controls(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | accessibility_update_add_related_described_by(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | accessibility_update_add_related_details(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | accessibility_update_add_related_flow_to(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | accessibility_update_add_related_labeled_by(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | accessibility_update_add_related_radio_group(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | accessibility_update_set_active_descendant(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | accessibility_update_set_background_color(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | accessibility_update_set_bounds(id: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | accessibility_update_set_checked(id: [RID](class_rid.md#class-rid), checekd: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | accessibility_update_set_classname(id: [RID](class_rid.md#class-rid), classname: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | accessibility_update_set_color_value(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | accessibility_update_set_description(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | accessibility_update_set_error_message(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | accessibility_update_set_extra_info(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | accessibility_update_set_flag(id: [RID](class_rid.md#class-rid), flag: AccessibilityFlags, value: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | accessibility_update_set_focus(id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | accessibility_update_set_foreground_color(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | accessibility_update_set_in_page_link_target(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | accessibility_update_set_language(id: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | accessibility_update_set_list_item_count(id: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | accessibility_update_set_list_item_expanded(id: [RID](class_rid.md#class-rid), expanded: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | accessibility_update_set_list_item_index(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | accessibility_update_set_list_item_level(id: [RID](class_rid.md#class-rid), level: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | accessibility_update_set_list_item_selected(id: [RID](class_rid.md#class-rid), selected: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | accessibility_update_set_list_orientation(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | accessibility_update_set_live(id: [RID](class_rid.md#class-rid), live: AccessibilityLiveMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | accessibility_update_set_member_of(id: [RID](class_rid.md#class-rid), group_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | accessibility_update_set_name(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | accessibility_update_set_next_on_line(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | accessibility_update_set_num_jump(id: [RID](class_rid.md#class-rid), jump: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | accessibility_update_set_num_range(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | accessibility_update_set_num_step(id: [RID](class_rid.md#class-rid), step: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | accessibility_update_set_num_value(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | accessibility_update_set_placeholder(id: [RID](class_rid.md#class-rid), placeholder: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | accessibility_update_set_popup_type(id: [RID](class_rid.md#class-rid), popup: AccessibilityPopupType)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | accessibility_update_set_previous_on_line(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | accessibility_update_set_role(id: [RID](class_rid.md#class-rid), role: AccessibilityRole)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | accessibility_update_set_role_description(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | accessibility_update_set_scroll_x(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | accessibility_update_set_scroll_x_range(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | accessibility_update_set_scroll_y(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | accessibility_update_set_scroll_y_range(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | accessibility_update_set_shortcut(id: [RID](class_rid.md#class-rid), shortcut: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | accessibility_update_set_state_description(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | accessibility_update_set_table_cell_position(id: [RID](class_rid.md#class-rid), row_index: [int](class_int.md#class-int), column_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | accessibility_update_set_table_cell_span(id: [RID](class_rid.md#class-rid), row_span: [int](class_int.md#class-int), column_span: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | accessibility_update_set_table_column_count(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | accessibility_update_set_table_column_index(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | accessibility_update_set_table_row_count(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | accessibility_update_set_table_row_index(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | accessibility_update_set_text_align(id: [RID](class_rid.md#class-rid), align: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | accessibility_update_set_text_decorations(id: [RID](class_rid.md#class-rid), underline: [bool](class_bool.md#class-bool), strikethrough: [bool](class_bool.md#class-bool), overline: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | accessibility_update_set_text_orientation(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | accessibility_update_set_text_selection(id: [RID](class_rid.md#class-rid), text_start_id: [RID](class_rid.md#class-rid), start_char: [int](class_int.md#class-int), text_end_id: [RID](class_rid.md#class-rid), end_char: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | accessibility_update_set_tooltip(id: [RID](class_rid.md#class-rid), tooltip: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | accessibility_update_set_transform(id: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | accessibility_update_set_url(id: [RID](class_rid.md#class-rid), url: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | accessibility_update_set_value(id: [RID](class_rid.md#class-rid), value: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | beep()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | clipboard_get()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Image](class_image.md#class-image)                                                     | clipboard_get_image()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [String](class_string.md#class-string)                                                  | clipboard_get_primary()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | clipboard_has()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | clipboard_has_image()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | clipboard_set(clipboard: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | clipboard_set_primary(clipboard_primary: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                        | color_picker(callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | create_status_indicator(icon: [Texture2D](class_texture2d.md#class-texture2d), tooltip: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CursorShape                                          | cursor_get_shape()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | cursor_set_custom_image(cursor: [Resource](class_resource.md#class-resource), shape: CursorShape = 0, hotspot: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | cursor_set_shape(shape: CursorShape)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | delete_status_indicator(id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | dialog_input_text(title: [String](class_string.md#class-string), description: [String](class_string.md#class-string), existing_text: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | dialog_show(title: [String](class_string.md#class-string), description: [String](class_string.md#class-string), buttons: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | enable_for_stealing_focus(process_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | file_dialog_show(title: [String](class_string.md#class-string), current_directory: [String](class_string.md#class-string), filename: [String](class_string.md#class-string), show_hidden: [bool](class_bool.md#class-bool), mode: FileDialogMode, filters: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), callback: [Callable](class_callable.md#class-callable), parent_window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                           |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | file_dialog_with_options_show(title: [String](class_string.md#class-string), current_directory: [String](class_string.md#class-string), root: [String](class_string.md#class-string), filename: [String](class_string.md#class-string), show_hidden: [bool](class_bool.md#class-bool), mode: FileDialogMode, filters: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), options: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)], callback: [Callable](class_callable.md#class-callable), parent_window_id: [int](class_int.md#class-int) = 0) |
|                                                                                         | force_process_and_drop_events()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Color](class_color.md#class-color)                                                     | get_accent_color()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Color](class_color.md#class-color)                                                     | get_base_color()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Array](class_array.md#class-array)[[Rect2](class_rect2.md#class-rect2)]                | get_display_cutouts()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Rect2i](class_rect2i.md#class-rect2i)                                                  | get_display_safe_area()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | get_keyboard_focus_screen()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                                                  | get_name()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                           | get_primary_screen()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                           | get_screen_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                           | get_screen_from_rect(rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | get_swap_cancel_ok()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                           | get_window_at_screen_position(position: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | get_window_list()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | global_menu_add_check_item(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                           | global_menu_add_icon_check_item(menu_root: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                                                      |
| [int](class_int.md#class-int)                                                           | global_menu_add_icon_item(menu_root: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | global_menu_add_icon_radio_check_item(menu_root: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                                          |
| [int](class_int.md#class-int)                                                           | global_menu_add_item(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | global_menu_add_multistate_item(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                    |
| [int](class_int.md#class-int)                                                           | global_menu_add_radio_check_item(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                           | global_menu_add_separator(menu_root: [String](class_string.md#class-string), index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | global_menu_add_submenu_item(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), submenu: [String](class_string.md#class-string), index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | global_menu_clear(menu_root: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Key](class_@globalscope.md#enum-globalscope-key)                                       | global_menu_get_item_accelerator(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Callable](class_callable.md#class-callable)                                            | global_menu_get_item_callback(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                           | global_menu_get_item_count(menu_root: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Texture2D](class_texture2d.md#class-texture2d)                                         | global_menu_get_item_icon(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | global_menu_get_item_indentation_level(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | global_menu_get_item_index_from_tag(menu_root: [String](class_string.md#class-string), tag: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | global_menu_get_item_index_from_text(menu_root: [String](class_string.md#class-string), text: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Callable](class_callable.md#class-callable)                                            | global_menu_get_item_key_callback(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                           | global_menu_get_item_max_states(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                                           | global_menu_get_item_state(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [String](class_string.md#class-string)                                                  | global_menu_get_item_submenu(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Variant](class_variant.md#class-variant)                                               | global_menu_get_item_tag(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [String](class_string.md#class-string)                                                  | global_menu_get_item_text(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | global_menu_get_item_tooltip(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | global_menu_get_system_menu_roots()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                        | global_menu_is_item_checkable(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                        | global_menu_is_item_checked(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | global_menu_is_item_disabled(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | global_menu_is_item_hidden(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | global_menu_is_item_radio_checkable(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | global_menu_remove_item(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | global_menu_set_item_accelerator(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), keycode: [Key](class_@globalscope.md#enum-globalscope-key))                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | global_menu_set_item_callback(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | global_menu_set_item_checkable(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | global_menu_set_item_checked(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | global_menu_set_item_disabled(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | global_menu_set_item_hidden(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | global_menu_set_item_hover_callbacks(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | global_menu_set_item_icon(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | global_menu_set_item_indentation_level(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), level: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | global_menu_set_item_key_callback(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), key_callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | global_menu_set_item_max_states(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | global_menu_set_item_radio_checkable(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | global_menu_set_item_state(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), state: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | global_menu_set_item_submenu(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), submenu: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | global_menu_set_item_tag(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), tag: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | global_menu_set_item_text(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | global_menu_set_item_tooltip(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | global_menu_set_popup_callbacks(menu_root: [String](class_string.md#class-string), open_callback: [Callable](class_callable.md#class-callable), close_callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | has_additional_outputs()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | has_feature(feature: Feature)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | has_hardware_keyboard()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | help_set_search_callbacks(search_callback: [Callable](class_callable.md#class-callable), action_callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | ime_get_selection()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                                                  | ime_get_text()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | is_dark_mode()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | is_dark_mode_supported()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | is_in_pip_mode(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | is_touchscreen_available()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | is_window_transparency_available()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                           | keyboard_get_current_layout()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Key](class_@globalscope.md#enum-globalscope-key)                                       | keyboard_get_keycode_from_physical(keycode: [Key](class_@globalscope.md#enum-globalscope-key))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Key](class_@globalscope.md#enum-globalscope-key)                                       | keyboard_get_label_from_physical(keycode: [Key](class_@globalscope.md#enum-globalscope-key))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | keyboard_get_layout_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                                                  | keyboard_get_layout_language(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [String](class_string.md#class-string)                                                  | keyboard_get_layout_name(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | keyboard_set_current_layout(index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)]             | mouse_get_button_state()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MouseMode                                              | mouse_get_mode()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | mouse_get_position()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | mouse_set_mode(mouse_mode: MouseMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | pip_mode_enter(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | pip_mode_set_aspect_ratio(numerator: [int](class_int.md#class-int), denominator: [int](class_int.md#class-int), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | pip_mode_set_auto_enter_on_background(auto_enter_on_background: [bool](class_bool.md#class-bool), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | process_events()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | register_additional_output(object: [Object](class_object.md#class-object))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | screen_get_dpi(screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Image](class_image.md#class-image)                                                     | screen_get_image(screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Image](class_image.md#class-image)                                                     | screen_get_image_rect(rect: [Rect2i](class_rect2i.md#class-rect2i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [float](class_float.md#class-float)                                                     | screen_get_max_scale()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ScreenOrientation                              | screen_get_orientation(screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Color](class_color.md#class-color)                                                     | screen_get_pixel(position: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | screen_get_position(screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                     | screen_get_refresh_rate(screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [float](class_float.md#class-float)                                                     | screen_get_scale(screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | screen_get_size(screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Rect2i](class_rect2i.md#class-rect2i)                                                  | screen_get_usable_rect(screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | screen_is_kept_on()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | screen_set_keep_on(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | screen_set_orientation(orientation: ScreenOrientation, screen: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | set_hardware_keyboard_connection_change_callback(callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | set_icon(image: [Image](class_image.md#class-image))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | set_native_icon(filename: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | set_system_theme_change_callback(callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | show_emoji_and_symbol_picker()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Rect2](class_rect2.md#class-rect2)                                                     | status_indicator_get_rect(id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | status_indicator_set_callback(id: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | status_indicator_set_icon(id: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | status_indicator_set_menu(id: [int](class_int.md#class-int), menu_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | status_indicator_set_tooltip(id: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)                                                  | tablet_get_current_driver()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                                                           | tablet_get_driver_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [String](class_string.md#class-string)                                                  | tablet_get_driver_name(idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | tablet_set_current_driver(name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | tts_get_voices()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | tts_get_voices_for_language(language: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | tts_is_paused()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | tts_is_speaking()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | tts_pause()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | tts_resume()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | tts_set_utterance_callback(event: TTSUtteranceEvent, callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | tts_speak(text: [String](class_string.md#class-string), voice: [String](class_string.md#class-string), volume: [int](class_int.md#class-int) = 50, pitch: [float](class_float.md#class-float) = 1.0, rate: [float](class_float.md#class-float) = 1.0, utterance_id: [int](class_int.md#class-int) = 0, interrupt: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                             |
|                                                                                         | tts_stop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | unregister_additional_output(object: [Object](class_object.md#class-object))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                           | virtual_keyboard_get_height()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | virtual_keyboard_hide()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | virtual_keyboard_show(existing_text: [String](class_string.md#class-string), position: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), type: VirtualKeyboardType = 0, max_length: [int](class_int.md#class-int) = -1, cursor_start: [int](class_int.md#class-int) = -1, cursor_end: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                 |
|                                                                                         | warp_mouse(position: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | window_can_draw(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | window_get_active_popup()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | window_get_attached_instance_id(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | window_get_current_screen(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | window_get_flag(flag: WindowFlags, window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                     | window_get_hdr_output_current_max_luminance(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [float](class_float.md#class-float)                                                     | window_get_hdr_output_current_reference_luminance(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                                     | window_get_hdr_output_max_luminance(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [float](class_float.md#class-float)                                                     | window_get_hdr_output_reference_luminance(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | window_get_max_size(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | window_get_min_size(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| WindowMode                                            | window_get_mode(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | window_get_native_handle(handle_type: HandleType, window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [float](class_float.md#class-float)                                                     | window_get_output_max_linear_value(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Rect2i](class_rect2i.md#class-rect2i)                                                  | window_get_popup_safe_rect(window: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | window_get_position(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | window_get_position_with_decorations(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Vector3i](class_vector3i.md#class-vector3i)                                            | window_get_safe_title_margins(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | window_get_size(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | window_get_size_with_decorations(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Vector2i](class_vector2i.md#class-vector2i)                                            | window_get_title_size(title: [String](class_string.md#class-string), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| VSyncMode                                              | window_get_vsync_mode(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | window_is_focused(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | window_is_hdr_output_enabled(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                        | window_is_hdr_output_requested(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | window_is_hdr_output_supported(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | window_is_maximize_allowed(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | window_maximize_on_title_dbl_click()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                        | window_minimize_on_title_dbl_click()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | window_move_to_foreground(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | window_request_attention(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | window_request_hdr_output(enable: [bool](class_bool.md#class-bool), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | window_set_color(color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | window_set_current_screen(screen: [int](class_int.md#class-int), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | window_set_drop_files_callback(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | window_set_exclusive(window_id: [int](class_int.md#class-int), exclusive: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | window_set_flag(flag: WindowFlags, enabled: [bool](class_bool.md#class-bool), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | window_set_hdr_output_max_luminance(max_luminance: [float](class_float.md#class-float), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | window_set_hdr_output_reference_luminance(reference_luminance: [float](class_float.md#class-float), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | window_set_icon(icon: [Image](class_image.md#class-image), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | window_set_ime_active(active: [bool](class_bool.md#class-bool), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | window_set_ime_position(position: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | window_set_input_event_callback(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | window_set_input_text_callback(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | window_set_max_size(max_size: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | window_set_min_size(min_size: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | window_set_mode(mode: WindowMode, window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | window_set_mouse_passthrough(region: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | window_set_popup_safe_rect(window: [int](class_int.md#class-int), rect: [Rect2i](class_rect2i.md#class-rect2i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | window_set_position(position: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | window_set_rect_changed_callback(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | window_set_size(size: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | window_set_taskbar_progress_state(state: ProgressState, window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | window_set_taskbar_progress_value(value: [float](class_float.md#class-float), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | window_set_title(title: [String](class_string.md#class-string), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | window_set_transient(window_id: [int](class_int.md#class-int), parent_window_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | window_set_vsync_mode(vsync_mode: VSyncMode, window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | window_set_window_buttons_offset(offset: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | window_set_window_event_callback(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | window_start_drag(window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | window_start_resize(edge: WindowResizeEdge, window_id: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

---

## Signals

**orientation_changed**(orientation: [int](class_int.md#class-int))

Emitted when the device orientation changes. `orientation` is the new orientation.

Returns `1` for portrait, `2` for landscape, and `0` if the orientation is undefined.

**Note:** This method is implemented on Android and iOS.

---

## Enumerations

enum **Feature**:

Feature **FEATURE_GLOBAL_MENU** = `0`

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Display server supports global menu. This allows the application to display its menu items in the operating system's top bar. **macOS**

Feature **FEATURE_SUBWINDOWS** = `1`

Display server supports multiple windows that can be moved outside of the main window. **Windows, macOS, Linux (X11)**

Feature **FEATURE_TOUCHSCREEN** = `2`

Display server supports touchscreen input. **Windows, Linux (X11/Wayland), Android, iOS, Web**

Feature **FEATURE_MOUSE** = `3`

Display server supports mouse input. **Windows, macOS, Linux (X11/Wayland), Android, Web**

Feature **FEATURE_MOUSE_WARP** = `4`

Display server supports warping mouse coordinates to keep the mouse cursor constrained within an area, but looping when one of the edges is reached. **Windows, macOS, Linux (X11/Wayland)**

Feature **FEATURE_CLIPBOARD** = `5`

Display server supports setting and getting clipboard data. See also FEATURE_CLIPBOARD_PRIMARY. **Windows, macOS, Linux (X11/Wayland), Android, iOS, Web**

Feature **FEATURE_VIRTUAL_KEYBOARD** = `6`

Display server supports popping up a virtual keyboard when requested to input text without a physical keyboard. **Android, iOS, Web**

Feature **FEATURE_CURSOR_SHAPE** = `7`

Display server supports setting the mouse cursor shape to be different from the default. **Windows, macOS, Linux (X11/Wayland), Android, Web**

Feature **FEATURE_CUSTOM_CURSOR_SHAPE** = `8`

Display server supports setting the mouse cursor shape to a custom image. **Windows, macOS, Linux (X11/Wayland), Web**

Feature **FEATURE_NATIVE_DIALOG** = `9`

Display server supports spawning text dialogs using the operating system's native look-and-feel. See dialog_show(). **Windows, macOS**

Feature **FEATURE_IME** = `10`

Display server supports [Input Method Editor](https://en.wikipedia.org/wiki/Input_method), which is commonly used for inputting Chinese/Japanese/Korean text. This is handled by the operating system, rather than by Godot. **Windows, macOS, Linux (X11)**

Feature **FEATURE_WINDOW_TRANSPARENCY** = `11`

Display server supports windows can use per-pixel transparency to make windows behind them partially or fully visible. **Windows, macOS, Linux (X11/Wayland), Android**

Feature **FEATURE_HIDPI** = `12`

Display server supports querying the operating system's display scale factor. This allows automatically detecting the hiDPI display *reliably*, instead of guessing based on the screen resolution and the display's reported DPI (which might be unreliable due to broken monitor EDID). **Windows, Linux (Wayland), macOS**

Feature **FEATURE_ICON** = `13`

Display server supports changing the window icon (usually displayed in the top-left corner). **Windows, macOS, Linux (X11/Wayland)**

**Note:** Use on Wayland requires the compositor to implement the [xdg_toplevel_icon_v1](https://wayland.app/protocols/xdg-toplevel-icon-v1#xdg_toplevel_icon_v1) protocol, which not all compositors do. See [xdg_toplevel_icon_v1#compositor-support](https://wayland.app/protocols/xdg-toplevel-icon-v1#compositor-support) for more information on individual compositor support.

Feature **FEATURE_NATIVE_ICON** = `14`

Display server supports changing the window icon (usually displayed in the top-left corner). **Windows, macOS**

Feature **FEATURE_ORIENTATION** = `15`

Display server supports changing the screen orientation. **Android, iOS**

Feature **FEATURE_SWAP_BUFFERS** = `16`

Display server supports V-Sync status can be changed from the default (which is forced to be enabled platforms not supporting this feature). **Windows, macOS, Linux (X11/Wayland)**

Feature **FEATURE_CLIPBOARD_PRIMARY** = `18`

Display server supports Primary clipboard can be used. This is a different clipboard from FEATURE_CLIPBOARD. **Linux (X11/Wayland)**

Feature **FEATURE_TEXT_TO_SPEECH** = `19`

Display server supports text-to-speech. See `tts_*` methods. **Windows, macOS, Linux (X11/Wayland), Android, iOS, Web**

Feature **FEATURE_EXTEND_TO_TITLE** = `20`

Display server supports expanding window content to the title. See WINDOW_FLAG_EXTEND_TO_TITLE. **macOS**

Feature **FEATURE_SCREEN_CAPTURE** = `21`

Display server supports reading screen pixels. See screen_get_pixel().

Feature **FEATURE_STATUS_INDICATOR** = `22`

Display server supports application status indicators.

Feature **FEATURE_NATIVE_HELP** = `23`

Display server supports native help system search callbacks. See help_set_search_callbacks().

Feature **FEATURE_NATIVE_DIALOG_INPUT** = `24`

Display server supports spawning text input dialogs using the operating system's native look-and-feel. See dialog_input_text(). **Windows, macOS**

Feature **FEATURE_NATIVE_DIALOG_FILE** = `25`

Display server supports spawning dialogs for selecting files or directories using the operating system's native look-and-feel. See file_dialog_show(). **Windows, macOS, Linux (X11/Wayland), Android**

Feature **FEATURE_NATIVE_DIALOG_FILE_EXTRA** = `26`

The display server supports all features of FEATURE_NATIVE_DIALOG_FILE, with the added functionality of Options and native dialog file access to `res://` and `user://` paths. See file_dialog_show() and file_dialog_with_options_show(). **Windows, macOS, Linux (X11/Wayland)**

Feature **FEATURE_WINDOW_DRAG** = `27`

The display server supports initiating window drag and resize operations on demand. See window_start_drag() and window_start_resize().

Feature **FEATURE_SCREEN_EXCLUDE_FROM_CAPTURE** = `28`

Display server supports WINDOW_FLAG_EXCLUDE_FROM_CAPTURE window flag. **Windows, macOS**

Feature **FEATURE_WINDOW_EMBEDDING** = `29`

Display server supports embedding a window from another process. **Windows, Linux (X11), macOS**

Feature **FEATURE_NATIVE_DIALOG_FILE_MIME** = `30`

Native file selection dialog supports MIME types as filters.

Feature **FEATURE_EMOJI_AND_SYMBOL_PICKER** = `31`

Display server supports system emoji and symbol picker. **Windows, macOS**

Feature **FEATURE_NATIVE_COLOR_PICKER** = `32`

Display server supports native color picker. **Linux (X11/Wayland)**

Feature **FEATURE_SELF_FITTING_WINDOWS** = `33`

Display server automatically fits popups according to the screen boundaries. Window nodes should not attempt to do that themselves.

Feature **FEATURE_ACCESSIBILITY_SCREEN_READER** = `34`

Display server supports interaction with screen reader or Braille display. **Linux (X11/Wayland), macOS, Windows**

Feature **FEATURE_HDR_OUTPUT** = `35`

Display server supports HDR output. **Linux (Wayland), macOS, iOS, visionOS, Windows**

Feature **FEATURE_PIP_MODE** = `36`

Display server supports putting the application in picture-in-picture mode. **Android**

---

enum **AccessibilityRole**:

AccessibilityRole **ROLE_UNKNOWN** = `0`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Unknown or custom role.

AccessibilityRole **ROLE_DEFAULT_BUTTON** = `1`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Default dialog button element.

AccessibilityRole **ROLE_AUDIO** = `2`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Audio player element.

AccessibilityRole **ROLE_VIDEO** = `3`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Video player element.

AccessibilityRole **ROLE_STATIC_TEXT** = `4`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Non-editable text label.

AccessibilityRole **ROLE_CONTAINER** = `5`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Container element. Elements with this role are used for internal structure and ignored by screen readers.

AccessibilityRole **ROLE_PANEL** = `6`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Panel container element.

AccessibilityRole **ROLE_BUTTON** = `7`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Button element.

AccessibilityRole **ROLE_LINK** = `8`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Link element.

AccessibilityRole **ROLE_CHECK_BOX** = `9`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Check box element.

AccessibilityRole **ROLE_RADIO_BUTTON** = `10`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Radio button element.

AccessibilityRole **ROLE_CHECK_BUTTON** = `11`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Check button element.

AccessibilityRole **ROLE_SCROLL_BAR** = `12`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll bar element.

AccessibilityRole **ROLE_SCROLL_VIEW** = `13`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll container element.

AccessibilityRole **ROLE_SPLITTER** = `14`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Container splitter handle element.

AccessibilityRole **ROLE_SLIDER** = `15`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Slider element.

AccessibilityRole **ROLE_SPIN_BUTTON** = `16`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Spin box element.

AccessibilityRole **ROLE_PROGRESS_INDICATOR** = `17`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Progress indicator element.

AccessibilityRole **ROLE_TEXT_FIELD** = `18`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Editable text field element.

AccessibilityRole **ROLE_MULTILINE_TEXT_FIELD** = `19`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Multiline editable text field element.

AccessibilityRole **ROLE_COLOR_PICKER** = `20`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Color picker element.

AccessibilityRole **ROLE_TABLE** = `21`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Table element.

AccessibilityRole **ROLE_CELL** = `22`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Table/tree cell element.

AccessibilityRole **ROLE_ROW** = `23`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Table/tree row element.

AccessibilityRole **ROLE_ROW_GROUP** = `24`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Table/tree row group element.

AccessibilityRole **ROLE_ROW_HEADER** = `25`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Table/tree row header element.

AccessibilityRole **ROLE_COLUMN_HEADER** = `26`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Table/tree column header element.

AccessibilityRole **ROLE_TREE** = `27`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Tree view element.

AccessibilityRole **ROLE_TREE_ITEM** = `28`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Tree view item element.

AccessibilityRole **ROLE_LIST** = `29`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

List element.

AccessibilityRole **ROLE_LIST_ITEM** = `30`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

List item element.

AccessibilityRole **ROLE_LIST_BOX** = `31`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

List view element.

AccessibilityRole **ROLE_LIST_BOX_OPTION** = `32`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

List view item element.

AccessibilityRole **ROLE_TAB_BAR** = `33`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Tab bar element.

AccessibilityRole **ROLE_TAB** = `34`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Tab bar item element.

AccessibilityRole **ROLE_TAB_PANEL** = `35`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Tab panel element.

AccessibilityRole **ROLE_MENU_BAR** = `36`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Menu bar element.

AccessibilityRole **ROLE_MENU** = `37`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Popup menu element.

AccessibilityRole **ROLE_MENU_ITEM** = `38`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Popup menu item element.

AccessibilityRole **ROLE_MENU_ITEM_CHECK_BOX** = `39`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Popup menu check button item element.

AccessibilityRole **ROLE_MENU_ITEM_RADIO** = `40`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Popup menu radio button item element.

AccessibilityRole **ROLE_IMAGE** = `41`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Image element.

AccessibilityRole **ROLE_WINDOW** = `42`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Window element.

AccessibilityRole **ROLE_TITLE_BAR** = `43`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Embedded window title bar element.

AccessibilityRole **ROLE_DIALOG** = `44`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Dialog window element.

AccessibilityRole **ROLE_TOOLTIP** = `45`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Tooltip element.

AccessibilityRole **ROLE_REGION** = `46`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Region/landmark element. Screen readers can navigate between regions using landmark navigation.

AccessibilityRole **ROLE_TEXT_RUN** = `47`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Unifor text run.

Note: This role is used for internal text elements, and should not be assigned to nodes.

---

enum **AccessibilityPopupType**:

AccessibilityPopupType **POPUP_MENU** = `0`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Popup menu.

AccessibilityPopupType **POPUP_LIST** = `1`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Popup list.

AccessibilityPopupType **POPUP_TREE** = `2`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Popup tree view.

AccessibilityPopupType **POPUP_DIALOG** = `3`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Popup dialog.

---

enum **AccessibilityFlags**:

AccessibilityFlags **FLAG_HIDDEN** = `0`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element is hidden for accessibility tools.

AccessibilityFlags **FLAG_MULTISELECTABLE** = `1`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element supports multiple item selection.

AccessibilityFlags **FLAG_REQUIRED** = `2`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element require user input.

AccessibilityFlags **FLAG_VISITED** = `3`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element is a visited link.

AccessibilityFlags **FLAG_BUSY** = `4`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element content is not ready (e.g. loading).

AccessibilityFlags **FLAG_MODAL** = `5`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element is modal window.

AccessibilityFlags **FLAG_TOUCH_PASSTHROUGH** = `6`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element allows touches to be passed through when a screen reader is in touch exploration mode.

AccessibilityFlags **FLAG_READONLY** = `7`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element is text field with selectable but read-only text.

AccessibilityFlags **FLAG_DISABLED** = `8`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element is disabled.

AccessibilityFlags **FLAG_CLIPS_CHILDREN** = `9`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Element clips children.

---

enum **AccessibilityAction**:

AccessibilityAction **ACTION_CLICK** = `0`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Single click action, callback argument is not set.

AccessibilityAction **ACTION_FOCUS** = `1`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Focus action, callback argument is not set.

AccessibilityAction **ACTION_BLUR** = `2`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Blur action, callback argument is not set.

AccessibilityAction **ACTION_COLLAPSE** = `3`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Collapse action, callback argument is not set.

AccessibilityAction **ACTION_EXPAND** = `4`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Expand action, callback argument is not set.

AccessibilityAction **ACTION_DECREMENT** = `5`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Decrement action, callback argument is not set.

AccessibilityAction **ACTION_INCREMENT** = `6`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Increment action, callback argument is not set.

AccessibilityAction **ACTION_HIDE_TOOLTIP** = `7`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Hide tooltip action, callback argument is not set.

AccessibilityAction **ACTION_SHOW_TOOLTIP** = `8`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Show tooltip action, callback argument is not set.

AccessibilityAction **ACTION_SET_TEXT_SELECTION** = `9`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Set text selection action, callback argument is set to [Dictionary](class_dictionary.md#class-dictionary) with the following keys:

- `"start_element"` accessibility element of the selection start.
- `"start_char"` character offset relative to the accessibility element of the selection start.
- `"end_element"` accessibility element of the selection end.
- `"end_char"` character offset relative to the accessibility element of the selection end.

AccessibilityAction **ACTION_REPLACE_SELECTED_TEXT** = `10`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Replace text action, callback argument is set to [String](class_string.md#class-string) with the replacement text.

AccessibilityAction **ACTION_SCROLL_BACKWARD** = `11`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll backward action, callback argument is not set.

AccessibilityAction **ACTION_SCROLL_DOWN** = `12`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll down action, callback argument is set to AccessibilityScrollUnit.

AccessibilityAction **ACTION_SCROLL_FORWARD** = `13`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll forward action, callback argument is not set.

AccessibilityAction **ACTION_SCROLL_LEFT** = `14`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll left action, callback argument is set to AccessibilityScrollUnit.

AccessibilityAction **ACTION_SCROLL_RIGHT** = `15`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll right action, callback argument is set to AccessibilityScrollUnit.

AccessibilityAction **ACTION_SCROLL_UP** = `16`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll up action, callback argument is set to AccessibilityScrollUnit.

AccessibilityAction **ACTION_SCROLL_INTO_VIEW** = `17`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll into view action, callback argument is set to AccessibilityScrollHint.

AccessibilityAction **ACTION_SCROLL_TO_POINT** = `18`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Scroll to point action, callback argument is set to [Vector2](class_vector2.md#class-vector2) with the relative point coordinates.

AccessibilityAction **ACTION_SET_SCROLL_OFFSET** = `19`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Set scroll offset action, callback argument is set to [Vector2](class_vector2.md#class-vector2) with the scroll offset.

AccessibilityAction **ACTION_SET_VALUE** = `20`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Set value action, callback argument is set to [String](class_string.md#class-string) or number with the new value.

AccessibilityAction **ACTION_SHOW_CONTEXT_MENU** = `21`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Show context menu action, callback argument is not set.

AccessibilityAction **ACTION_CUSTOM** = `22`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Custom action, callback argument is set to the integer action ID.

---

enum **AccessibilityLiveMode**:

AccessibilityLiveMode **LIVE_OFF** = `0`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Indicates that updates to the live region should not be presented.

AccessibilityLiveMode **LIVE_POLITE** = `1`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Indicates that updates to the live region should be presented at the next opportunity (for example at the end of speaking the current sentence).

AccessibilityLiveMode **LIVE_ASSERTIVE** = `2`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Indicates that updates to the live region have the highest priority and should be presented immediately.

---

enum **AccessibilityScrollUnit**:

AccessibilityScrollUnit **SCROLL_UNIT_ITEM** = `0`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

The amount by which to scroll. A single item of a list, line of text.

AccessibilityScrollUnit **SCROLL_UNIT_PAGE** = `1`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

The amount by which to scroll. A single page.

---

enum **AccessibilityScrollHint**:

AccessibilityScrollHint **SCROLL_HINT_TOP_LEFT** = `0`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

A preferred position for the node scrolled into view. Top-left edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_BOTTOM_RIGHT** = `1`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

A preferred position for the node scrolled into view. Bottom-right edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_TOP_EDGE** = `2`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

A preferred position for the node scrolled into view. Top edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_BOTTOM_EDGE** = `3`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

A preferred position for the node scrolled into view. Bottom edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_LEFT_EDGE** = `4`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

A preferred position for the node scrolled into view. Left edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_RIGHT_EDGE** = `5`

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

A preferred position for the node scrolled into view. Right edge of the scroll container.

---

enum **MouseMode**:

MouseMode **MOUSE_MODE_VISIBLE** = `0`

Makes the mouse cursor visible if it is hidden.

MouseMode **MOUSE_MODE_HIDDEN** = `1`

Makes the mouse cursor hidden if it is visible.

MouseMode **MOUSE_MODE_CAPTURED** = `2`

Captures the mouse. The mouse will be hidden and its position locked at the center of the window manager's window.

**Note:** If you want to process the mouse's movement in this mode, you need to use [InputEventMouseMotion.relative](class_inputeventmousemotion.md#class-inputeventmousemotion-property-relative).

MouseMode **MOUSE_MODE_CONFINED** = `3`

Confines the mouse cursor to the game window, and make it visible.

MouseMode **MOUSE_MODE_CONFINED_HIDDEN** = `4`

Confines the mouse cursor to the game window, and make it hidden.

MouseMode **MOUSE_MODE_MAX** = `5`

Max value of the MouseMode.

---

enum **ScreenOrientation**:

ScreenOrientation **SCREEN_LANDSCAPE** = `0`

Default landscape orientation.

ScreenOrientation **SCREEN_PORTRAIT** = `1`

Default portrait orientation.

ScreenOrientation **SCREEN_REVERSE_LANDSCAPE** = `2`

Reverse landscape orientation (upside down).

ScreenOrientation **SCREEN_REVERSE_PORTRAIT** = `3`

Reverse portrait orientation (upside down).

ScreenOrientation **SCREEN_SENSOR_LANDSCAPE** = `4`

Automatic landscape orientation (default or reverse depending on sensor).

ScreenOrientation **SCREEN_SENSOR_PORTRAIT** = `5`

Automatic portrait orientation (default or reverse depending on sensor).

ScreenOrientation **SCREEN_SENSOR** = `6`

Automatic landscape or portrait orientation (default or reverse depending on sensor).

---

enum **VirtualKeyboardType**:

VirtualKeyboardType **KEYBOARD_TYPE_DEFAULT** = `0`

Default text virtual keyboard.

VirtualKeyboardType **KEYBOARD_TYPE_MULTILINE** = `1`

Multiline virtual keyboard.

VirtualKeyboardType **KEYBOARD_TYPE_NUMBER** = `2`

Virtual number keypad, useful for PIN entry.

VirtualKeyboardType **KEYBOARD_TYPE_NUMBER_DECIMAL** = `3`

Virtual number keypad, useful for entering fractional numbers.

VirtualKeyboardType **KEYBOARD_TYPE_PHONE** = `4`

Virtual phone number keypad.

VirtualKeyboardType **KEYBOARD_TYPE_EMAIL_ADDRESS** = `5`

Virtual keyboard with additional keys to assist with typing email addresses.

VirtualKeyboardType **KEYBOARD_TYPE_PASSWORD** = `6`

Virtual keyboard for entering a password. On most platforms, this should disable autocomplete and autocapitalization.

**Note:** This is not supported on Web. Instead, this behaves identically to KEYBOARD_TYPE_DEFAULT.

VirtualKeyboardType **KEYBOARD_TYPE_URL** = `7`

Virtual keyboard with additional keys to assist with typing URLs.

---

enum **CursorShape**:

CursorShape **CURSOR_ARROW** = `0`

Arrow cursor shape. This is the default when not pointing anything that overrides the mouse cursor, such as a [LineEdit](class_lineedit.md#class-lineedit) or [TextEdit](class_textedit.md#class-textedit).

CursorShape **CURSOR_IBEAM** = `1`

I-beam cursor shape. This is used by default when hovering a control that accepts text input, such as [LineEdit](class_lineedit.md#class-lineedit) or [TextEdit](class_textedit.md#class-textedit).

CursorShape **CURSOR_POINTING_HAND** = `2`

Pointing hand cursor shape. This is used by default when hovering a [LinkButton](class_linkbutton.md#class-linkbutton) or a URL tag in a [RichTextLabel](class_richtextlabel.md#class-richtextlabel).

CursorShape **CURSOR_CROSS** = `3`

Crosshair cursor. This is intended to be displayed when the user needs precise aim over an element, such as a rectangle selection tool or a color picker.

CursorShape **CURSOR_WAIT** = `4`

Wait cursor. On most cursor themes, this displays a spinning icon *besides* the arrow. Intended to be used for non-blocking operations (when the user can do something else at the moment). See also CURSOR_BUSY.

CursorShape **CURSOR_BUSY** = `5`

Wait cursor. On most cursor themes, this *replaces* the arrow with a spinning icon. Intended to be used for blocking operations (when the user can't do anything else at the moment). See also CURSOR_WAIT.

CursorShape **CURSOR_DRAG** = `6`

Dragging hand cursor. This is displayed during drag-and-drop operations. See also CURSOR_CAN_DROP.

CursorShape **CURSOR_CAN_DROP** = `7`

"Can drop" cursor. This is displayed during drag-and-drop operations if hovering over a [Control](class_control.md#class-control) that can accept the drag-and-drop event. On most cursor themes, this displays a dragging hand with an arrow symbol besides it. See also CURSOR_DRAG.

CursorShape **CURSOR_FORBIDDEN** = `8`

Forbidden cursor. This is displayed during drag-and-drop operations if the hovered [Control](class_control.md#class-control) can't accept the drag-and-drop event.

CursorShape **CURSOR_VSIZE** = `9`

Vertical resize cursor. Intended to be displayed when the hovered [Control](class_control.md#class-control) can be vertically resized using the mouse. See also CURSOR_VSPLIT.

CursorShape **CURSOR_HSIZE** = `10`

Horizontal resize cursor. Intended to be displayed when the hovered [Control](class_control.md#class-control) can be horizontally resized using the mouse. See also CURSOR_HSPLIT.

CursorShape **CURSOR_BDIAGSIZE** = `11`

Secondary diagonal resize cursor (top-right/bottom-left). Intended to be displayed when the hovered [Control](class_control.md#class-control) can be resized on both axes at once using the mouse.

CursorShape **CURSOR_FDIAGSIZE** = `12`

Main diagonal resize cursor (top-left/bottom-right). Intended to be displayed when the hovered [Control](class_control.md#class-control) can be resized on both axes at once using the mouse.

CursorShape **CURSOR_MOVE** = `13`

Move cursor. Intended to be displayed when the hovered [Control](class_control.md#class-control) can be moved using the mouse.

CursorShape **CURSOR_VSPLIT** = `14`

Vertical split cursor. This is displayed when hovering a [Control](class_control.md#class-control) with splits that can be vertically resized using the mouse, such as [VSplitContainer](class_vsplitcontainer.md#class-vsplitcontainer). On some cursor themes, this cursor may have the same appearance as CURSOR_VSIZE.

CursorShape **CURSOR_HSPLIT** = `15`

Horizontal split cursor. This is displayed when hovering a [Control](class_control.md#class-control) with splits that can be horizontally resized using the mouse, such as [HSplitContainer](class_hsplitcontainer.md#class-hsplitcontainer). On some cursor themes, this cursor may have the same appearance as CURSOR_HSIZE.

CursorShape **CURSOR_HELP** = `16`

Help cursor. On most cursor themes, this displays a question mark icon instead of the mouse cursor. Intended to be used when the user has requested help on the next element that will be clicked.

CursorShape **CURSOR_MAX** = `17`

Represents the size of the CursorShape enum.

---

enum **FileDialogMode**:

FileDialogMode **FILE_DIALOG_MODE_OPEN_FILE** = `0`

The native file dialog allows selecting one, and only one file.

FileDialogMode **FILE_DIALOG_MODE_OPEN_FILES** = `1`

The native file dialog allows selecting multiple files.

FileDialogMode **FILE_DIALOG_MODE_OPEN_DIR** = `2`

The native file dialog only allows selecting a directory, disallowing the selection of any file.

FileDialogMode **FILE_DIALOG_MODE_OPEN_ANY** = `3`

The native file dialog allows selecting one file or directory.

FileDialogMode **FILE_DIALOG_MODE_SAVE_FILE** = `4`

The native file dialog will warn when a file exists.

---

enum **WindowMode**:

WindowMode **WINDOW_MODE_WINDOWED** = `0`

Windowed mode, i.e. [Window](class_window.md#class-window) doesn't occupy the whole screen (unless set to the size of the screen).

WindowMode **WINDOW_MODE_MINIMIZED** = `1`

Minimized window mode, i.e. [Window](class_window.md#class-window) is not visible and available on window manager's window list. Normally happens when the minimize button is pressed.

WindowMode **WINDOW_MODE_MAXIMIZED** = `2`

Maximized window mode, i.e. [Window](class_window.md#class-window) will occupy whole screen area except task bar and still display its borders. Normally happens when the maximize button is pressed.

WindowMode **WINDOW_MODE_FULLSCREEN** = `3`

Full screen mode with full multi-window support.

Full screen window covers the entire display area of a screen and has no decorations. The display's video mode is not changed.

**On Android:** This enables immersive mode.

**On macOS:** A new desktop is used to display the running project.

**Note:** Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supports [multiple resolutions](../tutorials/rendering/multiple_resolutions.md) when enabling full screen mode.

WindowMode **WINDOW_MODE_EXCLUSIVE_FULLSCREEN** = `4`

A single window full screen mode. This mode has less overhead, but only one window can be open on a given screen at a time (opening a child window or application switching will trigger a full screen transition).

Full screen window covers the entire display area of a screen and has no border or decorations. The display's video mode is not changed.

**Note:** This mode might not work with screen recording software.

**On Android:** This enables immersive mode.

**On Windows:** Depending on video driver, full screen transition might cause screens to go black for a moment.

**On macOS:** A new desktop is used to display the running project. Exclusive full screen mode prevents Dock and Menu from showing up when the mouse pointer is hovering the edge of the screen.

**On Linux (X11):** Exclusive full screen mode bypasses compositor.

**On Linux (Wayland):** Equivalent to WINDOW_MODE_FULLSCREEN.

**Note:** Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supports [multiple resolutions](../tutorials/rendering/multiple_resolutions.md) when enabling full screen mode.

---

enum **ProgressState**:

ProgressState **PROGRESS_STATE_NOPROGRESS** = `0`

Stops displaying progress and returns the button to its normal state.

ProgressState **PROGRESS_STATE_INDETERMINATE** = `1`

The progress indicator shows an indeterminate progress.

On Windows, the progress indicator does not grow in size, but cycles repeatedly along the length of the taskbar button by default.

ProgressState **PROGRESS_STATE_NORMAL** = `2`

The progress indicator shows progress normally.

ProgressState **PROGRESS_STATE_ERROR** = `3`

The progress indicator shows that an error has occurred.

On Windows, the progress indicator turns red by default to show that an error has occurred in one of the windows that is broadcasting progress.

ProgressState **PROGRESS_STATE_PAUSED** = `4`

The progress indicator shows it was paused.

On Windows, the progress indicator turns yellow by default to show that progress is currently stopped in one of the windows but can be resumed by the user.

---

enum **WindowFlags**:

WindowFlags **WINDOW_FLAG_RESIZE_DISABLED** = `0`

The window can't be resized by dragging its resize grip. It's still possible to resize the window using window_set_size(). This flag is ignored for full screen windows.

**Note:** This flag is implemented on Linux (X11), macOS, and Windows.

WindowFlags **WINDOW_FLAG_BORDERLESS** = `1`

The window do not have native title bar and other decorations. This flag is ignored for full-screen windows.

**Note:** This flag is implemented on Linux (X11/Wayland), macOS, and Windows.

WindowFlags **WINDOW_FLAG_ALWAYS_ON_TOP** = `2`

The window is floating on top of all other windows. This flag is ignored for full-screen windows.

**Note:** This flag is implemented on Linux (X11), macOS, and Windows.

WindowFlags **WINDOW_FLAG_TRANSPARENT** = `3`

The window background can be transparent.

**Note:** This flag has no effect if is_window_transparency_available() returns `false`.

**Note:** Transparency support is implemented on Linux (X11/Wayland), macOS, and Windows, but availability might vary depending on GPU driver, display manager, and compositor capabilities.

**Note:** Transparency support is implemented on Android, but can only be enabled via [ProjectSettings.display/window/per_pixel_transparency/allowed](class_projectsettings.md#class-projectsettings-property-display-window-per-pixel-transparency-allowed). This flag has no effect on Android.

WindowFlags **WINDOW_FLAG_NO_FOCUS** = `4`

The window can't be focused. No-focus window will ignore all input, except mouse clicks.

**Note:** This flag is implemented on Linux (X11), macOS, and Windows.

WindowFlags **WINDOW_FLAG_POPUP** = `5`

Window is part of menu or [OptionButton](class_optionbutton.md#class-optionbutton) dropdown. This flag can't be changed when the window is visible. An active popup window will exclusively receive all input, without stealing focus from its parent. Popup windows are automatically closed when uses click outside it, or when an application is switched. Popup window must have transient parent set (see window_set_transient()).

**Note:** This flag is implemented on Linux (X11/Wayland), macOS, and Windows.

WindowFlags **WINDOW_FLAG_EXTEND_TO_TITLE** = `6`

Window content is expanded to the full size of the window. Unlike borderless window, the frame is left intact and can be used to resize the window, title bar is transparent, but have minimize/maximize/close buttons.

Use window_set_window_buttons_offset() to adjust minimize/maximize/close buttons offset.

Use window_get_safe_title_margins() to determine area under the title bar that is not covered by decorations.

**Note:** This flag is implemented only on macOS.

WindowFlags **WINDOW_FLAG_MOUSE_PASSTHROUGH** = `7`

All mouse events are passed to the underlying window of the same application.

**Note:** This flag is implemented on Linux (X11), macOS, and Windows.

WindowFlags **WINDOW_FLAG_SHARP_CORNERS** = `8`

Window style is overridden, forcing sharp corners.

**Note:** This flag is implemented only on Windows (11).

WindowFlags **WINDOW_FLAG_EXCLUDE_FROM_CAPTURE** = `9`

Window is excluded from screenshots taken by screen_get_image(), screen_get_image_rect(), and screen_get_pixel().

**Note:** This flag is implemented on macOS and Windows (10, 20H1).

**Note:** Setting this flag will prevent standard screenshot methods from capturing a window image, but does **NOT** guarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.

WindowFlags **WINDOW_FLAG_POPUP_WM_HINT** = `10`

Signals the window manager that this window is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).

**Note:** This flag is implemented on Linux (Wayland).

WindowFlags **WINDOW_FLAG_MINIMIZE_DISABLED** = `11`

Window minimize button is disabled.

**Note:** This flag is implemented on Linux (X11), macOS, and Windows.

WindowFlags **WINDOW_FLAG_MAXIMIZE_DISABLED** = `12`

Window maximize button is disabled.

**Note:** This flag is implemented on Linux (X11), macOS, and Windows.

WindowFlags **WINDOW_FLAG_MAX** = `13`

Represents the size of the WindowFlags enum.

---

enum **WindowEvent**:

WindowEvent **WINDOW_EVENT_MOUSE_ENTER** = `0`

Sent when the mouse pointer enters the window.

WindowEvent **WINDOW_EVENT_MOUSE_EXIT** = `1`

Sent when the mouse pointer exits the window.

WindowEvent **WINDOW_EVENT_FOCUS_IN** = `2`

Sent when the window grabs focus.

WindowEvent **WINDOW_EVENT_FOCUS_OUT** = `3`

Sent when the window loses focus.

WindowEvent **WINDOW_EVENT_CLOSE_REQUEST** = `4`

Sent when the user has attempted to close the window (e.g. close button is pressed).

WindowEvent **WINDOW_EVENT_GO_BACK_REQUEST** = `5`

Sent when the device "Back" button is pressed.

**Note:** This event is implemented only on Android.

WindowEvent **WINDOW_EVENT_DPI_CHANGE** = `6`

Sent when the window is moved to the display with different DPI, or display DPI is changed.

**Note:** This flag is implemented only on macOS and Linux (Wayland).

WindowEvent **WINDOW_EVENT_TITLEBAR_CHANGE** = `7`

Sent when the window title bar decoration is changed (e.g. WINDOW_FLAG_EXTEND_TO_TITLE is set or window entered/exited full screen mode).

**Note:** This flag is implemented only on macOS.

WindowEvent **WINDOW_EVENT_FORCE_CLOSE** = `8`

Sent when the window has been forcibly closed by the display server. The window will immediately hide and clean any internal rendering references.

**Note:** This flag is implemented only on Linux (Wayland).

WindowEvent **WINDOW_EVENT_OUTPUT_MAX_LINEAR_VALUE_CHANGED** = `9`

Sent when the output max linear value returned by [Window.get_output_max_linear_value()](class_window.md#class-window-method-get-output-max-linear-value) has changed.

This occurs when HDR output is enabled or disabled and when any HDR output luminance values of the window have changed, such as when the player adjusts their screen brightness setting or moves the window to a different screen.

---

enum **WindowResizeEdge**:

WindowResizeEdge **WINDOW_EDGE_TOP_LEFT** = `0`

Top-left edge of a window.

WindowResizeEdge **WINDOW_EDGE_TOP** = `1`

Top edge of a window.

WindowResizeEdge **WINDOW_EDGE_TOP_RIGHT** = `2`

Top-right edge of a window.

WindowResizeEdge **WINDOW_EDGE_LEFT** = `3`

Left edge of a window.

WindowResizeEdge **WINDOW_EDGE_RIGHT** = `4`

Right edge of a window.

WindowResizeEdge **WINDOW_EDGE_BOTTOM_LEFT** = `5`

Bottom-left edge of a window.

WindowResizeEdge **WINDOW_EDGE_BOTTOM** = `6`

Bottom edge of a window.

WindowResizeEdge **WINDOW_EDGE_BOTTOM_RIGHT** = `7`

Bottom-right edge of a window.

WindowResizeEdge **WINDOW_EDGE_MAX** = `8`

Represents the size of the WindowResizeEdge enum.

---

enum **VSyncMode**:

VSyncMode **VSYNC_DISABLED** = `0`

No vertical synchronization, which means the engine will display frames as fast as possible (tearing may be visible). Framerate is unlimited (regardless of [Engine.max_fps](class_engine.md#class-engine-property-max-fps)).

VSyncMode **VSYNC_ENABLED** = `1`

Default vertical synchronization mode, the image is displayed only on vertical blanking intervals (no tearing is visible). Framerate is limited by the monitor refresh rate (regardless of [Engine.max_fps](class_engine.md#class-engine-property-max-fps)).

VSyncMode **VSYNC_ADAPTIVE** = `2`

Behaves like VSYNC_DISABLED when the framerate drops below the screen's refresh rate to reduce stuttering (tearing may be visible). Otherwise, vertical synchronization is enabled to avoid tearing. Framerate is limited by the monitor refresh rate (regardless of [Engine.max_fps](class_engine.md#class-engine-property-max-fps)). Behaves like VSYNC_ENABLED when using the Compatibility rendering method.

VSyncMode **VSYNC_MAILBOX** = `3`

Displays the most recent image in the queue on vertical blanking intervals, while rendering to the other images (no tearing is visible). Framerate is unlimited (regardless of [Engine.max_fps](class_engine.md#class-engine-property-max-fps)).

Although not guaranteed, the images can be rendered as fast as possible, which may reduce input lag (also called "Fast" V-Sync mode). VSYNC_MAILBOX works best when at least twice as many frames as the display refresh rate are rendered. Behaves like VSYNC_ENABLED when using the Compatibility rendering method.

---

enum **HandleType**:

HandleType **DISPLAY_HANDLE** = `0`

Display handle:

- Linux (X11): `X11::Display*` for the display.
- Linux (Wayland): `wl_display` for the display.
- Android: `EGLDisplay` for the display.

HandleType **WINDOW_HANDLE** = `1`

Window handle:

- Windows: `HWND` for the window.
- Linux (X11): `X11::Window*` for the window.
- Linux (Wayland): `wl_surface` for the window.
- macOS: `NSWindow*` for the window.
- iOS: `UIViewController*` for the view controller.
- Android: `jObject` for the activity.

HandleType **WINDOW_VIEW** = `2`

Window view:

- Windows: `HDC` for the window (only with the Compatibility renderer).
- macOS: `NSView*` for the window main view.
- iOS: `UIView*` for the window main view.

HandleType **OPENGL_CONTEXT** = `3`

OpenGL context (only with the Compatibility renderer):

- Windows: `HGLRC` for the window (native GL), or `EGLContext` for the window (ANGLE).
- Linux (X11): `GLXContext*` for the window.
- Linux (Wayland): `EGLContext` for the window.
- macOS: `NSOpenGLContext*` for the window (native GL), or `EGLContext` for the window (ANGLE).
- Android: `EGLContext` for the window.

HandleType **EGL_DISPLAY** = `4`

- Windows: `EGLDisplay` for the window (ANGLE).
- macOS: `EGLDisplay` for the window (ANGLE).
- Linux (Wayland): `EGLDisplay` for the window.

HandleType **EGL_CONFIG** = `5`

- Windows: `EGLConfig` for the window (ANGLE).
- macOS: `EGLConfig` for the window (ANGLE).
- Linux (Wayland): `EGLConfig` for the window.

HandleType **GLX_VISUALID** = `6`

The GLX `VisualID` for the window.

**Note:** Only available on Linux when using X11.

HandleType **GLX_FBCONFIG** = `7`

The `GLXFBConfig` for the window.

**Note:** Only available on Linux when using X11.

---

enum **TTSUtteranceEvent**:

TTSUtteranceEvent **TTS_UTTERANCE_STARTED** = `0`

Utterance has begun to be spoken.

TTSUtteranceEvent **TTS_UTTERANCE_ENDED** = `1`

Utterance was successfully finished.

TTSUtteranceEvent **TTS_UTTERANCE_CANCELED** = `2`

Utterance was canceled, or TTS service was unable to process it.

TTSUtteranceEvent **TTS_UTTERANCE_BOUNDARY** = `3`

Utterance reached a word or sentence boundary.

---

## Constants

**INVALID_SCREEN** = `-1`

The ID that refers to a screen that does not exist. This is returned by some **DisplayServer** methods if no screen matches the requested result.

**SCREEN_WITH_MOUSE_FOCUS** = `-4`

Represents the screen containing the mouse pointer.

**Note:** On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index `0`.

**SCREEN_WITH_KEYBOARD_FOCUS** = `-3`

Represents the screen containing the window with the keyboard focus.

**Note:** On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index `0`.

**SCREEN_PRIMARY** = `-2`

Represents the primary screen.

**Note:** On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index `0`.

**SCREEN_OF_MAIN_WINDOW** = `-1`

Represents the screen where the main window is located. This is usually the default value in functions that allow specifying one of several screens.

**Note:** On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index `0`.

**MAIN_WINDOW_ID** = `0`

The ID of the main window spawned by the engine, which can be passed to methods expecting a `window_id`.

**INVALID_WINDOW_ID** = `-1`

The ID that refers to a nonexistent window. This is returned by some **DisplayServer** methods if no window matches the requested result.

**INVALID_INDICATOR_ID** = `-1`

The ID that refers to a nonexistent application status indicator.

---

## Method Descriptions

[RID](class_rid.md#class-rid) **accessibility_create_element**(window_id: [int](class_int.md#class-int), role: AccessibilityRole)

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Creates a new, empty accessibility element resource.

**Note:** An accessibility element is created and freed automatically for each [Node](class_node.md#class-node). In general, this function should not be called manually.

---

[RID](class_rid.md#class-rid) **accessibility_create_sub_element**(parent_rid: [RID](class_rid.md#class-rid), role: AccessibilityRole, insert_pos: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Creates a new, empty accessibility sub-element resource. Sub-elements can be used to provide accessibility information for objects which are not [Node](class_node.md#class-node)s, such as list items, table cells, or menu items. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the accessibility_free_element() method.

---

[RID](class_rid.md#class-rid) **accessibility_create_sub_text_edit_elements**(parent_rid: [RID](class_rid.md#class-rid), shaped_text: [RID](class_rid.md#class-rid), min_height: [float](class_float.md#class-float), insert_pos: [int](class_int.md#class-int) = -1, is_last_line: [bool](class_bool.md#class-bool) = false)

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Creates a new, empty accessibility sub-element from the shaped text buffer. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the accessibility_free_element() method.

If `is_last_line` is `true`, no trailing newline is appended to the text content. Set to `true` for the last line in multi-line text fields and for single-line text fields.

---

[Variant](class_variant.md#class-variant) **accessibility_element_get_meta**(id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Returns the metadata of the accessibility element `id`.

---

 **accessibility_element_set_meta**(id: [RID](class_rid.md#class-rid), meta: [Variant](class_variant.md#class-variant))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets the metadata of the accessibility element `id` to `meta`.

---

 **accessibility_free_element**(id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Frees the accessibility element `id` created by accessibility_create_element(), accessibility_create_sub_element(), or accessibility_create_sub_text_edit_elements().

---

[RID](class_rid.md#class-rid) **accessibility_get_window_root**(window_id: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Returns the main accessibility element of the OS native window.

---

[bool](class_bool.md#class-bool) **accessibility_has_element**(id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Returns `true` if `id` is a valid accessibility element.

---

[int](class_int.md#class-int) **accessibility_screen_reader_active**()

Returns `1` if a screen reader, Braille display or other assistive app is active, `0` otherwise. Returns `-1` if status is unknown.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Accessibility debugging tools, such as Accessibility Insights for Windows, Accessibility Inspector (macOS), or AT-SPI Browser (Linux/BSD), do not count as assistive apps and will not affect this value. To test your project with these tools, set [ProjectSettings.accessibility/general/accessibility_support](class_projectsettings.md#class-projectsettings-property-accessibility-general-accessibility-support) to `1`.

---

 **accessibility_set_window_focused**(window_id: [int](class_int.md#class-int), focused: [bool](class_bool.md#class-bool))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets the window focused state for assistive apps.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Advanced users only! [Window](class_window.md#class-window) objects call this method automatically.

---

 **accessibility_set_window_rect**(window_id: [int](class_int.md#class-int), rect_out: [Rect2](class_rect2.md#class-rect2), rect_in: [Rect2](class_rect2.md#class-rect2))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets window outer (with decorations) and inner (without decorations) bounds for assistive apps.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Advanced users only! [Window](class_window.md#class-window) objects call this method automatically.

---

[int](class_int.md#class-int) **accessibility_should_increase_contrast**()

Returns `1` if a high-contrast user interface theme should be used, `0` otherwise. Returns `-1` if status is unknown.

**Note:** This method is implemented on Linux (X11/Wayland, GNOME), macOS, and Windows.

---

[int](class_int.md#class-int) **accessibility_should_reduce_animation**()

Returns `1` if flashing, blinking, and other moving content that can cause seizures in users with photosensitive epilepsy should be disabled, `0` otherwise. Returns `-1` if status is unknown.

**Note:** This method is implemented on macOS and Windows.

---

[int](class_int.md#class-int) **accessibility_should_reduce_transparency**()

Returns `1` if background images, transparency, and other features that can reduce the contrast between the foreground and background should be disabled, `0` otherwise. Returns `-1` if status is unknown.

**Note:** This method is implemented on macOS and Windows.

---

 **accessibility_update_add_action**(id: [RID](class_rid.md#class-rid), action: AccessibilityAction, callable: [Callable](class_callable.md#class-callable))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds a callback for the accessibility action (action which can be performed by using a special screen reader command or buttons on the Braille display), and marks this action as supported. The action callback receives one [Variant](class_variant.md#class-variant) argument, which value depends on action type.

---

 **accessibility_update_add_child**(id: [RID](class_rid.md#class-rid), child_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds a child accessibility element.

**Note:** [Node](class_node.md#class-node) children and sub-elements are added to the child list automatically.

---

 **accessibility_update_add_custom_action**(id: [RID](class_rid.md#class-rid), action_id: [int](class_int.md#class-int), action_description: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds support for a custom accessibility action. `action_id` is passed as an argument to the callback of ACTION_CUSTOM action.

---

 **accessibility_update_add_related_controls**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds an element that is controlled by this element.

---

 **accessibility_update_add_related_described_by**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds an element that describes this element.

---

 **accessibility_update_add_related_details**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds an element that details this element.

---

 **accessibility_update_add_related_flow_to**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds an element that this element flow into.

---

 **accessibility_update_add_related_labeled_by**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds an element that labels this element.

---

 **accessibility_update_add_related_radio_group**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds an element that is part of the same radio group.

**Note:** This method should be called on each element of the group, using all other elements as `related_id`.

---

 **accessibility_update_set_active_descendant**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Adds an element that is an active descendant of this element.

---

 **accessibility_update_set_background_color**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element background color.

---

 **accessibility_update_set_bounds**(id: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element bounding box, relative to the node position.

---

 **accessibility_update_set_checked**(id: [RID](class_rid.md#class-rid), checekd: [bool](class_bool.md#class-bool))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element checked state.

---

 **accessibility_update_set_classname**(id: [RID](class_rid.md#class-rid), classname: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element class name.

---

 **accessibility_update_set_color_value**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element color value.

---

 **accessibility_update_set_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element accessibility description.

---

 **accessibility_update_set_error_message**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets an element which contains an error message for this element.

---

 **accessibility_update_set_extra_info**(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element accessibility extra information added to the element name.

---

 **accessibility_update_set_flag**(id: [RID](class_rid.md#class-rid), flag: AccessibilityFlags, value: [bool](class_bool.md#class-bool))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element flag.

---

 **accessibility_update_set_focus**(id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets currently focused element.

---

 **accessibility_update_set_foreground_color**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element foreground color.

---

 **accessibility_update_set_in_page_link_target**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets target element for the link.

---

 **accessibility_update_set_language**(id: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element text language.

---

 **accessibility_update_set_list_item_count**(id: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets number of items in the list.

---

 **accessibility_update_set_list_item_expanded**(id: [RID](class_rid.md#class-rid), expanded: [bool](class_bool.md#class-bool))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets list/tree item expanded status.

---

 **accessibility_update_set_list_item_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets the position of the element in the list.

---

 **accessibility_update_set_list_item_level**(id: [RID](class_rid.md#class-rid), level: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets the hierarchical level of the element in the list.

---

 **accessibility_update_set_list_item_selected**(id: [RID](class_rid.md#class-rid), selected: [bool](class_bool.md#class-bool))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets list/tree item selected status.

---

 **accessibility_update_set_list_orientation**(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets the orientation of the list elements.

---

 **accessibility_update_set_live**(id: [RID](class_rid.md#class-rid), live: AccessibilityLiveMode)

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets the priority of the live region updates.

---

 **accessibility_update_set_member_of**(id: [RID](class_rid.md#class-rid), group_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets the element to be a member of the group.

---

 **accessibility_update_set_name**(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element accessibility name.

---

 **accessibility_update_set_next_on_line**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets next element on the line.

---

 **accessibility_update_set_num_jump**(id: [RID](class_rid.md#class-rid), jump: [float](class_float.md#class-float))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets numeric value jump.

---

 **accessibility_update_set_num_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets numeric value range.

---

 **accessibility_update_set_num_step**(id: [RID](class_rid.md#class-rid), step: [float](class_float.md#class-float))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets numeric value step.

---

 **accessibility_update_set_num_value**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets numeric value.

---

 **accessibility_update_set_placeholder**(id: [RID](class_rid.md#class-rid), placeholder: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets placeholder text.

---

 **accessibility_update_set_popup_type**(id: [RID](class_rid.md#class-rid), popup: AccessibilityPopupType)

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets popup type for popup buttons.

---

 **accessibility_update_set_previous_on_line**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets previous element on the line.

---

 **accessibility_update_set_role**(id: [RID](class_rid.md#class-rid), role: AccessibilityRole)

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element accessibility role.

---

 **accessibility_update_set_role_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element accessibility role description text.

---

 **accessibility_update_set_scroll_x**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets scroll bar x position.

---

 **accessibility_update_set_scroll_x_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets scroll bar x range.

---

 **accessibility_update_set_scroll_y**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets scroll bar y position.

---

 **accessibility_update_set_scroll_y_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets scroll bar y range.

---

 **accessibility_update_set_shortcut**(id: [RID](class_rid.md#class-rid), shortcut: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets the list of keyboard shortcuts used by element.

---

 **accessibility_update_set_state_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets human-readable description of the current checked state.

---

 **accessibility_update_set_table_cell_position**(id: [RID](class_rid.md#class-rid), row_index: [int](class_int.md#class-int), column_index: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets cell position in the table.

---

 **accessibility_update_set_table_cell_span**(id: [RID](class_rid.md#class-rid), row_span: [int](class_int.md#class-int), column_span: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets cell row/column span.

---

 **accessibility_update_set_table_column_count**(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets number of columns in the table.

---

 **accessibility_update_set_table_column_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets position of the column.

---

 **accessibility_update_set_table_row_count**(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets number of rows in the table.

---

 **accessibility_update_set_table_row_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets position of the row in the table.

---

 **accessibility_update_set_text_align**(id: [RID](class_rid.md#class-rid), align: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element text alignment.

---

 **accessibility_update_set_text_decorations**(id: [RID](class_rid.md#class-rid), underline: [bool](class_bool.md#class-bool), strikethrough: [bool](class_bool.md#class-bool), overline: [bool](class_bool.md#class-bool))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets text underline/overline/strikethrough.

---

 **accessibility_update_set_text_orientation**(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets text orientation.

---

 **accessibility_update_set_text_selection**(id: [RID](class_rid.md#class-rid), text_start_id: [RID](class_rid.md#class-rid), start_char: [int](class_int.md#class-int), text_end_id: [RID](class_rid.md#class-rid), end_char: [int](class_int.md#class-int))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets text selection to the text field. `text_start_id` and `text_end_id` should be elements created by accessibility_create_sub_text_edit_elements(). Character offsets are relative to the corresponding element.

---

 **accessibility_update_set_tooltip**(id: [RID](class_rid.md#class-rid), tooltip: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets tooltip text.

---

 **accessibility_update_set_transform**(id: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element 2D transform.

---

 **accessibility_update_set_url**(id: [RID](class_rid.md#class-rid), url: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets link URL.

---

 **accessibility_update_set_value**(id: [RID](class_rid.md#class-rid), value: [String](class_string.md#class-string))

**Deprecated:** Use [AccessibilityServer](class_accessibilityserver.md#class-accessibilityserver) instead.

Sets element text value.

---

 **beep**()

Plays the beep sound from the operative system, if possible. Because it comes from the OS, the beep sound will be audible even if the application is muted. It may also be disabled for the entire OS by the user.

**Note:** This method is implemented on macOS, Linux (X11/Wayland), and Windows.

---

[String](class_string.md#class-string) **clipboard_get**()

Returns the user's clipboard as a string if possible.

---

[Image](class_image.md#class-image) **clipboard_get_image**()

Returns the user's clipboard as an image if possible.

**Note:** This method uses the copied pixel data, e.g. from an image editing software or a web browser, not an image file copied from file explorer.

---

[String](class_string.md#class-string) **clipboard_get_primary**()

Returns the user's [primary](https://unix.stackexchange.com/questions/139191/whats-the-difference-between-primary-selection-and-clipboard-buffer) clipboard as a string if possible. This is the clipboard that is set when the user selects text in any application, rather than when pressing `Ctrl + C`. The clipboard data can then be pasted by clicking the middle mouse button in any application that supports the primary clipboard mechanism.

**Note:** This method is only implemented on Linux (X11/Wayland).

---

[bool](class_bool.md#class-bool) **clipboard_has**()

Returns `true` if there is a text content on the user's clipboard.

---

[bool](class_bool.md#class-bool) **clipboard_has_image**()

Returns `true` if there is an image content on the user's clipboard.

---

 **clipboard_set**(clipboard: [String](class_string.md#class-string))

Sets the user's clipboard content to the given string.

---

 **clipboard_set_primary**(clipboard_primary: [String](class_string.md#class-string))

Sets the user's [primary](https://unix.stackexchange.com/questions/139191/whats-the-difference-between-primary-selection-and-clipboard-buffer) clipboard content to the given string. This is the clipboard that is set when the user selects text in any application, rather than when pressing `Ctrl + C`. The clipboard data can then be pasted by clicking the middle mouse button in any application that supports the primary clipboard mechanism.

**Note:** This method is only implemented on Linux (X11/Wayland).

---

[bool](class_bool.md#class-bool) **color_picker**(callback: [Callable](class_callable.md#class-callable))

Displays OS native color picker.

Callbacks have the following arguments: `status: bool, color: Color`.

**Note:** This method is implemented if the display server has the FEATURE_NATIVE_COLOR_PICKER feature.

**Note:** This method is only implemented on Linux (X11/Wayland).

---

[int](class_int.md#class-int) **create_status_indicator**(icon: [Texture2D](class_texture2d.md#class-texture2d), tooltip: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable))

Creates a new application status indicator with the specified icon, tooltip, and activation callback.

`callback` should take two arguments: the pressed mouse button (one of the [MouseButton](class_@globalscope.md#enum-globalscope-mousebutton) constants) and the click position in screen coordinates (a [Vector2i](class_vector2i.md#class-vector2i)).

---

CursorShape **cursor_get_shape**()

Returns the default mouse cursor shape set by cursor_set_shape().

---

 **cursor_set_custom_image**(cursor: [Resource](class_resource.md#class-resource), shape: CursorShape = 0, hotspot: [Vector2](class_vector2.md#class-vector2) = Vector2(0, 0))

Sets a custom mouse cursor image for the given `shape`. This means the user's operating system and mouse cursor theme will no longer influence the mouse cursor's appearance.

`cursor` can be either a [Texture2D](class_texture2d.md#class-texture2d) or an [Image](class_image.md#class-image), and it should not be larger than 256×256 to display correctly. Optionally, `hotspot` can be set to offset the image's position relative to the click point. By default, `hotspot` is set to the top-left corner of the image. See also cursor_set_shape().

**Note:** On Web, calling this method every frame can cause the cursor to flicker.

---

 **cursor_set_shape**(shape: CursorShape)

Sets the default mouse cursor shape. The cursor's appearance will vary depending on the user's operating system and mouse cursor theme. See also cursor_get_shape() and cursor_set_custom_image().

---

 **delete_status_indicator**(id: [int](class_int.md#class-int))

Removes the application status indicator.

---

[Error](class_@globalscope.md#enum-globalscope-error) **dialog_input_text**(title: [String](class_string.md#class-string), description: [String](class_string.md#class-string), existing_text: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable))

Shows a text input dialog which uses the operating system's native look-and-feel. `callback` should accept a single [String](class_string.md#class-string) parameter which contains the text field's contents.

**Note:** This method is implemented if the display server has the FEATURE_NATIVE_DIALOG_INPUT feature. Supported platforms include macOS, Windows, and Android.

---

[Error](class_@globalscope.md#enum-globalscope-error) **dialog_show**(title: [String](class_string.md#class-string), description: [String](class_string.md#class-string), buttons: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), callback: [Callable](class_callable.md#class-callable))

Shows a text dialog which uses the operating system's native look-and-feel. `callback` should accept a single [int](class_int.md#class-int) parameter which corresponds to the index of the pressed button.

**Note:** This method is implemented if the display server has the FEATURE_NATIVE_DIALOG feature. Supported platforms include macOS, Windows, and Android.

---

 **enable_for_stealing_focus**(process_id: [int](class_int.md#class-int))

Allows the `process_id` PID to steal focus from this window. In other words, this disables the operating system's focus stealing protection for the specified PID.

**Note:** This method is implemented only on Windows.

---

[Error](class_@globalscope.md#enum-globalscope-error) **file_dialog_show**(title: [String](class_string.md#class-string), current_directory: [String](class_string.md#class-string), filename: [String](class_string.md#class-string), show_hidden: [bool](class_bool.md#class-bool), mode: FileDialogMode, filters: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), callback: [Callable](class_callable.md#class-callable), parent_window_id: [int](class_int.md#class-int) = 0)

Displays OS native dialog for selecting files or directories in the file system.

Each filter string in the `filters` array should be formatted like this: `*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of the filter is optional and can be omitted. It is recommended to set both file extension and MIME type. See also [FileDialog.filters](class_filedialog.md#class-filedialog-property-filters).

Callbacks have the following arguments: `status: bool, selected_paths: PackedStringArray, selected_filter_index: int`. **On Android,** the third callback argument (`selected_filter_index`) is always `0`.

**Note:** This method is implemented if the display server has the FEATURE_NATIVE_DIALOG_FILE feature. Supported platforms include Linux (X11/Wayland), Windows, macOS, and Android.

**Note:** `current_directory` might be ignored.

**Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

**Note:** On Android and Linux, `show_hidden` is ignored.

**Note:** On Android and macOS, native file dialogs have no title.

**Note:** On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. Use [OS.get_granted_permissions()](class_os.md#class-os-method-get-granted-permissions) to get a list of saved bookmarks.

**Note:** On Android, this method uses the Android Storage Access Framework (SAF).

The file picker returns a URI instead of a filesystem path. This URI can be passed directly to [FileAccess](class_fileaccess.md#class-fileaccess) to perform read/write operations.

When using FILE_DIALOG_MODE_OPEN_DIR, it returns a tree URI that grants full access to the selected directory. File operations inside this directory can be performed by passing a path on the form `treeUri#relative/path/to/file` to [FileAccess](class_fileaccess.md#class-fileaccess).

To avoid opening the file picker again after each app restart, you can take persistable URI permission as follows:

GDScript

```gdscript
val uri = "content://com.android..." # URI of the selected file or folder.
val persist = true # Set to false to release the persistable permission.
var android_runtime = Engine.get_singleton("AndroidRuntime")
android_runtime.updatePersistableUriPermission(uri, persist)
```

The persistable URI permission remains valid across app restarts as long as the directory is not moved, renamed, or deleted.

---

[Error](class_@globalscope.md#enum-globalscope-error) **file_dialog_with_options_show**(title: [String](class_string.md#class-string), current_directory: [String](class_string.md#class-string), root: [String](class_string.md#class-string), filename: [String](class_string.md#class-string), show_hidden: [bool](class_bool.md#class-bool), mode: FileDialogMode, filters: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), options: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)], callback: [Callable](class_callable.md#class-callable), parent_window_id: [int](class_int.md#class-int) = 0)

Displays OS native dialog for selecting files or directories in the file system with additional user selectable options.

Each filter string in the `filters` array should be formatted like this: `*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of the filter is optional and can be omitted. It is recommended to set both file extension and MIME type. See also [FileDialog.filters](class_filedialog.md#class-filedialog-property-filters).

`options` is array of [Dictionary](class_dictionary.md#class-dictionary)s with the following keys:

- `"name"` - option's name [String](class_string.md#class-string).
- `"values"` - [PackedStringArray](class_packedstringarray.md#class-packedstringarray) of values. If empty, boolean option (check box) is used.
- `"default"` - default selected option index ([int](class_int.md#class-int)) or default boolean value ([bool](class_bool.md#class-bool)).

Callbacks have the following arguments: `status: bool, selected_paths: PackedStringArray, selected_filter_index: int, selected_option: Dictionary`.

**Note:** This method is implemented if the display server has the FEATURE_NATIVE_DIALOG_FILE_EXTRA feature. Supported platforms include Linux (X11/Wayland), Windows, and macOS.

**Note:** `current_directory` might be ignored.

**Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

**Note:** On Linux (X11), `show_hidden` is ignored.

**Note:** On macOS, native file dialogs have no title.

**Note:** On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. Use [OS.get_granted_permissions()](class_os.md#class-os-method-get-granted-permissions) to get a list of saved bookmarks.

---

 **force_process_and_drop_events**()

Forces window manager processing while ignoring all [InputEvent](class_inputevent.md#class-inputevent)s. See also process_events().

**Note:** This method is implemented on Windows and macOS.

---

[Color](class_color.md#class-color) **get_accent_color**()

Returns OS theme accent color. Returns `Color(0, 0, 0, 0)`, if accent color is unknown.

**Note:** This method is implemented on macOS, Windows, Android, and Linux (X11/Wayland).

---

[Color](class_color.md#class-color) **get_base_color**()

Returns the OS theme base color (default control background). Returns `Color(0, 0, 0, 0)` if the base color is unknown.

**Note:** This method is implemented on macOS, Windows, and Android.

---

[Array](class_array.md#class-array)[[Rect2](class_rect2.md#class-rect2)] **get_display_cutouts**()

Returns an [Array](class_array.md#class-array) of [Rect2](class_rect2.md#class-rect2), each of which is the bounding rectangle for a display cutout or notch. These are non-functional areas on edge-to-edge screens used by cameras and sensors. Returns an empty array if the device does not have cutouts. See also get_display_safe_area().

**Note:** Currently only implemented on Android. Other platforms will return an empty array even if they do have display cutouts or notches.

---

[Rect2i](class_rect2i.md#class-rect2i) **get_display_safe_area**()

Returns the unobscured area of the display where interactive controls should be rendered. See also get_display_cutouts().

**Note:** Currently only implemented on Android and iOS. On other platforms, `screen_get_usable_rect(SCREEN_OF_MAIN_WINDOW)` will be returned as a fallback. See also screen_get_usable_rect().

---

[int](class_int.md#class-int) **get_keyboard_focus_screen**()

Returns the index of the screen containing the window with the keyboard focus, or the primary screen if there's no focused window.

**Note:** This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns the primary screen.

---

[String](class_string.md#class-string) **get_name**()

Returns the name of the **DisplayServer** currently in use. Most operating systems only have a single **DisplayServer**, but Linux has access to more than one **DisplayServer** (currently X11 and Wayland).

The names of built-in display servers are `Windows`, `macOS`, `X11` (Linux), `Wayland` (Linux), `Android`, `iOS`, `web` (HTML5), and `headless` (when started with the `--headless` [command line argument](../tutorials/editor/command_line_tutorial.md)).

---

[int](class_int.md#class-int) **get_primary_screen**()

Returns the index of the primary screen.

**Note:** This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns `0`.

---

[int](class_int.md#class-int) **get_screen_count**()

Returns the number of displays available.

**Note:** This method is implemented on Linux (X11 and Wayland), macOS, and Windows. On other platforms, this method always returns `1`.

---

[int](class_int.md#class-int) **get_screen_from_rect**(rect: [Rect2](class_rect2.md#class-rect2))

Returns the index of the screen that overlaps the most with the given rectangle. Returns INVALID_SCREEN if the rectangle doesn't overlap with any screen or has no area.

---

[bool](class_bool.md#class-bool) **get_swap_cancel_ok**()

Returns `true` if positions of **OK** and **Cancel** buttons are swapped in dialogs. This is enabled by default on Windows to follow interface conventions, and be toggled by changing [ProjectSettings.gui/common/swap_cancel_ok](class_projectsettings.md#class-projectsettings-property-gui-common-swap-cancel-ok).

**Note:** This doesn't affect native dialogs such as the ones spawned by dialog_show().

---

[int](class_int.md#class-int) **get_window_at_screen_position**(position: [Vector2i](class_vector2i.md#class-vector2i))

Returns the ID of the window at the specified screen `position` (in pixels). On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin may be located outside any display like this:

```text
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_window_list**()

Returns the list of Godot window IDs belonging to this process.

**Note:** Native dialogs are not included in this list.

---

[int](class_int.md#class-int) **global_menu_add_check_item**(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds a new checkable item with text `label` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[int](class_int.md#class-int) **global_menu_add_icon_check_item**(menu_root: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds a new checkable item with text `label` and icon `icon` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[int](class_int.md#class-int) **global_menu_add_icon_item**(menu_root: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds a new item with text `label` and icon `icon` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[int](class_int.md#class-int) **global_menu_add_icon_radio_check_item**(menu_root: [String](class_string.md#class-string), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds a new radio-checkable item with text `label` and icon `icon` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See global_menu_set_item_checked() for more info on how to control it.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[int](class_int.md#class-int) **global_menu_add_item**(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds a new item with text `label` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[int](class_int.md#class-int) **global_menu_add_multistate_item**(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds a new item with text `label` to the global menu with ID `menu_root`.

Contrarily to normal binary items, multistate items can have more than two states, as defined by `max_states`. Each press or activate of the item will increase the state by one. The default value is defined by `default_state`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** By default, there's no indication of the current item state, it should be changed manually.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[int](class_int.md#class-int) **global_menu_add_radio_check_item**(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds a new radio-checkable item with text `label` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See global_menu_set_item_checked() for more info on how to control it.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[int](class_int.md#class-int) **global_menu_add_separator**(menu_root: [String](class_string.md#class-string), index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds a separator between items to the global menu with ID `menu_root`. Separators also occupy an index.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[int](class_int.md#class-int) **global_menu_add_submenu_item**(menu_root: [String](class_string.md#class-string), label: [String](class_string.md#class-string), submenu: [String](class_string.md#class-string), index: [int](class_int.md#class-int) = -1)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Adds an item that will act as a submenu of the global menu `menu_root`. The `submenu` argument is the ID of the global menu root that will be shown when the item is clicked.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

 **global_menu_clear**(menu_root: [String](class_string.md#class-string))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Removes all items from the global menu with ID `menu_root`.

**Note:** This method is implemented only on macOS.

**Supported system menu IDs:**

```text
"_main" - Main menu (macOS).
"_dock" - Dock popup menu (macOS).
"_apple" - Apple menu (macOS, custom items added before "Services").
"_window" - Window menu (macOS, custom items added after "Bring All to Front").
"_help" - Help menu (macOS).
```

---

[Key](class_@globalscope.md#enum-globalscope-key) **global_menu_get_item_accelerator**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the accelerator of the item at index `idx`. Accelerators are special combinations of keys that activate the item, no matter which control is focused.

**Note:** This method is implemented only on macOS.

---

[Callable](class_callable.md#class-callable) **global_menu_get_item_callback**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the callback of the item at index `idx`.

**Note:** This method is implemented only on macOS.

---

[int](class_int.md#class-int) **global_menu_get_item_count**(menu_root: [String](class_string.md#class-string))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns number of items in the global menu with ID `menu_root`.

**Note:** This method is implemented only on macOS.

---

[Texture2D](class_texture2d.md#class-texture2d) **global_menu_get_item_icon**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the icon of the item at index `idx`.

**Note:** This method is implemented only on macOS.

---

[int](class_int.md#class-int) **global_menu_get_item_indentation_level**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the horizontal offset of the item at the given `idx`.

**Note:** This method is implemented only on macOS.

---

[int](class_int.md#class-int) **global_menu_get_item_index_from_tag**(menu_root: [String](class_string.md#class-string), tag: [Variant](class_variant.md#class-variant))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the index of the item with the specified `tag`. Indices are automatically assigned to each item by the engine, and cannot be set manually.

**Note:** This method is implemented only on macOS.

---

[int](class_int.md#class-int) **global_menu_get_item_index_from_text**(menu_root: [String](class_string.md#class-string), text: [String](class_string.md#class-string))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the index of the item with the specified `text`. Indices are automatically assigned to each item by the engine, and cannot be set manually.

**Note:** This method is implemented only on macOS.

---

[Callable](class_callable.md#class-callable) **global_menu_get_item_key_callback**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the callback of the item accelerator at index `idx`.

**Note:** This method is implemented only on macOS.

---

[int](class_int.md#class-int) **global_menu_get_item_max_states**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns number of states of a multistate item. See global_menu_add_multistate_item() for details.

**Note:** This method is implemented only on macOS.

---

[int](class_int.md#class-int) **global_menu_get_item_state**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the state of a multistate item. See global_menu_add_multistate_item() for details.

**Note:** This method is implemented only on macOS.

---

[String](class_string.md#class-string) **global_menu_get_item_submenu**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the submenu ID of the item at index `idx`. See global_menu_add_submenu_item() for more info on how to add a submenu.

**Note:** This method is implemented only on macOS.

---

[Variant](class_variant.md#class-variant) **global_menu_get_item_tag**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the metadata of the specified item, which might be of any type. You can set it with global_menu_set_item_tag(), which provides a simple way of assigning context data to items.

**Note:** This method is implemented only on macOS.

---

[String](class_string.md#class-string) **global_menu_get_item_text**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the text of the item at index `idx`.

**Note:** This method is implemented only on macOS.

---

[String](class_string.md#class-string) **global_menu_get_item_tooltip**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns the tooltip associated with the specified index `idx`.

**Note:** This method is implemented only on macOS.

---

[Dictionary](class_dictionary.md#class-dictionary) **global_menu_get_system_menu_roots**()

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns Dictionary of supported system menu IDs and names.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **global_menu_is_item_checkable**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns `true` if the item at index `idx` is checkable in some way, i.e. if it has a checkbox or radio button.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **global_menu_is_item_checked**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns `true` if the item at index `idx` is checked.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **global_menu_is_item_disabled**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns `true` if the item at index `idx` is disabled. When it is disabled it can't be selected, or its action invoked.

See global_menu_set_item_disabled() for more info on how to disable an item.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **global_menu_is_item_hidden**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns `true` if the item at index `idx` is hidden.

See global_menu_set_item_hidden() for more info on how to hide an item.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **global_menu_is_item_radio_checkable**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Returns `true` if the item at index `idx` has radio button-style checkability.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

**Note:** This method is implemented only on macOS.

---

 **global_menu_remove_item**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Removes the item at index `idx` from the global menu `menu_root`.

**Note:** The indices of items after the removed item will be shifted by one.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_accelerator**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), keycode: [Key](class_@globalscope.md#enum-globalscope-key))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the accelerator of the item at index `idx`. `keycode` can be a single [Key](class_@globalscope.md#enum-globalscope-key), or a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_callback**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the callback of the item at index `idx`. Callback is emitted when an item is pressed.

**Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_checkable**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets whether the item at index `idx` has a checkbox. If `false`, sets the type of the item to plain text.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_checked**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the checkstate status of the item at index `idx`.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_disabled**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Enables/disables the item at index `idx`. When it is disabled, it can't be selected and its action can't be invoked.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_hidden**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Hides/shows the item at index `idx`. When it is hidden, an item does not appear in a menu and its action cannot be invoked.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_hover_callbacks**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the callback of the item at index `idx`. The callback is emitted when an item is hovered.

**Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_icon**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Replaces the [Texture2D](class_texture2d.md#class-texture2d) icon of the specified `idx`.

**Note:** This method is implemented only on macOS.

**Note:** This method is not supported by macOS "_dock" menu items.

---

 **global_menu_set_item_indentation_level**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), level: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the horizontal offset of the item at the given `idx`.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_key_callback**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), key_callback: [Callable](class_callable.md#class-callable))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the callback of the item at index `idx`. Callback is emitted when its accelerator is activated.

**Note:** The `key_callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_max_states**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets number of state of a multistate item. See global_menu_add_multistate_item() for details.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_radio_checkable**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the type of the item at the specified index `idx` to radio button. If `false`, sets the type of the item to plain text.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_state**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), state: [int](class_int.md#class-int))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the state of a multistate item. See global_menu_add_multistate_item() for details.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_submenu**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), submenu: [String](class_string.md#class-string))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the submenu of the item at index `idx`. The submenu is the ID of a global menu root that would be shown when the item is clicked.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_tag**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), tag: [Variant](class_variant.md#class-variant))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the metadata of an item, which may be of any type. You can later get it with global_menu_get_item_tag(), which provides a simple way of assigning context data to items.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_text**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the text of the item at index `idx`.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_item_tooltip**(menu_root: [String](class_string.md#class-string), idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Sets the [String](class_string.md#class-string) tooltip of the item at the specified index `idx`.

**Note:** This method is implemented only on macOS.

---

 **global_menu_set_popup_callbacks**(menu_root: [String](class_string.md#class-string), open_callback: [Callable](class_callable.md#class-callable), close_callback: [Callable](class_callable.md#class-callable))

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class-nativemenu) or [PopupMenu](class_popupmenu.md#class-popupmenu) instead.

Registers callables to emit when the menu is respectively about to show or closed. Callback methods should have zero arguments.

---

[bool](class_bool.md#class-bool) **has_additional_outputs**()

Returns `true` if any additional outputs have been registered via register_additional_output().

---

[bool](class_bool.md#class-bool) **has_feature**(feature: Feature)

Returns `true` if the specified `feature` is supported by the current **DisplayServer**, `false` otherwise.

---

[bool](class_bool.md#class-bool) **has_hardware_keyboard**()

Returns `true` if a hardware keyboard is connected.

**Note:** This method is implemented on Android and iOS. On other platforms, this method always returns `true`.

---

 **help_set_search_callbacks**(search_callback: [Callable](class_callable.md#class-callable), action_callback: [Callable](class_callable.md#class-callable))

Sets native help system search callbacks.

`search_callback` has the following arguments: `String search_string, int result_limit` and return a [Dictionary](class_dictionary.md#class-dictionary) with "key, display name" pairs for the search results. Called when the user enters search terms in the `Help` menu.

`action_callback` has the following arguments: `String key`. Called when the user selects a search result in the `Help` menu.

**Note:** This method is implemented only on macOS.

---

[Vector2i](class_vector2i.md#class-vector2i) **ime_get_selection**()

Returns the text selection in the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) composition string, with the [Vector2i](class_vector2i.md#class-vector2i)'s `x` component being the caret position and `y` being the length of the selection.

**Note:** This method is implemented only on macOS.

---

[String](class_string.md#class-string) **ime_get_text**()

Returns the composition string contained within the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) window.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **is_dark_mode**()

Returns `true` if OS is using dark mode.

**Note:** This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).

---

[bool](class_bool.md#class-bool) **is_dark_mode_supported**()

Returns `true` if OS supports dark mode.

**Note:** This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).

---

[bool](class_bool.md#class-bool) **is_in_pip_mode**(window_id: [int](class_int.md#class-int) = 0)

Returns `true` if the application is in picture-in-picture mode.

**Note:** This method is implemented on Android.

---

[bool](class_bool.md#class-bool) **is_touchscreen_available**()

Returns `true` if touch events are available (Android or iOS), the capability is detected on the Web platform or if [ProjectSettings.input_devices/pointing/emulate_touch_from_mouse](class_projectsettings.md#class-projectsettings-property-input-devices-pointing-emulate-touch-from-mouse) is `true`.

---

[bool](class_bool.md#class-bool) **is_window_transparency_available**()

Returns `true` if the window background can be made transparent. This method returns `false` if [ProjectSettings.display/window/per_pixel_transparency/allowed](class_projectsettings.md#class-projectsettings-property-display-window-per-pixel-transparency-allowed) is set to `false`, or if transparency is not supported by the renderer or OS compositor.

---

[int](class_int.md#class-int) **keyboard_get_current_layout**()

Returns active keyboard layout index.

**Note:** This method is implemented on Linux (X11/Wayland), macOS, and Windows.

---

[Key](class_@globalscope.md#enum-globalscope-key) **keyboard_get_keycode_from_physical**(keycode: [Key](class_@globalscope.md#enum-globalscope-key))

Converts a physical (US QWERTY) `keycode` to one in the active keyboard layout.

**Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

[Key](class_@globalscope.md#enum-globalscope-key) **keyboard_get_label_from_physical**(keycode: [Key](class_@globalscope.md#enum-globalscope-key))

Converts a physical (US QWERTY) `keycode` to localized label printed on the key in the active keyboard layout.

**Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

[int](class_int.md#class-int) **keyboard_get_layout_count**()

Returns the number of keyboard layouts.

**Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

[String](class_string.md#class-string) **keyboard_get_layout_language**(index: [int](class_int.md#class-int))

Returns the ISO-639/BCP-47 language code of the keyboard layout at position `index`.

**Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

[String](class_string.md#class-string) **keyboard_get_layout_name**(index: [int](class_int.md#class-int))

Returns the localized name of the keyboard layout at position `index`.

**Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

 **keyboard_set_current_layout**(index: [int](class_int.md#class-int))

Sets the active keyboard layout.

**Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

[[MouseButtonMask](class_@globalscope.md#enum-globalscope-mousebuttonmask)] **mouse_get_button_state**()

Returns the current state of mouse buttons (whether each button is pressed) as a bitmask. If multiple mouse buttons are pressed at the same time, the bits are added together. Equivalent to [Input.get_mouse_button_mask()](class_input.md#class-input-method-get-mouse-button-mask).

---

MouseMode **mouse_get_mode**()

Returns the current mouse mode. See also mouse_set_mode().

---

[Vector2i](class_vector2i.md#class-vector2i) **mouse_get_position**()

Returns the mouse cursor's current position in screen coordinates.

---

 **mouse_set_mode**(mouse_mode: MouseMode)

Sets the current mouse mode. See also mouse_get_mode().

---

 **pip_mode_enter**(window_id: [int](class_int.md#class-int) = 0)

Enters picture-in-picture mode.

**Note:** This method is implemented on Android.

---

 **pip_mode_set_aspect_ratio**(numerator: [int](class_int.md#class-int), denominator: [int](class_int.md#class-int), window_id: [int](class_int.md#class-int) = 0)

Specifies the aspect ratio for picture-in-picture mode.

**Note:** This method is implemented on Android.

---

 **pip_mode_set_auto_enter_on_background**(auto_enter_on_background: [bool](class_bool.md#class-bool), window_id: [int](class_int.md#class-int) = 0)

Specifies whether picture-in-picture mode should be entered automatically when the application goes in the background.

**Note:** This method is implemented on Android.

---

 **process_events**()

Perform window manager processing, including input flushing. See also force_process_and_drop_events(), [Input.flush_buffered_events()](class_input.md#class-input-method-flush-buffered-events) and [Input.use_accumulated_input](class_input.md#class-input-property-use-accumulated-input).

---

 **register_additional_output**(object: [Object](class_object.md#class-object))

Registers an [Object](class_object.md#class-object) which represents an additional output that will be rendered too, beyond normal windows. The [Object](class_object.md#class-object) is only used as an identifier, which can be later passed to unregister_additional_output().

This can be used to prevent Godot from skipping rendering when no normal windows are visible.

---

[int](class_int.md#class-int) **screen_get_dpi**(screen: [int](class_int.md#class-int) = -1)

Returns the dots per inch density of the specified screen. Returns platform specific default value if `screen` is invalid.

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

**Note:** On macOS, returned value is inaccurate if fractional display scaling mode is used.

**Note:** On Android devices, the actual screen densities are grouped into six generalized densities:

```text
   ldpi - 120 dpi
   mdpi - 160 dpi
   hdpi - 240 dpi
  xhdpi - 320 dpi
 xxhdpi - 480 dpi
xxxhdpi - 640 dpi
```

**Note:** This method is implemented on Android, iOS, Linux (X11/Wayland), macOS, Web, and Windows. On other platforms, this method always returns `72`.

---

[Image](class_image.md#class-image) **screen_get_image**(screen: [int](class_int.md#class-int) = -1)

Returns a screenshot of the `screen`. Returns `null` if `screen` is invalid or the **DisplayServer** fails to capture screenshot.

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

**Note:** This method is implemented on Linux (X11, excluding XWayland), macOS, and Windows. On other platforms, this method always returns `null`.

**Note:** On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a screenshot that will not include other application windows or OS elements not related to the application.

---

[Image](class_image.md#class-image) **screen_get_image_rect**(rect: [Rect2i](class_rect2i.md#class-rect2i))

Returns a screenshot of the screen region defined by `rect`. Returns `null` if `rect` is outside screen bounds or the **DisplayServer** fails to capture screenshot.

**Note:** This method is implemented on macOS and Windows. On other platforms, this method always returns `null`.

**Note:** On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a screenshot that will not include other application windows or OS elements not related to the application.

---

[float](class_float.md#class-float) **screen_get_max_scale**()

Returns the greatest scale factor of all screens.

**Note:** On macOS returned value is `2.0` if there is at least one hiDPI (Retina) screen in the system, and `1.0` in all other cases.

**Note:** This method is implemented only on macOS.

---

ScreenOrientation **screen_get_orientation**(screen: [int](class_int.md#class-int) = -1)

Returns the `screen`'s current orientation. See also screen_set_orientation(). Returns SCREEN_LANDSCAPE if `screen` is invalid.

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

**Note:** This method is implemented on Android and iOS. On other platforms, this method always returns SCREEN_LANDSCAPE.

---

[Color](class_color.md#class-color) **screen_get_pixel**(position: [Vector2i](class_vector2i.md#class-vector2i))

Returns the color of the pixel at the given screen `position`. On multi-monitor setups, the screen position is relative to the virtual desktop area.

**Note:** This method is implemented on Linux (X11, excluding XWayland), macOS, and Windows. On other platforms, this method always returns `Color(0, 0, 0, 1)`.

**Note:** On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a color from a screenshot that will not include other application windows or OS elements not related to the application.

---

[Vector2i](class_vector2i.md#class-vector2i) **screen_get_position**(screen: [int](class_int.md#class-int) = -1)

Returns the screen's top-left corner position in pixels. Returns [Vector2i.ZERO](class_vector2i.md#class-vector2i-constant-zero) if `screen` is invalid. On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin might be located outside any display like this:

```text
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

See also screen_get_size().

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

---

[float](class_float.md#class-float) **screen_get_refresh_rate**(screen: [int](class_int.md#class-int) = -1)

Returns the current refresh rate of the specified screen. When V-Sync is enabled, this returns the maximum framerate the project can effectively reach. Returns `-1.0` if `screen` is invalid or the **DisplayServer** fails to find the refresh rate for the specified screen.

To fallback to a default refresh rate if the method fails, try:

```gdscript
var refresh_rate = DisplayServer.screen_get_refresh_rate()
if refresh_rate < 0:
    refresh_rate = 60.0
```

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

**Note:** This method is implemented on Android, iOS, macOS, Linux (X11 and Wayland), and Windows. On other platforms, this method always returns `-1.0`.

---

[float](class_float.md#class-float) **screen_get_scale**(screen: [int](class_int.md#class-int) = -1)

Returns the scale factor of the specified screen by index. Returns `1.0` if `screen` is invalid.

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

**Note:** On macOS, the returned value is `2.0` for hiDPI (Retina) screens, and `1.0` for all other cases.

**Note:** On Linux (Wayland), the returned value is accurate only when `screen` is SCREEN_OF_MAIN_WINDOW. Due to API limitations, passing a direct index will return a rounded-up integer, if the screen has a fractional scale (e.g. `1.25` would get rounded up to `2.0`).

**Note:** This method is implemented on Android, iOS, Web, macOS, and Linux (Wayland). On other platforms, this method always returns `1.0`.

---

[Vector2i](class_vector2i.md#class-vector2i) **screen_get_size**(screen: [int](class_int.md#class-int) = -1)

Returns the screen's size in pixels. See also screen_get_position() and screen_get_usable_rect(). Returns [Vector2i.ZERO](class_vector2i.md#class-vector2i-constant-zero) if `screen` is invalid.

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

---

[Rect2i](class_rect2i.md#class-rect2i) **screen_get_usable_rect**(screen: [int](class_int.md#class-int) = -1)

Returns the portion of the screen that is not obstructed by a status bar in pixels. See also screen_get_size().

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

**Note:** This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns `Rect2i(screen_get_position(screen), screen_get_size(screen))`.

---

[bool](class_bool.md#class-bool) **screen_is_kept_on**()

Returns `true` if the screen should never be turned off by the operating system's power-saving measures. See also screen_set_keep_on().

---

 **screen_set_keep_on**(enable: [bool](class_bool.md#class-bool))

Sets whether the screen should never be turned off by the operating system's power-saving measures. See also screen_is_kept_on().

---

 **screen_set_orientation**(orientation: ScreenOrientation, screen: [int](class_int.md#class-int) = -1)

Sets the `screen`'s `orientation`. See also screen_get_orientation().

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

**Note:** This method is implemented on Android and iOS.

**Note:** On iOS, this method has no effect if [ProjectSettings.display/window/handheld/orientation](class_projectsettings.md#class-projectsettings-property-display-window-handheld-orientation) is not set to SCREEN_SENSOR.

---

 **set_hardware_keyboard_connection_change_callback**(callable: [Callable](class_callable.md#class-callable))

Sets the callback that should be called when a hardware keyboard is connected or disconnected. `callable` should accept a single [bool](class_bool.md#class-bool) argument indicating whether the keyboard has been connected (`true`) or disconnected (`false`).

**Note:** This method is only implemented on Android.

---

 **set_icon**(image: [Image](class_image.md#class-image))

Sets the application icon and icons of all windows with an [Image](class_image.md#class-image). To use icons in the operating system's native format, use set_native_icon() instead.

**Note:** Requires support for FEATURE_ICON.

---

 **set_native_icon**(filename: [String](class_string.md#class-string))

Sets the window icon (usually displayed in the top-left corner) in the operating system's *native* format. The file at `filename` must be in `.ico` format on Windows or `.icns` on macOS. By using specially crafted `.ico` or `.icns` icons, set_native_icon() allows specifying different icons depending on the size the icon is displayed at. This size is determined by the operating system and user preferences (including the display scale factor). To use icons in other formats, use set_icon() instead.

**Note:** Requires support for FEATURE_NATIVE_ICON.

---

 **set_system_theme_change_callback**(callable: [Callable](class_callable.md#class-callable))

Sets the callback that should be called when the system's theme settings are changed. `callable` should accept zero arguments.

**Note:** This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).

---

 **show_emoji_and_symbol_picker**()

Opens system emoji and symbol picker.

**Note:** This method is implemented on macOS and Windows.

---

[Rect2](class_rect2.md#class-rect2) **status_indicator_get_rect**(id: [int](class_int.md#class-int))

Returns the rectangle for the given status indicator `id` in screen coordinates. If the status indicator is not visible, returns an empty [Rect2](class_rect2.md#class-rect2).

**Note:** This method is implemented on macOS and Windows.

---

 **status_indicator_set_callback**(id: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))

Sets the application status indicator activation callback. `callback` should take two arguments: [int](class_int.md#class-int) mouse button index (one of [MouseButton](class_@globalscope.md#enum-globalscope-mousebutton) values) and [Vector2i](class_vector2i.md#class-vector2i) click position in screen coordinates.

**Note:** This method is implemented on macOS and Windows.

---

 **status_indicator_set_icon**(id: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Sets the application status indicator icon.

**Note:** This method is implemented on macOS and Windows.

---

 **status_indicator_set_menu**(id: [int](class_int.md#class-int), menu_rid: [RID](class_rid.md#class-rid))

Sets the application status indicator native popup menu.

**Note:** On macOS, the menu is activated by any mouse button. Its activation callback is *not* triggered.

**Note:** On Windows, the menu is activated by the right mouse button, selecting the status icon and pressing `Shift + F10`, or the applications key. The menu's activation callback for the other mouse buttons is still triggered.

**Note:** Native popup is only supported if [NativeMenu](class_nativemenu.md#class-nativemenu) supports the [NativeMenu.FEATURE_POPUP_MENU](class_nativemenu.md#class-nativemenu-constant-feature-popup-menu) feature.

---

 **status_indicator_set_tooltip**(id: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets the application status indicator tooltip.

**Note:** This method is implemented on macOS and Windows.

---

[String](class_string.md#class-string) **tablet_get_current_driver**()

Returns current active tablet driver name.

**Note:** This method is implemented only on Windows.

---

[int](class_int.md#class-int) **tablet_get_driver_count**()

Returns the total number of available tablet drivers.

**Note:** This method is implemented only on Windows.

---

[String](class_string.md#class-string) **tablet_get_driver_name**(idx: [int](class_int.md#class-int))

Returns the tablet driver name for the given index.

**Note:** This method is implemented only on Windows.

---

 **tablet_set_current_driver**(name: [String](class_string.md#class-string))

Set active tablet driver name.

Supported drivers:

- `winink`: Windows Ink API, default.
- `wintab`: Wacom Wintab API (compatible device driver required).
- `dummy`: Dummy driver, tablet input is disabled.

**Note:** This method is implemented only on Windows.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **tts_get_voices**()

Returns an [Array](class_array.md#class-array) of voice information dictionaries.

Each [Dictionary](class_dictionary.md#class-dictionary) contains two [String](class_string.md#class-string) entries:

- `name` is voice name.
- `id` is voice identifier.
- `language` is language code in `lang_Variant` format. The `lang` part is a 2 or 3-letter code based on the ISO-639 standard, in lowercase. The `Variant` part is an engine-dependent string describing country, region or/and dialect.

Note that Godot depends on system libraries for text-to-speech functionality. These libraries are installed by default on Windows and macOS, but not on all Linux distributions. If they are not present, this method will return an empty list. This applies to both Godot users on Linux, as well as end-users on Linux running Godot games that use text-to-speech.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **tts_get_voices_for_language**(language: [String](class_string.md#class-string))

Returns a [PackedStringArray](class_packedstringarray.md#class-packedstringarray) of voice identifiers for the `language`.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

[bool](class_bool.md#class-bool) **tts_is_paused**()

Returns `true` if the synthesizer is in a paused state.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

[bool](class_bool.md#class-bool) **tts_is_speaking**()

Returns `true` if the synthesizer is generating speech, or have utterance waiting in the queue.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

 **tts_pause**()

Puts the synthesizer into a paused state.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

 **tts_resume**()

Resumes the synthesizer if it was paused.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

 **tts_set_utterance_callback**(event: TTSUtteranceEvent, callable: [Callable](class_callable.md#class-callable))

Adds a callback, which is called when the utterance has started, finished, canceled or reached a text boundary.

- TTS_UTTERANCE_STARTED, TTS_UTTERANCE_ENDED, and TTS_UTTERANCE_CANCELED callable's method should take one [int](class_int.md#class-int) parameter, the utterance ID.
- TTS_UTTERANCE_BOUNDARY callable's method should take two [int](class_int.md#class-int) parameters, the index of the character and the utterance ID.

**Note:** The granularity of the boundary callbacks is engine dependent.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

 **tts_speak**(text: [String](class_string.md#class-string), voice: [String](class_string.md#class-string), volume: [int](class_int.md#class-int) = 50, pitch: [float](class_float.md#class-float) = 1.0, rate: [float](class_float.md#class-float) = 1.0, utterance_id: [int](class_int.md#class-int) = 0, interrupt: [bool](class_bool.md#class-bool) = false)

Adds an utterance to the queue. If `interrupt` is `true`, the queue is cleared first.

- `voice` identifier is one of the `"id"` values returned by tts_get_voices() or one of the values returned by tts_get_voices_for_language().
- `volume` ranges from `0` (lowest) to `100` (highest).
- `pitch` ranges from `0.0` (lowest) to `2.0` (highest), `1.0` is default pitch for the current voice.
- `rate` ranges from `0.1` (lowest) to `10.0` (highest), `1.0` is a normal speaking rate. Other values act as a percentage relative.
- `utterance_id` is passed as a parameter to the callback functions.

**Note:** On Windows and Linux (X11/Wayland), utterance `text` can use SSML markup. SSML support is engine and voice dependent. If the engine does not support SSML, you should strip out all XML markup before calling tts_speak().

**Note:** The granularity of pitch, rate, and volume is engine and voice dependent. Values may be truncated.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

 **tts_stop**()

Stops synthesis in progress and removes all utterances from the queue.

**Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

 **unregister_additional_output**(object: [Object](class_object.md#class-object))

Unregisters an [Object](class_object.md#class-object) representing an additional output, that was registered via register_additional_output().

---

[int](class_int.md#class-int) **virtual_keyboard_get_height**()

Returns the on-screen keyboard's height in pixels. Returns `0` if there is no keyboard or if it is currently hidden.

**Note:** On Android 7 and 8, the keyboard height may return `0` the first time the keyboard is opened in non-immersive mode. This behavior does not occur in immersive mode.

---

 **virtual_keyboard_hide**()

Hides the virtual keyboard if it is shown, does nothing otherwise.

---

 **virtual_keyboard_show**(existing_text: [String](class_string.md#class-string), position: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), type: VirtualKeyboardType = 0, max_length: [int](class_int.md#class-int) = -1, cursor_start: [int](class_int.md#class-int) = -1, cursor_end: [int](class_int.md#class-int) = -1)

Shows the virtual keyboard if the platform has one.

`existing_text` parameter is useful for implementing your own [LineEdit](class_lineedit.md#class-lineedit) or [TextEdit](class_textedit.md#class-textedit), as it tells the virtual keyboard what text has already been typed (the virtual keyboard uses it for auto-correct and predictions).

`position` parameter is the screen space [Rect2](class_rect2.md#class-rect2) of the edited text.

`type` parameter allows configuring which type of virtual keyboard to show.

`max_length` limits the number of characters that can be entered if different from `-1`.

`cursor_start` can optionally define the current text cursor position if `cursor_end` is not set.

`cursor_start` and `cursor_end` can optionally define the current text selection.

**Note:** This method is implemented on Android, iOS and Web.

---

 **warp_mouse**(position: [Vector2i](class_vector2i.md#class-vector2i))

Sets the mouse cursor position to the given `position` relative to an origin at the upper left corner of the currently focused game Window Manager window.

**Note:** warp_mouse() is only supported on Windows, macOS, and Linux (X11/Wayland). It has no effect on Android, iOS, and Web.

---

[bool](class_bool.md#class-bool) **window_can_draw**(window_id: [int](class_int.md#class-int) = 0)

Returns `true` if anything can be drawn in the window specified by `window_id`, `false` otherwise. Using the `--disable-render-loop` command line argument or a headless build will return `false`.

---

[int](class_int.md#class-int) **window_get_active_popup**()

Returns ID of the active popup window, or INVALID_WINDOW_ID if there is none.

---

[int](class_int.md#class-int) **window_get_attached_instance_id**(window_id: [int](class_int.md#class-int) = 0)

Returns the [Object.get_instance_id()](class_object.md#class-object-method-get-instance-id) of the [Window](class_window.md#class-window) the `window_id` is attached to.

---

[int](class_int.md#class-int) **window_get_current_screen**(window_id: [int](class_int.md#class-int) = 0)

Returns the screen the window specified by `window_id` is currently positioned on. If the screen overlaps multiple displays, the screen where the window's center is located is returned. See also window_set_current_screen(). Returns INVALID_SCREEN if `window_id` is invalid.

**Note:** This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns `0`.

---

[bool](class_bool.md#class-bool) **window_get_flag**(flag: WindowFlags, window_id: [int](class_int.md#class-int) = 0)

Returns the current value of the given window's `flag`.

---

[float](class_float.md#class-float) **window_get_hdr_output_current_max_luminance**(window_id: [int](class_int.md#class-int) = 0)

**Experimental:** This method may be changed or removed in future versions.

When window_is_hdr_output_enabled() returns `true`, this returns the current maximum luminance in nits (cd/m²) for HDR output by the window specified by `window_id`. If the maximum luminance is being automatically adjusted based on the screen's capabilities, this method will return that value. Otherwise, it will return the value set by window_set_hdr_output_max_luminance(). This maximum luminance value is used when calculating window_get_output_max_linear_value().

**Note:** This maximum luminance may not match the physical behavior of the screen, but will always be proportionally correct relative to window_get_hdr_output_current_reference_luminance().

---

[float](class_float.md#class-float) **window_get_hdr_output_current_reference_luminance**(window_id: [int](class_int.md#class-int) = 0)

When window_is_hdr_output_enabled() returns `true`, this returns the current reference white luminance in nits (cd/m²) for HDR output by the window specified by `window_id`. If the reference luminance is being automatically adjusted to match the operating system brightness, this will return that value. Otherwise, it will return the value set by window_set_hdr_output_reference_luminance(). This reference luminance value is used when calculating window_get_output_max_linear_value().

**Note:** This reference white luminance may not match the physical behavior of the screen, but will always be proportionally correct relative to window_get_hdr_output_current_max_luminance().

---

[float](class_float.md#class-float) **window_get_hdr_output_max_luminance**(window_id: [int](class_int.md#class-int) = 0)

**Experimental:** This method may be changed or removed in future versions.

Returns the maximum luminance in nits (cd/m²) set for HDR output by the window specified by `window_id`. Negative values indicate that the value is being automatically adjusted based on the screen's capabilities. See also window_get_hdr_output_current_max_luminance().

---

[float](class_float.md#class-float) **window_get_hdr_output_reference_luminance**(window_id: [int](class_int.md#class-int) = 0)

Returns the reference white luminance in nits (cd/m²) set for HDR output by the window specified by `window_id`. Negative values indicate that the value is being automatically adjusted to match the operating system brightness. See also window_get_hdr_output_current_reference_luminance().

---

[Vector2i](class_vector2i.md#class-vector2i) **window_get_max_size**(window_id: [int](class_int.md#class-int) = 0)

Returns the window's maximum size (in pixels). See also window_set_max_size().

---

[Vector2i](class_vector2i.md#class-vector2i) **window_get_min_size**(window_id: [int](class_int.md#class-int) = 0)

Returns the window's minimum size (in pixels). See also window_set_min_size().

---

WindowMode **window_get_mode**(window_id: [int](class_int.md#class-int) = 0)

Returns the mode of the given window.

---

[int](class_int.md#class-int) **window_get_native_handle**(handle_type: HandleType, window_id: [int](class_int.md#class-int) = 0)

Returns internal structure pointers for use in plugins.

**Note:** This method is implemented on Android, Linux (X11/Wayland), macOS, and Windows.

---

[float](class_float.md#class-float) **window_get_output_max_linear_value**(window_id: [int](class_int.md#class-int) = 0)

Returns the maximum value for linear color components that can be displayed for the window specified by `window_id`, regardless of SDR or HDR output. Returns `1.0` if HDR is not enabled or not supported. When HDR output is enabled, this is calculated based on window_get_hdr_output_current_reference_luminance() and window_get_hdr_output_current_max_luminance(). The [Window.output_max_linear_value_changed](class_window.md#class-window-signal-output-max-linear-value-changed) signal will be emitted whenever this value changes. This value is used by tonemapping and other [Environment](class_environment.md#class-environment) effects to ensure that bright colors are presented in the range that can be displayed by this window. Corresponds to [Window.get_output_max_linear_value()](class_window.md#class-window-method-get-output-max-linear-value).

---

[Rect2i](class_rect2i.md#class-rect2i) **window_get_popup_safe_rect**(window: [int](class_int.md#class-int))

Returns the bounding box of control, or menu item that was used to open the popup window, in the screen coordinate system.

---

[Vector2i](class_vector2i.md#class-vector2i) **window_get_position**(window_id: [int](class_int.md#class-int) = 0)

Returns the position of the client area of the given window on the screen.

---

[Vector2i](class_vector2i.md#class-vector2i) **window_get_position_with_decorations**(window_id: [int](class_int.md#class-int) = 0)

Returns the position of the given window on the screen including the borders drawn by the operating system. See also window_get_position().

---

[Vector3i](class_vector3i.md#class-vector3i) **window_get_safe_title_margins**(window_id: [int](class_int.md#class-int) = 0)

Returns left margins (`x`), right margins (`y`) and height (`z`) of the title that are safe to use (contains no buttons or other elements) when WINDOW_FLAG_EXTEND_TO_TITLE flag is set.

---

[Vector2i](class_vector2i.md#class-vector2i) **window_get_size**(window_id: [int](class_int.md#class-int) = 0)

Returns the size of the window specified by `window_id` (in pixels), excluding the borders drawn by the operating system. This is also called the "client area". See also window_get_size_with_decorations(), window_set_size() and window_get_position().

---

[Vector2i](class_vector2i.md#class-vector2i) **window_get_size_with_decorations**(window_id: [int](class_int.md#class-int) = 0)

Returns the size of the window specified by `window_id` (in pixels), including the borders drawn by the operating system. See also window_get_size().

---

[Vector2i](class_vector2i.md#class-vector2i) **window_get_title_size**(title: [String](class_string.md#class-string), window_id: [int](class_int.md#class-int) = 0)

Returns the estimated window title bar size (including text and window buttons) for the window specified by `window_id` (in pixels). This method does not change the window title.

**Note:** This method is implemented on macOS and Windows.

---

VSyncMode **window_get_vsync_mode**(window_id: [int](class_int.md#class-int) = 0)

Returns the V-Sync mode of the given window.

---

[bool](class_bool.md#class-bool) **window_is_focused**(window_id: [int](class_int.md#class-int) = 0)

Returns `true` if the window specified by `window_id` is focused.

---

[bool](class_bool.md#class-bool) **window_is_hdr_output_enabled**(window_id: [int](class_int.md#class-int) = 0)

Returns `true` if HDR output is currently enabled for the window specified by `window_id`. The returned value may change dynamically based on system settings, screen capabilities, and which screen the window is currently on.

---

[bool](class_bool.md#class-bool) **window_is_hdr_output_requested**(window_id: [int](class_int.md#class-int) = 0)

Returns `true` if HDR output is requested for the window specified by `window_id`. Corresponds to [Window.hdr_output_requested](class_window.md#class-window-property-hdr-output-requested).

---

[bool](class_bool.md#class-bool) **window_is_hdr_output_supported**(window_id: [int](class_int.md#class-int) = 0)

Returns `true` if the window specified by `window_id` supports HDR output. This depends on the platform, screen capabilities, system settings, and the screen the window is currently on.

---

[bool](class_bool.md#class-bool) **window_is_maximize_allowed**(window_id: [int](class_int.md#class-int) = 0)

Returns `true` if the given window can be maximized (the maximize button is enabled).

---

[bool](class_bool.md#class-bool) **window_maximize_on_title_dbl_click**()

Returns `true` if double-clicking on a window's title should maximize it.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **window_minimize_on_title_dbl_click**()

Returns `true` if double-clicking on a window's title should minimize it.

**Note:** This method is implemented only on macOS.

---

 **window_move_to_foreground**(window_id: [int](class_int.md#class-int) = 0)

Moves the window specified by `window_id` to the foreground, so that it is visible over other windows.

---

 **window_request_attention**(window_id: [int](class_int.md#class-int) = 0)

Makes the window specified by `window_id` request attention, which is materialized by the window title and taskbar entry blinking until the window is focused. This usually has no visible effect if the window is currently focused. The exact behavior varies depending on the operating system.

---

 **window_request_hdr_output**(enable: [bool](class_bool.md#class-bool), window_id: [int](class_int.md#class-int) = 0)

If `enable` is `true`, HDR output is requested for the window specified by `window_id`. The window will automatically switch between HDR and SDR if it is moved between screens, screen capabilities change, or system settings are modified. This will internally force [Viewport.use_hdr_2d](class_viewport.md#class-viewport-property-use-hdr-2d) to be enabled on the main [Viewport](class_viewport.md#class-viewport). All other [SubViewport](class_subviewport.md#class-subviewport) of the [Window](class_window.md#class-window) must have their [Viewport.use_hdr_2d](class_viewport.md#class-viewport-property-use-hdr-2d) property enabled to produce HDR output. Corresponds to [Window.hdr_output_requested](class_window.md#class-window-property-hdr-output-requested).

---

 **window_set_color**(color: [Color](class_color.md#class-color))

Sets the background color of the root window.

**Note:** This method is implemented only on Android.

---

 **window_set_current_screen**(screen: [int](class_int.md#class-int), window_id: [int](class_int.md#class-int) = 0)

Moves the window specified by `window_id` to the specified `screen`. See also window_get_current_screen().

**Note:** One of the following constants can be used as `screen`: SCREEN_OF_MAIN_WINDOW, SCREEN_PRIMARY, SCREEN_WITH_MOUSE_FOCUS, or SCREEN_WITH_KEYBOARD_FOCUS.

**Note:** This method is implemented on Linux/X11, macOS, and Windows.

---

 **window_set_drop_files_callback**(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)

Sets the `callback` that should be called when files are dropped from the operating system's file manager to the window specified by `window_id`. `callback` should take one [PackedStringArray](class_packedstringarray.md#class-packedstringarray) argument, which is the list of dropped files.

**Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class-window) node will override its default implementation, which can introduce bugs.

**Note:** This method is implemented on Windows, macOS, Linux (X11/Wayland), and Web.

---

 **window_set_exclusive**(window_id: [int](class_int.md#class-int), exclusive: [bool](class_bool.md#class-bool))

If set to `true`, this window will always stay on top of its parent window, parent window will ignore input while this window is opened.

**Note:** On macOS, exclusive windows are confined to the same space (virtual desktop or screen) as the parent window.

**Note:** This method is implemented on macOS and Windows.

---

 **window_set_flag**(flag: WindowFlags, enabled: [bool](class_bool.md#class-bool), window_id: [int](class_int.md#class-int) = 0)

Enables or disables the given window's given `flag`.

---

 **window_set_hdr_output_max_luminance**(max_luminance: [float](class_float.md#class-float), window_id: [int](class_int.md#class-int) = 0)

**Experimental:** This method may be changed or removed in future versions.

Sets the maximum luminance in nits (cd/m²) for HDR output by the window specified by `window_id`. If `max_luminance` is negative, the window uses the screen's maximum luminance that is reported by the operating system. By default, this luminance is set to `-1.0` for every window. Typically this property should be left at this default value, but may optionally be exposed through in-game settings to allow the player to correct an inaccurate maximum luminance reported by the operating system. See also window_get_hdr_output_current_max_luminance() and window_get_hdr_output_max_luminance().

**Note:** This method is only implemented on macOS and Windows. Other platforms will always use the screen's maximum luminance that is reported by the operating system.

---

 **window_set_hdr_output_reference_luminance**(reference_luminance: [float](class_float.md#class-float), window_id: [int](class_int.md#class-int) = 0)

Sets the reference white luminance in nits (cd/m²) for HDR output by the window specified by `window_id`. If `reference_luminance` is negative, the window automatically adjusts to the brightness set by the operating system. By default, this luminance is set to `-1.0` for every window. Typically this property should be left at this default value, but may optionally be exposed as an "HDR Brightness" in-game setting to allow the player to adjust the brightness of their game, independently of their device settings. See also window_get_hdr_output_current_reference_luminance() and window_get_hdr_output_reference_luminance().

**Note:** This method is only implemented on Windows. Other platforms will always use the reference luminance that is reported by the operating system.

---

 **window_set_icon**(icon: [Image](class_image.md#class-image), window_id: [int](class_int.md#class-int) = 0)

Sets the window icon (usually displayed in the top-left corner) for the window specified by `window_id`.

**Note:** This method is implemented on Linux and Windows.

---

 **window_set_ime_active**(active: [bool](class_bool.md#class-bool), window_id: [int](class_int.md#class-int) = 0)

Sets whether [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) should be enabled for the window specified by `window_id`. See also window_set_ime_position().

---

 **window_set_ime_position**(position: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)

Sets the position of the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) popup for the specified `window_id`. Only effective if window_set_ime_active() was set to `true` for the specified `window_id`.

---

 **window_set_input_event_callback**(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)

Sets the `callback` that should be called when any [InputEvent](class_inputevent.md#class-inputevent) is sent to the window specified by `window_id`.

**Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class-window) node will override its default implementation, which can introduce bugs.

---

 **window_set_input_text_callback**(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)

Sets the `callback` that should be called when text is entered using the virtual keyboard to the window specified by `window_id`.

**Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class-window) node will override its default implementation, which can introduce bugs.

---

 **window_set_max_size**(max_size: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)

Sets the maximum size of the window specified by `window_id` in pixels. Normally, the user will not be able to drag the window to make it larger than the specified size. See also window_get_max_size().

**Note:** It's recommended to change this value using [Window.max_size](class_window.md#class-window-property-max-size) instead.

**Note:** Using third-party tools, it is possible for users to disable window geometry restrictions and therefore bypass this limit.

---

 **window_set_min_size**(min_size: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)

Sets the minimum size for the given window to `min_size` in pixels. Normally, the user will not be able to drag the window to make it smaller than the specified size. See also window_get_min_size().

**Note:** It's recommended to change this value using [Window.min_size](class_window.md#class-window-property-min-size) instead.

**Note:** By default, the main window has a minimum size of `Vector2i(64, 64)`. This prevents issues that can arise when the window is resized to a near-zero size.

**Note:** Using third-party tools, it is possible for users to disable window geometry restrictions and therefore bypass this limit.

---

 **window_set_mode**(mode: WindowMode, window_id: [int](class_int.md#class-int) = 0)

Sets window mode for the given window to `mode`.

**Note:** On Android, setting it to WINDOW_MODE_FULLSCREEN or WINDOW_MODE_EXCLUSIVE_FULLSCREEN will enable immersive mode.

**Note:** Setting the window to full screen forcibly sets the borderless flag to `true`, so make sure to set it back to `false` when not wanted.

---

 **window_set_mouse_passthrough**(region: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), window_id: [int](class_int.md#class-int) = 0)

Sets a polygonal region of the window which accepts mouse events. Mouse events outside the region will be passed through.

Passing an empty array will disable passthrough support (all mouse events will be intercepted by the window, which is the default behavior).

GDScript

```gdscript
# Set region, using Path2D node.
DisplayServer.window_set_mouse_passthrough($Path2D.curve.get_baked_points())

# Set region, using Polygon2D node.
DisplayServer.window_set_mouse_passthrough($Polygon2D.polygon)

# Reset region to default.
DisplayServer.window_set_mouse_passthrough([])
```

C#

```csharp
// Set region, using Path2D node.
DisplayServer.WindowSetMousePassthrough(GetNode<Path2D>("Path2D").Curve.GetBakedPoints());

// Set region, using Polygon2D node.
DisplayServer.WindowSetMousePassthrough(GetNode<Polygon2D>("Polygon2D").Polygon);

// Reset region to default.
DisplayServer.WindowSetMousePassthrough([]);
```

**Note:** On Windows, the portion of a window that lies outside the region is not drawn, while on Linux (X11) and macOS it is.

**Note:** This method is implemented on Linux (X11), macOS and Windows.

---

 **window_set_popup_safe_rect**(window: [int](class_int.md#class-int), rect: [Rect2i](class_rect2i.md#class-rect2i))

Sets the bounding box of control, or menu item that was used to open the popup window, in the screen coordinate system. Clicking this area will not auto-close this popup.

---

 **window_set_position**(position: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)

Sets the position of the given window to `position`. On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin may be located outside any display like this:

```text
* (0, 0)        +-------+
                |       |
+-------------+ |       |
|             | |       |
|             | |       |
+-------------+ +-------+
```

See also window_get_position() and window_set_size().

**Note:** It's recommended to change this value using [Window.position](class_window.md#class-window-property-position) instead.

**Note:** On Linux (Wayland): this method is a no-op.

---

 **window_set_rect_changed_callback**(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)

Sets the `callback` that will be called when the window specified by `window_id` is moved or resized.

**Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class-window) node will override its default implementation, which can introduce bugs.

---

 **window_set_size**(size: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)

Sets the size of the given window to `size` (in pixels). See also window_get_size() and window_get_position().

**Note:** It's recommended to change this value using [Window.size](class_window.md#class-window-property-size) instead.

---

 **window_set_taskbar_progress_state**(state: ProgressState, window_id: [int](class_int.md#class-int) = 0)

Sets the type and state of the progress bar on the taskbar/dock icon of the window specified by `window_id`. See ProgressState for possible values and how each mode behaves.

**Note:** This method is implemented only on Windows and macOS.

**Note:** On macOS, the progress bar is displayed only for the main window.

---

 **window_set_taskbar_progress_value**(value: [float](class_float.md#class-float), window_id: [int](class_int.md#class-int) = 0)

Creates a progress bar on the taskbar/dock icon of the window specified by `window_id` if it does not exist, sets the progress of the icon.

`value` acts as a relative percentage value, ranges from `0.0` (lowest) to `1.0` (highest).

**Note:** This method is implemented only on Windows and macOS.

**Note:** On macOS, the progress bar is displayed only for the main window.

---

 **window_set_title**(title: [String](class_string.md#class-string), window_id: [int](class_int.md#class-int) = 0)

Sets the title of the given window to `title`.

**Note:** It's recommended to change this value using [Window.title](class_window.md#class-window-property-title) instead.

**Note:** Avoid changing the window title every frame, as this can cause performance issues on certain window managers. Try to change the window title only a few times per second at most.

---

 **window_set_transient**(window_id: [int](class_int.md#class-int), parent_window_id: [int](class_int.md#class-int))

Sets window transient parent. Transient window will be destroyed with its transient parent and will return focus to their parent when closed. The transient window is displayed on top of a non-exclusive full-screen parent window. Transient windows can't enter full-screen mode.

**Note:** It's recommended to change this value using [Window.transient](class_window.md#class-window-property-transient) instead.

**Note:** The behavior might be different depending on the platform.

---

 **window_set_vsync_mode**(vsync_mode: VSyncMode, window_id: [int](class_int.md#class-int) = 0)

Sets the V-Sync mode of the given window. See also [ProjectSettings.display/window/vsync/vsync_mode](class_projectsettings.md#class-projectsettings-property-display-window-vsync-vsync-mode).

Depending on the platform and used renderer, the engine will fall back to VSYNC_ENABLED if the desired mode is not supported.

**Note:** V-Sync modes other than VSYNC_ENABLED are only supported in the Forward+ and Mobile rendering methods, not Compatibility.

---

 **window_set_window_buttons_offset**(offset: [Vector2i](class_vector2i.md#class-vector2i), window_id: [int](class_int.md#class-int) = 0)

When WINDOW_FLAG_EXTEND_TO_TITLE flag is set, set offset to the center of the first titlebar button.

**Note:** This flag is implemented only on macOS.

---

 **window_set_window_event_callback**(callback: [Callable](class_callable.md#class-callable), window_id: [int](class_int.md#class-int) = 0)

Sets the `callback` that will be called when an event occurs in the window specified by `window_id`.

**Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class-window) node will override its default implementation, which can introduce bugs.

---

 **window_start_drag**(window_id: [int](class_int.md#class-int) = 0)

Starts an interactive drag operation on the window with the given `window_id`, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's title bar. Using this method allows the window to participate in space switching, tiling, and other system features.

**Note:** This method is implemented on Linux (X11/Wayland), macOS, and Windows.

---

 **window_start_resize**(edge: WindowResizeEdge, window_id: [int](class_int.md#class-int) = 0)

Starts an interactive resize operation on the window with the given `window_id`, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's edge.

**Note:** This method is implemented on Linux (X11/Wayland), macOS, and Windows.
