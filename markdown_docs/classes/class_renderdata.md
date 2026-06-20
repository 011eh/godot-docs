# RenderData

**Inherits:** [Object](class_object.md#class-object)

**Inherited By:** [RenderDataExtension](class_renderdataextension.md#class-renderdataextension), [RenderDataRD](class_renderdatard.md#class-renderdatard)

Abstract render data object, holds frame data related to rendering a single frame of a viewport.

## Description

Abstract render data object, exists for the duration of rendering a single viewport. See also [RenderDataRD](class_renderdatard.md#class-renderdatard), [RenderSceneData](class_renderscenedata.md#class-renderscenedata), and [RenderSceneDataRD](class_renderscenedatard.md#class-renderscenedatard).

**Note:** This is an internal rendering server object. Do not instantiate this class from a script.

## Methods

| [RID](class_rid.md#class-rid)                                              | get_camera_attributes()       |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)                                              | get_environment()                   |
| [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) | get_render_scene_buffers() |
| [RenderSceneData](class_renderscenedata.md#class-renderscenedata)          | get_render_scene_data()       |

---

## Method Descriptions

[RID](class_rid.md#class-rid) **get_camera_attributes**()

Returns the [RID](class_rid.md#class-rid) of the camera attributes object in the [RenderingServer](class_renderingserver.md#class-renderingserver) being used to render this viewport.

---

[RID](class_rid.md#class-rid) **get_environment**()

Returns the [RID](class_rid.md#class-rid) of the environment object in the [RenderingServer](class_renderingserver.md#class-renderingserver) being used to render this viewport.

---

[RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) **get_render_scene_buffers**()

Returns the [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) object managing the scene buffers for rendering this viewport.

---

[RenderSceneData](class_renderscenedata.md#class-renderscenedata) **get_render_scene_data**()

Returns the [RenderSceneData](class_renderscenedata.md#class-renderscenedata) object managing this frames scene data.
