# EditorResourcePreview

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node used to generate previews of resources or files.

## Description

This node is used to generate previews for resources or files.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_resource_previewer()](class_editorinterface.md#class-editorinterface-method-get-resource-previewer).

## Methods

|    | add_preview_generator(generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator))                                                                                                                        |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | check_for_invalidation(path: [String](class_string.md#class-string))                                                                                                                                                                                                   |
|    | queue_edited_resource_preview(resource: [Resource](class_resource.md#class-resource), receiver: [Object](class_object.md#class-object), receiver_func: [StringName](class_stringname.md#class-stringname), userdata: [Variant](class_variant.md#class-variant)) |
|    | queue_resource_preview(path: [String](class_string.md#class-string), receiver: [Object](class_object.md#class-object), receiver_func: [StringName](class_stringname.md#class-stringname), userdata: [Variant](class_variant.md#class-variant))                         |
|    | remove_preview_generator(generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator))                                                                                                                  |

---

## Signals

**preview_invalidated**(path: [String](class_string.md#class-string))

Emitted if a preview was invalidated (changed). `path` corresponds to the path of the preview.

---

## Method Descriptions

 **add_preview_generator**(generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator))

Create an own, custom preview generator.

---

 **check_for_invalidation**(path: [String](class_string.md#class-string))

Check if the resource changed, if so, it will be invalidated and the corresponding signal emitted.

---

 **queue_edited_resource_preview**(resource: [Resource](class_resource.md#class-resource), receiver: [Object](class_object.md#class-object), receiver_func: [StringName](class_stringname.md#class-stringname), userdata: [Variant](class_variant.md#class-variant))

Queue the `resource` being edited for preview. Once the preview is ready, the `receiver`'s `receiver_func` will be called. The `receiver_func` must take the following four arguments: [String](class_string.md#class-string) path, [Texture2D](class_texture2d.md#class-texture2d) preview, [Texture2D](class_texture2d.md#class-texture2d) thumbnail_preview, [Variant](class_variant.md#class-variant) userdata. `userdata` can be anything, and will be returned when `receiver_func` is called.

**Note:** If it was not possible to create the preview the `receiver_func` will still be called, but the preview will be `null`.

---

 **queue_resource_preview**(path: [String](class_string.md#class-string), receiver: [Object](class_object.md#class-object), receiver_func: [StringName](class_stringname.md#class-stringname), userdata: [Variant](class_variant.md#class-variant))

Queue a resource file located at `path` for preview. Once the preview is ready, the `receiver`'s `receiver_func` will be called. The `receiver_func` must take the following four arguments: [String](class_string.md#class-string) path, [Texture2D](class_texture2d.md#class-texture2d) preview, [Texture2D](class_texture2d.md#class-texture2d) thumbnail_preview, [Variant](class_variant.md#class-variant) userdata. `userdata` can be anything, and will be returned when `receiver_func` is called.

**Note:** If it was not possible to create the preview the `receiver_func` will still be called, but the preview will be `null`.

---

 **remove_preview_generator**(generator: [EditorResourcePreviewGenerator](class_editorresourcepreviewgenerator.md#class-editorresourcepreviewgenerator))

Removes a custom preview generator.
