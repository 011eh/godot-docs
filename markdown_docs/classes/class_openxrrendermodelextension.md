# OpenXRRenderModelExtension

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class-openxrextensionwrapper) **<** [Object](class_object.md#class-object)

This class implements the OpenXR Render Model Extension.

## Description

This class implements the OpenXR Render Model Extension, if enabled it will maintain a list of active render models and provides an interface to the render model data.

## Methods

| [bool](class_bool.md#class-bool)                                        | is_active()                                                                                                                                                    |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)                                           | render_model_create(render_model_id: [int](class_int.md#class-int))                                                                                  |
|                                                                         | render_model_destroy(render_model: [RID](class_rid.md#class-rid))                                                                                   |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]      | render_model_get_all()                                                                                                                              |
| [int](class_int.md#class-int)                                           | render_model_get_animatable_node_count(render_model: [RID](class_rid.md#class-rid))                                               |
| [String](class_string.md#class-string)                                  | render_model_get_animatable_node_name(render_model: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))           |
| [Transform3D](class_transform3d.md#class-transform3d)                   | render_model_get_animatable_node_transform(render_model: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int)) |
| [TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence)    | render_model_get_confidence(render_model: [RID](class_rid.md#class-rid))                                                                     |
| [Transform3D](class_transform3d.md#class-transform3d)                   | render_model_get_root_transform(render_model: [RID](class_rid.md#class-rid))                                                             |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray) | render_model_get_subaction_paths(render_model: [RID](class_rid.md#class-rid))                                                           |
| [String](class_string.md#class-string)                                  | render_model_get_top_level_path(render_model: [RID](class_rid.md#class-rid))                                                             |
| [bool](class_bool.md#class-bool)                                        | render_model_is_animatable_node_visible(render_model: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))       |
| [Node3D](class_node3d.md#class-node3d)                                  | render_model_new_scene_instance(render_model: [RID](class_rid.md#class-rid))                                                             |

---

## Signals

**render_model_added**(render_model: [RID](class_rid.md#class-rid))

Emitted when a new render model is added.

---

**render_model_removed**(render_model: [RID](class_rid.md#class-rid))

Emitted when a render model is removed.

---

**render_model_top_level_path_changed**(render_model: [RID](class_rid.md#class-rid))

Emitted when the top level path associated with a render model changed.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **is_active**()

Returns `true` if OpenXR's render model extension is supported and enabled.

**Note:** This only returns a valid value after OpenXR has been initialized.

---

[RID](class_rid.md#class-rid) **render_model_create**(render_model_id: [int](class_int.md#class-int))

Creates a render model object within OpenXR using a render model id.

**Note:** This function is exposed for dependent OpenXR extensions that provide render model ids to be used with the render model extension.

---

 **render_model_destroy**(render_model: [RID](class_rid.md#class-rid))

Destroys a render model object within OpenXR that was previously created with render_model_create().

**Note:** This function is exposed for dependent OpenXR extensions that provide render model ids to be used with the render model extension.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **render_model_get_all**()

Returns an array of all currently active render models registered with this extension.

---

[int](class_int.md#class-int) **render_model_get_animatable_node_count**(render_model: [RID](class_rid.md#class-rid))

Returns the number of animatable nodes this render model has.

---

[String](class_string.md#class-string) **render_model_get_animatable_node_name**(render_model: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the name of the given animatable node.

---

[Transform3D](class_transform3d.md#class-transform3d) **render_model_get_animatable_node_transform**(render_model: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns the current local transform for an animatable node. This is updated every frame.

---

[TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence) **render_model_get_confidence**(render_model: [RID](class_rid.md#class-rid))

Returns the tracking confidence of the tracking data for the render model.

---

[Transform3D](class_transform3d.md#class-transform3d) **render_model_get_root_transform**(render_model: [RID](class_rid.md#class-rid))

Returns the root transform of a render model. This is the tracked position relative to our [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d) node.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **render_model_get_subaction_paths**(render_model: [RID](class_rid.md#class-rid))

Returns a list of active subaction paths for this `render_model`.

**Note:** If different devices are bound to your actions than available in suggested interaction bindings, this information shows paths related to the interaction bindings being mimicked by that device.

---

[String](class_string.md#class-string) **render_model_get_top_level_path**(render_model: [RID](class_rid.md#class-rid))

Returns the top level path associated with this `render_model`. If provided this identifies whether the render model is associated with the player's hands or other body part.

---

[bool](class_bool.md#class-bool) **render_model_is_animatable_node_visible**(render_model: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns `true` if this animatable node should be visible.

---

[Node3D](class_node3d.md#class-node3d) **render_model_new_scene_instance**(render_model: [RID](class_rid.md#class-rid))

Returns an instance of a subscene that contains all [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) nodes that allow you to visualize the render model.
