# Joint2D

**Inherits:** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

**Inherited By:** [DampedSpringJoint2D](class_dampedspringjoint2d.md#class-dampedspringjoint2d), [GrooveJoint2D](class_groovejoint2d.md#class-groovejoint2d), [PinJoint2D](class_pinjoint2d.md#class-pinjoint2d)

Abstract base class for all 2D physics joints.

## Description

Abstract base class for all joints in 2D physics. 2D joints bind together two physics bodies (node_a and node_b) and apply a constraint.

## Properties

| [float](class_float.md#class-float)          | bias                           | `0.0`          |
|----------------------------------------------|----------------------------------------------------------------|----------------|
| [bool](class_bool.md#class-bool)             | disable_collision | `true`         |
| [NodePath](class_nodepath.md#class-nodepath) | node_a                       | `NodePath("")` |
| [NodePath](class_nodepath.md#class-nodepath) | node_b                       | `NodePath("")` |

## Methods

| [RID](class_rid.md#class-rid)   | get_rid()    |
|---------------------------------|-----------------------------------------------|

---

## Property Descriptions

[float](class_float.md#class-float) **bias** = `0.0`

-  **set_bias**(value: [float](class_float.md#class-float))
- [float](class_float.md#class-float) **get_bias**()

When node_a and node_b move in different directions the bias controls how fast the joint pulls them back to their original position. The lower the bias the more the two bodies can pull on the joint.

When set to `0`, the default value from [ProjectSettings.physics/2d/solver/default_constraint_bias](class_projectsettings.md#class-projectsettings-property-physics-2d-solver-default-constraint-bias) is used.

---

[bool](class_bool.md#class-bool) **disable_collision** = `true`

-  **set_exclude_nodes_from_collision**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_exclude_nodes_from_collision**()

If `true`, the two bodies bound together do not collide with each other.

---

[NodePath](class_nodepath.md#class-nodepath) **node_a** = `NodePath("")`

-  **set_node_a**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_node_a**()

Path to the first body (A) attached to the joint. The node must inherit [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d).

---

[NodePath](class_nodepath.md#class-nodepath) **node_b** = `NodePath("")`

-  **set_node_b**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_node_b**()

Path to the second body (B) attached to the joint. The node must inherit [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d).

---

## Method Descriptions

[RID](class_rid.md#class-rid) **get_rid**()

Returns the joint's internal [RID](class_rid.md#class-rid) from the [PhysicsServer2D](class_physicsserver2d.md#class-physicsserver2d).
