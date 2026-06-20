# GDScriptLanguageProtocol

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [JSONRPC](class_jsonrpc.md#class-jsonrpc) **<** [Object](class_object.md#class-object)

GDScript language server.

## Description

Provides access to certain features that are implemented in the language server.

**Note:** This class is not a language server client that can be used to access LSP functionality. It only provides access to a limited set of features that is implemented using the same technical foundation as the language server.

## Methods

| [GDScriptTextDocument](class_gdscripttextdocument.md#class-gdscripttextdocument)   | get_text_document()                                                                                                                                                |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GDScriptWorkspace](class_gdscriptworkspace.md#class-gdscriptworkspace)            | get_workspace()                                                                                                                                                        |
| [Variant](class_variant.md#class-variant)                                          | initialize(params: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                    |
|                                                                                    | initialized(params: [Variant](class_variant.md#class-variant))                                                                                                           |
| [bool](class_bool.md#class-bool)                                                   | is_initialized()                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                   | is_smart_resolve_enabled()                                                                                                                                  |
|                                                                                    | notify_client(method: [String](class_string.md#class-string), params: [Variant](class_variant.md#class-variant) = null, client_id: [int](class_int.md#class-int) = -1) |
| [Error](class_@globalscope.md#enum-globalscope-error)                              | on_client_connected()                                                                                                                                            |
|                                                                                    | on_client_disconnected(client_id: [int](class_int.md#class-int))                                                                                              |

---

## Method Descriptions

[GDScriptTextDocument](class_gdscripttextdocument.md#class-gdscripttextdocument) **get_text_document**()

**Deprecated:** [GDScriptTextDocument](class_gdscripttextdocument.md#class-gdscripttextdocument) is deprecated.

Returns the language server's [GDScriptTextDocument](class_gdscripttextdocument.md#class-gdscripttextdocument) instance.

---

[GDScriptWorkspace](class_gdscriptworkspace.md#class-gdscriptworkspace) **get_workspace**()

Returns the language server's [GDScriptWorkspace](class_gdscriptworkspace.md#class-gdscriptworkspace) instance.

---

[Variant](class_variant.md#class-variant) **initialize**(params: [Dictionary](class_dictionary.md#class-dictionary))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

 **initialized**(params: [Variant](class_variant.md#class-variant))

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

---

[bool](class_bool.md#class-bool) **is_initialized**()

Returns `true` if the language server was initialized by a language server client, `false` otherwise.

---

[bool](class_bool.md#class-bool) **is_smart_resolve_enabled**()

Returns `true` if the language server is providing the smart resolve feature, `false` otherwise. The feature can be configured through the editor settings.

---

 **notify_client**(method: [String](class_string.md#class-string), params: [Variant](class_variant.md#class-variant) = null, client_id: [int](class_int.md#class-int) = -1)

**Deprecated:** Might result in unwanted side effects for connected clients.

---

[Error](class_@globalscope.md#enum-globalscope-error) **on_client_connected**()

**Deprecated:** Might result in unwanted side effects for connected clients.

---

 **on_client_disconnected**(client_id: [int](class_int.md#class-int))

**Deprecated:** Might result in unwanted side effects for connected clients.
