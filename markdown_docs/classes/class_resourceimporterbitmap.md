# ResourceImporterBitMap

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports a [BitMap](class_bitmap.md#class-bitmap) resource (2D array of boolean values).

## Description

[BitMap](class_bitmap.md#class-bitmap) resources are typically used as click masks in [TextureButton](class_texturebutton.md#class-texturebutton) and [TouchScreenButton](class_touchscreenbutton.md#class-touchscreenbutton).

## Tutorials

- [Importing images](../tutorials/assets_pipeline/importing_images.md)

## Properties

| [int](class_int.md#class-int)       | create_from   | `0`   |
|-------------------------------------|---------------------------------------------------------------------|-------|
| [float](class_float.md#class-float) | threshold       | `0.5` |

---

## Property Descriptions

[int](class_int.md#class-int) **create_from** = `0`

The data source to use for generating the bitmap.

**Black & White:** Pixels whose HSV value is greater than the threshold will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

**Alpha:** Pixels whose alpha value is greater than the threshold will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

---

[float](class_float.md#class-float) **threshold** = `0.5`

The threshold to use to determine which bits should be considered enabled or disabled. See also create_from.
