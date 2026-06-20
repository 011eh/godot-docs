# AtlasTexture

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A texture that crops out part of another Texture2D.

## Description

[Texture2D](class_texture2d.md#class-texture2d) resource that draws only part of its atlas texture, as defined by the region. An additional margin can also be set, which is useful for small adjustments.

Multiple **AtlasTexture** resources can be cropped from the same atlas. Packing many smaller textures into a singular large texture helps to optimize video memory costs and render calls.

**Note:** **AtlasTexture** cannot be used in an [AnimatedTexture](class_animatedtexture.md#class-animatedtexture), and will not tile properly in nodes such as [TextureRect](class_texturerect.md#class-texturerect) or [Sprite2D](class_sprite2d.md#class-sprite2d). To tile an **AtlasTexture**, modify its region instead.

## Properties

| [Texture2D](class_texture2d.md#class-texture2d)   | atlas             |                                                                                                   |
|---------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                  | filter_clip | `false`                                                                                           |
| [Rect2](class_rect2.md#class-rect2)               | margin           | `Rect2(0, 0, 0, 0)`                                                                               |
| [Rect2](class_rect2.md#class-rect2)               | region           | `Rect2(0, 0, 0, 0)`                                                                               |
| [bool](class_bool.md#class-bool)                  | resource_local_to_scene                                 | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |

---

## Property Descriptions

[Texture2D](class_texture2d.md#class-texture2d) **atlas**

-  **set_atlas**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_atlas**()

The texture that contains the atlas. Can be any type inheriting from [Texture2D](class_texture2d.md#class-texture2d), including another **AtlasTexture**.

---

[bool](class_bool.md#class-bool) **filter_clip** = `false`

-  **set_filter_clip**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **has_filter_clip**()

If `true`, the area outside of the region is clipped to avoid bleeding of the surrounding texture pixels.

---

[Rect2](class_rect2.md#class-rect2) **margin** = `Rect2(0, 0, 0, 0)`

-  **set_margin**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_margin**()

The margin around the region. Useful for small adjustments. If the [Rect2.size](class_rect2.md#class-rect2-property-size) of this property ("w" and "h" in the editor) is set, the drawn texture is resized to fit within the margin.

---

[Rect2](class_rect2.md#class-rect2) **region** = `Rect2(0, 0, 0, 0)`

-  **set_region**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_region**()

The region used to draw the atlas. If either dimension of the region's size is `0`, the value from atlas size will be used for that axis instead.

**Note:** The image size is always an integer, so the actual region size is rounded down.
