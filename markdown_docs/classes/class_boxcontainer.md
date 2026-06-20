# BoxContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer), [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer)

A container that arranges its child controls horizontally or vertically.

## Description

A container that arranges its child controls horizontally or vertically, rearranging them automatically when their minimum size changes.

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

## Properties

| AlignmentMode   | alignment   | `0`     |
|-----------------------------------------------------|-------------------------------------------------------|---------|
| [bool](class_bool.md#class-bool)                    | vertical     | `false` |

## Methods

| [Control](class_control.md#class-control)   | add_spacer(begin: [bool](class_bool.md#class-bool))   |
|---------------------------------------------|------------------------------------------------------------------------------------------------|

## Theme Properties

| [int](class_int.md#class-int)   | separation   | `4`   |
|---------------------------------|---------------------------------------------------------------|-------|

---

## Enumerations

enum **AlignmentMode**:

AlignmentMode **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container, i.e. top if orientation is vertical, left if orientation is horizontal (right for RTL layout).

AlignmentMode **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.

AlignmentMode **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e. bottom if orientation is vertical, right if orientation is horizontal (left for RTL layout).

---

## Property Descriptions

AlignmentMode **alignment** = `0`

-  **set_alignment**(value: AlignmentMode)
- AlignmentMode **get_alignment**()

The alignment of the container's children (must be one of ALIGNMENT_BEGIN, ALIGNMENT_CENTER, or ALIGNMENT_END).

---

[bool](class_bool.md#class-bool) **vertical** = `false`

-  **set_vertical**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_vertical**()

If `true`, the **BoxContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) and [VBoxContainer](class_vboxcontainer.md#class-vboxcontainer).

---

## Method Descriptions

[Control](class_control.md#class-control) **add_spacer**(begin: [bool](class_bool.md#class-bool))

Adds a [Control](class_control.md#class-control) node to the box as a spacer. If `begin` is `true`, it will insert the [Control](class_control.md#class-control) node in front of all other children.

---

## Theme Property Descriptions

[int](class_int.md#class-int) **separation** = `4`

The space between the **BoxContainer**'s elements, in pixels.
