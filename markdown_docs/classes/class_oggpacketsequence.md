# OggPacketSequence

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A sequence of Ogg packets.

## Description

A sequence of Ogg packets.

## Properties

| [PackedInt64Array](class_packedint64array.md#class-packedint64array)     | granule_positions   | `PackedInt64Array()`   |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------|
| [Array](class_array.md#class-array)[[Array](class_array.md#class-array)] | packet_data               | `[]`                   |
| [float](class_float.md#class-float)                                      | sampling_rate           | `0.0`                  |

## Methods

| [float](class_float.md#class-float)   | get_length()    |
|---------------------------------------|---------------------------------------------------------------|

---

## Property Descriptions

[PackedInt64Array](class_packedint64array.md#class-packedint64array) **granule_positions** = `PackedInt64Array()`

-  **set_packet_granule_positions**(value: [PackedInt64Array](class_packedint64array.md#class-packedint64array))
- [PackedInt64Array](class_packedint64array.md#class-packedint64array) **get_packet_granule_positions**()

Contains the granule positions for each page in this packet sequence.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt64Array](class_packedint64array.md#class-packedint64array) for more details.

---

[Array](class_array.md#class-array)[[Array](class_array.md#class-array)] **packet_data** = `[]`

-  **set_packet_data**(value: [Array](class_array.md#class-array)[[Array](class_array.md#class-array)])
- [Array](class_array.md#class-array)[[Array](class_array.md#class-array)] **get_packet_data**()

Contains the raw packets that make up this OggPacketSequence.

---

[float](class_float.md#class-float) **sampling_rate** = `0.0`

-  **set_sampling_rate**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_sampling_rate**()

Holds sample rate information about this sequence. Must be set by another class that actually understands the codec.

---

## Method Descriptions

[float](class_float.md#class-float) **get_length**()

The length of this stream, in seconds.
