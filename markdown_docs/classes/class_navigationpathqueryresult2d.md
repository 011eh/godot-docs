# NavigationPathQueryResult2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents the result of a 2D pathfinding query.

## Description

This class stores the result of a 2D navigation path query from the [NavigationServer2D](class_navigationserver2d.md#class-navigationserver2d).

## Tutorials

- [Using NavigationPathQueryObjects](../tutorials/navigation/navigation_using_navigationpathqueryobjects.md)

## Properties

| [PackedVector2Array](class_packedvector2array.md#class-packedvector2array)   | path                     | `PackedVector2Array()`   |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------------------------|
| [float](class_float.md#class-float)                                          | path_length       | `0.0`                    |
| [PackedInt64Array](class_packedint64array.md#class-packedint64array)         | path_owner_ids | `PackedInt64Array()`     |
| [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)]           | path_rids           | `[]`                     |
| [PackedInt32Array](class_packedint32array.md#class-packedint32array)         | path_types         | `PackedInt32Array()`     |

## Methods

|    | reset()   |
|----|--------------------------------------------------------------|

---

## Enumerations

enum **PathSegmentType**:

PathSegmentType **PATH_SEGMENT_TYPE_REGION** = `0`

This segment of the path goes through a region.

PathSegmentType **PATH_SEGMENT_TYPE_LINK** = `1`

This segment of the path goes through a link.

---

## Property Descriptions

[PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **path** = `PackedVector2Array()`

-  **set_path**(value: [PackedVector2Array](class_packedvector2array.md#class-packedvector2array))
- [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) **get_path**()

The resulting path array from the navigation query. All path array positions are in global coordinates. Without customized query parameters this is the same path as returned by [NavigationServer2D.map_get_path()](class_navigationserver2d.md#class-navigationserver2d-method-map-get-path).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) for more details.

---

[float](class_float.md#class-float) **path_length** = `0.0`

-  **set_path_length**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_path_length**()

Returns the length of the path.

---

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **path_owner_ids** = `PackedInt64Array()`

-  **set_path_owner_ids**(value: [PackedInt64Array](class_packedint64array.md#class-packedint64array))
- [PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_path_owner_ids**()

The `ObjectID`s of the [Object](class_object.md#class-object)s which manage the regions and links each point of the path goes through.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt64Array](class_packedint64array.md#class-packedint64array) for more details.

---

[Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **path_rids** = `[]`

-  **set_path_rids**(value: [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)])
- [Array](class_array.md#class-array)[[RID](class_rid.md#class-rid)] **get_path_rids**()

The [RID](class_rid.md#class-rid)s of the regions and links that each point of the path goes through.

---

[PackedInt32Array](class_packedint32array.md#class-packedint32array) **path_types** = `PackedInt32Array()`

-  **set_path_types**(value: [PackedInt32Array](class_packedint32array.md#class-packedint32array))
- [PackedInt32Array](class_packedint32array.md#class-packedint32array) **get_path_types**()

The type of navigation primitive (region or link) that each point of the path goes through.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class-packedint32array) for more details.

---

## Method Descriptions

 **reset**()

Reset the result object to its initial state. This is useful to reuse the object across multiple queries.
