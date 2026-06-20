# AudioListener2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Overrides the location sounds are heard from.

## Description

Once added to the scene tree and enabled using make_current(), this node will override the location sounds are heard from. Only one **AudioListener2D** can be current. Using make_current() will disable the previous **AudioListener2D**.

If there is no active **AudioListener2D** in the current [Viewport](class_viewport.md#class-viewport), center of the screen will be used as a hearing point for the audio. **AudioListener2D** needs to be inside [SceneTree](class_scenetree.md#class-scenetree) to function.

## Methods

|                                  | clear_current()   |
|----------------------------------|------------------------------------------------------------------|
| [bool](class_bool.md#class-bool) | is_current()         |
|                                  | make_current()     |

---

## Method Descriptions

 **clear_current**()

Disables the **AudioListener2D**. If it's not set as current, this method will have no effect.

---

[bool](class_bool.md#class-bool) **is_current**()

Returns `true` if this **AudioListener2D** is currently active.

---

 **make_current**()

Makes the **AudioListener2D** active, setting it as the hearing point for the sounds. If there is already another active **AudioListener2D**, it will be disabled.

This method will have no effect if the **AudioListener2D** is not added to [SceneTree](class_scenetree.md#class-scenetree).
