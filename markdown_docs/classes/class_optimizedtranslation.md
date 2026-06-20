# OptimizedTranslation

**Inherits:** [Translation](class_translation.md#class-translation) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An optimized translation.

## Description

An optimized translation. Uses real-time compressed translations, which results in very small dictionaries.

This class does not store the untranslated strings for optimization purposes. Therefore, [Translation.get_message_list()](class_translation.md#class-translation-method-get-message-list) always returns an empty array, and [Translation.get_message_count()](class_translation.md#class-translation-method-get-message-count) always returns `0`.

## Methods

| [bool](class_bool.md#class-bool)   | generate(from: [Translation](class_translation.md#class-translation))   |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------|

---

## Method Descriptions

[bool](class_bool.md#class-bool) **generate**(from: [Translation](class_translation.md#class-translation))

Generates and sets an optimized translation from the given [Translation](class_translation.md#class-translation) resource. Returns `true` if successful.

**Note:** Messages in `from` should not use context or plural forms.

**Note:** This method is intended to be used in the editor. It does nothing when called from an exported project.
