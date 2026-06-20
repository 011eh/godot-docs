# OpenXRCompositionLayerCylinder

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRCompositionLayer](class_openxrcompositionlayer.md#class-openxrcompositionlayer) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

An OpenXR composition layer that is rendered as an internal slice of a cylinder.

## Description

An OpenXR composition layer that allows rendering a [SubViewport](class_subviewport.md#class-subviewport) on an internal slice of a cylinder.

## Properties

| [float](class_float.md#class-float)   | aspect_ratio           | `1.0`       |
|---------------------------------------|---------------------------------------------------------------------------------------|-------------|
| [float](class_float.md#class-float)   | central_angle         | `1.5707964` |
| [int](class_int.md#class-int)         | fallback_segments | `10`        |
| [float](class_float.md#class-float)   | radius                       | `1.0`       |

---

## Property Descriptions

[float](class_float.md#class-float) **aspect_ratio** = `1.0`

-  **set_aspect_ratio**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_aspect_ratio**()

The aspect ratio of the slice. Used to set the height relative to the width.

---

[float](class_float.md#class-float) **central_angle** = `1.5707964`

-  **set_central_angle**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_central_angle**()

The central angle of the cylinder. Used to set the width.

---

[int](class_int.md#class-int) **fallback_segments** = `10`

-  **set_fallback_segments**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_fallback_segments**()

The number of segments to use in the fallback mesh.

---

[float](class_float.md#class-float) **radius** = `1.0`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The radius of the cylinder.
