# Noise

**Inherits:** [Resource](class_resource.md#class-resource) **<** [RefCounted](class_refcounted.md#class-refcounted) **<** [Object](class_object.md#class-object)

**Inherited By:** [FastNoiseLite](class_fastnoiselite.md#class-fastnoiselite)

Abstract base class for noise generators.

## Description

This class defines the interface for noise generation libraries to inherit from.

A default get_seamless_image() implementation is provided for libraries that do not provide seamless noise. This function requests a larger image from the get_image() method, reverses the quadrants of the image, then uses the strips of extra width to blend over the seams.

Inheriting noise classes can optionally override this function to provide a more optimal algorithm.

## Methods

| [Image](class_image.md#class-image)                                      | get_image(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, in_3d_space: [bool](class_bool.md#class-bool) = false, normalize: [bool](class_bool.md#class-bool) = true)                                                                     |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Array](class_array.md#class-array)[[Image](class_image.md#class-image)] | get_image_3d(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, normalize: [bool](class_bool.md#class-bool) = true)                                                                                |
| [float](class_float.md#class-float)                                      | get_noise_1d(x: [float](class_float.md#class-float))                                                                                                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                      | get_noise_2d(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float))                                                                                                                                                                                                                         |
| [float](class_float.md#class-float)                                      | get_noise_2dv(v: [Vector2](class_vector2.md#class-vector2))                                                                                                                                                                                                                                                         |
| [float](class_float.md#class-float)                                      | get_noise_3d(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float), z: [float](class_float.md#class-float))                                                                                                                                                                                 |
| [float](class_float.md#class-float)                                      | get_noise_3dv(v: [Vector3](class_vector3.md#class-vector3))                                                                                                                                                                                                                                                         |
| [Image](class_image.md#class-image)                                      | get_seamless_image(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, in_3d_space: [bool](class_bool.md#class-bool) = false, skirt: [float](class_float.md#class-float) = 0.1, normalize: [bool](class_bool.md#class-bool) = true) |
| [Array](class_array.md#class-array)[[Image](class_image.md#class-image)] | get_seamless_image_3d(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, skirt: [float](class_float.md#class-float) = 0.1, normalize: [bool](class_bool.md#class-bool) = true)            |

---

## Method Descriptions

[Image](class_image.md#class-image) **get_image**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, in_3d_space: [bool](class_bool.md#class-bool) = false, normalize: [bool](class_bool.md#class-bool) = true)

Returns an [Image](class_image.md#class-image) containing 2D noise values.

**Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---

[Array](class_array.md#class-array)[[Image](class_image.md#class-image)] **get_image_3d**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, normalize: [bool](class_bool.md#class-bool) = true)

Returns an [Array](class_array.md#class-array) of [Image](class_image.md#class-image)s containing 3D noise values for use with [ImageTexture3D.create()](class_imagetexture3d.md#class-imagetexture3d-method-create).

**Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---

[float](class_float.md#class-float) **get_noise_1d**(x: [float](class_float.md#class-float))

Returns the 1D noise value at the given (x) coordinate.

---

[float](class_float.md#class-float) **get_noise_2d**(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float))

Returns the 2D noise value at the given position.

---

[float](class_float.md#class-float) **get_noise_2dv**(v: [Vector2](class_vector2.md#class-vector2))

Returns the 2D noise value at the given position.

---

[float](class_float.md#class-float) **get_noise_3d**(x: [float](class_float.md#class-float), y: [float](class_float.md#class-float), z: [float](class_float.md#class-float))

Returns the 3D noise value at the given position.

---

[float](class_float.md#class-float) **get_noise_3dv**(v: [Vector3](class_vector3.md#class-vector3))

Returns the 3D noise value at the given position.

---

[Image](class_image.md#class-image) **get_seamless_image**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, in_3d_space: [bool](class_bool.md#class-bool) = false, skirt: [float](class_float.md#class-float) = 0.1, normalize: [bool](class_bool.md#class-bool) = true)

Returns an [Image](class_image.md#class-image) containing seamless 2D noise values.

**Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

---

[Array](class_array.md#class-array)[[Image](class_image.md#class-image)] **get_seamless_image_3d**(width: [int](class_int.md#class-int), height: [int](class_int.md#class-int), depth: [int](class_int.md#class-int), invert: [bool](class_bool.md#class-bool) = false, skirt: [float](class_float.md#class-float) = 0.1, normalize: [bool](class_bool.md#class-bool) = true)

Returns an [Array](class_array.md#class-array) of [Image](class_image.md#class-image)s containing seamless 3D noise values for use with [ImageTexture3D.create()](class_imagetexture3d.md#class-imagetexture3d-method-create).

**Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.
