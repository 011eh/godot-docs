# Skeleton3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A node containing a bone hierarchy, used to create a 3D skeletal animation.

## Description

**Skeleton3D** provides an interface for managing a hierarchy of bones, including pose, rest and animation (see [Animation](class_animation.md#class-animation)). It can also use ragdoll physics.

The overall transform of a bone with respect to the skeleton is determined by bone pose. Bone rest defines the initial transform of the bone pose.

Note that "global pose" below refers to the overall transform of the bone with respect to skeleton, so it is not the actual global/world transform of the bone.

## Tutorials

- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties

| [bool](class_bool.md#class-bool)                                            | animate_physical_bones                 | `true`   |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|----------|
| ModifierCallbackModeProcess | modifier_callback_mode_process | `1`      |
| [float](class_float.md#class-float)                                         | motion_scale                                     | `1.0`    |
| [bool](class_bool.md#class-bool)                                            | show_rest_only                                 | `false`  |

## Methods

| [int](class_int.md#class-int)                                                           | add_bone(name: [String](class_string.md#class-string))                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                         | advance(delta: [float](class_float.md#class-float))                                                                                                                                                                                                          |
|                                                                                         | clear_bones()                                                                                                                                                                                                                                            |
|                                                                                         | clear_bones_global_pose_override()                                                                                                                                                                                                  |
| [Skin](class_skin.md#class-skin)                                                        | create_skin_from_rest_transforms()                                                                                                                                                                                                  |
| [int](class_int.md#class-int)                                                           | find_bone(name: [String](class_string.md#class-string))                                                                                                                                                                                                    |
|                                                                                         | force_update_all_bone_transforms()                                                                                                                                                                                                  |
|                                                                                         | force_update_bone_child_transform(bone_idx: [int](class_int.md#class-int))                                                                                                                                                         |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | get_bone_children(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                         |
| [int](class_int.md#class-int)                                                           | get_bone_count()                                                                                                                                                                                                                                      |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | get_bone_global_pose(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                   |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | get_bone_global_pose_no_override(bone_idx: [int](class_int.md#class-int))                                                                                                                                                           |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | get_bone_global_pose_override(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                 |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | get_bone_global_rest(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                   |
| [Variant](class_variant.md#class-variant)                                               | get_bone_meta(bone_idx: [int](class_int.md#class-int), key: [StringName](class_stringname.md#class-stringname))                                                                                                                                        |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_bone_meta_list(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                       |
| [String](class_string.md#class-string)                                                  | get_bone_name(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                                 |
| [int](class_int.md#class-int)                                                           | get_bone_parent(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                             |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | get_bone_pose(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                                 |
| [Vector3](class_vector3.md#class-vector3)                                               | get_bone_pose_position(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                               |
| [Quaternion](class_quaternion.md#class-quaternion)                                      | get_bone_pose_rotation(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                               |
| [Vector3](class_vector3.md#class-vector3)                                               | get_bone_pose_scale(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                     |
| [Transform3D](class_transform3d.md#class-transform3d)                                   | get_bone_rest(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                                 |
| [StringName](class_stringname.md#class-stringname)                                      | get_concatenated_bone_names()                                                                                                                                                                                                            |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                    | get_parentless_bones()                                                                                                                                                                                                                          |
| [int](class_int.md#class-int)                                                           | get_version()                                                                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                        | has_bone_meta(bone_idx: [int](class_int.md#class-int), key: [StringName](class_stringname.md#class-stringname))                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | is_bone_enabled(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                             |
|                                                                                         | localize_rests()                                                                                                                                                                                                                                      |
|                                                                                         | physical_bones_add_collision_exception(exception: [RID](class_rid.md#class-rid))                                                                                                                                              |
|                                                                                         | physical_bones_remove_collision_exception(exception: [RID](class_rid.md#class-rid))                                                                                                                                        |
|                                                                                         | physical_bones_start_simulation(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = [])                                                                                                 |
|                                                                                         | physical_bones_stop_simulation()                                                                                                                                                                                                      |
| [SkinReference](class_skinreference.md#class-skinreference)                             | register_skin(skin: [Skin](class_skin.md#class-skin))                                                                                                                                                                                                  |
|                                                                                         | reset_bone_pose(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                                             |
|                                                                                         | reset_bone_poses()                                                                                                                                                                                                                                  |
|                                                                                         | set_bone_enabled(bone_idx: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool) = true)                                                                                                                                         |
|                                                                                         | set_bone_global_pose(bone_idx: [int](class_int.md#class-int), pose: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                      |
|                                                                                         | set_bone_global_pose_override(bone_idx: [int](class_int.md#class-int), pose: [Transform3D](class_transform3d.md#class-transform3d), amount: [float](class_float.md#class-float), persistent: [bool](class_bool.md#class-bool) = false) |
|                                                                                         | set_bone_meta(bone_idx: [int](class_int.md#class-int), key: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                      |
|                                                                                         | set_bone_name(bone_idx: [int](class_int.md#class-int), name: [String](class_string.md#class-string))                                                                                                                                                   |
|                                                                                         | set_bone_parent(bone_idx: [int](class_int.md#class-int), parent_idx: [int](class_int.md#class-int))                                                                                                                                                  |
|                                                                                         | set_bone_pose(bone_idx: [int](class_int.md#class-int), pose: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                    |
|                                                                                         | set_bone_pose_position(bone_idx: [int](class_int.md#class-int), position: [Vector3](class_vector3.md#class-vector3))                                                                                                                          |
|                                                                                         | set_bone_pose_rotation(bone_idx: [int](class_int.md#class-int), rotation: [Quaternion](class_quaternion.md#class-quaternion))                                                                                                                 |
|                                                                                         | set_bone_pose_scale(bone_idx: [int](class_int.md#class-int), scale: [Vector3](class_vector3.md#class-vector3))                                                                                                                                   |
|                                                                                         | set_bone_rest(bone_idx: [int](class_int.md#class-int), rest: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                    |
|                                                                                         | unparent_bone_and_rest(bone_idx: [int](class_int.md#class-int))                                                                                                                                                                               |

---

## Signals

**bone_enabled_changed**(bone_idx: [int](class_int.md#class-int))

Emitted when the bone at `bone_idx` is toggled with set_bone_enabled(). Use is_bone_enabled() to check the new value.

---

**bone_list_changed**()

Emitted when the list of bones changes, such as when calling add_bone(), set_bone_parent(), unparent_bone_and_rest(), or clear_bones().

---

**pose_updated**()

Emitted when the pose is updated.

**Note:** During the update process, this signal is not fired, so modification by [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) is not detected.

---

**rest_updated**()

Emitted when the rest is updated.

---

**show_rest_only_changed**()

Emitted when the value of show_rest_only changes.

---

**skeleton_updated**()

Emitted when the final pose has been calculated will be applied to the skin in the update process.

This means that all [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) processing is complete. In order to detect the completion of the processing of each [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d), use [SkeletonModifier3D.modification_processed](class_skeletonmodifier3d.md#class-skeletonmodifier3d-signal-modification-processed).

---

## Enumerations

enum **ModifierCallbackModeProcess**:

ModifierCallbackModeProcess **MODIFIER_CALLBACK_MODE_PROCESS_PHYSICS** = `0`

Set a flag to process modification during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class-node-constant-notification-internal-physics-process)).

ModifierCallbackModeProcess **MODIFIER_CALLBACK_MODE_PROCESS_IDLE** = `1`

Set a flag to process modification during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class-node-constant-notification-internal-process)).

ModifierCallbackModeProcess **MODIFIER_CALLBACK_MODE_PROCESS_MANUAL** = `2`

Do not process modification. Use advance() to process the modification manually.

---

## Constants

**NOTIFICATION_UPDATE_SKELETON** = `50`

Notification received when this skeleton's pose needs to be updated. In that case, this is called only once per frame in a deferred process.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **animate_physical_bones** = `true`

-  **set_animate_physical_bones**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_animate_physical_bones**()

**Deprecated:** This property may be changed or removed in future versions.

If you follow the recommended workflow and explicitly have [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d) as a child of **Skeleton3D**, you can control whether it is affected by raycasting without running physical_bones_start_simulation(), by its [SkeletonModifier3D.active](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-active).

However, for old (deprecated) configurations, **Skeleton3D** has an internal virtual [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d) for compatibility. This property controls the internal virtual [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class-physicalbonesimulator3d)'s [SkeletonModifier3D.active](class_skeletonmodifier3d.md#class-skeletonmodifier3d-property-active).

---

ModifierCallbackModeProcess **modifier_callback_mode_process** = `1`

-  **set_modifier_callback_mode_process**(value: ModifierCallbackModeProcess)
- ModifierCallbackModeProcess **get_modifier_callback_mode_process**()

Sets the processing timing for the Modifier.

---

[float](class_float.md#class-float) **motion_scale** = `1.0`

-  **set_motion_scale**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_motion_scale**()

Multiplies the 3D position track animation.

**Note:** Unless this value is `1.0`, the key value in animation will not match the actual position value.

---

[bool](class_bool.md#class-bool) **show_rest_only** = `false`

-  **set_show_rest_only**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_show_rest_only**()

If `true`, forces the bones in their default rest pose, regardless of their values. In the editor, this also prevents the bones from being edited.

---

## Method Descriptions

[int](class_int.md#class-int) **add_bone**(name: [String](class_string.md#class-string))

Adds a new bone with the given name. Returns the new bone's index, or `-1` if this method fails.

**Note:** Bone names should be unique, non empty, and cannot include the `:` and `/` characters.

---

 **advance**(delta: [float](class_float.md#class-float))

Manually advance the child [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d)s by the specified time (in seconds).

**Note:** The `delta` is temporarily accumulated in the **Skeleton3D**, and the deferred process uses the accumulated value to process the modification.

---

 **clear_bones**()

Clear all the bones in this skeleton.

---

 **clear_bones_global_pose_override**()

**Deprecated:** This method may be changed or removed in future versions.

Removes the global pose override on all bones in the skeleton.

---

[Skin](class_skin.md#class-skin) **create_skin_from_rest_transforms**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[int](class_int.md#class-int) **find_bone**(name: [String](class_string.md#class-string))

Returns the bone index that matches `name` as its name. Returns `-1` if no bone with this name exists.

---

 **force_update_all_bone_transforms**()

**Deprecated:** This method should only be called internally.

Force updates the bone transforms/poses for all bones in the skeleton.

---

 **force_update_bone_child_transform**(bone_idx: [int](class_int.md#class-int))

Force updates the bone transform for the bone at `bone_idx` and all of its children.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_bone_children**(bone_idx: [int](class_int.md#class-int))

Returns an array containing the bone indexes of all the child node of the passed in bone, `bone_idx`.

---

[int](class_int.md#class-int) **get_bone_count**()

Returns the number of bones in the skeleton.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_bone_global_pose**(bone_idx: [int](class_int.md#class-int))

Returns the overall transform of the specified bone, with respect to the skeleton. Being relative to the skeleton frame, this is not the actual "global" transform of the bone.

**Note:** This is the global pose you set to the skeleton in the process, the final global pose can get overridden by modifiers in the deferred process, if you want to access the final global pose, use [SkeletonModifier3D.modification_processed](class_skeletonmodifier3d.md#class-skeletonmodifier3d-signal-modification-processed).

---

[Transform3D](class_transform3d.md#class-transform3d) **get_bone_global_pose_no_override**(bone_idx: [int](class_int.md#class-int))

**Deprecated:** This method may be changed or removed in future versions.

Returns the overall transform of the specified bone, with respect to the skeleton, but without any global pose overrides. Being relative to the skeleton frame, this is not the actual "global" transform of the bone.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_bone_global_pose_override**(bone_idx: [int](class_int.md#class-int))

**Deprecated:** This method may be changed or removed in future versions.

Returns the global pose override transform for `bone_idx`.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_bone_global_rest**(bone_idx: [int](class_int.md#class-int))

Returns the global rest transform for `bone_idx`.

---

[Variant](class_variant.md#class-variant) **get_bone_meta**(bone_idx: [int](class_int.md#class-int), key: [StringName](class_stringname.md#class-stringname))

Returns the metadata with the given `key` for the bone at index `bone_idx`.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_bone_meta_list**(bone_idx: [int](class_int.md#class-int))

Returns the list of all metadata keys for the bone at index `bone_idx`.

---

[String](class_string.md#class-string) **get_bone_name**(bone_idx: [int](class_int.md#class-int))

Returns the name of the bone at index `bone_idx`.

---

[int](class_int.md#class-int) **get_bone_parent**(bone_idx: [int](class_int.md#class-int))

Returns the bone index which is the parent of the bone at `bone_idx`. If -1, then bone has no parent.

**Note:** The parent bone returned will always be less than `bone_idx`.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_bone_pose**(bone_idx: [int](class_int.md#class-int))

Returns the pose transform of the specified bone.

**Note:** This is the pose you set to the skeleton in the process, the final pose can get overridden by modifiers in the deferred process, if you want to access the final pose, use [SkeletonModifier3D.modification_processed](class_skeletonmodifier3d.md#class-skeletonmodifier3d-signal-modification-processed).

---

[Vector3](class_vector3.md#class-vector3) **get_bone_pose_position**(bone_idx: [int](class_int.md#class-int))

Returns the pose position of the bone at `bone_idx`. The returned [Vector3](class_vector3.md#class-vector3) is in the local coordinate space of the **Skeleton3D** node.

---

[Quaternion](class_quaternion.md#class-quaternion) **get_bone_pose_rotation**(bone_idx: [int](class_int.md#class-int))

Returns the pose rotation of the bone at `bone_idx`. The returned [Quaternion](class_quaternion.md#class-quaternion) is local to the bone with respect to the rotation of any parent bones.

---

[Vector3](class_vector3.md#class-vector3) **get_bone_pose_scale**(bone_idx: [int](class_int.md#class-int))

Returns the pose scale of the bone at `bone_idx`.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_bone_rest**(bone_idx: [int](class_int.md#class-int))

Returns the rest transform for a bone `bone_idx`.

---

[StringName](class_stringname.md#class-stringname) **get_concatenated_bone_names**()

Returns all bone names concatenated with commas (`,`) as a single [StringName](class_stringname.md#class-stringname).

It is useful to set it as a hint for the enum property.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_parentless_bones**()

Returns an array with all of the bones that are parentless. Another way to look at this is that it returns the indexes of all the bones that are not dependent or modified by other bones in the Skeleton.

---

[int](class_int.md#class-int) **get_version**()

Returns the number of times the bone hierarchy has changed within this skeleton, including renames.

The Skeleton version is not serialized: only use within a single instance of Skeleton3D.

Use for invalidating caches in IK solvers and other nodes which process bones.

---

[bool](class_bool.md#class-bool) **has_bone_meta**(bone_idx: [int](class_int.md#class-int), key: [StringName](class_stringname.md#class-stringname))

Returns `true` if the bone at index `bone_idx` has metadata with the given `key`.

---

[bool](class_bool.md#class-bool) **is_bone_enabled**(bone_idx: [int](class_int.md#class-int))

Returns whether the bone pose for the bone at `bone_idx` is enabled.

---

 **localize_rests**()

Returns all bones in the skeleton to their rest poses.

---

 **physical_bones_add_collision_exception**(exception: [RID](class_rid.md#class-rid))

**Deprecated:** This method may be changed or removed in future versions.

Adds a collision exception to the physical bone.

Works just like the [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) node.

---

 **physical_bones_remove_collision_exception**(exception: [RID](class_rid.md#class-rid))

**Deprecated:** This method may be changed or removed in future versions.

Removes a collision exception to the physical bone.

Works just like the [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) node.

---

 **physical_bones_start_simulation**(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = [])

**Deprecated:** This method may be changed or removed in future versions.

Tells the [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) nodes in the Skeleton to start simulating and reacting to the physics world.

Optionally, a list of bone names can be passed-in, allowing only the passed-in bones to be simulated.

---

 **physical_bones_stop_simulation**()

**Deprecated:** This method may be changed or removed in future versions.

Tells the [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) nodes in the Skeleton to stop simulating.

---

[SkinReference](class_skinreference.md#class-skinreference) **register_skin**(skin: [Skin](class_skin.md#class-skin))

Binds the given Skin to the Skeleton.

---

 **reset_bone_pose**(bone_idx: [int](class_int.md#class-int))

Sets the bone pose to rest for `bone_idx`.

---

 **reset_bone_poses**()

Sets all bone poses to rests.

---

 **set_bone_enabled**(bone_idx: [int](class_int.md#class-int), enabled: [bool](class_bool.md#class-bool) = true)

Disables the pose for the bone at `bone_idx` if `false`, enables the bone pose if `true`.

---

 **set_bone_global_pose**(bone_idx: [int](class_int.md#class-int), pose: [Transform3D](class_transform3d.md#class-transform3d))

Sets the global pose transform, `pose`, for the bone at `bone_idx`.

**Note:** If other bone poses have been changed, this method executes a dirty poses recalculation and will cause performance to deteriorate. If you know that multiple global poses will be applied, consider using set_bone_pose() with precalculation.

---

 **set_bone_global_pose_override**(bone_idx: [int](class_int.md#class-int), pose: [Transform3D](class_transform3d.md#class-transform3d), amount: [float](class_float.md#class-float), persistent: [bool](class_bool.md#class-bool) = false)

**Deprecated:** This method may be changed or removed in future versions.

Sets the global pose transform, `pose`, for the bone at `bone_idx`.

`amount` is the interpolation strength that will be used when applying the pose, and `persistent` determines if the applied pose will remain.

**Note:** The pose transform needs to be a global pose! To convert a world transform from a [Node3D](class_node3d.md#class-node3d) to a global bone pose, multiply the [Transform3D.affine_inverse()](class_transform3d.md#class-transform3d-method-affine-inverse) of the node's [Node3D.global_transform](class_node3d.md#class-node3d-property-global-transform) by the desired world transform.

---

 **set_bone_meta**(bone_idx: [int](class_int.md#class-int), key: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Sets the metadata with the given `key` to `value` for the bone at index `bone_idx`.

---

 **set_bone_name**(bone_idx: [int](class_int.md#class-int), name: [String](class_string.md#class-string))

Sets the bone name, `name`, for the bone at `bone_idx`.

---

 **set_bone_parent**(bone_idx: [int](class_int.md#class-int), parent_idx: [int](class_int.md#class-int))

Sets the bone index `parent_idx` as the parent of the bone at `bone_idx`. If -1, then bone has no parent.

**Note:** `parent_idx` must be less than `bone_idx`.

---

 **set_bone_pose**(bone_idx: [int](class_int.md#class-int), pose: [Transform3D](class_transform3d.md#class-transform3d))

Sets the pose transform, `pose`, for the bone at `bone_idx`.

---

 **set_bone_pose_position**(bone_idx: [int](class_int.md#class-int), position: [Vector3](class_vector3.md#class-vector3))

Sets the pose position of the bone at `bone_idx` to `position`. `position` is a [Vector3](class_vector3.md#class-vector3) describing a position local to the **Skeleton3D** node.

---

 **set_bone_pose_rotation**(bone_idx: [int](class_int.md#class-int), rotation: [Quaternion](class_quaternion.md#class-quaternion))

Sets the pose rotation of the bone at `bone_idx` to `rotation`. `rotation` is a [Quaternion](class_quaternion.md#class-quaternion) describing a rotation in the bone's local coordinate space with respect to the rotation of any parent bones.

---

 **set_bone_pose_scale**(bone_idx: [int](class_int.md#class-int), scale: [Vector3](class_vector3.md#class-vector3))

Sets the pose scale of the bone at `bone_idx` to `scale`.

---

 **set_bone_rest**(bone_idx: [int](class_int.md#class-int), rest: [Transform3D](class_transform3d.md#class-transform3d))

Sets the rest transform for bone `bone_idx`.

---

 **unparent_bone_and_rest**(bone_idx: [int](class_int.md#class-int))

Unparents the bone at `bone_idx` and sets its rest position to that of its parent prior to being reset.
