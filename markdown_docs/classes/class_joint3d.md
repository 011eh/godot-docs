# Joint3D

**Inherits:** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [ConeTwistJoint3D](class_conetwistjoint3d.md#class-conetwistjoint3d), [Generic6DOFJoint3D](class_generic6dofjoint3d.md#class-generic6dofjoint3d), [HingeJoint3D](class_hingejoint3d.md#class-hingejoint3d), [PinJoint3D](class_pinjoint3d.md#class-pinjoint3d), [SliderJoint3D](class_sliderjoint3d.md#class-sliderjoint3d)

Abstract base class for all 3D physics joints.

## Description

Abstract base class for all joints in 3D physics. 3D joints bind together two physics bodies (node_a and node_b) and apply a constraint. If only one body is defined, it is attached to a fixed [StaticBody3D](class_staticbody3d.md#class-staticbody3d) without collision shapes.

## Tutorials

- [3D Truck Town Demo](https://godotengine.org/asset-library/asset/2752)

## Properties

| [bool](class_bool.md#class-bool)             | exclude_nodes_from_collision   | `true`         |
|----------------------------------------------|----------------------------------------------------------------------------------------|----------------|
| [NodePath](class_nodepath.md#class-nodepath) | node_a                                               | `NodePath("")` |
| [NodePath](class_nodepath.md#class-nodepath) | node_b                                               | `NodePath("")` |
| [int](class_int.md#class-int)                | solver_priority                             | `1`            |

## Methods

| [RID](class_rid.md#class-rid)   | get_rid()    |
|---------------------------------|-----------------------------------------------|

---

## Property Descriptions

[bool](class_bool.md#class-bool) **exclude_nodes_from_collision** = `true`

-  **set_exclude_nodes_from_collision**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_exclude_nodes_from_collision**()

If `true`, the two bodies bound together do not collide with each other.

---

[NodePath](class_nodepath.md#class-nodepath) **node_a** = `NodePath("")`

-  **set_node_a**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_node_a**()

Path to the first node (A) attached to the joint. The node must inherit [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d).

If left empty and node_b is set, the body is attached to a fixed [StaticBody3D](class_staticbody3d.md#class-staticbody3d) without collision shapes.

---

[NodePath](class_nodepath.md#class-nodepath) **node_b** = `NodePath("")`

-  **set_node_b**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_node_b**()

Path to the second node (B) attached to the joint. The node must inherit [PhysicsBody3D](class_physicsbody3d.md#class-physicsbody3d).

If left empty and node_a is set, the body is attached to a fixed [StaticBody3D](class_staticbody3d.md#class-staticbody3d) without collision shapes.

---

[int](class_int.md#class-int) **solver_priority** = `1`

-  **set_solver_priority**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_solver_priority**()

The priority used to define which solver is executed first for multiple joints. The lower the value, the higher the priority.

**Note:** Only supported when using GodotPhysics3D. This property is ignored when using Jolt Physics.

---

## Method Descriptions

[RID](class_rid.md#class-rid) **get_rid**()

Returns the joint's internal [RID](class_rid.md#class-rid) from the [PhysicsServer3D](class_physicsserver3d.md#class-physicsserver3d).
