# Built-in functions

Godot supports a large number of built-in functions, conforming roughly to the
GLSL ES 3.0 specification.

#### NOTE
The following type aliases only used in documentation to reduce repetitive function declarations.
They can each refer to any of several actual types.

| alias           | actual types                                        | glsl documentation alias   |
|-----------------|-----------------------------------------------------|----------------------------|
| vec_type        | float, vec2, vec3, or vec4                          | genType                    |
| vec_int_type    | int, ivec2, ivec3, or ivec4                         | genIType                   |
| vec_uint_type   | uint, uvec2, uvec3, or uvec4                        | genUType                   |
| vec_bool_type   | bool, bvec2, bvec3, or bvec4                        | genBType                   |
| mat_type        | mat2, mat3, or mat4                                 | mat                        |
| gvec4_type      | vec4, ivec4, or uvec4                               | gvec4                      |
| gsampler2D      | sampler2D, isampler2D, or uSampler2D                | gsampler2D                 |
| gsampler2DArray | sampler2DArray, isampler2DArray, or uSampler2DArray | gsampler2DArray            |
| gsampler3D      | sampler3D, isampler3D, or uSampler3D                | gsampler3D                 |

If any of these are specified for multiple parameters, they must all be the same type unless otherwise noted.

#### NOTE
Many functions that accept one or more vectors or matrices perform the described function on each component of the vector/matrix.
Some examples:

| Operation                           | Equivalent Scalar Operation             |
|-------------------------------------|-----------------------------------------|
| `sqrt(vec2(4, 64))`                 | `vec2(sqrt(4), sqrt(64))`               |
| `min(vec2(3, 4), 1)`                | `vec2(min(3, 1), min(4, 1))`            |
| `min(vec3(1, 2, 3),vec3(5, 1, 3))`  | `vec3(min(1, 5), min(2, 1), min(3, 3))` |
| `pow(vec3(3, 8, 5 ), 2)`            | `vec3(pow(3, 2), pow(8, 2), pow(5, 2))` |
| `pow(vec3(3, 8, 5), vec3(1, 2, 4))` | `vec3(pow(3, 1), pow(8, 2), pow(5, 4))` |

The [GLSL Language Specification](http://www.opengl.org/registry/doc/GLSLangSpec.4.30.6.pdf) says under section 5.10 Vector and Matrix Operations:

> With a few exceptions, operations are component-wise. Usually, when an operator operates on a
> vector or matrix, it is operating independently on each component of the vector or matrix,
> in a component-wise fashion. [...] The exceptions are matrix multiplied by vector,
> vector multiplied by matrix, and matrix multiplied by matrix. These do not operate component-wise,
> but rather perform the correct linear algebraic multiply.

These function descriptions are adapted and modified from
[official OpenGL documentation](https://registry.khronos.org/OpenGL-Refpages/gl4/)
originally published by Khronos Group under the
[Open Publication License](https://opencontent.org/openpub).
Each function description links to the corresponding official OpenGL
documentation. Modification history for this page can be found on
[GitHub](https://github.com/godotengine/godot-docs/blob/master/tutorials/shaders/shader_reference/shader_functions.rst).

---

## Trigonometric functions

| Return Type     | Function                                                                                        | Description / Return value   |
|-----------------|-------------------------------------------------------------------------------------------------|------------------------------|
|                 | radians( degrees)                                                       | Convert degrees to radians.  |
|                 | degrees( radians)                                                       | Convert radians to degrees.  |
|                 | sin( x)                                                                     | Sine.                        |
|                 | cos( x)                                                                     | Cosine.                      |
|                 | tan( x)                                                                     | Tangent.                     |
|                 | asin( x)                                                                   | Arc sine.                    |
|                 | acos( x)                                                                   | Arc cosine.                  |
| <br/><br/><br/> | atan( y_over_x)<br/><br/><br/>atan( y,  x)<br/><br/> | Arc tangent.                 |
|                 | sinh( x)                                                                   | Hyperbolic sine.             |
|                 | cosh( x)                                                                   | Hyperbolic cosine.           |
|                 | tanh( x)                                                                   | Hyperbolic tangent.          |
|                 | asinh( x)                                                                 | Arc hyperbolic sine.         |
|                 | acosh( x)                                                                 | Arc hyperbolic cosine.       |
|                 | atanh( x)                                                                 | Arc hyperbolic tangent.      |

### Trigonometric function descriptions

 **radians**( degrees)

> Component-wise Function.

> Converts a quantity specified in degrees into radians, with the formula
> `degrees * (PI / 180)`.

> * **param degrees:**
>   The quantity, in degrees, to be converted to radians.
> * **return:**
>   The input `degrees` converted to radians.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/radians.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/radians.xhtml)

---

 **degrees**( radians)

> Component-wise Function.

> Converts a quantity specified in radians into degrees, with the formula
> `radians * (180 / PI)`

> * **param radians:**
>   The quantity, in radians, to be converted to degrees.
> * **return:**
>   The input `radians` converted to degrees.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/degrees.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/degrees.xhtml)

---

 **sin**( angle)

> Component-wise Function.

> Returns the trigonometric sine of `angle`.

> * **param angle:**
>   The quantity, in radians, of which to return the sine.
> * **return:**
>   The sine of `angle`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sin.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sin.xhtml)

---

 **cos**( angle)

> Component-wise Function.

> Returns the trigonometric cosine of `angle`.

> * **param angle:**
>   The quantity, in radians, of which to return the cosine.
> * **return:**
>   The cosine of `angle`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cos.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cos.xhtml)

---

 **tan**( angle)

> Component-wise Function.

> Returns the trigonometric tangent of `angle`.

> * **param angle:**
>   The quantity, in radians, of which to return the tangent.
> * **return:**
>   The tangent of `angle`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tan.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tan.xhtml)

---

 **asin**( x)

> Component-wise Function.

> Arc sine, or inverse sine.
> Calculates the angle whose sine is `x` and is in the range `[-PI/2, PI/2]`.
> The result is undefined if `x < -1` or `x > 1`.

> * **param x:**
>   The value whose arc sine to return.
> * **return:**
>   The angle whose trigonometric sine is `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asin.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asin.xhtml)

---

 **acos**( x)

> Component-wise Function.

> Arc cosine, or inverse cosine.
> Calculates the angle whose cosine is `x` and is in the range `[0, PI]`.

> The result is undefined if `x < -1` or `x > 1`.

> * **param x:**
>   The value whose arc cosine to return.
> * **return:**
>   The angle whose trigonometric cosine is `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acos.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acos.xhtml)

---

 **atan**( y_over_x)

> Component-wise Function.

> Calculates the arc tangent given a tangent value of `y/x`.

> #### NOTE
> Because of the sign ambiguity, the function cannot determine with certainty in
> which quadrant the angle falls only by its tangent value. If you need to know the
> quadrant, use atan(vec_type y, vec_type x).

> * **param y_over_x:**
>   The fraction whose arc tangent to return.
> * **return:**
>   The trigonometric arc-tangent of `y_over_x` and is
>   in the range `[-PI/2, PI/2]`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml)

---

 **atan**( y,  x)

> Component-wise Function.

> Calculates the arc tangent given a numerator and denominator. The signs of
> `y` and `x` are used to determine the quadrant that the angle lies in.
> The result is undefined if `x == 0`.

> Equivalent to [atan2()](../../../classes/class_@globalscope.md#class-globalscope-method-atan2) in GDScript.

> * **param y:**
>   The numerator of the fraction whose arc tangent to return.
> * **param x:**
>   The denominator of the fraction whose arc tangent to return.
> * **return:**
>   The trigonometric arc tangent of `y/x` and is in
>   the range `[-PI, PI]`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml)

---

 **sinh**( x)

> Component-wise Function.

> Calculates the hyperbolic sine using `(e^x - e^-x)/2`.

> * **param x:**
>   The value whose hyperbolic sine to return.
> * **return:**
>   The hyperbolic sine of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sinh.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sinh.xhtml)

---

 **cosh**( x)

> Component-wise Function.

> Calculates the hyperbolic cosine using `(e^x + e^-x)/2`.

> * **param x:**
>   The value whose hyperbolic cosine to return.
> * **return:**
>   The hyperbolic cosine of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cosh.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cosh.xhtml)

---

 **tanh**( x)

> Component-wise Function.

> Calculates the hyperbolic tangent using `sinh(x)/cosh(x)`.

> * **param x:**
>   The value whose hyperbolic tangent to return.
> * **return:**
>   The hyperbolic tangent of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tanh.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tanh.xhtml)

---

 **asinh**( x)

> Component-wise Function.

> Calculates the arc hyperbolic sine of `x`, or the inverse of `sinh`.

> * **param x:**
>   The value whose arc hyperbolic sine to return.
> * **return:**
>   The arc hyperbolic sine of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asinh.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asinh.xhtml)

---

 **acosh**( x)

> Component-wise Function.

> Calculates the arc hyperbolic cosine of `x`, or the non-negative inverse of `cosh`.
> The result is undefined if `x < 1`.

> * **param x:**
>   The value whose arc hyperbolic cosine to return.
> * **return:**
>   The arc hyperbolic cosine of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acosh.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acosh.xhtml)

---

 **atanh**( x)

> Component-wise Function.

> Calculates the arc hyperbolic tangent of `x`, or the inverse of `tanh`.
> The result is undefined if `abs(x) > 1`.

> * **param x:**
>   The value whose arc hyperbolic tangent to return.
> * **return:**
>   The arc hyperbolic tangent of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atanh.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atanh.xhtml)

---

