# Slider

**Inherits:** [Range](class_range.md#class-range) **<** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [HSlider](class_hslider.md#class-hslider), [VSlider](class_vslider.md#class-vslider)

Abstract base class for sliders.

## Description

Abstract base class for sliders, used to adjust a value by moving a grabber along a horizontal or vertical axis. Sliders are [Range](class_range.md#class-range)-based controls.

## Properties

| [bool](class_bool.md#class-bool)                     | editable                 | `true`                                                                        |
|------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------|
| [FocusMode](class_control.md#enum-control-focusmode) | focus_mode                                                  | `2` (overrides [Control](class_control.md#class-control-property-focus-mode)) |
| [bool](class_bool.md#class-bool)                     | scrollable             | `true`                                                                        |
| [float](class_float.md#class-float)                  | step                                                        | `1.0` (overrides [Range](class_range.md#class-range-property-step))           |
| [int](class_int.md#class-int)                        | tick_count             | `0`                                                                           |
| [bool](class_bool.md#class-bool)                     | ticks_on_borders | `false`                                                                       |
| TickPosition            | ticks_position     | `0`                                                                           |

## Theme Properties

| [int](class_int.md#class-int)                   | center_grabber              | `0`   |
|-------------------------------------------------|----------------------------------------------------------------------------|-------|
| [int](class_int.md#class-int)                   | grabber_offset              | `0`   |
| [int](class_int.md#class-int)                   | tick_offset                    | `0`   |
| [Texture2D](class_texture2d.md#class-texture2d) | grabber                                |       |
| [Texture2D](class_texture2d.md#class-texture2d) | grabber_disabled              |       |
| [Texture2D](class_texture2d.md#class-texture2d) | grabber_highlight            |       |
| [Texture2D](class_texture2d.md#class-texture2d) | tick                                      |       |
| [StyleBox](class_stylebox.md#class-stylebox)    | grabber_area                     |       |
| [StyleBox](class_stylebox.md#class-stylebox)    | grabber_area_highlight |       |
| [StyleBox](class_stylebox.md#class-stylebox)    | slider                                 |       |

---

## Signals

**drag_ended**(value_changed: [bool](class_bool.md#class-bool))

Emitted when the grabber stops being dragged. If `value_changed` is `true`, [Range.value](class_range.md#class-range-property-value) is different from the value when the dragging was started.

---

**drag_started**()

Emitted when the grabber starts being dragged. This is emitted before the corresponding [Range.value_changed](class_range.md#class-range-signal-value-changed) signal.

---

## Enumerations

enum **TickPosition**:

TickPosition **TICK_POSITION_BOTTOM_RIGHT** = `0`

Places the ticks at the bottom of the [HSlider](class_hslider.md#class-hslider), or right of the [VSlider](class_vslider.md#class-vslider).

TickPosition **TICK_POSITION_TOP_LEFT** = `1`

Places the ticks at the top of the [HSlider](class_hslider.md#class-hslider), or left of the [VSlider](class_vslider.md#class-vslider).

TickPosition **TICK_POSITION_BOTH** = `2`

Places the ticks at the both sides of the slider.

TickPosition **TICK_POSITION_CENTER** = `3`

Places the ticks at the center of the slider.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **editable** = `true`

-  **set_editable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_editable**()

If `true`, the slider can be interacted with. If `false`, the value can be changed only by code.

---

[bool](class_bool.md#class-bool) **scrollable** = `true`

-  **set_scrollable**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_scrollable**()

If `true`, the value can be changed using the mouse wheel.

---

[int](class_int.md#class-int) **tick_count** = `0`

-  **set_ticks**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_ticks**()

Number of ticks displayed on the slider, including border ticks. Ticks are uniformly-distributed value markers.

---

[bool](class_bool.md#class-bool) **ticks_on_borders** = `false`

-  **set_ticks_on_borders**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_ticks_on_borders**()

If `true`, the slider will display ticks for minimum and maximum values.

---

TickPosition **ticks_position** = `0`

-  **set_ticks_position**(value: TickPosition)
- TickPosition **get_ticks_position**()

Sets the position of the ticks. See TickPosition for details.

---

## Theme Property Descriptions

[int](class_int.md#class-int) **center_grabber** = `0`

Boolean constant. If `1`, the grabber texture size will be ignored and it will fit within slider's bounds based only on its center position.

---

[int](class_int.md#class-int) **grabber_offset** = `0`

Vertical or horizontal offset of the grabber.

---

[int](class_int.md#class-int) **tick_offset** = `0`

Vertical or horizontal offset of the ticks. The offset is reversed for top or left ticks.

---

[Texture2D](class_texture2d.md#class-texture2d) **grabber**

The texture for the grabber (the draggable element).

---

[Texture2D](class_texture2d.md#class-texture2d) **grabber_disabled**

The texture for the grabber when it's disabled.

---

[Texture2D](class_texture2d.md#class-texture2d) **grabber_highlight**

The texture for the grabber when it's focused.

---

[Texture2D](class_texture2d.md#class-texture2d) **tick**

The texture for the ticks, visible when tick_count is greater than 0.

---

[StyleBox](class_stylebox.md#class-stylebox) **grabber_area**

The background of the area to the left or bottom of the grabber.

---

[StyleBox](class_stylebox.md#class-stylebox) **grabber_area_highlight**

The background of the area to the left or bottom of the grabber that displays when it's being hovered or focused.

---

[StyleBox](class_stylebox.md#class-stylebox) **slider**

The background for the whole slider. Affects the height or width of the grabber_area.
