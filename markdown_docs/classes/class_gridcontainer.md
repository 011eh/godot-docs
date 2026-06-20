# GridContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A container that arranges its child controls in a grid layout.

## Description

**GridContainer** arranges its child controls in a grid layout. The number of columns is specified by the columns property, whereas the number of rows depends on how many are needed for the child controls. The number of rows and columns is preserved for every size of the container.

**Note:** **GridContainer** only works with child nodes inheriting from [Control](class_control.md#class-control). It won't rearrange child nodes inheriting from [Node2D](class_node2d.md#class-node2d).

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)
- [Operating System Testing Demo](https://godotengine.org/asset-library/asset/2789)

## Properties

| [int](class_int.md#class-int)   | columns   | `1`   |
|---------------------------------|----------------------------------------------------|-------|

## Theme Properties

| [int](class_int.md#class-int)   | h_separation   | `4`   |
|---------------------------------|--------------------------------------------------------------------|-------|
| [int](class_int.md#class-int)   | v_separation   | `4`   |

---

## Property Descriptions

[int](class_int.md#class-int) **columns** = `1`

-  **set_columns**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_columns**()

The number of columns in the **GridContainer**. If modified, **GridContainer** reorders its Control-derived children to accommodate the new layout.

---

## Theme Property Descriptions

[int](class_int.md#class-int) **h_separation** = `4`

The horizontal separation of child nodes.

---

[int](class_int.md#class-int) **v_separation** = `4`

The vertical separation of child nodes.
