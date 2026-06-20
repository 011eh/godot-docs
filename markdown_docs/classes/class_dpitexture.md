# DPITexture

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Texture2D](class_texture2d.md#class-texture2d) **<** [Texture](class_texture.md#class-texture) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An automatically scalable [Texture2D](class_texture2d.md#class-texture2d) based on an SVG image.

## Description

An automatically scalable [Texture2D](class_texture2d.md#class-texture2d) based on an SVG image. **DPITexture**s are used to automatically re-rasterize icons and other texture based UI theme elements to match viewport scale and font oversampling. See also [ProjectSettings.display/window/stretch/mode](class_projectsettings.md#class-projectsettings-property-display-window-stretch-mode) ("canvas_items" mode) and [Viewport.oversampling_override](class_viewport.md#class-viewport-property-oversampling-override).

## Properties

| [float](class_float.md#class-float)                | base_scale             | `1.0`                                                                                             |
|----------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [Dictionary](class_dictionary.md#class-dictionary) | color_map               | `{}`                                                                                              |
| [bool](class_bool.md#class-bool)                   | fix_alpha_border | `false`                                                                                           |
| [bool](class_bool.md#class-bool)                   | premult_alpha       | `false`                                                                                           |
| [bool](class_bool.md#class-bool)                   | resource_local_to_scene                                         | `false` (overrides [Resource](class_resource.md#class-resource-property-resource-local-to-scene)) |
| [float](class_float.md#class-float)                | saturation             | `1.0`                                                                                             |

## Methods

| DPITexture        | create_from_string(source: [String](class_string.md#class-string), scale: [float](class_float.md#class-float) = 1.0, saturation: [float](class_float.md#class-float) = 1.0, color_map: [Dictionary](class_dictionary.md#class-dictionary) = {})    |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)          | get_scaled_rid()                                                                                                                                                                                                                                       |
| [String](class_string.md#class-string) | get_source()                                                                                                                                                                                                                                               |
|                                        | set_size_override(size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                               |
|                                        | set_source(source: [String](class_string.md#class-string))                                                                                                                                                                                                 |

---

## Property Descriptions

[float](class_float.md#class-float) **base_scale** = `1.0`

-  **set_base_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_base_scale**()

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.

---

[Dictionary](class_dictionary.md#class-dictionary) **color_map** = `{}`

-  **set_color_map**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_color_map**()

If set, remaps texture colors according to [Color](class_color.md#class-color)-[Color](class_color.md#class-color) map.

---

[bool](class_bool.md#class-bool) **fix_alpha_border** = `false`

-  **set_fix_alpha_border**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_fix_alpha_border**()

If `true`, puts pixels of the same surrounding color in transition from transparent to opaque areas. For textures displayed with bilinear filtering, this helps to reduce the outline effect when exporting images from an image editor.

---

[bool](class_bool.md#class-bool) **premult_alpha** = `false`

-  **set_premult_alpha**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_premult_alpha**()

An alternative to fixing darkened borders with fix_alpha_border is to use premultiplied alpha. By enabling this option, the texture will be converted to this format. A premultiplied alpha texture requires specific materials to be displayed correctly:

- In 2D, a [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial) will need to be created and configured to use the [CanvasItemMaterial.BLEND_MODE_PREMULT_ALPHA](class_canvasitemmaterial.md#class-canvasitemmaterial-constant-blend-mode-premult-alpha) blend mode on [CanvasItem](class_canvasitem.md#class-canvasitem)s that use this texture. In custom `canvas_item` shaders, `render_mode blend_premul_alpha;` should be used.
- In 3D, a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d) will need to be created and configured to use the [BaseMaterial3D.BLEND_MODE_PREMULT_ALPHA](class_basematerial3d.md#class-basematerial3d-constant-blend-mode-premult-alpha) blend mode on materials that use this texture. In custom `spatial` shaders, `render_mode blend_premul_alpha;` should be used.

---

[float](class_float.md#class-float) **saturation** = `1.0`

-  **set_saturation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_saturation**()

Overrides texture saturation.

---

## Method Descriptions

DPITexture **create_from_string**(source: [String](class_string.md#class-string), scale: [float](class_float.md#class-float) = 1.0, saturation: [float](class_float.md#class-float) = 1.0, color_map: [Dictionary](class_dictionary.md#class-dictionary) = {})

Creates a new **DPITexture** and initializes it by allocating and setting the SVG data to `source`.

---

[RID](class_rid.md#class-rid) **get_scaled_rid**()

Returns the [RID](class_rid.md#class-rid) of the texture rasterized to match the oversampling of the currently drawn canvas item.

---

[String](class_string.md#class-string) **get_source**()

Returns this SVG texture's source code.

---

 **set_size_override**(size: [Vector2i](class_vector2i.md#class-vector2i))

Resizes the texture to the specified dimensions.

---

 **set_source**(source: [String](class_string.md#class-string))

Sets this SVG texture's source code.
