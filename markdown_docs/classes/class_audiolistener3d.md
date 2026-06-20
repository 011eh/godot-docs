# AudioListener3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Overrides the location sounds are heard from.

## Description

Once added to the scene tree and enabled using make_current(), this node will override the location sounds are heard from. This can be used to listen from a location different from the [Camera3D](class_camera3d.md#class-camera3d).

## Properties

| DopplerTracking   | doppler_tracking   | `0`   |
|------------------------------------------------------------|------------------------------------------------------------------------|-------|

## Methods

|                                                       | clear_current()                   |
|-------------------------------------------------------|----------------------------------------------------------------------------------|
| [Transform3D](class_transform3d.md#class-transform3d) | get_listener_transform() |
| [bool](class_bool.md#class-bool)                      | is_current()                         |
|                                                       | make_current()                     |

---

## Enumerations

enum **DopplerTracking**:

DopplerTracking **DOPPLER_TRACKING_DISABLED** = `0`

Disables [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) simulation (default).

DopplerTracking **DOPPLER_TRACKING_IDLE_STEP** = `1`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-pitch-scale)).

DopplerTracking **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_physics_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-pitch-scale)).

---

## Property Descriptions

DopplerTracking **doppler_tracking** = `0`

-  **set_doppler_tracking**(value: DopplerTracking)
- DopplerTracking **get_doppler_tracking**()

If not DOPPLER_TRACKING_DISABLED, this listener will simulate the [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) for objects changed in particular `_process` methods.

**Note:** The Doppler effect will only be heard on [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class-audiostreamplayer3d)s if [AudioStreamPlayer3D.doppler_tracking](class_audiostreamplayer3d.md#class-audiostreamplayer3d-property-doppler-tracking) is not set to [AudioStreamPlayer3D.DOPPLER_TRACKING_DISABLED](class_audiostreamplayer3d.md#class-audiostreamplayer3d-constant-doppler-tracking-disabled).

---

## Method Descriptions

 **clear_current**()

Disables the listener to use the current camera's listener instead.

---

[Transform3D](class_transform3d.md#class-transform3d) **get_listener_transform**()

Returns the listener's global orthonormalized [Transform3D](class_transform3d.md#class-transform3d).

---

[bool](class_bool.md#class-bool) **is_current**()

Returns `true` if the listener was made current using make_current(), `false` otherwise.

**Note:** There may be more than one AudioListener3D marked as "current" in the scene tree, but only the one that was made current last will be used.

---

 **make_current**()

Enables the listener. This will override the current camera's listener.
