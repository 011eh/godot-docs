# OpenXRActionMap

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Collection of [OpenXRActionSet](class_openxractionset.md#class-openxractionset) and [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) resources for the OpenXR module.

## Description

OpenXR uses an action system similar to Godots Input map system to bind inputs and outputs on various types of XR controllers to named actions. OpenXR specifies more detail on these inputs and outputs than Godot supports.

Another important distinction is that OpenXR offers no control over these bindings. The bindings we register are suggestions, it is up to the XR runtime to offer users the ability to change these bindings. This allows the XR runtime to fill in the gaps if new hardware becomes available.

The action map therefore needs to be loaded at startup and can't be changed afterwards. This resource is a container for the entire action map.

## Properties

| [Array](class_array.md#class-array)   | action_sets                   | `[]`   |
|---------------------------------------|------------------------------------------------------------------------------|--------|
| [Array](class_array.md#class-array)   | interaction_profiles | `[]`   |

## Methods

|                                                                                              | add_action_set(action_set: [OpenXRActionSet](class_openxractionset.md#class-openxractionset))                                                             |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                              | add_interaction_profile(interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile))       |
|                                                                                              | create_default_action_sets()                                                                                                                  |
| [OpenXRActionSet](class_openxractionset.md#class-openxractionset)                            | find_action_set(name: [String](class_string.md#class-string))                                                                                            |
| [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) | find_interaction_profile(name: [String](class_string.md#class-string))                                                                          |
| [OpenXRActionSet](class_openxractionset.md#class-openxractionset)                            | get_action_set(idx: [int](class_int.md#class-int))                                                                                                        |
| [int](class_int.md#class-int)                                                                | get_action_set_count()                                                                                                                              |
| [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) | get_interaction_profile(idx: [int](class_int.md#class-int))                                                                                      |
| [int](class_int.md#class-int)                                                                | get_interaction_profile_count()                                                                                                            |
|                                                                                              | remove_action_set(action_set: [OpenXRActionSet](class_openxractionset.md#class-openxractionset))                                                       |
|                                                                                              | remove_interaction_profile(interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)) |

---

## Property Descriptions

[Array](class_array.md#class-array) **action_sets** = `[]`

-  **set_action_sets**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_action_sets**()

Collection of [OpenXRActionSet](class_openxractionset.md#class-openxractionset)s that are part of this action map.

---

[Array](class_array.md#class-array) **interaction_profiles** = `[]`

-  **set_interaction_profiles**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_interaction_profiles**()

Collection of [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile)s that are part of this action map.

---

## Method Descriptions

 **add_action_set**(action_set: [OpenXRActionSet](class_openxractionset.md#class-openxractionset))

Add an action set.

---

 **add_interaction_profile**(interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile))

Add an interaction profile.

---

 **create_default_action_sets**()

Setup this action set with our default actions.

---

[OpenXRActionSet](class_openxractionset.md#class-openxractionset) **find_action_set**(name: [String](class_string.md#class-string))

Retrieve an action set by name.

---

[OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) **find_interaction_profile**(name: [String](class_string.md#class-string))

Find an interaction profile by its name (path).

---

[OpenXRActionSet](class_openxractionset.md#class-openxractionset) **get_action_set**(idx: [int](class_int.md#class-int))

Retrieve the action set at this index.

---

[int](class_int.md#class-int) **get_action_set_count**()

Retrieve the number of actions sets in our action map.

---

[OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile) **get_interaction_profile**(idx: [int](class_int.md#class-int))

Get the interaction profile at this index.

---

[int](class_int.md#class-int) **get_interaction_profile_count**()

Retrieve the number of interaction profiles in our action map.

---

 **remove_action_set**(action_set: [OpenXRActionSet](class_openxractionset.md#class-openxractionset))

Remove an action set.

---

 **remove_interaction_profile**(interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class-openxrinteractionprofile))

Remove an interaction profile.
