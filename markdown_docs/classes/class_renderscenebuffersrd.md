# RenderSceneBuffersRD

**Inherits:** [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Render scene buffer implementation for the RenderingDevice based renderers.

## Description

This object manages all 3D rendering buffers for the rendering device based renderers. An instance of this object is created for every viewport that has 3D rendering enabled. See also [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers).

All buffers are organized in **contexts**. The default context is called **render_buffers** and can contain amongst others the color buffer, depth buffer, velocity buffers, VRS density map and MSAA variants of these buffers.

Buffers are only guaranteed to exist during rendering of the viewport.

**Note:** This is an internal rendering server object. Do not instantiate this class from a script.

## Methods

|                                                                                              | clear_context(context: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)                                                                | create_texture(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), data_format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat), usage_bits: [int](class_int.md#class-int), texture_samples: [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples), size: [Vector2i](class_vector2i.md#class-vector2i), layers: [int](class_int.md#class-int), mipmaps: [int](class_int.md#class-int), unique: [bool](class_bool.md#class-bool), discardable: [bool](class_bool.md#class-bool)) |
| [RID](class_rid.md#class-rid)                                                                | create_texture_from_format(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), format: [RDTextureFormat](class_rdtextureformat.md#class-rdtextureformat), view: [RDTextureView](class_rdtextureview.md#class-rdtextureview), unique: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                              |
| [RID](class_rid.md#class-rid)                                                                | create_texture_view(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), view_name: [StringName](class_stringname.md#class-stringname), view: [RDTextureView](class_rdtextureview.md#class-rdtextureview))                                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                                | get_color_layer(layer: [int](class_int.md#class-int), msaa: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                                | get_color_texture(msaa: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                                | get_depth_layer(layer: [int](class_int.md#class-int), msaa: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                                | get_depth_texture(msaa: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                          | get_fsr_sharpness()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Vector2i](class_vector2i.md#class-vector2i)                                                 | get_internal_size()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa)                   | get_msaa_3d()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                                                | get_render_target()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode) | get_scaling_3d_mode()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa) | get_screen_space_aa()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Vector2i](class_vector2i.md#class-vector2i)                                                 | get_target_size()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                                | get_texture(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [RDTextureFormat](class_rdtextureformat.md#class-rdtextureformat)                            | get_texture_format(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples)               | get_texture_samples()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                                                | get_texture_slice(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), layer: [int](class_int.md#class-int), mipmap: [int](class_int.md#class-int), layers: [int](class_int.md#class-int), mipmaps: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                            |
| [Vector2i](class_vector2i.md#class-vector2i)                                                 | get_texture_slice_size(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), mipmap: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                                                | get_texture_slice_view(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), layer: [int](class_int.md#class-int), mipmap: [int](class_int.md#class-int), layers: [int](class_int.md#class-int), mipmaps: [int](class_int.md#class-int), view: [RDTextureView](class_rdtextureview.md#class-rdtextureview))                                                                                                                                                                                                               |
| [bool](class_bool.md#class-bool)                                                             | get_use_debanding()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                             | get_use_taa()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                                                | get_velocity_layer(layer: [int](class_int.md#class-int), msaa: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                                                | get_velocity_texture(msaa: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                                | get_view_count()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                             | has_texture(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

## Method Descriptions

 **clear_context**(context: [StringName](class_stringname.md#class-stringname))

Frees all buffers related to this context.

---

[RID](class_rid.md#class-rid) **create_texture**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), data_format: [DataFormat](class_renderingdevice.md#enum-renderingdevice-dataformat), usage_bits: [int](class_int.md#class-int), texture_samples: [TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples), size: [Vector2i](class_vector2i.md#class-vector2i), layers: [int](class_int.md#class-int), mipmaps: [int](class_int.md#class-int), unique: [bool](class_bool.md#class-bool), discardable: [bool](class_bool.md#class-bool))

Create a new texture with the given definition and cache this under the given name. Will return the existing texture if it already exists.

---

[RID](class_rid.md#class-rid) **create_texture_from_format**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), format: [RDTextureFormat](class_rdtextureformat.md#class-rdtextureformat), view: [RDTextureView](class_rdtextureview.md#class-rdtextureview), unique: [bool](class_bool.md#class-bool))

Create a new texture using the given format and view and cache this under the given name. Will return the existing texture if it already exists.

---

[RID](class_rid.md#class-rid) **create_texture_view**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), view_name: [StringName](class_stringname.md#class-stringname), view: [RDTextureView](class_rdtextureview.md#class-rdtextureview))

Create a new texture view for an existing texture and cache this under the given `view_name`. Will return the existing texture view if it already exists. Will error if the source texture doesn't exist.

---

[RID](class_rid.md#class-rid) **get_color_layer**(layer: [int](class_int.md#class-int), msaa: [bool](class_bool.md#class-bool) = false)

Returns the specified layer from the color texture we are rendering 3D content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

---

[RID](class_rid.md#class-rid) **get_color_texture**(msaa: [bool](class_bool.md#class-bool) = false)

Returns the color texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

---

[RID](class_rid.md#class-rid) **get_depth_layer**(layer: [int](class_int.md#class-int), msaa: [bool](class_bool.md#class-bool) = false)

Returns the specified layer from the depth texture we are rendering 3D content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

---

[RID](class_rid.md#class-rid) **get_depth_texture**(msaa: [bool](class_bool.md#class-bool) = false)

Returns the depth texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

---

[float](class_float.md#class-float) **get_fsr_sharpness**()

Returns the FSR sharpness value used while rendering the 3D content (if get_scaling_3d_mode() is an FSR mode).

---

[Vector2i](class_vector2i.md#class-vector2i) **get_internal_size**()

Returns the internal size of the render buffer (size before upscaling) with which textures are created by default.

---

[ViewportMSAA](class_renderingserver.md#enum-renderingserver-viewportmsaa) **get_msaa_3d**()

Returns the applied 3D MSAA mode for this viewport.

---

[RID](class_rid.md#class-rid) **get_render_target**()

Returns the render target associated with this buffers object.

---

[ViewportScaling3DMode](class_renderingserver.md#enum-renderingserver-viewportscaling3dmode) **get_scaling_3d_mode**()

Returns the scaling mode used for upscaling.

---

[ViewportScreenSpaceAA](class_renderingserver.md#enum-renderingserver-viewportscreenspaceaa) **get_screen_space_aa**()

Returns the screen-space antialiasing method applied.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_target_size**()

Returns the target size of the render buffer (size after upscaling).

---

[RID](class_rid.md#class-rid) **get_texture**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))

Returns a cached texture with this name.

---

[RDTextureFormat](class_rdtextureformat.md#class-rdtextureformat) **get_texture_format**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))

Returns the texture format information with which a cached texture was created.

---

[TextureSamples](class_renderingdevice.md#enum-renderingdevice-texturesamples) **get_texture_samples**()

Returns the number of MSAA samples used.

---

[RID](class_rid.md#class-rid) **get_texture_slice**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), layer: [int](class_int.md#class-int), mipmap: [int](class_int.md#class-int), layers: [int](class_int.md#class-int), mipmaps: [int](class_int.md#class-int))

Returns a specific slice (layer or mipmap) for a cached texture.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_texture_slice_size**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), mipmap: [int](class_int.md#class-int))

Returns the texture size of a given slice of a cached texture.

---

[RID](class_rid.md#class-rid) **get_texture_slice_view**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname), layer: [int](class_int.md#class-int), mipmap: [int](class_int.md#class-int), layers: [int](class_int.md#class-int), mipmaps: [int](class_int.md#class-int), view: [RDTextureView](class_rdtextureview.md#class-rdtextureview))

Returns a specific view of a slice (layer or mipmap) for a cached texture.

---

[bool](class_bool.md#class-bool) **get_use_debanding**()

Returns `true` if debanding is enabled.

---

[bool](class_bool.md#class-bool) **get_use_taa**()

Returns `true` if TAA is enabled.

---

[RID](class_rid.md#class-rid) **get_velocity_layer**(layer: [int](class_int.md#class-int), msaa: [bool](class_bool.md#class-bool) = false)

Returns the specified layer from the velocity texture we are rendering 3D content to.

---

[RID](class_rid.md#class-rid) **get_velocity_texture**(msaa: [bool](class_bool.md#class-bool) = false)

Returns the velocity texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is **true** and MSAA is enabled, this returns the MSAA variant of the buffer.

---

[int](class_int.md#class-int) **get_view_count**()

Returns the view count for the associated viewport.

---

[bool](class_bool.md#class-bool) **has_texture**(context: [StringName](class_stringname.md#class-stringname), name: [StringName](class_stringname.md#class-stringname))

Returns `true` if a cached texture exists for this name.
