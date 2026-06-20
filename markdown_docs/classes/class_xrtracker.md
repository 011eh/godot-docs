# XRTracker

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [XRFaceTracker](class_xrfacetracker.md#class-xrfacetracker), [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker)

A tracked object.

## Description

This object is the base of all XR trackers.

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

## Properties

| [String](class_string.md#class-string)                     | description   | `""`         |
|------------------------------------------------------------|--------------------------------------------------------|--------------|
| [StringName](class_stringname.md#class-stringname)         | name                 | `&"Unknown"` |
| [TrackerType](class_xrserver.md#enum-xrserver-trackertype) | type                 | `128`        |

---

## Property Descriptions

[String](class_string.md#class-string) **description** = `""`

-  **set_tracker_desc**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_tracker_desc**()

The description of this tracker.

---

[StringName](class_stringname.md#class-stringname) **name** = `&"Unknown"`

-  **set_tracker_name**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_tracker_name**()

The unique name of this tracker. The trackers that are available differ between various XR runtimes and can often be configured by the user. Godot maintains a number of reserved names that it expects the [XRInterface](class_xrinterface.md#class-xrinterface) to implement if applicable:

- `"head"` identifies the [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) of the player's head
- `"left_hand"` identifies the [XRControllerTracker](class_xrcontrollertracker.md#class-xrcontrollertracker) in the player's left hand
- `"right_hand"` identifies the [XRControllerTracker](class_xrcontrollertracker.md#class-xrcontrollertracker) in the player's right hand
- `"/user/hand_tracker/left"` identifies the [XRHandTracker](class_xrhandtracker.md#class-xrhandtracker) for the player's left hand
- `"/user/hand_tracker/right"` identifies the [XRHandTracker](class_xrhandtracker.md#class-xrhandtracker) for the player's right hand
- `"/user/body_tracker"` identifies the [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker) for the player's body
- `"/user/face_tracker"` identifies the [XRFaceTracker](class_xrfacetracker.md#class-xrfacetracker) for the player's face

---

[TrackerType](class_xrserver.md#enum-xrserver-trackertype) **type** = `128`

-  **set_tracker_type**(value: [TrackerType](class_xrserver.md#enum-xrserver-trackertype))
- [TrackerType](class_xrserver.md#enum-xrserver-trackertype) **get_tracker_type**()

The type of tracker.
