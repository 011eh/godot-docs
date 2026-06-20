# ScriptLanguageExtension

**Inherits:** [ScriptLanguage](class_scriptlanguage.md#class-scriptlanguage) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

## Methods

|                                                                                         | \_add_global_constant(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                         | \_add_named_global_constant(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                      |
| [String](class_string.md#class-string)                                                  | \_auto_indent_code(code: [String](class_string.md#class-string), from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | \_can_inherit_from_file()                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | \_can_make_function()                                                                                                                                                                                                                                                                                                |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_complete_code(code: [String](class_string.md#class-string), path: [String](class_string.md#class-string), owner: [Object](class_object.md#class-object))                                                                                                                                                               |
| [Object](class_object.md#class-object)                                                  | \_create_script()                                                                                                                                                                                                                                                                                                        |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_debug_get_current_stack_info()                                                                                                                                                                                                                                                                          |
| [String](class_string.md#class-string)                                                  | \_debug_get_error()                                                                                                                                                                                                                                                                                                    |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_debug_get_globals(max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int))                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                           | \_debug_get_stack_level_count()                                                                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)                                                  | \_debug_get_stack_level_function(level: [int](class_int.md#class-int))                                                                                                                                                                                                                                  |
| `void*`                                                                                 | \_debug_get_stack_level_instance(level: [int](class_int.md#class-int))                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | \_debug_get_stack_level_line(level: [int](class_int.md#class-int))                                                                                                                                                                                                                                          |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_debug_get_stack_level_locals(level: [int](class_int.md#class-int), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int))                                                                                                                                               |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_debug_get_stack_level_members(level: [int](class_int.md#class-int), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int))                                                                                                                                             |
| [String](class_string.md#class-string)                                                  | \_debug_get_stack_level_source(level: [int](class_int.md#class-int))                                                                                                                                                                                                                                      |
| [String](class_string.md#class-string)                                                  | \_debug_parse_stack_level_expression(level: [int](class_int.md#class-int), expression: [String](class_string.md#class-string), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int))                                                                               |
| [int](class_int.md#class-int)                                                           | \_find_function(function: [String](class_string.md#class-string), code: [String](class_string.md#class-string))                                                                                                                                                                                                          |
|                                                                                         | \_finish()                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | \_frame()                                                                                                                                                                                                                                                                                                                        |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_built_in_templates(object: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                            |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_comment_delimiters()                                                                                                                                                                                                                                                                                      |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_doc_comment_delimiters()                                                                                                                                                                                                                                                                              |
| [String](class_string.md#class-string)                                                  | \_get_extension()                                                                                                                                                                                                                                                                                                        |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_get_global_class_name(path: [String](class_string.md#class-string))                                                                                                                                                                                                                                            |
| [String](class_string.md#class-string)                                                  | \_get_name()                                                                                                                                                                                                                                                                                                                  |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_public_annotations()                                                                                                                                                                                                                                                                                      |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_get_public_constants()                                                                                                                                                                                                                                                                                          |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_public_functions()                                                                                                                                                                                                                                                                                          |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_recognized_extensions()                                                                                                                                                                                                                                                                                |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_reserved_words()                                                                                                                                                                                                                                                                                              |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_string_delimiters()                                                                                                                                                                                                                                                                                        |
| [String](class_string.md#class-string)                                                  | \_get_type()                                                                                                                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | \_handles_global_class_type(type: [String](class_string.md#class-string))                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | \_has_named_classes()                                                                                                                                                                                                                                                                                                |
|                                                                                         | \_init()                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | \_is_control_flow_keyword(keyword: [String](class_string.md#class-string))                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | \_is_using_templates()                                                                                                                                                                                                                                                                                              |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_lookup_code(code: [String](class_string.md#class-string), symbol: [String](class_string.md#class-string), path: [String](class_string.md#class-string), owner: [Object](class_object.md#class-object))                                                                                                                   |
| [String](class_string.md#class-string)                                                  | \_make_function(class_name: [String](class_string.md#class-string), function_name: [String](class_string.md#class-string), function_args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))                                                                                                       |
| [Script](class_script.md#class-script)                                                  | \_make_template(template: [String](class_string.md#class-string), class_name: [String](class_string.md#class-string), base_class_name: [String](class_string.md#class-string))                                                                                                                                           |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | \_open_in_external_editor(script: [Script](class_script.md#class-script), line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | \_overrides_external_editor()                                                                                                                                                                                                                                                                                |
| [ScriptNameCasing](class_scriptlanguage.md#enum-scriptlanguage-scriptnamecasing)        | \_preferred_file_name_casing()                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | \_profiling_get_accumulated_data(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class-int))                                                                                                                                                                          |
| [int](class_int.md#class-int)                                                           | \_profiling_get_frame_data(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class-int))                                                                                                                                                                                      |
|                                                                                         | \_profiling_set_save_native_calls(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                            |
|                                                                                         | \_profiling_start()                                                                                                                                                                                                                                                                                                    |
|                                                                                         | \_profiling_stop()                                                                                                                                                                                                                                                                                                      |
|                                                                                         | \_reload_all_scripts()                                                                                                                                                                                                                                                                                              |
|                                                                                         | \_reload_scripts(scripts: [Array](class_array.md#class-array), soft_reload: [bool](class_bool.md#class-bool))                                                                                                                                                                                                           |
|                                                                                         | \_reload_tool_script(script: [Script](class_script.md#class-script), soft_reload: [bool](class_bool.md#class-bool))                                                                                                                                                                                                 |
|                                                                                         | \_remove_named_global_constant(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | \_supports_builtin_mode()                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | \_supports_documentation()                                                                                                                                                                                                                                                                                      |
|                                                                                         | \_thread_enter()                                                                                                                                                                                                                                                                                                          |
|                                                                                         | \_thread_exit()                                                                                                                                                                                                                                                                                                            |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_validate(script: [String](class_string.md#class-string), path: [String](class_string.md#class-string), validate_functions: [bool](class_bool.md#class-bool), validate_errors: [bool](class_bool.md#class-bool), validate_warnings: [bool](class_bool.md#class-bool), validate_safe_lines: [bool](class_bool.md#class-bool)) |
| [String](class_string.md#class-string)                                                  | \_validate_path(path: [String](class_string.md#class-string))                                                                                                                                                                                                                                                            |

---

## Enumerations

enum **LookupResultType**:

LookupResultType **LOOKUP_RESULT_SCRIPT_LOCATION** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_CLASS** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_CLASS_CONSTANT** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_CLASS_PROPERTY** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_CLASS_METHOD** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_CLASS_SIGNAL** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_CLASS_ENUM** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_CLASS_TBD_GLOBALSCOPE** = `7`

**Deprecated:** This constant may be changed or removed in future versions.

LookupResultType **LOOKUP_RESULT_CLASS_ANNOTATION** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_LOCAL_CONSTANT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_LOCAL_VARIABLE** = `10`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LookupResultType **LOOKUP_RESULT_MAX** = `11`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

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

enum **CodeCompletionKind**:

CodeCompletionKind **CODE_COMPLETION_KIND_CLASS** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_FUNCTION** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_SIGNAL** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_VARIABLE** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_MEMBER** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_ENUM** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_CONSTANT** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_NODE_PATH** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_FILE_PATH** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_PLAIN_TEXT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_KEYWORD** = `10`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

CodeCompletionKind **CODE_COMPLETION_KIND_MAX** = `11`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

## Method Descriptions

 **\_add_global_constant**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_add_named_global_constant**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_auto_indent_code**(code: [String](class_string.md#class-string), from_line: [int](class_int.md#class-int), to_line: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_can_inherit_from_file**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_can_make_function**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **\_complete_code**(code: [String](class_string.md#class-string), path: [String](class_string.md#class-string), owner: [Object](class_object.md#class-object))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Object](class_object.md#class-object) **\_create_script**()

**Deprecated:** This method is not called by the engine.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_debug_get_current_stack_info**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_debug_get_error**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **\_debug_get_globals**(max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_debug_get_stack_level_count**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_debug_get_stack_level_function**(level: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

`void*` **\_debug_get_stack_level_instance**(level: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_debug_get_stack_level_line**(level: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **\_debug_get_stack_level_locals**(level: [int](class_int.md#class-int), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **\_debug_get_stack_level_members**(level: [int](class_int.md#class-int), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_debug_get_stack_level_source**(level: [int](class_int.md#class-int))

Returns the source associated with a given debug stack position.

---

[String](class_string.md#class-string) **\_debug_parse_stack_level_expression**(level: [int](class_int.md#class-int), expression: [String](class_string.md#class-string), max_subitems: [int](class_int.md#class-int), max_depth: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_find_function**(function: [String](class_string.md#class-string), code: [String](class_string.md#class-string))

Returns the line where the function is defined in the code, or `-1` if the function is not present.

---

 **\_finish**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_frame**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_built_in_templates**(object: [StringName](class_stringname.md#class-stringname))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_comment_delimiters**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_doc_comment_delimiters**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_get_extension**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_global_class_name**(path: [String](class_string.md#class-string))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_get_name**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_public_annotations**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_public_constants**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_public_functions**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_recognized_extensions**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_reserved_words**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_string_delimiters**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_get_type**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_handles_global_class_type**(type: [String](class_string.md#class-string))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_has_named_classes**()

**Deprecated:** This method is not called by the engine.

---

 **\_init**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_is_control_flow_keyword**(keyword: [String](class_string.md#class-string))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_is_using_templates**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **\_lookup_code**(code: [String](class_string.md#class-string), symbol: [String](class_string.md#class-string), path: [String](class_string.md#class-string), owner: [Object](class_object.md#class-object))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_make_function**(class_name: [String](class_string.md#class-string), function_name: [String](class_string.md#class-string), function_args: [PackedStringArray](class_packedstringarray.md#class-packedstringarray))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Script](class_script.md#class-script) **\_make_template**(template: [String](class_string.md#class-string), class_name: [String](class_string.md#class-string), base_class_name: [String](class_string.md#class-string))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_open_in_external_editor**(script: [Script](class_script.md#class-script), line: [int](class_int.md#class-int), column: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_overrides_external_editor**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[ScriptNameCasing](class_scriptlanguage.md#enum-scriptlanguage-scriptnamecasing) **\_preferred_file_name_casing**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_profiling_get_accumulated_data**(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **\_profiling_get_frame_data**(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_profiling_set_save_native_calls**(enable: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_profiling_start**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_profiling_stop**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_reload_all_scripts**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_reload_scripts**(scripts: [Array](class_array.md#class-array), soft_reload: [bool](class_bool.md#class-bool))

Reloads all `scripts` from disk and the specifics of how that happens is **ScriptLanguageExtension** specific.

---

 **\_reload_tool_script**(script: [Script](class_script.md#class-script), soft_reload: [bool](class_bool.md#class-bool))

Reloads the given `script` from disk and the specifics of how that happens is **ScriptLanguageExtension** specific.

---

 **\_remove_named_global_constant**(name: [StringName](class_stringname.md#class-stringname))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_supports_builtin_mode**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **\_supports_documentation**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_thread_enter**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_thread_exit**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Dictionary](class_dictionary.md#class-dictionary) **\_validate**(script: [String](class_string.md#class-string), path: [String](class_string.md#class-string), validate_functions: [bool](class_bool.md#class-bool), validate_errors: [bool](class_bool.md#class-bool), validate_warnings: [bool](class_bool.md#class-bool), validate_safe_lines: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[String](class_string.md#class-string) **\_validate_path**(path: [String](class_string.md#class-string))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
