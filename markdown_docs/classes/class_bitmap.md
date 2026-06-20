# BitMap

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

Boolean matrix.

## Description

A two-dimensional array of boolean values, can be used to efficiently store a binary matrix (every matrix element takes only one bit) and query the values using natural cartesian coordinates.

## Methods

| [Image](class_image.md#class-image)                                                                             | convert_to_image()                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                 | create(size: [Vector2i](class_vector2i.md#class-vector2i))                                                                                 |
|                                                                                                                 | create_from_image_alpha(image: [Image](class_image.md#class-image), threshold: [float](class_float.md#class-float) = 0.1) |
| [bool](class_bool.md#class-bool)                                                                                | get_bit(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int))                                                               |
| [bool](class_bool.md#class-bool)                                                                                | get_bitv(position: [Vector2i](class_vector2i.md#class-vector2i))                                                                         |
| [Vector2i](class_vector2i.md#class-vector2i)                                                                    | get_size()                                                                                                                               |
| [int](class_int.md#class-int)                                                                                   | get_true_bit_count()                                                                                                           |
|                                                                                                                 | grow_mask(pixels: [int](class_int.md#class-int), rect: [Rect2i](class_rect2i.md#class-rect2i))                                          |
| [Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] | opaque_to_polygons(rect: [Rect2i](class_rect2i.md#class-rect2i), epsilon: [float](class_float.md#class-float) = 2.0)           |
|                                                                                                                 | resize(new_size: [Vector2i](class_vector2i.md#class-vector2i))                                                                             |
|                                                                                                                 | set_bit(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), bit: [bool](class_bool.md#class-bool))                        |
|                                                                                                                 | set_bit_rect(rect: [Rect2i](class_rect2i.md#class-rect2i), bit: [bool](class_bool.md#class-bool))                                    |
|                                                                                                                 | set_bitv(position: [Vector2i](class_vector2i.md#class-vector2i), bit: [bool](class_bool.md#class-bool))                                  |

---

## Method Descriptions

[Image](class_image.md#class-image) **convert_to_image**()

Returns an image of the same size as the bitmap and with an [Format](class_image.md#enum-image-format) of type [Image.FORMAT_L8](class_image.md#class-image-constant-format-l8). `true` bits of the bitmap are being converted into white pixels, and `false` bits into black.

---

 **create**(size: [Vector2i](class_vector2i.md#class-vector2i))

Creates a bitmap with the specified size, filled with `false`.

---

 **create_from_image_alpha**(image: [Image](class_image.md#class-image), threshold: [float](class_float.md#class-float) = 0.1)

Creates a bitmap that matches the given image dimensions, every element of the bitmap is set to `false` if the alpha value of the image at that position is equal to `threshold` or less, and `true` in other case.

---

[bool](class_bool.md#class-bool) **get_bit**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int))

Returns bitmap's value at the specified position.

---

[bool](class_bool.md#class-bool) **get_bitv**(position: [Vector2i](class_vector2i.md#class-vector2i))

Returns bitmap's value at the specified position.

---

[Vector2i](class_vector2i.md#class-vector2i) **get_size**()

Returns bitmap's dimensions.

---

[int](class_int.md#class-int) **get_true_bit_count**()

Returns the number of bitmap elements that are set to `true`.

---

 **grow_mask**(pixels: [int](class_int.md#class-int), rect: [Rect2i](class_rect2i.md#class-rect2i))

Applies morphological dilation or erosion to the bitmap. If `pixels` is positive, dilation is applied to the bitmap. If `pixels` is negative, erosion is applied to the bitmap. `rect` defines the area where the morphological operation is applied. Pixels located outside the `rect` are unaffected by grow_mask().

---

[Array](class_array.md#class-array)[[PackedVector2Array](class_packedvector2array.md#class-packedvector2array)] **opaque_to_polygons**(rect: [Rect2i](class_rect2i.md#class-rect2i), epsilon: [float](class_float.md#class-float) = 2.0)

Creates an [Array](class_array.md#class-array) of polygons covering a rectangular portion of the bitmap. It uses a marching squares algorithm, followed by Ramer-Douglas-Peucker (RDP) reduction of the number of vertices. Each polygon is described as a [PackedVector2Array](class_packedvector2array.md#class-packedvector2array) of its vertices.

To get polygons covering the whole bitmap, pass:

```gdscript
Rect2(Vector2(), get_size())
```

`epsilon` is passed to RDP to control how accurately the polygons cover the bitmap: a lower `epsilon` corresponds to more points in the polygons.

---

 **resize**(new_size: [Vector2i](class_vector2i.md#class-vector2i))

Resizes the image to `new_size`.

---

 **set_bit**(x: [int](class_int.md#class-int), y: [int](class_int.md#class-int), bit: [bool](class_bool.md#class-bool))

Sets the bitmap's element at the specified position, to the specified value.

---

 **set_bit_rect**(rect: [Rect2i](class_rect2i.md#class-rect2i), bit: [bool](class_bool.md#class-bool))

Sets a rectangular portion of the bitmap to the specified value.

---

 **set_bitv**(position: [Vector2i](class_vector2i.md#class-vector2i), bit: [bool](class_bool.md#class-bool))

Sets the bitmap's element at the specified position, to the specified value.
