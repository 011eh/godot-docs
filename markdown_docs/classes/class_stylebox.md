# StyleBox

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [StyleBoxEmpty](class_styleboxempty.md#class-styleboxempty), [StyleBoxFlat](class_styleboxflat.md#class-styleboxflat), [StyleBoxLine](class_styleboxline.md#class-styleboxline), [StyleBoxTexture](class_styleboxtexture.md#class-styleboxtexture)

Abstract base class for defining stylized boxes for UI elements.

## Description

**StyleBox** is an abstract base class for drawing stylized boxes for UI elements. It is used for panels, buttons, [LineEdit](class_lineedit.md#class-lineedit) backgrounds, [Tree](class_tree.md#class-tree) backgrounds, etc. and also for testing a transparency mask for pointer signals. If mask test fails on a **StyleBox** assigned as mask to a control, clicks and motion signals will go through it to the one below.

**Note:** For control nodes that have *Theme Properties*, the `focus` **StyleBox** is displayed over the `normal`, `hover` or `pressed` **StyleBox**. This makes the `focus` **StyleBox** more reusable across different nodes.

## Properties

| [float](class_float.md#class-float)   | content_margin_bottom   | `-1.0`   |
|---------------------------------------|---------------------------------------------------------------------------|----------|
| [float](class_float.md#class-float)   | content_margin_left       | `-1.0`   |
| [float](class_float.md#class-float)   | content_margin_right     | `-1.0`   |
| [float](class_float.md#class-float)   | content_margin_top         | `-1.0`   |

## Methods

|                                                    | \_draw(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2))                                   |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect2](class_rect2.md#class-rect2)                | \_get_draw_rect(rect: [Rect2](class_rect2.md#class-rect2))                                                                |
| [Vector2](class_vector2.md#class-vector2)          | \_get_minimum_size()                                                                                                   |
| [bool](class_bool.md#class-bool)                   | \_test_mask(point: [Vector2](class_vector2.md#class-vector2), rect: [Rect2](class_rect2.md#class-rect2))                      |
|                                                    | draw(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2))                                                |
| [float](class_float.md#class-float)                | get_content_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                              |
| [CanvasItem](class_canvasitem.md#class-canvasitem) | get_current_item_drawn()                                                                                                 |
| [float](class_float.md#class-float)                | get_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side))                                                              |
| [Vector2](class_vector2.md#class-vector2)          | get_minimum_size()                                                                                                             |
| [Vector2](class_vector2.md#class-vector2)          | get_offset()                                                                                                                         |
|                                                    | set_content_margin(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float)) |
|                                                    | set_content_margin_all(offset: [float](class_float.md#class-float))                                                      |
| [bool](class_bool.md#class-bool)                   | test_mask(point: [Vector2](class_vector2.md#class-vector2), rect: [Rect2](class_rect2.md#class-rect2))                                |

---

## Property Descriptions

[float](class_float.md#class-float) **content_margin_bottom** = `-1.0`

-  **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

The bottom margin for the contents of this style box. Increasing this value reduces the space available to the contents from the bottom.

If this value is negative, it is ignored and a child-specific margin is used instead. For example, for [StyleBoxFlat](class_styleboxflat.md#class-styleboxflat), the border thickness (if any) is used instead.

It is up to the code using this style box to decide what these contents are: for example, a [Button](class_button.md#class-button) respects this content margin for the textual contents of the button.

get_margin() should be used to fetch this value as consumer instead of reading these properties directly. This is because it correctly respects negative values and the fallback mentioned above.

---

[float](class_float.md#class-float) **content_margin_left** = `-1.0`

-  **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

The left margin for the contents of this style box. Increasing this value reduces the space available to the contents from the left.

Refer to content_margin_bottom for extra considerations.

---

[float](class_float.md#class-float) **content_margin_right** = `-1.0`

-  **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

The right margin for the contents of this style box. Increasing this value reduces the space available to the contents from the right.

Refer to content_margin_bottom for extra considerations.

---

[float](class_float.md#class-float) **content_margin_top** = `-1.0`

-  **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side)) 

The top margin for the contents of this style box. Increasing this value reduces the space available to the contents from the top.

Refer to content_margin_bottom for extra considerations.

---

## Method Descriptions

 **\_draw**(to_canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Rect2](class_rect2.md#class-rect2) **\_get_draw_rect**(rect: [Rect2](class_rect2.md#class-rect2))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector2](class_vector2.md#class-vector2) **\_get_minimum_size**()

Virtual method to be implemented by the user. Returns a custom minimum size that the stylebox must respect when drawing. By default get_minimum_size() only takes content margins into account. This method can be overridden to add another size restriction. A combination of the default behavior and the output of this method will be used, to account for both sizes.

---

[bool](class_bool.md#class-bool) **\_test_mask**(point: [Vector2](class_vector2.md#class-vector2), rect: [Rect2](class_rect2.md#class-rect2))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **draw**(canvas_item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2))

Draws this stylebox using a canvas item identified by the given [RID](class_rid.md#class-rid).

The [RID](class_rid.md#class-rid) value can either be the result of [CanvasItem.get_canvas_item()](class_canvasitem.md#class-canvasitem-method-get-canvas-item) called on an existing [CanvasItem](class_canvasitem.md#class-canvasitem)-derived node, or directly from creating a canvas item in the [RenderingServer](class_renderingserver.md#class-renderingserver) with [RenderingServer.canvas_item_create()](class_renderingserver.md#class-renderingserver-method-canvas-item-create).

---

[float](class_float.md#class-float) **get_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the default margin of the specified [Side](class_@globalscope.md#enum-globalscope-side).

---

[CanvasItem](class_canvasitem.md#class-canvasitem) **get_current_item_drawn**()

Returns the [CanvasItem](class_canvasitem.md#class-canvasitem) that handles its [CanvasItem.NOTIFICATION_DRAW](class_canvasitem.md#class-canvasitem-constant-notification-draw) or [CanvasItem._draw()](class_canvasitem.md#class-canvasitem-private-method-draw) callback at this moment.

---

[float](class_float.md#class-float) **get_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side))

Returns the content margin offset for the specified [Side](class_@globalscope.md#enum-globalscope-side).

Positive values reduce size inwards, unlike [Control](class_control.md#class-control)'s margin values.

---

[Vector2](class_vector2.md#class-vector2) **get_minimum_size**()

Returns the minimum size that this stylebox can be shrunk to.

---

[Vector2](class_vector2.md#class-vector2) **get_offset**()

Returns the "offset" of a stylebox. This helper function returns a value equivalent to `Vector2(style.get_margin(MARGIN_LEFT), style.get_margin(MARGIN_TOP))`.

---

 **set_content_margin**(margin: [Side](class_@globalscope.md#enum-globalscope-side), offset: [float](class_float.md#class-float))

Sets the default value of the specified [Side](class_@globalscope.md#enum-globalscope-side) to `offset` pixels.

---

 **set_content_margin_all**(offset: [float](class_float.md#class-float))

Sets the default margin to `offset` pixels for all sides.

---

[bool](class_bool.md#class-bool) **test_mask**(point: [Vector2](class_vector2.md#class-vector2), rect: [Rect2](class_rect2.md#class-rect2))

Test a position in a rectangle, return whether it passes the mask test.
