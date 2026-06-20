# AccessibilityServer

**Inherits:** [Object](class_object.md#class-object)

A server interface for screen reader support.

## Methods

| [RID](class_rid.md#class-rid)             | create_element(window_id: [int](class_int.md#class-int), role: AccessibilityRole)                                                                                                                                                             |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)             | create_sub_element(parent_rid: [RID](class_rid.md#class-rid), role: AccessibilityRole, insert_pos: [int](class_int.md#class-int) = -1)                                                                                                    |
| [RID](class_rid.md#class-rid)             | create_sub_text_edit_elements(parent_rid: [RID](class_rid.md#class-rid), shaped_text: [RID](class_rid.md#class-rid), min_height: [float](class_float.md#class-float), insert_pos: [int](class_int.md#class-int) = -1, is_last_line: [bool](class_bool.md#class-bool) = false) |
| [Variant](class_variant.md#class-variant) | element_get_meta(id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                        |
|                                           | element_set_meta(id: [RID](class_rid.md#class-rid), meta: [Variant](class_variant.md#class-variant))                                                                                                                                                                                       |
|                                           | free_element(id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)             | get_window_root(window_id: [int](class_int.md#class-int))                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)          | has_element(id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)          | is_supported()                                                                                                                                                                                                                                                                                 |
|                                           | set_window_focused(window_id: [int](class_int.md#class-int), focused: [bool](class_bool.md#class-bool))                                                                                                                                                                                  |
|                                           | set_window_rect(window_id: [int](class_int.md#class-int), rect_out: [Rect2](class_rect2.md#class-rect2), rect_in: [Rect2](class_rect2.md#class-rect2))                                                                                                                                      |
|                                           | update_add_action(id: [RID](class_rid.md#class-rid), action: AccessibilityAction, callable: [Callable](class_callable.md#class-callable))                                                                                                |
|                                           | update_add_child(id: [RID](class_rid.md#class-rid), child_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                               |
|                                           | update_add_custom_action(id: [RID](class_rid.md#class-rid), action_id: [int](class_int.md#class-int), action_description: [String](class_string.md#class-string))                                                                                                                  |
|                                           | update_add_related_controls(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                       |
|                                           | update_add_related_described_by(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                               |
|                                           | update_add_related_details(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                         |
|                                           | update_add_related_flow_to(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                         |
|                                           | update_add_related_labeled_by(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                   |
|                                           | update_add_related_radio_group(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))                                                                                                                                                                 |
|                                           | update_set_active_descendant(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                       |
|                                           | update_set_background_color(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                      |
|                                           | update_set_bounds(id: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                           |
|                                           | update_set_braille_label(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))                                                                                                                                                                          |
|                                           | update_set_braille_role_description(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))                                                                                                                                             |
|                                           | update_set_checked(id: [RID](class_rid.md#class-rid), checekd: [bool](class_bool.md#class-bool))                                                                                                                                                                                         |
|                                           | update_set_classname(id: [RID](class_rid.md#class-rid), classname: [String](class_string.md#class-string))                                                                                                                                                                             |
|                                           | update_set_color_value(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                |
|                                           | update_set_description(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))                                                                                                                                                                       |
|                                           | update_set_error_message(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                               |
|                                           | update_set_extra_info(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))                                                                                                                                                                                |
|                                           | update_set_flag(id: [RID](class_rid.md#class-rid), flag: AccessibilityFlags, value: [bool](class_bool.md#class-bool))                                                                                                                       |
|                                           | update_set_focus(id: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                        |
|                                           | update_set_foreground_color(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                      |
|                                           | update_set_in_page_link_target(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                   |
|                                           | update_set_language(id: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))                                                                                                                                                                                |
|                                           | update_set_list_item_count(id: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))                                                                                                                                                                               |
|                                           | update_set_list_item_expanded(id: [RID](class_rid.md#class-rid), expanded: [bool](class_bool.md#class-bool))                                                                                                                                                                  |
|                                           | update_set_list_item_index(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                              |
|                                           | update_set_list_item_level(id: [RID](class_rid.md#class-rid), level: [int](class_int.md#class-int))                                                                                                                                                                              |
|                                           | update_set_list_item_selected(id: [RID](class_rid.md#class-rid), selected: [bool](class_bool.md#class-bool))                                                                                                                                                                  |
|                                           | update_set_list_orientation(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool))                                                                                                                                                                      |
|                                           | update_set_live(id: [RID](class_rid.md#class-rid), live: AccessibilityLiveMode)                                                                                                                                                          |
|                                           | update_set_member_of(id: [RID](class_rid.md#class-rid), group_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                       |
|                                           | update_set_name(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))                                                                                                                                                                                            |
|                                           | update_set_next_on_line(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                                 |
|                                           | update_set_num_jump(id: [RID](class_rid.md#class-rid), jump: [float](class_float.md#class-float))                                                                                                                                                                                       |
|                                           | update_set_num_range(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))                                                                                                                                            |
|                                           | update_set_num_step(id: [RID](class_rid.md#class-rid), step: [float](class_float.md#class-float))                                                                                                                                                                                       |
|                                           | update_set_num_value(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))                                                                                                                                                                                 |
|                                           | update_set_placeholder(id: [RID](class_rid.md#class-rid), placeholder: [String](class_string.md#class-string))                                                                                                                                                                       |
|                                           | update_set_popup_type(id: [RID](class_rid.md#class-rid), popup: AccessibilityPopupType)                                                                                                                                           |
|                                           | update_set_previous_on_line(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))                                                                                                                                                                         |
|                                           | update_set_role(id: [RID](class_rid.md#class-rid), role: AccessibilityRole)                                                                                                                                                                  |
|                                           | update_set_role_description(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))                                                                                                                                                             |
|                                           | update_set_scroll_x(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))                                                                                                                                                                                   |
|                                           | update_set_scroll_x_range(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))                                                                                                                                  |
|                                           | update_set_scroll_y(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))                                                                                                                                                                                   |
|                                           | update_set_scroll_y_range(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))                                                                                                                                  |
|                                           | update_set_shortcut(id: [RID](class_rid.md#class-rid), shortcut: [String](class_string.md#class-string))                                                                                                                                                                                |
|                                           | update_set_state_description(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))                                                                                                                                                           |
|                                           | update_set_table_cell_position(id: [RID](class_rid.md#class-rid), row_index: [int](class_int.md#class-int), column_index: [int](class_int.md#class-int))                                                                                                                     |
|                                           | update_set_table_cell_span(id: [RID](class_rid.md#class-rid), row_span: [int](class_int.md#class-int), column_span: [int](class_int.md#class-int))                                                                                                                               |
|                                           | update_set_table_column_count(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))                                                                                                                                                                        |
|                                           | update_set_table_column_index(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                        |
|                                           | update_set_table_row_count(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))                                                                                                                                                                              |
|                                           | update_set_table_row_index(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                              |
|                                           | update_set_text_align(id: [RID](class_rid.md#class-rid), align: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))                                                                                                                                    |
|                                           | update_set_text_decorations(id: [RID](class_rid.md#class-rid), underline: [bool](class_bool.md#class-bool), strikethrough: [bool](class_bool.md#class-bool), overline: [bool](class_bool.md#class-bool), color: [Color](class_color.md#class-color) = Color(0, 0, 0, 1))        |
|                                           | update_set_text_orientation(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool))                                                                                                                                                                      |
|                                           | update_set_text_selection(id: [RID](class_rid.md#class-rid), text_start_id: [RID](class_rid.md#class-rid), start_char: [int](class_int.md#class-int), text_end_id: [RID](class_rid.md#class-rid), end_char: [int](class_int.md#class-int))                                        |
|                                           | update_set_tooltip(id: [RID](class_rid.md#class-rid), tooltip: [String](class_string.md#class-string))                                                                                                                                                                                   |
|                                           | update_set_transform(id: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                              |
|                                           | update_set_url(id: [RID](class_rid.md#class-rid), url: [String](class_string.md#class-string))                                                                                                                                                                                               |
|                                           | update_set_value(id: [RID](class_rid.md#class-rid), value: [String](class_string.md#class-string))                                                                                                                                                                                         |

---

## Enumerations

enum **AccessibilityRole**:

AccessibilityRole **ROLE_UNKNOWN** = `0`

Unknown or custom role.

AccessibilityRole **ROLE_DEFAULT_BUTTON** = `1`

Default dialog button element.

AccessibilityRole **ROLE_AUDIO** = `2`

Audio player element.

AccessibilityRole **ROLE_VIDEO** = `3`

Video player element.

AccessibilityRole **ROLE_STATIC_TEXT** = `4`

Non-editable text label.

AccessibilityRole **ROLE_CONTAINER** = `5`

Container element. Elements with this role are used for internal structure and ignored by screen readers.

AccessibilityRole **ROLE_PANEL** = `6`

Panel container element.

AccessibilityRole **ROLE_BUTTON** = `7`

Button element.

AccessibilityRole **ROLE_LINK** = `8`

Link element.

AccessibilityRole **ROLE_CHECK_BOX** = `9`

Check box element.

AccessibilityRole **ROLE_RADIO_BUTTON** = `10`

Radio button element.

AccessibilityRole **ROLE_CHECK_BUTTON** = `11`

Check button element.

AccessibilityRole **ROLE_SCROLL_BAR** = `12`

Scroll bar element.

AccessibilityRole **ROLE_SCROLL_VIEW** = `13`

Scroll container element.

AccessibilityRole **ROLE_SPLITTER** = `14`

Container splitter handle element.

AccessibilityRole **ROLE_SLIDER** = `15`

Slider element.

AccessibilityRole **ROLE_SPIN_BUTTON** = `16`

Spin box element.

AccessibilityRole **ROLE_PROGRESS_INDICATOR** = `17`

Progress indicator element.

AccessibilityRole **ROLE_TEXT_FIELD** = `18`

Editable text field element.

AccessibilityRole **ROLE_MULTILINE_TEXT_FIELD** = `19`

Multiline editable text field element.

AccessibilityRole **ROLE_COLOR_PICKER** = `20`

Color picker element.

AccessibilityRole **ROLE_TABLE** = `21`

Table element.

AccessibilityRole **ROLE_CELL** = `22`

Table/tree cell element.

AccessibilityRole **ROLE_ROW** = `23`

Table/tree row element.

AccessibilityRole **ROLE_ROW_GROUP** = `24`

Table/tree row group element.

AccessibilityRole **ROLE_ROW_HEADER** = `25`

Table/tree row header element.

AccessibilityRole **ROLE_COLUMN_HEADER** = `26`

Table/tree column header element.

AccessibilityRole **ROLE_TREE** = `27`

Tree view element.

AccessibilityRole **ROLE_TREE_ITEM** = `28`

Tree view item element.

AccessibilityRole **ROLE_LIST** = `29`

List element.

AccessibilityRole **ROLE_LIST_ITEM** = `30`

List item element.

AccessibilityRole **ROLE_LIST_BOX** = `31`

List view element.

AccessibilityRole **ROLE_LIST_BOX_OPTION** = `32`

List view item element.

AccessibilityRole **ROLE_TAB_BAR** = `33`

Tab bar element.

AccessibilityRole **ROLE_TAB** = `34`

Tab bar item element.

AccessibilityRole **ROLE_TAB_PANEL** = `35`

Tab panel element.

AccessibilityRole **ROLE_MENU_BAR** = `36`

Menu bar element.

AccessibilityRole **ROLE_MENU** = `37`

Popup menu element.

AccessibilityRole **ROLE_MENU_ITEM** = `38`

Popup menu item element.

AccessibilityRole **ROLE_MENU_ITEM_CHECK_BOX** = `39`

Popup menu check button item element.

AccessibilityRole **ROLE_MENU_ITEM_RADIO** = `40`

Popup menu radio button item element.

AccessibilityRole **ROLE_IMAGE** = `41`

Image element.

AccessibilityRole **ROLE_WINDOW** = `42`

Window element.

AccessibilityRole **ROLE_TITLE_BAR** = `43`

Embedded window title bar element.

AccessibilityRole **ROLE_DIALOG** = `44`

Dialog window element.

AccessibilityRole **ROLE_TOOLTIP** = `45`

Tooltip element.

AccessibilityRole **ROLE_REGION** = `46`

Region/landmark element. Screen readers can navigate between regions using landmark navigation.

AccessibilityRole **ROLE_TEXT_RUN** = `47`

Unifor text run.

Note: This role is used for internal text elements, and should not be assigned to nodes.

---

enum **AccessibilityPopupType**:

AccessibilityPopupType **POPUP_MENU** = `0`

Popup menu.

AccessibilityPopupType **POPUP_LIST** = `1`

Popup list.

AccessibilityPopupType **POPUP_TREE** = `2`

Popup tree view.

AccessibilityPopupType **POPUP_DIALOG** = `3`

Popup dialog.

---

enum **AccessibilityFlags**:

AccessibilityFlags **FLAG_HIDDEN** = `0`

Element is hidden for accessibility tools.

AccessibilityFlags **FLAG_MULTISELECTABLE** = `1`

Element supports multiple item selection.

AccessibilityFlags **FLAG_REQUIRED** = `2`

Element require user input.

AccessibilityFlags **FLAG_VISITED** = `3`

Element is a visited link.

AccessibilityFlags **FLAG_BUSY** = `4`

Element content is not ready (e.g. loading).

AccessibilityFlags **FLAG_MODAL** = `5`

Element is modal window.

AccessibilityFlags **FLAG_TOUCH_PASSTHROUGH** = `6`

Element allows touches to be passed through when a screen reader is in touch exploration mode.

AccessibilityFlags **FLAG_READONLY** = `7`

Element is text field with selectable but read-only text.

AccessibilityFlags **FLAG_DISABLED** = `8`

Element is disabled.

AccessibilityFlags **FLAG_CLIPS_CHILDREN** = `9`

Element clips children.

---

enum **AccessibilityAction**:

AccessibilityAction **ACTION_CLICK** = `0`

Single click action, callback argument is not set.

AccessibilityAction **ACTION_FOCUS** = `1`

Focus action, callback argument is not set.

AccessibilityAction **ACTION_BLUR** = `2`

Blur action, callback argument is not set.

AccessibilityAction **ACTION_COLLAPSE** = `3`

Collapse action, callback argument is not set.

AccessibilityAction **ACTION_EXPAND** = `4`

Expand action, callback argument is not set.

AccessibilityAction **ACTION_DECREMENT** = `5`

Decrement action, callback argument is not set.

AccessibilityAction **ACTION_INCREMENT** = `6`

Increment action, callback argument is not set.

AccessibilityAction **ACTION_HIDE_TOOLTIP** = `7`

Hide tooltip action, callback argument is not set.

AccessibilityAction **ACTION_SHOW_TOOLTIP** = `8`

Show tooltip action, callback argument is not set.

AccessibilityAction **ACTION_SET_TEXT_SELECTION** = `9`

Set text selection action, callback argument is set to [Dictionary](class_dictionary.md#class-dictionary) with the following keys:

- `"start_element"` accessibility element of the selection start.
- `"start_char"` character offset relative to the accessibility element of the selection start.
- `"end_element"` accessibility element of the selection end.
- `"end_char"` character offset relative to the accessibility element of the selection end.

AccessibilityAction **ACTION_REPLACE_SELECTED_TEXT** = `10`

Replace text action, callback argument is set to [String](class_string.md#class-string) with the replacement text.

AccessibilityAction **ACTION_SCROLL_BACKWARD** = `11`

Scroll backward action, callback argument is not set.

AccessibilityAction **ACTION_SCROLL_DOWN** = `12`

Scroll down action, callback argument is set to AccessibilityScrollUnit.

AccessibilityAction **ACTION_SCROLL_FORWARD** = `13`

Scroll forward action, callback argument is not set.

AccessibilityAction **ACTION_SCROLL_LEFT** = `14`

Scroll left action, callback argument is set to AccessibilityScrollUnit.

AccessibilityAction **ACTION_SCROLL_RIGHT** = `15`

Scroll right action, callback argument is set to AccessibilityScrollUnit.

AccessibilityAction **ACTION_SCROLL_UP** = `16`

Scroll up action, callback argument is set to AccessibilityScrollUnit.

AccessibilityAction **ACTION_SCROLL_INTO_VIEW** = `17`

Scroll into view action, callback argument is set to AccessibilityScrollHint.

AccessibilityAction **ACTION_SCROLL_TO_POINT** = `18`

Scroll to point action, callback argument is set to [Vector2](class_vector2.md#class-vector2) with the relative point coordinates.

AccessibilityAction **ACTION_SET_SCROLL_OFFSET** = `19`

Set scroll offset action, callback argument is set to [Vector2](class_vector2.md#class-vector2) with the scroll offset.

AccessibilityAction **ACTION_SET_VALUE** = `20`

Set value action, callback argument is set to [String](class_string.md#class-string) or number with the new value.

AccessibilityAction **ACTION_SHOW_CONTEXT_MENU** = `21`

Show context menu action, callback argument is not set.

AccessibilityAction **ACTION_CUSTOM** = `22`

Custom action, callback argument is set to the integer action ID.

---

enum **AccessibilityLiveMode**:

AccessibilityLiveMode **LIVE_OFF** = `0`

Indicates that updates to the live region should not be presented.

AccessibilityLiveMode **LIVE_POLITE** = `1`

Indicates that updates to the live region should be presented at the next opportunity (for example at the end of speaking the current sentence).

AccessibilityLiveMode **LIVE_ASSERTIVE** = `2`

Indicates that updates to the live region have the highest priority and should be presented immediately.

---

enum **AccessibilityScrollUnit**:

AccessibilityScrollUnit **SCROLL_UNIT_ITEM** = `0`

The amount by which to scroll. A single item of a list, line of text.

AccessibilityScrollUnit **SCROLL_UNIT_PAGE** = `1`

The amount by which to scroll. A single page.

---

enum **AccessibilityScrollHint**:

AccessibilityScrollHint **SCROLL_HINT_TOP_LEFT** = `0`

A preferred position for the node scrolled into view. Top-left edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_BOTTOM_RIGHT** = `1`

A preferred position for the node scrolled into view. Bottom-right edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_TOP_EDGE** = `2`

A preferred position for the node scrolled into view. Top edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_BOTTOM_EDGE** = `3`

A preferred position for the node scrolled into view. Bottom edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_LEFT_EDGE** = `4`

A preferred position for the node scrolled into view. Left edge of the scroll container.

AccessibilityScrollHint **SCROLL_HINT_RIGHT_EDGE** = `5`

A preferred position for the node scrolled into view. Right edge of the scroll container.

---

## Method Descriptions

[RID](class_rid.md#class-rid) **create_element**(window_id: [int](class_int.md#class-int), role: AccessibilityRole)

Creates a new, empty accessibility element resource.

**Note:** An accessibility element is created and freed automatically for each [Node](class_node.md#class-node). In general, this function should not be called manually.

---

[RID](class_rid.md#class-rid) **create_sub_element**(parent_rid: [RID](class_rid.md#class-rid), role: AccessibilityRole, insert_pos: [int](class_int.md#class-int) = -1)

Creates a new, empty accessibility sub-element resource. Sub-elements can be used to provide accessibility information for objects which are not [Node](class_node.md#class-node)s, such as list items, table cells, or menu items. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the free_element() method.

---

[RID](class_rid.md#class-rid) **create_sub_text_edit_elements**(parent_rid: [RID](class_rid.md#class-rid), shaped_text: [RID](class_rid.md#class-rid), min_height: [float](class_float.md#class-float), insert_pos: [int](class_int.md#class-int) = -1, is_last_line: [bool](class_bool.md#class-bool) = false)

Creates a new, empty accessibility sub-element from the shaped text buffer. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the free_element() method.

If `is_last_line` is `true`, no trailing newline is appended to the text content. Set to `true` for the last line in multi-line text fields and for single-line text fields.

---

[Variant](class_variant.md#class-variant) **element_get_meta**(id: [RID](class_rid.md#class-rid))

Returns the metadata of the accessibility element `id`.

---

 **element_set_meta**(id: [RID](class_rid.md#class-rid), meta: [Variant](class_variant.md#class-variant))

Sets the metadata of the accessibility element `id` to `meta`.

---

 **free_element**(id: [RID](class_rid.md#class-rid))

Frees the accessibility element `id` created by create_element(), create_sub_element(), or create_sub_text_edit_elements().

---

[RID](class_rid.md#class-rid) **get_window_root**(window_id: [int](class_int.md#class-int))

Returns the main accessibility element of the OS native window.

---

[bool](class_bool.md#class-bool) **has_element**(id: [RID](class_rid.md#class-rid))

Returns `true` if `id` is a valid accessibility element.

---

[bool](class_bool.md#class-bool) **is_supported**()

Returns `true` if screen reader is support by this implementation.

---

 **set_window_focused**(window_id: [int](class_int.md#class-int), focused: [bool](class_bool.md#class-bool))

Sets the window focused state for assistive apps.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Advanced users only! [Window](class_window.md#class-window) objects call this method automatically.

---

 **set_window_rect**(window_id: [int](class_int.md#class-int), rect_out: [Rect2](class_rect2.md#class-rect2), rect_in: [Rect2](class_rect2.md#class-rect2))

Sets window outer (with decorations) and inner (without decorations) bounds for assistive apps.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Advanced users only! [Window](class_window.md#class-window) objects call this method automatically.

---

 **update_add_action**(id: [RID](class_rid.md#class-rid), action: AccessibilityAction, callable: [Callable](class_callable.md#class-callable))

Adds a callback for the accessibility action (action which can be performed by using a special screen reader command or buttons on the Braille display), and marks this action as supported. The action callback receives one [Variant](class_variant.md#class-variant) argument, which value depends on action type.

---

 **update_add_child**(id: [RID](class_rid.md#class-rid), child_id: [RID](class_rid.md#class-rid))

Adds a child accessibility element.

**Note:** [Node](class_node.md#class-node) children and sub-elements are added to the child list automatically.

---

 **update_add_custom_action**(id: [RID](class_rid.md#class-rid), action_id: [int](class_int.md#class-int), action_description: [String](class_string.md#class-string))

Adds support for a custom accessibility action. `action_id` is passed as an argument to the callback of ACTION_CUSTOM action.

---

 **update_add_related_controls**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

Adds an element that is controlled by this element.

---

 **update_add_related_described_by**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

Adds an element that describes this element.

---

 **update_add_related_details**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

Adds an element that details this element.

---

 **update_add_related_flow_to**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

Adds an element that this element flow into.

---

 **update_add_related_labeled_by**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

Adds an element that labels this element.

---

 **update_add_related_radio_group**(id: [RID](class_rid.md#class-rid), related_id: [RID](class_rid.md#class-rid))

Adds an element that is part of the same radio group.

**Note:** This method should be called on each element of the group, using all other elements as `related_id`.

---

 **update_set_active_descendant**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

Adds an element that is an active descendant of this element.

---

 **update_set_background_color**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Sets element background color.

---

 **update_set_bounds**(id: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2))

Sets element bounding box, relative to the node position.

---

 **update_set_braille_label**(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))

Sets element accessibility label for Braille display.

---

 **update_set_braille_role_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))

Sets element accessibility role description for Braille display.

---

 **update_set_checked**(id: [RID](class_rid.md#class-rid), checekd: [bool](class_bool.md#class-bool))

Sets element checked state.

---

 **update_set_classname**(id: [RID](class_rid.md#class-rid), classname: [String](class_string.md#class-string))

Sets element class name.

---

 **update_set_color_value**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Sets element color value.

---

 **update_set_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))

Sets element accessibility description.

---

 **update_set_error_message**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

Sets an element which contains an error message for this element.

---

 **update_set_extra_info**(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))

Sets element accessibility extra information added to the element name.

---

 **update_set_flag**(id: [RID](class_rid.md#class-rid), flag: AccessibilityFlags, value: [bool](class_bool.md#class-bool))

Sets element flag.

---

 **update_set_focus**(id: [RID](class_rid.md#class-rid))

Sets currently focused element.

---

 **update_set_foreground_color**(id: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Sets element foreground color.

---

 **update_set_in_page_link_target**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

Sets target element for the link.

---

 **update_set_language**(id: [RID](class_rid.md#class-rid), language: [String](class_string.md#class-string))

Sets element text language.

---

 **update_set_list_item_count**(id: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int))

Sets number of items in the list.

---

 **update_set_list_item_expanded**(id: [RID](class_rid.md#class-rid), expanded: [bool](class_bool.md#class-bool))

Sets list/tree item expanded status.

---

 **update_set_list_item_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Sets the position of the element in the list.

---

 **update_set_list_item_level**(id: [RID](class_rid.md#class-rid), level: [int](class_int.md#class-int))

Sets the hierarchical level of the element in the list.

---

 **update_set_list_item_selected**(id: [RID](class_rid.md#class-rid), selected: [bool](class_bool.md#class-bool))

Sets list/tree item selected status.

---

 **update_set_list_orientation**(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool))

Sets the orientation of the list elements.

---

 **update_set_live**(id: [RID](class_rid.md#class-rid), live: AccessibilityLiveMode)

Sets the priority of the live region updates.

---

 **update_set_member_of**(id: [RID](class_rid.md#class-rid), group_id: [RID](class_rid.md#class-rid))

Sets the element to be a member of the group.

---

 **update_set_name**(id: [RID](class_rid.md#class-rid), name: [String](class_string.md#class-string))

Sets element accessibility name.

---

 **update_set_next_on_line**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

Sets next element on the line.

---

 **update_set_num_jump**(id: [RID](class_rid.md#class-rid), jump: [float](class_float.md#class-float))

Sets numeric value jump.

---

 **update_set_num_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))

Sets numeric value range.

---

 **update_set_num_step**(id: [RID](class_rid.md#class-rid), step: [float](class_float.md#class-float))

Sets numeric value step.

---

 **update_set_num_value**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))

Sets numeric value.

---

 **update_set_placeholder**(id: [RID](class_rid.md#class-rid), placeholder: [String](class_string.md#class-string))

Sets placeholder text.

---

 **update_set_popup_type**(id: [RID](class_rid.md#class-rid), popup: AccessibilityPopupType)

Sets popup type for popup buttons.

---

 **update_set_previous_on_line**(id: [RID](class_rid.md#class-rid), other_id: [RID](class_rid.md#class-rid))

Sets previous element on the line.

---

 **update_set_role**(id: [RID](class_rid.md#class-rid), role: AccessibilityRole)

Sets element accessibility role.

---

 **update_set_role_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))

Sets element accessibility role description text.

---

 **update_set_scroll_x**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))

Sets scroll bar x position.

---

 **update_set_scroll_x_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))

Sets scroll bar x range.

---

 **update_set_scroll_y**(id: [RID](class_rid.md#class-rid), position: [float](class_float.md#class-float))

Sets scroll bar y position.

---

 **update_set_scroll_y_range**(id: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float))

Sets scroll bar y range.

---

 **update_set_shortcut**(id: [RID](class_rid.md#class-rid), shortcut: [String](class_string.md#class-string))

Sets the list of keyboard shortcuts used by element.

---

 **update_set_state_description**(id: [RID](class_rid.md#class-rid), description: [String](class_string.md#class-string))

Sets human-readable description of the current checked state.

---

 **update_set_table_cell_position**(id: [RID](class_rid.md#class-rid), row_index: [int](class_int.md#class-int), column_index: [int](class_int.md#class-int))

Sets cell position in the table.

---

 **update_set_table_cell_span**(id: [RID](class_rid.md#class-rid), row_span: [int](class_int.md#class-int), column_span: [int](class_int.md#class-int))

Sets cell row/column span.

---

 **update_set_table_column_count**(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))

Sets number of columns in the table.

---

 **update_set_table_column_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Sets position of the column.

---

 **update_set_table_row_count**(id: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))

Sets number of rows in the table.

---

 **update_set_table_row_index**(id: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Sets position of the row in the table.

---

 **update_set_text_align**(id: [RID](class_rid.md#class-rid), align: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))

Sets element text alignment.

---

 **update_set_text_decorations**(id: [RID](class_rid.md#class-rid), underline: [bool](class_bool.md#class-bool), strikethrough: [bool](class_bool.md#class-bool), overline: [bool](class_bool.md#class-bool), color: [Color](class_color.md#class-color) = Color(0, 0, 0, 1))

Sets text underline/overline/strikethrough.

---

 **update_set_text_orientation**(id: [RID](class_rid.md#class-rid), vertical: [bool](class_bool.md#class-bool))

Sets text orientation.

---

 **update_set_text_selection**(id: [RID](class_rid.md#class-rid), text_start_id: [RID](class_rid.md#class-rid), start_char: [int](class_int.md#class-int), text_end_id: [RID](class_rid.md#class-rid), end_char: [int](class_int.md#class-int))

Sets text selection to the text field. `text_start_id` and `text_end_id` should be elements created by create_sub_text_edit_elements(). Character offsets are relative to the corresponding element.

---

 **update_set_tooltip**(id: [RID](class_rid.md#class-rid), tooltip: [String](class_string.md#class-string))

Sets tooltip text.

---

 **update_set_transform**(id: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets element 2D transform.

---

 **update_set_url**(id: [RID](class_rid.md#class-rid), url: [String](class_string.md#class-string))

Sets link URL.

---

 **update_set_value**(id: [RID](class_rid.md#class-rid), value: [String](class_string.md#class-string))

Sets element text value.
