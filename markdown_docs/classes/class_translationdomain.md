# TranslationDomain

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A self-contained collection of [Translation](class_translation.md#class-translation) resources.

## Description

**TranslationDomain** is a self-contained collection of [Translation](class_translation.md#class-translation) resources. Translations can be added to or removed from it.

If you're working with the main translation domain, it is more convenient to use the wrap methods on [TranslationServer](class_translationserver.md#class-translationserver).

## Properties

| [bool](class_bool.md#class-bool)       | enabled                                                                           | `true`   |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------|
| [bool](class_bool.md#class-bool)       | pseudolocalization_accents_enabled                     | `true`   |
| [bool](class_bool.md#class-bool)       | pseudolocalization_double_vowels_enabled         | `false`  |
| [bool](class_bool.md#class-bool)       | pseudolocalization_enabled                                     | `false`  |
| [float](class_float.md#class-float)    | pseudolocalization_expansion_ratio                     | `0.0`    |
| [bool](class_bool.md#class-bool)       | pseudolocalization_fake_bidi_enabled                 | `false`  |
| [bool](class_bool.md#class-bool)       | pseudolocalization_override_enabled                   | `false`  |
| [String](class_string.md#class-string) | pseudolocalization_prefix                                       | `"["`    |
| [bool](class_bool.md#class-bool)       | pseudolocalization_skip_placeholders_enabled | `true`   |
| [String](class_string.md#class-string) | pseudolocalization_suffix                                       | `"]"`    |

## Methods

|                                                                                            | add_translation(translation: [Translation](class_translation.md#class-translation))                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                            | clear()                                                                                                                                                                                                                                                           |
| [Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] | find_translations(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool))                                                                                                                                            |
| [String](class_string.md#class-string)                                                     | get_locale_override()                                                                                                                                                                                                                               |
| [Translation](class_translation.md#class-translation)                                      | get_translation_object(locale: [String](class_string.md#class-string))                                                                                                                                                                           |
| [Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] | get_translations()                                                                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                           | has_translation(translation: [Translation](class_translation.md#class-translation))                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                           | has_translation_for_locale(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool))                                                                                                                          |
| [StringName](class_stringname.md#class-stringname)                                         | pseudolocalize(message: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                              |
|                                                                                            | remove_translation(translation: [Translation](class_translation.md#class-translation))                                                                                                                                                               |
|                                                                                            | set_locale_override(locale: [String](class_string.md#class-string))                                                                                                                                                                                 |
| [StringName](class_stringname.md#class-stringname)                                         | translate(message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")                                                                                                                     |
| [StringName](class_stringname.md#class-stringname)                                         | translate_plural(message: [StringName](class_stringname.md#class-stringname), message_plural: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"") |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **enabled** = `true`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

If `true`, translation is enabled. Otherwise, translate() and translate_plural() will return the input message unchanged regardless of the current locale.

---

[bool](class_bool.md#class-bool) **pseudolocalization_accents_enabled** = `true`

-  **set_pseudolocalization_accents_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_accents_enabled**()

Replace all characters with their accented variants during pseudolocalization.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

[bool](class_bool.md#class-bool) **pseudolocalization_double_vowels_enabled** = `false`

-  **set_pseudolocalization_double_vowels_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_double_vowels_enabled**()

Double vowels in strings during pseudolocalization to simulate the lengthening of text due to localization.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

[bool](class_bool.md#class-bool) **pseudolocalization_enabled** = `false`

-  **set_pseudolocalization_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_enabled**()

If `true`, enables pseudolocalization for the project. This can be used to spot untranslatable strings or layout issues that may occur once the project is localized to languages that have longer strings than the source language.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

[float](class_float.md#class-float) **pseudolocalization_expansion_ratio** = `0.0`

-  **set_pseudolocalization_expansion_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_pseudolocalization_expansion_ratio**()

The expansion ratio to use during pseudolocalization. A value of `0.3` is sufficient for most practical purposes, and will increase the length of each string by 30%.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

[bool](class_bool.md#class-bool) **pseudolocalization_fake_bidi_enabled** = `false`

-  **set_pseudolocalization_fake_bidi_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_fake_bidi_enabled**()

If `true`, emulate bidirectional (right-to-left) text when pseudolocalization is enabled. This can be used to spot issues with RTL layout and UI mirroring that will crop up if the project is localized to RTL languages such as Arabic or Hebrew.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

[bool](class_bool.md#class-bool) **pseudolocalization_override_enabled** = `false`

-  **set_pseudolocalization_override_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_override_enabled**()

Replace all characters in the string with `*`. Useful for finding non-localizable strings.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

[String](class_string.md#class-string) **pseudolocalization_prefix** = `"["`

-  **set_pseudolocalization_prefix**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_pseudolocalization_prefix**()

Prefix that will be prepended to the pseudolocalized string.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

[bool](class_bool.md#class-bool) **pseudolocalization_skip_placeholders_enabled** = `true`

-  **set_pseudolocalization_skip_placeholders_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pseudolocalization_skip_placeholders_enabled**()

Skip placeholders for string formatting like `%s` or `%f` during pseudolocalization. Useful to identify strings which need additional control characters to display correctly.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

[String](class_string.md#class-string) **pseudolocalization_suffix** = `"]"`

-  **set_pseudolocalization_suffix**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_pseudolocalization_suffix**()

Suffix that will be appended to the pseudolocalized string.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) notification manually after you have finished modifying pseudolocalization related options.

---

## Method Descriptions

 **add_translation**(translation: [Translation](class_translation.md#class-translation))

Adds a translation.

---

 **clear**()

Removes all translations.

---

[Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] **find_translations**(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool))

Returns the [Translation](class_translation.md#class-translation) instances that match `locale` (see [TranslationServer.compare_locales()](class_translationserver.md#class-translationserver-method-compare-locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` will be returned.

---

[String](class_string.md#class-string) **get_locale_override**()

Returns the locale override of the domain. Returns an empty string if locale override is disabled.

---

[Translation](class_translation.md#class-translation) **get_translation_object**(locale: [String](class_string.md#class-string))

**Deprecated:** Use find_translations() instead.

Returns the [Translation](class_translation.md#class-translation) instance that best matches `locale`. Returns `null` if there are no matches.

---

[Array](class_array.md#class-array)[[Translation](class_translation.md#class-translation)] **get_translations**()

Returns all available [Translation](class_translation.md#class-translation) instances as added by add_translation().

---

[bool](class_bool.md#class-bool) **has_translation**(translation: [Translation](class_translation.md#class-translation))

Returns `true` if this translation domain contains the given `translation`.

---

[bool](class_bool.md#class-bool) **has_translation_for_locale**(locale: [String](class_string.md#class-string), exact: [bool](class_bool.md#class-bool))

Returns `true` if there are any [Translation](class_translation.md#class-translation) instances that match `locale` (see [TranslationServer.compare_locales()](class_translationserver.md#class-translationserver-method-compare-locales)). If `exact` is `true`, only instances whose locale exactly equals `locale` are considered.

---

[StringName](class_stringname.md#class-stringname) **pseudolocalize**(message: [StringName](class_stringname.md#class-stringname))

Returns the pseudolocalized string based on the `message` passed in.

---

 **remove_translation**(translation: [Translation](class_translation.md#class-translation))

Removes the given translation.

---

 **set_locale_override**(locale: [String](class_string.md#class-string))

Sets the locale override of the domain.

If `locale` is an empty string, locale override is disabled. Otherwise, `locale` will be standardized to match known locales (e.g. `en-US` would be matched to `en_US`).

**Note:** Calling this method does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED](class_mainloop.md#class-mainloop-constant-notification-translation-changed) signal manually.

---

[StringName](class_stringname.md#class-stringname) **translate**(message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")

Returns the current locale's translation for the given message and context.

---

[StringName](class_stringname.md#class-stringname) **translate_plural**(message: [StringName](class_stringname.md#class-stringname), message_plural: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"")

Returns the current locale's translation for the given message, plural message and context.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.
