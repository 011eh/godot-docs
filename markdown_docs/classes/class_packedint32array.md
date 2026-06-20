# PackedInt32Array

A packed array of 32-bit integers.

## Description

An array specifically designed to hold 32-bit integer values. Packs data tightly, so it saves memory for large array sizes.

**Note:** This type stores signed 32-bit integers, which means it can take values in the interval `[-2^31, 2^31 - 1]`, i.e. `[-2147483648, 2147483647]`. Exceeding those bounds will wrap around. In comparison, [int](class_int.md#class-int) uses signed 64-bit integers which can hold much larger values. If you need to pack 64-bit integers tightly, see [PackedInt64Array](class_packedint64array.md#class-packedint64array).

**Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use duplicate(). This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

**Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

#### NOTE
There are notable differences when using this API with C#. See [C# API differences to GDScript](../tutorials/scripting/c_sharp/c_sharp_differences.md#doc-c-sharp-differences) for more information.

## Constructors

| PackedInt32Array   | PackedInt32Array()                                                  |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| PackedInt32Array   | PackedInt32Array(from: PackedInt32Array) |
| PackedInt32Array   | PackedInt32Array(from: [Array](class_array.md#class-array))         |

## Methods

| [bool](class_bool.md#class-bool)                                  | append(value: [int](class_int.md#class-int))                                                    |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                   | append_array(array: PackedInt32Array)                          |
| [int](class_int.md#class-int)                                     | bsearch(value: [int](class_int.md#class-int), before: [bool](class_bool.md#class-bool) = true) |
|                                                                   | clear()                                                                                          |
| [int](class_int.md#class-int)                                     | count(value: [int](class_int.md#class-int))                                                      |
| PackedInt32Array                       | duplicate()                                                                                  |
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
| PackedInt32Array                       | slice(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647)     |
|                                                                   | sort()                                                                                            |
| [PackedByteArray](class_packedbytearray.md#class-packedbytearray) | to_byte_array()                                                                          |

## Operators

| [bool](class_bool.md#class-bool)            | operator !=(right: PackedInt32Array)   |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| PackedInt32Array | operator +(right: PackedInt32Array)    |
| [bool](class_bool.md#class-bool)            | operator ==(right: PackedInt32Array)    |
| [int](class_int.md#class-int)               | operator [](index: [int](class_int.md#class-int))                              |

---

## Constructor Descriptions

PackedInt32Array **PackedInt32Array**()

Constructs an empty **PackedInt32Array**.

---

PackedInt32Array **PackedInt32Array**(from: PackedInt32Array)

Constructs a **PackedInt32Array** as a copy of the given **PackedInt32Array**.

---

PackedInt32Array **PackedInt32Array**(from: [Array](class_array.md#class-array))

Constructs a new **PackedInt32Array**. Optionally, you can pass in a generic [Array](class_array.md#class-array) that will be converted.

---

## Method Descriptions

[bool](class_bool.md#class-bool) **append**(value: [int](class_int.md#class-int))

Appends an element at the end of the array (alias of push_back()).

---

 **append_array**(array: PackedInt32Array)

Appends a **PackedInt32Array** at the end of this array.

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

PackedInt32Array **duplicate**()

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

Returns the 32-bit integer at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `0`.

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

PackedInt32Array **slice**(begin: [int](class_int.md#class-int), end: [int](class_int.md#class-int) = 2147483647)

Returns the slice of the **PackedInt32Array**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedInt32Array**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

---

 **sort**()

Sorts the elements of the array in ascending order.

---

[PackedByteArray](class_packedbytearray.md#class-packedbytearray) **to_byte_array**()

Returns a copy of the data converted to a [PackedByteArray](class_packedbytearray.md#class-packedbytearray), where each element has been encoded as 4 bytes.

The size of the new array will be `int32_array.size() * 4`.

---

## Operator Descriptions

[bool](class_bool.md#class-bool) **operator !=**(right: PackedInt32Array)

Returns `true` if contents of the arrays differ.

---

PackedInt32Array **operator +**(right: PackedInt32Array)

Returns a new **PackedInt32Array** with contents of `right` added at the end of this array. For better performance, consider using append_array() instead.

---

[bool](class_bool.md#class-bool) **operator ==**(right: PackedInt32Array)

Returns `true` if contents of both arrays are the same, i.e. they have all equal ints at the corresponding indices.

---

[int](class_int.md#class-int) **operator []**(index: [int](class_int.md#class-int))

Returns the [int](class_int.md#class-int) at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

Note that [int](class_int.md#class-int) type is 64-bit, unlike the values stored in the array.
