# StyleBoxTexture

**Inherits:** [StyleBox](class_stylebox.md#class-stylebox) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A texture-based nine-patch [StyleBox](class_stylebox.md#class-stylebox).

## Description

A texture-based nine-patch [StyleBox](class_stylebox.md#class-stylebox), in a way similar to [NinePatchRect](class_ninepatchrect.md#class-ninepatchrect). This stylebox performs a 3×3 scaling of a texture, where only the center cell is fully stretched. This makes it possible to design bordered styles regardless of the stylebox's size.

## Properties

| AxisStretchMode   | axis_stretch_horizontal   | `0`                 |
|------------------------------------------------------------|--------------------------------------------------------------------------------------|---------------------|
| AxisStretchMode   | axis_stretch_vertical       | `0`                 |
| [bool](class_bool.md#class-bool)                           | draw_center                           | `true`              |
| [float](class_float.md#class-float)                        | expand_margin_bottom         | `0.0`               |
| [float](class_float.md#class-float)                        | expand_margin_left             | `0.0`               |
| [float](class_float.md#class-float)                        | expand_margin_right           | `0.0`               |
| [float](class_float.md#class-float)                        | expand_margin_top               | `0.0`               |
| [Color](class_color.md#class-color)                        | modulate_color                     | `Color(1, 1, 1, 1)` |
| [Rect2](class_rect2.md#class-rect2)                        | region_rect                           | `Rect2(0, 0, 0, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d)            | texture                                   |                     |
| [float](class_float.md#class-float)                        | texture_margin_bottom       | `0.0`               |
| [float](class_float.md#class-float)                        | texture_margin_left           | `0.0`               |
| [float](class_float.md#class-float)                        | texture_margin_right         | `0.0`               |
| [float](class_float.md#class-float)                        | texture_margin_top             | `0.0`               |

## Methods

| [float](class_float.md#class-float)   | get_expand_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                              |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float)   | get_texture_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                            |
|                                       | set_expand_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))   |
|                                       | set_expand_margin_all(size: [float](class_float.md#class-float))                                                        |
|                                       | set_texture_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float)) |
|                                       | set_texture_margin_all(size: [float](class_float.md#class-float))                                                      |

---

## Enumerations

enum **AxisStretchMode**:

AxisStretchMode **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretch the stylebox's texture. This results in visible distortion unless the texture size matches the stylebox's size perfectly.

AxisStretchMode **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the stylebox's texture to match the stylebox's size according to the nine-patch system.

AxisStretchMode **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the stylebox's texture to match the stylebox's size according to the nine-patch system. Unlike AXIS_STRETCH_MODE_TILE, the texture may be slightly stretched to make the nine-patch texture tile seamlessly.

---

## Property Descriptions

AxisStretchMode **axis_stretch_horizontal** = `0`

-  **set_h_axis_stretch_mode**(value: AxisStretchMode)
- AxisStretchMode **get_h_axis_stretch_mode**()

Controls how the stylebox's texture will be stretched or tiled horizontally.

---

AxisStretchMode **axis_stretch_vertical** = `0`

-  **set_v_axis_stretch_mode**(value: AxisStretchMode)
- AxisStretchMode **get_v_axis_stretch_mode**()

Controls how the stylebox's texture will be stretched or tiled vertically.

---

[bool](class_bool.md#class-bool) **draw_center** = `true`

-  **set_draw_center**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_center_enabled**()

If `true`, the nine-patch texture's center tile will be drawn.

---

[float](class_float.md#class-float) **expand_margin_bottom** = `0.0`

-  **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Expands the bottom margin of this style box when drawing, causing it to be drawn larger than requested.

---

[float](class_float.md#class-float) **expand_margin_left** = `0.0`

-  **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Expands the left margin of this style box when drawing, causing it to be drawn larger than requested.

---

[float](class_float.md#class-float) **expand_margin_right** = `0.0`

-  **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Expands the right margin of this style box when drawing, causing it to be drawn larger than requested.

---

[float](class_float.md#class-float) **expand_margin_top** = `0.0`

-  **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Expands the top margin of this style box when drawing, causing it to be drawn larger than requested.

---

[Color](class_color.md#class-color) **modulate_color** = `Color(1, 1, 1, 1)`

-  **set_modulate**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_modulate**()

Modulates the color of the texture when this style box is drawn.

---

[Rect2](class_rect2.md#class-rect2) **region_rect** = `Rect2(0, 0, 0, 0)`

-  **set_region_rect**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_region_rect**()

The region to use from the texture.

This is equivalent to first wrapping the texture in an [AtlasTexture](class_atlastexture.md#class-atlastexture) with the same region.

If empty (`Rect2(0, 0, 0, 0)`), the whole texture is used.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The texture to use when drawing this style box.

---

[float](class_float.md#class-float) **texture_margin_bottom** = `0.0`

-  **set_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Increases the bottom margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the bottom border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_bottom](class_stylebox.md#class-stylebox-property-content-margin-bottom) if it is negative.

---

[float](class_float.md#class-float) **texture_margin_left** = `0.0`

-  **set_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Increases the left margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the left border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_left](class_stylebox.md#class-stylebox-property-content-margin-left) if it is negative.

---

[float](class_float.md#class-float) **texture_margin_right** = `0.0`

-  **set_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Increases the right margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the right border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_right](class_stylebox.md#class-stylebox-property-content-margin-right) if it is negative.

---

[float](class_float.md#class-float) **texture_margin_top** = `0.0`

-  **set_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

Increases the top margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the top border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_top](class_stylebox.md#class-stylebox-property-content-margin-top) if it is negative.

---

## Method Descriptions

[float](class_float.md#class-float) **get_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the expand margin size of the specified [Side](class_@globalscope.md#enum-globalscope-side).

---

[float](class_float.md#class-float) **get_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the margin size of the specified [Side](class_@globalscope.md#enum-globalscope-side).

---

 **set_expand_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))

Sets the expand margin to `size` pixels for the specified [Side](class_@globalscope.md#enum-globalscope-side).

---

 **set_expand_margin_all**(size: [float](class_float.md#class-float))

Sets the expand margin to `size` pixels for all sides.

---

 **set_texture_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), size: [float](class_float.md#class-float))

Sets the margin to `size` pixels for the specified [Side](class_@globalscope.md#enum-globalscope-side).

---

 **set_texture_margin_all**(size: [float](class_float.md#class-float))

Sets the margin to `size` pixels for all sides.
