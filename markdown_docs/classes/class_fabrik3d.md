# FABRIK3D

**Inherits:** [IterateIK3D](class_iterateik3d.md#class-iterateik3d) **<** [ChainIK3D](class_chainik3d.md#class-chainik3d) **<** [IKModifier3D](class_ikmodifier3d.md#class-ikmodifier3d) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Position based forward and backward reaching inverse kinematics solver.

## Description

**FABRIK3D** is position based IK, allowing precise and accurate tracking of targets. It's ideal for simple chains without limitations.

The resulting twist around the forward vector will always be kept from the previous pose.

**Note:** When the target is close to the root, it tends to produce zig-zag patterns, resulting in unnatural visual movement.

## Tutorials

- [Inverse Kinematics Returns to Godot 4.6 - IKModifier3D](https://godotengine.org/article/inverse-kinematics-returns-to-godot-4-6/#ikmodifier3d-and-7-child-classes)
