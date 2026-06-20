# OpenXRExtensionWrapper

**Inherits:** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRAndroidThreadSettingsExtension](class_openxrandroidthreadsettingsextension.md#class-openxrandroidthreadsettingsextension), [OpenXRExtensionWrapperExtension](class_openxrextensionwrapperextension.md#class-openxrextensionwrapperextension), [OpenXRFrameSynthesisExtension](class_openxrframesynthesisextension.md#class-openxrframesynthesisextension), [OpenXRFutureExtension](class_openxrfutureextension.md#class-openxrfutureextension), [OpenXRRenderModelExtension](class_openxrrendermodelextension.md#class-openxrrendermodelextension), [OpenXRSpatialAnchorCapability](class_openxrspatialanchorcapability.md#class-openxrspatialanchorcapability), [OpenXRSpatialEntityExtension](class_openxrspatialentityextension.md#class-openxrspatialentityextension), [OpenXRSpatialMarkerTrackingCapability](class_openxrspatialmarkertrackingcapability.md#class-openxrspatialmarkertrackingcapability), [OpenXRSpatialPlaneTrackingCapability](class_openxrspatialplanetrackingcapability.md#class-openxrspatialplanetrackingcapability)

Allows implementing OpenXR extensions with GDExtension.

## Description

**OpenXRExtensionWrapper** allows implementing OpenXR extensions with GDExtension. The extension should be registered with register_extension_wrapper().

When [OpenXRInterface](class_openxrinterface.md#class-openxrinterface) is initialized as the primary interface and any [Viewport](class_viewport.md#class-viewport) has [Viewport.use_xr](class_viewport.md#class-viewport-property-use-xr) set to `true`, OpenXR will become involved in Godot's rendering process. If [ProjectSettings.rendering/driver/threads/thread_model](class_projectsettings.md#class-projectsettings-property-rendering-driver-threads-thread-model) is set to "Separate", Godot's renderer will run on its own thread, and special care must be taken in all **OpenXRExtensionWrapper**s in order to prevent crashes or unexpected behavior. Some virtual methods will be called on the render thread, and any data they access should not be directly written to on the main thread. This is to prevent two potential issues:

1. Changes intended for the next frame, taking effect on the current frame. When using the "Separate" thread model, the main thread will immediately start working on the next frame while the render thread may still be rendering the current frame. If the main thread changes anything used by the render thread directly, the change could end up being used one frame earlier than intended.
2. Reading and writing to the same data at the same time from different threads can lead to the render thread using data in an invalid state.

In most cases, the solution is to use [RenderingServer.call_on_render_thread()](class_renderingserver.md#class-renderingserver-method-call-on-render-thread) to schedule [Callable](class_callable.md#class-callable)s to write to any data used on the render thread. When using the "Separate" thread model, these [Callable](class_callable.md#class-callable)s will run after the renderer finishes the current frame and before it starts rendering the next frame. When not using this mode, they'll run immediately, so it's recommended to always use [RenderingServer.call_on_render_thread()](class_renderingserver.md#class-renderingserver-method-call-on-render-thread) in these cases, which will allow your code to do the right thing regardless of the thread model.

Any virtual methods that run on the render thread will be noted below.

## Methods

| [int](class_int.md#class-int)                                                           | \_get_composition_layer(index: [int](class_int.md#class-int))                                                                                                                                         |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                                           | \_get_composition_layer_count()                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | \_get_composition_layer_order(index: [int](class_int.md#class-int))                                                                                                                             |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_get_requested_extensions(xr_version: [int](class_int.md#class-int))                                                                                                                              |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_suggested_tracker_names()                                                                                                                                                                 |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | \_get_viewport_composition_layer_extension_properties()                                                                                                                 |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | \_get_viewport_composition_layer_extension_property_defaults()                                                                                                   |
|                                                                                         | \_on_before_instance_created()                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | \_on_event_polled(event: `const void*`)                                                                                                                                                                     |
|                                                                                         | \_on_instance_created(instance: [int](class_int.md#class-int))                                                                                                                                          |
|                                                                                         | \_on_instance_destroyed()                                                                                                                                                                             |
|                                                                                         | \_on_main_swapchains_created()                                                                                                                                                                   |
|                                                                                         | \_on_post_draw_viewport(viewport: [RID](class_rid.md#class-rid))                                                                                                                                      |
|                                                                                         | \_on_pre_draw_viewport(viewport: [RID](class_rid.md#class-rid))                                                                                                                                        |
|                                                                                         | \_on_pre_render()                                                                                                                                                                                             |
|                                                                                         | \_on_process()                                                                                                                                                                                                   |
|                                                                                         | \_on_register_metadata(interaction_profile_metadata: [OpenXRInteractionProfileMetadata](class_openxrinteractionprofilemetadata.md#class-openxrinteractionprofilemetadata))                             |
|                                                                                         | \_on_session_created(session: [int](class_int.md#class-int))                                                                                                                                             |
|                                                                                         | \_on_session_destroyed()                                                                                                                                                                               |
|                                                                                         | \_on_state_exiting()                                                                                                                                                                                       |
|                                                                                         | \_on_state_focused()                                                                                                                                                                                       |
|                                                                                         | \_on_state_idle()                                                                                                                                                                                             |
|                                                                                         | \_on_state_loss_pending()                                                                                                                                                                             |
|                                                                                         | \_on_state_ready()                                                                                                                                                                                           |
|                                                                                         | \_on_state_stopping()                                                                                                                                                                                     |
|                                                                                         | \_on_state_synchronized()                                                                                                                                                                             |
|                                                                                         | \_on_state_visible()                                                                                                                                                                                       |
|                                                                                         | \_on_sync_actions()                                                                                                                                                                                         |
|                                                                                         | \_on_viewport_composition_layer_destroyed(layer: `const void*`)                                                                                                                     |
|                                                                                         | \_prepare_view_configuration(view_count: [int](class_int.md#class-int))                                                                                                                          |
|                                                                                         | \_print_view_configuration_info(view: [int](class_int.md#class-int))                                                                                                                          |
| [int](class_int.md#class-int)                                                           | \_set_android_surface_swapchain_create_info_and_get_next_pointer(property_values: [Dictionary](class_dictionary.md#class-dictionary), next_pointer: `void*`) |
| [int](class_int.md#class-int)                                                           | \_set_frame_end_info_and_get_next_pointer(next_pointer: `void*`)                                                                                                                    |
| [int](class_int.md#class-int)                                                           | \_set_frame_wait_info_and_get_next_pointer(next_pointer: `void*`)                                                                                                                  |
| [int](class_int.md#class-int)                                                           | \_set_hand_joint_locations_and_get_next_pointer(hand_index: [int](class_int.md#class-int), next_pointer: `void*`)                                                             |
| [int](class_int.md#class-int)                                                           | \_set_instance_create_info_and_get_next_pointer(xr_version: [int](class_int.md#class-int), next_pointer: `void*`)                                                             |
| [int](class_int.md#class-int)                                                           | \_set_projection_layer_and_get_next_pointer(next_pointer: `void*`)                                                                                                                |
| [int](class_int.md#class-int)                                                           | \_set_projection_views_and_get_next_pointer(view_index: [int](class_int.md#class-int), next_pointer: `void*`)                                                                     |
| [int](class_int.md#class-int)                                                           | \_set_reference_space_create_info_and_get_next_pointer(reference_space_type: [int](class_int.md#class-int), next_pointer: `void*`)                                     |
| [int](class_int.md#class-int)                                                           | \_set_session_create_and_get_next_pointer(next_pointer: `void*`)                                                                                                                    |
| [int](class_int.md#class-int)                                                           | \_set_swapchain_create_info_and_get_next_pointer(next_pointer: `void*`)                                                                                                      |
| [int](class_int.md#class-int)                                                           | \_set_system_properties_and_get_next_pointer(next_pointer: `void*`)                                                                                                              |
| [int](class_int.md#class-int)                                                           | \_set_view_configuration_and_get_next_pointer(view: [int](class_int.md#class-int), next_pointer: `void*`)                                                                       |
| [int](class_int.md#class-int)                                                           | \_set_view_locate_info_and_get_next_pointer(next_pointer: `void*`)                                                                                                                |
| [int](class_int.md#class-int)                                                           | \_set_viewport_composition_layer_and_get_next_pointer(layer: `const void*`, property_values: [Dictionary](class_dictionary.md#class-dictionary), next_pointer: `void*`) |
| [OpenXRAPIExtension](class_openxrapiextension.md#class-openxrapiextension)              | get_openxr_api()                                                                                                                                                                                                     |
|                                                                                         | register_extension_wrapper()                                                                                                                                                                             |

---

## Method Descriptions

[int](class_int.md#class-int) **\_get_composition_layer**(index: [int](class_int.md#class-int))

Returns a pointer to an `XrCompositionLayerBaseHeader` struct to provide the given composition layer.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_composition_layer_provider()](class_openxrapiextension.md#class-openxrapiextension-method-register-composition-layer-provider).

**Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time \_on_pre_render() runs.

---

[int](class_int.md#class-int) **\_get_composition_layer_count**()

Returns the number of composition layers this extension wrapper provides via \_get_composition_layer().

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_composition_layer_provider()](class_openxrapiextension.md#class-openxrapiextension-method-register-composition-layer-provider).

**Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time \_on_pre_render() runs.

---

[int](class_int.md#class-int) **\_get_composition_layer_order**(index: [int](class_int.md#class-int))

Returns an integer that will be used to sort the given composition layer provided via \_get_composition_layer(). Lower numbers will move the layer to the front of the list, and higher numbers to the end. The default projection layer has an order of `0`, so layers provided by this method should probably be above or below (but not exactly) `0`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_composition_layer_provider()](class_openxrapiextension.md#class-openxrapiextension-method-register-composition-layer-provider).

**Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time \_on_pre_render() runs.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_requested_extensions**(xr_version: [int](class_int.md#class-int))

Returns a [Dictionary](class_dictionary.md#class-dictionary) of OpenXR extensions related to this extension. `xr_version` specifies the OpenXR version we're instantiating. This will be zero if the editor requests this list to flag supported features. The [Dictionary](class_dictionary.md#class-dictionary) should contain the name of the extension, mapped to a `bool *` cast to an integer:

- If the `bool *` is a `nullptr` this extension is mandatory.
- If the `bool *` points to a boolean, the boolean will be updated to `true` if the extension is enabled.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_suggested_tracker_names**()

Returns a [PackedStringArray](class_packedstringarray.md#class-packedstringarray) of positional tracker names that are used within the extension wrapper.

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **\_get_viewport_composition_layer_extension_properties**()

Gets an array of [Dictionary](class_dictionary.md#class-dictionary)s that represent properties, just like [Object._get_property_list()](class_object.md#class-object-private-method-get-property-list), that will be added to [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class-openxrcompositionlayer) nodes.

**Note:** This virtual method will be called on the render thread.

---

[Dictionary](class_dictionary.md#class-dictionary) **\_get_viewport_composition_layer_extension_property_defaults**()

Gets a [Dictionary](class_dictionary.md#class-dictionary) containing the default values for the properties returned by \_get_viewport_composition_layer_extension_properties().

---

 **\_on_before_instance_created**()

Called before the OpenXR instance is created.

**Note:** This virtual method will be called on the main thread, however, it will be called *before* OpenXR becomes involved in rendering, so it is safe to write to data that will be used by the render thread.

---

[bool](class_bool.md#class-bool) **\_on_event_polled**(event: `const void*`)

Called when there is an OpenXR event to process. When implementing, return `true` if the event was handled, return `false` otherwise.

---

 **\_on_instance_created**(instance: [int](class_int.md#class-int))

Called right after the OpenXR instance is created.

**Note:** This virtual method will be called on the main thread, however, it will be called *before* OpenXR becomes involved in rendering, so it is safe to write to data that will be used by the render thread.

---

 **\_on_instance_destroyed**()

Called right before the OpenXR instance is destroyed.

**Note:** This virtual method will be called on the main thread, however, it will be called *after* OpenXR is done being involved in rendering, so it is safe to write to data that was used by the render thread.

---

 **\_on_main_swapchains_created**()

Called right after the main swapchains are (re)created.

**Note:** This virtual method will be called on the render thread.

---

 **\_on_post_draw_viewport**(viewport: [RID](class_rid.md#class-rid))

Called right after the given viewport is rendered.

**Note:** The draw commands might only be queued at this point, not executed.

**Note:** This virtual method will be called on the render thread.

---

 **\_on_pre_draw_viewport**(viewport: [RID](class_rid.md#class-rid))

Called right before the given viewport is rendered.

**Note:** This virtual method will be called on the render thread.

---

 **\_on_pre_render**()

Called right before the XR viewports begin their rendering step.

**Note:** This virtual method will be called on the render thread.

---

 **\_on_process**()

Called as part of the OpenXR process handling. This happens right before general and physics processing steps of the main loop. During this step controller data is queried and made available to game logic.

---

 **\_on_register_metadata**(interaction_profile_metadata: [OpenXRInteractionProfileMetadata](class_openxrinteractionprofilemetadata.md#class-openxrinteractionprofilemetadata))

Allows extensions to register additional controller metadata. This function is called even when the OpenXR API is not constructed as the metadata needs to be available to the editor.

Extensions should also provide metadata regardless of whether they are supported on the host system. The controller data is used to setup action maps for users who may have access to the relevant hardware.

---

 **\_on_session_created**(session: [int](class_int.md#class-int))

Called right after the OpenXR session is created.

**Note:** This virtual method will be called on the main thread, however, it will be called *before* OpenXR becomes involved in rendering, so it is safe to write to data that will be used by the render thread.

---

 **\_on_session_destroyed**()

Called right before the OpenXR session is destroyed.

**Note:** This virtual method will be called on the main thread, however, it will be called *after* OpenXR is done being involved in rendering, so it is safe to write to data that was used by the render thread.

---

 **\_on_state_exiting**()

Called when the OpenXR session state is changed to exiting.

---

 **\_on_state_focused**()

Called when the OpenXR session state is changed to focused. This state is the active state when the game runs.

---

 **\_on_state_idle**()

Called when the OpenXR session state is changed to idle.

---

 **\_on_state_loss_pending**()

Called when the OpenXR session state is changed to loss pending.

---

 **\_on_state_ready**()

Called when the OpenXR session state is changed to ready. This means OpenXR is ready to set up the session.

---

 **\_on_state_stopping**()

Called when the OpenXR session state is changed to stopping.

---

 **\_on_state_synchronized**()

Called when the OpenXR session state is changed to synchronized. OpenXR also returns to this state when the application loses focus.

---

 **\_on_state_visible**()

Called when the OpenXR session state is changed to visible. This means OpenXR is now ready to receive frames.

---

 **\_on_sync_actions**()

Called when OpenXR has performed its action sync.

---

 **\_on_viewport_composition_layer_destroyed**(layer: `const void*`)

Called when a composition layer created via [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class-openxrcompositionlayer) is destroyed.

`layer` is a pointer to an `XrCompositionLayerBaseHeader` struct.

---

 **\_prepare_view_configuration**(view_count: [int](class_int.md#class-int))

Called before \_set_view_configuration_and_get_next_pointer() to allow the extension to reserve data for the given number of views.

---

 **\_print_view_configuration_info**(view: [int](class_int.md#class-int))

Called to allow an extension to print additional information about its view configuration, if applicable. This will only be called if verbose output is enabled.

---

[int](class_int.md#class-int) **\_set_android_surface_swapchain_create_info_and_get_next_pointer**(property_values: [Dictionary](class_dictionary.md#class-dictionary), next_pointer: `void*`)

Add additional data structures to Android surface swapchains created by [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class-openxrcompositionlayer).

`property_values` contains the values of the properties returned by \_get_viewport_composition_layer_extension_properties().

**Note:** This virtual method will be called on the render thread.

---

[int](class_int.md#class-int) **\_set_frame_end_info_and_get_next_pointer**(next_pointer: `void*`)

Add additional data structures to `XrFrameEndInfo`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_frame_info_extension()](class_openxrapiextension.md#class-openxrapiextension-method-register-frame-info-extension).

**Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time \_on_pre_render() runs.

---

[int](class_int.md#class-int) **\_set_frame_wait_info_and_get_next_pointer**(next_pointer: `void*`)

Add additional data structures to `XrFrameWaitInfo`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_frame_info_extension()](class_openxrapiextension.md#class-openxrapiextension-method-register-frame-info-extension).

**Note:** This virtual method will be called on the render thread.

---

[int](class_int.md#class-int) **\_set_hand_joint_locations_and_get_next_pointer**(hand_index: [int](class_int.md#class-int), next_pointer: `void*`)

Add additional data structures when each hand tracker is created.

---

[int](class_int.md#class-int) **\_set_instance_create_info_and_get_next_pointer**(xr_version: [int](class_int.md#class-int), next_pointer: `void*`)

Add additional data structures when the OpenXR instance is created. `xr_version` specifies the OpenXR version we're instantiating.

---

[int](class_int.md#class-int) **\_set_projection_layer_and_get_next_pointer**(next_pointer: `void*`)

Adds additional data structures to `XrCompositionLayerProjection`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_projection_layer_extension()](class_openxrapiextension.md#class-openxrapiextension-method-register-projection-layer-extension).

---

[int](class_int.md#class-int) **\_set_projection_views_and_get_next_pointer**(view_index: [int](class_int.md#class-int), next_pointer: `void*`)

Add additional data structures to the projection view of the given `view_index`.

**Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time \_on_pre_render() runs.

---

[int](class_int.md#class-int) **\_set_reference_space_create_info_and_get_next_pointer**(reference_space_type: [int](class_int.md#class-int), next_pointer: `void*`)

Add additional data structures to `XrReferenceSpaceCreateInfo`.

---

[int](class_int.md#class-int) **\_set_session_create_and_get_next_pointer**(next_pointer: `void*`)

Add additional data structures when the OpenXR session is created.

---

[int](class_int.md#class-int) **\_set_swapchain_create_info_and_get_next_pointer**(next_pointer: `void*`)

Add additional data structures when creating OpenXR swapchains.

---

[int](class_int.md#class-int) **\_set_system_properties_and_get_next_pointer**(next_pointer: `void*`)

Add additional data structures when querying OpenXR system abilities.

---

[int](class_int.md#class-int) **\_set_view_configuration_and_get_next_pointer**(view: [int](class_int.md#class-int), next_pointer: `void*`)

Add additional data structures when querying OpenXR view configuration.

---

[int](class_int.md#class-int) **\_set_view_locate_info_and_get_next_pointer**(next_pointer: `void*`)

Add additional data structures to `XrViewLocateInfo`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_frame_info_extension()](class_openxrapiextension.md#class-openxrapiextension-method-register-frame-info-extension).

**Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time \_on_pre_render() runs.

---

[int](class_int.md#class-int) **\_set_viewport_composition_layer_and_get_next_pointer**(layer: `const void*`, property_values: [Dictionary](class_dictionary.md#class-dictionary), next_pointer: `void*`)

Add additional data structures to composition layers created by [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class-openxrcompositionlayer).

`property_values` contains the values of the properties returned by \_get_viewport_composition_layer_extension_properties().

`layer` is a pointer to an `XrCompositionLayerBaseHeader` struct.

**Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time \_on_pre_render() runs.

---

[OpenXRAPIExtension](class_openxrapiextension.md#class-openxrapiextension) **get_openxr_api**()

Returns the created [OpenXRAPIExtension](class_openxrapiextension.md#class-openxrapiextension), which can be used to access the OpenXR API.

---

 **register_extension_wrapper**()

Registers the extension. This should happen at core module initialization level.

**Note:** This cannot be called once OpenXR has been initialized.
