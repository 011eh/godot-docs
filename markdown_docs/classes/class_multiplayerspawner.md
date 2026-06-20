# MultiplayerSpawner

**Inherits:** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Automatically replicates spawnable nodes from the authority to other multiplayer peers.

## Description

Spawnable scenes can be configured in the editor or through code (see add_spawnable_scene()).

Also supports custom node spawns through spawn(), calling spawn_function on all peers.

Internally, **MultiplayerSpawner** uses [MultiplayerAPI.object_configuration_add()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-add) to notify spawns passing the spawned node as the `object` and itself as the `configuration`, and [MultiplayerAPI.object_configuration_remove()](class_multiplayerapi.md#class-multiplayerapi-method-object-configuration-remove) to notify despawns in a similar way.

## Properties

| [Callable](class_callable.md#class-callable)   | spawn_function   |                |
|------------------------------------------------|-----------------------------------------------------------------------|----------------|
| [int](class_int.md#class-int)                  | spawn_limit         | `0`            |
| [NodePath](class_nodepath.md#class-nodepath)   | spawn_path           | `NodePath("")` |

## Methods

|                                        | add_spawnable_scene(path: [String](class_string.md#class-string))   |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
|                                        | clear_spawnable_scenes()                                         |
| [String](class_string.md#class-string) | get_spawnable_scene(index: [int](class_int.md#class-int))           |
| [int](class_int.md#class-int)          | get_spawnable_scene_count()                                   |
| [Node](class_node.md#class-node)       | spawn(data: [Variant](class_variant.md#class-variant) = null)                     |

---

## Signals

**despawned**(node: [Node](class_node.md#class-node))

Emitted when a spawnable scene or custom spawn was despawned by the multiplayer authority. Only called on remote peers.

---

**spawned**(node: [Node](class_node.md#class-node))

Emitted when a spawnable scene or custom spawn was spawned by the multiplayer authority. Only called on remote peers.

---

## Property Descriptions

[Callable](class_callable.md#class-callable) **spawn_function**

-  **set_spawn_function**(value: [Callable](class_callable.md#class-callable))
- [Callable](class_callable.md#class-callable) **get_spawn_function**()

Method called on all peers when a custom spawn() is requested by the authority. Will receive the `data` parameter, and should return a [Node](class_node.md#class-node) that is not in the scene tree.

**Note:** The returned node should **not** be added to the scene with [Node.add_child()](class_node.md#class-node-method-add-child). This is done automatically.

---

[int](class_int.md#class-int) **spawn_limit** = `0`

-  **set_spawn_limit**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_spawn_limit**()

Maximum number of nodes allowed to be spawned by this spawner. Includes both spawnable scenes and custom spawns.

When set to `0` (the default), there is no limit.

---

[NodePath](class_nodepath.md#class-nodepath) **spawn_path** = `NodePath("")`

-  **set_spawn_path**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_spawn_path**()

Path to the spawn root. Spawnable scenes that are added as direct children are replicated to other peers.

---

## Method Descriptions

 **add_spawnable_scene**(path: [String](class_string.md#class-string))

Adds a scene path to spawnable scenes, making it automatically replicated from the multiplayer authority to other peers when added as children of the node pointed by spawn_path.

---

 **clear_spawnable_scenes**()

Clears all spawnable scenes. Does not despawn existing instances on remote peers.

---

[String](class_string.md#class-string) **get_spawnable_scene**(index: [int](class_int.md#class-int))

Returns the spawnable scene path by index.

---

[int](class_int.md#class-int) **get_spawnable_scene_count**()

Returns the count of spawnable scene paths.

---

[Node](class_node.md#class-node) **spawn**(data: [Variant](class_variant.md#class-variant) = null)

Requests a custom spawn, with `data` passed to spawn_function on all peers. Returns the locally spawned node instance already inside the scene tree, and added as a child of the node pointed by spawn_path.

**Note:** Spawnable scenes are spawned automatically. spawn() is only needed for custom spawns.
