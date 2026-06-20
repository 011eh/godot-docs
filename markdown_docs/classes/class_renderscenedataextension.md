# RenderSceneDataExtension

**Inherits:** [RenderSceneData](class_renderscenedata.md#class-renderscenedata) **<** [Object](class_object.md#class-object)

This class allows for a RenderSceneData implementation to be made in GDExtension.

## Description

This class allows for a RenderSceneData implementation to be made in GDExtension.

## Methods

| [Projection](class_projection.md#class-projection)    | \_get_cam_projection()                                      |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [Transform3D](class_transform3d.md#class-transform3d) | \_get_cam_transform()                                        |
| [RID](class_rid.md#class-rid)                         | \_get_uniform_buffer()                                      |
| [int](class_int.md#class-int)                         | \_get_view_count()                                              |
| [Vector3](class_vector3.md#class-vector3)             | \_get_view_eye_offset(view: [int](class_int.md#class-int)) |
| [Projection](class_projection.md#class-projection)    | \_get_view_projection(view: [int](class_int.md#class-int)) |

---

## Method Descriptions

[Projection](class_projection.md#class-projection) **\_get_cam_projection**()

Implement this in GDExtension to return the camera [Projection](class_projection.md#class-projection).

---

[Transform3D](class_transform3d.md#class-transform3d) **\_get_cam_transform**()

Implement this in GDExtension to return the camera [Transform3D](class_transform3d.md#class-transform3d).

---

[RID](class_rid.md#class-rid) **\_get_uniform_buffer**()

Implement this in GDExtension to return the [RID](class_rid.md#class-rid) of the uniform buffer containing the scene data as a UBO.

---

[int](class_int.md#class-int) **\_get_view_count**()

Implement this in GDExtension to return the view count.

---

[Vector3](class_vector3.md#class-vector3) **\_get_view_eye_offset**(view: [int](class_int.md#class-int))

Implement this in GDExtension to return the eye offset for the given `view`.

---

[Projection](class_projection.md#class-projection) **\_get_view_projection**(view: [int](class_int.md#class-int))

Implement this in GDExtension to return the view [Projection](class_projection.md#class-projection) for the given `view`.
