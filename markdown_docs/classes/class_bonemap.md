# BoneMap

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Describes a mapping of bone names for retargeting [Skeleton3D](class_skeleton3d.md#class-skeleton3d) into common names defined by a [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile).

## Description

This class contains a dictionary that uses a list of bone names in [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) as key names.

By assigning the actual [Skeleton3D](class_skeleton3d.md#class-skeleton3d) bone name as the key value, it maps the [Skeleton3D](class_skeleton3d.md#class-skeleton3d) to the [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile).

## Tutorials

- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons.md)

## Properties

| [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile)   | profile   |
|---------------------------------------------------------------------|----------------------------------------------|

## Methods

| [StringName](class_stringname.md#class-stringname)   | find_profile_bone_name(skeleton_bone_name: [StringName](class_stringname.md#class-stringname))                                                                        |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StringName](class_stringname.md#class-stringname)   | get_skeleton_bone_name(profile_bone_name: [StringName](class_stringname.md#class-stringname))                                                                         |
|                                                      | set_skeleton_bone_name(profile_bone_name: [StringName](class_stringname.md#class-stringname), skeleton_bone_name: [StringName](class_stringname.md#class-stringname)) |

---

## Signals

**bone_map_updated**()

This signal is emitted when change the key value in the **BoneMap**. This is used to validate mapping and to update **BoneMap** editor.

---

**profile_updated**()

This signal is emitted when change the value in profile or change the reference of profile. This is used to update key names in the **BoneMap** and to redraw the **BoneMap** editor.

---

## Property Descriptions

[SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) **profile**

-  **set_profile**(value: [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile))
- [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) **get_profile**()

A [SkeletonProfile](class_skeletonprofile.md#class-skeletonprofile) of the mapping target. Key names in the **BoneMap** are synchronized with it.

---

## Method Descriptions

[StringName](class_stringname.md#class-stringname) **find_profile_bone_name**(skeleton_bone_name: [StringName](class_stringname.md#class-stringname))

Returns a profile bone name having `skeleton_bone_name`. If not found, an empty [StringName](class_stringname.md#class-stringname) will be returned.

In the retargeting process, the returned bone name is the bone name of the target skeleton.

---

[StringName](class_stringname.md#class-stringname) **get_skeleton_bone_name**(profile_bone_name: [StringName](class_stringname.md#class-stringname))

Returns a skeleton bone name is mapped to `profile_bone_name`.

In the retargeting process, the returned bone name is the bone name of the source skeleton.

---

 **set_skeleton_bone_name**(profile_bone_name: [StringName](class_stringname.md#class-stringname), skeleton_bone_name: [StringName](class_stringname.md#class-stringname))

Maps a skeleton bone name to `profile_bone_name`.

In the retargeting process, the setting bone name is the bone name of the source skeleton.
