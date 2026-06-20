# Thread

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

A unit of execution in a process.

## Description

A unit of execution in a process. Can run methods on [Object](class_object.md#class-object)s simultaneously. The use of synchronization via [Mutex](class_mutex.md#class-mutex) or [Semaphore](class_semaphore.md#class-semaphore) is advised if working with shared objects.

**Warning:** To ensure proper cleanup without crashes or deadlocks, when a **Thread**'s reference count reaches zero and it is therefore destroyed, the following conditions must be met:

- It must not have any [Mutex](class_mutex.md#class-mutex) objects locked.
- It must not be waiting on any [Semaphore](class_semaphore.md#class-semaphore) objects.
- wait_to_finish() should have been called on it.

## Tutorials

- [Using multiple threads](../tutorials/performance/using_multiple_threads.md)
- [Thread-safe APIs](../tutorials/performance/thread_safe_apis.md)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

## Methods

| [String](class_string.md#class-string)                | get_id()                                                                                                      |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)                      | is_alive()                                                                                                  |
| [bool](class_bool.md#class-bool)                      | is_main_thread()                                                                                      |
| [bool](class_bool.md#class-bool)                      | is_started()                                                                                              |
|                                                       | set_thread_safety_checks_enabled(enabled: [bool](class_bool.md#class-bool))         |
| [Error](class_@globalscope.md#enum-globalscope-error) | start(callable: [Callable](class_callable.md#class-callable), priority: Priority = 1) |
| [Variant](class_variant.md#class-variant)             | wait_to_finish()                                                                                      |

---

## Enumerations

enum **Priority**:

Priority **PRIORITY_LOW** = `0`

A thread running with lower priority than normally.

Priority **PRIORITY_NORMAL** = `1`

A thread with a standard priority.

Priority **PRIORITY_HIGH** = `2`

A thread running with higher priority than normally.

---

## Method Descriptions

[String](class_string.md#class-string) **get_id**()

Returns the current **Thread**'s ID, uniquely identifying it among all threads. If the **Thread** has not started running or if wait_to_finish() has been called, this returns an empty string.

---

[bool](class_bool.md#class-bool) **is_alive**()

Returns `true` if this **Thread** is currently running the provided function. This is useful for determining if wait_to_finish() can be called without blocking the calling thread.

To check if a **Thread** is joinable, use is_started().

---

[bool](class_bool.md#class-bool) **is_main_thread**()

Returns `true` if the thread this method was called from is the main thread.

**Note:** This is a static method and isn't associated with a specific **Thread** object.

---

[bool](class_bool.md#class-bool) **is_started**()

Returns `true` if this **Thread** has been started. Once started, this will return `true` until it is joined using wait_to_finish(). For checking if a **Thread** is still executing its task, use is_alive().

---

 **set_thread_safety_checks_enabled**(enabled: [bool](class_bool.md#class-bool))

Sets whether the thread safety checks the engine normally performs in methods of certain classes (e.g., [Node](class_node.md#class-node)) should happen **on the current thread**.

The default, for every thread, is that they are enabled (as if called with `enabled` being `true`).

Those checks are conservative. That means that they will only succeed in considering a call thread-safe (and therefore allow it to happen) if the engine can guarantee such safety.

Because of that, there may be cases where the user may want to disable them (`enabled` being `false`) to make certain operations allowed again. By doing so, it becomes the user's responsibility to ensure thread safety (e.g., by using [Mutex](class_mutex.md#class-mutex)) for those objects that are otherwise protected by the engine.

**Note:** This is an advanced usage of the engine. You are advised to use it only if you know what you are doing and there is no safer way.

**Note:** This is useful for scripts running on either arbitrary **Thread** objects or tasks submitted to the [WorkerThreadPool](class_workerthreadpool.md#class-workerthreadpool). It doesn't apply to code running during [Node](class_node.md#class-node) group processing, where the checks will be always performed.

**Note:** Even in the case of having disabled the checks in a [WorkerThreadPool](class_workerthreadpool.md#class-workerthreadpool) task, there's no need to re-enable them at the end. The engine will do so.

---

[Error](class_@globalscope.md#enum-globalscope-error) **start**(callable: [Callable](class_callable.md#class-callable), priority: Priority = 1)

Starts a new **Thread** that calls `callable`.

If the method takes some arguments, you can pass them using [Callable.bind()](class_callable.md#class-callable-method-bind).

The `priority` of the **Thread** can be changed by passing a value from the Priority enum.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, or [@GlobalScope.ERR_CANT_CREATE](class_@globalscope.md#class-globalscope-constant-err-cant-create) on failure.

---

[Variant](class_variant.md#class-variant) **wait_to_finish**()

Joins the **Thread** and waits for it to finish. Returns the output of the [Callable](class_callable.md#class-callable) passed to start().

Should either be used when you want to retrieve the value returned from the method called by the **Thread** or before freeing the instance that contains the **Thread**.

To determine if this can be called without blocking the calling thread, check if is_alive() is `false`.
