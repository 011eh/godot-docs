# ImageFormatLoaderExtension

**Inherits:** [ImageFormatLoader](class_imageformatloader.md#class-imageformatloader) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for creating [ImageFormatLoader](class_imageformatloader.md#class-imageformatloader) extensions (adding support for extra image formats).

## Description

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending this class.

Be sure to respect the documented return types and values. You should create an instance of it, and call add_format_loader() to register that loader during the initialization phase.

## Methods

| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)   | \_get_recognized_extensions()                                                                                                                                                                                                                |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Error](class_@globalscope.md#enum-globalscope-error)                     | \_load_image(image: [Image](class_image.md#class-image), fileaccess: [FileAccess](class_fileaccess.md#class-fileaccess), flags: [[LoaderFlags](class_imageformatloader.md#enum-imageformatloader-loaderflags)], scale: [float](class_float.md#class-float)) |
|                                                                           | add_format_loader()                                                                                                                                                                                                                                          |
|                                                                           | remove_format_loader()                                                                                                                                                                                                                                    |

---

## Method Descriptions

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_recognized_extensions**()

Returns the list of file extensions for this image format. Files with the given extensions will be treated as image file and loaded using this class.

---

[Error](class_@globalscope.md#enum-globalscope-error) **\_load_image**(image: [Image](class_image.md#class-image), fileaccess: [FileAccess](class_fileaccess.md#class-fileaccess), flags: [[LoaderFlags](class_imageformatloader.md#enum-imageformatloader-loaderflags)], scale: [float](class_float.md#class-float))

Loads the content of `fileaccess` into the provided `image`.

---

 **add_format_loader**()

Add this format loader to the engine, allowing it to recognize the file extensions returned by \_get_recognized_extensions().

---

 **remove_format_loader**()

Remove this format loader from the engine.
