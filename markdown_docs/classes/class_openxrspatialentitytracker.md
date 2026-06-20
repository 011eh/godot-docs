# OpenXRSpatialEntityTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRAnchorTracker](class_openxranchortracker.md#class-openxranchortracker), [OpenXRMarkerTracker](class_openxrmarkertracker.md#class-openxrmarkertracker), [OpenXRPlaneTracker](class_openxrplanetracker.md#class-openxrplanetracker)

Base class for Positional trackers managed by OpenXR's spatial entity extensions.

## Description

These are trackers created and managed by OpenXR's spatial entity extensions that give access to specific data related to OpenXR's spatial entities. They will always be of type `TRACKER_ANCHOR`.

## Properties

| [RID](class_rid.md#class-rid)                                               | entity                                 | `RID()`                                                                       |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| EntityTrackingState | spatial_tracking_state | `2`                                                                           |
| [TrackerType](class_xrserver.md#enum-xrserver-trackertype)                  | type                                                                                        | `8` (overrides [XRTracker](class_xrtracker.md#class-xrtracker-property-type)) |

## Methods

|                                                                               | add_next(next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase))       |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) | get_next()                                                                                          |
| [RID](class_rid.md#class-rid)                                                 | get_spatial_context()                                                                    |
|                                                                               | remove_next(next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase)) |
|                                                                               | set_spatial_context(spatial_context: [RID](class_rid.md#class-rid))                      |

---

## Signals

**next_changed**()

Emitted when the next-chain changes, from either add_next() or remove_next().

---

**spatial_tracking_state_changed**(spatial_tracking_state: [int](class_int.md#class-int))

There is currently no description for this signal. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

---

## Enumerations

enum **EntityTrackingState**:

EntityTrackingState **ENTITY_TRACKING_STATE_STOPPED** = `1`

This anchor has stopped tracking.

EntityTrackingState **ENTITY_TRACKING_STATE_PAUSED** = `2`

Tracking is currently paused.

EntityTrackingState **ENTITY_TRACKING_STATE_TRACKING** = `3`

This anchor is currently being tracked.

---

## Property Descriptions

[RID](class_rid.md#class-rid) **entity** = `RID()`

-  **set_entity**(value: [RID](class_rid.md#class-rid))
- [RID](class_rid.md#class-rid) **get_entity**()

The spatial entity associated with this tracker.

---

EntityTrackingState **spatial_tracking_state** = `2`

-  **set_spatial_tracking_state**(value: EntityTrackingState)
- EntityTrackingState **get_spatial_tracking_state**()

The spatial tracking state for this tracker.

---

## Method Descriptions

 **add_next**(next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase))

Adds a new [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) to the next-chain.

get_next() will return this `next` until either add_next() is called again or it's removed in remove_next().

---

[OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) **get_next**()

Gets the head [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase) in the next-chain.

See also add_next() and remove_next().

---

[RID](class_rid.md#class-rid) **get_spatial_context**()

Gets the spatial context used to create this **OpenXRSpatialEntityTracker**.

---

 **remove_next**(next: [OpenXRStructureBase](class_openxrstructurebase.md#class-openxrstructurebase))

Removes a `next` object previously added in add_next() from the next-chain.

---

 **set_spatial_context**(spatial_context: [RID](class_rid.md#class-rid))

Sets the spatial context used to create this tracker.
