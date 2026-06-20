# Node3D

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [AudioListener3D](class_audiolistener3d.md#class-audiolistener3d), [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d), [BoneAttachment3D](class_boneattachment3d.md#class-boneattachment3d), [Camera3D](class_camera3d.md#class-camera3d), [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d), [CollisionPolygon3D](class_collisionpolygon3d.md#class-collisionpolygon3d), [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d), [GridMap](class_gridmap.md#class-gridmap), [ImporterMeshInstance3D](class_importermeshinstance3d.md#class-importermeshinstance3d), [Joint3D](class_joint3d.md#class-joint3d), [LightmapProbe](class_lightmapprobe.md#class-lightmapprobe), [Marker3D](class_marker3d.md#class-marker3d), [NavigationLink3D](class_navigationlink3d.md#class-navigationlink3d), [NavigationObstacle3D](class_navigationobstacle3d.md#class-navigationobstacle3d), [NavigationRegion3D](class_navigationregion3d.md#class-navigationregion3d), [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class-openxrcompositionlayer), [OpenXRHand](class_openxrhand.md#class-openxrhand), [OpenXRRenderModel](class_openxrrendermodel.md#class-openxrrendermodel), [OpenXRRenderModelManager](class_openxrrendermodelmanager.md#class-openxrrendermodelmanager), [Path3D](class_path3d.md#class-path3d), [PathFollow3D](class_pathfollow3d.md#class-pathfollow3d), [RayCast3D](class_raycast3d.md#class-raycast3d), [RemoteTransform3D](class_remotetransform3d.md#class-remotetransform3d), [ShapeCast3D](class_shapecast3d.md#class-shapecast3d), [Skeleton3D](class_skeleton3d.md#class-skeleton3d), [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d), [SpringArm3D](class_springarm3d.md#class-springarm3d), [SpringBoneCollision3D](class_springbonecollision3d.md#class-springbonecollision3d), [VehicleWheel3D](class_vehiclewheel3d.md#class-vehiclewheel3d), [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d), [XRFaceModifier3D](class_xrfacemodifier3d.md#class-xrfacemodifier3d), [XRNode3D](class_xrnode3d.md#class-xrnode3d), [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d)

Base object in 3D space, inherited by all 3D nodes.

## Description

The **Node3D** node is the base representation of a node in 3D space. All other 3D nodes inherit from this class.

Affine operations (translation, rotation, scale) are calculated in the coordinate system relative to the parent, unless the **Node3D**'s top_level is `true`. In this coordinate system, affine operations correspond to direct affine operations on the **Node3D**'s transform. The term *parent space* refers to this coordinate system. The coordinate system that is attached to the **Node3D** itself is referred to as object-local coordinate system, or *local space*.

**Note:** Unless otherwise specified, all methods that need angle parameters must receive angles in *radians*. To convert degrees to radians, use [@GlobalScope.deg_to_rad()](class_@globalscope.md#class-globalscope-method-deg-to-rad).

**Note:** In Godot 3 and older, **Node3D** was named *Spatial*.

## Tutorials

- [Introduction to 3D](../tutorials/3d/introduction_to_3d.md)
- [All 3D Demos](https://github.com/godotengine/godot-demo-projects/tree/master/3d)

## Properties

| [Basis](class_basis.md#class-basis)                             | basis                                     |                                                   |
|-----------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------|
| [Basis](class_basis.md#class-basis)                             | global_basis                       |                                                   |
| [Vector3](class_vector3.md#class-vector3)                       | global_position                 |                                                   |
| [Vector3](class_vector3.md#class-vector3)                       | global_rotation                 |                                                   |
| [Vector3](class_vector3.md#class-vector3)                       | global_rotation_degrees |                                                   |
| [Transform3D](class_transform3d.md#class-transform3d)           | global_transform               |                                                   |
| [Vector3](class_vector3.md#class-vector3)                       | position                               | `Vector3(0, 0, 0)`                                |
| [Quaternion](class_quaternion.md#class-quaternion)              | quaternion                           |                                                   |
| [Vector3](class_vector3.md#class-vector3)                       | rotation                               | `Vector3(0, 0, 0)`                                |
| [Vector3](class_vector3.md#class-vector3)                       | rotation_degrees               |                                                   |
| RotationEditMode               | rotation_edit_mode           | `0`                                               |
| [EulerOrder](class_@globalscope.md#enum-globalscope-eulerorder) | rotation_order                   | `2`                                               |
| [Vector3](class_vector3.md#class-vector3)                       | scale                                     | `Vector3(1, 1, 1)`                                |
| [bool](class_bool.md#class-bool)                                | top_level                             | `false`                                           |
| [Transform3D](class_transform3d.md#class-transform3d)           | transform                             | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| [NodePath](class_nodepath.md#class-nodepath)                    | visibility_parent             | `NodePath("")`                                    |
| [bool](class_bool.md#class-bool)                                | visible                                 | `true`                                            |

## Methods

|                                                                                            | add_gizmo(gizmo: [Node3DGizmo](class_node3dgizmo.md#class-node3dgizmo))                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                            | clear_gizmos()                                                                                                                                                                                                                                                      |
|                                                                                            | clear_subgizmo_selection()                                                                                                                                                                                                                              |
|                                                                                            | force_update_transform()                                                                                                                                                                                                                                  |
| [Array](class_array.md#class-array)[[Node3DGizmo](class_node3dgizmo.md#class-node3dgizmo)] | get_gizmos()                                                                                                                                                                                                                                                          |
| [Transform3D](class_transform3d.md#class-transform3d)                                      | get_global_transform_interpolated()                                                                                                                                                                                                            |
| Node3D                                                                    | get_parent_node_3d()                                                                                                                                                                                                                                          |
| [World3D](class_world3d.md#class-world3d)                                                  | get_world_3d()                                                                                                                                                                                                                                                      |
|                                                                                            | global_rotate(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))                                                                                                                                                         |
|                                                                                            | global_scale(scale: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                      |
|                                                                                            | global_translate(offset: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                             |
|                                                                                            | hide()                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                           | is_local_transform_notification_enabled()                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                           | is_scale_disabled()                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                           | is_transform_notification_enabled()                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                           | is_visible_in_tree()                                                                                                                                                                                                                                          |
|                                                                                            | look_at(target: [Vector3](class_vector3.md#class-vector3), up: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class-bool) = false)                                                                                  |
|                                                                                            | look_at_from_position(position: [Vector3](class_vector3.md#class-vector3), target: [Vector3](class_vector3.md#class-vector3), up: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class-bool) = false) |
|                                                                                            | orthonormalize()                                                                                                                                                                                                                                                  |
|                                                                                            | rotate(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))                                                                                                                                                                       |
|                                                                                            | rotate_object_local(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))                                                                                                                                             |
|                                                                                            | rotate_x(angle: [float](class_float.md#class-float))                                                                                                                                                                                                                    |
|                                                                                            | rotate_y(angle: [float](class_float.md#class-float))                                                                                                                                                                                                                    |
|                                                                                            | rotate_z(angle: [float](class_float.md#class-float))                                                                                                                                                                                                                    |
|                                                                                            | scale_object_local(scale: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                          |
|                                                                                            | set_disable_scale(disable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                   |
|                                                                                            | set_identity()                                                                                                                                                                                                                                                      |
|                                                                                            | set_ignore_transform_notification(enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                   |
|                                                                                            | set_notify_local_transform(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                  |
|                                                                                            | set_notify_transform(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                              |
|                                                                                            | set_subgizmo_selection(gizmo: [Node3DGizmo](class_node3dgizmo.md#class-node3dgizmo), id: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                 |
|                                                                                            | show()                                                                                                                                                                                                                                                                      |
| [Vector3](class_vector3.md#class-vector3)                                                  | to_global(local_point: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                      |
| [Vector3](class_vector3.md#class-vector3)                                                  | to_local(global_point: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                       |
|                                                                                            | translate(offset: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                           |
|                                                                                            | translate_object_local(offset: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                 |
|                                                                                            | update_gizmos()                                                                                                                                                                                                                                                    |

---

## Signals

**visibility_changed**()

Emitted when this node's visibility changes (see visible and is_visible_in_tree()).

This signal is emitted *after* the related NOTIFICATION_VISIBILITY_CHANGED notification.

---

## Enumerations

enum **RotationEditMode**:

RotationEditMode **ROTATION_EDIT_MODE_EULER** = `0`

The rotation is edited using a [Vector3](class_vector3.md#class-vector3) in [Euler angles](https://en.wikipedia.org/wiki/Euler_angles). In Godot, Euler angles always use intrinsic order, meaning that rotation happens around the local axes of the object.

RotationEditMode **ROTATION_EDIT_MODE_QUATERNION** = `1`

The rotation is edited using a [Quaternion](class_quaternion.md#class-quaternion). Quaternions avoid [gimbal lock](../tutorials/3d/using_transforms.md) and having to choose an order of rotation, but are less intuitive. Quaternion rotation is mostly the same as rotors in 3D geometric algebra, except that the numbers are labeled differently.

RotationEditMode **ROTATION_EDIT_MODE_BASIS** = `2`

The rotation is edited using a [Basis](class_basis.md#class-basis). In this mode, the raw basis's axes can be freely modified, but the scale property is not available.

---

## Constants

**NOTIFICATION_TRANSFORM_CHANGED** = `2000`

Notification received when this node's global_transform changes, if is_transform_notification_enabled() is `true`. See also set_notify_transform().

**Note:** Most 3D nodes such as [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) or [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) automatically enable this to function correctly.

**Note:** In the editor, nodes will propagate this notification to their children if a gizmo is attached (see add_gizmo()).

**NOTIFICATION_ENTER_WORLD** = `41`

Notification received when this node is registered to a new [World3D](class_world3d.md#class-world3d) (see get_world_3d()).

**NOTIFICATION_EXIT_WORLD** = `42`

Notification received when this node is unregistered from the current [World3D](class_world3d.md#class-world3d) (see get_world_3d()).

This notification is sent in reversed order.

**NOTIFICATION_VISIBILITY_CHANGED** = `43`

Notification received when this node's visibility changes (see visible and is_visible_in_tree()).

This notification is received *before* the related visibility_changed signal.

**NOTIFICATION_LOCAL_TRANSFORM_CHANGED** = `44`

Notification received when this node's transform changes, if is_local_transform_notification_enabled() is `true`. This is not received when a parent **Node3D**'s transform changes. See also set_notify_local_transform().

**Note:** Some 3D nodes such as [CSGShape3D](class_csgshape3d.md#class-csgshape3d) or [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) automatically enable this to function correctly.

---

## Property Descriptions

[Basis](class_basis.md#class-basis) **basis**

-  **set_basis**(value: [Basis](class_basis.md#class-basis))
- [Basis](class_basis.md#class-basis) **get_basis**()

Basis of the transform property. Represents the rotation, scale, and shear of this node in parent space (relative to the parent node).

---

[Basis](class_basis.md#class-basis) **global_basis**

-  **set_global_basis**(value: [Basis](class_basis.md#class-basis))
- [Basis](class_basis.md#class-basis) **get_global_basis**()

Basis of the global_transform property. Represents the rotation, scale, and shear of this node in global space (relative to the world).

**Note:** If the node is not inside the tree, getting this property fails and returns [Basis.IDENTITY](class_basis.md#class-basis-constant-identity).

---

[Vector3](class_vector3.md#class-vector3) **global_position**

-  **set_global_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_global_position**()

Global position (translation) of this node in global space (relative to the world). This is equivalent to the global_transform's [Transform3D.origin](class_transform3d.md#class-transform3d-property-origin).

**Note:** If the node is not inside the tree, getting this property fails and returns [Vector3.ZERO](class_vector3.md#class-vector3-constant-zero).

---

[Vector3](class_vector3.md#class-vector3) **global_rotation**

-  **set_global_rotation**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_global_rotation**()

Global rotation of this node as [Euler angles](https://en.wikipedia.org/wiki/Euler_angles), in radians and in global space (relative to the world). This value is obtained from global_basis's rotation.

- The [Vector3.x](class_vector3.md#class-vector3-property-x) is the angle around the global X axis (pitch);
- The [Vector3.y](class_vector3.md#class-vector3-property-y) is the angle around the global Y axis (yaw);
- The [Vector3.z](class_vector3.md#class-vector3-property-z) is the angle around the global Z axis (roll).

**Note:** Unlike rotation, this property always follows the YXZ convention ([@GlobalScope.EULER_ORDER_YXZ](class_@globalscope.md#class-globalscope-constant-euler-order-yxz)).

**Note:** If the node is not inside the tree, getting this property fails and returns [Vector3.ZERO](class_vector3.md#class-vector3-constant-zero).

---

[Vector3](class_vector3.md#class-vector3) **global_rotation_degrees**

-  **set_global_rotation_degrees**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_global_rotation_degrees**()

The global_rotation of this node, in degrees instead of radians.

**Note:** If the node is not inside the tree, getting this property fails and returns [Vector3.ZERO](class_vector3.md#class-vector3-constant-zero).

---

[Transform3D](class_transform3d.md#class-transform3d) **global_transform**

-  **set_global_transform**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_global_transform**()

The transformation of this node, in global space (relative to the world). Contains and represents this node's global_position, global_rotation, and global scale.

**Note:** If the node is not inside the tree, getting this property fails and returns [Transform3D.IDENTITY](class_transform3d.md#class-transform3d-constant-identity).

---

[Vector3](class_vector3.md#class-vector3) **position** = `Vector3(0, 0, 0)`

-  **set_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_position**()

Position (translation) of this node in parent space (relative to the parent node). This is equivalent to the transform's [Transform3D.origin](class_transform3d.md#class-transform3d-property-origin).

---

[Quaternion](class_quaternion.md#class-quaternion) **quaternion**

-  **set_quaternion**(value: [Quaternion](class_quaternion.md#class-quaternion))
- [Quaternion](class_quaternion.md#class-quaternion) **get_quaternion**()

Rotation of this node represented as a [Quaternion](class_quaternion.md#class-quaternion) in parent space (relative to the parent node). This value is obtained from basis's rotation.

**Note:** Quaternions are much more suitable for 3D math but are less intuitive. Setting this property can be useful for interpolation (see [Quaternion.slerp()](class_quaternion.md#class-quaternion-method-slerp)).

---

[Vector3](class_vector3.md#class-vector3) **rotation** = `Vector3(0, 0, 0)`

-  **set_rotation**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_rotation**()

Rotation of this node as [Euler angles](https://en.wikipedia.org/wiki/Euler_angles), in radians and in parent space (relative to the parent node). This value is obtained from basis's rotation.

- The [Vector3.x](class_vector3.md#class-vector3-property-x) is the angle around the local X axis (pitch);
- The [Vector3.y](class_vector3.md#class-vector3-property-y) is the angle around the local Y axis (yaw);
- The [Vector3.z](class_vector3.md#class-vector3-property-z) is the angle around the local Z axis (roll).

The order of each consecutive rotation can be changed with rotation_order (see [EulerOrder](class_@globalscope.md#enum-globalscope-eulerorder) constants). In Godot, Euler angles always use intrinsic order. By default, the intrinsic YXZ convention is used ([@GlobalScope.EULER_ORDER_YXZ](class_@globalscope.md#class-globalscope-constant-euler-order-yxz)).

**Note:** This property is edited in degrees in the inspector. If you want to use degrees in a script, use rotation_degrees.

---

[Vector3](class_vector3.md#class-vector3) **rotation_degrees**

-  **set_rotation_degrees**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_rotation_degrees**()

The rotation of this node, in degrees instead of radians.

**Note:** This is **not** the property available in the Inspector dock.

---

RotationEditMode **rotation_edit_mode** = `0`

-  **set_rotation_edit_mode**(value: RotationEditMode)
- RotationEditMode **get_rotation_edit_mode**()

How this node's rotation and scale are displayed in the Inspector dock.

---

[EulerOrder](class_@globalscope.md#enum-globalscope-eulerorder) **rotation_order** = `2`

-  **set_rotation_order**(value: [EulerOrder](class_@globalscope.md#enum-globalscope-eulerorder))
- [EulerOrder](class_@globalscope.md#enum-globalscope-eulerorder) **get_rotation_order**()

The axis rotation order of the rotation property. In Godot, Euler angles always use intrinsic order, meaning that the final orientation is calculated by rotating around the local axes in this order.

---

[Vector3](class_vector3.md#class-vector3) **scale** = `Vector3(1, 1, 1)`

-  **set_scale**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_scale**()

Scale of this node in local space (relative to this node). This value is obtained from basis's scale.

**Note:** The behavior of some 3D node types is not affected by this property. These include [Light3D](class_light3d.md#class-light3d), [Camera3D](class_camera3d.md#class-camera3d), [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d), and more.

**Warning:** The scale's components must either be all positive or all negative, and **not** exactly `0.0`. Otherwise, it won't be possible to obtain the scale from the basis. This may cause the intended scale to be lost when reloaded from disk, and potentially other unstable behavior.

---

[bool](class_bool.md#class-bool) **top_level** = `false`

-  **set_as_top_level**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_set_as_top_level**()

If `true`, the node does not inherit its transformations from its parent. As such, node transformations will only be in global space, which also means that global_transform and transform will be identical.

---

[Transform3D](class_transform3d.md#class-transform3d) **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`

-  **set_transform**(value: [Transform3D](class_transform3d.md#class-transform3d))
- [Transform3D](class_transform3d.md#class-transform3d) **get_transform**()

The local transformation of this node, in parent space (relative to the parent node). Contains and represents this node's position, rotation, and scale.

---

[NodePath](class_nodepath.md#class-nodepath) **visibility_parent** = `NodePath("")`

-  **set_visibility_parent**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_visibility_parent**()

Path to the visibility range parent for this node and its descendants. The visibility parent must be a [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d).

Any visual instance will only be visible if the visibility parent (and all of its visibility ancestors) is hidden by being closer to the camera than its own [GeometryInstance3D.visibility_range_begin](class_geometryinstance3d.md#class-geometryinstance3d-property-visibility-range-begin). Nodes hidden via the visible property are essentially removed from the visibility dependency tree, so dependent instances will not take the hidden node or its descendants into account.

---

[bool](class_bool.md#class-bool) **visible** = `true`

-  **set_visible**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_visible**()

If `true`, this node can be visible. The node is only rendered when all of its ancestors are visible, as well. That means is_visible_in_tree() must return `true`.

---

## Method Descriptions

 **add_gizmo**(gizmo: [Node3DGizmo](class_node3dgizmo.md#class-node3dgizmo))

Attaches the given `gizmo` to this node. Only works in the editor.

**Note:** `gizmo` should be an [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo). The argument type is [Node3DGizmo](class_node3dgizmo.md#class-node3dgizmo) to avoid depending on editor classes in **Node3D**.

---

 **clear_gizmos**()

Clears all [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) objects attached to this node. Only works in the editor.

---

 **clear_subgizmo_selection**()

Deselects all subgizmos for this node. Useful to call when the selected subgizmo may no longer exist after a property change. Only works in the editor.

---

 **force_update_transform**()

Forces the node's global_transform to update, by sending NOTIFICATION_TRANSFORM_CHANGED. Fails if the node is not inside the tree.

**Note:** For performance reasons, transform changes are usually accumulated and applied *once* at the end of the frame. The update propagates through **Node3D** children, as well. Therefore, use this method only when you need an up-to-date transform (such as during physics operations).

---

[Array](class_array.md#class-array)[[Node3DGizmo](class_node3dgizmo.md#class-node3dgizmo)] **get_gizmos**()

Returns all the [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) objects attached to this node. Only works in the editor.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_global_transform_interpolated**()

When using physics interpolation, there will be circumstances in which you want to know the interpolated (displayed) transform of a node rather than the standard transform (which may only be accurate to the most recent physics tick).

This is particularly important for frame-based operations that take place in [Node._process()](class_node.md#class-node-private-method-process), rather than [Node._physics_process()](class_node.md#class-node-private-method-physics-process). Examples include [Camera3D](class_camera3d.md#class-camera3d)s focusing on a node, or finding where to fire lasers from on a frame rather than physics tick.

**Note:** This function creates an interpolation pump on the **Node3D** the first time it is called, which can respond to physics interpolation resets. If you get problems with "streaking" when initially following a **Node3D**, be sure to call get_global_transform_interpolated() at least once *before* resetting the **Node3D** physics interpolation.

---

Node3D **get_parent_node_3d**()

Returns the parent **Node3D** that directly affects this node's global_transform. Returns `null` if no parent exists, the parent is not a **Node3D**, or top_level is `true`.

**Note:** This method is not always equivalent to [Node.get_parent()](class_node.md#class-node-method-get-parent), which does not take top_level into account.

---

[World3D](class_world3d.md#class-world3d) **get_world_3d**()

Returns the [World3D](class_world3d.md#class-world3d) this node is registered to.

Usually, this is the same as the world used by this node's viewport (see [Node.get_viewport()](class_node.md#class-node-method-get-viewport) and [Viewport.find_world_3d()](class_viewport.md#class-viewport-method-find-world-3d)).

---

 **global_rotate**(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))

Rotates this node's global_basis around the global `axis` by the given `angle`, in radians. This operation is calculated in global space (relative to the world) and preserves the global_position.

---

 **global_scale**(scale: [Vector3](class_vector3.md#class-vector3))

Scales this node's global_basis by the given `scale` factor. This operation is calculated in global space (relative to the world) and preserves the global_position.

**Note:** This method is not to be confused with the scale property.

---

 **global_translate**(offset: [Vector3](class_vector3.md#class-vector3))

Adds the given translation `offset` to the node's global_position in global space (relative to the world).

---

 **hide**()

Prevents this node from being rendered. Equivalent to setting visible to `false`. This is the opposite of show().

---

[bool](class_bool.md#class-bool) **is_local_transform_notification_enabled**()

Returns `true` if the node receives NOTIFICATION_LOCAL_TRANSFORM_CHANGED whenever transform changes. This is enabled with set_notify_local_transform().

---

[bool](class_bool.md#class-bool) **is_scale_disabled**()

Returns `true` if this node's global_transform is automatically orthonormalized. This results in this node not appearing distorted, as if its global scale were set to [Vector3.ONE](class_vector3.md#class-vector3-constant-one) (or its negative counterpart). See also set_disable_scale() and orthonormalize().

**Note:** transform is not affected by this setting.

---

[bool](class_bool.md#class-bool) **is_transform_notification_enabled**()

Returns `true` if the node receives NOTIFICATION_TRANSFORM_CHANGED whenever global_transform changes. This is enabled with set_notify_transform().

---

[bool](class_bool.md#class-bool) **is_visible_in_tree**()

Returns `true` if this node is inside the scene tree and the visible property is `true` for this node and all of its **Node3D** ancestors *in sequence*. An ancestor of any other type (such as [Node](class_node.md#class-node) or [Node2D](class_node2d.md#class-node2d)) breaks the sequence. See also [Node.get_parent()](class_node.md#class-node-method-get-parent).

**Note:** This method cannot take [VisualInstance3D.layers](class_visualinstance3d.md#class-visualinstance3d-property-layers) into account, so even if this method returns `true`, the node may not be rendered.

---

 **look_at**(target: [Vector3](class_vector3.md#class-vector3), up: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class-bool) = false)

Rotates the node so that the local forward axis (-Z, [Vector3.FORWARD](class_vector3.md#class-vector3-constant-forward)) points toward the `target` position. This operation is calculated in global space (relative to the world).

The local up axis (+Y) points as close to the `up` vector as possible while staying perpendicular to the local forward axis. The resulting transform is orthogonal, and the scale is preserved. Non-uniform scaling may not work correctly.

The `target` position cannot be the same as the node's position, the `up` vector cannot be [Vector3.ZERO](class_vector3.md#class-vector3-constant-zero). Furthermore, the direction from the node's position to the `target` position cannot be parallel to the `up` vector, to avoid an unintended rotation around the local Z axis.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward the `target` position. By default, the -Z axis (camera forward) is treated as forward (implies +X is right).

**Note:** This method fails if the node is not in the scene tree. If necessary, use look_at_from_position() instead.

---

 **look_at_from_position**(position: [Vector3](class_vector3.md#class-vector3), target: [Vector3](class_vector3.md#class-vector3), up: [Vector3](class_vector3.md#class-vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class-bool) = false)

Moves the node to the specified `position`, then rotates the node to point toward the `target` position, similar to look_at(). This operation is calculated in global space (relative to the world).

---

 **orthonormalize**()

Orthonormalizes this node's basis. This method sets this node's scale to [Vector3.ONE](class_vector3.md#class-vector3-constant-one) (or its negative counterpart), but preserves the position and rotation. See also [Transform3D.orthonormalized()](class_transform3d.md#class-transform3d-method-orthonormalized).

---

 **rotate**(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))

Rotates this node's basis around the `axis` by the given `angle`, in radians. This operation is calculated in parent space (relative to the parent) and preserves the position.

---

 **rotate_object_local**(axis: [Vector3](class_vector3.md#class-vector3), angle: [float](class_float.md#class-float))

Rotates this node's basis around the `axis` by the given `angle`, in radians. This operation is calculated in local space (relative to this node) and preserves the position.

---

 **rotate_x**(angle: [float](class_float.md#class-float))

Rotates this node's basis around the X axis by the given `angle`, in radians. This operation is calculated in parent space (relative to the parent) and preserves the position.

---

 **rotate_y**(angle: [float](class_float.md#class-float))

Rotates this node's basis around the Y axis by the given `angle`, in radians. This operation is calculated in parent space (relative to the parent) and preserves the position.

---

 **rotate_z**(angle: [float](class_float.md#class-float))

Rotates this node's basis around the Z axis by the given `angle`, in radians. This operation is calculated in parent space (relative to the parent) and preserves the position.

---

 **scale_object_local**(scale: [Vector3](class_vector3.md#class-vector3))

Scales this node's basis by the given `scale` factor. This operation is calculated in local space (relative to this node) and preserves the position.

---

 **set_disable_scale**(disable: [bool](class_bool.md#class-bool))

If `true`, this node's global_transform is automatically orthonormalized. This results in this node not appearing distorted, as if its global scale were set to [Vector3.ONE](class_vector3.md#class-vector3-constant-one) (or its negative counterpart). See also is_scale_disabled() and orthonormalize().

**Note:** transform is not affected by this setting.

---

 **set_identity**()

Sets this node's transform to [Transform3D.IDENTITY](class_transform3d.md#class-transform3d-constant-identity), which resets all transformations in parent space (position, rotation, and scale).

---

 **set_ignore_transform_notification**(enabled: [bool](class_bool.md#class-bool))

If `true`, the node will not receive NOTIFICATION_TRANSFORM_CHANGED or NOTIFICATION_LOCAL_TRANSFORM_CHANGED.

It may useful to call this method when handling these notifications to prevent infinite recursion.

---

 **set_notify_local_transform**(enable: [bool](class_bool.md#class-bool))

If `true`, the node will receive NOTIFICATION_LOCAL_TRANSFORM_CHANGED whenever transform changes.

**Note:** Some 3D nodes such as [CSGShape3D](class_csgshape3d.md#class-csgshape3d) or [CollisionShape3D](class_collisionshape3d.md#class-collisionshape3d) automatically enable this to function correctly.

---

 **set_notify_transform**(enable: [bool](class_bool.md#class-bool))

If `true`, the node will receive NOTIFICATION_TRANSFORM_CHANGED whenever global_transform changes.

**Note:** Most 3D nodes such as [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) or [CollisionObject3D](class_collisionobject3d.md#class-collisionobject3d) automatically enable this to function correctly.

**Note:** In the editor, nodes will propagate this notification to their children if a gizmo is attached (see add_gizmo()).

---

 **set_subgizmo_selection**(gizmo: [Node3DGizmo](class_node3dgizmo.md#class-node3dgizmo), id: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))

Selects the `gizmo`'s subgizmo with the given `id` and sets its transform. Only works in the editor.

**Note:** The gizmo object would typically be an instance of [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo), but the argument type is kept generic to avoid creating a dependency on editor classes in **Node3D**.

---

 **show**()

Allows this node to be rendered. Equivalent to setting visible to `true`. This is the opposite of hide().

---

[Vector3](class_vector3.md#class-vector3) **to_global**(local_point: [Vector3](class_vector3.md#class-vector3))

Returns the `local_point` converted from this node's local space to global space. This is the opposite of to_local().

---

[Vector3](class_vector3.md#class-vector3) **to_local**(global_point: [Vector3](class_vector3.md#class-vector3))

Returns the `global_point` converted from global space to this node's local space. This is the opposite of to_global().

---

 **translate**(offset: [Vector3](class_vector3.md#class-vector3))

Adds the given translation `offset` to the node's position, in local space (relative to this node).

**Note:** Prefer using translate_object_local(), instead, as this method may be changed in a future release.

**Note:** Despite the naming convention, this operation is **not** calculated in parent space for compatibility reasons. To translate in parent space, add `offset` to the position (`node_3d.position += offset`).

---

 **translate_object_local**(offset: [Vector3](class_vector3.md#class-vector3))

Adds the given translation `offset` to the node's position, in local space (relative to this node).

---

 **update_gizmos**()

Updates all the [EditorNode3DGizmo](class_editornode3dgizmo.md#class-editornode3dgizmo) objects attached to this node. Only works in the editor.
