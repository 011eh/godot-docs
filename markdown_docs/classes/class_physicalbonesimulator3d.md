# PhysicalBoneSimulator3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class-skeletonmodifier3d) **<** [Node3D](class_node3d.md#class-node3d) **<** [Node](class_node.md#class-node) **<** [Object](class_object.md#class-object)

Node that can be the parent of [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) and can apply the simulation results to [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

## Description

Node that can be the parent of [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) and can apply the simulation results to [Skeleton3D](class_skeleton3d.md#class-skeleton3d).

## Methods

| [bool](class_bool.md#class-bool)   | is_simulating_physics()                                                                                                                        |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                    | physical_bones_add_collision_exception(exception: [RID](class_rid.md#class-rid))                                              |
|                                    | physical_bones_remove_collision_exception(exception: [RID](class_rid.md#class-rid))                                        |
|                                    | physical_bones_start_simulation(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = []) |
|                                    | physical_bones_stop_simulation()                                                                                                      |

---

## Method Descriptions

[bool](class_bool.md#class-bool) **is_simulating_physics**()

Returns a boolean that indicates whether the **PhysicalBoneSimulator3D** is running and simulating.

---

 **physical_bones_add_collision_exception**(exception: [RID](class_rid.md#class-rid))

Adds a collision exception to the physical bone.

Works just like the [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) node.

---

 **physical_bones_remove_collision_exception**(exception: [RID](class_rid.md#class-rid))

Removes a collision exception to the physical bone.

Works just like the [RigidBody3D](class_rigidbody3d.md#class-rigidbody3d) node.

---

 **physical_bones_start_simulation**(bones: [Array](class_array.md#class-array)[[StringName](class_stringname.md#class-stringname)] = [])

Tells the [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) nodes in the Skeleton to start simulating and reacting to the physics world.

Optionally, a list of bone names can be passed-in, allowing only the passed-in bones to be simulated.

---

 **physical_bones_stop_simulation**()

Tells the [PhysicalBone3D](class_physicalbone3d.md#class-physicalbone3d) nodes in the Skeleton to stop simulating.
