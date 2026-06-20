# Camera3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [XRCamera3D](class_xrcamera3d.md#class-xrcamera3d)

Camera node, displays from a point of view.

## Description

**Camera3D** is a special node that displays what is visible from its current location. Cameras register themselves in the nearest [Viewport](class_viewport.md#class-viewport) node (when ascending the tree). Only one camera can be active per viewport. If no viewport is available ascending the tree, the camera will register in the global viewport. In other words, a camera just provides 3D display capabilities to a [Viewport](class_viewport.md#class-viewport), and, without one, a scene registered in that [Viewport](class_viewport.md#class-viewport) (or higher viewports) can't be displayed.

## Tutorials

- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [CameraAttributes](class_cameraattributes.md#class-cameraattributes)   | attributes             |                 |
|------------------------------------------------------------------------|---------------------------------------------------------------|-----------------|
| [Compositor](class_compositor.md#class-compositor)                     | compositor             |                 |
| [int](class_int.md#class-int)                                          | cull_mask               | `1048575`       |
| [bool](class_bool.md#class-bool)                                       | current                   | `false`         |
| DopplerTracking                      | doppler_tracking | `0`             |
| [Environment](class_environment.md#class-environment)                  | environment           |                 |
| [float](class_float.md#class-float)                                    | far                           | `4000.0`        |
| [float](class_float.md#class-float)                                    | fov                           | `75.0`          |
| [Vector2](class_vector2.md#class-vector2)                              | frustum_offset     | `Vector2(0, 0)` |
| [float](class_float.md#class-float)                                    | h_offset                 | `0.0`           |
| KeepAspect                                | keep_aspect           | `1`             |
| [float](class_float.md#class-float)                                    | near                         | `0.05`          |
| ProjectionType                        | projection             | `0`             |
| [float](class_float.md#class-float)                                    | size                         | `1.0`           |
| [float](class_float.md#class-float)                                    | v_offset                 | `0.0`           |

## Methods

|                                                                          | clear_current(enable_next: [bool](class_bool.md#class-bool) = true)                                                                                                                              |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Projection](class_projection.md#class-projection)                       | get_camera_projection()                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                            | get_camera_rid()                                                                                                                                                                                |
| [Transform3D](class_transform3d.md#class-transform3d)                    | get_camera_transform()                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                         | get_cull_mask_value(layer_number: [int](class_int.md#class-int))                                                                                                                           |
| [Array](class_array.md#class-array)[[Plane](class_plane.md#class-plane)] | get_frustum()                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                            | get_pyramid_shape_rid()                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                         | is_position_behind(world_point: [Vector3](class_vector3.md#class-vector3))                                                                                                                  |
| [bool](class_bool.md#class-bool)                                         | is_position_in_frustum(world_point: [Vector3](class_vector3.md#class-vector3))                                                                                                          |
|                                                                          | make_current()                                                                                                                                                                                    |
| [Vector3](class_vector3.md#class-vector3)                                | project_local_ray_normal(screen_point: [Vector2](class_vector2.md#class-vector2))                                                                                                     |
| [Vector3](class_vector3.md#class-vector3)                                | project_position(screen_point: [Vector2](class_vector2.md#class-vector2), z_depth: [float](class_float.md#class-float))                                                                       |
| [Vector3](class_vector3.md#class-vector3)                                | project_ray_normal(screen_point: [Vector2](class_vector2.md#class-vector2))                                                                                                                 |
| [Vector3](class_vector3.md#class-vector3)                                | project_ray_origin(screen_point: [Vector2](class_vector2.md#class-vector2))                                                                                                                 |
|                                                                          | set_cull_mask_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))                                                                                  |
|                                                                          | set_frustum(size: [float](class_float.md#class-float), offset: [Vector2](class_vector2.md#class-vector2), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float)) |
|                                                                          | set_orthogonal(size: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))                                              |
|                                                                          | set_perspective(fov: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))                                             |
| [Vector2](class_vector2.md#class-vector2)                                | unproject_position(world_point: [Vector3](class_vector3.md#class-vector3))                                                                                                                  |

---

## Enumerations

enum **ProjectionType**:

ProjectionType **PROJECTION_PERSPECTIVE** = `0`

Perspective projection. Objects on the screen becomes smaller when they are far away.

ProjectionType **PROJECTION_ORTHOGONAL** = `1`

Orthogonal projection, also known as orthographic projection. Objects remain the same size on the screen no matter how far away they are.

ProjectionType **PROJECTION_FRUSTUM** = `2`

Frustum projection. This mode allows adjusting frustum_offset to create "tilted frustum" effects.

---

enum **KeepAspect**:

KeepAspect **KEEP_WIDTH** = `0`

Preserves the horizontal aspect ratio; also known as Vert- scaling. This is usually the best option for projects running in portrait mode, as taller aspect ratios will benefit from a wider vertical FOV.

KeepAspect **KEEP_HEIGHT** = `1`

Preserves the vertical aspect ratio; also known as Hor+ scaling. This is usually the best option for projects running in landscape mode, as wider aspect ratios will automatically benefit from a wider horizontal FOV.

---

enum **DopplerTracking**:

DopplerTracking **DOPPLER_TRACKING_DISABLED** = `0`

Disables [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) simulation (default).

DopplerTracking **DOPPLER_TRACKING_IDLE_STEP** = `1`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_process`. Changes in the relative velocity of this camera compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-pitch-scale)).

DopplerTracking **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_physics_process`. Changes in the relative velocity of this camera compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-pitch-scale)).

---

## Property Descriptions

[CameraAttributes](class_cameraattributes.md#class-cameraattributes) **attributes**

-  **set_attributes**(value: [CameraAttributes](class_cameraattributes.md#class-cameraattributes))
- [CameraAttributes](class_cameraattributes.md#class-cameraattributes) **get_attributes**()

The [CameraAttributes](class_cameraattributes.md#class-cameraattributes) to use for this camera.

---

[Compositor](class_compositor.md#class-compositor) **compositor**

-  **set_compositor**(value: [Compositor](class_compositor.md#class-compositor))
- [Compositor](class_compositor.md#class-compositor) **get_compositor**()

The [Compositor](class_compositor.md#class-compositor) to use for this camera.

---

[int](class_int.md#class-int) **cull_mask** = `1048575`

-  **set_cull_mask**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_cull_mask**()

The culling mask that describes which [VisualInstance3D.layers](class_visualinstance3d.md#class-visualinstance3d-property-layers) are rendered by this camera. By default, all 20 user-visible layers are rendered.

**Note:** Since the cull_mask allows for 32 layers to be stored in total, there are an additional 12 layers that are only used internally by the engine and aren't exposed in the editor. Setting cull_mask using a script allows you to toggle those reserved layers, which can be useful for editor plugins.

To adjust cull_mask more easily using a script, use get_cull_mask_value() and set_cull_mask_value().

**Note:** [VoxelGI](class_voxelgi.md#class-voxelgi), SDFGI and [LightmapGI](class_lightmapgi.md#class-lightmapgi) will always take all layers into account to determine what contributes to global illumination. If this is an issue, set [GeometryInstance3D.gi_mode](class_geometryinstance3d.md#class-geometryinstance3d-property-gi-mode) to [GeometryInstance3D.GI_MODE_DISABLED](class_geometryinstance3d.md#class-geometryinstance3d-constant-gi-mode-disabled) for meshes and [Light3D.light_bake_mode](class_light3d.md#class-light3d-property-light-bake-mode) to [Light3D.BAKE_DISABLED](class_light3d.md#class-light3d-constant-bake-disabled) for lights to exclude them from global illumination.

---

[bool](class_bool.md#class-bool) **current** = `false`

-  **set_current**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_current**()

If `true`, the ancestor [Viewport](class_viewport.md#class-viewport) is currently using this camera.

If multiple cameras are in the scene, one will always be made current. For example, if two **Camera3D** nodes are present in the scene and only one is current, setting one camera's current to `false` will cause the other camera to be made current.

---

DopplerTracking **doppler_tracking** = `0`

-  **set_doppler_tracking**(value: DopplerTracking)
- DopplerTracking **get_doppler_tracking**()

If not DOPPLER_TRACKING_DISABLED, this camera will simulate the [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) for objects changed in particular `_process` methods.

**Note:** The Doppler effect will only be heard on [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d)s if [AudioStreamPlayer3D.doppler_tracking](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-doppler-tracking) is not set to [AudioStreamPlayer3D.DOPPLER_TRACKING_DISABLED](class_audiostreamplayer3d.md#class-audiostreamplayer3d-constant-doppler-tracking-disabled).

---

[Environment](class_environment.md#class-environment) **environment**

-  **set_environment**(value: [Environment](class_environment.md#class-environment))
- [Environment](class_environment.md#class-environment) **get_environment**()

The [Environment](class_environment.md#class-environment) to use for this camera.

---

[float](class_float.md#class-float) **far** = `4000.0`

-  **set_far**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_far**()

The distance to the far culling boundary for this camera relative to its local Z axis. Higher values allow the camera to see further away, while decreasing far can improve performance if it results in objects being partially or fully culled.

---

[float](class_float.md#class-float) **fov** = `75.0`

-  **set_fov**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_fov**()

The camera's field of view angle (in degrees). Only applicable in perspective mode. Since keep_aspect locks one axis, fov sets the other axis' field of view angle.

For reference, the default vertical field of view value (`75.0`) is equivalent to a horizontal FOV of:

- ~91.31 degrees in a 4:3 viewport
- ~101.67 degrees in a 16:10 viewport
- ~107.51 degrees in a 16:9 viewport
- ~121.63 degrees in a 21:9 viewport

---

[Vector2](class_vector2.md#class-vector2) **frustum_offset** = `Vector2(0, 0)`

-  **set_frustum_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_frustum_offset**()

The camera's frustum offset. This can be changed from the default to create "tilted frustum" effects such as [Y-shearing](https://zdoom.org/wiki/Y-shearing).

**Note:** Only effective if projection is PROJECTION_FRUSTUM.

---

[float](class_float.md#class-float) **h_offset** = `0.0`

-  **set_h_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_h_offset**()

The horizontal (X) offset of the camera viewport.

---

KeepAspect **keep_aspect** = `1`

-  **set_keep_aspect_mode**(value: KeepAspect)
- KeepAspect **get_keep_aspect_mode**()

The axis to lock during fov/size adjustments. Can be either KEEP_WIDTH or KEEP_HEIGHT.

---

[float](class_float.md#class-float) **near** = `0.05`

-  **set_near**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_near**()

The distance to the near culling boundary for this camera relative to its local Z axis. Lower values allow the camera to see objects more up close to its origin, at the cost of lower precision across the *entire* range. Values lower than the default can lead to increased Z-fighting.

---

ProjectionType **projection** = `0`

-  **set_projection**(value: ProjectionType)
- ProjectionType **get_projection**()

The camera's projection mode. In PROJECTION_PERSPECTIVE mode, objects' Z distance from the camera's local space scales their perceived size.

---

[float](class_float.md#class-float) **size** = `1.0`

-  **set_size**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_size**()

The camera's size in meters measured as the diameter of the width or height, depending on keep_aspect. Only applicable in orthogonal and frustum modes.

---

[float](class_float.md#class-float) **v_offset** = `0.0`

-  **set_v_offset**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_v_offset**()

The vertical (Y) offset of the camera viewport.

---

## Method Descriptions

 **clear_current**(enable_next: [bool](class_bool.md#class-bool) = true)

If this is the current camera, remove it from being current. If `enable_next` is `true`, request to make the next camera current, if any.

---

[Projection](class_projection.md#class-projection) **get_camera_projection**()

Returns the projection matrix that this camera uses to render to its associated viewport. The camera must be part of the scene tree to function.

---

[RID](class_rid.md#class-rid) **get_camera_rid**()

Returns the camera's RID from the [RenderingServer](class_renderingserver.md#class-renderingserver).

---

[Transform3D](class_transform3d.md#class-transform3d) **get_camera_transform**()

Returns the transform of the camera plus the vertical (v_offset) and horizontal (h_offset) offsets; and any other adjustments made to the position and orientation of the camera by subclassed cameras such as [XRCamera3D](class_xrcamera3d.md#class-xrcamera3d).

---

[bool](class_bool.md#class-bool) **get_cull_mask_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the cull_mask is enabled, given a `layer_number` between 1 and 20.

---

[Array](class_array.md#class-array)[[Plane](class_plane.md#class-plane)] **get_frustum**()

Returns the camera's frustum planes in world space units as an array of [Plane](class_plane.md#class-plane)s in the following order: near, far, left, top, right, bottom. Not to be confused with frustum_offset.

---

[RID](class_rid.md#class-rid) **get_pyramid_shape_rid**()

Returns the RID of a pyramid shape encompassing the camera's view frustum, ignoring the camera's near plane. The tip of the pyramid represents the position of the camera.

---

[bool](class_bool.md#class-bool) **is_position_behind**(world_point: [Vector3](class_vector3.md#class-vector3))

Returns `true` if the given position is behind the camera (the blue part of the linked diagram). [See this diagram](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/camera3d_position_frustum.png) for an overview of position query methods.

**Note:** A position which returns `false` may still be outside the camera's field of view.

---

[bool](class_bool.md#class-bool) **is_position_in_frustum**(world_point: [Vector3](class_vector3.md#class-vector3))

Returns `true` if the given position is inside the camera's frustum (the green part of the linked diagram). [See this diagram](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/camera3d_position_frustum.png) for an overview of position query methods.

---

 **make_current**()

Makes this camera the current camera for the [Viewport](class_viewport.md#class-viewport) (see class description). If the camera node is outside the scene tree, it will attempt to become current once it's added.

---

[Vector3](class_vector3.md#class-vector3) **project_local_ray_normal**(screen_point: [Vector2](class_vector2.md#class-vector2))

Returns a normal vector from the screen point location directed along the camera. Orthogonal cameras are normalized. Perspective cameras account for perspective, screen width/height, etc.

---

[Vector3](class_vector3.md#class-vector3) **project_position**(screen_point: [Vector2](class_vector2.md#class-vector2), z_depth: [float](class_float.md#class-float))

Returns the 3D point in world space that maps to the given 2D coordinate in the [Viewport](class_viewport.md#class-viewport) rectangle on a plane that is the given `z_depth` distance into the scene away from the camera.

---

[Vector3](class_vector3.md#class-vector3) **project_ray_normal**(screen_point: [Vector2](class_vector2.md#class-vector2))

Returns a normal vector in world space, that is the result of projecting a point on the [Viewport](class_viewport.md#class-viewport) rectangle by the inverse camera projection. This is useful for casting rays in the form of (origin, normal) for object intersection or picking.

---

[Vector3](class_vector3.md#class-vector3) **project_ray_origin**(screen_point: [Vector2](class_vector2.md#class-vector2))

Returns a 3D position in world space, that is the result of projecting a point on the [Viewport](class_viewport.md#class-viewport) rectangle by the inverse camera projection. This is useful for casting rays in the form of (origin, normal) for object intersection or picking.

---

 **set_cull_mask_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the cull_mask, given a `layer_number` between 1 and 20.

---

 **set_frustum**(size: [float](class_float.md#class-float), offset: [Vector2](class_vector2.md#class-vector2), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Sets the camera projection to frustum mode (see PROJECTION_FRUSTUM), by specifying a `size`, an `offset`, and the `z_near` and `z_far` clip planes in world space units. The `size` parameter represents the size of the near plane, either its width or height depending on the value of keep_aspect. See also frustum_offset.

---

 **set_orthogonal**(size: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Sets the camera projection to orthogonal mode (see PROJECTION_ORTHOGONAL), by specifying a `size`, and the `z_near` and `z_far` clip planes in world space units.

As a hint, 3D games that look 2D often use this projection, with `size` specified in pixels.

---

 **set_perspective**(fov: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Sets the camera projection to perspective mode (see PROJECTION_PERSPECTIVE), by specifying a `fov` (field of view) angle in degrees, and the `z_near` and `z_far` clip planes in world space units.

---

[Vector2](class_vector2.md#class-vector2) **unproject_position**(world_point: [Vector3](class_vector3.md#class-vector3))

Returns the 2D coordinate in the [Viewport](class_viewport.md#class-viewport) rectangle that maps to the given 3D point in world space.

**Note:** When using this to position GUI elements over a 3D viewport, use is_position_behind() to prevent them from appearing if the 3D point is behind the camera:

```gdscript
# This code block is part of a script that inherits from Node3D.
# `control` is a reference to a node inheriting from Control.
control.visible = not get_viewport().get_camera_3d().is_position_behind(global_transform.origin)
control.position = get_viewport().get_camera_3d().unproject_position(global_transform.origin)
```