## Exponential and math functions

| Return Type                                             | Function                                                                                                                                                                                                                                                                                                                                                                        | Description / Return value                                          |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|                                                         | pow( x,  y)                                                                                                                                                                                                                                                                                                                                                 | Power (undefined if `x < 0` or if `x == 0` and `y <= 0`).           |
|                                                         | exp( x)                                                                                                                                                                                                                                                                                                                                                     | Base-e exponential.                                                 |
|                                                         | exp2( x)                                                                                                                                                                                                                                                                                                                                                   | Base-2 exponential.                                                 |
|                                                         | log( x)                                                                                                                                                                                                                                                                                                                                                     | Natural (base-e) logarithm.                                         |
|                                                         | log2( x)                                                                                                                                                                                                                                                                                                                                                   | Base-2 logarithm.                                                   |
|                                                         | sqrt( x)                                                                                                                                                                                                                                                                                                                                                   | Square root.                                                        |
|                                                         | inversesqrt( x)                                                                                                                                                                                                                                                                                                                                     | Inverse square root.                                                |
| <br/><br/><br/>                                         | abs( x)<br/><br/><br/>abs( x)<br/><br/>                                                                                                                                                                                                                                                                                                 | Absolute value (returns positive value if negative).                |
|                                                         | sign( x)                                                                                                                                                                                                                                                                                                                                                   | Returns `1.0` if positive, `-1.0` if negative,<br/>`0.0` otherwise. |
|                                                         | sign( x)                                                                                                                                                                                                                                                                                                                                                   | Returns `1` if positive, `-1` if negative,<br/>`0` otherwise.       |
|                                                         | floor( x)                                                                                                                                                                                                                                                                                                                                                 | Rounds to the integer below.                                        |
|                                                         | round( x)                                                                                                                                                                                                                                                                                                                                                 | Rounds to the nearest integer.                                      |
|                                                         | roundEven( x)                                                                                                                                                                                                                                                                                                                                         | Rounds to the nearest even integer.                                 |
|                                                         | trunc( x)                                                                                                                                                                                                                                                                                                                                                 | Truncation.                                                         |
|                                                         | ceil( x)                                                                                                                                                                                                                                                                                                                                                   | Rounds to the integer above.                                        |
|                                                         | fract( x)                                                                                                                                                                                                                                                                                                                                                 | Fractional (returns `x - floor(x)`).                                |
| <br/><br/><br/>                                         | mod( x,  y)<br/><br/><br/>mod( x, float y)<br/><br/>                                                                                                                                                                                                                                                                                    | Modulo (division remainder).                                        |
|                                                         | modf( x, out  i)                                                                                                                                                                                                                                                                                                                                           | Fractional of `x`, with `i` as integer part.                        |
| <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> | min( a,  b)<br/><br/><br/>min( a, float b)<br/><br/><br/>min( a,  b)<br/><br/><br/>min( a, int b)<br/><br/><br/>min( a,  b)<br/><br/><br/>min( a, uint b)<br/><br/>                                                                                     | Lowest value between `a` and `b`.                                   |
| <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> | max( a,  b)<br/><br/><br/>max( a, float b)<br/><br/><br/>max( a,  b)<br/><br/><br/>max( a, int b)<br/><br/><br/>max( a,  b)<br/><br/><br/>max( a, uint b)<br/><br/>                                                                                     | Highest value between `a` and `b`.                                  |
| <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> | clamp( x,  min,  max)<br/><br/><br/>clamp( x, float min, float max)<br/><br/><br/>clamp( x,  min,  max)<br/><br/><br/>clamp( x, int min, int max)<br/><br/><br/>clamp( x,  min,  max)<br/><br/><br/>clamp( x, uint min, uint max)<br/><br/> | Clamps `x` between `min` and `max` (inclusive).                     |
| <br/><br/><br/><br/><br/>                               | mix( a,  b,  c)<br/><br/><br/>mix( a,  b, float c)<br/><br/><br/>mix( a,  b,  c)<br/><br/>                                                                                                                                                                                                                          | Linear interpolate between `a` and `b` by `c`.                      |
|                                                         | fma( a,  b,  c)                                                                                                                                                                                                                                                                                                                                             | Fused multiply-add operation: `(a * b + c)`                         |
| <br/><br/><br/>                                         | step( a,  b)<br/><br/><br/>step(float a,  b)<br/><br/>                                                                                                                                                                                                                                                                                | `b < a ? 0.0 : 1.0`                                                 |
| <br/><br/><br/>                                         | smoothstep( a,  b,  c)<br/><br/><br/>smoothstep(float a, float b,  c)<br/><br/>                                                                                                                                                                                                                                           | Hermite interpolate between `a` and `b` by `c`.                     |
|                                                         | isnan( x)                                                                                                                                                                                                                                                                                                                                                 | Returns `true` if scalar or vector component is `NaN`.              |
|                                                         | isinf( x)                                                                                                                                                                                                                                                                                                                                                 | Returns `true` if scalar or vector component is `INF`.              |
|                                                         | floatBitsToInt( x)                                                                                                                                                                                                                                                                                                                               | `float` to `int` bit copying, no conversion.                        |
|                                                         | floatBitsToUint( x)                                                                                                                                                                                                                                                                                                                             | `float` to `uint` bit copying, no conversion.                       |
|                                                         | intBitsToFloat( x)                                                                                                                                                                                                                                                                                                                               | `int` to `float` bit copying, no conversion.                        |
|                                                         | uintBitsToFloat( x)                                                                                                                                                                                                                                                                                                                             | `uint` to `float` bit copying, no conversion.                       |

### Exponential and math function descriptions

 **pow**( x,  y)

> Component-wise Function.

> Raises `x` to the power of `y`.

> The result is undefined if `x < 0` or  if `x == 0` and `y <= 0`.

> * **param x:**
>   The value to be raised to the power `y`.
> * **param y:**
>   The power to which `x` will be raised.
> * **return:**
>   The value of `x` raised to the `y` power.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/pow.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/pow.xhtml)

---

 **exp**( x)

> Component-wise Function.

> Raises `e` to the power of `x`, or the the natural exponentiation.

> Equivalent to `pow(e, x)`.

> * **param x:**
>   The value to exponentiate.
> * **return:**
>   The natural exponentiation of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp.xhtml)

---

 **exp2**( x)

> Component-wise Function.

> Raises `2` to the power of `x`.

> Equivalent to `pow(2.0, x)`.

> * **param x:**
>   The value of the power to which `2` will be raised.
> * **return:**
>   `2` raised to the power of x.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp2.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp2.xhtml)

---

 **log**( x)

> Component-wise Function.

> Returns the natural logarithm of `x`, i.e. the value `y` which satisfies `x == pow(e, y)`.
> The result is undefined if `x <= 0`.

> * **param x:**
>   The value of which to take the natural logarithm.
> * **return:**
>   The natural logarithm of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log.xhtml)

---

 **log2**( x)

> Component-wise Function.

> Returns the base-2 logarithm of `x`, i.e. the value `y` which satisfies `x == pow(2, y)`.
> The result is undefined if `x <= 0`.

> * **param x:**
>   The value of which to take the base-2 logarithm.
> * **return:**
>   The base-2 logarithm of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log2.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log2.xhtml)

---

 **sqrt**( x)

> Component-wise Function.

> Returns the square root of `x`.
> The result is undefined if `x < 0`.

> * **param x:**
>   The value of which to take the square root.
> * **return:**
>   The square root of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sqrt.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sqrt.xhtml)

---

 **inversesqrt**( x)

> Component-wise Function.

> Returns the inverse of the square root of `x`, or `1.0 / sqrt(x)`.
> The result is undefined if `x <= 0`.

> * **param x:**
>   The value of which to take the inverse of the square root.
> * **return:**
>   The inverse of the square root of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inversesqrt.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inversesqrt.xhtml)

---

 **abs**( x)

 **abs**( x)

> Component-wise Function.

> Returns the absolute value of `x`. Returns `x` if `x` is positive, otherwise returns `-1 * x`.

> * **param x:**
>   The value of which to return the absolute.
> * **return:**
>   The absolute value of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/abs.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/abs.xhtml)

---

 **sign**( x)

 **sign**( x)

> Component-wise Function.

> Returns `-1` if `x < 0`, `0` if `x == 0`, and `1` if `x > 0`.

> * **param x:**
>   The value from which to extract the sign.
> * **return:**
>   The sign of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sign.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sign.xhtml)

---

 **floor**( x)

> Component-wise Function.

> Returns a value equal to the nearest integer that is less than or equal to `x`.

