# InputEventKey

**Inherits:** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class-inputeventfromwindow) **<** [InputEvent](class_inputevent.md#class-inputevent) **<** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Represents a key on a keyboard being pressed or released.

## Description

An input event for keys on a keyboard. Supports key presses, key releases and echo events. It can also be received in [Node._unhandled_key_input()](class_node.md#class-node-private-method-unhandled-key-input).

**Note:** Events received from the keyboard usually have all properties set. Event mappings should have only one of the keycode, physical_keycode or unicode set.

When events are compared, properties are checked in the following priority - keycode, physical_keycode and unicode. Events with the first matching value will be considered equal.

## Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

## Properties

| [bool](class_bool.md#class-bool)                                  | echo                         | `false`   |
|-------------------------------------------------------------------|--------------------------------------------------------------------|-----------|
| [Key](class_@globalscope.md#enum-globalscope-key)                 | key_label               | `0`       |
| [Key](class_@globalscope.md#enum-globalscope-key)                 | keycode                   | `0`       |
| [KeyLocation](class_@globalscope.md#enum-globalscope-keylocation) | location                 | `0`       |
| [Key](class_@globalscope.md#enum-globalscope-key)                 | physical_keycode | `0`       |
| [bool](class_bool.md#class-bool)                                  | pressed                   | `false`   |
| [int](class_int.md#class-int)                                     | unicode                   | `0`       |

## Methods

| [String](class_string.md#class-string)            | as_text_key_label()                                     |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [String](class_string.md#class-string)            | as_text_keycode()                                         |
| [String](class_string.md#class-string)            | as_text_location()                                       |
| [String](class_string.md#class-string)            | as_text_physical_keycode()                       |
| [Key](class_@globalscope.md#enum-globalscope-key) | get_key_label_with_modifiers()               |
| [Key](class_@globalscope.md#enum-globalscope-key) | get_keycode_with_modifiers()                   |
| [Key](class_@globalscope.md#enum-globalscope-key) | get_physical_keycode_with_modifiers() |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **echo** = `false`

-  **set_echo**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_echo**()

If `true`, the key was already pressed before this event. An echo event is a repeated key event sent when the user is holding down the key.

**Note:** The rate at which echo events are sent is typically around 20 events per second (after holding down the key for roughly half a second). However, the key repeat delay/speed can be changed by the user or disabled entirely in the operating system settings. To ensure your project works correctly on all configurations, do not assume the user has a specific key repeat configuration in your project's behavior.

---

[Key](class_@globalscope.md#enum-globalscope-key) **key_label** = `0`

-  **set_key_label**(value: [Key](class_@globalscope.md#enum-globalscope-key))
- [Key](class_@globalscope.md#enum-globalscope-key) **get_key_label**()

Represents the localized label printed on the key in the current keyboard layout, which corresponds to one of the [Key](class_@globalscope.md#enum-globalscope-key) constants or any valid Unicode character. Key labels are meant for key prompts.

For keyboard layouts with a single label on the key, it is equivalent to keycode.

To get a human-readable representation of the **InputEventKey**, use `OS.get_keycode_string(event.key_label)` where `event` is the **InputEventKey**.

```text
+-----+ +-----+
| Q   | | Q   | - "Q" - keycode
|   Й | |  ض | - "Й" and "ض" - key_label
+-----+ +-----+
```

---

[Key](class_@globalscope.md#enum-globalscope-key) **keycode** = `0`

-  **set_keycode**(value: [Key](class_@globalscope.md#enum-globalscope-key))
- [Key](class_@globalscope.md#enum-globalscope-key) **get_keycode**()

Latin label printed on the key in the current keyboard layout, which corresponds to one of the [Key](class_@globalscope.md#enum-globalscope-key) constants. Key codes are meant for shortcuts expressed with a standard Latin keyboard, such as `Ctrl + S` for a "Save" shortcut.

To get a human-readable representation of the **InputEventKey**, use `OS.get_keycode_string(event.keycode)` where `event` is the **InputEventKey**.

```text
+-----+ +-----+
| Q   | | Q   | - "Q" - keycode
|   Й | |  ض | - "Й" and "ض" - key_label
+-----+ +-----+
```

---

[KeyLocation](class_@globalscope.md#enum-globalscope-keylocation) **location** = `0`

-  **set_location**(value: [KeyLocation](class_@globalscope.md#enum-globalscope-keylocation))
- [KeyLocation](class_@globalscope.md#enum-globalscope-keylocation) **get_location**()

Represents the location of a key which has both left and right versions, such as `Shift` or `Alt`.

---

[Key](class_@globalscope.md#enum-globalscope-key) **physical_keycode** = `0`

-  **set_physical_keycode**(value: [Key](class_@globalscope.md#enum-globalscope-key))
- [Key](class_@globalscope.md#enum-globalscope-key) **get_physical_keycode**()

Represents the physical location of a key on the 101/102-key US QWERTY keyboard, which corresponds to one of the [Key](class_@globalscope.md#enum-globalscope-key) constants. Physical key codes meant for game input, such as WASD movement, where only the location of the keys is important.

To get a human-readable representation of the **InputEventKey**, use [OS.get_keycode_string()](class_os.md#class-os-method-get-keycode-string) in combination with [DisplayServer.keyboard_get_keycode_from_physical()](class_displayserver.md#class-displayserver-method-keyboard-get-keycode-from-physical) or [DisplayServer.keyboard_get_label_from_physical()](class_displayserver.md#class-displayserver-method-keyboard-get-label-from-physical):

GDScript

```gdscript
func _input(event):
    if event is InputEventKey:
        var keycode = DisplayServer.keyboard_get_keycode_from_physical(event.physical_keycode)
        var label = DisplayServer.keyboard_get_label_from_physical(event.physical_keycode)
        print(OS.get_keycode_string(keycode))
        print(OS.get_keycode_string(label))
```

C#

```csharp
public override void _Input(InputEvent @event)
{
    if (@event is InputEventKey inputEventKey)
    {
        var keycode = DisplayServer.KeyboardGetKeycodeFromPhysical(inputEventKey.PhysicalKeycode);
        var label = DisplayServer.KeyboardGetLabelFromPhysical(inputEventKey.PhysicalKeycode);
        GD.Print(OS.GetKeycodeString(keycode));
        GD.Print(OS.GetKeycodeString(label));
    }
}
```

---

[bool](class_bool.md#class-bool) **pressed** = `false`

-  **set_pressed**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_pressed**()

If `true`, the key's state is pressed. If `false`, the key's state is released.

---

[int](class_int.md#class-int) **unicode** = `0`

-  **set_unicode**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_unicode**()

The key Unicode character code (when relevant), shifted by modifier keys. Unicode character codes for composite characters and complex scripts may not be available unless IME input mode is active. See [Window.set_ime_active()](class_window.md#class-window-method-set-ime-active) for more information. Unicode character codes are meant for text input.

**Note:** This property is set by the engine only for a pressed event. If the event is sent by an IME or a virtual keyboard, no corresponding key released event is sent.

---

## Method Descriptions

[String](class_string.md#class-string) **as_text_key_label**()

Returns a [String](class_string.md#class-string) representation of the event's key_label and modifiers.

---

[String](class_string.md#class-string) **as_text_keycode**()

Returns a [String](class_string.md#class-string) representation of the event's keycode and modifiers.

---

[String](class_string.md#class-string) **as_text_location**()

Returns a [String](class_string.md#class-string) representation of the event's location. This will be a blank string if the event is not specific to a location.

---

[String](class_string.md#class-string) **as_text_physical_keycode**()

Returns a [String](class_string.md#class-string) representation of the event's physical_keycode and modifiers.

---

[Key](class_@globalscope.md#enum-globalscope-key) **get_key_label_with_modifiers**()

Returns the localized key label combined with modifier keys such as `Shift` or `Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_key_label_with_modifiers())` where `event` is the **InputEventKey**.

---

[Key](class_@globalscope.md#enum-globalscope-key) **get_keycode_with_modifiers**()

Returns the Latin keycode combined with modifier keys such as `Shift` or `Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_keycode_with_modifiers())` where `event` is the **InputEventKey**.

---

[Key](class_@globalscope.md#enum-globalscope-key) **get_physical_keycode_with_modifiers**()

Returns the physical keycode combined with modifier keys such as `Shift` or `Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class-inputeventwithmodifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_physical_keycode_with_modifiers())` where `event` is the **InputEventKey**.
