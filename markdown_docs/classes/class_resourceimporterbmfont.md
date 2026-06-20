# ResourceImporterBMFont

**Inherits:** [ResourceImporter](class_resourceimporter.md#class-resourceimporter) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Imports a bitmap font in the BMFont (`.fnt`) format.

## Description

The BMFont format is a format created by the [BMFont](https://www.angelcode.com/products/bmfont/) program. Many BMFont-compatible programs also exist, like [BMGlyph](https://www.bmglyph.com/).

Compared to [ResourceImporterImageFont](class_resourceimporterimagefont.md#class-resourceimporterimagefont), **ResourceImporterBMFont** supports bitmap fonts with varying glyph widths/heights.

See also [ResourceImporterDynamicFont](class_resourceimporterdynamicfont.md#class-resourceimporterdynamicfont).

## Tutorials

- [Bitmap fonts - Using fonts](../tutorials/ui/gui_using_fonts.html#bitmap-fonts)

## Properties

| [bool](class_bool.md#class-bool)    | compress         | `true`   |
|-------------------------------------|---------------------------------------------------------------------|----------|
| [Array](class_array.md#class-array) | fallbacks       | `[]`     |
| [int](class_int.md#class-int)       | scaling_mode | `2`      |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **compress** = `true`

If `true`, uses lossless compression for the resulting font.

---

[Array](class_array.md#class-array) **fallbacks** = `[]`

List of font fallbacks to use if a glyph isn't found in this bitmap font. Fonts at the beginning of the array are attempted first.

---

[int](class_int.md#class-int) **scaling_mode** = `2`

Font scaling mode.
