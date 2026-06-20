# OpenXRMarkerTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Spatial entity tracker for our spatial entity marker tracking extension.

## Description

Spatial entity tracker for our OpenXR spatial entity marker tracking extension. These trackers identify entities in our real space detected by a visual marker such as a QRCode or Aruco code, and map their location to our virtual space.

## Properties

| [Vector2](class_vector2.md#class-vector2)                                                                | bounds_size   | `Vector2(0, 0)`   |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-------------------|
| [int](class_int.md#class-int)                                                                            | marker_id       | `0`               |
| [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) | marker_type   | `0`               |

## Methods

| [Variant](class_variant.md#class-variant)   | get_marker_data()                                                       |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|                                             | set_marker_data(marker_data: [Variant](class_variant.md#class-variant)) |

---

## Property Descriptions

[Vector2](class_vector2.md#class-vector2) **bounds_size** = `Vector2(0, 0)`

-  **set_bounds_size**(value: [Vector2](class_vector2.md#class-vector2))
- [Vector2](class_vector2.md#class-vector2) **get_bounds_size**()

The bounds size for this marker.

---

[int](class_int.md#class-int) **marker_id** = `0`

-  **set_marker_id**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_marker_id**()

The marker ID for this marker, this is only returned for Aruco and April Tag markers. Call get_marker_data() for QRCode markers.

---

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **marker_type** = `0`

-  **set_marker_type**(value: [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype))
- [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum-openxrspatialcomponentmarkerlist-markertype) **get_marker_type**()

The type of marker.

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **get_marker_data**()

Returns the marker data for this marker. This can return a [String](class_string.md#class-string) or [PackedByteArray](class_packedbytearray.md#class-packedbytearray). Only applicable to QR Code based markers.

---

 **set_marker_data**(marker_data: [Variant](class_variant.md#class-variant))

Sets the marker data for this marker.

**Note:** This should only be set by marker discovery logic.
