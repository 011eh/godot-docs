# OpenXRAnchorTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) **<** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Positional tracker for our spatial entity anchor extension.

## Description

Positional tracker for our OpenXR spatial entity anchor extension, it tracks a user defined location in real space and maps it to our virtual space.

## Properties

| [String](class_string.md#class-string)   | uuid   | `""`   |
|------------------------------------------|----------------------------------------------------|--------|

## Methods

| [bool](class_bool.md#class-bool)   | has_uuid()    |
|------------------------------------|-------------------------------------------------------------|

---

## Signals

**uuid_changed**()

Emitted when the UUID for this anchor was changed.

---

## Property Descriptions

[String](class_string.md#class-string) **uuid** = `""`

-  **set_uuid**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_uuid**()

The UUID provided for persistent anchors.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **has_uuid**()

Returns `true` if a non-zero UUID is set.
