# SceneTree

**Inherits:** [MainLoop](class_mainloop.md#class-mainloop) **<** [Object](class_object.md#class-object)

Manages the game loop via a hierarchy of nodes.

## Description

As one of the most important classes, the **SceneTree** manages the hierarchy of nodes in a scene, as well as scenes themselves. Nodes can be added, fetched and removed. The whole scene tree (and thus the current scene) can be paused. Scenes can be loaded, switched and reloaded.

You can also use the **SceneTree** to organize your nodes into **groups**: every node can be added to as many groups as you want to create, e.g. an "enemy" group. You can then iterate these groups or even call methods and set properties on all the nodes belonging to any given group.

**SceneTree** is the default [MainLoop](class_mainloop.md#class-mainloop) implementation used by the engine, and is thus in charge of the game loop.

## Tutorials

- [SceneTree](../tutorials/scripting/scene_tree.md)
- [Multiple resolutions](../tutorials/rendering/multiple_resolutions.md)

## Properties

| [bool](class_bool.md#class-bool)       | auto_accept_quit           | `true`   |
|----------------------------------------|--------------------------------------------------------------------------|----------|
| [Node](class_node.md#class-node)       | current_scene                 |          |
| [bool](class_bool.md#class-bool)       | debug_collisions_hint | `false`  |
| [bool](class_bool.md#class-bool)       | debug_navigation_hint | `false`  |
| [bool](class_bool.md#class-bool)       | debug_paths_hint           | `false`  |
| [Node](class_node.md#class-node)       | edited_scene_root         |          |
| [bool](class_bool.md#class-bool)       | multiplayer_poll           | `true`   |
| [bool](class_bool.md#class-bool)       | paused                               | `false`  |
| [bool](class_bool.md#class-bool)       | physics_interpolation | `false`  |
| [bool](class_bool.md#class-bool)       | quit_on_go_back             | `true`   |
| [Window](class_window.md#class-window) | root                                   |          |

## Methods

|                                                                          | call_group(group: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), ...)                                                                                                            |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                          | call_group_flags(flags: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), ...)                                                          |
| [Error](class_@globalscope.md#enum-globalscope-error)                    | change_scene_to_file(path: [String](class_string.md#class-string))                                                                                                                                                                      |
| [Error](class_@globalscope.md#enum-globalscope-error)                    | change_scene_to_node(node: [Node](class_node.md#class-node))                                                                                                                                                                            |
| [Error](class_@globalscope.md#enum-globalscope-error)                    | change_scene_to_packed(packed_scene: [PackedScene](class_packedscene.md#class-packedscene))                                                                                                                                           |
| [SceneTreeTimer](class_scenetreetimer.md#class-scenetreetimer)           | create_timer(time_sec: [float](class_float.md#class-float), process_always: [bool](class_bool.md#class-bool) = true, process_in_physics: [bool](class_bool.md#class-bool) = false, ignore_time_scale: [bool](class_bool.md#class-bool) = false) |
| [Tween](class_tween.md#class-tween)                                      | create_tween()                                                                                                                                                                                                                                  |
| [Node](class_node.md#class-node)                                         | get_first_node_in_group(group: [StringName](class_stringname.md#class-stringname))                                                                                                                                                   |
| [int](class_int.md#class-int)                                            | get_frame()                                                                                                                                                                                                                                        |
| [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi)           | get_multiplayer(for_path: [NodePath](class_nodepath.md#class-nodepath) = NodePath(""))                                                                                                                                                       |
| [int](class_int.md#class-int)                                            | get_node_count()                                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                            | get_node_count_in_group(group: [StringName](class_stringname.md#class-stringname))                                                                                                                                                   |
| [Array](class_array.md#class-array)[[Node](class_node.md#class-node)]    | get_nodes_in_group(group: [StringName](class_stringname.md#class-stringname))                                                                                                                                                             |
| [Array](class_array.md#class-array)[[Tween](class_tween.md#class-tween)] | get_processed_tweens()                                                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                         | has_group(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                         | is_accessibility_enabled()                                                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                         | is_accessibility_supported()                                                                                                                                                                                                      |
|                                                                          | notify_group(group: [StringName](class_stringname.md#class-stringname), notification: [int](class_int.md#class-int))                                                                                                                            |
|                                                                          | notify_group_flags(call_flags: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname), notification: [int](class_int.md#class-int))                                                                     |
|                                                                          | queue_delete(obj: [Object](class_object.md#class-object))                                                                                                                                                                                       |
|                                                                          | quit(exit_code: [int](class_int.md#class-int) = 0)                                                                                                                                                                                                      |
| [Error](class_@globalscope.md#enum-globalscope-error)                    | reload_current_scene()                                                                                                                                                                                                                  |
|                                                                          | set_group(group: [StringName](class_stringname.md#class-stringname), property: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))                                                                           |
|                                                                          | set_group_flags(call_flags: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname), property: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))                    |
|                                                                          | set_multiplayer(multiplayer: [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi), root_path: [NodePath](class_nodepath.md#class-nodepath) = NodePath(""))                                                                         |
|                                                                          | unload_current_scene()                                                                                                                                                                                                                  |

---

## Signals

**node_added**(node: [Node](class_node.md#class-node))

Emitted when the `node` enters this tree.

---

**node_configuration_warning_changed**(node: [Node](class_node.md#class-node))

Emitted when the `node`'s [Node.update_configuration_warnings()](class_node.md#class-node-method-update-configuration-warnings) is called. Only emitted in the editor.

---

**node_removed**(node: [Node](class_node.md#class-node))

Emitted when the `node` exits this tree.

---

**node_renamed**(node: [Node](class_node.md#class-node))

Emitted when the `node`'s [Node.name](class_node.md#class-node-property-name) is changed.

---

**physics_frame**()

Emitted immediately before [Node._physics_process()](class_node.md#class-node-private-method-physics-process) is called on every node in this tree.

---

**process_frame**()

Emitted immediately before [Node._process()](class_node.md#class-node-private-method-process) is called on every node in this tree.

---

**scene_changed**()

Emitted after the new scene is added to scene tree and initialized. Can be used to reliably access current_scene when changing scenes.

```gdscript
# This code should be inside an autoload.
get_tree().change_scene_to_file(other_scene_path)
await get_tree().scene_changed
print(get_tree().current_scene) # Prints the new scene.
```

---

**tree_changed**()

Emitted any time the tree's hierarchy changes (nodes being moved, renamed, etc.).

---

**tree_process_mode_changed**()

Emitted when the [Node.process_mode](class_node.md#class-node-property-process-mode) of any node inside the tree is changed. Only emitted in the editor, to update the visibility of disabled nodes.

---

## Enumerations

enum **GroupCallFlags**:

GroupCallFlags **GROUP_CALL_DEFAULT** = `0`

Call nodes within a group with no special behavior (default).

GroupCallFlags **GROUP_CALL_REVERSE** = `1`

Call nodes within a group in reverse tree hierarchy order (all nested children are called before their respective parent nodes).

GroupCallFlags **GROUP_CALL_DEFERRED** = `2`

Call nodes within a group at the end of the current frame (can be either process or physics frame), similar to [Object.call_deferred()](class_object.md#class-object-method-call-deferred).

GroupCallFlags **GROUP_CALL_UNIQUE** = `4`

Call nodes within a group only once, even if the call is executed many times in the same frame. Must be combined with GROUP_CALL_DEFERRED to work.

**Note:** Different arguments are not taken into account. Therefore, when the same call is executed with different arguments, only the first call will be performed.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **auto_accept_quit** = `true`

-  **set_auto_accept_quit**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_auto_accept_quit**()

If `true`, the application automatically accepts quitting requests.

For mobile platforms, see quit_on_go_back.

---

[Node](class_node.md#class-node) **current_scene**

-  **set_current_scene**(value: [Node](class_node.md#class-node))
- [Node](class_node.md#class-node) **get_current_scene**()

The root node of the currently loaded main scene, usually as a direct child of root. See also change_scene_to_file(), change_scene_to_packed(), and reload_current_scene().

**Warning:** Setting this property directly may not work as expected, as it does *not* add or remove any nodes from this tree.

---

[bool](class_bool.md#class-bool) **debug_collisions_hint** = `false`

-  **set_debug_collisions_hint**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_debugging_collisions_hint**()

If `true`, collision shapes will be visible when running the game from the editor for debugging purposes.

**Note:** This property is not designed to be changed at run-time. Changing the value of debug_collisions_hint while the project is running will not have the desired effect.

---

[bool](class_bool.md#class-bool) **debug_navigation_hint** = `false`

-  **set_debug_navigation_hint**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_debugging_navigation_hint**()

If `true`, navigation polygons will be visible when running the game from the editor for debugging purposes.

**Note:** This property is not designed to be changed at run-time. Changing the value of debug_navigation_hint while the project is running will not have the desired effect.

---

[bool](class_bool.md#class-bool) **debug_paths_hint** = `false`

-  **set_debug_paths_hint**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_debugging_paths_hint**()

If `true`, curves from [Path2D](class_path2d.md#class-path2d) and [Path3D](class_path3d.md#class-path3d) nodes will be visible when running the game from the editor for debugging purposes.

**Note:** This property is not designed to be changed at run-time. Changing the value of debug_paths_hint while the project is running will not have the desired effect.

---

[Node](class_node.md#class-node) **edited_scene_root**

-  **set_edited_scene_root**(value: [Node](class_node.md#class-node))
- [Node](class_node.md#class-node) **get_edited_scene_root**()

The root of the scene currently being edited in the editor. This is usually a direct child of root.

**Note:** This property does nothing in release builds.

---

[bool](class_bool.md#class-bool) **multiplayer_poll** = `true`

-  **set_multiplayer_poll_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_multiplayer_poll_enabled**()

If `true` (default value), enables automatic polling of the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) for this SceneTree during process_frame.

If `false`, you need to manually call [MultiplayerAPI.poll()](class_multiplayerapi.md#class-multiplayerapi-method-poll) to process network packets and deliver RPCs. This allows running RPCs in a different loop (e.g. physics, thread, specific time step) and for manual [Mutex](class_mutex.md#class-mutex) protection when accessing the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) from threads.

---

[bool](class_bool.md#class-bool) **paused** = `false`

-  **set_pause**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_paused**()

If `true`, the scene tree is considered paused. This causes the following behavior:

- 2D and 3D physics will be stopped, as well as collision detection and related signals.
- Depending on each node's [Node.process_mode](class_node.md#class-node-property-process-mode), their [Node._process()](class_node.md#class-node-private-method-process), [Node._physics_process()](class_node.md#class-node-private-method-physics-process) and [Node._input()](class_node.md#class-node-private-method-input) callback methods may not called anymore.

---

[bool](class_bool.md#class-bool) **physics_interpolation** = `false`

-  **set_physics_interpolation_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_physics_interpolation_enabled**()

If `true`, the renderer will interpolate the transforms of objects (both physics and non-physics) between the last two transforms, so that smooth motion is seen even when physics ticks do not coincide with rendered frames.

The default value of this property is controlled by [ProjectSettings.physics/common/physics_interpolation](class_projectsettings.md#class-projectsettings-property-physics-common-physics-interpolation).

**Note:** Although this is a global setting, finer control of individual branches of the **SceneTree** is possible using [Node.physics_interpolation_mode](class_node.md#class-node-property-physics-interpolation-mode).

---

[bool](class_bool.md#class-bool) **quit_on_go_back** = `true`

-  **set_quit_on_go_back**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_quit_on_go_back**()

If `true`, the application quits automatically when navigating back (e.g. using the system "Back" button on Android).

To handle 'Go Back' button when this option is disabled, use [DisplayServer.WINDOW_EVENT_GO_BACK_REQUEST](class_displayserver.md#class-displayserver-constant-window-event-go-back-request).

---

[Window](class_window.md#class-window) **root**

- [Window](class_window.md#class-window) **get_root**()

The tree's root [Window](class_window.md#class-window). This is top-most [Node](class_node.md#class-node) of the scene tree, and is always present. An absolute [NodePath](class_nodepath.md#class-nodepath) always starts from this node. Children of the root node may include the loaded current_scene, as well as any [AutoLoad](../tutorials/scripting/singletons_autoload.md) configured in the Project Settings.

**Warning:** Do not delete this node. This will result in unstable behavior, followed by a crash.

---

## Method Descriptions

 **call_group**(group: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), ...)

Calls `method` on each node inside this tree added to the given `group`. You can pass arguments to `method` by specifying them at the end of this method call. Nodes that cannot call `method` (either because the method doesn't exist or the arguments do not match) are ignored. See also set_group() and notify_group().

**Note:** This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.

**Note:** In C#, `method` must be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in the `MethodName` class to avoid allocating a new [StringName](class_stringname.md#class-stringname) on each call.

---

 **call_group_flags**(flags: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname), method: [StringName](class_stringname.md#class-stringname), ...)

Calls the given `method` on each node inside this tree added to the given `group`. Use `flags` to customize this method's behavior (see GroupCallFlags). Additional arguments for `method` can be passed at the end of this method. Nodes that cannot call `method` (either because the method doesn't exist or the arguments do not match) are ignored.

```gdscript
# Calls "hide" to all nodes of the "enemies" group, at the end of the frame and in reverse tree order.
get_tree().call_group_flags(
        SceneTree.GROUP_CALL_DEFERRED | SceneTree.GROUP_CALL_REVERSE,
        "enemies", "hide")
```

**Note:** In C#, `method` must be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in the `MethodName` class to avoid allocating a new [StringName](class_stringname.md#class-stringname) on each call.

---

[Error](class_@globalscope.md#enum-globalscope-error) **change_scene_to_file**(path: [String](class_string.md#class-string))

Changes the running scene to the one at the given `path`, after loading it into a [PackedScene](class_packedscene.md#class-packedscene) and creating a new instance.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, [@GlobalScope.ERR_CANT_OPEN](class_@globalscope.md#class-globalscope-constant-err-cant-open) if the `path` cannot be loaded into a [PackedScene](class_packedscene.md#class-packedscene), or [@GlobalScope.ERR_CANT_CREATE](class_@globalscope.md#class-globalscope-constant-err-cant-create) if that scene cannot be instantiated.

**Note:** See change_scene_to_node() for details on the order of operations.

---

[Error](class_@globalscope.md#enum-globalscope-error) **change_scene_to_node**(node: [Node](class_node.md#class-node))

Changes the running scene to the provided [Node](class_node.md#class-node). Useful when you want to set up the new scene before changing.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) if the `node` is `null`, or [@GlobalScope.ERR_UNCONFIGURED](class_@globalscope.md#class-globalscope-constant-err-unconfigured) if the `node` is already inside the scene tree.

**Note:** Operations happen in the following order when change_scene_to_node() is called:

1. The current scene node is immediately removed from the tree. From that point, [Node.get_tree()](class_node.md#class-node-method-get-tree) called on the current (outgoing) scene will return `null`. current_scene will be `null` too, because the new scene is not available yet.
2. At the end of the frame, the formerly current scene, already removed from the tree, will be deleted (freed from memory) and then the new scene node will be added to the tree. [Node.get_tree()](class_node.md#class-node-method-get-tree) and current_scene will be back to working as usual.

This ensures that both scenes aren't running at the same time, while still freeing the previous scene in a safe way similar to [Node.queue_free()](class_node.md#class-node-method-queue-free).

If you want to reliably access the new scene, await the scene_changed signal.

**Warning:** After using this method, the **SceneTree** will take ownership of the node and will free it automatically when changing scene again. Any references you had to that node will become invalid.

---

[Error](class_@globalscope.md#enum-globalscope-error) **change_scene_to_packed**(packed_scene: [PackedScene](class_packedscene.md#class-packedscene))

Changes the running scene to a new instance of the given [PackedScene](class_packedscene.md#class-packedscene) (which must be valid).

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, [@GlobalScope.ERR_CANT_CREATE](class_@globalscope.md#class-globalscope-constant-err-cant-create) if the scene cannot be instantiated, or [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) if the scene is invalid.

**Note:** See change_scene_to_node() for details on the order of operations.

---

[SceneTreeTimer](class_scenetreetimer.md#class-scenetreetimer) **create_timer**(time_sec: [float](class_float.md#class-float), process_always: [bool](class_bool.md#class-bool) = true, process_in_physics: [bool](class_bool.md#class-bool) = false, ignore_time_scale: [bool](class_bool.md#class-bool) = false)

Returns a new [SceneTreeTimer](class_scenetreetimer.md#class-scenetreetimer). After `time_sec` in seconds have passed, the timer will emit [SceneTreeTimer.timeout](class_scenetreetimer.md#class-scenetreetimer-signal-timeout) and will be automatically freed.

If `process_always` is `false`, the timer will be paused when setting paused to `true`.

If `process_in_physics` is `true`, the timer will update at the end of the physics frame, instead of the process frame.

If `ignore_time_scale` is `true`, the timer will ignore [Engine.time_scale](class_engine.md#class-engine-property-time-scale) and update with the real, elapsed time.

This method is commonly used to create a one-shot delay timer, as in the following example:

GDScript

```gdscript
func some_function():
    print("start")
    await get_tree().create_timer(1.0).timeout
    print("end")
```

C#

```csharp
public async Task SomeFunction()
{
    GD.Print("start");
    await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
    GD.Print("end");
}
```

**Note:** The timer is always updated *after* all of the nodes in the tree. A node's [Node._process()](class_node.md#class-node-private-method-process) method would be called before the timer updates (or [Node._physics_process()](class_node.md#class-node-private-method-physics-process) if `process_in_physics` is set to `true`).

---

[Tween](class_tween.md#class-tween) **create_tween**()

Creates and returns a new [Tween](class_tween.md#class-tween) processed in this tree. The Tween will start automatically on the next process frame or physics frame (depending on its [TweenProcessMode](class_tween.md#enum-tween-tweenprocessmode)).

**Note:** A [Tween](class_tween.md#class-tween) created using this method is not bound to any [Node](class_node.md#class-node). It may keep working until there is nothing left to animate. If you want the [Tween](class_tween.md#class-tween) to be automatically killed when the [Node](class_node.md#class-node) is freed, use [Node.create_tween()](class_node.md#class-node-method-create-tween) or [Tween.bind_node()](class_tween.md#class-tween-method-bind-node).

---

[Node](class_node.md#class-node) **get_first_node_in_group**(group: [StringName](class_stringname.md#class-stringname))

Returns the first [Node](class_node.md#class-node) found inside the tree, that has been added to the given `group`, in scene hierarchy order. Returns `null` if no match is found. See also get_nodes_in_group().

---

[int](class_int.md#class-int) **get_frame**()

Returns how many physics process steps have been processed, since the application started. This is *not* a measurement of elapsed time. See also physics_frame. For the number of frames rendered, see [Engine.get_process_frames()](class_engine.md#class-engine-method-get-process-frames).

---

[MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) **get_multiplayer**(for_path: [NodePath](class_nodepath.md#class-nodepath) = NodePath(""))

Searches for the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) configured for the given path, if one does not exist it searches the parent paths until one is found. If the path is empty, or none is found, the default one is returned. See set_multiplayer().

---

[int](class_int.md#class-int) **get_node_count**()

Returns the number of nodes inside this tree.

---

[int](class_int.md#class-int) **get_node_count_in_group**(group: [StringName](class_stringname.md#class-stringname))

Returns the number of nodes assigned to the given group.

---

[Array](class_array.md#class-array)[[Node](class_node.md#class-node)] **get_nodes_in_group**(group: [StringName](class_stringname.md#class-stringname))

Returns an [Array](class_array.md#class-array) containing all nodes inside this tree, that have been added to the given `group`, in scene hierarchy order.

---

[Array](class_array.md#class-array)[[Tween](class_tween.md#class-tween)] **get_processed_tweens**()

Returns an [Array](class_array.md#class-array) of currently existing [Tween](class_tween.md#class-tween)s in the tree, including paused tweens.

---

[bool](class_bool.md#class-bool) **has_group**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if a node added to the given group `name` exists in the tree.

---

[bool](class_bool.md#class-bool) **is_accessibility_enabled**()

Returns `true` if accessibility features are enabled, and accessibility information updates are actively processed.

---

[bool](class_bool.md#class-bool) **is_accessibility_supported**()

Returns `true` if accessibility features are supported by the OS and enabled in project settings.

---

 **notify_group**(group: [StringName](class_stringname.md#class-stringname), notification: [int](class_int.md#class-int))

Calls [Object.notification()](class_object.md#class-object-method-notification) with the given `notification` to all nodes inside this tree added to the `group`. See also [Godot notifications](../tutorials/best_practices/godot_notifications.md) and call_group() and set_group().

**Note:** This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.

---

 **notify_group_flags**(call_flags: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname), notification: [int](class_int.md#class-int))

Calls [Object.notification()](class_object.md#class-object-method-notification) with the given `notification` to all nodes inside this tree added to the `group`. Use `call_flags` to customize this method's behavior (see GroupCallFlags).

---

 **queue_delete**(obj: [Object](class_object.md#class-object))

Queues the given `obj` to be deleted, calling its [Object.free()](class_object.md#class-object-method-free) at the end of the current frame. This method is similar to [Node.queue_free()](class_node.md#class-node-method-queue-free).

---

 **quit**(exit_code: [int](class_int.md#class-int) = 0)

Quits the application at the end of the current iteration, with the given `exit_code`.

By convention, an exit code of `0` indicates success, whereas any other exit code indicates an error. For portability reasons, it should be between `0` and `125` (inclusive).

**Note:** On iOS this method doesn't work. Instead, as recommended by the [iOS Human Interface Guidelines](https://developer.apple.com/library/archive/qa/qa1561/_index.html), the user is expected to close apps via the Home button.

---

[Error](class_@globalscope.md#enum-globalscope-error) **reload_current_scene**()

Reloads the currently active scene, replacing current_scene with a new instance of its original [PackedScene](class_packedscene.md#class-packedscene).

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, [@GlobalScope.ERR_UNCONFIGURED](class_@globalscope.md#class-globalscope-constant-err-unconfigured) if no current_scene is defined, [@GlobalScope.ERR_CANT_OPEN](class_@globalscope.md#class-globalscope-constant-err-cant-open) if current_scene cannot be loaded into a [PackedScene](class_packedscene.md#class-packedscene), or [@GlobalScope.ERR_CANT_CREATE](class_@globalscope.md#class-globalscope-constant-err-cant-create) if the scene cannot be instantiated.

---

 **set_group**(group: [StringName](class_stringname.md#class-stringname), property: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))

Sets the given `property` to `value` on all nodes inside this tree added to the given `group`. Nodes that do not have the `property` are ignored. See also call_group() and notify_group().

**Note:** This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.

**Note:** In C#, `property` must be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in the `PropertyName` class to avoid allocating a new [StringName](class_stringname.md#class-stringname) on each call.

---

 **set_group_flags**(call_flags: [int](class_int.md#class-int), group: [StringName](class_stringname.md#class-stringname), property: [String](class_string.md#class-string), value: [Variant](class_variant.md#class-variant))

Sets the given `property` to `value` on all nodes inside this tree added to the given `group`. Nodes that do not have the `property` are ignored. Use `call_flags` to customize this method's behavior (see GroupCallFlags).

**Note:** In C#, `property` must be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in the `PropertyName` class to avoid allocating a new [StringName](class_stringname.md#class-stringname) on each call.

---

 **set_multiplayer**(multiplayer: [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi), root_path: [NodePath](class_nodepath.md#class-nodepath) = NodePath(""))

Sets a custom [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) with the given `root_path` (controlling also the relative subpaths), or override the default one if `root_path` is empty.

**Note:** No [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) must be configured for the subpath containing `root_path`, nested custom multiplayers are not allowed. I.e. if one is configured for `"/root/Foo"` setting one for `"/root/Foo/Bar"` will cause an error.

**Note:** set_multiplayer() should be called *before* the child nodes are ready at the given `root_path`. If multiplayer nodes like [MultiplayerSpawner](class_multiplayerspawner.md#class-multiplayerspawner) or [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer) are added to the tree before the custom multiplayer API is set, they will not work.

---

 **unload_current_scene**()

If a current scene is loaded, calling this method will unload it.
