# VisibleOnScreenNotifier3D

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [VisibleOnScreenEnabler3D](class_visibleonscreenenabler3d.md#class-visibleonscreenenabler3d)

A box-shaped region of 3D space that detects whether it is visible on screen.

## Description

**VisibleOnScreenNotifier3D** represents a box-shaped region of 3D space. When any part of this region becomes visible on screen or in a [Camera3D](class_camera3d.md#class-camera3d)'s view, it will emit a screen_entered signal, and likewise it will emit a screen_exited signal when no part of it remains visible.

If you want a node to be enabled automatically when this region is visible on screen, use [VisibleOnScreenEnabler3D](class_visibleonscreenenabler3d.md#class-visibleonscreenenabler3d).

**Note:** **VisibleOnScreenNotifier3D** uses an approximate heuristic that doesn't take walls and other occlusion into account, unless occlusion culling is used. It also won't function unless [Node3D.visible](class_node3d.md#class-node3d-property-visible) is set to `true`.

## Properties

| [AABB](class_aabb.md#class-aabb)   | aabb   | `AABB(-1, -1, -1, 2, 2, 2)`   |
|------------------------------------|----------------------------------------------------------|-------------------------------|

## Methods

| [bool](class_bool.md#class-bool)   | is_on_screen()    |
|------------------------------------|---------------------------------------------------------------------------|

---

## Signals

**screen_entered**()

Emitted when the **VisibleOnScreenNotifier3D** enters the screen.

---

**screen_exited**()

Emitted when the **VisibleOnScreenNotifier3D** exits the screen.

---

## Property Descriptions

[AABB](class_aabb.md#class-aabb) **aabb** = `AABB(-1, -1, -1, 2, 2, 2)`

-  **set_aabb**(value: [AABB](class_aabb.md#class-aabb))
- [AABB](class_aabb.md#class-aabb) **get_aabb**()

The **VisibleOnScreenNotifier3D**'s bounding box.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **is_on_screen**()

Returns `true` if the bounding box is on the screen.

**Note:** It takes one frame for the **VisibleOnScreenNotifier3D**'s visibility to be assessed once added to the scene tree, so this method will always return `false` right after it is instantiated.
