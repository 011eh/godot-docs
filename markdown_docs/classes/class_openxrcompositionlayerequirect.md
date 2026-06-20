# OpenXRCompositionLayerEquirect

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class-openxrcompositionlayer) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

An OpenXR composition layer that is rendered as an internal slice of a sphere.

## Description

An OpenXR composition layer that allows rendering a [SubViewport](class_subviewport.md#class-subviewport) on an internal slice of a sphere.

## Properties

| [float](class_float.md#class-float)   | central_horizontal_angle   | `1.5707964`   |
|---------------------------------------|-------------------------------------------------------------------------------------------------------|---------------|
| [int](class_int.md#class-int)         | fallback_segments                 | `10`          |
| [float](class_float.md#class-float)   | lower_vertical_angle           | `0.7853982`   |
| [float](class_float.md#class-float)   | radius                                       | `1.0`         |
| [float](class_float.md#class-float)   | upper_vertical_angle           | `0.7853982`   |

---

## Property Descriptions

[float](class_float.md#class-float) **central_horizontal_angle** = `1.5707964`

-  **set_central_horizontal_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_central_horizontal_angle**()

The central horizontal angle of the sphere. Used to set the width.

---

[int](class_int.md#class-int) **fallback_segments** = `10`

-  **set_fallback_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fallback_segments**()

The number of segments to use in the fallback mesh.

---

[float](class_float.md#class-float) **lower_vertical_angle** = `0.7853982`

-  **set_lower_vertical_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_lower_vertical_angle**()

The lower vertical angle of the sphere. Used (together with upper_vertical_angle) to set the height.

---

[float](class_float.md#class-float) **radius** = `1.0`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The radius of the sphere.

---

[float](class_float.md#class-float) **upper_vertical_angle** = `0.7853982`

-  **set_upper_vertical_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_upper_vertical_angle**()

The upper vertical angle of the sphere. Used (together with lower_vertical_angle) to set the height.