> * **param x:**
>   The value to floor.
> * **return:**
>   The nearest integer that is less than or equal to `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floor.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floor.xhtml)

---

 **round**( x)

> Component-wise Function.

> Rounds `x` to the nearest integer.

> #### NOTE
> Rounding of values with a fractional part of `0.5` is implementation-dependent.
> This includes the possibility that `round(x)` returns the same value as
> `roundEven(x)``for all values of ``x`.

> * **param x:**
>   The value to round.
> * **return:**
>   The rounded value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/round.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/round.xhtml)

---

 **roundEven**( x)

> Component-wise Function.

> Rounds `x` to the nearest integer. A value with a fractional part of `0.5`
> will always round toward the nearest even integer.
> For example, both `3.5` and `4.5` will round to `4.0`.

> * **param x:**
>   The value to round.
> * **return:**
>   The rounded value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/roundEven.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/roundEven.xhtml)

---

 **trunc**( x)

> Component-wise Function.

> Truncates `x`. Returns a value equal to the nearest integer to `x` whose
> absolute value is not larger than the absolute value of `x`.

> * **param x:**
>   The value to evaluate.
> * **return:**
>   The truncated value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/trunc.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/trunc.xhtml)

---

 **ceil**( x)

> Component-wise Function.

> Returns a value equal to the nearest integer that is greater than or equal to `x`.

> * **param x:**
>   The value to evaluate.
> * **return:**
>   The ceiling-ed value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ceil.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ceil.xhtml)

---

 **fract**( x)

> Component-wise Function.

> Returns the fractional part of `x`.

> This is calculated as `x - floor(x)`.

> * **param x:**
>   The value to evaluate.
> * **return:**
>   The fractional part of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fract.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fract.xhtml)

---

 **mod**( x,  y)

 **mod**( x, float y)

> Component-wise Function.

> Returns the value of `x modulo y`.
> This is also sometimes called the remainder.

> This is computed as `x - y * floor(x/y)`.

> * **param x:**
>   The value to evaluate.
> * **return:**
>   The value of `x modulo y`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mod.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mod.xhtml)

---

 **modf**( x, out  i)

> Component-wise Function.

> Separates a floating-point value `x` into its integer and fractional parts.

> The fractional part of the number is returned from the function.
> The integer part (as a floating-point quantity) is returned in the output parameter `i`.

> * **param x:**
>   The value to separate.
> * **param out i:**
>   A variable that receives the integer part of `x`.
> * **return:**
>   The fractional part of the number.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/modf.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/modf.xhtml)

---

 **min**( a,  b)

 **min**( a, float b)

 **min**( a,  b)

 **min**( a, int b)

 **min**( a,  b)

 **min**( a, uint b)

> Component-wise Function.

> Returns the minimum of two values `a` and `b`.

> Returns `b` if `b < a`, otherwise returns `a`.

> * **param a:**
>   The first value to compare.
> * **param b:**
>   The second value to compare.
> * **return:**
>   The minimum value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml)

---

 **max**( a,  b)

 **max**( a, float b)

 **max**( a,  b)

 **max**( a, uint b)

 **max**( a,  b)

 **max**( a, int b)

> Component-wise Function.

> Returns the maximum of two values `a` and `b`.

> It returns `b` if `b > a`, otherwise it returns `a`.

> * **param a:**
>   The first value to compare.
> * **param b:**
>   The second value to compare.
> * **return:**
>   The maximum value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml)

---

 **clamp**( x,  minVal,  maxVal)

 **clamp**( x, float minVal, float maxVal)

 **clamp**( x,  minVal,  maxVal)

 **clamp**( x, int minVal, int maxVal)

 **clamp**( x,  minVal,  maxVal)

 **clamp**( x, uint minVal, uint maxVal)

> Component-wise Function.

> Returns the value of `x` constrained to the range `minVal` to `maxVal`.

> The returned value is computed as `min(max(x, minVal), maxVal)`.

> * **param x:**
>   The value to constrain.
> * **param minVal:**
>   The lower end of the range into which to constrain `x`.
> * **param maxVal:**
>   The upper end of the range into which to constrain `x`.
> * **return:**
>   The clamped value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml)

---

 **mix**( a,  b,  c)

 **mix**( a,  b, float c)

> Component-wise Function.

> Performs a linear interpolation between `a` and `b` using `c` to weight between them.

> Computed as `a * (1 - c) + b * c`.

> Equivalent to [lerp()](../../../classes/class_@globalscope.md#class-globalscope-method-lerp) in GDScript.

> * **param a:**
>   The start of the range in which to interpolate.
> * **param b:**
>   The end of the range in which to interpolate.
> * **param c:**
>   The value to use to interpolate between `a` and `b`.
> * **return:**
>   The interpolated value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml)

---

 **mix**( a,  b,  c)

> Selects either value `a` or value `b` based on the value of `c`.
> For a component of `c` that is false, the corresponding component of `a` is returned.
> For a component of `c` that is true, the corresponding component of `b` is returned.
> Components of `a` and `b` that are not selected are allowed to be invalid floating-point values and will have no effect on the results.

> If `a`, `b`, and `c` are vector types the operation is performed component-wise.
> ie. `mix(vec2(42, 314), vec2(9.8, 6e23), bvec2(true, false)))` will return `vec2(9.8, 314)`.

> * **param a:**
>   Value returned when `c` is false.
> * **param b:**
>   Value returned when `c` is true.
> * **param c:**
>   The value used to select between `a` and `b`.
> * **return:**
>   The interpolated value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml)

---

 **fma**( a,  b,  c)

> Component-wise Function.

> Performs, where possible, a fused multiply-add operation, returning `a * b + c`. In use cases where the
> return value is eventually consumed by a variable declared as precise:

> > - `fma()` is considered a single operation, whereas the expression `a * b + c` consumed by a variable declared as precise is considered two operations.
> > - The precision of `fma()` can differ from the precision of the expression `a * b + c`.
> > - `fma()` will be computed with the same precision as any other `fma()` consumed by a precise variable,
> >   giving invariant results for the same input values of a, b and c.

> Otherwise, in the absence of precise consumption, there are no special constraints on the number of operations
> or difference in precision between `fma()` and the expression `a * b + c`.

> * **param a:**
>   The first value to be multiplied.
> * **param b:**
>   The second value to be multiplied.
> * **param c:**
>   The value to be added to the result.
> * **return:**
>   The value of `a * b + c`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fma.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fma.xhtml)

---

 **step**( a,  b)

 **step**(float a,  b)

> Component-wise Function.

> Generates a step function by comparing b to a.

> Equivalent to `if (b < a) { return 0.0; } else { return 1.0; }`.
> For element i of the return value, 0.0 is returned if b[i] < a[i], and 1.0 is returned otherwise.

> * **param a:**
>   The location of the edge of the step function.
> * **param b:**
>   The value to be used to generate the step function.
> * **return:**
>   `0.0` or `1.0`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/step.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/step.xhtml)

---

 **smoothstep**( a,  b,  c)

 **smoothstep**(float a, float b,  c)

> Component-wise Function.

> Performs smooth Hermite interpolation between `0` and `1` when a < c < b.
> This is useful in cases where a threshold function with a smooth transition is desired.

> Smoothstep is equivalent to:

> ```gdscript
> vec_type t;
> t = clamp((c - a) / (b - a), 0.0, 1.0);
> return t * t * (3.0 - 2.0 * t);
> ```

> Results are undefined if `a >= b`.

> * **param a:**
>   The value of the lower edge of the Hermite function.
> * **param b:**
>   The value of the upper edge of the Hermite function.
> * **param c:**
>   The source value for interpolation.
> * **return:**
>   The interpolated value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/smoothstep.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/smoothstep.xhtml)

---

 **isnan**( x)

> Component-wise Function.

> For each element i of the result, returns `true` if x[i] is positive
> or negative floating-point NaN (Not a Number) and false otherwise.

> * **param x:**
>   The value to test for NaN.
> * **return:**
>   `true` or `false`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isnan.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isnan.xhtml)

---

 **isinf**( x)

> Component-wise Function.

> For each element i of the result, returns `true` if x[i] is positive or negative
> floating-point infinity and false otherwise.

> * **param x:**
>   The value to test for infinity.
> * **return:**
>   `true` or `false`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isinf.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isinf.xhtml)

---

 **floatBitsToInt**( x)

> Component-wise Function.

> Returns the encoding of the floating-point parameters as `int`.

> The floating-point bit-level representation is preserved.

> * **param x:**
>   The value whose floating-point encoding to return.
> * **return:**
>   The floating-point encoding of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml)

---

 **floatBitsToUint**( x)

> Component-wise Function.

> Returns the encoding of the floating-point parameters as `uint`.

> The floating-point bit-level representation is preserved.

> * **param x:**
>   The value whose floating-point encoding to return.
> * **return:**
>   The floating-point encoding of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml)

---

 **intBitsToFloat**( x)

> Component-wise Function.

> Converts a bit encoding to a floating-point value. Opposite of floatBitsToInt<shader_func_floatBitsToInt>

> If the encoding of a `NaN` is passed in `x`, it will not signal and the resulting value will be undefined.

> If the encoding of a floating-point infinity is passed in parameter `x`, the resulting floating-point value is
> the corresponding (positive or negative) floating-point infinity.

> * **param x:**
>   The bit encoding to return as a floating-point value.
> * **return:**
>   A floating-point value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml)

---

 **uintBitsToFloat**( x)

> Component-wise Function.

> Converts a bit encoding to a floating-point value. Opposite of floatBitsToUint<shader_func_floatBitsToUint>

> If the encoding of a `NaN` is passed in `x`, it will not signal and the resulting value will be undefined.

> If the encoding of a floating-point infinity is passed in parameter `x`, the resulting floating-point value is
> the corresponding (positive or negative) floating-point infinity.

> * **param x:**
>   The bit encoding to return as a floating-point value.
> * **return:**
>   A floating-point value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml)

---

## Geometric functions

| float   | length( x)                          | Vector length.                                     |
|---------|------------------------------------------------------------|----------------------------------------------------|
| float   | distance( a,  b)                  | Distance between vectors i.e `length(a - b)`.      |
| float   | dot( a,  b)                            | Dot product.                                       |
| vec3    | cross(vec3 a, vec3 b)                | Cross product.                                     |
|         | normalize( x)                    | Normalize to unit length.                          |
| vec3    | reflect(vec3 I, vec3 N)            | Reflect.                                           |
| vec3    | refract(vec3 I, vec3 N, float eta) | Refract.                                           |
|         | faceforward( N,  I,  Nref)     | If `dot(Nref, I)` < 0, return `N`, otherwise `-N`. |
|         | matrixCompMult( x,  y)      | Matrix component multiplication.                   |
|         | outerProduct( column,  row)   | Matrix outer product.                              |
|         | transpose( m)                    | Transpose matrix.                                  |
| float   | determinant( m)                | Matrix determinant.                                |
|         | inverse( m)                        | Inverse matrix.                                    |

### Geometric function descriptions

float **length**( x)

> Returns the length of the vector.
> ie. `sqrt(x[0] * x[0] + x[1] * x[1] + ... + x[n] * x[n])`

> * **param x:**
>   The vector
> * **return:**
>   The length of the vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/length.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/length.xhtml)

---

float **distance**( a,  b)

> Returns the distance between the two points a and b.

> i.e., `length(b - a);`

> * **param a:**
>   The first point.
> * **param b:**
>   The second point.
> * **return:**
>   The scalar distance between the points

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/distance.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/distance.xhtml)

---

float **dot**( a,  b)

> Returns the dot product of two vectors, `a` and `b`.
> i.e., `a.x * b.x + a.y * b.y + ...`

> * **param a:**
>   The first vector.
> * **param b:**
>   The second vector.
> * **return:**
>   The dot product.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dot.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dot.xhtml)

---

vec3 **cross**(vec3 a, vec3 b)

> Returns the cross product of two vectors. i.e.:

> ```glsl
> vec2( a.y * b.z - b.y * a.z,
>       a.z * b.x - b.z * a.x,
>       a.x * b.z - b.x * a.y)
> ```

> * **param a:**
>   The first vector.
> * **param b:**
>   The second vector.
> * **return:**
>   The cross product of `a` and `b`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cross.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cross.xhtml)

---

 **normalize**( x)

> Returns a vector with the same direction as `x` but with length `1.0`.

> * **param x:**
>   The vector to normalize.
> * **return:**
>   The normalized vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/normalize.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/normalize.xhtml)

---

vec3 **reflect**(vec3 I, vec3 N)

> Calculate the reflection direction for an incident vector.

> For a given incident vector `I` and surface normal `N` reflect returns the reflection direction calculated as `I - 2.0 * dot(N, I) * N`.

> #### NOTE
> `N` should be normalized in order to achieve the desired result.

> * **param I:**
>   The incident vector.
> * **param N:**
>   The normal vector.
> * **return:**
>   The reflection vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/reflect.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/reflect.xhtml)

---

vec3 **refract**(vec3 I, vec3 N, float eta)

> Calculate the refraction direction for an incident vector.

> For a given incident vector `I`, surface normal `N` and ratio of indices of refraction, `eta`, refract returns the refraction vector, `R`.

> `R` is calculated as:

> ```glsl
> k = 1.0 - eta * eta * (1.0 - dot(N, I) * dot(N, I));
> if (k < 0.0)
>     R = genType(0.0);       // or genDType(0.0)
> else
>     R = eta * I - (eta * dot(N, I) + sqrt(k)) * N;
> ```

> #### NOTE
> The input parameters I and N should be normalized in order to achieve the desired result.

> * **param I:**
>   The incident vector.
> * **param N:**
>   The normal vector.
> * **param eta:**
>   The ratio of indices of refraction.
> * **return:**
>   The refraction vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/refract.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/refract.xhtml)

---

 **faceforward**( N,  I,  Nref)

> Returns a vector pointing in the same direction as another.

> Orients a vector to point away from a surface as defined by its normal.
> If `dot(Nref, I) < 0` faceforward returns `N`, otherwise it returns `-N`.

> * **param N:**
>   The vector to orient.
> * **param I:**
>   The incident vector.
> * **param Nref:**
>   The reference vector.
> * **return:**
>   The oriented vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/faceforward.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/faceforward.xhtml)

---

 **matrixCompMult**( x,  y)

> Perform a component-wise multiplication of two matrices.

> Performs a component-wise multiplication of two matrices, yielding a result
> matrix where each component, `result[i][j]` is computed as the scalar
> product of `x[i][j]` and `y[i][j]`.

> * **param x:**
>   The first matrix multiplicand.
> * **param y:**
>   The second matrix multiplicand.
> * **return:**
>   The resultant matrix.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/matrixCompMult.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/matrixCompMult.xhtml)

---

 **outerProduct**( column,  row)

> Calculate the outer product of a pair of vectors.

> Does a linear algebraic matrix multiply `column * row`, yielding a matrix whose number of
> rows is the number of components in `column` and whose number of columns is the number of
> components in `row`.

> * **param column:**
>   The column vector for multiplication.
> * **param row:**
>   The row vector for multiplication.
> * **return:**
>   The outer product matrix.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/outerProduct.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/outerProduct.xhtml)

---

 **transpose**( m)

> Calculate the transpose of a matrix.

> * **param m:**
>   The matrix to transpose.
> * **return:**
>   A new matrix that is the transpose of the input matrix `m`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/transpose.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/transpose.xhtml)

---

float **determinant**( m)

> Calculate the determinant of a matrix.

> * **param m:**
>   The matrix.
> * **return:**
>   The determinant of the input matrix `m`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/determinant.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/determinant.xhtml)

---

 **inverse**( m)

> Calculate the inverse of a matrix.

> The values in the returned matrix are undefined if `m` is singular or poorly-conditioned (nearly singular).

> * **param m:**
>   The matrix of which to take the inverse.
> * **return:**
>   A new matrix which is the inverse of the input matrix `m`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inverse.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inverse.xhtml)

---

## Comparison functions

|      | lessThan( x,  y)                  | Bool vector comparison on < int/uint/float vectors.     |
|------|------------------------------------------------------------|---------------------------------------------------------|
|      | greaterThan( x,  y)            | Bool vector comparison on > int/uint/float vectors.     |
|      | lessThanEqual( x,  y)        | Bool vector comparison on <= int/uint/float vectors.    |
|      | greaterThanEqual(  x,  y) | Bool vector comparison on >= int/uint/float vectors.    |
|      | equal( x,  y)                        | Bool vector comparison on == int/uint/float vectors.    |
|      | notEqual( x,  y)                  | Bool vector comparison on != int/uint/float vectors.    |
| bool | any( x)                                | `true` if any component is `true`, `false` otherwise.   |
| bool | all( x)                                | `true` if all components are `true`, `false` otherwise. |
|      | not( x)                                | Invert boolean vector.                                  |

### Comparison function descriptions

 **lessThan**( x,  y)

> Performs a component-wise less-than comparison of two vectors.

> * **param x:**
>   The first vector to compare.
> * **param y:**
>   The second vector to compare.
> * **return:**
>   A boolean vector in which each element `i` is computed as `x[i] < y[i]`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThan.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThan.xhtml)

---

 **greaterThan**( x,  y)

> Performs a component-wise greater-than comparison of two vectors.

> * **param x:**
>   The first vector to compare.
> * **param y:**
>   The second vector to compare.
> * **return:**
>   A boolean vector in which each element `i` is computed as `x[i] > y[i]`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThan.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThan.xhtml)

---

 **lessThanEqual**( x,  y)

> Performs a component-wise less-than-or-equal comparison of two vectors.

> * **param x:**
>   The first vector to compare.
> * **param y:**
>   The second vector to compare.
> * **return:**
>   A boolean vector in which each element `i` is computed as `x[i] <= y[i]`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThanEqual.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThanEqual.xhtml)

---

 **greaterThanEqual**( x,  y)

> Performs a component-wise greater-than-or-equal comparison of two vectors.

> * **param x:**
>   The first vector to compare.
> * **param y:**
>   The second vector to compare.
> * **return:**
>   A boolean vector in which each element `i` is computed as `x[i] >= y[i]`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThanEqual.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThanEqual.xhtml)

---

 **equal**( x,  y)

> Performs a component-wise equal-to comparison of two vectors.

> * **param x:**
>   The first vector to compare.
> * **param y:**
>   The second vector to compare.
> * **return:**
>   A boolean vector in which each element `i` is computed as `x[i] == y[i]`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/equal.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/equal.xhtml)

---

 **notEqual**( x,  y)

> Performs a component-wise not-equal-to comparison of two vectors.

> * **param x:**
>   The first vector for comparison.
> * **param y:**
>   The second vector for comparison.
> * **return:**
>   A boolean vector in which each element `i` is computed as `x[i] != y[i]`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/notEqual.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/notEqual.xhtml)

---

bool **any**( x)

> Returns `true` if any element of a boolean vector is `true`, `false` otherwise.

> Functionally equivalent to:

> ```gdscript
> bool any(bvec x) {     // bvec can be bvec2, bvec3 or bvec4
>     bool result = false;
>     int i;
>     for (i = 0; i < x.length(); ++i) {
>         result |= x[i];
>     }
>     return result;
> }
> ```

> * **param x:**
>   The vector to be tested for truth.
> * **return:**
>   True if any element of x is true and false otherwise.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/any.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/any.xhtml)

---

bool **all**( x)

> Returns `true` if all elements of a boolean vector are `true`, `false` otherwise.

> Functionally equivalent to:

> ```gdscript
> bool all(bvec x)       // bvec can be bvec2, bvec3 or bvec4
> {
>     bool result = true;
>     int i;
>     for (i = 0; i < x.length(); ++i)
>     {
>         result &= x[i];
>     }
>     return result;
> }
> ```

> * **param x:**
>   The vector to be tested for truth.
> * **return:**
>   `true` if all elements of `x` are `true` and `false` otherwise.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/all.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/all.xhtml)

---

 **not**( x)

> Logically invert a boolean vector.

> * **param x:**
>   The vector to be inverted.
> * **return:**
>   A new boolean vector for which each element i is computed as !x[i].

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/not.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/not.xhtml)

---

## Texture functions

| ivec2<br/><br/><br/>ivec2<br/><br/><br/>ivec2<br/><br/><br/>ivec3<br/><br/><br/>ivec3<br/><br/>   | textureSize( s, int lod)<br/><br/><br/>textureSize(samplerCube s, int lod)<br/><br/><br/>textureSize(samplerCubeArray s, int lod)<br/><br/><br/>textureSize( s, int lod)<br/><br/><br/>textureSize( s, int lod)<br/><br/>                                                                                                                                | Get the size of a texture.<br/><br/>For performance reasons, this function should be avoided as it<br/>always performs a full texture read. When possible, you should pass<br/>the texture size as a uniform instead.   |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vec2<br/><br/><br/>vec3<br/><br/><br/>vec2<br/><br/><br/>vec2<br/><br/>                           | textureQueryLod( s, vec2 p)<br/><br/><br/>textureQueryLod( s, vec2 p)<br/><br/><br/>textureQueryLod( s, vec3 p)<br/><br/><br/>textureQueryLod(samplerCube s, vec3 p)<br/><br/>                                                                                                                                                                                       | Compute the level-of-detail that would be used to sample from a<br/>texture.                                                                                                                                            |
| int<br/><br/><br/>int<br/><br/><br/>int<br/><br/><br/>int<br/><br/>                               | textureQueryLevels( s)<br/><br/><br/>textureQueryLevels( s)<br/><br/><br/>textureQueryLevels( s)<br/><br/><br/>textureQueryLevels(samplerCube s)<br/><br/>                                                                                                                                                                                               | Get the number of accessible mipmap levels of a texture.                                                                                                                                                                |
| <br/><br/><br/><br/><br/><br/>vec4<br/><br/><br/>vec4<br/><br/><br/>vec4<br/><br/>                | texture( s, vec2 p [, float bias] )<br/><br/><br/>texture( s, vec3 p [, float bias] )<br/><br/><br/>texture( s, vec3 p [, float bias] )<br/><br/><br/>texture(samplerCube s, vec3 p [, float bias] )<br/><br/><br/>texture(samplerCubeArray s, vec4 p [, float bias] )<br/><br/><br/>texture(samplerExternalOES s, vec2 p [, float bias] )<br/><br/> | Performs a texture read.                                                                                                                                                                                                |
| <br/><br/><br/><br/><br/>                                                                         | textureProj( s, vec3 p [, float bias] )<br/><br/><br/>textureProj( s, vec4 p [, float bias] )<br/><br/><br/>textureProj( s, vec4 p [, float bias] )<br/><br/>                                                                                                                                                                                                                                                    | Performs a texture read with projection.                                                                                                                                                                                |
| <br/><br/><br/><br/><br/><br/>vec4<br/><br/><br/>vec4<br/><br/>                                   | textureLod( s, vec2 p, float lod)<br/><br/><br/>textureLod( s, vec3 p, float lod)<br/><br/><br/>textureLod( s, vec3 p, float lod)<br/><br/><br/>textureLod(samplerCube s, vec3 p, float lod)<br/><br/><br/>textureLod(samplerCubeArray s, vec4 p, float lod)<br/><br/>                                                                                        | Performs a texture read at custom mipmap.                                                                                                                                                                               |
| <br/><br/><br/><br/><br/>                                                                         | textureProjLod( s, vec3 p, float lod)<br/><br/><br/>textureProjLod( s, vec4 p, float lod)<br/><br/><br/>textureProjLod( s, vec4 p, float lod)<br/><br/>                                                                                                                                                                                                                                                 | Performs a texture read with projection/LOD.                                                                                                                                                                            |
| <br/><br/><br/><br/><br/><br/>vec4<br/><br/><br/>vec4<br/><br/>                                   | textureGrad( s, vec2 p, vec2 dPdx, vec2 dPdy)<br/><br/><br/>textureGrad( s, vec3 p, vec2 dPdx, vec2 dPdy)<br/><br/><br/>textureGrad( s, vec3 p, vec2 dPdx, vec2 dPdy)<br/><br/><br/>textureGrad(samplerCube s, vec3 p, vec3 dPdx, vec3 dPdy)<br/><br/><br/>textureGrad(samplerCubeArray s, vec3 p, vec3 dPdx, vec3 dPdy)<br/><br/>                       | Performs a texture read with explicit gradients.                                                                                                                                                                        |
| <br/><br/><br/><br/><br/>                                                                         | textureProjGrad( s, vec3 p, vec2 dPdx, vec2 dPdy)<br/><br/><br/>textureProjGrad( s, vec4 p, vec2 dPdx, vec2 dPdy)<br/><br/><br/>textureProjGrad( s, vec4 p, vec3 dPdx, vec3 dPdy)<br/><br/>                                                                                                                                                                                                          | Performs a texture read with projection/LOD and with explicit                                                                                                                                                           |
| <br/><br/><br/><br/><br/>                                                                         | texelFetch( s, ivec2 p, int lod)<br/><br/><br/>texelFetch( s, ivec3 p, int lod)<br/><br/><br/>texelFetch( s, ivec3 p, int lod)<br/><br/>                                                                                                                                                                                                                                                                            | Fetches a single texel using integer coordinates.                                                                                                                                                                       |
| <br/><br/><br/><br/>vec4<br/><br/>                                                                | textureGather( s, vec2 p [, int comps] )<br/><br/><br/>textureGather( s, vec3 p [, int comps] )<br/><br/><br/>textureGather(samplerCube s, vec3 p [, int comps] )<br/><br/>                                                                                                                                                                                                                                | Gathers four texels from a texture.                                                                                                                                                                                     |
|                                                                                                   | dFdx( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Derivative with respect to `x` window coordinate,<br/>automatic granularity.                                                                                                                                            |
|                                                                                                   | dFdxCoarse( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Derivative with respect to `x` window coordinate,<br/>course granularity.<br/><br/>Not available when using the Compatibility renderer.                                                                                 |
|                                                                                                   | dFdxFine( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Derivative with respect to `x` window coordinate,<br/>fine granularity.<br/><br/>Not available when using the Compatibility renderer.                                                                                   |
|                                                                                                   | dFdy( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Derivative with respect to `y` window coordinate,<br/>automatic granularity.                                                                                                                                            |
|                                                                                                   | dFdyCoarse( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Derivative with respect to `y` window coordinate,<br/>course granularity.<br/><br/>Not available when using the Compatibility renderer.                                                                                 |
|                                                                                                   | dFdyFine( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Derivative with respect to `y` window coordinate,<br/>fine granularity.<br/><br/>Not available when using the Compatibility renderer.                                                                                   |
|                                                                                                   | fwidth( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Sum of absolute derivative in `x` and `y`.                                                                                                                                                                              |
|                                                                                                   | fwidthCoarse( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Sum of absolute derivative in `x` and `y`.<br/><br/>Not available when using the Compatibility renderer.                                                                                                                |
|                                                                                                   | fwidthFine( p)                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Sum of absolute derivative in `x` and `y`.<br/><br/>Not available when using the Compatibility renderer.                                                                                                                |

### Texture function descriptions

ivec2 **textureSize**( s, int lod)

ivec2 **textureSize**(samplerCube s, int lod)

ivec2 **textureSize**(samplerCubeArray s, int lod)

ivec3 **textureSize**( s, int lod)

ivec3 **textureSize**( s, int lod)

> Retrieves the dimensions of a level of a texture.

> Returns the dimensions of level `lod` (if present) of the texture bound to sampler.

> The components in the return value are filled in, in order, with the width, height and depth
> of the texture. For the array forms, the last component of the return value is
> the number of layers in the texture array.

> * **param s:**
>   The sampler to which the texture whose dimensions to retrieve is bound.
> * **param lod:**
>   The level of the texture for which to retrieve the dimensions.
> * **return:**
>   The dimensions of level `lod` (if present) of the texture bound to sampler.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureSize.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureSize.xhtml)

---

vec2 **textureQueryLod**( s, vec2 p)

vec2 **textureQueryLod**( s, vec2 p)

vec2 **textureQueryLod**( s, vec3 p)

vec2 **textureQueryLod**(samplerCube s, vec3 p)

> #### NOTE
> Available only in the fragment shader.

> Compute the level-of-detail that would be used to sample from a texture.

> The mipmap array(s) that would be accessed is returned in the x component of
> the return value. The computed level-of-detail relative to the base level is
> returned in the y component of the return value.

> If called on an incomplete texture, the result of the operation is undefined.

> * **param s:**
>   The sampler to which the texture whose level-of-detail will be queried is bound.
> * **param p:**
>   The texture coordinates at which the level-of-detail will be queried.
> * **return:**
>   See description.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLod.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLod.xhtml)

---

int **textureQueryLevels**( s)

int **textureQueryLevels**( s)

int **textureQueryLevels**( s)

int **textureQueryLevels**(samplerCube s)

> Compute the number of accessible mipmap levels of a texture.

> If called on an incomplete texture, or if no texture is associated with sampler, `0` is returned.

> * **param s:**
>   The sampler to which the texture whose mipmap level count will be queried is bound.
> * **return:**
>   The number of accessible mipmap levels in the texture, or `0`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLevels.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLevels.xhtml)

---

 **texture**( s, vec2 p [, float bias] )

 **texture**( s, vec3 p [, float bias] )

 **texture**( s, vec3 p [, float bias] )

vec4 **texture**(samplerCube s, vec3 p [, float bias] )

vec4 **texture**(samplerCubeArray s, vec4 p [, float bias] )

vec4 **texture**(samplerExternalOES s, vec2 p [, float bias] )

> Retrieves texels from a texture.

> Samples texels from the texture bound to `s` at texture coordinate `p`. An optional bias, specified in `bias` is
> included in the level-of-detail computation that is used to choose mipmap(s) from which to sample.

> For shadow forms, the last component of `p` is used as Dsub and the array layer is specified in the second to last
> component of `p`. (The second component of `p` is unused for 1D shadow lookups.)

> For non-shadow variants, the array layer comes from the last component of P.

> * **param s:**
>   The sampler to which the texture from which texels will be retrieved is bound.
> * **param p:**
>   The texture coordinates at which texture will be sampled.
> * **param bias:**
>   An optional bias to be applied during level-of-detail computation.
> * **return:**
>   A texel.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texture.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texture.xhtml)

---

 **textureProj**( s, vec3 p [, float bias] )

 **textureProj**( s, vec4 p [, float bias] )

 **textureProj**( s, vec4 p [, float bias] )

> Perform a texture lookup with projection.

> The texture coordinates consumed from `p`, not including the last component of `p`, are
> divided by the last component of `p`. The resulting 3rd component of `p` in the shadow
> forms is used as Dref. After these values are computed, the texture lookup proceeds as in texture.

> * **param s:**
>   The sampler to which the texture from which texels will be retrieved is bound.
> * **param p:**
>   The texture coordinates at which texture will be sampled.
> * **param bias:**
>   Optional bias to be applied during level-of-detail computation.
> * **return:**
>   A texel.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProj.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProj.xhtml)

---

 **textureLod**( s, vec2 p, float lod)

 **textureLod**( s, vec3 p, float lod)

 **textureLod**( s, vec3 p, float lod)

vec4 **textureLod**(samplerCube s, vec3 p, float lod)

vec4 **textureLod**(samplerCubeArray s, vec4 p, float lod)

> Performs a texture lookup at coordinate `p` from the texture bound to sampler with
> an explicit level-of-detail as specified in `lod`. `lod` specifies λbase and sets the
> partial derivatives as follows:

> ```gdscript
> δu/δx=0, δv/δx=0, δw/δx=0
> δu/δy=0, δv/δy=0, δw/δy=0
> ```

> * **param s:**
>   The sampler to which the texture from which texels will be retrieved is bound.
> * **param p:**
>   The texture coordinates at which texture will be sampled.
> * **param lod:**
>   The explicit level-of-detail.
> * **return:**
>   A texel.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureLod.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureLod.xhtml)

---

 **textureProjLod**( s, vec3 p, float lod)

 **textureProjLod**( s, vec4 p, float lod)

 **textureProjLod**( s, vec4 p, float lod)

> Performs a texture lookup with projection from an explicitly specified level-of-detail.

> The texture coordinates consumed from P, not including the last component of `p`, are
> divided by the last component of `p`. The resulting 3rd component of `p` in the shadow
> forms is used as Dref. After these values are computed, the texture lookup proceeds as in
> textureLod<shader_func_textureLod>, with `lod` used to specify the level-of-detail from
> which the texture will be sampled.

> * **param s:**
>   The sampler to which the texture from which texels will be retrieved is bound.
> * **param p:**
>   The texture coordinates at which texture will be sampled.
> * **param lod:**
>   The explicit level-of-detail from which to fetch texels.
> * **return:**
>   a texel

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjLod.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjLod.xhtml)

---

 **textureGrad**( s, vec2 p, vec2 dPdx, vec2 dPdy)

 **textureGrad**( s, vec3 p, vec2 dPdx, vec2 dPdy)

 **textureGrad**( s, vec3 p, vec2 dPdx, vec2 dPdy)

vec4 **textureGrad**(samplerCube s, vec3 p, vec3 dPdx, vec3 dPdy)

vec4 **textureGrad**(samplerCubeArray s, vec3 p, vec3 dPdx, vec3 dPdy)

> Performs a texture lookup at coordinate `p` from the texture bound to sampler with explicit texture coordinate gradiends as specified in `dPdx` and `dPdy`. Set:
> : - `δs/δx=δp/δx` for a 1D texture, `δp.s/δx` otherwise
>   - `δs/δy=δp/δy` for a 1D texture, `δp.s/δy` otherwise
>   - `δt/δx=0.0` for a 1D texture, `δp.t/δx` otherwise
>   - `δt/δy=0.0` for a 1D texture, `δp.t/δy` otherwise
>   - `δr/δx=0.0` for a 1D or 2D texture, `δp.p/δx` otherwise
>   - `δr/δy=0.0`  for a 1D or 2D texture, `δp.p/δy` otherwise

> For the cube version, the partial derivatives of `p` are assumed to be in the coordinate system used before texture coordinates are projected onto the appropriate cube face.

> * **param s:**
>   The sampler to which the texture from which texels will be retrieved is bound.
> * **param p:**
>   The texture coordinates at which texture will be sampled.
> * **param dPdx:**
>   The partial derivative of P with respect to window x.
> * **param dPdy:**
>   The partial derivative of P with respect to window y.
> * **return:**
>   A texel.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGrad.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGrad.xhtml)

---

 **textureProjGrad**( s, vec3 p, vec2 dPdx, vec2 dPdy)

 **textureProjGrad**( s, vec4 p, vec2 dPdx, vec2 dPdy)

 **textureProjGrad**( s, vec4 p, vec3 dPdx, vec3 dPdy)

> Perform a texture lookup with projection and explicit gradients.

> The texture coordinates consumed from `p`, not including the last component of `p`, are divided by the last component of `p`.
> After these values are computed, the texture lookup proceeds as in textureGrad<shader_func_textureGrad>, passing `dPdx` and `dPdy` as gradients.

> * **param s:**
>   The sampler to which the texture from which texels will be retrieved is bound.
> * **param p:**
>   The texture coordinates at which texture will be sampled.
> * **param dPdx:**
>   The partial derivative of `p` with respect to window x.
> * **param dPdy:**
>   The partial derivative of `p` with respect to window y.
> * **return:**
>   A texel.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjGrad.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjGrad.xhtml)

---

 **texelFetch**( s, ivec2 p, int lod)

 **texelFetch**( s, ivec3 p, int lod)

 **texelFetch**( s, ivec3 p, int lod)

> Performs a lookup of a single texel from texture coordinate `p` in the texture bound to sampler.

> * **param s:**
>   The sampler to which the texture from which texels will be retrieved is bound.
> * **param p:**
>   The texture coordinates at which texture will be sampled.
> * **param lod:**
>   Specifies the level-of-detail within the texture from which the texel will be fetched.
> * **return:**
>   A texel.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texelFetch.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texelFetch.xhtml)

---

 **textureGather**( s, vec2 p [, int comps] )

 **textureGather**( s, vec3 p [, int comps] )

vec4 **textureGather**(samplerCube s, vec3 p [, int comps] )

> Gathers four texels from a texture.

> Returns the value:

> ```gdscript
> vec4(Sample_i0_j1(p, base).comps,
>      Sample_i1_j1(p, base).comps,
>      Sample_i1_j0(p, base).comps,
>      Sample_i0_j0(p, base).comps);
> ```

> * **param s:**
>   The sampler to which the texture from which texels will be retrieved is bound.
> * **param p:**
>   The texture coordinates at which texture will be sampled.
> * **param comps:**
>   *optional* the component of the source texture (0 -> x, 1 -> y, 2 -> z, 3 -> w) that will be used to generate the resulting vector. Zero if not specified.
> * **return:**
>   The gathered texel.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGather.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGather.xhtml)

---

 **dFdx**( p)

> #### NOTE
> Available only in the fragment shader.

> Returns the partial derivative of `p` with respect to the window x coordinate using local differencing.

> Returns either dFdxCoarse or dFdxFine.
> The implementation may choose which calculation to perform based upon factors
> such as performance or the value of the API `GL_FRAGMENT_SHADER_DERIVATIVE_HINT` hint.

> #### WARNING
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))`
> have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.

