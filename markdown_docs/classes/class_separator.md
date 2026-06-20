# Separator

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [HSeparator](class_hseparator.md#class-hseparator), [VSeparator](class_vseparator.md#class-vseparator)

Abstract base class for separators.

## Description

Abstract base class for separators, used for separating other controls. **Separator**s are purely visual and normally drawn as a [StyleBoxLine](class_styleboxline.md#class-styleboxline).

## Theme Properties

| [int](class_int.md#class-int)                | separation   | `0`   |
|----------------------------------------------|------------------------------------------------------------|-------|
| [StyleBox](class_stylebox.md#class-stylebox) | separator        |       |

---

## Theme Property Descriptions

[int](class_int.md#class-int) **separation** = `0`

The size of the area covered by the separator. Effectively works like a minimum width/height.

---

[StyleBox](class_stylebox.md#class-stylebox) **separator**

The style for the separator line. Works best with [StyleBoxLine](class_styleboxline.md#class-styleboxline) (remember to enable [StyleBoxLine.vertical](class_styleboxline.md#class-styleboxline-property-vertical) for [VSeparator](class_vseparator.md#class-vseparator)).
