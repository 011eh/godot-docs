# CSGTorus3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class-csgprimitive3d) **<** [CSGShape3D](class_csgshape3d.md#class-csgshape3d) **<** [GeometryInstance3D](class_geometryinstance3d.md#class-geometryinstance3d) **<** [VisualInstance3D](class_visualinstance3d.md#class-visualinstance3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A CSG Torus shape.

## Description

This node allows you to create a torus for use with the CSG system.

**Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class-meshinstance3d) with a [PrimitiveMesh](class_primitivemesh.md#class-primitivemesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

## Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

## Properties

| [float](class_float.md#class-float)          | inner_radius   | `0.5`   |
|----------------------------------------------|-----------------------------------------------------------|---------|
| [Material](class_material.md#class-material) | material           |         |
| [float](class_float.md#class-float)          | outer_radius   | `1.0`   |
| [int](class_int.md#class-int)                | ring_sides       | `6`     |
| [int](class_int.md#class-int)                | sides                 | `8`     |
| [bool](class_bool.md#class-bool)             | smooth_faces   | `true`  |

---

## Property Descriptions

[float](class_float.md#class-float) **inner_radius** = `0.5`

-  **set_inner_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_inner_radius**()

The inner radius of the torus.

---

[Material](class_material.md#class-material) **material**

-  **set_material**(value: [Material](class_material.md#class-material))
- [Material](class_material.md#class-material) **get_material**()

The material used to render the torus.

---

[float](class_float.md#class-float) **outer_radius** = `1.0`

-  **set_outer_radius**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_outer_radius**()

The outer radius of the torus.

---

[int](class_int.md#class-int) **ring_sides** = `6`

-  **set_ring_sides**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_ring_sides**()

The number of edges each ring of the torus is constructed of.

---

[int](class_int.md#class-int) **sides** = `8`

-  **set_sides**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_sides**()

The number of slices the torus is constructed of.

---

[bool](class_bool.md#class-bool) **smooth_faces** = `true`

-  **set_smooth_faces**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_smooth_faces**()

If `true` the normals of the torus are set to give a smooth effect making the torus seem rounded. If `false` the torus will have a flat shaded look.
