# NavigationObstacle2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

2D obstacle used to affect navigation mesh baking or constrain velocities of avoidance controlled agents.

## Description

An obstacle needs a navigation map and outline vertices defined to work correctly. The outlines can not cross or overlap.

Obstacles can be included in the navigation mesh baking process when affect_navigation_mesh is enabled. They do not add walkable geometry, instead their role is to discard other source geometry inside the shape. This can be used to prevent navigation mesh from appearing in unwanted places. If carve_navigation_mesh is enabled the baked shape will not be affected by offsets of the navigation mesh baking, e.g. the agent radius.

With avoidance_enabled the obstacle can constrain the avoidance velocities of avoidance using agents. If the obstacle's vertices are wound in clockwise order, avoidance agents will be pushed in by the obstacle, otherwise, avoidance agents will be pushed out. Obstacles using vertices and avoidance can warp to a new position but should not be moved every single frame as each change requires a rebuild of the avoidance map.

## Tutorials

- [Using NavigationObstacles](../tutorials/navigation/navigation_using_navigationobstacles.md)

## Properties

| [bool](class_bool.md#class-bool)                                           | affect_navigation_mesh   | `false`                |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|------------------------|
| [bool](class_bool.md#class-bool)                                           | avoidance_enabled             | `true`                 |
| [int](class_int.md#class-int)                                              | avoidance_layers               | `1`                    |
| [bool](class_bool.md#class-bool)                                           | carve_navigation_mesh     | `false`                |
| [float](class_float.md#class-float)                                        | radius                                   | `0.0`                  |
| [Vector2](class_vector2.md#class-vector2)                                  | velocity                               | `Vector2(0, 0)`        |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | vertices                               | `PackedVector2Array()` |

## Methods

| [bool](class_bool.md#class-bool)   | get_avoidance_layer_value(layer_number: [int](class_int.md#class-int))                                          |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [RID](class_rid.md#class-rid)      | get_navigation_map()                                                                                                   |
| [RID](class_rid.md#class-rid)      | get_rid()                                                                                                                         |
|                                    | set_avoidance_layer_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
|                                    | set_navigation_map(navigation_map: [RID](class_rid.md#class-rid))                                                      |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **affect_navigation_mesh** = `false`

-  **set_affect_navigation_mesh**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_affect_navigation_mesh**()

If enabled and parsed in a navigation mesh baking process the obstacle will discard source geometry inside its vertices defined shape.

---

[bool](class_bool.md#class-bool) **avoidance_enabled** = `true`

-  **set_avoidance_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_avoidance_enabled**()

If `true` the obstacle affects avoidance using agents.

---

[int](class_int.md#class-int) **avoidance_layers** = `1`

-  **set_avoidance_layers**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_avoidance_layers**()

A bitfield determining the avoidance layers for this obstacle. Agents with a matching bit on the their avoidance mask will avoid this obstacle.

---

[bool](class_bool.md#class-bool) **carve_navigation_mesh** = `false`

-  **set_carve_navigation_mesh**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_carve_navigation_mesh**()

If enabled the obstacle vertices will carve into the baked navigation mesh with the shape unaffected by additional offsets (e.g. agent radius).

It will still be affected by further postprocessing of the baking process, like edge and polygon simplification.

Requires affect_navigation_mesh to be enabled.

---

[float](class_float.md#class-float) **radius** = `0.0`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

Sets the avoidance radius for the obstacle.

---

[Vector2](class_vector2.md#class-vector2) **velocity** = `Vector2(0, 0)`

-  **set_velocity**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_velocity**()

Sets the wanted velocity for the obstacle so other agent's can better predict the obstacle if it is moved with a velocity regularly (every frame) instead of warped to a new position. Does only affect avoidance for the obstacles radius. Does nothing for the obstacles static vertices.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **vertices** = `PackedVector2Array()`

-  **set_vertices**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_vertices**()

The outline vertices of the obstacle. If the vertices are winded in clockwise order agents will be pushed in by the obstacle, else they will be pushed out. Outlines can not be crossed or overlap. Should the vertices using obstacle be warped to a new position agent's can not predict this movement and may get trapped inside the obstacle.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **get_avoidance_layer_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the avoidance_layers bitmask is enabled, given a `layer_number` between 1 and 32.

---

[RID](class_rid.md#class-rid) **get_navigation_map**()

Returns the [RID](class_rid.md#class-rid) of the navigation map for this NavigationObstacle node. This function returns always the map set on the NavigationObstacle node and not the map of the abstract obstacle on the NavigationServer. If the obstacle map is changed directly with the NavigationServer API the NavigationObstacle node will not be aware of the map change. Use set_navigation_map() to change the navigation map for the NavigationObstacle and also update the obstacle on the NavigationServer.

---

[RID](class_rid.md#class-rid) **get_rid**()

Returns the [RID](class_rid.md#class-rid) of this obstacle on the [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d).

---

 **set_avoidance_layer_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the avoidance_layers bitmask, given a `layer_number` between 1 and 32.

---

 **set_navigation_map**(navigation_map: [RID](class_rid.md#class-rid))

Sets the [RID](class_rid.md#class-rid) of the navigation map this NavigationObstacle node should use and also updates the `obstacle` on the NavigationServer.
