# CameraFeed

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A camera feed gives you access to a single physical camera attached to your device.

## Description

A camera feed gives you access to a single physical camera attached to your device. When enabled, Godot will start capturing frames from the camera which can then be used. See also [CameraServer](class_cameraserver.md#class-cameraserver).

**Note:** Many cameras will return YCbCr images which are split into two textures and need to be combined in a shader. Godot does this automatically for you if you set the environment to show the camera image in the background.

**Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no **CameraFeed**s will be available. To get a **CameraFeed** on iOS, enable [EditorExportPlatformIOS.modules/camera](class_editorexportplatformios.md#class-editorexportplatformios-property-modules-camera).

## Properties

| [bool](class_bool.md#class-bool)                      | feed_is_active   | `false`                          |
|-------------------------------------------------------|---------------------------------------------------------------|----------------------------------|
| [Transform2D](class_transform2d.md#class-transform2d) | feed_transform   | `Transform2D(1, 0, 0, -1, 0, 1)` |
| [Array](class_array.md#class-array)                   | formats                 | `[]`                             |

## Methods

| [bool](class_bool.md#class-bool)              | \_activate_feed()                                                                                               |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                               | \_deactivate_feed()                                                                                           |
| [Array](class_array.md#class-array)           | \_get_formats()                                                                                                   |
| [bool](class_bool.md#class-bool)              | \_set_format(index: [int](class_int.md#class-int), parameters: [Dictionary](class_dictionary.md#class-dictionary)) |
| FeedDataType | get_datatype()                                                                                                           |
| [int](class_int.md#class-int)                 | get_id()                                                                                                                       |
| [String](class_string.md#class-string)        | get_name()                                                                                                                   |
| FeedPosition | get_position()                                                                                                           |
| [int](class_int.md#class-int)                 | get_texture_tex_id(feed_image_type: [FeedImage](class_cameraserver.md#enum-cameraserver-feedimage))                |
|                                               | set_external(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int))                                |
| [bool](class_bool.md#class-bool)              | set_format(index: [int](class_int.md#class-int), parameters: [Dictionary](class_dictionary.md#class-dictionary))           |
|                                               | set_name(name: [String](class_string.md#class-string))                                                                       |
|                                               | set_position(position: FeedPosition)                                                    |
|                                               | set_rgb_image(rgb_image: [Image](class_image.md#class-image))                                                           |
|                                               | set_ycbcr_image(ycbcr_image: [Image](class_image.md#class-image))                                                     |
|                                               | set_ycbcr_images(y_image: [Image](class_image.md#class-image), cbcr_image: [Image](class_image.md#class-image))      |

---

## Signals

**format_changed**()

Emitted when the format has changed.

---

**frame_changed**()

Emitted when a new frame is available.

---

## Enumerations

enum **FeedDataType**:

FeedDataType **FEED_NOIMAGE** = `0`

No image set for the feed.

FeedDataType **FEED_RGB** = `1`

Feed supplies RGB images.

FeedDataType **FEED_YCBCR** = `2`

Feed supplies YCbCr images that need to be converted to RGB.

FeedDataType **FEED_YCBCR_SEP** = `3`

Feed supplies separate Y and CbCr images that need to be combined and converted to RGB.

FeedDataType **FEED_EXTERNAL** = `4`

Feed supplies external image.

---

enum **FeedPosition**:

FeedPosition **FEED_UNSPECIFIED** = `0`

Unspecified position.

FeedPosition **FEED_FRONT** = `1`

Camera is mounted at the front of the device.

FeedPosition **FEED_BACK** = `2`

Camera is mounted at the back of the device.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **feed_is_active** = `false`

-  **set_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_active**()

If `true`, the feed is active.

---

[Transform2D](class_transform2d.md#class-transform2d) **feed_transform** = `Transform2D(1, 0, 0, -1, 0, 1)`

-  **set_transform**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_transform**()

The transform applied to the camera's image.

---

[Array](class_array.md#class-array) **formats** = `[]`

- [Array](class_array.md#class-array) **get_formats**()

Formats supported by the feed. Each entry is a [Dictionary](class_dictionary.md#class-dictionary) describing format parameters.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **\_activate_feed**()

Called when the camera feed is activated.

---

 **\_deactivate_feed**()

Called when the camera feed is deactivated.

---

[Array](class_array.md#class-array) **\_get_formats**()

Override this method to define supported formats of the camera feed.

---

[bool](class_bool.md#class-bool) **\_set_format**(index: [int](class_int.md#class-int), parameters: [Dictionary](class_dictionary.md#class-dictionary))

Override this method to set the format of the camera feed.

---

FeedDataType **get_datatype**()

Returns feed image data type.

---

[int](class_int.md#class-int) **get_id**()

Returns the unique ID for this feed.

---

[String](class_string.md#class-string) **get_name**()

Returns the camera's name.

---

FeedPosition **get_position**()

Returns the position of camera on the device.

---

[int](class_int.md#class-int) **get_texture_tex_id**(feed_image_type: [FeedImage](class_cameraserver.md#enum-cameraserver-feedimage))

Returns the texture backend ID (usable by some external libraries that need a handle to a texture to write data).

---

 **set_external**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int))

Sets the feed as external feed provided by another library.

---

[bool](class_bool.md#class-bool) **set_format**(index: [int](class_int.md#class-int), parameters: [Dictionary](class_dictionary.md#class-dictionary))

Sets the feed format parameters for the given `index` in the formats array. Returns `true` on success. By default, the YUYV encoded stream is transformed to FEED_RGB. The YUYV encoded stream output format can be changed by setting `parameters`'s `output` entry to one of the following:

- `"separate"` will result in FEED_YCBCR_SEP;
- `"grayscale"` will result in desaturated FEED_RGB;
- `"copy"` will result in FEED_YCBCR.

---

 **set_name**(name: [String](class_string.md#class-string))

Sets the camera's name.

---

 **set_position**(position: FeedPosition)

Sets the position of this camera.

---

 **set_rgb_image**(rgb_image: [Image](class_image.md#class-image))

Sets RGB image for this feed.

---

 **set_ycbcr_image**(ycbcr_image: [Image](class_image.md#class-image))

Sets YCbCr image for this feed.

---

 **set_ycbcr_images**(y_image: [Image](class_image.md#class-image), cbcr_image: [Image](class_image.md#class-image))

Sets Y and CbCr images for this feed.