> * **param p:**
>   The expression of which to take the partial derivative.

>   #### NOTE
>   It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
> * **return:**
>   The partial derivative of `p`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dFdx.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dFdx.xhtml)

---

 **dFdxCoarse**( p)

> #### NOTE
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.

> Returns the partial derivative of `p` with respect to the window x coordinate.

> Calculates derivatives using local differencing based on the value of `p`
> for the current fragment's neighbors, and will possibly, but not necessarily,
> include the value for the current fragment. That is, over a given area, the
> implementation can compute derivatives in fewer unique locations than would
> be allowed for the corresponding dFdxFine function.

> #### WARNING
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))`
> have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.

> * **param p:**
>   The expression of which to take the partial derivative.

>   #### NOTE
>   It is assumed that the expression `p` is continuous and therefore
>   expressions evaluated via non-uniform control flow may be undefined.
> * **return:**
>   The partial derivative of `p`.

> [https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml](https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml)

---

 **dFdxFine**( p)

> #### NOTE
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.

> Returns the partial derivative of `p` with respect to the window x coordinate.

> Calculates derivatives using local differencing based on the value of `p` for the current fragment and its immediate neighbor(s).

> #### WARNING
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))`
> have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.

> * **param p:**
>   The expression of which to take the partial derivative.

