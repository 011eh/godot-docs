# TextureRect

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A control that displays a texture.

## Description

A control that displays a texture, for example an icon inside a GUI. The texture's placement can be controlled with the stretch_mode property. It can scale, tile, or stay centered inside its bounding rectangle.

## Tutorials

- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

## Properties

| ExpandMode               | expand_mode   | `0`                                                                             |
|----------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                         | flip_h             | `false`                                                                         |
| [bool](class_bool.md#class-bool)                         | flip_v             | `false`                                                                         |
| [MouseFilter](class_control.md#enum-control-mousefilter) | mouse_filter                                             | `1` (overrides [Control](class_control.md#class-control-property-mouse-filter)) |
| StretchMode             | stretch_mode | `0`                                                                             |
| [Texture2D](class_texture2d.md#class-texture2d)          | texture           |                                                                                 |

---

## Enumerations

enum **ExpandMode**:

ExpandMode **EXPAND_KEEP_SIZE** = `0`

The minimum size will be equal to texture size, i.e. **TextureRect** can't be smaller than the texture.

ExpandMode **EXPAND_IGNORE_SIZE** = `1`

The size of the texture won't be considered for minimum size calculation, so the **TextureRect** can be shrunk down past the texture size.

ExpandMode **EXPAND_FIT_WIDTH** = `2`

The height of the texture will be ignored. Minimum width will be equal to the current height. Useful for horizontal layouts, e.g. inside [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer).

ExpandMode **EXPAND_FIT_WIDTH_PROPORTIONAL** = `3`

Same as EXPAND_FIT_WIDTH, but keeps texture's aspect ratio.

ExpandMode **EXPAND_FIT_HEIGHT** = `4`

The width of the texture will be ignored. Minimum height will be equal to the current width. Useful for vertical layouts, e.g. inside [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer).

ExpandMode **EXPAND_FIT_HEIGHT_PROPORTIONAL** = `5`

Same as EXPAND_FIT_HEIGHT, but keeps texture's aspect ratio.

---

enum **StretchMode**:

StretchMode **STRETCH_SCALE** = `0`

Scale to fit the node's bounding rectangle.

StretchMode **STRETCH_TILE** = `1`

Tile inside the node's bounding rectangle.

**Note:** STRETCH_TILE mode is not supported for texture set to an [AtlasTexture](class_atlastexture.md#class-atlastexture) with non-zero [AtlasTexture.margin](class_atlastexture.md#class-atlastexture-property-margin).

StretchMode **STRETCH_KEEP** = `2`

The texture keeps its original size and stays in the bounding rectangle's top-left corner.

StretchMode **STRETCH_KEEP_CENTERED** = `3`

The texture keeps its original size and stays centered in the node's bounding rectangle.

StretchMode **STRETCH_KEEP_ASPECT** = `4`

Scale the texture to fit the node's bounding rectangle, but maintain the texture's aspect ratio.

StretchMode **STRETCH_KEEP_ASPECT_CENTERED** = `5`

Scale the texture to fit the node's bounding rectangle, center it and maintain its aspect ratio.

StretchMode **STRETCH_KEEP_ASPECT_COVERED** = `6`

Scale the texture so that the shorter side fits the bounding rectangle. The other side clips to the node's limits.

---

## Property Descriptions

ExpandMode **expand_mode** = `0`

-  **set_expand_mode**(value: ExpandMode)
- ExpandMode **get_expand_mode**()

**Experimental:** Using EXPAND_FIT_WIDTH, EXPAND_FIT_WIDTH_PROPORTIONAL, EXPAND_FIT_HEIGHT, or EXPAND_FIT_HEIGHT_PROPORTIONAL may result in unstable behavior in some [Container](class_container.md#class-container) controls. This behavior may be re-evaluated and changed in the future.

Defines how minimum size is determined based on the texture's size.

---

[bool](class_bool.md#class-bool) **flip_h** = `false`

-  **set_flip_h**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_h**()

If `true`, texture is flipped horizontally.

---

[bool](class_bool.md#class-bool) **flip_v** = `false`

-  **set_flip_v**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_flipped_v**()

If `true`, texture is flipped vertically.

---

StretchMode **stretch_mode** = `0`

-  **set_stretch_mode**(value: StretchMode)
- StretchMode **get_stretch_mode**()

Controls the texture's behavior when resizing the node's bounding rectangle.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The node's [Texture2D](class_texture2d.md#class-texture2d) resource.
