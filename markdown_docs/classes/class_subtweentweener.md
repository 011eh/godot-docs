# SubtweenTweener

**Inherits:** [Tweener](class_tweener.md#class-tweener) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Runs a [Tween](class_tween.md#class-tween) nested within another [Tween](class_tween.md#class-tween).

## Description

**SubtweenTweener** is used to execute a [Tween](class_tween.md#class-tween) as one step in a sequence defined by another [Tween](class_tween.md#class-tween). See [Tween.tween_subtween()](class_tween.md#class-tween-method-tween-subtween) for more usage information.

**Note:** [Tween.tween_subtween()](class_tween.md#class-tween-method-tween-subtween) is the only correct way to create **SubtweenTweener**. Any **SubtweenTweener** created manually will not function correctly.

## Methods

| SubtweenTweener   | set_delay(delay: [float](class_float.md#class-float))   |
|---------------------------------------------|----------------------------------------------------------------------------------------------------|

---

## Method Descriptions

SubtweenTweener **set_delay**(delay: [float](class_float.md#class-float))

Sets the time in seconds after which the **SubtweenTweener** will start running the subtween. By default there's no delay.
