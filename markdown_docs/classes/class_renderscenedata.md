# RenderSceneData

**Inherits:** [Object](class_object.md#class-object)

**Inherited By:** [RenderSceneDataExtension](class_renderscenedataextension.md#class-renderscenedataextension), [RenderSceneDataRD](class_renderscenedatard.md#class-renderscenedatard)

Abstract render data object, holds scene data related to rendering a single frame of a viewport.

## Description

Abstract scene data object, exists for the duration of rendering a single viewport. See also [RenderSceneDataRD](class_renderscenedatard.md#class-renderscenedatard), [RenderData](class_renderdata.md#class-renderdata), and [RenderDataRD](class_renderdatard.md#class-renderdatard).

**Note:** This is an internal rendering server object. Do not instantiate this class from a script.

## Methods

| [Projection](class_projection.md#class-projection)    | get_cam_projection()                                      |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [Transform3D](class_transform3d.md#class-transform3d) | get_cam_transform()                                        |
| [RID](class_rid.md#class-rid)                         | get_uniform_buffer()                                      |
| [int](class_int.md#class-int)                         | get_view_count()                                              |
| [Vector3](class_vector3.md#class-vector3)             | get_view_eye_offset(view: [int](class_int.md#class-int)) |
| [Projection](class_projection.md#class-projection)    | get_view_projection(view: [int](class_int.md#class-int)) |

---

## Method Descriptions

[Projection](class_projection.md#class-projection) **get_cam_projection**()

Returns the camera projection used to render this frame.

**Note:** If more than one view is rendered, this will return a combined projection.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_cam_transform**()

Returns the camera transform used to render this frame.

**Note:** If more than one view is rendered, this will return a centered transform.

---

[RID](class_rid.md#class-rid) **get_uniform_buffer**()

Return the [RID](class_rid.md#class-rid) of the uniform buffer containing the scene data as a UBO.

---

[int](class_int.md#class-int) **get_view_count**()

Returns the number of views being rendered.

---

[Vector3](class_vector3.md#class-vector3) **get_view_eye_offset**(view: [int](class_int.md#class-int))

Returns the eye offset per view used to render this frame. This is the offset between our camera transform and the eye transform.

---

[Projection](class_projection.md#class-projection) **get_view_projection**(view: [int](class_int.md#class-int))

Returns the view projection per view used to render this frame.

**Note:** If a single view is rendered, this returns the camera projection. If more than one view is rendered, this will return a projection for the given view including the eye offset.
