# InputEventFromWindow

**Inherits:** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [InputEventScreenDrag](class_inputeventscreendrag.md#class-inputeventscreendrag), [InputEventScreenTouch](class_inputeventscreentouch.md#class-inputeventscreentouch), [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers)

Abstract base class for [Viewport](class_viewport.md#class-viewport)-based input events.

## Description

InputEventFromWindow represents events specifically received by windows. This includes mouse events, keyboard events in focused windows or touch screen actions.

## Properties

| [int](class_int.md#class-int)   | window_id   | `0`   |
|---------------------------------|---------------------------------------------------------------|-------|

---

## Property Descriptions

[int](class_int.md#class-int) **window_id** = `0`

-  **set_window_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_window_id**()

The ID of a [Window](class_window.md#class-window) that received this event.
