# Shortcut

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A shortcut for binding input.

## Description

Shortcuts (also known as hotkeys) are containers of [InputEvent](class_inputevent.md#class-inputevent) resources. They are commonly used to interact with a [Control](class_control.md#class-control) element from an [InputEvent](class_inputevent.md#class-inputevent).

One shortcut can contain multiple [InputEvent](class_inputevent.md#class-inputevent) resources, making it possible to trigger one action with multiple different inputs.

**Example:** Capture the `Ctrl + S` shortcut using a **Shortcut** resource:

GDScript

```gdscript
extends Node

var save_shortcut = Shortcut.new()
func _ready():
    var key_event = InputEventKey.new()
    key_event.keycode = KEY_S
    key_event.ctrl_pressed = true
    key_event.command_or_control_autoremap = true # Swaps Ctrl for Command on Mac.
    save_shortcut.events = [key_event]

func _input(event):
    if save_shortcut.matches_event(event) and event.is_pressed() and not event.is_echo():
        print("Save shortcut pressed!")
        get_viewport().set_input_as_handled()
```

C#

```csharp
using Godot;

public partial class MyNode : Node
{
    private readonly Shortcut _saveShortcut = new Shortcut();

    public override void _Ready()
    {
        InputEventKey keyEvent = new InputEventKey
        {
            Keycode = Key.S,
            CtrlPressed = true,
            CommandOrControlAutoremap = true, // Swaps Ctrl for Command on Mac.
        };

        _saveShortcut.Events = [keyEvent];
    }

    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventKey keyEvent &&
            _saveShortcut.MatchesEvent(@event) &&
            keyEvent.Pressed && !keyEvent.Echo)
        {
            GD.Print("Save shortcut pressed!");
            GetViewport().SetInputAsHandled();
        }
    }
}
```

## Properties

| [Array](class_array.md#class-array)   | events   | `[]`   |
|---------------------------------------|---------------------------------------------|--------|

## Methods

| [String](class_string.md#class-string)   | get_as_text()                                                              |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)         | has_valid_event()                                                      |
| [bool](class_bool.md#class-bool)         | matches_event(event: [InputEvent](class_inputevent.md#class-inputevent)) |

---

## Property Descriptions

[Array](class_array.md#class-array) **events** = `[]`

-  **set_events**(value: [Array](class_array.md#class-array))
- [Array](class_array.md#class-array) **get_events**()

The shortcut's [InputEvent](class_inputevent.md#class-inputevent) array.

Generally the [InputEvent](class_inputevent.md#class-inputevent) used is an [InputEventKey](class_inputeventkey.md#class-inputeventkey), though it can be any [InputEvent](class_inputevent.md#class-inputevent), including an [InputEventAction](class_inputeventaction.md#class-inputeventaction).

---

## Method Descriptions

[String](class_string.md#class-string) **get_as_text**()

Returns the shortcut's first valid [InputEvent](class_inputevent.md#class-inputevent) as a [String](class_string.md#class-string).

---

[bool](class_bool.md#class-bool) **has_valid_event**()

Returns whether events contains an [InputEvent](class_inputevent.md#class-inputevent) which is valid.

---

[bool](class_bool.md#class-bool) **matches_event**(event: [InputEvent](class_inputevent.md#class-inputevent))

Returns whether any [InputEvent](class_inputevent.md#class-inputevent) in events equals `event`. This uses [InputEvent.is_match()](class_inputevent.md#class-inputevent-method-is-match) to compare events.
