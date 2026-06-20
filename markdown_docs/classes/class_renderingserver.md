# RenderingServer

**Inherits:** [Object](class_object.md#class-object)

Server for anything visible.

## Description

The rendering server is the API backend for everything visible. The whole scene system mounts on it to display. The rendering server is completely opaque: the internals are entirely implementation-specific and cannot be accessed.

The rendering server can be used to bypass the scene/[Node](class_node.md#class-node) system entirely. This can improve performance in cases where the scene system is the bottleneck, but won't improve performance otherwise (for instance, if the GPU is already fully utilized).

Resources are created using the `*_create` functions. These functions return [RID](class_rid.md#class-rid)s which are not references to the objects themselves, but opaque *pointers* towards these objects.

All objects are drawn to a viewport. You can use the [Viewport](class_viewport.md#class-viewport) attached to the [SceneTree](class_scenetree.md#class-scenetree) or you can create one yourself with viewport_create(). When using a custom scenario or canvas, the scenario or canvas needs to be attached to the viewport using viewport_set_scenario() or viewport_attach_canvas().

**Scenarios:** In 3D, all visual objects must be associated with a scenario. The scenario is a visual representation of the world. If accessing the rendering server from a running game, the scenario can be accessed from the scene tree from any [Node3D](class_node3d.md#class-node3d) node with [Node3D.get_world_3d()](class_node3d.md#class-node3d-method-get-world-3d). Otherwise, a scenario can be created with scenario_create().

Similarly, in 2D, a canvas is needed to draw all canvas items.

**3D:** In 3D, all visible objects are comprised of a resource and an instance. A resource can be a mesh, a particle system, a light, or any other 3D object. In order to be visible resources must be attached to an instance using instance_set_base(). The instance must also be attached to the scenario using instance_set_scenario() in order to be visible. RenderingServer methods that don't have a prefix are usually 3D-specific (but not always).

**2D:** In 2D, all visible objects are some form of canvas item. In order to be visible, a canvas item needs to be the child of a canvas attached to a viewport, or it needs to be the child of another canvas item that is eventually attached to the canvas. 2D-specific RenderingServer methods generally start with `canvas_*`.

**Headless mode:** Starting the engine with the `--headless` [command line argument](../tutorials/editor/command_line_tutorial.md) disables all rendering and window management functions. Most functions from **RenderingServer** will return dummy values in this case.

## Tutorials

- [Optimization using Servers](../tutorials/performance/using_servers.md)

## Properties

| [bool](class_bool.md#class-bool)   | render_loop_enabled   |
|------------------------------------|------------------------------------------------------------------------------|

## Methods

| [RID](class_rid.md#class-rid)                                                           | area_light_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)[[Image](class_image.md#class-image)]                | bake_render_uv2(base: [RID](class_rid.md#class-rid), material_overrides: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], image_size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | call_on_render_thread(callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | camera_attributes_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | camera_attributes_set_auto_exposure(camera_attributes: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), min_sensitivity: [float](class_float.md#class-float), max_sensitivity: [float](class_float.md#class-float), speed: [float](class_float.md#class-float), scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | camera_attributes_set_dof_blur(camera_attributes: [RID](class_rid.md#class-rid), far_enable: [bool](class_bool.md#class-bool), far_distance: [float](class_float.md#class-float), far_transition: [float](class_float.md#class-float), near_enable: [bool](class_bool.md#class-bool), near_distance: [float](class_float.md#class-float), near_transition: [float](class_float.md#class-float), amount: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                     |
|                                                                                         | camera_attributes_set_dof_blur_bokeh_shape(shape: DOFBokehShape)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | camera_attributes_set_dof_blur_quality(quality: DOFBlurQuality, use_jitter: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | camera_attributes_set_exposure(camera_attributes: [RID](class_rid.md#class-rid), multiplier: [float](class_float.md#class-float), normalization: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [RID](class_rid.md#class-rid)                                                           | camera_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | camera_set_camera_attributes(camera: [RID](class_rid.md#class-rid), effects: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | camera_set_compositor(camera: [RID](class_rid.md#class-rid), compositor: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | camera_set_cull_mask(camera: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | camera_set_environment(camera: [RID](class_rid.md#class-rid), env: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | camera_set_frustum(camera: [RID](class_rid.md#class-rid), size: [float](class_float.md#class-float), offset: [Vector2](class_vector2.md#class-vector2), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | camera_set_orthogonal(camera: [RID](class_rid.md#class-rid), size: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | camera_set_perspective(camera: [RID](class_rid.md#class-rid), fovy_degrees: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | camera_set_transform(camera: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | camera_set_use_vertical_aspect(camera: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                           | canvas_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | canvas_item_add_animation_slice(item: [RID](class_rid.md#class-rid), animation_length: [float](class_float.md#class-float), slice_begin: [float](class_float.md#class-float), slice_end: [float](class_float.md#class-float), offset: [float](class_float.md#class-float) = 0.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | canvas_item_add_circle(item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), radius: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), antialiased: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | canvas_item_add_clip_ignore(item: [RID](class_rid.md#class-rid), ignore: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | canvas_item_add_ellipse(item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), major: [float](class_float.md#class-float), minor: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), antialiased: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_item_add_lcd_texture_rect_region(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | canvas_item_add_line(item: [RID](class_rid.md#class-rid), from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | canvas_item_add_mesh(item: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d) = Transform2D(1, 0, 0, 1, 0, 0), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), texture: [RID](class_rid.md#class-rid) = RID())                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | canvas_item_add_msdf_texture_rect_region(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), outline_size: [int](class_int.md#class-int) = 0, px_range: [float](class_float.md#class-float) = 1.0, scale: [float](class_float.md#class-float) = 1.0)                                                                                                                                                                                                                                                                                             |
|                                                                                         | canvas_item_add_multiline(item: [RID](class_rid.md#class-rid), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | canvas_item_add_multimesh(item: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid) = RID())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | canvas_item_add_nine_patch(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), source: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), topleft: [Vector2](class_vector2.md#class-vector2), bottomright: [Vector2](class_vector2.md#class-vector2), x_axis_mode: NinePatchAxisMode = 0, y_axis_mode: NinePatchAxisMode = 0, draw_center: [bool](class_bool.md#class-bool) = true, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1))                                                                                                                                                   |
|                                                                                         | canvas_item_add_particles(item: [RID](class_rid.md#class-rid), particles: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | canvas_item_add_polygon(item: [RID](class_rid.md#class-rid), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) = PackedVector2Array(), texture: [RID](class_rid.md#class-rid) = RID())                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | canvas_item_add_polyline(item: [RID](class_rid.md#class-rid), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | canvas_item_add_primitive(item: [RID](class_rid.md#class-rid), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | canvas_item_add_rect(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), color: [Color](class_color.md#class-color), antialiased: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | canvas_item_add_set_transform(item: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | canvas_item_add_texture_rect(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), tile: [bool](class_bool.md#class-bool) = false, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | canvas_item_add_texture_rect_region(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false, clip_uv: [bool](class_bool.md#class-bool) = true)                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | canvas_item_add_triangle_array(item: [RID](class_rid.md#class-rid), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) = PackedVector2Array(), bones: [PackedInt32Array](class_packedint32array.md#class-packedint32array) = PackedInt32Array(), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) = PackedFloat32Array(), texture: [RID](class_rid.md#class-rid) = RID(), count: [int](class_int.md#class-int) = -1)            |
|                                                                                         | canvas_item_attach_skeleton(item: [RID](class_rid.md#class-rid), skeleton: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | canvas_item_clear(item: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [RID](class_rid.md#class-rid)                                                           | canvas_item_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Variant](class_variant.md#class-variant)                                               | canvas_item_get_instance_shader_parameter(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Variant](class_variant.md#class-variant)                                               | canvas_item_get_instance_shader_parameter_default_value(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | canvas_item_get_instance_shader_parameter_list(instance: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | canvas_item_reset_physics_interpolation(item: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | canvas_item_set_canvas_group_mode(item: [RID](class_rid.md#class-rid), mode: CanvasGroupMode, clear_margin: [float](class_float.md#class-float) = 5.0, fit_empty: [bool](class_bool.md#class-bool) = false, fit_margin: [float](class_float.md#class-float) = 0.0, blur_mipmaps: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | canvas_item_set_clip(item: [RID](class_rid.md#class-rid), clip: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | canvas_item_set_copy_to_backbuffer(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool), rect: [Rect2](class_rect2.md#class-rect2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | canvas_item_set_custom_rect(item: [RID](class_rid.md#class-rid), use_custom_rect: [bool](class_bool.md#class-bool), rect: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | canvas_item_set_default_texture_filter(item: [RID](class_rid.md#class-rid), filter: CanvasItemTextureFilter)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | canvas_item_set_default_texture_repeat(item: [RID](class_rid.md#class-rid), repeat: CanvasItemTextureRepeat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | canvas_item_set_distance_field_mode(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | canvas_item_set_draw_behind_parent(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | canvas_item_set_draw_index(item: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | canvas_item_set_instance_shader_parameter(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | canvas_item_set_interpolated(item: [RID](class_rid.md#class-rid), interpolated: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | canvas_item_set_light_mask(item: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_item_set_material(item: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_item_set_modulate(item: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | canvas_item_set_parent(item: [RID](class_rid.md#class-rid), parent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | canvas_item_set_self_modulate(item: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | canvas_item_set_sort_children_by_y(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | canvas_item_set_transform(item: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | canvas_item_set_use_parent_material(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | canvas_item_set_visibility_layer(item: [RID](class_rid.md#class-rid), visibility_layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | canvas_item_set_visibility_notifier(item: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), area: [Rect2](class_rect2.md#class-rect2), enter_callable: [Callable](class_callable.md#class-callable), exit_callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | canvas_item_set_visible(item: [RID](class_rid.md#class-rid), visible: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_item_set_z_as_relative_to_parent(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_item_set_z_index(item: [RID](class_rid.md#class-rid), z_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | canvas_item_transform_physics_interpolation(item: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | canvas_light_attach_to_canvas(light: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [RID](class_rid.md#class-rid)                                                           | canvas_light_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | canvas_light_occluder_attach_to_canvas(occluder: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                                           | canvas_light_occluder_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | canvas_light_occluder_reset_physics_interpolation(occluder: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | canvas_light_occluder_set_as_sdf_collision(occluder: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | canvas_light_occluder_set_enabled(occluder: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | canvas_light_occluder_set_interpolated(occluder: [RID](class_rid.md#class-rid), interpolated: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | canvas_light_occluder_set_light_mask(occluder: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | canvas_light_occluder_set_polygon(occluder: [RID](class_rid.md#class-rid), polygon: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | canvas_light_occluder_set_transform(occluder: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | canvas_light_occluder_transform_physics_interpolation(occluder: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | canvas_light_reset_physics_interpolation(light: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | canvas_light_set_blend_mode(light: [RID](class_rid.md#class-rid), mode: CanvasLightBlendMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | canvas_light_set_color(light: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_light_set_enabled(light: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | canvas_light_set_energy(light: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | canvas_light_set_height(light: [RID](class_rid.md#class-rid), height: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | canvas_light_set_interpolated(light: [RID](class_rid.md#class-rid), interpolated: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | canvas_light_set_item_cull_mask(light: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | canvas_light_set_item_shadow_cull_mask(light: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | canvas_light_set_layer_range(light: [RID](class_rid.md#class-rid), min_layer: [int](class_int.md#class-int), max_layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | canvas_light_set_mode(light: [RID](class_rid.md#class-rid), mode: CanvasLightMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | canvas_light_set_shadow_color(light: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | canvas_light_set_shadow_enabled(light: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | canvas_light_set_shadow_filter(light: [RID](class_rid.md#class-rid), filter: CanvasLightShadowFilter)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | canvas_light_set_shadow_smooth(light: [RID](class_rid.md#class-rid), smooth: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | canvas_light_set_texture(light: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_light_set_texture_offset(light: [RID](class_rid.md#class-rid), offset: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | canvas_light_set_texture_scale(light: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_light_set_transform(light: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | canvas_light_set_z_range(light: [RID](class_rid.md#class-rid), min_z: [int](class_int.md#class-int), max_z: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | canvas_light_transform_physics_interpolation(light: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                           | canvas_occluder_polygon_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | canvas_occluder_polygon_set_cull_mode(occluder_polygon: [RID](class_rid.md#class-rid), mode: CanvasOccluderPolygonCullMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | canvas_occluder_polygon_set_shape(occluder_polygon: [RID](class_rid.md#class-rid), shape: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), closed: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | canvas_set_disable_scale(disable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | canvas_set_item_mirroring(canvas: [RID](class_rid.md#class-rid), item: [RID](class_rid.md#class-rid), mirroring: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | canvas_set_item_repeat(item: [RID](class_rid.md#class-rid), repeat_size: [Vector2](class_vector2.md#class-vector2), repeat_times: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | canvas_set_modulate(canvas: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | canvas_set_shadow_texture_size(size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [RID](class_rid.md#class-rid)                                                           | canvas_texture_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | canvas_texture_set_channel(canvas_texture: [RID](class_rid.md#class-rid), channel: CanvasTextureChannel, texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | canvas_texture_set_shading_parameters(canvas_texture: [RID](class_rid.md#class-rid), base_color: [Color](class_color.md#class-color), shininess: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | canvas_texture_set_texture_filter(canvas_texture: [RID](class_rid.md#class-rid), filter: CanvasItemTextureFilter)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | canvas_texture_set_texture_repeat(canvas_texture: [RID](class_rid.md#class-rid), repeat: CanvasItemTextureRepeat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [RID](class_rid.md#class-rid)                                                           | compositor_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [RID](class_rid.md#class-rid)                                                           | compositor_effect_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | compositor_effect_set_callback(effect: [RID](class_rid.md#class-rid), callback_type: CompositorEffectCallbackType, callback: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | compositor_effect_set_enabled(effect: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | compositor_effect_set_flag(effect: [RID](class_rid.md#class-rid), flag: CompositorEffectFlags, set: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | compositor_set_compositor_effects(compositor: [RID](class_rid.md#class-rid), effects: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [RenderingDevice](class_renderingdevice.md#class-renderingdevice)                       | create_local_rendering_device()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Rect2](class_rect2.md#class-rect2)                                                     | debug_canvas_item_get_rect(item: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                           | decal_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | decal_set_albedo_mix(decal: [RID](class_rid.md#class-rid), albedo_mix: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | decal_set_cull_mask(decal: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | decal_set_distance_fade(decal: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool), begin: [float](class_float.md#class-float), length: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | decal_set_emission_energy(decal: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | decal_set_fade(decal: [RID](class_rid.md#class-rid), above: [float](class_float.md#class-float), below: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | decal_set_modulate(decal: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | decal_set_normal_fade(decal: [RID](class_rid.md#class-rid), fade: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | decal_set_size(decal: [RID](class_rid.md#class-rid), size: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | decal_set_texture(decal: [RID](class_rid.md#class-rid), type: DecalTexture, texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | decals_set_filter(filter: DecalFilter)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                                           | directional_light_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | directional_shadow_atlas_set_size(size: [int](class_int.md#class-int), is_16bits: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | directional_soft_shadow_filter_set_quality(quality: ShadowQuality)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Image](class_image.md#class-image)                                                     | environment_bake_panorama(environment: [RID](class_rid.md#class-rid), bake_irradiance: [bool](class_bool.md#class-bool), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                                           | environment_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | environment_glow_set_use_bicubic_upscale(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | environment_set_adjustment(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), brightness: [float](class_float.md#class-float), contrast: [float](class_float.md#class-float), saturation: [float](class_float.md#class-float), use_1d_color_correction: [bool](class_bool.md#class-bool), color_correction: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | environment_set_ambient_light(env: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color), ambient: EnvironmentAmbientSource = 0, energy: [float](class_float.md#class-float) = 1.0, sky_contribution: [float](class_float.md#class-float) = 0.0, reflection_source: EnvironmentReflectionSource = 0)                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | environment_set_background(env: [RID](class_rid.md#class-rid), bg: EnvironmentBG)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | environment_set_bg_color(env: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | environment_set_bg_energy(env: [RID](class_rid.md#class-rid), multiplier: [float](class_float.md#class-float), exposure_value: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | environment_set_camera_id(env: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | environment_set_canvas_max_layer(env: [RID](class_rid.md#class-rid), max_layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | environment_set_fog(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), light_color: [Color](class_color.md#class-color), light_energy: [float](class_float.md#class-float), sun_scatter: [float](class_float.md#class-float), density: [float](class_float.md#class-float), height: [float](class_float.md#class-float), height_density: [float](class_float.md#class-float), aerial_perspective: [float](class_float.md#class-float), sky_affect: [float](class_float.md#class-float), fog_mode: EnvironmentFogMode = 0)                                                                                                                                                            |
|                                                                                         | environment_set_fog_depth(env: [RID](class_rid.md#class-rid), curve: [float](class_float.md#class-float), begin: [float](class_float.md#class-float), end: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | environment_set_glow(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), levels: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), intensity: [float](class_float.md#class-float), strength: [float](class_float.md#class-float), mix: [float](class_float.md#class-float), bloom_threshold: [float](class_float.md#class-float), blend_mode: EnvironmentGlowBlendMode, hdr_bleed_threshold: [float](class_float.md#class-float), hdr_bleed_scale: [float](class_float.md#class-float), hdr_luminance_cap: [float](class_float.md#class-float), glow_map_strength: [float](class_float.md#class-float), glow_map: [RID](class_rid.md#class-rid))     |
|                                                                                         | environment_set_sdfgi(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), cascades: [int](class_int.md#class-int), min_cell_size: [float](class_float.md#class-float), y_scale: EnvironmentSDFGIYScale, use_occlusion: [bool](class_bool.md#class-bool), bounce_feedback: [float](class_float.md#class-float), read_sky: [bool](class_bool.md#class-bool), energy: [float](class_float.md#class-float), normal_bias: [float](class_float.md#class-float), probe_bias: [float](class_float.md#class-float))                                                                                                                                                                      |
|                                                                                         | environment_set_sdfgi_frames_to_converge(frames: EnvironmentSDFGIFramesToConverge)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | environment_set_sdfgi_frames_to_update_light(frames: EnvironmentSDFGIFramesToUpdateLight)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | environment_set_sdfgi_ray_count(ray_count: EnvironmentSDFGIRayCount)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | environment_set_sky(env: [RID](class_rid.md#class-rid), sky: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | environment_set_sky_custom_fov(env: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | environment_set_sky_orientation(env: [RID](class_rid.md#class-rid), orientation: [Basis](class_basis.md#class-basis))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | environment_set_ssao(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), radius: [float](class_float.md#class-float), intensity: [float](class_float.md#class-float), power: [float](class_float.md#class-float), detail: [float](class_float.md#class-float), horizon: [float](class_float.md#class-float), sharpness: [float](class_float.md#class-float), light_affect: [float](class_float.md#class-float), ao_channel_affect: [float](class_float.md#class-float))                                                                                                                                                                                                                                                          |
|                                                                                         | environment_set_ssao_quality(quality: EnvironmentSSAOQuality, half_size: [bool](class_bool.md#class-bool), adaptive_target: [float](class_float.md#class-float), blur_passes: [int](class_int.md#class-int), fadeout_from: [float](class_float.md#class-float), fadeout_to: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | environment_set_ssil_quality(quality: EnvironmentSSILQuality, half_size: [bool](class_bool.md#class-bool), adaptive_target: [float](class_float.md#class-float), blur_passes: [int](class_int.md#class-int), fadeout_from: [float](class_float.md#class-float), fadeout_to: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | environment_set_ssr(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), max_steps: [int](class_int.md#class-int), fade_in: [float](class_float.md#class-float), fade_out: [float](class_float.md#class-float), depth_tolerance: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | environment_set_ssr_half_size(half_size: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | environment_set_ssr_roughness_quality(quality: EnvironmentSSRRoughnessQuality)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | environment_set_tonemap(env: [RID](class_rid.md#class-rid), tone_mapper: EnvironmentToneMapper, exposure: [float](class_float.md#class-float), white: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | environment_set_tonemap_agx_contrast(env: [RID](class_rid.md#class-rid), agx_contrast: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | environment_set_volumetric_fog(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), density: [float](class_float.md#class-float), albedo: [Color](class_color.md#class-color), emission: [Color](class_color.md#class-color), emission_energy: [float](class_float.md#class-float), anisotropy: [float](class_float.md#class-float), length: [float](class_float.md#class-float), detail_spread: [float](class_float.md#class-float), gi_inject: [float](class_float.md#class-float), temporal_reprojection: [bool](class_bool.md#class-bool), temporal_reprojection_amount: [float](class_float.md#class-float), ambient_inject: [float](class_float.md#class-float), sky_affect: [float](class_float.md#class-float)) |
|                                                                                         | environment_set_volumetric_fog_filter_active(active: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | environment_set_volumetric_fog_volume_size(size: [int](class_int.md#class-int), depth: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [RID](class_rid.md#class-rid)                                                           | fog_volume_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | fog_volume_set_material(fog_volume: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | fog_volume_set_shape(fog_volume: [RID](class_rid.md#class-rid), shape: FogVolumeShape)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | fog_volume_set_size(fog_volume: [RID](class_rid.md#class-rid), size: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | force_draw(swap_buffers: [bool](class_bool.md#class-bool) = true, frame_step: [float](class_float.md#class-float) = 0.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | force_sync()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | free_rid(rid: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [String](class_string.md#class-string)                                                  | get_current_rendering_driver_name()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [String](class_string.md#class-string)                                                  | get_current_rendering_method()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Color](class_color.md#class-color)                                                     | get_default_clear_color()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                     | get_frame_setup_time_cpu()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RenderingDevice](class_renderingdevice.md#class-renderingdevice)                       | get_rendering_device()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [int](class_int.md#class-int)                                                           | get_rendering_info(info: RenderingInfo)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | get_shader_parameter_list(shader: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                           | get_test_cube()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                                           | get_test_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [String](class_string.md#class-string)                                                  | get_video_adapter_api_version()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [String](class_string.md#class-string)                                                  | get_video_adapter_name()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [DeviceType](class_renderingdevice.md#enum-renderingdevice-devicetype)                  | get_video_adapter_type()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [String](class_string.md#class-string)                                                  | get_video_adapter_vendor()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | get_white_texture()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | gi_set_use_half_resolution(half_resolution: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | global_shader_parameter_add(name: [StringName](class_stringname.md#class-stringname), type: GlobalShaderParameterType, default_value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Variant](class_variant.md#class-variant)                                               | global_shader_parameter_get(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | global_shader_parameter_get_list()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| GlobalShaderParameterType            | global_shader_parameter_get_type(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | global_shader_parameter_remove(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | global_shader_parameter_set(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | global_shader_parameter_set_override(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                        | has_changed()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)                                                        | has_feature(feature: Features)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | has_os_feature(feature: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | instance_attach_object_instance_id(instance: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | instance_attach_skeleton(instance: [RID](class_rid.md#class-rid), skeleton: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | instance_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                           | instance_create2(base: [RID](class_rid.md#class-rid), scenario: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Variant](class_variant.md#class-variant)                                               | instance_geometry_get_shader_parameter(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Variant](class_variant.md#class-variant)                                               | instance_geometry_get_shader_parameter_default_value(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] | instance_geometry_get_shader_parameter_list(instance: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | instance_geometry_set_cast_shadows_setting(instance: [RID](class_rid.md#class-rid), shadow_casting_setting: ShadowCastingSetting)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | instance_geometry_set_flag(instance: [RID](class_rid.md#class-rid), flag: InstanceFlags, enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | instance_geometry_set_lightmap(instance: [RID](class_rid.md#class-rid), lightmap: [RID](class_rid.md#class-rid), lightmap_uv_scale: [Rect2](class_rect2.md#class-rect2), lightmap_slice: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | instance_geometry_set_lod_bias(instance: [RID](class_rid.md#class-rid), lod_bias: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | instance_geometry_set_material_overlay(instance: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | instance_geometry_set_material_override(instance: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | instance_geometry_set_shader_parameter(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | instance_geometry_set_transparency(instance: [RID](class_rid.md#class-rid), transparency: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | instance_geometry_set_visibility_range(instance: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float), min_margin: [float](class_float.md#class-float), max_margin: [float](class_float.md#class-float), fade_mode: VisibilityRangeFadeMode)                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | instance_set_base(instance: [RID](class_rid.md#class-rid), base: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | instance_set_blend_shape_weight(instance: [RID](class_rid.md#class-rid), shape: [int](class_int.md#class-int), weight: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | instance_set_custom_aabb(instance: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | instance_set_extra_visibility_margin(instance: [RID](class_rid.md#class-rid), margin: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | instance_set_ignore_culling(instance: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | instance_set_layer_mask(instance: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | instance_set_pivot_data(instance: [RID](class_rid.md#class-rid), sorting_offset: [float](class_float.md#class-float), use_aabb_center: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | instance_set_scenario(instance: [RID](class_rid.md#class-rid), scenario: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | instance_set_surface_override_material(instance: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | instance_set_transform(instance: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | instance_set_visibility_parent(instance: [RID](class_rid.md#class-rid), parent: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | instance_set_visible(instance: [RID](class_rid.md#class-rid), visible: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | instance_teleport(instance: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array)                    | instances_cull_aabb(aabb: [AABB](class_aabb.md#class-aabb), scenario: [RID](class_rid.md#class-rid) = RID())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array)                    | instances_cull_convex(convex: [Array](class_array.md#class-array)[[Plane](class_plane.md#class-plane)], scenario: [RID](class_rid.md#class-rid) = RID())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array)                    | instances_cull_ray(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3), scenario: [RID](class_rid.md#class-rid) = RID())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | is_on_render_thread()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | light_area_set_normalize_energy(light: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | light_area_set_size(light: [RID](class_rid.md#class-rid), size: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | light_directional_set_blend_splits(light: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | light_directional_set_shadow_mode(light: [RID](class_rid.md#class-rid), mode: LightDirectionalShadowMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | light_directional_set_sky_mode(light: [RID](class_rid.md#class-rid), mode: LightDirectionalSkyMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | light_omni_set_shadow_mode(light: [RID](class_rid.md#class-rid), mode: LightOmniShadowMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | light_projectors_set_filter(filter: LightProjectorFilter)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | light_set_bake_mode(light: [RID](class_rid.md#class-rid), bake_mode: LightBakeMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | light_set_color(light: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | light_set_cull_mask(light: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | light_set_distance_fade(decal: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool), begin: [float](class_float.md#class-float), shadow: [float](class_float.md#class-float), length: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | light_set_max_sdfgi_cascade(light: [RID](class_rid.md#class-rid), cascade: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | light_set_negative(light: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | light_set_param(light: [RID](class_rid.md#class-rid), param: LightParam, value: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | light_set_projector(light: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | light_set_reverse_cull_face_mode(light: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | light_set_shadow(light: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | light_set_shadow_caster_mask(light: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [RID](class_rid.md#class-rid)                                                           | lightmap_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | lightmap_get_probe_capture_bsp_tree(lightmap: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [PackedVector3Array](class_packedvector3array.md#class-packedvector3array)              | lightmap_get_probe_capture_points(lightmap: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)                    | lightmap_get_probe_capture_sh(lightmap: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | lightmap_get_probe_capture_tetrahedra(lightmap: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | lightmap_set_baked_exposure_normalization(lightmap: [RID](class_rid.md#class-rid), baked_exposure: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | lightmap_set_probe_bounds(lightmap: [RID](class_rid.md#class-rid), bounds: [AABB](class_aabb.md#class-aabb))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | lightmap_set_probe_capture_data(lightmap: [RID](class_rid.md#class-rid), points: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), point_sh: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), tetrahedra: [PackedInt32Array](class_packedint32array.md#class-packedint32array), bsp_tree: [PackedInt32Array](class_packedint32array.md#class-packedint32array))                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | lightmap_set_probe_capture_update_speed(speed: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | lightmap_set_probe_interior(lightmap: [RID](class_rid.md#class-rid), interior: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | lightmap_set_textures(lightmap: [RID](class_rid.md#class-rid), light: [RID](class_rid.md#class-rid), uses_sh: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | lightmaps_set_bicubic_filter(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | make_sphere_mesh(latitudes: [int](class_int.md#class-int), longitudes: [int](class_int.md#class-int), radius: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | material_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Variant](class_variant.md#class-variant)                                               | material_get_param(material: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | material_set_next_pass(material: [RID](class_rid.md#class-rid), next_material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | material_set_param(material: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | material_set_render_priority(material: [RID](class_rid.md#class-rid), priority: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | material_set_shader(shader_material: [RID](class_rid.md#class-rid), shader: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | material_set_use_debanding(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | mesh_add_surface(mesh: [RID](class_rid.md#class-rid), surface: [Dictionary](class_dictionary.md#class-dictionary))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | mesh_add_surface_from_arrays(mesh: [RID](class_rid.md#class-rid), primitive: PrimitiveType, arrays: [Array](class_array.md#class-array), blend_shapes: [Array](class_array.md#class-array) = [], lods: [Dictionary](class_dictionary.md#class-dictionary) = {}, compress_format: [ArrayFormat] = 0)                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | mesh_clear(mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                           | mesh_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                                           | mesh_create_from_surfaces(surfaces: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)], blend_shape_count: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [int](class_int.md#class-int)                                                           | mesh_get_blend_shape_count(mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| BlendShapeMode                                  | mesh_get_blend_shape_mode(mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [AABB](class_aabb.md#class-aabb)                                                        | mesh_get_custom_aabb(mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dictionary](class_dictionary.md#class-dictionary)                                      | mesh_get_surface(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | mesh_get_surface_count(mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | mesh_set_blend_shape_mode(mesh: [RID](class_rid.md#class-rid), mode: BlendShapeMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | mesh_set_custom_aabb(mesh: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | mesh_set_shadow_mesh(mesh: [RID](class_rid.md#class-rid), shadow_mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Array](class_array.md#class-array)                                                     | mesh_surface_get_arrays(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Array](class_array.md#class-array)[[Array](class_array.md#class-array)]                | mesh_surface_get_blend_shape_arrays(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                                           | mesh_surface_get_format_attribute_stride(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [int](class_int.md#class-int)                                                           | mesh_surface_get_format_index_stride(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | mesh_surface_get_format_normal_tangent_stride(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                                           | mesh_surface_get_format_offset(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int), array_index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | mesh_surface_get_format_skin_stride(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                           | mesh_surface_get_format_vertex_stride(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [RID](class_rid.md#class-rid)                                                           | mesh_surface_get_material(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | mesh_surface_remove(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | mesh_surface_set_material(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | mesh_surface_update_attribute_region(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | mesh_surface_update_index_region(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | mesh_surface_update_skin_region(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | mesh_surface_update_vertex_region(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | multimesh_allocate_data(multimesh: [RID](class_rid.md#class-rid), instances: [int](class_int.md#class-int), transform_format: MultimeshTransformFormat, color_format: [bool](class_bool.md#class-bool) = false, custom_data_format: [bool](class_bool.md#class-bool) = false, use_indirect: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                           | multimesh_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [AABB](class_aabb.md#class-aabb)                                                        | multimesh_get_aabb(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)              | multimesh_get_buffer(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | multimesh_get_buffer_rd_rid(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                           | multimesh_get_command_buffer_rd_rid(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [AABB](class_aabb.md#class-aabb)                                                        | multimesh_get_custom_aabb(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | multimesh_get_instance_count(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | multimesh_get_mesh(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | multimesh_get_visible_instances(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Color](class_color.md#class-color)                                                     | multimesh_instance_get_color(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Color](class_color.md#class-color)                                                     | multimesh_instance_get_custom_data(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | multimesh_instance_get_transform(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Transform2D](class_transform2d.md#class-transform2d)                                   | multimesh_instance_get_transform_2d(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | multimesh_instance_reset_physics_interpolation(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | multimesh_instance_set_color(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | multimesh_instance_set_custom_data(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), custom_data: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | multimesh_instance_set_transform(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | multimesh_instance_set_transform_2d(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | multimesh_instances_reset_physics_interpolation(multimesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | multimesh_set_buffer(multimesh: [RID](class_rid.md#class-rid), buffer: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | multimesh_set_buffer_interpolated(multimesh: [RID](class_rid.md#class-rid), buffer: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), buffer_previous: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | multimesh_set_custom_aabb(multimesh: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | multimesh_set_mesh(multimesh: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | multimesh_set_physics_interpolated(multimesh: [RID](class_rid.md#class-rid), interpolated: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | multimesh_set_physics_interpolation_quality(multimesh: [RID](class_rid.md#class-rid), quality: MultimeshPhysicsInterpolationQuality)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | multimesh_set_visible_instances(multimesh: [RID](class_rid.md#class-rid), visible: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                           | occluder_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | occluder_set_mesh(occluder: [RID](class_rid.md#class-rid), vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                           | omni_light_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [RID](class_rid.md#class-rid)                                                           | particles_collision_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | particles_collision_height_field_update(particles_collision: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | particles_collision_set_attractor_attenuation(particles_collision: [RID](class_rid.md#class-rid), curve: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | particles_collision_set_attractor_directionality(particles_collision: [RID](class_rid.md#class-rid), amount: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | particles_collision_set_attractor_strength(particles_collision: [RID](class_rid.md#class-rid), strength: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | particles_collision_set_box_extents(particles_collision: [RID](class_rid.md#class-rid), extents: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | particles_collision_set_collision_type(particles_collision: [RID](class_rid.md#class-rid), type: ParticlesCollisionType)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | particles_collision_set_cull_mask(particles_collision: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | particles_collision_set_field_texture(particles_collision: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | particles_collision_set_height_field_mask(particles_collision: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | particles_collision_set_height_field_resolution(particles_collision: [RID](class_rid.md#class-rid), resolution: ParticlesCollisionHeightfieldResolution)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | particles_collision_set_sphere_radius(particles_collision: [RID](class_rid.md#class-rid), radius: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [RID](class_rid.md#class-rid)                                                           | particles_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | particles_emit(particles: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), velocity: [Vector3](class_vector3.md#class-vector3), color: [Color](class_color.md#class-color), custom: [Color](class_color.md#class-color), emit_flags: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [AABB](class_aabb.md#class-aabb)                                                        | particles_get_current_aabb(particles: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | particles_get_emitting(particles: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | particles_is_inactive(particles: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | particles_request_process(particles: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | particles_request_process_time(particles: [RID](class_rid.md#class-rid), process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | particles_restart(particles: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | particles_set_amount(particles: [RID](class_rid.md#class-rid), amount: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | particles_set_amount_ratio(particles: [RID](class_rid.md#class-rid), ratio: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | particles_set_collision_base_size(particles: [RID](class_rid.md#class-rid), size: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | particles_set_custom_aabb(particles: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | particles_set_draw_order(particles: [RID](class_rid.md#class-rid), order: ParticlesDrawOrder)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | particles_set_draw_pass_mesh(particles: [RID](class_rid.md#class-rid), pass: [int](class_int.md#class-int), mesh: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | particles_set_draw_passes(particles: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | particles_set_emission_transform(particles: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | particles_set_emitter_velocity(particles: [RID](class_rid.md#class-rid), velocity: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | particles_set_emitting(particles: [RID](class_rid.md#class-rid), emitting: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | particles_set_explosiveness_ratio(particles: [RID](class_rid.md#class-rid), ratio: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | particles_set_fixed_fps(particles: [RID](class_rid.md#class-rid), fps: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | particles_set_fractional_delta(particles: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | particles_set_interp_to_end(particles: [RID](class_rid.md#class-rid), factor: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | particles_set_interpolate(particles: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | particles_set_lifetime(particles: [RID](class_rid.md#class-rid), lifetime: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | particles_set_mode(particles: [RID](class_rid.md#class-rid), mode: ParticlesMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | particles_set_one_shot(particles: [RID](class_rid.md#class-rid), one_shot: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | particles_set_pre_process_time(particles: [RID](class_rid.md#class-rid), time: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | particles_set_process_material(particles: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | particles_set_randomness_ratio(particles: [RID](class_rid.md#class-rid), ratio: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | particles_set_speed_scale(particles: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | particles_set_subemitter(particles: [RID](class_rid.md#class-rid), subemitter_particles: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | particles_set_trail_bind_poses(particles: [RID](class_rid.md#class-rid), bind_poses: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | particles_set_trails(particles: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), length_sec: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | particles_set_transform_align(particles: [RID](class_rid.md#class-rid), align: ParticlesTransformAlign)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | particles_set_transform_align_axis(particles: [RID](class_rid.md#class-rid), rotation_axis: ParticlesTransformAlignAxis)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | particles_set_transform_align_channel_filter(particles: [RID](class_rid.md#class-rid), channel_filter: ParticlesTransformAlignCustomSrc)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | particles_set_use_local_coordinates(particles: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | positional_soft_shadow_filter_set_quality(quality: ShadowQuality)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [RID](class_rid.md#class-rid)                                                           | reflection_probe_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | reflection_probe_set_ambient_color(probe: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | reflection_probe_set_ambient_energy(probe: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | reflection_probe_set_ambient_mode(probe: [RID](class_rid.md#class-rid), mode: ReflectionProbeAmbientMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | reflection_probe_set_as_interior(probe: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | reflection_probe_set_blend_distance(probe: [RID](class_rid.md#class-rid), blend_distance: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | reflection_probe_set_cull_mask(probe: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | reflection_probe_set_enable_box_projection(probe: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | reflection_probe_set_enable_shadows(probe: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | reflection_probe_set_intensity(probe: [RID](class_rid.md#class-rid), intensity: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | reflection_probe_set_max_distance(probe: [RID](class_rid.md#class-rid), distance: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | reflection_probe_set_mesh_lod_threshold(probe: [RID](class_rid.md#class-rid), pixels: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | reflection_probe_set_origin_offset(probe: [RID](class_rid.md#class-rid), offset: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | reflection_probe_set_reflection_mask(probe: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | reflection_probe_set_resolution(probe: [RID](class_rid.md#class-rid), resolution: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | reflection_probe_set_size(probe: [RID](class_rid.md#class-rid), size: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | reflection_probe_set_update_mode(probe: [RID](class_rid.md#class-rid), mode: ReflectionProbeUpdateMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | request_frame_drawn_callback(callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [RID](class_rid.md#class-rid)                                                           | scenario_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | scenario_set_camera_attributes(scenario: [RID](class_rid.md#class-rid), effects: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | scenario_set_compositor(scenario: [RID](class_rid.md#class-rid), compositor: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | scenario_set_environment(scenario: [RID](class_rid.md#class-rid), environment: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | scenario_set_fallback_environment(scenario: [RID](class_rid.md#class-rid), environment: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | screen_space_roughness_limiter_set_active(enable: [bool](class_bool.md#class-bool), amount: [float](class_float.md#class-float), limit: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | set_boot_image(image: [Image](class_image.md#class-image), color: [Color](class_color.md#class-color), scale: [bool](class_bool.md#class-bool), use_filter: [bool](class_bool.md#class-bool) = true)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | set_boot_image_with_stretch(image: [Image](class_image.md#class-image), color: [Color](class_color.md#class-color), stretch_mode: SplashStretchMode, use_filter: [bool](class_bool.md#class-bool) = true)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | set_debug_generate_wireframes(generate: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | set_default_clear_color(color: [Color](class_color.md#class-color))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [RID](class_rid.md#class-rid)                                                           | shader_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [String](class_string.md#class-string)                                                  | shader_get_code(shader: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                                           | shader_get_default_texture_parameter(shader: [RID](class_rid.md#class-rid), name: [StringName](class_stringname.md#class-stringname), index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Variant](class_variant.md#class-variant)                                               | shader_get_parameter_default(shader: [RID](class_rid.md#class-rid), name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | shader_set_code(shader: [RID](class_rid.md#class-rid), code: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | shader_set_default_texture_parameter(shader: [RID](class_rid.md#class-rid), name: [StringName](class_stringname.md#class-stringname), texture: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | shader_set_path_hint(shader: [RID](class_rid.md#class-rid), path: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | skeleton_allocate_data(skeleton: [RID](class_rid.md#class-rid), bones: [int](class_int.md#class-int), is_2d_skeleton: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | skeleton_bone_get_transform(skeleton: [RID](class_rid.md#class-rid), bone: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Transform2D](class_transform2d.md#class-transform2d)                                   | skeleton_bone_get_transform_2d(skeleton: [RID](class_rid.md#class-rid), bone: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | skeleton_bone_set_transform(skeleton: [RID](class_rid.md#class-rid), bone: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | skeleton_bone_set_transform_2d(skeleton: [RID](class_rid.md#class-rid), bone: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                                           | skeleton_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [int](class_int.md#class-int)                                                           | skeleton_get_bone_count(skeleton: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | skeleton_set_base_transform_2d(skeleton: [RID](class_rid.md#class-rid), base_transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Image](class_image.md#class-image)                                                     | sky_bake_panorama(sky: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float), bake_irradiance: [bool](class_bool.md#class-bool), size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [RID](class_rid.md#class-rid)                                                           | sky_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | sky_set_material(sky: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | sky_set_mode(sky: [RID](class_rid.md#class-rid), mode: SkyMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | sky_set_radiance_size(sky: [RID](class_rid.md#class-rid), radiance_size: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                                           | spot_light_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | sub_surface_scattering_set_quality(quality: SubSurfaceScatteringQuality)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | sub_surface_scattering_set_scale(scale: [float](class_float.md#class-float), depth_scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [RID](class_rid.md#class-rid)                                                           | texture_2d_create(image: [Image](class_image.md#class-image))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Image](class_image.md#class-image)                                                     | texture_2d_get(texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Image](class_image.md#class-image)                                                     | texture_2d_layer_get(texture: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [RID](class_rid.md#class-rid)                                                           | texture_2d_layered_create(layers: [Array](class_array.md#class-array)[[Image](class_image.md#class-image)], layered_type: TextureLayeredType)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | texture_2d_layered_placeholder_create(layered_type: TextureLayeredType)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                                           | texture_2d_placeholder_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | texture_2d_update(texture: [RID](class_rid.md#class-rid), image: [Image](class_image.md#class-image), layer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [RID](class_rid.md#class-rid)                                                           | texture_3d_create(format: [Format](class_image.md#enum-image-format), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), mipmaps: [bool](class_bool.md#class-bool), data: [Array](class_array.md#class-array)[[Image](class_image.md#class-image)])                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Array](class_array.md#class-array)[[Image](class_image.md#class-image)]                | texture_3d_get(texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [RID](class_rid.md#class-rid)                                                           | texture_3d_placeholder_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | texture_3d_update(texture: [RID](class_rid.md#class-rid), data: [Array](class_array.md#class-array)[[Image](class_image.md#class-image)])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [RID](class_rid.md#class-rid)                                                           | texture_create_from_native_handle(type: TextureType, format: [Format](class_image.md#enum-image-format), native_handle: [int](class_int.md#class-int), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), layers: [int](class_int.md#class-int) = 1, layered_type: TextureLayeredType = 0)                                                                                                                                                                                                                                                                                                   |
|                                                                                         | texture_drawable_blit_rect(textures: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], rect: [Rect2i](class_rect2i.md#class-rect2i), material: [RID](class_rid.md#class-rid), modulate: [Color](class_color.md#class-color), source_textures: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], to_mipmap: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                    |
| [RID](class_rid.md#class-rid)                                                           | texture_drawable_create(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), format: TextureDrawableFormat, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), with_mipmaps: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | texture_drawable_generate_mipmaps(texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [RID](class_rid.md#class-rid)                                                           | texture_drawable_get_default_material()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Format](class_image.md#enum-image-format)                                              | texture_get_format(texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [int](class_int.md#class-int)                                                           | texture_get_native_handle(texture: [RID](class_rid.md#class-rid), srgb: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [String](class_string.md#class-string)                                                  | texture_get_path(texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [RID](class_rid.md#class-rid)                                                           | texture_get_rd_texture(texture: [RID](class_rid.md#class-rid), srgb: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [RID](class_rid.md#class-rid)                                                           | texture_proxy_create(base: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | texture_proxy_update(texture: [RID](class_rid.md#class-rid), proxy_to: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RID](class_rid.md#class-rid)                                                           | texture_rd_create(rd_texture: [RID](class_rid.md#class-rid), layer_type: TextureLayeredType = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | texture_replace(texture: [RID](class_rid.md#class-rid), by_texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | texture_set_force_redraw_if_visible(texture: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | texture_set_path(texture: [RID](class_rid.md#class-rid), path: [String](class_string.md#class-string))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | texture_set_size_override(texture: [RID](class_rid.md#class-rid), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | viewport_attach_camera(viewport: [RID](class_rid.md#class-rid), camera: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | viewport_attach_canvas(viewport: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | viewport_attach_to_screen(viewport: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), screen: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                                           | viewport_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [float](class_float.md#class-float)                                                     | viewport_get_measured_render_time_cpu(viewport: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [float](class_float.md#class-float)                                                     | viewport_get_measured_render_time_gpu(viewport: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [int](class_int.md#class-int)                                                           | viewport_get_render_info(viewport: [RID](class_rid.md#class-rid), type: ViewportRenderInfoType, info: ViewportRenderInfo)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                           | viewport_get_render_target(viewport: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                           | viewport_get_texture(viewport: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ViewportUpdateMode                          | viewport_get_update_mode(viewport: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | viewport_remove_canvas(viewport: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | viewport_set_active(viewport: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | viewport_set_anisotropic_filtering_level(viewport: [RID](class_rid.md#class-rid), anisotropic_filtering_level: ViewportAnisotropicFiltering)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | viewport_set_canvas_cull_mask(viewport: [RID](class_rid.md#class-rid), canvas_cull_mask: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | viewport_set_canvas_stacking(viewport: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int), sublayer: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | viewport_set_canvas_transform(viewport: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), offset: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | viewport_set_clear_mode(viewport: [RID](class_rid.md#class-rid), clear_mode: ViewportClearMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | viewport_set_debug_draw(viewport: [RID](class_rid.md#class-rid), draw: ViewportDebugDraw)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | viewport_set_default_canvas_item_texture_filter(viewport: [RID](class_rid.md#class-rid), filter: CanvasItemTextureFilter)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | viewport_set_default_canvas_item_texture_repeat(viewport: [RID](class_rid.md#class-rid), repeat: CanvasItemTextureRepeat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | viewport_set_disable_2d(viewport: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | viewport_set_disable_3d(viewport: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | viewport_set_environment_mode(viewport: [RID](class_rid.md#class-rid), mode: ViewportEnvironmentMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | viewport_set_fsr_sharpness(viewport: [RID](class_rid.md#class-rid), sharpness: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | viewport_set_global_canvas_transform(viewport: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | viewport_set_measure_render_time(viewport: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | viewport_set_msaa_2d(viewport: [RID](class_rid.md#class-rid), msaa: ViewportMSAA)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | viewport_set_msaa_3d(viewport: [RID](class_rid.md#class-rid), msaa: ViewportMSAA)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | viewport_set_occlusion_culling_build_quality(quality: ViewportOcclusionCullingBuildQuality)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                         | viewport_set_occlusion_rays_per_thread(rays_per_thread: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | viewport_set_parent_viewport(viewport: [RID](class_rid.md#class-rid), parent_viewport: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | viewport_set_positional_shadow_atlas_quadrant_subdivision(viewport: [RID](class_rid.md#class-rid), quadrant: [int](class_int.md#class-int), subdivision: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | viewport_set_positional_shadow_atlas_size(viewport: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), use_16_bits: [bool](class_bool.md#class-bool) = false)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | viewport_set_render_direct_to_screen(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | viewport_set_scaling_3d_mode(viewport: [RID](class_rid.md#class-rid), scaling_3d_mode: ViewportScaling3DMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                         | viewport_set_scaling_3d_scale(viewport: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                         | viewport_set_scenario(viewport: [RID](class_rid.md#class-rid), scenario: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | viewport_set_screen_space_aa(viewport: [RID](class_rid.md#class-rid), mode: ViewportScreenSpaceAA)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | viewport_set_sdf_oversize_and_scale(viewport: [RID](class_rid.md#class-rid), oversize: ViewportSDFOversize, scale: ViewportSDFScale)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                         | viewport_set_size(viewport: [RID](class_rid.md#class-rid), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), view_count: [int](class_int.md#class-int) = 1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | viewport_set_snap_2d_transforms_to_pixel(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | viewport_set_snap_2d_vertices_to_pixel(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | viewport_set_texture_mipmap_bias(viewport: [RID](class_rid.md#class-rid), mipmap_bias: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | viewport_set_transparent_background(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                         | viewport_set_update_mode(viewport: [RID](class_rid.md#class-rid), update_mode: ViewportUpdateMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | viewport_set_use_debanding(viewport: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | viewport_set_use_hdr_2d(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                         | viewport_set_use_occlusion_culling(viewport: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                         | viewport_set_use_taa(viewport: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                         | viewport_set_use_xr(viewport: [RID](class_rid.md#class-rid), use_xr: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | viewport_set_vrs_mode(viewport: [RID](class_rid.md#class-rid), mode: ViewportVRSMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                         | viewport_set_vrs_texture(viewport: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                         | viewport_set_vrs_update_mode(viewport: [RID](class_rid.md#class-rid), mode: ViewportVRSUpdateMode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [RID](class_rid.md#class-rid)                                                           | visibility_notifier_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | visibility_notifier_set_aabb(notifier: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | visibility_notifier_set_callbacks(notifier: [RID](class_rid.md#class-rid), enter_callable: [Callable](class_callable.md#class-callable), exit_callable: [Callable](class_callable.md#class-callable))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | voxel_gi_allocate_data(voxel_gi: [RID](class_rid.md#class-rid), to_cell_xform: [Transform3D](class_transform3d.md#class-transform3d), aabb: [AABB](class_aabb.md#class-aabb), octree_size: [Vector3i](class_vector3i.md#class-vector3i), octree_cells: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), data_cells: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), distance_field: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), level_counts: [PackedInt32Array](class_packedint32array.md#class-packedint32array))                                                                                                                                                                          |
| [RID](class_rid.md#class-rid)                                                           | voxel_gi_create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)                       | voxel_gi_get_data_cells(voxel_gi: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)                       | voxel_gi_get_distance_field(voxel_gi: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | voxel_gi_get_level_counts(voxel_gi: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray)                       | voxel_gi_get_octree_cells(voxel_gi: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Vector3i](class_vector3i.md#class-vector3i)                                            | voxel_gi_get_octree_size(voxel_gi: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | voxel_gi_get_to_cell_xform(voxel_gi: [RID](class_rid.md#class-rid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | voxel_gi_set_baked_exposure_normalization(voxel_gi: [RID](class_rid.md#class-rid), baked_exposure: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                         | voxel_gi_set_bias(voxel_gi: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | voxel_gi_set_dynamic_range(voxel_gi: [RID](class_rid.md#class-rid), range: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | voxel_gi_set_energy(voxel_gi: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                         | voxel_gi_set_interior(voxel_gi: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                         | voxel_gi_set_normal_bias(voxel_gi: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                         | voxel_gi_set_propagation(voxel_gi: [RID](class_rid.md#class-rid), amount: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                         | voxel_gi_set_quality(quality: VoxelGIQuality)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                         | voxel_gi_set_use_two_bounces(voxel_gi: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

## Signals

**frame_post_draw**()

Emitted at the end of the frame, after the RenderingServer has finished updating all the Viewports.

---

**frame_pre_draw**()

Emitted at the beginning of the frame, before the RenderingServer updates all the Viewports.

---

## Enumerations

enum **TextureType**:

TextureType **TEXTURE_TYPE_2D** = `0`

2D texture.

TextureType **TEXTURE_TYPE_LAYERED** = `1`

Layered texture.

TextureType **TEXTURE_TYPE_3D** = `2`

3D texture.

---

enum **TextureLayeredType**:

TextureLayeredType **TEXTURE_LAYERED_2D_ARRAY** = `0`

Array of 2-dimensional textures (see [Texture2DArray](class_texture2darray.md#class-texture2darray)).

TextureLayeredType **TEXTURE_LAYERED_CUBEMAP** = `1`

Cubemap texture (see [Cubemap](class_cubemap.md#class-cubemap)).

TextureLayeredType **TEXTURE_LAYERED_CUBEMAP_ARRAY** = `2`

Array of cubemap textures (see [CubemapArray](class_cubemaparray.md#class-cubemaparray)).

---

enum **CubeMapLayer**:

CubeMapLayer **CUBEMAP_LAYER_LEFT** = `0`

Left face of a [Cubemap](class_cubemap.md#class-cubemap).

CubeMapLayer **CUBEMAP_LAYER_RIGHT** = `1`

Right face of a [Cubemap](class_cubemap.md#class-cubemap).

CubeMapLayer **CUBEMAP_LAYER_BOTTOM** = `2`

Bottom face of a [Cubemap](class_cubemap.md#class-cubemap).

CubeMapLayer **CUBEMAP_LAYER_TOP** = `3`

Top face of a [Cubemap](class_cubemap.md#class-cubemap).

CubeMapLayer **CUBEMAP_LAYER_FRONT** = `4`

Front face of a [Cubemap](class_cubemap.md#class-cubemap).

CubeMapLayer **CUBEMAP_LAYER_BACK** = `5`

Back face of a [Cubemap](class_cubemap.md#class-cubemap).

---

enum **TextureDrawableFormat**:

TextureDrawableFormat **TEXTURE_DRAWABLE_FORMAT_RGBA8** = `0`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

TextureDrawableFormat **TEXTURE_DRAWABLE_FORMAT_RGBA8_SRGB** = `1`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

When drawn to, an sRGB to linear color space conversion is performed.

TextureDrawableFormat **TEXTURE_DRAWABLE_FORMAT_RGBAH** = `2`

OpenGL texture format GL_RGBA16F where there are four components, each a 16-bit "half-precision" floating-point value.

TextureDrawableFormat **TEXTURE_DRAWABLE_FORMAT_RGBAF** = `3`

OpenGL texture format GL_RGBA32F where there are four components, each a 32-bit floating-point value.

---

enum **ShaderMode**:

ShaderMode **SHADER_SPATIAL** = `0`

Shader is a 3D shader.

ShaderMode **SHADER_CANVAS_ITEM** = `1`

Shader is a 2D shader.

ShaderMode **SHADER_PARTICLES** = `2`

Shader is a particle shader (can be used in both 2D and 3D).

ShaderMode **SHADER_SKY** = `3`

Shader is a 3D sky shader.

ShaderMode **SHADER_FOG** = `4`

Shader is a 3D fog shader.

ShaderMode **SHADER_TEXTURE_BLIT** = `5`

Shader is a texture_blit shader.

ShaderMode **SHADER_MAX** = `6`

Represents the size of the ShaderMode enum.

---

enum **ArrayType**:

ArrayType **ARRAY_VERTEX** = `0`

Array is a vertex position array.

ArrayType **ARRAY_NORMAL** = `1`

Array is a normal array.

ArrayType **ARRAY_TANGENT** = `2`

Array is a tangent array.

ArrayType **ARRAY_COLOR** = `3`

Array is a vertex color array.

ArrayType **ARRAY_TEX_UV** = `4`

Array is a UV coordinates array.

ArrayType **ARRAY_TEX_UV2** = `5`

Array is a UV coordinates array for the second set of UV coordinates.

ArrayType **ARRAY_CUSTOM0** = `6`

Array is a custom data array for the first set of custom data.

ArrayType **ARRAY_CUSTOM1** = `7`

Array is a custom data array for the second set of custom data.

ArrayType **ARRAY_CUSTOM2** = `8`

Array is a custom data array for the third set of custom data.

ArrayType **ARRAY_CUSTOM3** = `9`

Array is a custom data array for the fourth set of custom data.

ArrayType **ARRAY_BONES** = `10`

Array contains bone information.

ArrayType **ARRAY_WEIGHTS** = `11`

Array is weight information.

ArrayType **ARRAY_INDEX** = `12`

Array is an index array.

ArrayType **ARRAY_MAX** = `13`

Represents the size of the ArrayType enum.

---

enum **ArrayCustomFormat**:

ArrayCustomFormat **ARRAY_CUSTOM_RGBA8_UNORM** = `0`

Custom data array contains 8-bit-per-channel red/green/blue/alpha color data. Values are normalized, unsigned floating-point in the `[0.0, 1.0]` range.

ArrayCustomFormat **ARRAY_CUSTOM_RGBA8_SNORM** = `1`

Custom data array contains 8-bit-per-channel red/green/blue/alpha color data. Values are normalized, signed floating-point in the `[-1.0, 1.0]` range.

ArrayCustomFormat **ARRAY_CUSTOM_RG_HALF** = `2`

Custom data array contains 16-bit-per-channel red/green color data. Values are floating-point in half precision.

ArrayCustomFormat **ARRAY_CUSTOM_RGBA_HALF** = `3`

Custom data array contains 16-bit-per-channel red/green/blue/alpha color data. Values are floating-point in half precision.

ArrayCustomFormat **ARRAY_CUSTOM_R_FLOAT** = `4`

Custom data array contains 32-bit-per-channel red color data. Values are floating-point in single precision.

ArrayCustomFormat **ARRAY_CUSTOM_RG_FLOAT** = `5`

Custom data array contains 32-bit-per-channel red/green color data. Values are floating-point in single precision.

ArrayCustomFormat **ARRAY_CUSTOM_RGB_FLOAT** = `6`

Custom data array contains 32-bit-per-channel red/green/blue color data. Values are floating-point in single precision.

ArrayCustomFormat **ARRAY_CUSTOM_RGBA_FLOAT** = `7`

Custom data array contains 32-bit-per-channel red/green/blue/alpha color data. Values are floating-point in single precision.

ArrayCustomFormat **ARRAY_CUSTOM_MAX** = `8`

Represents the size of the ArrayCustomFormat enum.

---

flags **ArrayFormat**:

ArrayFormat **ARRAY_FORMAT_VERTEX** = `1`

Flag used to mark a vertex position array.

ArrayFormat **ARRAY_FORMAT_NORMAL** = `2`

Flag used to mark a normal array.

ArrayFormat **ARRAY_FORMAT_TANGENT** = `4`

Flag used to mark a tangent array.

ArrayFormat **ARRAY_FORMAT_COLOR** = `8`

Flag used to mark a vertex color array.

ArrayFormat **ARRAY_FORMAT_TEX_UV** = `16`

Flag used to mark a UV coordinates array.

ArrayFormat **ARRAY_FORMAT_TEX_UV2** = `32`

Flag used to mark a UV coordinates array for the second UV coordinates.

ArrayFormat **ARRAY_FORMAT_CUSTOM0** = `64`

Flag used to mark an array of custom per-vertex data for the first set of custom data.

ArrayFormat **ARRAY_FORMAT_CUSTOM1** = `128`

Flag used to mark an array of custom per-vertex data for the second set of custom data.

ArrayFormat **ARRAY_FORMAT_CUSTOM2** = `256`

Flag used to mark an array of custom per-vertex data for the third set of custom data.

ArrayFormat **ARRAY_FORMAT_CUSTOM3** = `512`

Flag used to mark an array of custom per-vertex data for the fourth set of custom data.

ArrayFormat **ARRAY_FORMAT_BONES** = `1024`

Flag used to mark a bone information array.

ArrayFormat **ARRAY_FORMAT_WEIGHTS** = `2048`

Flag used to mark a weights array.

ArrayFormat **ARRAY_FORMAT_INDEX** = `4096`

Flag used to mark an index array.

ArrayFormat **ARRAY_FORMAT_BLEND_SHAPE_MASK** = `7`

Mask of mesh channels permitted in blend shapes.

ArrayFormat **ARRAY_FORMAT_CUSTOM_BASE** = `13`

Shift of first custom channel.

ArrayFormat **ARRAY_FORMAT_CUSTOM_BITS** = `3`

Number of format bits per custom channel. See ArrayCustomFormat.

ArrayFormat **ARRAY_FORMAT_CUSTOM0_SHIFT** = `13`

Amount to shift ArrayCustomFormat for custom channel index 0.

ArrayFormat **ARRAY_FORMAT_CUSTOM1_SHIFT** = `16`

Amount to shift ArrayCustomFormat for custom channel index 1.

ArrayFormat **ARRAY_FORMAT_CUSTOM2_SHIFT** = `19`

Amount to shift ArrayCustomFormat for custom channel index 2.

ArrayFormat **ARRAY_FORMAT_CUSTOM3_SHIFT** = `22`

Amount to shift ArrayCustomFormat for custom channel index 3.

ArrayFormat **ARRAY_FORMAT_CUSTOM_MASK** = `7`

Mask of custom format bits per custom channel. Must be shifted by one of the SHIFT constants. See ArrayCustomFormat.

ArrayFormat **ARRAY_COMPRESS_FLAGS_BASE** = `25`

Shift of first compress flag. Compress flags should be passed to [ArrayMesh.add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays) and [SurfaceTool.commit()](class_surfacetool.md#class-surfacetool-method-commit).

ArrayFormat **ARRAY_FLAG_USE_2D_VERTICES** = `33554432`

Flag used to mark that the array contains 2D vertices.

ArrayFormat **ARRAY_FLAG_USE_DYNAMIC_UPDATE** = `67108864`

Flag used to mark that the mesh data will use `GL_DYNAMIC_DRAW` on GLES. Unused on Vulkan.

ArrayFormat **ARRAY_FLAG_USE_8_BONE_WEIGHTS** = `134217728`

Flag used to mark that the array uses 8 bone weights instead of 4.

ArrayFormat **ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY** = `268435456`

Flag used to mark that the mesh does not have a vertex array and instead will infer vertex positions in the shader using indices and other information.

ArrayFormat **ARRAY_FLAG_COMPRESS_ATTRIBUTES** = `536870912`

Flag used to mark that a mesh is using compressed attributes (vertices, normals, tangents, UVs). When this form of compression is enabled, vertex positions will be packed into an RGBA16UNORM attribute and scaled in the vertex shader. The normal and tangent will be packed into an RG16UNORM representing an axis, and a 16-bit float stored in the A-channel of the vertex. UVs will use 16-bit normalized floats instead of full 32-bit signed floats. When using this compression mode you must use either vertices, normals, and tangents or only vertices. You cannot use normals without tangents. Importers will automatically enable this compression if they can.

ArrayFormat **ARRAY_FLAG_FORMAT_VERSION_BASE** = `35`

Flag used to mark the start of the bits used to store the mesh version.

ArrayFormat **ARRAY_FLAG_FORMAT_VERSION_SHIFT** = `35`

Flag used to shift a mesh format int to bring the version into the lowest digits.

ArrayFormat **ARRAY_FLAG_FORMAT_VERSION_1** = `0`

Flag used to record the format used by prior mesh versions before the introduction of a version.

ArrayFormat **ARRAY_FLAG_FORMAT_VERSION_2** = `34359738368`

Flag used to record the second iteration of the mesh version flag. The primary difference between this and ARRAY_FLAG_FORMAT_VERSION_1 is that this version supports ARRAY_FLAG_COMPRESS_ATTRIBUTES and in this version vertex positions are de-interleaved from normals and tangents.

ArrayFormat **ARRAY_FLAG_FORMAT_CURRENT_VERSION** = `34359738368`

Flag used to record the current version that the engine expects. Currently this is the same as ARRAY_FLAG_FORMAT_VERSION_2.

ArrayFormat **ARRAY_FLAG_FORMAT_VERSION_MASK** = `255`

Flag used to isolate the bits used for mesh version after using ARRAY_FLAG_FORMAT_VERSION_SHIFT to shift them into place.

---

enum **PrimitiveType**:

PrimitiveType **PRIMITIVE_POINTS** = `0`

Primitive to draw consists of points.

PrimitiveType **PRIMITIVE_LINES** = `1`

Primitive to draw consists of lines.

PrimitiveType **PRIMITIVE_LINE_STRIP** = `2`

Primitive to draw consists of a line strip from start to end.

PrimitiveType **PRIMITIVE_TRIANGLES** = `3`

Primitive to draw consists of triangles.

PrimitiveType **PRIMITIVE_TRIANGLE_STRIP** = `4`

Primitive to draw consists of a triangle strip (the last 3 vertices are always combined to make a triangle).

PrimitiveType **PRIMITIVE_MAX** = `5`

Represents the size of the PrimitiveType enum.

---

enum **BlendShapeMode**:

BlendShapeMode **BLEND_SHAPE_MODE_NORMALIZED** = `0`

Blend shapes are normalized.

BlendShapeMode **BLEND_SHAPE_MODE_RELATIVE** = `1`

Blend shapes are relative to base weight.

---

enum **MultimeshTransformFormat**:

MultimeshTransformFormat **MULTIMESH_TRANSFORM_2D** = `0`

Use [Transform2D](class_transform2d.md#class-transform2d) to store MultiMesh transform.

MultimeshTransformFormat **MULTIMESH_TRANSFORM_3D** = `1`

Use [Transform3D](class_transform3d.md#class-transform3d) to store MultiMesh transform.

---

enum **MultimeshPhysicsInterpolationQuality**:

MultimeshPhysicsInterpolationQuality **MULTIMESH_INTERP_QUALITY_FAST** = `0`

MultiMesh physics interpolation favors speed over quality.

MultimeshPhysicsInterpolationQuality **MULTIMESH_INTERP_QUALITY_HIGH** = `1`

MultiMesh physics interpolation favors quality over speed.

---

enum **LightProjectorFilter**:

LightProjectorFilter **LIGHT_PROJECTOR_FILTER_NEAREST** = `0`

Nearest-neighbor filter for light projectors (use for pixel art light projectors). No mipmaps are used for rendering, which means light projectors at a distance will look sharp but grainy. This has roughly the same performance cost as using mipmaps.

LightProjectorFilter **LIGHT_PROJECTOR_FILTER_LINEAR** = `1`

Linear filter for light projectors (use for non-pixel art light projectors). No mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as using mipmaps.

LightProjectorFilter **LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS** = `2`

Nearest-neighbor filter for light projectors (use for pixel art light projectors). Isotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.

LightProjectorFilter **LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS** = `3`

Linear filter for light projectors (use for non-pixel art light projectors). Isotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.

LightProjectorFilter **LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS_ANISOTROPIC** = `4`

Nearest-neighbor filter for light projectors (use for pixel art light projectors). Anisotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined by [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

LightProjectorFilter **LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS_ANISOTROPIC** = `5`

Linear filter for light projectors (use for non-pixel art light projectors). Anisotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined by [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

---

enum **LightType**:

LightType **LIGHT_DIRECTIONAL** = `0`

Directional (sun/moon) light (see [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d)).

LightType **LIGHT_OMNI** = `1`

Omni light (see [OmniLight3D](class_omnilight3d.md#class-omnilight3d)).

LightType **LIGHT_SPOT** = `2`

Spot light (see [SpotLight3D](class_spotlight3d.md#class-spotlight3d)).

LightType **LIGHT_AREA** = `3`

Area light (see [AreaLight3D](class_arealight3d.md#class-arealight3d)).

---

enum **LightParam**:

LightParam **LIGHT_PARAM_ENERGY** = `0`

The light's energy multiplier.

LightParam **LIGHT_PARAM_INDIRECT_ENERGY** = `1`

The light's indirect energy multiplier (final indirect energy is LIGHT_PARAM_ENERGY \* LIGHT_PARAM_INDIRECT_ENERGY).

LightParam **LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY** = `2`

The light's volumetric fog energy multiplier (final volumetric fog energy is LIGHT_PARAM_ENERGY \* LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY).

LightParam **LIGHT_PARAM_SPECULAR** = `3`

The light's influence on specularity.

LightParam **LIGHT_PARAM_RANGE** = `4`

The light's range.

LightParam **LIGHT_PARAM_SIZE** = `5`

The size of the light when using spot light or omni light. The angular size of the light when using directional light.

LightParam **LIGHT_PARAM_ATTENUATION** = `6`

The light's attenuation.

LightParam **LIGHT_PARAM_SPOT_ANGLE** = `7`

The spotlight's angle.

LightParam **LIGHT_PARAM_SPOT_ATTENUATION** = `8`

The spotlight's attenuation.

LightParam **LIGHT_PARAM_SHADOW_MAX_DISTANCE** = `9`

The maximum distance for shadow splits. Increasing this value will make directional shadows visible from further away, at the cost of lower overall shadow detail and performance (since more objects need to be included in the directional shadow rendering).

LightParam **LIGHT_PARAM_SHADOW_SPLIT_1_OFFSET** = `10`

Proportion of shadow atlas occupied by the first split.

LightParam **LIGHT_PARAM_SHADOW_SPLIT_2_OFFSET** = `11`

Proportion of shadow atlas occupied by the second split.

LightParam **LIGHT_PARAM_SHADOW_SPLIT_3_OFFSET** = `12`

Proportion of shadow atlas occupied by the third split. The fourth split occupies the rest.

LightParam **LIGHT_PARAM_SHADOW_FADE_START** = `13`

Proportion of shadow max distance where the shadow will start to fade out.

LightParam **LIGHT_PARAM_SHADOW_NORMAL_BIAS** = `14`

Normal bias used to offset shadow lookup by object normal. Can be used to fix self-shadowing artifacts.

LightParam **LIGHT_PARAM_SHADOW_BIAS** = `15`

Bias for the shadow lookup to fix self-shadowing artifacts.

LightParam **LIGHT_PARAM_SHADOW_PANCAKE_SIZE** = `16`

Sets the size of the directional shadow pancake. The pancake offsets the start of the shadow's camera frustum to provide a higher effective depth resolution for the shadow. However, a high pancake size can cause artifacts in the shadows of large objects that are close to the edge of the frustum. Reducing the pancake size can help. Setting the size to `0` turns off the pancaking effect.

LightParam **LIGHT_PARAM_SHADOW_OPACITY** = `17`

The light's shadow opacity. Values lower than `1.0` make the light appear through shadows. This can be used to fake global illumination at a low performance cost.

LightParam **LIGHT_PARAM_SHADOW_BLUR** = `18`

Blurs the edges of the shadow. Can be used to hide pixel artifacts in low resolution shadow maps. A high value can make shadows appear grainy and can cause other unwanted artifacts. Try to keep as near default as possible.

LightParam **LIGHT_PARAM_TRANSMITTANCE_BIAS** = `19`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

LightParam **LIGHT_PARAM_INTENSITY** = `20`

Constant representing the intensity of the light, measured in Lumens when dealing with a [SpotLight3D](class_spotlight3d.md#class-spotlight3d) or [OmniLight3D](class_omnilight3d.md#class-omnilight3d), or measured in Lux with a [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d). Only used when [ProjectSettings.rendering/lights_and_shadows/use_physical_light_units](class_projectsettings.md#class-projectsettings-property-rendering-lights-and-shadows-use-physical-light-units) is `true`.

LightParam **LIGHT_PARAM_MAX** = `21`

Represents the size of the LightParam enum.

---

enum **LightBakeMode**:

LightBakeMode **LIGHT_BAKE_DISABLED** = `0`

Light is ignored when baking. This is the fastest mode, but the light will be taken into account when baking global illumination. This mode should generally be used for dynamic lights that change quickly, as the effect of global illumination is less noticeable on those lights.

LightBakeMode **LIGHT_BAKE_STATIC** = `1`

Light is taken into account in static baking ([VoxelGI](class_voxelgi.md#class-voxelgi), [LightmapGI](class_lightmapgi.md#class-lightmapgi), SDFGI ([Environment.sdfgi_enabled](class_environment.md#class-environment-property-sdfgi-enabled))). The light can be moved around or modified, but its global illumination will not update in real-time. This is suitable for subtle changes (such as flickering torches), but generally not large changes such as toggling a light on and off.

LightBakeMode **LIGHT_BAKE_DYNAMIC** = `2`

Light is taken into account in dynamic baking ([VoxelGI](class_voxelgi.md#class-voxelgi) and SDFGI ([Environment.sdfgi_enabled](class_environment.md#class-environment-property-sdfgi-enabled)) only). The light can be moved around or modified with global illumination updating in real-time. The light's global illumination appearance will be slightly different compared to LIGHT_BAKE_STATIC. This has a greater performance cost compared to LIGHT_BAKE_STATIC. When using SDFGI, the update speed of dynamic lights is affected by [ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights](class_projectsettings.md#class-projectsettings-property-rendering-global-illumination-sdfgi-frames-to-update-lights).

---

enum **LightOmniShadowMode**:

LightOmniShadowMode **LIGHT_OMNI_SHADOW_DUAL_PARABOLOID** = `0`

Use a dual paraboloid shadow map for omni lights.

LightOmniShadowMode **LIGHT_OMNI_SHADOW_CUBE** = `1`

Use a cubemap shadow map for omni lights. Slower but better quality than dual paraboloid.

---

enum **LightDirectionalShadowMode**:

LightDirectionalShadowMode **LIGHT_DIRECTIONAL_SHADOW_ORTHOGONAL** = `0`

Use orthogonal shadow projection for directional light.

LightDirectionalShadowMode **LIGHT_DIRECTIONAL_SHADOW_PARALLEL_2_SPLITS** = `1`

Use 2 splits for shadow projection when using directional light.

LightDirectionalShadowMode **LIGHT_DIRECTIONAL_SHADOW_PARALLEL_4_SPLITS** = `2`

Use 4 splits for shadow projection when using directional light.

---

enum **LightDirectionalSkyMode**:

LightDirectionalSkyMode **LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_AND_SKY** = `0`

Use DirectionalLight3D in both sky rendering and scene lighting.

LightDirectionalSkyMode **LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_ONLY** = `1`

Only use DirectionalLight3D in scene lighting.

LightDirectionalSkyMode **LIGHT_DIRECTIONAL_SKY_MODE_SKY_ONLY** = `2`

Only use DirectionalLight3D in sky rendering.

---

enum **ShadowQuality**:

ShadowQuality **SHADOW_QUALITY_HARD** = `0`

Lowest shadow filtering quality (fastest). Soft shadows are not available with this quality setting, which means the [Light3D.shadow_blur](class_light3d.md#class-light3d-property-shadow-blur) property is ignored if [Light3D.light_size](class_light3d.md#class-light3d-property-light-size) and [Light3D.light_angular_distance](class_light3d.md#class-light3d-property-light-angular-distance) is `0.0`.

**Note:** The variable shadow blur performed by [Light3D.light_size](class_light3d.md#class-light3d-property-light-size) and [Light3D.light_angular_distance](class_light3d.md#class-light3d-property-light-angular-distance) is still effective when using hard shadow filtering. In this case, [Light3D.shadow_blur](class_light3d.md#class-light3d-property-shadow-blur) *is* taken into account. However, the results will not be blurred, instead the blur amount is treated as a maximum radius for the penumbra.

ShadowQuality **SHADOW_QUALITY_SOFT_VERY_LOW** = `1`

Very low shadow filtering quality (faster). When using this quality setting, [Light3D.shadow_blur](class_light3d.md#class-light3d-property-shadow-blur) is automatically multiplied by 0.75× to avoid introducing too much noise. This division only applies to lights whose [Light3D.light_size](class_light3d.md#class-light3d-property-light-size) or [Light3D.light_angular_distance](class_light3d.md#class-light3d-property-light-angular-distance) is `0.0`).

ShadowQuality **SHADOW_QUALITY_SOFT_LOW** = `2`

Low shadow filtering quality (fast).

ShadowQuality **SHADOW_QUALITY_SOFT_MEDIUM** = `3`

Medium low shadow filtering quality (average).

ShadowQuality **SHADOW_QUALITY_SOFT_HIGH** = `4`

High low shadow filtering quality (slow). When using this quality setting, [Light3D.shadow_blur](class_light3d.md#class-light3d-property-shadow-blur) is automatically multiplied by 1.5× to better make use of the high sample count. This increased blur also improves the stability of dynamic object shadows. This multiplier only applies to lights whose [Light3D.light_size](class_light3d.md#class-light3d-property-light-size) or [Light3D.light_angular_distance](class_light3d.md#class-light3d-property-light-angular-distance) is `0.0`).

ShadowQuality **SHADOW_QUALITY_SOFT_ULTRA** = `5`

Highest low shadow filtering quality (slowest). When using this quality setting, [Light3D.shadow_blur](class_light3d.md#class-light3d-property-shadow-blur) is automatically multiplied by 2× to better make use of the high sample count. This increased blur also improves the stability of dynamic object shadows. This multiplier only applies to lights whose [Light3D.light_size](class_light3d.md#class-light3d-property-light-size) or [Light3D.light_angular_distance](class_light3d.md#class-light3d-property-light-angular-distance) is `0.0`).

ShadowQuality **SHADOW_QUALITY_MAX** = `6`

Represents the size of the ShadowQuality enum.

---

enum **ReflectionProbeUpdateMode**:

ReflectionProbeUpdateMode **REFLECTION_PROBE_UPDATE_ONCE** = `0`

Reflection probe will update reflections once and then stop.

ReflectionProbeUpdateMode **REFLECTION_PROBE_UPDATE_ALWAYS** = `1`

Reflection probe will update each frame. This mode is necessary to capture moving objects.

---

enum **ReflectionProbeAmbientMode**:

ReflectionProbeAmbientMode **REFLECTION_PROBE_AMBIENT_DISABLED** = `0`

Do not apply any ambient lighting inside the reflection probe's box defined by its size.

ReflectionProbeAmbientMode **REFLECTION_PROBE_AMBIENT_ENVIRONMENT** = `1`

Apply automatically-sourced environment lighting inside the reflection probe's box defined by its size.

ReflectionProbeAmbientMode **REFLECTION_PROBE_AMBIENT_COLOR** = `2`

Apply custom ambient lighting inside the reflection probe's box defined by its size. See reflection_probe_set_ambient_color() and reflection_probe_set_ambient_energy().

---

enum **DecalTexture**:

DecalTexture **DECAL_TEXTURE_ALBEDO** = `0`

Albedo texture slot in a decal ([Decal.texture_albedo](class_decal.md#class-decal-property-texture-albedo)).

DecalTexture **DECAL_TEXTURE_NORMAL** = `1`

Normal map texture slot in a decal ([Decal.texture_normal](class_decal.md#class-decal-property-texture-normal)).

DecalTexture **DECAL_TEXTURE_ORM** = `2`

Occlusion/Roughness/Metallic texture slot in a decal ([Decal.texture_orm](class_decal.md#class-decal-property-texture-orm)).

DecalTexture **DECAL_TEXTURE_EMISSION** = `3`

Emission texture slot in a decal ([Decal.texture_emission](class_decal.md#class-decal-property-texture-emission)).

DecalTexture **DECAL_TEXTURE_MAX** = `4`

Represents the size of the DecalTexture enum.

---

enum **DecalFilter**:

DecalFilter **DECAL_FILTER_NEAREST** = `0`

Nearest-neighbor filter for decals (use for pixel art decals). No mipmaps are used for rendering, which means decals at a distance will look sharp but grainy. This has roughly the same performance cost as using mipmaps.

DecalFilter **DECAL_FILTER_LINEAR** = `1`

Linear filter for decals (use for non-pixel art decals). No mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as using mipmaps.

DecalFilter **DECAL_FILTER_NEAREST_MIPMAPS** = `2`

Nearest-neighbor filter for decals (use for pixel art decals). Isotropic mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.

DecalFilter **DECAL_FILTER_LINEAR_MIPMAPS** = `3`

Linear filter for decals (use for non-pixel art decals). Isotropic mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.

DecalFilter **DECAL_FILTER_NEAREST_MIPMAPS_ANISOTROPIC** = `4`

Nearest-neighbor filter for decals (use for pixel art decals). Anisotropic mipmaps are used for rendering, which means decals at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined by [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

DecalFilter **DECAL_FILTER_LINEAR_MIPMAPS_ANISOTROPIC** = `5`

Linear filter for decals (use for non-pixel art decals). Anisotropic mipmaps are used for rendering, which means decals at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined by [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

---

enum **VoxelGIQuality**:

VoxelGIQuality **VOXEL_GI_QUALITY_LOW** = `0`

Low [VoxelGI](class_voxelgi.md#class-voxelgi) rendering quality using 4 cones.

VoxelGIQuality **VOXEL_GI_QUALITY_HIGH** = `1`

High [VoxelGI](class_voxelgi.md#class-voxelgi) rendering quality using 6 cones.

---

enum **ParticlesMode**:

ParticlesMode **PARTICLES_MODE_2D** = `0`

2D particles.

ParticlesMode **PARTICLES_MODE_3D** = `1`

3D particles.

---

enum **ParticlesTransformAlign**:

ParticlesTransformAlign **PARTICLES_TRANSFORM_ALIGN_DISABLED** = `0`

Do not align particle transforms relative to the camera or velocity.

ParticlesTransformAlign **PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD** = `1`

Align each particle's Z axis to face the camera.

ParticlesTransformAlign **PARTICLES_TRANSFORM_ALIGN_Y_TO_VELOCITY** = `2`

Align each particle's Y axis to the velocity vector.

ParticlesTransformAlign **PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD_Y_TO_VELOCITY** = `3`

Align each particle's Z axis to face the camera and Y axis to the velocity vector.

ParticlesTransformAlign **PARTICLES_TRANSFORM_ALIGN_LOCAL_BILLBOARD** = `4`

Billboard each particles around a local axis.

---

enum **ParticlesTransformAlignCustomSrc**:

ParticlesTransformAlignCustomSrc **PARTICLES_ALIGN_CHANNEL_FILTER_DISABLED** = `0`

Do not read from CUSTOM when performing billboarding.

ParticlesTransformAlignCustomSrc **PARTICLES_ALIGN_CHANNEL_FILTER_X** = `1`

Read from `CUSTOM.x` when performing billboarding and use it as an angle, in radians.

ParticlesTransformAlignCustomSrc **PARTICLES_ALIGN_CHANNEL_FILTER_Y** = `2`

Read from `CUSTOM.y` when performing billboarding and use it as an angle, in radians.

ParticlesTransformAlignCustomSrc **PARTICLES_ALIGN_CHANNEL_FILTER_Z** = `3`

Read from `CUSTOM.z` when performing billboarding and use it as an angle, in radians.

ParticlesTransformAlignCustomSrc **PARTICLES_ALIGN_CHANNEL_FILTER_W** = `4`

Read from `CUSTOM.w` when performing billboarding and use it as an angle, in radians.

---

enum **ParticlesTransformAlignAxis**:

ParticlesTransformAlignAxis **PARTICLES_ALIGN_AXIS_X** = `0`

Use the X axis for local billboarding.

ParticlesTransformAlignAxis **PARTICLES_ALIGN_AXIS_Y** = `1`

Use the Y axis for local billboarding.

---

enum **ParticlesDrawOrder**:

ParticlesDrawOrder **PARTICLES_DRAW_ORDER_INDEX** = `0`

Draw particles in the order that they appear in the particles array.

ParticlesDrawOrder **PARTICLES_DRAW_ORDER_LIFETIME** = `1`

Sort particles based on their lifetime. In other words, the particle with the highest lifetime is drawn at the front.

ParticlesDrawOrder **PARTICLES_DRAW_ORDER_REVERSE_LIFETIME** = `2`

Sort particles based on the inverse of their lifetime. In other words, the particle with the lowest lifetime is drawn at the front.

ParticlesDrawOrder **PARTICLES_DRAW_ORDER_VIEW_DEPTH** = `3`

Sort particles based on their distance to the camera.

---

enum **ParticlesCollisionType**:

ParticlesCollisionType **PARTICLES_COLLISION_TYPE_SPHERE_ATTRACT** = `0`

Sphere attractor type for [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) (see [GPUParticlesAttractorSphere3D](class_gpuparticlesattractorsphere3d.md#class-gpuparticlesattractorsphere3d)).

ParticlesCollisionType **PARTICLES_COLLISION_TYPE_BOX_ATTRACT** = `1`

Box attractor type for [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) (see [GPUParticlesAttractorBox3D](class_gpuparticlesattractorbox3d.md#class-gpuparticlesattractorbox3d)).

ParticlesCollisionType **PARTICLES_COLLISION_TYPE_VECTOR_FIELD_ATTRACT** = `2`

Vector field attractor type for [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) (see [GPUParticlesAttractorVectorField3D](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d)).

ParticlesCollisionType **PARTICLES_COLLISION_TYPE_SPHERE_COLLIDE** = `3`

Sphere collision type for [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) (see [GPUParticlesCollisionSphere3D](class_gpuparticlescollisionsphere3d.md#class-gpuparticlescollisionsphere3d)).

ParticlesCollisionType **PARTICLES_COLLISION_TYPE_BOX_COLLIDE** = `4`

Box collision type for [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) (see [GPUParticlesCollisionBox3D](class_gpuparticlescollisionbox3d.md#class-gpuparticlescollisionbox3d)).

ParticlesCollisionType **PARTICLES_COLLISION_TYPE_SDF_COLLIDE** = `5`

Signed distance field collision type for [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) (see [GPUParticlesCollisionSDF3D](class_gpuparticlescollisionsdf3d.md#class-gpuparticlescollisionsdf3d)).

ParticlesCollisionType **PARTICLES_COLLISION_TYPE_HEIGHTFIELD_COLLIDE** = `6`

Heightfield collision type for [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) (see [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d)).

---

enum **ParticlesCollisionHeightfieldResolution**:

ParticlesCollisionHeightfieldResolution **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_256** = `0`

256×256 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d).

ParticlesCollisionHeightfieldResolution **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_512** = `1`

512×512 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d).

ParticlesCollisionHeightfieldResolution **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_1024** = `2`

1024×1024 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d).

ParticlesCollisionHeightfieldResolution **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_2048** = `3`

2048×2048 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d).

ParticlesCollisionHeightfieldResolution **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_4096** = `4`

4096×4096 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d).

ParticlesCollisionHeightfieldResolution **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_8192** = `5`

8192×8192 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d).

ParticlesCollisionHeightfieldResolution **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_MAX** = `6`

Represents the size of the ParticlesCollisionHeightfieldResolution enum.

---

enum **FogVolumeShape**:

FogVolumeShape **FOG_VOLUME_SHAPE_ELLIPSOID** = `0`

[FogVolume](class_fogvolume.md#class-fogvolume) will be shaped like an ellipsoid (stretched sphere).

FogVolumeShape **FOG_VOLUME_SHAPE_CONE** = `1`

[FogVolume](class_fogvolume.md#class-fogvolume) will be shaped like a cone pointing upwards (in local coordinates). The cone's angle is set automatically to fill the size. The cone will be adjusted to fit within the size. Rotate the [FogVolume](class_fogvolume.md#class-fogvolume) node to reorient the cone. Non-uniform scaling via size is not supported (scale the [FogVolume](class_fogvolume.md#class-fogvolume) node instead).

FogVolumeShape **FOG_VOLUME_SHAPE_CYLINDER** = `2`

[FogVolume](class_fogvolume.md#class-fogvolume) will be shaped like an upright cylinder (in local coordinates). Rotate the [FogVolume](class_fogvolume.md#class-fogvolume) node to reorient the cylinder. The cylinder will be adjusted to fit within the size. Non-uniform scaling via size is not supported (scale the [FogVolume](class_fogvolume.md#class-fogvolume) node instead).

FogVolumeShape **FOG_VOLUME_SHAPE_BOX** = `3`

[FogVolume](class_fogvolume.md#class-fogvolume) will be shaped like a box.

FogVolumeShape **FOG_VOLUME_SHAPE_WORLD** = `4`

[FogVolume](class_fogvolume.md#class-fogvolume) will have no shape, will cover the whole world and will not be culled.

FogVolumeShape **FOG_VOLUME_SHAPE_MAX** = `5`

Represents the size of the FogVolumeShape enum.

---

enum **ViewportScaling3DMode**:

ViewportScaling3DMode **VIEWPORT_SCALING_3D_MODE_BILINEAR** = `0`

Use bilinear scaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class-viewport-property-scaling-3d-scale). Values less than `1.0` will result in undersampling while values greater than `1.0` will result in supersampling. A value of `1.0` disables scaling.

ViewportScaling3DMode **VIEWPORT_SCALING_3D_MODE_FSR** = `1`

Use AMD FidelityFX Super Resolution 1.0 upscaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class-viewport-property-scaling-3d-scale). Values less than `1.0` will result in the viewport being upscaled using FSR. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` disables scaling.

ViewportScaling3DMode **VIEWPORT_SCALING_3D_MODE_FSR2** = `2`

Use AMD FidelityFX Super Resolution 2.2 upscaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class-viewport-property-scaling-3d-scale). Values less than `1.0` will result in the viewport being upscaled using FSR2. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` will use FSR2 at native resolution as a TAA solution.

ViewportScaling3DMode **VIEWPORT_SCALING_3D_MODE_METALFX_SPATIAL** = `3`

Use MetalFX spatial upscaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class-viewport-property-scaling-3d-scale). Values less than `1.0` will result in the viewport being upscaled using MetalFX. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` disables scaling.

**Note:** Only supported when the Metal rendering driver is in use, which limits this scaling mode to macOS and iOS.

ViewportScaling3DMode **VIEWPORT_SCALING_3D_MODE_METALFX_TEMPORAL** = `4`

Use MetalFX temporal upscaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class-viewport-property-scaling-3d-scale). Values less than `1.0` will result in the viewport being upscaled using MetalFX. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` will use MetalFX at native resolution as a TAA solution.

**Note:** Only supported when the Metal rendering driver is in use, which limits this scaling mode to macOS and iOS.

ViewportScaling3DMode **VIEWPORT_SCALING_3D_MODE_NEAREST** = `5`

Use nearest-neighbor filtering for the viewport's 3D buffer. This looks crisper than VIEWPORT_SCALING_3D_MODE_BILINEAR and has no additional rendering cost. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class-viewport-property-scaling-3d-scale). Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` disables scaling.

**Note:** When using the **Nearest** scaling mode, to avoid uneven pixel scaling, it's highly recommended to use a value equal to an integer divisor with a dividend of `1`. For example, it's best to use a scale of `0.5` (1/2), `0.3333` (1/3), `0.25` (1/4), `0.2` (1/5), and so on.

ViewportScaling3DMode **VIEWPORT_SCALING_3D_MODE_MAX** = `6`

Represents the size of the ViewportScaling3DMode enum.

---

enum **ViewportUpdateMode**:

ViewportUpdateMode **VIEWPORT_UPDATE_DISABLED** = `0`

Do not update the viewport's render target.

ViewportUpdateMode **VIEWPORT_UPDATE_ONCE** = `1`

Update the viewport's render target once, then switch to VIEWPORT_UPDATE_DISABLED.

ViewportUpdateMode **VIEWPORT_UPDATE_WHEN_VISIBLE** = `2`

Update the viewport's render target only when it is visible. This is the default value.

ViewportUpdateMode **VIEWPORT_UPDATE_WHEN_PARENT_VISIBLE** = `3`

Update the viewport's render target only when its parent is visible.

ViewportUpdateMode **VIEWPORT_UPDATE_ALWAYS** = `4`

Always update the viewport's render target.

---

enum **ViewportClearMode**:

ViewportClearMode **VIEWPORT_CLEAR_ALWAYS** = `0`

Always clear the viewport's render target before drawing.

ViewportClearMode **VIEWPORT_CLEAR_NEVER** = `1`

Never clear the viewport's render target.

ViewportClearMode **VIEWPORT_CLEAR_ONLY_NEXT_FRAME** = `2`

Clear the viewport's render target on the next frame, then switch to VIEWPORT_CLEAR_NEVER.

---

enum **ViewportEnvironmentMode**:

ViewportEnvironmentMode **VIEWPORT_ENVIRONMENT_DISABLED** = `0`

Disable rendering of 3D environment over 2D canvas.

ViewportEnvironmentMode **VIEWPORT_ENVIRONMENT_ENABLED** = `1`

Enable rendering of 3D environment over 2D canvas.

ViewportEnvironmentMode **VIEWPORT_ENVIRONMENT_INHERIT** = `2`

Inherit enable/disable value from parent. If the topmost parent is also set to VIEWPORT_ENVIRONMENT_INHERIT, then this has the same behavior as VIEWPORT_ENVIRONMENT_ENABLED.

ViewportEnvironmentMode **VIEWPORT_ENVIRONMENT_MAX** = `3`

Represents the size of the ViewportEnvironmentMode enum.

---

enum **ViewportSDFOversize**:

ViewportSDFOversize **VIEWPORT_SDF_OVERSIZE_100_PERCENT** = `0`

Do not oversize the 2D signed distance field. Occluders may disappear when touching the viewport's edges, and [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d) collision may stop working earlier than intended. This has the lowest GPU requirements.

ViewportSDFOversize **VIEWPORT_SDF_OVERSIZE_120_PERCENT** = `1`

2D signed distance field covers 20% of the viewport's size outside the viewport on each side (top, right, bottom, left).

ViewportSDFOversize **VIEWPORT_SDF_OVERSIZE_150_PERCENT** = `2`

2D signed distance field covers 50% of the viewport's size outside the viewport on each side (top, right, bottom, left).

ViewportSDFOversize **VIEWPORT_SDF_OVERSIZE_200_PERCENT** = `3`

2D signed distance field covers 100% of the viewport's size outside the viewport on each side (top, right, bottom, left). This has the highest GPU requirements.

ViewportSDFOversize **VIEWPORT_SDF_OVERSIZE_MAX** = `4`

Represents the size of the ViewportSDFOversize enum.

---

enum **ViewportSDFScale**:

ViewportSDFScale **VIEWPORT_SDF_SCALE_100_PERCENT** = `0`

Full resolution 2D signed distance field scale. This has the highest GPU requirements.

ViewportSDFScale **VIEWPORT_SDF_SCALE_50_PERCENT** = `1`

Half resolution 2D signed distance field scale on each axis (25% of the viewport pixel count).

ViewportSDFScale **VIEWPORT_SDF_SCALE_25_PERCENT** = `2`

Quarter resolution 2D signed distance field scale on each axis (6.25% of the viewport pixel count). This has the lowest GPU requirements.

ViewportSDFScale **VIEWPORT_SDF_SCALE_MAX** = `3`

Represents the size of the ViewportSDFScale enum.

---

enum **ViewportMSAA**:

ViewportMSAA **VIEWPORT_MSAA_DISABLED** = `0`

Multisample antialiasing for 3D is disabled. This is the default value, and also the fastest setting.

ViewportMSAA **VIEWPORT_MSAA_2X** = `1`

Multisample antialiasing uses 2 samples per pixel for 3D. This has a moderate impact on performance.

ViewportMSAA **VIEWPORT_MSAA_4X** = `2`

Multisample antialiasing uses 4 samples per pixel for 3D. This has a high impact on performance.

ViewportMSAA **VIEWPORT_MSAA_8X** = `3`

Multisample antialiasing uses 8 samples per pixel for 3D. This has a very high impact on performance. Likely unsupported on low-end and older hardware.

ViewportMSAA **VIEWPORT_MSAA_MAX** = `4`

Represents the size of the ViewportMSAA enum.

---

enum **ViewportAnisotropicFiltering**:

ViewportAnisotropicFiltering **VIEWPORT_ANISOTROPY_DISABLED** = `0`

Anisotropic filtering is disabled.

ViewportAnisotropicFiltering **VIEWPORT_ANISOTROPY_2X** = `1`

Use 2× anisotropic filtering.

ViewportAnisotropicFiltering **VIEWPORT_ANISOTROPY_4X** = `2`

Use 4× anisotropic filtering. This is the default value.

ViewportAnisotropicFiltering **VIEWPORT_ANISOTROPY_8X** = `3`

Use 8× anisotropic filtering.

ViewportAnisotropicFiltering **VIEWPORT_ANISOTROPY_16X** = `4`

Use 16× anisotropic filtering.

ViewportAnisotropicFiltering **VIEWPORT_ANISOTROPY_MAX** = `5`

Represents the size of the ViewportAnisotropicFiltering enum.

---

enum **ViewportScreenSpaceAA**:

ViewportScreenSpaceAA **VIEWPORT_SCREEN_SPACE_AA_DISABLED** = `0`

Do not perform any antialiasing in the full screen post-process.

ViewportScreenSpaceAA **VIEWPORT_SCREEN_SPACE_AA_FXAA** = `1`

Use fast approximate antialiasing. FXAA is a popular screen-space antialiasing method, which is fast but will make the image look blurry, especially at lower resolutions. It can still work relatively well at large resolutions such as 1440p and 4K.

ViewportScreenSpaceAA **VIEWPORT_SCREEN_SPACE_AA_SMAA** = `2`

Use subpixel morphological antialiasing. SMAA may produce clearer results than FXAA, but at a slightly higher performance cost.

ViewportScreenSpaceAA **VIEWPORT_SCREEN_SPACE_AA_MAX** = `3`

Represents the size of the ViewportScreenSpaceAA enum.

---

enum **ViewportOcclusionCullingBuildQuality**:

ViewportOcclusionCullingBuildQuality **VIEWPORT_OCCLUSION_BUILD_QUALITY_LOW** = `0`

Low occlusion culling BVH build quality (as defined by Embree). Results in the lowest CPU usage, but least effective culling.

ViewportOcclusionCullingBuildQuality **VIEWPORT_OCCLUSION_BUILD_QUALITY_MEDIUM** = `1`

Medium occlusion culling BVH build quality (as defined by Embree).

ViewportOcclusionCullingBuildQuality **VIEWPORT_OCCLUSION_BUILD_QUALITY_HIGH** = `2`

High occlusion culling BVH build quality (as defined by Embree). Results in the highest CPU usage, but most effective culling.

---

enum **ViewportRenderInfo**:

ViewportRenderInfo **VIEWPORT_RENDER_INFO_OBJECTS_IN_FRAME** = `0`

Number of objects drawn in a single frame.

ViewportRenderInfo **VIEWPORT_RENDER_INFO_PRIMITIVES_IN_FRAME** = `1`

Number of points, lines, or triangles drawn in a single frame.

ViewportRenderInfo **VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME** = `2`

Number of draw calls during this frame.

ViewportRenderInfo **VIEWPORT_RENDER_INFO_MAX** = `3`

Represents the size of the ViewportRenderInfo enum.

---

enum **ViewportRenderInfoType**:

ViewportRenderInfoType **VIEWPORT_RENDER_INFO_TYPE_VISIBLE** = `0`

Visible render pass (excluding shadows).

ViewportRenderInfoType **VIEWPORT_RENDER_INFO_TYPE_SHADOW** = `1`

Shadow render pass. Objects will be rendered several times depending on the number of amounts of lights with shadows and the number of directional shadow splits.

ViewportRenderInfoType **VIEWPORT_RENDER_INFO_TYPE_CANVAS** = `2`

Canvas item rendering. This includes all 2D rendering.

ViewportRenderInfoType **VIEWPORT_RENDER_INFO_TYPE_MAX** = `3`

Represents the size of the ViewportRenderInfoType enum.

---

enum **ViewportDebugDraw**:

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_DISABLED** = `0`

Debug draw is disabled. Default setting.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_UNSHADED** = `1`

Objects are displayed without light information.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_LIGHTING** = `2`

Objects are displayed with only light information.

**Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_OVERDRAW** = `3`

Objects are displayed semi-transparent with additive blending so you can see where they are drawing over top of one another. A higher overdraw (represented by brighter colors) means you are wasting performance on drawing pixels that are being hidden behind others.

**Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_WIREFRAME** = `4`

Debug draw draws objects in wireframe.

**Note:** set_debug_generate_wireframes() must be called before loading any meshes for wireframes to be visible when using the Compatibility renderer.

**Note:** In the Compatibility renderer, backfaces are always visible when using wireframe rendering. In the Forward+ and Mobile renderers, wireframes follow the material's backface culling properties instead.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_NORMAL_BUFFER** = `5`

Normal buffer is drawn instead of regular scene so you can see the per-pixel normals that will be used by post-processing effects.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_VOXEL_GI_ALBEDO** = `6`

Objects are displayed with only the albedo value from [VoxelGI](class_voxelgi.md#class-voxelgi)s. Requires at least one visible [VoxelGI](class_voxelgi.md#class-voxelgi) node that has been baked to have a visible effect.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_VOXEL_GI_LIGHTING** = `7`

Objects are displayed with only the lighting value from [VoxelGI](class_voxelgi.md#class-voxelgi)s. Requires at least one visible [VoxelGI](class_voxelgi.md#class-voxelgi) node that has been baked to have a visible effect.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_VOXEL_GI_EMISSION** = `8`

Objects are displayed with only the emission color from [VoxelGI](class_voxelgi.md#class-voxelgi)s. Requires at least one visible [VoxelGI](class_voxelgi.md#class-voxelgi) node that has been baked to have a visible effect.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_SHADOW_ATLAS** = `9`

Draws the shadow atlas that stores shadows from [OmniLight3D](class_omnilight3d.md#class-omnilight3d)s and [SpotLight3D](class_spotlight3d.md#class-spotlight3d)s in the upper left quadrant of the [Viewport](class_viewport.md#class-viewport).

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS** = `10`

Draws the shadow atlas that stores shadows from [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d)s in the upper left quadrant of the [Viewport](class_viewport.md#class-viewport).

The slice of the camera frustum related to the shadow map cascade is superimposed to visualize coverage. The color of each slice matches the colors used for VIEWPORT_DEBUG_DRAW_PSSM_SPLITS. When shadow cascades are blended the overlap is taken into account when drawing the frustum slices.

The last cascade shows all frustum slices to illustrate the coverage of all slices.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_SCENE_LUMINANCE** = `11`

Draws the estimated scene luminance. This is a 1×1 texture that is generated when autoexposure is enabled to control the scene's exposure.

**Note:** Only supported when using the Forward+ or Mobile rendering methods.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_SSAO** = `12`

Draws the screen space ambient occlusion texture instead of the scene so that you can clearly see how it is affecting objects. In order for this display mode to work, you must have [Environment.ssao_enabled](class_environment.md#class-environment-property-ssao-enabled) set in your [WorldEnvironment](class_worldenvironment.md#class-worldenvironment).

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_SSIL** = `13`

Draws the screen space indirect lighting texture instead of the scene so that you can clearly see how it is affecting objects. In order for this display mode to work, you must have [Environment.ssil_enabled](class_environment.md#class-environment-property-ssil-enabled) set in your [WorldEnvironment](class_worldenvironment.md#class-worldenvironment).

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_PSSM_SPLITS** = `14`

Colors each PSSM split for the [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d)s in the scene a different color so you can see where the splits are. In order (from closest to furthest from the camera), they are colored red, green, blue, and yellow.

**Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

**Note:** Only supported when using the Forward+ or Mobile rendering methods.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_DECAL_ATLAS** = `15`

Draws the decal atlas that stores decal textures from [Decal](class_decal.md#class-decal)s.

**Note:** Only supported when using the Forward+ or Mobile rendering methods.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_SDFGI** = `16`

Draws SDFGI cascade data. This is the data structure that is used to bounce lighting against and create reflections.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_SDFGI_PROBES** = `17`

Draws SDFGI probe data. This is the data structure that is used to give indirect lighting dynamic objects moving within the scene.

When in the editor, left-clicking a probe will display additional bright dots that show its occlusion information. A white dot means the light is not occluded at all at the dot's position, while a red dot means the light is fully occluded. Intermediate values are possible.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_GI_BUFFER** = `18`

Draws the global illumination buffer from [VoxelGI](class_voxelgi.md#class-voxelgi) or SDFGI. Requires [VoxelGI](class_voxelgi.md#class-voxelgi) (at least one visible baked VoxelGI node) or SDFGI ([Environment.sdfgi_enabled](class_environment.md#class-environment-property-sdfgi-enabled)) to be enabled to have a visible effect.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_DISABLE_LOD** = `19`

Disable mesh LOD. All meshes are drawn with full detail, which can be used to compare performance.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS** = `20`

Draws the [OmniLight3D](class_omnilight3d.md#class-omnilight3d) cluster. Clustering determines where lights are positioned in screen-space, which allows the engine to only process these portions of the screen for lighting.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS** = `21`

Draws the [SpotLight3D](class_spotlight3d.md#class-spotlight3d) cluster. Clustering determines where lights are positioned in screen-space, which allows the engine to only process these portions of the screen for lighting.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_CLUSTER_DECALS** = `22`

Draws the [Decal](class_decal.md#class-decal) cluster. Clustering determines where decals are positioned in screen-space, which allows the engine to only process these portions of the screen for decals.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES** = `23`

Draws the [ReflectionProbe](class_reflectionprobe.md#class-reflectionprobe) cluster. Clustering determines where reflection probes are positioned in screen-space, which allows the engine to only process these portions of the screen for reflection probes.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_OCCLUDERS** = `24`

Draws the occlusion culling buffer. This low-resolution occlusion culling buffer is rasterized on the CPU and is used to check whether instances are occluded by other objects.

**Note:** Only supported when using the Forward+ or Mobile rendering methods.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_MOTION_VECTORS** = `25`

Draws the motion vectors buffer. This is used by temporal antialiasing to correct for motion that occurs during gameplay.

**Note:** Only supported when using the Forward+ rendering method.

ViewportDebugDraw **VIEWPORT_DEBUG_DRAW_INTERNAL_BUFFER** = `26`

Internal buffer is drawn instead of regular scene so you can see the per-pixel output that will be used by post-processing effects.

**Note:** Only supported when using the Forward+ or Mobile rendering methods.

---

enum **ViewportVRSMode**:

ViewportVRSMode **VIEWPORT_VRS_DISABLED** = `0`

Variable rate shading is disabled.

ViewportVRSMode **VIEWPORT_VRS_TEXTURE** = `1`

Variable rate shading uses a texture. Note, for stereoscopic use a texture atlas with a texture for each view.

ViewportVRSMode **VIEWPORT_VRS_XR** = `2`

Variable rate shading texture is supplied by the primary [XRInterface](class_xrinterface.md#class-xrinterface). Note that this may override the update mode.

ViewportVRSMode **VIEWPORT_VRS_MAX** = `3`

Represents the size of the ViewportVRSMode enum.

---

enum **ViewportVRSUpdateMode**:

ViewportVRSUpdateMode **VIEWPORT_VRS_UPDATE_DISABLED** = `0`

The input texture for variable rate shading will not be processed.

ViewportVRSUpdateMode **VIEWPORT_VRS_UPDATE_ONCE** = `1`

The input texture for variable rate shading will be processed once.

ViewportVRSUpdateMode **VIEWPORT_VRS_UPDATE_ALWAYS** = `2`

The input texture for variable rate shading will be processed each frame.

ViewportVRSUpdateMode **VIEWPORT_VRS_UPDATE_MAX** = `3`

Represents the size of the ViewportVRSUpdateMode enum.

---

enum **SkyMode**:

SkyMode **SKY_MODE_AUTOMATIC** = `0`

Automatically selects the appropriate process mode based on your sky shader. If your shader uses `TIME` or `POSITION`, this will use SKY_MODE_REALTIME. If your shader uses any of the `LIGHT_*` variables or any custom uniforms, this uses SKY_MODE_INCREMENTAL. Otherwise, this defaults to SKY_MODE_QUALITY.

SkyMode **SKY_MODE_QUALITY** = `1`

Uses high quality importance sampling to process the radiance map. In general, this results in much higher quality than SKY_MODE_REALTIME but takes much longer to generate. This should not be used if you plan on changing the sky at runtime. If you are finding that the reflection is not blurry enough and is showing sparkles or fireflies, try increasing [ProjectSettings.rendering/reflections/sky_reflections/ggx_samples](class_projectsettings.md#class-projectsettings-property-rendering-reflections-sky-reflections-ggx-samples).

SkyMode **SKY_MODE_INCREMENTAL** = `2`

Uses the same high quality importance sampling to process the radiance map as SKY_MODE_QUALITY, but updates over several frames. The number of frames is determined by [ProjectSettings.rendering/reflections/sky_reflections/roughness_layers](class_projectsettings.md#class-projectsettings-property-rendering-reflections-sky-reflections-roughness-layers). Use this when you need highest quality radiance maps, but have a sky that updates slowly.

SkyMode **SKY_MODE_REALTIME** = `3`

Uses the fast filtering algorithm to process the radiance map. In general this results in lower quality, but substantially faster run times. If you need better quality, but still need to update the sky every frame, consider turning on [ProjectSettings.rendering/reflections/sky_reflections/fast_filter_high_quality](class_projectsettings.md#class-projectsettings-property-rendering-reflections-sky-reflections-fast-filter-high-quality).

**Note:** The fast filtering algorithm is limited to 256×256 cubemaps, so sky_set_radiance_size() must be set to `256`. Otherwise, a warning is printed and the overridden radiance size is ignored.

---

enum **CompositorEffectFlags**:

CompositorEffectFlags **COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_COLOR** = `1`

The rendering effect requires the color buffer to be resolved if MSAA is enabled.

CompositorEffectFlags **COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_DEPTH** = `2`

The rendering effect requires the depth buffer to be resolved if MSAA is enabled.

CompositorEffectFlags **COMPOSITOR_EFFECT_FLAG_NEEDS_MOTION_VECTORS** = `4`

The rendering effect requires motion vectors to be produced.

CompositorEffectFlags **COMPOSITOR_EFFECT_FLAG_NEEDS_ROUGHNESS** = `8`

The rendering effect requires normals and roughness g-buffer to be produced (Forward+ only).

CompositorEffectFlags **COMPOSITOR_EFFECT_FLAG_NEEDS_SEPARATE_SPECULAR** = `16`

The rendering effect requires specular data to be separated out (Forward+ only).

---

enum **CompositorEffectCallbackType**:

CompositorEffectCallbackType **COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_OPAQUE** = `0`

The callback is called before our opaque rendering pass, but after depth prepass (if applicable).

CompositorEffectCallbackType **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_OPAQUE** = `1`

The callback is called after our opaque rendering pass, but before our sky is rendered.

CompositorEffectCallbackType **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_SKY** = `2`

The callback is called after our sky is rendered, but before our back buffers are created (and if enabled, before subsurface scattering and/or screen space reflections).

CompositorEffectCallbackType **COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_TRANSPARENT** = `3`

The callback is called before our transparent rendering pass, but after our sky is rendered and we've created our back buffers.

CompositorEffectCallbackType **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_TRANSPARENT** = `4`

The callback is called after our transparent rendering pass, but before any built-in post-processing effects and output to our render target.

CompositorEffectCallbackType **COMPOSITOR_EFFECT_CALLBACK_TYPE_ANY** = `-1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

enum **EnvironmentBG**:

EnvironmentBG **ENV_BG_CLEAR_COLOR** = `0`

Use the clear color as background.

EnvironmentBG **ENV_BG_COLOR** = `1`

Use a specified color as the background.

EnvironmentBG **ENV_BG_SKY** = `2`

Use a sky resource for the background.

EnvironmentBG **ENV_BG_CANVAS** = `3`

Use a specified canvas layer as the background. This can be useful for instantiating a 2D scene in a 3D world.

EnvironmentBG **ENV_BG_KEEP** = `4`

Do not clear the background, use whatever was rendered last frame as the background.

EnvironmentBG **ENV_BG_CAMERA_FEED** = `5`

Displays a camera feed in the background.

EnvironmentBG **ENV_BG_MAX** = `6`

Represents the size of the EnvironmentBG enum.

---

enum **EnvironmentAmbientSource**:

EnvironmentAmbientSource **ENV_AMBIENT_SOURCE_BG** = `0`

Gather ambient light from whichever source is specified as the background.

EnvironmentAmbientSource **ENV_AMBIENT_SOURCE_DISABLED** = `1`

Disable ambient light.

EnvironmentAmbientSource **ENV_AMBIENT_SOURCE_COLOR** = `2`

Specify a specific [Color](class_color.md#class-color) for ambient light.

EnvironmentAmbientSource **ENV_AMBIENT_SOURCE_SKY** = `3`

Gather ambient light from the [Sky](class_sky.md#class-sky) regardless of what the background is.

---

enum **EnvironmentReflectionSource**:

EnvironmentReflectionSource **ENV_REFLECTION_SOURCE_BG** = `0`

Use the background for reflections.

EnvironmentReflectionSource **ENV_REFLECTION_SOURCE_DISABLED** = `1`

Disable reflections.

EnvironmentReflectionSource **ENV_REFLECTION_SOURCE_SKY** = `2`

Use the [Sky](class_sky.md#class-sky) for reflections regardless of what the background is.

---

enum **EnvironmentGlowBlendMode**:

EnvironmentGlowBlendMode **ENV_GLOW_BLEND_MODE_ADDITIVE** = `0`

Adds the glow effect to the scene.

EnvironmentGlowBlendMode **ENV_GLOW_BLEND_MODE_SCREEN** = `1`

Adds the glow effect to the scene after modifying the glow influence based on the scene value; dark values will be highly influenced by glow and bright values will not be influenced by glow. This approach avoids bright values becoming overly bright from the glow effect. [Environment.tonemap_white](class_environment.md#class-environment-property-tonemap-white) is used to determine the maximum scene value where the glow should have no influence. When [Environment.tonemap_mode](class_environment.md#class-environment-property-tonemap-mode) is set to [Environment.TONE_MAPPER_LINEAR](class_environment.md#class-environment-constant-tone-mapper-linear) and [Viewport.use_hdr_2d](class_viewport.md#class-viewport-property-use-hdr-2d) is `true`, the parent window's [Window.get_output_max_linear_value()](class_window.md#class-window-method-get-output-max-linear-value) will be used as the maximum scene value.

EnvironmentGlowBlendMode **ENV_GLOW_BLEND_MODE_SOFTLIGHT** = `2`

Adds the glow effect to the tonemapped image after modifying the glow influence based on the image value; dark values and bright values will not be influenced by glow and mid-range values will be highly influenced by glow. This approach avoids bright values becoming overly bright from the glow effect. The glow will have the largest influence on image values of `0.25` and will have no influence when applied to image values greater than `1.0`.

**Note:** This blend mode does not support HDR output because expects a maximum output value of `1.0`. It is recommended to use a different blend mode when rendering to an HDR screen.

EnvironmentGlowBlendMode **ENV_GLOW_BLEND_MODE_REPLACE** = `3`

Replaces all pixels' color by the glow effect. This can be used to simulate a full-screen blur effect by tweaking the glow parameters to match the original image's brightness or to preview glow configuration in the editor.

EnvironmentGlowBlendMode **ENV_GLOW_BLEND_MODE_MIX** = `4`

Mixes the glow image with the scene image. Best used with [Environment.glow_bloom](class_environment.md#class-environment-property-glow-bloom) to avoid darkening the scene.

---

enum **EnvironmentFogMode**:

EnvironmentFogMode **ENV_FOG_MODE_EXPONENTIAL** = `0`

Use a physically-based fog model defined primarily by fog density.

EnvironmentFogMode **ENV_FOG_MODE_DEPTH** = `1`

Use a simple fog model defined by start and end positions and a custom curve. While not physically accurate, this model can be useful when you need more artistic control.

---

enum **EnvironmentToneMapper**:

EnvironmentToneMapper **ENV_TONE_MAPPER_LINEAR** = `0`

Does not modify color data, resulting in a linear tonemapping curve which unnaturally clips bright values, causing bright lighting to look blown out. The simplest and fastest tonemapper.

EnvironmentToneMapper **ENV_TONE_MAPPER_REINHARD** = `1`

A simple tonemapping curve that rolls off bright values to prevent clipping. This results in an image that can appear dull and low contrast. Slower than ENV_TONE_MAPPER_LINEAR.

**Note:** When [Environment.tonemap_white](class_environment.md#class-environment-property-tonemap-white) is left at the default value of `1.0`, ENV_TONE_MAPPER_REINHARD produces an identical image to ENV_TONE_MAPPER_LINEAR.

EnvironmentToneMapper **ENV_TONE_MAPPER_FILMIC** = `2`

Uses a film-like tonemapping curve to prevent clipping of bright values and provide better contrast than ENV_TONE_MAPPER_REINHARD. Slightly slower than ENV_TONE_MAPPER_REINHARD.

**Note:** This tonemapper does not support HDR output because it produces output in the SDR range. It is recommended to use a different tonemapper when rendering to an HDR screen.

EnvironmentToneMapper **ENV_TONE_MAPPER_ACES** = `3`

Uses a high-contrast film-like tonemapping curve and desaturates bright values for a more realistic appearance. Slightly slower than ENV_TONE_MAPPER_FILMIC.

**Note:** This tonemapping operator is called "ACES Fitted" in Godot 3.x.

**Note:** This tonemapper does not support HDR output because it produces output in the SDR range. It is recommended to use a different tonemapper when rendering to an HDR screen.

EnvironmentToneMapper **ENV_TONE_MAPPER_AGX** = `4`

Uses an adjustable film-like tonemapping curve and desaturates bright values for a more realistic appearance. Better than other tonemappers at maintaining the hue of colors as they become brighter. The slowest tonemapping option.

---

enum **EnvironmentSSRRoughnessQuality**:

EnvironmentSSRRoughnessQuality **ENV_SSR_ROUGHNESS_QUALITY_DISABLED** = `0`

Lowest quality of roughness filter for screen-space reflections. Rough materials will not have blurrier screen-space reflections compared to smooth (non-rough) materials. This is the fastest option.

EnvironmentSSRRoughnessQuality **ENV_SSR_ROUGHNESS_QUALITY_LOW** = `1`

Low quality of roughness filter for screen-space reflections.

EnvironmentSSRRoughnessQuality **ENV_SSR_ROUGHNESS_QUALITY_MEDIUM** = `2`

Medium quality of roughness filter for screen-space reflections.

EnvironmentSSRRoughnessQuality **ENV_SSR_ROUGHNESS_QUALITY_HIGH** = `3`

High quality of roughness filter for screen-space reflections. This is the slowest option.

---

enum **EnvironmentSSAOQuality**:

EnvironmentSSAOQuality **ENV_SSAO_QUALITY_VERY_LOW** = `0`

Lowest quality of screen-space ambient occlusion.

EnvironmentSSAOQuality **ENV_SSAO_QUALITY_LOW** = `1`

Low quality screen-space ambient occlusion.

EnvironmentSSAOQuality **ENV_SSAO_QUALITY_MEDIUM** = `2`

Medium quality screen-space ambient occlusion.

EnvironmentSSAOQuality **ENV_SSAO_QUALITY_HIGH** = `3`

High quality screen-space ambient occlusion.

EnvironmentSSAOQuality **ENV_SSAO_QUALITY_ULTRA** = `4`

Highest quality screen-space ambient occlusion. Uses the adaptive target setting which can be dynamically adjusted to smoothly balance performance and visual quality.

---

enum **EnvironmentSSILQuality**:

EnvironmentSSILQuality **ENV_SSIL_QUALITY_VERY_LOW** = `0`

Lowest quality of screen-space indirect lighting.

EnvironmentSSILQuality **ENV_SSIL_QUALITY_LOW** = `1`

Low quality screen-space indirect lighting.

EnvironmentSSILQuality **ENV_SSIL_QUALITY_MEDIUM** = `2`

High quality screen-space indirect lighting.

EnvironmentSSILQuality **ENV_SSIL_QUALITY_HIGH** = `3`

High quality screen-space indirect lighting.

EnvironmentSSILQuality **ENV_SSIL_QUALITY_ULTRA** = `4`

Highest quality screen-space indirect lighting. Uses the adaptive target setting which can be dynamically adjusted to smoothly balance performance and visual quality.

---

enum **EnvironmentSDFGIYScale**:

EnvironmentSDFGIYScale **ENV_SDFGI_Y_SCALE_50_PERCENT** = `0`

Use 50% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be twice as short as they are wide. This allows providing increased GI detail and reduced light leaking with thin floors and ceilings. This is usually the best choice for scenes that don't feature much verticality.

EnvironmentSDFGIYScale **ENV_SDFGI_Y_SCALE_75_PERCENT** = `1`

Use 75% scale for SDFGI on the Y (vertical) axis. This is a balance between the 50% and 100% SDFGI Y scales.

EnvironmentSDFGIYScale **ENV_SDFGI_Y_SCALE_100_PERCENT** = `2`

Use 100% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be as tall as they are wide. This is usually the best choice for highly vertical scenes. The downside is that light leaking may become more noticeable with thin floors and ceilings.

---

enum **EnvironmentSDFGIRayCount**:

EnvironmentSDFGIRayCount **ENV_SDFGI_RAY_COUNT_4** = `0`

Throw 4 rays per frame when converging SDFGI. This has the lowest GPU requirements, but creates the most noisy result.

EnvironmentSDFGIRayCount **ENV_SDFGI_RAY_COUNT_8** = `1`

Throw 8 rays per frame when converging SDFGI.

EnvironmentSDFGIRayCount **ENV_SDFGI_RAY_COUNT_16** = `2`

Throw 16 rays per frame when converging SDFGI.

EnvironmentSDFGIRayCount **ENV_SDFGI_RAY_COUNT_32** = `3`

Throw 32 rays per frame when converging SDFGI.

EnvironmentSDFGIRayCount **ENV_SDFGI_RAY_COUNT_64** = `4`

Throw 64 rays per frame when converging SDFGI.

EnvironmentSDFGIRayCount **ENV_SDFGI_RAY_COUNT_96** = `5`

Throw 96 rays per frame when converging SDFGI. This has high GPU requirements.

EnvironmentSDFGIRayCount **ENV_SDFGI_RAY_COUNT_128** = `6`

Throw 128 rays per frame when converging SDFGI. This has very high GPU requirements, but creates the least noisy result.

EnvironmentSDFGIRayCount **ENV_SDFGI_RAY_COUNT_MAX** = `7`

Represents the size of the EnvironmentSDFGIRayCount enum.

---

enum **EnvironmentSDFGIFramesToConverge**:

EnvironmentSDFGIFramesToConverge **ENV_SDFGI_CONVERGE_IN_5_FRAMES** = `0`

Converge SDFGI over 5 frames. This is the most responsive, but creates the most noisy result with a given ray count.

EnvironmentSDFGIFramesToConverge **ENV_SDFGI_CONVERGE_IN_10_FRAMES** = `1`

Configure SDFGI to fully converge over 10 frames.

EnvironmentSDFGIFramesToConverge **ENV_SDFGI_CONVERGE_IN_15_FRAMES** = `2`

Configure SDFGI to fully converge over 15 frames.

EnvironmentSDFGIFramesToConverge **ENV_SDFGI_CONVERGE_IN_20_FRAMES** = `3`

Configure SDFGI to fully converge over 20 frames.

EnvironmentSDFGIFramesToConverge **ENV_SDFGI_CONVERGE_IN_25_FRAMES** = `4`

Configure SDFGI to fully converge over 25 frames.

EnvironmentSDFGIFramesToConverge **ENV_SDFGI_CONVERGE_IN_30_FRAMES** = `5`

Configure SDFGI to fully converge over 30 frames. This is the least responsive, but creates the least noisy result with a given ray count.

EnvironmentSDFGIFramesToConverge **ENV_SDFGI_CONVERGE_MAX** = `6`

Represents the size of the EnvironmentSDFGIFramesToConverge enum.

---

enum **EnvironmentSDFGIFramesToUpdateLight**:

EnvironmentSDFGIFramesToUpdateLight **ENV_SDFGI_UPDATE_LIGHT_IN_1_FRAME** = `0`

Update indirect light from dynamic lights in SDFGI over 1 frame. This is the most responsive, but has the highest GPU requirements.

EnvironmentSDFGIFramesToUpdateLight **ENV_SDFGI_UPDATE_LIGHT_IN_2_FRAMES** = `1`

Update indirect light from dynamic lights in SDFGI over 2 frames.

EnvironmentSDFGIFramesToUpdateLight **ENV_SDFGI_UPDATE_LIGHT_IN_4_FRAMES** = `2`

Update indirect light from dynamic lights in SDFGI over 4 frames.

EnvironmentSDFGIFramesToUpdateLight **ENV_SDFGI_UPDATE_LIGHT_IN_8_FRAMES** = `3`

Update indirect light from dynamic lights in SDFGI over 8 frames.

EnvironmentSDFGIFramesToUpdateLight **ENV_SDFGI_UPDATE_LIGHT_IN_16_FRAMES** = `4`

Update indirect light from dynamic lights in SDFGI over 16 frames. This is the least responsive, but has the lowest GPU requirements.

EnvironmentSDFGIFramesToUpdateLight **ENV_SDFGI_UPDATE_LIGHT_MAX** = `5`

Represents the size of the EnvironmentSDFGIFramesToUpdateLight enum.

---

enum **SubSurfaceScatteringQuality**:

SubSurfaceScatteringQuality **SUB_SURFACE_SCATTERING_QUALITY_DISABLED** = `0`

Disables subsurface scattering entirely, even on materials that have [BaseMaterial3D.subsurf_scatter_enabled](class_basematerial3d.md#class-basematerial3d-property-subsurf-scatter-enabled) set to `true`. This has the lowest GPU requirements.

SubSurfaceScatteringQuality **SUB_SURFACE_SCATTERING_QUALITY_LOW** = `1`

Low subsurface scattering quality.

SubSurfaceScatteringQuality **SUB_SURFACE_SCATTERING_QUALITY_MEDIUM** = `2`

Medium subsurface scattering quality.

SubSurfaceScatteringQuality **SUB_SURFACE_SCATTERING_QUALITY_HIGH** = `3`

High subsurface scattering quality. This has the highest GPU requirements.

---

enum **DOFBokehShape**:

DOFBokehShape **DOF_BOKEH_BOX** = `0`

Calculate the DOF blur using a box filter. The fastest option, but results in obvious lines in blur pattern.

DOFBokehShape **DOF_BOKEH_HEXAGON** = `1`

Calculates DOF blur using a hexagon shaped filter.

DOFBokehShape **DOF_BOKEH_CIRCLE** = `2`

Calculates DOF blur using a circle shaped filter. Best quality and most realistic, but slowest. Use only for areas where a lot of performance can be dedicated to post-processing (e.g. cutscenes).

---

enum **DOFBlurQuality**:

DOFBlurQuality **DOF_BLUR_QUALITY_VERY_LOW** = `0`

Lowest quality DOF blur. This is the fastest setting, but you may be able to see filtering artifacts.

DOFBlurQuality **DOF_BLUR_QUALITY_LOW** = `1`

Low quality DOF blur.

DOFBlurQuality **DOF_BLUR_QUALITY_MEDIUM** = `2`

Medium quality DOF blur.

DOFBlurQuality **DOF_BLUR_QUALITY_HIGH** = `3`

Highest quality DOF blur. Results in the smoothest looking blur by taking the most samples, but is also significantly slower.

---

enum **InstanceType**:

InstanceType **INSTANCE_NONE** = `0`

The instance does not have a type.

InstanceType **INSTANCE_MESH** = `1`

The instance is a mesh.

InstanceType **INSTANCE_MULTIMESH** = `2`

The instance is a multimesh.

InstanceType **INSTANCE_PARTICLES** = `3`

The instance is a particle emitter.

InstanceType **INSTANCE_PARTICLES_COLLISION** = `4`

The instance is a GPUParticles collision shape.

InstanceType **INSTANCE_LIGHT** = `5`

The instance is a light.

InstanceType **INSTANCE_REFLECTION_PROBE** = `6`

The instance is a reflection probe.

InstanceType **INSTANCE_DECAL** = `7`

The instance is a decal.

InstanceType **INSTANCE_VOXEL_GI** = `8`

The instance is a VoxelGI.

InstanceType **INSTANCE_LIGHTMAP** = `9`

The instance is a lightmap.

InstanceType **INSTANCE_OCCLUDER** = `10`

The instance is an occlusion culling occluder.

InstanceType **INSTANCE_VISIBLITY_NOTIFIER** = `11`

The instance is a visible on-screen notifier.

InstanceType **INSTANCE_FOG_VOLUME** = `12`

The instance is a fog volume.

InstanceType **INSTANCE_MAX** = `13`

Represents the size of the InstanceType enum.

InstanceType **INSTANCE_GEOMETRY_MASK** = `14`

A combination of the flags of geometry instances (mesh, multimesh, immediate and particles).

---

enum **InstanceFlags**:

InstanceFlags **INSTANCE_FLAG_USE_BAKED_LIGHT** = `0`

Allows the instance to be used in baked lighting.

InstanceFlags **INSTANCE_FLAG_USE_DYNAMIC_GI** = `1`

Allows the instance to be used with dynamic global illumination.

InstanceFlags **INSTANCE_FLAG_DRAW_NEXT_FRAME_IF_VISIBLE** = `2`

When set, manually requests to draw geometry on next frame.

InstanceFlags **INSTANCE_FLAG_IGNORE_OCCLUSION_CULLING** = `3`

Always draw, even if the instance would be culled by occlusion culling. Does not affect view frustum culling.

InstanceFlags **INSTANCE_FLAG_MAX** = `4`

Represents the size of the InstanceFlags enum.

---

enum **ShadowCastingSetting**:

ShadowCastingSetting **SHADOW_CASTING_SETTING_OFF** = `0`

Disable shadows from this instance.

ShadowCastingSetting **SHADOW_CASTING_SETTING_ON** = `1`

Cast shadows from this instance.

ShadowCastingSetting **SHADOW_CASTING_SETTING_DOUBLE_SIDED** = `2`

Disable backface culling when rendering the shadow of the object. This is slightly slower but may result in more correct shadows.

ShadowCastingSetting **SHADOW_CASTING_SETTING_SHADOWS_ONLY** = `3`

Only render the shadows from the object. The object itself will not be drawn.

---

enum **VisibilityRangeFadeMode**:

VisibilityRangeFadeMode **VISIBILITY_RANGE_FADE_DISABLED** = `0`

Disable visibility range fading for the given instance.

VisibilityRangeFadeMode **VISIBILITY_RANGE_FADE_SELF** = `1`

Fade-out the given instance when it approaches its visibility range limits.

VisibilityRangeFadeMode **VISIBILITY_RANGE_FADE_DEPENDENCIES** = `2`

Fade-in the given instance's dependencies when reaching its visibility range limits.

---

enum **BakeChannels**:

BakeChannels **BAKE_CHANNEL_ALBEDO_ALPHA** = `0`

Index of [Image](class_image.md#class-image) in array of [Image](class_image.md#class-image)s returned by bake_render_uv2(). Image uses [Image.FORMAT_RGBA8](class_image.md#class-image-constant-format-rgba8) and contains albedo color in the `.rgb` channels and alpha in the `.a` channel.

BakeChannels **BAKE_CHANNEL_NORMAL** = `1`

Index of [Image](class_image.md#class-image) in array of [Image](class_image.md#class-image)s returned by bake_render_uv2(). Image uses [Image.FORMAT_RGBA8](class_image.md#class-image-constant-format-rgba8) and contains the per-pixel normal of the object in the `.rgb` channels and nothing in the `.a` channel. The per-pixel normal is encoded as `normal * 0.5 + 0.5`.

BakeChannels **BAKE_CHANNEL_ORM** = `2`

Index of [Image](class_image.md#class-image) in array of [Image](class_image.md#class-image)s returned by bake_render_uv2(). Image uses [Image.FORMAT_RGBA8](class_image.md#class-image-constant-format-rgba8) and contains ambient occlusion (from material and decals only) in the `.r` channel, roughness in the `.g` channel, metallic in the `.b` channel and sub surface scattering amount in the `.a` channel.

BakeChannels **BAKE_CHANNEL_EMISSION** = `3`

Index of [Image](class_image.md#class-image) in array of [Image](class_image.md#class-image)s returned by bake_render_uv2(). Image uses [Image.FORMAT_RGBAH](class_image.md#class-image-constant-format-rgbah) and contains emission color in the `.rgb` channels and nothing in the `.a` channel.

---

enum **CanvasTextureChannel**:

CanvasTextureChannel **CANVAS_TEXTURE_CHANNEL_DIFFUSE** = `0`

Diffuse canvas texture ([CanvasTexture.diffuse_texture](class_canvastexture.md#class-canvastexture-property-diffuse-texture)).

CanvasTextureChannel **CANVAS_TEXTURE_CHANNEL_NORMAL** = `1`

Normal map canvas texture ([CanvasTexture.normal_texture](class_canvastexture.md#class-canvastexture-property-normal-texture)).

CanvasTextureChannel **CANVAS_TEXTURE_CHANNEL_SPECULAR** = `2`

Specular map canvas texture ([CanvasTexture.specular_texture](class_canvastexture.md#class-canvastexture-property-specular-texture)).

---

enum **NinePatchAxisMode**:

NinePatchAxisMode **NINE_PATCH_STRETCH** = `0`

The nine patch gets stretched where needed.

NinePatchAxisMode **NINE_PATCH_TILE** = `1`

The nine patch gets filled with tiles where needed.

NinePatchAxisMode **NINE_PATCH_TILE_FIT** = `2`

The nine patch gets filled with tiles where needed and stretches them a bit if needed.

---

enum **CanvasItemTextureFilter**:

CanvasItemTextureFilter **CANVAS_ITEM_TEXTURE_FILTER_DEFAULT** = `0`

Uses the default filter mode for this [Viewport](class_viewport.md#class-viewport).

CanvasItemTextureFilter **CANVAS_ITEM_TEXTURE_FILTER_NEAREST** = `1`

The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).

CanvasItemTextureFilter **CANVAS_ITEM_TEXTURE_FILTER_LINEAR** = `2`

The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).

CanvasItemTextureFilter **CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS** = `3`

The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`). This makes the texture look pixelated from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class-camera2d) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

CanvasItemTextureFilter **CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS** = `4`

The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`). This makes the texture look smooth from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class-camera2d) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

CanvasItemTextureFilter **CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC** = `5`

The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

**Note:** This texture filter is rarely useful in 2D projects. CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS is usually more appropriate in this case.

CanvasItemTextureFilter **CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC** = `6`

The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap if [ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-use-nearest-mipmap-filter) is `true`) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting [ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level](class_projectsettings.md#class-projectsettings-property-rendering-textures-default-filters-anisotropic-filtering-level).

**Note:** This texture filter is rarely useful in 2D projects. CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS is usually more appropriate in this case.

CanvasItemTextureFilter **CANVAS_ITEM_TEXTURE_FILTER_MAX** = `7`

Max value for CanvasItemTextureFilter enum.

---

enum **CanvasItemTextureRepeat**:

CanvasItemTextureRepeat **CANVAS_ITEM_TEXTURE_REPEAT_DEFAULT** = `0`

Uses the default repeat mode for this [Viewport](class_viewport.md#class-viewport).

CanvasItemTextureRepeat **CANVAS_ITEM_TEXTURE_REPEAT_DISABLED** = `1`

Disables textures repeating. Instead, when reading UVs outside the 0-1 range, the value will be clamped to the edge of the texture, resulting in a stretched out look at the borders of the texture.

CanvasItemTextureRepeat **CANVAS_ITEM_TEXTURE_REPEAT_ENABLED** = `2`

Enables the texture to repeat when UV coordinates are outside the 0-1 range. If using one of the linear filtering modes, this can result in artifacts at the edges of a texture when the sampler filters across the edges of the texture.

CanvasItemTextureRepeat **CANVAS_ITEM_TEXTURE_REPEAT_MIRROR** = `3`

Flip the texture when repeating so that the edge lines up instead of abruptly changing.

CanvasItemTextureRepeat **CANVAS_ITEM_TEXTURE_REPEAT_MAX** = `4`

Max value for CanvasItemTextureRepeat enum.

---

enum **CanvasGroupMode**:

CanvasGroupMode **CANVAS_GROUP_MODE_DISABLED** = `0`

Child draws over parent and is not clipped.

CanvasGroupMode **CANVAS_GROUP_MODE_CLIP_ONLY** = `1`

Parent is used for the purposes of clipping only. Child is clipped to the parent's visible area, parent is not drawn.

CanvasGroupMode **CANVAS_GROUP_MODE_CLIP_AND_DRAW** = `2`

Parent is used for clipping child, but parent is also drawn underneath child as normal before clipping child to its visible area.

CanvasGroupMode **CANVAS_GROUP_MODE_TRANSPARENT** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

enum **CanvasLightMode**:

CanvasLightMode **CANVAS_LIGHT_MODE_POINT** = `0`

2D point light (see [PointLight2D](class_pointlight2d.md#class-pointlight2d)).

CanvasLightMode **CANVAS_LIGHT_MODE_DIRECTIONAL** = `1`

2D directional (sun/moon) light (see [DirectionalLight2D](class_directionallight2d.md#class-directionallight2d)).

---

enum **CanvasLightBlendMode**:

CanvasLightBlendMode **CANVAS_LIGHT_BLEND_MODE_ADD** = `0`

Adds light color additive to the canvas.

CanvasLightBlendMode **CANVAS_LIGHT_BLEND_MODE_SUB** = `1`

Adds light color subtractive to the canvas.

CanvasLightBlendMode **CANVAS_LIGHT_BLEND_MODE_MIX** = `2`

The light adds color depending on transparency.

---

enum **CanvasLightShadowFilter**:

CanvasLightShadowFilter **CANVAS_LIGHT_FILTER_NONE** = `0`

Do not apply a filter to canvas light shadows.

CanvasLightShadowFilter **CANVAS_LIGHT_FILTER_PCF5** = `1`

Use PCF5 filtering to filter canvas light shadows.

CanvasLightShadowFilter **CANVAS_LIGHT_FILTER_PCF13** = `2`

Use PCF13 filtering to filter canvas light shadows.

CanvasLightShadowFilter **CANVAS_LIGHT_FILTER_MAX** = `3`

Max value of the CanvasLightShadowFilter enum.

---

enum **CanvasOccluderPolygonCullMode**:

CanvasOccluderPolygonCullMode **CANVAS_OCCLUDER_POLYGON_CULL_DISABLED** = `0`

Culling of the canvas occluder is disabled.

CanvasOccluderPolygonCullMode **CANVAS_OCCLUDER_POLYGON_CULL_CLOCKWISE** = `1`

Culling of the canvas occluder is clockwise.

CanvasOccluderPolygonCullMode **CANVAS_OCCLUDER_POLYGON_CULL_COUNTER_CLOCKWISE** = `2`

Culling of the canvas occluder is counterclockwise.

---

enum **GlobalShaderParameterType**:

GlobalShaderParameterType **GLOBAL_VAR_TYPE_BOOL** = `0`

Boolean global shader parameter (`global uniform bool ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_BVEC2** = `1`

2-dimensional boolean vector global shader parameter (`global uniform bvec2 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_BVEC3** = `2`

3-dimensional boolean vector global shader parameter (`global uniform bvec3 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_BVEC4** = `3`

4-dimensional boolean vector global shader parameter (`global uniform bvec4 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_INT** = `4`

Integer global shader parameter (`global uniform int ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_IVEC2** = `5`

2-dimensional integer vector global shader parameter (`global uniform ivec2 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_IVEC3** = `6`

3-dimensional integer vector global shader parameter (`global uniform ivec3 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_IVEC4** = `7`

4-dimensional integer vector global shader parameter (`global uniform ivec4 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_RECT2I** = `8`

2-dimensional integer rectangle global shader parameter (`global uniform ivec4 ...`). Equivalent to GLOBAL_VAR_TYPE_IVEC4 in shader code, but exposed as a [Rect2i](class_rect2i.md#class-rect2i) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_UINT** = `9`

Unsigned integer global shader parameter (`global uniform uint ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_UVEC2** = `10`

2-dimensional unsigned integer vector global shader parameter (`global uniform uvec2 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_UVEC3** = `11`

3-dimensional unsigned integer vector global shader parameter (`global uniform uvec3 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_UVEC4** = `12`

4-dimensional unsigned integer vector global shader parameter (`global uniform uvec4 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_FLOAT** = `13`

Single-precision floating-point global shader parameter (`global uniform float ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_VEC2** = `14`

2-dimensional floating-point vector global shader parameter (`global uniform vec2 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_VEC3** = `15`

3-dimensional floating-point vector global shader parameter (`global uniform vec3 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_VEC4** = `16`

4-dimensional floating-point vector global shader parameter (`global uniform vec4 ...`).

GlobalShaderParameterType **GLOBAL_VAR_TYPE_COLOR** = `17`

Color global shader parameter (`global uniform vec4 ...`). Equivalent to GLOBAL_VAR_TYPE_VEC4 in shader code, but exposed as a [Color](class_color.md#class-color) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_RECT2** = `18`

2-dimensional floating-point rectangle global shader parameter (`global uniform vec4 ...`). Equivalent to GLOBAL_VAR_TYPE_VEC4 in shader code, but exposed as a [Rect2](class_rect2.md#class-rect2) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_MAT2** = `19`

2×2 matrix global shader parameter (`global uniform mat2 ...`). Exposed as a [PackedInt32Array](class_packedint32array.md#class-packedint32array) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_MAT3** = `20`

3×3 matrix global shader parameter (`global uniform mat3 ...`). Exposed as a [Basis](class_basis.md#class-basis) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_MAT4** = `21`

4×4 matrix global shader parameter (`global uniform mat4 ...`). Exposed as a [Projection](class_projection.md#class-projection) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_TRANSFORM_2D** = `22`

2-dimensional transform global shader parameter (`global uniform mat2x3 ...`). Exposed as a [Transform2D](class_transform2d.md#class-transform2d) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_TRANSFORM** = `23`

3-dimensional transform global shader parameter (`global uniform mat3x4 ...`). Exposed as a [Transform3D](class_transform3d.md#class-transform3d) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_SAMPLER2D** = `24`

2D sampler global shader parameter (`global uniform sampler2D ...`). Exposed as a [Texture2D](class_texture2d.md#class-texture2d) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_SAMPLER2DARRAY** = `25`

2D sampler array global shader parameter (`global uniform sampler2DArray ...`). Exposed as a [Texture2DArray](class_texture2darray.md#class-texture2darray) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_SAMPLER3D** = `26`

3D sampler global shader parameter (`global uniform sampler3D ...`). Exposed as a [Texture3D](class_texture3d.md#class-texture3d) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_SAMPLERCUBE** = `27`

Cubemap sampler global shader parameter (`global uniform samplerCube ...`). Exposed as a [Cubemap](class_cubemap.md#class-cubemap) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_SAMPLEREXT** = `28`

External sampler global shader parameter (`global uniform samplerExternalOES ...`). Exposed as an [ExternalTexture](class_externaltexture.md#class-externaltexture) in the editor UI.

GlobalShaderParameterType **GLOBAL_VAR_TYPE_MAX** = `29`

Represents the size of the GlobalShaderParameterType enum.

---

enum **RenderingInfo**:

RenderingInfo **RENDERING_INFO_TOTAL_OBJECTS_IN_FRAME** = `0`

Number of objects rendered in the current 3D scene. This varies depending on camera position and rotation.

RenderingInfo **RENDERING_INFO_TOTAL_PRIMITIVES_IN_FRAME** = `1`

Number of points, lines, or triangles rendered in the current 3D scene. This varies depending on camera position and rotation.

RenderingInfo **RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME** = `2`

Number of draw calls performed to render in the current 3D scene. This varies depending on camera position and rotation.

RenderingInfo **RENDERING_INFO_TEXTURE_MEM_USED** = `3`

Texture memory used (in bytes).

RenderingInfo **RENDERING_INFO_BUFFER_MEM_USED** = `4`

Buffer memory used (in bytes). This includes vertex data, uniform buffers, and many miscellaneous buffer types used internally.

RenderingInfo **RENDERING_INFO_VIDEO_MEM_USED** = `5`

Video memory used (in bytes). When using the Forward+ or Mobile renderers, this is always greater than the sum of RENDERING_INFO_TEXTURE_MEM_USED and RENDERING_INFO_BUFFER_MEM_USED, since there is miscellaneous data not accounted for by those two metrics. When using the Compatibility renderer, this is equal to the sum of RENDERING_INFO_TEXTURE_MEM_USED and RENDERING_INFO_BUFFER_MEM_USED.

RenderingInfo **RENDERING_INFO_PIPELINE_COMPILATIONS_CANVAS** = `6`

Number of pipeline compilations that were triggered by the 2D canvas renderer.

RenderingInfo **RENDERING_INFO_PIPELINE_COMPILATIONS_MESH** = `7`

Number of pipeline compilations that were triggered by loading meshes. These compilations will show up as longer loading times the first time a user runs the game and the pipeline is required.

RenderingInfo **RENDERING_INFO_PIPELINE_COMPILATIONS_SURFACE** = `8`

Number of pipeline compilations that were triggered by building the surface cache before rendering the scene. These compilations will show up as a stutter when loading a scene the first time a user runs the game and the pipeline is required.

RenderingInfo **RENDERING_INFO_PIPELINE_COMPILATIONS_DRAW** = `9`

Number of pipeline compilations that were triggered while drawing the scene. These compilations will show up as stutters during gameplay the first time a user runs the game and the pipeline is required.

RenderingInfo **RENDERING_INFO_PIPELINE_COMPILATIONS_SPECIALIZATION** = `10`

Number of pipeline compilations that were triggered to optimize the current scene. These compilations are done in the background and should not cause any stutters whatsoever.

---

enum **PipelineSource**:

PipelineSource **PIPELINE_SOURCE_CANVAS** = `0`

Pipeline compilation that was triggered by the 2D canvas renderer.

PipelineSource **PIPELINE_SOURCE_MESH** = `1`

Pipeline compilation that was triggered by loading a mesh.

PipelineSource **PIPELINE_SOURCE_SURFACE** = `2`

Pipeline compilation that was triggered by building the surface cache before rendering the scene.

PipelineSource **PIPELINE_SOURCE_DRAW** = `3`

Pipeline compilation that was triggered while drawing the scene.

PipelineSource **PIPELINE_SOURCE_SPECIALIZATION** = `4`

Pipeline compilation that was triggered to optimize the current scene.

PipelineSource **PIPELINE_SOURCE_MAX** = `5`

Represents the size of the PipelineSource enum.

---

enum **SplashStretchMode**:

SplashStretchMode **SPLASH_STRETCH_MODE_DISABLED** = `0`

No stretching is applied.

SplashStretchMode **SPLASH_STRETCH_MODE_KEEP** = `1`

Stretches image to fullscreen while preserving aspect ratio.

SplashStretchMode **SPLASH_STRETCH_MODE_KEEP_WIDTH** = `2`

Stretches the height of the image based on the width of the screen.

SplashStretchMode **SPLASH_STRETCH_MODE_KEEP_HEIGHT** = `3`

Stretches the width of the image based on the height of the screen.

SplashStretchMode **SPLASH_STRETCH_MODE_COVER** = `4`

Stretches the image to cover the entire screen while preserving aspect ratio.

SplashStretchMode **SPLASH_STRETCH_MODE_IGNORE** = `5`

Stretches the image to cover the entire screen but doesn't preserve aspect ratio.

---

enum **Features**:

Features **FEATURE_SHADERS** = `0`

**Deprecated:** This constant has not been used since Godot 3.0.

Features **FEATURE_MULTITHREADED** = `1`

**Deprecated:** This constant has not been used since Godot 3.0.

---

## Constants

**NO_INDEX_ARRAY** = `-1`

Marks an error that shows that the index array is empty.

**ARRAY_WEIGHTS_SIZE** = `4`

Number of weights/bones per vertex.

**CANVAS_ITEM_Z_MIN** = `-4096`

The minimum Z-layer for canvas items.

**CANVAS_ITEM_Z_MAX** = `4096`

The maximum Z-layer for canvas items.

**CANVAS_LAYER_MIN** = `-2147483648`

The minimum canvas layer.

**CANVAS_LAYER_MAX** = `2147483647`

The maximum canvas layer.

**MAX_GLOW_LEVELS** = `7`

The maximum number of glow levels that can be used with the glow post-processing effect.

**MAX_CURSORS** = `8`

**Deprecated:** This constant is not used by the engine.

**MAX_2D_DIRECTIONAL_LIGHTS** = `8`

The maximum number of directional lights that can be rendered at a given time in 2D.

**MAX_MESH_SURFACES** = `256`

The maximum number of surfaces a mesh can have.

**MATERIAL_RENDER_PRIORITY_MIN** = `-128`

The minimum renderpriority of all materials.

**MATERIAL_RENDER_PRIORITY_MAX** = `127`

The maximum renderpriority of all materials.

**ARRAY_CUSTOM_COUNT** = `4`

The number of custom data arrays available (ARRAY_CUSTOM0, ARRAY_CUSTOM1, ARRAY_CUSTOM2, ARRAY_CUSTOM3).

**PARTICLES_EMIT_FLAG_POSITION** = `1`

Particle starts at the specified position.

**PARTICLES_EMIT_FLAG_ROTATION_SCALE** = `2`

Particle starts with specified rotation and scale.

**PARTICLES_EMIT_FLAG_VELOCITY** = `4`

Particle starts with the specified velocity vector, which defines the emission direction and speed.

**PARTICLES_EMIT_FLAG_COLOR** = `8`

Particle starts with specified color.

**PARTICLES_EMIT_FLAG_CUSTOM** = `16`

Particle starts with specified `CUSTOM` data.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **render_loop_enabled**

-  **set_render_loop_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_render_loop_enabled**()

If `false`, disables rendering completely, but the engine logic is still being processed. You can call force_draw() to draw a frame even with rendering disabled.

---

## Method Descriptions

[RID](class_rid.md#class-rid) **area_light_create**()

Creates a new area light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this area light to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent node is [AreaLight3D](class_arealight3d.md#class-arealight3d).

---

[Array](class_array.md#class-array)[[Image](class_image.md#class-image)] **bake_render_uv2**(base: [RID](class_rid.md#class-rid), material_overrides: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], image_size: [Vector2i](class_vector2i.md#class-vector2i))

Bakes the material data of the Mesh passed in the `base` parameter with optional `material_overrides` to a set of [Image](class_image.md#class-image)s of size `image_size`. Returns an array of [Image](class_image.md#class-image)s containing material properties as specified in BakeChannels.

---

 **call_on_render_thread**(callable: [Callable](class_callable.md#class-callable))

As the RenderingServer actual logic may run on a separate thread, accessing its internals from the main (or any other) thread will result in errors. To make it easier to run code that can safely access the rendering internals (such as [RenderingDevice](class_renderingdevice.md#class-renderingdevice) and similar RD classes), push a callable via this function so it will be executed on the render thread.

---

[RID](class_rid.md#class-rid) **camera_attributes_create**()

Creates a camera attributes object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `camera_attributes_` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [CameraAttributes](class_cameraattributes.md#class-cameraattributes).

---

 **camera_attributes_set_auto_exposure**(camera_attributes: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), min_sensitivity: [float](class_float.md#class-float), max_sensitivity: [float](class_float.md#class-float), speed: [float](class_float.md#class-float), scale: [float](class_float.md#class-float))

Sets the parameters to use with the auto-exposure effect. These parameters take on the same meaning as their counterparts in [CameraAttributes](class_cameraattributes.md#class-cameraattributes) and [CameraAttributesPractical](class_cameraattributespractical.md#class-cameraattributespractical).

---

 **camera_attributes_set_dof_blur**(camera_attributes: [RID](class_rid.md#class-rid), far_enable: [bool](class_bool.md#class-bool), far_distance: [float](class_float.md#class-float), far_transition: [float](class_float.md#class-float), near_enable: [bool](class_bool.md#class-bool), near_distance: [float](class_float.md#class-float), near_transition: [float](class_float.md#class-float), amount: [float](class_float.md#class-float))

Sets the parameters to use with the DOF blur effect. These parameters take on the same meaning as their counterparts in [CameraAttributesPractical](class_cameraattributespractical.md#class-cameraattributespractical).

---

 **camera_attributes_set_dof_blur_bokeh_shape**(shape: DOFBokehShape)

Sets the shape of the DOF bokeh pattern to `shape`. Different shapes may be used to achieve artistic effect, or to meet performance targets.

---

 **camera_attributes_set_dof_blur_quality**(quality: DOFBlurQuality, use_jitter: [bool](class_bool.md#class-bool))

Sets the quality level of the DOF blur effect to `quality`. `use_jitter` can be used to jitter samples taken during the blur pass to hide artifacts at the cost of looking more fuzzy.

---

 **camera_attributes_set_exposure**(camera_attributes: [RID](class_rid.md#class-rid), multiplier: [float](class_float.md#class-float), normalization: [float](class_float.md#class-float))

Sets the exposure values that will be used by the renderers. The normalization amount is used to bake a given Exposure Value (EV) into rendering calculations to reduce the dynamic range of the scene.

The normalization factor can be calculated from exposure value (EV100) as follows:

```gdscript
func get_exposure_normalization(ev100: float):
    return 1.0 / (pow(2.0, ev100) * 1.2)
```

The exposure value can be calculated from aperture (in f-stops), shutter speed (in seconds), and sensitivity (in ISO) as follows:

```gdscript
func get_exposure(aperture: float, shutter_speed: float, sensitivity: float):
    return log((aperture * aperture) / shutter_speed * (100.0 / sensitivity)) / log(2)
```

---

[RID](class_rid.md#class-rid) **camera_create**()

Creates a 3D camera and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `camera_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent node is [Camera3D](class_camera3d.md#class-camera3d).

---

 **camera_set_camera_attributes**(camera: [RID](class_rid.md#class-rid), effects: [RID](class_rid.md#class-rid))

Sets the camera_attributes created with camera_attributes_create() to the given camera.

---

 **camera_set_compositor**(camera: [RID](class_rid.md#class-rid), compositor: [RID](class_rid.md#class-rid))

Sets the compositor used by this camera. Equivalent to [Camera3D.compositor](class_camera3d.md#class-camera3d-property-compositor).

---

 **camera_set_cull_mask**(camera: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))

Sets the cull mask associated with this camera. The cull mask describes which 3D layers are rendered by this camera. Equivalent to [Camera3D.cull_mask](class_camera3d.md#class-camera3d-property-cull-mask).

---

 **camera_set_environment**(camera: [RID](class_rid.md#class-rid), env: [RID](class_rid.md#class-rid))

Sets the environment used by this camera. Equivalent to [Camera3D.environment](class_camera3d.md#class-camera3d-property-environment).

---

 **camera_set_frustum**(camera: [RID](class_rid.md#class-rid), size: [float](class_float.md#class-float), offset: [Vector2](class_vector2.md#class-vector2), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Sets camera to use frustum projection. This mode allows adjusting the `offset` argument to create "tilted frustum" effects.

---

 **camera_set_orthogonal**(camera: [RID](class_rid.md#class-rid), size: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Sets camera to use orthogonal projection, also known as orthographic projection. Objects remain the same size on the screen no matter how far away they are.

---

 **camera_set_perspective**(camera: [RID](class_rid.md#class-rid), fovy_degrees: [float](class_float.md#class-float), z_near: [float](class_float.md#class-float), z_far: [float](class_float.md#class-float))

Sets camera to use perspective projection. Objects on the screen becomes smaller when they are far away.

---

 **camera_set_transform**(camera: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))

Sets [Transform3D](class_transform3d.md#class-transform3d) of camera.

---

 **camera_set_use_vertical_aspect**(camera: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, preserves the horizontal aspect ratio which is equivalent to [Camera3D.KEEP_WIDTH](class_camera3d.md#class-camera3d-constant-keep-width). If `false`, preserves the vertical aspect ratio which is equivalent to [Camera3D.KEEP_HEIGHT](class_camera3d.md#class-camera3d-constant-keep-height).

---

[RID](class_rid.md#class-rid) **canvas_create**()

Creates a canvas and returns the assigned [RID](class_rid.md#class-rid). It can be accessed with the RID that is returned. This RID will be used in all `canvas_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

Canvas has no [Resource](class_resource.md#class-resource) or [Node](class_node.md#class-node) equivalent.

---

 **canvas_item_add_animation_slice**(item: [RID](class_rid.md#class-rid), animation_length: [float](class_float.md#class-float), slice_begin: [float](class_float.md#class-float), slice_end: [float](class_float.md#class-float), offset: [float](class_float.md#class-float) = 0.0)

Subsequent drawing commands will be ignored unless they fall within the specified animation slice. This is a faster way to implement animations that loop on background rather than redrawing constantly.

---

 **canvas_item_add_circle**(item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), radius: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), antialiased: [bool](class_bool.md#class-bool) = false)

Draws a circle on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_circle()](class_canvasitem.md#class-canvasitem-method-draw-circle).

---

 **canvas_item_add_clip_ignore**(item: [RID](class_rid.md#class-rid), ignore: [bool](class_bool.md#class-bool))

If `ignore` is `true`, ignore clipping on items drawn with this canvas item until this is called again with `ignore` set to `false`.

---

 **canvas_item_add_ellipse**(item: [RID](class_rid.md#class-rid), pos: [Vector2](class_vector2.md#class-vector2), major: [float](class_float.md#class-float), minor: [float](class_float.md#class-float), color: [Color](class_color.md#class-color), antialiased: [bool](class_bool.md#class-bool) = false)

Draws an ellipse with semi-major axis `major` and semi-minor axis `minor` on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_ellipse()](class_canvasitem.md#class-canvasitem-method-draw-ellipse).

---

 **canvas_item_add_lcd_texture_rect_region**(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color))

See also [CanvasItem.draw_lcd_texture_rect_region()](class_canvasitem.md#class-canvasitem-method-draw-lcd-texture-rect-region).

---

 **canvas_item_add_line**(item: [RID](class_rid.md#class-rid), from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2), color: [Color](class_color.md#class-color), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false)

Draws a line on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_line()](class_canvasitem.md#class-canvasitem-method-draw-line).

---

 **canvas_item_add_mesh**(item: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d) = Transform2D(1, 0, 0, 1, 0, 0), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), texture: [RID](class_rid.md#class-rid) = RID())

Draws a mesh created with mesh_create() with given `transform`, `modulate` color, and `texture`. This is used internally by [MeshInstance2D](class_meshinstance2d.md#class-meshinstance2d).

---

 **canvas_item_add_msdf_texture_rect_region**(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), outline_size: [int](class_int.md#class-int) = 0, px_range: [float](class_float.md#class-float) = 1.0, scale: [float](class_float.md#class-float) = 1.0)

See also [CanvasItem.draw_msdf_texture_rect_region()](class_canvasitem.md#class-canvasitem-method-draw-msdf-texture-rect-region).

---

 **canvas_item_add_multiline**(item: [RID](class_rid.md#class-rid), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false)

Draws a 2D multiline on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_multiline()](class_canvasitem.md#class-canvasitem-method-draw-multiline) and [CanvasItem.draw_multiline_colors()](class_canvasitem.md#class-canvasitem-method-draw-multiline-colors).

---

 **canvas_item_add_multimesh**(item: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid) = RID())

Draws a 2D [MultiMesh](class_multimesh.md#class-multimesh) on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_multimesh()](class_canvasitem.md#class-canvasitem-method-draw-multimesh).

---

 **canvas_item_add_nine_patch**(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), source: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), topleft: [Vector2](class_vector2.md#class-vector2), bottomright: [Vector2](class_vector2.md#class-vector2), x_axis_mode: NinePatchAxisMode = 0, y_axis_mode: NinePatchAxisMode = 0, draw_center: [bool](class_bool.md#class-bool) = true, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1))

Draws a nine-patch rectangle on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid).

---

 **canvas_item_add_particles**(item: [RID](class_rid.md#class-rid), particles: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))

Draws particles on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid).

---

 **canvas_item_add_polygon**(item: [RID](class_rid.md#class-rid), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) = PackedVector2Array(), texture: [RID](class_rid.md#class-rid) = RID())

Draws a 2D polygon on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). If you need more flexibility (such as being able to use bones), use canvas_item_add_triangle_array() instead. See also [CanvasItem.draw_polygon()](class_canvasitem.md#class-canvasitem-method-draw-polygon).

**Note:** If you frequently redraw the same polygon with a large number of vertices, consider pre-calculating the triangulation with [Geometry2D.triangulate_polygon()](class_geometry2d.md#class-geometry2d-method-triangulate-polygon) and using [CanvasItem.draw_mesh()](class_canvasitem.md#class-canvasitem-method-draw-mesh), [CanvasItem.draw_multimesh()](class_canvasitem.md#class-canvasitem-method-draw-multimesh), or canvas_item_add_triangle_array().

---

 **canvas_item_add_polyline**(item: [RID](class_rid.md#class-rid), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), width: [float](class_float.md#class-float) = -1.0, antialiased: [bool](class_bool.md#class-bool) = false)

Draws a 2D polyline on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_polyline()](class_canvasitem.md#class-canvasitem-method-draw-polyline) and [CanvasItem.draw_polyline_colors()](class_canvasitem.md#class-canvasitem-method-draw-polyline-colors).

---

 **canvas_item_add_primitive**(item: [RID](class_rid.md#class-rid), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), texture: [RID](class_rid.md#class-rid))

Draws a 2D primitive on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_primitive()](class_canvasitem.md#class-canvasitem-method-draw-primitive).

---

 **canvas_item_add_rect**(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), color: [Color](class_color.md#class-color), antialiased: [bool](class_bool.md#class-bool) = false)

Draws a rectangle on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_rect()](class_canvasitem.md#class-canvasitem-method-draw-rect).

---

 **canvas_item_add_set_transform**(item: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets a [Transform2D](class_transform2d.md#class-transform2d) that will be used to transform subsequent canvas item commands.

---

 **canvas_item_add_texture_rect**(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), tile: [bool](class_bool.md#class-bool) = false, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false)

Draws a 2D textured rectangle on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_texture_rect()](class_canvasitem.md#class-canvasitem-method-draw-texture-rect) and [Texture2D.draw_rect()](class_texture2d.md#class-texture2d-method-draw-rect).

---

 **canvas_item_add_texture_rect_region**(item: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2), texture: [RID](class_rid.md#class-rid), src_rect: [Rect2](class_rect2.md#class-rect2), modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class-bool) = false, clip_uv: [bool](class_bool.md#class-bool) = true)

Draws the specified region of a 2D textured rectangle on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). See also [CanvasItem.draw_texture_rect_region()](class_canvasitem.md#class-canvasitem-method-draw-texture-rect-region) and [Texture2D.draw_rect_region()](class_texture2d.md#class-texture2d-method-draw-rect-region).

---

 **canvas_item_add_triangle_array**(item: [RID](class_rid.md#class-rid), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array), points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), colors: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), uvs: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) = PackedVector2Array(), bones: [PackedInt32Array](class_packedint32array.md#class-packedint32array) = PackedInt32Array(), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) = PackedFloat32Array(), texture: [RID](class_rid.md#class-rid) = RID(), count: [int](class_int.md#class-int) = -1)

Draws a triangle array on the [CanvasItem](class_canvasitem.md#class-canvasitem) pointed to by the `item` [RID](class_rid.md#class-rid). This is internally used by [Line2D](class_line2d.md#class-line2d) and [StyleBoxFlat](class_styleboxflat.md#class-styleboxflat) for rendering. canvas_item_add_triangle_array() is highly flexible, but more complex to use than canvas_item_add_polygon().

**Note:** If `count` is set to a non-negative value, only the first `count * 3` indices (corresponding to `count` triangles) will be drawn. Otherwise, all indices are drawn.

---

 **canvas_item_attach_skeleton**(item: [RID](class_rid.md#class-rid), skeleton: [RID](class_rid.md#class-rid))

Attaches a skeleton to the [CanvasItem](class_canvasitem.md#class-canvasitem). Removes the previous skeleton.

---

 **canvas_item_clear**(item: [RID](class_rid.md#class-rid))

Clears the [CanvasItem](class_canvasitem.md#class-canvasitem) and removes all commands in it.

---

[RID](class_rid.md#class-rid) **canvas_item_create**()

Creates a new CanvasItem instance and returns its [RID](class_rid.md#class-rid). It can be accessed with the RID that is returned. This RID will be used in all `canvas_item_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent node is [CanvasItem](class_canvasitem.md#class-canvasitem).

---

[Variant](class_variant.md#class-variant) **canvas_item_get_instance_shader_parameter**(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))

Returns the value of the per-instance shader uniform from the specified canvas item instance. Equivalent to [CanvasItem.get_instance_shader_parameter()](class_canvasitem.md#class-canvasitem-method-get-instance-shader-parameter).

---

[Variant](class_variant.md#class-variant) **canvas_item_get_instance_shader_parameter_default_value**(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))

Returns the default value of the per-instance shader uniform from the specified canvas item instance. Equivalent to [CanvasItem.get_instance_shader_parameter()](class_canvasitem.md#class-canvasitem-method-get-instance-shader-parameter).

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **canvas_item_get_instance_shader_parameter_list**(instance: [RID](class_rid.md#class-rid))

Returns a dictionary of per-instance shader uniform names of the per-instance shader uniform from the specified canvas item instance.

The returned dictionary is in PropertyInfo format, with the keys `name`, `class_name`, `type`, `hint`, `hint_string`, and `usage`.

---

 **canvas_item_reset_physics_interpolation**(item: [RID](class_rid.md#class-rid))

Prevents physics interpolation for the current physics tick.

This is useful when moving a canvas item to a new location, to give an instantaneous change rather than interpolation from the previous location.

---

 **canvas_item_set_canvas_group_mode**(item: [RID](class_rid.md#class-rid), mode: CanvasGroupMode, clear_margin: [float](class_float.md#class-float) = 5.0, fit_empty: [bool](class_bool.md#class-bool) = false, fit_margin: [float](class_float.md#class-float) = 0.0, blur_mipmaps: [bool](class_bool.md#class-bool) = false)

Sets the canvas group mode used during 2D rendering for the canvas item specified by the `item` RID. For faster but more limited clipping, use canvas_item_set_clip() instead.

**Note:** The equivalent node functionality is found in [CanvasGroup](class_canvasgroup.md#class-canvasgroup) and [CanvasItem.clip_children](class_canvasitem.md#class-canvasitem-property-clip-children).

---

 **canvas_item_set_clip**(item: [RID](class_rid.md#class-rid), clip: [bool](class_bool.md#class-bool))

If `clip` is `true`, makes the canvas item specified by the `item` RID not draw anything outside of its rect's coordinates. This clipping is fast, but works only with axis-aligned rectangles. This means that rotation is ignored by the clipping rectangle. For more advanced clipping shapes, use canvas_item_set_canvas_group_mode() instead.

**Note:** The equivalent node functionality is found in [Label.clip_text](class_label.md#class-label-property-clip-text), [RichTextLabel](class_richtextlabel.md#class-richtextlabel) (always enabled) and more.

---

 **canvas_item_set_copy_to_backbuffer**(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool), rect: [Rect2](class_rect2.md#class-rect2))

Sets the [CanvasItem](class_canvasitem.md#class-canvasitem) to copy a rect to the backbuffer.

---

 **canvas_item_set_custom_rect**(item: [RID](class_rid.md#class-rid), use_custom_rect: [bool](class_bool.md#class-bool), rect: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0))

If `use_custom_rect` is `true`, sets the custom visibility rectangle (used for culling) to `rect` for the canvas item specified by `item`. Setting a custom visibility rect can reduce CPU load when drawing lots of 2D instances. If `use_custom_rect` is `false`, automatically computes a visibility rectangle based on the canvas item's draw commands.

---

 **canvas_item_set_default_texture_filter**(item: [RID](class_rid.md#class-rid), filter: CanvasItemTextureFilter)

Sets the default texture filter mode for the canvas item specified by the `item` RID. Equivalent to [CanvasItem.texture_filter](class_canvasitem.md#class-canvasitem-property-texture-filter).

---

 **canvas_item_set_default_texture_repeat**(item: [RID](class_rid.md#class-rid), repeat: CanvasItemTextureRepeat)

Sets the default texture repeat mode for the canvas item specified by the `item` RID. Equivalent to [CanvasItem.texture_repeat](class_canvasitem.md#class-canvasitem-property-texture-repeat).

---

 **canvas_item_set_distance_field_mode**(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, enables multichannel signed distance field rendering mode for the canvas item specified by the `item` RID. This is meant to be used for font rendering, or with specially generated images using [msdfgen](https://github.com/Chlumsky/msdfgen).

---

 **canvas_item_set_draw_behind_parent**(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, draws the canvas item specified by the `item` RID behind its parent. Equivalent to [CanvasItem.show_behind_parent](class_canvasitem.md#class-canvasitem-property-show-behind-parent).

---

 **canvas_item_set_draw_index**(item: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Sets the index for the [CanvasItem](class_canvasitem.md#class-canvasitem).

---

 **canvas_item_set_instance_shader_parameter**(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Sets the per-instance shader uniform on the specified canvas item instance. Equivalent to [CanvasItem.set_instance_shader_parameter()](class_canvasitem.md#class-canvasitem-method-set-instance-shader-parameter).

---

 **canvas_item_set_interpolated**(item: [RID](class_rid.md#class-rid), interpolated: [bool](class_bool.md#class-bool))

If `interpolated` is `true`, turns on physics interpolation for the canvas item.

---

 **canvas_item_set_light_mask**(item: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Sets the light `mask` for the canvas item specified by the `item` RID. Equivalent to [CanvasItem.light_mask](class_canvasitem.md#class-canvasitem-property-light-mask).

---

 **canvas_item_set_material**(item: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))

Sets a new `material` to the canvas item specified by the `item` RID. Equivalent to [CanvasItem.material](class_canvasitem.md#class-canvasitem-property-material).

---

 **canvas_item_set_modulate**(item: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Multiplies the color of the canvas item specified by the `item` RID, while affecting its children. See also canvas_item_set_self_modulate(). Equivalent to [CanvasItem.modulate](class_canvasitem.md#class-canvasitem-property-modulate).

---

 **canvas_item_set_parent**(item: [RID](class_rid.md#class-rid), parent: [RID](class_rid.md#class-rid))

Sets a parent [CanvasItem](class_canvasitem.md#class-canvasitem) to the [CanvasItem](class_canvasitem.md#class-canvasitem). The item will inherit transform, modulation and visibility from its parent, like [CanvasItem](class_canvasitem.md#class-canvasitem) nodes in the scene tree.

---

 **canvas_item_set_self_modulate**(item: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Multiplies the color of the canvas item specified by the `item` RID, without affecting its children. See also canvas_item_set_modulate(). Equivalent to [CanvasItem.self_modulate](class_canvasitem.md#class-canvasitem-property-self-modulate).

---

 **canvas_item_set_sort_children_by_y**(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `enabled` is `true`, child nodes with the lowest Y position are drawn before those with a higher Y position. Y-sorting only affects children that inherit from the canvas item specified by the `item` RID, not the canvas item itself. Equivalent to [CanvasItem.y_sort_enabled](class_canvasitem.md#class-canvasitem-property-y-sort-enabled).

---

 **canvas_item_set_transform**(item: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the `transform` of the canvas item specified by the `item` RID. This affects where and how the item will be drawn. Child canvas items' transforms are multiplied by their parent's transform. Equivalent to [Node2D.transform](class_node2d.md#class-node2d-property-transform).

---

 **canvas_item_set_use_parent_material**(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

Sets if the [CanvasItem](class_canvasitem.md#class-canvasitem) uses its parent's material.

---

 **canvas_item_set_visibility_layer**(item: [RID](class_rid.md#class-rid), visibility_layer: [int](class_int.md#class-int))

Sets the rendering visibility layer associated with this [CanvasItem](class_canvasitem.md#class-canvasitem). Only [Viewport](class_viewport.md#class-viewport) nodes with a matching rendering mask will render this [CanvasItem](class_canvasitem.md#class-canvasitem).

---

 **canvas_item_set_visibility_notifier**(item: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), area: [Rect2](class_rect2.md#class-rect2), enter_callable: [Callable](class_callable.md#class-callable), exit_callable: [Callable](class_callable.md#class-callable))

Sets the given [CanvasItem](class_canvasitem.md#class-canvasitem) as visibility notifier. `area` defines the area of detecting visibility. `enter_callable` is called when the [CanvasItem](class_canvasitem.md#class-canvasitem) enters the screen, `exit_callable` is called when the [CanvasItem](class_canvasitem.md#class-canvasitem) exits the screen. If `enable` is `false`, the item will no longer function as notifier.

This method can be used to manually mimic [VisibleOnScreenNotifier2D](class_visibleonscreennotifier2d.md#class-visibleonscreennotifier2d).

---

 **canvas_item_set_visible**(item: [RID](class_rid.md#class-rid), visible: [bool](class_bool.md#class-bool))

Sets the visibility of the [CanvasItem](class_canvasitem.md#class-canvasitem).

---

 **canvas_item_set_z_as_relative_to_parent**(item: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If this is enabled, the Z index of the parent will be added to the children's Z index.

---

 **canvas_item_set_z_index**(item: [RID](class_rid.md#class-rid), z_index: [int](class_int.md#class-int))

Sets the [CanvasItem](class_canvasitem.md#class-canvasitem)'s Z index, i.e. its draw order (lower indexes are drawn first).

---

 **canvas_item_transform_physics_interpolation**(item: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Transforms both the current and previous stored transform for a canvas item.

This allows transforming a canvas item without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.

---

 **canvas_light_attach_to_canvas**(light: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid))

Attaches the canvas light to the canvas. Removes it from its previous canvas.

---

[RID](class_rid.md#class-rid) **canvas_light_create**()

Creates a canvas light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `canvas_light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent node is [Light2D](class_light2d.md#class-light2d).

---

 **canvas_light_occluder_attach_to_canvas**(occluder: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid))

Attaches a light occluder to the canvas. Removes it from its previous canvas.

---

[RID](class_rid.md#class-rid) **canvas_light_occluder_create**()

Creates a light occluder and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `canvas_light_occluder_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent node is [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d).

---

 **canvas_light_occluder_reset_physics_interpolation**(occluder: [RID](class_rid.md#class-rid))

Prevents physics interpolation for the current physics tick.

This is useful when moving an occluder to a new location, to give an instantaneous change rather than interpolation from the previous location.

---

 **canvas_light_occluder_set_as_sdf_collision**(occluder: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Enables or disables using the light occluder as a signed distance field for 2D particle collision.

---

 **canvas_light_occluder_set_enabled**(occluder: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

Enables or disables light occluder.

---

 **canvas_light_occluder_set_interpolated**(occluder: [RID](class_rid.md#class-rid), interpolated: [bool](class_bool.md#class-bool))

If `interpolated` is `true`, turns on physics interpolation for the light occluder.

---

 **canvas_light_occluder_set_light_mask**(occluder: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

The light mask. See [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d) for more information on light masks.

---

 **canvas_light_occluder_set_polygon**(occluder: [RID](class_rid.md#class-rid), polygon: [RID](class_rid.md#class-rid))

Sets a light occluder's polygon.

---

 **canvas_light_occluder_set_transform**(occluder: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets a light occluder's [Transform2D](class_transform2d.md#class-transform2d).

---

 **canvas_light_occluder_transform_physics_interpolation**(occluder: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Transforms both the current and previous stored transform for a light occluder.

This allows transforming an occluder without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.

---

 **canvas_light_reset_physics_interpolation**(light: [RID](class_rid.md#class-rid))

Prevents physics interpolation for the current physics tick.

This is useful when moving a canvas item to a new location, to give an instantaneous change rather than interpolation from the previous location.

---

 **canvas_light_set_blend_mode**(light: [RID](class_rid.md#class-rid), mode: CanvasLightBlendMode)

Sets the blend mode for the given canvas light to `mode`. Equivalent to [Light2D.blend_mode](class_light2d.md#class-light2d-property-blend-mode).

---

 **canvas_light_set_color**(light: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Sets the color for a light.

---

 **canvas_light_set_enabled**(light: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

Enables or disables a canvas light.

---

 **canvas_light_set_energy**(light: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float))

Sets a canvas light's energy.

---

 **canvas_light_set_height**(light: [RID](class_rid.md#class-rid), height: [float](class_float.md#class-float))

Sets a canvas light's height.

---

 **canvas_light_set_interpolated**(light: [RID](class_rid.md#class-rid), interpolated: [bool](class_bool.md#class-bool))

If `interpolated` is `true`, turns on physics interpolation for the canvas light.

---

 **canvas_light_set_item_cull_mask**(light: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

The light mask. See [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d) for more information on light masks.

---

 **canvas_light_set_item_shadow_cull_mask**(light: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

The binary mask used to determine which layers this canvas light's shadows affects. See [LightOccluder2D](class_lightoccluder2d.md#class-lightoccluder2d) for more information on light masks.

---

 **canvas_light_set_layer_range**(light: [RID](class_rid.md#class-rid), min_layer: [int](class_int.md#class-int), max_layer: [int](class_int.md#class-int))

The layer range that gets rendered with this light.

---

 **canvas_light_set_mode**(light: [RID](class_rid.md#class-rid), mode: CanvasLightMode)

Sets the mode of the canvas light.

---

 **canvas_light_set_shadow_color**(light: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Sets the color of the canvas light's shadow.

---

 **canvas_light_set_shadow_enabled**(light: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

Enables or disables the canvas light's shadow.

---

 **canvas_light_set_shadow_filter**(light: [RID](class_rid.md#class-rid), filter: CanvasLightShadowFilter)

Sets the canvas light's shadow's filter.

---

 **canvas_light_set_shadow_smooth**(light: [RID](class_rid.md#class-rid), smooth: [float](class_float.md#class-float))

Smoothens the shadow. The lower, the smoother.

---

 **canvas_light_set_texture**(light: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))

Sets the texture to be used by a [PointLight2D](class_pointlight2d.md#class-pointlight2d). Equivalent to [PointLight2D.texture](class_pointlight2d.md#class-pointlight2d-property-texture).

---

 **canvas_light_set_texture_offset**(light: [RID](class_rid.md#class-rid), offset: [Vector2](class_vector2.md#class-vector2))

Sets the offset of a [PointLight2D](class_pointlight2d.md#class-pointlight2d)'s texture. Equivalent to [PointLight2D.offset](class_pointlight2d.md#class-pointlight2d-property-offset).

---

 **canvas_light_set_texture_scale**(light: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))

Sets the scale factor of a [PointLight2D](class_pointlight2d.md#class-pointlight2d)'s texture. Equivalent to [PointLight2D.texture_scale](class_pointlight2d.md#class-pointlight2d-property-texture-scale).

---

 **canvas_light_set_transform**(light: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the canvas light's [Transform2D](class_transform2d.md#class-transform2d).

---

 **canvas_light_set_z_range**(light: [RID](class_rid.md#class-rid), min_z: [int](class_int.md#class-int), max_z: [int](class_int.md#class-int))

Sets the Z range of objects that will be affected by this light. Equivalent to [Light2D.range_z_min](class_light2d.md#class-light2d-property-range-z-min) and [Light2D.range_z_max](class_light2d.md#class-light2d-property-range-z-max).

---

 **canvas_light_transform_physics_interpolation**(light: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Transforms both the current and previous stored transform for a canvas light.

This allows transforming a light without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.

---

[RID](class_rid.md#class-rid) **canvas_occluder_polygon_create**()

Creates a new light occluder polygon and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `canvas_occluder_polygon_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [OccluderPolygon2D](class_occluderpolygon2d.md#class-occluderpolygon2d).

---

 **canvas_occluder_polygon_set_cull_mode**(occluder_polygon: [RID](class_rid.md#class-rid), mode: CanvasOccluderPolygonCullMode)

Sets an occluder polygon's cull mode.

---

 **canvas_occluder_polygon_set_shape**(occluder_polygon: [RID](class_rid.md#class-rid), shape: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), closed: [bool](class_bool.md#class-bool))

Sets the shape of the occluder polygon.

---

 **canvas_set_disable_scale**(disable: [bool](class_bool.md#class-bool))

If `disable` is `true`, makes 2D rendering ignore the canvas scale defined for each canvas layer. This affects [CanvasLayer](class_canvaslayer.md#class-canvaslayer)s with the [CanvasLayer.follow_viewport_enabled](class_canvaslayer.md#class-canvaslayer-property-follow-viewport-enabled) property set to `true`.

In the editor, this is set to `true` by default, and set to `false` when **View > Preview Canvas Scale** is enabled at the top of the 2D editor viewport.

**Note:** Setting this to `true` does not impact the behavior of [CanvasLayer.scale](class_canvaslayer.md#class-canvaslayer-property-scale), [Node2D.scale](class_node2d.md#class-node2d-property-scale), or [Control.scale](class_control.md#class-control-property-scale).

---

 **canvas_set_item_mirroring**(canvas: [RID](class_rid.md#class-rid), item: [RID](class_rid.md#class-rid), mirroring: [Vector2](class_vector2.md#class-vector2))

A copy of the canvas item will be drawn with a local offset of the `mirroring`.

**Note:** This is equivalent to calling canvas_set_item_repeat() like `canvas_set_item_repeat(item, mirroring, 1)`, with an additional check ensuring `canvas` is a parent of `item`.

---

 **canvas_set_item_repeat**(item: [RID](class_rid.md#class-rid), repeat_size: [Vector2](class_vector2.md#class-vector2), repeat_times: [int](class_int.md#class-int))

A copy of the canvas item will be drawn with a local offset of the `repeat_size` by the number of times of the `repeat_times`. As the `repeat_times` increases, the copies will spread away from the origin texture.

---

 **canvas_set_modulate**(canvas: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Modulates all colors in the given canvas.

---

 **canvas_set_shadow_texture_size**(size: [int](class_int.md#class-int))

Sets the [ProjectSettings.rendering/2d/shadow_atlas/size](class_projectsettings.md#class-projectsettings-property-rendering-2d-shadow-atlas-size) to use for [Light2D](class_light2d.md#class-light2d) shadow rendering (in pixels). The value is rounded up to the nearest power of 2.

---

[RID](class_rid.md#class-rid) **canvas_texture_create**()

Creates a canvas texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `canvas_texture_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method. See also texture_2d_create().

**Note:** The equivalent resource is [CanvasTexture](class_canvastexture.md#class-canvastexture) and is only meant to be used in 2D rendering, not 3D.

---

 **canvas_texture_set_channel**(canvas_texture: [RID](class_rid.md#class-rid), channel: CanvasTextureChannel, texture: [RID](class_rid.md#class-rid))

Sets the `channel`'s `texture` for the canvas texture specified by the `canvas_texture` RID. Equivalent to [CanvasTexture.diffuse_texture](class_canvastexture.md#class-canvastexture-property-diffuse-texture), [CanvasTexture.normal_texture](class_canvastexture.md#class-canvastexture-property-normal-texture) and [CanvasTexture.specular_texture](class_canvastexture.md#class-canvastexture-property-specular-texture).

---

 **canvas_texture_set_shading_parameters**(canvas_texture: [RID](class_rid.md#class-rid), base_color: [Color](class_color.md#class-color), shininess: [float](class_float.md#class-float))

Sets the `base_color` and `shininess` to use for the canvas texture specified by the `canvas_texture` RID. Equivalent to [CanvasTexture.specular_color](class_canvastexture.md#class-canvastexture-property-specular-color) and [CanvasTexture.specular_shininess](class_canvastexture.md#class-canvastexture-property-specular-shininess).

---

 **canvas_texture_set_texture_filter**(canvas_texture: [RID](class_rid.md#class-rid), filter: CanvasItemTextureFilter)

Sets the texture `filter` mode to use for the canvas texture specified by the `canvas_texture` RID.

---

 **canvas_texture_set_texture_repeat**(canvas_texture: [RID](class_rid.md#class-rid), repeat: CanvasItemTextureRepeat)

Sets the texture `repeat` mode to use for the canvas texture specified by the `canvas_texture` RID.

---

[RID](class_rid.md#class-rid) **compositor_create**()

Creates a new compositor and adds it to the RenderingServer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

---

[RID](class_rid.md#class-rid) **compositor_effect_create**()

Creates a new rendering effect and adds it to the RenderingServer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

---

 **compositor_effect_set_callback**(effect: [RID](class_rid.md#class-rid), callback_type: CompositorEffectCallbackType, callback: [Callable](class_callable.md#class-callable))

Sets the callback type (`callback_type`) and callback method(`callback`) for this rendering effect.

---

 **compositor_effect_set_enabled**(effect: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

Enables/disables this rendering effect.

---

 **compositor_effect_set_flag**(effect: [RID](class_rid.md#class-rid), flag: CompositorEffectFlags, set: [bool](class_bool.md#class-bool))

Sets the flag (`flag`) for this rendering effect to `true` or `false` (`set`).

---

 **compositor_set_compositor_effects**(compositor: [RID](class_rid.md#class-rid), effects: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])

Sets the compositor effects for the specified compositor RID. `effects` should be an array containing RIDs created with compositor_effect_create().

---

[RenderingDevice](class_renderingdevice.md#class-renderingdevice) **create_local_rendering_device**()

Creates a RenderingDevice that can be used to do draw and compute operations on a separate thread. Cannot draw to the screen nor share data with the global RenderingDevice.

**Note:** When using the OpenGL rendering driver or when running in headless mode, this function always returns `null`.

---

[Rect2](class_rect2.md#class-rect2) **debug_canvas_item_get_rect**(item: [RID](class_rid.md#class-rid))

Returns the bounding rectangle for a canvas item in local space, as calculated by the renderer. This bound is used internally for culling.

**Warning:** This function is intended for debugging in the editor, and will pass through and return a zero [Rect2](class_rect2.md#class-rect2) in exported projects.

---

[RID](class_rid.md#class-rid) **decal_create**()

Creates a decal and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `decal_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this decal to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent node is [Decal](class_decal.md#class-decal).

---

 **decal_set_albedo_mix**(decal: [RID](class_rid.md#class-rid), albedo_mix: [float](class_float.md#class-float))

Sets the `albedo_mix` in the decal specified by the `decal` RID. Equivalent to [Decal.albedo_mix](class_decal.md#class-decal-property-albedo-mix).

---

 **decal_set_cull_mask**(decal: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Sets the cull `mask` in the decal specified by the `decal` RID. Equivalent to [Decal.cull_mask](class_decal.md#class-decal-property-cull-mask).

---

 **decal_set_distance_fade**(decal: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool), begin: [float](class_float.md#class-float), length: [float](class_float.md#class-float))

Sets the distance fade parameters in the decal specified by the `decal` RID. Equivalent to [Decal.distance_fade_enabled](class_decal.md#class-decal-property-distance-fade-enabled), [Decal.distance_fade_begin](class_decal.md#class-decal-property-distance-fade-begin) and [Decal.distance_fade_length](class_decal.md#class-decal-property-distance-fade-length).

---

 **decal_set_emission_energy**(decal: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float))

Sets the emission `energy` in the decal specified by the `decal` RID. Equivalent to [Decal.emission_energy](class_decal.md#class-decal-property-emission-energy).

---

 **decal_set_fade**(decal: [RID](class_rid.md#class-rid), above: [float](class_float.md#class-float), below: [float](class_float.md#class-float))

Sets the upper fade (`above`) and lower fade (`below`) in the decal specified by the `decal` RID. Equivalent to [Decal.upper_fade](class_decal.md#class-decal-property-upper-fade) and [Decal.lower_fade](class_decal.md#class-decal-property-lower-fade).

---

 **decal_set_modulate**(decal: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Sets the color multiplier in the decal specified by the `decal` RID to `color`. Equivalent to [Decal.modulate](class_decal.md#class-decal-property-modulate).

---

 **decal_set_normal_fade**(decal: [RID](class_rid.md#class-rid), fade: [float](class_float.md#class-float))

Sets the normal `fade` in the decal specified by the `decal` RID. Equivalent to [Decal.normal_fade](class_decal.md#class-decal-property-normal-fade).

---

 **decal_set_size**(decal: [RID](class_rid.md#class-rid), size: [Vector3](class_vector3.md#class-vector3))

Sets the `size` of the decal specified by the `decal` RID. Equivalent to [Decal.size](class_decal.md#class-decal-property-size).

---

 **decal_set_texture**(decal: [RID](class_rid.md#class-rid), type: DecalTexture, texture: [RID](class_rid.md#class-rid))

Sets the `texture` in the given texture `type` slot for the specified decal. Equivalent to [Decal.set_texture()](class_decal.md#class-decal-method-set-texture).

---

 **decals_set_filter**(filter: DecalFilter)

Sets the texture `filter` mode to use when rendering decals. This parameter is global and cannot be set on a per-decal basis.

---

[RID](class_rid.md#class-rid) **directional_light_create**()

Creates a directional light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this directional light to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent node is [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d).

---

 **directional_shadow_atlas_set_size**(size: [int](class_int.md#class-int), is_16bits: [bool](class_bool.md#class-bool))

Sets the `size` of the directional light shadows in 3D. See also [ProjectSettings.rendering/lights_and_shadows/directional_shadow/size](class_projectsettings.md#class-projectsettings-property-rendering-lights-and-shadows-directional-shadow-size). This parameter is global and cannot be set on a per-viewport basis.

---

 **directional_soft_shadow_filter_set_quality**(quality: ShadowQuality)

Sets the filter `quality` for directional light shadows in 3D. See also [ProjectSettings.rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality](class_projectsettings.md#class-projectsettings-property-rendering-lights-and-shadows-directional-shadow-soft-shadow-filter-quality). This parameter is global and cannot be set on a per-viewport basis.

---

[Image](class_image.md#class-image) **environment_bake_panorama**(environment: [RID](class_rid.md#class-rid), bake_irradiance: [bool](class_bool.md#class-bool), size: [Vector2i](class_vector2i.md#class-vector2i))

Generates and returns an [Image](class_image.md#class-image) containing the radiance map for the specified `environment` RID's sky. This supports built-in sky material and custom sky shaders. If `bake_irradiance` is `true`, the irradiance map is saved instead of the radiance map. The radiance map is used to render reflected light, while the irradiance map is used to render ambient light. See also sky_bake_panorama().

**Note:** The image is saved using linear encoding without any tonemapping performed, which means it will look too dark if viewed directly in an image editor.

**Note:** `size` should be a 2:1 aspect ratio for the generated panorama to have square pixels. For radiance maps, there is no point in using a height greater than [Sky.radiance_size](class_sky.md#class-sky-property-radiance-size), as it won't increase detail. Irradiance maps only contain low-frequency data, so there is usually no point in going past a size of 128×64 pixels when saving an irradiance map.

---

[RID](class_rid.md#class-rid) **environment_create**()

Creates an environment and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `environment_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [Environment](class_environment.md#class-environment).

---

 **environment_glow_set_use_bicubic_upscale**(enable: [bool](class_bool.md#class-bool))

If `enable` is `true`, enables bicubic upscaling for glow which improves quality at the cost of performance. Equivalent to [ProjectSettings.rendering/environment/glow/upscale_mode](class_projectsettings.md#class-projectsettings-property-rendering-environment-glow-upscale-mode).

**Note:** This setting is only effective when using the Forward+ or Mobile rendering methods, as Compatibility uses a different glow implementation.

---

 **environment_set_adjustment**(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), brightness: [float](class_float.md#class-float), contrast: [float](class_float.md#class-float), saturation: [float](class_float.md#class-float), use_1d_color_correction: [bool](class_bool.md#class-bool), color_correction: [RID](class_rid.md#class-rid))

Sets the values to be used with the "adjustments" post-process effect. See [Environment](class_environment.md#class-environment) for more details.

---

 **environment_set_ambient_light**(env: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color), ambient: EnvironmentAmbientSource = 0, energy: [float](class_float.md#class-float) = 1.0, sky_contribution: [float](class_float.md#class-float) = 0.0, reflection_source: EnvironmentReflectionSource = 0)

Sets the values to be used for ambient light rendering. See [Environment](class_environment.md#class-environment) for more details.

---

 **environment_set_background**(env: [RID](class_rid.md#class-rid), bg: EnvironmentBG)

Sets the environment's background mode. Equivalent to [Environment.background_mode](class_environment.md#class-environment-property-background-mode).

---

 **environment_set_bg_color**(env: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Color displayed for clear areas of the scene. Only effective if using the ENV_BG_COLOR background mode.

---

 **environment_set_bg_energy**(env: [RID](class_rid.md#class-rid), multiplier: [float](class_float.md#class-float), exposure_value: [float](class_float.md#class-float))

Sets the intensity of the background color.

---

 **environment_set_camera_id**(env: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))

Sets the camera ID to be used as environment background.

---

 **environment_set_canvas_max_layer**(env: [RID](class_rid.md#class-rid), max_layer: [int](class_int.md#class-int))

Sets the maximum layer to use if using Canvas background mode.

---

 **environment_set_fog**(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), light_color: [Color](class_color.md#class-color), light_energy: [float](class_float.md#class-float), sun_scatter: [float](class_float.md#class-float), density: [float](class_float.md#class-float), height: [float](class_float.md#class-float), height_density: [float](class_float.md#class-float), aerial_perspective: [float](class_float.md#class-float), sky_affect: [float](class_float.md#class-float), fog_mode: EnvironmentFogMode = 0)

Configures fog for the specified environment RID. See `fog_*` properties in [Environment](class_environment.md#class-environment) for more information.

---

 **environment_set_fog_depth**(env: [RID](class_rid.md#class-rid), curve: [float](class_float.md#class-float), begin: [float](class_float.md#class-float), end: [float](class_float.md#class-float))

Configures fog depth for the specified environment RID. Only has an effect when the fog mode of the environment is ENV_FOG_MODE_DEPTH. See `fog_depth_*` properties in [Environment](class_environment.md#class-environment) for more information.

---

 **environment_set_glow**(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), levels: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), intensity: [float](class_float.md#class-float), strength: [float](class_float.md#class-float), mix: [float](class_float.md#class-float), bloom_threshold: [float](class_float.md#class-float), blend_mode: EnvironmentGlowBlendMode, hdr_bleed_threshold: [float](class_float.md#class-float), hdr_bleed_scale: [float](class_float.md#class-float), hdr_luminance_cap: [float](class_float.md#class-float), glow_map_strength: [float](class_float.md#class-float), glow_map: [RID](class_rid.md#class-rid))

Configures glow for the specified environment RID. See `glow_*` properties in [Environment](class_environment.md#class-environment) for more information.

---

 **environment_set_sdfgi**(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), cascades: [int](class_int.md#class-int), min_cell_size: [float](class_float.md#class-float), y_scale: EnvironmentSDFGIYScale, use_occlusion: [bool](class_bool.md#class-bool), bounce_feedback: [float](class_float.md#class-float), read_sky: [bool](class_bool.md#class-bool), energy: [float](class_float.md#class-float), normal_bias: [float](class_float.md#class-float), probe_bias: [float](class_float.md#class-float))

Configures signed distance field global illumination for the specified environment RID. See `sdfgi_*` properties in [Environment](class_environment.md#class-environment) for more information.

---

 **environment_set_sdfgi_frames_to_converge**(frames: EnvironmentSDFGIFramesToConverge)

Sets the number of frames to use for converging signed distance field global illumination. Equivalent to [ProjectSettings.rendering/global_illumination/sdfgi/frames_to_converge](class_projectsettings.md#class-projectsettings-property-rendering-global-illumination-sdfgi-frames-to-converge).

---

 **environment_set_sdfgi_frames_to_update_light**(frames: EnvironmentSDFGIFramesToUpdateLight)

Sets the update speed for dynamic lights' indirect lighting when computing signed distance field global illumination. Equivalent to [ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights](class_projectsettings.md#class-projectsettings-property-rendering-global-illumination-sdfgi-frames-to-update-lights).

---

 **environment_set_sdfgi_ray_count**(ray_count: EnvironmentSDFGIRayCount)

Sets the number of rays to throw per frame when computing signed distance field global illumination. Equivalent to [ProjectSettings.rendering/global_illumination/sdfgi/probe_ray_count](class_projectsettings.md#class-projectsettings-property-rendering-global-illumination-sdfgi-probe-ray-count).

---

 **environment_set_sky**(env: [RID](class_rid.md#class-rid), sky: [RID](class_rid.md#class-rid))

Sets the [Sky](class_sky.md#class-sky) to be used as the environment's background when using *BGMode* sky. Equivalent to [Environment.sky](class_environment.md#class-environment-property-sky).

---

 **environment_set_sky_custom_fov**(env: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))

Sets a custom field of view for the background [Sky](class_sky.md#class-sky). Equivalent to [Environment.sky_custom_fov](class_environment.md#class-environment-property-sky-custom-fov).

---

 **environment_set_sky_orientation**(env: [RID](class_rid.md#class-rid), orientation: [Basis](class_basis.md#class-basis))

Sets the rotation of the background [Sky](class_sky.md#class-sky) expressed as a [Basis](class_basis.md#class-basis). Equivalent to [Environment.sky_rotation](class_environment.md#class-environment-property-sky-rotation), where the rotation vector is used to construct the [Basis](class_basis.md#class-basis).

---

 **environment_set_ssao**(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), radius: [float](class_float.md#class-float), intensity: [float](class_float.md#class-float), power: [float](class_float.md#class-float), detail: [float](class_float.md#class-float), horizon: [float](class_float.md#class-float), sharpness: [float](class_float.md#class-float), light_affect: [float](class_float.md#class-float), ao_channel_affect: [float](class_float.md#class-float))

Sets the variables to be used with the screen-space ambient occlusion (SSAO) post-process effect. See [Environment](class_environment.md#class-environment) for more details.

---

 **environment_set_ssao_quality**(quality: EnvironmentSSAOQuality, half_size: [bool](class_bool.md#class-bool), adaptive_target: [float](class_float.md#class-float), blur_passes: [int](class_int.md#class-int), fadeout_from: [float](class_float.md#class-float), fadeout_to: [float](class_float.md#class-float))

Sets the quality level of the screen-space ambient occlusion (SSAO) post-process effect. See [Environment](class_environment.md#class-environment) for more details.

---

 **environment_set_ssil_quality**(quality: EnvironmentSSILQuality, half_size: [bool](class_bool.md#class-bool), adaptive_target: [float](class_float.md#class-float), blur_passes: [int](class_int.md#class-int), fadeout_from: [float](class_float.md#class-float), fadeout_to: [float](class_float.md#class-float))

Sets the quality level of the screen-space indirect lighting (SSIL) post-process effect. See [Environment](class_environment.md#class-environment) for more details.

---

 **environment_set_ssr**(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), max_steps: [int](class_int.md#class-int), fade_in: [float](class_float.md#class-float), fade_out: [float](class_float.md#class-float), depth_tolerance: [float](class_float.md#class-float))

Sets the variables to be used with the screen-space reflections (SSR) post-process effect. See [Environment](class_environment.md#class-environment) for more details.

---

 **environment_set_ssr_half_size**(half_size: [bool](class_bool.md#class-bool))

Sets whether screen-space reflections will be rendered at full or half size. Half size is faster, but may look pixelated or cause flickering.

---

 **environment_set_ssr_roughness_quality**(quality: EnvironmentSSRRoughnessQuality)

**Deprecated:** This option no longer does anything.

---

 **environment_set_tonemap**(env: [RID](class_rid.md#class-rid), tone_mapper: EnvironmentToneMapper, exposure: [float](class_float.md#class-float), white: [float](class_float.md#class-float))

Sets the variables to be used with the "tonemap" post-process effect. See [Environment](class_environment.md#class-environment) for more details.

---

 **environment_set_tonemap_agx_contrast**(env: [RID](class_rid.md#class-rid), agx_contrast: [float](class_float.md#class-float))

See [Environment.tonemap_agx_contrast](class_environment.md#class-environment-property-tonemap-agx-contrast) for more details.

---

 **environment_set_volumetric_fog**(env: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), density: [float](class_float.md#class-float), albedo: [Color](class_color.md#class-color), emission: [Color](class_color.md#class-color), emission_energy: [float](class_float.md#class-float), anisotropy: [float](class_float.md#class-float), length: [float](class_float.md#class-float), detail_spread: [float](class_float.md#class-float), gi_inject: [float](class_float.md#class-float), temporal_reprojection: [bool](class_bool.md#class-bool), temporal_reprojection_amount: [float](class_float.md#class-float), ambient_inject: [float](class_float.md#class-float), sky_affect: [float](class_float.md#class-float))

Sets the variables to be used with the volumetric fog post-process effect. See [Environment](class_environment.md#class-environment) for more details.

---

 **environment_set_volumetric_fog_filter_active**(active: [bool](class_bool.md#class-bool))

Enables filtering of the volumetric fog scattering buffer. This results in much smoother volumes with very few under-sampling artifacts.

---

 **environment_set_volumetric_fog_volume_size**(size: [int](class_int.md#class-int), depth: [int](class_int.md#class-int))

Sets the resolution of the volumetric fog's froxel buffer. `size` is modified by the screen's aspect ratio and then used to set the width and height of the buffer. While `depth` is directly used to set the depth of the buffer.

---

[RID](class_rid.md#class-rid) **fog_volume_create**()

Creates a new fog volume and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `fog_volume_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent node is [FogVolume](class_fogvolume.md#class-fogvolume).

---

 **fog_volume_set_material**(fog_volume: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))

Sets the [Material](class_material.md#class-material) of the fog volume. Can be either a [FogMaterial](class_fogmaterial.md#class-fogmaterial) or a custom [ShaderMaterial](class_shadermaterial.md#class-shadermaterial).

---

 **fog_volume_set_shape**(fog_volume: [RID](class_rid.md#class-rid), shape: FogVolumeShape)

Sets the shape of the fog volume to either FOG_VOLUME_SHAPE_ELLIPSOID, FOG_VOLUME_SHAPE_CONE, FOG_VOLUME_SHAPE_CYLINDER, FOG_VOLUME_SHAPE_BOX or FOG_VOLUME_SHAPE_WORLD.

---

 **fog_volume_set_size**(fog_volume: [RID](class_rid.md#class-rid), size: [Vector3](class_vector3.md#class-vector3))

Sets the size of the fog volume when shape is FOG_VOLUME_SHAPE_ELLIPSOID, FOG_VOLUME_SHAPE_CONE, FOG_VOLUME_SHAPE_CYLINDER or FOG_VOLUME_SHAPE_BOX.

---

 **force_draw**(swap_buffers: [bool](class_bool.md#class-bool) = true, frame_step: [float](class_float.md#class-float) = 0.0)

Forces redrawing of all viewports at once. Must be called from the main thread.

---

 **force_sync**()

Forces a synchronization between the CPU and GPU, which may be required in certain cases. Only call this when needed, as CPU-GPU synchronization has a performance cost.

---

 **free_rid**(rid: [RID](class_rid.md#class-rid))

Tries to free an object in the RenderingServer. To avoid memory leaks, this should be called after using an object as memory management does not occur automatically when using RenderingServer directly.

---

[String](class_string.md#class-string) **get_current_rendering_driver_name**()

Returns the name of the current rendering driver. This can be `vulkan`, `d3d12`, `metal`, `opengl3`, `opengl3_es`, or `opengl3_angle`. See also get_current_rendering_method().

When [ProjectSettings.rendering/renderer/rendering_method](class_projectsettings.md#class-projectsettings-property-rendering-renderer-rendering-method) is `forward_plus` or `mobile`, the rendering driver is determined by [ProjectSettings.rendering/rendering_device/driver](class_projectsettings.md#class-projectsettings-property-rendering-rendering-device-driver).

When [ProjectSettings.rendering/renderer/rendering_method](class_projectsettings.md#class-projectsettings-property-rendering-renderer-rendering-method) is `gl_compatibility`, the rendering driver is determined by [ProjectSettings.rendering/gl_compatibility/driver](class_projectsettings.md#class-projectsettings-property-rendering-gl-compatibility-driver).

The rendering driver is also determined by the `--rendering-driver` command line argument that overrides this project setting, or an automatic fallback that is applied depending on the hardware.

---

[String](class_string.md#class-string) **get_current_rendering_method**()

Returns the name of the current rendering method. This can be `forward_plus`, `mobile`, or `gl_compatibility`. See also get_current_rendering_driver_name().

The rendering method is determined by [ProjectSettings.rendering/renderer/rendering_method](class_projectsettings.md#class-projectsettings-property-rendering-renderer-rendering-method), the `--rendering-method` command line argument that overrides this project setting, or an automatic fallback that is applied depending on the hardware.

---

[Color](class_color.md#class-color) **get_default_clear_color**()

Returns the default clear color which is used when a specific clear color has not been selected. See also set_default_clear_color().

---

[float](class_float.md#class-float) **get_frame_setup_time_cpu**()

Returns the time taken to setup rendering on the CPU in milliseconds. This value is shared across all viewports and does *not* require viewport_set_measure_render_time() to be enabled on a viewport to be queried. See also viewport_get_measured_render_time_cpu().

---

[RenderingDevice](class_renderingdevice.md#class-renderingdevice) **get_rendering_device**()

Returns the global RenderingDevice.

**Note:** When using the OpenGL rendering driver or when running in headless mode, this function always returns `null`.

---

[int](class_int.md#class-int) **get_rendering_info**(info: RenderingInfo)

Returns a statistic about the rendering engine which can be used for performance profiling. See also viewport_get_render_info(), which returns information specific to a viewport.

**Note:** Only 3D rendering is currently taken into account by some of these values, such as the number of draw calls.

**Note:** Rendering information is not available until at least 2 frames have been rendered by the engine. If rendering information is not available, get_rendering_info() returns `0`. To print rendering information in `_ready()` successfully, use the following:

```gdscript
func _ready():
    for _i in 2:
        await get_tree().process_frame

    print(RenderingServer.get_rendering_info(RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME))
```

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **get_shader_parameter_list**(shader: [RID](class_rid.md#class-rid))

Returns the parameters of a shader.

---

[RID](class_rid.md#class-rid) **get_test_cube**()

Returns the RID of the test cube. This mesh will be created and returned on the first call to get_test_cube(), then it will be cached for subsequent calls. See also make_sphere_mesh().

---

[RID](class_rid.md#class-rid) **get_test_texture**()

Returns the RID of a 256×256 texture with a testing pattern on it (in [Image.FORMAT_RGB8](class_image.md#class-image-constant-format-rgb8) format). This texture will be created and returned on the first call to get_test_texture(), then it will be cached for subsequent calls. See also get_white_texture().

**Example:** Get the test texture and apply it to a [Sprite2D](class_sprite2d.md#class-sprite2d) node:

```gdscript
var texture_rid = RenderingServer.get_test_texture()
var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
$Sprite2D.texture = texture
```

---

[String](class_string.md#class-string) **get_video_adapter_api_version**()

Returns the version of the graphics video adapter *currently in use* (e.g. "1.2.189" for Vulkan, "3.3.0 NVIDIA 510.60.02" for OpenGL). This version may be different from the actual latest version supported by the hardware, as Godot may not always request the latest version. See also [OS.get_video_adapter_driver_info()](class_os.md#class-os-method-get-video-adapter-driver-info).

**Note:** When running a headless or server binary, this function returns an empty string.

---

[String](class_string.md#class-string) **get_video_adapter_name**()

Returns the name of the video adapter (e.g. "GeForce GTX 1080/PCIe/SSE2").

**Note:** When running a headless or server binary, this function returns an empty string.

**Note:** On the web platform, some browsers such as Firefox may report a different, fixed GPU name such as "GeForce GTX 980" (regardless of the user's actual GPU model). This is done to make fingerprinting more difficult.

---

[DeviceType](class_renderingdevice.md#enum-renderingdevice-devicetype) **get_video_adapter_type**()

Returns the type of the video adapter. Since dedicated graphics cards from a given generation will *usually* be significantly faster than integrated graphics made in the same generation, the device type can be used as a basis for automatic graphics settings adjustment. However, this is not always true, so make sure to provide users with a way to manually override graphics settings.

**Note:** When using the OpenGL rendering driver or when running in headless mode, this function always returns [RenderingDevice.DEVICE_TYPE_OTHER](class_renderingdevice.md#class-renderingdevice-constant-device-type-other).

---

[String](class_string.md#class-string) **get_video_adapter_vendor**()

Returns the vendor of the video adapter (e.g. "NVIDIA Corporation").

**Note:** When running a headless or server binary, this function returns an empty string.

---

[RID](class_rid.md#class-rid) **get_white_texture**()

Returns the ID of a 4×4 white texture (in [Image.FORMAT_RGB8](class_image.md#class-image-constant-format-rgb8) format). This texture will be created and returned on the first call to get_white_texture(), then it will be cached for subsequent calls. See also get_test_texture().

**Example:** Get the white texture and apply it to a [Sprite2D](class_sprite2d.md#class-sprite2d) node:

```gdscript
var texture_rid = RenderingServer.get_white_texture()
var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
$Sprite2D.texture = texture
```

---

 **gi_set_use_half_resolution**(half_resolution: [bool](class_bool.md#class-bool))

If `half_resolution` is `true`, renders [VoxelGI](class_voxelgi.md#class-voxelgi) and SDFGI ([Environment.sdfgi_enabled](class_environment.md#class-environment-property-sdfgi-enabled)) buffers at halved resolution on each axis (e.g. 960×540 when the viewport size is 1920×1080). This improves performance significantly when VoxelGI or SDFGI is enabled, at the cost of artifacts that may be visible on polygon edges. The loss in quality becomes less noticeable as the viewport resolution increases. [LightmapGI](class_lightmapgi.md#class-lightmapgi) rendering is not affected by this setting. Equivalent to [ProjectSettings.rendering/global_illumination/gi/use_half_resolution](class_projectsettings.md#class-projectsettings-property-rendering-global-illumination-gi-use-half-resolution).

---

 **global_shader_parameter_add**(name: [StringName](class_stringname.md#class-stringname), type: GlobalShaderParameterType, default_value: [Variant](class_variant.md#class-variant))

Creates a new global shader uniform.

**Note:** Global shader parameter names are case-sensitive.

---

[Variant](class_variant.md#class-variant) **global_shader_parameter_get**(name: [StringName](class_stringname.md#class-stringname))

Returns the value of the global shader uniform specified by `name`.

**Note:** global_shader_parameter_get() has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **global_shader_parameter_get_list**()

Returns the list of global shader uniform names.

**Note:** global_shader_parameter_get() has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.

---

GlobalShaderParameterType **global_shader_parameter_get_type**(name: [StringName](class_stringname.md#class-stringname))

Returns the type associated to the global shader uniform specified by `name`.

**Note:** global_shader_parameter_get() has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.

---

 **global_shader_parameter_remove**(name: [StringName](class_stringname.md#class-stringname))

Removes the global shader uniform specified by `name`.

---

 **global_shader_parameter_set**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Sets the global shader uniform `name` to `value`.

---

 **global_shader_parameter_set_override**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Overrides the global shader uniform `name` with `value`. Equivalent to the [ShaderGlobalsOverride](class_shaderglobalsoverride.md#class-shaderglobalsoverride) node.

---

[bool](class_bool.md#class-bool) **has_changed**()

Returns `true` if changes have been made to the RenderingServer's data. force_draw() is usually called if this happens.

---

[bool](class_bool.md#class-bool) **has_feature**(feature: Features)

**Deprecated:** This method has not been used since Godot 3.0.

This method does nothing and always returns `false`.

---

[bool](class_bool.md#class-bool) **has_os_feature**(feature: [String](class_string.md#class-string))

Returns `true` if the OS supports a certain `feature`. Features might be `s3tc`, `etc`, and `etc2`.

---

 **instance_attach_object_instance_id**(instance: [RID](class_rid.md#class-rid), id: [int](class_int.md#class-int))

Attaches a unique Object ID to instance. Object ID must be attached to instance for proper culling with instances_cull_aabb(), instances_cull_convex(), and instances_cull_ray().

---

 **instance_attach_skeleton**(instance: [RID](class_rid.md#class-rid), skeleton: [RID](class_rid.md#class-rid))

Attaches a skeleton to an instance. Removes the previous skeleton from the instance.

---

[RID](class_rid.md#class-rid) **instance_create**()

Creates a visual instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `instance_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

An instance is a way of placing a 3D object in the scenario. Objects like particles, meshes, reflection probes and decals need to be associated with an instance to be visible in the scenario using instance_set_base().

**Note:** The equivalent node is [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d).

---

[RID](class_rid.md#class-rid) **instance_create2**(base: [RID](class_rid.md#class-rid), scenario: [RID](class_rid.md#class-rid))

Creates a visual instance, adds it to the RenderingServer, and sets both base and scenario. It can be accessed with the RID that is returned. This RID will be used in all `instance_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method. This is a shorthand for using instance_create() and setting the base and scenario manually.

---

[Variant](class_variant.md#class-variant) **instance_geometry_get_shader_parameter**(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))

Returns the value of the per-instance shader uniform from the specified 3D geometry instance. Equivalent to [GeometryInstance3D.get_instance_shader_parameter()](class_geometryinstance3d.md#class-geometryinstance3d-method-get-instance-shader-parameter).

**Note:** Per-instance shader parameter names are case-sensitive.

---

[Variant](class_variant.md#class-variant) **instance_geometry_get_shader_parameter_default_value**(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))

Returns the default value of the per-instance shader uniform from the specified 3D geometry instance. Equivalent to [GeometryInstance3D.get_instance_shader_parameter()](class_geometryinstance3d.md#class-geometryinstance3d-method-get-instance-shader-parameter).

---

[Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)] **instance_geometry_get_shader_parameter_list**(instance: [RID](class_rid.md#class-rid))

Returns a dictionary of per-instance shader uniform names of the per-instance shader uniform from the specified 3D geometry instance. The returned dictionary is in PropertyInfo format, with the keys `name`, `class_name`, `type`, `hint`, `hint_string` and `usage`. Equivalent to [GeometryInstance3D.get_instance_shader_parameter()](class_geometryinstance3d.md#class-geometryinstance3d-method-get-instance-shader-parameter).

---

 **instance_geometry_set_cast_shadows_setting**(instance: [RID](class_rid.md#class-rid), shadow_casting_setting: ShadowCastingSetting)

Sets the shadow casting setting. Equivalent to [GeometryInstance3D.cast_shadow](class_geometryinstance3d.md#class-geometryinstance3d-property-cast-shadow).

---

 **instance_geometry_set_flag**(instance: [RID](class_rid.md#class-rid), flag: InstanceFlags, enabled: [bool](class_bool.md#class-bool))

Sets the `flag` for a given `instance` to `enabled`.

---

 **instance_geometry_set_lightmap**(instance: [RID](class_rid.md#class-rid), lightmap: [RID](class_rid.md#class-rid), lightmap_uv_scale: [Rect2](class_rect2.md#class-rect2), lightmap_slice: [int](class_int.md#class-int))

Sets the lightmap GI instance to use for the specified 3D geometry instance. The lightmap UV scale for the specified instance (equivalent to [GeometryInstance3D.gi_lightmap_scale](class_geometryinstance3d.md#class-geometryinstance3d-property-gi-lightmap-scale)) and lightmap atlas slice must also be specified.

---

 **instance_geometry_set_lod_bias**(instance: [RID](class_rid.md#class-rid), lod_bias: [float](class_float.md#class-float))

Sets the level of detail bias to use when rendering the specified 3D geometry instance. Higher values result in higher detail from further away. Equivalent to [GeometryInstance3D.lod_bias](class_geometryinstance3d.md#class-geometryinstance3d-property-lod-bias).

---

 **instance_geometry_set_material_overlay**(instance: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))

Sets a material that will be rendered for all surfaces on top of active materials for the mesh associated with this instance. Equivalent to [GeometryInstance3D.material_overlay](class_geometryinstance3d.md#class-geometryinstance3d-property-material-overlay).

---

 **instance_geometry_set_material_override**(instance: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))

Sets a material that will override the material for all surfaces on the mesh associated with this instance. Equivalent to [GeometryInstance3D.material_override](class_geometryinstance3d.md#class-geometryinstance3d-property-material-override).

---

 **instance_geometry_set_shader_parameter**(instance: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Sets the per-instance shader uniform on the specified 3D geometry instance. Equivalent to [GeometryInstance3D.set_instance_shader_parameter()](class_geometryinstance3d.md#class-geometryinstance3d-method-set-instance-shader-parameter).

---

 **instance_geometry_set_transparency**(instance: [RID](class_rid.md#class-rid), transparency: [float](class_float.md#class-float))

Sets the transparency for the given geometry instance. Equivalent to [GeometryInstance3D.transparency](class_geometryinstance3d.md#class-geometryinstance3d-property-transparency).

A transparency of `0.0` is fully opaque, while `1.0` is fully transparent. Values greater than `0.0` (exclusive) will force the geometry's materials to go through the transparent pipeline, which is slower to render and can exhibit rendering issues due to incorrect transparency sorting. However, unlike using a transparent material, setting `transparency` to a value greater than `0.0` (exclusive) will *not* disable shadow rendering.

In spatial shaders, `1.0 - transparency` is set as the default value of the `ALPHA` built-in.

**Note:** `transparency` is clamped between `0.0` and `1.0`, so this property cannot be used to make transparent materials more opaque than they originally are.

---

 **instance_geometry_set_visibility_range**(instance: [RID](class_rid.md#class-rid), min: [float](class_float.md#class-float), max: [float](class_float.md#class-float), min_margin: [float](class_float.md#class-float), max_margin: [float](class_float.md#class-float), fade_mode: VisibilityRangeFadeMode)

Sets the visibility range values for the given geometry instance. Equivalent to [GeometryInstance3D.visibility_range_begin](class_geometryinstance3d.md#class-geometryinstance3d-property-visibility-range-begin) and related properties.

---

 **instance_set_base**(instance: [RID](class_rid.md#class-rid), base: [RID](class_rid.md#class-rid))

Sets the base of the instance. A base can be any of the 3D objects that are created in the RenderingServer that can be displayed. For example, any of the light types, mesh, multimesh, particle system, reflection probe, decal, lightmap, voxel GI and visibility notifiers are all types that can be set as the base of an instance in order to be displayed in the scenario.

---

 **instance_set_blend_shape_weight**(instance: [RID](class_rid.md#class-rid), shape: [int](class_int.md#class-int), weight: [float](class_float.md#class-float))

Sets the weight for a given blend shape associated with this instance.

---

 **instance_set_custom_aabb**(instance: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))

Sets a custom AABB to use when culling objects from the view frustum. Equivalent to setting [GeometryInstance3D.custom_aabb](class_geometryinstance3d.md#class-geometryinstance3d-property-custom-aabb).

---

 **instance_set_extra_visibility_margin**(instance: [RID](class_rid.md#class-rid), margin: [float](class_float.md#class-float))

Sets a margin to increase the size of the AABB when culling objects from the view frustum. This allows you to avoid culling objects that fall outside the view frustum. Equivalent to [GeometryInstance3D.extra_cull_margin](class_geometryinstance3d.md#class-geometryinstance3d-property-extra-cull-margin).

---

 **instance_set_ignore_culling**(instance: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `true`, ignores all culling on the specified 3D geometry instance, including frustum culling, occlusion culling, and layer culling. This is not the same as [GeometryInstance3D.ignore_occlusion_culling](class_geometryinstance3d.md#class-geometryinstance3d-property-ignore-occlusion-culling), which only ignores occlusion culling but leaves frustum and layer culling intact.

---

 **instance_set_layer_mask**(instance: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Sets the render layers that this instance will be drawn to. Equivalent to [VisualInstance3D.layers](class_visualinstance3d.md#class-visualinstance3d-property-layers).

---

 **instance_set_pivot_data**(instance: [RID](class_rid.md#class-rid), sorting_offset: [float](class_float.md#class-float), use_aabb_center: [bool](class_bool.md#class-bool))

Sets the sorting offset and switches between using the bounding box or instance origin for depth sorting.

---

 **instance_set_scenario**(instance: [RID](class_rid.md#class-rid), scenario: [RID](class_rid.md#class-rid))

Sets the scenario that the instance is in. The scenario is the 3D world that the objects will be displayed in.

---

 **instance_set_surface_override_material**(instance: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), material: [RID](class_rid.md#class-rid))

Sets the override material of a specific surface. Equivalent to [MeshInstance3D.set_surface_override_material()](class_meshinstance3d.md#class-meshinstance3d-method-set-surface-override-material).

---

 **instance_set_transform**(instance: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))

Sets the world space transform of the instance. Equivalent to [Node3D.global_transform](class_node3d.md#class-node3d-property-global-transform).

---

 **instance_set_visibility_parent**(instance: [RID](class_rid.md#class-rid), parent: [RID](class_rid.md#class-rid))

Sets the visibility parent for the given instance. Equivalent to [Node3D.visibility_parent](class_node3d.md#class-node3d-property-visibility-parent).

---

 **instance_set_visible**(instance: [RID](class_rid.md#class-rid), visible: [bool](class_bool.md#class-bool))

Sets whether an instance is drawn or not. Equivalent to [Node3D.visible](class_node3d.md#class-node3d-property-visible).

---

 **instance_teleport**(instance: [RID](class_rid.md#class-rid))

Resets motion vectors and other interpolated values. Use this *after* teleporting a mesh from one position to another to avoid ghosting artifacts.

---

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **instances_cull_aabb**(aabb: [AABB](class_aabb.md#class-aabb), scenario: [RID](class_rid.md#class-rid) = RID())

Returns an array of object IDs intersecting with the provided AABB. Only 3D nodes that inherit from [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) are considered, such as [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) or [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d). Use [@GlobalScope.instance_from_id()](class_@globalscope.md#class-globalscope-method-instance-from-id) to obtain the actual nodes. A scenario RID must be provided, which is available in the [World3D](class_world3d.md#class-world3d) you want to query. This forces an update for all resources queued to update.

**Warning:** This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.

---

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **instances_cull_convex**(convex: [Array](class_array.md#class-array)[[Plane](class_plane.md#class-plane)], scenario: [RID](class_rid.md#class-rid) = RID())

Returns an array of object IDs intersecting with the provided convex shape. Only 3D nodes that inherit from [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) are considered, such as [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) or [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d). Use [@GlobalScope.instance_from_id()](class_@globalscope.md#class-globalscope-method-instance-from-id) to obtain the actual nodes. A scenario RID must be provided, which is available in the [World3D](class_world3d.md#class-world3d) you want to query. This forces an update for all resources queued to update.

**Warning:** This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.

---

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **instances_cull_ray**(from: [Vector3](class_vector3.md#class-vector3), to: [Vector3](class_vector3.md#class-vector3), scenario: [RID](class_rid.md#class-rid) = RID())

Returns an array of object IDs intersecting with the provided 3D ray. Only 3D nodes that inherit from [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) are considered, such as [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) or [DirectionalLight3D](class_directionallight3d.md#class-directionallight3d). Use [@GlobalScope.instance_from_id()](class_@globalscope.md#class-globalscope-method-instance-from-id) to obtain the actual nodes. A scenario RID must be provided, which is available in the [World3D](class_world3d.md#class-world3d) you want to query. This forces an update for all resources queued to update.

**Warning:** This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.

---

[bool](class_bool.md#class-bool) **is_on_render_thread**()

Returns `true` if our code is currently executing on the rendering thread.

---

 **light_area_set_normalize_energy**(light: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Defines whether the energy of an [AreaLight3D](class_arealight3d.md#class-arealight3d) is normalized (divided) by its area. If set to `true`, changing the size does not affect the total energy output. Equivalent to [AreaLight3D.area_normalize_energy](class_arealight3d.md#class-arealight3d-property-area-normalize-energy).

---

 **light_area_set_size**(light: [RID](class_rid.md#class-rid), size: [Vector2](class_vector2.md#class-vector2))

Sets the extents (width and height) in meters for this area light. Equivalent to [AreaLight3D.area_size](class_arealight3d.md#class-arealight3d-property-area-size).

---

 **light_directional_set_blend_splits**(light: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, this directional light will blend between shadow map splits resulting in a smoother transition between them. Equivalent to [DirectionalLight3D.directional_shadow_blend_splits](class_directionallight3d.md#class-directionallight3d-property-directional-shadow-blend-splits).

---

 **light_directional_set_shadow_mode**(light: [RID](class_rid.md#class-rid), mode: LightDirectionalShadowMode)

Sets the shadow mode for this directional light. Equivalent to [DirectionalLight3D.directional_shadow_mode](class_directionallight3d.md#class-directionallight3d-property-directional-shadow-mode).

---

 **light_directional_set_sky_mode**(light: [RID](class_rid.md#class-rid), mode: LightDirectionalSkyMode)

If `true`, this light will not be used for anything except sky shaders. Use this for lights that impact your sky shader that you may want to hide from affecting the rest of the scene. For example, you may want to enable this when the sun in your sky shader falls below the horizon.

---

 **light_omni_set_shadow_mode**(light: [RID](class_rid.md#class-rid), mode: LightOmniShadowMode)

Sets whether to use a dual paraboloid or a cubemap for the shadow map. Dual paraboloid is faster but may suffer from artifacts. Equivalent to [OmniLight3D.omni_shadow_mode](class_omnilight3d.md#class-omnilight3d-property-omni-shadow-mode).

---

 **light_projectors_set_filter**(filter: LightProjectorFilter)

Sets the texture filter mode to use when rendering light projectors. This parameter is global and cannot be set on a per-light basis.

---

 **light_set_bake_mode**(light: [RID](class_rid.md#class-rid), bake_mode: LightBakeMode)

Sets the bake mode to use for the specified 3D light. Equivalent to [Light3D.light_bake_mode](class_light3d.md#class-light3d-property-light-bake-mode).

---

 **light_set_color**(light: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Sets the color of the light. Equivalent to [Light3D.light_color](class_light3d.md#class-light3d-property-light-color).

---

 **light_set_cull_mask**(light: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Sets the cull mask for this 3D light. Lights only affect objects in the selected layers. Equivalent to [Light3D.light_cull_mask](class_light3d.md#class-light3d-property-light-cull-mask).

---

 **light_set_distance_fade**(decal: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool), begin: [float](class_float.md#class-float), shadow: [float](class_float.md#class-float), length: [float](class_float.md#class-float))

Sets the distance fade for this 3D light. This acts as a form of level of detail (LOD) and can be used to improve performance. Equivalent to [Light3D.distance_fade_enabled](class_light3d.md#class-light3d-property-distance-fade-enabled), [Light3D.distance_fade_begin](class_light3d.md#class-light3d-property-distance-fade-begin), [Light3D.distance_fade_shadow](class_light3d.md#class-light3d-property-distance-fade-shadow), and [Light3D.distance_fade_length](class_light3d.md#class-light3d-property-distance-fade-length).

---

 **light_set_max_sdfgi_cascade**(light: [RID](class_rid.md#class-rid), cascade: [int](class_int.md#class-int))

Sets the maximum SDFGI cascade in which the 3D light's indirect lighting is rendered. Higher values allow the light to be rendered in SDFGI further away from the camera.

---

 **light_set_negative**(light: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, the 3D light will subtract light instead of adding light. Equivalent to [Light3D.light_negative](class_light3d.md#class-light3d-property-light-negative).

---

 **light_set_param**(light: [RID](class_rid.md#class-rid), param: LightParam, value: [float](class_float.md#class-float))

Sets the specified 3D light parameter. Equivalent to [Light3D.set_param()](class_light3d.md#class-light3d-method-set-param).

---

 **light_set_projector**(light: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))

Sets the projector texture to use for the specified 3D light. Equivalent to [Light3D.light_projector](class_light3d.md#class-light3d-property-light-projector).

---

 **light_set_reverse_cull_face_mode**(light: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `true`, reverses the backface culling of the mesh. This can be useful when you have a flat mesh that has a light behind it. If you need to cast a shadow on both sides of the mesh, set the mesh to use double-sided shadows with instance_geometry_set_cast_shadows_setting(). Equivalent to [Light3D.shadow_reverse_cull_face](class_light3d.md#class-light3d-property-shadow-reverse-cull-face).

---

 **light_set_shadow**(light: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `true`, light will cast shadows. Equivalent to [Light3D.shadow_enabled](class_light3d.md#class-light3d-property-shadow-enabled).

---

 **light_set_shadow_caster_mask**(light: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Sets the shadow caster mask for this 3D light. Shadows will only be cast using objects in the selected layers. Equivalent to [Light3D.shadow_caster_mask](class_light3d.md#class-light3d-property-shadow-caster-mask).

---

[RID](class_rid.md#class-rid) **lightmap_create**()

Creates a new lightmap global illumination instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `lightmap_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent node is [LightmapGI](class_lightmapgi.md#class-lightmapgi).

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **lightmap_get_probe_capture_bsp_tree**(lightmap: [RID](class_rid.md#class-rid))

Returns the BSP tree data used for accelerating probe lookups. The BSP data is structured as a series of six signed 32-bit values per BSP node in this order: `float plane_x`, `float plane_y`, `float plane_z`, `float plane_distance`, `int32_t over`, `int32_t under`. An empty leaf is denoted by the value `-2147483648` (the minimum 32-bit signed integer). See also lightmap_set_probe_capture_data().

---

[PackedVector3Array](class_packedvector3array.md#class-packedvector3array) **lightmap_get_probe_capture_points**(lightmap: [RID](class_rid.md#class-rid))

Returns the *local space* positions of each lightmap probe capture point. Keep in mind the lightmap instance may have a non-zero transform, which will affect the position of the probe capture points. See also lightmap_set_probe_capture_data().

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **lightmap_get_probe_capture_sh**(lightmap: [RID](class_rid.md#class-rid))

Returns the L0, L1, and L2 [spherical harmonics](https://en.wikipedia.org/wiki/Spherical_harmonics) data for each lightmap probe capture point. This is specified as 9 [Color](class_color.md#class-color) values per probe, which means the size of the returned data is always 9 times the number of probe points. See also lightmap_set_probe_capture_data().

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **lightmap_get_probe_capture_tetrahedra**(lightmap: [RID](class_rid.md#class-rid))

Returns the tetrahedralization data used for interpolating between lightmap probe capture points. Each tetrahedron is specified as a series of 4 numbers, each being an index into the probe capture points array returned by lightmap_get_probe_capture_points(). See also lightmap_set_probe_capture_data().

---

 **lightmap_set_baked_exposure_normalization**(lightmap: [RID](class_rid.md#class-rid), baked_exposure: [float](class_float.md#class-float))

Used to inform the renderer what exposure normalization value was used while baking the lightmap. This value will be used and modulated at run time to ensure that the lightmap maintains a consistent level of exposure even if the scene-wide exposure normalization is changed at run time. For more information see camera_attributes_set_exposure().

---

 **lightmap_set_probe_bounds**(lightmap: [RID](class_rid.md#class-rid), bounds: [AABB](class_aabb.md#class-aabb))

Sets the bounds that this lightmap instance should visually affect, both in terms of static lightmap baking and probe-based global illumination.

---

 **lightmap_set_probe_capture_data**(lightmap: [RID](class_rid.md#class-rid), points: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), point_sh: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray), tetrahedra: [PackedInt32Array](class_packedint32array.md#class-packedint32array), bsp_tree: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Sets the probe capture data for the given lightmap instance. See lightmap_get_probe_capture_points(), lightmap_get_probe_capture_sh(), lightmap_get_probe_capture_tetrahedra(), and lightmap_get_probe_capture_bsp_tree() for the expected data formats.

---

 **lightmap_set_probe_capture_update_speed**(speed: [float](class_float.md#class-float))

The framerate-independent update speed when representing dynamic object lighting from [LightmapProbe](class_lightmapprobe.md#class-lightmapprobe)s. Higher values make dynamic object lighting update faster. Higher values can prevent fast-moving objects from having "outdated" indirect lighting displayed on them, at the cost of possible flickering when an object moves from a bright area to a shaded area. See also [ProjectSettings.rendering/lightmapping/probe_capture/update_speed](class_projectsettings.md#class-projectsettings-property-rendering-lightmapping-probe-capture-update-speed).

---

 **lightmap_set_probe_interior**(lightmap: [RID](class_rid.md#class-rid), interior: [bool](class_bool.md#class-bool))

Sets whether the lightmap instance should be considered as interior (when `interior` is `true`). If the lightmap is marked as interior, environment lighting is ignored when baking lightmaps.

---

 **lightmap_set_textures**(lightmap: [RID](class_rid.md#class-rid), light: [RID](class_rid.md#class-rid), uses_sh: [bool](class_bool.md#class-bool))

Set the textures on the given `lightmap` GI instance to the texture array pointed to by the `light` RID. If the lightmap texture was baked with [LightmapGI.directional](class_lightmapgi.md#class-lightmapgi-property-directional) set to `true`, then `uses_sh` must also be `true`.

---

 **lightmaps_set_bicubic_filter**(enable: [bool](class_bool.md#class-bool))

Toggles whether a bicubic filter should be used when lightmaps are sampled. This smoothens their appearance at a performance cost.

---

[RID](class_rid.md#class-rid) **make_sphere_mesh**(latitudes: [int](class_int.md#class-int), longitudes: [int](class_int.md#class-int), radius: [float](class_float.md#class-float))

Returns a mesh of a sphere with the given number of horizontal subdivisions, vertical subdivisions and radius. See also get_test_cube().

---

[RID](class_rid.md#class-rid) **material_create**()

Creates an empty material and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `material_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [Material](class_material.md#class-material).

---

[Variant](class_variant.md#class-variant) **material_get_param**(material: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname))

Returns the value of a certain material's parameter.

---

 **material_set_next_pass**(material: [RID](class_rid.md#class-rid), next_material: [RID](class_rid.md#class-rid))

Sets an object's next material.

---

 **material_set_param**(material: [RID](class_rid.md#class-rid), parameter: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Sets a material's parameter.

---

 **material_set_render_priority**(material: [RID](class_rid.md#class-rid), priority: [int](class_int.md#class-int))

Sets a material's render priority.

---

 **material_set_shader**(shader_material: [RID](class_rid.md#class-rid), shader: [RID](class_rid.md#class-rid))

Sets a shader material's shader.

---

 **material_set_use_debanding**(enable: [bool](class_bool.md#class-bool))

When using the Mobile renderer, material_set_use_debanding() can be used to enable or disable the debanding feature of 3D materials ([BaseMaterial3D](class_basematerial3d.md#class-basematerial3d) and [ShaderMaterial](class_shadermaterial.md#class-shadermaterial)).

material_set_use_debanding() has no effect when using the Compatibility or Forward+ renderer. In Forward+, [Viewport](class_viewport.md#class-viewport) debanding can be used instead.

See also [ProjectSettings.rendering/anti_aliasing/quality/use_debanding](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-use-debanding) and viewport_set_use_debanding().

---

 **mesh_add_surface**(mesh: [RID](class_rid.md#class-rid), surface: [Dictionary](class_dictionary.md#class-dictionary))

Creates a new surface on the given `mesh`. Equivalent to mesh_add_surface_from_arrays(), but takes a single [Dictionary](class_dictionary.md#class-dictionary) argument instead of separate arguments. The dictionary must follow this structure:

```gdscript
{
    # Required:
    "primitive": RenderingServer.PrimitiveType,
    "format": RenderingServer.ArrayFormat,
    "vertex_data": PackedByteArray,
    "vertex_count": int,
    "aabb": AABB,

    # Optional:
    "attribute_data": PackedByteArray,
    "skin_data": PackedByteArray,
    "index_data": PackedByteArray,
    "index_count": int, # Required if `index_data` is specified.
    "uv_scale": Vector4,
    "lods": [
        # Both values are required for each LOD level.
        {
            "edge_length": float,
            "index_data": PackedByteArray,
        },
    ],
    "bone_aabbs": Array[AABB],
    "blend_shape_data": PackedByteArray,
    "material": Material,
}
```

See also mesh_get_surface(), which returns data in the same structure defined above.

---

 **mesh_add_surface_from_arrays**(mesh: [RID](class_rid.md#class-rid), primitive: PrimitiveType, arrays: [Array](class_array.md#class-array), blend_shapes: [Array](class_array.md#class-array) = [], lods: [Dictionary](class_dictionary.md#class-dictionary) = {}, compress_format: [ArrayFormat] = 0)

Creates a new surface on the given `mesh`. mesh_get_surface_count() will become the surface index for this new surface.

Surfaces are created to be rendered using a `primitive`, which may be any of the values defined in [PrimitiveType](class_mesh.md#enum-mesh-primitivetype).

The `arrays` argument is an array of arrays. Each of the [Mesh.ARRAY_MAX](class_mesh.md#class-mesh-constant-array-max) elements contains an array with some of the mesh data for this surface as described by the corresponding member of [ArrayType](class_mesh.md#enum-mesh-arraytype) or `null` if it is not used by the surface. For example, `arrays[0]` is the array of vertices. That first vertex sub-array is always required; the others are optional. Adding an index array puts this surface into "index mode" where the vertex and other arrays become the sources of data and the index array defines the vertex order. All sub-arrays must have the same length as the vertex array (or be an exact multiple of the vertex array's length, when multiple elements of a sub-array correspond to a single vertex) or be empty, except for [Mesh.ARRAY_INDEX](class_mesh.md#class-mesh-constant-array-index) if it is used.

The `blend_shapes` argument is an array of vertex data for each blend shape. Each element is an array of the same structure as `arrays`, but [Mesh.ARRAY_VERTEX](class_mesh.md#class-mesh-constant-array-vertex), [Mesh.ARRAY_NORMAL](class_mesh.md#class-mesh-constant-array-normal), and [Mesh.ARRAY_TANGENT](class_mesh.md#class-mesh-constant-array-tangent) are set if and only if they are set in `arrays` and all other entries are `null`.

The `lods` argument is a dictionary with [float](class_float.md#class-float) keys and [PackedInt32Array](class_packedint32array.md#class-packedint32array) values. Each entry in the dictionary represents an LOD level of the surface, where the value is the [Mesh.ARRAY_INDEX](class_mesh.md#class-mesh-constant-array-index) array to use for the LOD level and the key is roughly proportional to the distance at which the LOD stats being used. I.e., increasing the key of an LOD also increases the distance that the objects has to be from the camera before the LOD is used.

The `compress_format` argument is the bitwise OR of, as required: One value of ArrayFormat left shifted by `ARRAY_FORMAT_CUSTOMn_SHIFT` for each custom channel in use, ARRAY_FLAG_USE_DYNAMIC_UPDATE, ARRAY_FLAG_USE_8_BONE_WEIGHTS, or ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY.

See [ArrayMesh.add_surface_from_arrays()](class_arraymesh.md#class-arraymesh-method-add-surface-from-arrays) and [ImporterMesh.add_surface()](class_importermesh.md#class-importermesh-method-add-surface) for higher-level equivalents of this method.

**Note:** When using indices, it is recommended to only use points, lines, or triangles.

---

 **mesh_clear**(mesh: [RID](class_rid.md#class-rid))

Removes all surfaces from a mesh.

---

[RID](class_rid.md#class-rid) **mesh_create**()

Creates a new mesh and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `mesh_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this mesh to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent resource is [Mesh](class_mesh.md#class-mesh).

---

[RID](class_rid.md#class-rid) **mesh_create_from_surfaces**(surfaces: [Array](class_array.md#class-array)[[Dictionary](class_dictionary.md#class-dictionary)], blend_shape_count: [int](class_int.md#class-int) = 0)

Creates a new mesh with predefined surfaces for it and adds the mesh to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `mesh_*` RenderingServer functions. This method is more efficient for creating meshes with multiple surfaces compared to creating an empty mesh with mesh_create() and adding surfaces one by one with mesh_add_surface().

Each element in the `surfaces` array must follow the same structure as described in mesh_add_surface(). The `blend_shape_count` parameter must match the blend shape data defined in all surfaces.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this mesh to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent resource is [Mesh](class_mesh.md#class-mesh).

---

[int](class_int.md#class-int) **mesh_get_blend_shape_count**(mesh: [RID](class_rid.md#class-rid))

Returns a mesh's blend shape count.

---

BlendShapeMode **mesh_get_blend_shape_mode**(mesh: [RID](class_rid.md#class-rid))

Returns a mesh's blend shape mode.

---

[AABB](class_aabb.md#class-aabb) **mesh_get_custom_aabb**(mesh: [RID](class_rid.md#class-rid))

Returns a mesh's custom aabb.

---

[Dictionary](class_dictionary.md#class-dictionary) **mesh_get_surface**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))

Returns a mesh's surface as a dictionary following the same structure as described in mesh_add_surface().

---

[int](class_int.md#class-int) **mesh_get_surface_count**(mesh: [RID](class_rid.md#class-rid))

Returns a mesh's number of surfaces.

---

 **mesh_set_blend_shape_mode**(mesh: [RID](class_rid.md#class-rid), mode: BlendShapeMode)

Sets a mesh's blend shape mode.

---

 **mesh_set_custom_aabb**(mesh: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))

Sets a mesh's custom aabb.

---

 **mesh_set_shadow_mesh**(mesh: [RID](class_rid.md#class-rid), shadow_mesh: [RID](class_rid.md#class-rid))

Sets an optional second mesh which can be used for rendering shadows and the depth prepass. Can be used to increase performance by supplying a mesh with fused vertices and only vertex position data (without normals, UVs, colors, etc.).

**Note:** This mesh must have exactly the same vertex positions as the source mesh (including the source mesh's LODs, if present). If vertex positions differ, then the mesh will not draw correctly.

---

[Array](class_array.md#class-array) **mesh_surface_get_arrays**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))

Returns a mesh's surface's buffer arrays.

---

[Array](class_array.md#class-array)[[Array](class_array.md#class-array)] **mesh_surface_get_blend_shape_arrays**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))

Returns a mesh's surface's arrays for blend shapes.

---

[int](class_int.md#class-int) **mesh_surface_get_format_attribute_stride**(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))

Returns the stride of the attribute buffer for a mesh with given `format`.

---

[int](class_int.md#class-int) **mesh_surface_get_format_index_stride**(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))

Returns the stride of the index buffer for a mesh with the given `format`.

---

[int](class_int.md#class-int) **mesh_surface_get_format_normal_tangent_stride**(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))

Returns the stride of the combined normals and tangents for a mesh with given `format`. Note importantly that, while normals and tangents are in the vertex buffer with vertices, they are only interleaved with each other and so have a different stride than vertex positions.

---

[int](class_int.md#class-int) **mesh_surface_get_format_offset**(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int), array_index: [int](class_int.md#class-int))

Returns the offset of a given attribute by `array_index` in the start of its respective buffer.

---

[int](class_int.md#class-int) **mesh_surface_get_format_skin_stride**(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))

Returns the stride of the skin buffer for a mesh with given `format`.

---

[int](class_int.md#class-int) **mesh_surface_get_format_vertex_stride**(format: [ArrayFormat], vertex_count: [int](class_int.md#class-int))

Returns the stride of the vertex positions for a mesh with given `format`. Note importantly that vertex positions are stored consecutively and are not interleaved with the other attributes in the vertex buffer (normals and tangents).

---

[RID](class_rid.md#class-rid) **mesh_surface_get_material**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))

Returns a mesh's surface's material.

---

 **mesh_surface_remove**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int))

Removes the surface at the given index from the Mesh, shifting surfaces with higher index down by one.

---

 **mesh_surface_set_material**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), material: [RID](class_rid.md#class-rid))

Sets a mesh's surface's material.

---

 **mesh_surface_update_attribute_region**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Updates the attribute buffer of the mesh surface with the given `data`. The expected data per attribute is 8 or 12 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector2](class_vector2.md#class-vector2) or [Vector3](class_vector3.md#class-vector3) vertices. This value can be determined with mesh_surface_get_format_attribute_stride() instead.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each attribute.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of attribute locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.

---

 **mesh_surface_update_index_region**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Updates the index buffer of the mesh surface with the given `data`. The expected data are 16 or 32-bit unsigned integers, which can be determined with mesh_surface_get_format_index_stride().

---

 **mesh_surface_update_skin_region**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Updates the skin buffer of the mesh surface with the given `data`. The expected data per skin is 8 or 12 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector2](class_vector2.md#class-vector2) or [Vector3](class_vector3.md#class-vector3) vertices. This value can be determined with mesh_surface_get_format_skin_stride() instead.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each skin.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of skin locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.

---

 **mesh_surface_update_vertex_region**(mesh: [RID](class_rid.md#class-rid), surface: [int](class_int.md#class-int), offset: [int](class_int.md#class-int), data: [PackedByteArray](class_packedbytearray.md#class-packedbytearray))

Updates the vertex buffer of the mesh surface with the given `data`. The expected data per vertex is 8 or 12 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class-vector2), and 3 floats per [Vector3](class_vector3.md#class-vector3)) depending on if the mesh is using [Vector2](class_vector2.md#class-vector2) or [Vector3](class_vector3.md#class-vector3) vertices. This value can be determined with mesh_surface_get_format_vertex_stride() instead.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each vertex.

A [PackedVector3Array](class_packedvector3array.md#class-packedvector3array) of vertex locations can be converted into a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class-packedvector3array-method-to-byte-array) for use in `data`.

---

 **multimesh_allocate_data**(multimesh: [RID](class_rid.md#class-rid), instances: [int](class_int.md#class-int), transform_format: MultimeshTransformFormat, color_format: [bool](class_bool.md#class-bool) = false, custom_data_format: [bool](class_bool.md#class-bool) = false, use_indirect: [bool](class_bool.md#class-bool) = false)

Sets up the multimesh using the specified data. The number of instances is set by `instances`. The format of the instance transforms is set by `transform_format`, which should be set according to whether the multimesh is meant to be rendered in 2D or 3D. If `color_format` is `true`, each instance will have a color associated with it. If `custom_data_format` is `true`, each instance will have a custom data vector associated with it. If `use_indirect` is `true`, an indirect command buffer will be created for this multimesh, allowing the instance count to be modified directly on the GPU. See also multimesh_get_command_buffer_rd_rid().

---

[RID](class_rid.md#class-rid) **multimesh_create**()

Creates a new multimesh on the RenderingServer and returns an [RID](class_rid.md#class-rid) handle. This RID will be used in all `multimesh_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this multimesh to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent resource is [MultiMesh](class_multimesh.md#class-multimesh).

---

[AABB](class_aabb.md#class-aabb) **multimesh_get_aabb**(multimesh: [RID](class_rid.md#class-rid))

Calculates and returns the axis-aligned bounding box that encloses all instances within the multimesh.

---

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **multimesh_get_buffer**(multimesh: [RID](class_rid.md#class-rid))

Returns the MultiMesh data (such as instance transforms, colors, etc.). See multimesh_set_buffer() for details on the returned data.

**Note:** If the buffer is in the engine's internal cache, it will have to be fetched from GPU memory and possibly decompressed. This means multimesh_get_buffer() is potentially a slow operation and should be avoided whenever possible.

---

[RID](class_rid.md#class-rid) **multimesh_get_buffer_rd_rid**(multimesh: [RID](class_rid.md#class-rid))

Returns the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) [RID](class_rid.md#class-rid) handle of the [MultiMesh](class_multimesh.md#class-multimesh), which can be used as any other buffer on the Rendering Device.

---

[RID](class_rid.md#class-rid) **multimesh_get_command_buffer_rd_rid**(multimesh: [RID](class_rid.md#class-rid))

Returns the [RenderingDevice](class_renderingdevice.md#class-renderingdevice) [RID](class_rid.md#class-rid) handle of the [MultiMesh](class_multimesh.md#class-multimesh) command buffer. This [RID](class_rid.md#class-rid) is only valid if `use_indirect` is set to `true` when allocating data through multimesh_allocate_data(). It can be used to directly modify the instance count via buffer.

The data structure is dependent on both how many surfaces the mesh contains and whether it is indexed or not, the buffer has 5 integers in it, with the last unused if the mesh is not indexed.

Each of the values in the buffer correspond to these options:

```text
Indexed:
  0 - indexCount;
  1 - instanceCount;
  2 - firstIndex;
  3 - vertexOffset;
  4 - firstInstance;
Non-indexed:
  0 - vertexCount;
  1 - instanceCount;
  2 - firstVertex;
  3 - firstInstance;
  4 - unused;
```

---

[AABB](class_aabb.md#class-aabb) **multimesh_get_custom_aabb**(multimesh: [RID](class_rid.md#class-rid))

Returns the custom AABB defined for this MultiMesh resource.

---

[int](class_int.md#class-int) **multimesh_get_instance_count**(multimesh: [RID](class_rid.md#class-rid))

Returns the number of instances allocated for this multimesh.

---

[RID](class_rid.md#class-rid) **multimesh_get_mesh**(multimesh: [RID](class_rid.md#class-rid))

Returns the RID of the mesh that will be used in drawing this multimesh.

---

[int](class_int.md#class-int) **multimesh_get_visible_instances**(multimesh: [RID](class_rid.md#class-rid))

Returns the number of visible instances for this multimesh.

---

[Color](class_color.md#class-color) **multimesh_instance_get_color**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the color by which the specified instance will be modulated.

---

[Color](class_color.md#class-color) **multimesh_instance_get_custom_data**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the custom data associated with the specified instance.

---

[Transform3D](class_transform3d.md#class-transform3d) **multimesh_instance_get_transform**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the [Transform3D](class_transform3d.md#class-transform3d) of the specified instance.

---

[Transform2D](class_transform2d.md#class-transform2d) **multimesh_instance_get_transform_2d**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the [Transform2D](class_transform2d.md#class-transform2d) of the specified instance. For use when the multimesh is set to use 2D transforms.

---

 **multimesh_instance_reset_physics_interpolation**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Prevents physics interpolation for the specified instance during the current physics tick.

This is useful when moving an instance to a new location, to give an instantaneous change rather than interpolation from the previous location.

---

 **multimesh_instance_set_color**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), color: [Color](class_color.md#class-color))

Sets the color by which this instance will be modulated. Equivalent to [MultiMesh.set_instance_color()](class_multimesh.md#class-multimesh-method-set-instance-color).

---

 **multimesh_instance_set_custom_data**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), custom_data: [Color](class_color.md#class-color))

Sets the custom data for this instance. Custom data is passed as a [Color](class_color.md#class-color), but is interpreted as a `vec4` in the shader. Equivalent to [MultiMesh.set_instance_custom_data()](class_multimesh.md#class-multimesh-method-set-instance-custom-data).

---

 **multimesh_instance_set_transform**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))

Sets the [Transform3D](class_transform3d.md#class-transform3d) for this instance. Equivalent to [MultiMesh.set_instance_transform()](class_multimesh.md#class-multimesh-method-set-instance-transform).

---

 **multimesh_instance_set_transform_2d**(multimesh: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the [Transform2D](class_transform2d.md#class-transform2d) for this instance. For use when multimesh is used in 2D. Equivalent to [MultiMesh.set_instance_transform_2d()](class_multimesh.md#class-multimesh-method-set-instance-transform-2d).

---

 **multimesh_instances_reset_physics_interpolation**(multimesh: [RID](class_rid.md#class-rid))

Prevents physics interpolation for all instances during the current physics tick.

This is useful when moving all instances to new locations, to give instantaneous changes rather than interpolation from the previous locations.

---

 **multimesh_set_buffer**(multimesh: [RID](class_rid.md#class-rid), buffer: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Set the entire data to use for drawing the `multimesh` at once to `buffer` (such as instance transforms and colors). `buffer`'s size must match the number of instances multiplied by the per-instance data size (which depends on the enabled MultiMesh fields). Otherwise, an error message is printed and nothing is rendered. See also multimesh_get_buffer().

The per-instance data size and expected data order is:

```text
2D:
  - Position: 8 floats (8 floats for Transform2D)
  - Position + Vertex color: 12 floats (8 floats for Transform2D, 4 floats for Color)
  - Position + Custom data: 12 floats (8 floats for Transform2D, 4 floats of custom data)
  - Position + Vertex color + Custom data: 16 floats (8 floats for Transform2D, 4 floats for Color, 4 floats of custom data)
3D:
  - Position: 12 floats (12 floats for Transform3D)
  - Position + Vertex color: 16 floats (12 floats for Transform3D, 4 floats for Color)
  - Position + Custom data: 16 floats (12 floats for Transform3D, 4 floats of custom data)
  - Position + Vertex color + Custom data: 20 floats (12 floats for Transform3D, 4 floats for Color, 4 floats of custom data)
```

Instance transforms are in row-major order. Specifically:

- For [Transform2D](class_transform2d.md#class-transform2d) the float-order is: `(x.x, y.x, padding_float, origin.x, x.y, y.y, padding_float, origin.y)`.
- For [Transform3D](class_transform3d.md#class-transform3d) the float-order is: `(basis.x.x, basis.y.x, basis.z.x, origin.x, basis.x.y, basis.y.y, basis.z.y, origin.y, basis.x.z, basis.y.z, basis.z.z, origin.z)`.

---

 **multimesh_set_buffer_interpolated**(multimesh: [RID](class_rid.md#class-rid), buffer: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array), buffer_previous: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Alternative version of multimesh_set_buffer() for use with physics interpolation.

Takes both an array of current data and an array of data for the previous physics tick.

---

 **multimesh_set_custom_aabb**(multimesh: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))

Sets the custom AABB for this MultiMesh resource.

---

 **multimesh_set_mesh**(multimesh: [RID](class_rid.md#class-rid), mesh: [RID](class_rid.md#class-rid))

Sets the mesh to be drawn by the multimesh. Equivalent to [MultiMesh.mesh](class_multimesh.md#class-multimesh-property-mesh).

---

 **multimesh_set_physics_interpolated**(multimesh: [RID](class_rid.md#class-rid), interpolated: [bool](class_bool.md#class-bool))

Turns on and off physics interpolation for this MultiMesh resource.

---

 **multimesh_set_physics_interpolation_quality**(multimesh: [RID](class_rid.md#class-rid), quality: MultimeshPhysicsInterpolationQuality)

Sets the physics interpolation quality for the [MultiMesh](class_multimesh.md#class-multimesh).

A value of MULTIMESH_INTERP_QUALITY_FAST gives fast but low quality interpolation, a value of MULTIMESH_INTERP_QUALITY_HIGH gives slower but higher quality interpolation.

---

 **multimesh_set_visible_instances**(multimesh: [RID](class_rid.md#class-rid), visible: [int](class_int.md#class-int))

Sets the number of instances visible at a given time. If -1, all instances that have been allocated are drawn. Equivalent to [MultiMesh.visible_instance_count](class_multimesh.md#class-multimesh-property-visible-instance-count).

---

[RID](class_rid.md#class-rid) **occluder_create**()

Creates an occluder instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `occluder_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [Occluder3D](class_occluder3d.md#class-occluder3d) (not to be confused with the [OccluderInstance3D](class_occluderinstance3d.md#class-occluderinstance3d) node).

---

 **occluder_set_mesh**(occluder: [RID](class_rid.md#class-rid), vertices: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), indices: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Sets the mesh data for the given occluder RID, which controls the shape of the occlusion culling that will be performed.

---

[RID](class_rid.md#class-rid) **omni_light_create**()

Creates a new omni light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this omni light to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent node is [OmniLight3D](class_omnilight3d.md#class-omnilight3d).

---

[RID](class_rid.md#class-rid) **particles_collision_create**()

Creates a new 3D GPU particle collision or attractor and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `particles_collision_*` RenderingServer functions.

**Note:** The equivalent nodes are [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d) and [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d).

---

 **particles_collision_height_field_update**(particles_collision: [RID](class_rid.md#class-rid))

Requests an update for the 3D GPU particle collision heightfield. This may be automatically called by the 3D GPU particle collision heightfield depending on its [GPUParticlesCollisionHeightField3D.update_mode](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d-property-update-mode).

---

 **particles_collision_set_attractor_attenuation**(particles_collision: [RID](class_rid.md#class-rid), curve: [float](class_float.md#class-float))

Sets the attenuation `curve` for the 3D GPU particles attractor specified by the `particles_collision` RID. Only used for attractors, not colliders. Equivalent to [GPUParticlesAttractor3D.attenuation](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-attenuation).

---

 **particles_collision_set_attractor_directionality**(particles_collision: [RID](class_rid.md#class-rid), amount: [float](class_float.md#class-float))

Sets the directionality `amount` for the 3D GPU particles attractor specified by the `particles_collision` RID. Only used for attractors, not colliders. Equivalent to [GPUParticlesAttractor3D.directionality](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-directionality).

---

 **particles_collision_set_attractor_strength**(particles_collision: [RID](class_rid.md#class-rid), strength: [float](class_float.md#class-float))

Sets the `strength` for the 3D GPU particles attractor specified by the `particles_collision` RID. Only used for attractors, not colliders. Equivalent to [GPUParticlesAttractor3D.strength](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-strength).

---

 **particles_collision_set_box_extents**(particles_collision: [RID](class_rid.md#class-rid), extents: [Vector3](class_vector3.md#class-vector3))

Sets the `extents` for the 3D GPU particles collision by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionBox3D.size](class_gpuparticlescollisionbox3d.md#class-gpuparticlescollisionbox3d-property-size), [GPUParticlesCollisionSDF3D.size](class_gpuparticlescollisionsdf3d.md#class-gpuparticlescollisionsdf3d-property-size), [GPUParticlesCollisionHeightField3D.size](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d-property-size), [GPUParticlesAttractorBox3D.size](class_gpuparticlesattractorbox3d.md#class-gpuparticlesattractorbox3d-property-size) or [GPUParticlesAttractorVectorField3D.size](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d-property-size) depending on the `particles_collision` type.

---

 **particles_collision_set_collision_type**(particles_collision: [RID](class_rid.md#class-rid), type: ParticlesCollisionType)

Sets the collision or attractor shape `type` for the 3D GPU particles collision or attractor specified by the `particles_collision` RID.

---

 **particles_collision_set_cull_mask**(particles_collision: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Sets the cull `mask` for the 3D GPU particles collision or attractor specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollision3D.cull_mask](class_gpuparticlescollision3d.md#class-gpuparticlescollision3d-property-cull-mask) or [GPUParticlesAttractor3D.cull_mask](class_gpuparticlesattractor3d.md#class-gpuparticlesattractor3d-property-cull-mask) depending on the `particles_collision` type.

---

 **particles_collision_set_field_texture**(particles_collision: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))

Sets the signed distance field `texture` for the 3D GPU particles collision specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionSDF3D.texture](class_gpuparticlescollisionsdf3d.md#class-gpuparticlescollisionsdf3d-property-texture) or [GPUParticlesAttractorVectorField3D.texture](class_gpuparticlesattractorvectorfield3d.md#class-gpuparticlesattractorvectorfield3d-property-texture) depending on the `particles_collision` type.

---

 **particles_collision_set_height_field_mask**(particles_collision: [RID](class_rid.md#class-rid), mask: [int](class_int.md#class-int))

Sets the heightfield `mask` for the 3D GPU particles heightfield collision specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionHeightField3D.heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d-property-heightfield-mask).

---

 **particles_collision_set_height_field_resolution**(particles_collision: [RID](class_rid.md#class-rid), resolution: ParticlesCollisionHeightfieldResolution)

Sets the heightmap `resolution` for the 3D GPU particles heightfield collision specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionHeightField3D.resolution](class_gpuparticlescollisionheightfield3d.md#class-gpuparticlescollisionheightfield3d-property-resolution).

---

 **particles_collision_set_sphere_radius**(particles_collision: [RID](class_rid.md#class-rid), radius: [float](class_float.md#class-float))

Sets the `radius` for the 3D GPU particles sphere collision or attractor specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionSphere3D.radius](class_gpuparticlescollisionsphere3d.md#class-gpuparticlescollisionsphere3d-property-radius) or [GPUParticlesAttractorSphere3D.radius](class_gpuparticlesattractorsphere3d.md#class-gpuparticlesattractorsphere3d-property-radius) depending on the `particles_collision` type.

---

[RID](class_rid.md#class-rid) **particles_create**()

Creates a GPU-based particle system and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `particles_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach these particles to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent nodes are [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) and [GPUParticles3D](class_gpuparticles3d.md#class-gpuparticles3d).

**Note:** All `particles_*` methods only apply to GPU-based particles, not CPU-based particles. [CPUParticles2D](class_cpuparticles2d.md#class-cpuparticles2d) and [CPUParticles3D](class_cpuparticles3d.md#class-cpuparticles3d) do not have equivalent RenderingServer functions available, as these use [MultiMeshInstance2D](class_multimeshinstance2d.md#class-multimeshinstance2d) and [MultiMeshInstance3D](class_multimeshinstance3d.md#class-multimeshinstance3d) under the hood (see `multimesh_*` methods).

---

 **particles_emit**(particles: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d), velocity: [Vector3](class_vector3.md#class-vector3), color: [Color](class_color.md#class-color), custom: [Color](class_color.md#class-color), emit_flags: [int](class_int.md#class-int))

Manually emits particles from the `particles` instance.

---

[AABB](class_aabb.md#class-aabb) **particles_get_current_aabb**(particles: [RID](class_rid.md#class-rid))

Calculates and returns the axis-aligned bounding box that contains all the particles. Equivalent to [GPUParticles3D.capture_aabb()](class_gpuparticles3d.md#class-gpuparticles3d-method-capture-aabb).

---

[bool](class_bool.md#class-bool) **particles_get_emitting**(particles: [RID](class_rid.md#class-rid))

Returns `true` if particles are currently set to emitting.

---

[bool](class_bool.md#class-bool) **particles_is_inactive**(particles: [RID](class_rid.md#class-rid))

Returns `true` if particles are not emitting and particles are set to inactive.

---

 **particles_request_process**(particles: [RID](class_rid.md#class-rid))

Add particle system to list of particle systems that need to be updated. Update will take place on the next frame, or on the next call to instances_cull_aabb(), instances_cull_convex(), or instances_cull_ray().

---

 **particles_request_process_time**(particles: [RID](class_rid.md#class-rid), process_time: [float](class_float.md#class-float), process_time_residual: [float](class_float.md#class-float) = 0.0)

Requests the particles to process for extra process time during a single frame.

`process_time` defines the time that the particles will process while emitting is on. `process_time_residual` defines the time that particles will process with emitting turned off for the simulation. When combined with the particles' speed scale set to `0.0`, this is useful to be able to seek a particle system timeline.

---

 **particles_restart**(particles: [RID](class_rid.md#class-rid))

Reset the particles on the next update. Equivalent to [GPUParticles3D.restart()](class_gpuparticles3d.md#class-gpuparticles3d-method-restart).

---

 **particles_set_amount**(particles: [RID](class_rid.md#class-rid), amount: [int](class_int.md#class-int))

Sets the number of particles to be drawn and allocates the memory for them. Equivalent to [GPUParticles3D.amount](class_gpuparticles3d.md#class-gpuparticles3d-property-amount).

---

 **particles_set_amount_ratio**(particles: [RID](class_rid.md#class-rid), ratio: [float](class_float.md#class-float))

Sets the amount ratio for particles to be emitted. Equivalent to [GPUParticles3D.amount_ratio](class_gpuparticles3d.md#class-gpuparticles3d-property-amount-ratio).

---

 **particles_set_collision_base_size**(particles: [RID](class_rid.md#class-rid), size: [float](class_float.md#class-float))

Sets the base size for particle collision. Equivalent to [GPUParticles3D.collision_base_size](class_gpuparticles3d.md#class-gpuparticles3d-property-collision-base-size).

---

 **particles_set_custom_aabb**(particles: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))

Sets a custom axis-aligned bounding box for the particle system. Equivalent to [GPUParticles3D.visibility_aabb](class_gpuparticles3d.md#class-gpuparticles3d-property-visibility-aabb).

---

 **particles_set_draw_order**(particles: [RID](class_rid.md#class-rid), order: ParticlesDrawOrder)

Sets the draw order of the particles. Equivalent to [GPUParticles3D.draw_order](class_gpuparticles3d.md#class-gpuparticles3d-property-draw-order).

---

 **particles_set_draw_pass_mesh**(particles: [RID](class_rid.md#class-rid), pass: [int](class_int.md#class-int), mesh: [RID](class_rid.md#class-rid))

Sets the mesh to be used for the specified draw pass. Equivalent to [GPUParticles3D.draw_pass_1](class_gpuparticles3d.md#class-gpuparticles3d-property-draw-pass-1), [GPUParticles3D.draw_pass_2](class_gpuparticles3d.md#class-gpuparticles3d-property-draw-pass-2), [GPUParticles3D.draw_pass_3](class_gpuparticles3d.md#class-gpuparticles3d-property-draw-pass-3), and [GPUParticles3D.draw_pass_4](class_gpuparticles3d.md#class-gpuparticles3d-property-draw-pass-4).

---

 **particles_set_draw_passes**(particles: [RID](class_rid.md#class-rid), count: [int](class_int.md#class-int))

Sets the number of draw passes to use. Equivalent to [GPUParticles3D.draw_passes](class_gpuparticles3d.md#class-gpuparticles3d-property-draw-passes).

---

 **particles_set_emission_transform**(particles: [RID](class_rid.md#class-rid), transform: [Transform3D](class_transform3d.md#class-transform3d))

Sets the [Transform3D](class_transform3d.md#class-transform3d) that will be used by the particles when they first emit.

---

 **particles_set_emitter_velocity**(particles: [RID](class_rid.md#class-rid), velocity: [Vector3](class_vector3.md#class-vector3))

Sets the velocity of a particle node, that will be used by [ParticleProcessMaterial.inherit_velocity_ratio](class_particleprocessmaterial.md#class-particleprocessmaterial-property-inherit-velocity-ratio).

---

 **particles_set_emitting**(particles: [RID](class_rid.md#class-rid), emitting: [bool](class_bool.md#class-bool))

If `true`, particles will emit over time. Setting to `false` does not reset the particles, but only stops their emission. Equivalent to [GPUParticles3D.emitting](class_gpuparticles3d.md#class-gpuparticles3d-property-emitting).

---

 **particles_set_explosiveness_ratio**(particles: [RID](class_rid.md#class-rid), ratio: [float](class_float.md#class-float))

Sets the explosiveness ratio. Equivalent to [GPUParticles3D.explosiveness](class_gpuparticles3d.md#class-gpuparticles3d-property-explosiveness).

---

 **particles_set_fixed_fps**(particles: [RID](class_rid.md#class-rid), fps: [int](class_int.md#class-int))

Sets the frame rate that the particle system rendering will be fixed to. Equivalent to [GPUParticles3D.fixed_fps](class_gpuparticles3d.md#class-gpuparticles3d-property-fixed-fps).

---

 **particles_set_fractional_delta**(particles: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, uses fractional delta which smooths the movement of the particles. Equivalent to [GPUParticles3D.fract_delta](class_gpuparticles3d.md#class-gpuparticles3d-property-fract-delta).

---

 **particles_set_interp_to_end**(particles: [RID](class_rid.md#class-rid), factor: [float](class_float.md#class-float))

Sets the value that informs a [ParticleProcessMaterial](class_particleprocessmaterial.md#class-particleprocessmaterial) to rush all particles towards the end of their lifetime.

---

 **particles_set_interpolate**(particles: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Sets whether particles should use interpolation between fixed steps. Equivalent to [GPUParticles3D.interpolate](class_gpuparticles3d.md#class-gpuparticles3d-property-interpolate).

---

 **particles_set_lifetime**(particles: [RID](class_rid.md#class-rid), lifetime: [float](class_float.md#class-float))

Sets the lifetime of each particle in the system. Equivalent to [GPUParticles3D.lifetime](class_gpuparticles3d.md#class-gpuparticles3d-property-lifetime).

---

 **particles_set_mode**(particles: [RID](class_rid.md#class-rid), mode: ParticlesMode)

Sets whether the GPU particles specified by the `particles` RID should be rendered in 2D or 3D according to `mode`.

---

 **particles_set_one_shot**(particles: [RID](class_rid.md#class-rid), one_shot: [bool](class_bool.md#class-bool))

If `true`, particles will emit once and then stop. Equivalent to [GPUParticles3D.one_shot](class_gpuparticles3d.md#class-gpuparticles3d-property-one-shot).

---

 **particles_set_pre_process_time**(particles: [RID](class_rid.md#class-rid), time: [float](class_float.md#class-float))

Sets the preprocess time for the particles' animation. This lets you delay starting an animation until after the particles have begun emitting. Equivalent to [GPUParticles3D.preprocess](class_gpuparticles3d.md#class-gpuparticles3d-property-preprocess).

---

 **particles_set_process_material**(particles: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))

Sets the material for processing the particles.

**Note:** This is not the material used to draw the materials. Equivalent to [GPUParticles3D.process_material](class_gpuparticles3d.md#class-gpuparticles3d-property-process-material).

---

 **particles_set_randomness_ratio**(particles: [RID](class_rid.md#class-rid), ratio: [float](class_float.md#class-float))

Sets the emission randomness ratio. This randomizes the emission of particles within their phase. Equivalent to [GPUParticles3D.randomness](class_gpuparticles3d.md#class-gpuparticles3d-property-randomness).

---

 **particles_set_speed_scale**(particles: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))

Sets the speed scale of the particle system. Equivalent to [GPUParticles3D.speed_scale](class_gpuparticles3d.md#class-gpuparticles3d-property-speed-scale).

---

 **particles_set_subemitter**(particles: [RID](class_rid.md#class-rid), subemitter_particles: [RID](class_rid.md#class-rid))

Sets the subemitter particles for the particle system. Equivalent to [GPUParticles3D.sub_emitter](class_gpuparticles3d.md#class-gpuparticles3d-property-sub-emitter).

---

 **particles_set_trail_bind_poses**(particles: [RID](class_rid.md#class-rid), bind_poses: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)])

Sets the trail bind poses for the particle system. This specified as an array of [Transform3D](class_transform3d.md#class-transform3d)s representing the bind pose for each draw pass. See [GPUParticles3D.draw_skin](class_gpuparticles3d.md#class-gpuparticles3d-property-draw-skin), [Skin.get_bind_count()](class_skin.md#class-skin-method-get-bind-count), and [Skin.get_bind_pose()](class_skin.md#class-skin-method-get-bind-pose). Set the value for each draw pass to [Transform3D.IDENTITY](class_transform3d.md#class-transform3d-constant-identity) to use the default behavior, which is what built-in trails use ([RibbonTrailMesh](class_ribbontrailmesh.md#class-ribbontrailmesh) and [TubeTrailMesh](class_tubetrailmesh.md#class-tubetrailmesh)).

---

 **particles_set_trails**(particles: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool), length_sec: [float](class_float.md#class-float))

If `enable` is `true`, enables trails for the `particles` with the specified `length_sec` in seconds. Equivalent to [GPUParticles3D.trail_enabled](class_gpuparticles3d.md#class-gpuparticles3d-property-trail-enabled) and [GPUParticles3D.trail_lifetime](class_gpuparticles3d.md#class-gpuparticles3d-property-trail-lifetime).

---

 **particles_set_transform_align**(particles: [RID](class_rid.md#class-rid), align: ParticlesTransformAlign)

Sets the transform alignment for the particle system. Equivalent to [GPUParticles3D.transform_align](class_gpuparticles3d.md#class-gpuparticles3d-property-transform-align).

---

 **particles_set_transform_align_axis**(particles: [RID](class_rid.md#class-rid), rotation_axis: ParticlesTransformAlignAxis)

Sets which axis to use for transform alignment.

---

 **particles_set_transform_align_channel_filter**(particles: [RID](class_rid.md#class-rid), channel_filter: ParticlesTransformAlignCustomSrc)

When using Z-Billboarding, which CUSTOM channel to read from.

---

 **particles_set_use_local_coordinates**(particles: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, particles use local coordinates. If `false` they use global coordinates. Equivalent to [GPUParticles3D.local_coords](class_gpuparticles3d.md#class-gpuparticles3d-property-local-coords).

---

 **positional_soft_shadow_filter_set_quality**(quality: ShadowQuality)

Sets the filter quality for omni and spot light shadows in 3D. See also [ProjectSettings.rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality](class_projectsettings.md#class-projectsettings-property-rendering-lights-and-shadows-positional-shadow-soft-shadow-filter-quality). This parameter is global and cannot be set on a per-viewport basis.

---

[RID](class_rid.md#class-rid) **reflection_probe_create**()

Creates a reflection probe and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `reflection_probe_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this reflection probe to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent node is [ReflectionProbe](class_reflectionprobe.md#class-reflectionprobe).

---

 **reflection_probe_set_ambient_color**(probe: [RID](class_rid.md#class-rid), color: [Color](class_color.md#class-color))

Sets the reflection probe's custom ambient light color. Equivalent to [ReflectionProbe.ambient_color](class_reflectionprobe.md#class-reflectionprobe-property-ambient-color).

---

 **reflection_probe_set_ambient_energy**(probe: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float))

Sets the reflection probe's custom ambient light energy. Equivalent to [ReflectionProbe.ambient_color_energy](class_reflectionprobe.md#class-reflectionprobe-property-ambient-color-energy).

---

 **reflection_probe_set_ambient_mode**(probe: [RID](class_rid.md#class-rid), mode: ReflectionProbeAmbientMode)

Sets the reflection probe's ambient light mode. Equivalent to [ReflectionProbe.ambient_mode](class_reflectionprobe.md#class-reflectionprobe-property-ambient-mode).

---

 **reflection_probe_set_as_interior**(probe: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, reflections will ignore sky contribution. Equivalent to [ReflectionProbe.interior](class_reflectionprobe.md#class-reflectionprobe-property-interior).

---

 **reflection_probe_set_blend_distance**(probe: [RID](class_rid.md#class-rid), blend_distance: [float](class_float.md#class-float))

Sets the distance in meters over which a probe blends into the scene.

---

 **reflection_probe_set_cull_mask**(probe: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))

Sets the render cull mask for this reflection probe. Only instances with a matching layer will be reflected by this probe. Equivalent to [ReflectionProbe.cull_mask](class_reflectionprobe.md#class-reflectionprobe-property-cull-mask).

---

 **reflection_probe_set_enable_box_projection**(probe: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, uses box projection. This can make reflections look more correct in certain situations. Equivalent to [ReflectionProbe.box_projection](class_reflectionprobe.md#class-reflectionprobe-property-box-projection).

---

 **reflection_probe_set_enable_shadows**(probe: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, computes shadows in the reflection probe. This makes the reflection much slower to compute. Equivalent to [ReflectionProbe.enable_shadows](class_reflectionprobe.md#class-reflectionprobe-property-enable-shadows).

---

 **reflection_probe_set_intensity**(probe: [RID](class_rid.md#class-rid), intensity: [float](class_float.md#class-float))

Sets the intensity of the reflection probe. Intensity modulates the strength of the reflection. Equivalent to [ReflectionProbe.intensity](class_reflectionprobe.md#class-reflectionprobe-property-intensity).

---

 **reflection_probe_set_max_distance**(probe: [RID](class_rid.md#class-rid), distance: [float](class_float.md#class-float))

Sets the max distance away from the probe an object can be before it is culled. Equivalent to [ReflectionProbe.max_distance](class_reflectionprobe.md#class-reflectionprobe-property-max-distance).

---

 **reflection_probe_set_mesh_lod_threshold**(probe: [RID](class_rid.md#class-rid), pixels: [float](class_float.md#class-float))

Sets the mesh level of detail to use in the reflection probe rendering. Higher values will use less detailed versions of meshes that have LOD variations generated, which can improve performance. Equivalent to [ReflectionProbe.mesh_lod_threshold](class_reflectionprobe.md#class-reflectionprobe-property-mesh-lod-threshold).

---

 **reflection_probe_set_origin_offset**(probe: [RID](class_rid.md#class-rid), offset: [Vector3](class_vector3.md#class-vector3))

Sets the origin offset to be used when this reflection probe is in box project mode. Equivalent to [ReflectionProbe.origin_offset](class_reflectionprobe.md#class-reflectionprobe-property-origin-offset).

---

 **reflection_probe_set_reflection_mask**(probe: [RID](class_rid.md#class-rid), layers: [int](class_int.md#class-int))

Sets the render reflection mask for this reflection probe. Only instances with a matching layer will have reflections applied from this probe. Equivalent to [ReflectionProbe.reflection_mask](class_reflectionprobe.md#class-reflectionprobe-property-reflection-mask).

---

 **reflection_probe_set_resolution**(probe: [RID](class_rid.md#class-rid), resolution: [int](class_int.md#class-int))

**Deprecated:** This method has not done anything since Godot 3.

Deprecated. This method does nothing.

---

 **reflection_probe_set_size**(probe: [RID](class_rid.md#class-rid), size: [Vector3](class_vector3.md#class-vector3))

Sets the size of the area that the reflection probe will capture. Equivalent to [ReflectionProbe.size](class_reflectionprobe.md#class-reflectionprobe-property-size).

---

 **reflection_probe_set_update_mode**(probe: [RID](class_rid.md#class-rid), mode: ReflectionProbeUpdateMode)

Sets how often the reflection probe updates. Can either be once or every frame.

---

 **request_frame_drawn_callback**(callable: [Callable](class_callable.md#class-callable))

Schedules a callback to the given callable after a frame has been drawn.

---

[RID](class_rid.md#class-rid) **scenario_create**()

Creates a scenario and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `scenario_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

The scenario is the 3D world that all the visual instances exist in.

---

 **scenario_set_camera_attributes**(scenario: [RID](class_rid.md#class-rid), effects: [RID](class_rid.md#class-rid))

Sets the camera attributes (`effects`) that will be used with this scenario. See also [CameraAttributes](class_cameraattributes.md#class-cameraattributes).

---

 **scenario_set_compositor**(scenario: [RID](class_rid.md#class-rid), compositor: [RID](class_rid.md#class-rid))

Sets the compositor (`compositor`) that will be used with this scenario. See also [Compositor](class_compositor.md#class-compositor).

---

 **scenario_set_environment**(scenario: [RID](class_rid.md#class-rid), environment: [RID](class_rid.md#class-rid))

Sets the environment that will be used with this scenario. See also [Environment](class_environment.md#class-environment).

---

 **scenario_set_fallback_environment**(scenario: [RID](class_rid.md#class-rid), environment: [RID](class_rid.md#class-rid))

Sets the fallback environment to be used by this scenario. The fallback environment is used if no environment is set. Internally, this is used by the editor to provide a default environment.

---

 **screen_space_roughness_limiter_set_active**(enable: [bool](class_bool.md#class-bool), amount: [float](class_float.md#class-float), limit: [float](class_float.md#class-float))

Sets the screen-space roughness limiter parameters, such as whether it should be enabled and its thresholds. Equivalent to [ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/enabled](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-screen-space-roughness-limiter-enabled), [ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/amount](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-screen-space-roughness-limiter-amount) and [ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/limit](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-screen-space-roughness-limiter-limit).

---

 **set_boot_image**(image: [Image](class_image.md#class-image), color: [Color](class_color.md#class-color), scale: [bool](class_bool.md#class-bool), use_filter: [bool](class_bool.md#class-bool) = true)

**Deprecated:** Use set_boot_image_with_stretch() instead.

Sets a boot image. The `color` defines the background color. The value of `scale` indicates if the image will be scaled to fit the screen size. If `use_filter` is `true`, the image will be scaled with linear interpolation. If `use_filter` is `false`, the image will be scaled with nearest-neighbor interpolation.

---

 **set_boot_image_with_stretch**(image: [Image](class_image.md#class-image), color: [Color](class_color.md#class-color), stretch_mode: SplashStretchMode, use_filter: [bool](class_bool.md#class-bool) = true)

Sets a boot image. The `color` defines the background color. The value of `stretch_mode` indicates how the image will be stretched (see SplashStretchMode for possible values). If `use_filter` is `true`, the image will be scaled with linear interpolation. If `use_filter` is `false`, the image will be scaled with nearest-neighbor interpolation.

---

 **set_debug_generate_wireframes**(generate: [bool](class_bool.md#class-bool))

If `generate` is `true`, generates debug wireframes for all meshes that are loaded when using the Compatibility renderer. By default, the engine does not generate debug wireframes at runtime, since they slow down loading of assets and take up VRAM.

**Note:** You must call this method before loading any meshes when using the Compatibility renderer. Otherwise, wireframes will not be used.

---

 **set_default_clear_color**(color: [Color](class_color.md#class-color))

Sets the default clear color which is used when a specific clear color has not been selected. See also get_default_clear_color().

---

[RID](class_rid.md#class-rid) **shader_create**()

Creates an empty shader and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `shader_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [Shader](class_shader.md#class-shader).

---

[String](class_string.md#class-string) **shader_get_code**(shader: [RID](class_rid.md#class-rid))

Returns a shader's source code as a string.

---

[RID](class_rid.md#class-rid) **shader_get_default_texture_parameter**(shader: [RID](class_rid.md#class-rid), name: [StringName](class_stringname.md#class-stringname), index: [int](class_int.md#class-int) = 0)

Returns a default texture from a shader searched by name.

**Note:** If the sampler array is used use `index` to access the specified texture.

---

[Variant](class_variant.md#class-variant) **shader_get_parameter_default**(shader: [RID](class_rid.md#class-rid), name: [StringName](class_stringname.md#class-stringname))

Returns the default value for the specified shader uniform. This is usually the value written in the shader source code.

---

 **shader_set_code**(shader: [RID](class_rid.md#class-rid), code: [String](class_string.md#class-string))

Sets the shader's source code (which triggers recompilation after being changed).

---

 **shader_set_default_texture_parameter**(shader: [RID](class_rid.md#class-rid), name: [StringName](class_stringname.md#class-stringname), texture: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int) = 0)

Sets a shader's default texture. Overwrites the texture given by name.

**Note:** If the sampler array is used use `index` to access the specified texture.

---

 **shader_set_path_hint**(shader: [RID](class_rid.md#class-rid), path: [String](class_string.md#class-string))

Sets the path hint for the specified shader. This should generally match the [Shader](class_shader.md#class-shader) resource's [Resource.resource_path](class_resource.md#class-resource-property-resource-path).

---

 **skeleton_allocate_data**(skeleton: [RID](class_rid.md#class-rid), bones: [int](class_int.md#class-int), is_2d_skeleton: [bool](class_bool.md#class-bool) = false)

Allocates data for this skeleton using the number of bones specified in `bones`. If `is_2d_skeleton` is `true`, the skeleton will be treated as a 2D skeleton instead of a 3D skeleton. See also skeleton_get_bone_count().

---

[Transform3D](class_transform3d.md#class-transform3d) **skeleton_bone_get_transform**(skeleton: [RID](class_rid.md#class-rid), bone: [int](class_int.md#class-int))

Returns the [Transform3D](class_transform3d.md#class-transform3d) set for a specific bone of this skeleton.

---

[Transform2D](class_transform2d.md#class-transform2d) **skeleton_bone_get_transform_2d**(skeleton: [RID](class_rid.md#class-rid), bone: [int](class_int.md#class-int))

Returns the [Transform2D](class_transform2d.md#class-transform2d) set for a specific bone of this skeleton.

---

 **skeleton_bone_set_transform**(skeleton: [RID](class_rid.md#class-rid), bone: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))

Sets the [Transform3D](class_transform3d.md#class-transform3d) for a specific bone of this skeleton.

---

 **skeleton_bone_set_transform_2d**(skeleton: [RID](class_rid.md#class-rid), bone: [int](class_int.md#class-int), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the [Transform2D](class_transform2d.md#class-transform2d) for a specific bone of this skeleton.

---

[RID](class_rid.md#class-rid) **skeleton_create**()

Creates a skeleton and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `skeleton_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

---

[int](class_int.md#class-int) **skeleton_get_bone_count**(skeleton: [RID](class_rid.md#class-rid))

Returns the number of bones allocated for this skeleton. See also skeleton_allocate_data().

---

 **skeleton_set_base_transform_2d**(skeleton: [RID](class_rid.md#class-rid), base_transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the base [Transform2D](class_transform2d.md#class-transform2d) to use for the specified skeleton.

---

[Image](class_image.md#class-image) **sky_bake_panorama**(sky: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float), bake_irradiance: [bool](class_bool.md#class-bool), size: [Vector2i](class_vector2i.md#class-vector2i))

Generates and returns an [Image](class_image.md#class-image) containing the radiance map for the specified `sky` RID. This supports built-in sky material and custom sky shaders. If `bake_irradiance` is `true`, the irradiance map is saved instead of the radiance map. The radiance map is used to render reflected light, while the irradiance map is used to render ambient light. See also environment_bake_panorama().

**Note:** The image is saved using linear encoding without any tonemapping performed, which means it will look too dark if viewed directly in an image editor. `energy` values above `1.0` can be used to brighten the resulting image.

**Note:** `size` should be a 2:1 aspect ratio for the generated panorama to have square pixels. For radiance maps, there is no point in using a height greater than [Sky.radiance_size](class_sky.md#class-sky-property-radiance-size), as it won't increase detail. Irradiance maps only contain low-frequency data, so there is usually no point in going past a size of 128×64 pixels when saving an irradiance map.

---

[RID](class_rid.md#class-rid) **sky_create**()

Creates an empty sky and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `sky_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

---

 **sky_set_material**(sky: [RID](class_rid.md#class-rid), material: [RID](class_rid.md#class-rid))

Sets the material that the sky uses to render the background, ambient and reflection maps.

---

 **sky_set_mode**(sky: [RID](class_rid.md#class-rid), mode: SkyMode)

Sets the process `mode` of the sky specified by the `sky` RID. Equivalent to [Sky.process_mode](class_sky.md#class-sky-property-process-mode).

---

 **sky_set_radiance_size**(sky: [RID](class_rid.md#class-rid), radiance_size: [int](class_int.md#class-int))

Sets the `radiance_size` of the sky specified by the `sky` RID (in pixels). Equivalent to [Sky.radiance_size](class_sky.md#class-sky-property-radiance-size).

---

[RID](class_rid.md#class-rid) **spot_light_create**()

Creates a spot light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this spot light to an instance using instance_set_base() using the returned RID.

---

 **sub_surface_scattering_set_quality**(quality: SubSurfaceScatteringQuality)

Sets [ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_quality](class_projectsettings.md#class-projectsettings-property-rendering-environment-subsurface-scattering-subsurface-scattering-quality) to use when rendering materials that have subsurface scattering enabled.

---

 **sub_surface_scattering_set_scale**(scale: [float](class_float.md#class-float), depth_scale: [float](class_float.md#class-float))

Sets the [ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_scale](class_projectsettings.md#class-projectsettings-property-rendering-environment-subsurface-scattering-subsurface-scattering-scale) and [ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale](class_projectsettings.md#class-projectsettings-property-rendering-environment-subsurface-scattering-subsurface-scattering-depth-scale) to use when rendering materials that have subsurface scattering enabled.

---

[RID](class_rid.md#class-rid) **texture_2d_create**(image: [Image](class_image.md#class-image))

Creates a 2-dimensional texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_2d_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [Texture2D](class_texture2d.md#class-texture2d).

**Note:** Not to be confused with [RenderingDevice.texture_create()](class_renderingdevice.md#class-renderingdevice-method-texture-create), which creates the graphics API's own texture type as opposed to the Godot-specific [Texture2D](class_texture2d.md#class-texture2d) resource.

---

[Image](class_image.md#class-image) **texture_2d_get**(texture: [RID](class_rid.md#class-rid))

Returns an [Image](class_image.md#class-image) instance from the given `texture` [RID](class_rid.md#class-rid).

**Example:** Get the test texture from get_test_texture() and apply it to a [Sprite2D](class_sprite2d.md#class-sprite2d) node:

```gdscript
var texture_rid = RenderingServer.get_test_texture()
var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
$Sprite2D.texture = texture
```

---

[Image](class_image.md#class-image) **texture_2d_layer_get**(texture: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int))

Returns an [Image](class_image.md#class-image) instance from the given `texture` [RID](class_rid.md#class-rid) and `layer`.

---

[RID](class_rid.md#class-rid) **texture_2d_layered_create**(layers: [Array](class_array.md#class-array)[[Image](class_image.md#class-image)], layered_type: TextureLayeredType)

Creates a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_2d_layered_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [TextureLayered](class_texturelayered.md#class-texturelayered).

---

[RID](class_rid.md#class-rid) **texture_2d_layered_placeholder_create**(layered_type: TextureLayeredType)

Creates a placeholder for a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_2d_layered_*` RenderingServer functions, although it does nothing when used. See also texture_2d_placeholder_create().

**Note:** The equivalent resource is [PlaceholderTextureLayered](class_placeholdertexturelayered.md#class-placeholdertexturelayered).

---

[RID](class_rid.md#class-rid) **texture_2d_placeholder_create**()

Creates a placeholder for a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_2d_layered_*` RenderingServer functions, although it does nothing when used. See also texture_2d_layered_placeholder_create().

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [PlaceholderTexture2D](class_placeholdertexture2d.md#class-placeholdertexture2d).

---

 **texture_2d_update**(texture: [RID](class_rid.md#class-rid), image: [Image](class_image.md#class-image), layer: [int](class_int.md#class-int))

Updates the texture specified by the `texture` [RID](class_rid.md#class-rid) with the data in `image`. A `layer` must also be specified, which should be `0` when updating a single-layer texture ([Texture2D](class_texture2d.md#class-texture2d)).

**Note:** The `image` must have the same width, height and format as the current `texture` data. Otherwise, an error will be printed and the original texture won't be modified. If you need to use different width, height or format, use texture_replace() instead.

---

[RID](class_rid.md#class-rid) **texture_3d_create**(format: [Format](class_image.md#enum-image-format), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), mipmaps: [bool](class_bool.md#class-bool), data: [Array](class_array.md#class-array)[[Image](class_image.md#class-image)])

**Note:** The equivalent resource is [Texture3D](class_texture3d.md#class-texture3d).

---

[Array](class_array.md#class-array)[[Image](class_image.md#class-image)] **texture_3d_get**(texture: [RID](class_rid.md#class-rid))

Returns 3D texture data as an array of [Image](class_image.md#class-image)s for the specified texture [RID](class_rid.md#class-rid).

---

[RID](class_rid.md#class-rid) **texture_3d_placeholder_create**()

Creates a placeholder for a 3-dimensional texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_3d_*` RenderingServer functions, although it does nothing when used.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [PlaceholderTexture3D](class_placeholdertexture3d.md#class-placeholdertexture3d).

---

 **texture_3d_update**(texture: [RID](class_rid.md#class-rid), data: [Array](class_array.md#class-array)[[Image](class_image.md#class-image)])

Updates the texture specified by the `texture` [RID](class_rid.md#class-rid)'s data with the data in `data`. All the texture's layers must be replaced at once.

**Note:** The `texture` must have the same width, height, depth and format as the current texture data. Otherwise, an error will be printed and the original texture won't be modified. If you need to use different width, height, depth or format, use texture_replace() instead.

---

[RID](class_rid.md#class-rid) **texture_create_from_native_handle**(type: TextureType, format: [Format](class_image.md#enum-image-format), native_handle: [int](class_int.md#class-int), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), layers: [int](class_int.md#class-int) = 1, layered_type: TextureLayeredType = 0)

Creates a texture based on a native handle that was created outside of Godot's renderer.

**Note:** If using only the rendering device renderer, it's recommend to use [RenderingDevice.texture_create_from_extension()](class_renderingdevice.md#class-renderingdevice-method-texture-create-from-extension) together with texture_rd_create(), rather than this method. This way, the texture's format and usage can be controlled more effectively.

---

 **texture_drawable_blit_rect**(textures: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], rect: [Rect2i](class_rect2i.md#class-rect2i), material: [RID](class_rid.md#class-rid), modulate: [Color](class_color.md#class-color), source_textures: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)], to_mipmap: [int](class_int.md#class-int) = 0)

Draws to `rect` on up to 4 given Drawable `textures`, using a TextureBlit Shader from `material`. `modulate` and up to 4 `source_textures` are uniforms for the Shader to process with. `to_mipmap` can specify to perform this draw to a lower mipmap level.

**Note:** All `textures` must be the same size and format.

---

[RID](class_rid.md#class-rid) **texture_drawable_create**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), format: TextureDrawableFormat, color: [Color](class_color.md#class-color) = Color(1, 1, 1, 1), with_mipmaps: [bool](class_bool.md#class-bool) = false)

Creates a 2-dimensional texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_drawable*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent resource is [DrawableTexture2D](class_drawabletexture2d.md#class-drawabletexture2d).

---

 **texture_drawable_generate_mipmaps**(texture: [RID](class_rid.md#class-rid))

Calculates new MipMaps for the given Drawable `texture`.

---

[RID](class_rid.md#class-rid) **texture_drawable_get_default_material**()

Returns a ShaderMaterial with the default texture_blit Shader.

---

[Format](class_image.md#enum-image-format) **texture_get_format**(texture: [RID](class_rid.md#class-rid))

Returns the format for the texture.

---

[int](class_int.md#class-int) **texture_get_native_handle**(texture: [RID](class_rid.md#class-rid), srgb: [bool](class_bool.md#class-bool) = false)

Returns the internal graphics handle for this texture object. For use when communicating with third-party APIs mostly with GDExtension.

`srgb` should be `true` when the texture uses nonlinear sRGB encoding and `false` when the texture uses linear encoding.

**Note:** This function returns a `uint64_t` which internally maps to a `GLuint` (OpenGL) or `VkImage` (Vulkan).

---

[String](class_string.md#class-string) **texture_get_path**(texture: [RID](class_rid.md#class-rid))

Returns the resource path (starting with `res://` or `uid://`) for the specified texture RID. Returns an empty [String](class_string.md#class-string) if the resource is built-in. See also texture_set_path().

---

[RID](class_rid.md#class-rid) **texture_get_rd_texture**(texture: [RID](class_rid.md#class-rid), srgb: [bool](class_bool.md#class-bool) = false)

Returns a texture [RID](class_rid.md#class-rid) that can be used with [RenderingDevice](class_renderingdevice.md#class-renderingdevice).

`srgb` should be `true` when the texture uses nonlinear sRGB encoding and `false` when the texture uses linear encoding.

---

[RID](class_rid.md#class-rid) **texture_proxy_create**(base: [RID](class_rid.md#class-rid))

**Deprecated:** ProxyTexture was removed in Godot 4.

This method does nothing and always returns an invalid [RID](class_rid.md#class-rid).

---

 **texture_proxy_update**(texture: [RID](class_rid.md#class-rid), proxy_to: [RID](class_rid.md#class-rid))

**Deprecated:** ProxyTexture was removed in Godot 4.

This method does nothing.

---

[RID](class_rid.md#class-rid) **texture_rd_create**(rd_texture: [RID](class_rid.md#class-rid), layer_type: TextureLayeredType = 0)

Creates a new texture object based on a texture created directly on the [RenderingDevice](class_renderingdevice.md#class-renderingdevice). If the texture contains layers, `layer_type` is used to define the layer type.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The RenderingServer's free_rid() won't free the underlying `rd_texture`, you will want to free the `rd_texture` using [RenderingDevice.free_rid()](class_renderingdevice.md#class-renderingdevice-method-free-rid).

---

 **texture_replace**(texture: [RID](class_rid.md#class-rid), by_texture: [RID](class_rid.md#class-rid))

Replaces `texture`'s texture data by the texture specified by the `by_texture` RID, without changing `texture`'s RID.

---

 **texture_set_force_redraw_if_visible**(texture: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Sets whether the texture RID should force redrawing when it's visible on screen when [OS.low_processor_usage_mode](class_os.md#class-os-property-low-processor-usage-mode) is `true`. This is used by [AnimatedTexture](class_animatedtexture.md#class-animatedtexture) to force redrawing.

---

 **texture_set_path**(texture: [RID](class_rid.md#class-rid), path: [String](class_string.md#class-string))

Sets the resource path for this texture RID. See also texture_get_path().

**Note:** This is purely a hint and does not cause the texture to be automatically saved when set to a `res://` path.

---

 **texture_set_size_override**(texture: [RID](class_rid.md#class-rid), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int))

Sets the size at which the texture should be *displayed* in 2D, ignoring its original size. This does not rescale the texture data itself, only how it is drawn in 2D. Set `width` and `height` to 0 to disable the size override.

---

 **viewport_attach_camera**(viewport: [RID](class_rid.md#class-rid), camera: [RID](class_rid.md#class-rid))

Sets a viewport's camera.

---

 **viewport_attach_canvas**(viewport: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid))

Sets a viewport's canvas.

---

 **viewport_attach_to_screen**(viewport: [RID](class_rid.md#class-rid), rect: [Rect2](class_rect2.md#class-rect2) = Rect2(0, 0, 0, 0), screen: [int](class_int.md#class-int) = 0)

Copies the viewport to a region of the screen specified by `rect`. If viewport_set_render_direct_to_screen() is `true`, then the viewport does not use a framebuffer and the contents of the viewport are rendered directly to screen. However, note that the root viewport is drawn last, therefore it will draw over the screen. Accordingly, you must set the root viewport to an area that does not cover the area that you have attached this viewport to.

For example, you can set the root viewport to not render at all with the following code:

GDScript

```gdscript
func _ready():
    RenderingServer.viewport_attach_to_screen(get_viewport().get_viewport_rid(), Rect2())
    RenderingServer.viewport_attach_to_screen($Viewport.get_viewport_rid(), Rect2(0, 0, 600, 600))
```

Using this can result in significant optimization, especially on lower-end devices. However, it comes at the cost of having to manage your viewports manually. For further optimization, see viewport_set_render_direct_to_screen().

---

[RID](class_rid.md#class-rid) **viewport_create**()

Creates an empty viewport and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `viewport_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent node is [Viewport](class_viewport.md#class-viewport).

---

[float](class_float.md#class-float) **viewport_get_measured_render_time_cpu**(viewport: [RID](class_rid.md#class-rid))

Returns the CPU time taken to render the last frame in milliseconds. This *only* includes time spent in rendering-related operations; scripts' `_process` functions and other engine subsystems are not included in this readout. To get a complete readout of CPU time spent to render the scene, sum the render times of all viewports that are drawn every frame plus get_frame_setup_time_cpu(). Unlike [Engine.get_frames_per_second()](class_engine.md#class-engine-method-get-frames-per-second), this method will accurately reflect CPU utilization even if framerate is capped via V-Sync or [Engine.max_fps](class_engine.md#class-engine-property-max-fps). See also viewport_get_measured_render_time_gpu().

**Note:** Requires measurements to be enabled on the specified `viewport` using viewport_set_measure_render_time(). Otherwise, this method returns `0.0`.

---

[float](class_float.md#class-float) **viewport_get_measured_render_time_gpu**(viewport: [RID](class_rid.md#class-rid))

Returns the GPU time taken to render the last frame in milliseconds. To get a complete readout of GPU time spent to render the scene, sum the render times of all viewports that are drawn every frame. Unlike [Engine.get_frames_per_second()](class_engine.md#class-engine-method-get-frames-per-second), this method accurately reflects GPU utilization even if framerate is capped via V-Sync or [Engine.max_fps](class_engine.md#class-engine-property-max-fps). See also viewport_get_measured_render_time_cpu().

**Note:** Requires measurements to be enabled on the specified `viewport` using viewport_set_measure_render_time(). Otherwise, this method returns `0.0`.

**Note:** When GPU utilization is low enough during a certain period of time, GPUs will decrease their power state (which in turn decreases core and memory clock speeds). This can cause the reported GPU time to increase if GPU utilization is kept low enough by a framerate cap (compared to what it would be at the GPU's highest power state). Keep this in mind when benchmarking using viewport_get_measured_render_time_gpu(). This behavior can be overridden in the graphics driver settings at the cost of higher power usage.

---

[int](class_int.md#class-int) **viewport_get_render_info**(viewport: [RID](class_rid.md#class-rid), type: ViewportRenderInfoType, info: ViewportRenderInfo)

Returns a statistic about the rendering engine which can be used for performance profiling. This is separated into render pass `type`s, each of them having the same `info`s you can query (different passes will return different values).

See also get_rendering_info(), which returns global information across all viewports.

**Note:** Viewport rendering information is not available until at least 2 frames have been rendered by the engine. If rendering information is not available, viewport_get_render_info() returns `0`. To print rendering information in `_ready()` successfully, use the following:

```gdscript
func _ready():
    for _i in 2:
        await get_tree().process_frame

    print(
            RenderingServer.viewport_get_render_info(get_viewport().get_viewport_rid(),
            RenderingServer.VIEWPORT_RENDER_INFO_TYPE_VISIBLE,
            RenderingServer.VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME)
    )
```

---

[RID](class_rid.md#class-rid) **viewport_get_render_target**(viewport: [RID](class_rid.md#class-rid))

Returns the render target for the viewport.

---

[RID](class_rid.md#class-rid) **viewport_get_texture**(viewport: [RID](class_rid.md#class-rid))

Returns the viewport's last rendered frame.

---

ViewportUpdateMode **viewport_get_update_mode**(viewport: [RID](class_rid.md#class-rid))

Returns the viewport's update mode.

**Warning:** Calling this from any thread other than the rendering thread will be detrimental to performance.

---

 **viewport_remove_canvas**(viewport: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid))

Detaches a viewport from a canvas.

---

 **viewport_set_active**(viewport: [RID](class_rid.md#class-rid), active: [bool](class_bool.md#class-bool))

If `true`, sets the viewport active, else sets it inactive.

---

 **viewport_set_anisotropic_filtering_level**(viewport: [RID](class_rid.md#class-rid), anisotropic_filtering_level: ViewportAnisotropicFiltering)

Sets the maximum number of samples to take when using anisotropic filtering on textures (as a power of two). A higher sample count will result in sharper textures at oblique angles, but is more expensive to compute. A value of `0` forcibly disables anisotropic filtering, even on materials where it is enabled.

The anisotropic filtering level also affects decals and light projectors if they are configured to use anisotropic filtering. See [ProjectSettings.rendering/textures/decals/filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-decals-filter) and [ProjectSettings.rendering/textures/light_projectors/filter](class_projectsettings.md#class-projectsettings-property-rendering-textures-light-projectors-filter).

**Note:** In 3D, for this setting to have an effect, set [BaseMaterial3D.texture_filter](class_basematerial3d.md#class-basematerial3d-property-texture-filter) to [BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC](class_basematerial3d.md#class-basematerial3d-constant-texture-filter-linear-with-mipmaps-anisotropic) or [BaseMaterial3D.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC](class_basematerial3d.md#class-basematerial3d-constant-texture-filter-nearest-with-mipmaps-anisotropic) on materials.

**Note:** In 2D, for this setting to have an effect, set [CanvasItem.texture_filter](class_canvasitem.md#class-canvasitem-property-texture-filter) to [CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC](class_canvasitem.md#class-canvasitem-constant-texture-filter-linear-with-mipmaps-anisotropic) or [CanvasItem.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC](class_canvasitem.md#class-canvasitem-constant-texture-filter-nearest-with-mipmaps-anisotropic) on the [CanvasItem](class_canvasitem.md#class-canvasitem) node displaying the texture (or in [CanvasTexture](class_canvastexture.md#class-canvastexture)). However, anisotropic filtering is rarely useful in 2D, so only enable it for textures in 2D if it makes a meaningful visual difference.

---

 **viewport_set_canvas_cull_mask**(viewport: [RID](class_rid.md#class-rid), canvas_cull_mask: [int](class_int.md#class-int))

Sets the rendering mask associated with this [Viewport](class_viewport.md#class-viewport). Only [CanvasItem](class_canvasitem.md#class-canvasitem) nodes with a matching rendering visibility layer will be rendered by this [Viewport](class_viewport.md#class-viewport).

---

 **viewport_set_canvas_stacking**(viewport: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), layer: [int](class_int.md#class-int), sublayer: [int](class_int.md#class-int))

Sets the stacking order for a viewport's canvas.

`layer` is the actual canvas layer, while `sublayer` specifies the stacking order of the canvas among those in the same layer.

**Note:** `layer` should be between CANVAS_LAYER_MIN and CANVAS_LAYER_MAX (inclusive). Any other value will wrap around.

---

 **viewport_set_canvas_transform**(viewport: [RID](class_rid.md#class-rid), canvas: [RID](class_rid.md#class-rid), offset: [Transform2D](class_transform2d.md#class-transform2d))

Sets the transformation of a viewport's canvas.

---

 **viewport_set_clear_mode**(viewport: [RID](class_rid.md#class-rid), clear_mode: ViewportClearMode)

Sets the clear mode of a viewport.

---

 **viewport_set_debug_draw**(viewport: [RID](class_rid.md#class-rid), draw: ViewportDebugDraw)

Sets the debug draw mode of a viewport.

---

 **viewport_set_default_canvas_item_texture_filter**(viewport: [RID](class_rid.md#class-rid), filter: CanvasItemTextureFilter)

Sets the default texture filtering mode for the specified `viewport` RID.

---

 **viewport_set_default_canvas_item_texture_repeat**(viewport: [RID](class_rid.md#class-rid), repeat: CanvasItemTextureRepeat)

Sets the default texture repeat mode for the specified `viewport` RID.

---

 **viewport_set_disable_2d**(viewport: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool))

If `true`, the viewport's canvas (i.e. 2D and GUI elements) is not rendered.

---

 **viewport_set_disable_3d**(viewport: [RID](class_rid.md#class-rid), disable: [bool](class_bool.md#class-bool))

If `true`, the viewport's 3D elements are not rendered.

---

 **viewport_set_environment_mode**(viewport: [RID](class_rid.md#class-rid), mode: ViewportEnvironmentMode)

Sets the viewport's environment mode which allows enabling or disabling rendering of 3D environment over 2D canvas. When disabled, 2D will not be affected by the environment. When enabled, 2D will be affected by the environment if the environment background mode is ENV_BG_CANVAS. The default behavior is to inherit the setting from the viewport's parent. If the topmost parent is also set to VIEWPORT_ENVIRONMENT_INHERIT, then the behavior will be the same as if it was set to VIEWPORT_ENVIRONMENT_ENABLED.

---

 **viewport_set_fsr_sharpness**(viewport: [RID](class_rid.md#class-rid), sharpness: [float](class_float.md#class-float))

Determines how sharp the upscaled image will be when using the FSR upscaling mode. Sharpness halves with every whole number. Values go from 0.0 (sharpest) to 2.0. Values above 2.0 won't make a visible difference.

---

 **viewport_set_global_canvas_transform**(viewport: [RID](class_rid.md#class-rid), transform: [Transform2D](class_transform2d.md#class-transform2d))

Sets the viewport's global transformation matrix.

---

 **viewport_set_measure_render_time**(viewport: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Sets the measurement for the given `viewport` RID (obtained using [Viewport.get_viewport_rid()](class_viewport.md#class-viewport-method-get-viewport-rid)). Once enabled, viewport_get_measured_render_time_cpu() and viewport_get_measured_render_time_gpu() will return values greater than `0.0` when queried with the given `viewport`.

---

 **viewport_set_msaa_2d**(viewport: [RID](class_rid.md#class-rid), msaa: ViewportMSAA)

Sets the multisample antialiasing mode for 2D/Canvas on the specified `viewport` RID. Equivalent to [ProjectSettings.rendering/anti_aliasing/quality/msaa_2d](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-msaa-2d) or [Viewport.msaa_2d](class_viewport.md#class-viewport-property-msaa-2d).

---

 **viewport_set_msaa_3d**(viewport: [RID](class_rid.md#class-rid), msaa: ViewportMSAA)

Sets the multisample antialiasing mode for 3D on the specified `viewport` RID. Equivalent to [ProjectSettings.rendering/anti_aliasing/quality/msaa_3d](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-msaa-3d) or [Viewport.msaa_3d](class_viewport.md#class-viewport-property-msaa-3d).

---

 **viewport_set_occlusion_culling_build_quality**(quality: ViewportOcclusionCullingBuildQuality)

Sets the [ProjectSettings.rendering/occlusion_culling/bvh_build_quality](class_projectsettings.md#class-projectsettings-property-rendering-occlusion-culling-bvh-build-quality) to use for occlusion culling. This parameter is global and cannot be set on a per-viewport basis.

---

 **viewport_set_occlusion_rays_per_thread**(rays_per_thread: [int](class_int.md#class-int))

Sets the [ProjectSettings.rendering/occlusion_culling/occlusion_rays_per_thread](class_projectsettings.md#class-projectsettings-property-rendering-occlusion-culling-occlusion-rays-per-thread) to use for occlusion culling. This parameter is global and cannot be set on a per-viewport basis.

---

 **viewport_set_parent_viewport**(viewport: [RID](class_rid.md#class-rid), parent_viewport: [RID](class_rid.md#class-rid))

Sets the viewport's parent to the viewport specified by the `parent_viewport` RID.

---

 **viewport_set_positional_shadow_atlas_quadrant_subdivision**(viewport: [RID](class_rid.md#class-rid), quadrant: [int](class_int.md#class-int), subdivision: [int](class_int.md#class-int))

Sets the number of subdivisions to use in the specified shadow atlas `quadrant` for omni and spot shadows. See also [Viewport.set_positional_shadow_atlas_quadrant_subdiv()](class_viewport.md#class-viewport-method-set-positional-shadow-atlas-quadrant-subdiv).

---

 **viewport_set_positional_shadow_atlas_size**(viewport: [RID](class_rid.md#class-rid), size: [int](class_int.md#class-int), use_16_bits: [bool](class_bool.md#class-bool) = false)

Sets the `size` of the shadow atlas's images (used for omni and spot lights) on the viewport specified by the `viewport` RID. The value is rounded up to the nearest power of 2. If `use_16_bits` is `true`, use 16 bits for the omni/spot shadow depth map. Enabling this results in shadows having less precision and may result in shadow acne, but can lead to performance improvements on some devices.

**Note:** If this is set to `0`, no positional shadows will be visible at all. This can improve performance significantly on low-end systems by reducing both the CPU and GPU load (as fewer draw calls are needed to draw the scene without shadows).

---

 **viewport_set_render_direct_to_screen**(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `true`, render the contents of the viewport directly to screen. This allows a low-level optimization where you can skip drawing a viewport to the root viewport. While this optimization can result in a significant increase in speed (especially on older devices), it comes at a cost of usability. When this is enabled, you cannot read from the viewport or from the screen_texture. You also lose the benefit of certain window settings, such as the various stretch modes. Another consequence to be aware of is that in 2D the rendering happens in window coordinates, so if you have a viewport that is double the size of the window, and you set this, then only the portion that fits within the window will be drawn, no automatic scaling is possible, even if your game scene is significantly larger than the window size.

---

 **viewport_set_scaling_3d_mode**(viewport: [RID](class_rid.md#class-rid), scaling_3d_mode: ViewportScaling3DMode)

Sets the 3D resolution scaling mode. Bilinear scaling renders at different resolution to either undersample or supersample the viewport. FidelityFX Super Resolution 1.0, abbreviated to FSR, is an upscaling technology that produces high quality images at fast framerates by using a spatially aware upscaling algorithm. FSR is slightly more expensive than bilinear, but it produces significantly higher image quality. FSR should be used where possible.

---

 **viewport_set_scaling_3d_scale**(viewport: [RID](class_rid.md#class-rid), scale: [float](class_float.md#class-float))

Scales the 3D render buffer based on the viewport size uses an image filter specified in ViewportScaling3DMode to scale the output image to the full viewport size. Values lower than `1.0` can be used to speed up 3D rendering at the cost of quality (undersampling). Values greater than `1.0` are only valid for bilinear mode and can be used to improve 3D rendering quality at a high performance cost (supersampling). See also ViewportMSAA for multi-sample antialiasing, which is significantly cheaper but only smoothens the edges of polygons.

When using FSR upscaling, AMD recommends exposing the following values as preset options to users "Ultra Quality: 0.77", "Quality: 0.67", "Balanced: 0.59", "Performance: 0.5" instead of exposing the entire scale.

---

 **viewport_set_scenario**(viewport: [RID](class_rid.md#class-rid), scenario: [RID](class_rid.md#class-rid))

Sets a viewport's scenario. The scenario contains information about environment information, reflection atlas, etc.

---

 **viewport_set_screen_space_aa**(viewport: [RID](class_rid.md#class-rid), mode: ViewportScreenSpaceAA)

Sets the viewport's screen-space antialiasing mode. Equivalent to [ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-screen-space-aa) or [Viewport.screen_space_aa](class_viewport.md#class-viewport-property-screen-space-aa).

---

 **viewport_set_sdf_oversize_and_scale**(viewport: [RID](class_rid.md#class-rid), oversize: ViewportSDFOversize, scale: ViewportSDFScale)

Sets the viewport's 2D signed distance field [ProjectSettings.rendering/2d/sdf/oversize](class_projectsettings.md#class-projectsettings-property-rendering-2d-sdf-oversize) and [ProjectSettings.rendering/2d/sdf/scale](class_projectsettings.md#class-projectsettings-property-rendering-2d-sdf-scale). This is used when sampling the signed distance field in [CanvasItem](class_canvasitem.md#class-canvasitem) shaders as well as [GPUParticles2D](class_gpuparticles2d.md#class-gpuparticles2d) collision. This is *not* used by SDFGI in 3D rendering.

---

 **viewport_set_size**(viewport: [RID](class_rid.md#class-rid), width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), view_count: [int](class_int.md#class-int) = 1)

Sets the viewport's `width` and `height` in pixels. Optionally the `view_count` can be set to increase the number of view layers for stereo rendering.

---

 **viewport_set_snap_2d_transforms_to_pixel**(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `true`, canvas item transforms (i.e. origin position) are snapped to the nearest pixel when rendering. This can lead to a crisper appearance at the cost of less smooth movement, especially when [Camera2D](class_camera2d.md#class-camera2d) smoothing is enabled. Equivalent to [ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel](class_projectsettings.md#class-projectsettings-property-rendering-2d-snap-snap-2d-transforms-to-pixel).

---

 **viewport_set_snap_2d_vertices_to_pixel**(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `true`, canvas item vertices (i.e. polygon points) are snapped to the nearest pixel when rendering. This can lead to a crisper appearance at the cost of less smooth movement, especially when [Camera2D](class_camera2d.md#class-camera2d) smoothing is enabled. Equivalent to [ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel](class_projectsettings.md#class-projectsettings-property-rendering-2d-snap-snap-2d-vertices-to-pixel).

---

 **viewport_set_texture_mipmap_bias**(viewport: [RID](class_rid.md#class-rid), mipmap_bias: [float](class_float.md#class-float))

Affects the final texture sharpness by reading from a lower or higher mipmap (also called "texture LOD bias"). Negative values make mipmapped textures sharper but grainier when viewed at a distance, while positive values make mipmapped textures blurrier (even when up close). To get sharper textures at a distance without introducing too much graininess, set this between `-0.75` and `0.0`. Enabling temporal antialiasing ([ProjectSettings.rendering/anti_aliasing/quality/use_taa](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-use-taa)) can help reduce the graininess visible when using negative mipmap bias.

**Note:** When the 3D scaling mode is set to FSR 1.0, this value is used to adjust the automatic mipmap bias which is calculated internally based on the scale factor. The formula for this is `-log2(1.0 / scale) + mipmap_bias`.

**Note:** This method is only supported in the Forward+ and Mobile renderers, not Compatibility. In Compatibility, this method is always treated as if `mipmap_bias` was set to `0.0`.

---

 **viewport_set_transparent_background**(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `true`, the viewport renders its background as transparent.

---

 **viewport_set_update_mode**(viewport: [RID](class_rid.md#class-rid), update_mode: ViewportUpdateMode)

Sets when the viewport should be updated.

---

 **viewport_set_use_debanding**(viewport: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Equivalent to [Viewport.use_debanding](class_viewport.md#class-viewport-property-use-debanding). See also [ProjectSettings.rendering/anti_aliasing/quality/use_debanding](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-use-debanding).

---

 **viewport_set_use_hdr_2d**(viewport: [RID](class_rid.md#class-rid), enabled: [bool](class_bool.md#class-bool))

If `true`, 2D rendering will use a high dynamic range (HDR) `RGBA16` format framebuffer. Additionally, 2D rendering will be performed on linear values and will be converted using the appropriate transfer function immediately before blitting to the screen (if the Viewport is attached to the screen).

Practically speaking, this means that the end result of the Viewport will not be clamped to the `0-1` range and can be used in 3D rendering without color encoding adjustments. This allows 2D rendering to take advantage of effects requiring high dynamic range (e.g. 2D glow) as well as substantially improves the appearance of effects requiring highly detailed gradients. This setting has the same effect as [Viewport.use_hdr_2d](class_viewport.md#class-viewport-property-use-hdr-2d).

---

 **viewport_set_use_occlusion_culling**(viewport: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, enables occlusion culling on the specified viewport. Equivalent to [ProjectSettings.rendering/occlusion_culling/use_occlusion_culling](class_projectsettings.md#class-projectsettings-property-rendering-occlusion-culling-use-occlusion-culling).

---

 **viewport_set_use_taa**(viewport: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

If `true`, use temporal antialiasing. Equivalent to [ProjectSettings.rendering/anti_aliasing/quality/use_taa](class_projectsettings.md#class-projectsettings-property-rendering-anti-aliasing-quality-use-taa) or [Viewport.use_taa](class_viewport.md#class-viewport-property-use-taa).

---

 **viewport_set_use_xr**(viewport: [RID](class_rid.md#class-rid), use_xr: [bool](class_bool.md#class-bool))

If `true`, the viewport uses augmented or virtual reality technologies. See [XRInterface](class_xrinterface.md#class-xrinterface).

---

 **viewport_set_vrs_mode**(viewport: [RID](class_rid.md#class-rid), mode: ViewportVRSMode)

Sets the Variable Rate Shading (VRS) mode for the viewport. If the GPU does not support VRS, this property is ignored. Equivalent to [ProjectSettings.rendering/vrs/mode](class_projectsettings.md#class-projectsettings-property-rendering-vrs-mode).

---

 **viewport_set_vrs_texture**(viewport: [RID](class_rid.md#class-rid), texture: [RID](class_rid.md#class-rid))

The texture to use when the VRS mode is set to VIEWPORT_VRS_TEXTURE. Equivalent to [ProjectSettings.rendering/vrs/texture](class_projectsettings.md#class-projectsettings-property-rendering-vrs-texture).

---

 **viewport_set_vrs_update_mode**(viewport: [RID](class_rid.md#class-rid), mode: ViewportVRSUpdateMode)

Sets the update mode for Variable Rate Shading (VRS) for the viewport. VRS requires the input texture to be converted to the format usable by the VRS method supported by the hardware. The update mode defines how often this happens. If the GPU does not support VRS, or VRS is not enabled, this property is ignored.

If set to VIEWPORT_VRS_UPDATE_ONCE, the input texture is copied once and the mode is changed to VIEWPORT_VRS_UPDATE_DISABLED.

---

[RID](class_rid.md#class-rid) **visibility_notifier_create**()

Creates a new 3D visibility notifier object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `visibility_notifier_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

To place in a scene, attach this notifier to an instance using instance_set_base() using the returned RID.

**Note:** The equivalent node is [VisibleOnScreenNotifier3D](class_visibleonscreennotifier3d.md#class-visibleonscreennotifier3d).

---

 **visibility_notifier_set_aabb**(notifier: [RID](class_rid.md#class-rid), aabb: [AABB](class_aabb.md#class-aabb))

Sets the AABB of the specified visibility notifier.

---

 **visibility_notifier_set_callbacks**(notifier: [RID](class_rid.md#class-rid), enter_callable: [Callable](class_callable.md#class-callable), exit_callable: [Callable](class_callable.md#class-callable))

Sets the methods to be called when the notifier enters or exits the view.

---

 **voxel_gi_allocate_data**(voxel_gi: [RID](class_rid.md#class-rid), to_cell_xform: [Transform3D](class_transform3d.md#class-transform3d), aabb: [AABB](class_aabb.md#class-aabb), octree_size: [Vector3i](class_vector3i.md#class-vector3i), octree_cells: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), data_cells: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), distance_field: [PackedByteArray](class_packedbytearray.md#class-packedbytearray), level_counts: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Allocates and initializes the voxel GI data for the specified `voxel_gi` RID. `octree_cells` must be a multiple of 32. `octree_cells` must be double the size of `data_cells`. The allocated data can be retrieved later using the various `voxel_gi_get_*` methods.

---

[RID](class_rid.md#class-rid) **voxel_gi_create**()

Creates a new voxel-based global illumination object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `voxel_gi_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's free_rid() method.

**Note:** The equivalent node is [VoxelGI](class_voxelgi.md#class-voxelgi).

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **voxel_gi_get_data_cells**(voxel_gi: [RID](class_rid.md#class-rid))

Returns the data cells for the specified voxel GI data instance. See also voxel_gi_allocate_data().

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **voxel_gi_get_distance_field**(voxel_gi: [RID](class_rid.md#class-rid))

Returns the distance field data for the specified voxel GI data instance. See also voxel_gi_allocate_data().

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **voxel_gi_get_level_counts**(voxel_gi: [RID](class_rid.md#class-rid))

Returns the level counts for the specified voxel GI data instance. See also voxel_gi_allocate_data().

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **voxel_gi_get_octree_cells**(voxel_gi: [RID](class_rid.md#class-rid))

Returns the octree cell data for the specified voxel GI data instance. See also voxel_gi_allocate_data().

---

[Vector3i](class_vector3i.md#class-vector3i) **voxel_gi_get_octree_size**(voxel_gi: [RID](class_rid.md#class-rid))

Returns the octree size for the specified voxel GI data instance, which corresponds to the number of subdivisions per axis. This can be viewed in the editor by hovering the **Bake VoxelGI** button at the top of the 3D editor viewport when a [VoxelGI](class_voxelgi.md#class-voxelgi) node is selected and looking at the **Subdivisions** field in the tooltip.

---

[Transform3D](class_transform3d.md#class-transform3d) **voxel_gi_get_to_cell_xform**(voxel_gi: [RID](class_rid.md#class-rid))

Returns the transform to cell space for the specified voxel GI data instance. See also voxel_gi_allocate_data().

---

 **voxel_gi_set_baked_exposure_normalization**(voxel_gi: [RID](class_rid.md#class-rid), baked_exposure: [float](class_float.md#class-float))

Used to inform the renderer what exposure normalization value was used while baking the voxel gi. This value will be used and modulated at run time to ensure that the voxel gi maintains a consistent level of exposure even if the scene-wide exposure normalization is changed at run time. For more information see camera_attributes_set_exposure().

---

 **voxel_gi_set_bias**(voxel_gi: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float))

Sets the [VoxelGIData.bias](class_voxelgidata.md#class-voxelgidata-property-bias) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class-rid).

---

 **voxel_gi_set_dynamic_range**(voxel_gi: [RID](class_rid.md#class-rid), range: [float](class_float.md#class-float))

Sets the [VoxelGIData.dynamic_range](class_voxelgidata.md#class-voxelgidata-property-dynamic-range) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class-rid).

---

 **voxel_gi_set_energy**(voxel_gi: [RID](class_rid.md#class-rid), energy: [float](class_float.md#class-float))

Sets the [VoxelGIData.energy](class_voxelgidata.md#class-voxelgidata-property-energy) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class-rid).

---

 **voxel_gi_set_interior**(voxel_gi: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Sets the [VoxelGIData.interior](class_voxelgidata.md#class-voxelgidata-property-interior) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class-rid).

---

 **voxel_gi_set_normal_bias**(voxel_gi: [RID](class_rid.md#class-rid), bias: [float](class_float.md#class-float))

Sets the [VoxelGIData.normal_bias](class_voxelgidata.md#class-voxelgidata-property-normal-bias) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class-rid).

---

 **voxel_gi_set_propagation**(voxel_gi: [RID](class_rid.md#class-rid), amount: [float](class_float.md#class-float))

Sets the [VoxelGIData.propagation](class_voxelgidata.md#class-voxelgidata-property-propagation) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class-rid).

---

 **voxel_gi_set_quality**(quality: VoxelGIQuality)

Sets the [ProjectSettings.rendering/global_illumination/voxel_gi/quality](class_projectsettings.md#class-projectsettings-property-rendering-global-illumination-voxel-gi-quality) value to use when rendering. This parameter is global and cannot be set on a per-VoxelGI basis.

---

 **voxel_gi_set_use_two_bounces**(voxel_gi: [RID](class_rid.md#class-rid), enable: [bool](class_bool.md#class-bool))

Sets the [VoxelGIData.use_two_bounces](class_voxelgidata.md#class-voxelgidata-property-use-two-bounces) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class-rid).
