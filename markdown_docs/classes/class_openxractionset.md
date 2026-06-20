# OpenXRActionSet

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Collection of [OpenXRAction](class_openxraction.md#class-openxraction) resources that make up an action set.

## Description

Action sets in OpenXR define a collection of actions that can be activated in unison. This allows games to easily change between different states that require different inputs or need to reinterpret inputs. For instance we could have an action set that is active when a menu is open, an action set that is active when the player is freely walking around and an action set that is active when the player is controlling a vehicle.

Action sets can contain the same action with the same name, if such action sets are active at the same time the action set with the highest priority defines which binding is active.

## Properties

| [Array](class_array.md#class-array)    | actions               | `[]`   |
|----------------------------------------|------------------------------------------------------------------|--------|
| [String](class_string.md#class-string) | localized_name | `""`   |
| [int](class_int.md#class-int)          | priority             | `0`    |

## Methods

|                               | add_action(action: [OpenXRAction](class_openxraction.md#class-openxraction))       |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int) | get_action_count()                                                           |
|                               | remove_action(action: [OpenXRAction](class_openxraction.md#class-openxraction)) |

---

## Property Descriptions

[Array](class_array.md#class-array) **actions** = `[]`

-  **set_actions**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_actions**()

Collection of actions for this action set.

---

[String](class_string.md#class-string) **localized_name** = `""`

-  **set_localized_name**(value: [String](class_string.md#class-string))
- [String](class_string.md#class-string) **get_localized_name**()

The localized name of this action set.

---

[int](class_int.md#class-int) **priority** = `0`

-  **set_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_priority**()

The priority for this action set.

---

## Method Descriptions

 **add_action**(action: [OpenXRAction](class_openxraction.md#class-openxraction))

Add an action to this action set.

---

[int](class_int.md#class-int) **get_action_count**()

Retrieve the number of actions in our action set.

---

 **remove_action**(action: [OpenXRAction](class_openxraction.md#class-openxraction))

Remove an action from this action set.
