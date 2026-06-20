# GraphFrame

**Inherits:** [GraphElement](class_graphelement.md#class-graphelement) **<** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

GraphFrame is a special [GraphElement](class_graphelement.md#class-graphelement) that can be used to organize other [GraphElement](class_graphelement.md#class-graphelement)s inside a [GraphEdit](class_graphedit.md#class-graphedit).

## Description

GraphFrame is a special [GraphElement](class_graphelement.md#class-graphelement) to which other [GraphElement](class_graphelement.md#class-graphelement)s can be attached. It can be configured to automatically resize to enclose all attached [GraphElement](class_graphelement.md#class-graphelement)s. If the frame is moved, all the attached [GraphElement](class_graphelement.md#class-graphelement)s inside it will be moved as well.

A GraphFrame is always kept behind the connection layer and other [GraphElement](class_graphelement.md#class-graphelement)s inside a [GraphEdit](class_graphedit.md#class-graphedit).

## Properties

| [bool](class_bool.md#class-bool)                         | autoshrink_enabled   | `true`                                                                          |
|----------------------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                            | autoshrink_margin     | `40`                                                                            |
| [int](class_int.md#class-int)                            | drag_margin                 | `16`                                                                            |
| [MouseFilter](class_control.md#enum-control-mousefilter) | mouse_filter                                                          | `0` (overrides [Control](class_control.md#class-control-property-mouse-filter)) |
| [Color](class_color.md#class-color)                      | tint_color                   | `Color(0.3, 0.3, 0.3, 0.75)`                                                    |
| [bool](class_bool.md#class-bool)                         | tint_color_enabled   | `false`                                                                         |
| [String](class_string.md#class-string)                   | title                             | `""`                                                                            |

## Methods

| [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer)   | get_titlebar_hbox()   |
|---------------------------------------------------------------|---------------------------------------------------------------------|

## Theme Properties

| [Color](class_color.md#class-color)          | resizer_color         | `Color(0.875, 0.875, 0.875, 1)`   |
|----------------------------------------------|----------------------------------------------------------------------|-----------------------------------|
| [StyleBox](class_stylebox.md#class-stylebox) | panel                         |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | panel_selected       |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | titlebar                   |                                   |
| [StyleBox](class_stylebox.md#class-stylebox) | titlebar_selected |                                   |

---

## Signals

**autoshrink_changed**()

Emitted when autoshrink_enabled or autoshrink_margin changes.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **autoshrink_enabled** = `true`

-  **set_autoshrink_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_autoshrink_enabled**()

If `true`, the frame's rect will be adjusted automatically to enclose all attached [GraphElement](class_graphelement.md#class-graphelement)s.

---

[int](class_int.md#class-int) **autoshrink_margin** = `40`

-  **set_autoshrink_margin**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_autoshrink_margin**()

The margin around the attached nodes that is used to calculate the size of the frame when autoshrink_enabled is `true`.

---

[int](class_int.md#class-int) **drag_margin** = `16`

-  **set_drag_margin**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_drag_margin**()

The margin inside the frame that can be used to drag the frame.

---

[Color](class_color.md#class-color) **tint_color** = `Color(0.3, 0.3, 0.3, 0.75)`

-  **set_tint_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_tint_color**()

The color of the frame when tint_color_enabled is `true`.

---

[bool](class_bool.md#class-bool) **tint_color_enabled** = `false`

-  **set_tint_color_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_tint_color_enabled**()

If `true`, the tint color will be used to tint the frame.

---

[String](class_string.md#class-string) **title** = `""`

-  **set_title**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_title**()

Title of the frame.

---

## Method Descriptions

[HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) **get_titlebar_hbox**()

Returns the [HBoxContainer](class_hboxcontainer.md#class-hboxcontainer) used for the title bar, only containing a [Label](class_label.md#class-label) for displaying the title by default.

This can be used to add custom controls to the title bar such as option or close buttons.

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **resizer_color** = `Color(0.875, 0.875, 0.875, 1)`

The color modulation applied to the resizer icon.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

The default [StyleBox](class_stylebox.md#class-stylebox) used for the background of the **GraphFrame**.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel_selected**

The [StyleBox](class_stylebox.md#class-stylebox) used for the background of the **GraphFrame** when it is selected.

---

[StyleBox](class_stylebox.md#class-stylebox) **titlebar**

The [StyleBox](class_stylebox.md#class-stylebox) used for the title bar of the **GraphFrame**.

---

[StyleBox](class_stylebox.md#class-stylebox) **titlebar_selected**

The [StyleBox](class_stylebox.md#class-stylebox) used for the title bar of the **GraphFrame** when it is selected.
