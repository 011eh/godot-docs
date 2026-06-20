# XRInterfaceExtension

**Inherits:** [XRInterface](class_xrinterface.md#class-xrinterface) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Base class for XR interface extensions (plugins).

## Description

External XR interface plugins should inherit from this class.

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

## Methods

|                                                                            | \_end_frame()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                                           | \_get_anchor_detection_is_enabled()                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                              | \_get_camera_feed_id()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Transform3D](class_transform3d.md#class-transform3d)                      | \_get_camera_transform()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                              | \_get_capabilities()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                              | \_get_color_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [RID](class_rid.md#class-rid)                                              | \_get_depth_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [StringName](class_stringname.md#class-stringname)                         | \_get_name()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) | \_get_play_area()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode)         | \_get_play_area_mode()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) | \_get_projection_for_view(view: [int](class_int.md#class-int), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                   |
| [Vector2](class_vector2.md#class-vector2)                                  | \_get_render_target_size()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)    | \_get_suggested_pose_names(tracker_name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)    | \_get_suggested_tracker_names()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dictionary](class_dictionary.md#class-dictionary)                         | \_get_system_info()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [TrackingStatus](class_xrinterface.md#enum-xrinterface-trackingstatus)     | \_get_tracking_status()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Transform3D](class_transform3d.md#class-transform3d)                      | \_get_transform_for_view(view: [int](class_int.md#class-int), cam_transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                                                                                                                                                     |
| [RID](class_rid.md#class-rid)                                              | \_get_velocity_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                              | \_get_view_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [RID](class_rid.md#class-rid)                                              | \_get_vrs_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [VRSTextureFormat](class_xrinterface.md#enum-xrinterface-vrstextureformat) | \_get_vrs_texture_format()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                           | \_initialize()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                           | \_is_initialized()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                            | \_post_draw_viewport(render_target: [RID](class_rid.md#class-rid), screen_rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                           | \_pre_draw_viewport(render_target: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                            | \_pre_render()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                            | \_process()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                            | \_set_anchor_detection_is_enabled(enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                           | \_set_play_area_mode(mode: [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode))                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                           | \_supports_play_area_mode(mode: [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode))                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                            | \_trigger_haptic_pulse(action_name: [String](class_string.md#class-string), tracker_name: [StringName](class_stringname.md#class-stringname), frequency: [float](class_float.md#class-float), amplitude: [float](class_float.md#class-float), duration_sec: [float](class_float.md#class-float), delay_sec: [float](class_float.md#class-float))                                                                                                                                                                          |
|                                                                            | \_uninitialize()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                            | add_blit(render_target: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), dst_rect: [Rect2i](class_rect2i.md#class-rect2i), use_layer: [bool](class_bool.md#class-bool), layer: [int](class_int.md#class-int), apply_lens_distortion: [bool](class_bool.md#class-bool), eye_center: [Vector2](class_vector2.md#class-vector2), k1: [float](class_float.md#class-float), k2: [float](class_float.md#class-float), upscale: [float](class_float.md#class-float), aspect_ratio: [float](class_float.md#class-float)) |
| [RID](class_rid.md#class-rid)                                              | get_color_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                              | get_depth_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                              | get_render_target_texture(render_target: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                              | get_velocity_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

## Method Descriptions

 **\_end_frame**()

Called if interface is active and queues have been submitted.

---

[bool](class_bool.md#class-bool) **\_get_anchor_detection_is_enabled**()

Return `true` if anchor detection is enabled for this interface.

---

[int](class_int.md#class-int) **\_get_camera_feed_id**()

Returns the camera feed ID for the [CameraFeed](class_camerafeed.md#class-camerafeed) registered with the [CameraServer](class_cameraserver.md#class-cameraserver) that should be presented as the background on an AR capable device (if applicable).

---

[Transform3D](class_transform3d.md#class-transform3d) **\_get_camera_transform**()

Returns the [Transform3D](class_transform3d.md#class-transform3d) that positions the [XRCamera3D](class_xrcamera3d.md#class-xrcamera3d) in the world.

---

[int](class_int.md#class-int) **\_get_capabilities**()

Returns the capabilities of this interface.

---

[RID](class_rid.md#class-rid) **\_get_color_texture**()

Return color texture into which to render (if applicable).

---

[RID](class_rid.md#class-rid) **\_get_depth_texture**()

Return depth texture into which to render (if applicable).

---

[StringName](class_stringname.md#class-stringname) **\_get_name**()

Returns the name of this interface.

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **\_get_play_area**()

Returns a [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) that represents the play areas boundaries (if applicable).

---

[PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode) **\_get_play_area_mode**()

Returns the play area mode that sets up our play area.

---

[PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array) **\_get_projection_for_view**(view: [int](class_int.md#class-int), aspect: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Returns the projection matrix for the given view as a [PackedFloat64Array](class_packedfloat64array.md#class-packedfloat64array).

---

[Vector2](class_vector2.md#class-vector2) **\_get_render_target_size**()

Returns the size of our render target for this interface, this overrides the size of the [Viewport](class_viewport.md#class-viewport) marked as the xr viewport.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_suggested_pose_names**(tracker_name: [StringName](class_stringname.md#class-stringname))

Returns a [PackedStringArray](class_packedstringarray.md#class-packedstringarray) with pose names configured by this interface. Note that user configuration can override this list.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_suggested_tracker_names**()

Returns a [PackedStringArray](class_packedstringarray.md#class-packedstringarray) with tracker names configured by this interface. Note that user configuration can override this list.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_system_info**()

Returns a [Dictionary](class_dictionary.md#class-dictionary) with system information related to this interface.

---

[TrackingStatus](class_xrinterface.md#enum-xrinterface-trackingstatus) **\_get_tracking_status**()

Returns the current status of our tracking.

---

[Transform3D](class_transform3d.md#class-transform3d) **\_get_transform_for_view**(view: [int](class_int.md#class-int), cam_transform: [Transform3D](class_transform3d.md#class-transform3d))

Returns a [Transform3D](class_transform3d.md#class-transform3d) for a given view.

---

[RID](class_rid.md#class-rid) **\_get_velocity_texture**()

Return velocity texture into which to render (if applicable).

---

[int](class_int.md#class-int) **\_get_view_count**()

Returns the number of views this interface requires, 1 for mono, 2 for stereoscopic.

---

[RID](class_rid.md#class-rid) **\_get_vrs_texture**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[VRSTextureFormat](class_xrinterface.md#enum-xrinterface-vrstextureformat) **\_get_vrs_texture_format**()

Returns the format of the texture returned by \_get_vrs_texture().

---

[bool](class_bool.md#class-bool) **\_initialize**()

Initializes the interface, returns `true` on success.

---

[bool](class_bool.md#class-bool) **\_is_initialized**()

Returns `true` if this interface has been initialized.

---

 **\_post_draw_viewport**(render_target: [RID](class_rid.md#class-rid), screen_rect: [Rect2](class_rect2.md#class-rect2))

Called after the XR [Viewport](class_viewport.md#class-viewport) draw logic has completed.

---

[bool](class_bool.md#class-bool) **\_pre_draw_viewport**(render_target: [RID](class_rid.md#class-rid))

Called if this is our primary **XRInterfaceExtension** before we start processing a [Viewport](class_viewport.md#class-viewport) for every active XR [Viewport](class_viewport.md#class-viewport), returns `true` if that viewport should be rendered. An XR interface may return `false` if the user has taken off their headset and we can pause rendering.

---

 **\_pre_render**()

Called if this **XRInterfaceExtension** is active before rendering starts. Most XR interfaces will sync tracking at this point in time.

---

 **\_process**()

Called if this **XRInterfaceExtension** is active before our physics and game process is called. Most XR interfaces will update its [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker)s at this point in time.

---

 **\_set_anchor_detection_is_enabled**(enabled: [bool](class_bool.md#class-bool))

Enables anchor detection on this interface if supported.

---

[bool](class_bool.md#class-bool) **\_set_play_area_mode**(mode: [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode))

Set the play area mode for this interface.

---

[bool](class_bool.md#class-bool) **\_supports_play_area_mode**(mode: [PlayAreaMode](class_xrinterface.md#enum-xrinterface-playareamode))

Returns `true` if this interface supports this play area mode.

---

 **\_trigger_haptic_pulse**(action_name: [String](class_string.md#class-string), tracker_name: [StringName](class_stringname.md#class-stringname), frequency: [float](class_float.md#class-float), amplitude: [float](class_float.md#class-float), duration_sec: [float](class_float.md#class-float), delay_sec: [float](class_float.md#class-float))

Triggers a haptic pulse to be emitted on the specified tracker.

---

 **\_uninitialize**()

Uninitialize the interface.

---

 **add_blit**(render_target: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), dst_rect: [Rect2i](class_rect2i.md#class-rect2i), use_layer: [bool](class_bool.md#class-bool), layer: [int](class_int.md#class-int), apply_lens_distortion: [bool](class_bool.md#class-bool), eye_center: [Vector2](class_vector2.md#class-vector2), k1: [float](class_float.md#class-float), k2: [float](class_float.md#class-float), upscale: [float](class_float.md#class-float), aspect_ratio: [float](class_float.md#class-float))

Blits our render results to screen optionally applying lens distortion. This can only be called while processing `_commit_views`.

---

[RID](class_rid.md#class-rid) **get_color_texture**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **get_depth_texture**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[RID](class_rid.md#class-rid) **get_render_target_texture**(render_target: [RID](class_rid.md#class-rid))

Returns a valid [RID](class_rid.md#class-rid) for a texture to which we should render the current frame if supported by the interface.

---

[RID](class_rid.md#class-rid) **get_velocity_texture**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!
