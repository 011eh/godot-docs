# NinePatchRect

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control that displays a texture by keeping its corners intact, but tiling its edges and center.

## Description

Also known as 9-slice panels, **NinePatchRect** produces clean panels of any size based on a small texture. To do so, it splits the texture in a 3×3 grid. When you scale the node, it tiles the texture's edges horizontally or vertically, tiles the center on both axes, and leaves the corners unchanged.

## Properties

| AxisStretchMode   | axis_stretch_horizontal   | `0`                                                                             |
|----------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| AxisStretchMode   | axis_stretch_vertical       | `0`                                                                             |
| [bool](class_bool.md#class-bool)                         | draw_center                           | `true`                                                                          |
| [MouseFilter](class_control.md#enum-control-mousefilter) | mouse_filter                                                                       | `2` (overrides [Control](class_control.md#class-control-property-mouse-filter)) |
| [int](class_int.md#class-int)                            | patch_margin_bottom           | `0`                                                                             |
| [int](class_int.md#class-int)                            | patch_margin_left               | `0`                                                                             |
| [int](class_int.md#class-int)                            | patch_margin_right             | `0`                                                                             |
| [int](class_int.md#class-int)                            | patch_margin_top                 | `0`                                                                             |
| [Rect2](class_rect2.md#class-rect2)                      | region_rect                           | `Rect2(0, 0, 0, 0)`                                                             |
| [Texture2D](class_texture2d.md#class-texture2d)          | texture                                   |                                                                                 |

## Methods

| [int](class_int.md#class-int)   | get_patch_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                       |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                 | set_patch_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side), value: [int](class_int.md#class-int)) |

---

## Signals

**texture_changed**()

Emitted when the node's texture changes.

---

## Enumerations

enum **AxisStretchMode**:

AxisStretchMode **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretches the center texture across the NinePatchRect. This may cause the texture to be distorted.

AxisStretchMode **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the center texture across the NinePatchRect. This won't cause any visible distortion. The texture must be seamless for this to work without displaying artifacts between edges.

AxisStretchMode **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the center texture across the NinePatchRect, but will also stretch the texture to make sure each tile is visible in full. This may cause the texture to be distorted, but less than AXIS_STRETCH_MODE_STRETCH. The texture must be seamless for this to work without displaying artifacts between edges.

---

## Property Descriptions

AxisStretchMode **axis_stretch_horizontal** = `0`

-  **set_h_axis_stretch_mode**(value: AxisStretchMode)
- AxisStretchMode **get_h_axis_stretch_mode**()

The stretch mode to use for horizontal stretching/tiling.

---

AxisStretchMode **axis_stretch_vertical** = `0`

-  **set_v_axis_stretch_mode**(value: AxisStretchMode)
- AxisStretchMode **get_v_axis_stretch_mode**()

The stretch mode to use for vertical stretching/tiling.

---

[bool](class_bool.md#class-bool) **draw_center** = `true`

-  **set_draw_center**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_draw_center_enabled**()

If `true`, draw the panel's center. Else, only draw the 9-slice's borders.

---

[int](class_int.md#class-int) **patch_margin_bottom** = `0`

-  **set_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

The height of the 9-slice's bottom row. A margin of 16 means the 9-slice's bottom corners and side will have a height of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.

---

[int](class_int.md#class-int) **patch_margin_left** = `0`

-  **set_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

The width of the 9-slice's left column. A margin of 16 means the 9-slice's left corners and side will have a width of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.

---

[int](class_int.md#class-int) **patch_margin_right** = `0`

-  **set_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

The width of the 9-slice's right column. A margin of 16 means the 9-slice's right corners and side will have a width of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.

---

[int](class_int.md#class-int) **patch_margin_top** = `0`

-  **set_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

The height of the 9-slice's top row. A margin of 16 means the 9-slice's top corners and side will have a height of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.

---

[Rect2](class_rect2.md#class-rect2) **region_rect** = `Rect2(0, 0, 0, 0)`

-  **set_region_rect**(value: [Rect2](class_rect2.md#class-rect2))
- [Rect2](class_rect2.md#class-rect2) **get_region_rect**()

Rectangular region of the texture to sample from. If you're working with an atlas, use this property to define the area the 9-slice should use. All other properties are relative to this one. If the rect is empty, NinePatchRect will use the whole texture.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The node's texture resource.

---

## Method Descriptions

[int](class_int.md#class-int) **get_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the size of the margin on the specified [Side](class_@globalscope.md#enum-globalscope-side).

---

 **set_patch_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), value: [int](class_int.md#class-int))

Sets the size of the margin on the specified [Side](class_@globalscope.md#enum-globalscope-side) to `value` pixels.
