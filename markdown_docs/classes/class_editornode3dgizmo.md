# EditorNode3DGizmo

**Inherits:** [Node3DGizmo](class_node3dgizmo.md#class-node3dgizmo) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Gizmo for editing [Node3D](class_node3d.md#class-node3d) objects.

## Description

Gizmo that is used for providing custom visualization and editing (handles and subgizmos) for [Node3D](class_node3d.md#class-node3d) objects. Can be overridden to create custom gizmos, but for simple gizmos creating an [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin) is usually recommended.

## Methods

|                                                                                           | \_begin_handle_action(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                           | \_commit_handle(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool), restore: [Variant](class_variant.md#class-variant), cancel: [bool](class_bool.md#class-bool))                                                                                                                                       |
|                                                                                           | \_commit_subgizmos(ids: [PackedInt32Array](class_packedint32array.md#class-packedint32array), restores: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)], cancel: [bool](class_bool.md#class-bool))                                                                                    |
| [String](class_string.md#class-string)                                                    | \_get_handle_name(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                 |
| [Variant](class_variant.md#class-variant)                                                 | \_get_handle_value(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                               |
| [Transform3D](class_transform3d.md#class-transform3d)                                     | \_get_subgizmo_transform(id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                          | \_is_handle_highlighted(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                     |
|                                                                                           | \_redraw()                                                                                                                                                                                                                                                                                                                                 |
|                                                                                           | \_set_handle(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool), camera: [Camera3D](class_camera3d.md#class-camera3d), point: [Vector2](class_vector2.md#class-vector2))                                                                                                                                   |
|                                                                                           | \_set_subgizmo_transform(id: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))                                                                                                                                                                                              |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                      | \_subgizmos_intersect_frustum(camera: [Camera3D](class_camera3d.md#class-camera3d), frustum: [Array](class_array.md#class-array)[[Plane](class_plane.md#class-plane)])                                                                                                                                                |
| [int](class_int.md#class-int)                                                             | \_subgizmos_intersect_ray(camera: [Camera3D](class_camera3d.md#class-camera3d), point: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                         |
|                                                                                           | add_collision_segments(segments: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))                                                                                                                                                                                                                       |
|                                                                                           | add_collision_triangles(triangles: [TriangleMesh](class_trianglemesh.md#class-trianglemesh))                                                                                                                                                                                                                                      |
|                                                                                           | add_handles(handles: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), material: [Material](class_material.md#class-material), ids: [PackedInt32Array](class_packedint32array.md#class-packedint32array), billboard: [bool](class_bool.md#class-bool) = false, secondary: [bool](class_bool.md#class-bool) = false) |
|                                                                                           | add_lines(lines: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), material: [Material](class_material.md#class-material), billboard: [bool](class_bool.md#class-bool) = false, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1))                                                                    |
|                                                                                           | add_mesh(mesh: [Mesh](class_mesh.md#class-mesh), material: [Material](class_material.md#class-material) = null, transform: [Transform3D](class_transform3d.md#class-transform3d) = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), skeleton: [SkinReference](class_skinreference.md#class-skinreference) = null)                                |
|                                                                                           | add_unscaled_billboard(material: [Material](class_material.md#class-material), default_scale: [float](class_float.md#class-float) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1))                                                                                                                          |
|                                                                                           | clear()                                                                                                                                                                                                                                                                                                                                             |
| [Node3D](class_node3d.md#class-node3d)                                                    | get_node_3d()                                                                                                                                                                                                                                                                                                                                 |
| [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin) | get_plugin()                                                                                                                                                                                                                                                                                                                                   |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)                      | get_subgizmo_selection()                                                                                                                                                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                          | is_subgizmo_selected(id: [int](class_int.md#class-int))                                                                                                                                                                                                                                                                              |
|                                                                                           | set_hidden(hidden: [bool](class_bool.md#class-bool))                                                                                                                                                                                                                                                                                           |
|                                                                                           | set_node_3d(node: [Node](class_node.md#class-node))                                                                                                                                                                                                                                                                                           |

---

## Method Descriptions

 **\_begin_handle_action**(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **\_commit_handle**(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool), restore: [Variant](class_variant.md#class-variant), cancel: [bool](class_bool.md#class-bool))

Override this method to commit a handle being edited (handles must have been previously added by add_handles()). This usually means creating an [UndoRedo](class_undoredo.md#class-undoredo) action for the change, using the current handle value as "do" and the `restore` argument as "undo".

If the `cancel` argument is `true`, the `restore` value should be directly set, without any [UndoRedo](class_undoredo.md#class-undoredo) action.

The `secondary` argument is `true` when the committed handle is secondary (see add_handles() for more information).

---

 **\_commit_subgizmos**(ids: [PackedInt32Array](class_packedint32array.md#class-packedint32array), restores: [Array](class_array.md#class-array)[[Transform3D](class_transform3d.md#class-transform3d)], cancel: [bool](class_bool.md#class-bool))

Override this method to commit a group of subgizmos being edited (see \_subgizmos_intersect_ray() and \_subgizmos_intersect_frustum()). This usually means creating an [UndoRedo](class_undoredo.md#class-undoredo) action for the change, using the current transforms as "do" and the `restores` transforms as "undo".

If the `cancel` argument is `true`, the `restores` transforms should be directly set, without any [UndoRedo](class_undoredo.md#class-undoredo) action.

---

[String](class_string.md#class-string) **\_get_handle_name**(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool))

Override this method to return the name of an edited handle (handles must have been previously added by add_handles()). Handles can be named for reference to the user when editing.

The `secondary` argument is `true` when the requested handle is secondary (see add_handles() for more information).

---

[Variant](class_variant.md#class-variant) **\_get_handle_value**(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool))

Override this method to return the current value of a handle. This value will be requested at the start of an edit and used as the `restore` argument in \_commit_handle().

The `secondary` argument is `true` when the requested handle is secondary (see add_handles() for more information).

---

[Transform3D](class_transform3d.md#class-transform3d) **\_get_subgizmo_transform**(id: [int](class_int.md#class-int))

Override this method to return the current transform of a subgizmo. This transform will be requested at the start of an edit and used as the `restore` argument in \_commit_subgizmos().

---

[bool](class_bool.md#class-bool) **\_is_handle_highlighted**(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool))

Override this method to return `true` whenever the given handle should be highlighted in the editor.

The `secondary` argument is `true` when the requested handle is secondary (see add_handles() for more information).

---

 **\_redraw**()

Override this method to add all the gizmo elements whenever a gizmo update is requested. It's common to call clear() at the beginning of this method and then add visual elements depending on the node's properties.

---

 **\_set_handle**(id: [int](class_int.md#class-int), secondary: [bool](class_bool.md#class-bool), camera: [Camera3D](class_camera3d.md#class-camera3d), point: [Vector2](class_vector2.md#class-vector2))

Override this method to update the node properties when the user drags a gizmo handle (previously added with add_handles()). The provided `point` is the mouse position in screen coordinates and the `camera` can be used to convert it to raycasts.

The `secondary` argument is `true` when the edited handle is secondary (see add_handles() for more information).

---

 **\_set_subgizmo_transform**(id: [int](class_int.md#class-int), transform: [Transform3D](class_transform3d.md#class-transform3d))

Override this method to update the node properties during subgizmo editing (see \_subgizmos_intersect_ray() and \_subgizmos_intersect_frustum()). The `transform` is given in the [Node3D](class_node3d.md#class-node3d)'s local coordinate system.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **\_subgizmos_intersect_frustum**(camera: [Camera3D](class_camera3d.md#class-camera3d), frustum: [Array](class_array.md#class-array)[[Plane](class_plane.md#class-plane)])

Override this method to allow selecting subgizmos using mouse drag box selection. Given a `camera` and a `frustum`, this method should return which subgizmos are contained within the frustum. The `frustum` argument consists of an array with all the [Plane](class_plane.md#class-plane)s that make up the selection frustum. The returned value should contain a list of unique subgizmo identifiers, which can have any non-negative value and will be used in other virtual methods like \_get_subgizmo_transform() or \_commit_subgizmos().

---

[int](class_int.md#class-int) **\_subgizmos_intersect_ray**(camera: [Camera3D](class_camera3d.md#class-camera3d), point: [Vector2](class_vector2.md#class-vector2))

Override this method to allow selecting subgizmos using mouse clicks. Given a `camera` and a `point` in screen coordinates, this method should return which subgizmo should be selected. The returned value should be a unique subgizmo identifier, which can have any non-negative value and will be used in other virtual methods like \_get_subgizmo_transform() or \_commit_subgizmos().

---

 **add_collision_segments**(segments: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array))

Adds the specified `segments` to the gizmo's collision shape for picking. Call this method during \_redraw().

---

 **add_collision_triangles**(triangles: [TriangleMesh](class_trianglemesh.md#class-trianglemesh))

Adds collision triangles to the gizmo for picking. A [TriangleMesh](class_trianglemesh.md#class-trianglemesh) can be generated from a regular [Mesh](class_mesh.md#class-mesh) too. Call this method during \_redraw().

---

 **add_handles**(handles: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), material: [Material](class_material.md#class-material), ids: [PackedInt32Array](class_packedint32array.md#class-packedint32array), billboard: [bool](class_bool.md#class-bool) = false, secondary: [bool](class_bool.md#class-bool) = false)

Adds a list of handles (points) which can be used to edit the properties of the gizmo's [Node3D](class_node3d.md#class-node3d). The `ids` argument can be used to specify a custom identifier for each handle, if an empty array is passed, the ids will be assigned automatically from the `handles` argument order.

The `secondary` argument marks the added handles as secondary, meaning they will normally have lower selection priority than regular handles. When the user is holding the shift key secondary handles will switch to have higher priority than regular handles. This change in priority can be used to place multiple handles at the same point while still giving the user control on their selection.

There are virtual methods which will be called upon editing of these handles. Call this method during \_redraw().

---

 **add_lines**(lines: [PackedVector3Array](class_packedvector3array.md#class-packedvector3array), material: [Material](class_material.md#class-material), billboard: [bool](class_bool.md#class-bool) = false, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1))

Adds lines to the gizmo (as sets of 2 points), with a given material. The lines are used for visualizing the gizmo. Call this method during \_redraw().

---

 **add_mesh**(mesh: [Mesh](class_mesh.md#class-mesh), material: [Material](class_material.md#class-material) = null, transform: [Transform3D](class_transform3d.md#class-transform3d) = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), skeleton: [SkinReference](class_skinreference.md#class-skinreference) = null)

Adds a mesh to the gizmo with the specified `material`, local `transform` and `skeleton`. Call this method during \_redraw().

---

 **add_unscaled_billboard**(material: [Material](class_material.md#class-material), default_scale: [float](class_float.md#class-float) = 1, modulate: [Color](class_color.md#class-color) = Color(1, 1, 1, 1))

Adds an unscaled billboard for visualization and selection. Call this method during \_redraw().

---

 **clear**()

Removes everything in the gizmo including meshes, collisions and handles.

---

[Node3D](class_node3d.md#class-node3d) **get_node_3d**()

Returns the [Node3D](class_node3d.md#class-node3d) node associated with this gizmo.

---

[EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin) **get_plugin**()

Returns the [EditorNode3DGizmoPlugin](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin) that owns this gizmo. It's useful to retrieve materials using [EditorNode3DGizmoPlugin.get_material()](class_editornode3dgizmoplugin.md#class-editornode3dgizmoplugin-method-get-material).

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_subgizmo_selection**()

Returns a list of the currently selected subgizmos. Can be used to highlight selected elements during \_redraw().

---

[bool](class_bool.md#class-bool) **is_subgizmo_selected**(id: [int](class_int.md#class-int))

Returns `true` if the given subgizmo is currently selected. Can be used to highlight selected elements during \_redraw().

---

 **set_hidden**(hidden: [bool](class_bool.md#class-bool))

Sets the gizmo's hidden state. If `true`, the gizmo will be hidden. If `false`, it will be shown.

---

 **set_node_3d**(node: [Node](class_node.md#class-node))

Sets the reference [Node3D](class_node3d.md#class-node3d) node for the gizmo. `node` must inherit from [Node3D](class_node3d.md#class-node3d).
