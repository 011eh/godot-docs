# SceneTreeTimer

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

One-shot timer.

## Description

A one-shot timer managed by the scene tree, which emits timeout on completion. See also [SceneTree.create_timer()](class_scenetree.md#class-scenetree-method-create-timer).

As opposed to [Timer](class_timer.md#class-timer), it does not require the instantiation of a node. Commonly used to create a one-shot delay timer as in the following example:

GDScript

```gdscript
func some_function():
    print("Timer started.")
    await get_tree().create_timer(1.0).timeout
    print("Timer ended.")
```

C#

```csharp
public async Task SomeFunction()
{
    GD.Print("Timer started.");
    await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
    GD.Print("Timer ended.");
}
```

The timer will be dereferenced after its time elapses. To preserve the timer, you can keep a reference to it. See [RefCounted](class_refcounted.md#class-refcounted).

**Note:** The timer is processed after all of the nodes in the current frame, i.e. node's [Node._process()](class_node.md#class-node-private-method-process) method would be called before the timer (or [Node._physics_process()](class_node.md#class-node-private-method-physics-process) if `process_in_physics` in [SceneTree.create_timer()](class_scenetree.md#class-scenetree-method-create-timer) has been set to `true`).

## Properties

| [float](class_float.md#class-float)   | time_left   |
|---------------------------------------|---------------------------------------------------------|

---

## Signals

**timeout**()

Emitted when the timer reaches 0.

---

## Property Descriptions

[float](class_float.md#class-float) **time_left**

-  **set_time_left**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_time_left**()

The time remaining (in seconds).
