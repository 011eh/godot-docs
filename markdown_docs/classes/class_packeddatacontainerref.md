# PackedDataContainerRef

**Deprecated:** Use [@GlobalScope.var_to_bytes()](class_@globalscope.md#class-globalscope-method-var-to-bytes) or [FileAccess.store_var()](class_fileaccess.md#class-fileaccess-method-store-var) instead. To enable data compression, use [PackedByteArray.compress()](class_packedbytearray.md#class-packedbytearray-method-compress) or [FileAccess.open_compressed()](class_fileaccess.md#class-fileaccess-method-open-compressed).

**Inherits:** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

An internal class used by [PackedDataContainer](class_packeddatacontainer.md#class-packeddatacontainer) to pack nested arrays and dictionaries.

## Description

When packing nested containers using [PackedDataContainer](class_packeddatacontainer.md#class-packeddatacontainer), they are recursively packed into **PackedDataContainerRef** (only applies to [Array](class_array.md#class-array) and [Dictionary](class_dictionary.md#class-dictionary)). Their data can be retrieved the same way as from [PackedDataContainer](class_packeddatacontainer.md#class-packeddatacontainer).

```gdscript
var packed = PackedDataContainer.new()
packed.pack([1, 2, 3, ["nested1", "nested2"], 4, 5, 6])

for element in packed:
    if element is PackedDataContainerRef:
        for subelement in element:
            print("::", subelement)
    else:
        print(element)
```

Prints:

```text
1
2
3
::nested1
::nested2
4
5
6
```

## Methods

| [int](class_int.md#class-int)   | size()    |
|---------------------------------|--------------------------------------------------------|

---

## Method Descriptions

[int](class_int.md#class-int) **size**()

Returns the size of the packed container (see [Array.size()](class_array.md#class-array-method-size) and [Dictionary.size()](class_dictionary.md#class-dictionary-method-size)).
