# ScrollBar

**Inherits:** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [HScrollBar](class_hscrollbar.md#class-hscrollbar), [VScrollBar](class_vscrollbar.md#class-vscrollbar)

Abstract base class for scrollbars.

## Description

Abstract base class for scrollbars, typically used to navigate through content that extends beyond the visible area of a control. Scrollbars are [Range](class_range.md#class-range)-based controls.

## Properties

| [float](class_float.md#class-float)                  | custom_step   | `-1.0`                                                                        |
|------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------------------------------|
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode                                             | `3` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [float](class_float.md#class-float)                  | step                                                   | `0.0` (overrides [Range](class_range.md#class-range-property-step))           |

## Theme Properties

| [Texture2D](class_texture2d.md#class-texture2d)   | decrement                     |
|---------------------------------------------------|------------------------------------------------------------------------|
| [Texture2D](class_texture2d.md#class-texture2d)   | decrement_highlight |
| [Texture2D](class_texture2d.md#class-texture2d)   | decrement_pressed     |
| [Texture2D](class_texture2d.md#class-texture2d)   | increment                     |
| [Texture2D](class_texture2d.md#class-texture2d)   | increment_highlight |
| [Texture2D](class_texture2d.md#class-texture2d)   | increment_pressed     |
| [StyleBox](class_stylebox.md#class-stylebox)      | grabber                        |
| [StyleBox](class_stylebox.md#class-stylebox)      | grabber_highlight    |
| [StyleBox](class_stylebox.md#class-stylebox)      | grabber_pressed        |
| [StyleBox](class_stylebox.md#class-stylebox)      | scroll                          |
| [StyleBox](class_stylebox.md#class-stylebox)      | scroll_focus              |

---

## Signals

**scrolling**()

Emitted when the scrollbar is being scrolled.

---

## Property Descriptions

[float](class_float.md#class-float) **custom_step** = `-1.0`

-  **set_custom_step**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_custom_step**()

Overrides the step used when clicking increment and decrement buttons or when using arrow keys when the **ScrollBar** is focused.

---

## Theme Property Descriptions

[Texture2D](class_texture2d.md#class-texture2d) **decrement**

Icon used as a button to scroll the **ScrollBar** left/up. Supports custom step using the custom_step property.

---

[Texture2D](class_texture2d.md#class-texture2d) **decrement_highlight**

Displayed when the mouse cursor hovers over the decrement button.

---

[Texture2D](class_texture2d.md#class-texture2d) **decrement_pressed**

Displayed when the decrement button is being pressed.

---

[Texture2D](class_texture2d.md#class-texture2d) **increment**

Icon used as a button to scroll the **ScrollBar** right/down. Supports custom step using the custom_step property.

---

[Texture2D](class_texture2d.md#class-texture2d) **increment_highlight**

Displayed when the mouse cursor hovers over the increment button.

---

[Texture2D](class_texture2d.md#class-texture2d) **increment_pressed**

Displayed when the increment button is being pressed.

---

[StyleBox](class_stylebox.md#class-stylebox) **grabber**

Used as texture for the grabber, the draggable element representing current scroll.

---

[StyleBox](class_stylebox.md#class-stylebox) **grabber_highlight**

Used when the mouse hovers over the grabber.

---

[StyleBox](class_stylebox.md#class-stylebox) **grabber_pressed**

Used when the grabber is being dragged.

---

[StyleBox](class_stylebox.md#class-stylebox) **scroll**

Used as background of this **ScrollBar**.

---

[StyleBox](class_stylebox.md#class-stylebox) **scroll_focus**

Used as background when the **ScrollBar** has the GUI focus.