>   #### NOTE
>   It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
> * **return:**
>   The partial derivative of `p`.

> [https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml](https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml)

---

 **dFdy**( p)

> #### NOTE
> Available only in the fragment shader.

> Returns the partial derivative of `p` with respect to the window y coordinate using local differencing.

> Returns either dFdyCoarse or dFdyFine.
> The implementation may choose which calculation to perform based upon factors
> such as performance or the value of the API `GL_FRAGMENT_SHADER_DERIVATIVE_HINT` hint.

> #### WARNING
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))`
> have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.

> * **param p:**
>   The expression of which to take the partial derivative.

>   #### NOTE
>   It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
> * **return:**
>   The partial derivative of `p`.

> [https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml](https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml)

---

 **dFdyCoarse**( p)

> #### NOTE
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.

> Returns the partial derivative of `p` with respect to the window y coordinate.

> Calculates derivatives using local differencing based on the value of `p` for the current fragment's neighbors, and will possibly,
> but not necessarily, include the value for the current fragment. That is, over a given area, the implementation can compute derivatives in fewer unique locations than
> would be allowed for the corresponding dFdyFine and dFdyFine functions.

> #### WARNING
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.

> * **param p:**
>   The expression of which to take the partial derivative.

>   #### NOTE
>   It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
> * **return:**
>   The partial derivative of `p`.

> [https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml](https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml)

---

 **dFdyFine**( p)

> #### NOTE
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.

> Returns the partial derivative of `p` with respect to the window y coordinate.

> Calculates derivatives using local differencing based on the value of `p` for the current fragment and its immediate neighbor(s).

> #### WARNING
> Expressions that imply higher order derivatives such as `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives such as `dFdx(dFdy(n))`.

