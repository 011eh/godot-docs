# EditorResourceConversionPlugin

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Plugin for adding custom converters from one resource format to another in the editor resource picker context menu; for example, converting a [StandardMaterial3D](class_standardmaterial3d.md#class-standardmaterial3d) to a [ShaderMaterial](class_shadermaterial.md#class-shadermaterial).

## Description

**EditorResourceConversionPlugin** is invoked when the context menu is brought up for a resource in the editor inspector. Relevant conversion plugins will appear as menu options to convert the given resource to a target type.

Below shows an example of a basic plugin that will convert an [ImageTexture](class_imagetexture.md#class-imagetexture) to a [PortableCompressedTexture2D](class_portablecompressedtexture2d.md#class-portablecompressedtexture2d).

GDScript

```gdscript
extends EditorResourceConversionPlugin

func _handles(resource: Resource):
    return resource is ImageTexture

func _converts_to():
    return "PortableCompressedTexture2D"

func _convert(itex: Resource):
    var ptex = PortableCompressedTexture2D.new()
    ptex.create_from_image(itex.get_image(), PortableCompressedTexture2D.COMPRESSION_MODE_LOSSLESS)
    return ptex
```

To use an **EditorResourceConversionPlugin**, register it using the [EditorPlugin.add_resource_conversion_plugin()](class_editorplugin.md#class-editorplugin-method-add-resource-conversion-plugin) method first.

## Methods

| [Resource](class_resource.md#class-resource)   | \_convert(resource: [Resource](class_resource.md#class-resource))     |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)         | \_converts_to()                                                   |
| [bool](class_bool.md#class-bool)               | \_handles(resource: [Resource](class_resource.md#class-resource))     |

---

## Method Descriptions

[Resource](class_resource.md#class-resource) **\_convert**(resource: [Resource](class_resource.md#class-resource))

Takes an input [Resource](class_resource.md#class-resource) and converts it to the type given in \_converts_to(). The returned [Resource](class_resource.md#class-resource) is the result of the conversion, and the input [Resource](class_resource.md#class-resource) remains unchanged.

---

[String](class_string.md#class-string) **\_converts_to**()

Returns the class name of the target type of [Resource](class_resource.md#class-resource) that this plugin converts source resources to.

---

[bool](class_bool.md#class-bool) **\_handles**(resource: [Resource](class_resource.md#class-resource))

Called to determine whether a particular [Resource](class_resource.md#class-resource) can be converted to the target resource type by this plugin.
