# Node2D

**Inherits:** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [AnimatedSprite2D](class_animatedsprite2d.md#class-animatedsprite2d), [AudioListener2D](class_audiolistener2d.md#class-audiolistener2d), [AudioStreamPlayer2D](class_audiostreamplayer2d.md#class-audiostreamplayer2d), [BackBufferCopy](class_backbuffercopy.md#class-backbuffercopy), [Bone2D](class_bone2d.md#class-bone2d), [Camera2D](class_camera2d.md#class-camera2d), [CanvasGroup](class_canvasgroup.md#class-canvasgroup), [CanvasModulate](class_canvasmodulate.md#class-canvasmodulate), [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d), [CollisionPolygon2D](class_collisionpolygon2d.md#class-collisionpolygon2d), [CollisionShape2D](class_collisionshape2d.md#class-collisionshape2d), [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d), [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d), [Joint2D](class_joint2d.md#class-joint2d), [Light2D](class_light2d.md#class-light2d), [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d), [Line2D](class_line2d.md#class-line2d), [Marker2D](class_marker2d.md#class-marker2d), [MeshInstance2D](class_meshinstance2d.md#class-meshinstance2d), [MultiMeshInstance2D](class_multimeshinstance2d.md#class-multimeshinstance2d), [NavigationLink2D](class_navigationlink2d.md#class-navigationlink2d), [NavigationObstacle2D](class_navigationobstacle2d.md#class-navigationobstacle2d), [NavigationRegion2D](class_navigationregion2d.md#class-navigationregion2d), [Parallax2D](class_parallax2d.md#class-parallax2d), [ParallaxLayer](class_parallaxlayer.md#class-parallaxlayer), [Path2D](class_path2d.md#class-path2d), [PathFollow2D](class_pathfollow2d.md#class-pathfollow2d), [Polygon2D](class_polygon2d.md#class-polygon2d), [RayCast2D](class_raycast2d.md#class-raycast2d), [RemoteTransform2D](class_remotetransform2d.md#class-remotetransform2d), [ShapeCast2D](class_shapecast2d.md#class-shapecast2d), [Skeleton2D](class_skeleton2d.md#class-skeleton2d), [Sprite2D](class_sprite2d.md#class-sprite2d), [TileMap](class_tilemap.md#class-tilemap), [TileMapLayer](class_tilemaplayer.md#class-tilemaplayer), [TouchScreenButton](class_touchscreenbutton.md#class-touchscreenbutton), [VisibleOnScreenNotifier2D](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d)

A 2D game object, inherited by all 2D-related nodes. Has a position, rotation, scale, and skew.

## Description

A 2D game object, with a transform (position, rotation, and scale). All 2D nodes, including physics objects and sprites, inherit from Node2D. Use Node2D as a parent node to move, scale and rotate children in a 2D project. Also gives control of the node's render order.

**Note:** Since both **Node2D** and [Control](class_control.md#class-control) inherit from [CanvasItem](class_canvasitem.md#class-canvasitem), they share several concepts from the class such as the [CanvasItem.z_index](class_canvasitem.md#class-canvasitem-property-z-index) and [CanvasItem.visible](class_canvasitem.md#class-canvasitem-property-visible) properties.

## Tutorials

- [Custom drawing in 2D](../tutorials/2d/custom_drawing_in_2d.md)
- [All 2D Demos](https://github.com/godotengine/godot-demo-projects/tree/master/2d)

## Properties

| [Vector2](class_vector2.md#class-vector2)             | global_position                 |                 |
|-------------------------------------------------------|---------------------------------------------------------------------------|-----------------|
| [float](class_float.md#class-float)                   | global_rotation                 |                 |
| [float](class_float.md#class-float)                   | global_rotation_degrees |                 |
| [Vector2](class_vector2.md#class-vector2)             | global_scale                       |                 |
| [float](class_float.md#class-float)                   | global_skew                         |                 |
| [Transform2D](class_transform2d.md#class-transform2d) | global_transform               |                 |
| [Vector2](class_vector2.md#class-vector2)             | position                               | `Vector2(0, 0)` |
| [float](class_float.md#class-float)                   | rotation                               | `0.0`           |
| [float](class_float.md#class-float)                   | rotation_degrees               |                 |
| [Vector2](class_vector2.md#class-vector2)             | scale                                     | `Vector2(1, 1)` |
| [float](class_float.md#class-float)                   | skew                                       | `0.0`           |
| [Transform2D](class_transform2d.md#class-transform2d) | transform                             |                 |

## Methods

|                                                       | apply_scale(ratio: [Vector2](class_vector2.md#class-vector2))                                               |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [float](class_float.md#class-float)                   | get_angle_to(point: [Vector2](class_vector2.md#class-vector2))                                             |
| [Transform2D](class_transform2d.md#class-transform2d) | get_relative_transform_to_parent(parent: [Node](class_node.md#class-node))             |
|                                                       | global_translate(offset: [Vector2](class_vector2.md#class-vector2))                                    |
|                                                       | look_at(point: [Vector2](class_vector2.md#class-vector2))                                                       |
|                                                       | move_local_x(delta: [float](class_float.md#class-float), scaled: [bool](class_bool.md#class-bool) = false) |
|                                                       | move_local_y(delta: [float](class_float.md#class-float), scaled: [bool](class_bool.md#class-bool) = false) |
|                                                       | rotate(radians: [float](class_float.md#class-float))                                                             |
| [Vector2](class_vector2.md#class-vector2)             | to_global(local_point: [Vector2](class_vector2.md#class-vector2))                                             |
| [Vector2](class_vector2.md#class-vector2)             | to_local(global_point: [Vector2](class_vector2.md#class-vector2))                                              |
|                                                       | translate(offset: [Vector2](class_vector2.md#class-vector2))                                                  |

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **global_position**

-  **set_global_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_global_position**()

Global position. See also position.

---

[float](class_float.md#class-float) **global_rotation**

-  **set_global_rotation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_global_rotation**()

Global rotation in radians. See also rotation.

---

[float](class_float.md#class-float) **global_rotation_degrees**

-  **set_global_rotation_degrees**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_global_rotation_degrees**()

Helper property to access global_rotation in degrees instead of radians. See also rotation_degrees.

---

[Vector2](class_vector2.md#class-vector2) **global_scale**

-  **set_global_scale**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_global_scale**()

Global scale. See also scale.

---

[float](class_float.md#class-float) **global_skew**

-  **set_global_skew**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_global_skew**()

Global skew in radians. See also skew.

---

[Transform2D](class_transform2d.md#class-transform2d) **global_transform**

-  **set_global_transform**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_global_transform**()

Global [Transform2D](class_transform2d.md#class-transform2d). See also transform.

---

[Vector2](class_vector2.md#class-vector2) **position** = `Vector2(0, 0)`

-  **set_position**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_position**()

Position, relative to the node's parent. See also global_position.

---

[float](class_float.md#class-float) **rotation** = `0.0`

-  **set_rotation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_rotation**()

Rotation in radians, relative to the node's parent. See also global_rotation.

**Note:** This property is edited in the inspector in degrees. If you want to use degrees in a script, use rotation_degrees.

---

[float](class_float.md#class-float) **rotation_degrees**

-  **set_rotation_degrees**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_rotation_degrees**()

Helper property to access rotation in degrees instead of radians. See also global_rotation_degrees.

---

[Vector2](class_vector2.md#class-vector2) **scale** = `Vector2(1, 1)`

-  **set_scale**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_scale**()

The node's scale, relative to the node's parent. Unscaled value: `(1, 1)`. See also global_scale.

**Note:** Negative X scales in 2D are not decomposable from the transformation matrix. Due to the way scale is represented with transformation matrices in Godot, negative scales on the X axis will be changed to negative scales on the Y axis and a rotation of 180 degrees when decomposed.

---

[float](class_float.md#class-float) **skew** = `0.0`

-  **set_skew**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_skew**()

If set to a non-zero value, slants the node in one direction or another. This can be used for pseudo-3D effects. See also global_skew.

**Note:** Skew is performed on the X axis only, and *between* rotation and scaling.

**Note:** This property is edited in the inspector in degrees. If you want to use degrees in a script, use `skew = deg_to_rad(value_in_degrees)`.

---

[Transform2D](class_transform2d.md#class-transform2d) **transform**

-  **set_transform**(value: [Transform2D](class_transform2d.md#class-transform2d))
- [Transform2D](class_transform2d.md#class-transform2d) **get_transform**()

The node's [Transform2D](class_transform2d.md#class-transform2d), relative to the node's parent. See also global_transform.

---

## Method Descriptions

 **apply_scale**(ratio: [Vector2](class_vector2.md#class-vector2))

Multiplies the current scale by the `ratio` vector.

---

[float](class_float.md#class-float) **get_angle_to**(point: [Vector2](class_vector2.md#class-vector2))

Returns the angle between the node and the `point` in radians. See also look_at().

[Illustration of the returned angle.](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/node2d_get_angle_to.png)

---

[Transform2D](class_transform2d.md#class-transform2d) **get_relative_transform_to_parent**(parent: [Node](class_node.md#class-node))

Returns the [Transform2D](class_transform2d.md#class-transform2d) relative to this node's parent.

---

 **global_translate**(offset: [Vector2](class_vector2.md#class-vector2))

Adds the `offset` vector to the node's global position.

---

 **look_at**(point: [Vector2](class_vector2.md#class-vector2))

Rotates the node so that its local +X axis points towards the `point`, which is expected to use global coordinates. This method is a combination of both rotate() and get_angle_to().

`point` should not be the same as the node's position, otherwise the node always looks to the right.

---

 **move_local_x**(delta: [float](class_float.md#class-float), scaled: [bool](class_bool.md#class-bool) = false)

Applies a local translation on the node's X axis with the amount specified in `delta`. If `scaled` is `false`, normalizes the movement to occur independently of the node's scale.

---

 **move_local_y**(delta: [float](class_float.md#class-float), scaled: [bool](class_bool.md#class-bool) = false)

Applies a local translation on the node's Y axis with the amount specified in `delta`. If `scaled` is `false`, normalizes the movement to occur independently of the node's scale.

---

 **rotate**(radians: [float](class_float.md#class-float))

Applies a rotation to the node, in radians, starting from its current rotation. This is equivalent to `rotation += radians`.

---

[Vector2](class_vector2.md#class-vector2) **to_global**(local_point: [Vector2](class_vector2.md#class-vector2))

Transforms the provided local position into a position in global coordinate space. The input is expected to be local relative to the **Node2D** it is called on. e.g. Applying this method to the positions of child nodes will correctly transform their positions into the global coordinate space, but applying it to a node's own position will give an incorrect result, as it will incorporate the node's own transformation into its global position.

---

[Vector2](class_vector2.md#class-vector2) **to_local**(global_point: [Vector2](class_vector2.md#class-vector2))

Transforms the provided global position into a position in local coordinate space. The output will be local relative to the **Node2D** it is called on. e.g. It is appropriate for determining the positions of child nodes, but it is not appropriate for determining its own position relative to its parent.

---

 **translate**(offset: [Vector2](class_vector2.md#class-vector2))

Translates the node by the given `offset` in local coordinates. This is equivalent to `position += offset`.
