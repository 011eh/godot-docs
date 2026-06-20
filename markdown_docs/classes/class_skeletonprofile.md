# SkeletonProfile

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid)

Base class for a profile of a virtual skeleton used as a target for retargeting.

## Description

This resource is used in [EditorScenePostImport](class_editorscenepostimport.md#class-editorscenepostimport). Some parameters are referring to bones in [Skeleton3D](class_skeleton3d.md#class-skeleton3d), [Skin](class_skin.md#class-skin), [Animation](class_animation.md#class-animation), and some other nodes are rewritten based on the parameters of **SkeletonProfile**.

**Note:** These parameters need to be set only when creating a custom profile. In [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid), they are defined internally as read-only values.

## Tutorials

- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons.md)

## Properties

| [int](class_int.md#class-int)                      | bone_size             | `0`   |
|----------------------------------------------------|--------------------------------------------------------------------|-------|
| [int](class_int.md#class-int)                      | group_size           | `0`   |
| [StringName](class_stringname.md#class-stringname) | root_bone             | `&""` |
| [StringName](class_stringname.md#class-stringname) | scale_base_bone | `&""` |

## Methods

| [int](class_int.md#class-int)                         | find_bone(bone_name: [StringName](class_stringname.md#class-stringname))                                                                   |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [StringName](class_stringname.md#class-stringname)    | get_bone_name(bone_idx: [int](class_int.md#class-int))                                                                                 |
| [StringName](class_stringname.md#class-stringname)    | get_bone_parent(bone_idx: [int](class_int.md#class-int))                                                                             |
| [StringName](class_stringname.md#class-stringname)    | get_bone_tail(bone_idx: [int](class_int.md#class-int))                                                                                 |
| [StringName](class_stringname.md#class-stringname)    | get_group(bone_idx: [int](class_int.md#class-int))                                                                                         |
| [StringName](class_stringname.md#class-stringname)    | get_group_name(group_idx: [int](class_int.md#class-int))                                                                              |
| [Vector2](class_vector2.md#class-vector2)             | get_handle_offset(bone_idx: [int](class_int.md#class-int))                                                                         |
| [Transform3D](class_transform3d.md#class-transform3d) | get_reference_pose(bone_idx: [int](class_int.md#class-int))                                                                       |
| TailDirection  | get_tail_direction(bone_idx: [int](class_int.md#class-int))                                                                       |
| [Texture2D](class_texture2d.md#class-texture2d)       | get_texture(group_idx: [int](class_int.md#class-int))                                                                                    |
| [bool](class_bool.md#class-bool)                      | is_required(bone_idx: [int](class_int.md#class-int))                                                                                     |
|                                                       | set_bone_name(bone_idx: [int](class_int.md#class-int), bone_name: [StringName](class_stringname.md#class-stringname))                  |
|                                                       | set_bone_parent(bone_idx: [int](class_int.md#class-int), bone_parent: [StringName](class_stringname.md#class-stringname))            |
|                                                       | set_bone_tail(bone_idx: [int](class_int.md#class-int), bone_tail: [StringName](class_stringname.md#class-stringname))                  |
|                                                       | set_group(bone_idx: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname))                              |
|                                                       | set_group_name(group_idx: [int](class_int.md#class-int), group_name: [StringName](class_stringname.md#class-stringname))              |
|                                                       | set_handle_offset(bone_idx: [int](class_int.md#class-int), handle_offset: [Vector2](class_vector2.md#class-vector2))               |
|                                                       | set_reference_pose(bone_idx: [int](class_int.md#class-int), bone_name: [Transform3D](class_transform3d.md#class-transform3d))     |
|                                                       | set_required(bone_idx: [int](class_int.md#class-int), required: [bool](class_bool.md#class-bool))                                       |
|                                                       | set_tail_direction(bone_idx: [int](class_int.md#class-int), tail_direction: TailDirection) |
|                                                       | set_texture(group_idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))                          |

---

## Signals

**profile_updated**()

This signal is emitted when change the value in profile. This is used to update key name in the [BoneMap](class_bonemap.md#class-bonemap) and to redraw the [BoneMap](class_bonemap.md#class-bonemap) editor.

**Note:** This signal is not connected directly to editor to simplify the reference, instead it is passed on to editor through the [BoneMap](class_bonemap.md#class-bonemap).

---

## Enumerations

enum **TailDirection**:

TailDirection **TAIL_DIRECTION_AVERAGE_CHILDREN** = `0`

Direction to the average coordinates of bone children.

TailDirection **TAIL_DIRECTION_SPECIFIC_CHILD** = `1`

Direction to the coordinates of specified bone child.

TailDirection **TAIL_DIRECTION_END** = `2`

Direction is not calculated.

---

## Property Descriptions

[int](class_int.md#class-int) **bone_size** = `0`

-  **set_bone_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone_size**()

The amount of bones in retargeting section's [BoneMap](class_bonemap.md#class-bonemap) editor. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid) has 56 bones.

The size of elements in [BoneMap](class_bonemap.md#class-bonemap) updates when changing this property in it's assigned **SkeletonProfile**.

---

[int](class_int.md#class-int) **group_size** = `0`

-  **set_group_size**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_group_size**()

The amount of groups of bones in retargeting section's [BoneMap](class_bonemap.md#class-bonemap) editor. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid) has 4 groups.

This property exists to separate the bone list into several sections in the editor.

---

[StringName](class_stringname.md#class-stringname) **root_bone** = `&""`

-  **set_root_bone**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_root_bone**()

A bone name that will be used as the root bone in [AnimationTree](class_animationtree.md#class-animationtree). This should be the bone of the parent of hips that exists at the world origin.

---

[StringName](class_stringname.md#class-stringname) **scale_base_bone** = `&""`

-  **set_scale_base_bone**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_scale_base_bone**()

A bone name which will use model's height as the coefficient for normalization. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class-skeletonprofilehumanoid) defines it as `Hips`.

---

## Method Descriptions

[int](class_int.md#class-int) **find_bone**(bone_name: [StringName](class_stringname.md#class-stringname))

Returns the bone index that matches `bone_name` as its name.

---

[StringName](class_stringname.md#class-stringname) **get_bone_name**(bone_idx: [int](class_int.md#class-int))

Returns the name of the bone at `bone_idx` that will be the key name in the [BoneMap](class_bonemap.md#class-bonemap).

In the retargeting process, the returned bone name is the bone name of the target skeleton.

---

[StringName](class_stringname.md#class-stringname) **get_bone_parent**(bone_idx: [int](class_int.md#class-int))

Returns the name of the bone which is the parent to the bone at `bone_idx`. The result is empty if the bone has no parent.

---

[StringName](class_stringname.md#class-stringname) **get_bone_tail**(bone_idx: [int](class_int.md#class-int))

Returns the name of the bone which is the tail of the bone at `bone_idx`.

---

[StringName](class_stringname.md#class-stringname) **get_group**(bone_idx: [int](class_int.md#class-int))

Returns the group of the bone at `bone_idx`.

---

[StringName](class_stringname.md#class-stringname) **get_group_name**(group_idx: [int](class_int.md#class-int))

Returns the name of the group at `group_idx` that will be the drawing group in the [BoneMap](class_bonemap.md#class-bonemap) editor.

---

[Vector2](class_vector2.md#class-vector2) **get_handle_offset**(bone_idx: [int](class_int.md#class-int))

Returns the offset of the bone at `bone_idx` that will be the button position in the [BoneMap](class_bonemap.md#class-bonemap) editor.

This is the offset with origin at the top left corner of the square.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_reference_pose**(bone_idx: [int](class_int.md#class-int))

Returns the reference pose transform for bone `bone_idx`.

---

TailDirection **get_tail_direction**(bone_idx: [int](class_int.md#class-int))

Returns the tail direction of the bone at `bone_idx`.

---

[Texture2D](class_texture2d.md#class-texture2d) **get_texture**(group_idx: [int](class_int.md#class-int))

Returns the texture of the group at `group_idx` that will be the drawing group background image in the [BoneMap](class_bonemap.md#class-bonemap) editor.

---

[bool](class_bool.md#class-bool) **is_required**(bone_idx: [int](class_int.md#class-int))

Returns whether the bone at `bone_idx` is required for retargeting.

This value is used by the bone map editor. If this method returns `true`, and no bone is assigned, the handle color will be red on the bone map editor.

---

 **set_bone_name**(bone_idx: [int](class_int.md#class-int), bone_name: [StringName](class_stringname.md#class-stringname))

Sets the name of the bone at `bone_idx` that will be the key name in the [BoneMap](class_bonemap.md#class-bonemap).

In the retargeting process, the setting bone name is the bone name of the target skeleton.

---

 **set_bone_parent**(bone_idx: [int](class_int.md#class-int), bone_parent: [StringName](class_stringname.md#class-stringname))

Sets the bone with name `bone_parent` as the parent of the bone at `bone_idx`. If an empty string is passed, then the bone has no parent.

---

 **set_bone_tail**(bone_idx: [int](class_int.md#class-int), bone_tail: [StringName](class_stringname.md#class-stringname))

Sets the bone with name `bone_tail` as the tail of the bone at `bone_idx`.

---

 **set_group**(bone_idx: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname))

Sets the group of the bone at `bone_idx`.

---

 **set_group_name**(group_idx: [int](class_int.md#class-int), group_name: [StringName](class_stringname.md#class-stringname))

Sets the name of the group at `group_idx` that will be the drawing group in the [BoneMap](class_bonemap.md#class-bonemap) editor.

---

 **set_handle_offset**(bone_idx: [int](class_int.md#class-int), handle_offset: [Vector2](class_vector2.md#class-vector2))

Sets the offset of the bone at `bone_idx` that will be the button position in the [BoneMap](class_bonemap.md#class-bonemap) editor.

This is the offset with origin at the top left corner of the square.

---

 **set_reference_pose**(bone_idx: [int](class_int.md#class-int), bone_name: [Transform3D](class_transform3d.md#class-transform3d))

Sets the reference pose transform for bone `bone_idx`.

---

 **set_required**(bone_idx: [int](class_int.md#class-int), required: [bool](class_bool.md#class-bool))

Sets the required status for bone `bone_idx` to `required`.

---

 **set_tail_direction**(bone_idx: [int](class_int.md#class-int), tail_direction: TailDirection)

Sets the tail direction of the bone at `bone_idx`.

**Note:** This only specifies the method of calculation. The actual coordinates required should be stored in an external skeleton, so the calculation itself needs to be done externally.

---

 **set_texture**(group_idx: [int](class_int.md#class-int), texture: [Texture2D](class_texture2d.md#class-texture2d))

Sets the texture of the group at `group_idx` that will be the drawing group background image in the [BoneMap](class_bonemap.md#class-bonemap) editor.
