# NavigationMeshSourceGeometryData2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Container for parsed source geometry data used in navigation mesh baking.

## Description

Container for parsed source geometry data used in navigation mesh baking.

## Methods

|                                                                                                                 | add_obstruction_outline(shape_outline: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))                                                     |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                 | add_projected_obstruction(vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), carve: [bool](class_bool.md#class-bool))             |
|                                                                                                                 | add_traversable_outline(shape_outline: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))                                                     |
|                                                                                                                 | append_obstruction_outlines(obstruction_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) |
|                                                                                                                 | append_traversable_outlines(traversable_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)]) |
|                                                                                                                 | clear()                                                                                                                                                                                  |
|                                                                                                                 | clear_projected_obstructions()                                                                                                                                    |
| [Rect2](class_rect2.md#class-rect2)                                                                             | get_bounds()                                                                                                                                                                        |
| [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] | get_obstruction_outlines()                                                                                                                                            |
| [Array](class_array.md#class-array)                                                                             | get_projected_obstructions()                                                                                                                                        |
| [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] | get_traversable_outlines()                                                                                                                                            |
| [bool](class_bool.md#class-bool)                                                                                | has_data()                                                                                                                                                                            |
|                                                                                                                 | merge(other_geometry: NavigationMeshSourceGeometryData2D)                                                                                   |
|                                                                                                                 | set_obstruction_outlines(obstruction_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)])       |
|                                                                                                                 | set_projected_obstructions(projected_obstructions: [Array](class_array.md#class-array))                                                                             |
|                                                                                                                 | set_traversable_outlines(traversable_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)])       |

---

## Method Descriptions

 **add_obstruction_outline**(shape_outline: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))

Adds the outline points of a shape as obstructed area.

---

 **add_projected_obstruction**(vertices: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array), carve: [bool](class_bool.md#class-bool))

Adds a projected obstruction shape to the source geometry. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.

---

 **add_traversable_outline**(shape_outline: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))

Adds the outline points of a shape as traversable area.

---

 **append_obstruction_outlines**(obstruction_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)])

Appends another array of `obstruction_outlines` at the end of the existing obstruction outlines array.

---

 **append_traversable_outlines**(traversable_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)])

Appends another array of `traversable_outlines` at the end of the existing traversable outlines array.

---

 **clear**()

Clears the internal data.

---

 **clear_projected_obstructions**()

Clears all projected obstructions.

---

[Rect2](class_rect2.md#class-rect2) **get_bounds**()

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.

---

[Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] **get_obstruction_outlines**()

Returns all the obstructed area outlines arrays.

---

[Array](class_array.md#class-array) **get_projected_obstructions**()

Returns the projected obstructions as an [Array](class_array.md#class-array) of dictionaries. Each [Dictionary](class_dictionary.md#class-dictionary) contains the following entries:

- `vertices` - A [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) that defines the outline points of the projected shape.
- `carve` - A [bool](class_bool.md#class-bool) that defines how the projected shape affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

---

[Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] **get_traversable_outlines**()

Returns all the traversable area outlines arrays.

---

[bool](class_bool.md#class-bool) **has_data**()

Returns `true` when parsed source geometry data exists.

---

 **merge**(other_geometry: NavigationMeshSourceGeometryData2D)

Adds the geometry data of another **NavigationMeshSourceGeometryData2D** to the navigation mesh baking data.

---

 **set_obstruction_outlines**(obstruction_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)])

Sets all the obstructed area outlines arrays.

---

 **set_projected_obstructions**(projected_obstructions: [Array](class_array.md#class-array))

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:

GDScript

```gdscript
"vertices" : PackedFloat32Array
"carve" : bool
```

---

 **set_traversable_outlines**(traversable_outlines: [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)])

Sets all the traversable area outlines arrays.
