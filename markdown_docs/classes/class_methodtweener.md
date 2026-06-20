# MethodTweener

**Inherits:** [Tweener](class_tweener.md#class-tweener) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Interpolates an abstract value and supplies it to a method called over time.

## Description

**MethodTweener** is similar to a combination of [CallbackTweener](class_callbacktweener.md#class-callbacktweener) and [PropertyTweener](class_propertytweener.md#class-propertytweener). It calls a method providing an interpolated value as a parameter. See [Tween.tween_method()](class_tween.md#class-tween-method-tween-method) for more usage information.

The tweener will finish automatically if the callback's target object is freed.

**Note:** [Tween.tween_method()](class_tween.md#class-tween-method-tween-method) is the only correct way to create **MethodTweener**. Any **MethodTweener** created manually will not function correctly.

## Methods

| MethodTweener   | set_delay(delay: [float](class_float.md#class-float))                        |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| MethodTweener   | set_ease(ease: [EaseType](class_tween.md#enum-tween-easetype))                |
| MethodTweener   | set_trans(trans: [TransitionType](class_tween.md#enum-tween-transitiontype)) |

---

## Method Descriptions

MethodTweener **set_delay**(delay: [float](class_float.md#class-float))

Sets the time in seconds after which the **MethodTweener** will start interpolating. By default there's no delay.

---

MethodTweener **set_ease**(ease: [EaseType](class_tween.md#enum-tween-easetype))

Sets the type of used easing from [EaseType](class_tween.md#enum-tween-easetype). If not set, the default easing is used from the [Tween](class_tween.md#class-tween) that contains this Tweener.

---

MethodTweener **set_trans**(trans: [TransitionType](class_tween.md#enum-tween-transitiontype))

Sets the type of used transition from [TransitionType](class_tween.md#enum-tween-transitiontype). If not set, the default transition is used from the [Tween](class_tween.md#class-tween) that contains this Tweener.
