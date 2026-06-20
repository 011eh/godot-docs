# RenderDataExtension

**Inherits:** [RenderData](class_renderdata.md#class-renderdata) **<** [Object](class_object.md#class-object)

This class allows for a RenderData implementation to be made in GDExtension.

## Description

This class allows for a RenderData implementation to be made in GDExtension.

## Methods

| [RID](class_rid.md#class-rid)                                              | \_get_camera_attributes()       |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)                                              | \_get_environment()                   |
| [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) | \_get_render_scene_buffers() |
| [RenderSceneData](class_renderscenedata.md#class-renderscenedata)          | \_get_render_scene_data()       |

---

## Method Descriptions

[RID](class_rid.md#class-rid) **\_get_camera_attributes**()

Implement this in GDExtension to return the [RID](class_rid.md#class-rid) for the implementation's camera attributes object.

---

[RID](class_rid.md#class-rid) **\_get_environment**()

Implement this in GDExtension to return the [RID](class_rid.md#class-rid) of the implementation's environment object.

---

[RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) **\_get_render_scene_buffers**()

Implement this in GDExtension to return the implementation's [RenderSceneBuffers](class_renderscenebuffers.md#class-renderscenebuffers) object.

---

[RenderSceneData](class_renderscenedata.md#class-renderscenedata) **\_get_render_scene_data**()

Implement this in GDExtension to return the implementation's [RenderSceneDataExtension](class_renderscenedataextension.md#class-renderscenedataextension) object.
