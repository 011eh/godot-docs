# EditorVCSInterface

**Inherits:** [Object](class_object.md#class-object)

Version Control System (VCS) interface, which reads and writes to the local VCS in use.

## Description

Defines the API that the editor uses to extract information from the underlying VCS. The implementation of this API is included in VCS plugins, which are GDExtension plugins that inherit **EditorVCSInterface** and are attached (on demand) to the singleton instance of **EditorVCSInterface**. Instead of performing the task themselves, all the virtual functions listed below are calling the internally overridden functions in the VCS plugins to provide a plug-n-play experience. A custom VCS plugin is supposed to inherit from **EditorVCSInterface** and override each of these virtual functions.

## Tutorials

- [Version control systems](../tutorials/best_practices/version_control_systems.md)

## Methods

| [bool](class_bool.md#class-bool)                                                        | \_allow_amends()                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                                        | \_checkout_branch(branch_name: [String](class_string.md#class-string))                                                                                                                                                                                                                                   |
|                                                                                         | \_commit(msg: [String](class_string.md#class-string), amend: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                    |
|                                                                                         | \_create_branch(branch_name: [String](class_string.md#class-string))                                                                                                                                                                                                                                       |
|                                                                                         | \_create_remote(remote_name: [String](class_string.md#class-string), remote_url: [String](class_string.md#class-string))                                                                                                                                                                                   |
|                                                                                         | \_discard_file(file_path: [String](class_string.md#class-string))                                                                                                                                                                                                                                           |
|                                                                                         | \_fetch(remote: [String](class_string.md#class-string))                                                                                                                                                                                                                                                            |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)]             | \_get_branch_list()                                                                                                                                                                                                                                                                                      |
| [String](class_string.md#class-string)                                                  | \_get_current_branch_name()                                                                                                                                                                                                                                                                      |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_diff(identifier: [String](class_string.md#class-string), area: [int](class_int.md#class-int))                                                                                                                                                                                                             |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_line_diff(file_path: [String](class_string.md#class-string), text: [String](class_string.md#class-string))                                                                                                                                                                                           |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_modified_files_data()                                                                                                                                                                                                                                                                      |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_previous_commits(max_commits: [int](class_int.md#class-int))                                                                                                                                                                                                                                  |
| [Array](class_array.md#class-array)[[String](class_string.md#class-string)]             | \_get_remotes()                                                                                                                                                                                                                                                                                              |
| [String](class_string.md#class-string)                                                  | \_get_vcs_name()                                                                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                        | \_initialize(project_path: [String](class_string.md#class-string))                                                                                                                                                                                                                                            |
|                                                                                         | \_pull(remote: [String](class_string.md#class-string))                                                                                                                                                                                                                                                              |
|                                                                                         | \_push(remote: [String](class_string.md#class-string), force: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                     |
|                                                                                         | \_remove_branch(branch_name: [String](class_string.md#class-string))                                                                                                                                                                                                                                       |
|                                                                                         | \_remove_remote(remote_name: [String](class_string.md#class-string))                                                                                                                                                                                                                                       |
|                                                                                         | \_set_credentials(username: [String](class_string.md#class-string), password: [String](class_string.md#class-string), ssh_public_key_path: [String](class_string.md#class-string), ssh_private_key_path: [String](class_string.md#class-string), ssh_passphrase: [String](class_string.md#class-string)) |
| [bool](class_bool.md#class-bool)                                                        | \_shut_down()                                                                                                                                                                                                                                                                                                  |
|                                                                                         | \_stage_file(file_path: [String](class_string.md#class-string))                                                                                                                                                                                                                                               |
|                                                                                         | \_unstage_file(file_path: [String](class_string.md#class-string))                                                                                                                                                                                                                                           |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | add_diff_hunks_into_diff_file(diff_file: [Dictionary](class_dictionary.md#class-dictionary), diff_hunks: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)])                                                                                                  |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | add_line_diffs_into_diff_hunk(diff_hunk: [Dictionary](class_dictionary.md#class-dictionary), line_diffs: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)])                                                                                                  |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | create_commit(msg: [String](class_string.md#class-string), author: [String](class_string.md#class-string), id: [String](class_string.md#class-string), unix_timestamp: [int](class_int.md#class-int), offset_minutes: [int](class_int.md#class-int))                                                               |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | create_diff_file(new_file: [String](class_string.md#class-string), old_file: [String](class_string.md#class-string))                                                                                                                                                                                            |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | create_diff_hunk(old_start: [int](class_int.md#class-int), new_start: [int](class_int.md#class-int), old_lines: [int](class_int.md#class-int), new_lines: [int](class_int.md#class-int))                                                                                                                        |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | create_diff_line(new_line_no: [int](class_int.md#class-int), old_line_no: [int](class_int.md#class-int), content: [String](class_string.md#class-string), status: [String](class_string.md#class-string))                                                                                                       |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | create_status_file(file_path: [String](class_string.md#class-string), change_type: ChangeType, area: TreeArea)                                                                                                                    |
|                                                                                         | popup_error(msg: [String](class_string.md#class-string))                                                                                                                                                                                                                                                             |

---

## Enumerations

enum **ChangeType**:

ChangeType **CHANGE_TYPE_NEW** = `0`

A new file has been added.

ChangeType **CHANGE_TYPE_MODIFIED** = `1`

An earlier added file has been modified.

ChangeType **CHANGE_TYPE_RENAMED** = `2`

An earlier added file has been renamed.

ChangeType **CHANGE_TYPE_DELETED** = `3`

An earlier added file has been deleted.

ChangeType **CHANGE_TYPE_TYPECHANGE** = `4`

An earlier added file has been typechanged.

ChangeType **CHANGE_TYPE_UNMERGED** = `5`

A file is left unmerged.

---

enum **TreeArea**:

TreeArea **TREE_AREA_COMMIT** = `0`

A commit is encountered from the commit area.

TreeArea **TREE_AREA_STAGED** = `1`

A file is encountered from the staged area.

TreeArea **TREE_AREA_UNSTAGED** = `2`

A file is encountered from the unstaged area.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **\_allow_amends**()

Returns whether or not the plugin allows commit amends.

---

[bool](class_bool.md#class-bool) **\_checkout_branch**(branch_name: [String](class_string.md#class-string))

Checks out a `branch_name` in the VCS.

---

 **\_commit**(msg: [String](class_string.md#class-string), amend: [bool](class_bool.md#class-bool))

Commits the currently staged changes and applies the commit `msg` to the resulting commit. If `amend` is `true` the commit will modify the most recent commit instead.

---

 **\_create_branch**(branch_name: [String](class_string.md#class-string))

Creates a new branch named `branch_name` in the VCS.

---

 **\_create_remote**(remote_name: [String](class_string.md#class-string), remote_url: [String](class_string.md#class-string))

Creates a new remote destination with name `remote_name` and points it to `remote_url`. This can be an HTTPS remote or an SSH remote.

---

 **\_discard_file**(file_path: [String](class_string.md#class-string))

Discards the changes made in a file present at `file_path`.

---

 **\_fetch**(remote: [String](class_string.md#class-string))

Fetches new changes from the `remote`, but doesn't write changes to the current working directory. Equivalent to `git fetch`.

---

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **\_get_branch_list**()

Gets an instance of an [Array](class_array.md#class-array) of [String](class_string.md#class-string)s containing available branch names in the VCS.

---

[String](class_string.md#class-string) **\_get_current_branch_name**()

Gets the current branch name defined in the VCS.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_diff**(identifier: [String](class_string.md#class-string), area: [int](class_int.md#class-int))

Returns an array of [Dictionary](class_dictionary.md#class-dictionary) items (see create_diff_file(), create_diff_hunk(), create_diff_line(), add_line_diffs_into_diff_hunk() and add_diff_hunks_into_diff_file()), each containing information about a diff. If `identifier` is a file path, returns a file diff, and if it is a commit identifier, then returns a commit diff.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_line_diff**(file_path: [String](class_string.md#class-string), text: [String](class_string.md#class-string))

Returns an [Array](class_array.md#class-array) of [Dictionary](class_dictionary.md#class-dictionary) items (see create_diff_hunk()), each containing a line diff between a file at `file_path` and the `text` which is passed in.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_modified_files_data**()

Returns an [Array](class_array.md#class-array) of [Dictionary](class_dictionary.md#class-dictionary) items (see create_status_file()), each containing the status data of every modified file in the project folder.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_previous_commits**(max_commits: [int](class_int.md#class-int))

Returns an [Array](class_array.md#class-array) of [Dictionary](class_dictionary.md#class-dictionary) items (see create_commit()), each containing the data for a past commit.

---

[Array](class_array.md#class-array)[[String](class_string.md#class-string)] **\_get_remotes**()

Returns an [Array](class_array.md#class-array) of [String](class_string.md#class-string)s, each containing the name of a remote configured in the VCS.

---

[String](class_string.md#class-string) **\_get_vcs_name**()

Returns the name of the underlying VCS provider.

---

[bool](class_bool.md#class-bool) **\_initialize**(project_path: [String](class_string.md#class-string))

Initializes the VCS plugin when called from the editor. Returns whether or not the plugin was successfully initialized. A VCS project is initialized at `project_path`.

---

 **\_pull**(remote: [String](class_string.md#class-string))

Pulls changes from the remote. This can give rise to merge conflicts.

---

 **\_push**(remote: [String](class_string.md#class-string), force: [bool](class_bool.md#class-bool))

Pushes changes to the `remote`. If `force` is `true`, a force push will override the change history already present on the remote.

---

 **\_remove_branch**(branch_name: [String](class_string.md#class-string))

Remove a branch from the local VCS.

---

 **\_remove_remote**(remote_name: [String](class_string.md#class-string))

Remove a remote from the local VCS.

---

 **\_set_credentials**(username: [String](class_string.md#class-string), password: [String](class_string.md#class-string), ssh_public_key_path: [String](class_string.md#class-string), ssh_private_key_path: [String](class_string.md#class-string), ssh_passphrase: [String](class_string.md#class-string))

Set user credentials in the underlying VCS. `username` and `password` are used only during HTTPS authentication unless not already mentioned in the remote URL. `ssh_public_key_path`, `ssh_private_key_path`, and `ssh_passphrase` are only used during SSH authentication.

---

[bool](class_bool.md#class-bool) **\_shut_down**()

Shuts down VCS plugin instance. Called when the user either closes the editor or shuts down the VCS plugin through the editor UI.

---

 **\_stage_file**(file_path: [String](class_string.md#class-string))

Stages the file present at `file_path` to the staged area.

---

 **\_unstage_file**(file_path: [String](class_string.md#class-string))

Unstages the file present at `file_path` from the staged area to the unstaged area.

---

[Dictionary](class_dictionary.md#class-dictionary) **add_diff_hunks_into_diff_file**(diff_file: [Dictionary](class_dictionary.md#class-dictionary), diff_hunks: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)])

Helper function to add an array of `diff_hunks` into a `diff_file`.

---

[Dictionary](class_dictionary.md#class-dictionary) **add_line_diffs_into_diff_hunk**(diff_hunk: [Dictionary](class_dictionary.md#class-dictionary), line_diffs: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)])

Helper function to add an array of `line_diffs` into a `diff_hunk`.

---

[Dictionary](class_dictionary.md#class-dictionary) **create_commit**(msg: [String](class_string.md#class-string), author: [String](class_string.md#class-string), id: [String](class_string.md#class-string), unix_timestamp: [int](class_int.md#class-int), offset_minutes: [int](class_int.md#class-int))

Helper function to create a commit [Dictionary](class_dictionary.md#class-dictionary) item. `msg` is the commit message of the commit. `author` is a single human-readable string containing all the author's details, e.g. the email and name configured in the VCS. `id` is the identifier of the commit, in whichever format your VCS may provide an identifier to commits. `unix_timestamp` is the UTC Unix timestamp of when the commit was created. `offset_minutes` is the timezone offset in minutes, recorded from the system timezone where the commit was created.

---

[Dictionary](class_dictionary.md#class-dictionary) **create_diff_file**(new_file: [String](class_string.md#class-string), old_file: [String](class_string.md#class-string))

Helper function to create a [Dictionary](class_dictionary.md#class-dictionary) for storing old and new diff file paths.

---

[Dictionary](class_dictionary.md#class-dictionary) **create_diff_hunk**(old_start: [int](class_int.md#class-int), new_start: [int](class_int.md#class-int), old_lines: [int](class_int.md#class-int), new_lines: [int](class_int.md#class-int))

Helper function to create a [Dictionary](class_dictionary.md#class-dictionary) for storing diff hunk data. `old_start` is the starting line number in old file. `new_start` is the starting line number in new file. `old_lines` is the number of lines in the old file. `new_lines` is the number of lines in the new file.

---

[Dictionary](class_dictionary.md#class-dictionary) **create_diff_line**(new_line_no: [int](class_int.md#class-int), old_line_no: [int](class_int.md#class-int), content: [String](class_string.md#class-string), status: [String](class_string.md#class-string))

Helper function to create a [Dictionary](class_dictionary.md#class-dictionary) for storing a line diff. `new_line_no` is the line number in the new file (can be `-1` if the line is deleted). `old_line_no` is the line number in the old file (can be `-1` if the line is added). `content` is the diff text. `status` is a single character string which stores the line origin.

---

[Dictionary](class_dictionary.md#class-dictionary) **create_status_file**(file_path: [String](class_string.md#class-string), change_type: ChangeType, area: TreeArea)

Helper function to create a [Dictionary](class_dictionary.md#class-dictionary) used by editor to read the status of a file.

---

 **popup_error**(msg: [String](class_string.md#class-string))

Pops up an error message in the editor which is shown as coming from the underlying VCS. Use this to show VCS specific error messages.
