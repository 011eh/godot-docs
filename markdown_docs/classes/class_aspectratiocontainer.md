# AspectRatioContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A container that preserves the proportions of its child controls.

## Description

A container type that arranges its child controls in a way that preserves their proportions automatically when the container is resized. Useful when a container has a dynamic size and the child nodes must adjust their sizes accordingly without losing their aspect ratios.

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

## Properties

| AlignmentMode   | alignment_horizontal   | `1`   |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------|-------|
| AlignmentMode   | alignment_vertical       | `1`   |
| [float](class_float.md#class-float)                         | ratio                                 | `1.0` |
| StretchMode       | stretch_mode                   | `2`   |

---

## Enumerations

enum **StretchMode**:

StretchMode **STRETCH_WIDTH_CONTROLS_HEIGHT** = `0`

The height of child controls is automatically adjusted based on the width of the container.

StretchMode **STRETCH_HEIGHT_CONTROLS_WIDTH** = `1`

The width of child controls is automatically adjusted based on the height of the container.

StretchMode **STRETCH_FIT** = `2`

The bounding rectangle of child controls is automatically adjusted to fit inside the container while keeping the aspect ratio.

StretchMode **STRETCH_COVER** = `3`

The width and height of child controls is automatically adjusted to make their bounding rectangle cover the entire area of the container while keeping the aspect ratio.

When the bounding rectangle of child controls exceed the container's size and [Control.clip_contents](class_control.md#class-control-property-clip-contents) is enabled, this allows to show only the container's area restricted by its own bounding rectangle.

---

enum **AlignmentMode**:

AlignmentMode **ALIGNMENT_BEGIN** = `0`

Aligns child controls with the beginning (left or top) of the container.

AlignmentMode **ALIGNMENT_CENTER** = `1`

Aligns child controls with the center of the container.

AlignmentMode **ALIGNMENT_END** = `2`

Aligns child controls with the end (right or bottom) of the container.

---

## Property Descriptions

AlignmentMode **alignment_horizontal** = `1`

-  **set_alignment_horizontal**(value: AlignmentMode)
- AlignmentMode **get_alignment_horizontal**()

Specifies the horizontal relative position of child controls.

---

AlignmentMode **alignment_vertical** = `1`

-  **set_alignment_vertical**(value: AlignmentMode)
- AlignmentMode **get_alignment_vertical**()

Specifies the vertical relative position of child controls.

---

[float](class_float.md#class-float) **ratio** = `1.0`

-  **set_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_ratio**()

The aspect ratio to enforce on child controls. This is the width divided by the height. The ratio depends on the stretch_mode.

---

StretchMode **stretch_mode** = `2`

-  **set_stretch_mode**(value: StretchMode)
- StretchMode **get_stretch_mode**()

The stretch mode used to align child controls.
