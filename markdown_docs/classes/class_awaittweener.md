# AwaitTweener

**Inherits:** [Tweener](class_tweener.md#class-tweener) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Awaits a specified signal.

## Description

**AwaitTweener** is used to await a specified signal, allowing asynchronous steps in [Tween](class_tween.md#class-tween) animation. See [Tween.tween_await()](class_tween.md#class-tween-method-tween-await) for more usage information.

The [Tweener.finished](class_tweener.md#class-tweener-signal-finished) signal is emitted when either the awaited signal is received, when timeout is reached, or when the target object is freed.

## Methods

| AwaitTweener   | set_timeout(timeout: [float](class_float.md#class-float))   |
|---------------------------------------|-------------------------------------------------------------------------------------------------------|

---

## Method Descriptions

AwaitTweener **set_timeout**(timeout: [float](class_float.md#class-float))

Sets the maximum time an **AwaitTweener** can wait for the signal. Can be used as a safeguard for signals that may never be emitted. If not specified, the tweener will wait indefinitely.
