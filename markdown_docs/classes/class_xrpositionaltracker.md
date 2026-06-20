# XRPositionalTracker

**Inherits:** [XRTracker](class_xrtracker.md#class-xrtracker) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class-openxrspatialentitytracker), [XRBodyTracker](class_xrbodytracker.md#class-xrbodytracker), [XRControllerTracker](class_xrcontrollertracker.md#class-xrcontrollertracker), [XRHandTracker](class_xrhandtracker.md#class-xrhandtracker)

A tracked object.

## Description

An instance of this object represents a device that is tracked, such as a controller or anchor point. HMDs aren't represented here as they are handled internally.

As controllers are turned on and the [XRInterface](class_xrinterface.md#class-xrinterface) detects them, instances of this object are automatically added to this list of active tracking objects accessible through the [XRServer](class_xrserver.md#class-xrserver).

The [XRNode3D](class_xrnode3d.md#class-xrnode3d) and [XRAnchor3D](class_xranchor3d.md#class-xranchor3d) both consume objects of this type and should be used in your project. The positional trackers are just under-the-hood objects that make this all work. These are mostly exposed so that GDExtension-based interfaces can interact with them.

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

## Properties

| TrackerHand   | hand       | `0`   |
|--------------------------------------------------------|--------------------------------------------------------|-------|
| [String](class_string.md#class-string)                 | profile | `""`  |

## Methods

| [Variant](class_variant.md#class-variant)   | get_input(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                     |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [XRPose](class_xrpose.md#class-xrpose)      | get_pose(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                       |
| [bool](class_bool.md#class-bool)            | has_pose(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                                       |
|                                             | invalidate_pose(name: [StringName](class_stringname.md#class-stringname))                                                                                                                                                                                                                                                                         |
|                                             | set_input(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))                                                                                                                                                                                                                                   |
|                                             | set_pose(name: [StringName](class_stringname.md#class-stringname), transform: [Transform3D](class_transform3d.md#class-transform3d), linear_velocity: [Vector3](class_vector3.md#class-vector3), angular_velocity: [Vector3](class_vector3.md#class-vector3), tracking_confidence: [TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence)) |

---

## Signals

**button_pressed**(action_name: [String](class_string.md#class-string))

Emitted when a button on this tracker is pressed. Note that many XR runtimes allow other inputs to be mapped to buttons.

---

**button_released**(action_name: [String](class_string.md#class-string))

Emitted when a button on this tracker is released.

---

**input_float_changed**(action_name: [String](class_string.md#class-string), value: [float](class_float.md#class-float))

Emitted when a trigger or similar input on this tracker changes value.

---

**input_vector2_changed**(action_name: [String](class_string.md#class-string), vector: [Vector2](class_vector2.md#class-vector2))

Emitted when a thumbstick or thumbpad on this tracker moves.

---

**pose_changed**(pose: [XRPose](class_xrpose.md#class-xrpose))

Emitted when the state of a pose tracked by this tracker changes.

---

**pose_lost_tracking**(pose: [XRPose](class_xrpose.md#class-xrpose))

Emitted when a pose tracked by this tracker stops getting updated tracking data.

---

**profile_changed**(role: [String](class_string.md#class-string))

Emitted when the profile of our tracker changes.

---

## Enumerations

enum **TrackerHand**:

TrackerHand **TRACKER_HAND_UNKNOWN** = `0`

The hand this tracker is held in is unknown or not applicable.

TrackerHand **TRACKER_HAND_LEFT** = `1`

This tracker is the left hand controller.

TrackerHand **TRACKER_HAND_RIGHT** = `2`

This tracker is the right hand controller.

TrackerHand **TRACKER_HAND_MAX** = `3`

Represents the size of the TrackerHand enum.

---

## Property Descriptions

TrackerHand **hand** = `0`

-  **set_tracker_hand**(value: TrackerHand)
- TrackerHand **get_tracker_hand**()

Defines which hand this tracker relates to.

---

[String](class_string.md#class-string) **profile** = `""`

-  **set_tracker_profile**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_tracker_profile**()

The profile associated with this tracker, interface dependent but will indicate the type of controller being tracked.

---

## Method Descriptions

[Variant](class_variant.md#class-variant) **get_input**(name: [StringName](class_stringname.md#class-stringname))

**Deprecated:** Use through [XRControllerTracker](class_xrcontrollertracker.md#class-xrcontrollertracker).

Returns an input for this tracker. It can return a boolean, float or [Vector2](class_vector2.md#class-vector2) value depending on whether the input is a button, trigger or thumbstick/thumbpad.

---

[XRPose](class_xrpose.md#class-xrpose) **get_pose**(name: [StringName](class_stringname.md#class-stringname))

Returns the current [XRPose](class_xrpose.md#class-xrpose) state object for the bound `name` pose.

---

[bool](class_bool.md#class-bool) **has_pose**(name: [StringName](class_stringname.md#class-stringname))

Returns `true` if the tracker is available and is currently tracking the bound `name` pose.

---

 **invalidate_pose**(name: [StringName](class_stringname.md#class-stringname))

Marks this pose as invalid, we don't clear the last reported state but it allows users to decide if trackers need to be hidden if we lose tracking or just remain at their last known position.

---

 **set_input**(name: [StringName](class_stringname.md#class-stringname), value: [Variant](class_variant.md#class-variant))

**Deprecated:** Use through [XRControllerTracker](class_xrcontrollertracker.md#class-xrcontrollertracker).

Changes the value for the given input. This method is called by an [XRInterface](class_xrinterface.md#class-xrinterface) implementation and should not be used directly.

---

 **set_pose**(name: [StringName](class_stringname.md#class-stringname), transform: [Transform3D](class_transform3d.md#class-transform3d), linear_velocity: [Vector3](class_vector3.md#class-vector3), angular_velocity: [Vector3](class_vector3.md#class-vector3), tracking_confidence: [TrackingConfidence](class_xrpose.md#enum-xrpose-trackingconfidence))

Sets the transform, linear velocity, angular velocity and tracking confidence for the given pose. This method is called by an [XRInterface](class_xrinterface.md#class-xrinterface) implementation and should not be used directly.
