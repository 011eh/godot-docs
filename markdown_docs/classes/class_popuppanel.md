# PopupPanel

**Inherits:** [Popup](class_popup.md#class-popup) **<** [Window](class_window.md#class-window) **<** [Viewport](class_viewport.md#class-viewport) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A popup with a panel background.

## Description

A popup with a configurable panel background. Any child controls added to this node will be stretched to fit the panel's size (similar to how [PanelContainer](class_panelcontainer.md#class-panelcontainer) works). If you are making windows, see [Window](class_window.md#class-window).

## Properties

| [DefaultCanvasItemTextureFilter](class_viewport.md#enum-viewport-defaultcanvasitemtexturefilter)   | canvas_item_default_texture_filter   | `4` (overrides [Viewport](class_viewport.md#class-viewport-property-canvas-item-default-texture-filter))   |
|----------------------------------------------------------------------------------------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------|
| [DefaultCanvasItemTextureRepeat](class_viewport.md#enum-viewport-defaultcanvasitemtexturerepeat)   | canvas_item_default_texture_repeat   | `3` (overrides [Viewport](class_viewport.md#class-viewport-property-canvas-item-default-texture-repeat))   |
| [bool](class_bool.md#class-bool)                                                                   | transparent                          | `true` (overrides [Window](class_window.md#class-window-property-transparent))                             |
| [bool](class_bool.md#class-bool)                                                                   | transparent_bg                       | `true` (overrides [Viewport](class_viewport.md#class-viewport-property-transparent-bg))                    |

## Theme Properties

| [StyleBox](class_stylebox.md#class-stylebox)   | panel   |
|------------------------------------------------|------------------------------------------------|

---

## Theme Property Descriptions

[StyleBox](class_stylebox.md#class-stylebox) **panel**

[StyleBox](class_stylebox.md#class-stylebox) for the background panel.
