# Tweener

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [AwaitTweener](class_awaittweener.md#class-awaittweener), [CallbackTweener](class_callbacktweener.md#class-callbacktweener), [IntervalTweener](class_intervaltweener.md#class-intervaltweener), [MethodTweener](class_methodtweener.md#class-methodtweener), [PropertyTweener](class_propertytweener.md#class-propertytweener), [SubtweenTweener](class_subtweentweener.md#class-subtweentweener)

Abstract class for all Tweeners used by [Tween](class_tween.md#class-tween).

## Description

Tweeners are objects that perform a specific animating task, e.g. interpolating a property or calling a method at a given time. A **Tweener** can't be created manually, you need to use a dedicated method from [Tween](class_tween.md#class-tween).

---

## Signals

**finished**()

Emitted when the **Tweener** has just finished its job or became invalid (e.g. due to a freed object).
