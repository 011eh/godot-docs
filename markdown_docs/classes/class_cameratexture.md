# CameraTexture

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture provided by a [CameraFeed](class_camerafeed.md#class-camerafeed).

## Description

This texture gives access to the camera texture provided by a [CameraFeed](class_camerafeed.md#class-camerafeed).

**Note:** Many cameras supply YCbCr images which need to be converted in a shader.

## Properties

| [int](class_int.md#class-int)                                  | camera_feed_id     | `0`                                                                                               |
|----------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                               | camera_is_active | `false`                                                                                           |
| [bool](class_bool.md#class-bool)                               | resource_local_to_scene                                            | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [FeedImage](class_cameraserver.md#enum-cameraserver-feedimage) | which_feed             | `0`                                                                                               |

---

## Property Descriptions

[int](class_int.md#class-int) **camera_feed_id** = `0`

-  **set_camera_feed_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_camera_feed_id**()

The ID of the [CameraFeed](class_camerafeed.md#class-camerafeed) for which we want to display the image.

---

[bool](class_bool.md#class-bool) **camera_is_active** = `false`

-  **set_camera_active**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_camera_active**()

Convenience property that gives access to the active property of the [CameraFeed](class_camerafeed.md#class-camerafeed).

---

[FeedImage](class_cameraserver.md#enum-cameraserver-feedimage) **which_feed** = `0`

-  **set_which_feed**(value: [FeedImage](class_cameraserver.md#enum-cameraserver-feedimage))
- [FeedImage](class_cameraserver.md#enum-cameraserver-feedimage) **get_which_feed**()

Which image within the [CameraFeed](class_camerafeed.md#class-camerafeed) we want access to, important if the camera image is split in a Y and CbCr component.
