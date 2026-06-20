# InputMap

**Inherits:** [Object](class_object.md#class-object)

A singleton that manages all [InputEventAction](class_inputeventaction.md#class-inputeventaction)s.

## Description

Manages all [InputEventAction](class_inputeventaction.md#class-inputeventaction) which can be created/modified from the project settings menu **Project > Project Settings > Input Map** or in code with add_action() and action_add_event(). See [Node._input()](class_node.md#class-node-private-method-input).

## Tutorials

- [Using InputEvent: InputMap](../tutorials/inputs/inputevent.html#inputmap)

## Methods

|                                                                                         | action_add_event(action: [StringName](class_stringname.md#class-stringname), event: [InputEvent](class_inputevent.md#class-inputevent))                                                      |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                         | action_erase_event(action: [StringName](class_stringname.md#class-stringname), event: [InputEvent](class_inputevent.md#class-inputevent))                                                  |
|                                                                                         | action_erase_events(action: [StringName](class_stringname.md#class-stringname))                                                                                                           |
| [float](class_float.md#class-float)                                                     | action_get_deadzone(action: [StringName](class_stringname.md#class-stringname))                                                                                                           |
| [Array](class_array.md#class-array)[[InputEvent](class_inputevent.md#class-inputevent)] | action_get_events(action: [StringName](class_stringname.md#class-stringname))                                                                                                               |
| [bool](class_bool.md#class-bool)                                                        | action_has_event(action: [StringName](class_stringname.md#class-stringname), event: [InputEvent](class_inputevent.md#class-inputevent))                                                      |
|                                                                                         | action_set_deadzone(action: [StringName](class_stringname.md#class-stringname), deadzone: [float](class_float.md#class-float))                                                            |
|                                                                                         | add_action(action: [StringName](class_stringname.md#class-stringname), deadzone: [float](class_float.md#class-float) = 0.2)                                                                        |
|                                                                                         | erase_action(action: [StringName](class_stringname.md#class-stringname))                                                                                                                         |
| [bool](class_bool.md#class-bool)                                                        | event_is_action(event: [InputEvent](class_inputevent.md#class-inputevent), action: [StringName](class_stringname.md#class-stringname), exact_match: [bool](class_bool.md#class-bool) = false) |
| [String](class_string.md#class-string)                                                  | get_action_description(action: [StringName](class_stringname.md#class-stringname))                                                                                                     |
| [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] | get_actions()                                                                                                                                                                                     |
| [bool](class_bool.md#class-bool)                                                        | has_action(action: [StringName](class_stringname.md#class-stringname))                                                                                                                             |
|                                                                                         | load_from_project_settings()                                                                                                                                                       |

---

## Signals

**project_settings_loaded**()

Emitted when the [ProjectSettings](class_projectsettings.md#class-projectsettings) **InputMap** has been loaded.

---

## Method Descriptions

 **action_add_event**(action: [StringName](class_stringname.md#class-stringname), event: [InputEvent](class_inputevent.md#class-inputevent))

Adds an [InputEvent](class_inputevent.md#class-inputevent) to an action. This [InputEvent](class_inputevent.md#class-inputevent) will trigger the action.

---

 **action_erase_event**(action: [StringName](class_stringname.md#class-stringname), event: [InputEvent](class_inputevent.md#class-inputevent))

Removes an [InputEvent](class_inputevent.md#class-inputevent) from an action.

---

 **action_erase_events**(action: [StringName](class_stringname.md#class-stringname))

Removes all events from an action.

---

[float](class_float.md#class-float) **action_get_deadzone**(action: [StringName](class_stringname.md#class-stringname))

Returns a deadzone value for the action.

---

[Array](class_array.md#class-array)[[InputEvent](class_inputevent.md#class-inputevent)] **action_get_events**(action: [StringName](class_stringname.md#class-stringname))

Returns an array of [InputEvent](class_inputevent.md#class-inputevent)s associated with a given action.

**Note:** When used in the editor (e.g. a tool script or [EditorPlugin](class_editorplugin.md#class-editorplugin)), this method will return events for the editor action. If you want to access your project's input binds from the editor, read the `input/*` settings from [ProjectSettings](class_projectsettings.md#class-projectsettings).

---

[bool](class_bool.md#class-bool) **action_has_event**(action: [StringName](class_stringname.md#class-stringname), event: [InputEvent](class_inputevent.md#class-inputevent))

Returns `true` if the action has the given [InputEvent](class_inputevent.md#class-inputevent) associated with it.

---

 **action_set_deadzone**(action: [StringName](class_stringname.md#class-stringname), deadzone: [float](class_float.md#class-float))

Sets a deadzone value for the action.

---

 **add_action**(action: [StringName](class_stringname.md#class-stringname), deadzone: [float](class_float.md#class-float) = 0.2)

Adds an empty action to the **InputMap** with a configurable `deadzone`.

An [InputEvent](class_inputevent.md#class-inputevent) can then be added to this action with action_add_event().

---

 **erase_action**(action: [StringName](class_stringname.md#class-stringname))

Removes an action from the **InputMap**.

---

[bool](class_bool.md#class-bool) **event_is_action**(event: [InputEvent](class_inputevent.md#class-inputevent), action: [StringName](class_stringname.md#class-stringname), exact_match: [bool](class_bool.md#class-bool) = false)

Returns `true` if the given event is part of an existing action. This method ignores keyboard modifiers if the given [InputEvent](class_inputevent.md#class-inputevent) is not pressed (for proper release detection). See action_has_event() if you don't want this behavior.

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class-inputeventkey) and [InputEventMouseButton](class_inputeventmousebutton.md#class-inputeventmousebutton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class-inputeventjoypadmotion) events.

---

[String](class_string.md#class-string) **get_action_description**(action: [StringName](class_stringname.md#class-stringname))

Returns the human-readable description of the given action.

---

[Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] **get_actions**()

Returns an array of all actions in the **InputMap**.

---

[bool](class_bool.md#class-bool) **has_action**(action: [StringName](class_stringname.md#class-stringname))

Returns `true` if the **InputMap** has a registered action with the given name.

---

 **load_from_project_settings**()

Clears all [InputEventAction](class_inputeventaction.md#class-inputeventaction) in the **InputMap** and load it anew from [ProjectSettings](class_projectsettings.md#class-projectsettings).
