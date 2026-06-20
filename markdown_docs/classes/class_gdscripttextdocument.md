# GDScriptTextDocument

**Deprecated:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Document related language server functionality.

## Description

Provides language server functionality related to documents.

## Methods

| [Array](class_array.md#class-array)                | codeLens(params: [Dictionary](class_dictionary.md#class-dictionary))                                |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)                | colorPresentation(params: [Dictionary](class_dictionary.md#class-dictionary))              |
| [Array](class_array.md#class-array)                | completion(params: [Dictionary](class_dictionary.md#class-dictionary))                            |
| [Variant](class_variant.md#class-variant)          | declaration(params: [Dictionary](class_dictionary.md#class-dictionary))                          |
| [Array](class_array.md#class-array)                | definition(params: [Dictionary](class_dictionary.md#class-dictionary))                            |
|                                                    | didChange(params: [Variant](class_variant.md#class-variant))                                       |
|                                                    | didClose(params: [Variant](class_variant.md#class-variant))                                         |
|                                                    | didOpen(params: [Variant](class_variant.md#class-variant))                                           |
|                                                    | didSave(params: [Variant](class_variant.md#class-variant))                                           |
| [Array](class_array.md#class-array)                | documentLink(params: [Dictionary](class_dictionary.md#class-dictionary))                        |
| [Array](class_array.md#class-array)                | documentSymbol(params: [Dictionary](class_dictionary.md#class-dictionary))                    |
| [Array](class_array.md#class-array)                | foldingRange(params: [Dictionary](class_dictionary.md#class-dictionary))                        |
| [Variant](class_variant.md#class-variant)          | hover(params: [Dictionary](class_dictionary.md#class-dictionary))                                      |
| [Variant](class_variant.md#class-variant)          | nativeSymbol(params: [Dictionary](class_dictionary.md#class-dictionary))                        |
| [Variant](class_variant.md#class-variant)          | prepareRename(params: [Dictionary](class_dictionary.md#class-dictionary))                      |
| [Array](class_array.md#class-array)                | references(params: [Dictionary](class_dictionary.md#class-dictionary))                            |
| [Dictionary](class_dictionary.md#class-dictionary) | rename(params: [Dictionary](class_dictionary.md#class-dictionary))                                    |
| [Dictionary](class_dictionary.md#class-dictionary) | resolve(params: [Dictionary](class_dictionary.md#class-dictionary))                                  |
|                                                    | show_native_symbol_in_editor(symbol_id: [String](class_string.md#class-string)) |
| [Variant](class_variant.md#class-variant)          | signatureHelp(params: [Dictionary](class_dictionary.md#class-dictionary))                      |
|                                                    | willSaveWaitUntil(params: [Variant](class_variant.md#class-variant))                       |

---

## Method Descriptions

[Array](class_array.md#class-array) **codeLens**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Array](class_array.md#class-array) **colorPresentation**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Array](class_array.md#class-array) **completion**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Variant](class_variant.md#class-variant) **declaration**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Array](class_array.md#class-array) **definition**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

 **didChange**(params: [Variant](class_variant.md#class-variant))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

 **didClose**(params: [Variant](class_variant.md#class-variant))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

 **didOpen**(params: [Variant](class_variant.md#class-variant))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

 **didSave**(params: [Variant](class_variant.md#class-variant))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Array](class_array.md#class-array) **documentLink**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Array](class_array.md#class-array) **documentSymbol**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Array](class_array.md#class-array) **foldingRange**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Variant](class_variant.md#class-variant) **hover**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Variant](class_variant.md#class-variant) **nativeSymbol**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Variant](class_variant.md#class-variant) **prepareRename**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Array](class_array.md#class-array) **references**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Dictionary](class_dictionary.md#class-dictionary) **rename**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[Dictionary](class_dictionary.md#class-dictionary) **resolve**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

 **show_native_symbol_in_editor**(symbol_id: [String](class_string.md#class-string))

**Deprecated:** Use [ScriptEditor.goto_help()](class_scripteditor.md#class-scripteditor-method-goto-help) instead.

---

[Variant](class_variant.md#class-variant) **signatureHelp**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

 **willSaveWaitUntil**(params: [Variant](class_variant.md#class-variant))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.
