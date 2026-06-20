# FoldableContainer

**Inherits:** [Container](class_container.md#class-container) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A container that can be expanded/collapsed.

## Description

A container that can be expanded/collapsed, with a title that can be filled with controls, such as buttons. This is also called an accordion.

The title can be positioned at the top or bottom of the container. The container can be expanded or collapsed by clicking the title or by pressing `ui_accept` when focused. Child control nodes are hidden when the container is collapsed. Ignores non-control children.

A FoldableContainer can be grouped with other FoldableContainers so that only one of them can be opened at a time; see foldable_group and [FoldableGroup](class_foldablegroup.md#class-foldablegroup).

## Properties

| [FocusMode](class_control.md#enum-control-focusmode)                              | focus_mode                                                                                   | `2` (overrides [Control](class_control.md#class-control-property-focus-mode))   |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [FoldableGroup](class_foldablegroup.md#class-foldablegroup)                       | foldable_group                           |                                                                                 |
| [bool](class_bool.md#class-bool)                                                  | folded                                           | `false`                                                                         |
| [String](class_string.md#class-string)                                            | language                                       | `""`                                                                            |
| [MouseFilter](class_control.md#enum-control-mousefilter)                          | mouse_filter                                                                                 | `0` (overrides [Control](class_control.md#class-control-property-mouse-filter)) |
| [String](class_string.md#class-string)                                            | title                                             | `""`                                                                            |
| [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) | title_alignment                         | `0`                                                                             |
| TitlePosition                            | title_position                           | `0`                                                                             |
| [TextDirection](class_control.md#enum-control-textdirection)                      | title_text_direction               | `0`                                                                             |
| [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior)            | title_text_overrun_behavior | `0`                                                                             |

## Methods

|    | add_title_bar_control(control: [Control](class_control.md#class-control))       |
|----|------------------------------------------------------------------------------------------------------------------------------------------|
|    | expand()                                                                                       |
|    | fold()                                                                                           |
|    | remove_title_bar_control(control: [Control](class_control.md#class-control)) |

## Theme Properties

| [Color](class_color.md#class-color)             | collapsed_font_color               | `Color(1, 1, 1, 1)`             |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------|
| [Color](class_color.md#class-color)             | font_color                                   | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class-color)             | font_outline_color                   | `Color(1, 1, 1, 1)`             |
| [Color](class_color.md#class-color)             | hover_font_color                       | `Color(0.95, 0.95, 0.95, 1)`    |
| [int](class_int.md#class-int)                   | h_separation                            | `2`                             |
| [int](class_int.md#class-int)                   | outline_size                            | `0`                             |
| [Font](class_font.md#class-font)                | font                                                |                                 |
| [int](class_int.md#class-int)                   | font_size                                 |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | expanded_arrow                            |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | expanded_arrow_mirrored          |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | folded_arrow                                |                                 |
| [Texture2D](class_texture2d.md#class-texture2d) | folded_arrow_mirrored              |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | focus                                             |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | panel                                             |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | title_collapsed_hover_panel |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | title_collapsed_panel             |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | title_hover_panel                     |                                 |
| [StyleBox](class_stylebox.md#class-stylebox)    | title_panel                                 |                                 |

---

## Signals

**folding_changed**(is_folded: [bool](class_bool.md#class-bool))

Emitted when the container is folded/expanded.

---

## Enumerations

enum **TitlePosition**:

TitlePosition **POSITION_TOP** = `0`

Makes the title appear at the top of the container.

TitlePosition **POSITION_BOTTOM** = `1`

Makes the title appear at the bottom of the container. Also makes all StyleBoxes flipped vertically.

---

## Property Descriptions

[FoldableGroup](class_foldablegroup.md#class-foldablegroup) **foldable_group**

-  **set_foldable_group**(value: [FoldableGroup](class_foldablegroup.md#class-foldablegroup))
- [FoldableGroup](class_foldablegroup.md#class-foldablegroup) **get_foldable_group**()

The [FoldableGroup](class_foldablegroup.md#class-foldablegroup) associated with the container. When multiple **FoldableContainer** nodes share the same group, only one of them is allowed to be unfolded.

---

[bool](class_bool.md#class-bool) **folded** = `false`

-  **set_folded**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_folded**()

If `true`, the container will become folded and will hide all its children.

---

[String](class_string.md#class-string) **language** = `""`

-  **set_language**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_language**()

Language code used for text shaping algorithms. If left empty, the current locale is used instead.

---

[String](class_string.md#class-string) **title** = `""`

-  **set_title**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_title**()

The container's title text.

---

[HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **title_alignment** = `0`

-  **set_title_alignment**(value: [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment))
- [HorizontalAlignment](class_@globalscope.md#enum-globalscope-horizontalalignment) **get_title_alignment**()

Title's horizontal text alignment.

---

TitlePosition **title_position** = `0`

-  **set_title_position**(value: TitlePosition)
- TitlePosition **get_title_position**()

Title's position.

---

[TextDirection](class_control.md#enum-control-textdirection) **title_text_direction** = `0`

-  **set_title_text_direction**(value: [TextDirection](class_control.md#enum-control-textdirection))
- [TextDirection](class_control.md#enum-control-textdirection) **get_title_text_direction**()

Title text writing direction.

---

[OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **title_text_overrun_behavior** = `0`

-  **set_title_text_overrun_behavior**(value: [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior))
- [OverrunBehavior](class_textserver.md#enum-textserver-overrunbehavior) **get_title_text_overrun_behavior**()

Defines the behavior of the title when the text is longer than the available space.

---

## Method Descriptions

 **add_title_bar_control**(control: [Control](class_control.md#class-control))

Adds a [Control](class_control.md#class-control) that will be placed next to the container's title, obscuring the clickable area. Prime usage is adding [Button](class_button.md#class-button) nodes, but it can be any [Control](class_control.md#class-control).

The control will be added as a child of this container and removed from previous parent if necessary. The controls will be placed aligned to the right, with the first added control being the leftmost one.

---

 **expand**()

Expands the container and emits folding_changed.

---

 **fold**()

Folds the container and emits folding_changed.

---

 **remove_title_bar_control**(control: [Control](class_control.md#class-control))

Removes a [Control](class_control.md#class-control) added with add_title_bar_control(). The node is not freed automatically, you need to use [Node.queue_free()](class_node.md#class-node-method-queue-free).

---

## Theme Property Descriptions

[Color](class_color.md#class-color) **collapsed_font_color** = `Color(1, 1, 1, 1)`

The title's font color when collapsed.

---

[Color](class_color.md#class-color) **font_color** = `Color(0.875, 0.875, 0.875, 1)`

The title's font color when expanded.

---

[Color](class_color.md#class-color) **font_outline_color** = `Color(1, 1, 1, 1)`

The title's font outline color.

---

[Color](class_color.md#class-color) **hover_font_color** = `Color(0.95, 0.95, 0.95, 1)`

The title's font hover color.

---

[int](class_int.md#class-int) **h_separation** = `2`

The horizontal separation between the title's icon and text, and between title bar controls.

---

[int](class_int.md#class-int) **outline_size** = `0`

The title's font outline size.

---

[Font](class_font.md#class-font) **font**

The title's font.

---

[int](class_int.md#class-int) **font_size**

The title's font size.

---

[Texture2D](class_texture2d.md#class-texture2d) **expanded_arrow**

The title's icon used when expanded.

---

[Texture2D](class_texture2d.md#class-texture2d) **expanded_arrow_mirrored**

The title's icon used when expanded (for bottom title).

---

[Texture2D](class_texture2d.md#class-texture2d) **folded_arrow**

The title's icon used when folded (for left-to-right layouts).

---

[Texture2D](class_texture2d.md#class-texture2d) **folded_arrow_mirrored**

The title's icon used when collapsed (for right-to-left layouts).

---

[StyleBox](class_stylebox.md#class-stylebox) **focus**

Background used when **FoldableContainer** has GUI focus. The focus [StyleBox](class_stylebox.md#class-stylebox) is displayed *over* the base [StyleBox](class_stylebox.md#class-stylebox), so a partially transparent [StyleBox](class_stylebox.md#class-stylebox) should be used to ensure the base [StyleBox](class_stylebox.md#class-stylebox) remains visible. A [StyleBox](class_stylebox.md#class-stylebox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

[StyleBox](class_stylebox.md#class-stylebox) **panel**

Default background for the **FoldableContainer**.

---

[StyleBox](class_stylebox.md#class-stylebox) **title_collapsed_hover_panel**

Background used when the mouse cursor enters the title's area when collapsed.

---

[StyleBox](class_stylebox.md#class-stylebox) **title_collapsed_panel**

Default background for the **FoldableContainer**'s title when collapsed.

---

[StyleBox](class_stylebox.md#class-stylebox) **title_hover_panel**

Background used when the mouse cursor enters the title's area when expanded.

---

[StyleBox](class_stylebox.md#class-stylebox) **title_panel**

Default background for the **FoldableContainer**'s title when expanded.
