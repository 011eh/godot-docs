# PointLight2D

**Inherits:** [Light2D](class_light2d.md#class-light2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Positional 2D light source.

## Description

Casts light in a 2D environment. This light's shape is defined by a (usually grayscale) texture.

## Tutorials

- [2D lights and shadows](../tutorials/2d/2d_lights_and_shadows.md)

## Properties

| [float](class_float.md#class-float)             | height               | `0.0`           |
|-------------------------------------------------|-------------------------------------------------------------|-----------------|
| [Vector2](class_vector2.md#class-vector2)       | offset               | `Vector2(0, 0)` |
| [Texture2D](class_texture2d.md#class-texture2d) | texture             |                 |
| [float](class_float.md#class-float)             | texture_scale | `1.0`           |

---

## Property Descriptions

[float](class_float.md#class-float) **height** = `0.0`

-  **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The height of the light. Used with 2D normal mapping. The units are in pixels, e.g. if the height is 100, then it will illuminate an object 100 pixels away at a 45° angle to the plane.

---

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)`

-  **set_texture_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_texture_offset**()

The offset of the light's texture.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

[Texture2D](class_texture2d.md#class-texture2d) used for the light's appearance.

---

[float](class_float.md#class-float) **texture_scale** = `1.0`

-  **set_texture_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_scale**()

The texture's scale factor.
