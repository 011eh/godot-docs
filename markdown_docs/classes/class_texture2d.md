# Texture2D

**Inherits:** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AnimatedTexture](class_animatedtexture.md#class-animatedtexture), [AtlasTexture](class_atlastexture.md#class-atlastexture), [CameraTexture](class_cameratexture.md#class-cameratexture), [CanvasTexture](class_canvastexture.md#class-canvastexture), [CompressedTexture2D](class_compressedtexture2d.md#class-compressedtexture2d), [CurveTexture](class_curvetexture.md#class-curvetexture), [CurveXYZTexture](class_curvexyztexture.md#class-curvexyztexture), [DPITexture](class_dpitexture.md#class-dpitexture), [DrawableTexture2D](class_drawabletexture2d.md#class-drawabletexture2d), [ExternalTexture](class_externaltexture.md#class-externaltexture), [GradientTexture1D](class_gradienttexture1d.md#class-gradienttexture1d), [GradientTexture2D](class_gradienttexture2d.md#class-gradienttexture2d), [ImageTexture](class_imagetexture.md#class-imagetexture), [MeshTexture](class_meshtexture.md#class-meshtexture), [NoiseTexture2D](class_noisetexture2d.md#class-noisetexture2d), [PlaceholderTexture2D](class_placeholdertexture2d.md#class-placeholdertexture2d), [PortableCompressedTexture2D](class_portablecompressedtexture2d.md#class-portablecompressedtexture2d), [Texture2DRD](class_texture2drd.md#class-texture2drd), [ViewportTexture](class_viewporttexture.md#class-viewporttexture)

Texture for 2D and 3D.

## Description

A texture works by registering an image in the video hardware, which then can be used in 3D models or 2D [Sprite2D](class_sprite2d.md#class-sprite2d) or GUI [Control](class_control.md#class-control).

Textures are often created by loading them from a file. See [@GDScript.load()](class_@gdscript.md#class-gdscript-method-load).

**Texture2D** is a base for other resources. It cannot be used directly.

**Note:** The maximum texture size is 16384×16384 pixels due to graphics hardware limitations. Larger textures may fail to import.

## Methods

|                                              | \_draw(to_canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool))                                                                                                                                    |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                              | \_draw_rect(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool))                                                                                       |
|                                              | \_draw_rect_region(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool), clip_uv: [bool](class_bool.md#class-bool))                       |
| [Format](class_image.md#enum-image-format)   | \_get_format()                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                | \_get_height()                                                                                                                                                                                                                                                                                                                 |
| [Image](class_image.md#class-image)          | \_get_image()                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                | \_get_mipmap_count()                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                | \_get_width()                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)             | \_has_alpha()                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)             | \_has_mipmaps()                                                                                                                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)             | \_is_pixel_opaque(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int))                                                                                                                                                                                                                                     |
| [Resource](class_resource.md#class-resource) | create_placeholder()                                                                                                                                                                                                                                                                                                           |
|                                              | draw(canvas_item: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false)                                                                                                                |
|                                              | draw_rect(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false)                                                                        |
|                                              | draw_rect_region(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false, clip_uv: [bool](class_bool.md#class-bool) = true) |
| [Format](class_image.md#enum-image-format)   | get_format()                                                                                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                | get_height()                                                                                                                                                                                                                                                                                                                           |
| [Image](class_image.md#class-image)          | get_image()                                                                                                                                                                                                                                                                                                                             |
| [int](class_int.md#class-int)                | get_mipmap_count()                                                                                                                                                                                                                                                                                                               |
| [Vector2](class_vector2.md#class-vector2)    | get_size()                                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                | get_width()                                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)             | has_alpha()                                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)             | has_mipmaps()                                                                                                                                                                                                                                                                                                                         |

---

## Method Descriptions

 **\_draw**(to_canvas_item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool))

Called when the entire **Texture2D** is requested to be drawn over a [CanvasItem](class_canvasitem.md#class-canvasitem), with the top-left offset specified in `pos`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

---

 **\_draw_rect**(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool))

Called when the **Texture2D** is requested to be drawn onto [CanvasItem](class_canvasitem.md#class-canvasitem)'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

---

 **\_draw_rect_region**(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color), transpose: [bool](class_bool.md#class-bool), clip_uv: [bool](class_bool.md#class-bool))

Called when a part of the **Texture2D** specified by `src_rect`'s coordinates is requested to be drawn onto [CanvasItem](class_canvasitem.md#class-canvasitem)'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

---

[Format](class_image.md#enum-image-format) **\_get_format**()

Called when get_format() is called.

---

[int](class_int.md#class-int) **\_get_height**()

Called when the **Texture2D**'s height is queried.

---

[Image](class_image.md#class-image) **\_get_image**()

Called when get_image() is called.

---

[int](class_int.md#class-int) **\_get_mipmap_count**()

Called when get_mipmap_count() is called.

---

[int](class_int.md#class-int) **\_get_width**()

Called when the **Texture2D**'s width is queried.

---

[bool](class_bool.md#class-bool) **\_has_alpha**()

Called when the presence of an alpha channel in the **Texture2D** is queried.

---

[bool](class_bool.md#class-bool) **\_has_mipmaps**()

Called when has_mipmaps() is called.

---

[bool](class_bool.md#class-bool) **\_is_pixel_opaque**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int))

Called when a pixel's opaque state in the **Texture2D** is queried at the specified `(x, y)` position.

---

[Resource](class_resource.md#class-resource) **create_placeholder**()

Creates a placeholder version of this resource ([PlaceholderTexture2D](class_placeholdertexture2d.md#class-placeholdertexture2d)).

---

 **draw**(canvas_item: [RID](class_rid.md#class-rid), position: [Vector2](class_vector2.md#class-vector2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false)

Draws the texture using a [CanvasItem](class_canvasitem.md#class-canvasitem) with the [RenderingServer](class_renderingserver.md#class-renderingserver) API at the specified `position`.

---

 **draw_rect**(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), tile: [bool](class_bool.md#class-bool), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false)

Draws the texture using a [CanvasItem](class_canvasitem.md#class-canvasitem) with the [RenderingServer](class_renderingserver.md#class-renderingserver) API.

---

 **draw_rect_region**(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false, clip_uv: [bool](class_bool.md#class-bool) = true)

Draws a part of the texture using a [CanvasItem](class_canvasitem.md#class-canvasitem) with the [RenderingServer](class_renderingserver.md#class-renderingserver) API.

---

[Format](class_image.md#enum-image-format) **get_format**()

Returns the image format of the texture.

---

[int](class_int.md#class-int) **get_height**()

Returns the texture height in pixels.

---

[Image](class_image.md#class-image) **get_image**()

Returns an [Image](class_image.md#class-image) that is a copy of data from this **Texture2D** (a new [Image](class_image.md#class-image) is created each time). [Image](class_image.md#class-image)s can be accessed and manipulated directly.

**Note:** This will return `null` if this **Texture2D** is invalid.

**Note:** This will fetch the texture data from the GPU, which might cause performance problems when overused. Avoid calling get_image() every frame, especially on large textures.

---

[int](class_int.md#class-int) **get_mipmap_count**()

Returns the number of mipmaps of the texture.

---

[Vector2](class_vector2.md#class-vector2) **get_size**()

Returns the texture size in pixels.

---

[int](class_int.md#class-int) **get_width**()

Returns the texture width in pixels.

---

[bool](class_bool.md#class-bool) **has_alpha**()

Returns `true` if this **Texture2D** has an alpha channel.

---

[bool](class_bool.md#class-bool) **has_mipmaps**()

Returns `true` if the texture has mipmaps.
