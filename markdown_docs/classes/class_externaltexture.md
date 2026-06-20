# ExternalTexture

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Texture which displays the content of an external buffer.

## Description

Displays the content of an external buffer provided by the platform.

Requires the [OES_EGL_image_external](https://registry.khronos.org/OpenGL/extensions/OES/OES_EGL_image_external.txt) extension (OpenGL) or [VK_ANDROID_external_memory_android_hardware_buffer](https://registry.khronos.org/vulkan/specs/1.1-extensions/html/vkspec.html#VK_ANDROID_external_memory_android_hardware_buffer) extension (Vulkan).

**Note:** This is currently only supported in Android builds.

## Properties

| [bool](class_bool.md#class-bool)          | resource_local_to_scene                      | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene))   |
|-------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Vector2](class_vector2.md#class-vector2) | size | `Vector2(256, 256)`                                                                                 |

## Methods

| [int](class_int.md#class-int)   | get_external_texture_id()                                                |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|                                 | set_external_buffer_id(external_buffer_id: [int](class_int.md#class-int)) |

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **size** = `Vector2(256, 256)`

-  **set_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_size**()

External texture size.

---

## Method Descriptions

[int](class_int.md#class-int) **get_external_texture_id**()

Returns the external texture ID.

Depending on your use case, you may need to pass this to platform APIs, for example, when creating an `android.graphics.SurfaceTexture` on Android.

---

 **set_external_buffer_id**(external_buffer_id: [int](class_int.md#class-int))

Sets the external buffer ID.

Depending on your use case, you may need to call this with data received from a platform API, for example, `SurfaceTexture.getHardwareBuffer()` on Android.
