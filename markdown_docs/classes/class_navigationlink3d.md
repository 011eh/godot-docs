# NavigationLink3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A link between two positions on [NavigationRegion3D](class_navigationregion3d.md#class-navigationregion3d)s that agents can be routed through.

## Description

A link between two positions on [NavigationRegion3D](class_navigationregion3d.md#class-navigationregion3d)s that agents can be routed through. These positions can be on the same [NavigationRegion3D](class_navigationregion3d.md#class-navigationregion3d) or on two different ones. Links are useful to express navigation methods other than traveling along the surface of the navigation mesh, such as ziplines, teleporters, or gaps that can be jumped across.

## Tutorials

- [Using NavigationLinks](../tutorials/navigation/navigation_using_navigationlinks.md)

## Properties

| [bool](class_bool.md#class-bool)          | bidirectional         | `true`             |
|-------------------------------------------|-------------------------------------------------------------------------|--------------------|
| [bool](class_bool.md#class-bool)          | enabled                     | `true`             |
| [Vector3](class_vector3.md#class-vector3) | end_position           | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float)       | enter_cost               | `0.0`              |
| [int](class_int.md#class-int)             | navigation_layers | `1`                |
| [Vector3](class_vector3.md#class-vector3) | start_position       | `Vector3(0, 0, 0)` |
| [float](class_float.md#class-float)       | travel_cost             | `1.0`              |

## Methods

| [Vector3](class_vector3.md#class-vector3)   | get_global_end_position()                                                                                           |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Vector3](class_vector3.md#class-vector3)   | get_global_start_position()                                                                                       |
| [bool](class_bool.md#class-bool)            | get_navigation_layer_value(layer_number: [int](class_int.md#class-int))                                          |
| [RID](class_rid.md#class-rid)               | get_navigation_map()                                                                                                     |
| [RID](class_rid.md#class-rid)               | get_rid()                                                                                                                           |
|                                             | set_global_end_position(position: [Vector3](class_vector3.md#class-vector3))                                        |
|                                             | set_global_start_position(position: [Vector3](class_vector3.md#class-vector3))                                    |
|                                             | set_navigation_layer_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
|                                             | set_navigation_map(navigation_map: [RID](class_rid.md#class-rid))                                                        |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **bidirectional** = `true`

-  **set_bidirectional**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_bidirectional**()

Whether this link can be traveled in both directions or only from start_position to end_position.

---

[bool](class_bool.md#class-bool) **enabled** = `true`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

Whether this link is currently active. If `false`, [NavigationServer3D.map_get_path()](class_navigationserver3d.md#class-navigationserver3d-method-map-get-path) will ignore this link.

---

[Vector3](class_vector3.md#class-vector3) **end_position** = `Vector3(0, 0, 0)`

-  **set_end_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_end_position**()

Ending position of the link.

This position will search out the nearest polygon in the navigation mesh to attach to.

The distance the link will search is controlled by [NavigationServer3D.map_set_link_connection_radius()](class_navigationserver3d.md#class-navigationserver3d-method-map-set-link-connection-radius).

---

[float](class_float.md#class-float) **enter_cost** = `0.0`

-  **set_enter_cost**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_enter_cost**()

When pathfinding enters this link from another regions navigation mesh the enter_cost value is added to the path distance for determining the shortest path.

---

[int](class_int.md#class-int) **navigation_layers** = `1`

-  **set_navigation_layers**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_navigation_layers**()

A bitfield determining all navigation layers the link belongs to. These navigation layers will be checked when requesting a path with [NavigationServer3D.map_get_path()](class_navigationserver3d.md#class-navigationserver3d-method-map-get-path).

---

[Vector3](class_vector3.md#class-vector3) **start_position** = `Vector3(0, 0, 0)`

-  **set_start_position**(value: [Vector3](class_vector3.md#class-vector3))
- [Vector3](class_vector3.md#class-vector3) **get_start_position**()

Starting position of the link.

This position will search out the nearest polygon in the navigation mesh to attach to.

The distance the link will search is controlled by [NavigationServer3D.map_set_link_connection_radius()](class_navigationserver3d.md#class-navigationserver3d-method-map-set-link-connection-radius).

---

[float](class_float.md#class-float) **travel_cost** = `1.0`

-  **set_travel_cost**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_travel_cost**()

When pathfinding moves along the link the traveled distance is multiplied with travel_cost for determining the shortest path.

---

## Method Descriptions

[Vector3](class_vector3.md#class-vector3) **get_global_end_position**()

Returns the end_position that is relative to the link as a global position.

---

[Vector3](class_vector3.md#class-vector3) **get_global_start_position**()

Returns the start_position that is relative to the link as a global position.

---

[bool](class_bool.md#class-bool) **get_navigation_layer_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the navigation_layers bitmask is enabled, given a `layer_number` between 1 and 32.

---

[RID](class_rid.md#class-rid) **get_navigation_map**()

Returns the current navigation map [RID](class_rid.md#class-rid) used by this link.

---

[RID](class_rid.md#class-rid) **get_rid**()

Returns the [RID](class_rid.md#class-rid) of this link on the [NavigationServer3D](class_navigationserver3d.md#class-navigationserver3d).

---

 **set_global_end_position**(position: [Vector3](class_vector3.md#class-vector3))

Sets the end_position that is relative to the link from a global `position`.

---

 **set_global_start_position**(position: [Vector3](class_vector3.md#class-vector3))

Sets the start_position that is relative to the link from a global `position`.

---

 **set_navigation_layer_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the navigation_layers bitmask, given a `layer_number` between 1 and 32.

---

 **set_navigation_map**(navigation_map: [RID](class_rid.md#class-rid))

Sets the [RID](class_rid.md#class-rid) of the navigation map this link should use. By default the link will automatically join the [World3D](class_world3d.md#class-world3d) default navigation map so this function is only required to override the default map.