> * **param p:**
>   The expression of which to take the partial derivative.

>   #### NOTE
>   It is assumed that the expression `p` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.
> * **return:**
>   The partial derivative of `p`.

> [https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml](https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml)

---

 **fwidth**( p)

> Returns the sum of the absolute value of derivatives in x and y.

> Uses local differencing for the input argument `p`.

> Equivalent to `abs(dFdx(p)) + abs(dFdy(p))`.

> * **param p:**
>   The expression of which to take the partial derivative.
> * **return:**
>   The partial derivative.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml)

---

 **fwidthCoarse**( p)

> #### NOTE
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.

> Returns the sum of the absolute value of derivatives in x and y.

> Uses local differencing for the input argument p.

> Equivalent  to `abs(dFdxCoarse(p)) + abs(dFdyCoarse(p))`.

> * **param p:**
>   The expression of which to take the partial derivative.
> * **return:**
>   The partial derivative.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml)

---

 **fwidthFine**( p)

> #### NOTE
> Available only in the fragment shader.
> Not available when using the Compatibility renderer.

> Returns the sum of the absolute value of derivatives in x and y.

> Uses local differencing for the input argument p.

> Equivalent to `abs(dFdxFine(p)) + abs(dFdyFine(p))`.

> * **param p:**
>   The expression of which to take the partial derivative.
> * **return:**
>   The partial derivative.

