# Translation

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OptimizedTranslation](class_optimizedtranslation.md#class-optimizedtranslation)

A language translation that maps a collection of strings to their individual translations.

## Description

**Translation** maps a collection of strings to their individual translations, and also provides convenience methods for pluralization.

A **Translation** consists of messages. A message is identified by its context and untranslated string. Unlike [gettext](https://www.gnu.org/software/gettext/), using an empty context string in Godot means not using any context.

## Tutorials

- [Internationalizing games](../tutorials/i18n/internationalizing_games.md)
- [Localization using gettext](../tutorials/i18n/localization_using_gettext.md)
- [Locales](../tutorials/i18n/locales.md)

## Properties

| [String](class_string.md#class-string)   | locale                               | `"en"`   |
|------------------------------------------|----------------------------------------------------------------------------|----------|
| [String](class_string.md#class-string)   | plural_rules_override | `""`     |

## Methods

| [StringName](class_stringname.md#class-stringname)                      | \_get_message(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname))                                                                                                                         |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StringName](class_stringname.md#class-stringname)                      | \_get_plural_message(src_message: [StringName](class_stringname.md#class-stringname), src_plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname)) |
|                                                                         | add_message(src_message: [StringName](class_stringname.md#class-stringname), xlated_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")                                                         |
|                                                                         | add_plural_message(src_message: [StringName](class_stringname.md#class-stringname), xlated_messages: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), context: [StringName](class_stringname.md#class-stringname) = &"")                     |
|                                                                         | erase_message(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")                                                                                                                         |
| [StringName](class_stringname.md#class-stringname)                      | get_message(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")                                                                                                                             |
| [int](class_int.md#class-int)                                           | get_message_count()                                                                                                                                                                                                                                                   |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_message_list()                                                                                                                                                                                                                                                     |
| [StringName](class_stringname.md#class-stringname)                      | get_plural_message(src_message: [StringName](class_stringname.md#class-stringname), src_plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"")     |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | get_translated_message_list()                                                                                                                                                                                                                               |

---

## Property Descriptions

[String](class_string.md#class-string) **locale** = `"en"`

-  **set_locale**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_locale**()

The locale of the translation.

---

[String](class_string.md#class-string) **plural_rules_override** = `""`

-  **set_plural_rules_override**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_plural_rules_override**()

The plural rules string to enforce. See [GNU gettext](https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html) for examples and more info.

If empty or invalid, default plural rules from [TranslationServer.get_plural_rules()](class_translationserver.md#class-translationserver-method-get-plural-rules) are used. The English plural rules are used as a fallback.

---

## Method Descriptions

[StringName](class_stringname.md#class-stringname) **\_get_message**(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname))

Virtual method to override get_message().

---

[StringName](class_stringname.md#class-stringname) **\_get_plural_message**(src_message: [StringName](class_stringname.md#class-stringname), src_plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname))

Virtual method to override get_plural_message().

---

 **add_message**(src_message: [StringName](class_stringname.md#class-stringname), xlated_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")

Adds a message if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.

---

 **add_plural_message**(src_message: [StringName](class_stringname.md#class-stringname), xlated_messages: [PackedStringArray](class_packedstringarray.md#class-packedstringarray), context: [StringName](class_stringname.md#class-stringname) = &"")

Adds a message involving plural translation if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.

---

 **erase_message**(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")

Erases a message.

---

[StringName](class_stringname.md#class-stringname) **get_message**(src_message: [StringName](class_stringname.md#class-stringname), context: [StringName](class_stringname.md#class-stringname) = &"")

Returns a message's translation.

---

[int](class_int.md#class-int) **get_message_count**()

Returns the number of existing messages.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_message_list**()

Returns the keys of all messages, that is, the context and untranslated strings of each message.

**Note:** If a message does not use a context, the corresponding element is the untranslated string. Otherwise, the corresponding element is the context and untranslated string separated by the EOT character (`U+0004`). This is done for compatibility purposes.

```gdscript
for key in translation.get_message_list():
    var p = key.find("\u0004")
    if p == -1:
        var untranslated = key
        print("Message %s" % untranslated)
    else:
        var context = key.substr(0, p)
        var untranslated = key.substr(p + 1)
        print("Message %s with context %s" % [untranslated, context])
```

---

[StringName](class_stringname.md#class-stringname) **get_plural_message**(src_message: [StringName](class_stringname.md#class-stringname), src_plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = &"")

Returns a message's translation involving plurals.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

**Note:** Plurals are only supported in [gettext-based translations (PO)](../tutorials/i18n/localization_using_gettext.md), not CSV.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **get_translated_message_list**()

Returns all the translated strings.
