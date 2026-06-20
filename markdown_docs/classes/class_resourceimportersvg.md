# ResourceImporterSVG

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports an SVG file as an automatically scalable texture for use in UI elements and 2D rendering.

## Description

This importer imports [DPITexture](class_dpitexture.md#class-dpitexture) resources. See also [ResourceImporterTexture](class_resourceimportertexture.md#class-resourceimportertexture) and [ResourceImporterImage](class_resourceimporterimage.md#class-resourceimporterimage).

## Properties

| [float](class_float.md#class-float)                | base_scale             | `1.0`   |
|----------------------------------------------------|--------------------------------------------------------------------------|---------|
| [Dictionary](class_dictionary.md#class-dictionary) | color_map               | `{}`    |
| [bool](class_bool.md#class-bool)                   | compress                 | `true`  |
| [bool](class_bool.md#class-bool)                   | fix_alpha_border | `false` |
| [bool](class_bool.md#class-bool)                   | premult_alpha       | `false` |
| [float](class_float.md#class-float)                | saturation             | `1.0`   |

---

## Property Descriptions

[float](class_float.md#class-float) **base_scale** = `1.0`

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.

---

[Dictionary](class_dictionary.md#class-dictionary) **color_map** = `{}`

If set, remaps texture colors according to [Color](class_color.md#class-color)-[Color](class_color.md#class-color) map.

---

[bool](class_bool.md#class-bool) **compress** = `true`

If `true`, uses lossless compression for the SVG source.

---

[bool](class_bool.md#class-bool) **fix_alpha_border** = `false`

If `true`, puts pixels of the same surrounding color in transition from transparent to opaque areas. For textures displayed with bilinear filtering, this helps to reduce the outline effect when exporting images from an image editor.

---

[bool](class_bool.md#class-bool) **premult_alpha** = `false`

An alternative to fixing darkened borders with fix_alpha_border is to use premultiplied alpha. By enabling this option, the texture will be converted to this format. A premultiplied alpha texture requires specific materials to be displayed correctly:

- In 2D, a [CanvasItemMaterial](class_canvasitemmaterial.md#class-canvasitemmaterial) will need to be created and configured to use the [CanvasItemMaterial.BLEND_MODE_PREMULT_ALPHA](class_canvasitemmaterial.md#class-canvasitemmaterial-constant-blend-mode-premult-alpha) blend mode on [CanvasItem](class_canvasitem.md#class-canvasitem)s that use this texture. In custom `canvas_item` shaders, `render_mode blend_premul_alpha;` should be used.
- In 3D, a [BaseMaterial3D](class_basematerial3d.md#class-basematerial3d) will need to be created and configured to use the [BaseMaterial3D.BLEND_MODE_PREMULT_ALPHA](class_basematerial3d.md#class-basematerial3d-constant-blend-mode-premult-alpha) blend mode on materials that use this texture. In custom `spatial` shaders, `render_mode blend_premul_alpha;` should be used.

---

[float](class_float.md#class-float) **saturation** = `1.0`

Overrides texture saturation.
