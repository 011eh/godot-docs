# PackedInt64Array

A packed array of 64-bit integers.

## Description

An array specifically designed to hold 64-bit integer values. Packs data tightly, so it saves memory for large array sizes.

**Note:** This type stores signed 64-bit integers, which means it can take values in the interval `[-2^63, 2^63 - 1]`, i.e. `[-9223372036854775808, 9223372036854775807]`. Exceeding those bounds will wrap around. If you only need to pack 32-bit integers tightly, see [PackedInt32Array](class_packedint32array.md#class-packedint32array) for a more memory-friendly alternative.

**Differences between packed arrays, typed arrays, and untyped arrays:** Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g. **PackedInt64Array** versus `Array[int]`). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such as [Array.map()](class_array.md#class-array-method-map). Typed arrays are in turn faster to iterate on and modify than untyped arrays.

**Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use duplicate(). This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

**Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Constructors

| PackedInt64Array   | PackedInt64Array()                                                  |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| PackedInt64Array   | PackedInt64Array(from: PackedInt64Array) |
| PackedInt64Array   | PackedInt64Array(from: [Array](class_array.md#class-array))         |

## Methods

| [bool](class_bool.md#class-bool)                                  | append(value: [int](class_int.md#class-int))                                                    |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                   | append_array(array: PackedInt64Array)                          |
| [int](class_int.md#class-int)                                     | bsearch(value: [int](class_int.md#class-int), before: [bool](class_bool.md#class-bool) = true) |
|                                                                   | clear()                                                                                          |
| [int](class_int.md#class-int)                                     | count(value: [int](class_int.md#class-int))                                                      |
| PackedInt64Array                       | duplicate()                                                                                  |
| [bool](class_bool.md#class-bool)                                  | erase(value: [int](class_int.md#class-int))                                                      |
|                                                                   | fill(value: [int](class_int.md#class-int))                                                        |
| [int](class_int.md#class-int)                                     | find(value: [int](class_int.md#class-int), from: [int](class_int.md#class-int) = 0)               |
| [int](class_int.md#class-int)                                     | get(index: [int](class_int.md#class-int))                                                          |
| [bool](class_bool.md#class-bool)                                  | has(value: [int](class_int.md#class-int))                                                          |
| [int](class_int.md#class-int)                                     | insert(at_index: [int](class_int.md#class-int), value: [int](class_int.md#class-int))           |
| [bool](class_bool.md#class-bool)                                  | is_empty()                                                                                    |
| [bool](class_bool.md#class-bool)                                  | push_back(value: [int](class_int.md#class-int))                                              |
|                                                                   | remove_at(index: [int](class_int.md#class-int))                                              |
| [int](class_int.md#class-int)                                     | resize(new_size: [int](class_int.md#class-int))                                                 |
|                                                                   | reverse()                                                                                      |
| [int](class_int.md#class-int)                                     | rfind(value: [int](class_int.md#class-int), from: [int](class_int.md#class-int) = -1)            |
|                                                                   | set(index: [int](class_int.md#class-int), value: [int](class_int.md#class-int))                    |
| [int](class_int.md#class-int)                                     | size()                                                                                            |
| PackedInt64Array                       | slice(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647)     |
|                                                                   | sort()                                                                                            |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | to_byte_array()                                                                          |

## Operators

| [bool](class_bool.md#class-bool)            | operator !=(right: PackedInt64Array)   |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| PackedInt64Array | operator +(right: PackedInt64Array)    |
| [bool](class_bool.md#class-bool)            | operator ==(right: PackedInt64Array)    |
| [int](class_int.md#class-int)               | operator [](index: [int](class_int.md#class-int))                              |

---

## Constructor Descriptions

PackedInt64Array **PackedInt64Array**()

Constructs an empty **PackedInt64Array**.

---

PackedInt64Array **PackedInt64Array**(from: PackedInt64Array)

Constructs a **PackedInt64Array** as a copy of the given **PackedInt64Array**.

---

PackedInt64Array **PackedInt64Array**(from: [Array](class_array.md#class-array))

Constructs a new **PackedInt64Array**. Optionally, you can pass in a generic [Array](class_array.md#class-array) that will be converted.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **append**(value: [int](class_int.md#class-int))

Appends an element at the end of the array (alias of push_back()).

---

 **append_array**(array: PackedInt64Array)

Appends a **PackedInt64Array** at the end of this array.

---

[int](class_int.md#class-int) **bsearch**(value: [int](class_int.md#class-int), before: [bool](class_bool.md#class-bool) = true)

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

**Note:** Calling bsearch() on an unsorted array results in unexpected behavior.

---

 **clear**()

Clears the array. This is equivalent to using resize() with a size of `0`.

---

[int](class_int.md#class-int) **count**(value: [int](class_int.md#class-int))

Returns the number of times an element is in the array.

---

PackedInt64Array **duplicate**()

Creates a copy of the array, and returns it.

---

[bool](class_bool.md#class-bool) **erase**(value: [int](class_int.md#class-int))

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use remove_at() instead.

---

 **fill**(value: [int](class_int.md#class-int))

Assigns the given value to all elements in the array. This can typically be used together with resize() to create an array with a given size and initialized elements.

---

[int](class_int.md#class-int) **find**(value: [int](class_int.md#class-int), from: [int](class_int.md#class-int) = 0)

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

---

[int](class_int.md#class-int) **get**(index: [int](class_int.md#class-int))

Returns the 64-bit integer at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `0`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

---

[bool](class_bool.md#class-bool) **has**(value: [int](class_int.md#class-int))

Returns `true` if the array contains `value`.

---

[int](class_int.md#class-int) **insert**(at_index: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Inserts a new integer at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).

---

[bool](class_bool.md#class-bool) **is_empty**()

Returns `true` if the array is empty.

---

[bool](class_bool.md#class-bool) **push_back**(value: [int](class_int.md#class-int))

Appends a value to the array.

---

 **remove_at**(index: [int](class_int.md#class-int))

Removes an element from the array by index.

---

[int](class_int.md#class-int) **resize**(new_size: [int](class_int.md#class-int))

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling resize() once and assigning the new values is faster than adding new elements one by one.

Returns [@GlobalScope.OK](class_@globalscope.md#class-globalscope-constant-ok) on success, or one of the following [Error](class_@globalscope.md#enum-globalscope-error) constants if this method fails: [@GlobalScope.ERR_INVALID_PARAMETER](class_@globalscope.md#class-globalscope-constant-err-invalid-parameter) if the size is negative, or [@GlobalScope.ERR_OUT_OF_MEMORY](class_@globalscope.md#class-globalscope-constant-err-out-of-memory) if allocations fail. Use size() to find the actual size of the array after resize.

---

 **reverse**()

Reverses the order of the elements in the array.

---

[int](class_int.md#class-int) **rfind**(value: [int](class_int.md#class-int), from: [int](class_int.md#class-int) = -1)

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

---

 **set**(index: [int](class_int.md#class-int), value: [int](class_int.md#class-int))

Changes the integer at the given index.

---

[int](class_int.md#class-int) **size**()

Returns the number of elements in the array.

---

PackedInt64Array **slice**(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647)

Returns the slice of the **PackedInt64Array**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedInt64Array**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

---

 **sort**()

Sorts the elements of the array in ascending order.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_byte_array**()

Returns a copy of the data converted to a [PackedByteArray](class_packedbytearray.md#class-packedbytearray), where each element has been encoded as 8 bytes.

The size of the new array will be `int64_array.size() * 8`.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: PackedInt64Array)

Returns `true` if contents of the arrays differ.

---

PackedInt64Array **operator +**(right: PackedInt64Array)

Returns a new **PackedInt64Array** with contents of `right` added at the end of this array. For better performance, consider using append_array() instead.

---

[bool](class_bool.md#class-bool) **operator ==**(right: PackedInt64Array)

Returns `true` if contents of both arrays are the same, i.e. they have all equal ints at the corresponding indices.

---

[int](class_int.md#class-int) **operator []**(index: [int](class_int.md#class-int))

Returns the [int](class_int.md#class-int) at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.
