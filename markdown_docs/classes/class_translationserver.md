# TranslationServer

**Inherits:** [Object](class_object.md#class-object)

The server responsible for language translations.

## Description

The translation server is the API backend that manages all language translations.

Translations are stored in [TranslationDomain](class_translationdomain.md#class-translationdomain)s, which can be accessed by name. The most commonly used translation domain is the main translation domain. It always exists and can be accessed using an empty [StringName](class_stringname.md#class-stringname). The translation server provides wrapper methods for accessing the main translation domain directly, without having to fetch the translation domain first. Custom translation domains are mainly for advanced usages like editor plugins. Names starting with `godot.` are reserved for engine internals.

## Tutorials

- [Internationalizing games](../tutorials/i18n/internationalizing_games.md)
- [Locales](../tutorials/i18n/locales.md)

## Properties

| [bool](class_bool.md#class-bool)   | pseudolocalization_enabled   | `false`   |
|------------------------------------|----------------------------------------------------------------------------------------------|-----------|

## Methods

|                                                                                            | add_translation(translation: [Translation](class_translation.md#class-translation))                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                            | clear()                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                              | compare_locales(locale_a: [String](class_string.md#class-string), locale_b: [String](class_string.md#class-string))                                                                                                                                     |
| [Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] | find_translations(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool))                                                                                                                                            |
| [String](class_string.md#class-string)                                                     | format_number(number: [String](class_string.md#class-string), locale: [String](class_string.md#class-string))                                                                                                                                             |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                    | get_all_countries()                                                                                                                                                                                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                    | get_all_languages()                                                                                                                                                                                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                    | get_all_scripts()                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                     | get_country_name(country: [String](class_string.md#class-string))                                                                                                                                                                                      |
| [String](class_string.md#class-string)                                                     | get_language_name(language: [String](class_string.md#class-string))                                                                                                                                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                    | get_loaded_locales()                                                                                                                                                                                                                                 |
| [String](class_string.md#class-string)                                                     | get_locale()                                                                                                                                                                                                                                                 |
| [String](class_string.md#class-string)                                                     | get_locale_name(locale: [String](class_string.md#class-string))                                                                                                                                                                                         |
| [TranslationDomain](class_translationdomain.md#class-translationdomain)                    | get_or_add_domain(domain: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                         |
| [String](class_string.md#class-string)                                                     | get_percent_sign(locale: [String](class_string.md#class-string))                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                     | get_plural_rules(locale: [String](class_string.md#class-string))                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                     | get_script_name(script: [String](class_string.md#class-string))                                                                                                                                                                                         |
| [String](class_string.md#class-string)                                                     | get_tool_locale()                                                                                                                                                                                                                                       |
| [Translation](class_translation.md#class-translation)                                      | get_translation_object(locale: [String](class_string.md#class-string))                                                                                                                                                                           |
| [Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] | get_translations()                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                           | has_domain(domain: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                           | has_translation(translation: [Translation](class_translation.md#class-translation))                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                           | has_translation_for_locale(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool))                                                                                                                          |
| [String](class_string.md#class-string)                                                     | parse_number(number: [String](class_string.md#class-string), locale: [String](class_string.md#class-string))                                                                                                                                               |
| [StringName](class_stringname.md#class-stringname)                                         | pseudolocalize(message: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                              |
|                                                                                            | reload_pseudolocalization()                                                                                                                                                                                                                   |
|                                                                                            | remove_domain(domain: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                 |
|                                                                                            | remove_translation(translation: [Translation](class_translation.md#class-translation))                                                                                                                                                               |
|                                                                                            | set_locale(locale: [String](class_string.md#class-string))                                                                                                                                                                                                   |
| [String](class_string.md#class-string)                                                     | standardize_locale(locale: [String](class_string.md#class-string), add_defaults: [bool](class_bool.md#class-bool) = false)                                                                                                                           |
| [StringName](class_stringname.md#class-stringname)                                         | translate(message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")                                                                                                                     |
| [StringName](class_stringname.md#class-stringname)                                         | translate_plural(message: [StringName](class_stringname.md#class-stringname), plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"") |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **pseudolocalization_enabled** = `false`

-  **set_pseudolocalization_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_enabled**()

If `true`, enables the use of pseudolocalization on the main translation domain. See [ProjectSettings.internationalization/pseudolocalization/use_pseudolocalization](class_projectsettings.md#class-projectsettings-property-internationalization-pseudolocalization-use-pseudolocalization) for details.

---

## Method Descriptions

 **add_translation**(translation: [Translation](class_translation.md#class-translation))

Adds a translation to the main translation domain.

---

 **clear**()

Removes all translations from the main translation domain.

---

[int](class_int.md#class-int) **compare_locales**(locale_a: [String](class_string.md#class-string), locale_b: [String](class_string.md#class-string))

Compares two locales and returns a similarity score between `0` (no match) and `10` (full match).

---

[Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] **find_translations**(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool))

Returns the [Translation](class_translation.md#class-translation) instances in the main translation domain that match `locale` (see compare_locales()). If `exact` is `true`, only instances whose locale exactly equals `locale` will be returned.

---

[String](class_string.md#class-string) **format_number**(number: [String](class_string.md#class-string), locale: [String](class_string.md#class-string))

Converts a number from Western Arabic (0..9) to the numeral system used in the given `locale`.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_all_countries**()

Returns an array of known country codes.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_all_languages**()

Returns array of known language codes.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_all_scripts**()

Returns an array of known script codes.

---

[String](class_string.md#class-string) **get_country_name**(country: [String](class_string.md#class-string))

Returns a readable country name for the `country` code.

---

[String](class_string.md#class-string) **get_language_name**(language: [String](class_string.md#class-string))

Returns a readable language name for the `language` code.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_loaded_locales**()

Returns an array of all loaded locales of the project.

---

[String](class_string.md#class-string) **get_locale**()

Returns the current locale of the project.

See also [OS.get_locale()](class_os.md#class-os-method-get-locale) and [OS.get_locale_language()](class_os.md#class-os-method-get-locale-language) to query the locale of the user system.

---

[String](class_string.md#class-string) **get_locale_name**(locale: [String](class_string.md#class-string))

Returns a locale's language and its variant (e.g. `"en_US"` would return `"English (United States)"`).

---

[TranslationDomain](class_translationdomain.md#class-translationdomain) **get_or_add_domain**(domain: [StringName](class_stringname.md#class-stringname))

Returns the translation domain with the specified name. An empty translation domain will be created and added if it does not exist.

---

[String](class_string.md#class-string) **get_percent_sign**(locale: [String](class_string.md#class-string))

Returns the percent sign used in the given `locale`.

---

[String](class_string.md#class-string) **get_plural_rules**(locale: [String](class_string.md#class-string))

Returns the default plural rules for the `locale`.

---

[String](class_string.md#class-string) **get_script_name**(script: [String](class_string.md#class-string))

Returns a readable script name for the `script` code.

---

[String](class_string.md#class-string) **get_tool_locale**()

Returns the current locale of the editor.

**Note:** When called from an exported project returns the same value as get_locale().

---

[Translation](class_translation.md#class-translation) **get_translation_object**(locale: [String](class_string.md#class-string))

**Deprecated:** Use find_translations() instead.

Returns the [Translation](class_translation.md#class-translation) instance that best matches `locale` in the main translation domain. Returns `null` if there are no matches.

---

[Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] **get_translations**()

Returns all available [Translation](class_translation.md#class-translation) instances in the main translation domain as added by add_translation().

---

[bool](class_bool.md#class-bool) **has_domain**(domain: [StringName](class_stringname.md#class-stringname))

Returns `true` if a translation domain with the specified name exists.

---

[bool](class_bool.md#class-bool) **has_translation**(translation: [Translation](class_translation.md#class-translation))

Returns `true` if the main translation domain contains the given `translation`.

---

[bool](class_bool.md#class-bool) **has_translation_for_locale**(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool))

Returns `true` if there are any [Translation](class_translation.md#class-translation) instances in the main translation domain that match `locale` (see compare_locales()). If `exact` is `true`, only instances whose locale exactly equals `locale` are considered.

---

[String](class_string.md#class-string) **parse_number**(number: [String](class_string.md#class-string), locale: [String](class_string.md#class-string))

Converts `number` from the numeral system used in the given `locale` to Western Arabic (0..9).

---

[StringName](class_stringname.md#class-stringname) **pseudolocalize**(message: [StringName](class_stringname.md#class-stringname))

Returns the pseudolocalized string based on the `message` passed in.

**Note:** This method always uses the main translation domain.

---

 **reload_pseudolocalization**()

Reparses the pseudolocalization options and reloads the translation for the main translation domain.

---

 **remove_domain**(domain: [StringName](class_stringname.md#class-stringname))

Removes the translation domain with the specified name.

**Note:** Trying to remove the main translation domain is an error.

---

 **remove_translation**(translation: [Translation](class_translation.md#class-translation))

Removes the given translation from the main translation domain.

---

 **set_locale**(locale: [String](class_string.md#class-string))

Sets the locale of the project. The `locale` string will be standardized to match known locales (e.g. `en-US` would be matched to `en_US`).

If translations have been loaded beforehand for the new locale, they will be applied.

---

[String](class_string.md#class-string) **standardize_locale**(locale: [String](class_string.md#class-string), add_defaults: [bool](class_bool.md#class-bool) = false)

Returns a `locale` string standardized to match known locales (e.g. `en-US` would be matched to `en_US`). If `add_defaults` is `true`, the locale may have a default script or country added.

---

[StringName](class_stringname.md#class-stringname) **translate**(message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")

Returns the current locale's translation for the given message and context.

**Note:** This method always uses the main translation domain.

---

[StringName](class_stringname.md#class-stringname) **translate_plural**(message: [StringName](class_stringname.md#class-stringname), plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"")

Returns the current locale's translation for the given message, plural message and context.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

**Note:** This method always uses the main translation domain.
