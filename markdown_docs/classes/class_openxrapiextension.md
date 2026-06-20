# OpenXRAPIExtension

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Makes the OpenXR API available for GDExtension.

## Description

**OpenXRAPIExtension** makes OpenXR available for GDExtension. It provides the OpenXR API to GDExtension through the get_instance_proc_addr() method, and the OpenXR instance through get_instance().

It also provides methods for querying the status of OpenXR initialization, and helper methods for ease of use of the API with GDExtension.

## Tutorials

- [XrResult documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html)
- [XrInstance documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrInstance.html)
- [XrSpace documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html)
- [XrSession documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSession.html)
- [XrSystemId documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSystemId.html)
- [xrBeginSession documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrBeginSession.html)
- [XrPosef documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrPosef.html)

## Methods

| [int](class_int.md#class-int)                                                       | action_get_handle(action: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                     | begin_debug_label_region(label_name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                    | can_render()                                                                                                                                                                                                                                                                                                                                        |
|                                                                                     | end_debug_label_region()                                                                                                                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)                                                       | find_action(name: [String](class_string.md#class-string), action_set: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                               |
| [String](class_string.md#class-string)                                              | get_error_string(result: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                       |
| [int](class_int.md#class-int)                                                       | get_hand_tracker(hand_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                       | get_instance()                                                                                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                                       | get_instance_proc_addr(name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                                       | get_next_frame_time()                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                       | get_openxr_version()                                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                       | get_play_space()                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                       | get_predicted_display_time()                                                                                                                                                                                                                                                                                                        |
| [int](class_int.md#class-int)                                                       | get_projection_layer()                                                                                                                                                                                                                                                                                                                    |
| [float](class_float.md#class-float)                                                 | get_render_state_z_far()                                                                                                                                                                                                                                                                                                                |
| [float](class_float.md#class-float)                                                 | get_render_state_z_near()                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                       | get_session()                                                                                                                                                                                                                                                                                                                                      |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array)                | get_supported_swapchain_formats()                                                                                                                                                                                                                                                                                              |
| [String](class_string.md#class-string)                                              | get_swapchain_format_name(swapchain_format: [int](class_int.md#class-int))                                                                                                                                                                                                                                                           |
| [int](class_int.md#class-int)                                                       | get_system_id()                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                       | get_view_configuration()                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                       | get_view_count()                                                                                                                                                                                                                                                                                                                                |
|                                                                                     | insert_debug_label(label_name: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                      |
| OpenXRAlphaBlendModeSupport | is_environment_blend_mode_alpha_supported()                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                    | is_initialized()                                                                                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                    | is_running()                                                                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                    | openxr_is_enabled(check_run_in_editor: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                     |
|                                                                                     | openxr_swapchain_acquire(swapchain: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                                       | openxr_swapchain_create(create_flags: [int](class_int.md#class-int), usage_flags: [int](class_int.md#class-int), swapchain_format: [int](class_int.md#class-int), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), sample_count: [int](class_int.md#class-int), array_size: [int](class_int.md#class-int)) |
|                                                                                     | openxr_swapchain_free(swapchain: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                                       | openxr_swapchain_get_image(swapchain: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                       | openxr_swapchain_get_swapchain(swapchain: [int](class_int.md#class-int))                                                                                                                                                                                                                                                        |
|                                                                                     | openxr_swapchain_release(swapchain: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                    |
|                                                                                     | register_composition_layer_provider(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))                                                                                                                                                                                     |
|                                                                                     | register_frame_info_extension(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))                                                                                                                                                                                                 |
|                                                                                     | register_projection_layer_extension(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))                                                                                                                                                                                     |
|                                                                                     | register_projection_views_extension(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))                                                                                                                                                                                     |
|                                                                                     | set_custom_play_space(space: `const void*`)                                                                                                                                                                                                                                                                                              |
|                                                                                     | set_emulate_environment_blend_mode_alpha_blend(enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                       |
|                                                                                     | set_object_name(object_type: [int](class_int.md#class-int), object_handle: [int](class_int.md#class-int), object_name: [String](class_string.md#class-string))                                                                                                                                                                                 |
|                                                                                     | set_render_region(render_region: [Rect2i](class_rect2i.md#class-rect2i))                                                                                                                                                                                                                                                                     |
|                                                                                     | set_velocity_depth_texture(render_target: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                            |
|                                                                                     | set_velocity_target_size(target_size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                   |
|                                                                                     | set_velocity_texture(render_target: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                        |
| [Transform3D](class_transform3d.md#class-transform3d)                               | transform_from_pose(pose: `const void*`)                                                                                                                                                                                                                                                                                                   |
|                                                                                     | unregister_composition_layer_provider(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))                                                                                                                                                                                 |
|                                                                                     | unregister_frame_info_extension(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))                                                                                                                                                                                             |
|                                                                                     | unregister_projection_layer_extension(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))                                                                                                                                                                                 |
|                                                                                     | unregister_projection_views_extension(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))                                                                                                                                                                                 |
|                                                                                     | update_main_swapchain_size()                                                                                                                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                    | xr_result(result: [int](class_int.md#class-int), format: [String](class_string.md#class-string), args: [Array](class_array.md#class-array))                                                                                                                                                                                                          |

---

## Enumerations

enum **OpenXRAlphaBlendModeSupport**:

OpenXRAlphaBlendModeSupport **OPENXR_ALPHA_BLEND_MODE_SUPPORT_NONE** = `0`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) isn't supported at all.

OpenXRAlphaBlendModeSupport **OPENXR_ALPHA_BLEND_MODE_SUPPORT_REAL** = `1`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) is really supported.

OpenXRAlphaBlendModeSupport **OPENXR_ALPHA_BLEND_MODE_SUPPORT_EMULATING** = `2`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) is emulated.

---

## Method Descriptions

[int](class_int.md#class-int) **action_get_handle**(action: [RID](class_rid.md#class-rid))

Returns the corresponding `XrAction` OpenXR handle for the given action RID.

---

 **begin_debug_label_region**(label_name: [String](class_string.md#class-string))

Begins a new debug label region, this label will be reported in debug messages for any calls following this until end_debug_label_region() is called. Debug labels can be stacked.

---

[bool](class_bool.md#class-bool) **can_render**()

Returns `true` if OpenXR is initialized for rendering with an XR viewport.

---

 **end_debug_label_region**()

Marks the end of a debug label region. Removes the latest debug label region added by calling begin_debug_label_region().

---

[RID](class_rid.md#class-rid) **find_action**(name: [String](class_string.md#class-string), action_set: [RID](class_rid.md#class-rid))

Returns the [RID](class_rid.md#class-rid) corresponding to an `Action` of a matching name, optionally limited to a specified action set.

---

[String](class_string.md#class-string) **get_error_string**(result: [int](class_int.md#class-int))

Returns an error string for the given [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html).

---

[int](class_int.md#class-int) **get_hand_tracker**(hand_index: [int](class_int.md#class-int))

Returns the corresponding `XRHandTrackerEXT` handle for the given hand index value.

---

[int](class_int.md#class-int) **get_instance**()

Returns the [XrInstance](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrInstance.html) created during the initialization of the OpenXR API.

---

[int](class_int.md#class-int) **get_instance_proc_addr**(name: [String](class_string.md#class-string))

Returns the function pointer of the OpenXR function with the specified name, cast to an integer. If the function with the given name does not exist, the method returns `0`.

**Note:** `openxr/util.h` contains utility macros for acquiring OpenXR functions, e.g. `GDEXTENSION_INIT_XR_FUNC_V(xrCreateAction)`.

---

[int](class_int.md#class-int) **get_next_frame_time**()

Returns the predicted display timing for the next frame.

---

[int](class_int.md#class-int) **get_openxr_version**()

Returns the version of OpenXR that was initialized. Only valid after the OpenXR instance has been created. See [XR_MAKE_VERSION](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_MAKE_VERSION) for how the version is calculated.

---

[int](class_int.md#class-int) **get_play_space**()

Returns the play space, which is an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html) cast to an integer.

---

[int](class_int.md#class-int) **get_predicted_display_time**()

Returns the predicted display timing for the current frame.

---

[int](class_int.md#class-int) **get_projection_layer**()

Returns a pointer to the render state's `XrCompositionLayerProjection` struct.

**Note:** This method should only be called from the rendering thread.

---

[float](class_float.md#class-float) **get_render_state_z_far**()

Returns the far boundary value of the camera frustum.

**Note:** This is only accessible in the render thread.

---

[float](class_float.md#class-float) **get_render_state_z_near**()

Returns the near boundary value of the camera frustum.

**Note:** This is only accessible in the render thread.

---

[int](class_int.md#class-int) **get_session**()

Returns the OpenXR session, which is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSession.html) cast to an integer.

---

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_supported_swapchain_formats**()

Returns an array of supported swapchain formats.

---

[String](class_string.md#class-string) **get_swapchain_format_name**(swapchain_format: [int](class_int.md#class-int))

Returns the name of the specified swapchain format.

---

[int](class_int.md#class-int) **get_system_id**()

Returns the ID of the system, which is an [XrSystemId](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSystemId.html) cast to an integer.

---

[int](class_int.md#class-int) **get_view_configuration**()

Returns the view configuration type, which is an [XrViewConfigurationType](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrViewConfigurationType.html) cast to an integer.

---

[int](class_int.md#class-int) **get_view_count**()

Returns the number of views. It is usually two, one for each eye, but may differ with different view configurations.

---

 **insert_debug_label**(label_name: [String](class_string.md#class-string))

Inserts a debug label, this label is reported in any debug message resulting from the OpenXR calls that follows, until any of begin_debug_label_region(), end_debug_label_region(), or insert_debug_label() is called.

---

OpenXRAlphaBlendModeSupport **is_environment_blend_mode_alpha_supported**()

Returns OpenXRAlphaBlendModeSupport denoting if [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) is really supported, emulated or not supported at all.

---

[bool](class_bool.md#class-bool) **is_initialized**()

Returns `true` if OpenXR is initialized.

---

[bool](class_bool.md#class-bool) **is_running**()

Returns `true` if OpenXR is running ([xrBeginSession](https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrBeginSession.html) was successfully called and the swapchains were created).

---

[bool](class_bool.md#class-bool) **openxr_is_enabled**(check_run_in_editor: [bool](class_bool.md#class-bool))

Returns `true` if OpenXR is enabled.

---

 **openxr_swapchain_acquire**(swapchain: [int](class_int.md#class-int))

Acquires the image of the provided swapchain.

---

[int](class_int.md#class-int) **openxr_swapchain_create**(create_flags: [int](class_int.md#class-int), usage_flags: [int](class_int.md#class-int), swapchain_format: [int](class_int.md#class-int), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), sample_count: [int](class_int.md#class-int), array_size: [int](class_int.md#class-int))

Returns a pointer to a new swapchain created using the provided parameters.

---

 **openxr_swapchain_free**(swapchain: [int](class_int.md#class-int))

Destroys the provided swapchain and frees it from memory.

---

[RID](class_rid.md#class-rid) **openxr_swapchain_get_image**(swapchain: [int](class_int.md#class-int))

Returns the RID of the provided swapchain's image.

---

[int](class_int.md#class-int) **openxr_swapchain_get_swapchain**(swapchain: [int](class_int.md#class-int))

Returns the `XrSwapchain` handle of the provided swapchain.

---

 **openxr_swapchain_release**(swapchain: [int](class_int.md#class-int))

Releases the image of the provided swapchain.

---

 **register_composition_layer_provider**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))

Registers the given extension as a composition layer provider.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-on-session-created).

---

 **register_frame_info_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))

Registers the given extension as modifying frame info via the [OpenXRExtensionWrapper._set_frame_wait_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-set-frame-wait-info-and-get-next-pointer), [OpenXRExtensionWrapper._set_view_locate_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-set-view-locate-info-and-get-next-pointer), or [OpenXRExtensionWrapper._set_frame_end_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-set-frame-end-info-and-get-next-pointer) virtual methods.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-on-session-created).

---

 **register_projection_layer_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))

Registers the given extension as modifying `XrCompositionLayerProjection` via the [OpenXRExtensionWrapper._set_projection_layer_and_get_next_pointer()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-set-projection-layer-and-get-next-pointer) virtual method.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-on-session-created).

---

 **register_projection_views_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))

Registers the given extension as a provider of additional data structures to projections views.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class-openxrextensionwrapper-private-method-on-session-created).

---

 **set_custom_play_space**(space: `const void*`)

Sets the reference space used by OpenXR to the given [XrSpace](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html) (cast to a `void *`).

---

 **set_emulate_environment_blend_mode_alpha_blend**(enabled: [bool](class_bool.md#class-bool))

If set to `true`, an OpenXR extension is loaded which is capable of emulating the [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class-xrinterface-constant-xr-env-blend-mode-alpha-blend) blend mode.

---

 **set_object_name**(object_type: [int](class_int.md#class-int), object_handle: [int](class_int.md#class-int), object_name: [String](class_string.md#class-string))

Set the object name of an OpenXR object, used for debug output. `object_type` must be a valid OpenXR `XrObjectType` enum and `object_handle` must be a valid OpenXR object handle.

---

 **set_render_region**(render_region: [Rect2i](class_rect2i.md#class-rect2i))

Sets the render region to `render_region`, overriding the normal render target's rect.

---

 **set_velocity_depth_texture**(render_target: [RID](class_rid.md#class-rid))

Sets the render target of the velocity depth texture.

---

 **set_velocity_target_size**(target_size: [Vector2i](class_vector2i.md#class-vector2i))

Sets the target size of the velocity and velocity depth textures.

---

 **set_velocity_texture**(render_target: [RID](class_rid.md#class-rid))

Sets the render target of the velocity texture.

---

[Transform3D](class_transform3d.md#class-transform3d) **transform_from_pose**(pose: `const void*`)

Creates a [Transform3D](class_transform3d.md#class-transform3d) from an [XrPosef](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrPosef.html).

---

 **unregister_composition_layer_provider**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))

Unregisters the given extension as a composition layer provider.

**Note:** This cannot be called while the OpenXR session is still running.

---

 **unregister_frame_info_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))

Unregisters the given extension as modifying frame info.

**Note:** This cannot be called while the OpenXR session is still running.

---

 **unregister_projection_layer_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))

Unregisters the given extension as modifying `XrCompositionLayerProjection`.

**Note:** This cannot be called while the OpenXR session is still running.

---

 **unregister_projection_views_extension**(extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper))

Unregisters the given extension as a provider of additional data structures to projections views.

**Note:** This cannot be called while the OpenXR session is still running.

---

 **update_main_swapchain_size**()

Request the recommended resolution from the OpenXR runtime and update the main swapchain size if it has changed.

---

[bool](class_bool.md#class-bool) **xr_result**(result: [int](class_int.md#class-int), format: [String](class_string.md#class-string), args: [Array](class_array.md#class-array))

Returns `true` if the provided [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html) (cast to an integer) is successful. Otherwise returns `false` and prints the [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html) converted to a string, with the specified additional information.
