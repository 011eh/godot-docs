# OpenXRFutureResult

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Result object tracking the asynchronous result of an OpenXR Future object.

## Description

Result object tracking the asynchronous result of an OpenXR Future object, you can use this object to track the result status.

## Methods

|                                                       | cancel_future()                                                              |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [int](class_int.md#class-int)                         | get_future()                                                                    |
| [Variant](class_variant.md#class-variant)             | get_result_value()                                                        |
| ResultStatus | get_status()                                                                    |
|                                                       | set_result_value(result_value: [Variant](class_variant.md#class-variant)) |

---

## Signals

**completed**(result: OpenXRFutureResult)

Emitted when the asynchronous function is finished or has been cancelled.

---

## Enumerations

enum **ResultStatus**:

ResultStatus **RESULT_RUNNING** = `0`

The asynchronous function is running.

ResultStatus **RESULT_FINISHED** = `1`

The asynchronous function has finished.

ResultStatus **RESULT_CANCELLED** = `2`

The asynchronous function has been cancelled.

---

## Method Descriptions

 **cancel_future**()

Cancel this future, this will interrupt and stop the asynchronous function.

---

[int](class_int.md#class-int) **get_future**()

Return the `XrFutureEXT` value this result relates to.

---

[Variant](class_variant.md#class-variant) **get_result_value**()

Returns the result value of our asynchronous function (if set by the extension). The type of this result value depends on the function being called. Consult the documentation of the relevant function.

---

ResultStatus **get_status**()

Returns the status of this result.

---

 **set_result_value**(result_value: [Variant](class_variant.md#class-variant))

Stores the result value we expose to the user.

**Note:** This method should only be called by an OpenXR extension that implements an asynchronous function.
