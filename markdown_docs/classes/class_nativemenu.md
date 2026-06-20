# NativeMenu

**Inherits:** [Object](class_object.md#class-object)

A server interface for OS native menus.

## Description

**NativeMenu** handles low-level access to the OS native global menu bar and popup menus.

**Note:** This is low-level API, consider using [MenuBar](class_menubar.md#class-menubar) with [MenuBar.prefer_global_menu](class_menubar.md#class-menubar-property-prefer-global-menu) set to `true`, and [PopupMenu](class_popupmenu.md#class-popupmenu) with [PopupMenu.prefer_native_menu](class_popupmenu.md#class-popupmenu-property-prefer-native-menu) set to `true`.

To create a menu, use create_menu(), add menu items using `add_*_item` methods. To remove a menu, use free_menu().

```gdscript
var menu

func _menu_callback(item_id):
    if item_id == "ITEM_CUT":
        cut()
    elif item_id == "ITEM_COPY":
        copy()
    elif item_id == "ITEM_PASTE":
        paste()

func _enter_tree():
    # Create new menu and add items:
    menu = NativeMenu.create_menu()
    NativeMenu.add_item(menu, "Cut", _menu_callback, Callable(), "ITEM_CUT")
    NativeMenu.add_item(menu, "Copy", _menu_callback, Callable(), "ITEM_COPY")
    NativeMenu.add_separator(menu)
    NativeMenu.add_item(menu, "Paste", _menu_callback, Callable(), "ITEM_PASTE")

func _on_button_pressed():
    # Show popup menu at mouse position:
    NativeMenu.popup(menu, DisplayServer.mouse_get_position())

func _exit_tree():
    # Remove menu when it's no longer needed:
    NativeMenu.free_menu(menu)
```

## Methods

| [int](class_int.md#class-int)                     | add_check_item(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                    |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                     | add_icon_check_item(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                   |
| [int](class_int.md#class-int)                     | add_icon_item(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                               |
| [int](class_int.md#class-int)                     | add_icon_radio_check_item(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                       |
| [int](class_int.md#class-int)                     | add_item(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                                                |
| [int](class_int.md#class-int)                     | add_multistate_item(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1) |
| [int](class_int.md#class-int)                     | add_radio_check_item(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)                                                                                        |
| [int](class_int.md#class-int)                     | add_separator(rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                     | add_submenu_item(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), submenu_rid: [RID](class_rid.md#class-rid), tag: [Variant](class_variant.md#class-variant) = null, index: [int](class_int.md#class-int) = -1)                                                                                                                                                                                                                                                                      |
|                                                   | clear(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                     | create_menu()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                     | find_item_index_with_submenu(rid: [RID](class_rid.md#class-rid), submenu_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                     | find_item_index_with_tag(rid: [RID](class_rid.md#class-rid), tag: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                     | find_item_index_with_text(rid: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                   | free_menu(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Key](class_@globalscope.md#enum-globalscope-key) | get_item_accelerator(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Callable](class_callable.md#class-callable)      | get_item_callback(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                     | get_item_count(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Texture2D](class_texture2d.md#class-texture2d)   | get_item_icon(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                     | get_item_indentation_level(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Callable](class_callable.md#class-callable)      | get_item_key_callback(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                     | get_item_max_states(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                     | get_item_state(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                     | get_item_submenu(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Variant](class_variant.md#class-variant)         | get_item_tag(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)            | get_item_text(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)            | get_item_tooltip(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)               | get_minimum_width(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Callable](class_callable.md#class-callable)      | get_popup_close_callback(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Callable](class_callable.md#class-callable)      | get_popup_open_callback(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Vector2](class_vector2.md#class-vector2)         | get_size(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                     | get_system_menu(menu_id: SystemMenus)                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [String](class_string.md#class-string)            | get_system_menu_name(menu_id: SystemMenus)                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [String](class_string.md#class-string)            | get_system_menu_text(menu_id: SystemMenus)                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                  | has_feature(feature: Feature)                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                  | has_menu(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                  | has_system_menu(menu_id: SystemMenus)                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                  | is_item_checkable(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                  | is_item_checked(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                  | is_item_disabled(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                  | is_item_hidden(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                  | is_item_radio_checkable(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                  | is_opened(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                  | is_system_menu(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                   | popup(rid: [RID](class_rid.md#class-rid), position: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                   | remove_item(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                   | set_interface_direction(rid: [RID](class_rid.md#class-rid), is_rtl: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                   | set_item_accelerator(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), keycode: [Key](class_@globalscope.md#enum-globalscope-key))                                                                                                                                                                                                                                                                                                                                                           |
|                                                   | set_item_callback(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   | set_item_checkable(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                              |
|                                                   | set_item_checked(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                   | set_item_disabled(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                   | set_item_hidden(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                   | set_item_hover_callbacks(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                       |
|                                                   | set_item_icon(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))                                                                                                                                                                                                                                                                                                                                                                              |
|                                                   | set_item_indentation_level(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), level: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                     | set_item_index(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), target_idx: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                   | set_item_key_callback(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), key_callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                         |
|                                                   | set_item_max_states(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                              |
|                                                   | set_item_radio_checkable(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                  |
|                                                   | set_item_state(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), state: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                   | set_item_submenu(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), submenu_rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                   | set_item_tag(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), tag: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                   | set_item_text(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                   | set_item_tooltip(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                              |
|                                                   | set_minimum_width(rid: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   | set_popup_close_callback(rid: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                   | set_popup_open_callback(rid: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                   | set_system_menu_text(menu_id: SystemMenus, name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                           |

---

## Enumerations

enum **Feature**:

Feature **FEATURE_GLOBAL_MENU** = `0`

**NativeMenu** supports native global main menu.

Feature **FEATURE_POPUP_MENU** = `1`

**NativeMenu** supports native popup menus.

Feature **FEATURE_OPEN_CLOSE_CALLBACK** = `2`

**NativeMenu** supports menu open and close callbacks.

Feature **FEATURE_HOVER_CALLBACK** = `3`

**NativeMenu** supports menu item hover callback.

Feature **FEATURE_KEY_CALLBACK** = `4`

**NativeMenu** supports menu item accelerator/key callback.

---

enum **SystemMenus**:

SystemMenus **INVALID_MENU_ID** = `0`

Invalid special system menu ID.

SystemMenus **MAIN_MENU_ID** = `1`

Global main menu ID.

SystemMenus **APPLICATION_MENU_ID** = `2`

Application (first menu after "Apple" menu on macOS) menu ID.

SystemMenus **WINDOW_MENU_ID** = `3`

"Window" menu ID (on macOS this menu includes standard window control items and a list of open windows).

SystemMenus **HELP_MENU_ID** = `4`

"Help" menu ID (on macOS this menu includes help search bar).

SystemMenus **DOCK_MENU_ID** = `5`

Dock icon right-click menu ID (on macOS this menu include standard application control items and a list of open windows).

---

## Method Descriptions

[int](class_int.md#class-int) **add_check_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

Adds a new checkable item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---

[int](class_int.md#class-int) **add_icon_check_item**(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

Adds a new checkable item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---

[int](class_int.md#class-int) **add_icon_item**(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

Adds a new item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---

[int](class_int.md#class-int) **add_icon_radio_check_item**(rid: [RID](class_rid.md#class-rid), icon: [Texture2D](class_texture2d.md#class-texture2d), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

Adds a new radio-checkable item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See set_item_checked() for more info on how to control it.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---

[int](class_int.md#class-int) **add_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

Adds a new item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---

[int](class_int.md#class-int) **add_multistate_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), max_states: [int](class_int.md#class-int), default_state: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

Adds a new item with text `label` to the global menu `rid`.

Contrarily to normal binary items, multistate items can have more than two states, as defined by `max_states`. Each press or activate of the item will increase the state by one. The default value is defined by `default_state`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** By default, there's no indication of the current item state, it should be changed manually.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---

[int](class_int.md#class-int) **add_radio_check_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), callback: [Callable](class_callable.md#class-callable) = Callable(), key_callback: [Callable](class_callable.md#class-callable) = Callable(), tag: [Variant](class_variant.md#class-variant) = null, accelerator: [Key](class_@globalscope.md#enum-globalscope-key) = 0, index: [int](class_int.md#class-int) = -1)

Adds a new radio-checkable item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See set_item_checked() for more info on how to control it.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

---

[int](class_int.md#class-int) **add_separator**(rid: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int) = -1)

Adds a separator between items to the global menu `rid`. Separators also occupy an index.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

**Note:** This method is implemented on macOS and Windows.

---

[int](class_int.md#class-int) **add_submenu_item**(rid: [RID](class_rid.md#class-rid), label: [String](class_string.md#class-string), submenu_rid: [RID](class_rid.md#class-rid), tag: [Variant](class_variant.md#class-variant) = null, index: [int](class_int.md#class-int) = -1)

Adds an item that will act as a submenu of the global menu `rid`. The `submenu_rid` argument is the RID of the global menu that will be shown when the item is clicked.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

**Note:** This method is implemented on macOS and Windows.

---

 **clear**(rid: [RID](class_rid.md#class-rid))

Removes all items from the global menu `rid`.

**Note:** This method is implemented on macOS and Windows.

---

[RID](class_rid.md#class-rid) **create_menu**()

Creates a new global menu object.

**Note:** This method is implemented on macOS and Windows.

---

[int](class_int.md#class-int) **find_item_index_with_submenu**(rid: [RID](class_rid.md#class-rid), submenu_rid: [RID](class_rid.md#class-rid))

Returns the index of the item with the submenu specified by `submenu_rid`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

---

[int](class_int.md#class-int) **find_item_index_with_tag**(rid: [RID](class_rid.md#class-rid), tag: [Variant](class_variant.md#class-variant))

Returns the index of the item with the specified `tag`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

---

[int](class_int.md#class-int) **find_item_index_with_text**(rid: [RID](class_rid.md#class-rid), text: [String](class_string.md#class-string))

Returns the index of the item with the specified `text`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

---

 **free_menu**(rid: [RID](class_rid.md#class-rid))

Frees a global menu object created by this **NativeMenu**.

**Note:** This method is implemented on macOS and Windows.

---

[Key](class_@globalscope.md#enum-globalscope-key) **get_item_accelerator**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the accelerator of the item at index `idx`. Accelerators are special combinations of keys that activate the item, no matter which control is focused.

**Note:** This method is implemented only on macOS.

---

[Callable](class_callable.md#class-callable) **get_item_callback**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the callback of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---

[int](class_int.md#class-int) **get_item_count**(rid: [RID](class_rid.md#class-rid))

Returns number of items in the global menu `rid`.

**Note:** This method is implemented on macOS and Windows.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_item_icon**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the icon of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---

[int](class_int.md#class-int) **get_item_indentation_level**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the horizontal offset of the item at the given `idx`.

**Note:** This method is implemented only on macOS.

---

[Callable](class_callable.md#class-callable) **get_item_key_callback**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the callback of the item accelerator at index `idx`.

**Note:** This method is implemented only on macOS.

---

[int](class_int.md#class-int) **get_item_max_states**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns number of states of a multistate item. See add_multistate_item() for details.

**Note:** This method is implemented on macOS and Windows.

---

[int](class_int.md#class-int) **get_item_state**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the state of a multistate item. See add_multistate_item() for details.

**Note:** This method is implemented on macOS and Windows.

---

[RID](class_rid.md#class-rid) **get_item_submenu**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the submenu ID of the item at index `idx`. See add_submenu_item() for more info on how to add a submenu.

**Note:** This method is implemented on macOS and Windows.

---

[Variant](class_variant.md#class-variant) **get_item_tag**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the metadata of the specified item, which might be of any type. You can set it with set_item_tag(), which provides a simple way of assigning context data to items.

**Note:** This method is implemented on macOS and Windows.

---

[String](class_string.md#class-string) **get_item_text**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the text of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---

[String](class_string.md#class-string) **get_item_tooltip**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns the tooltip associated with the specified index `idx`.

**Note:** This method is implemented only on macOS.

---

[float](class_float.md#class-float) **get_minimum_width**(rid: [RID](class_rid.md#class-rid))

Returns global menu minimum width.

**Note:** This method is implemented only on macOS.

---

[Callable](class_callable.md#class-callable) **get_popup_close_callback**(rid: [RID](class_rid.md#class-rid))

Returns global menu close callback.

**Note:** This method is implemented on macOS and Windows.

---

[Callable](class_callable.md#class-callable) **get_popup_open_callback**(rid: [RID](class_rid.md#class-rid))

Returns global menu open callback.

**Note:** This method is implemented only on macOS.

---

[Vector2](class_vector2.md#class-vector2) **get_size**(rid: [RID](class_rid.md#class-rid))

Returns global menu size.

**Note:** This method is implemented on macOS and Windows.

---

[RID](class_rid.md#class-rid) **get_system_menu**(menu_id: SystemMenus)

Returns RID of a special system menu.

**Note:** This method is implemented only on macOS.

---

[String](class_string.md#class-string) **get_system_menu_name**(menu_id: SystemMenus)

Returns readable name of a special system menu.

**Note:** This method is implemented only on macOS.

---

[String](class_string.md#class-string) **get_system_menu_text**(menu_id: SystemMenus)

Returns the text of the system menu item.

**Note:** This method is implemented on macOS.

---

[bool](class_bool.md#class-bool) **has_feature**(feature: Feature)

Returns `true` if the specified `feature` is supported by the current **NativeMenu**, `false` otherwise.

**Note:** This method is implemented on macOS and Windows.

---

[bool](class_bool.md#class-bool) **has_menu**(rid: [RID](class_rid.md#class-rid))

Returns `true` if `rid` is valid global menu.

**Note:** This method is implemented on macOS and Windows.

---

[bool](class_bool.md#class-bool) **has_system_menu**(menu_id: SystemMenus)

Returns `true` if a special system menu is supported.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **is_item_checkable**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns `true` if the item at index `idx` is checkable in some way, i.e. if it has a checkbox or radio button.

**Note:** This method is implemented on macOS and Windows.

---

[bool](class_bool.md#class-bool) **is_item_checked**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns `true` if the item at index `idx` is checked.

**Note:** This method is implemented on macOS and Windows.

---

[bool](class_bool.md#class-bool) **is_item_disabled**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns `true` if the item at index `idx` is disabled. When it is disabled it can't be selected, or its action invoked.

See set_item_disabled() for more info on how to disable an item.

**Note:** This method is implemented on macOS and Windows.

---

[bool](class_bool.md#class-bool) **is_item_hidden**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns `true` if the item at index `idx` is hidden.

See set_item_hidden() for more info on how to hide an item.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **is_item_radio_checkable**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Returns `true` if the item at index `idx` has radio button-style checkability.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

**Note:** This method is implemented on macOS and Windows.

---

[bool](class_bool.md#class-bool) **is_opened**(rid: [RID](class_rid.md#class-rid))

Returns `true` if the menu is currently opened.

**Note:** This method is implemented only on macOS.

---

[bool](class_bool.md#class-bool) **is_system_menu**(rid: [RID](class_rid.md#class-rid))

Return `true` is global menu is a special system menu.

**Note:** This method is implemented only on macOS.

---

 **popup**(rid: [RID](class_rid.md#class-rid), position: [Vector2i](class_vector2i.md#class-vector2i))

Shows the global menu at `position` in the screen coordinates.

**Note:** This method is implemented on macOS and Windows.

---

 **remove_item**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int))

Removes the item at index `idx` from the global menu `rid`.

**Note:** The indices of items after the removed item will be shifted by one.

**Note:** This method is implemented on macOS and Windows.

---

 **set_interface_direction**(rid: [RID](class_rid.md#class-rid), is_rtl: [bool](class_bool.md#class-bool))

Sets the menu text layout direction from right-to-left if `is_rtl` is `true`.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_accelerator**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), keycode: [Key](class_@globalscope.md#enum-globalscope-key))

Sets the accelerator of the item at index `idx`. `keycode` can be a single [Key](class_@globalscope.md#enum-globalscope-key), or a combination of [KeyModifierMask](class_@globalscope.md#enum-globalscope-keymodifiermask)s and [Key](class_@globalscope.md#enum-globalscope-key)s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** This method is implemented only on macOS.

---

 **set_item_callback**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))

Sets the callback of the item at index `idx`. Callback is emitted when an item is pressed.

**Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_checkable**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool))

Sets whether the item at index `idx` has a checkbox. If `false`, sets the type of the item to plain text.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_checked**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checked: [bool](class_bool.md#class-bool))

Sets the checkstate status of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_disabled**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), disabled: [bool](class_bool.md#class-bool))

Enables/disables the item at index `idx`. When it is disabled, it can't be selected and its action can't be invoked.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_hidden**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), hidden: [bool](class_bool.md#class-bool))

Hides/shows the item at index `idx`. When it is hidden, an item does not appear in a menu and its action cannot be invoked.

**Note:** This method is implemented only on macOS.

---

 **set_item_hover_callbacks**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), callback: [Callable](class_callable.md#class-callable))

Sets the callback of the item at index `idx`. The callback is emitted when an item is hovered.

**Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

---

 **set_item_icon**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), icon: [Texture2D](class_texture2d.md#class-texture2d))

Replaces the [Texture2D](class_texture2d.md#class-texture2d) icon of the specified `idx`.

**Note:** This method is implemented on macOS and Windows.

**Note:** This method is not supported by macOS Dock menu items.

---

 **set_item_indentation_level**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), level: [int](class_int.md#class-int))

Sets the horizontal offset of the item at the given `idx`.

**Note:** This method is implemented only on macOS.

---

[int](class_int.md#class-int) **set_item_index**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), target_idx: [int](class_int.md#class-int))

Changes the index of the item at index `idx` to be at index `target_idx`. This can be used to move an item above other items.

Returns the new index of the moved item, it's not guaranteed to be the same as `target_idx`.

**Note:** The indices of any items between index `idx` and index `target_idx` will be shifted by one.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_key_callback**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), key_callback: [Callable](class_callable.md#class-callable))

Sets the callback of the item at index `idx`. Callback is emitted when its accelerator is activated.

**Note:** The `key_callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

---

 **set_item_max_states**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), max_states: [int](class_int.md#class-int))

Sets number of state of a multistate item. See add_multistate_item() for details.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_radio_checkable**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), checkable: [bool](class_bool.md#class-bool))

Sets the type of the item at the specified index `idx` to radio button. If `false`, sets the type of the item to plain text.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_state**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), state: [int](class_int.md#class-int))

Sets the state of a multistate item. See add_multistate_item() for details.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_submenu**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), submenu_rid: [RID](class_rid.md#class-rid))

Sets the submenu RID of the item at index `idx`. The submenu is a global menu that would be shown when the item is clicked.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_tag**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), tag: [Variant](class_variant.md#class-variant))

Sets the metadata of an item, which may be of any type. You can later get it with get_item_tag(), which provides a simple way of assigning context data to items.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_text**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), text: [String](class_string.md#class-string))

Sets the text of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

---

 **set_item_tooltip**(rid: [RID](class_rid.md#class-rid), idx: [int](class_int.md#class-int), tooltip: [String](class_string.md#class-string))

Sets the [String](class_string.md#class-string) tooltip of the item at the specified index `idx`.

**Note:** This method is implemented only on macOS.

---

 **set_minimum_width**(rid: [RID](class_rid.md#class-rid), width: [float](class_float.md#class-float))

Sets the minimum width of the global menu.

**Note:** This method is implemented only on macOS.

---

 **set_popup_close_callback**(rid: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))

Registers callable to emit when the menu is about to show.

**Note:** The OS can simulate menu opening to track menu item changes and global shortcuts, in which case the corresponding close callback is not triggered. Use is_opened() to check if the menu is currently opened.

**Note:** This method is implemented on macOS and Windows.

---

 **set_popup_open_callback**(rid: [RID](class_rid.md#class-rid), callback: [Callable](class_callable.md#class-callable))

Registers callable to emit after the menu is closed.

**Note:** This method is implemented only on macOS.

---

 **set_system_menu_text**(menu_id: SystemMenus, name: [String](class_string.md#class-string))

Sets the text of the system menu item.

**Note:** This method is implemented on macOS.
