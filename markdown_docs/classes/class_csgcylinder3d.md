# CSGCylinder3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class-csgprimitive3d) **<** [CSGShape3D](class_csgshape3d.md#class-csgshape3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A CSG Cylinder shape.

## Description

This node allows you to create a cylinder (or cone) for use with the CSG system.

**Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) with a [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

## Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

## Properties

| [bool](class_bool.md#class-bool)             | cone                 | `false`   |
|----------------------------------------------|------------------------------------------------------------|-----------|
| [float](class_float.md#class-float)          | height             | `2.0`     |
| [Material](class_material.md#class-material) | material         |           |
| [float](class_float.md#class-float)          | radius             | `0.5`     |
| [int](class_int.md#class-int)                | sides               | `8`       |
| [bool](class_bool.md#class-bool)             | smooth_faces | `true`    |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **cone** = `false`

-  **set_cone**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **is_cone**()

If `true` a cone is created, the radius will only apply to one side.

---

[float](class_float.md#class-float) **height** = `2.0`

-  **set_height**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_height**()

The height of the cylinder.

---

[Material](class_material.md#class-material) **material**

-  **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

The material used to render the cylinder.

---

[float](class_float.md#class-float) **radius** = `0.5`

-  **set_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_radius**()

The radius of the cylinder.

---

[int](class_int.md#class-int) **sides** = `8`

-  **set_sides**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sides**()

The number of sides of the cylinder, the higher this number the more detail there will be in the cylinder.

---

[bool](class_bool.md#class-bool) **smooth_faces** = `true`

-  **set_smooth_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_smooth_faces**()

If `true` the normals of the cylinder are set to give a smooth effect making the cylinder seem rounded. If `false` the cylinder will have a flat shaded look.
