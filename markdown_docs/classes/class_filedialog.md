# FileDialog

**Inherits:** [ConfirmationDialog](class_confirmationdialog.md#class-confirmationdialog) **<** [AcceptDialog](class_acceptdialog.md#class-acceptdialog) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [EditorFileDialog](class_editorfiledialog.md#class-editorfiledialog)

A dialog for selecting files or directories in the filesystem.

## Description

**FileDialog** is a preset dialog used to choose files and directories in the filesystem. It supports filter masks. **FileDialog** automatically sets its window title according to the file_mode. If you want to use a custom title, disable this by setting mode_overrides_title to `false`.

**Note:** **FileDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class-window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class-window-method-popup-centered-clamped).

## Properties

| Access                                       | access                                           | `0`                                                                                                     |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)                                  | current_dir                                 |                                                                                                         |
| [String](class_string.md#class-string)                                  | current_file                               |                                                                                                         |
| [String](class_string.md#class-string)                                  | current_path                               |                                                                                                         |
| [bool](class_bool.md#class-bool)                                        | deleting_enabled                       | `true`                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | dialog_hide_on_ok                                                                     | `false` (overrides [AcceptDialog](class_acceptdialog.md#class-acceptdialog-property-dialog-hide-on-ok)) |
| DisplayMode                             | display_mode                               | `0`                                                                                                     |
| [bool](class_bool.md#class-bool)                                        | favorites_enabled                     | `true`                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | file_filter_toggle_enabled   | `true`                                                                                                  |
| FileMode                                   | file_mode                                     | `4`                                                                                                     |
| [bool](class_bool.md#class-bool)                                        | file_sort_options_enabled     | `true`                                                                                                  |
| [String](class_string.md#class-string)                                  | filename_filter                         | `""`                                                                                                    |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | filters                                         | `PackedStringArray()`                                                                                   |
| [bool](class_bool.md#class-bool)                                        | folder_creation_enabled         | `true`                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | hidden_files_toggle_enabled | `true`                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | layout_toggle_enabled             | `true`                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | mode_overrides_title               | `true`                                                                                                  |
| [int](class_int.md#class-int)                                           | option_count                               | `0`                                                                                                     |
| [int](class_int.md#class-int)                                           | option_{index}/default             | `0`                                                                                                     |
| [String](class_string.md#class-string)                                  | option_{index}/name                   | `""`                                                                                                    |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | option_{index}/values               | `PackedStringArray()`                                                                                   |
| [bool](class_bool.md#class-bool)                                        | overwrite_warning_enabled     | `true`                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | recent_list_enabled                 | `true`                                                                                                  |
| [String](class_string.md#class-string)                                  | root_subfolder                           | `""`                                                                                                    |
| [bool](class_bool.md#class-bool)                                        | show_hidden_files                     | `false`                                                                                                 |
| [Vector2i](class_vector2i.md#class-vector2i)                            | size                                                                                  | `Vector2i(640, 360)` (overrides [Window](class_window.md#class-window-property-size))                   |
| [String](class_string.md#class-string)                                  | title                                                                                 | `"Save a File"` (overrides [Window](class_window.md#class-window-property-title))                       |
| [bool](class_bool.md#class-bool)                                        | use_native_dialog                     | `false`                                                                                                 |

## Methods

|                                                                         | add_filter(filter: [String](class_string.md#class-string), description: [String](class_string.md#class-string) = "", mime_type: [String](class_string.md#class-string) = "")                  |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                         | add_option(name: [String](class_string.md#class-string), values: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), default_value_index: [int](class_int.md#class-int)) |
|                                                                         | clear_filename_filter()                                                                                                                                                            |
|                                                                         | clear_filters()                                                                                                                                                                            |
|                                                                         | deselect_all()                                                                                                                                                                              |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_favorite_list()                                                                                                                                                                    |
| [LineEdit](class_lineedit.md#class-lineedit)                            | get_line_edit()                                                                                                                                                                            |
| [int](class_int.md#class-int)                                           | get_option_default(option: [int](class_int.md#class-int))                                                                                                                             |
| [String](class_string.md#class-string)                                  | get_option_name(option: [int](class_int.md#class-int))                                                                                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_option_values(option: [int](class_int.md#class-int))                                                                                                                               |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_recent_list()                                                                                                                                                                        |
| [Dictionary](class_dictionary.md#class-dictionary)                      | get_selected_options()                                                                                                                                                              |
| [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer)             | get_vbox()                                                                                                                                                                                      |
|                                                                         | invalidate()                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                        | is_customization_flag_enabled(flag: Customization)                                                                                       |
|                                                                         | popup_file_dialog()                                                                                                                                                                    |
|                                                                         | set_customization_flag_enabled(flag: Customization, enabled: [bool](class_bool.md#class-bool))                                          |
|                                                                         | set_favorite_list(favorites: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                                                                  |
|                                                                         | set_get_icon_callback(callback: [Callable](class_callable.md#class-callable))                                                                                                      |
|                                                                         | set_get_thumbnail_callback(callback: [Callable](class_callable.md#class-callable))                                                                                            |
|                                                                         | set_option_default(option: [int](class_int.md#class-int), default_value_index: [int](class_int.md#class-int))                                                                         |
|                                                                         | set_option_name(option: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                                     |
|                                                                         | set_option_values(option: [int](class_int.md#class-int), values: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                              |
|                                                                         | set_recent_list(recents: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                                                                        |

## Theme Properties

| [Color](class_color.md#class-color)             | file_disabled_color            | `Color(1, 1, 1, 0.25)`   |
|-------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------|
| [Color](class_color.md#class-color)             | file_icon_color                    | `Color(1, 1, 1, 1)`      |
| [Color](class_color.md#class-color)             | folder_icon_color                | `Color(1, 1, 1, 1)`      |
| [int](class_int.md#class-int)                   | thumbnail_size                   | `64`                     |
| [Texture2D](class_texture2d.md#class-texture2d) | back_folder                             |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | create_folder                         |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | favorite                                   |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | favorite_down                         |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | favorite_up                             |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | file                                           |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | file_thumbnail                       |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | folder                                       |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | folder_thumbnail                   |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | forward_folder                       |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | list_mode                                 |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | menu_copy_path                       |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | menu_delete                             |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | menu_new_folder                     |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | menu_open_bundle                   |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | menu_refresh                           |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | menu_show_in_file_manager |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | parent_folder                         |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | reload                                       |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | sort                                           |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | thumbnail_mode                       |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | toggle_filename_filter       |                          |
| [Texture2D](class_texture2d.md#class-texture2d) | toggle_hidden                         |                          |

---

## Signals

**dir_selected**(dir: [String](class_string.md#class-string))

Emitted when the user selects a directory.

---

**file_selected**(path: [String](class_string.md#class-string))

Emitted when the user selects a file by double-clicking it or pressing the **OK** button.

---

**filename_filter_changed**(filter: [String](class_string.md#class-string))

Emitted when the filter for file names changes.

---

**files_selected**(paths: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Emitted when the user selects multiple files.

---

## Enumerations

enum **FileMode**:

FileMode **FILE_MODE_OPEN_FILE** = `0`

The dialog allows selecting one, and only one file.

FileMode **FILE_MODE_OPEN_FILES** = `1`

The dialog allows selecting multiple files.

FileMode **FILE_MODE_OPEN_DIR** = `2`

The dialog only allows selecting a directory, disallowing the selection of any file.

FileMode **FILE_MODE_OPEN_ANY** = `3`

The dialog allows selecting one file or directory.

FileMode **FILE_MODE_SAVE_FILE** = `4`

The dialog will warn when a file exists.

---

enum **Access**:

Access **ACCESS_RESOURCES** = `0`

The dialog only allows accessing files under the [Resource](class_resource.md#class-resource) path (`res://`).

Access **ACCESS_USERDATA** = `1`

The dialog only allows accessing files under user data path (`user://`).

Access **ACCESS_FILESYSTEM** = `2`

The dialog allows accessing files on the whole file system.

---

enum **DisplayMode**:

DisplayMode **DISPLAY_THUMBNAILS** = `0`

The dialog displays files as a grid of thumbnails. Use thumbnail_size to adjust their size.

DisplayMode **DISPLAY_LIST** = `1`

The dialog displays files as a list of filenames.

---

enum **Customization**:

Customization **CUSTOMIZATION_HIDDEN_FILES** = `0`

Toggles visibility of the favorite button, and the favorite list on the left side of the dialog.

Equivalent to hidden_files_toggle_enabled.

Customization **CUSTOMIZATION_CREATE_FOLDER** = `1`

If enabled, shows the button for creating new directories (when using FILE_MODE_OPEN_DIR, FILE_MODE_OPEN_ANY, or FILE_MODE_SAVE_FILE).

Equivalent to folder_creation_enabled.

Customization **CUSTOMIZATION_FILE_FILTER** = `2`

If enabled, shows the toggle file filter button.

Equivalent to file_filter_toggle_enabled.

Customization **CUSTOMIZATION_FILE_SORT** = `3`

If enabled, shows the file sorting options button.

Equivalent to file_sort_options_enabled.

Customization **CUSTOMIZATION_FAVORITES** = `4`

If enabled, shows the toggle favorite button and favorite list on the left side of the dialog.

Equivalent to favorites_enabled.

Customization **CUSTOMIZATION_RECENT** = `5`

If enabled, shows the recent directories list on the left side of the dialog.

Equivalent to recent_list_enabled.

Customization **CUSTOMIZATION_LAYOUT** = `6`

If enabled, shows the layout switch buttons (list/thumbnails).

Equivalent to layout_toggle_enabled.

Customization **CUSTOMIZATION_OVERWRITE_WARNING** = `7`

If enabled, the **FileDialog** will warn the user before overwriting files in save mode.

Equivalent to overwrite_warning_enabled.

Customization **CUSTOMIZATION_DELETE** = `8`

If enabled, the context menu will show the "Delete" option, which allows moving files and folders to trash.

Equivalent to deleting_enabled.

---

## Property Descriptions

Access **access** = `0`

-  **set_access**(value: Access)
- Access **get_access**()

The file system access scope.

**Warning:** In Web builds, FileDialog cannot access the host file system. In sandboxed Linux and macOS environments, use_native_dialog is automatically used to allow limited access to host file system.

---

[String](class_string.md#class-string) **current_dir**

-  **set_current_dir**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_current_dir**()

The current working directory of the file dialog.

**Note:** For native file dialogs, this property is only treated as a hint and may not be respected by specific OS implementations.

---

[String](class_string.md#class-string) **current_file**

-  **set_current_file**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_current_file**()

The currently selected file of the file dialog.

---

[String](class_string.md#class-string) **current_path**

-  **set_current_path**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_current_path**()

The currently selected file path of the file dialog.

---

[bool](class_bool.md#class-bool) **deleting_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, the context menu will show the "Delete" option, which allows moving files and folders to trash.

---

DisplayMode **display_mode** = `0`

-  **set_display_mode**(value: DisplayMode)
- DisplayMode **get_display_mode**()

Display mode of the dialog's file list.

---

[bool](class_bool.md#class-bool) **favorites_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, shows the toggle favorite button and favorite list on the left side of the dialog.

---

[bool](class_bool.md#class-bool) **file_filter_toggle_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, shows the toggle file filter button.

---

FileMode **file_mode** = `4`

-  **set_file_mode**(value: FileMode)
- FileMode **get_file_mode**()

The dialog's open or save mode, which affects the selection behavior.

---

[bool](class_bool.md#class-bool) **file_sort_options_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, shows the file sorting options button.

---

[String](class_string.md#class-string) **filename_filter** = `""`

-  **set_filename_filter**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_filename_filter**()

The filter for file names (case-insensitive). When set to a non-empty string, only files that contains the substring will be shown. filename_filter can be edited by the user with the filter button at the top of the file dialog.

See also filters, which should be used to restrict the file types that can be selected instead of filename_filter which is meant to be set by the user.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **filters** = `PackedStringArray()`

-  **set_filters**(value: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))
- [PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_filters**()

The available file type filters. Each filter string in the array should be formatted like this: `*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of the filter is optional and can be omitted. Both file extensions and MIME type should be always set.

**Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

[bool](class_bool.md#class-bool) **folder_creation_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, shows the button for creating new directories (when using FILE_MODE_OPEN_DIR, FILE_MODE_OPEN_ANY, or FILE_MODE_SAVE_FILE), and the context menu will have the "New Folder..." option.

---

[bool](class_bool.md#class-bool) **hidden_files_toggle_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, shows the toggle hidden files button.

---

[bool](class_bool.md#class-bool) **layout_toggle_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, shows the layout switch buttons (list/thumbnails).

---

[bool](class_bool.md#class-bool) **mode_overrides_title** = `true`

-  **set_mode_overrides_title**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_mode_overriding_title**()

If `true`, changing the file_mode property will set the window title accordingly (e.g. setting file_mode to FILE_MODE_OPEN_FILE will change the window title to "Open a File").

---

[int](class_int.md#class-int) **option_count** = `0`

-  **set_option_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_option_count**()

The number of additional [OptionButton](class_optionbutton.md#class-optionbutton)s and [CheckBox](class_checkbox.md#class-checkbox)es in the dialog.

---

[int](class_int.md#class-int) **option_{index}/default** = `0`

The default value for the option at `index`.

**Note:** `index` is a value in the `0 .. option_count - 1` range.

---

[String](class_string.md#class-string) **option_{index}/name** = `""`

The name of the option at `index`.

**Note:** `index` is a value in the `0 .. option_count - 1` range.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **option_{index}/values** = `PackedStringArray()`

The list of values for the option at `index`.

**Note:** `index` is a value in the `0 .. option_count - 1` range.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class-packedstringarray) for more details.

---

[bool](class_bool.md#class-bool) **overwrite_warning_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, the **FileDialog** will warn the user before overwriting files in save mode.

---

[bool](class_bool.md#class-bool) **recent_list_enabled** = `true`

-  **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization) 

If `true`, shows the recent directories list on the left side of the dialog.

---

[String](class_string.md#class-string) **root_subfolder** = `""`

-  **set_root_subfolder**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_root_subfolder**()

If non-empty, the given sub-folder will be "root" of this **FileDialog**, i.e. user won't be able to go to its parent directory.

**Note:** This property is ignored by native file dialogs.

---

[bool](class_bool.md#class-bool) **show_hidden_files** = `false`

-  **set_show_hidden_files**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_showing_hidden_files**()

If `true`, the dialog will show hidden files.

**Note:** This property is ignored by native file dialogs on Android and Linux.

---

[bool](class_bool.md#class-bool) **use_native_dialog** = `false`

-  **set_use_native_dialog**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_native_dialog**()

If `true`, and if supported by the current [DisplayServer](class_displayserver.md#class-displayserver), OS native dialog will be used instead of custom one.

**Note:** On Android, it is only supported when using ACCESS_FILESYSTEM. For access mode ACCESS_RESOURCES and ACCESS_USERDATA, the system will fall back to custom FileDialog.

**Note:** On Linux and macOS, sandboxed apps always use native dialogs to access the host file system.

**Note:** On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. Use [OS.get_granted_permissions()](class_os.md#class-os-method-get-granted-permissions) to get a list of saved bookmarks.

**Note:** Native dialogs are isolated from the base process, file dialog properties can't be modified once the dialog is shown.

**Note:** This property is ignored in [EditorFileDialog](class_editorfiledialog.md#class-editorfiledialog).

---

## Method Descriptions

 **add_filter**(filter: [String](class_string.md#class-string), description: [String](class_string.md#class-string) = "", mime_type: [String](class_string.md#class-string) = "")

Adds a comma-separated file extension `filter` and comma-separated MIME type `mime_type` option to the **FileDialog** with an optional `description`, which restricts what files can be picked.

A `filter` should be of the form `"filename.extension"`, where filename and extension can be `*` to match any string. Filters starting with `.` (i.e. empty filenames) are not allowed.

For example, a `filter` of `"*.png, *.jpg"`, a `mime_type` of `image/png, image/jpeg`, and a `description` of `"Images"` results in filter text "Images (\*.png, \*.jpg)".

**Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

---

 **add_option**(name: [String](class_string.md#class-string), values: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), default_value_index: [int](class_int.md#class-int))

Adds an additional [OptionButton](class_optionbutton.md#class-optionbutton) to the file dialog. If `values` is empty, a [CheckBox](class_checkbox.md#class-checkbox) is added instead.

`default_value_index` should be an index of the value in the `values`. If `values` is empty it should be either `1` (checked), or `0` (unchecked).

---

 **clear_filename_filter**()

Clear the filter for file names.

---

 **clear_filters**()

Clear all the added filters in the dialog.

---

 **deselect_all**()

Clear all currently selected items in the dialog.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_favorite_list**()

Returns the list of favorite directories, which is shared by all **FileDialog** nodes. Useful to store the list of favorites between project sessions. This method can be called only from the main thread.

---

[LineEdit](class_lineedit.md#class-lineedit) **get_line_edit**()

Returns the LineEdit for the selected file.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

---

[int](class_int.md#class-int) **get_option_default**(option: [int](class_int.md#class-int))

Returns the default value index of the [OptionButton](class_optionbutton.md#class-optionbutton) or [CheckBox](class_checkbox.md#class-checkbox) with index `option`.

---

[String](class_string.md#class-string) **get_option_name**(option: [int](class_int.md#class-int))

Returns the name of the [OptionButton](class_optionbutton.md#class-optionbutton) or [CheckBox](class_checkbox.md#class-checkbox) with index `option`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_option_values**(option: [int](class_int.md#class-int))

Returns an array of values of the [OptionButton](class_optionbutton.md#class-optionbutton) with index `option`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_recent_list**()

Returns the list of recent directories, which is shared by all **FileDialog** nodes. Useful to store the list of recents between project sessions. This method can be called only from the main thread.

---

[Dictionary](class_dictionary.md#class-dictionary) **get_selected_options**()

Returns a [Dictionary](class_dictionary.md#class-dictionary) with the selected values of the additional [OptionButton](class_optionbutton.md#class-optionbutton)s and/or [CheckBox](class_checkbox.md#class-checkbox)es. [Dictionary](class_dictionary.md#class-dictionary) keys are names and values are selected value indices.

---

[VBoxContainer](class_vboxcontainer.md#class-vboxcontainer) **get_vbox**()

Returns the vertical box container of the dialog, custom controls can be added to it.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) property.

**Note:** Changes to this node are ignored by native file dialogs, use add_option() to add custom elements to the dialog instead.

---

 **invalidate**()

Invalidates and updates this dialog's content list.

**Note:** This method does nothing on native file dialogs.

---

[bool](class_bool.md#class-bool) **is_customization_flag_enabled**(flag: Customization)

Returns `true` if the provided `flag` is enabled.

---

 **popup_file_dialog**()

Shows the **FileDialog** using the default size and position for file dialogs, and selects the file name if there is a current file.

---

 **set_customization_flag_enabled**(flag: Customization, enabled: [bool](class_bool.md#class-bool))

Sets the specified customization `flag`, allowing to customize the features available in this **FileDialog**.

---

 **set_favorite_list**(favorites: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Sets the list of favorite directories, which is shared by all **FileDialog** nodes. Useful to restore the list of favorites saved with get_favorite_list(). This method can be called only from the main thread.

**Note:** **FileDialog** will update its internal [ItemList](class_itemlist.md#class-itemlist) of favorites when its visibility changes. Be sure to call this method earlier if you want your changes to have effect.

---

 **set_get_icon_callback**(callback: [Callable](class_callable.md#class-callable))

Sets the callback used by the **FileDialog** nodes to get a file icon, when DISPLAY_LIST mode is used. The callback should take a single [String](class_string.md#class-string) argument (file path), and return a [Texture2D](class_texture2d.md#class-texture2d). If an invalid texture is returned, the file icon will be used instead.

---

 **set_get_thumbnail_callback**(callback: [Callable](class_callable.md#class-callable))

Sets the callback used by the **FileDialog** nodes to get a file icon, when DISPLAY_THUMBNAILS mode is used. The callback should take a single [String](class_string.md#class-string) argument (file path), and return a [Texture2D](class_texture2d.md#class-texture2d). If an invalid texture is returned, the file_thumbnail icon will be used instead.

Thumbnails are usually more complex and may take a while to load. To avoid stalling the application, you can use [ImageTexture](class_imagetexture.md#class-imagetexture) to asynchronously create the thumbnail.

```gdscript
func _ready():
    FileDialog.set_get_thumbnail_callback(thumbnail_method)

func thumbnail_method(path):
    var image_texture = ImageTexture.new()
    make_thumbnail_async(path, image_texture)
    return image_texture

func make_thumbnail_async(path, image_texture):
    var thumbnail_texture = await generate_thumbnail(path) # Some method that generates a thumbnail.
    image_texture.set_image(thumbnail_texture.get_image())
```

---

 **set_option_default**(option: [int](class_int.md#class-int), default_value_index: [int](class_int.md#class-int))

Sets the default value index of the [OptionButton](class_optionbutton.md#class-optionbutton) or [CheckBox](class_checkbox.md#class-checkbox) with index `option`.

---

 **set_option_name**(option: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets the name of the [OptionButton](class_optionbutton.md#class-optionbutton) or [CheckBox](class_checkbox.md#class-checkbox) with index `option`.

---

 **set_option_values**(option: [int](class_int.md#class-int), values: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Sets the option values of the [OptionButton](class_optionbutton.md#class-optionbutton) with index `option`.

---

 **set_recent_list**(recents: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

Sets the list of recent directories, which is shared by all **FileDialog** nodes. Useful to restore the list of recents saved with set_recent_list(). This method can be called only from the main thread.

**Note:** **FileDialog** will update its internal [ItemList](class_itemlist.md#class-itemlist) of recent directories when its visibility changes. Be sure to call this method earlier if you want your changes to have effect.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **file_disabled_color** = `Color(1, 1, 1, 0.25)`

The color tint for disabled files (when the **FileDialog** is used in open folder mode).

---

[Color](class_color.md#class-color) **file_icon_color** = `Color(1, 1, 1, 1)`

The color modulation applied to the file icon.

---

[Color](class_color.md#class-color) **folder_icon_color** = `Color(1, 1, 1, 1)`

The color modulation applied to the folder icon.

---

[int](class_int.md#class-int) **thumbnail_size** = `64`

The size of thumbnail icons when DISPLAY_THUMBNAILS is enabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **back_folder**

Custom icon for the back arrow.

---

[Texture2D](class_texture2d.md#class-texture2d) **create_folder**

Custom icon for the create folder button.

---

[Texture2D](class_texture2d.md#class-texture2d) **favorite**

Custom icon for favorite folder button.

---

[Texture2D](class_texture2d.md#class-texture2d) **favorite_down**

Custom icon for button to move down a favorite entry.

---

[Texture2D](class_texture2d.md#class-texture2d) **favorite_up**

Custom icon for button to move up a favorite entry.

---

[Texture2D](class_texture2d.md#class-texture2d) **file**

Custom icon for files.

---

[Texture2D](class_texture2d.md#class-texture2d) **file_thumbnail**

Icon for files when in thumbnail mode.

---

[Texture2D](class_texture2d.md#class-texture2d) **folder**

Custom icon for folders.

---

[Texture2D](class_texture2d.md#class-texture2d) **folder_thumbnail**

Icon for folders when in thumbnail mode.

---

[Texture2D](class_texture2d.md#class-texture2d) **forward_folder**

Custom icon for the forward arrow.

---

[Texture2D](class_texture2d.md#class-texture2d) **list_mode**

Icon for the button that enables list mode.

---

[Texture2D](class_texture2d.md#class-texture2d) **menu_copy_path**

Icon for the "Copy Path" context menu option.

---

[Texture2D](class_texture2d.md#class-texture2d) **menu_delete**

Icon for the "Delete" context menu option.

---

[Texture2D](class_texture2d.md#class-texture2d) **menu_new_folder**

Icon for the "New Folder..." context menu option. Usually it should be the same as create_folder; leave it empty if you want the context menu to show no icons.

---

[Texture2D](class_texture2d.md#class-texture2d) **menu_open_bundle**

Icon for the "Show Package Contents" context menu option. The option only appears for macOS bundles.

---

[Texture2D](class_texture2d.md#class-texture2d) **menu_refresh**

Icon for the "Refresh" context menu option. Usually it should be the same as reload; leave it empty if you want the context menu to show no icons.

---

[Texture2D](class_texture2d.md#class-texture2d) **menu_show_in_file_manager**

Icon for the "Show in File Manager" context menu option.

---

[Texture2D](class_texture2d.md#class-texture2d) **parent_folder**

Custom icon for the parent folder arrow.

---

[Texture2D](class_texture2d.md#class-texture2d) **reload**

Custom icon for the reload button.

---

[Texture2D](class_texture2d.md#class-texture2d) **sort**

Custom icon for the sorting options menu.

---

[Texture2D](class_texture2d.md#class-texture2d) **thumbnail_mode**

Icon for the button that enables thumbnail mode.

---

[Texture2D](class_texture2d.md#class-texture2d) **toggle_filename_filter**

Custom icon for the toggle button for the filter for file names.

---

[Texture2D](class_texture2d.md#class-texture2d) **toggle_hidden**

Custom icon for the toggle hidden button.