> [https://registry.khronos.org/OpenGL-Refpages/gl4/html/fwidth.xhtml](https://registry.khronos.org/OpenGL-Refpages/gl4/html/fwidth.xhtml)

---

## Packing and unpacking functions

These functions convert floating-point numbers into various sized integers and
then pack those integers into a single 32bit unsigned integer. The 'unpack'
functions perform the opposite operation, returning the original
floating-point numbers.

| uint<br/><br/><br/>vec2<br/><br/>   | packHalf2x16(vec2 v)<br/><br/><br/>unpackHalf2x16(uint v)<br/><br/>     | Convert two 32-bit floats to 16 bit floats and pack them.                                            |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| uint<br/><br/><br/>vec2<br/><br/>   | packUnorm2x16(vec2 v)<br/><br/><br/>unpackUnorm2x16(uint v)<br/><br/> | Convert two normalized (range 0..1) 32-bit floats<br/>to 16-bit unsigned ints and pack them.         |
| uint<br/><br/><br/>vec2<br/><br/>   | packSnorm2x16(vec2 v)<br/><br/><br/>unpackSnorm2x16(uint v)<br/><br/> | Convert two signed normalized (range -1..1) 32-bit floats<br/>to 16-bit signed ints and pack them.   |
| uint<br/><br/><br/>vec4<br/><br/>   | packUnorm4x8(vec4 v)<br/><br/><br/>unpackUnorm4x8(uint v)<br/><br/>     | Convert four normalized (range 0..1) 32-bit floats<br/>into 8-bit unsigned ints and pack them.       |
| uint<br/><br/><br/>vec4<br/><br/>   | packSnorm4x8(vec4 v)<br/><br/><br/>unpackSnorm4x8(uint v)<br/><br/>     | Convert four signed normalized (range -1..1) 32-bit floats<br/>into 8-bit signed ints and pack them. |

### Packing and unpacking function descriptions

uint **packHalf2x16**(vec2 v)

> Converts two 32-bit floating-point quantities to 16-bit floating-point
> quantities and packs them into a single 32-bit integer.

> Returns an unsigned integer obtained by converting the components of a two-component floating-point vector to
> the 16-bit floating-point representation found in the OpenGL Specification, and then packing these two
> 16-bit integers into a 32-bit unsigned integer. The first vector component specifies the 16 least-significant
> bits of the result; the second component specifies the 16 most-significant bits.

> * **param v:**
>   A vector of two 32-bit floating-point values that are to be converted to 16-bit representation and packed into the result.
> * **return:**
>   The packed value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packHalf2x16.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packHalf2x16.xhtml)

---

vec2 **unpackHalf2x16**(uint v)

> Inverse of packHalf2x16.

> Unpacks a 32-bit integer into two 16-bit floating-point values, converts them to 32-bit floating-point values, and puts them into a vector.
> The first component of the vector is obtained from the 16 least-significant bits of `v`; the second component is obtained from the
> 16 most-significant bits of `v`.

> * **param v:**
>   A single 32-bit unsigned integer containing 2 packed 16-bit floating-point values.
> * **return:**
>   Two unpacked floating-point values.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackHalf2x16.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackHalf2x16.xhtml)

---

uint **packUnorm2x16**(vec2 v)

> Pack floating-point values into an unsigned integer.

> Converts each component of the normalized floating-point value v into 16-bit integer values and then packs the results into a 32-bit unsigned integer.

> The conversion for component c of `v` to fixed-point is performed as follows:

> ```gdscript
> round(clamp(c, 0.0, 1.0) * 65535.0)
> ```

> The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.

> * **param v:**
>   A vector of values to be packed into an unsigned integer.
> * **return:**
>   Unsigned 32 bit integer containing the packed encoding of the vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml)

---

vec2 **unpackUnorm2x16**(uint v)

> Unpack floating-point values from an unsigned integer.

> Unpack single 32-bit unsigned integers into a pair of 16-bit unsigned integers.
> Then, each component is converted to a normalized floating-point value to generate the returned two-component vector.

> The conversion for unpacked fixed point value f to floating-point is performed as follows:

> > f / 65535.0

> The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.

> * **param v:**
>   An unsigned integer containing packed floating-point values.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml)

---

uint **packSnorm2x16**(vec2 v)

> Packs floating-point values into an unsigned integer.

> Convert each component of the normalized floating-point value `v` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.

> The conversion for component c of `v` to fixed-point is performed as follows:

> ```gdscript
> round(clamp(c, -1.0, 1.0) * 32767.0)
> ```

> The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.

> * **param v:**
>   A vector of values to be packed into an unsigned integer.
> * **return:**
>   Unsigned 32 bit integer containing the packed encoding of the vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml)

---

vec2 **unpackSnorm2x16**(uint v)

> Unpacks floating-point values from an unsigned integer.

> Unpacks single 32-bit unsigned integers into a pair of 16-bit signed integers.
> Then, each component is converted to a normalized floating-point value to generate the returned two-component vector.

> The conversion for unpacked fixed point value f to floating-point is performed as follows:

> > clamp(f / 32727.0, -1.0, 1.0)

> The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.

> * **param v:**
>   An unsigned integer containing packed floating-point values.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml)

---

uint **packUnorm4x8**(vec4 v)

> Packs floating-point values into an unsigned integer.

> Converts each component of the normalized floating-point value `v` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.

> The conversion for component c of `v` to fixed-point is performed as follows:

> ```gdscript
> round(clamp(c, 0.0, 1.0) * 255.0)
> ```

> The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.

> * **param v:**
>   A vector of values to be packed into an unsigned integer.
> * **return:**
>   Unsigned 32 bit integer containing the packed encoding of the vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml)

---

vec4 **unpackUnorm4x8**(uint v)

> Unpacks floating-point values from an unsigned integer.

> Unpacks single 32-bit unsigned integers into four 8-bit unsigned integers.
> Then, each component is converted to a normalized floating-point value to generate the returned four-component vector.

> The conversion for unpacked fixed point value f to floating-point is performed as follows:

> > f / 255.0

> The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.

> * **param v:**
>   An unsigned integer containing packed floating-point values.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml)

---

uint **packSnorm4x8**(vec4 v)

> Packs floating-point values into an unsigned integer.

> Convert each component of the normalized floating-point value `v` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.

> The conversion for component c of `v` to fixed-point is performed as follows:

> ```gdscript
> round(clamp(c, -1.0, 1.0) * 127.0)
> ```

> The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.

> * **param v:**
>   A vector of values to be packed into an unsigned integer.
> * **return:**
>   Unsigned 32 bit integer containing the packed encoding of the vector.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml)

