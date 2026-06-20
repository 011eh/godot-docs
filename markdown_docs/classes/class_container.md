# Container

**Inherits:** [Control](class_control.md#class-control) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [AspectRatioContainer](class_aspectratiocontainer.md#class-aspectratiocontainer), [BoxContainer](class_boxcontainer.md#class-boxcontainer), [CenterContainer](class_centercontainer.md#class-centercontainer), [EditorProperty](class_editorproperty.md#class-editorproperty), [FlowContainer](class_flowcontainer.md#class-flowcontainer), [FoldableContainer](class_foldablecontainer.md#class-foldablecontainer), [GraphElement](class_graphelement.md#class-graphelement), [GridContainer](class_gridcontainer.md#class-gridcontainer), [MarginContainer](class_margincontainer.md#class-margincontainer), [PanelContainer](class_panelcontainer.md#class-panelcontainer), [ScrollContainer](class_scrollcontainer.md#class-scrollcontainer), [SplitContainer](class_splitcontainer.md#class-splitcontainer), [SubViewportContainer](class_subviewportcontainer.md#class-subviewportcontainer), [TabContainer](class_tabcontainer.md#class-tabcontainer)

Base class for all GUI containers.

## Description

Base class for all GUI containers. A **Container** automatically arranges its child controls in a certain way. This class can be inherited to make custom container types.

## Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

## Properties

| [bool](class_bool.md#class-bool)                         | accessibility_region   | `false`                                                                                      |
|----------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [MouseFilter](class_control.md#enum-control-mousefilter) | mouse_filter                                                             | `1` (overrides [Control](class_control.md#class-control-property-mouse-filter))              |
| [bool](class_bool.md#class-bool)                         | propagate_maximum_size                                                   | `true` (overrides [Control](class_control.md#class-control-property-propagate-maximum-size)) |

## Methods

| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | \_get_allowed_size_flags_horizontal()                                                  |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)   | \_get_allowed_size_flags_vertical()                                                      |
|                                                                        | fit_child_in_rect(child: [Control](class_control.md#class-control), rect: [Rect2](class_rect2.md#class-rect2)) |
|                                                                        | queue_sort()                                                                                                          |

---

## Signals

**pre_sort_children**()

Emitted when children are going to be sorted.

---

**sort_children**()

Emitted when sorting the children is needed.

---

## Constants

**NOTIFICATION_PRE_SORT_CHILDREN** = `50`

Notification just before children are going to be sorted, in case there's something to process beforehand.

**NOTIFICATION_SORT_CHILDREN** = `51`

Notification for when sorting the children, it must be obeyed immediately.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **accessibility_region** = `false`

-  **set_accessibility_region**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_accessibility_region**()

If `true`, this container is marked as a region for accessibility. Use [Control.accessibility_name](class_control.md#class-control-property-accessibility-name) to give the region a descriptive name. Screen readers can navigate between regions using landmark navigation.

---

## Method Descriptions

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_get_allowed_size_flags_horizontal**()

Implement to return a list of allowed horizontal [SizeFlags](class_control.md#enum-control-sizeflags) for child nodes. This doesn't technically prevent the usages of any other size flags, if your implementation requires that. This only limits the options available to the user in the Inspector dock.

**Note:** Having no size flags is equal to having [Control.SIZE_SHRINK_BEGIN](class_control.md#class-control-constant-size-shrink-begin). As such, this value is always implicitly allowed.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_get_allowed_size_flags_vertical**()

Implement to return a list of allowed vertical [SizeFlags](class_control.md#enum-control-sizeflags) for child nodes. This doesn't technically prevent the usages of any other size flags, if your implementation requires that. This only limits the options available to the user in the Inspector dock.

**Note:** Having no size flags is equal to having [Control.SIZE_SHRINK_BEGIN](class_control.md#class-control-constant-size-shrink-begin). As such, this value is always implicitly allowed.

---

 **fit_child_in_rect**(child: [Control](class_control.md#class-control), rect: [Rect2](class_rect2.md#class-rect2))

Fit a child control in a given rect. This is mainly a helper for creating custom container classes.

---

 **queue_sort**()

Queue resort of the contained children. This is called automatically anyway, but can be called upon request.
