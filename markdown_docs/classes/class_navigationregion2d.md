# NavigationRegion2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A traversable 2D region that [NavigationAgent2D](class_navigationagent2d.md#class-navigationagent2d)s can use for pathfinding.

## Description

A traversable 2D region based on a [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon) that [NavigationAgent2D](class_navigationagent2d.md#class-navigationagent2d)s can use for pathfinding.

Two regions can be connected to each other if they share a similar edge. You can set the minimum distance between two vertices required to connect two edges by using [NavigationServer2D.map_set_edge_connection_margin()](class_navigationserver2d.md#class-navigationserver2d-method-map-set-edge-connection-margin).

**Note:** Overlapping two regions' navigation polygons is not enough for connecting two regions. They must share a similar edge.

The pathfinding cost of entering a region from another region can be controlled with the enter_cost value.

**Note:** This value is not added to the path cost when the start position is already inside this region.

The pathfinding cost of traveling distances inside this region can be controlled with the travel_cost multiplier.

**Note:** This node caches changes to its properties, so if you make changes to the underlying region [RID](class_rid.md#class-rid) in [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d), they will not be reflected in this node's properties.

## Tutorials

- [Using NavigationRegions](../tutorials/navigation/navigation_using_navigationregions.md)

## Properties

| [bool](class_bool.md#class-bool)                                        | enabled                           | `true`   |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------|----------|
| [float](class_float.md#class-float)                                     | enter_cost                     | `0.0`    |
| [int](class_int.md#class-int)                                           | navigation_layers       | `1`      |
| [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon) | navigation_polygon     |          |
| [float](class_float.md#class-float)                                     | travel_cost                   | `1.0`    |
| [bool](class_bool.md#class-bool)                                        | use_edge_connections | `true`   |

## Methods

|                                     | bake_navigation_polygon(on_thread: [bool](class_bool.md#class-bool) = true)                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect2](class_rect2.md#class-rect2) | get_bounds()                                                                                                                     |
| [bool](class_bool.md#class-bool)    | get_navigation_layer_value(layer_number: [int](class_int.md#class-int))                                          |
| [RID](class_rid.md#class-rid)       | get_navigation_map()                                                                                                     |
| [RID](class_rid.md#class-rid)       | get_region_rid()                                                                                                             |
| [RID](class_rid.md#class-rid)       | get_rid()                                                                                                                           |
| [bool](class_bool.md#class-bool)    | is_baking()                                                                                                                       |
|                                     | set_navigation_layer_value(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool)) |
|                                     | set_navigation_map(navigation_map: [RID](class_rid.md#class-rid))                                                        |

---

## Signals

**bake_finished**()

Emitted when a navigation polygon bake operation is completed.

---

**navigation_polygon_changed**()

Emitted when the used navigation polygon is replaced or changes to the internals of the current navigation polygon are committed.

---

## Property Descriptions

[bool](class_bool.md#class-bool) **enabled** = `true`

-  **set_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_enabled**()

Determines if the **NavigationRegion2D** is enabled or disabled.

---

[float](class_float.md#class-float) **enter_cost** = `0.0`

-  **set_enter_cost**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_enter_cost**()

When pathfinding enters this region's navigation mesh from another regions navigation mesh the enter_cost value is added to the path distance for determining the shortest path.

---

[int](class_int.md#class-int) **navigation_layers** = `1`

-  **set_navigation_layers**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_navigation_layers**()

A bitfield determining all navigation layers the region belongs to. These navigation layers can be checked upon when requesting a path with [NavigationServer2D.map_get_path()](class_navigationserver2d.md#class-navigationserver2d-method-map-get-path).

---

[NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon) **navigation_polygon**

-  **set_navigation_polygon**(value: [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon))
- [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon) **get_navigation_polygon**()

The [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon) resource to use.

---

[float](class_float.md#class-float) **travel_cost** = `1.0`

-  **set_travel_cost**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_travel_cost**()

When pathfinding moves inside this region's navigation mesh the traveled distances are multiplied with travel_cost for determining the shortest path.

---

[bool](class_bool.md#class-bool) **use_edge_connections** = `true`

-  **set_use_edge_connections**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_use_edge_connections**()

If enabled the navigation region will use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

## Method Descriptions

 **bake_navigation_polygon**(on_thread: [bool](class_bool.md#class-bool) = true)

Bakes the [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon). If `on_thread` is set to `true` (default), the baking is done on a separate thread.

---

[Rect2](class_rect2.md#class-rect2) **get_bounds**()

Returns the axis-aligned rectangle for the region's transformed navigation mesh.

---

[bool](class_bool.md#class-bool) **get_navigation_layer_value**(layer_number: [int](class_int.md#class-int))

Returns whether or not the specified layer of the navigation_layers bitmask is enabled, given a `layer_number` between 1 and 32.

---

[RID](class_rid.md#class-rid) **get_navigation_map**()

Returns the current navigation map [RID](class_rid.md#class-rid) used by this region.

---

[RID](class_rid.md#class-rid) **get_region_rid**()

**Deprecated:** Use get_rid() instead.

Returns the [RID](class_rid.md#class-rid) of this region on the [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d).

---

[RID](class_rid.md#class-rid) **get_rid**()

Returns the [RID](class_rid.md#class-rid) of this region on the [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d). Combined with [NavigationServer2D.map_get_closest_point_owner()](class_navigationserver2d.md#class-navigationserver2d-method-map-get-closest-point-owner) can be used to identify the **NavigationRegion2D** closest to a point on the merged navigation map.

---

[bool](class_bool.md#class-bool) **is_baking**()

Returns `true` when the [NavigationPolygon](class_navigationpolygon.md#class-navigationpolygon) is being baked on a background thread.

---

 **set_navigation_layer_value**(layer_number: [int](class_int.md#class-int), value: [bool](class_bool.md#class-bool))

Based on `value`, enables or disables the specified layer in the navigation_layers bitmask, given a `layer_number` between 1 and 32.

---

 **set_navigation_map**(navigation_map: [RID](class_rid.md#class-rid))

Sets the [RID](class_rid.md#class-rid) of the navigation map this region should use. By default the region will automatically join the [World2D](class_world2d.md#class-world2d) default navigation map so this function is only required to override the default map.