---

vec4 **unpackSnorm4x8**(uint v)

> Unpack floating-point values from an unsigned integer.

> Unpack single 32-bit unsigned integers into four 8-bit signed integers.
> Then, each component is converted to a normalized floating-point value to generate the returned four-component vector.

> The conversion for unpacked fixed point value f to floating-point is performed as follows:

> > clamp(f / 127.0, -1.0, 1.0)

> The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.

> * **param v:**
>   An unsigned integer containing packed floating-point values.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml)

---

## Bitwise functions

| <br/><br/><br/>   | bitfieldExtract( value, int offset, int bits)<br/><br/><br/>bitfieldExtract( value, int offset, int bits)<br/><br/>             | Extracts a range of bits from an integer.                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <br/><br/><br/>   | bitfieldInsert( base,  insert, int offset, int bits)<br/><br/><br/>bitfieldInsert( base,  insert, int offset, int bits)<br/><br/> | Insert a range of bits into an integer.                                       |
| <br/><br/><br/>   | bitfieldReverse( value)<br/><br/><br/>bitfieldReverse( value)<br/><br/>                                                         | Reverse the order of bits in an integer.                                      |
| <br/><br/><br/>   | bitCount( value)<br/><br/><br/>bitCount( value)<br/><br/>                                                                                     | Counts the number of 1 bits in an integer.                                    |
| <br/><br/><br/>   | findLSB( value)<br/><br/><br/>findLSB( value)<br/><br/>                                                                                         | Find the index of the least significant bit set to 1 in an integer.           |
| <br/><br/><br/>   | findMSB( value)<br/><br/><br/>findMSB( value)<br/><br/>                                                                                         | Find the index of the most significant bit set to 1 in an integer.            |
| <br/><br/><br/>   | imulExtended( x,  y, out  msb, out  lsb)<br/><br/><br/>umulExtended( x,  y, out  msb, out  lsb)<br/><br/>                             | Multiplies two 32-bit numbers and produce a 64-bit result.                    |
|                   | uaddCarry( x,  y, out  carry)                                                                                                                                         | Adds two unsigned integers and generates carry.                               |
|                   | usubBorrow( x,  y, out  borrow)                                                                                                                                      | Subtracts two unsigned integers and generates borrow.                         |
|                   | ldexp( x, out  exp)                                                                                                                                                       | Assemble a floating-point number from a value and exponent.                   |
|                   | frexp( x, out  exp)                                                                                                                                                       | Splits a floating-point number (`x`) into significand integral<br/>components |

### Bitwise function descriptions

 **bitfieldExtract**( value, int offset, int bits)

> Extracts a subset of the bits of `value` and returns it in the least significant bits of the result.
> The range of bits extracted is `[offset, offset + bits - 1]`.

> The most significant bits of the result will be set to zero.

> #### NOTE
> If bits is zero, the result will be zero.

> #### WARNING
> The result will be undefined if:

> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits used to store the operand.

> * **param value:**
>   The integer from which to extract bits.
> * **param offset:**
>   The index of the first bit to extract.
> * **param bits:**
>   The number of bits to extract.
> * **return:**
>   Integer with the requested bits.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml)

---

 **bitfieldExtract**( value, int offset, int bits)

> Component-wise Function.

> Extracts a subset of the bits of `value` and returns it in the least significant bits of the result.
> The range of bits extracted is `[offset, offset + bits - 1]`.

> The most significant bits will be set to the value of `offset + base - 1` (i.e., it is sign extended to the width of the return type).

> #### NOTE
> If bits is zero, the result will be zero.

> #### WARNING
> The result will be undefined if:

> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits used to store the operand.

> * **param value:**
>   The integer from which to extract bits.
> * **param offset:**
>   The index of the first bit to extract.
> * **param bits:**
>   The number of bits to extract.
> * **return:**
>   Integer with the requested bits.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml)

---

 **bitfieldExtract**( value, int offset, int bits)

 **bitfieldInsert**( base,  insert, int offset, int bits)

> Component-wise Function.

> Inserts the `bits` least significant bits of `insert` into `base` at offset `offset`.

> The returned value will have bits [offset, offset + bits + 1] taken from [0, bits - 1] of `insert` and
> all other bits taken directly from the corresponding bits of base.

> #### NOTE
> If bits is zero, the result will be the original value of base.

> #### WARNING
> The result will be undefined if:

> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits used to store the operand.

> * **param base:**
>   The integer into which to insert `insert`.
> * **param insert:**
>   The value of the bits to insert.
> * **param offset:**
>   The index of the first bit to insert.
> * **param bits:**
>   The number of bits to insert.
> * **return:**
>   `base` with inserted bits.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldInsert.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldInsert.xhtml)

---

 **bitfieldReverse**( value)

 **bitfieldReverse**( value)

> Component-wise Function.

> Reverse the order of bits in an integer.

> The bit numbered `n` will be taken from bit `(bits - 1) - n` of `value`, where bits is the total number of bits used to represent `value`.

> * **param value:**
>   The value whose bits to reverse.
> * **return:**
>   `value` but with its bits reversed.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldReverse.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldReverse.xhtml)

---

 **bitCount**( value)

 **bitCount**( value)

> Component-wise Function.

> Counts the number of 1 bits in an integer.

> * **param value:**
>   The value whose bits to count.
> * **return:**
>   The number of bits that are set to 1 in the binary representation of `value`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitCount.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitCount.xhtml)

---

 **findLSB**( value)

 **findLSB**( value)

> Component-wise Function.

> Find the index of the least significant bit set to `1`.

> #### NOTE
> If `value` is zero, `-1` will be returned.

> * **param value:**
>   The value whose bits to scan.
> * **return:**
>   The bit number of the least significant bit that is set to 1 in the binary representation of value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findLSB.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findLSB.xhtml)

---

 **findMSB**( value)

 **findMSB**( value)

> Component-wise Function.

> Find the index of the most significant bit set to 1.

> #### NOTE
> For signed integer types, the sign bit is checked first and then:
> : - For positive integers, the result will be the bit number of the most significant bit that is set to 1.
>   - For negative integers, the result will be the bit number of the most significant bit set to 0.

> #### NOTE
> For a value of zero or negative 1, -1 will be returned.

> * **param value:**
>   The value whose bits to scan.
> * **return:**
>   The bit number of the most significant bit that is set to 1 in the binary representation of value.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findMSB.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findMSB.xhtml)

---

 **imulExtended**( x,  y, out  msb, out  lsb)

> Component-wise Function.

> Perform 32-bit by 32-bit signed multiplication to produce a 64-bit result.

> The 32 least significant bits of this product are returned in `lsb` and the 32 most significant bits are returned in `msb`.

> * **param x:**
>   The first multiplicand.
> * **param y:**
>   The second multiplicand.
> * **param msb:**
>   The variable to receive the most significant word of the product.
> * **param lsb:**
>   The variable to receive the least significant word of the product.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml)

---

 **umulExtended**( x,  y, out  msb, out  lsb)

> Component-wise Function.

> Perform 32-bit by 32-bit unsigned multiplication to produce a 64-bit result.

> The 32 least significant bits of this product are returned in `lsb` and the 32 most significant bits are returned in `msb`.

> * **param x:**
>   The first multiplicand.
> * **param y:**
>   The second multiplicand.
> * **param msb:**
>   The variable to receive the most significant word of the product.
> * **param lsb:**
>   The variable to receive the least significant word of the product.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml)

---

 **uaddCarry**( x,  y, out  carry)

> Component-wise Function.

> Add unsigned integers and generate carry.

> adds two 32-bit unsigned integer variables (scalars or vectors) and generates a 32-bit unsigned integer result, along with a carry output.
> The value carry is .

> * **param x:**
>   The first operand.
> * **param y:**
>   The second operand.
> * **param carry:**
>   0 if the sum is less than 2<sub>32</sub>, otherwise 1.
> * **return:**
>   `(x + y) % 2^32`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/uaddCarry.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/uaddCarry.xhtml)

---

 **usubBorrow**( x,  y, out  borrow)

> Component-wise Function.

> Subtract unsigned integers and generate borrow.

> * **param x:**
>   The first operand.
> * **param y:**
>   The second operand.
> * **param borrow:**
>   `0` if `x >= y`, otherwise `1`.
> * **return:**
>   The difference of `x` and `y` if non-negative, or 2<sub>32</sub> plus that difference otherwise.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/usubBorrow.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/usubBorrow.xhtml)

---

 **ldexp**( x, out  exp)

> Component-wise Function.

> Assembles a floating-point number from a value and exponent.

> #### WARNING
> If this product is too large to be represented in the floating-point
> type, the result is undefined.

> * **param x:**
>   The value to be used as a source of significand.
> * **param exp:**
>   The value to be used as a source of exponent.
> * **return:**
>   `x * 2^exp`

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ldexp.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ldexp.xhtml)

---

 **frexp**( x, out  exp)

> Component-wise Function.

> Extracts `x` into a floating-point significand in the range `[0.5, 1.0)` and in integral exponent of two, such that:

> ```gdscript
> x = significand * 2 ^ exponent
> ```

> For a floating-point value of zero, the significand and exponent are both zero.

> #### WARNING
> For a floating-point value that is an infinity or a floating-point NaN, the results are undefined.

> * **param x:**
>   The value from which significand and exponent are to be extracted.
> * **param exp:**
>   The variable into which to place the exponent of `x`.
> * **return:**
>   The significand of `x`.

> [https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/frexp.xhtml](https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/frexp.xhtml)

---
