# PhysicalBone2D

**Inherits:** [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d) **<** [PhysicsBody2D](class_physicsbody2d.md#class-physicsbody2d) **<** [CollisionObject2D](class_collisionobject2d.md#class-collisionobject2d) **<** [Node2D](class_node2d.md#class-node2d) **<** [CanvasItem](class_canvasitem.md#class-canvasitem) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

A [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d)-derived node used to make [Bone2D](class_bone2d.md#class-bone2d)s in a [Skeleton2D](class_skeleton2d.md#class-skeleton2d) react to physics.

## Description

The **PhysicalBone2D** node is a [RigidBody2D](class_rigidbody2d.md#class-rigidbody2d)-based node that can be used to make [Bone2D](class_bone2d.md#class-bone2d)s in a [Skeleton2D](class_skeleton2d.md#class-skeleton2d) react to physics.

**Note:** To make the [Bone2D](class_bone2d.md#class-bone2d)s visually follow the **PhysicalBone2D** node, use a [SkeletonModification2DPhysicalBones](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones) modification on the [Skeleton2D](class_skeleton2d.md#class-skeleton2d) parent.

**Note:** The **PhysicalBone2D** node does not automatically create a [Joint2D](class_joint2d.md#class-joint2d) node to keep **PhysicalBone2D** nodes together. They must be created manually. For most cases, you want to use a [PinJoint2D](class_pinjoint2d.md#class-pinjoint2d) node. The **PhysicalBone2D** node will automatically configure the [Joint2D](class_joint2d.md#class-joint2d) node once it's been added as a child node.

## Properties

| [bool](class_bool.md#class-bool)             | auto_configure_joint               | `true`         |
|----------------------------------------------|-------------------------------------------------------------------------------------------|----------------|
| [int](class_int.md#class-int)                | bone2d_index                               | `-1`           |
| [NodePath](class_nodepath.md#class-nodepath) | bone2d_nodepath                         | `NodePath("")` |
| [bool](class_bool.md#class-bool)             | follow_bone_when_simulating | `false`        |
| [bool](class_bool.md#class-bool)             | simulate_physics                       | `false`        |

## Methods

| [Joint2D](class_joint2d.md#class-joint2d)   | get_joint()                         |
|---------------------------------------------|-------------------------------------------------------------------------------|
| [bool](class_bool.md#class-bool)            | is_simulating_physics() |

---

## Property Descriptions

[bool](class_bool.md#class-bool) **auto_configure_joint** = `true`

-  **set_auto_configure_joint**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_auto_configure_joint**()

If `true`, the **PhysicalBone2D** will automatically configure the first [Joint2D](class_joint2d.md#class-joint2d) child node. The automatic configuration is limited to setting up the node properties and positioning the [Joint2D](class_joint2d.md#class-joint2d).

---

[int](class_int.md#class-int) **bone2d_index** = `-1`

-  **set_bone2d_index**(value: [int](class_int.md#class-int))
- [int](class_int.md#class-int) **get_bone2d_index**()

The index of the [Bone2D](class_bone2d.md#class-bone2d) that this **PhysicalBone2D** should simulate.

---

[NodePath](class_nodepath.md#class-nodepath) **bone2d_nodepath** = `NodePath("")`

-  **set_bone2d_nodepath**(value: [NodePath](class_nodepath.md#class-nodepath))
- [NodePath](class_nodepath.md#class-nodepath) **get_bone2d_nodepath**()

The [NodePath](class_nodepath.md#class-nodepath) to the [Bone2D](class_bone2d.md#class-bone2d) that this **PhysicalBone2D** should simulate.

---

[bool](class_bool.md#class-bool) **follow_bone_when_simulating** = `false`

-  **set_follow_bone_when_simulating**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_follow_bone_when_simulating**()

If `true`, the **PhysicalBone2D** will keep the transform of the bone it is bound to when simulating physics.

---

[bool](class_bool.md#class-bool) **simulate_physics** = `false`

-  **set_simulate_physics**(value: [bool](class_bool.md#class-bool))
- [bool](class_bool.md#class-bool) **get_simulate_physics**()

If `true`, the **PhysicalBone2D** will start simulating using physics. If `false`, the **PhysicalBone2D** will follow the transform of the [Bone2D](class_bone2d.md#class-bone2d) node.

**Note:** To have the [Bone2D](class_bone2d.md#class-bone2d)s visually follow the **PhysicalBone2D**, use a [SkeletonModification2DPhysicalBones](class_skeletonmodification2dphysicalbones.md#class-skeletonmodification2dphysicalbones) modification on the [Skeleton2D](class_skeleton2d.md#class-skeleton2d) node with the [Bone2D](class_bone2d.md#class-bone2d) nodes.

---

## Method Descriptions

[Joint2D](class_joint2d.md#class-joint2d) **get_joint**()

Returns the first [Joint2D](class_joint2d.md#class-joint2d) child node, if one exists. This is mainly a helper function to make it easier to get the [Joint2D](class_joint2d.md#class-joint2d) that the **PhysicalBone2D** is autoconfiguring.

---

[bool](class_bool.md#class-bool) **is_simulating_physics**()

Returns a boolean that indicates whether the **PhysicalBone2D** is running and simulating using the Godot 2D physics engine. When `true`, the PhysicalBone2D node is using physics.
