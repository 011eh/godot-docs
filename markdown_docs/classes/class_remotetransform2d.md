# RemoteTransform2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

RemoteTransform2D pushes its own [Transform2D](class_transform2d.md#class-transform2d) to another [Node2D](class_node2d.md#class-node2d) derived node in the scene.

## Description

RemoteTransform2D pushes its own [Transform2D](class_transform2d.md#class-transform2d) to another [Node2D](class_node2d.md#class-node2d) derived node (called the remote node) in the scene.

It can be set to update another node's position, rotation and/or scale. It can use either global or local coordinates.

## Properties

| [NodePath](class_nodepath.md#class-nodepath)   | remote_path                       | `NodePath("")`   |
|------------------------------------------------|------------------------------------------------------------------------------------|------------------|
| [bool](class_bool.md#class-bool)               | update_position               | `true`           |
| [bool](class_bool.md#class-bool)               | update_rotation               | `true`           |
| [bool](class_bool.md#class-bool)               | update_scale                     | `true`           |
| [bool](class_bool.md#class-bool)               | use_global_coordinates | `true`           |

## Methods

|    | force_update_cache()   |
|----|------------------------------------------------------------------------------|

---

## Property Descriptions

[NodePath](class_nodepath.md#class-nodepath) **remote_path** = `NodePath("")`

-  **set_remote_node**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_remote_node**()

The [NodePath](class_nodepath.md#class-nodepath) to the remote node, relative to the RemoteTransform2D's position in the scene.

---

[bool](class_bool.md#class-bool) **update_position** = `true`

-  **set_update_position**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_update_position**()

If `true`, the remote node's position is updated.

---

[bool](class_bool.md#class-bool) **update_rotation** = `true`

-  **set_update_rotation**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_update_rotation**()

If `true`, the remote node's rotation is updated.

---

[bool](class_bool.md#class-bool) **update_scale** = `true`

-  **set_update_scale**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_update_scale**()

If `true`, the remote node's scale is updated.

---

[bool](class_bool.md#class-bool) **use_global_coordinates** = `true`

-  **set_use_global_coordinates**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_global_coordinates**()

If `true`, global coordinates are used. If `false`, local coordinates are used.

---

## Method Descriptions

 **force_update_cache**()

**RemoteTransform2D** caches the remote node. It may not notice if the remote node disappears; force_update_cache() forces it to update the cache again.
