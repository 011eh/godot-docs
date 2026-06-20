# Polygon2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A 2D polygon.

## Description

A Polygon2D is defined by a set of points. Each point is connected to the next, with the final point being connected to the first, resulting in a closed polygon. Polygon2Ds can be filled with color (solid or gradient) or filled with a given texture.

## Properties

| [bool](class_bool.md#class-bool)                                           | antialiased                     | `false`                |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------|------------------------|
| [Color](class_color.md#class-color)                                        | color                                 | `Color(1, 1, 1, 1)`    |
| [int](class_int.md#class-int)                                              | internal_vertex_count | `0`                    |
| [float](class_float.md#class-float)                                        | invert_border                 | `100.0`                |
| [bool](class_bool.md#class-bool)                                           | invert_enabled               | `false`                |
| [Vector2](class_vector2.md#class-vector2)                                  | offset                               | `Vector2(0, 0)`        |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | polygon                             | `PackedVector2Array()` |
| [Array](class_array.md#class-array)                                        | polygons                           | `[]`                   |
| [NodePath](class_nodepath.md#class-nodepath)                               | skeleton                           | `NodePath("")`         |
| [Texture2D](class_texture2d.md#class-texture2d)                            | texture                             |                        |
| [Vector2](class_vector2.md#class-vector2)                                  | texture_offset               | `Vector2(0, 0)`        |
| [float](class_float.md#class-float)                                        | texture_rotation           | `0.0`                  |
| [Vector2](class_vector2.md#class-vector2)                                  | texture_scale                 | `Vector2(1, 1)`        |
| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) | uv                                       | `PackedVector2Array()` |
| [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray)       | vertex_colors                 | `PackedColorArray()`   |

## Methods

|                                                                            | add_bone(path: [NodePath](class_nodepath.md#class-nodepath), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))   |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                            | clear_bones()                                                                                                                                    |
|                                                                            | erase_bone(index: [int](class_int.md#class-int))                                                                                                  |
| [int](class_int.md#class-int)                                              | get_bone_count()                                                                                                                              |
| [NodePath](class_nodepath.md#class-nodepath)                               | get_bone_path(index: [int](class_int.md#class-int))                                                                                            |
| [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) | get_bone_weights(index: [int](class_int.md#class-int))                                                                                      |
|                                                                            | set_bone_path(index: [int](class_int.md#class-int), path: [NodePath](class_nodepath.md#class-nodepath))                                        |
|                                                                            | set_bone_weights(index: [int](class_int.md#class-int), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array)) |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **antialiased** = `false`

-  **set_antialiased**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_antialiased**()

If `true`, polygon edges will be anti-aliased.

---

[Color](class_color.md#class-color) **color** = `Color(1, 1, 1, 1)`

-  **set_color**(value: [Color](class_color.md#class-color))
- [Color](class_color.md#class-color) **get_color**()

The polygon's fill color. If texture is set, it will be multiplied by this color. It will also be the default color for vertices not set in vertex_colors.

---

[int](class_int.md#class-int) **internal_vertex_count** = `0`

-  **set_internal_vertex_count**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_internal_vertex_count**()

Number of internal vertices, used for UV mapping.

---

[float](class_float.md#class-float) **invert_border** = `100.0`

-  **set_invert_border**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_invert_border**()

Added padding applied to the bounding box when invert_enabled is set to `true`. Setting this value too small may result in a "Bad Polygon" error.

---

[bool](class_bool.md#class-bool) **invert_enabled** = `false`

-  **set_invert_enabled**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_invert_enabled**()

If `true`, the polygon will be inverted, containing the area outside the defined points and extending to the invert_border.

---

[Vector2](class_vector2.md#class-vector2) **offset** = `Vector2(0, 0)`

-  **set_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_offset**()

The offset applied to each vertex.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **polygon** = `PackedVector2Array()`

-  **set_polygon**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_polygon**()

The polygon's list of vertices. The final point will be connected to the first.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---

[Array](class_array.md#class-array) **polygons** = `[]`

-  **set_polygons**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_polygons**()

The list of polygons, in case more than one is being represented. Every individual polygon is stored as a [PackedInt32Array](class_packedint32array.md#class-packedint32array) where each [int](class_int.md#class-int) is an index to a point in polygon. If empty, this property will be ignored, and the resulting single polygon will be composed of all points in polygon, using the order they are stored in.

---

[NodePath](class_nodepath.md#class-nodepath) **skeleton** = `NodePath("")`

-  **set_skeleton**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_skeleton**()

Path to a [Skeleton2D](class_skeleton2d.md#class-skeleton2d) node used for skeleton-based deformations of this polygon. If empty or invalid, skeletal deformations will not be used.

---

[Texture2D](class_texture2d.md#class-texture2d) **texture**

-  **set_texture**(value: [Texture2D](class_texture2d.md#class-texture2d))
- [Texture2D](class_texture2d.md#class-texture2d) **get_texture**()

The polygon's fill texture. Use uv to set texture coordinates.

---

[Vector2](class_vector2.md#class-vector2) **texture_offset** = `Vector2(0, 0)`

-  **set_texture_offset**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_texture_offset**()

Amount to offset the polygon's texture. If set to `Vector2(0, 0)`, the texture's origin (its top-left corner) will be placed at the polygon's position.

---

[float](class_float.md#class-float) **texture_rotation** = `0.0`

-  **set_texture_rotation**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_texture_rotation**()

The texture's rotation in radians.

---

[Vector2](class_vector2.md#class-vector2) **texture_scale** = `Vector2(1, 1)`

-  **set_texture_scale**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_texture_scale**()

Amount to multiply the uv coordinates when using texture. Larger values make the texture smaller, and vice versa.

---

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **uv** = `PackedVector2Array()`

-  **set_uv**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_uv**()

Texture coordinates for each vertex of the polygon. There should be one UV value per polygon vertex. If there are fewer, undefined vertices will use `Vector2(0, 0)`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---

[PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **vertex_colors** = `PackedColorArray()`

-  **set_vertex_colors**(value: [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray))
- [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) **get_vertex_colors**()

Color for each vertex. Colors are interpolated between vertices, resulting in smooth gradients. There should be one per polygon vertex. If there are fewer, undefined vertices will use color.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class-packedcolorarray) for more details.

---

## Method Descriptions

 **add_bone**(path: [NodePath](class_nodepath.md#class-nodepath), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Adds a bone with the specified `path` and `weights`.

---

 **clear_bones**()

Removes all bones from this **Polygon2D**.

---

 **erase_bone**(index: [int](class_int.md#class-int))

Removes the specified bone from this **Polygon2D**.

---

[int](class_int.md#class-int) **get_bone_count**()

Returns the number of bones in this **Polygon2D**.

---

[NodePath](class_nodepath.md#class-nodepath) **get_bone_path**(index: [int](class_int.md#class-int))

Returns the path to the node associated with the specified bone.

---

[PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array) **get_bone_weights**(index: [int](class_int.md#class-int))

Returns the weight values of the specified bone.

---

 **set_bone_path**(index: [int](class_int.md#class-int), path: [NodePath](class_nodepath.md#class-nodepath))

Sets the path to the node associated with the specified bone.

---

 **set_bone_weights**(index: [int](class_int.md#class-int), weights: [PackedFloat32Array](class_packedfloat32array.md#class-packedfloat32array))

Sets the weight values for the specified bone.
