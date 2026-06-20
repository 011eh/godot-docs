# OpenXRSpatialComponentMarkerList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class-openxrspatialcomponentdata) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Object for storing the queries marker result data.

## Description

Object for storing the queries marker result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class-openxrspatialentityextension-method-query-snapshot).

## Methods

| [Variant](class_variant.md#class-variant)                       | get_marker_data(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))    |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                                   | get_marker_id(index: [int](class_int.md#class-int))                                                 |
| MarkerType | get_marker_type(index: [int](class_int.md#class-int))                                             |

---

## Enumerations

enum **MarkerType**:

MarkerType **MARKER_TYPE_UNKNOWN** = `0`

Unknown or unset marker type.

MarkerType **MARKER_TYPE_QRCODE** = `1`

Marker based on a QR code.

MarkerType **MARKER_TYPE_MICRO_QRCODE** = `2`

Marker based on a micro QR code.

MarkerType **MARKER_TYPE_ARUCO** = `3`

Marker based on an Aruco code.

MarkerType **MARKER_TYPE_APRIL_TAG** = `4`

Marker based on an April Tag.

MarkerType **MARKER_TYPE_MAX** = `5`

Maximum value for this enum.

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **get_marker_data**(snapshot: [RID](class_rid.md#class-rid), index: [int](class_int.md#class-int))

Returns either a [String](class_string.md#class-string) or a [PackedByteArray](class_packedbytearray.md#class-packedbytearray) buffer with data for the marker at this `index`. Only applicable for QR code markers.

---

[int](class_int.md#class-int) **get_marker_id**(index: [int](class_int.md#class-int))

Returns the marker ID for the marker at this `index`. Only applicable for Aruco or April Tag markers.

---

MarkerType **get_marker_type**(index: [int](class_int.md#class-int))

Returns the marker type for the marker at this `index`.
