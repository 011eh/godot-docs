# CharFXTransform

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Controls how an individual character will be displayed in a [RichTextEffect](class_richtexteffect.md#class-richtexteffect).

## Description

By setting various properties on this object, you can control how individual characters will be displayed in a [RichTextEffect](class_richtexteffect.md#class-richtexteffect).

## Tutorials

- [BBCode in RichTextLabel](../tutorials/ui/bbcode_in_richtextlabel.md)

## Properties

| [Color](class_color.md#class-color)                   | color                   | `Color(0, 0, 0, 1)`             |
|-------------------------------------------------------|------------------------------------------------------------------|---------------------------------|
| [float](class_float.md#class-float)                   | elapsed_time     | `0.0`                           |
| [Dictionary](class_dictionary.md#class-dictionary)    | env                       | `{}`                            |
| [RID](class_rid.md#class-rid)                         | font                     | `RID()`                         |
| [int](class_int.md#class-int)                         | glyph_count       | `0`                             |
| [int](class_int.md#class-int)                         | glyph_flags       | `0`                             |
| [int](class_int.md#class-int)                         | glyph_index       | `0`                             |
| [Vector2](class_vector2.md#class-vector2)             | offset                 | `Vector2(0, 0)`                 |
| [bool](class_bool.md#class-bool)                      | outline               | `false`                         |
| [Vector2i](class_vector2i.md#class-vector2i)          | range                   | `Vector2i(0, 0)`                |
| [int](class_int.md#class-int)                         | relative_index | `0`                             |
| [Transform2D](class_transform2d.md#class-transform2d) | transform           | `Transform2D(1, 0, 0, 1, 0, 0)` |
| [bool](class_bool.md#class-bool)                      | visible               | `true`                          |

---

## Property Descriptions

[Color](class_color.md#class-color) **color** = `Color(0, 0, 0, 1)`

-  **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The color the character will be drawn with.

---

[float](class_float.md#class-float) **elapsed_time** = `0.0`

-  **set_elapsed_time**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_elapsed_time**()

The time elapsed since the [RichTextLabel](class_richtextlabel.md#class-richtextlabel) was added to the scene tree (in seconds). Time stops when the [RichTextLabel](class_richtextlabel.md#class-richtextlabel) is paused (see [Node.process_mode](class_node.md#class-node-property-process-mode)). Resets when the text in the [RichTextLabel](class_richtextlabel.md#class-richtextlabel) is changed.

**Note:** Time still passes while the [RichTextLabel](class_richtextlabel.md#class-richtextlabel) is hidden.

---

[Dictionary](class_dictionary.md#class-dictionary) **env** = `{}`

-  **set_environment**(value: [Dictionary](class_dictionary.md#class-dictionary))
- [Dictionary](class_dictionary.md#class-dictionary) **get_environment**()

Contains the arguments passed in the opening BBCode tag. By default, arguments are strings; if their contents match a type such as [bool](class_bool.md#class-bool), [int](class_int.md#class-int) or [float](class_float.md#class-float), they will be converted automatically. Color codes in the form `#rrggbb` or `#rgb` will be converted to an opaque [Color](class_color.md#class-color). String arguments may not contain spaces, even if they're quoted. If present, quotes will also be present in the final string.

For example, the opening BBCode tag `[example foo=hello bar=true baz=42 color=#ffffff]` will map to the following [Dictionary](class_dictionary.md#class-dictionary):

```gdscript
{"foo": "hello", "bar": true, "baz": 42, "color": Color(1, 1, 1, 1)}
```

---

[RID](class_rid.md#class-rid) **font** = `RID()`

-  **set_font**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_font**()

[TextServer](class_textserver.md#class-textserver) RID of the font used to render glyph, this value can be used with `TextServer.font_*` methods to retrieve font information.

**Note:** Read-only. Setting this property won't affect drawing.

---

[int](class_int.md#class-int) **glyph_count** = `0`

-  **set_glyph_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_glyph_count**()

Number of glyphs in the grapheme cluster. This value is set in the first glyph of a cluster.

**Note:** Read-only. Setting this property won't affect drawing.

---

[int](class_int.md#class-int) **glyph_flags** = `0`

-  **set_glyph_flags**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_glyph_flags**()

Glyph flags. See [GraphemeFlag](class_textserver.md#enum-textserver-graphemeflag) for more info.

**Note:** Read-only. Setting this property won't affect drawing.

---

[int](class_int.md#class-int) **glyph_index** = `0`

-  **set_glyph_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_glyph_index**()

Glyph index specific to the font. If you want to replace this glyph, use [TextServer.font_get_glyph_index()](class_textserver.md#class-textserver-method-font-get-glyph-index) with font to get a new glyph index for a single character.

---

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)`

-  **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The position offset the character will be drawn with (in pixels).

---

[bool](class_bool.md#class-bool) **outline** = `false`

-  **set_outline**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_outline**()

If `true`, FX transform is called for outline drawing.

**Note:** Read-only. Setting this property won't affect drawing.

---

[Vector2i](class_vector2i.md#class-vector2i) **range** = `Vector2i(0, 0)`

-  **set_range**(value: [Vector2i](class_vector2i.md#class-vector2i))
- [Vector2i](class_vector2i.md#class-vector2i) **get_range**()

Absolute character range in the string, corresponding to the glyph.

**Note:** Read-only. Setting this property won't affect drawing.

---

[int](class_int.md#class-int) **relative_index** = `0`

-  **set_relative_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_relative_index**()

The character offset of the glyph, relative to the current [RichTextEffect](class_richtexteffect.md#class-richtexteffect) custom block.

**Note:** Read-only. Setting this property won't affect drawing.

---

[Transform2D](class_transform2d.md#class-transform2d) **transform** = `Transform2D(1, 0, 0, 1, 0, 0)`

-  **set_transform**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_transform**()

The current transform of the current glyph. It can be overridden (for example, by driving the position and rotation from a curve). You can also alter the existing value to apply transforms on top of other effects.

---

[bool](class_bool.md#class-bool) **visible** = `true`

-  **set_visibility**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visible**()

If `true`, the character will be drawn. If `false`, the character will be hidden. Characters around hidden characters will reflow to take the space of hidden characters. If this is not desired, set their color to `Color(1, 1, 1, 0)` instead.
