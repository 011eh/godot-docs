# PolygonPathFinder

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

## Methods

| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)   | find_path(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2))                                                                |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Rect2](class_rect2.md#class-rect2)                                          | get_bounds()                                                                                                                                                            |
| [Vector2](class_vector2.md#class-vector2)                                    | get_closest_point(point: [Vector2](class_vector2.md#class-vector2))                                                                                              |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)   | get_intersections(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2))                                                |
| [float](class_float.md#class-float)                                          | get_point_penalty(idx: [int](class_int.md#class-int))                                                                                                            |
| [bool](class_bool.md#class-bool)                                             | is_point_inside(point: [Vector2](class_vector2.md#class-vector2))                                                                                                  |
|                                                                              | set_point_penalty(idx: [int](class_int.md#class-int), penalty: [float](class_float.md#class-float))                                                              |
|                                                                              | setup(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), connections: [PackedInt32Array](class_packedint32array.md#class-packedint32array)) |

---

## Method Descriptions

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **find_path**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Rect2](class_rect2.md#class-rect2) **get_bounds**()

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[Vector2](class_vector2.md#class-vector2) **get_closest_point**(point: [Vector2](class_vector2.md#class-vector2))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_intersections**(from: [Vector2](class_vector2.md#class-vector2), to: [Vector2](class_vector2.md#class-vector2))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[float](class_float.md#class-float) **get_point_penalty**(idx: [int](class_int.md#class-int))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

[bool](class_bool.md#class-bool) **is_point_inside**(point: [Vector2](class_vector2.md#class-vector2))

Returns `true` if `point` falls inside the polygon area.

GDScript

```gdscript
var polygon_path_finder = PolygonPathFinder.new()
var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
var connections = [0, 1, 1, 2, 2, 0]
polygon_path_finder.setup(points, connections)
print(polygon_path_finder.is_point_inside(Vector2(0.2, 0.2))) # Prints true
print(polygon_path_finder.is_point_inside(Vector2(1.0, 1.0))) # Prints false
```

C#

```csharp
var polygonPathFinder = new PolygonPathFinder();
Vector2[] points =
[
    new Vector2(0.0f, 0.0f),
    new Vector2(1.0f, 0.0f),
    new Vector2(0.0f, 1.0f)
];
int[] connections = [0, 1, 1, 2, 2, 0];
polygonPathFinder.Setup(points, connections);
GD.Print(polygonPathFinder.IsPointInside(new Vector2(0.2f, 0.2f))); // Prints True
GD.Print(polygonPathFinder.IsPointInside(new Vector2(1.0f, 1.0f))); // Prints False
```

---

 **set_point_penalty**(idx: [int](class_int.md#class-int), penalty: [float](class_float.md#class-float))

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

 **setup**(points: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), connections: [PackedInt32Array](class_packedint32array.md#class-packedint32array))

Sets up **PolygonPathFinder** with an array of points that define the vertices of the polygon, and an array of indices that determine the edges of the polygon.

The length of `connections` must be even, returns an error if odd.

GDScript

```gdscript
var polygon_path_finder = PolygonPathFinder.new()
var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
var connections = [0, 1, 1, 2, 2, 0]
polygon_path_finder.setup(points, connections)
```

C#

```csharp
var polygonPathFinder = new PolygonPathFinder();
Vector2[] points =
[
    new Vector2(0.0f, 0.0f),
    new Vector2(1.0f, 0.0f),
    new Vector2(0.0f, 1.0f)
];
int[] connections = [0, 1, 1, 2, 2, 0];
polygonPathFinder.Setup(points, connections);
```
