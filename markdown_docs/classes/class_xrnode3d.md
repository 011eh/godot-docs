# XRNode3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [XRAnchor3D](class_xranchor3d.md#class-xranchor3d), [XRController3D](class_xrcontroller3d.md#class-xrcontroller3d)

A 3D node that has its position automatically updated by the [XRServer](class_xrserver.md#class-xrserver).

## Description

This node can be bound to a specific pose of an [XRPositionalTracker](class_xrpositionaltracker.md#class-xrpositionaltracker) and will automatically have its [Node3D.transform](class_node3d.md#class-node3d-property-transform) updated by the [XRServer](class_xrserver.md#class-xrserver). Nodes of this type must be added as children of the [XROrigin3D](class_xrorigin3d.md#class-xrorigin3d) node.

## Tutorials

- [XR documentation index](../tutorials/xr/index.md)

## Properties

| [PhysicsInterpolationMode](class_node.md#enum-node-physicsinterpolationmode)   | physics_interpolation_mode                                      | `2` (overrides [Node](class_node.md#class-node-property-physics-interpolation-mode))   |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [StringName](class_stringname.md#class-stringname)                             | pose                           | `&"default"`                                                                           |
| [bool](class_bool.md#class-bool)                                               | show_when_tracked | `false`                                                                                |
| [StringName](class_stringname.md#class-stringname)                             | tracker                     | `&""`                                                                                  |

## Methods

| [bool](class_bool.md#class-bool)       | get_has_tracking_data()                                                                                                                                                                                                                                                     |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)       | get_is_active()                                                                                                                                                                                                                                                                     |
| [XRPose](class_xrpose.md#class-xrpose) | get_pose()                                                                                                                                                                                                                                                                               |
|                                        | trigger_haptic_pulse(action_name: [String](class_string.md#class-string), frequency: [float](class_float.md#class-float), amplitude: [float](class_float.md#class-float), duration_sec: [float](class_float.md#class-float), delay_sec: [float](class_float.md#class-float)) |

---

## Signals

**tracking_changed**(tracking: [bool](class_bool.md#class-bool))

Emitted when the tracker starts or stops receiving updated tracking data for the pose being tracked. The `tracking` argument indicates whether the tracker is getting updated tracking data.

---

## Property Descriptions

[StringName](class_stringname.md#class-stringname) **pose** = `&"default"`

-  **set_pose_name**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_pose_name**()

The name of the pose we're bound to. Which poses a tracker supports is not known during design time.

Godot defines number of standard pose names such as `aim` and `grip` but other may be configured within a given [XRInterface](class_xrinterface.md#class-xrinterface).

---

[bool](class_bool.md#class-bool) **show_when_tracked** = `false`

-  **set_show_when_tracked**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_show_when_tracked**()

Enables showing the node when tracking starts, and hiding the node when tracking is lost.

---

[StringName](class_stringname.md#class-stringname) **tracker** = `&""`

-  **set_tracker**(value: [StringName](class_stringname.md#class-stringname))
- [StringName](class_stringname.md#class-stringname) **get_tracker**()

The name of the tracker we're bound to. Which trackers are available is not known during design time.

Godot defines a number of standard trackers such as `left_hand` and `right_hand` but others may be configured within a given [XRInterface](class_xrinterface.md#class-xrinterface).

---

## Method Descriptions

[bool](class_bool.md#class-bool) **get_has_tracking_data**()

Returns `true` if the tracker has current tracking data for the pose being tracked.

---

[bool](class_bool.md#class-bool) **get_is_active**()

Returns `true` if the tracker has been registered and the pose is being tracked.

---

[XRPose](class_xrpose.md#class-xrpose) **get_pose**()

Returns the [XRPose](class_xrpose.md#class-xrpose) containing the current state of the pose being tracked. This gives access to additional properties of this pose.

---

 **trigger_haptic_pulse**(action_name: [String](class_string.md#class-string), frequency: [float](class_float.md#class-float), amplitude: [float](class_float.md#class-float), duration_sec: [float](class_float.md#class-float), delay_sec: [float](class_float.md#class-float))

Triggers a haptic pulse on a device associated with this interface.

`action_name` is the name of the action for this pulse.

`frequency` is the frequency of the pulse, set to `0.0` to have the system use a default frequency.

`amplitude` is the amplitude of the pulse between `0.0` and `1.0`.

`duration_sec` is the duration of the pulse in seconds.

`delay_sec` is a delay in seconds before the pulse is given.
