# Node

**Inherits:** [Object](class_object.md#class-object)

**Inherited By:** [AnimationMixer](class_animationmixer.md#class-animationmixer), [AudioStreamPlayer](class_audiostreamplayer.md#class-audiostreamplayer), [CanvasItem](class_canvasitem.md#class-canvasitem), [CanvasLayer](class_canvaslayer.md#class-canvaslayer), [EditorFileSystem](class_editorfilesystem.md#class-editorfilesystem), [EditorPlugin](class_editorplugin.md#class-editorplugin), [EditorResourcePreview](class_editorresourcepreview.md#class-editorresourcepreview), [HTTPRequest](class_httprequest.md#class-httprequest), [InstancePlaceholder](class_instanceplaceholder.md#class-instanceplaceholder), [MissingNode](class_missingnode.md#class-missingnode), [MultiplayerSpawner](class_multiplayerspawner.md#class-multiplayerspawner), [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer), [NavigationAgent2D](class_navigationagent2d.md#class-navigationagent2d), [NavigationAgent3D](class_navigationagent3d.md#class-navigationagent3d), [Node3D](class_node3d.md#class-node3d), [ResourcePreloader](class_resourcepreloader.md#class-resourcepreloader), [ShaderGlobalsOverride](class_shaderglobalsoverride.md#class-shaderglobalsoverride), [StatusIndicator](class_statusindicator.md#class-statusindicator), [Timer](class_timer.md#class-timer), [Viewport](class_viewport.md#class-viewport), [WorldEnvironment](class_worldenvironment.md#class-worldenvironment)

Base class for all scene objects.

## Description

Nodes are Godot's building blocks. They can be assigned as the child of another node, resulting in a tree arrangement. A given node can contain any number of nodes as children with the requirement that all siblings (direct children of a node) should have unique names.

A tree of nodes is called a *scene*. Scenes can be saved to the disk and then instantiated into other scenes. This allows for very high flexibility in the architecture and data model of Godot projects.

**Scene tree:** The [SceneTree](class_scenetree.md#class-scenetree) contains the active tree of nodes. When a node is added to the scene tree, it receives the NOTIFICATION_ENTER_TREE notification and its \_enter_tree() callback is triggered. Child nodes are always added *after* their parent node, i.e. the \_enter_tree() callback of a parent node will be triggered before its child's.

Once all nodes have been added in the scene tree, they receive the NOTIFICATION_READY notification and their respective \_ready() callbacks are triggered. For groups of nodes, the \_ready() callback is called in reverse order, starting with the children and moving up to the parent nodes.

This means that when adding a node to the scene tree, the following order will be used for the callbacks: \_enter_tree() of the parent, \_enter_tree() of the children, \_ready() of the children and finally \_ready() of the parent (recursively for the entire scene tree).

**Processing:** Nodes can override the "process" state, so that they receive a callback on each frame requesting them to process (do something). Normal processing (callback \_process(), toggled with set_process()) happens as fast as possible and is dependent on the frame rate, so the processing time *delta* (in seconds) is passed as an argument. Physics processing (callback \_physics_process(), toggled with set_physics_process()) happens a fixed number of times per second (60 by default) and is useful for code related to the physics engine.

Nodes can also process input events. When present, the \_input() function will be called for each input that the program receives. In many cases, this can be overkill (unless used for simple projects), and the \_unhandled_input() function might be preferred; it is called when the input event was not handled by anyone else (typically, GUI [Control](class_control.md#class-control) nodes), ensuring that the node only receives the events that were meant for it.

To keep track of the scene hierarchy (especially when instantiating scenes into other scenes), an "owner" can be set for the node with the owner property. This keeps track of who instantiated what. This is mostly useful when writing editors and tools, though.

Finally, when a node is freed with [Object.free()](class_object.md#class-object-method-free) or queue_free(), it will also free all its children.

**Groups:** Nodes can be added to as many groups as you want to be easy to manage, you could create groups like "enemies" or "collectables" for example, depending on your game. See add_to_group(), is_in_group() and remove_from_group(). You can then retrieve all nodes in these groups, iterate them and even call methods on groups via the methods on [SceneTree](class_scenetree.md#class-scenetree).

**Networking with nodes:** After connecting to a server (or making one, see [ENetMultiplayerPeer](class_enetmultiplayerpeer.md#class-enetmultiplayerpeer)), it is possible to use the built-in RPC (remote procedure call) system to communicate over the network. By calling rpc() with a method name, it will be called locally and in all connected peers (peers = clients and the server that accepts connections). To identify which node receives the RPC call, Godot will use its [NodePath](class_nodepath.md#class-nodepath) (make sure node names are the same on all peers). Also, take a look at the high-level networking tutorial and corresponding demos.

**Note:** The `script` property is part of the [Object](class_object.md#class-object) class, not **Node**. It isn't exposed like most properties but does have a setter and getter (see [Object.set_script()](class_object.md#class-object-method-set-script) and [Object.get_script()](class_object.md#class-object-method-get-script)).

## Tutorials

- [Nodes and scenes](../getting_started/step_by_step/nodes_and_scenes.md)
- [All Demos](https://github.com/godotengine/godot-demo-projects/)

## Properties

| AutoTranslateMode               | auto_translate_mode               | `0`     |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------|---------|
| [String](class_string.md#class-string)                          | editor_description                 | `""`    |
| [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi)  | multiplayer                               |         |
| [StringName](class_stringname.md#class-stringname)              | name                                             |         |
| Node                                             | owner                                           |         |
| PhysicsInterpolationMode | physics_interpolation_mode | `0`     |
| ProcessMode                           | process_mode                             | `0`     |
| [int](class_int.md#class-int)                                   | process_physics_priority     | `0`     |
| [int](class_int.md#class-int)                                   | process_priority                     | `0`     |
| ProcessThreadGroup             | process_thread_group             | `0`     |
| [int](class_int.md#class-int)                                   | process_thread_group_order |         |
| [ProcessThreadMessages]     | process_thread_messages       |         |
| [String](class_string.md#class-string)                          | scene_file_path                       |         |
| [bool](class_bool.md#class-bool)                                | unique_name_in_owner             | `false` |

## Methods

|                                                                                         | \_enter_tree()                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                         | \_exit_tree()                                                                                                                                                                                                      |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_accessibility_configuration_warnings()                                                                                                                                        |
| [PackedStringArray](class_packedstringarray.md#class-packedstringarray)                 | \_get_configuration_warnings()                                                                                                                                                                    |
| [RID](class_rid.md#class-rid)                                                           | \_get_focused_accessibility_element()                                                                                                                                                      |
|                                                                                         | \_input(event: [InputEvent](class_inputevent.md#class-inputevent))                                                                                                                                                     |
|                                                                                         | \_physics_process(delta: [float](class_float.md#class-float))                                                                                                                                                |
|                                                                                         | \_process(delta: [float](class_float.md#class-float))                                                                                                                                                                |
|                                                                                         | \_ready()                                                                                                                                                                                                              |
|                                                                                         | \_shortcut_input(event: [InputEvent](class_inputevent.md#class-inputevent))                                                                                                                                   |
|                                                                                         | \_unhandled_input(event: [InputEvent](class_inputevent.md#class-inputevent))                                                                                                                                 |
|                                                                                         | \_unhandled_key_input(event: [InputEvent](class_inputevent.md#class-inputevent))                                                                                                                         |
|                                                                                         | add_child(node: Node, force_readable_name: [bool](class_bool.md#class-bool) = false, internal: InternalMode = 0)                                                                 |
|                                                                                         | add_sibling(sibling: Node, force_readable_name: [bool](class_bool.md#class-bool) = false)                                                                                                                 |
|                                                                                         | add_to_group(group: [StringName](class_stringname.md#class-stringname), persistent: [bool](class_bool.md#class-bool) = false)                                                                                           |
| [String](class_string.md#class-string)                                                  | atr(message: [String](class_string.md#class-string), context: [StringName](class_stringname.md#class-stringname) = "")                                                                                                           |
| [String](class_string.md#class-string)                                                  | atr_n(message: [String](class_string.md#class-string), plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = "") |
| [Variant](class_variant.md#class-variant)                                               | call_deferred_thread_group(method: [StringName](class_stringname.md#class-stringname), ...)                                                                                                               |
| [Variant](class_variant.md#class-variant)                                               | call_thread_safe(method: [StringName](class_stringname.md#class-stringname), ...)                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | can_auto_translate()                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | can_process()                                                                                                                                                                                                            |
| [Tween](class_tween.md#class-tween)                                                     | create_tween()                                                                                                                                                                                                          |
| Node                                                                     | duplicate(flags: [int](class_int.md#class-int) = 15)                                                                                                                                                                       |
| Node                                                                     | find_child(pattern: [String](class_string.md#class-string), recursive: [bool](class_bool.md#class-bool) = true, owned: [bool](class_bool.md#class-bool) = true)                                                           |
| [Array](class_array.md#class-array)[Node]                                | find_children(pattern: [String](class_string.md#class-string), type: [String](class_string.md#class-string) = "", recursive: [bool](class_bool.md#class-bool) = true, owned: [bool](class_bool.md#class-bool) = true)  |
| Node                                                                     | find_parent(pattern: [String](class_string.md#class-string))                                                                                                                                                             |
| [RID](class_rid.md#class-rid)                                                           | get_accessibility_element()                                                                                                                                                                                |
| Node                                                                     | get_child(idx: [int](class_int.md#class-int), include_internal: [bool](class_bool.md#class-bool) = false)                                                                                                                  |
| [int](class_int.md#class-int)                                                           | get_child_count(include_internal: [bool](class_bool.md#class-bool) = false)                                                                                                                                          |
| [Array](class_array.md#class-array)[Node]                                | get_children(include_internal: [bool](class_bool.md#class-bool) = false)                                                                                                                                                |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_groups()                                                                                                                                                                                                              |
| [int](class_int.md#class-int)                                                           | get_index(include_internal: [bool](class_bool.md#class-bool) = false)                                                                                                                                                      |
| [Window](class_window.md#class-window)                                                  | get_last_exclusive_window()                                                                                                                                                                                |
| [int](class_int.md#class-int)                                                           | get_multiplayer_authority()                                                                                                                                                                                |
| Node                                                                     | get_node(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                                                                                |
| [Array](class_array.md#class-array)                                                     | get_node_and_resource(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                                                      |
| Node                                                                     | get_node_or_null(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                                                                |
| [Variant](class_variant.md#class-variant)                                               | get_node_rpc_config()                                                                                                                                                                                            |
| [Array](class_array.md#class-array)[[int](class_int.md#class-int)]                      | get_orphan_node_ids()                                                                                                                                                                                            |
| Node                                                                     | get_parent()                                                                                                                                                                                                              |
| [NodePath](class_nodepath.md#class-nodepath)                                            | get_path()                                                                                                                                                                                                                  |
| [NodePath](class_nodepath.md#class-nodepath)                                            | get_path_to(node: Node, use_unique_path: [bool](class_bool.md#class-bool) = false)                                                                                                                        |
| [float](class_float.md#class-float)                                                     | get_physics_process_delta_time()                                                                                                                                                                      |
| [float](class_float.md#class-float)                                                     | get_process_delta_time()                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | get_scene_instance_load_placeholder()                                                                                                                                                            |
| [SceneTree](class_scenetree.md#class-scenetree)                                         | get_tree()                                                                                                                                                                                                                  |
| [String](class_string.md#class-string)                                                  | get_tree_string()                                                                                                                                                                                                    |
| [String](class_string.md#class-string)                                                  | get_tree_string_pretty()                                                                                                                                                                                      |
| [Viewport](class_viewport.md#class-viewport)                                            | get_viewport()                                                                                                                                                                                                          |
| [Window](class_window.md#class-window)                                                  | get_window()                                                                                                                                                                                                              |
| [bool](class_bool.md#class-bool)                                                        | has_node(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                                                                                |
| [bool](class_bool.md#class-bool)                                                        | has_node_and_resource(path: [NodePath](class_nodepath.md#class-nodepath))                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | is_ancestor_of(node: Node)                                                                                                                                                                             |
| [bool](class_bool.md#class-bool)                                                        | is_displayed_folded()                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                        | is_editable_instance(node: Node)                                                                                                                                                                 |
| [bool](class_bool.md#class-bool)                                                        | is_greater_than(node: Node)                                                                                                                                                                           |
| [bool](class_bool.md#class-bool)                                                        | is_in_group(group: [StringName](class_stringname.md#class-stringname))                                                                                                                                                   |
| [bool](class_bool.md#class-bool)                                                        | is_inside_tree()                                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | is_multiplayer_authority()                                                                                                                                                                                  |
| [bool](class_bool.md#class-bool)                                                        | is_node_ready()                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | is_part_of_edited_scene()                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | is_physics_interpolated()                                                                                                                                                                                    |
| [bool](class_bool.md#class-bool)                                                        | is_physics_interpolated_and_enabled()                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                        | is_physics_processing()                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | is_physics_processing_internal()                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | is_processing()                                                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | is_processing_input()                                                                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                        | is_processing_internal()                                                                                                                                                                                      |
| [bool](class_bool.md#class-bool)                                                        | is_processing_shortcut_input()                                                                                                                                                                          |
| [bool](class_bool.md#class-bool)                                                        | is_processing_unhandled_input()                                                                                                                                                                        |
| [bool](class_bool.md#class-bool)                                                        | is_processing_unhandled_key_input()                                                                                                                                                                |
|                                                                                         | move_child(child_node: Node, to_index: [int](class_int.md#class-int))                                                                                                                                      |
|                                                                                         | notify_deferred_thread_group(what: [int](class_int.md#class-int))                                                                                                                                       |
|                                                                                         | notify_thread_safe(what: [int](class_int.md#class-int))                                                                                                                                                           |
|                                                                                         | print_orphan_nodes()                                                                                                                                                                                              |
|                                                                                         | print_tree()                                                                                                                                                                                                              |
|                                                                                         | print_tree_pretty()                                                                                                                                                                                                |
|                                                                                         | propagate_call(method: [StringName](class_stringname.md#class-stringname), args: [Array](class_array.md#class-array) = [], parent_first: [bool](class_bool.md#class-bool) = false)                                    |
|                                                                                         | propagate_notification(what: [int](class_int.md#class-int))                                                                                                                                                   |
|                                                                                         | queue_accessibility_update()                                                                                                                                                                              |
|                                                                                         | queue_free()                                                                                                                                                                                                              |
|                                                                                         | remove_child(node: Node)                                                                                                                                                                                 |
|                                                                                         | remove_from_group(group: [StringName](class_stringname.md#class-stringname))                                                                                                                                       |
|                                                                                         | reparent(new_parent: Node, keep_global_transform: [bool](class_bool.md#class-bool) = true)                                                                                                                   |
|                                                                                         | replace_by(node: Node, keep_groups: [bool](class_bool.md#class-bool) = false)                                                                                                                              |
|                                                                                         | request_ready()                                                                                                                                                                                                        |
|                                                                                         | reset_physics_interpolation()                                                                                                                                                                            |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | rpc(method: [StringName](class_stringname.md#class-stringname), ...)                                                                                                                                                             |
|                                                                                         | rpc_config(method: [StringName](class_stringname.md#class-stringname), config: [Variant](class_variant.md#class-variant))                                                                                                 |
| [Error](class_@globalscope.md#enum-globalscope-error)                                   | rpc_id(peer_id: [int](class_int.md#class-int), method: [StringName](class_stringname.md#class-stringname), ...)                                                                                                               |
|                                                                                         | set_deferred_thread_group(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                  |
|                                                                                         | set_display_folded(fold: [bool](class_bool.md#class-bool))                                                                                                                                                        |
|                                                                                         | set_editable_instance(node: Node, is_editable: [bool](class_bool.md#class-bool))                                                                                                                |
|                                                                                         | set_multiplayer_authority(id: [int](class_int.md#class-int), recursive: [bool](class_bool.md#class-bool) = true)                                                                                           |
|                                                                                         | set_physics_process(enable: [bool](class_bool.md#class-bool))                                                                                                                                                    |
|                                                                                         | set_physics_process_internal(enable: [bool](class_bool.md#class-bool))                                                                                                                                  |
|                                                                                         | set_process(enable: [bool](class_bool.md#class-bool))                                                                                                                                                                    |
|                                                                                         | set_process_input(enable: [bool](class_bool.md#class-bool))                                                                                                                                                        |
|                                                                                         | set_process_internal(enable: [bool](class_bool.md#class-bool))                                                                                                                                                  |
|                                                                                         | set_process_shortcut_input(enable: [bool](class_bool.md#class-bool))                                                                                                                                      |
|                                                                                         | set_process_unhandled_input(enable: [bool](class_bool.md#class-bool))                                                                                                                                    |
|                                                                                         | set_process_unhandled_key_input(enable: [bool](class_bool.md#class-bool))                                                                                                                            |
|                                                                                         | set_scene_instance_load_placeholder(load_placeholder: [bool](class_bool.md#class-bool))                                                                                                          |
|                                                                                         | set_thread_safe(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                      |
|                                                                                         | set_translation_domain_inherited()                                                                                                                                                                  |
|                                                                                         | update_configuration_warnings()                                                                                                                                                                        |

---

## Signals

**child_entered_tree**(node: Node)

Emitted when the child `node` enters the [SceneTree](class_scenetree.md#class-scenetree), usually because this node entered the tree (see tree_entered), or add_child() has been called.

This signal is emitted *after* the child node's own NOTIFICATION_ENTER_TREE and tree_entered.

---

**child_exiting_tree**(node: Node)

Emitted when the child `node` is about to exit the [SceneTree](class_scenetree.md#class-scenetree), usually because this node is exiting the tree (see tree_exiting), or because the child `node` is being removed or freed.

When this signal is received, the child `node` is still accessible inside the tree. This signal is emitted *after* the child node's own tree_exiting and NOTIFICATION_EXIT_TREE.

---

**child_order_changed**()

Emitted when the list of children is changed. This happens when child nodes are added, moved or removed.

---

**editor_description_changed**(node: Node)

Emitted when the node's editor description field changed.

---

**editor_state_changed**()

Emitted when an attribute of the node that is relevant to the editor is changed. Only emitted in the editor.

---

**ready**()

Emitted when the node is considered ready, after \_ready() is called.

---

**renamed**()

Emitted when the node's name is changed, if the node is inside the tree.

---

**replacing_by**(node: Node)

Emitted when this node is being replaced by the `node`, see replace_by().

This signal is emitted *after* `node` has been added as a child of the original parent node, but *before* all original child nodes have been reparented to `node`.

---

**tree_entered**()

Emitted when the node enters the tree.

This signal is emitted *after* the related NOTIFICATION_ENTER_TREE notification.

---

**tree_exited**()

Emitted after the node exits the tree and is no longer active.

This signal is emitted *after* the related NOTIFICATION_EXIT_TREE notification.

---

**tree_exiting**()

Emitted when the node is just about to exit the tree. The node is still valid. As such, this is the right place for de-initialization (or a "destructor", if you will).

This signal is emitted *after* the node's \_exit_tree(), and *before* the related NOTIFICATION_EXIT_TREE.

---

## Enumerations

enum **ProcessMode**:

ProcessMode **PROCESS_MODE_INHERIT** = `0`

Inherits process_mode from the node's parent. This is the default for any newly created node.

ProcessMode **PROCESS_MODE_PAUSABLE** = `1`

Processes when [SceneTree.paused](class_scenetree.md#class-scenetree-property-paused) is `false`. This is the inverse of PROCESS_MODE_WHEN_PAUSED, and the default for the root node.

ProcessMode **PROCESS_MODE_WHEN_PAUSED** = `2`

Processes **only** when [SceneTree.paused](class_scenetree.md#class-scenetree-property-paused) is `true`. This is the inverse of PROCESS_MODE_PAUSABLE.

ProcessMode **PROCESS_MODE_ALWAYS** = `3`

Always processes. Keeps processing, ignoring [SceneTree.paused](class_scenetree.md#class-scenetree-property-paused). This is the inverse of PROCESS_MODE_DISABLED.

ProcessMode **PROCESS_MODE_DISABLED** = `4`

Never processes. Completely disables processing, ignoring [SceneTree.paused](class_scenetree.md#class-scenetree-property-paused). This is the inverse of PROCESS_MODE_ALWAYS.

---

enum **ProcessThreadGroup**:

ProcessThreadGroup **PROCESS_THREAD_GROUP_INHERIT** = `0`

Process this node based on the thread group mode of the first parent (or grandparent) node that has a thread group mode that is not inherit. See process_thread_group for more information.

ProcessThreadGroup **PROCESS_THREAD_GROUP_MAIN_THREAD** = `1`

Process this node (and child nodes set to inherit) on the main thread. See process_thread_group for more information.

ProcessThreadGroup **PROCESS_THREAD_GROUP_SUB_THREAD** = `2`

Process this node (and child nodes set to inherit) on a sub-thread. See process_thread_group for more information.

---

flags **ProcessThreadMessages**:

ProcessThreadMessages **FLAG_PROCESS_THREAD_MESSAGES** = `1`

Allows this node to process threaded messages created with call_deferred_thread_group() right before \_process() is called.

ProcessThreadMessages **FLAG_PROCESS_THREAD_MESSAGES_PHYSICS** = `2`

Allows this node to process threaded messages created with call_deferred_thread_group() right before \_physics_process() is called.

ProcessThreadMessages **FLAG_PROCESS_THREAD_MESSAGES_ALL** = `3`

Allows this node to process threaded messages created with call_deferred_thread_group() right before either \_process() or \_physics_process() are called.

---

enum **PhysicsInterpolationMode**:

PhysicsInterpolationMode **PHYSICS_INTERPOLATION_MODE_INHERIT** = `0`

Inherits physics_interpolation_mode from the node's parent. This is the default for any newly created node.

PhysicsInterpolationMode **PHYSICS_INTERPOLATION_MODE_ON** = `1`

Enables physics interpolation for this node and for children set to PHYSICS_INTERPOLATION_MODE_INHERIT. This is the default for the root node.

PhysicsInterpolationMode **PHYSICS_INTERPOLATION_MODE_OFF** = `2`

Disables physics interpolation for this node and for children set to PHYSICS_INTERPOLATION_MODE_INHERIT.

---

enum **DuplicateFlags**:

DuplicateFlags **DUPLICATE_SIGNALS** = `1`

Duplicate the node's signal connections that are connected with the [Object.CONNECT_PERSIST](class_object.md#class-object-constant-connect-persist) flag.

DuplicateFlags **DUPLICATE_GROUPS** = `2`

Duplicate the node's groups.

DuplicateFlags **DUPLICATE_SCRIPTS** = `4`

Duplicate the node's script (also overriding the duplicated children's scripts, if combined with DUPLICATE_USE_INSTANTIATION).

DuplicateFlags **DUPLICATE_USE_INSTANTIATION** = `8`

Duplicate using [PackedScene.instantiate()](class_packedscene.md#class-packedscene-method-instantiate). If the node comes from a scene saved on disk, reuses [PackedScene.instantiate()](class_packedscene.md#class-packedscene-method-instantiate) as the base for the duplicated node and its children.

DuplicateFlags **DUPLICATE_INTERNAL_STATE** = `16`

Duplicate also non-serializable variables (i.e. without [@GlobalScope.PROPERTY_USAGE_STORAGE](class_@globalscope.md#class-globalscope-constant-property-usage-storage)).

DuplicateFlags **DUPLICATE_DEFAULT** = `15`

Duplicate using default flags. This constant is useful to add or remove a single flag.

```gdscript
# Duplicate non-exported variables.
var dupe = duplicate(DUPLICATE_DEFAULT | DUPLICATE_INTERNAL_STATE)
```

---

enum **InternalMode**:

InternalMode **INTERNAL_MODE_DISABLED** = `0`

The node will not be internal.

InternalMode **INTERNAL_MODE_FRONT** = `1`

The node will be placed at the beginning of the parent's children, before any non-internal sibling.

InternalMode **INTERNAL_MODE_BACK** = `2`

The node will be placed at the end of the parent's children, after any non-internal sibling.

---

enum **AutoTranslateMode**:

AutoTranslateMode **AUTO_TRANSLATE_MODE_INHERIT** = `0`

Inherits auto_translate_mode from the node's parent. This is the default for any newly created node.

AutoTranslateMode **AUTO_TRANSLATE_MODE_ALWAYS** = `1`

Always automatically translate. This is the inverse of AUTO_TRANSLATE_MODE_DISABLED, and the default for the root node.

AutoTranslateMode **AUTO_TRANSLATE_MODE_DISABLED** = `2`

Never automatically translate. This is the inverse of AUTO_TRANSLATE_MODE_ALWAYS.

String parsing for translation template generation will be skipped for this node and children that are set to AUTO_TRANSLATE_MODE_INHERIT.

---

## Constants

**NOTIFICATION_ENTER_TREE** = `10`

Notification received when the node enters a [SceneTree](class_scenetree.md#class-scenetree). See \_enter_tree().

This notification is received *before* the related tree_entered signal.

**NOTIFICATION_EXIT_TREE** = `11`

Notification received when the node is about to exit a [SceneTree](class_scenetree.md#class-scenetree). See \_exit_tree().

This notification is received *after* the related tree_exiting signal.

This notification is sent in reversed order.

**NOTIFICATION_MOVED_IN_PARENT** = `12`

**Deprecated:** This notification is no longer sent by the engine. Use NOTIFICATION_CHILD_ORDER_CHANGED instead.

**NOTIFICATION_READY** = `13`

Notification received when the node is ready. See \_ready().

**NOTIFICATION_PAUSED** = `14`

Notification received when the node is paused. See process_mode.

**NOTIFICATION_UNPAUSED** = `15`

Notification received when the node is unpaused. See process_mode.

**NOTIFICATION_PHYSICS_PROCESS** = `16`

Notification received from the tree every physics frame when is_physics_processing() returns `true`. See \_physics_process().

**NOTIFICATION_PROCESS** = `17`

Notification received from the tree every rendered frame when is_processing() returns `true`. See \_process().

**NOTIFICATION_PARENTED** = `18`

Notification received when the node is set as a child of another node (see add_child() and add_sibling()).

**Note:** This does *not* mean that the node entered the [SceneTree](class_scenetree.md#class-scenetree).

**NOTIFICATION_UNPARENTED** = `19`

Notification received when the parent node calls remove_child() on this node.

**Note:** This does *not* mean that the node exited the [SceneTree](class_scenetree.md#class-scenetree).

**NOTIFICATION_SCENE_INSTANTIATED** = `20`

Notification received *only* by the newly instantiated scene root node, when [PackedScene.instantiate()](class_packedscene.md#class-packedscene-method-instantiate) is completed.

**NOTIFICATION_DRAG_BEGIN** = `21`

Notification received when a drag operation begins. All nodes receive this notification, not only the dragged one.

Can be triggered either by dragging a [Control](class_control.md#class-control) that provides drag data (see [Control._get_drag_data()](class_control.md#class-control-private-method-get-drag-data)) or using [Control.force_drag()](class_control.md#class-control-method-force-drag).

Use [Viewport.gui_get_drag_data()](class_viewport.md#class-viewport-method-gui-get-drag-data) to get the dragged data.

**NOTIFICATION_DRAG_END** = `22`

Notification received when a drag operation ends.

Use [Viewport.gui_is_drag_successful()](class_viewport.md#class-viewport-method-gui-is-drag-successful) to check if the drag succeeded.

**NOTIFICATION_PATH_RENAMED** = `23`

Notification received when the node's name or one of its ancestors' name is changed. This notification is *not* received when the node is removed from the [SceneTree](class_scenetree.md#class-scenetree).

**NOTIFICATION_CHILD_ORDER_CHANGED** = `24`

Notification received when the list of children is changed. This happens when child nodes are added, moved or removed.

**NOTIFICATION_INTERNAL_PROCESS** = `25`

Notification received from the tree every rendered frame when is_processing_internal() returns `true`.

**NOTIFICATION_INTERNAL_PHYSICS_PROCESS** = `26`

Notification received from the tree every physics frame when is_physics_processing_internal() returns `true`.

**NOTIFICATION_POST_ENTER_TREE** = `27`

Notification received when the node enters the tree, just before NOTIFICATION_READY may be received. Unlike the latter, it is sent every time the node enters tree, not just once.

**NOTIFICATION_DISABLED** = `28`

Notification received when the node is disabled. See PROCESS_MODE_DISABLED.

**NOTIFICATION_ENABLED** = `29`

Notification received when the node is enabled again after being disabled. See PROCESS_MODE_DISABLED.

**NOTIFICATION_RESET_PHYSICS_INTERPOLATION** = `2001`

Notification received when reset_physics_interpolation() is called on the node or its ancestors.

**NOTIFICATION_EDITOR_PRE_SAVE** = `9001`

Notification received right before the scene with the node is saved in the editor. This notification is only sent in the Godot editor and will not occur in exported projects.

**NOTIFICATION_EDITOR_POST_SAVE** = `9002`

Notification received right after the scene with the node is saved in the editor. This notification is only sent in the Godot editor and will not occur in exported projects.

**NOTIFICATION_WM_MOUSE_ENTER** = `1002`

Notification received when the mouse enters the window.

Implemented for embedded windows and on desktop and web platforms.

**NOTIFICATION_WM_MOUSE_EXIT** = `1003`

Notification received when the mouse leaves the window.

Implemented for embedded windows and on desktop and web platforms.

**NOTIFICATION_WM_WINDOW_FOCUS_IN** = `1004`

Notification received from the OS when the node's [Window](class_window.md#class-window) ancestor is focused. This may be a change of focus between two windows of the same engine instance, or from the OS desktop or a third-party application to a window of the game (in which case NOTIFICATION_APPLICATION_FOCUS_IN is also received).

A [Window](class_window.md#class-window) node receives this notification when it is focused.

**NOTIFICATION_WM_WINDOW_FOCUS_OUT** = `1005`

Notification received from the OS when the node's [Window](class_window.md#class-window) ancestor is defocused. This may be a change of focus between two windows of the same engine instance, or from a window of the game to the OS desktop or a third-party application (in which case NOTIFICATION_APPLICATION_FOCUS_OUT is also received).

A [Window](class_window.md#class-window) node receives this notification when it is defocused.

**NOTIFICATION_WM_CLOSE_REQUEST** = `1006`

Notification received from the OS when a close request is sent (e.g. closing the window with a "Close" button or `Alt + F4`).

Implemented on desktop platforms.

**NOTIFICATION_WM_GO_BACK_REQUEST** = `1007`

Notification received from the OS when a go back request is sent (e.g. pressing the "Back" button on Android).

Implemented only on Android.

**NOTIFICATION_WM_SIZE_CHANGED** = `1008`

Notification received when the window is resized.

**Note:** Only the resized [Window](class_window.md#class-window) node receives this notification, and it's not propagated to the child nodes.

**NOTIFICATION_WM_DPI_CHANGE** = `1009`

Notification received from the OS when the screen's dots per inch (DPI) scale is changed. Only implemented on macOS.

**NOTIFICATION_VP_MOUSE_ENTER** = `1010`

Notification received when the mouse cursor enters the [Viewport](class_viewport.md#class-viewport)'s visible area, that is not occluded behind other [Control](class_control.md#class-control)s or [Window](class_window.md#class-window)s, provided its [Viewport.gui_disable_input](class_viewport.md#class-viewport-property-gui-disable-input) is `false` and regardless if it's currently focused or not.

**NOTIFICATION_VP_MOUSE_EXIT** = `1011`

Notification received when the mouse cursor leaves the [Viewport](class_viewport.md#class-viewport)'s visible area, that is not occluded behind other [Control](class_control.md#class-control)s or [Window](class_window.md#class-window)s, provided its [Viewport.gui_disable_input](class_viewport.md#class-viewport-property-gui-disable-input) is `false` and regardless if it's currently focused or not.

**NOTIFICATION_WM_POSITION_CHANGED** = `1012`

Notification received when the window is moved.

**NOTIFICATION_WM_OUTPUT_MAX_LINEAR_VALUE_CHANGED** = `1013`

Notification received when the output max linear value returned by [Window.get_output_max_linear_value()](class_window.md#class-window-method-get-output-max-linear-value) has changed.

This occurs when HDR output is enabled or disabled and when any HDR output luminance values of the window have changed, such as when the player adjusts their screen brightness setting or moves the window to a different screen.

**NOTIFICATION_OS_MEMORY_WARNING** = `2009`

Notification received from the OS when the application is exceeding its allocated memory.

Implemented only on iOS.

**NOTIFICATION_TRANSLATION_CHANGED** = `2010`

Notification received when translations may have changed. Can be triggered by the user changing the locale, changing auto_translate_mode or when the node enters the scene tree. Can be used to respond to language changes, for example to change the UI strings on the fly. Useful when working with the built-in translation support, like [Object.tr()](class_object.md#class-object-method-tr).

**Note:** This notification is received alongside NOTIFICATION_ENTER_TREE, so if you are instantiating a scene, the child nodes will not be initialized yet. You can use it to setup translations for this node, child nodes created from script, or if you want to access child nodes added in the editor, make sure the node is ready using is_node_ready().

```gdscript
func _notification(what):
    if what == NOTIFICATION_TRANSLATION_CHANGED:
        if not is_node_ready():
            await ready # Wait until ready signal.
        $Label.text = atr("%d Bananas") % banana_counter
```

**NOTIFICATION_WM_ABOUT** = `2011`

Notification received from the OS when a request for "About" information is sent.

Implemented only on macOS.

**NOTIFICATION_CRASH** = `2012`

Notification received from Godot's crash handler when the engine is about to crash.

Implemented on desktop platforms, if the crash handler is enabled.

**NOTIFICATION_OS_IME_UPDATE** = `2013`

Notification received from the OS when an update of the Input Method Engine occurs (e.g. change of IME cursor position or composition string).

Implemented on desktop and web platforms.

**NOTIFICATION_APPLICATION_RESUMED** = `2014`

Notification received from the OS when the application is resumed.

Specific to the Android and iOS platforms.

**NOTIFICATION_APPLICATION_PAUSED** = `2015`

Notification received from the OS when the application is paused.

Specific to the Android and iOS platforms.

**Note:** On iOS, you only have approximately 5 seconds to finish a task started by this signal. If you go over this allotment, iOS will kill the app instead of pausing it.

**NOTIFICATION_APPLICATION_FOCUS_IN** = `2016`

Notification received from the OS when the application is focused, i.e. when changing the focus from the OS desktop or a thirdparty application to any open window of the Godot instance.

Implemented on desktop and mobile platforms.

**NOTIFICATION_APPLICATION_FOCUS_OUT** = `2017`

Notification received from the OS when the application is defocused, i.e. when changing the focus from any open window of the Godot instance to the OS desktop or a thirdparty application.

Implemented on desktop and mobile platforms.

**NOTIFICATION_TEXT_SERVER_CHANGED** = `2018`

Notification received when the [TextServer](class_textserver.md#class-textserver) is changed.

**NOTIFICATION_APPLICATION_PIP_MODE_ENTERED** = `2019`

Notification received when the application enters picture-in-picture mode.

**NOTIFICATION_APPLICATION_PIP_MODE_EXITED** = `2020`

Notification received when the application exits picture-in-picture mode.

**NOTIFICATION_ACCESSIBILITY_UPDATE** = `3000`

Notification received when an accessibility information update is required.

**NOTIFICATION_ACCESSIBILITY_INVALIDATE** = `3001`

Notification received when accessibility elements are invalidated. All node accessibility elements are automatically deleted after receiving this message, therefore all existing references to such elements should be discarded.

---

## Property Descriptions

AutoTranslateMode **auto_translate_mode** = `0`

-  **set_auto_translate_mode**(value: AutoTranslateMode)
- AutoTranslateMode **get_auto_translate_mode**()

Defines if any text should automatically change to its translated version depending on the current locale (for nodes such as [Label](class_label.md#class-label), [RichTextLabel](class_richtextlabel.md#class-richtextlabel), [Window](class_window.md#class-window), etc.). Also decides if the node's strings should be parsed for translation template generation.

**Note:** For the root node, auto translate mode can also be set via [ProjectSettings.internationalization/rendering/root_node_auto_translate](class_projectsettings.md#class-projectsettings-property-internationalization-rendering-root-node-auto-translate).

---

[String](class_string.md#class-string) **editor_description** = `""`

-  **set_editor_description**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_editor_description**()

An optional description to the node. It will be displayed as a tooltip when hovering over the node in the editor's Scene dock.

---

[MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) **multiplayer**

- [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) **get_multiplayer**()

The [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) instance associated with this node. See [SceneTree.get_multiplayer()](class_scenetree.md#class-scenetree-method-get-multiplayer).

**Note:** Renaming the node, or moving it in the tree, will not move the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) to the new path, you will have to update this manually.

---

[StringName](class_stringname.md#class-stringname) **name**

-  **set_name**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_name**()

The name of the node. This name must be unique among the siblings (other child nodes from the same parent). When set to an existing sibling's name, the node is automatically renamed.

**Note:** When changing the name, the following characters will be replaced with an underscore: (`.` `:` `@` `/` `"` `%`). In particular, the `@` character is reserved for auto-generated names. See also [String.validate_node_name()](class_string.md#class-string-method-validate-node-name).

---

Node **owner**

-  **set_owner**(value: Node)
- Node **get_owner**()

The owner of this node. The owner must be an ancestor of this node. When packing the owner node in a [PackedScene](class_packedscene.md#class-packedscene), all the nodes it owns are also saved with it. See also unique_name_in_owner.

**Note:** In the editor, nodes not owned by the scene root are usually not displayed in the Scene dock, and will **not** be saved. To prevent this, remember to set the owner after calling add_child().

**Note:** The owner needs to be the current scene root. See [Instancing scenes](../tutorials/plugins/running_code_in_the_editor.html#instancing-scenes) in the documentation for more information.

---

PhysicsInterpolationMode **physics_interpolation_mode** = `0`

-  **set_physics_interpolation_mode**(value: PhysicsInterpolationMode)
- PhysicsInterpolationMode **get_physics_interpolation_mode**()

The physics interpolation mode to use for this node. Only effective if [ProjectSettings.physics/common/physics_interpolation](class_projectsettings.md#class-projectsettings-property-physics-common-physics-interpolation) or [SceneTree.physics_interpolation](class_scenetree.md#class-scenetree-property-physics-interpolation) is `true`.

By default, nodes inherit the physics interpolation mode from their parent. This property can enable or disable physics interpolation individually for each node, regardless of their parents' physics interpolation mode.

**Note:** Some node types like [VehicleWheel3D](class_vehiclewheel3d.md#class-vehiclewheel3d) have physics interpolation disabled by default, as they rely on their own custom solution.

**Note:** When teleporting a node to a distant position, it's recommended to temporarily disable interpolation with reset_physics_interpolation() *after* moving the node. This avoids creating a visual streak between the old and new positions.

---

ProcessMode **process_mode** = `0`

-  **set_process_mode**(value: ProcessMode)
- ProcessMode **get_process_mode**()

The node's processing behavior. To check if the node can process in its current mode, use can_process().

---

[int](class_int.md#class-int) **process_physics_priority** = `0`

-  **set_physics_process_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_physics_process_priority**()

Similar to process_priority but for NOTIFICATION_PHYSICS_PROCESS, \_physics_process(), or NOTIFICATION_INTERNAL_PHYSICS_PROCESS.

---

[int](class_int.md#class-int) **process_priority** = `0`

-  **set_process_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_process_priority**()

The node's execution order of the process callbacks (\_process(), NOTIFICATION_PROCESS, and NOTIFICATION_INTERNAL_PROCESS). Nodes whose priority value is *lower* call their process callbacks first, regardless of tree order.

---

ProcessThreadGroup **process_thread_group** = `0`

-  **set_process_thread_group**(value: ProcessThreadGroup)
- ProcessThreadGroup **get_process_thread_group**()

Set the process thread group for this node (basically, whether it receives NOTIFICATION_PROCESS, NOTIFICATION_PHYSICS_PROCESS, \_process() or \_physics_process() (and the internal versions) on the main thread or in a sub-thread.

By default, the thread group is PROCESS_THREAD_GROUP_INHERIT, which means that this node belongs to the same thread group as the parent node. The thread groups means that nodes in a specific thread group will process together, separate to other thread groups (depending on process_thread_group_order). If the value is set is PROCESS_THREAD_GROUP_SUB_THREAD, this thread group will occur on a sub thread (not the main thread), otherwise if set to PROCESS_THREAD_GROUP_MAIN_THREAD it will process on the main thread. If there is not a parent or grandparent node set to something other than inherit, the node will belong to the *default thread group*. This default group will process on the main thread and its group order is 0.

During processing in a sub-thread, accessing most functions in nodes outside the thread group is forbidden (and it will result in an error in debug mode). Use [Object.call_deferred()](class_object.md#class-object-method-call-deferred), call_thread_safe(), call_deferred_thread_group() and the likes in order to communicate from the thread groups to the main thread (or to other thread groups).

To better understand process thread groups, the idea is that any node set to any other value than PROCESS_THREAD_GROUP_INHERIT will include any child (and grandchild) nodes set to inherit into its process thread group. This means that the processing of all the nodes in the group will happen together, at the same time as the node including them.

---

[int](class_int.md#class-int) **process_thread_group_order**

-  **set_process_thread_group_order**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_process_thread_group_order**()

Change the process thread group order. Groups with a lesser order will process before groups with a greater order. This is useful when a large amount of nodes process in sub thread and, afterwards, another group wants to collect their result in the main thread, as an example.

---

[ProcessThreadMessages] **process_thread_messages**

-  **set_process_thread_messages**(value: [ProcessThreadMessages])
- [ProcessThreadMessages] **get_process_thread_messages**()

Set whether the current thread group will process messages (calls to call_deferred_thread_group() on threads), and whether it wants to receive them during regular process or physics process callbacks.

---

[String](class_string.md#class-string) **scene_file_path**

-  **set_scene_file_path**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_scene_file_path**()

The original scene's file path, if the node has been instantiated from a [PackedScene](class_packedscene.md#class-packedscene) file. Only scene root nodes contains this.

---

[bool](class_bool.md#class-bool) **unique_name_in_owner** = `false`

-  **set_unique_name_in_owner**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_unique_name_in_owner**()

If `true`, the node can be accessed from any node sharing the same owner or from the owner itself, with special `%Name` syntax in get_node().

**Note:** If another node with the same owner shares the same name as this node, the other node will no longer be accessible as unique.

---

## Method Descriptions

 **\_enter_tree**()

Called when the node enters the [SceneTree](class_scenetree.md#class-scenetree) (e.g. upon instantiating, scene changing, or after calling add_child() in a script). If the node has children, its \_enter_tree() callback will be called first, and then that of the children.

Corresponds to the NOTIFICATION_ENTER_TREE notification in [Object._notification()](class_object.md#class-object-private-method-notification).

---

 **\_exit_tree**()

Called when the node is about to leave the [SceneTree](class_scenetree.md#class-scenetree) (e.g. upon freeing, scene changing, or after calling remove_child() in a script). If the node has children, its \_exit_tree() callback will be called last, after all its children have left the tree.

Corresponds to the NOTIFICATION_EXIT_TREE notification in [Object._notification()](class_object.md#class-object-private-method-notification) and signal tree_exiting. To get notified when the node has already left the active tree, connect to the tree_exited.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_accessibility_configuration_warnings**()

The elements in the array returned from this method are displayed as warnings in the Scene dock if the script that overrides it is a `tool` script, and accessibility warnings are enabled in the editor settings.

Returning an empty array produces no warnings.

---

[PackedStringArray](class_packedstringarray.md#class-packedstringarray) **\_get_configuration_warnings**()

The elements in the array returned from this method are displayed as warnings in the Scene dock if the script that overrides it is a `tool` script.

Returning an empty array produces no warnings.

Call update_configuration_warnings() when the warnings need to be updated for this node.

```gdscript
@export var energy = 0:
    set(value):
        energy = value
        update_configuration_warnings()

func _get_configuration_warnings():
    if energy < 0:
        return ["Energy must be 0 or greater."]
    else:
        return []
```

---

[RID](class_rid.md#class-rid) **\_get_focused_accessibility_element**()

Called during accessibility information updates to determine the currently focused sub-element, should return a sub-element RID or the value returned by get_accessibility_element().

---

 **\_input**(event: [InputEvent](class_inputevent.md#class-inputevent))

Called when there is an input event. The input event propagates up through the node tree until a node consumes it.

It is only called if input processing is enabled, which is done automatically if this method is overridden, and can be toggled with set_process_input().

To consume the input event and stop it propagating further to other nodes, [Viewport.set_input_as_handled()](class_viewport.md#class-viewport-method-set-input-as-handled) can be called.

For gameplay input, \_unhandled_input() and \_unhandled_key_input() are usually a better fit as they allow the GUI to intercept the events first.

**Note:** This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).

---

 **\_physics_process**(delta: [float](class_float.md#class-float))

Called once on each physics tick, and allows Nodes to synchronize their logic with physics ticks. `delta` is the logical time between physics ticks in seconds and is equal to [Engine.time_scale](class_engine.md#class-engine-property-time-scale) / [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second).

It is only called if physics processing is enabled for this Node, which is done automatically if this method is overridden, and can be toggled with set_physics_process().

Processing happens in order of process_physics_priority, lower priority values are called first. Nodes with the same priority are processed in tree order, or top to bottom as seen in the editor (also known as pre-order traversal).

Corresponds to the NOTIFICATION_PHYSICS_PROCESS notification in [Object._notification()](class_object.md#class-object-private-method-notification).

**Note:** This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).

**Note:** Accumulated `delta` may diverge from real world seconds.

---

 **\_process**(delta: [float](class_float.md#class-float))

Called on each idle frame, prior to rendering, and after physics ticks have been processed. `delta` is the time between frames in seconds.

It is only called if processing is enabled for this Node, which is done automatically if this method is overridden, and can be toggled with set_process().

Processing happens in order of process_priority, lower priority values are called first. Nodes with the same priority are processed in tree order, or top to bottom as seen in the editor (also known as pre-order traversal).

Corresponds to the NOTIFICATION_PROCESS notification in [Object._notification()](class_object.md#class-object-private-method-notification).

**Note:** This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).

**Note:** When the engine is struggling and the frame rate is lowered, `delta` will increase. When `delta` is increased, it's capped at a maximum of [Engine.time_scale](class_engine.md#class-engine-property-time-scale) \* [Engine.max_physics_steps_per_frame](class_engine.md#class-engine-property-max-physics-steps-per-frame) / [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second). As a result, accumulated `delta` may not represent real world time.

**Note:** When `--fixed-fps` is enabled or the engine is running in Movie Maker mode (see [MovieWriter](class_moviewriter.md#class-moviewriter)), process `delta` will always be the same for every frame, regardless of how much time the frame took to render.

**Note:** Frame delta may be post-processed by [OS.delta_smoothing](class_os.md#class-os-property-delta-smoothing) if this is enabled for the project.

---

 **\_ready**()

Called when the node is "ready", i.e. when both the node and its children have entered the scene tree. If the node has children, their \_ready() callbacks get triggered first, and the parent node will receive the ready notification afterwards.

Corresponds to the NOTIFICATION_READY notification in [Object._notification()](class_object.md#class-object-private-method-notification). See also the `@onready` annotation for variables.

Usually used for initialization. For even earlier initialization, [Object._init()](class_object.md#class-object-private-method-init) may be used. See also \_enter_tree().

**Note:** This method may be called only once for each node. After removing a node from the scene tree and adding it again, \_ready() will **not** be called a second time. This can be bypassed by requesting another call with request_ready(), which may be called anywhere before adding the node again.

---

 **\_shortcut_input**(event: [InputEvent](class_inputevent.md#class-inputevent))

Called when an [InputEventKey](class_inputeventkey.md#class-inputeventkey), [InputEventShortcut](class_inputeventshortcut.md#class-inputeventshortcut), or [InputEventJoypadButton](class_inputeventjoypadbutton.md#class-inputeventjoypadbutton) hasn't been consumed by \_input() or any GUI [Control](class_control.md#class-control) item. It is called before \_unhandled_key_input() and \_unhandled_input(). The input event propagates up through the node tree until a node consumes it.

It is only called if shortcut processing is enabled, which is done automatically if this method is overridden, and can be toggled with set_process_shortcut_input().

To consume the input event and stop it propagating further to other nodes, [Viewport.set_input_as_handled()](class_viewport.md#class-viewport-method-set-input-as-handled) can be called.

This method can be used to handle shortcuts. For generic GUI events, use \_input() instead. Gameplay events should usually be handled with either \_unhandled_input() or \_unhandled_key_input().

**Note:** This method is only called if the node is present in the scene tree (i.e. if it's not orphan).

---

 **\_unhandled_input**(event: [InputEvent](class_inputevent.md#class-inputevent))

Called when an [InputEvent](class_inputevent.md#class-inputevent) hasn't been consumed by \_input() or any GUI [Control](class_control.md#class-control) item. It is called after \_shortcut_input() and after \_unhandled_key_input(). The input event propagates up through the node tree until a node consumes it.

It is only called if unhandled input processing is enabled, which is done automatically if this method is overridden, and can be toggled with set_process_unhandled_input().

To consume the input event and stop it propagating further to other nodes, [Viewport.set_input_as_handled()](class_viewport.md#class-viewport-method-set-input-as-handled) can be called.

For gameplay input, this method is usually a better fit than \_input(), as GUI events need a higher priority. For keyboard shortcuts, consider using \_shortcut_input() instead, as it is called before this method. Finally, to handle keyboard events, consider using \_unhandled_key_input() for performance reasons.

**Note:** This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).

---

 **\_unhandled_key_input**(event: [InputEvent](class_inputevent.md#class-inputevent))

Called when an [InputEventKey](class_inputeventkey.md#class-inputeventkey) hasn't been consumed by \_input() or any GUI [Control](class_control.md#class-control) item. It is called after \_shortcut_input() but before \_unhandled_input(). The input event propagates up through the node tree until a node consumes it.

It is only called if unhandled key input processing is enabled, which is done automatically if this method is overridden, and can be toggled with set_process_unhandled_key_input().

To consume the input event and stop it propagating further to other nodes, [Viewport.set_input_as_handled()](class_viewport.md#class-viewport-method-set-input-as-handled) can be called.

This method can be used to handle Unicode character input with `Alt`, `Alt + Ctrl`, and `Alt + Shift` modifiers, after shortcuts were handled.

For gameplay input, this and \_unhandled_input() are usually a better fit than \_input(), as GUI events should be handled first. This method also performs better than \_unhandled_input(), since unrelated events such as [InputEventMouseMotion](class_inputeventmousemotion.md#class-inputeventmousemotion) are automatically filtered. For shortcuts, consider using \_shortcut_input() instead.

**Note:** This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).

---

 **add_child**(node: Node, force_readable_name: [bool](class_bool.md#class-bool) = false, internal: InternalMode = 0)

Adds a child `node`. Nodes can have any number of children, but every child must have a unique name. Child nodes are automatically deleted when the parent node is deleted, so an entire scene can be removed by deleting its topmost node.

If `force_readable_name` is `true`, improves the readability of the added `node`. If not named, the `node` is renamed to its type, and if it shares name with a sibling, a number is suffixed more appropriately. This operation is very slow. As such, it is recommended leaving this to `false`, which assigns a dummy name featuring `@` in both situations.

If `internal` is different than INTERNAL_MODE_DISABLED, the child will be added as internal node. These nodes are ignored by methods like get_children(), unless their parameter `include_internal` is `true`. It also prevents these nodes being duplicated with their parent. The intended usage is to hide the internal nodes from the user, so the user won't accidentally delete or modify them. Used by some GUI nodes, e.g. [ColorPicker](class_colorpicker.md#class-colorpicker).

**Note:** If `node` already has a parent, this method will fail. Use remove_child() first to remove `node` from its current parent. For example:

GDScript

```gdscript
var child_node = get_child(0)
if child_node.get_parent():
    child_node.get_parent().remove_child(child_node)
add_child(child_node)
```

C#

```csharp
Node childNode = GetChild(0);
if (childNode.GetParent() != null)
{
    childNode.GetParent().RemoveChild(childNode);
}
AddChild(childNode);
```

If you need the child node to be added below a specific node in the list of children, use add_sibling() instead of this method.

**Note:** If you want a child to be persisted to a [PackedScene](class_packedscene.md#class-packedscene), you must set owner in addition to calling add_child(). This is typically relevant for [tool scripts](../tutorials/plugins/running_code_in_the_editor.md) and [editor plugins](../tutorials/plugins/editor/index.md). If add_child() is called without setting owner, the newly added **Node** will not be visible in the scene tree, though it will be visible in the 2D/3D view.

---

 **add_sibling**(sibling: Node, force_readable_name: [bool](class_bool.md#class-bool) = false)

Adds a `sibling` node to this node's parent, and moves the added sibling right below this node.

If `force_readable_name` is `true`, improves the readability of the added `sibling`. If not named, the `sibling` is renamed to its type, and if it shares name with a sibling, a number is suffixed more appropriately. This operation is very slow. As such, it is recommended leaving this to `false`, which assigns a dummy name featuring `@` in both situations.

Use add_child() instead of this method if you don't need the child node to be added below a specific node in the list of children.

**Note:** If this node is internal, the added sibling will be internal too (see add_child()'s `internal` parameter).

---

 **add_to_group**(group: [StringName](class_stringname.md#class-stringname), persistent: [bool](class_bool.md#class-bool) = false)

Adds the node to the `group`. Groups can be helpful to organize a subset of nodes, for example `"enemies"` or `"collectables"`. See notes in the description, and the group methods in [SceneTree](class_scenetree.md#class-scenetree).

If `persistent` is `true`, the group will be stored when saved inside a [PackedScene](class_packedscene.md#class-packedscene). All groups created and displayed in the Groups dock are persistent.

**Note:** To improve performance, the order of group names is *not* guaranteed and may vary between project runs. Therefore, do not rely on the group order.

**Note:** [SceneTree](class_scenetree.md#class-scenetree)'s group methods will *not* work on this node if not inside the tree (see is_inside_tree()).

---

[String](class_string.md#class-string) **atr**(message: [String](class_string.md#class-string), context: [StringName](class_stringname.md#class-stringname) = "")

Translates a `message`, using the translation catalogs configured in the Project Settings. Further `context` can be specified to help with the translation. Note that most [Control](class_control.md#class-control) nodes automatically translate their strings, so this method is mostly useful for formatted strings or custom drawn text.

This method works the same as [Object.tr()](class_object.md#class-object-method-tr), with the addition of respecting the auto_translate_mode state.

If [Object.can_translate_messages()](class_object.md#class-object-method-can-translate-messages) is `false`, or no translation is available, this method returns the `message` without changes. See [Object.set_message_translation()](class_object.md#class-object-method-set-message-translation).

For detailed examples, see [Internationalizing games](../tutorials/i18n/internationalizing_games.md).

---

[String](class_string.md#class-string) **atr_n**(message: [String](class_string.md#class-string), plural_message: [StringName](class_stringname.md#class-stringname), n: [int](class_int.md#class-int), context: [StringName](class_stringname.md#class-stringname) = "")

Translates a `message` or `plural_message`, using the translation catalogs configured in the Project Settings. Further `context` can be specified to help with the translation.

This method works the same as [Object.tr_n()](class_object.md#class-object-method-tr-n), with the addition of respecting the auto_translate_mode state.

If [Object.can_translate_messages()](class_object.md#class-object-method-can-translate-messages) is `false`, or no translation is available, this method returns `message` or `plural_message`, without changes. See [Object.set_message_translation()](class_object.md#class-object-method-set-message-translation).

The `n` is the number, or amount, of the message's subject. It is used by the translation system to fetch the correct plural form for the current language.

For detailed examples, see [Localization using gettext](../tutorials/i18n/localization_using_gettext.md).

**Note:** Negative and [float](class_float.md#class-float) numbers may not properly apply to some countable subjects. It's recommended to handle these cases with atr().

---

[Variant](class_variant.md#class-variant) **call_deferred_thread_group**(method: [StringName](class_stringname.md#class-stringname), ...)

This function is similar to [Object.call_deferred()](class_object.md#class-object-method-call-deferred) except that the call will take place when the node thread group is processed. If the node thread group processes in sub-threads, then the call will be done on that thread, right before NOTIFICATION_PROCESS or NOTIFICATION_PHYSICS_PROCESS, the \_process() or \_physics_process() or their internal versions are called.

---

[Variant](class_variant.md#class-variant) **call_thread_safe**(method: [StringName](class_stringname.md#class-stringname), ...)

This function ensures that the calling of this function will succeed, no matter whether it's being done from a thread or not. If called from a thread that is not allowed to call the function, the call will become deferred. Otherwise, the call will go through directly.

---

[bool](class_bool.md#class-bool) **can_auto_translate**()

Returns `true` if this node can automatically translate messages depending on the current locale. See auto_translate_mode, atr(), and atr_n().

---

[bool](class_bool.md#class-bool) **can_process**()

Returns `true` if the node can receive processing notifications and input callbacks (NOTIFICATION_PROCESS, \_input(), etc.) from the [SceneTree](class_scenetree.md#class-scenetree) and [Viewport](class_viewport.md#class-viewport). The returned value depends on process_mode:

- If set to PROCESS_MODE_PAUSABLE, returns `true` when the game is processing, i.e. [SceneTree.paused](class_scenetree.md#class-scenetree-property-paused) is `false`;
- If set to PROCESS_MODE_WHEN_PAUSED, returns `true` when the game is paused, i.e. [SceneTree.paused](class_scenetree.md#class-scenetree-property-paused) is `true`;
- If set to PROCESS_MODE_ALWAYS, always returns `true`;
- If set to PROCESS_MODE_DISABLED, always returns `false`;
- If set to PROCESS_MODE_INHERIT, use the parent node's process_mode to determine the result.

If the node is not inside the tree, returns `false` no matter the value of process_mode.

---

[Tween](class_tween.md#class-tween) **create_tween**()

Creates a new [Tween](class_tween.md#class-tween) and binds it to this node.

This is the equivalent of doing:

GDScript

```gdscript
get_tree().create_tween().bind_node(self)
```

C#

```csharp
GetTree().CreateTween().BindNode(this);
```

The Tween will start automatically on the next process frame or physics frame (depending on [TweenProcessMode](class_tween.md#enum-tween-tweenprocessmode)). See [Tween.bind_node()](class_tween.md#class-tween-method-bind-node) for more info on Tweens bound to nodes.

**Note:** The method can still be used when the node is not inside [SceneTree](class_scenetree.md#class-scenetree). It can fail in an unlikely case of using a custom [MainLoop](class_mainloop.md#class-mainloop).

---

Node **duplicate**(flags: [int](class_int.md#class-int) = 15)

Duplicates the node, returning a new node with all of its properties, signals, groups, and children copied from the original, recursively. The behavior can be tweaked through the `flags` (see DuplicateFlags). Internal nodes are not duplicated.

**Note:** For nodes with a [Script](class_script.md#class-script) attached, if [Object._init()](class_object.md#class-object-private-method-init) has been defined with required parameters, the duplicated node will not have a [Script](class_script.md#class-script).

**Note:** By default, this method will duplicate only properties marked for serialization (i.e. using [@GlobalScope.PROPERTY_USAGE_STORAGE](class_@globalscope.md#class-globalscope-constant-property-usage-storage), or in GDScript, [@GDScript.@export](class_@gdscript.md#class-gdscript-annotation-export)). If you want to duplicate all properties, use DUPLICATE_INTERNAL_STATE.

---

Node **find_child**(pattern: [String](class_string.md#class-string), recursive: [bool](class_bool.md#class-bool) = true, owned: [bool](class_bool.md#class-bool) = true)

Finds the first descendant of this node whose name matches `pattern`, returning `null` if no match is found. The matching is done against node names, *not* their paths, through [String.match()](class_string.md#class-string-method-match). As such, it is case-sensitive, `"*"` matches zero or more characters, and `"?"` matches any single character.

If `recursive` is `false`, only this node's direct children are checked. Nodes are checked in tree order, so this node's first direct child is checked first, then its own direct children, etc., before moving to the second direct child, and so on. Internal children are also included in the search (see `internal` parameter in add_child()).

If `owned` is `true`, only descendants with a valid owner node are checked.

**Note:** This method can be very slow. Consider storing a reference to the found node in a variable. Alternatively, use get_node() with unique names (see unique_name_in_owner).

**Note:** To find all descendant nodes matching a pattern or a class type, see find_children().

---

[Array](class_array.md#class-array)[Node] **find_children**(pattern: [String](class_string.md#class-string), type: [String](class_string.md#class-string) = "", recursive: [bool](class_bool.md#class-bool) = true, owned: [bool](class_bool.md#class-bool) = true)

Finds all descendants of this node whose names match `pattern`, returning an empty [Array](class_array.md#class-array) if no match is found. The matching is done against node names, *not* their paths, through [String.match()](class_string.md#class-string-method-match). As such, it is case-sensitive, `"*"` matches zero or more characters, and `"?"` matches any single character.

If `type` is not empty, only descendants inheriting from `type` are included (see [Object.is_class()](class_object.md#class-object-method-is-class)).

If `recursive` is `false`, only this node's direct children are checked. Nodes are checked in tree order, so this node's first direct child is checked first, then its own direct children, etc., before moving to the second direct child, and so on. Internal children are also included in the search (see `internal` parameter in add_child()).

If `owned` is `true`, only descendants with a valid owner node are checked.

**Note:** This method can be very slow. Consider storing references to the found nodes in a variable.

**Note:** To find a single descendant node matching a pattern, see find_child().

---

Node **find_parent**(pattern: [String](class_string.md#class-string))

Finds the first ancestor of this node whose name matches `pattern`, returning `null` if no match is found. The matching is done through [String.match()](class_string.md#class-string-method-match). As such, it is case-sensitive, `"*"` matches zero or more characters, and `"?"` matches any single character. See also find_child() and find_children().

**Note:** As this method walks upwards in the scene tree, it can be slow in large, deeply nested nodes. Consider storing a reference to the found node in a variable. Alternatively, use get_node() with unique names (see unique_name_in_owner).

---

[RID](class_rid.md#class-rid) **get_accessibility_element**()

Returns main accessibility element RID.

**Note:** This method should be called only during accessibility information updates (NOTIFICATION_ACCESSIBILITY_UPDATE).

---

Node **get_child**(idx: [int](class_int.md#class-int), include_internal: [bool](class_bool.md#class-bool) = false)

Fetches a child node by its index. Each child node has an index relative to its siblings (see get_index()). The first child is at index 0. Negative values can also be used to start from the end of the list. This method can be used in combination with get_child_count() to iterate over this node's children. If no child exists at the given index, this method returns `null` and an error is generated.

If `include_internal` is `false`, internal children are ignored (see add_child()'s `internal` parameter).

```gdscript
# Assuming the following are children of this node, in order:
# First, Middle, Last.

var a = get_child(0).name  # a is "First"
var b = get_child(1).name  # b is "Middle"
var b = get_child(2).name  # b is "Last"
var c = get_child(-1).name # c is "Last"
```

**Note:** To fetch a node by [NodePath](class_nodepath.md#class-nodepath), use get_node().

---

[int](class_int.md#class-int) **get_child_count**(include_internal: [bool](class_bool.md#class-bool) = false)

Returns the number of children of this node.

If `include_internal` is `false`, internal children are not counted (see add_child()'s `internal` parameter).

---

[Array](class_array.md#class-array)[Node] **get_children**(include_internal: [bool](class_bool.md#class-bool) = false)

Returns all children of this node inside an [Array](class_array.md#class-array).

If `include_internal` is `false`, excludes internal children from the returned array (see add_child()'s `internal` parameter).

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_groups**()

Returns an [Array](class_array.md#class-array) of group names that the node has been added to.

**Note:** To improve performance, the order of group names is *not* guaranteed and may vary between project runs. Therefore, do not rely on the group order.

**Note:** This method may also return some group names starting with an underscore (`_`). These are internally used by the engine. To avoid conflicts, do not use custom groups starting with underscores. To exclude internal groups, see the following code snippet:

GDScript

```gdscript
# Stores the node's non-internal groups only (as an array of StringNames).
var non_internal_groups = []
for group in get_groups():
    if not str(group).begins_with("_"):
        non_internal_groups.push_back(group)
```

C#

```csharp
// Stores the node's non-internal groups only (as a List of StringNames).
List<string> nonInternalGroups = new List<string>();
foreach (string group in GetGroups())
{
    if (!group.BeginsWith("_"))
        nonInternalGroups.Add(group);
}
```

---

[int](class_int.md#class-int) **get_index**(include_internal: [bool](class_bool.md#class-bool) = false)

Returns this node's order among its siblings. The first node's index is `0`. See also get_child().

If `include_internal` is `false`, returns the index ignoring internal children. The first, non-internal child will have an index of `0` (see add_child()'s `internal` parameter).

---

[Window](class_window.md#class-window) **get_last_exclusive_window**()

Returns the [Window](class_window.md#class-window) that contains this node, or the last exclusive child in a chain of windows starting with the one that contains this node.

---

[int](class_int.md#class-int) **get_multiplayer_authority**()

Returns the peer ID of the multiplayer authority for this node. See set_multiplayer_authority().

---

Node **get_node**(path: [NodePath](class_nodepath.md#class-nodepath))

Fetches a node. The [NodePath](class_nodepath.md#class-nodepath) can either be a relative path (from this node), or an absolute path (from the [SceneTree.root](class_scenetree.md#class-scenetree-property-root)) to a node. If `path` does not point to a valid node, generates an error and returns `null`. Attempts to access methods on the return value will result in an  *"Attempt to call <method> on a null instance."* error.

**Note:** Fetching by absolute path only works when the node is inside the scene tree (see is_inside_tree()).

**Example:** Assume this method is called from the Character node, inside the following tree:

```text
┖╴root
   ┠╴Character (you are here!)
   ┃  ┠╴Sword
   ┃  ┖╴Backpack
   ┃     ┖╴Dagger
   ┠╴MyGame
   ┖╴Swamp
      ┠╴Alligator
      ┠╴Mosquito
      ┖╴Goblin
```

The following calls will return a valid node:

GDScript

```gdscript
get_node("Sword")
get_node("Backpack/Dagger")
get_node("../Swamp/Alligator")
get_node("/root/MyGame")
```

C#

```csharp
GetNode("Sword");
GetNode("Backpack/Dagger");
GetNode("../Swamp/Alligator");
GetNode("/root/MyGame");
```

---

[Array](class_array.md#class-array) **get_node_and_resource**(path: [NodePath](class_nodepath.md#class-nodepath))

Fetches a node and its most nested resource as specified by the [NodePath](class_nodepath.md#class-nodepath)'s subname. Returns an [Array](class_array.md#class-array) of size `3` where:

- Element `0` is the **Node**, or `null` if not found;
- Element `1` is the subname's last nested [Resource](class_resource.md#class-resource), or `null` if not found;
- Element `2` is the remaining [NodePath](class_nodepath.md#class-nodepath), referring to an existing, non-[Resource](class_resource.md#class-resource) property (see [Object.get_indexed()](class_object.md#class-object-method-get-indexed)).

**Example:** Assume that the child's [Sprite2D.texture](class_sprite2d.md#class-sprite2d-property-texture) has been assigned an [AtlasTexture](class_atlastexture.md#class-atlastexture):

GDScript

```gdscript
var a = get_node_and_resource("Area2D/Sprite2D")
print(a[0].name) # Prints Sprite2D
print(a[1])      # Prints <null>
print(a[2])      # Prints ^""

var b = get_node_and_resource("Area2D/Sprite2D:texture:atlas")
print(b[0].name)        # Prints Sprite2D
print(b[1].get_class()) # Prints AtlasTexture
print(b[2])             # Prints ^""

var c = get_node_and_resource("Area2D/Sprite2D:texture:atlas:region")
print(c[0].name)        # Prints Sprite2D
print(c[1].get_class()) # Prints AtlasTexture
print(c[2])             # Prints ^":region"
```

C#

```csharp
var a = GetNodeAndResource(NodePath("Area2D/Sprite2D"));
GD.Print(a[0].Name); // Prints Sprite2D
GD.Print(a[1]);      // Prints <null>
GD.Print(a[2]);      // Prints ^"

var b = GetNodeAndResource(NodePath("Area2D/Sprite2D:texture:atlas"));
GD.Print(b[0].name);        // Prints Sprite2D
GD.Print(b[1].get_class()); // Prints AtlasTexture
GD.Print(b[2]);             // Prints ^""

var c = GetNodeAndResource(NodePath("Area2D/Sprite2D:texture:atlas:region"));
GD.Print(c[0].name);        // Prints Sprite2D
GD.Print(c[1].get_class()); // Prints AtlasTexture
GD.Print(c[2]);             // Prints ^":region"
```

---

Node **get_node_or_null**(path: [NodePath](class_nodepath.md#class-nodepath))

Fetches a node by [NodePath](class_nodepath.md#class-nodepath). Similar to get_node(), but does not generate an error if `path` does not point to a valid node.

---

[Variant](class_variant.md#class-variant) **get_node_rpc_config**()

Returns a [Dictionary](class_dictionary.md#class-dictionary) mapping method names to their RPC configuration defined for this node using rpc_config().

**Note:** This method only returns the RPC configuration assigned via rpc_config(). See [Script.get_rpc_config()](class_script.md#class-script-method-get-rpc-config) to retrieve the RPCs defined by the [Script](class_script.md#class-script).

---

[Array](class_array.md#class-array)[[int](class_int.md#class-int)] **get_orphan_node_ids**()

Returns object IDs of all orphan nodes (nodes outside the [SceneTree](class_scenetree.md#class-scenetree)). Used for debugging.

**Note:** get_orphan_node_ids() only works in debug builds. When called in a project exported in release mode, get_orphan_node_ids() will return an empty array.

---

Node **get_parent**()

Returns this node's parent node, or `null` if the node doesn't have a parent.

---

[NodePath](class_nodepath.md#class-nodepath) **get_path**()

Returns the node's absolute path, relative to the [SceneTree.root](class_scenetree.md#class-scenetree-property-root). If the node is not inside the scene tree, this method fails and returns an empty [NodePath](class_nodepath.md#class-nodepath).

---

[NodePath](class_nodepath.md#class-nodepath) **get_path_to**(node: Node, use_unique_path: [bool](class_bool.md#class-bool) = false)

Returns the relative [NodePath](class_nodepath.md#class-nodepath) from this node to the specified `node`. Both nodes must be in the same [SceneTree](class_scenetree.md#class-scenetree) or scene hierarchy, otherwise this method fails and returns an empty [NodePath](class_nodepath.md#class-nodepath).

If `use_unique_path` is `true`, returns the shortest path accounting for this node's unique name (see unique_name_in_owner).

**Note:** If you get a relative path which starts from a unique node, the path may be longer than a normal relative path, due to the addition of the unique node's name.

---

[float](class_float.md#class-float) **get_physics_process_delta_time**()

Returns the time elapsed (in seconds) since the last physics callback. This value is identical to \_physics_process()'s `delta` parameter, and is often consistent at run-time, unless [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second) is changed. See also NOTIFICATION_PHYSICS_PROCESS.

**Note:** The returned value will be larger than expected if running at a framerate lower than [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second) / [Engine.max_physics_steps_per_frame](class_engine.md#class-engine-property-max-physics-steps-per-frame) FPS. This is done to avoid "spiral of death" scenarios where performance would plummet due to an ever-increasing number of physics steps per frame. This behavior affects both \_process() and \_physics_process(). As a result, avoid using `delta` for time measurements in real-world seconds. Use the [Time](class_time.md#class-time) singleton's methods for this purpose instead, such as [Time.get_ticks_usec()](class_time.md#class-time-method-get-ticks-usec).

---

[float](class_float.md#class-float) **get_process_delta_time**()

Returns the time elapsed (in seconds) since the last process callback. This value is identical to \_process()'s `delta` parameter, and may vary from frame to frame. See also NOTIFICATION_PROCESS.

**Note:** The returned value will be larger than expected if running at a framerate lower than [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second) / [Engine.max_physics_steps_per_frame](class_engine.md#class-engine-property-max-physics-steps-per-frame) FPS. This is done to avoid "spiral of death" scenarios where performance would plummet due to an ever-increasing number of physics steps per frame. This behavior affects both \_process() and \_physics_process(). As a result, avoid using `delta` for time measurements in real-world seconds. Use the [Time](class_time.md#class-time) singleton's methods for this purpose instead, such as [Time.get_ticks_usec()](class_time.md#class-time-method-get-ticks-usec).

---

[bool](class_bool.md#class-bool) **get_scene_instance_load_placeholder**()

Returns `true` if this node is an instance load placeholder. See [InstancePlaceholder](class_instanceplaceholder.md#class-instanceplaceholder) and set_scene_instance_load_placeholder().

---

[SceneTree](class_scenetree.md#class-scenetree) **get_tree**()

Returns the [SceneTree](class_scenetree.md#class-scenetree) that contains this node. If this node is not inside the tree, generates an error and returns `null`. See also is_inside_tree().

---

[String](class_string.md#class-string) **get_tree_string**()

Returns the tree as a [String](class_string.md#class-string). Used mainly for debugging purposes. This version displays the path relative to the current node, and is good for copy/pasting into the get_node() function. It also can be used in game UI/UX.

May print, for example:

```text
TheGame
TheGame/Menu
TheGame/Menu/Label
TheGame/Menu/Camera2D
TheGame/SplashScreen
TheGame/SplashScreen/Camera2D
```

---

[String](class_string.md#class-string) **get_tree_string_pretty**()

Similar to get_tree_string(), this returns the tree as a [String](class_string.md#class-string). This version displays a more graphical representation similar to what is displayed in the Scene Dock. It is useful for inspecting larger trees.

May print, for example:

```text
┖╴TheGame
   ┠╴Menu
   ┃  ┠╴Label
   ┃  ┖╴Camera2D
   ┖╴SplashScreen
      ┖╴Camera2D
```

---

[Viewport](class_viewport.md#class-viewport) **get_viewport**()

Returns the node's closest [Viewport](class_viewport.md#class-viewport) ancestor, if the node is inside the tree. Otherwise, returns `null`.

---

[Window](class_window.md#class-window) **get_window**()

Returns the [Window](class_window.md#class-window) that contains this node. If the node is in the main window, this is equivalent to getting the root node (`get_tree().get_root()`).

---

[bool](class_bool.md#class-bool) **has_node**(path: [NodePath](class_nodepath.md#class-nodepath))

Returns `true` if the `path` points to a valid node. See also get_node().

---

[bool](class_bool.md#class-bool) **has_node_and_resource**(path: [NodePath](class_nodepath.md#class-nodepath))

Returns `true` if `path` points to a valid node and its subnames point to a valid [Resource](class_resource.md#class-resource), e.g. `Area2D/CollisionShape2D:shape`. Properties that are not [Resource](class_resource.md#class-resource) types (such as nodes or other [Variant](class_variant.md#class-variant) types) are not considered. See also get_node_and_resource().

---

[bool](class_bool.md#class-bool) **is_ancestor_of**(node: Node)

Returns `true` if the given `node` is a direct or indirect child of this node.

---

[bool](class_bool.md#class-bool) **is_displayed_folded**()

Returns `true` if the node is folded (collapsed) in the Scene dock. This method is intended to be used in editor plugins and tools. See also set_display_folded().

---

[bool](class_bool.md#class-bool) **is_editable_instance**(node: Node)

Returns `true` if `node` has editable children enabled relative to this node. This method is intended to be used in editor plugins and tools. See also set_editable_instance().

---

[bool](class_bool.md#class-bool) **is_greater_than**(node: Node)

Returns `true` if the given `node` occurs later in the scene hierarchy than this node. A node occurring later is usually processed last.

---

[bool](class_bool.md#class-bool) **is_in_group**(group: [StringName](class_stringname.md#class-stringname))

Returns `true` if this node has been added to the given `group`. See add_to_group() and remove_from_group(). See also notes in the description, and the [SceneTree](class_scenetree.md#class-scenetree)'s group methods.

---

[bool](class_bool.md#class-bool) **is_inside_tree**()

Returns `true` if this node is currently inside a [SceneTree](class_scenetree.md#class-scenetree). See also get_tree().

---

[bool](class_bool.md#class-bool) **is_multiplayer_authority**()

Returns `true` if the local system is the multiplayer authority of this node.

---

[bool](class_bool.md#class-bool) **is_node_ready**()

Returns `true` if the node is ready, i.e. it's inside scene tree and all its children are initialized.

request_ready() resets it back to `false`.

---

[bool](class_bool.md#class-bool) **is_part_of_edited_scene**()

Returns `true` if the node is part of the scene currently opened in the editor.

---

[bool](class_bool.md#class-bool) **is_physics_interpolated**()

Returns `true` if physics interpolation is enabled for this node (see physics_interpolation_mode).

**Note:** Interpolation will only be active if both the flag is set **and** physics interpolation is enabled within the [SceneTree](class_scenetree.md#class-scenetree). This can be tested using is_physics_interpolated_and_enabled().

---

[bool](class_bool.md#class-bool) **is_physics_interpolated_and_enabled**()

Returns `true` if physics interpolation is enabled (see physics_interpolation_mode) **and** enabled in the [SceneTree](class_scenetree.md#class-scenetree).

This is a convenience version of is_physics_interpolated() that also checks whether physics interpolation is enabled globally.

See [SceneTree.physics_interpolation](class_scenetree.md#class-scenetree-property-physics-interpolation) and [ProjectSettings.physics/common/physics_interpolation](class_projectsettings.md#class-projectsettings-property-physics-common-physics-interpolation).

---

[bool](class_bool.md#class-bool) **is_physics_processing**()

Returns `true` if physics processing is enabled (see set_physics_process()).

---

[bool](class_bool.md#class-bool) **is_physics_processing_internal**()

Returns `true` if internal physics processing is enabled (see set_physics_process_internal()).

---

[bool](class_bool.md#class-bool) **is_processing**()

Returns `true` if processing is enabled (see set_process()).

---

[bool](class_bool.md#class-bool) **is_processing_input**()

Returns `true` if the node is processing input (see set_process_input()).

---

[bool](class_bool.md#class-bool) **is_processing_internal**()

Returns `true` if internal processing is enabled (see set_process_internal()).

---

[bool](class_bool.md#class-bool) **is_processing_shortcut_input**()

Returns `true` if the node is processing shortcuts (see set_process_shortcut_input()).

---

[bool](class_bool.md#class-bool) **is_processing_unhandled_input**()

Returns `true` if the node is processing unhandled input (see set_process_unhandled_input()).

---

[bool](class_bool.md#class-bool) **is_processing_unhandled_key_input**()

Returns `true` if the node is processing unhandled key input (see set_process_unhandled_key_input()).

---

 **move_child**(child_node: Node, to_index: [int](class_int.md#class-int))

Moves `child_node` to the given index. A node's index is the order among its siblings. If `to_index` is negative, the index is counted from the end of the list. See also get_child() and get_index().

**Note:** The processing order of several engine callbacks (\_ready(), \_process(), etc.) and notifications sent through propagate_notification() is affected by tree order. [CanvasItem](class_canvasitem.md#class-canvasitem) nodes are also rendered in tree order. See also process_priority.

---

 **notify_deferred_thread_group**(what: [int](class_int.md#class-int))

Similar to call_deferred_thread_group(), but for notifications.

---

 **notify_thread_safe**(what: [int](class_int.md#class-int))

Similar to call_thread_safe(), but for notifications.

---

 **print_orphan_nodes**()

Prints all orphan nodes (nodes outside the [SceneTree](class_scenetree.md#class-scenetree)). Useful for debugging.

**Note:** This method only works in debug builds. It does nothing in a project exported in release mode.

---

 **print_tree**()

Prints the node and its children to the console, recursively. The node does not have to be inside the tree. This method outputs [NodePath](class_nodepath.md#class-nodepath)s relative to this node, and is good for copy/pasting into get_node(). See also print_tree_pretty().

May print, for example:

```text
.
Menu
Menu/Label
Menu/Camera2D
SplashScreen
SplashScreen/Camera2D
```

---

 **print_tree_pretty**()

Prints the node and its children to the console, recursively. The node does not have to be inside the tree. Similar to print_tree(), but the graphical representation looks like what is displayed in the editor's Scene dock. It is useful for inspecting larger trees.

May print, for example:

```text
┖╴TheGame
   ┠╴Menu
   ┃  ┠╴Label
   ┃  ┖╴Camera2D
   ┖╴SplashScreen
      ┖╴Camera2D
```

---

 **propagate_call**(method: [StringName](class_stringname.md#class-stringname), args: [Array](class_array.md#class-array) = [], parent_first: [bool](class_bool.md#class-bool) = false)

Calls the given `method` name, passing `args` as arguments, on this node and all of its children, recursively.

If `parent_first` is `true`, the method is called on this node first, then on all of its children. If `false`, the children's methods are called first.

---

 **propagate_notification**(what: [int](class_int.md#class-int))

Calls [Object.notification()](class_object.md#class-object-method-notification) with `what` on this node and all of its children, recursively.

---

 **queue_accessibility_update**()

Queues an accessibility information update for this node.

---

 **queue_free**()

Queues this node to be deleted at the end of the current frame. When deleted, all of its children are deleted as well, and all references to the node and its children become invalid.

Unlike with [Object.free()](class_object.md#class-object-method-free), the node is not deleted instantly, and it can still be accessed before deletion. It is also safe to call queue_free() multiple times. Use [Object.is_queued_for_deletion()](class_object.md#class-object-method-is-queued-for-deletion) to check if the node will be deleted at the end of the frame.

**Note:** The node will only be freed after all other deferred calls are finished. Using this method is not always the same as calling [Object.free()](class_object.md#class-object-method-free) through [Object.call_deferred()](class_object.md#class-object-method-call-deferred).

---

 **remove_child**(node: Node)

Removes a child `node`. The `node`, along with its children, are **not** deleted. To delete a node, see queue_free().

**Note:** When this node is inside the tree, this method sets the owner of the removed `node` (or its descendants) to `null`, if their owner is no longer an ancestor (see is_ancestor_of()).

---

 **remove_from_group**(group: [StringName](class_stringname.md#class-stringname))

Removes the node from the given `group`. Does nothing if the node is not in the `group`. See also notes in the description, and the [SceneTree](class_scenetree.md#class-scenetree)'s group methods.

---

 **reparent**(new_parent: Node, keep_global_transform: [bool](class_bool.md#class-bool) = true)

Changes the parent of this **Node** to the `new_parent`. The node needs to already have a parent. The node's owner is preserved if its owner is still reachable from the new location (i.e., the node is still a descendant of the new parent after the operation).

If `keep_global_transform` is `true`, the node's global transform will be preserved if supported. [Node2D](class_node2d.md#class-node2d), [Node3D](class_node3d.md#class-node3d) and [Control](class_control.md#class-control) support this argument (but [Control](class_control.md#class-control) keeps only position).

**Warning:** If [ProjectSettings.physics/common/physics_interpolation](class_projectsettings.md#class-projectsettings-property-physics-common-physics-interpolation) is enabled and reparenting causes a large change in global transform, the object may appear to move from its old position to its new one over the next physics tick. To avoid this, call reset_physics_interpolation() after reparenting.

---

 **replace_by**(node: Node, keep_groups: [bool](class_bool.md#class-bool) = false)

Replaces this node by the given `node`. All children of this node are moved to `node`.

If `keep_groups` is `true`, the `node` is added to the same groups that the replaced node is in (see add_to_group()).

**Warning:** The replaced node is removed from the tree, but it is **not** deleted. To prevent memory leaks, store a reference to the node in a variable, or use [Object.free()](class_object.md#class-object-method-free).

---

 **request_ready**()

Requests \_ready() to be called again the next time the node enters the tree. Does **not** immediately call \_ready().

**Note:** This method only affects the current node. If the node's children also need to request ready, this method needs to be called for each one of them. When the node and its children enter the tree again, the order of \_ready() callbacks will be the same as normal.

---

 **reset_physics_interpolation**()

When physics interpolation is active, moving a node to a radically different transform (such as placement within a level) can result in a visible glitch as the object is rendered moving from the old to new position over the physics tick.

That glitch can be prevented by calling this method, which temporarily disables interpolation until the physics tick is complete.

The notification NOTIFICATION_RESET_PHYSICS_INTERPOLATION will be received by the node and all children recursively.

**Note:** This function should be called **after** moving the node, rather than before.

---

[Error](class_@globalscope.md#enum-globalscope-error) **rpc**(method: [StringName](class_stringname.md#class-stringname), ...)

Sends a remote procedure call request for the given `method` to peers on the network (and locally), sending additional arguments to the method called by the RPC. The call request will only be received by nodes with the same [NodePath](class_nodepath.md#class-nodepath), including the exact same name. Behavior depends on the RPC configuration for the given `method` (see rpc_config() and [@GDScript.@rpc](class_@gdscript.md#class-gdscript-annotation-rpc)). By default, methods are not exposed to RPCs.

May return [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) if the call is successful, [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) if the arguments passed in the `method` do not match, [@GlobalScope.ERR_UNCONFIGURED](class_@globalscope.md#class-globalscope-constant-err-unconfigured) if the node's multiplayer cannot be fetched (such as when the node is not inside the tree), [@GlobalScope.ERR_CONNECTION_ERROR](class_@globalscope.md#class-globalscope-constant-err-connection-error) if multiplayer's connection is not available.

**Note:** You can only safely use RPCs on clients after you received the [MultiplayerAPI.connected_to_server](class_multiplayerapi.md#class-multiplayerapi-signal-connected-to-server) signal from the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi). You also need to keep track of the connection state, either by the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi) signals like [MultiplayerAPI.server_disconnected](class_multiplayerapi.md#class-multiplayerapi-signal-server-disconnected) or by checking (`get_multiplayer().peer.get_connection_status() == CONNECTION_CONNECTED`).

---

 **rpc_config**(method: [StringName](class_stringname.md#class-stringname), config: [Variant](class_variant.md#class-variant))

Changes the RPC configuration for the given `method`. `config` should either be `null` to disable the feature (as by default), or a [Dictionary](class_dictionary.md#class-dictionary) containing the following entries:

- `rpc_mode`: see [RPCMode](class_multiplayerapi.md#enum-multiplayerapi-rpcmode);
- `transfer_mode`: see [TransferMode](class_multiplayerpeer.md#enum-multiplayerpeer-transfermode);
- `call_local`: if `true`, the method will also be called locally;
- `channel`: an [int](class_int.md#class-int) representing the channel to send the RPC on.

**Note:** In GDScript, this method corresponds to the [@GDScript.@rpc](class_@gdscript.md#class-gdscript-annotation-rpc) annotation, with various parameters passed (`@rpc(any)`, `@rpc(authority)`...). See also the [high-level multiplayer](../tutorials/networking/high_level_multiplayer.md) tutorial.

---

[Error](class_@globalscope.md#enum-globalscope-error) **rpc_id**(peer_id: [int](class_int.md#class-int), method: [StringName](class_stringname.md#class-stringname), ...)

Sends a rpc() to a specific peer identified by `peer_id` (see [MultiplayerPeer.set_target_peer()](class_multiplayerpeer.md#class-multiplayerpeer-method-set-target-peer)).

May return [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) if the call is successful, [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) if the arguments passed in the `method` do not match, [@GlobalScope.ERR_UNCONFIGURED](class_@globalscope.md#class-globalscope-constant-err-unconfigured) if the node's multiplayer cannot be fetched (such as when the node is not inside the tree), [@GlobalScope.ERR_CONNECTION_ERROR](class_@globalscope.md#class-globalscope-constant-err-connection-error) if multiplayer's connection is not available.

---

 **set_deferred_thread_group**(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Similar to call_deferred_thread_group(), but for setting properties.

---

 **set_display_folded**(fold: [bool](class_bool.md#class-bool))

If set to `true`, the node appears folded in the Scene dock. As a result, all of its children are hidden. This method is intended to be used in editor plugins and tools, but it also works in release builds. See also is_displayed_folded().

---

 **set_editable_instance**(node: Node, is_editable: [bool](class_bool.md#class-bool))

Set to `true` to allow all nodes owned by `node` to be available, and editable, in the Scene dock, even if their owner is not the scene root. This method is intended to be used in editor plugins and tools, but it also works in release builds. See also is_editable_instance().

---

 **set_multiplayer_authority**(id: [int](class_int.md#class-int), recursive: [bool](class_bool.md#class-bool) = true)

Sets the node's multiplayer authority to the peer with the given peer `id`. The multiplayer authority is the peer that has authority over the node on the network. Defaults to peer ID 1 (the server). Useful in conjunction with rpc_config() and the [MultiplayerAPI](class_multiplayerapi.md#class-multiplayerapi).

If `recursive` is `true`, the given peer is recursively set as the authority for all children of this node.

**Warning:** This does **not** automatically replicate the new authority to other peers. It is the developer's responsibility to do so. You may replicate the new authority's information using [MultiplayerSpawner.spawn_function](class_multiplayerspawner.md#class-multiplayerspawner-property-spawn-function), an RPC, or a [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class-multiplayersynchronizer). Furthermore, the parent's authority does **not** propagate to newly added children.

---

 **set_physics_process**(enable: [bool](class_bool.md#class-bool))

If set to `true`, enables physics (fixed framerate) processing. When a node is being processed, it will receive a NOTIFICATION_PHYSICS_PROCESS at a fixed (usually 60 FPS, see [Engine.physics_ticks_per_second](class_engine.md#class-engine-property-physics-ticks-per-second) to change) interval (and the \_physics_process() callback will be called if it exists).

**Note:** If \_physics_process() is overridden, this will be automatically enabled before \_ready() is called.

---

 **set_physics_process_internal**(enable: [bool](class_bool.md#class-bool))

If set to `true`, enables internal physics for this node. Internal physics processing happens in isolation from the normal \_physics_process() calls and is used by some nodes internally to guarantee proper functioning even if the node is paused or physics processing is disabled for scripting (set_physics_process()).

**Warning:** Built-in nodes rely on internal processing for their internal logic. Disabling it is unsafe and may lead to unexpected behavior. Use this method if you know what you are doing.

---

 **set_process**(enable: [bool](class_bool.md#class-bool))

If set to `true`, enables processing. When a node is being processed, it will receive a NOTIFICATION_PROCESS on every drawn frame (and the \_process() callback will be called if it exists).

**Note:** If \_process() is overridden, this will be automatically enabled before \_ready() is called.

**Note:** This method only affects the \_process() callback, i.e. it has no effect on other callbacks like \_physics_process(). If you want to disable all processing for the node, set process_mode to PROCESS_MODE_DISABLED.

---

 **set_process_input**(enable: [bool](class_bool.md#class-bool))

If set to `true`, enables input processing.

**Note:** If \_input() is overridden, this will be automatically enabled before \_ready() is called. Input processing is also already enabled for GUI controls, such as [Button](class_button.md#class-button) and [TextEdit](class_textedit.md#class-textedit).

---

 **set_process_internal**(enable: [bool](class_bool.md#class-bool))

If set to `true`, enables internal processing for this node. Internal processing happens in isolation from the normal \_process() calls and is used by some nodes internally to guarantee proper functioning even if the node is paused or processing is disabled for scripting (set_process()).

**Warning:** Built-in nodes rely on internal processing for their internal logic. Disabling it is unsafe and may lead to unexpected behavior. Use this method if you know what you are doing.

---

 **set_process_shortcut_input**(enable: [bool](class_bool.md#class-bool))

If set to `true`, enables shortcut processing for this node.

**Note:** If \_shortcut_input() is overridden, this will be automatically enabled before \_ready() is called.

---

 **set_process_unhandled_input**(enable: [bool](class_bool.md#class-bool))

If set to `true`, enables unhandled input processing. It enables the node to receive all input that was not previously handled (usually by a [Control](class_control.md#class-control)).

**Note:** If \_unhandled_input() is overridden, this will be automatically enabled before \_ready() is called. Unhandled input processing is also already enabled for GUI controls, such as [Button](class_button.md#class-button) and [TextEdit](class_textedit.md#class-textedit).

---

 **set_process_unhandled_key_input**(enable: [bool](class_bool.md#class-bool))

If set to `true`, enables unhandled key input processing.

**Note:** If \_unhandled_key_input() is overridden, this will be automatically enabled before \_ready() is called.

---

 **set_scene_instance_load_placeholder**(load_placeholder: [bool](class_bool.md#class-bool))

If set to `true`, the node becomes an [InstancePlaceholder](class_instanceplaceholder.md#class-instanceplaceholder) when packed and instantiated from a [PackedScene](class_packedscene.md#class-packedscene). See also get_scene_instance_load_placeholder().

---

 **set_thread_safe**(property: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

Similar to call_thread_safe(), but for setting properties.

---

 **set_translation_domain_inherited**()

Makes this node inherit the translation domain from its parent node. If this node has no parent, the main translation domain will be used.

This is the default behavior for all nodes. Calling [Object.set_translation_domain()](class_object.md#class-object-method-set-translation-domain) disables this behavior.

---

 **update_configuration_warnings**()

Refreshes the warnings displayed for this node in the Scene dock. Use \_get_configuration_warnings() to customize the warning messages to display.
